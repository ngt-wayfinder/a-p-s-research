# Repository structure and file ownership

**Status:** Proposed target structure; **not yet migrated**.  
**Documented:** 15 October 2026.  
**Authority:** [RESEARCH_ROADMAP.md](../RESEARCH_ROADMAP.md) defines research goals, step numbers, acceptance gates and progress. This document defines where artifacts should live and how to migrate them safely.

## 1. Principles

1. Preserve the full audit trail, source URLs, dates, evidence identifiers and all 316 candidate records.
2. Give each current register a single authoritative location and document its owner, schema and update policy.
3. Separate raw input, transformed working data, approved outputs, live evidence, QA and historical batch artifacts.
4. Group artifacts by research function, **not** by individual batch/date; keep historical batches under their originating workstream.
5. Create later-stage directories only when needed. Folder prefixes are **organisational labels, not replacements for roadmap step IDs**.
6. Make scripts independent of the shell's working directory; resolve paths from the repository root or explicit arguments.
7. Do not interpret issuer-identity confirmation as security, historical continuity, trading-status or Level 1 eligibility sign-off.

## 2. Target layout (illustrative, not yet present)

```text
a-p-s-research/
├── README.md                        # Entry point and authoritative file index
├── RESEARCH_ROADMAP.md              # Research objective, steps and status (existing)
├── docs/
│   ├── REPOSITORY_STRUCTURE.md      # This design and migration guide
│   ├── RESEARCH_METHODOLOGY.md      # Future detailed scoring and decision rules
│   └── DATA_DICTIONARY.md           # Future schema, statuses and source definitions
├── data/
│   ├── raw/                         # Immutable downloaded/source snapshots
│   ├── working/                     # Derived provisional candidate datasets
│   └── outputs/                     # Approved/final exported universes
├── research/
│   ├── 01_universe_validation/
│   │   ├── identity/                # Issuer, legal-name and ticker lineage investigations
│   │   ├── corporate_actions/       # Capital/security changes and exceptions
│   │   ├── trading_status/          # Dated suspension/tradeability checks
│   │   ├── registers/               # Authoritative current matrices, ledgers, eligibility
│   │   ├── qa/                      # Cross-checks, anomalies, reconciliations
│   │   └── archive/                 # Historical batch reports and checkpoints
│   ├── 02_market_data/              # Price, liquidity and market-cap analysis
│   ├── 03_financial_analysis/        # Financial resilience and screening
│   ├── 04_dilution_and_catalysts/   # Capital structure, dilution and catalysts
│   ├── 05_shortlisting/             # Ranked screening decisions
│   ├── 06_deep_research/            # Detailed company dossiers
│   ├── 07_valuation_and_portfolio/  # Scenarios, position sizing and portfolio
│   └── 08_monitoring/               # Future monitoring
├── scripts/                          # Reproducible audit/ingestion scripts
└── .github/workflows/                # Optional automated checks when implemented
```

Empty future directories need not be committed. No proposed filename above implies the file already exists.

## 3. Existing files and intended destinations

| Existing file/location | Intended location | Role / migration caution |
|---|---|---|
| `RESEARCH_ROADMAP.md` | **Stay at root** | Authoritative roadmap and decision gates; rewrite moved relative links |
| `data/raw/ASXListedCompanies.csv` | `data/raw/` | Source directory snapshot; record snapshot/cutoff date |
| `data/working/operating_candidates.csv` | `data/working/` | Provisional population; scripts currently reference root path |
| `research/01_universe_validation/registers/STEP_1_3_2_EVIDENCE_MATRIX.csv` | `research/01_universe_validation/registers/` | Working 316-company status matrix; **not** a Level 1 approval register |
| `research/01_universe_validation/registers/STEP_1_3_2_4_PRIMARY_EVIDENCE_LEDGER.csv` | Same `registers/` | Primary evidence IDs and provenance |
| `research/01_universe_validation/registers/STEP_1_3_2_4_COMPLETE_VERIFICATION_REGISTER.csv` | Same `registers/` | Historical verification coverage; inspect scope and cutoff before treating as current |
| `research/01_universe_validation/registers/STEP_1_3_2_4_UNRESOLVED_EXCEPTIONS.csv` | Same `registers/` | Open exceptions; reconcile against later updates |
| `research/STEP_1_3_2_4_IDENTIFIER_QA.csv` | `research/01_universe_validation/qa/` | Identifier integrity checks |
| `research/STEP_1_3_2_EVIDENCE_MATRIX_README.md` | Alongside matrix in `registers/` | Matrix interpretation, status caveats |
| `research/01_universe_validation/archive/STEP_1_3_2_4_COMPREHENSIVE_VERIFICATION_REPORT.md` | `research/01_universe_validation/archive/` | Dated report, not automatically latest state |
| `research/STEP_1_3_2_TICKER_CHANGE_REGISTER.md`, `research/STEP_1_3_2_NAME_CONTINUITY_REVIEW.md`, `research/STEP_1_3_2_ISSUER_CONTINUITY_QUEUE.md` | `research/01_universe_validation/identity/` | Historical identity work and unresolved lineage |
| `research/STEP_1_3_2_CORPORATE_ACTION_EXCEPTIONS.md` | `research/01_universe_validation/corporate_actions/` | Corporate-action exceptions |
| `research/trading_status/*` | `research/01_universe_validation/trading_status/` | Preserve dated per-ticker reports and register |
| `research/identity_checks/*` | `research/01_universe_validation/identity/` | Focused identity investigations |
| `research/checkpoints/*` | `research/01_universe_validation/archive/checkpoints/` | Recovered execution state; retain for traceability |
| `research/*BATCH*`, dated verification reports and receipts | `research/01_universe_validation/archive/` | Preserve original files and links; distinguish from live registers |
| `research/*QA*.json` and crossmatch QA outputs | `research/01_universe_validation/qa/` | Keep associated batch receipts in archive when necessary |
| `scripts/*` | **Stay in `scripts/`** | Fix default paths and validate execution |
| `chatgpt-connection-test.md`, `research/GITHUB_ACCESS_TEST.md` | `research/01_universe_validation/archive/` or a clearly labelled test archive | Operational tests, not investment evidence |

