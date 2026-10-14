# ASX Penny-Stock Research Roadmap

**Goal:** Progress from a provisional ASX operating-company universe to 5–10 deeply researched opportunities over a 1–2-year horizon. Intended portfolio budget: under A$10, 000. Research plan only, not investment advice.

**Last reviewed:** 13 October 2026

## Status definitions

- **COMPLETED:** The specified deliverable has been produced and checked within its stated scope.
- **IN PROGRESS:** Work has started, but acceptance criteria are not yet satisfied.
- **NOT STARTED:** No completed deliverable is recorded.
- **BLOCKED / NEEDS VERIFICATION:** A specific evidence gap prevents completion. An ASX announcement headline is not equivalent to reading the underlying PDF.
- Statuses reflect the repository evidence and work performed to date, not a claim of live market status.

## Entire sequence — authoritative stage titles

The titles below are identical to the detailed headings and must remain synchronised if a stage is renamed.

| Stage | Title | Status |
|---|---|---|
| Phase 0 | Initial universe and numerical screening | COMPLETED — historical baseline |
| Step 1 | Validate the operating-company universe | IN PROGRESS |
| Step 2 | Resolve missing market data | NOT STARTED |
| Step 3 | Collect financial statements | NOT STARTED |
| Step 4 | Calculate financial health | NOT STARTED |
| Step 5 | Screen for financial resilience | NOT STARTED |
| Step 6 | Assess dilution | NOT STARTED |
| Step 7 | Identify 3–24-month catalysts | NOT STARTED |
| Step 8 | Shortlist 30–50 companies | NOT STARTED |
| Step 9 | Deep-research 15–20 companies | NOT STARTED |
| Step 10 | Value 5–10 finalists | NOT STARTED |
| Step 11 | Propose portfolio construction | NOT STARTED |
| Step 12 | Implement monitoring | NOT STARTED |

## Phase 0 — Initial universe and numerical screening [COMPLETED — historical baseline]

- **0.1 [COMPLETED]** Assemble initial ASX directory universe: 1, 923 securities (historical baseline).
- **0.2 [COMPLETED]** Apply preliminary numerical price, market-cap and liquidity criteria: 339 qualified (historical baseline).
- **0.3 [COMPLETED — PROVISIONAL]** Initial operating/investment-vehicle classification: 318 operating candidates, 20 excluded investment vehicles and 1 uncertain (historical classification, not independently validated).
- **0.4 [COMPLETED]** Upload working `operating_candidates.csv` to GitHub. Subsequent verification used **316 rows**, not 318. The difference is explained: GDF (Garda Property Group) and GDI (GDI Property Group) were removed as REIT/property investment vehicles; original workbook GICS labels both as Equity Real Estate Investment Trusts (REITs).

## Step 1 — Validate the operating-company universe [IN PROGRESS]

**Purpose:** Reconcile the working candidate count, confirm directory identity, examine trading-status exceptions and validate the business model and listing status before establishing the final universe.

- **1.1 [COMPLETED] Directory identity check**
   - **1.1.1 [COMPLETED]** Obtain and upload `ASXListedCompanies.csv` from the ASX directory.
   - **1.1.2 [COMPLETED]** Compare the 316 working candidates with the uploaded directory: 316 ticker/name matches, zero missing tickers and zero name mismatches.
   - **Limitation:** Directory membership does not confirm that shares are presently tradeable.

