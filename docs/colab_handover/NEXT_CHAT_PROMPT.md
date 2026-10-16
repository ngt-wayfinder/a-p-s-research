# Copy/paste handover prompt for the next a-p-s-research chat

Continue the ASX Penny Stock Research project in GitHub at https://github.com/ngt-wayfinder/a-p-s-research. Act as a senior Australian equity researcher, Python automation engineer and data-quality auditor. The immediate task is **repairing and validating the BHP-only Version 2 Google Colab issuer-report downloader** before any scaling.

**First read** `docs/colab_handover/README.md` on branch `feature/issuer-report-downloader`, then inspect the repository scripts, `docs/GOOGLE_COLAB_RESEARCH.md`, PR #8 status, roadmap, and 316-company Level 1 register. Verify current GitHub state rather than assuming the branch is merged.

Context: Five-company V2 test produced 5/15 accepted report categories, with 87 audited candidates. BHP-only V2 test found all 1,878 BHP announcements, accepted annual but rejected half-year and quarterly; actual audit contains 21 candidates (16 stale, 4 content-rejected, 1 accepted). The BHP-only ZIP accidentally retained four ACW/ACE PDFs from earlier runs. Root issues: overly narrow PDF text inspection, inappropriate quarterly marker requirements, output directory contamination, weak report-period identity checks.

**Source integrity:** `scripts/asx_issuer_reports_google_colab.py` in GitHub is only a limited five-company, first-page announcement-title prototype with tranche delays. It is **not** the full Version 2 downloader. Full Version 2 source is in the prior chat and `asx_batch_v2.py` attachment/local artifact, not yet committed. The original outputs are `asx_batch_5.zip`, `asx_batch_v2.zip`, `asx_batch_v2(1).zip`. Ask for the files if they are not accessible; never invent their content.

**User requirements:** Provide fully commented, runnable Google Colab code; suffix Colab-only scripts `_google_colab.py`; keep version control in GitHub with clear documentation and auditable evidence. Requested pacing: 10 companies/tranche, 15-second inter-company pause, 15-minute inter-tranche pause, stop on HTTP 403/429; full V2 has NOT yet received these changes. Test BHP first, then five-company regression, then 316 only after a quality gate. Keep eligibility evidence separate from automated report collection.

**Source/compliance:** Public ASX API accessibility does not imply permission for unattended/bulk downloads. Do not activate GitHub Actions or run bulk collection until access rights are confirmed. Consider authorised/licensed APIs or issuer investor-relations sources. Rate limiting is not a substitute for authorisation.

**Immediate deliverables:**
1. Verify branch/PR and full V2 source availability.
2. Implement improved annual/half-year/quarterly classification, robust bounded PDF text checks, isolated run output, audit diagnostics and tests in a new documented `*_google_colab.py` file.
3. Commit reviewed changes to the existing feature branch, keeping the prototype distinct.
4. Provide a BHP-only Colab test procedure and objective acceptance criteria; analyse actual new ZIP only after user executes.
5. Update roadmap and handover documentation with factual progress.

Do not claim unexecuted tests passed, or that full V2 has been committed. Begin by reporting verified repository state and the exact next step.
