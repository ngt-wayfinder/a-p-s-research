# Automated issuer-report downloader (experimental)

This tool reads `ASX_Code` from the existing 316-company Level 1 CSV. It does **not** modify eligibility assessments.

## Source limitations

The ASX MarkitDigital endpoint used for discovery is **undocumented and unverified for permitted bulk automation**. It may be retired, blocked, paginated, capped or require an access token. The delivery endpoint is not proof of discovery or redistribution rights. Obtain confirmation of permitted automated access before a 316-company run. Do not circumvent rate limits or access controls. A `NOT_FOUND_IN_RESPONSE` result is **not** proof that the issuer did not file a report.

## Install and run

```sh
python -m pip install requests
python scripts/download_issuer_reports.py --codes ACW,ACE --dry-run
python scripts/download_issuer_reports.py --codes ACW,ACE
# Only after source/access validation:
python scripts/download_issuer_reports.py
```

Run from repository root. Use `--input path/to/codes.csv` for another ASX_Code CSV, `--output path` to change destination, and `--delay 5` to reduce request frequency.

Outputs: `research/issuer_reports/download_register.csv`, `exceptions.csv`, and `pdf/<ASX_CODE>/<report_type>/<document_key>.pdf`. Register writes are atomic and occur after each company. Re-running skips already downloaded matching document keys and retains the latest record for each company/type. PDF files are validated by header and SHA-256 recorded. Do not commit downloaded PDFs without checking source terms and repository storage limits.

## Known gaps requiring resolution before production

* Verify live endpoint and response schema against ACW and ACE.
* Confirm whether discovery includes all recent reports and how to paginate; a 200-item response may be capped.
* Verify whether PDF delivery requires a documented token or permitted alternative.
* Validate report period from document content/metadata; current CSV leaves Reporting_Period empty rather than inventing it.
* Add official company-website fallback and robust retry/backoff after source rights are confirmed.
* Treat quarterly 4C/5B as applicable only to reporting issuers; missing category is not necessarily an exception.
* This experimental version is **not yet an end-to-end validated downloader**.
