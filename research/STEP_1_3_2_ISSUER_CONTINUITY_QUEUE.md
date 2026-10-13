# Step 1.3.2 — Action 2.3: Remaining issuer-continuity queue

**Research date:** 13 October 2026. **Status:** triage prepared; 13 P1 issuer identity checks corroborated by independent ASX/issuer evidence; 243 P2/P3 issuer checks not independently checked. These checks do not confirm current trading status or full ACN/ISIN history.

This queue is the set difference of all **316** codes in `operating_candidates.csv` and the **37** already documented in `STEP_1_3_2_NAME_CONTINUITY_REVIEW.md`. Exactly **279** candidates remain. Rows explicitly marked *Not independently checked* have no independent issuer evidence yet; all 13 annotated P1 rows have limited independent corroboration; none of these findings independently clears current tradeability. Priority is a **workflow heuristic, not an issuer-risk finding**. P1 = previously flagged ticker-reuse or trading-status exceptions; P2 = issuer name contains a parent/security-form term; P3 = remaining codes. The P2/P3 labels are not evidence of any corporate action.

**Priority counts:** P1 13; P2 46; P3 220; total 279.

**Verification procedure:** For each issuer, retrieve ASX company profile and latest issuer annual report; establish legal issuer name, ACN/ARBN or equivalent, current security/ISIN, previous names, and any scheme or issuer substitution. Confirm any discrepancies through dated ASX issuer announcements. Record URL, effective date, issuer continuity decision, and whether any ticker reuse or parent substitution affects historical financial joins. Check current trading status separately under Step 1.2.

**Primary source links:** https://www.asx.com.au/markets/trade-our-cash-market/directory.html ; https://www.asx.com.au/asx/v2/statistics/announcements.do ; https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes.html

