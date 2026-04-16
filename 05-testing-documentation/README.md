# Phase 05: Testing Documentation

## Purpose

This phase codifies deterministic test governance aligned with BS ISO/IEC/IEEE 29119-3:2013 so that strategy, planning, and reporting artifacts are auditable and traceable.

## Sub-Skills

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-test-strategy | Test_Strategy.md | BS ISO/IEC/IEEE 29119-3 Sec 6 |
| 2 | 02-test-plan | Test_Plan.md | BS ISO/IEC/IEEE 29119-3 Sec 7-8 |
| 3 | 03-test-report | Test_Report_Template.md | BS ISO/IEC/IEEE 29119-3 Sec 9-10 |

## Deterministic Conformance

Phase 05 now references the deterministic conformance checklist in `05-testing-documentation/references/29119-deterministic-checks.md`, which ensures each artifact enumerates the required document tree, normative fields, traceability, and exit criteria defined by 29119-3.

## Execution Order

Run 01-test-strategy FIRST (it defines test levels, types, tools, and criteria that govern all downstream testing artifacts). Then run 02-test-plan (it derives test cases from SRS requirements using the strategy as its framework). Finally, run 03-test-report (it produces the execution report template structured around the test plan).

## Dependencies

- **Upstream:** Phase 02 (Requirements Engineering) -- requires `SRS_Draft.md` in `projects/<ProjectName>/<phase>/<document>/`. Phase 03 (Design Documentation) -- requires `HLD.md` in `projects/<ProjectName>/<phase>/<document>/`.
- **Downstream:** Phase 09 (Governance) -- consumes testing artifacts for compliance and audit evidence.

## Input Source

All skills read from `projects/<ProjectName>/<phase>/<document>/` (SRS_Draft.md, HLD.md, Test_Strategy.md, Test_Plan.md) and `projects/<ProjectName>/_context/quality_standards.md`.

## Output Destination

All skills write to `projects/<ProjectName>/<phase>/<document>/`.
## Auxiliary Artifacts

Described templates include:

- `templates/incident-report.md` (BS ISO/IEC/IEEE 29119-3 §7.5) — structured incident record with severity, trace links, and resolution tracking.
- `templates/test-completion-report.md` (BS ISO/IEC/IEEE 29119-3 §7.6) — final closure artifact capturing coverage, metrics, exit criteria, and waiver log.

Phase 05 skills reference the deterministic checklist in `references/29119-deterministic-checks.md` before writing each artifact to prove clause-level conformance. When executing the test plan or report skills, copy the relevant templates into the project workspace so auditors can cite the numbered sections required by 29119-3.
