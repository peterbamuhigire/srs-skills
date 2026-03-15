---
name: requirements-analysis
description: Analyze, classify, detect conflicts, assess feasibility, and prioritize gathered requirements per IEEE 29148 Section 6.5 and Wiegers Practices 7-9.
---

# Requirements Analysis Skill

## Overview

This skill transforms raw elicitation artifacts into a structured analysis report. It classifies requirements by type and priority, detects conflicts between competing requirements, assesses feasibility across five dimensions (TELOS), and applies a stakeholder-selected prioritization method. The output serves as the authoritative analysis baseline before specification and validation activities begin.

## When to Use This Skill

- After elicitation activities have produced `elicitation_log.md` with raw requirements
- When the requirements set has grown large enough that conflicts and redundancies are likely
- Before writing formal SRS specifications to ensure only feasible, conflict-free requirements proceed
- When stakeholders need a defensible prioritization of the requirements backlog

## Quick Reference

| Attribute     | Value                                                                  |
|---------------|------------------------------------------------------------------------|
| **Inputs**    | `../output/elicitation_log.md`, `vision.md`, `features.md`, `business_rules.md` |
| **Output**    | `../output/requirements_analysis_report.md`                            |
| **Tone**      | Analytical, objective, evidence-based; no subjective adjectives        |
| **Standards** | IEEE 29148-2018 Section 6.5, IEEE 830-1998, IEEE 1233-1998            |

## Input Files

| File               | Location                                  | Required | Purpose                                          |
|--------------------|-------------------------------------------|----------|--------------------------------------------------|
| elicitation_log.md | `../output/elicitation_log.md`            | Yes      | Raw requirements gathered from stakeholders       |
| vision.md          | `../project_context/vision.md`            | Yes      | Business goals for traceability and prioritization|
| features.md        | `../project_context/features.md`          | Yes      | Feature descriptions for classification           |
| business_rules.md  | `../project_context/business_rules.md`    | No       | Business rules for conflict detection             |

## Output Files

| File                           | Location                                       | Description                                    |
|--------------------------------|------------------------------------------------|------------------------------------------------|
| requirements_analysis_report.md| `../output/requirements_analysis_report.md`    | Complete analysis with classification, conflicts, feasibility, and prioritization |

## Core Instructions

Follow these steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read and Inventory Context Files

Read `elicitation_log.md`, `vision.md`, `features.md`, and optionally `business_rules.md` from `../project_context/`. Assign a temporary identifier (e.g., RAW-001) to each requirement that lacks one. Log the total count of raw requirements discovered.

### Step 2: Classify Requirements

Classify each requirement along two axes:

**By Type (IEEE 29148 Section 6.5.2):**

| Type           | Definition                                                       | Identifier Prefix |
|----------------|------------------------------------------------------------------|--------------------|
| Functional     | A capability the system shall provide (stimulus-response)        | FR-                |
| Non-Functional | A quality attribute or constraint the system shall satisfy       | NFR-               |
| Constraint     | A design or implementation restriction imposed externally        | CON-               |
| Interface      | A requirement on system boundaries and external interactions     | IR-                |

**By Obligation (IEEE 1233):**

| Level      | Keyword  | Meaning                                          |
|------------|----------|--------------------------------------------------|
| Mandatory  | shall    | Non-negotiable; system fails acceptance without it|
| Desirable  | should   | Expected but negotiable under constraint pressure |
| Optional   | may      | Nice-to-have; included only if resources permit   |

Produce a classification matrix table listing every requirement with its type, obligation level, and source reference.

### Step 3: Detect Conflicts

Scan the classified requirements for four conflict types per Wiegers Practice 8:

1. **Contradiction:** Two requirements specify mutually exclusive behaviors for the same stimulus. Flag both with `[CONFLICT-CONTRADICTION]`.
2. **Redundancy:** Two requirements specify the same behavior in different words. Flag the duplicate with `[CONFLICT-REDUNDANCY]`.
3. **Subsumption:** One requirement is a strict subset of another. Flag the subsumed requirement with `[CONFLICT-SUBSUMPTION]`.
4. **Boundary Conflict:** Two requirements define overlapping numeric ranges or thresholds that cannot simultaneously be satisfied. Flag both with `[CONFLICT-BOUNDARY]`.

For each detected conflict, document:
- The conflicting requirement identifiers
- The conflict type
- A recommended resolution strategy (merge, escalate, defer, remove)
- The escalation path if stakeholder arbitration is required

See `references/conflict-detection.md` for the detection algorithm and resolution strategies.

### Step 4: Assess Feasibility (TELOS Framework)

Evaluate every mandatory requirement against five feasibility dimensions:

| Dimension   | Question                                                        | Score Range |
|-------------|-----------------------------------------------------------------|-------------|
| Technical   | Can the requirement be implemented with available technology?   | 1-5         |
| Economic    | Can the requirement be implemented within budget constraints?   | 1-5         |
| Legal       | Does the requirement comply with applicable regulations?        | 1-5         |
| Operational | Can the organization support this requirement operationally?    | 1-5         |
| Schedule    | Can the requirement be delivered within the project timeline?   | 1-5         |

Compute a composite feasibility score:

$FeasibilityScore = \frac{T + E + L + O + S}{5}$

Apply the following thresholds:
- **Score >= 4.0:** Go (proceed to specification)
- **Score 2.5-3.9:** Conditional (proceed with documented risks)
- **Score < 2.5:** No-Go (defer or remove; flag with `[FEASIBILITY-FAIL]`)

See `references/feasibility-analysis.md` for the scoring rubric and go/no-go decision criteria.

### Step 5: Prioritize Requirements

