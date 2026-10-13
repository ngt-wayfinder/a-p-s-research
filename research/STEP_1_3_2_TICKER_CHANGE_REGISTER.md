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

## 2025 register supplied by user — cross-match (13 October 2026)

**Source:** User-transcribed 2025 ASX company name/code-change table. Entries were compared against the 316 candidate codes. This is a source-based reconciliation, not independent authentication of the transcription against ASX.

**Results:** 8 matching candidate tickers; **1 code change** (D2O → RIV) and **7 name-only changes**.

| Effective date | Old code | Old name | New code | New name | Change type | Candidate action |
|---|---|---|---|---|---|---|
| 8 Apr 2025 | 3DA | Amaero International Ltd | 3DA | Amaero Ltd | Name only | Retain 3DA; verify discrepancy with candidate CSV 'AMAERO INC.' |
| 28 Jul 2025 | MTM | MTM Critical Metals Limited | MTM | Metallium Limited | Name only | Retain |
| 7 Aug 2025 | RMI | Resource Mining Corporation Limited | RMI | Resource Minerals International Ltd | Name only | Retain |
| 15 Oct 2025 | D2O | Duxton Water Limited | RIV | Rivco Australia Ltd | **Code and name** | Retain RIV; link D2O historical price/announcement records |
| 2 Dec 2025 | IVR | Investigator Resources Ltd | IVR | Investigator Silver Limited | Name only | Retain |
| 4 Dec 2025 | MGX | Mount Gibson Iron Limited | MGX | MGX Resources Limited | Name only | Retain |
| 4 Dec 2025 | OCN | Oceana Lithium Limited | OCN | Oceana Metals Limited | Name only | Retain |
| 10 Dec 2025 | RAC | Race Oncology Ltd | RAC | Racura Oncology Ltd | Name only | Retain |

**Notes:** MGX and RAC were already mentioned in the initial illustrative register and are not additional unique matches. RIV is the one candidate requiring a historical ticker alias. A company-name mismatch between 3DA's CSV name and the 2025 table is a review item, not evidence of a duplicate. This is a **2025-section comparison only**; earlier years remain outstanding.

**Next:** Obtain and compare the 2024 ASX code/name-change register against the same 316 candidates.

## 2024 register supplied by user — cross-match (13 October 2026)

**Source:** User-transcribed 2024 ASX company name/code-change table. Cross-matched old and new ticker columns to the 316-candidate working universe. Not independently authenticated against the ASX site.

**Eight matched change events:** five historical code changes **into** current candidate codes, two name-only changes, and one **old-code collision** that must not be mistaken for a current candidate's corporate history.

| Effective date | Old code | Old name | New code | New name | Classification / action |
|---|---|---|---|---|---|
| 5 Jan 2024 | BAT | Battery Minerals Limited | WTM | Waratah Minerals Limited | Historical candidate ticker alias; retain WTM |
| 19 Apr 2024 | GCX | GCX Metals Limited | TM1 | Terra Metals Limited | Historical candidate ticker alias; retain TM1 |
| 17 May 2024 | CHK | Cohiba Minerals Limited | ALR | Altair Minerals Limited | Historical candidate ticker alias; retain ALR |
| 26 Jun 2024 | AFW | Applyflow Limited | FMR | FMR Resources Limited | Historical candidate ticker alias; retain FMR |
| 11 Jul 2024 | MMC | Mitre Mining Corporation Limited | ASL | Andean Silver Limited | Historical candidate ticker alias; retain ASL |
| 9 May 2024 | G50 | Gold 50 Limited | G50 | G50 Corp Limited | Name-only change; retain G50 |
| 4 Dec 2024 | MYE | Metarock Group Limited | MYE | Mastermyne Group Limited | Name-only change; retain MYE |
| 9 Apr 2024 | VAL | Valor Resources Limited | THB | Thunderbird Resources Limited | **Old-code collision:** current candidate VAL = Valiant Gold Limited; DO NOT assign Valor Resources history to Valiant Gold. Investigate reuse and effective start date |

**Important:** The 2024 table also includes code changes such as WEB → WEB (Webjet → Web Travel Group), but **WEB is not the candidate WJL** (Webjet Group Limited); do not match by company-name similarity alone. The supplied 2024 table includes two SGH entries for the same old code SVW on different dates; neither code is in our candidate universe.

**Data handling:** Historical aliases BAT→WTM, GCX→TM1, CHK→ALR, AFW→FMR, MMC→ASL should inform historical price/announcement retrieval. Old-code collisions like VAL require issuer identity checks before linking time series.

**Next:** Verify the VAL code-reuse issue and reconcile the 2023 annual register. Stage 2.2 remains in progress. No candidate removals.

## 2023 register supplied by user — full 2023-section cross-match (13 October 2026)

**Source:** User-transcribed ASX 2023 company name/code-change register. Matched **both** old and new codes against the actual 316-code `operating_candidates.csv` in GitHub. Transcription not independently authenticated against the ASX website.

**Result: 19 matching entries — 11 code changes and 8 name-only changes.** No candidate exclusions.

### Historical code changes (11)

| Effective date | Old code | New candidate code | New company at change |
|---|---|---|---|
| 22 Dec 2023 | GMR | AS1 | Asara Resources Limited |
| 22 Dec 2023 | BBX | BCM | Brazilian Critical Minerals Limited |
| 18 Dec 2023 | ALG | CEH | Coast Entertainment Holdings Limited |
| 1 Dec 2023 | JRL | JLL | Jindalee Lithium Limited |
| 15 Nov 2023 | SAU | ION | Iondrive Limited |
| 24 Oct 2023 | DC2 | AI1 | Adisyn Ltd |
| 6 Jun 2023 | DEX | TNC | True North Copper Limited |
| 22 May 2023 | HT1 | A1N | ARN Media Limited |
| 1 May 2023 | RDT | DLI | Delta Lithium Limited |
| 6 Mar 2023 | E2M | USL | Unico Silver Limited |
| 25 Jan 2023 | TNG | TVN | Tivan Limited |

### Name-only changes (8)

| Effective date | Code unchanged | Old name | New name at change |
|---|---|---|---|
| 30 Nov 2023 | SGI | Stealth Global Holdings Ltd | Stealth Group Holdings Ltd |
| 27 Nov 2023 | ACF | Acrow Formwork and Construction Services Limited | Acrow Limited |
| 10 Jul 2023 | SHN | Sunshine Gold Limited | Sunshine Metals Limited |
| 8 Jun 2023 | CEL | Challenger Exploration Limited | Challenger Gold Limited |
| 9 May 2023 | CUP | Countplus Limited | Count Limited |
| 1 May 2023 | MTM | Mt Monger Resources Limited | MTM Critical Metals Limited |
| 21 Feb 2023 | EVO | Embark Education Limited | Embark Education Group Limited |
| 14 Feb 2023 | CY5 | Cygnus Gold Limited | Cygnus Metals Limited |

### Identity/history notes

- **MTM**: a further name-only change in 2025 (MTM Critical Metals → Metallium); ticker unchanged.
- **EVO**: the 2023 destination name 'Embark Education Group Limited' differs from the candidate CSV name 'Embark Early Education Limited'. Confirm any intervening name change.
- Several 2023 events were already identified in the initial non-exhaustive register. Do not double-count these as independent events.
- The 2023 register also contains historical codes used by later entities (for example, TRT → TX3 and ARO → ASE), but neither of those codes is in the **current** candidate set, so they are excluded from the 19 matched events.

**Next:** Reconcile 2022. Stage 2.2 remains **IN PROGRESS**.
