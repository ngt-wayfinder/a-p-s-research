import csv, hashlib, io, re, time, zipfile
from datetime import datetime, timezone
from pathlib import Path
import requests
from pypdf import PdfReader

CODES = ['ACW', 'ACE', 'BHP', 'CSL', 'WDS']
BASE = 'https://asx.api.cmfyapp.com/asx-research/1.0'
ROOT = Path('/content/asx_batch_v2')
ROOT.mkdir(parents=True, exist_ok=True)
PAGE_SIZE, MAX_PAGES, DELAY = 25, 100, 0.7
NOW = datetime.now(timezone.utc)
S = requests.Session()
S.headers.update({'User-Agent': 'Mozilla/5.0', 'Accept': '*/*'})

BAD_TITLE = re.compile(r'presentation|transcript|webcast|briefing|webinar|slides|conference call|notice of meeting|corporate governance|results and outlook|investor update|highlights|trading update|results announcement|results release|summary of results|media release', re.I)
RULES = {
 'ANNUAL': [
  (re.compile(r'appendix\s*4e\b', re.I), 120),
  (re.compile(r'\bannual (financial )?report\b|\bfinancial report\b.*\b(year ended|full year|fy\s*20\d\d)\b', re.I), 95),
  (re.compile(r'\bfull[ -]?year financial statements\b|\bannual financial statements\b', re.I), 100),
  (re.compile(r'\bform\s*20-f\b', re.I), 30),
 ],
 'HALF_YEAR': [
  (re.compile(r'appendix\s*4d\b', re.I), 120),
  (re.compile(r'half[ -]?year(ly)? (financial )?(report|accounts|financial statements)\b|half[ -]?year financial report', re.I), 105),
  (re.compile(r'interim (financial )?(report|financial statements|accounts)\b', re.I), 95),
 ],
 'QUARTERLY': [
  (re.compile(r'appendix\s*[45][cb]\b', re.I), 110),
  (re.compile(r'quarterly (activities|activity|cash[ -]?flow) report\b', re.I), 95),
 ]
}
FINANCIAL_TERMS = [
 re.compile(r'statement[s]? of (financial position|profit or loss|cash flows|comprehensive income)', re.I),
 re.compile(r'consolidated (balance sheet|statement[s]? of|income statement|cash flow)', re.I),
 re.compile(r'notes to (the )?(consolidated )?financial statements', re.I),
 re.compile(r'independent auditor.s report|independent review report', re.I),
]

def fetch(url, **kw):
 for attempt in range(3):
  try:
   r=S.get(url, timeout=90, **kw)
   r.raise_for_status()
   return r
  except requests.RequestException:
   if attempt == 2: raise
   time.sleep(2**attempt + 1)

def resolve(code):
 items=fetch(f'{BASE}/search/predictive',params={'searchText':code,'useBondsLookup':'true'}).json().get('data',{}).get('items',[])
 hits=[x for x in items if str(x.get('symbol','')).upper()==code and x.get('xidEntity') is not None]
 ids={str(x['xidEntity']) for x in hits}
 if len(ids)!=1: raise ValueError(f'Expected one exact entity ID, got {ids}')
 return ids.pop(),hits[0].get('displayName','')

def discover(xid):
 rows=[]; seen=set(); total=None
 for page in range(MAX_PAGES):
  data=fetch(f'{BASE}/markets/announcements',params={'entityXids':xid,'page':page,'itemsPerPage':PAGE_SIZE,'summaryCountsDate':NOW.date().isoformat()}).json().get('data',{})
  items=data.get('items',[]); total=data.get('count',total)
  if not isinstance(items,list):raise ValueError('Malformed items')
  for x in items:
   k=x.get('documentKey')
   if k and k not in seen:rows.append(x);seen.add(k)
  if not items or len(items)<PAGE_SIZE or (isinstance(total,int) and len(rows)>=total):break
  time.sleep(DELAY)
 return rows,total,isinstance(total,int) and len(rows)>=total

def candidates(items,category):
 result=[]
 for item in items:
  title=str(item.get('headline',''))
  if not item.get('documentKey'):continue
  if BAD_TITLE.search(title):continue
  scores=[score for regex,score in RULES[category] if regex.search(title)]
  if not scores:continue
  score=max(scores)
  if category=='ANNUAL' and re.search(r'form\s*20-f',title,re.I):score-=15
  result.append((item,score))
 # Restrict to the most recent plausible reporting cycle before preferring title quality.
 result.sort(key=lambda x:(x[0].get('date',''),x[1]),reverse=True)
 return result

