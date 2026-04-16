---
name: "test-plan"
description: "Generate a detailed test plan with test cases, requirement traceability, test data, schedule, and resource allocation per BS ISO/IEC/IEEE 29119-3 Sections 7-8."
metadata:
  use_when: "Use when the task matches test plan skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Test Plan Skill

## Overview

This is the second skill in Phase 05 (Testing Documentation). It transforms the SRS functional and non-functional requirements into a detailed test plan containing test cases, test data definitions, schedule, resource allocation, and a requirement-to-test traceability matrix. Every "shall" statement in SRS Section 3.2 becomes a test case. The output conforms to BS ISO/IEC/IEEE 29119-3 Sections 7-8 and references the deterministic checklist for artifact completeness.

## When to Use

- After 01-test-strategy completes and `Test_Strategy.md` exists in `projects/<ProjectName>/<phase>/<document>/` with test levels, types, and criteria.
- When `SRS_Draft.md` exists in `projects/<ProjectName>/<phase>/<document>/` with functional requirements containing "shall" statements.
- Optionally, when `acceptance_criteria.md` exists in `projects/<ProjectName>/<phase>/<document>/` for agile projects requiring acceptance-test mapping.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`, `projects/<ProjectName>/<phase>/<document>/Test_Strategy.md`, `projects/<ProjectName>/<phase>/<document>/acceptance_criteria.md` (optional) |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Test_Plan.md` |
| **Tone**    | Detailed, case-driven, QA-facing |
| **Standard** | BS ISO/IEC/IEEE 29119-3 Sec 7-8 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| SRS_Draft.md | `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` | Yes | Functional (Section 3.2) and non-functional (Sections 3.3, 3.5) requirements as test case sources |
| Test_Strategy.md | `projects/<ProjectName>/<phase>/<document>/Test_Strategy.md` | Yes | Test levels, types, tools, and criteria governing test case structure |
| acceptance_criteria.md | `projects/<ProjectName>/<phase>/<document>/acceptance_criteria.md` | No | Agile acceptance criteria for mapping to UAT test cases |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Test_Plan.md | `projects/<ProjectName>/<phase>/<document>/Test_Plan.md` | Complete test plan with test cases, traceability matrix, schedule, and resources |

## Core Instructions

Follow these nine steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `SRS_Draft.md` and `Test_Strategy.md` from `projects/<ProjectName>/<phase>/<document>/`. Optionally read `acceptance_criteria.md` from `projects/<ProjectName>/<phase>/<document>/` if it exists. Log the absolute path of each file read. If any required file is missing, halt execution and report the gap.

### Step 2: Extract Testable Requirements

Parse SRS Section 3.2 and extract every "shall" statement as a testable requirement. Assign each requirement a unique identifier (e.g., REQ-FUNC-001). Log the total count of extracted requirements.

### Step 3: Map Acceptance Criteria

If `acceptance_criteria.md` exists, map each acceptance criterion to its corresponding SRS requirement and note which test cases shall validate it at the UAT level. If the file does not exist, skip this step and note that UAT cases derive from SRS requirements directly.

### Step 4: Define Test Design Specification & Test Case Format

Document the selected test design techniques (equivalence partitioning, boundary values, state machine testing, decision tables, use case testing) and cite the applicable 29119-3 clause (§7.3.3). Each technique shall reference the requirements it exercises.

Establish the test case format using the nine normative 29119-3 fields: TC-ID, Objective/Purpose, Priority, Traceability to requirement ID, Preconditions, Test Input, Expected Result (with deterministic pass/fail), Actual Result (filled at execution), and Test Result (Pass/Incident). Include Steps (numbered actions) beneath the structured fields.

### Step 5: Generate Functional Test Cases

For each functional requirement extracted in Step 2, generate one or more test cases. Each test case shall define preconditions, sequential steps, and a deterministic expected result. Group test cases by SRS feature (Section 3.2.x subsections).

### Step 6: Generate Non-Functional Test Cases

Generate test cases for non-functional requirements: Performance tests from SRS Section 3.3 (response time, throughput, capacity), Security tests from SRS Section 3.5.3 (authentication, authorization, data protection). Each NFR test case shall include measurable acceptance thresholds.

### Step 7: Define Test Data Requirements

For each test case group, define the test data required: data entities, volume, generation method (manual, scripted, anonymized production data), and precondition data state. Identify shared test data dependencies across test case groups.

### Step 8: Define Schedule and Resource Allocation

Define the test execution schedule: phases aligned with Test_Strategy.md test levels, estimated duration per phase, resource assignments (roles, not named individuals), and dependencies between phases. Identify parallel execution opportunities.

### Step 9: Generate Traceability Matrix and Write Output

Generate a requirement-to-test traceability matrix mapping every REQ-ID to its TC-IDs, confirming full coverage. Flag any requirements without test cases as coverage gaps. Before writing output, verify the deterministic gate in `../references/29119-deterministic-checks.md` has been satisfied (mandatory artifact tree, clause annotations, entry/exit criteria). Write the completed document to `projects/<ProjectName>/<phase>/<document>/Test_Plan.md`. Log the total count of test cases, coverage percentage, and any gaps.

## Output Format

The generated `Test_Plan.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Test Scope, 2. Test Case Summary Table, 3. Detailed Test Cases (grouped by feature), 4. Test Data, 5. Schedule, 6. Resources, 7. Traceability Matrix, Appendix A: Coverage Gap Report.

## Final Step: Write `manifest.md`

After generating all section files, create (or overwrite) `manifest.md` in this document's directory listing the section files in the correct assembly order:

```markdown
# Document Manifest — Test Plan
# Generated by test-plan. Edit to reorder or exclude sections before building.
01-test-scope.md
02-test-cases.md
03-test-data.md
04-schedule.md
05-resources.md
06-traceability.md
07-coverage-gaps.md
```

This ensures `scripts/build-doc.sh` assembles sections in the intended order rather than alphabetical fallback.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Test cases without preconditions | Every test case shall state the required system state before execution |
| Expected results without pass/fail criteria | Every expected result shall define a deterministic observable outcome |
| NFR test cases without measurable thresholds | Performance and security tests shall include numeric acceptance criteria |
| Missing traceability for edge-case requirements | Every "shall" statement in SRS Section 3.2 shall have at least one test case |

## Verification Checklist

- [ ] `Test_Plan.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all seven sections populated.
- [ ] Every "shall" statement in SRS Section 3.2 has at least one corresponding test case.
- [ ] Test cases include preconditions, sequential steps, and deterministic expected results.
- [ ] NFR test cases include measurable acceptance thresholds from SRS Sections 3.3 and 3.5.
- [ ] Test data requirements are defined for each test case group.
- [ ] Schedule aligns with test levels from Test_Strategy.md.
- [ ] Traceability matrix achieves full requirement coverage; gaps are flagged in the appendix.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 01-test-strategy | Consumes test levels, types, tools, and criteria framework |
| Upstream | Phase 02 (Requirements Engineering) | Consumes `SRS_Draft.md` for requirement extraction |
| Downstream | 03-test-report | Feeds test case inventory and traceability matrix for report template |
| Downstream | Phase 09 (Governance) | Feeds test plan as audit evidence for compliance verification |

## Standards

- **BS ISO/IEC/IEEE 29119-3** -- Current international standard for test documentation; governs project-level test plans, traceability, and required artifact set (Sections 7-8).

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step test plan generation logic.
- `README.md` -- Quick-start guide for this skill.

## Worked example

See [`examples/representative/`](examples/representative/).
