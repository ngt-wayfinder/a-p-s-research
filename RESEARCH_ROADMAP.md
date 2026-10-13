# ASX Penny-Stock Research Roadmap

**Goal:** Progress from a provisional ASX operating-company universe to 5–10 deeply researched opportunities over a 1–2-year horizon. Intended portfolio budget: under A$10,000. Research plan only, not investment advice.

**Last reviewed:** 13 October 2026

## Status definitions

- **COMPLETED:** The specified deliverable has been produced and checked within its stated scope.
- **IN PROGRESS:** Work has started, but acceptance criteria are not yet satisfied.
- **NOT STARTED:** No completed deliverable is recorded.
- **BLOCKED / NEEDS VERIFICATION:** A specific evidence gap prevents completion. An ASX announcement headline is not equivalent to reading the underlying PDF.
- Statuses reflect the repository evidence and work performed to date, not a claim of live market status.

## Phase 0 — Initial universe and numerical screening [COMPLETED — historical baseline]

- **0.1 [COMPLETED]** Assemble initial ASX directory universe: 1,923 securities (historical baseline).
- **0.2 [COMPLETED]** Apply preliminary numerical price, market-cap and liquidity criteria: 339 qualified (historical baseline).
- **0.3 [COMPLETED — PROVISIONAL]** Initial operating/investment-vehicle classification: 318 operating candidates, 20 excluded investment vehicles and 1 uncertain (historical classification, not independently validated).
- **0.4 [COMPLETED]** Upload working `operating_candidates.csv` to GitHub. Subsequent verification used **316 rows**, not 318. The difference is explained: GDF (Garda Property Group) and GDI (GDI Property Group) were removed as REIT/property investment vehicles; original workbook GICS labels both as Equity Real Estate Investment Trusts (REITs).

## Step 1 — Validate the operating-company universe [IN PROGRESS]

**Purpose:** Reconcile the working candidate count, confirm directory identity, examine trading-status exceptions and validate the business model and listing status before establishing the final universe.

1. **1.1 [COMPLETED] Directory identity check**
   - **1.1.1 [COMPLETED]** Obtain and upload `ASXListedCompanies.csv` from the ASX directory.
   - **1.1.2 [COMPLETED]** Compare the 316 working candidates with the uploaded directory: 316 ticker/name matches, zero missing tickers and zero name mismatches.
   - **Limitation:** Directory membership does not confirm that shares are presently tradeable.

2. **1.2 [IN PROGRESS] Trading-status verification**
   - **1.2.1 [COMPLETED]** Test Yahoo Finance price-history retrieval on 10 candidates.
   - **1.2.2 [COMPLETED]** Run preliminary scan of 316 candidates: 306 recent price dates and 10 requiring review; no missing/error results. Calendar-day thresholds are screening heuristics only.
   - **1.2.3 [COMPLETED — HEADLINE REVIEW]** Review ASX announcement histories for all 10 exceptions: 3DA, BSA, EWC, GWR, MRD, PAR, REC, SFM, SGI and TM1.
   - **1.2.4 [COMPLETED]** Read official trading-halt PDFs for 3DA, MRD, REC and TM1. Recorded reasons and scheduled halt end dates (14 October for TM1; 15 October for 3DA, MRD and REC). Scheduled end dates do **not** prove trading resumed.
   - **1.2.5 [COMPLETED]** Save 10 individual GitHub review records and the consolidated CSV: [trading-status verification register](research/trading_status/trading_status_verification_register_2026-10-13.csv).
   - **1.2.6 [BLOCKED / NEEDS VERIFICATION]** Confirm subsequent trading resumption for 3DA, MRD, REC and TM1; verify PAR's continuing suspension/administration from underlying notices and subsequent disclosures; verify live status of BSA, EWC, GWR, SFM and SGI. Do not classify the latter five as definitively actively trading on announcement-headline evidence alone.
   - **Interim classification as of review:** four trading halts (3DA, MRD, REC, TM1); one suspended/in voluntary administration (PAR); one historical suspension followed by reinstatement (BSA); four with no current suspension found in supplied headlines (EWC, GWR, SFM, SGI). PAR is excluded from the **currently tradeable shortlist**, not automatically deleted from the historical research universe.

3. **1.3 [IN PROGRESS] Reconcile the universe and validate operating-company classification**
   - **1.3.1 [COMPLETED]** Reconciled the historical **318** provisional operating candidates with **316** working candidates using uploaded `ASX_Operating_Company_Classification.xlsx`: **GDF (Garda Property Group)** and **GDI (GDI Property Group)** were excluded because both are classified as Equity Real Estate Investment Trusts (REITs) in the source workbook. **318 − 2 = 316**. This explains the count difference; broader business-model review remains outstanding.
   - **1.3.2 [IN PROGRESS]** Check duplicates, ticker changes, delistings and corporate actions affecting identity. **Action 1 completed:** 316 records, 316 unique tickers, no exact/normalized duplicate names; four fuzzy-name pairs flagged. Results: [duplicate audit](research/STEP_1_3_2_DUPLICATE_AUDIT.md). **Action 2.1 completed:** all four fuzzy-name pairs independently verified as distinct legal entities and retained. **Action 2.2 IN PROGRESS:** initial historical ticker-change cases documented in [ticker-change register](research/STEP_1_3_2_TICKER_CHANGE_REGISTER.md); full 316-company historical cross-match remains pending. **Actions 2.3–2.5 pending:** systematic name changes, mergers and delistings review against ASX evidence.
   - **1.3.3 [NOT STARTED]** Validate operating-business versus investment-vehicle classification using current company activities and official reports. Specifically review GWR's business model.
   - **1.3.4 [NOT STARTED]** Produce an auditable final candidate register with inclusion/exclusion reasons and source dates.

