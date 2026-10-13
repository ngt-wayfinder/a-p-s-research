# Step 1.3.2 — Action 2.3: Remaining issuer-continuity queue

**Research date:** 13 October 2026. **Status:** triage prepared; 13 P1 issuer identity checks corroborated by independent ASX/issuer evidence; 180 P3 issuer checks not independently checked. These checks do not confirm current trading status or full ACN/ISIN history.

This queue is the set difference of all **316** codes in `operating_candidates.csv` and the **37** already documented in `STEP_1_3_2_NAME_CONTINUITY_REVIEW.md`. Exactly **279** candidates remain. Rows explicitly marked *Not independently checked* have no independent issuer evidence yet; all 13 annotated P1 rows have limited independent corroboration; none of these findings independently clears current tradeability. Priority is a **workflow heuristic, not an issuer-risk finding**. P1 = previously flagged ticker-reuse or trading-status exceptions; P2 = issuer name contains a parent/security-form term; P3 = remaining codes. The P2/P3 labels are not evidence of any corporate action.

**Priority counts:** P1 13; P2 46; P3 220; total 279.

**Verification procedure:** For each issuer, retrieve ASX company profile and latest issuer annual report; establish legal issuer name, ACN/ARBN or equivalent, current security/ISIN, previous names, and any scheme or issuer substitution. Confirm any discrepancies through dated ASX issuer announcements. Record URL, effective date, issuer continuity decision, and whether any ticker reuse or parent substitution affects historical financial joins. Check current trading status separately under Step 1.2.

**Primary source links:** https://www.asx.com.au/markets/trade-our-cash-market/directory.html ; https://www.asx.com.au/asx/v2/statistics/announcements.do ; https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes.html

