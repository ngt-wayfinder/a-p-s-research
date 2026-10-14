"""Parse official ASX year tabs, reject lost rows and future effective dates."""
import csv,json,re,datetime,collections,pathlib,hashlib,argparse
from lxml import html
SOURCE='https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes'
parser=argparse.ArgumentParser()
parser.add_argument('--html',required=True)
parser.add_argument('--matrix',default='research/STEP_1_3_2_EVIDENCE_MATRIX.csv')
parser.add_argument('--output-dir',default='research')
parser.add_argument('--cutoff',default='2026-10-13')
args=parser.parse_args();out=pathlib.Path(args.output_dir);out.mkdir(parents=True,exist_ok=True)
cutoff=datetime.date.fromisoformat(args.cutoff)
raw=pathlib.Path(args.html).read_bytes()
s=html.fromstring(raw);codes={x['ASX_Code'] for x in csv.DictReader(open(args.matrix))}
allrows=[];counts={};errors=[]
for tab in s.xpath('//table'):
 parent=tab.xpath('ancestor::*[@role="tabpanel"]')[0]
 year=list(json.loads(parent.get('data-cmp-data-layer')).values())[0]['dc:title']
 counts[year]=0
 for row in tab.xpath('.//tr'):
  cells=[' '.join(x.text_content().split()) for x in row.xpath('./td')]
  if not cells: continue
  counts[year]+=1
  if len(cells)<5 or any(cells[5:]): errors.append({'year':year,'cells':cells});continue
  day,month=re.fullmatch(r'(\d{1,2})[\s-]*([A-Za-z]+)',cells[0]).groups()
  date=datetime.datetime.strptime(f'{day}-{month[:3]}-{year}','%d-%b-%Y').date()
  old,oldname,new,newname=cells[1:5]
  allrows.append({'year':year,'source_date_text':cells[0],'effective_date':str(date),'old_code':old,'old_name':oldname,'new_code':new,'new_name':newname,'matched_codes':' | '.join(sorted(codes&{old,new})),'event_type':'NAME_ONLY' if old==new else 'CODE_CHANGE_REQUIRES_IDENTIFIER_BRIDGE','source_url':SOURCE,'source_section':f'{year} annual table','after_cutoff':date>cutoff})
assert not errors, errors
assert set(counts)==set(map(str,range(2018,2027)))
assert len(allrows)==sum(counts.values())
matches=[r for r in allrows if r['matched_codes'] and not r['after_cutoff']]
for name,rows in [('asx_code_changes_population',matches),('asx_code_changes_all',allrows)]:
 (out/f'{name}.json').write_text(json.dumps(rows,indent=2))
 with open(out/f'{name}.csv','w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
qa={'source_url':SOURCE,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(raw).hexdigest(),'year_counts':counts,'source_rows':len(allrows),'matched_event_rows':len(matches),'matched_codes':len({c for r in matches for c in r['matched_codes'].split(' | ')}),'matched_code_changes':sum(r['event_type'].startswith('CODE_CHANGE') for r in matches),'matched_name_only':sum(r['event_type']=='NAME_ONLY' for r in matches),'future_rows_excluded':sum(r['after_cutoff'] for r in allrows),'parse_errors':errors,'cutoff':args.cutoff,'limitations':'Official register is an event list, not an exhaustive issuer legal/capital history. Old-code collision rows require separate issuer mapping.'}
(out/'asx_code_changes_qa.json').write_text(json.dumps(qa,indent=2));print(json.dumps(qa,indent=2))