4. **1.4 [NOT STARTED] Step 1 sign-off**
   - **1.4.1 [NOT STARTED]** Resolve or explicitly document outstanding 1.2 trading-status uncertainties and 1.3 classification/count exceptions.
   - **1.4.2 [NOT STARTED]** Approve the final eligible operating-company universe for downstream screening.

**Step 1 exit criterion:** Every included candidate has an auditable identity and business classification; halted/suspended status is distinguished from delisting; outstanding exceptions are explicitly flagged.

## Step 2 — Resolve missing market data [NOT STARTED]

- **2.1 [NOT STARTED]** Revisit the **196 historical missing-price records** and identify whether gaps reflect ticker formatting, corporate actions, delistings, suspensions or provider limitations.
- **2.2 [NOT STARTED]** Investigate remaining missing market capitalisations; reconcile shares outstanding and corporate actions.
- **2.3 [NOT STARTED]** Reapply the price, market-cap and liquidity screen with verified data; add eligible operating companies and record exclusions.
- **2.4 [NOT STARTED]** Save a refreshed universe and data-quality log.

## Step 3 — Collect financial statements [NOT STARTED]

- **3.1 [NOT STARTED]** Collect annual, half-year and relevant quarterly cash-flow reports.
- **3.2 [NOT STARTED]** Extract cash, revenue, operating cash flow, debt and shares outstanding with reporting dates.
- **3.3 [NOT STARTED]** Preserve official source links and resolve extraction exceptions.

## Step 4 — Calculate financial health [NOT STARTED]

- **4.1 [NOT STARTED]** Calculate cash runway and funding needs.
- **4.2 [NOT STARTED]** Assess revenue growth, profitability and debt where relevant.
- **4.3 [NOT STARTED]** Apply sector-appropriate metrics for explorers, biotech and established businesses.

## Step 5 — Screen for financial resilience [NOT STARTED]

- **5.1 [NOT STARTED]** Set documented sector-specific screening thresholds.
- **5.2 [NOT STARTED]** Narrow toward approximately 100–150 candidates, with justified exceptions.
- **5.3 [NOT STARTED]** Save rankings and exclusion reasons.

## Step 6 — Assess dilution [NOT STARTED]

- **6.1 [NOT STARTED]** Review historical placements, share issues, options and convertibles.
- **6.2 [NOT STARTED]** Estimate prospective financing requirements and dilution scenarios.
- **6.3 [NOT STARTED]** Record dilution-risk flags with sources.

## Step 7 — Identify 3–24-month catalysts [NOT STARTED]

- **7.1 [NOT STARTED]** Identify exploration, regulatory, clinical, commercial and production milestones.
- **7.2 [NOT STARTED]** Assess likely timing, dependencies and uncertainty.
- **7.3 [NOT STARTED]** Create a sourced catalyst calendar.

## Step 8 — Shortlist 30–50 companies [NOT STARTED]

- **8.1 [NOT STARTED]** Score resilience, catalysts, execution, valuation, liquidity and dilution.
- **8.2 [NOT STARTED]** Review sector concentration and remove weak candidates.
- **8.3 [NOT STARTED]** Document a shortlist of approximately 30–50.

## Step 9 — Deep-research 15–20 companies [NOT STARTED]

- **9.1 [NOT STARTED]** Review management, governance, shareholders and disclosure quality.
- **9.2 [NOT STARTED]** Evaluate competition, assets/project economics and execution history.
- **9.3 [NOT STARTED]** Document evidence, risks and thesis invalidation conditions.

## Step 10 — Value 5–10 finalists [NOT STARTED]

- **10.1 [NOT STARTED]** Build appropriate valuation models and assumptions.
- **10.2 [NOT STARTED]** Prepare bear/base/bull cases incorporating funding and dilution.
- **10.3 [NOT STARTED]** Review sensitivities and rank 5–10 finalists.

## Step 11 — Propose portfolio construction [NOT STARTED]

- **11.1 [NOT STARTED]** Assess liquidity, sizing and diversification for a portfolio under A$10,000.
- **11.2 [NOT STARTED]** Define entry criteria, thesis-invalidating events and exits.
- **11.3 [NOT STARTED]** Document portfolio risks; do not assume high returns are likely.

## Step 12 — Implement monitoring [NOT STARTED]

- **12.1 [NOT STARTED]** Design GitHub Actions refreshes with persistent checkpoints.
- **12.2 [NOT STARTED]** Monitor ASX announcements, capital raisings and trading-status changes.
- **12.3 [NOT STARTED]** Track financial/catalyst updates and thesis changes.
- **12.4 [NOT STARTED]** Test alerts and establish a review cadence.

## Immediate next action

**Step 1.3.2 Action 2.2:** Review historical ticker changes across the 316 candidates, followed by name changes, mergers and delistings (Actions 2.3–2.5). All four fuzzy-name pairs were verified as distinct (Action 2.1 completed); the static duplicate audit (Action 1) is complete. Then complete 1.3.3–1.3.4. In parallel, keep the 1.2.6 trading-status follow-ups open until independently confirmed.

## Research controls

- Keep raw source files, evidence dates and original outputs.
- Separate **verified facts**, **headline-only observations**, **provisional classifications** and **unresolved questions**.
- Never equate missing data with zero or a stale price date with a trading suspension.
- Reconcile corporate actions and shares on issue before valuation.
- Update statuses only when supporting deliverables exist; review and sign off each stage before moving to the next.