- **1.2 [IN PROGRESS] Trading-status verification**
   - **1.2.1 [COMPLETED]** Test Yahoo Finance price-history retrieval on 10 candidates.
   - **1.2.2 [COMPLETED]** Run preliminary scan of 316 candidates: 306 recent price dates and 10 requiring review; no missing/error results. Calendar-day thresholds are screening heuristics only.
   - **1.2.3 [COMPLETED — HEADLINE REVIEW]** Review ASX announcement histories for all 10 exceptions: 3DA, BSA, EWC, GWR, MRD, PAR, REC, SFM, SGI and TM1.
   - **1.2.4 [COMPLETED]** Read official trading-halt PDFs for 3DA, MRD, REC and TM1. Recorded reasons and scheduled halt end dates (14 October for TM1; 15 October for 3DA, MRD and REC). Scheduled end dates do **not** prove trading resumed.
   - **1.2.5 [COMPLETED]** Save 10 individual GitHub review records and the consolidated CSV: [trading-status verification register](research/trading_status/trading_status_verification_register_2026-10-13.csv).
   - **1.2.6 [BLOCKED / NEEDS VERIFICATION]** Confirm subsequent trading resumption for 3DA, MRD, REC and TM1; verify PAR's continuing suspension/administration from underlying notices and subsequent disclosures; verify live status of BSA, EWC, GWR, SFM and SGI. Do not classify the latter five as definitively actively trading on announcement-headline evidence alone.
   - **Interim classification as of review:** four trading halts (3DA, MRD, REC, TM1); one suspended/in voluntary administration (PAR); one historical suspension followed by reinstatement (BSA); four with no current suspension found in supplied headlines (EWC, GWR, SFM, SGI). PAR is excluded from the **currently tradeable shortlist**, not automatically deleted from the historical research universe.

