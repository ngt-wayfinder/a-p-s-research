#!/usr/bin/env python3
"""Compare provisional ASX candidates with a user-supplied official ASX company directory CSV.

Usage:
 python scripts/verify_asx_directory.py --candidates data/working/operating_candidates.csv --directory data/raw/ASXListedCompanies.csv --output verification_results.csv
"""
import argparse
import csv
import difflib
from pathlib import Path

def load_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def pick(row, names):
    normal = {k.lower().strip().replace(" ", "_"): v for k, v in row.items() if k}
    for name in names:
        val = normal.get(name)
        if val is not None:
            return val.strip()
    return ""

def normalise_name(value):
    return " ".join("".join(c if c.isalnum() else " " for c in value.upper()).split())

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--candidates", default="data/working/operating_candidates.csv")
    p.add_argument("--directory", required=True, help="CSV downloaded from the official ASX company directory")
    p.add_argument("--output", default="verification_results.csv")
    a = p.parse_args()
    candidates = load_csv(a.candidates)
    official = load_csv(a.directory)
    if not candidates or not official:
        raise SystemExit("One of the CSV files is empty")
    directory = {}
    for row in official:
        ticker = pick(row, ["asx_code", "asx_code_", "code", "ticker", "asxcode"])
        name = pick(row, ["company_name", "company", "name", "company_name_"])
        if ticker:
            directory.setdefault(ticker.upper().removesuffix(".AX"), []).append(name)
    if not directory:
        raise SystemExit("No ticker column recognised in official directory; check its CSV headers")
    result = []
    for row in candidates:
        ticker = pick(row, ["asx_code", "ticker", "code"]).upper().removesuffix(".AX")
        name = pick(row, ["company_name", "company", "name"])
        if not ticker:
            raise SystemExit("Candidate CSV has an empty ticker")
        names = directory.get(ticker, [])
        if not names:
            status, official_name, similarity = "MISSING", "", ""
        else:
            official_name = max(names, key=lambda n: difflib.SequenceMatcher(None, normalise_name(name), normalise_name(n)).ratio())
            similarity = round(difflib.SequenceMatcher(None, normalise_name(name), normalise_name(official_name)).ratio(), 3)
            status = "MATCHED" if similarity >= 0.85 else "NAME_REVIEW"
            if len(names) > 1:
                status = "DUPLICATE_OFFICIAL"
        result.append({"ASX_Code": ticker, "Candidate_Name": name, "Official_Name": official_name, "Result": status, "Name_Similarity": similarity, "GICS_Industry": pick(row, ["gics_industry"]), "Listing_Status": "NOT_CHECKED", "Business_Model_Status": "NOT_CHECKED"})
    out = Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(result[0]))
        writer.writeheader()
        writer.writerows(result)
    print(f"Candidates: {len(result)} | Official directory tickers: {len(directory)}")
    for status in ["MATCHED", "NAME_REVIEW", "MISSING", "DUPLICATE_OFFICIAL"]:
        print(f"{status}: {sum(r['Result'] == status for r in result)}")
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
