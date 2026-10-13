# Step 1.3.2 — Action 2.3: Remaining issuer-continuity queue

**Research date:** 13 October 2026. **Status:** triage prepared; 5 P1 issuer identity checks corroborated by independent ASX/issuer evidence (ALR, ASL, ARX, AR1, VAL); remaining 274 not independently checked. These checks do not confirm current trading status or full ACN/ISIN history.

This queue is the set difference of all **316** codes in `operating_candidates.csv` and the **37** already documented in `STEP_1_3_2_NAME_CONTINUITY_REVIEW.md`. Exactly **279** candidates remain. Rows explicitly marked *Not independently checked* have no independent issuer evidence yet; the five annotated P1 rows have limited independent corroboration. Priority is a **workflow heuristic, not an issuer-risk finding**. P1 = previously flagged ticker-reuse or trading-status exceptions; P2 = issuer name contains a parent/security-form term; P3 = remaining codes. The P2/P3 labels are not evidence of any corporate action.

**Priority counts:** P1 13; P2 46; P3 220; total 279.

**Verification procedure:** For each issuer, retrieve ASX company profile and latest issuer annual report; establish legal issuer name, ACN/ARBN or equivalent, current security/ISIN, previous names, and any scheme or issuer substitution. Confirm any discrepancies through dated ASX issuer announcements. Record URL, effective date, issuer continuity decision, and whether any ticker reuse or parent substitution affects historical financial joins. Check current trading status separately under Step 1.2.

**Primary source links:** https://www.asx.com.au/markets/trade-our-cash-market/directory.html ; https://www.asx.com.au/asx/v2/statistics/announcements.do ; https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes.html

