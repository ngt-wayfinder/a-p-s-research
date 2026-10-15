# Data dictionary and authoritative sources

**Current canonical locations (until migration completes):**
- Candidate population: `data/working/operating_candidates.csv` (provisional working input).
- Status matrix: `research/01_universe_validation/registers/STEP_1_3_2_EVIDENCE_MATRIX.csv` (316 rows; status classifications, not eligibility).
- Evidence ledger: `research/01_universe_validation/registers/STEP_1_3_2_4_PRIMARY_EVIDENCE_LEDGER.csv`.
- Exceptions: `research/01_universe_validation/registers/STEP_1_3_2_4_UNRESOLVED_EXCEPTIONS.csv`.
- Historical comprehensive report: `research/01_universe_validation/archive/STEP_1_3_2_4_COMPREHENSIVE_VERIFICATION_REPORT.md` (dated snapshot).

**Proposed after migration:** candidate input in `data/working/`; registers and evidence ledger in `research/01_universe_validation/registers/`. Verify actual Git paths first.

**Level 1 status vocabulary:** `REVIEW_PENDING` = unassessed/incomplete; `ELIGIBLE` = all Level 1 gates evidenced; `QUARANTINED` = material conflict or unresolved disqualifying gate. Preserve detailed existing issuer/security/trading vocabularies; do not translate them automatically into eligibility.

**Existing matrix columns:** `ASX_Code`, `Company_Name`, `Priority`, `Issuer_Evidence_Status`, `Historical_Continuity_Status`, `Security_Form_Status`, `Trading_Status`, `Existing_Research_Note`. Interpret with its accompanying README. Treat date-stamped batches as snapshots.
