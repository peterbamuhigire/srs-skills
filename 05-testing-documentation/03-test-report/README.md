# 03-Test-Report Skill

## Objective

This skill produces a reusable test execution report template that structures test results, defect logs, coverage metrics, failed test analysis, and release recommendations. It pre-populates test case identifiers from the test plan and provides structured placeholders for actual execution data per IEEE 829-2008 Sections 9-10.

## Execution Steps

1. Verify `../output/Test_Plan.md` exists with test cases and traceability matrix. Halt if the file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates the report template with executive summary, execution log, defect log, coverage metrics, analysis, recommendations, and sign-off sections, then writes `../output/Test_Report_Template.md`.
3. Review the template to confirm TC-IDs from the test plan are pre-populated in the execution log and that all placeholder fields are clearly marked for completion during test execution.
4. This is the final skill in Phase 05. The completed testing documentation suite (Test_Strategy.md, Test_Plan.md, Test_Report_Template.md) feeds downstream to Phase 09 (Governance) as audit evidence.

## Quality Reminder

The executive summary shall include numeric placeholders for all quantitative metrics. The defect log shall classify severity and priority independently. The coverage metrics section shall reference the traceability matrix and flag gap categories. The sign-off section shall include named approval fields. Flag template structural issues rather than inserting fabricated test results.

## Standards

- IEEE 829-2008 (Software and System Test Documentation, Sections 9-10)