| Code | Candidate CSV company name | Triage priority | Independent issuer check |
|---|---|---|---|
| 14D | 1414 DEGREES LIMITED | P3 — routine issuer confirmation | 2026 issuer corroborated (ABN 57 138 803 620); 1 Sep 2026 acquisition of Vast Solar Aurora Pty Ltd flags project ownership, not proven parent change. https://www.marketindex.com.au/asx/14d/announcements/14d-secures-100-of-aurora-energy-precinct-2A1694120 |
| AX1 | ACCENT GROUP LIMITED | P2 — parent/security-form check | P2 VERIFIED — ASX-filed 4 May 2026 trading update identifies Accent Group Limited (ASX:AX1), consistent with CSV name (https://announcements.asx.com.au/asxpdf/20260504/pdf/06z63tw1rf6dwj.pdf). No parent substitution or CDI treatment evidenced by this filing; full ACN/ISIN review outstanding. |
| ACW | ACTINOGEN MEDICAL LIMITED | P3 — routine issuer confirmation | 2026 issuer corroborated: Actinogen Medical Limited ACN 086 778 476, ASX ACW. https://investors.actinogen.com.au/announcements/7705819?fromLink=true |
| ACE | ACUSENSUS LIMITED. | P2 — parent/security-form check | ISSUER corroborated — Nov 2025 Acusensus ASX AGM release: https://announcements.asx.com.au/asxpdf/20251119/pdf/06s5l3hlxr5h4q.pdf . Full historical succession/ISIN outstanding. |
| ADH | ADAIRS LIMITED | P3 — routine issuer confirmation | 2026 issuer corroborated: Adairs Limited ASX ADH, February 2026 1H results. https://announcements.asx.com.au/asxpdf/20260223/pdf/06wltn60g9ry6q.pdf |
| AI1 | ADISYN LTD | P3 — routine issuer confirmation | Reviewed; no sufficiently grounded 2026 primary issuer filing in this batch. Identity/security class remains provisional. |
| AVM | ADVANCE METALS LIMITED | P3 — routine issuer confirmation | 2026 issuer corroborated: Advance Metals Limited ASX AVM, February 2026 board-authorised presentation. https://announcements.asx.com.au/asxpdf/20260216/pdf/06wc293zpt4ykb.pdf |
| AIH | ADVANCED INNERGY HOLDINGS LIMITED | P2 — parent/security-form check | ISSUER corroborated — Jan 2026 AGM proxy form: https://announcements.asx.com.au/asxpdf/20260120/pdf/06vf3qf93prd1b.pdf . Proposed Matrix Composites takeover (20 Apr 2026) is a separate transaction, not evidence of completion: https://announcements.asx.com.au/asxpdf/20260420/pdf/06yn2px0gr8x1h.pdf |
| AGR | AGUIA RESOURCES LIMITED | P3 — routine issuer confirmation | 2026 issuer corroborated: Aguia Resources Limited ASX AGR; July 2026 proposed issue of fully paid ordinary shares, completion separately unverified. https://www.marketindex.com.au/asx/agr/announcements/proposed-issue-of-securities-agr-2A1685357 |
| AUQ | ALARA RESOURCES LIMITED | P3 — routine issuer confirmation | Reviewed; no sufficiently grounded 2026 primary issuer filing in this batch. Identity/security class remains provisional. |
| ALC | ALCIDION GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 29 Apr 2026 Alcidion quarterly activities report identifies Alcidion Group Limited (ASX:ALC), ABN 77 143 142 410; parent-substitution history and ISIN still to verify. Source: https://announcements.asx.com.au/asxpdf/20260429/pdf/06yz2ypw46c3pn.pdf |
| ARN | ALDORO RESOURCES LIMITED | P3 — routine issuer confirmation | 2026 issuer securities-announcement listing corroborated: Aldoro Resources ASX ARN; verify primary document and securities class. https://www.marketindex.com.au/asx/arn/announcements/proposed-issue-of-securities-arn-6A1334515 |
| AQZ | ALLIANCE AVIATION SERVICES LIMITED | P3 — routine issuer confirmation | 2025 issuer corroborated: Alliance Aviation Services Limited ACN 153 361 525 ASX AQZ; 2026 confirmation pending. https://announcements.asx.com.au/asxpdf/20250821/pdf/06n4tp9r3gbxw5.pdf |
| AGE | ALLIGATOR ENERGY LIMITED | P3 — routine issuer confirmation | 2026 annual report listing corroborates Alligator Energy ASX AGE; detailed report/security verification pending. https://www.marketindex.com.au/asx/age/announcements/annual-report-2026-2A1700738 |
| ALR | ALTAIR MINERALS LIMITED | P1 — issuer reuse/status exception | Primary issuer evidence found: 27 Apr 2026 Altair Minerals ASX announcement (https://announcements.asx.com.au/asxpdf/20260427/pdf/06ywhv0xtg23bp.pdf); CHK→ALR 17 May 2024 ASX code-change register; unrelated Aberdeen Leaders ALR→CLF 2018. Current issuer name corroborated; ACN/ISIN not yet checked. |
| ATH | ALTERITY THERAPEUTICS LIMITED | P3 — routine issuer confirmation | 2026 primary issuer notice confirms Alterity Therapeutics Limited, ACN 080 699 065, ASX ATH; historical name Prana Biotechnology requires continuity mapping: https://announcements.asx.com.au/asxpdf/20260429/pdf/06yzydghc8l2vq.pdf |
| ALU | ALURION RESOURCES LIMITED | P3 — routine issuer confirmation | 2026 demerger/IPO evidence: Alurion Resources was distributed by BRE and commenced ASX trading 31 Jul 2026. DO NOT splice earlier ALU ticker history (Altium, delisted 2024) into this issuer. Primary demerger disclosure https://data-api.marketindex.com.au/api/v1/announcements/XASX%3ABRE%3A6A1328543/pdf/inline/bre-issue-demerger-documents-and-alu-lodges-prospectus ; listing archive https://www.intelligentinvestor.com.au/shares/asx-alu/alurion-resources-limited/announcements . Full ACN/ISIN pending. |
| ALV | ALVO MINERALS LIMITED | P3 — routine issuer confirmation | 2026 issuer website confirms Alvo Minerals Limited ASX ALV, including Oct 2026 placement and prior securities quotations; potential dilution requires allotment checks. https://alvo.com.au/investors-centre/asx-announcements/ . Full ACN/ISIN pending. |
| AMA | AMA GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 1 Oct 2025 ASX-filed AGM notice defines AMA Group Limited ACN 113 883 560 and fully paid ordinary shares; further historical continuity checks outstanding. Source: https://announcements.asx.com.au/asxpdf/20251001/pdf/06pyj02jc7bbv0.pdf |
| ARR | AMERICAN RARE EARTHS LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AL3 | AML3D LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| ANX | ANAX METALS LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| ASL | ANDEAN SILVER LIMITED | P1 — issuer reuse/status exception | Primary issuer evidence found: 27 Sep 2024 Andean Silver annual report (https://announcements.asx.com.au/asxpdf/20240927/pdf/068cvyvhrhl8ms.pdf) explicitly confirms Mitre Mining→Andean Silver, ASL trading from 11 Jul 2024; unrelated Ausdrill ASL→PRN 2019. Current issuer succession corroborated; ACN/ISIN not yet checked. |
| AZY | ANTIPA MINERALS LIMITED | P3 — routine issuer confirmation | 2025 primary issuer AGM announcement confirms Antipa Minerals Limited ASX AZY, ABN 79 147 133 364. 2026 filing and legal history outstanding. https://announcements.asx.com.au/asxpdf/20250919/pdf/06pf743txwf3r4.pdf ; separate unlisted option exercise/expiry evidence https://announcements.asx.com.au/asxpdf/20250829/pdf/06nl6dp25kh7lb.pdf |
| AON | APOLLO MINERALS LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| APX | APPEN LIMITED | P3 — routine issuer confirmation | 2026 issuer AGM notice corroborates Appen Limited ASX APX. 2024 issuer SPP notice gives ABN 60 138 878 298; 2026 ACN/security history pending. https://announcements.asx.com.au/asxpdf/20260417/pdf/06yl96nt6sx9t1.pdf ; https://announcements.asx.com.au/asxpdf/20241018/pdf/0698b7xl18w02v.pdf |
| AR9 | ARCHTIS LIMITED | P3 — routine issuer confirmation | 2025 primary issuer filing confirms archTIS Limited ASX AR9, ACN 123 098 671. Spirion business-asset acquisition was proposed for Sep 2025; completion and share issuance must be independently checked. https://announcements.asx.com.au/asxpdf/20250827/pdf/06nf0898f250x2.pdf |
| ARD | ARGENT MINERALS LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| A1N | ARN MEDIA LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| ARX | AROA BIOSURGERY LIMITED | P1 — issuer reuse/status exception | ASX primary issuer profile (https://www.asx.com.au/blog/listed-at-asx/new-zealands-aroa-biosurgery-takes-wound-technology-to-the-world) confirms Aroa Biosurgery IPO under ARX in July 2020; ASX historic announcement archive (https://www.asx.com.au/asx/v2/statistics/announcements.do?by=issuerId&issuerId=2046&timeframe=Y&year=2022) explicitly lists other ARX users. Current issuer separate from Arc Exploration; ACN/ISIN not yet checked. |
| ALA | AROVELLA THERAPEUTICS LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AMD | ARROW MINERALS LTD | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AS1 | ASARA RESOURCES LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| A11 | ATLANTIC LITHIUM LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AKN | AUKING MINING LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AEE | AURA ENERGY LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AWJ | AURIC MINING LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AUE | AURUM RESOURCES LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AHC | AUSTCO HEALTHCARE LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AR1 | AUSTRAL RESOURCES AUSTRALIA LTD | P1 — issuer reuse/status exception | Independent issuer identity corroborated: ASX FY27 broker-report list names AR1 as Austral Resources Australia Ltd (https://www.asx.com.au/investors/investment-tools-and-resources/broker-reports.html); issuer's 2 Apr 2026 Appendix 2A names AUSTRAL RESOURCES AUSTRALIA LTD, AR1 ordinary shares (https://www.marketindex.com.au/asx/ar1/announcements/application-for-quotation-of-securities-ar1-2A1664103). Separate from Arrowhead Resources (historic AR1→EM1 in 2018). ACN/ISIN not yet verified; no current trading-status conclusion. |
| AUZ | AUSTRALIAN MINES LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| AVL | AUSTRALIAN VANADIUM LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| ASG | AUTOSPORTS GROUP LIMITED. | P2 — parent/security-form check | ISSUER CORROBORATED — 26 Feb 2026 issuer announcement identifies Autosports Group Limited (ASX:ASG); ACN/ISIN and full corporate lineage not established. Source: https://announcements.asx.com.au/asxpdf/20260226/pdf/06ws4wn5nfx4pr.pdf |
| BBN | BABY BUNTING GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 24 Jun 2026 issuer trading update identifies Baby Bunting Group Limited; no evidence of parent substitution from this filing; ACN/ISIN not yet checked. Source: https://announcements.asx.com.au/asxpdf/20260624/pdf/070yd7m1qkrhyk.pdf |
| BM1 | BALLARD MINING LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| BGD | BARTON GOLD HOLDINGS LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 1 Jun 2026 issuer placement notice identifies Barton Gold Holdings Limited and ordinary shares, 239,698,877 pre-placement and 30m proposed new ordinary shares; check completion in separate capital-action work. Source: https://announcements.asx.com.au/asxpdf/20260601/pdf/07059kdk7gjn4z.pdf |
| BAS | BASS OIL LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| BLX | BEACON LIGHTING GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 4 May 2026 issuer Appendix 3Y names Beacon Lighting Group Limited, ABN 90 164 122 785; full parent succession and ISIN not yet checked. Source: https://www.marketindex.com.au/asx/blx/announcements/blx-appendix-3y-3A692629 |
| BFG | BELL FINANCIAL GROUP LIMITED | P2 — parent/security-form check | ISSUER CORROBORATED — 7 May 2026 issuer AGM announcement names Bell Financial Group Limited, ABN 27 152 260 814; issuer investor site provides Aug 2026 reports. Historical legal-entity continuity not exhaustively verified. Source: https://www.marketindex.com.au/asx/bfg/announcements/2026-agm-results-3A692893 |
| BVR | BELLAVISTA RESOURCES LTD | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| BKY | BERKELEY ENERGIA LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| BET | BETMAKERS TECHNOLOGY GROUP LTD | P2 — parent/security-form check | ISSUER CORROBORATED — 29 Apr 2026 issuer Q3 update names BetMakers Technology Group Ltd, ABN 21 164 521 395; legal-parent history and ISIN not yet checked. Source: https://announcements.asx.com.au/asxpdf/20260429/pdf/06yzpzr04q7xff.pdf |
| BWN | BHAGWAN MARINE LIMITED | P3 — routine issuer confirmation | INITIAL TRIAGE ONLY — issuer identity, security form and 2026 primary-source continuity not independently verified in this batch; primary filing required. |
| BIO | BIOME AUSTRALIA LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2026; ACN 627 364 014); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlm222npgbp0.pdf |
| BB1 | BLINKLAB LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2026; proposed 26923077 ordinary shares and 5384615 options, completion pending); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20260416/pdf/06yjzt519r44fs.pdf |
| BLG | BLUGLASS LIMITED | P3 — routine issuer confirmation | Issuer 2026 annual report and AGM listed: https://bluglass.com/news/ ; capital issuance review pending. |
| BOA | BOA RESOURCES LTD | P3 — routine issuer confirmation | Issuer website identifies BOA Resources ASX BOA, ACN 149 582 687: https://boaresources.com/investor-centre/announcements/ |
| BML | BOAB METALS LIMITED | P3 — routine issuer confirmation | Issuer July 2026 quarterly confirms Boab Metals ASX BML: https://investors.boabmetals.com/announcements/7657869 |
| BOT | BOTANIX PHARMACEUTICALS LTD | P3 — routine issuer confirmation | Issuer 2026 annual report confirms BOT; securities issue review pending: https://botanixpharma.com/invest |
| BPM | BPM MINERALS LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2026); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20260304/pdf/06x10skbrck22h.pdf |
| BRN | BRAINCHIP HOLDINGS LTD | P2 — parent/security-form check | 2026 issuer AGM filing corroborated; legal succession pending |
| BCM | BRAZILIAN CRITICAL MINERALS LIMITED | P3 — routine issuer confirmation | Third-party 2026 filing index located; primary issuer document not checked: https://boldinvestors.com.au/asx/bcm/announcements |
| BRK | BROOKSIDE ENERGY LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2026); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20260423/pdf/06ysv4lzc6b48j.pdf |
| BSA | BSA LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — ASX-filed 2026 half-year report identifies BSA Limited as an Australian-incorporated ASX-listed company (https://announcements.asx.com.au/asxpdf/20260220/pdf/06wjrz3p9rnvwm.pdf). ASX Appendix 3G dated 1 May 2026 identifies BSA Limited, ACN 088 412 748, ASX code BSA (https://www.marketindex.com.au/asx/bsa/announcements/notification-regarding-unquoted-securities-bsa-2A1669611). FY2026 annual report (20 Aug 2026) identifies BSA as listed ultimate parent (https://financialfilings.com/filings/bsa-limited/annual-report/2026/57006560/). September 2026 suspension notices exist; tradeability is NOT established by these identity filings. Historic parent continuity before 2026 not exhaustively checked. |
| BUB | BUBS AUSTRALIA LIMITED | P3 — routine issuer confirmation | Issuer FY26 reports confirm Bubs Australia; historical trading halt requires separate Step 1.2 check: https://investor.bubsaustralia.com/news/ |
| CRS | CAPRICE RESOURCES LTD | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2025); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20250826/pdf/06nbkbw2kxk23w.pdf |
| CVV | CARAVEL MINERALS LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| CMA | CARMA LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| CNB | CARNABY RESOURCES LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| CCV | CASH CONVERTERS INTERNATIONAL | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2025; ABN 39 069 141 546; capital raise/acquisition follow-up); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20251120/pdf/06s8dq9cz4lb3w.pdf |
| CPN | CASPIN RESOURCES LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2025; proposed ordinary shares and unlisted options, completion pending); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20250915/pdf/06p6tkmldf5dx7.pdf |
| CXU | CAULDRON ENERGY LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2025; 324756398 fully paid ordinary shares quoted 20 June 2025); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20250620/pdf/06ky4slklw6jcr.pdf |
| CTM | CENTAURUS METALS LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| CAF | CENTREPOINT ALLIANCE LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2026; ABN 72 052 507 507); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20260224/pdf/06wnhklqn4s4q3.pdf |
| CTS | CERETAS LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| CTT | CETTIRE LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2025; ACN 645 474 166); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20250226/pdf/06fyxvw8yz8nz1.pdf |
| CLV | CLOVER CORPORATION LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| CEH | COAST ENTERTAINMENT HOLDINGS LIMITED | P2 — parent/security-form check | 2026 ASX Appendix 4D confirms CEH and ABN 51 628 881 603: https://announcements.asx.com.au/asxpdf/20260213/pdf/06w898v7bb90hw.pdf ; historical succession not yet checked |
| CBE | COBRE LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| COD | CODA MINERALS LTD | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| COI | COMET RIDGE LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| CRN | CORONADO GLOBAL RESOURCES INC. | P2 — parent/security-form check | P2 VERIFIED — ASX issuer profile confirms CORONADO GLOBAL RESOURCES INC., CRN, ISIN AU0000026122, security **CHESS Depositary Interests 10:1**, ASX listed 23 Oct 2018 (https://www.asx.com.au/markets/company/CRN). Foreign issuer; treat 10 CDIs = 1 underlying share, do not treat ASX CDI count as US common-share count. Parent legal incorporation/ARBN to verify separately. |
| CYM | CYPRIUM METALS LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2026; entitlement issue and quotation timetable, completion pending); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20260206/pdf/06w0ycbbcfzmkw.pdf |
| DAL | DALAROO METALS LTD | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| DTR | DATELINE RESOURCES LIMITED | P3 — routine issuer confirmation | Issuer 2026 announcements confirm Dateline Resources; securities issuance and suspension/reinstatement history to check: https://www.datelineresources.com.au/investors/asx-announcements/ |
| DLI | DELTA LITHIUM LIMITED | P3 — routine issuer confirmation | Initial triage only; primary 2026 issuer evidence and security class pending. |
| DEV | DEVEX RESOURCES LIMITED | P3 — routine issuer confirmation | Issuer 2026 reports confirm DevEx Resources; multiple equity classes require mapping: https://www.devexresources.com.au/investors/ |
| DCC | DIGITALX LIMITED | P3 — routine issuer confirmation | Issuer 2026 announcement archive located; specific filing and identity not checked: https://www.digitalx.com/asx-announcements-presentations-and-reports/ |
| DXB | DIMERIX LIMITED | P3 — routine issuer confirmation | Issuer primary filing corroborates identity (2026); full legal continuity pending. https://announcements.asx.com.au/asxpdf/20260428/pdf/06yxzb4916vlq6.pdf |
| DUG | DUG TECHNOLOGY LTD | P3 — routine issuer confirmation | 2025 primary ASX results corroborate DUG Technology Ltd ASX DUG; 2026 check pending. https://announcements.asx.com.au/asxpdf/20250227/pdf/06g0t02p8r3t58.pdf |
| EBR | EBR SYSTEMS INC. | P2 — parent/security-form check | P2 VERIFIED — **RESOLVED 1 Apr 2026 (Australian time):** issuer ASX announcement 26 Mar 2026 confirms 1-for-10 reverse split of underlying US common shares, while ASX CDIs are **not consolidated**; CDI-to-common-share ratio changes from 1:1 to 10:1. Primary issuer filing: https://wcsecure.weblink.com.au/pdf/EBR/03072291.pdf . SEC-hosted 2025 annual report explicitly says historic figures were not adjusted for the proposed split: https://www.sec.gov/Archives/edgar/data/1347123/000121465926003810/j325265ars.pdf . June 2026 issuer capital raising confirms 10 CDIs = 1 US share: https://www.sec.gov/Archives/edgar/data/1347123/000121465926007314/z692638k.htm . **Handling:** preserve CDI historical prices/units; normalise US share counts and per-US-share financial metrics for pre/post split; no 10x adjustment to unchanged CDI units solely for this event. |
| EIQ | ECHOIQ LIMITED | P3 — routine issuer confirmation | 2026 ASX-announced Echo IQ Ltd ASX EIQ attached to Pro Medicus filing; proposed financing/reseller arrangement subject to definitive documents. https://announcements.asx.com.au/asxpdf/20260625/pdf/070zsss29bsg3w.pdf |
| EDE | EDEN INNOVATIONS LTD | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| EDU | EDU HOLDINGS LIMITED | P2 — parent/security-form check | 2026 issuer FY25 results corroborated; ABN 85 108 962 152; legal succession pending |
| ELT | ELEMENTOS LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| EL8 | ELEVATE URANIUM LTD | P3 — routine issuer confirmation | 2026 issuer half-year financial report corroborates Elevate Uranium Ltd; 2025 employee options/performance rights are distinct from ordinary shares. https://announcements.asx.com.au/asxpdf/20260313/pdf/06xcmfvn1n4l04.pdf |
| EML | EML PAYMENTS LIMITED | P3 — routine issuer confirmation | 2026 issuer interim report corroborates EML Payments Limited; legal lineage pending. https://announcements.asx.com.au/asxpdf/20260225/pdf/06wqbfzq6cd51z.pdf |
| EMP | EMPEROR ENERGY LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| EMV | EMVISION MEDICAL DEVICES LTD | P3 — routine issuer confirmation | 2026 primary issuer ASX announcement confirms EMVision Medical Devices Limited (ASX:EMV). https://announcements.asx.com.au/asxpdf/20260527/pdf/07003pnm28ltf0.pdf |
| ENR | ENCOUNTER RESOURCES LIMITED | P3 — routine issuer confirmation | 2025 primary issuer quarterly report confirms Encounter Resources Ltd ASX ENR and 499m shares, 18.8m options/rights at 30 Jun 2025; Oct 2025 $25m placement commitments need actual issuance check. https://announcements.asx.com.au/asxpdf/20250730/pdf/06m8zwd8p90qhr.pdf ; https://announcements.asx.com.au/asxpdf/20251030/pdf/06r8bwgzfbszyv.pdf |
| ETM | ENERGY TRANSITION MINERALS LTD | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| EWC | ENERGY WORLD CORPORATION LTD | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — issuer investor site identifies Energy World Corporation Ltd (ASX:EWC), ACN 009 124 994, and links June 2026 company disclosure: https://ewc-energy.com/ . No historical entity substitution established from this source; current tradeability unverified. |
| ECT | ENVIRONMENTAL CLEAN TECHNOLOGIES LIMITED. | P2 — parent/security-form check | ISSUER corroborated — 6 Oct 2026 issuer announcement, ABN 28 009 120 405: https://www.marketindex.com.au/asx/ect/announcements/ect-strengthens-board-for-next-phase-of-growth-6A1347881 . MATERIAL CORPORATE ACTION: 1-for-15 ordinary-share consolidation completed 26 Aug 2025, per issuer ASX filing https://announcements.asx.com.au/asxpdf/20250826/pdf/06nc9sp162507s.pdf . Historical share counts/prices need basis control. |
| EQU | EQUUS ENERGY LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| EGH | EUREKA GROUP HOLDINGS LIMITED | P2 — parent/security-form check | ISSUER corroborated — Feb 2026 half-year issuer results, ABN 15 097 241 159: https://announcements.asx.com.au/asxpdf/20260224/pdf/06wnlx6brfb1rg.pdf . Historical succession/ISIN pending. |
| EVZ | EVZ LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| FAL | FALCON METALS LTD | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| FXG | FELIX GOLD LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| FEX | FENIX RESOURCES LTD | P3 — routine issuer confirmation | 2026 issuer half-year results corroborate Fenix Resources Ltd ASX FEX; production expansion impacts financial comparisons, not issuer identity. https://announcements.asx.com.au/asxpdf/20260225/pdf/06wq7t7c6ylctc.pdf |
| FDR | FINDER ENERGY HOLDINGS LIMITED | P2 — parent/security-form check | 2026 issuer SPP booklet corroborated; ordinary shares |
| FMR | FMR RESOURCES LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| FML | FOCUS MINERALS LTD | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| FHE | FRONTIER ENERGY LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| GEM | G8 EDUCATION LIMITED | P3 — routine issuer confirmation | 2026 issuer full-year results corroborate G8 Education Limited ASX GEM; financial impairment is not corporate-action issuer change. https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlhl3rrb1dvq.pdf |
| GLN | GALAN LITHIUM LIMITED | P3 — routine issuer confirmation | 2026 issuer January announcement corroborates Galan Lithium Limited ASX GLN; capital placement and Jan trading halt require separate action/status checks. https://announcements.asx.com.au/asxpdf/20260129/pdf/06vplmwtzrrq91.pdf |
| GML | GATEWAY MINING LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| GSS | GENETIC SIGNATURES LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| GL1 | GLOBAL LITHIUM RESOURCES LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| GHY | GOLD HYDROGEN LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| GHM | GOLDEN HORSE MINERALS LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| GRR | GRANGE RESOURCES LIMITED. | P2 — parent/security-form check | 2026 issuer quarterly activities report confirms Grange Resources Limited ASX GRR and ABN 80 009 132 405; historical succession/ISIN pending. https://announcements.asx.com.au/asxpdf/20260729/pdf/071sjv6sp79sgf.pdf |
| GBR | GREAT BOULDER RESOURCES LIMITED | P3 — routine issuer confirmation | 2025 issuer placement notice confirms Great Boulder Resources Limited ASX GBR ABN 70 611 695 955; 204.92m proposed new shares in two tranches, actual allotment pending. https://announcements.asx.com.au/asxpdf/20250623/pdf/06l0gx9hkf67r0.pdf |
| GW1 | GREENWING RESOURCES LTD | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| GWR | GWR GROUP LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — company investor archive lists GWR Group 29 Sep 2026 annual report and Sep 2026 capital return: https://gwrgroup.com.au/investor-centre/asx-announcements/ . Capital return is a corporate action to assess separately; does not establish name/issuer change or current trading status. |
| HMG | HAMELIN GOLD LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| HMX | HAMMER METALS LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| HAV | HAVILAH RESOURCES LIMITED | P3 — routine issuer confirmation | Initial triage completed; no adequate 2026 primary issuer evidence established in this pass. Identity, security form and continuity remain pending. |
| HLO | HELLOWORLD TRAVEL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HMD | HERAMED LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HTM | HIGH-TECH METALS LTD | P3 — routine issuer confirmation | Not independently checked |
| HZN | HORIZON OIL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HCH | HOT CHILI LIMITED | P3 — routine issuer confirmation | Not independently checked |
| HUM | HUMM GROUP LIMITED | P2 — parent/security-form check | 2026 issuer announcement corroborated; ACN 122 574 583 |
| IMA | IMAGE RESOURCES NL | P3 — routine issuer confirmation | Not independently checked |
| IMM | IMMUTEP LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IMU | IMUGENE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IFN | INFRAGREEN GROUP LIMITED | P2 — parent/security-form check | ISSUER corroborated — Sep 2025 issuer announcement, ACN 668 228 742: https://announcements.asx.com.au/asxpdf/20250926/pdf/06pq5qs277zx9w.pdf . Ordinary share evidence: https://announcements.asx.com.au/asxpdf/20250627/pdf/06l66nr9wnwqrw.pdf . 2026 update pending. |
| INN | INNOVAERO TECHNOLOGIES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| IMB | INTELLIGENT MONITORING GROUP LIMITED | P2 — parent/security-form check | December 2025 issuer announcement corroborated; ABN 36 060 774 227; 2026 confirmation pending |
| IVZ | INVICTUS ENERGY LTD | P3 — routine issuer confirmation | Not independently checked |
| ION | IONDRIVE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| INR | IONEER LTD | P3 — routine issuer confirmation | Not independently checked |
| IXR | IONIC RARE EARTHS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| ILA | ISLAND PHARMACEUTICALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| JGH | JADE GAS HOLDINGS LIMITED | P2 — parent/security-form check | 2026 issuer annual report confirms Australian parent and JGH ASX code: https://announcements.asx.com.au/asxpdf/20260330/pdf/06xz4q9ck03gjv.pdf |
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
| LDX | LUMOS DIAGNOSTICS HOLDINGS LIMITED | P2 — parent/security-form check | 2026 issuer SPP announcement confirms LDX, fully paid ordinary shares and attaching options: https://announcements.asx.com.au/asxpdf/20260501/pdf/06z44jt40njxq5.pdf |
| LM8 | LUNNON METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| LUX | LUX COPPER CORP. LTD | P2 — parent/security-form check | July 2026 registry distribution schedule corroborates LUX ordinary shares and escrowed classes; corporate issuer identity requires primary prospectus check: https://www.marketindex.com.au/asx/lux/announcements/distribution-schedule-6A1333970 |
| M24 | MAMBA EXPLORATION LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MKR | MANUKA RESOURCES LTD. | P3 — routine issuer confirmation | Not independently checked |
| MPK | MANY PEAKS MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| MEU | MARMOTA LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MMA | MARONAN METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MM8 | MEDALLION METALS LIMITED. | P2 — parent/security-form check | 2026 issuer SPP announcement confirms Medallion Metals and ABN 89 609 225 023: https://announcements.asx.com.au/asxpdf/20260114/pdf/06v7rvqnccjmlc.pdf |
| MMI | METRO MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MX1 | MICRO-X LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MM1 | MIDAS MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| MNB | MINBOS RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MSV | MITCHELL SERVICES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MLG | MLG OZ LIMITED | P3 — routine issuer confirmation | Not independently checked |
| MVF | MONASH IVF GROUP LIMITED | P2 — parent/security-form check | 2026 issuer trading update confirms Monash IVF Group and MVF: https://announcements.asx.com.au/asxpdf/20260612/pdf/070kb7gmrhsyp8.pdf |
| MXO | MOTIO LTD | P3 — routine issuer confirmation | Not independently checked |
| MRD | MOUNT RIDLEY MINES LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — issuer announcement dated 4 Sep 2026 identifies Mount Ridley Mines Limited, ABN 93 092 304 964: https://www.marketindex.com.au/asx/mrd/announcements/-2-million-placement-to-advance-selectro-and-grass-patch-6A1342191 . ASX archive flags *other historical MRD users* (https://www.asx.com.au/asx/v2/statistics/announcements.do?by=issuerId&issuerId=1787&timeframe=Y&year=2000); issuer-aware historical joins required. Trading halt outcome unresolved. |
| MYR | MYER HOLDINGS LIMITED | P2 — parent/security-form check | 2026 issuer 1H26 results confirm Myer Holdings and ABN 14 119 085 602; apparel integration noted: https://announcements.asx.com.au/asxpdf/20260324/pdf/06xqwdmjdn32mg.pdf |
| NYM | NARRYER METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NMR | NATIVE MINERAL RESOURCES HOLDINGS LIMITED | P2 — parent/security-form check | 2026 FY26 issuer financial report listed by ASX announcement distributor; detailed issuer document still to inspect: https://www.marketindex.com.au/asx/nmr/announcements/fy26-financial-report-2A1700800 |
| NTI | NEUROTECH INTERNATIONAL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NOL | NOBLEOAK LIFE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NMD | NORMANDY MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| NTU | NORTHERN MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NOU | NOUMI LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NVX | NOVONIX LIMITED | P3 — routine issuer confirmation | Not independently checked |
| NYR | NYRADA INC. | P2 — parent/security-form check | 2026 issuer annual report confirms Delaware parent, ARBN 625 401 818 and NYR 1:1 CDIs representing Class A common shares: https://www.nyrada.com/annualreport/2026/ |
| OD6 | OD6 METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| OFX | OFX GROUP LIMITED | P2 — parent/security-form check | 2025 issuer quarterly release confirms OFX Group, ASX OFX, ABN 12 165 602 273; 2026 primary check pending: https://announcements.asx.com.au/asxpdf/20251027/pdf/06r1wrpm6bw5dt.pdf |
| OMA | OMEGA OIL & GAS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| OBL | OMNI BRIDGEWAY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| OCC | ORTHOCELL LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PAR | PARADIGM BIOPHARMACEUTICALS LIMITED.. | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — 27 Apr 2026 ASX-hosted investor presentation identifies Paradigm Biopharmaceuticals (ASX:PAR): https://announcements.asx.com.au/asxpdf/20260427/pdf/06ywp9vzwtwhzl.pdf . The previously recorded voluntary-administration/suspension classification requires a separate *dated* 2026 recheck; April presentation cannot prove current status. |
| PGC | PARAGON CARE LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PC2 | PC GOLD LTD | P3 — routine issuer confirmation | Not independently checked |
| PEN | PENINSULA ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PWR | PETER WARREN AUTOMOTIVE HOLDINGS LIMITED | P2 — parent/security-form check | 2026 issuer investor archive confirms FY26 results and 2 Oct 2026 Wakeling acquisition completion; corporate acquisition not assumed parent change: https://www.pwah.com.au/site/investor-centre/asx-announcements |
| PVT | PIVOTAL METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PLT | PLENTI GROUP LIMITED | P2 — parent/security-form check | 2026 issuer annual report confirms Plenti Group Limited ASX PLT and ACN 166 646 635; historical succession/ISIN still pending. https://announcements.asx.com.au/asxpdf/20260826/pdf/072pnqf0w07w9w.pdf |
| PVE | PO VALLEY ENERGY LIMITED | P3 — routine issuer confirmation | Not independently checked |
| POL | POLYMETALS RESOURCES LTD | P3 — routine issuer confirmation | Not independently checked |
| PPS | PRAEMIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PTX | PRESCIENT THERAPEUTICS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| PSC | PROSPECT RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| QML | QMINES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RZI | RAIZ INVEST LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RDY | READYTECH HOLDINGS LIMITED | P2 — parent/security-form check | 2026 annual report listed 27 Aug 2026 in market announcements; issuer report content/ACN not independently inspected. https://www.marketindex.com.au/asx/rdy |
| REC | RECHARGE METALS LIMITED | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — ASX-filed 26 Sep 2025 AGM announcement identifies Recharge Metals Limited (ASX:REC), ABN 13 647 703 839: https://announcements.asx.com.au/asxpdf/20250926/pdf/06pr0hgjlfwv4f.pdf . ASX historical issuer-code archive lists another REC user (https://www.asx.com.au/asx/v2/statistics/announcements.do?by=issuerId&issuerId=3924&timeframe=Y&year=2020). Current halt/trading outcome unresolved. |
| RNU | RENASCOR RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RMC | RESIMAC GROUP LTD | P2 — parent/security-form check | 2026 issuer annual report confirms Resimac Group Ltd ASX RMC and ABN 67 002 997 935; historical succession/ISIN pending. https://announcements.asx.com.au/asxpdf/20260828/pdf/072s82ylcgtz85.pdf |
| RML | RESOLUTION MINERALS LTD | P3 — routine issuer confirmation | Not independently checked |
| RFG | RETAIL FOOD GROUP LIMITED | P2 — parent/security-form check | 2026 annual report listed 26 Aug 2026; issuer report content/ACN not independently inspected. https://hotcopper.com.au/asx/rfg/announcements/ |
| RIV | RIVCO AUSTRALIA LTD | P3 — routine issuer confirmation | Not independently checked |
| RWL | RUBICON WATER LIMITED | P3 — routine issuer confirmation | Not independently checked |
| RTR | RUMBLE RESOURCES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SLD | "SALUDA MEDICAL | P3 — routine issuer confirmation | Not independently checked |
| SFM | SANTA FE MINERALS LTD | P1 — issuer reuse/status exception | P1 ISSUER CORROBORATED — 29 Apr 2026 ASX-filed shareholder AGM notice identifies Santa Fe Minerals Limited (ASX:SFM): https://announcements.asx.com.au/asxpdf/20260429/pdf/06yzpdsw3fflnd.pdf . Current tradeability not established. |
| SMI | SANTANA MINERALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| STN | SATURN METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SCX | SCX.AI HOLDINGS LIMITED | P2 — parent/security-form check | Issuer website identifies SCX.ai Holdings Limited ASX:SCX and ACN 688 872 095; legal continuity/security form not fully checked. https://scx.ai/investors |
| SEA | SEA FOREST LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SNM | SENTINEL METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SSG | SHAVER SHOP GROUP LIMITED | P2 — parent/security-form check | 2026 issuer annual report confirms Shaver Shop Group Limited ASX SSG and ABN 78 150 747 649; historical succession/ISIN pending. https://announcements.asx.com.au/asxpdf/20260828/pdf/072s0b46twc9bk.pdf |
| SNX | SIERRA NEVADA GOLD INC. | P2 — parent/security-form check | ISSUER corroborated — Apr 2026 AGM notice confirms Sierra Nevada Gold Inc, ARBN 653 575 618 and 1 CDI representing 1 US common share: https://announcements.asx.com.au/asxpdf/20260428/pdf/06yy0pccc500yl.pdf . Foreign issuer; maintain CDI/share distinction. |
| SVL | SILVER MINES LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SHG | SINGULAR HEALTH GROUP LTD | P2 — parent/security-form check | 2026 issuer half-year report confirms Singular Health Group Ltd ASX SHG and ACN 626 548 214; historical succession/ISIN pending. https://announcements.asx.com.au/asxpdf/20260227/pdf/06wvtx18vrbx38.pdf |
| SKY | SKY METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SPZ | SMART PARKING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SVR | SOLVAR LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SXL | SOUTHERN CROSS MEDIA GROUP LIMITED | P2 — parent/security-form check | ISSUER corroborated — 11 Jun 2026 issuer trading update: https://announcements.asx.com.au/asxpdf/20260611/pdf/070hztpwgkz8c7.pdf . MATERIAL MERGER: Seven West Media combined with Southern Cross Media effective 7 Jan 2026; FY26 pro forma metrics assume merger on 1 Jul 2025 and must not be treated as historical statutory comparables. |
| SPD | SOUTHERN PALLADIUM LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SVM | SOVEREIGN METALS LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SGQ | ST GEORGE MINING LIMITED | P3 — routine issuer confirmation | Not independently checked |
| SPL | STARPHARMA HOLDINGS LIMITED | P2 — parent/security-form check | ISSUER corroborated — 26 Aug 2026 FY26 results issuer release: https://www.marketindex.com.au/asx/spl/announcements/fy26-key-financial-results-and-annual-report-3A699854 . Historical succession/ISIN pending. |
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
| TOK | TOLU MINERALS LIMITED. | P2 — parent/security-form check | 2026 issuer annual report corroborates Tolu Minerals Limited; PNG-incorporated, ARBN 657 300 359. https://announcements.asx.com.au/asxpdf/20260331/pdf/06y0b7kswgq80l.pdf ; PNG registration https://announcements.asx.com.au/asxpdf/20250331/pdf/06h66ygfd759bl.pdf . Security form/ISIN pending. |
| TOR | TORQUE METALS LIMITED.. | P2 — parent/security-form check | 2026 issuer half-year financial statements corroborate Torque Metals Limited, ABN 44 621 122 905, ASX TOR. https://announcements.asx.com.au/asxpdf/20260316/pdf/06xhf3m202xd16.pdf ; historical succession/ISIN pending. |
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
| WJL | WEBJET GROUP LIMITED | P2 — parent/security-form check | 2026 issuer results corroborate Webjet Group Limited ACN 679 116 762 ASX WJL: https://announcements.asx.com.au/asxpdf/20260520/pdf/06zs1jh6zq9y1p.pdf . Material 30 Sep 2024 demerger from Web Travel Group; predecessor operating results must be segmented, not joined as same listed issuer: https://announcements.asx.com.au/asxpdf/20241127/pdf/06bwtcz6mvrwpk.pdf . 19 May 2026 trading halt does not establish present tradeability. |
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


