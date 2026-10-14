# Primary issuer identity verification — batch B, next 20 pending companies

Review date: **14 October 2026**. Selected the next 20 PRIMARY_SOURCE_PENDING rows in live repository order, after the preceding 20 batch. Baseline commit is recorded in publication metadata.

## Outcome

**20/20 source-supported issuer-name/ticker/identifier conclusions.** All 20 move to PRIMARY_ISSUER_IDENTITY_CONFIRMED. This is a limited identity-evidence status, not full country/history/security/trading sign-off. Genuine report/registry conflicts remain explicit.

| Matrix measure | Before | After |
|---|---:|---:|
| PRIMARY_SOURCE_PENDING | 153 | 133 |
| Recorded primary identity evidence | 95 | 115 |
| Primary evidence partial review | 68 | 68 |
| Candidate rows | 316 | 316 |

Fresh official 2026 ASX archives, 35 issuer/ASX PDFs and 20 current ABR records were retrieved without failures. An additional ABR record was read to investigate CCV's conflicting cover identifier. 61 new source assertions are linked in the ledger. Earlier 2018/2021/2024 leads were replaced with recent 2026 issuer evidence for this batch.

## Company results

| ASX | Current issuer supported by primary source | ABN | Express ACN established in batch | Evidence IDs |
|---|---|---|---|---|
| BVR | BELLAVISTA RESOURCES LTD | 43655732246 | 655732246 | E00845, E00846, E00847 |
| BKY | BERKELEY ENERGIA LIMITED | 40052468569 | UNRESOLVED | E00848, E00849, E00850 |
| BWN | BHAGWAN MARINE LIMITED | 81009154349 | 009154349 | E00851, E00852, E00853 |
| BPM | BPM MINERALS LIMITED | 60644263516 | 644263516 | E00854, E00855, E00856 |
| BRK | BROOKSIDE ENERGY LIMITED | 15108787720 | UNRESOLVED | E00857, E00858, E00859 |
| CRS | CAPRICE RESOURCES LTD | 96624970725 | UNRESOLVED | E00860, E00861, E00862 |
| CMA | CARMA LIMITED | 20648091418 | 648091418 | E00863, E00864, E00865 |
| CNB | CARNABY RESOURCES LIMITED | 62610855064 | UNRESOLVED | E00866, E00867, E00868 |
| CCV | CASH CONVERTERS INTERNATIONAL LIMITED | 39069141546 | UNRESOLVED | E00869, E00870, E00871, E00872 |
| CPN | CASPIN RESOURCES LIMITED | 33641813587 | UNRESOLVED | E00873, E00874, E00875 |
| CXU | CAULDRON ENERGY LIMITED | 22102912783 | UNRESOLVED | E00876, E00877, E00878 |
| CTM | CENTAURUS METALS LIMITED | 40009468099 | UNRESOLVED | E00879, E00880, E00881 |
| CAF | CENTREPOINT ALLIANCE LIMITED | 72052507507 | 052507507 | E00882, E00883, E00884 |
| CTS | CERETAS LIMITED | 15681662224 | UNRESOLVED | E00885, E00886, E00887 |
| CTT | CETTIRE LIMITED | 75645474166 | UNRESOLVED | E00888, E00889, E00890 |
| CBE | COBRE LIMITED | 75626241067 | UNRESOLVED | E00891, E00892, E00893 |
| COD | CODA MINERALS LTD | 49625763957 | 625763957 | E00894, E00895, E00896 |
| COI | COMET RIDGE LIMITED | 47106092577 | UNRESOLVED | E00897, E00898, E00899 |
| DAL | DALAROO METALS LTD | 23648476699 | 648476699 | E00900, E00901, E00902 |
| EDE | EDEN INNOVATIONS LTD | 58109200900 | UNRESOLVED | E00903, E00904, E00905 |

## Material findings and retained exceptions

- **CCV:** FY2026 annual-report cover prints ABN 75 009 288 804 under Cash Converters International Limited. The body and ASX Appendix 2A support listed-parent ABN 39 069 141 546, corroborated by ABR. The cover was visually inspected. The other ABN is registered to Cash Converters Pty Ltd; report PDF page 32 calls that company a 100% owned subsidiary. Do not substitute subsidiary identity for parent identity; keep the misleading cover discrepancy for issuer clarification.
- **CMA:** ASX filing confirms Carma Limited ACN 648 091 418, while ABR still names ClickCar Holdings Pty Ltd. Annual-report PDF page 11 expressly states the FY2026 name change. Registry metadata/exact effective date remain open; current Carma must be segregated from unrelated historical Centuria CMA/COF.
- **CTS:** issuer report says Ceretas Limited while ABR says Ceretas Pty Ltd with the same ABN 15 681 662 224; registry name/type reconciliation stays open.
- **BWN:** issuer/ASX documentation identifies Bhagwan Marine Limited, but ABR entity type remains Australian Private Company. The issuer name and stated ACN/ABN agree; type discrepancy retained.
- **DAL:** fresh ABR lookup using explicit issuer ACN 648 476 699 establishes previously missing ABN 23 648 476 699. No ABN was invented from the ACN.
- **CCV name shorthand:** the matrix/ASX form omits Limited; the report and ABR establish the full legal parent name. Original matrix name is preserved; exact legal name is recorded in the detailed register.

## Method and limits

Appendix 2A Part 1 entity names, identifier types/numbers and issuer tickers were inspected, plus annual-report corporate directories/general information and official ASX issuer/report links where no current quotation form was available. ABR exact current names and registration numbers were checked; CMA/CTS differences were documented instead of falsely described as exact current-name matches. All 20 ABNs pass arithmetic checks, but a passing checksum alone is not identity proof.

Auditor/subsidiary identifiers are not substituted for issuer identifiers. Generic ABR registration-number labels are not automatically typed as ACN/ARBN. Country is recorded only where expressly stated for the parent. Unknown facts remain unknown. Exact quoted-code descriptions are distinguished from option/rights codes. Dated issuer forms do not clear complete security history, current capital processing or current tradeability. No issuer receives full Step 1.3.2.4 sign-off from this batch.

## Traceability and publication QA

The [batch CSV](STEP_1_3_2_4_PRIMARY_IDENTITY_BATCH_20_2026_10_14_B.csv) contains source URLs, qualifications and outcome per company. The [primary ledger](STEP_1_3_2_4_PRIMARY_EVIDENCE_LEDGER.csv), complete register and exception register contain the new page-specific facts and continuing gaps. All 316 candidates retained; exactly 20 matrix rows changed; the other 296 rows and original notes are preserved. CSVs and evidence references validated. Commit/readback verification precedes reporting success.
