# Step 1.3.2 — Stage 2.2: Historical ASX ticker-change verification (initial evidence register)

**Research date:** 13 October 2026  
**Status:** IN PROGRESS — initial historical cases identified; not a comprehensive check of all 316 issuers.

## Primary source

ASX official company name/code-change register (2018–2026): https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes.html

This register lists effective dates, old codes and names, and new codes and names. The cases below were identified from its published entries. A past code change is not evidence of a duplicate or delisting.

## Historical code changes relevant to the current 316-candidate universe

| Effective date (ASX register) | Old code | Candidate code | Old name | New name on change | Status |
|---|---|---|---|---|---|
| 22 Dec 2023 | GMR | AS1 | Golden Rim Resources Limited | Asara Resources Limited | Historical change, retain AS1 |
| 22 Dec 2023 | BBX | BCM | BBX Minerals Limited | Brazilian Critical Minerals Limited | Historical change, retain BCM |
| 18 Dec 2023 | ALG | CEH | Ardent Leisure Group Limited | Coast Entertainment Holdings Limited | Historical change, retain CEH |
| 1 Dec 2023 | JRL | JLL | Jindalee Resources Limited | Jindalee Lithium Limited | Historical change, retain JLL |
| 6 Jun 2023 | DEX | TNC | Duke Exploration Limited | True North Copper Limited | Historical change, retain TNC |
| 1 May 2023 | RDT | DLI | Red Dirt Metals Limited | Delta Lithium Limited | Historical change, retain DLI |
| 6 Mar 2023 | E2M | USL | E2 Metals Limited | Unico Silver Limited | Historical change, retain USL |
| 25 Jan 2023 | TNG | TVN | TNG Limited | Tivan Limited | Historical change, retain TVN |
| 17 Dec 2021 | TPS | IMB | Threat Protect Australia Limited | Intelligent Monitoring Group Limited | Historical change, retain IMB |
| 15 Dec 2021 | UCW | EDU | UCW Limited | EDU Holdings Limited | Historical change, retain EDU |
| 10 Dec 2020 | LCM | VBC | Logicamms Limited | Verbrec Limited | Historical change, retain VBC |
| 2 Jul 2020 | BPL | ARR | Broken Hill Prospecting Limited | American Rare Earths Limited | Historical change, retain ARR |
| 19 Jul 2019 | PGS | SKY | Planet Gas Limited | Sky Metals Limited | Historical change, retain SKY |
| 13 May 2019 | BMT | CNB | Berkut Minerals Limited | Carnaby Resources Limited | Historical change, retain CNB |
| 12 Apr 2019 | PBT | ATH | Prana Biotechnology Ltd | Alterity Therapeutics Limited | Historical change, retain ATH |

**Caution:** Historical company identities and codes can be reused; these entries only establish the listed change events. Each issuer's current code was separately matched to the uploaded ASX company directory in Step 1.1, but the directory snapshot is not proof of live tradeability.

## Name changes without a ticker change (separate from ticker-change count)

- **RAC:** Race Oncology Ltd → Racura Oncology Ltd, code RAC retained, 10 Dec 2025 (ASX register).
- **SHN:** Sunshine Gold Limited → Sunshine Metals Limited, code SHN retained, 10 Jul 2023.
- **AAR:** Anglo Australian Resources NL → Astral Resources NL, code AAR retained, 2 May 2022.
- **MGX:** Mount Gibson Iron Limited → MGX Resources Limited, code MGX retained, effective Dec 2025 (official company announcement, see [KGL/MGX identity check](identity_checks/KGL_MGX_2026-10-13.md)).

## Outstanding work

1. Systematically cross-match **all** entries of the official 2018–2026 ASX code-change register against the 316 candidate tickers, rather than relying on these initial manually extracted examples.
2. Review any changes predating 2018 separately where materially relevant.
3. Identify old ticker collisions with current candidate tickers, if any.
4. Confirm that every candidate's current ASX code is still valid as of the review date; a directory snapshot alone is insufficient.
5. Record source evidence and affected financial-data histories for each confirmed case.

**No candidate exclusions or edits to `operating_candidates.csv` have been made.**

## Full-universe cross-match status (13 October 2026)

**NOT COMPLETE / SOURCE ACCESS BLOCKED.** The official ASX code-change webpage is discoverable through web search, but attempts to retrieve the full page for programmatic parsing failed in this session. The 15 initial code-change entries above are **not** an exhaustive cross-match against 316 candidates. No unverified match totals are reported.

A reusable parser is now committed at [`scripts/crossmatch_asx_code_changes.py`](../scripts/crossmatch_asx_code_changes.py). It accepts a locally saved complete ASX code-change HTML page and `operating_candidates.csv`, and emits matched historical change events as CSV. It requires Beautiful Soup (`pip install beautifulsoup4`).

**Next input required:** a saved full HTML copy of https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes.html with all 2018–2026 year sections present. Before certifying completion, verify all year sections and ensure no rows were missed because of webpage layout. A browser's Save Page As → Webpage, HTML Only may provide the necessary input; dynamic content must be expanded first if applicable.

## 2026 register supplied by user — cross-match (13 October 2026)

**Source:** User-transcribed 2026 ASX company name/code-change register, 53 entries. This section records a comparison with the 316-code working universe; it does not independently authenticate the transcription against the ASX website.

- **Rows provided:** 53 (including the future-dated 15 Oct 2026 GLL → GSE entry).
- **Candidate matches by old or new code:** 1 unique company — **MHC**.
- **Candidate ticker-code changes:** **0**.
- **Candidate name-only changes:** **1**.

| Effective date | Old code | Old name | New code | New name | Classification | Decision |
|---|---|---|---|---|---|---|
| 16 Jan 2026 | MHC | Manhattan Corporation Limited | MHC | Manhattan Gold Corporation Limited | Name change; code unchanged | Retain MHC; CSV already uses new name |

**Caveats:** The 15 Oct 2026 entry is future-dated relative to the research date (13 Oct) and is not treated as an already-effective change. This match covers **only the 2026 entries supplied**, not 2018–2025 or any omissions from the supplied transcription. Other 2026 entries have no old/new ticker match to the 316 candidates.

**Next:** Obtain and cross-match the **2025** ASX change-register section, followed by earlier years. The full 2018–2026 historical audit remains **IN PROGRESS**.
