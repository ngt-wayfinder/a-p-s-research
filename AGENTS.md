# Instructions for research agents

Read `README.md`, `operations/PROJECT_STATUS.md`, `operations/NEXT_ACTIONS.md`, `RESEARCH_ROADMAP.md`, and `docs/REPOSITORY_STRUCTURE.md` in that order. Confirm repository branch and HEAD before editing.

## Non-negotiable controls
- Objective: find 5–10 evidence-supported opportunities; do not optimise for verification counts alone.
- Treat 316 candidate issuer identities as *classified*; do not assume full continuity, trading, security or eligibility verified.
- Use issuer-authored ASX filings, official registers and primary reports where material. Record URL, document date, fact, security class, reviewer date and limitations. Secondary data is a lead, not final verification.
- Do not splice ticker histories across distinct issuers; consider code reuse, RTOs, consolidations, options, CDIs and effective dates.
- Use `REVIEW_PENDING`, `ELIGIBLE`, `QUARANTINED` for Level 1 decisions; default to pending until evidence is assessed.
- Quarantine material unresolved conflicts. No blanket approvals, fabricated sources or unsupported status upgrades.
- Preserve all 316 candidate rows and evidence identifiers unless an explicitly documented scope change is approved.
- Prefer bounded batches with deterministic ASX code lists, stable batch IDs and idempotent updates.
- Preserve original historical files, and distinguish snapshots from current registers.
- Before commit: validate paths, Markdown links, CSV counts/unique codes, allowed statuses and source references. Record test results and any exceptions.
- After commit: update project status, next actions, and decision log when methodology changes; include commit and exact remaining work.
- If tooling or validation fails, stop and document the blocker; never claim completion.

## Git workflow
Work on a feature branch. Inspect current HEAD and file SHA before writing. Do not force-push. Use reviewable commits. Merge only after acceptance tests pass. Baseline tags require confirmed validated merged commit; do not label an unverified branch as a baseline.

## Level 1 proportionality — adopted 16 October 2026

Use the approved minimum-sufficient-evidence Level 1 model in RESEARCH_ROADMAP.md. Five controls remain: correct issuer/listed security; dated tradeability; reliable dated ordinary shares and market-cap basis (ISIN only where instrument identity is ambiguous); corporate actions material to actual screening lookback; and operating-business classification. Defer immaterial historical continuity to Level 2/3. Do not confuse proposed financing with completed allotment or infer a live trading state from an expired halt. Record decision-critical gaps and source dates. Advance only demonstrably eligible issuers; quarantine documented material defects; otherwise retain REVIEW_PENDING.
