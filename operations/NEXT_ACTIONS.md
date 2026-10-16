# Next actions — 16 October 2026

## R1: Level 1 risk-based eligibility decisions (ACTIVE)
The repository restructure and 316-company Level 1 register creation have been merged to main. The reconciled register has 316 REVIEW_PENDING, 0 ELIGIBLE and 0 QUARANTINED. Follow the approved proportionality clarification in RESEARCH_ROADMAP.md.

For each candidate: verify current issuer and security identity; dated tradeability; dated reliable ordinary-share count/market-cap input; only material lookback corporate actions; and recent operating-business classification. ISIN is conditional on security ambiguity; full remote historical continuity is not a Level 1 prerequisite. Record source/date/finding and per-gate limitations. Resolve material evidence gaps or document quarantine and re-entry conditions. Never upgrade solely because an ASX announcement exists.

**Immediate four-company work:** 14D, ACF, ACW and ACE need recent dated trading-state evidence and current shares-outstanding/actual allotment reconciliation; operating-business and issuer indications are already available but need formal gate signoff. See research/01_universe_validation/qa/LEVEL_1_RISK_BASED_FOUR_COMPANY_REVIEW_2026-10-16.md. Leave REVIEW_PENDING until decision-critical facts close.

## R2: Controlled progression to financial screening
Advance each ELIGIBLE issuer to Step 2 as approved. Resolve missing price/market-cap data and evaluate runway and resilience. Apply Level 2 continuity where actual financial/price comparisons require it; no wholesale 316-company historical closure.

## R3: Governance and QA
Keep 316 unique codes and consistent decision values, verify source provenance and CSV shape, update PROJECT_STATUS.md and decision log when statuses change, run regression tests, and review PR before merge.
