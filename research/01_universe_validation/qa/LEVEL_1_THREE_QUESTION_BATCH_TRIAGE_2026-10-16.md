# Three-question Level 1 population triage — 16 October 2026

Applied the approved three-question screen to all **316 unique ASX codes** using the existing primary evidence ledger and authoritative eligibility register. The output is `registers/LEVEL_1_THREE_QUESTION_BATCH_TRIAGE_2026-10-16.csv`.

## Batch findings
- **316/316** have recorded issuer-identity evidence classifications; this does **not** independently establish current listing.
- **280/316** have at least one URL on `announcements.asx.com.au` in the evidence ledger; **36** do not have one detected by this domain-only check. Domain presence is evidence inventory, **not** verification that a PDF was read, a security is listed, or a company is operating.
- **0/316** have newly established dated current listing/trading and material impediment status in this batch.
- Operating-business classification remains unverified in this batch; provisional GICS/industry labels do not independently establish operations.
- **Disposition:** 0 ELIGIBLE / 0 QUARANTINED / 316 REVIEW_PENDING. No unsupported decisions were made and the authoritative Level 1 register was not overwritten.

## Efficient closure plan
1. Obtain a dated authoritative current ASX listed-equity/security-status snapshot for all 316 codes in **one** bulk data retrieval, including suspended/delisted flags; crossmatch and record snapshot date.
2. Bulk match recent issuer reports/business descriptions to classify operating-company status, escalating ambiguous investment vehicles, shells and restructuring cases only.
3. Apply the three-question decision rules across the entire register and promote qualifying companies to financial screening immediately. Investigate only material exceptions; do not require blanket ISIN, current share count or complete corporate-action reconstruction.
4. Run CSV integrity checks, reconcile decision counts and document each exception and source.

**Limitation:** The present GitHub evidence ledger is predominantly issuer-identity/historical-source material, not a reliable current trading-status feed. This batch completes a 316-company *existing-evidence triage*, **not** the requested final verified screen. A current dated exchange source is necessary before representing the result as a full Level 1 determination.