- **1.3 [IN PROGRESS] Reconcile the universe and validate operating-company classification**
   - **1.3.1 [COMPLETED]** Reconciled the historical **318** provisional operating candidates with **316** working candidates using uploaded `ASX_Operating_Company_Classification.xlsx`: **GDF (Garda Property Group)** and **GDI (GDI Property Group)** were excluded because both are classified as Equity Real Estate Investment Trusts (REITs) in the source workbook. **318 − 2 = 316**. This explains the count difference; broader business-model review remains outstanding.
   - **1.3.2 [IN PROGRESS]** Check duplicates, ticker changes, delistings and corporate actions affecting identity.
     - **1.3.2.1 [COMPLETED] Duplicate audit:** 316 records, 316 unique tickers; no exact/normalised duplicate names; four fuzzy-name pairs identified. [Duplicate audit](research/STEP_1_3_2_DUPLICATE_AUDIT.md).
     - **1.3.2.2 [COMPLETED] Fuzzy-name resolution:** Four fuzzy-name pairs independently established as distinct legal entities and retained.
     - **1.3.2.3 [COMPLETED — DEFINED SCOPE] Ticker/name-change register:** 2018–13 October 2026 ticker/name-change register: 111 matched historical events (64 ticker changes, 41 name-only, six historic code collisions). [Ticker-change register](research/STEP_1_3_2_TICKER_CHANGE_REGISTER.md). This does not certify every issuer's full legal lineage.
     - **1.3.2.4 [IN PROGRESS — EVIDENCE CLOSURE] Issuer identity and historical continuity:** All **279** remaining issuer records have been triaged: **13 P1, 46 P2 and 220 P3**; the other **37** are covered by the separate name-continuity review. All **220/220 P3** have initial triage, but initial triage **does not** constitute independent primary-source verification. A [316-company evidence matrix](research/STEP_1_3_2_EVIDENCE_MATRIX.csv) and [methodology](research/STEP_1_3_2_EVIDENCE_MATRIX_README.md) now track evidence and gaps. Many records still require issuer-specific primary filings, ACN/ARBN and security-class checks, and historical continuity review. [Issuer continuity queue](research/STEP_1_3_2_ISSUER_CONTINUITY_QUEUE.md).
     - **1.3.2.5 [IN PROGRESS — EXCEPTIONS DOCUMENTED] Corporate actions:** [Corporate-action exception register](research/STEP_1_3_2_CORPORATE_ACTION_EXCEPTIONS.md) records material mergers, demergers, ticker reuse, consolidations, CDIs and acquisition events. AIH's Matrix acquisition is documented as completed in July 2026; IXR, ALU, ECT, SXL, WJL, SLD and other exceptions have specific treatment flags. Comprehensive 316-issuer action reconciliation and completion/implementation evidence remain outstanding.
     - **1.3.2.6 [IN PROGRESS — SELECTED CASES ONLY] Delisting/relisting review:** Selected ASX notices reviewed, including TNC's former Duke Exploration identity, October 2024 administration/suspension and January 2026 placement settlement activity. This is **not** an exhaustive delisting/relisting audit; dates of reinstatement and present trading status remain subject to separate Step 1.2 evidence.
     - **1.3.2.4 progress update (13 Oct 2026):** Four additional primary issuer identity confirmations (AX1, ALC, ATH, AMA), bringing the evidence-recorded total to **41/316**. [Primary verification report](research/STEP_1_3_2_4_PRIMARY_VERIFICATION_2026_10_13.md). Historical continuity remains pending; identity confirmation alone is not full Step 1.3.2.4 sign-off.
     - **1.3.2.4 further progress (13 Oct 2026):** Six primary ASX issuer identity confirmations (ACW, AVM, ALR, ASL, ASG, BET) bring the total to **47/316**. [Batch evidence report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_D.md). Identity-only verification; legal lineage and security-class reconciliation still open.
     - **1.3.2.4 further progress (13 Oct 2026, batch E):** Three primary issuer identity confirmations (ACE, ADH, BGD) bring evidence-recorded total to **50/316**. [Batch E report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_E.md). Full historical continuity/security-class checks remain outstanding.
     - **1.3.2.4 progress (13 Oct 2026, CEH and EMV):** Two more issuer identities corroborated from primary ASX filings, bringing total to **52/316**. Full historical continuity and security-form sign-off remains outstanding.
     - **1.3.2.4 progress (13 Oct 2026, batch F):** Primary ASX records confirm CRN's 10:1 CDI structure, ISIN and ARBN and BBN's 2015 listing identity; **54/316** primary issuer identities have evidence recorded. [Batch F report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_F.md). Complete historical continuity remains open.
     - **1.3.2.4 progress (13 Oct 2026, batch G):** SNX, TM1 and WJL corroborated with ASX primary documents; issuer identity evidence now **57/316**. SNX 1:1 CDI structure and TM1 ordinary fully paid securities recorded; historical lineage remains pending. [Batch G report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_G.md).
     - **1.3.2.4 progress (13 Oct 2026, batch H):** Primary ASX filings verified AZY, AR9, NYR and LDX; **61/316** primary issuer identities have evidence recorded. [Batch H report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_H.md). Complete historical continuity remains open.
     - **1.3.2.4 progress (13 Oct 2026, batch I):** MYR, JGH and GEM issuer identity corroborated from primary ASX filings; **64/316** identities now have primary evidence recorded. MYR 2009 admission and ISIN recorded. [Batch I report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_I.md). Full continuity sign-off pending.
     - **1.3.2.4 progress (13 Oct 2026, batch J):** MVF and EL8 identity corroborated from ASX issuer filings; **66/316** identity evidence recorded. EL8 conflicting ABN prefixes in issuer ASX documents remain a legal-identity exception pending ABR/ASIC check. [Batch J report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_J.md).
     - **1.3.2.4 progress (13 Oct 2026, batch K):** SFM, REC and BSA issuer identities corroborated from primary ASX records; **69/316** primary identity evidence recorded. REC historic ticker reuse and BSA current trading status remain unresolved. [Batch K report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_K.md).
     - **1.3.2.4 progress (13 Oct 2026, batch L):** BLX and MM8 verified against primary ASX filings, including ordinary fully paid share-class evidence; **71/316** identities recorded. [Batch L report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_L.md). Historical continuity remains open.
     - **1.3.2.4 progress (13 Oct 2026, batch M):** BFG issuer and ordinary fully paid security verified from ASX filings; corrected prior incorrect BFG ABN to **59 083 194 763**. **72/316** identities recorded. [Batch M report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_M.md).
     - **1.3.2.4 progress (13 Oct 2026, batch N):** GLN and ENR verified from ASX primary filings; GLN actual versus proposed allotments distinguished and ENR 2004 incorporation/2005 public conversion recorded. **74/316** identity evidence recorded. [Batch N report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_N.md).
     - **1.3.2.4 progress (13 Oct 2026, batch O):** HUM issuer identity confirmed from primary ASX filings, ACN 122 574 583; conditional Credit Corp proposal must not be treated as completed acquisition. **75/316** identity evidence recorded. [Batch O report](research/STEP_1_3_2_4_VERIFICATION_BATCH_2026_10_13_O.md).
     - **1.3.2.7 [COMPLETED — INVENTORY ONLY, 13 Oct 2026] Outstanding-evidence gap audit:** Reconciled all 316 matrix records: **75** have primary identity evidence recorded; **241** still require primary identity closure (**173 primary source pending, 31 evidence recorded/review required, 37 separate name-history reviews**). The original 279-row snapshot documents next evidence gates in the [279-company gap audit](research/STEP_1_3_2_ALL_REMAINING_GAP_AUDIT_2026_10_13.md). This is a full outstanding-work inventory, **not** 279 completed primary-source verifications or 2.4–2.5 sign-off.
     - **1.3.2 exit criteria [NOT MET]:** Per-company auditable issuer identity, historical continuity and security form; reconciled material corporate actions and delisting history; unresolved exceptions explicitly documented or quarantined. The **316 candidates remain provisional**, not fully verified.

   - **1.3.3 [NOT STARTED]** Validate operating-business versus investment-vehicle classification using current company activities and official reports. Specifically review GWR's business model.
   - **1.3.4 [NOT STARTED]** Produce an auditable final candidate register with inclusion/exclusion reasons and source dates.