### P2 batch 4 (13 October 2026)

Ten reviewed: JGH, LDX, LUX, MM8, MVF, MYR, NMR, NYR, OFX, PWR. Most issuer identities corroborated; LUX relies on registry disclosure and NMR on announcement listing, so full issuer-document checks remain. NYR is a US-incorporated issuer whose ASX security is a 1:1 CDI, not ordinary Australian stock. LDX placement/SPP attaching options and MYR apparel integration are corporate-action flags. PWR acquisition concerns an operating subsidiary/business, not demonstrated change of listed parent. 33/46 P2 reviewed, 13 unreviewed. No CSV exclusions. This is not a trading-status verification.


### P2 batch 5 (13 October 2026)

Ten tickers reviewed: PLT, RDY, RMC, RFG, SCX, SSG, SNX, SHG, SXL, SPL. **Only SCX has a current issuer-owned identity source from this pass.** RDY/RFG/SNX have 2026 announcement-listing evidence but underlying issuer filings were not inspected. SXL/SPL historical index holdings are not 2026 confirmation. PLT/RMC/SSG/SHG remain evidence gaps. These are review statuses, not completed legal-parent/security-form verification. P2 reviewed 43/46; three not yet reviewed. P2/P3 not yet reviewed 223. No CSV exclusions or trading-status conclusion.


