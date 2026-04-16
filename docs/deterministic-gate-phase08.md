---
gate: phase08
checks:
  - phase08.user_manual_has_screenshots
  - phase08.release_notes_link_to_fr
  - phase08.faq_has_at_least_5_qa
clause_refs:
  - standard: "IEEE Std 26514-2022"
    clause: "8"
---

# Phase 08 Deterministic Gate

Use this checklist before end-user documentation is considered release-ready.

1. **Source Alignment**
   - User manuals, installation guides, FAQs, and release notes reference the current product behavior described in design, testing, and deployment artifacts.
   - Any legacy `../output/` references are treated as aliases to the active project workspace outputs.

2. **Deterministic Coverage**
   - Installation guide includes exact prerequisites, install steps, verification checks, rollback or uninstall notes, and known limitations.
   - User manual covers primary workflows, error states, and recovery steps.
   - Release notes distinguish new, changed, fixed, deprecated, and known issues.

3. **Audience and Control Context**
   - Administrator-only or regulated workflows are marked clearly.
   - Safety, privacy, or operational consequences are called out where misuse could create business or compliance risk.

4. **Verification**
   - Documentation claims are sampled against the actual generated artifacts or implementation evidence.
   - Broken screenshots, placeholder text, and unresolved TODOs are blocked.

5. **Exit Evidence**
   - A reviewer can follow the documentation to install, operate, and troubleshoot the system without consulting hidden tribal knowledge.