| Code | Candidate CSV company name | Triage priority | Independent issuer check |
|---|---|---|---|
| 14D | 1414 DEGREES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AX1 | ACCENT GROUP LIMITED | P2 — parent/security-form check | P2 VERIFIED — ASX-filed 4 May 2026 trading update identifies Accent Group Limited (ASX:AX1), consistent with CSV name (https://announcements.asx.com.au/asxpdf/20260504/pdf/06z63tw1rf6dwj.pdf). No parent substitution or CDI treatment evidenced by this filing; full ACN/ISIN review outstanding. |
| ACW | ACTINOGEN MEDICAL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ACE | ACUSENSUS LIMITED. | P2 — parent/security-form check | INDEX CORROBORATED — S&P/ASX June 2026 index notice identifies ACE as Acusensus Limited, but is not an issuer filing; issuer ACN/ISIN and continuity remain unverified. Source: https://announcements.asx.com.au/asxpdf/20260605/pdf/070ck790lxncyr.pdf |
| ADH | ADAIRS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AI1 | ADISYN LTD | P3 — routine issuer confirmation | Not independently checked |
| AVM | ADVANCE METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AIH | ADVANCED INNERGY HOLDINGS LIMITED | P2 — parent/security-form check | INDEX CORROBORATED — S&P/ASX March 2026 index notice identifies AIH as Advanced Innergy Holdings Limited; issuer filing, ACN/ISIN and predecessor review still required. Source: https://announcements.asx.com.au/asxpdf/20260306/pdf/06x4vd88v6bpg7.pdf |
| AGR | AGUIA RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AUQ | ALARA RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ALC | ALCIDION GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 29 Apr 2026 Alcidion quarterly activities report identifies Alcidion Group Limited (ASX:ALC), ABN 77 143 142 410; parent-substitution history and ISIN still to verify. Source: https://announcements.asx.com.au/asxpdf/20260429/pdf/06yz2ypw46c3pn.pdf |
| ARN | ALDORO RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AQZ | ALLIANCE AVIATION SERVICES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AGE | ALLIGATOR ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ALR | ALTAIR MINERALS LIMITED | P1 — issuer reuse/status exception | Primary issuer evidence found: 27 Apr 2026 Altair Minerals ASX announcement (https://announcements.asx.com.au/asxpdf/20260427/pdf/06ywhv0xtg23bp.pdf); CHK→ALR 17 May 2024 ASX code-change register; unrelated Aberdeen Leaders ALR→CLF 2018. Current issuer name corroborated; ACN/ISIN not yet checked. |
| ATH | ALTERITY THERAPEUTICS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ALU | ALURION RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ALV | ALVO MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AMA | AMA GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 1 Oct 2025 ASX-filed AGM notice defines AMA Group Limited ACN 113 883 560 and fully paid ordinary shares; further historical continuity checks outstanding. Source: https://announcements.asx.com.au/asxpdf/20251001/pdf/06pyj02jc7bbv0.pdf |
| ARR | AMERICAN RARE EARTHS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AL3 | AML3D LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ANX | ANAX METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ASL | ANDEAN SILVER LIMITED | P1 — issuer reuse/status exception | Primary issuer evidence found: 27 Sep 2024 Andean Silver annual report (https://announcements.asx.com.au/asxpdf/20240927/pdf/068cvyvhrhl8ms.pdf) explicitly confirms Mitre Mining→Andean Silver, ASL trading from 11 Jul 2024; unrelated Ausdrill ASL→PRN 2019. Current issuer succession corroborated; ACN/ISIN not yet checked. |
| AZY | ANTIPA MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AON | APOLLO MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| APX | APPEN LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AR9 | ARCHTIS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ARD | ARGENT MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| A1N | ARN MEDIA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ARX | AROA BIOSURGERY LIMITED | P1 — issuer reuse/status exception | ASX primary issuer profile (https://www.asx.com.au/blog/listed-at-asx/new-zealands-aroa-biosurgery-takes-wound-technology-to-the-world) confirms Aroa Biosurgery IPO under ARX in July 2020; ASX historic announcement archive (https://www.asx.com.au/asx/v2/statistics/announcements.do?by=issuerId&issuerId=2046&timeframe=Y&year=2022) explicitly lists other ARX users. Current issuer separate from Arc Exploration; ACN/ISIN not yet checked. |
| ALA | AROVELLA THERAPEUTICS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AMD | ARROW MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| AS1 | ASARA RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| A11 | ATLANTIC LITHIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AKN | AUKING MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AEE | AURA ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AWJ | AURIC MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AUE | AURUM RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AHC | AUSTCO HEALTHCARE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AR1 | AUSTRAL RESOURCES AUSTRALIA LTD | P1 — issuer reuse/status exception | Independent issuer identity corroborated: ASX FY27 broker-report list names AR1 as Austral Resources Australia Ltd (https://www.asx.com.au/investors/investment-tools-and-resources/broker-reports.html); issuer's 2 Apr 2026 Appendix 2A names AUSTRAL RESOURCES AUSTRALIA LTD, AR1 ordinary shares (https://www.marketindex.com.au/asx/ar1/announcements/application-for-quotation-of-securities-ar1-2A1664103). Separate from Arrowhead Resources (historic AR1→EM1 in 2018). ACN/ISIN not yet verified; no current trading-status conclusion. |
| AUZ | AUSTRALIAN MINES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AVL | AUSTRALIAN VANADIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ASG | AUTOSPORTS GROUP LIMITED. | P2 — parent/security-form check | ISSUER CORROBORATED — 26 Feb 2026 issuer announcement identifies Autosports Group Limited (ASX:ASG); ACN/ISIN and full corporate lineage not established. Source: https://announcements.asx.com.au/asxpdf/20260226/pdf/06ws4wn5nfx4pr.pdf |
| BBN | BABY BUNTING GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 24 Jun 2026 issuer trading update identifies Baby Bunting Group Limited; no evidence of parent substitution from this filing; ACN/ISIN not yet checked. Source: https://announcements.asx.com.au/asxpdf/20260624/pdf/070yd7m1qkrhyk.pdf |
| BM1 | BALLARD MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BGD | BARTON GOLD HOLDINGS LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 1 Jun 2026 issuer placement notice identifies Barton Gold Holdings Limited and ordinary shares, 239,698,877 pre-placement and 30m proposed new ordinary shares; check completion in separate capital-action work. Source: https://announcements.asx.com.au/asxpdf/20260601/pdf/07059kdk7gjn4z.pdf |
| BAS | BASS OIL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BLX | BEACON LIGHTING GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 4 May 2026 issuer Appendix 3Y names Beacon Lighting Group Limited, ABN 90 164 122 785; full parent succession and ISIN not yet checked. Source: https://www.marketindex.com.au/asx/blx/announcements/blx-appendix-3y-3A692629 |
| BFG | BELL FINANCIAL GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 7 May 2026 issuer AGM announcement names Bell Financial Group Limited, ABN 27 152 260 814; issuer investor site provides Aug 2026 reports. Historical legal-entity continuity not exhaustively verified. Source: https://www.marketindex.com.au/asx/bfg/announcements/2026-agm-results-3A692893 |
| BVR | BELLAVISTA RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| BKY | BERKELEY ENERGIA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BET | BETMAKERS TECHNOLOGY GROUP LTD | P2 — parent/security-form check | ISSUER CORROBORATED — 29 Apr 2026 issuer Q3 update names BetMakers Technology Group Ltd, ABN 21 164 521 395; legal-parent history and ISIN not yet checked. Source: https://announcements.asx.com.au/asxpdf/20260429/pdf/06yzpzr04q7xff.pdf |
| BWN | BHAGWAN MARINE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BIO | BIOME AUSTRALIA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BB1 | BLINKLAB LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BLG | BLUGLASS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BOA | BOA RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| BML | BOAB METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BOT | BOTANIX PHARMACEUTICALS LTD | P3 — routine issuer confirmation | Not independently checked |
| BPM | BPM MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BRN | BRAINCHIP HOLDINGS LTD | P2 — parent/security-form check | 2026 issuer AGM filing corroborated; legal succession pending |
| BCM | BRAZILIAN CRITICAL MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BRK | BROOKSIDE ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BSA | BSA LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — ASX-filed 2026 half-year report identifies BSA Limited as an Australian-incorporated ASX-listed company (https://announcements.asx.com.au/asxpdf/20260220/pdf/06wjrz3p9rnvwm.pdf). ASX Appendix 3G dated 1 May 2026 identifies BSA Limited, ACN 088 412 748, ASX code BSA (https://www.marketindex.com.au/asx/bsa/announcements/notification-regarding-unquoted-securities-bsa-2A1669611). FY2026 annual report (20 Aug 2026) identifies BSA as listed ultimate parent (https://financialfilings.com/filings/bsa-limited/annual-report/2026/57006560/). September 2026 suspension notices exist; tradeability is NOT established by these identity filings. Historic parent continuity before 2026 not exhaustively checked. |
| BUB | BUBS AUSTRALIA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CRS | CAPRICE RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| CVV | CARAVEL MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CMA | CARMA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CNB | CARNABY RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CCV | CASH CONVERTERS INTERNATIONAL | P3 — routine issuer confirmation | Not independently checked |
| CPN | CASPIN RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CXU | CAULDRON ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CTM | CENTAURUS METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CAF | CENTREPOINT ALLIANCE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CTS | CERETAS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CTT | CETTIRE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CLV | CLOVER CORPORATION LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CEH | COAST ENTERTAINMENT HOLDINGS LIMITED | P2 — parent/security-form check | 2026 ASX Appendix 4D confirms CEH and ABN 51 628 881 603: https://announcements.asx.com.au/asxpdf/20260213/pdf/06w898v7bb90hw.pdf ; historical succession not yet checked |
| CBE | COBRE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| COD | CODA MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| COI | COMET RIDGE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CRN | CORONADO GLOBAL RESOURCES INC. | P2 — parent/security-form check | P2 VERIFIED — ASX issuer profile confirms CORONADO GLOBAL RESOURCES INC., CRN, ISIN AU0000026122, security **CHESS Depositary Interests 10:1**, ASX listed 23 Oct 2018 (https://www.asx.com.au/markets/company/CRN). Foreign issuer; treat 10 CDIs = 1 underlying share, do not treat ASX CDI count as US common-share count. Parent legal incorporation/ARBN to verify separately. |
| CYM | CYPRIUM METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DAL | DALAROO METALS LTD | P3 — routine issuer confirmation | Not independently checked |
| DTR | DATELINE RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DLI | DELTA LITHIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DEV | DEVEX RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DCC | DIGITALX LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DXB | DIMERIX LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DUG | DUG TECHNOLOGY LTD | P3 — routine issuer confirmation | Not independently checked |
| EBR | EBR SYSTEMS INC. | P2 — parent/security-form check | P2 VERIFIED — **RESOLVED 1 Apr 2026 (Australian time):** issuer ASX announcement 26 Mar 2026 confirms 1-for-10 reverse split of underlying US common shares, while ASX CDIs are **not consolidated**; CDI-to-common-share ratio changes from 1:1 to 10:1. Primary issuer filing: https://wcsecure.weblink.com.au/pdf/EBR/03072291.pdf . SEC-hosted 2025 annual report explicitly says historic figures were not adjusted for the proposed split: https://www.sec.gov/Archives/edgar/data/1347123/000121465926003810/j325265ars.pdf . June 2026 issuer capital raising confirms 10 CDIs = 1 US share: https://www.sec.gov/Archives/edgar/data/1347123/000121465926007314/z692638k.htm . **Handling:** preserve CDI historical prices/units; normalise US share counts and per-US-share financial metrics for pre/post split; no 10x adjustment to unchanged CDI units solely for this event. |
| EIQ | ECHOIQ LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EDE | EDEN INNOVATIONS LTD | P3 — routine issuer confirmation | Not independently checked |
| EDU | EDU HOLDINGS LIMITED | P2 — parent/security-form check | 2026 issuer FY25 results corroborated; ABN 85 108 962 152; legal succession pending |
| ELT | ELEMENTOS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EL8 | ELEVATE URANIUM LTD | P3 — routine issuer confirmation | Not independently checked |
| EML | EML PAYMENTS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EMP | EMPEROR ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EMV | EMVISION MEDICAL DEVICES LTD | P3 — routine issuer confirmation | Not independently checked |
| ENR | ENCOUNTER RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ETM | ENERGY TRANSITION MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| EWC | ENERGY WORLD CORPORATION LTD | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — issuer investor site identifies Energy World Corporation Ltd (ASX:EWC), ACN 009 124 994, and links June 2026 company disclosure: https://ewc-energy.com/ . No historical entity substitution established from this source; current tradeability unverified. |
| ECT | ENVIRONMENTAL CLEAN TECHNOLOGIES LIMITED. | P2 — parent/security-form check | 2025 issuer annual report corroborated; 2026 confirmation pending |
| EQU | EQUUS ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EGH | EUREKA GROUP HOLDINGS LIMITED | P2 — parent/security-form check | Historical issuer financial report corroborated; 2026 confirmation pending |
| EVZ | EVZ LIMITED | P3 — routine issuer confirmation | Not independently checked |
| FAL | FALCON METALS LTD | P3 — routine issuer confirmation | Not independently checked |
| FXG | FELIX GOLD LIMITED | P3 — routine issuer confirmation | Not independently checked |
| FEX | FENIX RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| FDR | FINDER ENERGY HOLDINGS LIMITED | P2 — parent/security-form check | 2026 issuer SPP booklet corroborated; ordinary shares |
| FMR | FMR RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| FML | FOCUS MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| FHE | FRONTIER ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GEM | G8 EDUCATION LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GLN | GALAN LITHIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GML | GATEWAY MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GSS | GENETIC SIGNATURES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GL1 | GLOBAL LITHIUM RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GHY | GOLD HYDROGEN LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GHM | GOLDEN HORSE MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GRR | GRANGE RESOURCES LIMITED. | P2 — parent/security-form check | Third-party 2026 mention only; issuer filing pending |
| GBR | GREAT BOULDER RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GW1 | GREENWING RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| GWR | GWR GROUP LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — company investor archive lists GWR Group 29 Sep 2026 annual report and Sep 2026 capital return: https://gwrgroup.com.au/investor-centre/asx-announcements/ . Capital return is a corporate action to assess separately; does not establish name/issuer change or current trading status. |
| HMG | HAMELIN GOLD LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HMX | HAMMER METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HAV | HAVILAH RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HLO | HELLOWORLD TRAVEL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HMD | HERAMED LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HTM | HIGH-TECH METALS LTD | P3 — routine issuer confirmation | Not independently checked |
| HZN | HORIZON OIL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HCH | HOT CHILI LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HUM | HUMM GROUP LIMITED | P2 — parent/security-form check | 2026 issuer announcement corroborated; ACN 122 574 583 |
| IMA | IMAGE RESOURCES NL | P3 — routine issuer confirmation | Not independently checked |
| IMM | IMMUTEP LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IMU | IMUGENE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IFN | INFRAGREEN GROUP LIMITED | P2 — parent/security-form check | 2025 index notice only; issuer filing pending |
| INN | INNOVAERO TECHNOLOGIES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IMB | INTELLIGENT MONITORING GROUP LIMITED | P2 — parent/security-form check | December 2025 issuer announcement corroborated; ABN 36 060 774 227; 2026 confirmation pending |
| IVZ | INVICTUS ENERGY LTD | P3 — routine issuer confirmation | Not independently checked |
| ION | IONDRIVE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| INR | IONEER LTD | P3 — routine issuer confirmation | Not independently checked |
| IXR | IONIC RARE EARTHS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ILA | ISLAND PHARMACEUTICALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| JGH | JADE GAS HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| JAV | JAVELIN MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| JLL | JINDALEE LITHIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KAU | KAISER REEF LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KZR | KALAMAZOO RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KAO | KAOKO METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KGL | KGL RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KLI | KILLI RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KSL | KINA SECURITIES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KRR | KING RIVER RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KME | KIP MCGRATH EDUCATION CENTRES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| KTK | KTEK AEROSYSTEMS LTD | P3 — routine issuer confirmation | Not independently checked |
| LKE | LAKE RESOURCES N.L. | P3 — routine issuer confirmation | Not independently checked |
| LRV | LARVOTTO RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LMG | LATROBE MAGNESIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LFT | LI-FT POWER LTD. | P3 — routine issuer confirmation | Not independently checked |
| LML | LINCOLN MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LAU | LINDSAY AUSTRALIA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LNQ | LINQ MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LKY | LOCKSLEY RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LOT | LOTUS RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LTP | LTR PHARMA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LDX | LUMOS DIAGNOSTICS HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| LM8 | LUNNON METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LUX | LUX COPPER CORP. LTD | P2 — parent/security-form check | Not independently checked |
| M24 | MAMBA EXPLORATION LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MKR | MANUKA RESOURCES LTD. | P3 — routine issuer confirmation | Not independently checked |
| MPK | MANY PEAKS MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| MEU | MARMOTA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MMA | MARONAN METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MM8 | MEDALLION METALS LIMITED. | P2 — parent/security-form check | Not independently checked |
| MMI | METRO MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MX1 | MICRO-X LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MM1 | MIDAS MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| MNB | MINBOS RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MSV | MITCHELL SERVICES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MLG | MLG OZ LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MVF | MONASH IVF GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| MXO | MOTIO LTD | P3 — routine issuer confirmation | Not independently checked |
| MRD | MOUNT RIDLEY MINES LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — issuer announcement dated 4 Sep 2026 identifies Mount Ridley Mines Limited, ABN 93 092 304 964: https://www.marketindex.com.au/asx/mrd/announcements/-2-million-placement-to-advance-selectro-and-grass-patch-6A1342191 . ASX archive flags *other historical MRD users* (https://www.asx.com.au/asx/v2/statistics/announcements.do?by=issuerId&issuerId=1787&timeframe=Y&year=2000); issuer-aware historical joins required. Trading halt outcome unresolved. |
| MYR | MYER HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| NYM | NARRYER METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NMR | NATIVE MINERAL RESOURCES HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| NTI | NEUROTECH INTERNATIONAL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NOL | NOBLEOAK LIFE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NMD | NORMANDY MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| NTU | NORTHERN MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NOU | NOUMI LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NVX | NOVONIX LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NYR | NYRADA INC. | P2 — parent/security-form check | Not independently checked |
| OD6 | OD6 METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| OFX | OFX GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| OMA | OMEGA OIL & GAS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| OBL | OMNI BRIDGEWAY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| OCC | ORTHOCELL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PAR | PARADIGM BIOPHARMACEUTICALS LIMITED.. | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — 27 Apr 2026 ASX-hosted investor presentation identifies Paradigm Biopharmaceuticals (ASX:PAR): https://announcements.asx.com.au/asxpdf/20260427/pdf/06ywp9vzwtwhzl.pdf . The previously recorded voluntary-administration/suspension classification requires a separate *dated* 2026 recheck; April presentation cannot prove current status. |
| PGC | PARAGON CARE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PC2 | PC GOLD LTD | P3 — routine issuer confirmation | Not independently checked |
| PEN | PENINSULA ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PWR | PETER WARREN AUTOMOTIVE HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| PVT | PIVOTAL METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PLT | PLENTI GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| PVE | PO VALLEY ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| POL | POLYMETALS RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| PPS | PRAEMIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PTX | PRESCIENT THERAPEUTICS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PSC | PROSPECT RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| QML | QMINES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RZI | RAIZ INVEST LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RDY | READYTECH HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| REC | RECHARGE METALS LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — ASX-filed 26 Sep 2025 AGM announcement identifies Recharge Metals Limited (ASX:REC), ABN 13 647 703 839: https://announcements.asx.com.au/asxpdf/20250926/pdf/06pr0hgjlfwv4f.pdf . ASX historical issuer-code archive lists another REC user (https://www.asx.com.au/asx/v2/statistics/announcements.do?by=issuerId&issuerId=3924&timeframe=Y&year=2020). Current halt/trading outcome unresolved. |
| RNU | RENASCOR RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RMC | RESIMAC GROUP LTD | P2 — parent/security-form check | Not independently checked |
| RML | RESOLUTION MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| RFG | RETAIL FOOD GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| RIV | RIVCO AUSTRALIA LTD | P3 — routine issuer confirmation | Not independently checked |
| RWL | RUBICON WATER LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RTR | RUMBLE RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SLD | "SALUDA MEDICAL | P3 — routine issuer confirmation | Not independently checked |
| SFM | SANTA FE MINERALS LTD | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — 29 Apr 2026 ASX-filed shareholder AGM notice identifies Santa Fe Minerals Limited (ASX:SFM): https://announcements.asx.com.au/asxpdf/20260429/pdf/06yzpdsw3fflnd.pdf . Current tradeability not established. |
| SMI | SANTANA MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| STN | SATURN METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SCX | SCX.AI HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| SEA | SEA FOREST LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SNM | SENTINEL METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SSG | SHAVER SHOP GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| SNX | SIERRA NEVADA GOLD INC. | P2 — parent/security-form check | Not independently checked |
| SVL | SILVER MINES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SHG | SINGULAR HEALTH GROUP LTD | P2 — parent/security-form check | Not independently checked |
| SKY | SKY METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SPZ | SMART PARKING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SVR | SOLVAR LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SXL | SOUTHERN CROSS MEDIA GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| SPD | SOUTHERN PALLADIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SVM | SOVEREIGN METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SGQ | ST GEORGE MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SPL | STARPHARMA HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| SLB | STELAR METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SRZ | STELLAR RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| STK | STRICKLAND METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| STX | STRIKE ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SS1 | SUN SILVER LIMITED | P3 — routine issuer confirmation | Not independently checked |
| STM | SUNSTONE METALS LTD | P3 — routine issuer confirmation | Not independently checked |
| SOP | SYNERTEC CORPORATION LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SYR | SYRAH RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| TAM | TANAMI GOLD NL | P3 — routine issuer confirmation | Not independently checked |
| TM1 | TERRA METALS LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — ASX-filed 27 Feb 2026 Appendix 3B identifies Terra Metals Limited, TM1 fully paid ordinary shares: https://announcements.asx.com.au/asxpdf/20260227/pdf/06wvtsxwydq9zt.pdf . Historical PNL→GCX→TM1 chain documented in ticker register; ASX archive shows *other historical GCX users*: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=issuerId&issuerId=6032&timeframe=Y&year=2008 . Current halt outcome unresolved. |
| TER | TERRACOM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| TTM | TITAN MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| TTT | TITOMIC LIMITED | P3 — routine issuer confirmation | Not independently checked |
| TVN | TIVAN LIMITED | P3 — routine issuer confirmation | Not independently checked |
| TOK | TOLU MINERALS LIMITED. | P2 — parent/security-form check | Not independently checked |
| TOR | TORQUE METALS LIMITED.. | P2 — parent/security-form check | Not independently checked |
| TRE | TOUBANI RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| TNC | TRUE NORTH COPPER LIMITED | P3 — routine issuer confirmation | Not independently checked |
| TGN | TUNGSTEN MINING NL | P3 — routine issuer confirmation | Not independently checked |
| TYR | TYRO PAYMENTS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| USL | UNICO SILVER LIMITED | P3 — routine issuer confirmation | Not independently checked |
| VAL | VALIANT GOLD LIMITED | P1 — issuer reuse/status exception | Independent ASX admission evidence: ASX notice 25 Mar 2026 (https://asxonline.com/content/asxonline/public/notices/2026/march/0331.26.03.html), and Valiant Gold IPO completion confirms first VAL quotation 27 Mar 2026 (https://company-announcements.afr.com/asx/val/bb74128f-2bba-11f1-a6df-1a10ddfe25b2.pdf). Distinct from Valor Resources, historic VAL→THB in 2024. ACN/ISIN not yet verified; no current trading-status conclusion. |
| VR8 | VANADIUM RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| VBX | VBX LIMITED | P3 — routine issuer confirmation | Not independently checked |
| VMC | VENUS METALS CORPORATION LIMITED | P3 — routine issuer confirmation | Not independently checked |
| VBC | VERBREC LIMITED | P3 — routine issuer confirmation | Not independently checked |
| VHM | VHM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| VTM | VICTORY METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| VVA | VIVA LEISURE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| VYS | VYSARN LIMITED | P3 — routine issuer confirmation | Not independently checked |
| WTM | WARATAH MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| WJL | WEBJET GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| WWI | WEST WITS MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| WCN | WHITE CLIFF MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| WEC | WHITE ENERGY COMPANY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| WC8 | WILDCAT RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| WZR | WISR LIMITED | P3 — routine issuer confirmation | Not independently checked |
| XRF | XRF SCIENTIFIC LIMITED | P3 — routine issuer confirmation | Not independently checked |


### Priority 1 follow-up — 13 October 2026

Reviewed the remaining eight Priority 1 tickers. Seven (EWC, GWR, MRD, PAR, REC, SFM, TM1) have independent issuer-name corroboration from dated company/ASX filings or investor disclosures. **BSA remains unresolved** for lack of a retrieved primary filing in this pass. This is issuer identity evidence only: do **not** treat as proof of current tradeability, absence of delisting, or full legal succession. GWR capital return and historical MRD/REC code reuse warrant explicit corporate-action/data-join checks. The 316 candidate records remain unchanged.


### Priority 1 completion note — BSA (13 October 2026)

BSA's issuer identity is supported by the ASX-filed February 2026 half-year report and May 2026 Appendix 3G (ACN 088 412 748); the August 2026 annual report confirms the listed parent. All 13 P1 candidates now have some independently corroborated issuer-identity evidence. **This does not sign off full legal-entity lineage or Step 1.2 trading status.** BSA's September 2026 suspension history requires a separate dated follow-up.


### Priority 2 batch 1 — 13 October 2026

Three issuer identities independently corroborated: AX1, CRN and EBR. **CRN CDIs represent 10 units per common share** per ASX profile. **EBR 2025 annual report describes a 1:1 CDI/share relationship, but a June 2026 offer booklet specifies 10 CDIs per common share.** Do not collapse these into one ratio without verifying effective dates, security consolidation or other conversion events. The present candidate CSV remains unchanged. Remaining P2 count: 43; remaining unverified P2/P3: 263. This review is issuer/security-form evidence, not proof of current trading status.


### EBR CDI ratio discrepancy — resolved (13 October 2026)

The 26 March 2026 **issuer ASX announcement** confirms the reverse split of EBR's underlying common stock at **1-for-10**, effective **1 April 2026 (Australian time)**. The CDIs were **not consolidated**: the CDI:common-share conversion changed from **1:1 before** to **10:1 after**. The 2025 annual report's earlier ratio and June 2026 offer booklet's later ratio therefore reflect distinct effective periods, **not contradictory company identities**. No issuer exclusion or CSV rename. Historical US common-share denominators and per-US-share figures require corporate-action-aware adjustment; ASX CDI unit histories must not be split-adjusted mechanically by 10 for this event. Sources: https://wcsecure.weblink.com.au/pdf/EBR/03072291.pdf ; https://www.sec.gov/Archives/edgar/data/1347123/000121465926003810/j325265ars.pdf ; https://www.sec.gov/Archives/edgar/data/1347123/000121465926007314/z692638k.htm .


### Priority 2 batch 2 — 13 October 2026 (10 tickers)

Reviewed **ACE, AIH, ALC, AMA, ASG, BBN, BGD, BLX, BFG, BET** against dated public evidence; individual row notes link the supporting document. **Eight** have issuer-authored disclosure corroborating the CSV identity (ALC, AMA, ASG, BBN, BGD, BLX, BFG, BET). **Two** (ACE, AIH) have S&P/ASX index-list evidence only and **must not be treated as independently issuer-verified** until primary company filings are examined. This batch is an initial *name/issuer identity check*, not exhaustive historical parent-entity or ISIN verification. No evidence in the reviewed documents requires a candidate exclusion or CSV rename. **P2 progress: 13/46 reviewed, 33 not yet reviewed; of the 13, two remain issuer-evidence provisional.** Total P2/P3 unreviewed: 253.
