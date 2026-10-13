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

## 2022 register supplied by user — full 2022-section cross-match (13 October 2026)

**Source:** User-transcribed ASX 2022 company name/code-change register. Matched both old and new ticker columns to actual `operating_candidates.csv`. Transcription not independently authenticated against the ASX website.

**Result:** 12 matching entries: **6 historical code changes into candidate tickers** and **6 name-only changes**.

### Historical code changes (6)

| Effective date | Old code | New candidate code | New company at change |
|---|---|---|---|
| 12 Dec 2022 | MNY | SVR | Solvar Limited |
| 29 Nov 2022 | RFR | PVT | Pivotal Metals Limited |
| 24 Nov 2022 | 1VG | VTM | Victory Metals Limited |
| 10 Nov 2022 | GGG | ETM | Energy Transition Minerals Ltd |
| 15 Jun 2022 | PAK | AVM | Advance Metals Limited |
| 9 Feb 2022 | SUP | FHE | Frontier Energy Limited |

### Name-only changes (6)

| Effective date | Code | Old name | New name at change |
|---|---|---|---|
| 20 Oct 2022 | EVO | Evolve Education Group Limited | Embark Education Limited |
| 20 Jul 2022 | MEK | Meeka Gold Limited | Meeka Metals Limited |
| 17 Jun 2022 | PNN | Pepinnini Minerals Limited | Power Minerals Limited |
| 2 May 2022 | TSO | Tesoro Resources Limited | Tesoro Gold Ltd |
| 2 May 2022 | AAR | Anglo Australian Resources NL | Astral Resources NL |
| 18 Mar 2022 | KMD | Kathmandu Holdings Limited | KMD Brands Limited |

### Multi-year identity chains / further checks

- **EVO**: Evolve Education Group → Embark Education (2022) → Embark Education Group (2023); candidate CSV lists Embark Early Education. Verify later name history.
- **TM1**: The 2022 register contains PNL (Paringa Resources) → GCX (GCX Metals), and the 2024 register contains GCX → TM1 (Terra Metals). The 2022 event is **not** one of the 12 direct matches because neither PNL nor GCX is a current candidate ticker; nevertheless, preserve the historical chain `PNL → GCX → TM1`.
- **AAR**: 2022 name change is consistent with separate-entity identity verification against AS1.
- **No candidate exclusions** or changes to `operating_candidates.csv`.

**Next:** Reconcile the 2021 ASX change register. Stage 2.2 remains **IN PROGRESS**.

## 2021 register supplied by user — full 2021-section cross-match (13 October 2026)

**Source:** User-transcribed ASX 2021 name/code-change register. Matched old and new ticker columns to the 316-code `operating_candidates.csv` from GitHub. Source transcription not independently authenticated.

**Result:** 18 matching change events: **12 historical code changes** into current candidate tickers and **6 name-only changes**. No candidate exclusions.

### Historical ticker changes (12)

| Date | Old | Candidate code | Company at change |
|---|---|---|---|
| 17 Dec 2021 | TPS | IMB | Intelligent Monitoring Group |
| 15 Dec 2021 | UCW | EDU | EDU Holdings |
| 8 Dec 2021 | HWH | EIQ | EchoIQ |
| 6 Dec 2021 | VIC | JAV | Javelin Minerals |
| 1 Dec 2021 | LCD | MEK | Meeka Gold |
| 30 Nov 2021 | IP1 | WRK | mrkr |
| 30 Nov 2021 | FNP | NOU | Noumi |
| 25 Oct 2021 | SUD | ALA | Arovella Therapeutics |
| 30 Sep 2021 | HGM | JGH | Jade Gas Holdings |
| 29 Jul 2021 | BSM | GW1 | Greenwing Resources |
| 8 Jun 2021 | MEY | EL8 | Elevate Uranium |
| 12 Jan 2021 | PMY | BML | Boab Metals |

### Name-only changes (6)

| Date | Code | Old name | New name at change |
|---|---|---|---|
| 16 Dec 2021 | PPE | People Infrastructure | Peoplein |
| 25 Nov 2021 | EZL | Euroz | Euroz Hartleys Group |
| 18 Nov 2021 | CVN | Carnarvon Petroleum | Carnarvon Energy |
| 17 Nov 2021 | MYE | Mastermyne Group | Metarock Group |
| 17 Sep 2021 | MXI | MaxiTRANS Industries | MaxiPARTS |
| 6 Jul 2021 | AIM | Access Innovation Holdings | Ai-Media Technologies |

