# ASX issuer-report downloader — Colab research handover (16 October 2026)

## Scope and repository state

Repository: `ngt-wayfinder/a-p-s-research`. Working branch: `feature/issuer-report-downloader`. The prior draft PR #8 should be inspected rather than assumed merged. These handover notes are on the feature branch only. No unattended collection is authorised or enabled.

The existing `scripts/download_issuer_reports.py` is a separate experimental implementation and must **not** be confused with the interactive Version 2 Colab downloader. `scripts/asx_issuer_reports_google_colab.py` is a *limited first-page title-audit prototype*, not the full Version 2 PDF downloader. `scripts/requirements_google_colab.txt` and `docs/GOOGLE_COLAB_RESEARCH.md` describe that prototype. The full experimental Version 2 Colab baseline is now committed as `scripts/asx_batch_v2_google_colab.py` (176 lines); it has not been repaired or rerun after the commit. See `docs/colab_handover/STATUS.md`.

## Research objective

Build an auditable, reproducible mechanism for collecting current issuer annual, half-year and applicable quarterly reports for **316 provisional ASX operating-company candidates**, as input to evidence-based Level 1 eligibility screening. Do not alter eligibility decisions merely because a document downloaded. Source register was previously identified as `research/01_universe_validation/registers/LEVEL_1_SCREENING_ELIGIBILITY_REGISTER.csv`; confirm its present location and schema in GitHub.

## Discovery investigation (observed during Colab tests)

- Website announcement pages expose `https://asx.api.cmfyapp.com/asx-research/1.0` API calls.
- Predictive search `/search/predictive?searchText=ACE&useBondsLookup=true` yields a ticker-specific `xidEntity`. **Use `xidEntity`, not `xid`**, for announcement discovery.
- `/markets/announcements?entityXids=<id>&page=<n>&itemsPerPage=25&summaryCountsDate=<YYYY-MM-DD>` supports pagination. Confirm completeness against `data.count`, de-duplicate by `documentKey`.
- `/file/<documentKey>` returned PDF content in controlled tests. Do not append `&v=undefined`.
- An older `/companies/<ticker>/announcements` endpoint returned a limited five-item response and was unsuitable for complete history.
- These are unofficial/public website endpoints, **not evidence of permission for automated bulk collection**.

## Version history and measured outputs

1. Single-company ACE exploratory run: 233 announcements, three PDFs downloaded. This established technical reachability, not financial-content accuracy.
2. Five-company V1 test (`ACW, ACE, BHP, CSL, WDS`): 13 PDFs downloaded; selection errors included stale CSL annual, CSL investor presentation selected as half-year, WDS briefing transcript selected as half-year. Hence V1 was **not accepted**.
3. Five-company V2 run (`asx_batch_v2.zip`): 15 company/category register rows; 5 `SUCCESS`, 8 `REVIEW_REQUIRED`, 2 `NOT_FOUND_REVIEW_REQUIRED`; 87 audited candidates = 74 `STALE`, 8 `CONTENT_REJECTED`, 5 `ACCEPTED`. All five announcement histories matched API totals: ACW 1078, ACE 233, BHP 1878, CSL 2140, WDS 1171.
4. BHP-only V2 rerun (`asx_batch_v2(1).zip`): 3 register rows; 1 `SUCCESS` (annual), 2 `REVIEW_REQUIRED` (half-year, quarterly); **21** audited candidates = 16 `STALE`, 4 `CONTENT_REJECTED`, 1 `ACCEPTED`. BHP announcement discovery: 1878/1878. A prior chat response said 20 candidates; inspection of the actual ZIP shows **21**.
5. BHP-only ZIP contained five PDFs (BHP annual plus ACW annual, half-year, quarterly and ACE half-year), despite its register covering BHP only. This is **stale output-directory contamination**, not evidence that other tickers ran in the BHP-only test.

## Company/category V2 outcomes

