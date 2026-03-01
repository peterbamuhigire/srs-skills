# 01-Test-Strategy Skill

## Objective

This skill produces a test strategy that defines the quality assurance framework for the project: test levels, test types, tooling, environments, entry/exit criteria, defect management, and metrics. It serves as the governing document for all downstream testing artifacts per IEEE 829-2008 Section 6.

## Execution Steps

1. Verify `../output/SRS_Draft.md`, `../output/HLD.md`, and `../project_context/quality_standards.md` exist. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill defines test levels, types, tools, environments, criteria, defect management, and metrics, then writes `../output/Test_Strategy.md`.
3. Review the traceability section to confirm every test level and type maps to SRS sections and quality_standards.md targets.
4. Proceed to `02-test-plan` which consumes the strategy as its governing framework.

## Quality Reminder

Every test level shall define scope boundaries, responsible roles, and automation expectations. Every entry/exit criterion shall include a measurable threshold traced to quality_standards.md. Every tool selection shall justify its fit to the HLD technology stack. Flag strategy gaps rather than fabricating quality targets.

## Standards

- IEEE 829-2008 (Software and System Test Documentation, Section 6)
