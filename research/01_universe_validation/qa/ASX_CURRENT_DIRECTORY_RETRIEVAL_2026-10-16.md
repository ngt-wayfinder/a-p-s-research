# ASX current directory retrieval attempt — 16 October 2026

## Authoritative source
- Official ASX directory: https://www.asx.com.au/markets/trade-our-cash-market/directory.html
- Bulk CSV endpoint identified from public ASX API references: https://www.asx.com.au/asx/research/ASXListedCompanies.csv
- ASX directory includes a separate trading-status indication; directory membership alone is **not** evidence that a security is unsuspended.

## Attempt and outcome
- Web retrieval of directory HTML succeeded and confirmed the official directory exists.
- Web retrieval of the CSV URL failed with unsupported `text/csv` content type.
- Direct container download of the CSV URL failed (container network resolution/download unavailable).
- **No ASX CSV bytes obtained, no 316-code join executed, and no current listing/trading status independently established.** Do not treat the endpoint's existence as proof of successful retrieval or fresh matching.

## Resume steps
1. Download the ASX CSV through a CSV-capable network/browser client and record retrieval date, file hash, headers and row count.
2. Join ASX code against the 316-company candidate register. Check issuer names/changes and directory coverage.
3. Check suspension/trading-status indicators and official reinstatement/delisting announcements for exceptions.
4. Combine with issuer operating-company evidence; only then change the authoritative Level 1 decision register.
5. Preserve `REVIEW_PENDING` for unresolved material discrepancies. Do not require blanket ISIN or full historical capital-action verification.