Other Step 1 audit and status documents should be classified individually before moving; do not automatically archive an active queue or assume an older status summary is authoritative. A complete old-path → new-path manifest must cover **every file** before migration.

## 4. New Level 1 register

Create `research/01_universe_validation/registers/LEVEL_1_SCREENING_ELIGIBILITY_REGISTER.csv` **after migration** (or at the existing research path if migration is postponed). One row per provisional candidate. Suggested fields:

- ASX code; current issuer/legal identity and evidence reference/date.
- Security class and material corporate-action attribution.
- Dated trading/suspension assessment.
- Operating-business versus investment-vehicle classification.
- Level 1 decision: `REVIEW_PENDING`, `ELIGIBLE` or `QUARANTINED`.
- Missing evidence, conflict/risk flags, reviewer date, decision rationale and linked primary sources.

**Do not bulk-mark all 316 eligible** from the identity-classification field. Open historical/security/trading gates remain independent.

## 5. Link and script safety

The pre-migration spot check on 15 October 2026 found **64 local Markdown links** in three central documents (48 roadmap, 6 matrix README, 10 comprehensive report), with **zero broken at their current paths**. This is a *limited baseline*, not an all-repository link audit. Moving files will change relative-link resolution.

Known script dependencies include:
- `scripts/audit_operating_duplicates.py`: default `data/working/operating_candidates.csv`.
- `scripts/verify_asx_directory.py`: default candidates at root; directory/output supplied by flags.
- `scripts/crossmatch_asx_code_changes.py`: documented usage references root candidates.
- `scripts/audit_primary_code_changes.py`: default matrix at `research/01_universe_validation/registers/STEP_1_3_2_EVIDENCE_MATRIX.csv` and output under `research/`.

When migrating, update every Markdown relative link, literal path in prose, script default, documented command, and any GitHub workflow. Validate references from the **new containing directory**, not merely from repository root. Prefer relative Markdown links within the repo and explicit root-aware path handling in scripts. External URLs and evidence IDs must remain unchanged.

## 6. Controlled migration procedure and acceptance gates

1. Inventory every tracked file and produce a checked old→new manifest; classify current, historical, raw, working, QA, code or operational test.
2. Identify the authoritative register for each subject and its evidence cutoff. Preserve historical snapshots without overwriting later work.
3. Move files in a reviewable commit or tightly scoped commits; preserve original content, source URLs and evidence IDs.
4. Rewrite links in all Markdown files and any literal file references; update scripts and usage examples.
5. Validate **all** internal Markdown links and file-path references; test scripts with representative input and compare outputs.
6. Reconcile record counts, unique tickers, CSV schemas, evidence IDs, file hashes and exceptions before/after.
7. Update root `README.md`, roadmap links and data dictionary; explicitly document remaining limitations.
8. Only then begin the Level 1 eligibility register under the approved authoritative location.

**Acceptance criteria:** Every existing file accounted for; zero broken local links; all four scripts work with new paths; 316 unique candidate tickers preserved without unintended matrix changes; evidence references and archived batches accessible; one documented authoritative current register per subject; roadmap remains navigable.

## 7. Current state

**Documentation only.** This file describes the target architecture. The existing repository has **not been reorganised**; use current paths in the roadmap until a separate migration commit is completed and validated.