### P2 batch 6 — final initial reviews (13 October 2026)

TOK: PNG-incorporated issuer, ARBN 657 300 359; TOR: Australian issuer, ABN 44 621 122 905; WJL: ACN 679 116 762 and material **30 September 2024 demerger** from Web Travel Group (WEB). Primary ASX filing links recorded in rows. **46/46 P2 rows now initially reviewed**, but many have provisional/old/third-party-only evidence and parent/security-form details remain unresolved. **Do not mark Step 1.3.2 complete.** Remaining 220 P3 initial checks; no changes to 316-company universe.


### P2 evidence-gap follow-up (13 October 2026)

New 2026 issuer-authored ASX filings corroborate PLT, RMC, SSG, SHG, and GRR (primary URLs in rows). These replace missing or third-party-only evidence; they do **not** establish full historical legal-entity continuity, ISIN or tradeability. Remaining weaker-evidence P2 cases include ACE, AIH, ECT, EGH, IFN, SNX, SXL and SPL. No changes to the 316 candidate rows.


### P2 evidence follow-up (13 October 2026)

Issuer-source identity corroboration added for ACE, AIH, ECT, EGH, IFN, SNX, SXL, SPL. **Critical historical-data flags:** ECT 1:15 consolidation (26 Aug 2025); SXL/Seven West Media merger (7 Jan 2026) with FY26 pro-forma versus statutory basis; SNX US common stock represented by 1:1 CDIs. AIH/Matrix proposed acquisition is not treated as completed without implementation evidence. These updates close selected issuer-source gaps only, not full legal-entity succession, ISIN history or Step 1.2 tradeability. No change to 316 candidates.


