#!/usr/bin/env python3
"""Step 1.3.2 Action 1: deterministic duplicate audit of operating_candidates.csv."""
import csv
import re
import sys
from collections import defaultdict
from itertools import combinations

THRESHOLD = 0.84

def normalize(name):
    name = name.upper().replace("&", " AND ")
    name = re.sub(r"[^A-Z0-9 ]", " ", name)
    name = re.sub(r"\b(LIMITED|LTD|INC|NL|CORPORATION|CORP|GROUP|HOLDINGS|HOLDING|THE)\b", " ", name)
    return " ".join(name.split())

def duplicates(rows, key):
    buckets = defaultdict(list)
    for row in rows:
        buckets[key(row)].append(row)
    return {k: v for k, v in buckets.items() if len(v) > 1}

def similarity(a, b):
    """Normalized Levenshtein similarity (same metric as initial audit)."""
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return 1 - prev[-1] / max(len(a), len(b), 1)

def audit(path):
    with open(path, encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["ASX_Code"] = row["ASX_Code"].strip().upper()
        row["Company_Name"] = row["Company_Name"].strip()
    exact_ticker = duplicates(rows, lambda r: r["ASX_Code"])
    exact_name = duplicates(rows, lambda r: r["Company_Name"].upper())
    normalized_name = duplicates(rows, lambda r: normalize(r["Company_Name"]))
    similar = []
    for a, b in combinations(rows, 2):
        an, bn = normalize(a["Company_Name"]), normalize(b["Company_Name"])
        if an == bn:
            continue
        score = similarity(an, bn)
        if score >= THRESHOLD:
            similar.append((round(score, 3), a["ASX_Code"], b["ASX_Code"], a["Company_Name"], b["Company_Name"]))
    similar.sort(reverse=True)
    print(f"Records: {len(rows)}; unique tickers: {len(set(r['ASX_Code'] for r in rows))}")
    print(f"Duplicate tickers: {len(exact_ticker)}; exact names: {len(exact_name)}; normalized names: {len(normalized_name)}")
    print(f"Fuzzy matches (normalized Levenshtein >= {THRESHOLD}): {len(similar)}")
    for score, code_a, code_b, name_a, name_b in similar:
        print(f"{code_a}/{code_b}: {score:.3f} | {name_a} | {name_b}")
    return bool(exact_ticker or exact_name or normalized_name)

if __name__ == "__main__":
    sys.exit(1 if audit(sys.argv[1] if len(sys.argv) > 1 else "operating_candidates.csv") else 0)
