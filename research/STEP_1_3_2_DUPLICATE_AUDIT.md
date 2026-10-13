# Step 1.3.2 — Action 1: Duplicate audit

**Date:** 13 October 2026  
**Input:** Repository `operating_candidates.csv` (316 records)  
**Scope:** Static CSV duplicate and similar-name analysis only. **Not** an ASX corporate-action or delisting verification.

## Results

| Test | Result |
|---|---:|
| Candidate records | 316 |
| Unique ASX tickers | 316 |
| Repeated ASX ticker groups | 0 |
| Repeated exact company-name groups | 0 |
| Repeated normalized-name groups | 0 |
| Similar-name pairs requiring manual review | 4 |

### Fuzzy matches from initial audit

Initial fuzzy score uses **normalized Levenshtein similarity**: `1 - edit_distance / max(name lengths)`, with threshold **0.84**. Normalization uppercases, replaces ampersands, removes punctuation and common corporate suffixes.

| Ticker A | Ticker B | Company A | Company B | Initial similarity |
|---|---|---|---|---:|
| AUQ | AS1 | Alara Resources Limited | Asara Resources Limited | 0.933 |
| AS1 | AAR | Asara Resources Limited | Astral Resources NL | 0.875 |
| SHN | STM | Sunshine Metals Limited | Sunstone Metals Ltd | 0.867 |
| KGL | MGX | KGL Resources Limited | MGX Resources Limited | 0.846 |

**Interpretation:** No exact or normalized duplicates found. The four pairs are string-similarity alerts only, **not confirmed duplicate companies**. No records were removed.

## Next action

Action 2: investigate flagged pairs and any identity-related corporate actions, ticker changes and delistings using authoritative ASX records. Confirm whether each pair represents distinct issuers. Only after this evidence review should Step 1.3.2 be marked complete.

## Reproducibility

`scripts/audit_operating_duplicates.py` is a reusable Python script for ticker/name duplicates and fuzzy review. It uses the same normalized Levenshtein fuzzy-scoring method as the initial audit; the threshold is 0.84.

## Action 2 — Pair-by-pair verification

- **AUQ / AS1 — VERIFIED DISTINCT (13 Oct 2026):** Different ABNs (27 122 892 719 vs 39 006 710 774) and different mining projects (Oman vs Guinea). Both retained. [Evidence record](identity_checks/AUQ_AS1_2026-10-13.md).
- **AS1 / AAR — VERIFIED DISTINCT (13 Oct 2026):** Different ABNs (39 006 710 774 vs 24 651 541 976), different ACNs and separate Guinea / WA gold projects. Both retained. [Evidence record](identity_checks/AS1_AAR_2026-10-13.md).
- **SHN / STM — PENDING.**
- **KGL / MGX — PENDING.**
