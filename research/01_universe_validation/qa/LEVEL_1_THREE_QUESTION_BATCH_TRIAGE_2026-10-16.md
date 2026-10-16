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

## Additional company-by-company evidence assessment
See [the named 316-company decision table](../registers/LEVEL_1_THREE_QUESTION_COMPANY_DECISION_TABLE_2026-10-16.csv), with company name as the first column, ASX code, evidence classifications, decision, exact outstanding checks, evidence IDs and a primary URL.

- **170 companies:** an ASX quotation application in the existing ledger explicitly records ORDINARY FULLY PAID securities. This establishes a historical security-class fact, **not** current trading eligibility.
- **182 companies:** an annual, half-year, quarterly, activities or investor report is identified by title. The title is a lead for operating-company assessment, **not** proof the company operates.
- **280 companies:** have at least one ASX-hosted announcement PDF in the ledger, which can support historical issuer attribution but is not a dated current trading-status check.
- **316 companies:** current listing/trading and material impediment evidence is not established by this exercise. Accordingly **none can yet be promoted to ELIGIBLE** solely from the existing ledger. The 316-row table explicitly explains each outstanding condition.

These groups **overlap** and must not be summed. The quotation-application count here (170) requires an explicit `ORDINARY FULLY PAID` string in the extracted fact, whereas 173 document titles matched the broader quotation-application pattern. No current exchange status or operations evidence has been fabricated.