| Code | Candidate CSV company name | Triage priority | Independent issuer check |
|---|---|---|---|
| 14D | 1414 DEGREES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AX1 | ACCENT GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| ACW | ACTINOGEN MEDICAL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ACE | ACUSENSUS LIMITED. | P2 — parent/security-form check | Not independently checked |
| ADH | ADAIRS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AI1 | ADISYN LTD | P3 — routine issuer confirmation | Not independently checked |
| AVM | ADVANCE METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AIH | ADVANCED INNERGY HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| AGR | AGUIA RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AUQ | ALARA RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ALC | ALCIDION GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| ARN | ALDORO RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AQZ | ALLIANCE AVIATION SERVICES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AGE | ALLIGATOR ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ALR | ALTAIR MINERALS LIMITED | P1 — issuer reuse/status exception | Primary issuer evidence found: 27 Apr 2026 Altair Minerals ASX announcement (https://announcements.asx.com.au/asxpdf/20260427/pdf/06ywhv0xtg23bp.pdf); CHK→ALR 17 May 2024 ASX code-change register; unrelated Aberdeen Leaders ALR→CLF 2018. Current issuer name corroborated; ACN/ISIN not yet checked. |
| ATH | ALTERITY THERAPEUTICS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ALU | ALURION RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ALV | ALVO MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| AMA | AMA GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
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
| ASG | AUTOSPORTS GROUP LIMITED. | P2 — parent/security-form check | Not independently checked |
| BBN | BABY BUNTING GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| BM1 | BALLARD MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BGD | BARTON GOLD HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| BAS | BASS OIL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BLX | BEACON LIGHTING GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| BFG | BELL FINANCIAL GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| BVR | BELLAVISTA RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| BKY | BERKELEY ENERGIA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BET | BETMAKERS TECHNOLOGY GROUP LTD | P2 — parent/security-form check | Not independently checked |
| BWN | BHAGWAN MARINE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BIO | BIOME AUSTRALIA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BB1 | BLINKLAB LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BLG | BLUGLASS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BOA | BOA RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| BML | BOAB METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BOT | BOTANIX PHARMACEUTICALS LTD | P3 — routine issuer confirmation | Not independently checked |
| BPM | BPM MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BRN | BRAINCHIP HOLDINGS LTD | P2 — parent/security-form check | Not independently checked |
| BCM | BRAZILIAN CRITICAL MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BRK | BROOKSIDE ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| BSA | BSA LIMITED | P1 — issuer reuse/status exception | Not independently checked |
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
| CEH | COAST ENTERTAINMENT HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| CBE | COBRE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| COD | CODA MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| COI | COMET RIDGE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| CRN | CORONADO GLOBAL RESOURCES INC. | P2 — parent/security-form check | Not independently checked |
| CYM | CYPRIUM METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DAL | DALAROO METALS LTD | P3 — routine issuer confirmation | Not independently checked |
| DTR | DATELINE RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DLI | DELTA LITHIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DEV | DEVEX RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DCC | DIGITALX LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DXB | DIMERIX LIMITED | P3 — routine issuer confirmation | Not independently checked |
| DUG | DUG TECHNOLOGY LTD | P3 — routine issuer confirmation | Not independently checked |
| EBR | EBR SYSTEMS INC. | P2 — parent/security-form check | Not independently checked |
| EIQ | ECHOIQ LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EDE | EDEN INNOVATIONS LTD | P3 — routine issuer confirmation | Not independently checked |
| EDU | EDU HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| ELT | ELEMENTOS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EL8 | ELEVATE URANIUM LTD | P3 — routine issuer confirmation | Not independently checked |
| EML | EML PAYMENTS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EMP | EMPEROR ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EMV | EMVISION MEDICAL DEVICES LTD | P3 — routine issuer confirmation | Not independently checked |
| ENR | ENCOUNTER RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ETM | ENERGY TRANSITION MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| EWC | ENERGY WORLD CORPORATION LTD | P1 — issuer reuse/status exception | Not independently checked |
| ECT | ENVIRONMENTAL CLEAN TECHNOLOGIES LIMITED. | P2 — parent/security-form check | Not independently checked |
| EQU | EQUUS ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| EGH | EUREKA GROUP HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
| EVZ | EVZ LIMITED | P3 — routine issuer confirmation | Not independently checked |
| FAL | FALCON METALS LTD | P3 — routine issuer confirmation | Not independently checked |
| FXG | FELIX GOLD LIMITED | P3 — routine issuer confirmation | Not independently checked |
| FEX | FENIX RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| FDR | FINDER ENERGY HOLDINGS LIMITED | P2 — parent/security-form check | Not independently checked |
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
| GRR | GRANGE RESOURCES LIMITED. | P2 — parent/security-form check | Not independently checked |
| GBR | GREAT BOULDER RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| GW1 | GREENWING RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| GWR | GWR GROUP LIMITED | P1 — issuer reuse/status exception | Not independently checked |
| HMG | HAMELIN GOLD LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HMX | HAMMER METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HAV | HAVILAH RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HLO | HELLOWORLD TRAVEL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HMD | HERAMED LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HTM | HIGH-TECH METALS LTD | P3 — routine issuer confirmation | Not independently checked |
| HZN | HORIZON OIL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HCH | HOT CHILI LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HUM | HUMM GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| IMA | IMAGE RESOURCES NL | P3 — routine issuer confirmation | Not independently checked |
| IMM | IMMUTEP LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IMU | IMUGENE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IFN | INFRAGREEN GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| INN | INNOVAERO TECHNOLOGIES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IMB | INTELLIGENT MONITORING GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
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
| MRD | MOUNT RIDLEY MINES LIMITED | P1 — issuer reuse/status exception | Not independently checked |
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
| PAR | PARADIGM BIOPHARMACEUTICALS LIMITED.. | P1 — issuer reuse/status exception | Not independently checked |
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
| REC | RECHARGE METALS LIMITED | P1 — issuer reuse/status exception | Not independently checked |
| RNU | RENASCOR RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RMC | RESIMAC GROUP LTD | P2 — parent/security-form check | Not independently checked |
| RML | RESOLUTION MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| RFG | RETAIL FOOD GROUP LIMITED | P2 — parent/security-form check | Not independently checked |
| RIV | RIVCO AUSTRALIA LTD | P3 — routine issuer confirmation | Not independently checked |
| RWL | RUBICON WATER LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RTR | RUMBLE RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SLD | "SALUDA MEDICAL | P3 — routine issuer confirmation | Not independently checked |
| SFM | SANTA FE MINERALS LTD | P1 — issuer reuse/status exception | Not independently checked |
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
| TM1 | TERRA METALS LIMITED | P1 — issuer reuse/status exception | Not independently checked |
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