### Multi-year history notes

- **MEK:** LCD (Latitude Consolidated) → MEK (Meeka Gold) in 2021; MEK name change to Meeka Metals in 2022.
- **MYE:** Mastermyne Group → Metarock Group (2021), reverting to Mastermyne Group in 2024; ticker MYE unchanged.
- **WRK:** Historical change from IP1 to WRK (named 'mrkr Ltd' in 2021 register); current CSV name 'WRKR LTD'. Verify subsequent name history as needed.
- **No candidate exclusions** or edits to `operating_candidates.csv`.

**Next:** Reconcile the 2020 ASX change register. Stage 2.2 remains **IN PROGRESS**.

## 2020 register supplied by user — full 2020-section cross-match (13 October 2026)

**Source:** User-transcribed ASX 2020 company name/code-change register. Matched both old and new ticker columns against the actual 316-code `operating_candidates.csv`. The source transcription has not been independently authenticated against ASX.

**Result: 18 matched entries — 12 historical code changes into current candidates, 5 name-only changes, and 1 historical code collision (COF).** No candidate exclusions.

### Historical ticker changes (12)

| Effective date | Old code | Current candidate code | Company at change |
|---|---|---|---|
| 10 Dec 2020 | LCM | VBC | Verbrec Limited |
| 1 Dec 2020 | PEL | SHN | Sunshine Gold Limited |
| 30 Nov 2020 | FXL | HUM | Humm Group Limited |
| 27 Nov 2020 | AZV | AHC | Austco Healthcare Limited |
| 12 Nov 2020 | XTD | MXO | Motio Ltd |
| 21 Oct 2020 | ARM | ANX | Anax Metals Limited |
| 19 Aug 2020 | AYR | STK | Strickland Metals Limited |
| 23 Jul 2020 | FRN | WC8 | Wildcat Resources Limited |
| 2 Jul 2020 | BPL | ARR | American Rare Earths Limited |
| 3 Apr 2020 | IMF | OBL | Omni Bridgeway Limited |
| 24 Mar 2020 | OVL | IXR | Ionic Rare Earths Limited |
| 3 Feb 2020 | PKA | TSO | Tesoro Resources Limited |

### Name-only changes (5)

| Effective date | Code | Old name | New name at change |
|---|---|---|---|
| 30 Dec 2020 | ODY | Odyssey Energy Limited | Odyssey Gold Ltd |
| 9 Dec 2020 | CHN | Chalice Gold Mines Limited | Chalice Mining Limited |
| 18 Nov 2020 | COG | Consolidated Operations Group Limited | COG Financial Services Limited |
| 25 Sep 2020 | EMD | Emerald Clinics Limited | Emyria Limited |
| 11 Sep 2020 | PNN | PepinNini Lithium Limited | PepinNini Minerals Limited |

### Historical code collision (1)

| Effective date | Old code | New code | Historic issuer | Current candidate | Decision |
|---|---|---|---|---|---|
| 10 Feb 2020 | CMA | COF | Centuria Metropolitan REIT → Centuria Office REIT | COF = Carma Limited | **Different issuer; do not link historical Centuria REIT data to Carma** |

**Multi-year notes:** PEL → SHN (2020) followed by Sunshine Gold → Sunshine Metals name change (2023); PKA → TSO (2020) followed by Tesoro Resources → Tesoro Gold (2022); PNN name changes in 2020 and 2022. A separate 2024 code collision was recorded for VAL.

**Next:** Reconcile the 2019 ASX change register. Stage 2.2 remains **IN PROGRESS**.

## 2019 register supplied by user — full 2019-section cross-match (13 October 2026)

**Source:** User-transcribed 2019 ASX company name/code-change register. Matched both old and new code columns to the actual 316-code `operating_candidates.csv` in GitHub. Transcription not independently authenticated against ASX.

**Result: 14 matching events — 7 ticker changes into candidate codes, 5 name-only changes, and 2 historical ticker collisions.** No candidate exclusions.

### Historical code changes into candidate tickers (7)

