#!/usr/bin/env python3
"""BHP-only interactive ASX report collection research, Version 3.

Run in Google Colab after confirming authorised access to the source.
Never bypass 403/429. No unattended collection, no eligibility decisions.
The full Version 2 baseline remains unchanged in GitHub.
"""
import csv
import hashlib
import json
import os
import re
import sys
import time
import uuid


def log(message):
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] {message}", flush=True)
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import requests

# Load the standalone offline validator from the same repository checkout.
from issuer_pdf_validation import validate_pdf, TITLE_RULES

CODES = ["BHP"]
TRANCHE_SIZE = 10
COMPANY_DELAY_SECONDS = 15
TRANCHE_DELAY_SECONDS = 15 * 60
REQUEST_DELAY_SECONDS = 1.5
PAGE_SIZE = 25
MAX_PAGES = 100
MAX_CANDIDATES_PER_TYPE = 5
CURRENT_LOOKBACK_DAYS = 550
BASE = "https://asx.api.cmfyapp.com/asx-research/1.0"
NOW = datetime.now(timezone.utc)
RUN_ID = NOW.strftime("%Y%m%dT%H%M%SZ") + "_" + uuid.uuid4().hex[:8]
ROOT = Path("/content/asx_bhp_v3") / RUN_ID
ROOT.mkdir(parents=True, exist_ok=False)
ARCHIVE = ROOT.parent / f"{RUN_ID}.zip"

class AccessRestricted(RuntimeError):
    """Stop the entire run, including other categories and companies."""

session = requests.Session()
session.headers.update({"Accept": "application/json, application/pdf, */*"})

def fetch(path, *, params=None):
    # Throttle every request, not only transitions between companies.
    time.sleep(REQUEST_DELAY_SECONDS)
    url = f"{BASE}/{path}"
    for attempt in range(3):
        try:
            log(f"GET {path} | attempt {attempt + 1}/3")
            response = session.get(url, params=params, timeout=90)
            if response.status_code in (403, 429):
                raise AccessRestricted(f"HTTP {response.status_code} at {path}; stopping")
            response.raise_for_status()
            log(f"HTTP {response.status_code} | {len(response.content):,} bytes | {path}")
            return response
        except AccessRestricted:
            raise
        except requests.RequestException:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)

def resolve(code):
    payload = fetch("search/predictive", params={
        "searchText": code, "useBondsLookup": "true"
    }).json()
    items = payload.get("data", {}).get("items", [])
    hits = [item for item in items if str(item.get("symbol", "")).upper() == code
            and item.get("xidEntity") is not None]
    ids = {str(item["xidEntity"]) for item in hits}
    if len(ids) != 1:
        raise ValueError(f"{code}: expected one exact xidEntity, found {sorted(ids)}")
    return ids.pop(), hits[0].get("displayName", "")

def discover(xid):
    rows, seen, total = [], set(), None
    for page in range(MAX_PAGES):
        data = fetch("markets/announcements", params={
            "entityXids": xid, "page": page, "itemsPerPage": PAGE_SIZE,
            "summaryCountsDate": NOW.date().isoformat()
        }).json().get("data", {})
        items = data.get("items")
        if not isinstance(items, list):
            raise ValueError("Invalid announcement response items")
        count = data.get("count")
        if isinstance(count, int):
            total = count
        for item in items:
            key = item.get("documentKey")
            if key and key not in seen:
                seen.add(key)
                rows.append(item)
        log(f"Announcements page {page + 1}: {len(items)} items; unique {len(rows)}/{total if total is not None else '?'}")
        if total is not None and len(rows) >= total:
            break
        if len(items) < PAGE_SIZE:
            break
    complete = isinstance(total, int) and len(rows) == total
    return rows, total, complete

def age_days(value):
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return (NOW - dt).days
    except (ValueError, TypeError):
        return None

def write_csv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

AUDIT_FIELDS = ["Run_ID", "ASX_Code", "Report_Type", "Announcement_Date",
                "Headline", "Document_Key", "Title_Score", "Age_Days",
                "Decision", "Reason", "Detected_Type", "Subtype",
                "Period_End", "Pages_Total", "Pages_Inspected", "Markers",
                "Marker_Pages", "SHA256", "Bytes"]
REGISTER_FIELDS = ["Run_ID", "ASX_Code", "Company", "Report_Type",
                   "Status", "Reason", "Document_Key", "Headline",
                   "Announcement_Date", "Period_End", "Subtype",
                   "Local_Path", "SHA256", "Announcements_Found",
                   "Announcements_Total", "Discovery_Complete"]

