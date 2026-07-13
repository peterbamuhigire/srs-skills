# Concrete Build Backlog

Status at 2026-07-13: structural conformance debt is complete. The items below are capability expansion and proof work; none is a waiver in `tests/skill-quality-baseline.json`.

| # | Filename/path | Purpose | Acceptance criteria | Effort |
| --- | --- | --- | --- | --- |
| 1 | docs/world-class-exemplar/README.md | Define one complete exemplar programme with context, generated outputs, validation logs, and export evidence. | A new user can inspect the exemplar and see every phase, gate, and artefact without using private project folders. | M |
| 2 | tests/fixtures/skills/<skill>/positive.md | Add positive input/output fixtures for high-value skills first: PRD, SRS, HLD, RTM, audit, runbook. | At least 25 core skills have runnable representative fixtures and expected artefact checks. | L |
| 3 | tests/fixtures/skills/<skill>/negative.md | Add bad-example fixtures that prove anti-slop and V&V gates catch defects. | Each major phase has at least 3 negative fixtures with expected fail tags. | M |
| 4 | docs/cross-engine-handoff-contract.md | Document exact finance/design/engineering handoff inputs, outputs, and stop conditions. | Each handoff names trigger, source files to read, output obligation, and evidence to record. | S |
| 5 | scripts/validate-cross-engine-routes.py | Automate route checks against design-system-skills and chwezi-accounting-doctrine. | Fresh checkout validation fails if a referenced cross-engine route cannot be resolved. | M |