| Effective date | Old code | Candidate code | New name at change |
|---|---|---|---|
| 29 Nov 2019 | N27 | RML | Resolution Minerals Ltd |
| 27 Sep 2019 | HCO | LOT | Lotus Resources Limited |
| 30 Jul 2019 | TNO | VR8 | Vanadium Resources Limited |
| 26 Jun 2019 | TBH | BET | Betmakers Technology Group Ltd |
| 20 Jun 2019 | PGS | SKY | Sky Metals Limited |
| 13 May 2019 | BMT | CNB | Carnaby Resources Limited |
| 12 Apr 2019 | PBT | ATH | Alterity Therapeutics Limited |

### Name-only changes (5)

| Effective date | Code | Old name | New name |
|---|---|---|---|
| 15 Nov 2019 | ADO | Anteo Diagnostics Limited | AnteoTech Ltd |
| 5 Nov 2019 | AXE | Archer Exploration Limited | Archer Materials Limited |
| 26 Jul 2019 | DXN | The Data Exchange Network Limited | DXN Limited |
| 4 Jun 2019 | EXR | Elixir Petroleum Limited | Elixir Energy Limited |
| 13 May 2019 | CEL | Challenger Energy Limited | Challenger Exploration Limited |

### Historical ticker collisions (2)

| Effective date | Historical code change | Current candidate code/name | Decision |
|---|---|---|---|
| 25 Oct 2019 | ASL (Ausdrill Limited) → PRN (Perenti Global Limited) | ASL = Andean Silver Limited | Do **not** join Ausdrill history to current ASL; the current issuer's MMC→ASL event occurred in 2024 |
| 26 Jun 2019 | ARX (Arc Exploration Limited) → CYM (Cyprium Metals Limited) | ARX = Aroa Biosurgery Limited | Do **not** join Arc Exploration history to current ARX |

**Additional notes:** CEL name changes again to Challenger Gold in 2023. 2019 old codes ASL and ARX are historical ticker collisions, not valid predecessors of the present candidate issuers. Earlier collisions recorded: VAL (2024), COF (2020).

**Next:** Reconcile the 2018 ASX change register. Stage 2.2 remains **IN PROGRESS**.

## 2018 register supplied by user — full 2018-section cross-match (13 October 2026)

**Source:** User-transcribed 2018 ASX name/code-change register; old/new codes matched against actual 316-code `operating_candidates.csv` in GitHub. Transcription not independently authenticated.

**Result: 13 matched events: 10 historical code changes into current candidate tickers, 1 name-only event, and 2 historical old-code collisions.** No candidate exclusions.

### Historical ticker changes (10)

| Date | Old code | Current candidate code | Company at change |
|---|---|---|---|
| 5 Dec 2018 | PRY | HLS | Healius Limited |
| 4 Dec 2018 | HOM | RMC | Resimac Group Ltd |
| 4 Dec 2018 | KRC | KRR | King River Resources Limited |
| 6 Nov 2018 | GSC | INR | Ioneer Ltd |
| 24 Sep 2018 | EMG | FEX | Fenix Resources Ltd |
| 15 Aug 2018 | DMI | GLN | Galan Lithium Limited |
| 9 Jul 2018 | ESI | ECT | Environmental Clean Technologies Limited |
| 21 Jun 2018 | IHS | IVZ | Invictus Energy Ltd |
| 29 Mar 2018 | NMG | ACF | Acrow Formwork and Construction Services Limited |
| 14 Mar 2018 | DM1 | WZR | Wisr Limited |

### Name-only change (1)

| Date | Code | Old name | New name |
|---|---|---|---|
| 14 Dec 2018 | HLS | Healius Ltd | Healius Limited |

### Historical old-code collisions (2)

| Date | Historic event | Current candidate | Interpretation |
|---|---|---|---|
| 17 Apr 2018 | AR1 (Arrowhead Resources Limited) → EM1 (Emerge Gaming Limited) | AR1 = Austral Resources Australia Ltd | Different issuer; do not associate historic Arrowhead data with Austral Resources |
| 12 Apr 2018 | ALR (Aberdeen Leaders Limited) → CLF (Concentrated Leaders Fund Limited) | ALR = Altair Minerals Limited | Different issuer; do not associate historic Aberdeen Leaders data with Altair Minerals |

### Stage 2.2 reconciliation summary, 2018–2026

