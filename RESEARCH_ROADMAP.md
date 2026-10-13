# ASX Penny-Stock Research Roadmap

**Goal:** Progress from 318 provisionally classified ASX operating-company candidates to 5–10 deeply researched opportunities over a 1–2-year investment horizon. Intended portfolio budget: under A$10,000. This is a research process, not a recommendation to buy.

## Ordered next steps

**Status key:** COMPLETED = documented work finished; IN PROGRESS = partially verified; NOT STARTED = pending.

1. **[IN PROGRESS] Validate the 318 operating companies.** Confirm active ASX listings, remove duplicates and misclassified investment vehicles, and flag suspended or delisted securities.
2. **[NOT STARTED] Resolve missing market data.** Investigate 196 securities with missing price histories and remaining missing market capitalisations; add any eligible operating companies.
3. **[NOT STARTED] Collect financial statements.** Retrieve annual, half-year and applicable quarterly cash-flow reports; record cash, revenue, operating cash flow, debt, shares outstanding, source dates and links.
4. **[NOT STARTED] Calculate financial health.** Assess cash runway, revenue growth, profitability, debt and likely funding needs, using sector-specific measures for explorers, biotech and established businesses.
5. **[NOT STARTED] Screen for financial resilience.** Narrow toward 100–150 candidates, with documented exceptions for early-stage companies with credible milestones.
6. **[NOT STARTED] Assess dilution.** Review historical issuance, placements, convertibles, options and expected future capital raisings.
7. **[NOT STARTED] Identify catalysts in the next 3–24 months.** Include exploration results, approvals, trials, contracts, production milestones and product launches; record uncertainty.
8. **[NOT STARTED] Shortlist 30–50 companies.** Prioritise resilience, catalysts, execution, valuation, liquidity and dilution, not momentum alone.
9. **[NOT STARTED] Deep-research 15–20.** Examine management, competition, project economics, shareholders, filings and execution history.
10. **[NOT STARTED] Value 5–10 finalists.** Prepare bear/base/bull scenarios including financing and dilution assumptions.
11. **[NOT STARTED] Propose portfolio construction.** Evaluate sizing, liquidity, diversification, thesis-invalidating events and exits within the under-A$10,000 budget.
12. **[NOT STARTED] Implement monitoring.** Use GitHub Actions and persistent storage to refresh market data, track ASX announcements and capital raisings, and flag thesis changes.

## Current status (updated 13 October 2026)

- Initial ASX universe: 1,923 securities.
- Numerical screening: 339 qualified.
- Earlier provisional classification: 318 operating candidates, 20 investment vehicles excluded, 1 uncertain. **The subsequently uploaded verification CSV contains 316 candidates**; reconcile the two-company difference before closing Step 1.
- **Step 1.1 — COMPLETED:** All 316 tickers and company names in `operating_candidates.csv` matched the uploaded official ASX company directory (`ASXListedCompanies.csv`). Directory presence alone does not establish tradeability.
- **Step 1.2 — PRELIMINARY REVIEW COMPLETED; FINAL CONFIRMATION PENDING:** 316 Yahoo Finance tickers scanned (306 recent price data; 10 exceptions). All 10 exceptions reviewed against ASX announcement histories and documented in `research/trading_status/trading_status_verification_register_2026-10-13.csv`.
  - Four trading halts identified: 3DA, MRD, REC, TM1. Official halt PDFs reviewed; actual resumption not confirmed.
  - PAR: suspension and voluntary administration identified; exclude from currently tradeable shortlist pending evidence of reinstatement.
  - BSA: reinstatement announced 1 October; current tradeability not independently confirmed.
  - EWC, GWR, SFM, SGI: no current suspension identified in supplied announcement histories; live tradeability unconfirmed.
- **Step 1 outstanding:** Reconcile 318 versus 316 candidates; check duplicates, delistings and operating-company classification; confirm actual resumption/live status where required. Do not mark all 316 as actively trading.
- 196 missing-price records remain to be investigated.
- **Immediate next action: Complete Step 1.3 — reconcile the 318-to-316 difference and verify business-model classification, duplicates and delistings for the 316-company candidate list.** Then close remaining trading-status exceptions. **Step 2** (missing market data) follows once Step 1 is signed off.

## Quality controls

- Retain sources, observation dates and original datasets.
- Treat missing values as unknown, not zero.
- Verify corporate actions and shares on issue before valuation.
- Review results at each stage before proceeding.
