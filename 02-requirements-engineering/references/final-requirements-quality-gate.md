# Final Requirements Quality Gate (PRD and SRS)

Load as the last step before a PRD or SRS goes to the Human Review Gate or is built to `.docx`.
This file adds no new criteria of its own. It fixes the order of the existing checks and names the
one place where each is defined, so a document cannot pass on a partial run. Any unticked row
blocks delivery and becomes the fail tag shown.

## When the gate runs

1. After the last section is drafted and after `08-semantic-auditing` (SRS) or the PRD
   Verification Checklist (PRD) has run.
2. Again after any change to a baselined requirement, before the new version is issued.

## Gate rows

| # | Check | Pass condition | Defined in | Fail tag |
|---|---|---|---|---|
| G1 | Unique identity | Every requirement, objective and NFR has one stable ID; no ID reused or orphaned (`python -m engine validate <project>` id-registry checks pass) | Waterfall checklist Part 7 `29148-IND-CONFORMING`; project registry rules in `CLAUDE.md` | `[V&V-FAIL: duplicate or missing ID]` |
| G2 | Singular | One capability or constraint per statement; no "and/or" joining separate behaviours | Waterfall checklist `29148-IND-SINGULAR` | `[V&V-FAIL: not singular]` |
| G3 | Verifiable, with method | Each requirement names its verification method (test, analysis, inspection, demonstration) and a deterministic oracle | `29148-IND-VERIFIABLE`; [fit criteria and acceptance oracles](fit-criteria-oracles.md) | `[VERIFIABILITY-FAIL]` |
| G4 | Traced to a need | Each requirement traces up to a PRD objective, stakeholder need or regulation, and down to a test | `29148-IND-NECESSARY`; `09-traceability-engineering`; `09-governance-compliance/01-traceability-matrix` | `[TRACE-GAP: <ID>]` |
| G5 | Free of implementation detail | No technology, schema or design choice unless a stakeholder or regulation mandates it, and then it sits in Design Constraints with its source | `29148-IND-APPROPRIATE` | `[V&V-FAIL: implementation detail]` |
| G6 | Measurable NFRs | Every relevant ISO/IEC 25010:2023 characteristic has a relevance decision; each NFR carries metric, threshold, load or condition, and measurement method | `07-attribute-mapping/references/iso-25010-2023-nfr-coverage.md`; [SaaS NFR catalogue](saas-nfr-catalog.md) where applicable | `[SMART-FAIL: NFR not measurable]` |
| G7 | Assumptions, constraints, out of scope | Each is an explicit, numbered section: SRS 2.4 Constraints, 2.5 Assumptions and Dependencies, 1.2 Scope exclusions and 2.6 Apportioning; PRD Section 7 plus an out-of-scope register. Every assumption has an owner and a validation date | Waterfall checklist Part 2 (`IEEE830-5.2.4` to `IEEE830-5.2.6`); PRD Output Format | `[CONTEXT-GAP: assumptions/scope]` |
| G8 | Glossary | Every domain term and acronym is defined; zero unresolved glossary gaps | `08-semantic-auditing` Glossary Audit; `_registry/glossary.yaml` | `[GLOSSARY-GAP: <term>]` |
| G9 | Change control and versioning | Document header carries version, date, status and revision history; the requirement set is baselined; any change to a baselined item has a change-impact entry and approved delta | `08-requirements-management`; `09-governance-compliance/06-change-impact-analysis`, `07-baseline-delta`, `06-ccb-charter` | `[V&V-FAIL: uncontrolled change]` |
| G10 | Set quality | Requirement set is complete, consistent, feasible, comprehensible and able to be validated | Waterfall checklist `29148-SET-*` | `[V&V-FAIL: set <characteristic>]` |
| G11 | Anti-AI-slop prose pass | Ship-gate checklist passes; audit grade is not F | `09-governance-compliance/28-anti-ai-slop`, then `29-ai-slop-audit` | Tag named by the slop finding |

The waterfall checklist is `02-requirements-engineering/waterfall/ieee-830-compliance-checklist.md`.
Its Part 7 (ISO/IEC/IEEE 29148:2018) is the governing quality test; IEEE 830-1998 is superseded and
supplies only the section layout.

## What passing looks like

A senior reviewer can pick any requirement, follow its ID up to the objective it serves and down to
the test that proves it, read one behaviour with one measurable outcome, find every term in the
glossary, and see which version of the document introduced it and who approved the change. A
document that reads well but fails that walk has not passed.

Generic output fails in recognisable ways: "the system shall be fast and secure" (G2, G3, G6), a
requirement naming a database product with no mandate (G5), an "Assumptions" heading with no owner
or date (G7), or a version table stuck at "1.0 Draft" after three review rounds (G9).

## Recording the result

Record one row per gate item in the phase validation record: result (`pass`, `fail`,
`not assessed`), evidence location, reviewer and date. An item that could not be run is
`not assessed` and blocks sign-off; it is never recorded as a pass.

## Evidence/currentness

Accessed 2026-09-24. ISO/IEC/IEEE 29148:2018 is the active requirements-engineering standard and
supersedes IEEE 830-1998; ISO/IEC 25010:2023 is the current product quality model (both as
recorded with sources in the waterfall checklist Part 7 and the 25010 coverage reference). This
file restates engine checks and adds no external thresholds.