| Year | Matched events | Ticker changes into candidates | Name-only changes | Historical ticker collisions |
|---|---:|---:|---:|---:|
| 2026 | 1 | 0 | 1 | 0 |
| 2025 | 8 | 1 | 7 | 0 |
| 2024 | 8 | 5 | 2 | 1 |
| 2023 | 19 | 11 | 8 | 0 |
| 2022 | 12 | 6 | 6 | 0 |
| 2021 | 18 | 12 | 6 | 0 |
| 2020 | 18 | 12 | 5 | 1 |
| 2019 | 14 | 7 | 5 | 2 |
| 2018 | 13 | 10 | 1 | 2 |
| **TOTAL** | **111** | **64** | **41** | **6** |

**Interpretation:** 111 matched *change events*, not necessarily 111 unique issuers. Six historic ticker collisions: VAL (2024), COF (2020), ASL and ARX (2019), AR1 and ALR (2018). The 316-company candidate universe remains unchanged.

**Outstanding quality checks before marking Stage 2.2 complete:** Verify current-issuer history for six code collisions; confirm name mismatches such as EVO and WRK; verify 2025 3DA name mismatch; consider chained changes not directly touching present candidate codes (e.g., PNL→GCX→TM1). User-supplied annual tables cover 2018–2026; not independently authenticated. Future-dated 2026 events must be excluded as of 13 Oct 2026.

## Stage 2.2 Action 3 — Six historical code collisions: issuer separation check (13 October 2026)

**Method:** Compare each dated historic ASX name/code change to the exact present candidate code and name in `operating_candidates.csv`. The official ASX historical register (https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes.html) corroborates the dated old/new issuer pairs. A matching ticker *alone* does not establish corporate continuity. This check establishes that the historic issuer is different from the candidate identified by the current CSV; it does **not** independently establish current live listing/trading status or the current issuer's full corporate history.

| Code reused | Historical event (ASX register) | Candidate in CSV | Conclusion |
|---|---|---|---|
| VAL | 9 Apr 2024: Valor Resources Limited (VAL) → Thunderbird Resources Limited (THB) | VAL — Valiant Gold Limited | **SEPARATE**: Valor/Thunderbird data must not be attributed to Valiant Gold |
| COF | 10 Feb 2020: Centuria Metropolitan REIT (CMA) → Centuria Office REIT (COF) | COF — Carma Limited | **SEPARATE**: Centuria REIT financials must not be attributed to Carma |
| ASL | 25 Oct 2019: Ausdrill Limited (ASL) → Perenti Global Limited (PRN) | ASL — Andean Silver Limited | **SEPARATE**: Ausdrill/Perenti data must not be attributed to Andean Silver; Andean's own MMC→ASL event is dated 11 Jul 2024 |
| ARX | 26 Jun 2019: Arc Exploration Limited (ARX) → Cyprium Metals Limited (CYM) | ARX — Aroa Biosurgery Limited | **SEPARATE**: Arc/Cyprium data must not be attributed to Aroa |
| AR1 | 17 Apr 2018: Arrowhead Resources Limited (AR1) → Emerge Gaming Limited (EM1) | AR1 — Austral Resources Australia Ltd | **SEPARATE**: Arrowhead/Emerge data must not be attributed to Austral Resources |
| ALR | 12 Apr 2018: Aberdeen Leaders Limited (ALR) → Concentrated Leaders Fund Limited (CLF) | ALR — Altair Minerals Limited | **SEPARATE**: Aberdeen/CLF data must not be attributed to Altair; Altair's own CHK→ALR event is dated 17 May 2024 |

### Additional primary issuer evidence

- **COF:** Centuria Office REIT's FY2020 financial statements expressly document the 10 Feb 2020 CMA→COF transition: https://www.asx.com.au/asxpdf/20200805/pdf/44l6gdgdpdd681.pdf
- **ARX:** Arc Exploration's 17 Jun 2019 ASX announcement confirms its proposed name/code change to Cyprium Metals/CYM: https://announcements.asx.com.au/asxpdf/20190617/pdf/445wkc0swmh9r9.pdf
- **ALR:** Concentrated Leaders Fund's ASX-filed company history confirms it previously traded as Aberdeen Leaders under ALR before changing to CLF in April 2018: https://announcements.asx.com.au/asxpdf/20200903/pdf/44m9r950skyrtm.pdf

### Disposition