audit, register, fatal_error = [], [], None
try:
    if os.environ.get("ASX_AUTOMATED_ACCESS_AUTHORISED") != "YES":
        raise PermissionError("Set ASX_AUTOMATED_ACCESS_AUTHORISED=YES only after confirming access rights.")
    for tranche_start in range(0, len(CODES), TRANCHE_SIZE):
        tranche = CODES[tranche_start:tranche_start + TRANCHE_SIZE]
        if tranche_start:
            time.sleep(TRANCHE_DELAY_SECONDS)
        for index, code in enumerate(tranche):
            if index:
                time.sleep(COMPANY_DELAY_SECONDS)
            log(f"START {code}: resolving issuer identity")
            xid, company = resolve(code)
            log(f"{code}: issuer resolved as {company} ({xid}); retrieving announcements")
            announcements, total, complete = discover(xid)
            print(f"{code}: {len(announcements)}/{total} announcements; complete={complete}")
            if not complete:
                raise ValueError(f"{code}: announcement discovery incomplete; selection withheld")
            for category, rule in TITLE_RULES.items():
                log(f"{code} {category}: identifying report candidates")
                candidates = [a for a in announcements if a.get("documentKey")
                              and rule.search(str(a.get("headline", "")))]
                candidates.sort(key=lambda a: str(a.get("date", "")), reverse=True)
                candidates = [a for a in candidates if age_days(a.get("date")) is not None and 0 <= age_days(a.get("date")) <= CURRENT_LOOKBACK_DAYS and not re.search(r"presentation|transcript|webcast|briefing", str(a.get("headline", "")), re.I)]
                log(f"{code} {category}: {len(candidates)} matching titles; inspecting up to {MAX_CANDIDATES_PER_TYPE}")
                selected = None
                expected_period = {"ANNUAL": "2026-06-30", "HALF_YEAR": "2025-12-31", "QUARTERLY": "2026-06-30"}[category]
                for item in candidates[:MAX_CANDIDATES_PER_TYPE]:
                    key = str(item["documentKey"])
                    title = str(item.get("headline", ""))
                    announcement_date = str(item.get("date", ""))
                    row = dict(Run_ID=RUN_ID, ASX_Code=code, Report_Type=category,
                               Announcement_Date=announcement_date, Headline=title,
                               Document_Key=key, Title_Score=1,
                               Age_Days=age_days(announcement_date),
                               Decision="", Reason="")
                    try:
                        log(f"{code} {category}: validating {key} | {announcement_date} | {title[:90]}")
                        content = fetch(f"file/{key}").content
                        result = validate_pdf(content, title, category)
                        log(f"{code} {category}: {result.status} | {result.reason} | {result.pages_inspected}/{result.pages_total} pages | period {result.period_end}")
                        row.update(Detected_Type=result.detected_type,
                                   Subtype=result.subtype, Period_End=result.period_end,
                                   Pages_Total=result.pages_total,
                                   Pages_Inspected=result.pages_inspected,
                                   Markers="|".join(result.markers),
                                   Marker_Pages=json.dumps(result.marker_pages),
                                   SHA256=result.sha256, Bytes=len(content),
                                   Decision=result.status, Reason=result.reason)
                        if result.status == "CANDIDATE_VALIDATED" and result.period_end != expected_period:
                            row.update(Decision="REVIEW_REQUIRED", Reason=f"Expected {expected_period}; detected {result.period_end}")
                            log(f"{code} {category}: PERIOD MISMATCH; expected {expected_period}")
                            audit.append(row)
                            continue
                        # The candidate is saved for analyst inspection, NOT marked
                        # verified or Level 1 eligible. Recency is recorded, not inferred.
                        if result.status == "CANDIDATE_VALIDATED":
                            pdf_dir = ROOT / code
                            pdf_dir.mkdir(exist_ok=True)
                            pdf_path = pdf_dir / f"{code}_{category}_{key}.pdf"
                            pdf_path.write_bytes(content)
                            selected = (item, result, pdf_path)
                            audit.append(row)
                            break
                    except AccessRestricted:
                        row.update(Decision="ACCESS_RESTRICTED",
                                   Reason="HTTP 403/429: run terminated")
                        audit.append(row)
                        raise
                    except (requests.RequestException, ValueError) as exc:
                        row.update(Decision="ERROR", Reason=f"{type(exc).__name__}: {exc}")
                    audit.append(row)
                record = dict(Run_ID=RUN_ID, ASX_Code=code, Company=company,
                              Report_Type=category, Announcements_Found=len(announcements),
                              Announcements_Total=total, Discovery_Complete=complete)
                if selected:
                    item, result, pdf_path = selected
                    record.update(Status="CANDIDATE_VALIDATED",
                                  Reason=result.reason, Document_Key=item["documentKey"],
                                  Headline=item.get("headline", ""),
                                  Announcement_Date=item.get("date", ""),
                                  Period_End=result.period_end, Subtype=result.subtype,
                                  Local_Path=str(pdf_path.relative_to(ROOT)),
                                  SHA256=result.sha256)
                else:
                    record.update(Status="REVIEW_REQUIRED",
                                  Reason="No candidate passed conservative PDF checks; inspect audit")
                register.append(record)
                log(f"{code} {category}: FINAL {record['Status']}")
except (AccessRestricted, PermissionError, ValueError, requests.RequestException) as exc:
    fatal_error = f"{type(exc).__name__}: {exc}"
    print("RUN STOPPED:", fatal_error)
finally:
    write_csv(ROOT / "candidate_audit.csv", audit, AUDIT_FIELDS)
    write_csv(ROOT / "report_register.csv", register, REGISTER_FIELDS)
    (ROOT / "manifest.json").write_text(json.dumps({
        "run_id": RUN_ID, "codes": CODES, "created_utc": NOW.isoformat(),
        "fatal_error": fatal_error, "audit_count": len(audit),
        "register_count": len(register),
        "access_authorisation_confirmed_by_operator": os.environ.get(
            "ASX_AUTOMATED_ACCESS_AUTHORISED") == "YES",
        "note": "CANDIDATE_VALIDATED is preliminary; not an eligibility decision."
    }, indent=2), encoding="utf-8")
    # Archive only this run directory; never package stale output from prior runs.
    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(ROOT.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(ROOT.parent))
    log(f"ZIP created: {ARCHIVE}")
    print("Candidate audit rows:", len(audit), "Register rows:", len(register))
    log("Archive ready. Download it from a separate Colab notebook cell.")