### Priority 3 batch 1 (13 October 2026)

Initial review of 14D, ACW, ADH, AI1, AVM, AGR, AUQ, ARN, AQZ, AGE. Issuer-primary 2026 evidence for 14D, ACW, ADH, AVM and AGR; ARN/AGE have 2026 announcement-listing evidence, AQZ issuer-primary 2025 evidence, and AI1/AUQ lack adequate primary evidence in this pass. Corporate action flags: 14D Aurora project ownership; AGR proposed ordinary share issue (not proven completed). 10/220 P3 initially reviewed; 210 P3 remain. No trading-status or full issuer-lineage clearance and no change to 316 candidates.


### P3 batch 2 — 30-row initial triage (13 October 2026)

Codes: ATH, ALU, ALV, ARR, AL3, ANX, AZY, AON, APX, AR9, ARD, A1N, ALA, AMD, AS1, A11, AKN, AEE, AWJ, AUE, AHC, AUZ, AVL, BM1, BAS, BVR, BKY, BWN, BIO, BB1. **2/30** have new issuer-specific evidence (ALU, ALV); **28/30** are queued for issuer-source confirmation, NOT marked verified. ALU is a material historical ticker reuse / new issuer: 2026 Alurion IPO/demerger from BRE versus former Altium (ALU) delisted 2024. ALV placement/quotation history needs share-capital checks. This was a 30-row triage, not 30 completed issuer confirmations. 40/220 P3 initially reviewed/triaged, 180 untouched. No candidate exclusions or tradeability conclusions.


