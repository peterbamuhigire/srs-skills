# 02-Test-Plan Skill

## Objective

This skill produces a detailed test plan that translates every SRS "shall" statement into traceable test cases with preconditions, steps, and deterministic expected results. It includes test data definitions, a schedule aligned with the test strategy, and a requirement-to-test traceability matrix per IEEE 829-2008 Sections 7-8.

## Execution Steps

1. Verify `../output/SRS_Draft.md` and `../output/Test_Strategy.md` exist. Optionally check for `../output/acceptance_criteria.md`. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill extracts testable requirements, generates test cases, defines test data, builds the schedule, and writes `../output/Test_Plan.md`.
3. Review the traceability matrix to confirm every SRS "shall" statement maps to at least one test case. Investigate any coverage gaps flagged in the appendix.
4. Proceed to `03-test-report` which consumes the test plan to structure the execution report template.

## Quality Reminder

Every test case shall include preconditions, sequential steps, and a deterministic expected result with a clear pass/fail criterion. Every NFR test case shall include measurable acceptance thresholds. The traceability matrix shall achieve full requirement coverage; flag gaps rather than omitting untested requirements.

## Standards

- IEEE 829-2008 (Software and System Test Documentation, Sections 7-8)
