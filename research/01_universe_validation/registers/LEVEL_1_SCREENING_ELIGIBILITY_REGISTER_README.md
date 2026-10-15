# Level 1 screening eligibility register — initial establishment

**Created:** 2026-10-15. **Population:** 316 unique ASX tickers. **State:** screening register established; no Level 1 approvals or exclusions adjudicated.

## Authoritative input and traceability

- Population and industry: `data/working/operating_candidates.csv`.
- Source gate classifications and priorities: `research/01_universe_validation/registers/STEP_1_3_2_EVIDENCE_MATRIX.csv`.
- Primary source evidence: `research/01_universe_validation/registers/STEP_1_3_2_4_PRIMARY_EVIDENCE_LEDGER.csv` (1,291 evidence records; evidence IDs retained in each company row).
- Open exceptions: `research/01_universe_validation/registers/STEP_1_3_2_4_UNRESOLVED_EXCEPTIONS.csv` (316 records; missing facts, review flags and recommended resolutions imported).

## Conservative screening decision

Every row starts as `REVIEW_PENDING`, **not** `ELIGIBLE` or `QUARANTINED`. Issuer identity evidence is recorded, but does not certify complete historical continuity, security rights, current trading status, corporate-action attribution or operating-business eligibility. Every source matrix row records historical-continuity and dated-trading-status gaps. No investment recommendation follows from this register.

### Gate interpretation

- `Issuer_Identity_Gate=EVIDENCE_RECORDED_REVIEW_REQUIRED`: an issuer identity confirmation is recorded in the source matrix; Level 1 reviewer signoff remains outstanding.
- `Historical_Continuity_Gate=OPEN_EVIDENCE_GAPS`: source matrix reports partial historical-continuity evidence.
- `Security_Form_Gate=OPEN_EVIDENCE_GAPS`: incomplete, pending or not-fully-verified security classification. `PARTIAL_EVIDENCE_REVIEW_REQUIRED`: a specific security-form fact is recorded but full gate clearance has not been established.
- `Trading_Status_Gate=OPEN_DATED_STATUS_GAPS`: a current dated primary trading/suspension assessment remains open.
- `Operating_Company_Gate=PROVISIONAL_OPERATING_CLASSIFICATION_UNVERIFIED`: candidate inclusion is provisional, not independently certified here.
- `Corporate_Actions_Gate=REVIEW_REQUIRED`: complete economic lineage and material actions have not been signed off.

### Required manual decision protocol

To set `ELIGIBLE`, individually verify and document all six gates with primary evidence, cutoff dates, security-specific identity and corporate-action comparability, plus an explicit reviewer decision and date. Set `QUARANTINED` only after documenting a material disqualifying conflict or eligibility failure; do not quarantine merely because evidence is incomplete. Preserve `REVIEW_PENDING` for missing evidence. Never infer live trading status from ABR activity or an issuer announcement alone.

`Review_As_Of` and `Decision_Evidence_Cutoff` indicate the **initial register snapshot**, not a completed review of each issuer. `Last_Decision_Review_Date` is intentionally blank for every row. Evidence dates remain governed by the original ledger and exception records. The source ledger path is stored alongside row-specific evidence IDs, and the detailed exception facts are preserved without treating them as verified findings.

## Initial quality checks

- 316 rows, 316 unique tickers, all present in the candidate population.
- 316 rows with linked primary evidence IDs; 316 rows with recorded unresolved exceptions.
- All 316 decisions `REVIEW_PENDING`; 0 `ELIGIBLE`; 0 `QUARANTINED`.
- The original research inputs were read, not modified.

**Next work:** evidence-driven gate closure, dated trading and security review, explicit operating-company assessment and reviewer signoff. Do not move to financial screening on the strength of this register alone.
