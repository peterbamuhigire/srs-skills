---
name: "traceability-engineering"
description: "Establish forward and backward traceability links between business goals, requirements, design elements, and test cases per IEEE 1012 and IEEE 29148."
metadata:
  use_when: "Use when the task matches traceability engineering skill guidance and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `references/` when deeper detail is needed."
---

# Traceability Engineering Skill Guidance

## Overview

Run this skill after requirements have been baselined and validated. It builds a four-level trace chain linking every requirement to its originating business goal, downstream design element, and verification test case. The skill detects orphan requirements, gold-plating, and coverage gaps, producing a comprehensive traceability matrix that serves both Waterfall auditing and Agile quality gates.

## When to Use This Skill

- After `08-requirements-management` has established a baseline.
- When preparing for design phase handoff to ensure all requirements are traceable.
- As a quality gate before development begins.
- During audits to demonstrate requirements coverage and accountability.
- As an Agile quality gate to verify user stories trace to business goals.

## Quick Reference

- **Inputs:** `../project_context/vision.md`, `../project_context/stakeholder_register.md`, all `../output/` artifacts
- **Outputs:** `../output/traceability_matrix.md`
- **Tone:** Analytical, systematic, gap-focused

## Input Files

| File | Source | Required? |
|------|--------|-----------|
| `vision.md` | `../project_context/` | Yes |
| `stakeholder_register.md` | `../project_context/` | Yes |
| All `*.md` artifacts | `../output/` | Yes |
| `requirements_baseline.md` | `../output/` | Recommended |

## Output Files

| File | Contents | Destination |
|------|----------|-------------|
| `traceability_matrix.md` | Four-level trace matrix with gap analysis and coverage metrics | `../output/` |

## Core Instructions

### Step 1: Read All Inputs

Read `../project_context/vision.md`, `../project_context/stakeholder_register.md`, and every artifact in `../output/`. Log each file path read. Extract:

- **Business Goals:** From `vision.md` -- assign identifiers (BG-001, BG-002, ...) if not already present.
- **Requirements:** From all output artifacts -- collect every requirement ID (REQ-xxx, FR-xxx, NFR-xxx, US-xxx).
- **Design Elements:** From any design or architecture artifacts -- assign identifiers (DE-001, DE-002, ...) if present.
- **Test Cases:** From any test artifacts -- collect test case IDs (TC-001, TC-002, ...) if present.
- **Stakeholders:** From `stakeholder_register.md` -- map each requirement to its source stakeholder.

### Step 2: Define Trace Link Types

Establish the following trace link taxonomy for all connections in the matrix:

| Link Type | Direction | Description |
|-----------|-----------|-------------|
| derives-from | Requirement -> Business Goal | Requirement originates from a business goal |
| satisfies | Design Element -> Requirement | Design element fulfills a requirement |
| implements | Code Component -> Design Element | Code realizes a design element |
| verified-by | Requirement -> Test Case | Test case validates a requirement |
| conflicts-with | Requirement <-> Requirement | Two requirements contradict each other |
| refines | Requirement -> Requirement | Detailed requirement elaborates a parent |
| replaces | Requirement -> Requirement | New requirement supersedes an old one |

All links shall be maintained bidirectionally: if REQ-001 derives-from BG-003, then BG-003 shall list REQ-001 as a derived requirement.

### Step 3: Build Four-Level Trace Chain

For every requirement, establish the complete trace chain:

```
Business Goal (BG-xxx)
  -> Requirement (REQ-xxx) [derives-from]
    -> Design Element (DE-xxx) [satisfies]
      -> Test Case (TC-xxx) [verified-by]
```

For each requirement, record:

| Field | Description |
|-------|-------------|
| Req ID | Unique requirement identifier |
| Business Goal | BG-xxx that this requirement derives from |
| Source Stakeholder | Stakeholder who originated or owns the requirement |
| Design Element | DE-xxx that satisfies this requirement (if available) |
| Test Case ID | TC-xxx that verifies this requirement (if available) |
| Trace Status | Complete, Partial, Orphan, or Untested |

### Step 4: Detect Orphan Requirements

An orphan requirement has no upward trace link to a business goal. For each orphan:

1. Tag the requirement with `[TRACE-GAP]`.
2. Record the gap type: "No business goal linkage."
3. Recommend action: link to an existing goal, create a new goal, or retire the requirement.

### Step 5: Detect Gold-Plating

Gold-plating occurs when a design element or feature exists without a corresponding requirement. For each instance:

1. Tag the element with `[TRACE-GAP]`.
2. Record the gap type: "Design element without requirement justification."
3. Recommend action: create a requirement to justify the element, or remove the element.

### Step 6: Detect Untested Requirements

An untested requirement has no downward trace link to a test case. For each instance:

1. Tag the requirement with `[TRACE-GAP]`.
2. Record the gap type: "No test case linkage."
3. Recommend action: create a test case with verifiable acceptance criteria.

### Step 7: Calculate Traceability Coverage

Compute the following coverage metrics:

$$\text{Upward Coverage} = \frac{\text{Requirements with Business Goal links}}{\text{Total Requirements}} \times 100$$