def pdf_check(content,category):
 if not content.startswith(b'%PDF-'):return False,'Invalid PDF signature',0
 try:
  reader=PdfReader(io.BytesIO(content),strict=False)
  pages=len(reader.pages)
  if pages<1:return False,'Empty PDF',0
  indexes=list(dict.fromkeys([0,1,2,3,4,5,6,7,8,9, min(15,pages-1), min(25,pages-1),min(40,pages-1), pages-1]))
  text='\n'.join(reader.pages[i].extract_text() or '' for i in indexes if i<pages)
  if len(text.strip())<100:return False,'Insufficient extractable text; manual review required',pages
  if category=='QUARTERLY':
   ok=bool(re.search(r'appendix\s*[45][cb]\b|quarterly cash flow|quarterly activities|cash flows from operating activities',text,re.I))
   return ok, 'Quarterly content markers' if ok else 'No quarterly markers in sampled pages',pages
  hits=sum(bool(p.search(text)) for p in FINANCIAL_TERMS)
  # Appendix 4D/E reports can include financial statements in annexes.
  ok=hits>=2
  return ok,f'{hits} financial-statement markers in sampled pages',pages
 except Exception as e:return False,f'PDF parsing failed: {type(e).__name__}: {e}',0

def age_status(iso,category):
 try: age=(NOW-datetime.fromisoformat(iso.replace('Z','+00:00'))).days
 except Exception:return 'DATE_UNKNOWN'
 limit={'ANNUAL':520,'HALF_YEAR':340,'QUARTERLY':220}[category]
 return 'STALE' if age>limit else 'CURRENT_WINDOW'

results=[]; audit=[]; summaries=[]
for code in CODES:
 print('\n'+'='*65+'\n',code)
 xid='';name='';items=[];total=None;complete=False;fatal=''
 try:
  xid,name=resolve(code);items,total,complete=discover(xid)
  print('Company:',name,'| entity:',xid,'| announcements:',len(items),'/',total,'| complete:',complete)
  if not complete:raise ValueError('Announcement pagination incomplete; report selection withheld')
  if not items:raise ValueError('No announcements')
 except Exception as e:fatal=f'{type(e).__name__}: {e}';print('DISCOVERY ERROR:',fatal)
 successes=0
 for category in RULES:
  row=dict(ASX_Code=code,Company=name,Entity_XID=xid,Report_Type=category,Announcement_Date='',Headline='',Document_Key='',Local_Path='',Bytes='',SHA256='',Pages='',Status='',Reason='',Announcements_Found=len(items),Announcements_Total=total,Discovery_Complete=complete)
  if fatal:row.update(Status='DISCOVERY_FAILED',Reason=fatal)
  else:
   found=candidates(items,category)
   if not found:row.update(Status='NOT_FOUND_REVIEW_REQUIRED',Reason='No matching report title; reporting obligations not assessed')
   else:
    # Examine candidates newest first, with a capped number of PDF fetches.
    for item,score in found[:12]:
     key=item['documentKey']; title=item.get('headline',''); date=item.get('date','')
     auditrow=dict(ASX_Code=code,Report_Type=category,Date=date,Headline=title,Document_Key=key,Title_Score=score,Decision='',Reason='')
     try:
      content=fetch(f'{BASE}/file/{key}').content
      valid,reason,pages=pdf_check(content,category)
      age=age_status(date,category)
      if not valid:
       auditrow.update(Decision='REJECTED',Reason=reason)
      elif age=='STALE':
       auditrow.update(Decision='STALE',Reason=f'{reason}; publication outside recency window')
      else:
       out=ROOT/code;out.mkdir(parents=True,exist_ok=True)
       path=out/f'{code}_{category}_{key}.pdf';path.write_bytes(content)
       row.update(Announcement_Date=date,Headline=title,Document_Key=key,Local_Path=str(path),Bytes=len(content),SHA256=hashlib.sha256(content).hexdigest(),Pages=pages,Status='SUCCESS',Reason=reason)
       auditrow.update(Decision='SELECTED',Reason=reason)
       successes+=1
     except Exception as e:
      auditrow.update(Decision='ERROR',Reason=f'{type(e).__name__}: {e}')
     audit.append(auditrow)
     if auditrow['Decision']=='SELECTED':break
     time.sleep(DELAY)
    if not row['Status']:
     row.update(Status='REVIEW_REQUIRED',Reason='No candidate passed PDF-content and recency checks; see candidate audit')
  results.append(row)
  print(category,':',row['Status'],'|',row['Headline'][:100], '|',row['Reason'])
 summaries.append((code,successes,len(items),complete))

for name,rows in [('batch_v2_register.csv',results),('batch_v2_candidate_audit.csv',audit)]:
 path=ROOT/name
 if rows:
  with path.open('w',newline='',encoding='utf-8') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

archive=Path('/content/asx_batch_v2.zip')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for path in ROOT.rglob('*'):
  if path.is_file():z.write(path,path.relative_to(ROOT.parent))
print('\n'+'='*65+'\nBATCH V2 SUMMARY')
for code,n,count,complete in summaries:print(f'{code:4} | accepted PDFs {n}/3 | announcements {count} | complete {complete}')
print('ACCEPTED:',sum(r['Status']=='SUCCESS' for r in results),'/',len(results))
print('REVIEW:',sum(r['Status']!='SUCCESS' for r in results))
print('AUDIT:',ROOT/'batch_v2_candidate_audit.csv')
print('ZIP:',archive)
try:
 from google.colab import files
 files.download(str(archive))
except ImportError:pass
