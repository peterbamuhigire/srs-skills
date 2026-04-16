---
name: "requirements-metrics"
description: "Score requirements artifacts against quantitative quality metrics and enforce quality gate thresholds per IEEE 29148 and IEEE 982.1."
metadata:
  use_when: "Use when the task matches requirements metrics & quality gates skill guidance and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `references/` when deeper detail is needed."
---

# Requirements Metrics & Quality Gates Skill Guidance

## Overview

Run this skill as the universal quality gate for both Waterfall and Agile pipelines. It reads all requirements artifacts, computes quantitative quality metrics, and issues a GREEN/YELLOW/RED gate verdict. No downstream activity (design, development, sprint planning) shall proceed until this gate passes at YELLOW or above.

## When to Use This Skill

- After requirements baselining (`08-requirements-management`) and traceability analysis (`09-traceability-engineering`).
- As a pre-development quality gate in Waterfall workflows.
- As a sprint-entry quality gate in Agile workflows.
- Periodically during requirements evolution to track quality trends.

## Quick Reference

- **Inputs:** All artifacts in `projects/<ProjectName>/<phase>/<document>/`, `projects/<ProjectName>/_context/vision.md`
- **Outputs:** `projects/<ProjectName>/<phase>/<document>/requirements_metrics_report.md`
- **Tone:** Quantitative, data-driven, pass/fail oriented

## Input Files

| File | Source | Required? |
|------|--------|-----------|
| All `*.md` artifacts | `projects/<ProjectName>/<phase>/<document>/` | Yes |
| `vision.md` | `projects/<ProjectName>/_context/` | Yes |
| `traceability_matrix.md` | `projects/<ProjectName>/<phase>/<document>/` | Recommended |
| `requirements_baseline.md` | `projects/<ProjectName>/<phase>/<document>/` | Recommended |

## Output Files

| File | Contents | Destination |
|------|----------|-------------|
| `requirements_metrics_report.md` | Per-metric scores, overall gate verdict, remediation guidance | `projects/<ProjectName>/<phase>/<document>/` |

## Core Instructions

### Step 1: Read All Artifacts

Read every file in `projects/<ProjectName>/<phase>/<document>/` and `projects/<ProjectName>/_context/vision.md`. Log each file path read. Build a consolidated requirements inventory with all requirement identifiers, their fields, and their trace links.

### Step 2: Calculate Metrics

Compute each metric below. For metrics requiring historical data that is unavailable, note "Insufficient history -- baseline measurement recorded."

#### 2a: Volatility Index

$$\text{Volatility Index} = \frac{R_{\text{changed}} + R_{\text{added}} + R_{\text{deleted}}}{R_{\text{total}}} \times 100$$

Where:
- $R_{\text{changed}}$: Requirements modified since last baseline.
- $R_{\text{added}}$: Requirements added since last baseline.
- $R_{\text{deleted}}$: Requirements deleted since last baseline.
- $R_{\text{total}}$: Total requirements in current baseline.

If this is the first baseline, record Volatility Index as 0% (initial measurement).

#### 2b: Completeness Index

$$\text{Completeness Index} = \frac{R_{\text{complete}}}{R_{\text{total}}} \times 100$$

A requirement is complete when all mandatory fields are populated:
- Unique identifier
- Description with "The system shall..." phrasing
- Priority assigned
- Source stakeholder identified
- Acceptance criteria defined
- Requirement state assigned

#### 2c: Ambiguity Index

Count occurrences of the following vague terms across all requirements:

| Prohibited Term | IEEE 830 Violation |
|-----------------|-------------------|
| fast | Missing quantitative performance target |
| easy | Subjective usability claim |
| intuitive | Undefined interaction metric |
| user-friendly | No measurable UX criterion |
| robust | Missing reliability specification |
| flexible | Undefined adaptability scope |
| scalable | Missing load/capacity targets |
| efficient | No resource utilization metric |
| appropriate | Undefined acceptance boundary |
| reasonable | Subjective judgment term |
| sufficient | Missing quantitative threshold |
| adequate | Undefined quality level |
| minimal | Missing lower-bound specification |
| maximize/minimize | Missing target value |
| support | Ambiguous capability claim |

