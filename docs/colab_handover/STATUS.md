# Issuer-report downloader status — 16 October 2026

## Committed source

- `scripts/asx_batch_v2_google_colab.py`: full experimental V2 Colab baseline, 176 lines, committed in `7145acaf3fc238d66a08303ea81da5acae478dba`. No subsequent repair or rerun is claimed.
- `scripts/asx_issuer_reports_google_colab.py`: separate, limited first-page announcement-title prototype; NOT the full V2 downloader.
- `scripts/requirements_google_colab.txt`: dependencies.
- `docs/GOOGLE_COLAB_RESEARCH.md`: prototype setup and limitations.
- `docs/colab_handover/README.md`: research history and evidence.
- `docs/colab_handover/NEXT_CHAT_PROMPT.md`: takeover prompt.

## Historical results

| Run | Results |
|---|---|
| Five-company V2 (ACW, ACE, BHP, CSL, WDS) | 5 of 15 report categories accepted; 87 candidate records audited |
| BHP-only V2 | 1,878 of 1,878 announcements retrieved; annual accepted, half-year and quarterly review required; 21 candidates audited (1 accepted, 4 content rejected, 16 stale) |

The BHP-only ZIP also included four ACW/ACE PDFs left over from an earlier run; this was output-directory contamination, not proof that those issuers were processed in the BHP-only test.

## Outstanding engineering and compliance

1. Improve PDF statement validation beyond the sampled pages, with bounded resource usage.
2. Distinguish quarterly activities reports from quarterly cash-flow reports; assess issuer-specific reporting applicability.
3. Isolate or clear run output before ZIP packaging.
4. Add explicit stop behavior for HTTP 403/429 and an authorisation gate before any automated access.
5. Implement and test requested pacing in full V2: 10 companies per tranche, 15 seconds between companies, 15 minutes between tranches. These safeguards currently exist only in the limited prototype.
6. Add local regression tests and document report-period verification. Re-run BHP-only before five-company regression and 316-company scale-up.

## Repository and evidence policy

All listed source files and handover documents are on `feature/issuer-report-downloader`; do not assume the branch or PR #8 is merged. No GitHub Actions bulk schedule has been enabled. Do not commit the approximately 20 MB test ZIP archives or copied issuer PDFs. The actual ZIPs remain local/conversation evidence and are not reproducible from GitHub alone. Rate limits do not confer permission for bulk ASX access; confirm rights or use an authorised source before unattended collection.


## 16 October 2026 — offline validator development
- Added `scripts/issuer_pdf_validation.py` (offline, bounded full-PDF text inspection and conservative annual/half-year/quarterly classification).
- Added `tests/test_issuer_pdf_validation.py` (six synthetic tests, including late-page half-year statements and quarterly activities without cash-flow statements).
- These are **committed but tests have not yet been executed in a Python environment**. No BHP rerun has occurred.
- Known limitations: PDF text extraction cannot validate scanned/image-only documents; period extraction may flag documents with comparative reporting dates; issuer identity, financial-period expectations and quarterly reporting applicability still require external metadata and/or analyst review.
- The module is **not yet integrated** into the full V2 Colab downloader. Next: execute tests, repair any failures, implement output isolation and 403/429 stop handling, then integrate the module into a new V3 Colab script.