- **1.4 [NOT STARTED] Step 1 sign-off**
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

- **11.1 [NOT STARTED]** Assess liquidity, sizing and diversification for a portfolio under A$10, 000.
- **11.2 [NOT STARTED]** Define entry criteria, thesis-invalidating events and exits.
- **11.3 [NOT STARTED]** Document portfolio risks; do not assume high returns are likely.

## Step 12 — Implement monitoring [NOT STARTED]

- **12.1 [NOT STARTED]** Design GitHub Actions refreshes with persistent checkpoints.
- **12.2 [NOT STARTED]** Monitor ASX announcements, capital raisings and trading-status changes.
- **12.3 [NOT STARTED]** Track financial/catalyst updates and thesis changes.
- **12.4 [NOT STARTED]** Test alerts and establish a review cadence.

## Immediate next action

**Step 1.3.2.4–1.3.2.6:** Work through the [316-company evidence matrix](research/STEP_1_3_2_EVIDENCE_MATRIX.csv), obtaining dated primary ASX/issuer evidence for outstanding identity and security-form checks; reconcile implemented corporate actions and historical delisting/relisting events; document any unresolved cases. Update the matrix only when the supporting evidence is inspected. Then undertake **1.3.3** operating-business classification and **1.3.4** final auditable candidate register. Keep **1.2.6** trading-status verification open separately until resumption and suspension statuses are confirmed.

## Research controls

- Keep raw source files, evidence dates and original outputs.
- Separate **verified facts**, **headline-only observations**, **provisional classifications** and **unresolved questions**.
- Never equate missing data with zero or a stale price date with a trading suspension.
- Reconcile corporate actions and shares on issue before valuation.
- Update statuses only when supporting deliverables exist; review and sign off each stage before moving to the next.


## Step 1.3.2.4 — Population primary review, 14 October 2026

**STILL IN PROGRESS.** Research cutoff: 13 October 2026. All 316 candidates retained. Fully verified: 0; partially verified: 316; unresolved legal-name outcome: 0; records with open issues: 316; manual-review flags:  46. Population coverage is not full historical/security/trading sign-off. The earlier 75 identity-evidence count is a baseline, not a fully verified count.

- [Complete population register](research/STEP_1_3_2_4_COMPLETE_VERIFICATION_REGISTER.csv)
- [Comprehensive report and acceptance limitations](research/STEP_1_3_2_4_COMPREHENSIVE_VERIFICATION_REPORT.md)
- [Precise remaining queue](research/STEP_1_3_2_4_UNRESOLVED_EXCEPTIONS.csv)
- [Primary assertion ledger](research/STEP_1_3_2_4_PRIMARY_EVIDENCE_LEDGER.csv)
- [Identifier arithmetic QA](research/STEP_1_3_2_4_IDENTIFIER_QA.csv)

Valid prior research preserved. The interrupted run hit a usage limit; recovered work is now checkpointed and consolidated. Remaining historical archives, security/capital-action reconciliation and latest trading-status evidence are unfinished research, not automatically accepted irreducible exceptions.


## Primary identity batch of 20 — 14 October 2026