$$\text{Ambiguity Index} = \sum \text{vague term occurrences}$$

Each occurrence shall be listed with the requirement ID and the offending term.

#### 2d: Testability Score

$$\text{Testability Score} = \frac{R_{\text{testable}}}{R_{\text{total}}} \times 100$$

A requirement is testable when it has:
- Verifiable acceptance criteria with pass/fail conditions.
- Quantitative thresholds where applicable (response time, throughput, accuracy).
- No subjective terms from the Ambiguity Index list.

#### 2e: Traceability Coverage

$$\text{Traceability Coverage} = \frac{R_{\text{traced}}}{R_{\text{total}}} \times 100$$

A requirement is traced when it links to both a business goal (upward) AND a test case (downward). Source this metric from `traceability_matrix.md` if available.

#### 2f: Conflict Count

Count the number of unresolved contradictions between requirements. Source from `traceability_matrix.md` or perform a fresh scan for:
- Mutually exclusive behaviors for the same system element.
- Contradictory non-functional targets (e.g., "response time < 100ms" vs. "response time < 500ms" for the same operation).
- Conflicting priority assignments from different stakeholders.

#### 2g: Data Quality Score

$$\text{Data Quality Score} = \frac{D_{\text{complete}} + D_{\text{consistent}}}{2 \times D_{\text{total}}} \times 100$$

Where:
- $D_{\text{complete}}$: Data requirements with all fields defined (type, format, constraints, validation rules).
- $D_{\text{consistent}}$: Data requirements with no naming or type conflicts across artifacts.
- $D_{\text{total}}$: Total data requirements identified.

#### 2h: INVEST Compliance (Agile Only)

$$\text{INVEST Compliance} = \frac{S_{\text{passing}}}{S_{\text{total}}} \times 100$$

A user story passes INVEST when it satisfies all six criteria: Independent, Negotiable, Valuable, Estimable, Small, Testable. Apply only when user stories exist in `projects/<ProjectName>/<phase>/<document>/`.

### Step 3: Apply Quality Gate Thresholds

Evaluate each metric against the following thresholds:

| Metric | GREEN (Pass) | YELLOW (Conditional) | RED (Fail) |
|--------|-------------|---------------------|------------|
| Completeness Index | >= 95% | >= 80% | < 80% |
| Ambiguity Index | 0 | <= 5 | > 5 |
| Testability Score | >= 90% | >= 75% | < 75% |
| Traceability Coverage | >= 85% | >= 70% | < 70% |
| Conflict Count | 0 | <= 2 | > 2 |
| Data Quality Score | >= 90% | >= 75% | < 75% |
| INVEST Compliance | >= 90% | >= 75% | < 75% |
| Volatility Index | <= 10% | <= 25% | > 25% |

### Step 4: Determine Overall Gate Verdict

The overall gate verdict is the **lowest** individual metric status:

- **GREEN:** All metrics are GREEN. Proceed to downstream activities.
- **YELLOW:** At least one metric is YELLOW, none are RED. Proceed with documented risk acceptance and remediation plan.
- **RED:** At least one metric is RED. Halt downstream activities. Return failing requirements to upstream skills for correction.

For YELLOW verdicts, the report shall include:
- Justification for proceeding despite deficiencies.
- Specific remediation actions with owners and deadlines.
- Escalation path if remediation is not completed on schedule.

### Step 5: Generate Per-Metric Breakdown

For each metric, provide:
- The calculated score.
- The threshold status (GREEN/YELLOW/RED).
- A list of specific requirements contributing to deficiency (if not GREEN).
- Recommended remediation actions.

### Step 6: Generate Output

Write `projects/<ProjectName>/<phase>/<document>/requirements_metrics_report.md` following the output format below.

## Output Format

