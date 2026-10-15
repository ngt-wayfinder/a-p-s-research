#!/usr/bin/env python3
"""Validate repository structure, Markdown links and baseline research invariants.

Run from any directory: python scripts/validate_repository.py
"""
from pathlib import Path
import csv, re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
files=[p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
for md in [p for p in files if p.suffix.lower()==".md"]:
    text=md.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)",text):
        if target.startswith(("http:","https:","mailto:","#","data:")):continue
        target=target.split("#",1)[0].split("?",1)[0]
        if target and not (md.parent/target).exists():
            errors.append(f"Broken Markdown link: {md.relative_to(ROOT)} -> {target}")
matrix_candidates=[ROOT/"research/STEP_1_3_2_EVIDENCE_MATRIX.csv",ROOT/"research/01_universe_validation/registers/STEP_1_3_2_EVIDENCE_MATRIX.csv"]
matrix=next((p for p in matrix_candidates if p.exists()),None)
if not matrix:errors.append("Missing authoritative evidence matrix")
else:
    with matrix.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
    codes=[r["ASX_Code"].strip().upper() for r in rows]
    if len(rows)!=316:errors.append(f"Expected 316 matrix rows, got {len(rows)}")
    if len(set(codes))!=316:errors.append("Duplicate or missing ASX codes in evidence matrix")
    expected={"ASX_Code","Company_Name","Priority","Issuer_Evidence_Status","Historical_Continuity_Status","Security_Form_Status","Trading_Status","Existing_Research_Note"}
    if rows and set(rows[0])!=expected:errors.append("Matrix schema differs from baseline")
print(f"Checked {len(files)} files; matrix rows: {len(rows) if matrix else 'missing'}; errors: {len(errors)}")
for err in errors:print("ERROR:",err)
sys.exit(bool(errors))