$$\text{Downward Coverage} = \frac{\text{Requirements with Test Case links}}{\text{Total Requirements}} \times 100$$

$$\text{Full Coverage} = \frac{\text{Requirements with both BG and TC links}}{\text{Total Requirements}} \times 100$$

$$\text{Design Coverage} = \frac{\text{Requirements with Design Element links}}{\text{Total Requirements}} \times 100$$

### Step 8: Detect Conflicts

Scan all requirements for contradictions. Two requirements conflict when they specify mutually exclusive behaviors for the same system element. Tag each conflict pair with `[TRACE-GAP]` and record:

- Conflicting requirement IDs.
- Nature of the conflict.
- Recommended resolution.

### Step 9: Generate Output

Write `../output/traceability_matrix.md` following the output format below.

## Output Format

### traceability_matrix.md

```markdown
# Traceability Matrix: [Project Name]

**Generated:** [Date]
**Baseline:** BL-[PROJECT]-[VERSION]
**Standards:** IEEE 1012-2016, IEEE 29148-2018

---

## Coverage Summary

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Upward Coverage (BG links) | N% | >= 85% | [PASS/FAIL] |
| Downward Coverage (TC links) | N% | >= 85% | [PASS/FAIL] |
| Full Coverage (BG + TC) | N% | >= 70% | [PASS/FAIL] |
| Design Coverage (DE links) | N% | >= 60% | [PASS/FAIL] |
| Orphan Requirements | N | 0 | [PASS/FAIL] |
| Gold-Plated Elements | N | 0 | [PASS/FAIL] |
| Conflicts Detected | N | 0 | [PASS/FAIL] |

---

## Trace Matrix

| Req ID | Title | Business Goal | Stakeholder | Design Element | Test Case | Status |
|--------|-------|---------------|-------------|----------------|-----------|--------|
| REQ-001 | ... | BG-001 | [Name] | DE-001 | TC-001 | Complete |
| REQ-002 | ... | [TRACE-GAP] | [Name] | DE-002 | TC-002 | Orphan |

---

## Gap Analysis

### Orphan Requirements (No Business Goal)

| Req ID | Title | Recommended Action |
|--------|-------|--------------------|
| REQ-002 | ... | Link to BG-003 or retire |

### Untested Requirements (No Test Case)

| Req ID | Title | Recommended Action |
|--------|-------|--------------------|
| REQ-005 | ... | Create TC with acceptance criteria |

### Gold-Plated Elements (No Requirement)

| Element ID | Description | Recommended Action |
|------------|-------------|--------------------|
| DE-007 | ... | Create requirement or remove element |

### Requirement Conflicts

| Req A | Req B | Conflict Description | Recommended Resolution |
|-------|-------|---------------------|----------------------|
| REQ-003 | REQ-012 | ... | ... |

---

## Trace Link Summary

| Link Type | Count |
|-----------|-------|
| derives-from | N |
| satisfies | N |
| verified-by | N |
| conflicts-with | N |
| refines | N |
| replaces | N |
```

## Common Pitfalls

- **Shallow tracing:** Linking requirements only to goals but not to test cases creates a false sense of coverage. Always build the full four-level chain.
- **Missing bidirectional maintenance:** If a forward link exists (REQ -> TC), the reverse link (TC -> REQ) must also be maintained. One-way links break audit traversal.
- **Ignoring non-functional requirements:** NFRs are often excluded from trace matrices. Every NFR shall have a business goal link and a verification method.
- **Stale links:** When requirements change, trace links become outdated. Re-run this skill after every baseline update.
- **Over-counting conflicts:** Distinguish genuine contradictions from complementary requirements that address different scenarios of the same feature.

## Verification Checklist

- [ ] Every requirement has been evaluated for upward (BG) and downward (TC) trace links.
- [ ] Orphan requirements are tagged with `[TRACE-GAP]` and have recommended actions.
- [ ] Gold-plated design elements are identified and tagged.
- [ ] Coverage percentages are calculated for all four metrics.
- [ ] Conflicts are documented with resolution recommendations.
- [ ] All trace links use the defined link type taxonomy.
- [ ] Bidirectional link integrity is maintained.

## Integration

- **Upstream:** `08-requirements-management`, all specification and validation skills
- **Downstream:** `10-requirements-metrics`, `waterfall/08-semantic-auditing`
- **Complements:** `waterfall/08-semantic-auditing` (RTM section); this skill produces a standalone, enhanced trace matrix

## Standards

- **IEEE Std 1012-2016:** Software Verification and Validation -- traceability analysis.
- **IEEE Std 29148-2018:** Requirements engineering -- traceability provisions.
- **Laplante Ch.7.3:** Requirements traceability matrices and coverage analysis.
- **Wiegers Practice 18:** Requirements traceability and link management.
- **IEEE Std 610.12-1990:** Terminology definitions.

## Resources

- `references/trace-matrix-template.md`: Traceability matrix template and usage guide.
- `references/trace-link-types.md`: Trace link taxonomy and bidirectional maintenance rules.

---
**Last Updated:** 2026-03-07
**Skill Version:** 1.0.0
