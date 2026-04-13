---
name: "test-report"
description: "Generate a test execution report template with results summary, defect log, coverage metrics, and pass/fail analysis per BS ISO/IEC/IEEE 29119-3 Sections 9-10."
metadata:
  use_when: "Use when the task matches test report skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Test Report Skill

## Overview

This is the third and final skill in Phase 05 (Testing Documentation). It reads the test plan to produce a reusable test execution report template containing an executive summary, test execution log, defect log, coverage metrics, failed test analysis, and recommendations. The template includes structured placeholders for actual results to be filled during test execution. The output conforms to BS ISO/IEC/IEEE 29119-3 Sections 9-10 and references the deterministic gate checklist plus the incident/test completion templates.

## When to Use

- After 02-test-plan completes and `Test_Plan.md` exists in `../output/` with test cases and traceability matrix.
- When the project requires a standardized report template for recording test execution outcomes.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../output/Test_Plan.md` |
| **Output**  | `../output/Test_Report_Template.md` |
| **Tone**    | Structured, metrics-driven, stakeholder-facing |
| **Standard** | BS ISO/IEC/IEEE 29119-3 Sec 9-10 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| Test_Plan.md | `../output/Test_Plan.md` | Yes | Test case inventory, traceability matrix, and schedule driving report structure |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Test_Report_Template.md | `../output/Test_Report_Template.md` | Reusable report template with placeholders for test execution results |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if the required input file is missing.

### Step 1: Read Test Plan

Read `Test_Plan.md` from `../output/`. Log the absolute path. If the file is missing, halt execution and report the gap. Extract the total test case count, test case groupings, and traceability matrix.

### Step 2: Generate Executive Summary Template

Create an executive summary section with placeholders for: total tests executed, tests passed, tests failed, tests blocked, tests skipped, overall pass rate (%), requirement coverage percentage, and a release readiness recommendation field. Include a summary dashboard table.

### Step 3: Generate Test Execution Log

Create a test execution log table with columns: TC-ID, Test Case Name, Result (Pass/Fail/Blocked/Skipped), Execution Date, Tester, Defect Reference (if failed), and Notes. Pre-populate TC-IDs from Test_Plan.md with placeholder values for results.

### Step 4: Generate Defect Log

Create a defect log table with columns: DEF-ID (auto-incrementing), Severity (Critical/Major/Minor/Trivial), Priority (P1-P4), Status (Open/In Progress/Resolved/Verified/Closed), Summary Description, Steps to Reproduce, Linked TC-ID, Assigned To, and Resolution Date. Include placeholder rows demonstrating the expected format.

### Step 5: Generate Coverage Metrics Section

Create a coverage metrics section with: Requirement Coverage (percentage of REQ-IDs with at least one executed test case), Feature Coverage (percentage of SRS Section 3.2 features tested), Code Coverage Targets (from Test_Strategy.md if available), and a coverage gap list referencing unexecuted or failed traceability entries.

### Step 6: Generate Failed Test Analysis and Recommendations

Create a failed test analysis section with a template per failure: TC-ID, Failure Description, Root Cause Category (defect, environment, test data, requirement ambiguity), Impact Assessment, and Remediation Action. Create a recommendations section with fields for: release readiness decision (Go/No-Go/Conditional), outstanding risks, and required follow-up actions.

### Step 7: Write Template with Sign-Off

Before writing output, confirm the deterministic gate in `../references/29119-deterministic-checks.md` is satisfied and that incident-report.md plus test-completion-report.md templates are referenced for use during execution reporting. Write the completed template to `../output/Test_Report_Template.md`. Include a sign-off section with fields for: QA Lead (name, date, signature), Project Manager (name, date, signature), and stakeholder approval fields. Log the total number of template sections and placeholder test case entries.

## Output Format

The generated `Test_Report_Template.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Executive Summary, 2. Test Execution Log, 3. Defect Log, 4. Coverage Metrics, 5. Failed Test Analysis, 6. Recommendations, 7. Sign-Off.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Executive summary without numeric placeholders | The summary shall include placeholder fields for all quantitative metrics |
| Defect log missing severity/priority columns | Every defect entry shall classify both severity and priority independently |
| Coverage metrics without gap identification | The coverage section shall list specific unexecuted or failed traceability entries |
| Missing sign-off fields | The template shall include named approval fields for QA Lead and Project Manager |

## Verification Checklist

- [ ] `Test_Report_Template.md` exists in `../output/` with all seven sections populated.
- [ ] Executive summary includes placeholders for total, passed, failed, blocked, and coverage metrics.
- [ ] Test execution log table pre-populates TC-IDs from Test_Plan.md.
- [ ] Defect log includes severity, priority, status, steps to reproduce, and linked TC-ID columns.
- [ ] Coverage metrics section references the traceability matrix and identifies gap categories.
- [ ] Failed test analysis template includes root cause categories and remediation actions.
- [ ] Sign-off section includes QA Lead and Project Manager approval fields.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 02-test-plan | Consumes test case inventory and traceability matrix for report structure |
| Upstream | 01-test-strategy | Inherits defect severity/priority taxonomy and metrics definitions |
| Downstream | Phase 09 (Governance) | Feeds completed test reports as audit evidence for compliance verification |

## Standards

- **BS ISO/IEC/IEEE 29119-3** -- Current international standard for test documentation; governs test execution reports, incident logging, and completion reporting structure (Sections 9-10).

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step test report template generation logic.
- `README.md` -- Quick-start guide for this skill.
