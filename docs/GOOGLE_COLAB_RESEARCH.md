# Google Colab research scripts (experimental)

## Purpose

This folder documents interactive, non-production issuer-announcement experiments.

## Files

- `scripts/asx_issuer_reports_google_colab.py`: small five-ticker exploratory announcement-title audit. It does **not** download or validate PDFs, does not retrieve full pagination, and is not the tested Version 2 downloader.
- `scripts/requirements_google_colab.txt`: Python dependencies for Colab experiments.
- `scripts/download_issuer_reports.py`: separate pre-existing experimental production-oriented script; **not** interchangeable with the Colab prototype.

## Execution

1. Open Google Colab and clone/check out `feature/issuer-report-downloader`.
2. Install dependencies: `pip install -r scripts/requirements_google_colab.txt`.
3. Review the source and obtain confirmation that automated access to the relevant ASX endpoints is authorised.
4. The script requires an explicit `ASX_AUTOMATED_ACCESS_AUTHORISED=YES` environment setting before making requests.
5. Execute `python scripts/asx_issuer_reports_google_colab.py`.
6. Examine `/content/asx_colab_candidate_audit.csv`. Matches are title-only and are **not** validated financial statements.

## Important limitations

- Public accessibility of an API does not establish permission for automated collection.
- The Colab research file intentionally checks only the first announcement page.
- No unattended GitHub Actions schedule should run these scripts until source access rights and production safeguards have been established.
- The Version 2 Colab PDF downloader used in the conversation remains a separate uncommitted research artifact pending exact source capture and verification.

## GitHub policy

Keep interactive Colab experiments suffixed `_google_colab.py`, and keep them separate from production code, scheduling workflows and research eligibility registers.
