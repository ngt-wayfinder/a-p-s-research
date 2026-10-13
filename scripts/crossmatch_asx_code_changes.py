#!/usr/bin/env python3
"""Cross-match all rows of a saved official ASX code-change HTML page with candidate tickers.
Usage: python scripts/crossmatch_asx_code_changes.py operating_candidates.csv asx-code-changes.html
Requires: pip install beautifulsoup4
Outputs: stdout CSV of matches and a coverage summary on stderr.
Important: check the source page is complete and includes all year sections 2018-2026.
"""
import csv
import re
import sys
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8-sig", newline="") as f:
        candidates = {r["ASX_Code"].strip().upper() for r in csv.DictReader(f)}
    with open(sys.argv[2], encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    writer = csv.writer(sys.stdout)
    writer.writerow(["date_text","old_code","old_name","new_code","new_name","matched_candidate","change_type"])
    count = 0
    matched = set()
    years = set()
    for table in soup.find_all("table"):
        for tr in table.find_all("tr"):
            cells = [" ".join(td.get_text(" ", strip=True).split()) for td in tr.find_all(["td","th"], recursive=False)]
            # ASX table convention: As of | old code | old name | new code | new name
            if len(cells) < 5:
                continue
            date, old_code, old_name, new_code, new_name = cells[:5]
            old_code = old_code.upper().strip()
            new_code = new_code.upper().strip()
            if not re.fullmatch(r"[A-Z0-9]{2,6}", old_code) or not re.fullmatch(r"[A-Z0-9]{2,6}", new_code):
                continue
            if new_code in candidates or old_code in candidates:
                change_type = "CODE_CHANGE" if old_code != new_code else "NAME_ONLY"
                writer.writerow([date, old_code, old_name, new_code, new_name, new_code if new_code in candidates else old_code, change_type])
                matched.add(new_code if new_code in candidates else old_code)
                count += 1
    print(f"Candidates: {len(candidates)}; matched change events: {count}; candidate codes appearing in change events: {len(matched)}", file=sys.stderr)
    print("WARNING: HTML may omit year sections or use a different table structure. Validate all years and row totals manually before treating as exhaustive.", file=sys.stderr)

if __name__ == "__main__":
    main()