### P3 batch 2 primary-evidence follow-up (13 October 2026)

Upgraded AZY (2025 primary issuer and option expiry), AR9 (2025 primary issuer plus proposed Spirion acquisition), and APX (2026 primary issuer AGM). This is issuer corroboration only; AR9 acquisition completion remains unverified. From 30 batch-2 rows: ALU, ALV, ATH, AZY, AR9, APX have issuer-specific evidence; 24 remain triage-only. No tradeability clearance or universe changes.


### P3 batch 3 (13 October 2026)

30 initial triages: BLG, BOA, BML, BOT, BPM, BCM, BRK, BUB, CRS, CVV, CMA, CNB, CCV, CPN, CXU, CTM, CAF, CTS, CTT, CLV, CBE, COD, COI, CYM, DAL, DTR, DLI, DEV, DCC, DXB. Seven have issuer evidence (BLG, BOA, BML, BOT, BUB, DTR, DEV); DCC has issuer archive only, BCM secondary index only, and 21 await primary corroboration. 70/220 P3 processed, 150 untouched. No exclusions or trading status conclusions.


### P3 batch 3 evidence follow-up (13 October 2026)

Primary ASX issuer filings now recorded for BPM, BRK, CRS, CCV, CPN, CAF, DXB, CXU, CTT, BB1, BIO, CYM. Seven are 2026 evidence and five 2025 evidence. Batch-3 evidence now 19/30 issuer-specific, plus DCC archive and BCM secondary index; 9 triage-only. Overall 70/220 P3 initially processed, 150 untouched. Issuer corroboration does not establish full lineage or current trading status.


### P3 batch 4 — next 30 initial reviews (13 October 2026)

DUG, EIQ, EDE, ELT, EL8, EML, EMP, EMV, ENR, ETM, EQU, EVZ, FAL, FXG, FEX, FMR, FML, FHE, GEM, GLN, GML, GSS, GL1, GHY, GHM, GBR, GW1, HMG, HMX, HAV. Primary 2026 issuer evidence for EL8, EML, FEX, GEM, GLN; 2025 issuer evidence DUG; 2026 ASX filing reproducing Echo IQ announcement EIQ. Remaining 23 need primary issuer confirmation. Historical-action flags: EL8 options/performance rights; GLN placement/trading halt; EIQ proposed financing terms not proven final. **100/220 P3 initially processed, 120 untouched.** No candidate exclusions, no current tradeability conclusions.


### P3 batch 4 evidence follow-up (13 October 2026)

Upgraded EMV (2026 primary issuer), ENR and GBR (2025 primary issuers). ENR 2025 placement and GBR two-tranche placement require confirmation of allotted shares before capitalisation modelling. Batch 4 now 10 issuer-evidence records and 20 provisional. P3 100/220 initially processed, 120 untouched. Full historical legal continuity and tradeability remain outstanding.