Freshly inspected primary issuer/ASX documents and ABR records for AIH, ALU, ANX, AON, APX, ARD, A1N, ALA, AMD, AS1, A11, AKN, AEE, AWJ, AUE, AHC, AUZ, AVL, BM1, BAS. All 20 moved from PRIMARY_SOURCE_PENDING to PRIMARY_ISSUER_IDENTITY_CONFIRMED with explicit limited scope and remaining gaps. Primary-source pending: 173 → 153. Primary identity-evidence count: 75 → 95. All 316 retained; fully verified: 0. Overall Step 1.3.2.4 remains IN PROGRESS.

[Batch report](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14.md) · [Batch source register](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14.csv). The earlier population publication accidentally retained PRIMARY_SOURCE_PENDING statuses; this commit reconciles only these 20 freshly rechecked rows, preserving the remaining 153 as pending.


## Primary identity batch B — next 20, 14 October 2026

Fresh primary verification completed for BVR, BKY, BWN, BPM, BRK, CRS, CMA, CNB, CCV, CPN, CXU, CTM, CAF, CTS, CTT, CBE, COD, COI, DAL, EDE. All 20 selected rows now PRIMARY_ISSUER_IDENTITY_CONFIRMED with remaining country/history/security/trading gaps explicitly open. Primary-source pending 153 → 133; recorded primary identity evidence 95 → 115. 316 candidates retained. No full Step 1.3.2.4 sign-off. CCV cover/parent-versus-subsidiary ABN discrepancy newly documented; CMA, CTS, BWN registry discrepancies retained; DAL missing ABN recovered.

[Batch B report](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_B.md) · [Batch B source register](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_B.csv). Current manual-review flags: 47; ledger assertions: 905. Only the 20 selected matrix rows changed; other 296 preserved.


## Primary identity batch C — next 20, 14 October 2026

Fresh source-supported name/ticker/identifier evidence recorded for EDU, ELT, EMP, EQU, EVZ, FMR, FML, FHE, GML, GL1, GHY, GHM, GRR, GBR, GW1, HMG, HMX, HAV, HTM, IFN. Pending 133 → 113; recorded primary identity evidence 115 → 135. All 316 candidates retained. Country/history/security/trading gaps remain explicit; Step 1.3.2.4 remains IN PROGRESS. Manual-review flags: 50; source assertions: 967.

[Batch C report](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_C.md) · [Batch C register](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_C.csv). Exactly 20 matrix rows changed; other 296 preserved.


## Primary identity batch D — next 20, 14 October 2026

Fresh source-supported name/ticker/identifier evidence recorded for INN, IMB, IVZ, JLL, KAU, KZR, KAO, KGL, KLI, KSL, KRR, KME, KTK, LKE, LRV, LMG, LFT, LML, LAU, LNQ. Pending 113 → 93; recorded primary identity evidence 135 → 155. All 316 candidates retained. Country/history/security/trading gaps remain explicit; Step 1.3.2.4 remains IN PROGRESS. Manual-review flags: 54; source assertions: 1029.

[Batch D report](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_D.md) · [Batch D register](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_D.csv). Exactly 20 matrix rows changed; other 296 preserved.


## Primary identity batch E — next 20, 14 October 2026

Fresh source-supported name/ticker/identifier evidence recorded for LKY, LOT, LTP, LM8, M24, MKR, MPK, MEU, MMA, MMI, MX1, MM1, MNB, MSV, MLG, MXO, NYM, NTI, NOL, NMD. Pending 93 → 73; recorded primary identity evidence 155 → 175. All 316 candidates retained. Country/history/security/trading gaps remain explicit; Step 1.3.2.4 remains IN PROGRESS. Manual-review flags: 57; source assertions: 1094.

[Batch E report](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_E.md) · [Batch E register](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_E.csv). Exactly 20 matrix rows changed; other 296 preserved.


## Primary identity batch F — next 20, 14 October 2026

Fresh source-supported name/ticker/identifier evidence recorded for NTU, NOU, NVX, OD6, OFX, OMA, OBL, PGC, PC2, PEN, PVT, PLT, PVE, POL, PPS, PTX, PSC, QML, RZI, RNU. Pending 73 → 53; recorded primary identity evidence 175 → 195. All 316 candidates retained. Country/history/security/trading gaps remain explicit; Step 1.3.2.4 remains IN PROGRESS. Manual-review flags: 63; source assertions: 1159.

[Batch F report](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_F.md) · [Batch F register](research/STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_F.csv). Exactly 20 matrix rows changed; other 296 preserved.
