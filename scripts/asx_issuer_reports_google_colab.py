#!/usr/bin/env python3
"""Google Colab-only ASX issuer-report research prototype.

PURPOSE: Inspect announcements and report candidates for a five-company test.
STATUS: Experimental; not approved for bulk or scheduled ASX collection.
SOURCE: Unofficial public website endpoints. Confirm permission before use.
OUTPUT: /content/asx_colab_candidate_audit.csv
"""
import csv
import re
import time
from datetime import datetime, timezone
from pathlib import Path
import requests

# STEP 1: Configure a deliberately small research sample.
# Future authorised larger runs may supply more codes; this test uses five.
TRANCHE_SIZE = 10
COMPANY_DELAY_SECONDS = 15
TRANCHE_DELAY_SECONDS = 15 * 60

CODES = ("ACW", "ACE", "BHP", "CSL", "WDS")
API = "https://asx.api.cmfyapp.com/asx-research/1.0"
OUTPUT = Path("/content/asx_colab_candidate_audit.csv")
REPORT_TERMS = re.compile(r"appendix\s*4[dec]|annual report|half.year|quarterly|financial statements", re.I)
EXCLUDE_TERMS = re.compile(r"presentation|transcript|webcast|briefing", re.I)

# STEP 2: Define API access. This code is disabled by default until permission
# for automated access is established; do not bypass rate limits or blocks.
def get_json(session, route, params):
    response = session.get(f"{API}/{route}", params=params, timeout=30)
    # Access restrictions must stop the entire run; never retry or bypass them.
    if response.status_code in (403, 429):
        raise RuntimeError(f"ASX access restricted (HTTP {response.status_code}); stopping")
    response.raise_for_status()
    return response.json().get("data", {})

# STEP 3: Resolve exact ASX symbols to entity IDs (xidEntity, not xid).
def resolve(session, code):
    items = get_json(session, "search/predictive", {
        "searchText": code, "useBondsLookup": "true"
    }).get("items", [])
    matches = [i for i in items if i.get("symbol") == code and i.get("xidEntity")]
    if len(matches) != 1:
        raise ValueError(f"Ambiguous ticker: {code}")
    return matches[0]["xidEntity"]

# STEP 4: Inspect only one announcement page in this exploratory prototype.
# A production collector MUST implement full pagination and completeness checks.
def inspect_first_page(session, code, entity):
    data = get_json(session, "markets/announcements", {
        "entityXids": entity, "page": 0, "itemsPerPage": 25,
        "summaryCountsDate": datetime.now(timezone.utc).date().isoformat()
    })
    for item in data.get("items", []):
        title = item.get("headline", "")
        if REPORT_TERMS.search(title) and not EXCLUDE_TERMS.search(title):
            yield {
                "ASX_Code": code,
                "Headline": title,
                "Date": item.get("date", ""),
                "Document_Key": item.get("documentKey", ""),
                "Note": "TITLE MATCH ONLY — NOT VERIFIED FINANCIAL REPORT"
            }

# STEP 5: Explicit opt-in is required; this prevents accidental API requests
# when a user imports or runs this experimental Colab file.
def main():
    import os
    if os.getenv("ASX_AUTOMATED_ACCESS_AUTHORISED") != "YES":
        raise SystemExit(
            "No ASX requests made. Confirm authorised automated access, "
            "then explicitly set ASX_AUTOMATED_ACCESS_AUTHORISED=YES."
        )
    rows = []
    with requests.Session() as session:
        # STEP 6: Process at most ten companies per tranche.
        # Wait 15 seconds between companies and 15 minutes between tranches.
        # No wait occurs after the final company or final tranche.
        for start in range(0, len(CODES), TRANCHE_SIZE):
            tranche = CODES[start:start + TRANCHE_SIZE]
            print(f"Starting tranche {start // TRANCHE_SIZE + 1}: {tranche}")
            for index, code in enumerate(tranche):
                entity = resolve(session, code)
                rows.extend(inspect_first_page(session, code, entity))
                if index < len(tranche) - 1:
                    print(f"Waiting {COMPANY_DELAY_SECONDS}s before next company")
                    time.sleep(COMPANY_DELAY_SECONDS)
            if start + TRANCHE_SIZE < len(CODES):
                print(f"Waiting {TRANCHE_DELAY_SECONDS}s before next tranche")
                time.sleep(TRANCHE_DELAY_SECONDS)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "ASX_Code", "Headline", "Date", "Document_Key", "Note"
        ])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Exploratory candidate audit: {OUTPUT}; rows={len(rows)}")

if __name__ == "__main__":
    main()