### requirements_metrics_report.md

```markdown
# Requirements Metrics Report: [Project Name]

**Generated:** [Date]
**Baseline:** BL-[PROJECT]-[VERSION]
**Standards:** IEEE 29148-2018, IEEE 982.1-2005

---

## Overall Gate Verdict: [GREEN / YELLOW / RED]

---

## Metrics Summary

| Metric | Score | Threshold | Status |
|--------|-------|-----------|--------|
| Completeness Index | N% | >= 95% | [GREEN/YELLOW/RED] |
| Ambiguity Index | N | 0 | [GREEN/YELLOW/RED] |
| Testability Score | N% | >= 90% | [GREEN/YELLOW/RED] |
| Traceability Coverage | N% | >= 85% | [GREEN/YELLOW/RED] |
| Conflict Count | N | 0 | [GREEN/YELLOW/RED] |
| Data Quality Score | N% | >= 90% | [GREEN/YELLOW/RED] |
| INVEST Compliance | N% | >= 90% | [GREEN/YELLOW/RED] |
| Volatility Index | N% | <= 10% | [GREEN/YELLOW/RED] |

---

## Per-Metric Detail

### Completeness Index: N%

[List of incomplete requirements with missing fields]

### Ambiguity Index: N

[List of requirements with vague terms, term identified]

### Testability Score: N%

[List of untestable requirements with deficiency noted]

[Continue for each metric...]

---

## Remediation Plan

| Priority | Requirement(s) | Issue | Action | Owner | Deadline |
|----------|----------------|-------|--------|-------|----------|
| Critical | REQ-xxx | Missing acceptance criteria | Add verifiable criteria | [Name] | [Date] |

---

## Historical Trend (if available)

| Date | Completeness | Ambiguity | Testability | Traceability | Verdict |
|------|-------------|-----------|-------------|--------------|---------|
| [Date] | N% | N | N% | N% | [Verdict] |
```

## Common Pitfalls

- **Gaming metrics:** Marking requirements "complete" without genuine acceptance criteria inflates the Completeness Index. Audit field quality, not just field presence.
- **Ignoring YELLOW status:** A conditional pass is not a free pass. Every YELLOW metric requires a documented remediation plan with deadlines.
- **Snapshot-only measurement:** A single measurement is a snapshot, not a trend. Track metrics over time to detect quality degradation.
- **Excluding NFRs:** Non-functional requirements are often the hardest to make testable. Include them in all metric calculations.

## Verification Checklist

- [ ] All eight metrics are calculated and reported.
- [ ] Each metric has a GREEN/YELLOW/RED status based on defined thresholds.
- [ ] Overall gate verdict equals the lowest individual metric status.
- [ ] Failing requirements are listed with specific deficiencies.
- [ ] Remediation plan is provided for all non-GREEN metrics.
- [ ] Vague terms list matches the prohibited terms catalog.
- [ ] INVEST Compliance is calculated only when user stories exist.

## Integration

- **Upstream:** `08-requirements-management`, `09-traceability-engineering`
- **Downstream:** Development phase, sprint planning, `waterfall/08-semantic-auditing`
- **Gate role:** Universal quality gate for both Waterfall and Agile pipelines

## Standards

- **IEEE Std 29148-2018:** Requirements quality characteristics.
- **IEEE Std 982.1-2005:** Measures to produce reliable software.
- **IEEE Std 830-1998:** Quality attributes for requirements (correct, unambiguous, complete, consistent, verifiable, modifiable, traceable).
- **Laplante Ch.7.4:** Requirements quality measurement.
- **Wiegers Practices 19-20:** Requirements quality metrics and process improvement.
- **IEEE Std 610.12-1990:** Terminology definitions.

## Resources

- `references/metrics-catalog.md`: Complete metrics catalog with formulas and benchmarks.
- `references/quality-gate-thresholds.md`: Gate configuration and escalation procedures.

---
**Last Updated:** 2026-03-07
**Skill Version:** 1.0.0