| Code | Annual | Half-year | Quarterly |
|---|---|---|---|
| ACW | SUCCESS | SUCCESS | SUCCESS |
| ACE | REVIEW_REQUIRED | SUCCESS | REVIEW_REQUIRED |
| BHP | SUCCESS | REVIEW_REQUIRED | REVIEW_REQUIRED |
| CSL | REVIEW_REQUIRED | REVIEW_REQUIRED | NOT_FOUND_REVIEW_REQUIRED |
| WDS | REVIEW_REQUIRED | REVIEW_REQUIRED | NOT_FOUND_REVIEW_REQUIRED |

`SUCCESS` means heuristic automated acceptance, **not** independently verified correct fiscal period, report type or financial statement content. Quarterly reporting may be inapplicable for some issuers.

## Known defects / next engineering work

1. BHP 2026 half-year PDF (118 pages) was rejected for insufficient statement markers; financial statements may be outside the first 12/last 8 inspected pages. Improve targeted/full-document extraction with bounded CPU/memory.
2. BHP July 2026 quarterly activities PDF (25 pages) was rejected because its content did not match Appendix 4C/5B-oriented terms. Distinguish activities reports from cash-flow reports and verify reporting applicability.
3. BHP FY2026 annual accepted (250 pages), but content identity and period still need independent validation.
4. ACE FY2026 annual Appendix 4E, WDS 2025 annual and BHP Form 20-F may be false rejects. Review audited candidates and improve page extraction/marker rules; avoid accepting investor presentations/transcripts.
5. CSL discovery/ranking and stale-age thresholds require review. Thresholds used were annual 520 days, half-year 340, quarterly 220 — **heuristics**, not legal deadlines.
6. Create unique per-run output directories or clear stale outputs before each run; ZIP membership must match the run's register.
7. Add structured error categories, source metadata, SHA-256, report-period classification, reproducible tests, and manual review queue.
8. Requested scheduling safeguards: **10 companies per tranche; 15 seconds between companies; 15 minutes between tranches; stop on HTTP 403/429**. These were committed to the limited Colab prototype only; **not** incorporated or tested in the full Version 2 downloader. Enforce per-request limits as well if authorised.
9. Future architecture proposal: GitHub Actions for scheduled execution; durable external storage for PDFs; GitHub for code and compact registers. **No workflow has been activated.**

## Access and compliance gate

ASX website terms may restrict automated scraping/downloading; obtain ASX permission or another licensed/authorised source before any unattended or bulk access. Delays are load-reduction safeguards, not a substitute for permission. The limited Colab prototype deliberately requires `ASX_AUTOMATED_ACCESS_AUTHORISED=YES` before making requests. Never attempt to bypass 403/429 responses.

## How to resume safely

1. Read this README, `docs/GOOGLE_COLAB_RESEARCH.md`, the relevant scripts, current branch/PR and roadmap.
2. Inspect the committed V2 baseline and retrieve the actual test ZIPs from conversation/user attachments; **do not infer ZIP contents from chat alone**.
3. Repair BHP content validation and output isolation in a distinct `*_google_colab.py` full V2 script. Add unit tests with local fixtures; do not issue bulk ASX requests until access is authorised.
4. Re-run a controlled, authorised BHP-only validation; compare annual/half-year/quarterly document identity, report period, statement markers and output files.
5. After quality gate passes, return to five-company regression and only then plan scaling to 316.

## Files that must be preserved outside GitHub

- `asx_batch_5.zip` (V1, 13 PDFs)
- `asx_batch_v2.zip` (five-company V2)
- `asx_batch_v2(1).zip` (BHP-only V2)
- `asx_batch_v2.py` (full V2 source, local/chat artifact)

The full V2 Python source is now committed as `scripts/asx_batch_v2_google_colab.py`; the ZIP archives and copied PDFs have **not** been committed. Avoid committing large PDF archives without an explicit storage decision.

## Handover status update

On 16 October 2026, the complete experimental Version 2 baseline was committed at `scripts/asx_batch_v2_google_colab.py`. For the definitive code inventory, historical results, defects, access safeguards and next steps, see [`STATUS.md`](STATUS.md). The original test ZIPs and issuer PDFs are intentionally not in GitHub.