Apply the prioritization method selected by the stakeholder team. If no method has been chosen, recommend one using the decision tree in `references/requirements-prioritization.md`.

**Supported Methods:**

1. **MoSCoW (Wiegers Practice 9):** Assign each requirement to Must Have, Should Have, Could Have, or Won't Have. Validate that Must Have requirements do not exceed 60% of total effort capacity.

2. **Kano Model:** Classify requirements as Basic (expected), Performance (linear satisfaction), or Excitement (delight). Ensure all Basic requirements are included before Performance requirements.

3. **WSJF (Weighted Shortest Job First):** Calculate priority score:
   $WSJF = \frac{UserValue + TimeCriticality + RiskReduction}{JobSize}$

4. **100-Dollar Method:** Distribute 100 hypothetical dollars across requirements. Aggregate stakeholder allocations and rank by total investment.

Produce a prioritized requirements list sorted by priority score or category, with justification for each ranking decision.

### Step 6: Goal Modeling (Optional)

If business goals in `vision.md` are complex or hierarchical, decompose them using goal-oriented requirements engineering:

- Build AND/OR goal decomposition trees linking business goals to functional requirements
- Identify goal conflicts where satisfying one goal impedes another
- Map agents (actors) to goals they are responsible for achieving

See `references/goal-modeling.md` for KAOS and i* modeling guidance.

### Step 7: Generate Analysis Report

Write the completed analysis to `../output/requirements_analysis_report.md` using the output format below. Log summary statistics: total requirements, classifications, conflicts detected, feasibility failures, and priority distribution.

## Output Format Specification

The generated `requirements_analysis_report.md` SHALL contain the following sections:

```
# Requirements Analysis Report: [Project Name]

## 1. Document Information
## 2. Analysis Summary
### 2.1 Scope and Objectives
### 2.2 Input Artifacts Analyzed
### 2.3 Key Findings
## 3. Requirements Classification Matrix
### 3.1 By Type (Functional / Non-Functional / Constraint / Interface)
### 3.2 By Obligation (Mandatory / Desirable / Optional)
### 3.3 Classification Summary Statistics
## 4. Conflict Detection Report
### 4.1 Contradictions
### 4.2 Redundancies
### 4.3 Subsumptions
### 4.4 Boundary Conflicts
### 4.5 Resolution Recommendations
## 5. Feasibility Assessment
### 5.1 TELOS Scoring Matrix
### 5.2 Go / Conditional / No-Go Summary
### 5.3 Risk Register for Conditional Requirements
## 6. Requirements Prioritization
### 6.1 Method Selected and Rationale
### 6.2 Prioritized Requirements List
### 6.3 Priority Distribution Analysis
## 7. Goal Model (if applicable)
## 8. Recommendations and Next Steps
## 9. Appendix: Standards Traceability
```

## Common Pitfalls

1. **Classifying implementation details as requirements:** A requirement describes *what* the system shall do, not *how* it shall be built. Filter out design decisions during classification.
2. **Ignoring non-functional conflicts:** Two NFRs can conflict (e.g., "response time < 100ms" vs. "encrypt all data at rest with AES-256"). Analyze NFR interactions explicitly.
3. **Feasibility scores without evidence:** Every score SHALL include a one-sentence justification. A number without rationale is an opinion.
4. **MoSCoW inflation:** Stakeholders tend to classify everything as "Must Have." Enforce the 60% capacity cap and challenge classifications with evidence.
5. **Skipping redundancy detection:** Redundant requirements inflate effort estimates and create maintenance burden in the SRS.

## Verification Checklist

- [ ] All required input files were read and logged.
- [ ] Every raw requirement has a unique identifier and classification.
- [ ] Conflict detection covered all four conflict types.
- [ ] Every mandatory requirement has a TELOS feasibility score with justification.
- [ ] No-Go requirements are flagged with `[FEASIBILITY-FAIL]` and excluded from prioritization.
- [ ] Prioritization method is documented with rationale for selection.
- [ ] Must Have requirements do not exceed 60% of capacity (if MoSCoW is used).
- [ ] No subjective adjectives appear without a defined metric.
- [ ] Standards traceability appendix maps sections to IEEE 29148 and IEEE 1233 clauses.

## Integration

| Direction  | Skill                                              | Relationship                                   |
|------------|----------------------------------------------------|-------------------------------------------------|
| Upstream   | `02-requirements-engineering/fundamentals/during/03-*` | Consumes elicitation artifacts              |
| Downstream | `02-requirements-engineering/fundamentals/during/05-*` | Feeds classified requirements to data modeling |
| Downstream | `02-requirements-engineering/fundamentals/during/06-*` | Feeds prioritized requirements to patterns     |
| Downstream | `02-requirements-engineering/waterfall/05-*`           | Feeds into SRS feature decomposition           |

## Standards Compliance

| Standard          | Governs                                                    |
|-------------------|------------------------------------------------------------|
| IEEE 29148-2018   | Requirements analysis activities and classification scheme |
| IEEE 830-1998     | Quality attributes for well-formed requirements            |
| IEEE 1233-1998    | Obligation levels and requirement well-formedness          |
| Laplante Ch.5     | Analysis techniques and feasibility assessment             |
| Wiegers Ch.7-9    | Classification, conflict detection, and prioritization     |

## Resources

- `references/conflict-detection.md` -- Conflict types, detection algorithm, resolution strategies
- `references/feasibility-analysis.md` -- TELOS framework with scoring rubric
- `references/requirements-prioritization.md` -- Four prioritization methods compared
- `references/goal-modeling.md` -- KAOS and i* goal-oriented requirements engineering