**All six historical code collisions are resolved for the narrow purpose of historical issuer separation.** None is a duplicate within the present 316-code universe. **Retain all 316 candidates.** For historical financial-data joins, require issuer name and relevant date/corporate identity in addition to ticker; explicitly exclude these six old-issuer histories from corresponding current-candidate records.

**Remaining Stage 2.2 data-quality work (not covered by collision verification):** confirm current issuer continuity and any intervening names for EVO, WRK and 3DA; ensure chained historical aliases are preserved (e.g. PNL→GCX→TM1); confirm that future-dated 2026 entries were excluded from any as-of-13-Oct-2026 statistics. Do not claim the whole stage complete until those checks are addressed.

## Stage 2.2 Action 4 — EVO, WRK and 3DA issuer-name discrepancy review (13 October 2026)

**Method:** Compare the current `operating_candidates.csv` names with issuer/ASX announcements and corporate filings. Keep changes of *legal parent entity* separate from simple legal-name changes.

| Code | Current CSV name | Findings and effective events | Disposition |
|---|---|---|---|
| EVO | EMBARK EARLY EDUCATION LIMITED | Evolve Education Group Limited → Embark Education Limited (18 Oct 2022), then Embark Education Group Limited (10 Feb 2023), ticker EVO unchanged; 2023 scheme swapped shares 1:1 into newly incorporated Australian parent **Embark Early Education Limited**, admitted to ASX 27 Jun 2023. | **MATCH VERIFIED**; do not overwrite CSV; record 2023 parent substitution as corporate succession, not just name change |
| WRK | WRKR LTD | Integrated Payment Technologies Limited → WRK in 2021; ASX announcement titled *Change of Company Name and Amended Constitution* dated 25 Nov 2021 identifies wrkr Ltd. The supplied ASX 2021 register instead gives intermediate 'mrkr Ltd' at 30 Nov; inconsistency in the historic naming requires careful annotation, but same listed WRK code and present name are confirmed. | **CURRENT NAME VERIFIED**; no CSV edit; historical 'mrkr' transcription should not be silently treated as a distinct issuer |
| 3DA | AMAERO INC. | Amaero International Limited → Amaero Ltd, effective ASX 8 Apr 2025, ticker 3DA unchanged. In June 2026 court-approved scheme, US Delaware parent **Amaero Inc.** replaced the Australian parent and ASX trading continued through CDIs under 3DA; 22 Jun 2026 company announcement identifies Amaero Inc. (ASX:3DA). | **MATCH VERIFIED**; no CSV edit; preserve legal parent/ISIN/security type transition |

### Primary/source references

- EVO issuer's 2022 announcement: https://www.asx.com.au/asxpdf/20221003/pdf/45ftkwdr9yrmry.pdf
- EVO 2022 annual accounts showing the 2022 and Feb 2023 names: https://announcements.asx.com.au/asxpdf/20230301/pdf/45m633t7f7fmtw.pdf
- EVO 2023 report explicitly describing the Australian parent scheme and ASX admission: https://announcements.asx.com.au/asxpdf/20240227/pdf/060v93w4mhksq3.pdf
- WRK 25 Nov 2021 issuer announcement: https://www.marketindex.com.au/asx/wrk/announcements/change-of-company-name-and-amended-constitution-2A1341520
- WRK ASX announcement history: https://www.asx.com.au/asx/v2/statistics/announcements.do?asxCode=WRK&by=asxCode&period=M6&timeframe=D
- 3DA FY2025 annual report with 8 Apr 2025 name change: https://announcements.asx.com.au/asxpdf/20250818/pdf/06mzddnk2gylmw.pdf
- 3DA court-approved scheme effective June 2026: https://www.globenewswire.com/news-release/2026/06/11/3310566/0/en/Amaero-Re-domiciliation-Schemes-Become-Effective.html
- 3DA issuer announcement of completed re-domiciliation on 22 Jun 2026: https://www.marketindex.com.au/asx/3da/announcements/amaero-expands-powder-capacity-ahead-of-schedule-3A695692
- ASX 3DA issuer profile now lists AMAERO INC. and CHESS Depositary Interests: https://www.asx.com.au/markets/company/3DA

**Decision:** All three present CSV names are supported. No edits to `operating_candidates.csv`, no candidate exclusions. **Next remaining action:** Verify the multi-stage historical ticker chains and check as-of-date handling before closing Stage 2.2.
