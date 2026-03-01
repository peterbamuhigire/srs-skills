# Phase 05: Testing Documentation

## Purpose

This phase generates testing documentation that ensures quality assurance coverage across all verified requirements. It transforms the SRS and design artifacts into a structured testing framework comprising strategy, planning, and reporting artifacts per IEEE 829-2008.

## Sub-Skills

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-test-strategy | Test_Strategy.md | IEEE 829-2008 Sec 6 |
| 2 | 02-test-plan | Test_Plan.md | IEEE 829-2008 Sec 7-8 |
| 3 | 03-test-report | Test_Report_Template.md | IEEE 829-2008 Sec 9-10 |

## Execution Order

Run 01-test-strategy FIRST (it defines test levels, types, tools, and criteria that govern all downstream testing artifacts). Then run 02-test-plan (it derives test cases from SRS requirements using the strategy as its framework). Finally, run 03-test-report (it produces the execution report template structured around the test plan).

## Dependencies

- **Upstream:** Phase 02 (Requirements Engineering) -- requires `SRS_Draft.md` in `../output/`. Phase 03 (Design Documentation) -- requires `HLD.md` in `../output/`.
- **Downstream:** Phase 09 (Governance) -- consumes testing artifacts for compliance and audit evidence.

## Input Source

All skills read from `../output/` (SRS_Draft.md, HLD.md, Test_Strategy.md, Test_Plan.md) and `../project_context/quality_standards.md`.

## Output Destination

All skills write to `../output/`.
