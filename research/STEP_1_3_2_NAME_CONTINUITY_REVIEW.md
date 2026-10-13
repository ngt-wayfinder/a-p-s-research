# Step 1.3.2 — Action 2.3: Company-name and issuer continuity review

**Research date:** 13 October 2026  
**Status:** IN PROGRESS — historical-register cohort reconciled; all-issuer independent validation outstanding.

## Scope and method

Reviewed the **37 unique present candidate codes** identified from the name-only change histories in the ASX 2018–2026 register and the previously investigated WRK name/parent-identity discrepancy. Checked every code's presence and present company name in the repository's actual `operating_candidates.csv` (316 records). Compared those names with the latest known company identities in `STEP_1_3_2_TICKER_CHANGE_REGISTER.md`. The register was primarily transcribed by the user; this is **not** a fresh independent verification of all 316 issuers or of current ASX trading status.

## Reconciled candidate codes and CSV names

| Current ticker | Current CSV name |
|---|---|
| MHC | MANHATTAN GOLD CORPORATION LIMITED |
| 3DA | AMAERO INC. |
| MTM | METALLIUM LIMITED |
| RMI | RESOURCE MINERALS INTERNATIONAL LTD |
| IVR | INVESTIGATOR SILVER LIMITED |
| MGX | MGX RESOURCES LIMITED |
| OCN | OCEANA METALS LIMITED |
| RAC | RACURA ONCOLOGY LTD |
| G50 | G50 CORP LIMITED |
| MYE | MASTERMYNE GROUP LIMITED |
| SGI | STEALTH GROUP HOLDINGS LTD |
| ACF | ACROW LIMITED |
| SHN | SUNSHINE METALS LIMITED |
| CEL | CHALLENGER GOLD LIMITED |
| CUP | COUNT LIMITED |
| EVO | EMBARK EARLY EDUCATION LIMITED |
| CY5 | CYGNUS METALS LIMITED |
| MEK | MEEKA METALS LIMITED |
| PNN | POWER MINERALS LIMITED |
| TSO | TESORO GOLD LTD |
| AAR | ASTRAL RESOURCES NL |
| KMD | KMD BRANDS LIMITED |
| PPE | PEOPLEIN LIMITED |
| EZL | EUROZ HARTLEYS GROUP LIMITED |
| CVN | CARNARVON ENERGY LIMITED |
| MXI | MAXIPARTS LIMITED |
| AIM | AI-MEDIA TECHNOLOGIES LIMITED |
| ODY | ODYSSEY GOLD LTD |
| CHN | CHALICE MINING LIMITED |
| COG | COG FINANCIAL SERVICES LIMITED |
| EMD | EMYRIA LIMITED |
| ADO | ANTEOTECH LTD |
| AXE | ARCHER MATERIALS LIMITED |
| DXN | DXN LIMITED |
| EXR | ELIXIR ENERGY LIMITED |
| HLS | HEALIUS LIMITED |
| WRK | WRKR LTD |

**Outcome:** 37/37 codes present; 0 absent. No conflicting latest names detected within the reviewed historical-register cohort. No CSV modifications required on this evidence.

## Continuity qualifications

1. **EVO** — Embark Early Education Limited became the new Australian listed parent in a 2023 scheme. Record corporate succession, not a mere rename.
2. **3DA** — Amaero Inc. became the US parent in a 2026 re-domiciliation; ASX CDI/security details changed. Do not blindly stitch price/share-count data.
3. **WRK** — 2021 source transcription gives 'mrkr Ltd', while the current issuer is WRKR LTD. Current identity was reviewed in the ticker register; preserve the historic spelling inconsistency for any future source recheck.
4. **MYE, MTM, PNN, EVO** — multiple historical names per unchanged ticker; use effective-date ranges for name-based joins.
5. **Historical ticker reuse** — VAL, COF, ASL, ARX, AR1 and ALR remain explicit exclusion joins for unrelated predecessors.

## Outstanding Action 2.3 requirements

- Review the remaining **279 candidate codes** for issuer-name continuity, mergers, scheme substitutions and undocumented changes using issuer/ASX primary evidence, rather than assuming absence from the name-change register proves unchanged identity.
- Resolve any issuer-specific name differences with dated primary announcements, not fuzzy text matching.
- Keep Action 2.3 **IN PROGRESS** until the full cohort has been checked; do not mark overall Step 1.3.2 complete.
- Actions 2.4–2.5 (mergers, delistings and other identity-changing corporate actions) and Step 1.2 trading-status checks remain separate outstanding work.

**Primary register:** [Historical ticker-change register](STEP_1_3_2_TICKER_CHANGE_REGISTER.md).  
**ASX source index:** https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes.html
