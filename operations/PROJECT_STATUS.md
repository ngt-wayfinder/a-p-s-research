# Project status — 15 October 2026

**Source of truth for strategy:** [Roadmap](../RESEARCH_ROADMAP.md). This is a concise operational snapshot; confirm current branch/HEAD and authoritative CSV before relying on counts.

- Phase 0: historical numerical screen complete, from 1,923 securities to 316 provisional operating candidates (318 less GDF/GDI).
- Step 1: **in progress**. Issuer identity status classification: **316/316** (311 primary issuer, 4 primary ASX, 1 primary historical issuer).
- Historical continuity: **316/316** still have open partial gaps. Security-form evidence: **310/316** incomplete. Dated trading-status review: **316/316** open.
- Level 1 screening eligibility: **not assessed**. No company is authorised to enter Step 2 solely from identity flags.
- Steps 2–12: not started.
- Current engineering task: implement and validate the repository restructure on `repository-restructure`; merge and establish `research-baseline-v1.0` only after acceptance.
- Next research task after baseline: create evidence-based Level 1 eligibility register for 316 candidates.

**Do not conflate** a 316-row identity classification with complete investment due diligence. Counts are from the 15 October roadmap reconciliation and must be recalculated when data changes.

## Repository link audit — 15 October 2026

- Audited all **66 Markdown files** in the `repository-restructure` Git tree using the complete tracked-file path set.
- **Zero unresolved internal Markdown file-path links** remained after repair.
- Scope: standard inline Markdown links with relative file paths, ignoring external URLs and fragments; does **not** validate heading anchors, reference-style links, or external destinations.
- Full GitHub Actions execution and Python regression tests remain pending; baseline tag must not be created until those checks pass.

## Level 1 eligibility register reconciliation — 16 October 2026

Parsed `research/01_universe_validation/registers/LEVEL_1_SCREENING_ELIGIBILITY_REGISTER.csv` from `main` with a quote-aware CSV parser (including escaped quotes and embedded commas). Source blob SHA: `8d3e6add77b2dcade4d2d12c0fc694a2244c3434`.

| Level_1_Decision | Count |
|---|---:|
| `ELIGIBLE` | 0 |
| `QUARANTINED` | 0 |
| `REVIEW_PENDING` | 316 |
| **Total** | **316** |

Integrity checks: 316 data rows; 316 unique ASX codes; 25 header columns; zero malformed-width rows, duplicate codes, or unexpected decision values. These are **recorded decisions**, not an independent re-assessment of the underlying evidence. Recent 14D/ACF/ACW/ACE evidence work does not itself satisfy all Level 1 gates. No Step 2 eligible cohort is established. Prior statements above describing the Level 1 register as not yet created are superseded by this reconciliation; update `NEXT_ACTIONS.md` separately to reflect the completed register creation and remaining gate assessments.
