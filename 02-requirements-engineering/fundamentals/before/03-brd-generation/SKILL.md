---
name: "brd-generation"
description: "Generate a Business Requirements Document bridging strategic vision to technical requirements. Includes a decision gate for determining BRD necessity. Per IEEE 29148 Section 6.4 and Business Requirements Gathering Ch.2-4."
metadata:
  use_when: "Use when the task matches brd generation skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `references/` when deeper detail is needed."
---

# BRD Generation Skill

## Overview

This skill generates a Business Requirements Document (BRD) that bridges strategic vision to detailed technical requirements. The BRD captures business objectives, scope boundaries, business rules, process flows, and measurable success criteria. The skill includes a decision gate that evaluates whether a formal BRD is warranted for the project, making it optional for smaller or agile-first initiatives.

## When to Use This Skill

- After stakeholder analysis and elicitation have been completed
- When the project requires formal documentation of business requirements before SRS authoring
- When multiple stakeholder groups need a shared understanding of business scope and rules
- When regulatory or contractual obligations mandate a BRD artifact

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/<phase>/<document>/stakeholder_register.md`, `projects/<ProjectName>/<phase>/<document>/elicitation_log.md` |
| **Output** | `projects/<ProjectName>/<phase>/<document>/brd.md` |
| **Tone** | Business-formal, objective, decision-oriented |
| **Standards** | IEEE 29148-2018 Section 6.4, Business Requirements Gathering Ch.2-4 |
| **Optional** | Yes -- includes decision gate |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `projects/<ProjectName>/_context/vision.md` | Yes | Business goals, problem statement, constraints |
| features.md | `projects/<ProjectName>/_context/features.md` | Yes | Feature list with descriptions |
| stakeholder_register.md | `projects/<ProjectName>/<phase>/<document>/stakeholder_register.md` | Yes | Stakeholder roles, classifications, communication plan |
| elicitation_log.md | `projects/<ProjectName>/<phase>/<document>/elicitation_log.md` | No | Elicitation findings with source attribution |
| glossary.md | `projects/<ProjectName>/_context/glossary.md` | No | Domain terminology (IEEE 610.12) |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| brd.md | `projects/<ProjectName>/<phase>/<document>/brd.md` | Complete Business Requirements Document |

## Core Instructions

### Step 0: Decision Gate

Before generating the BRD, evaluate whether a formal BRD is warranted. Present the following checklist to the user:

| Criterion | Yes/No | Weight |
|-----------|--------|--------|
| The project involves multiple stakeholder groups with competing priorities | | 3 |
| Regulatory or compliance requirements mandate formal business documentation | | 3 |
| The project is contractually obligated to deliver a BRD | | 3 |
| The project budget exceeds the organization's "small project" threshold | | 2 |
| The project spans multiple departments or business units | | 2 |
| The project replaces or integrates with existing business processes | | 2 |
| The project timeline exceeds 6 months | | 1 |
| Stakeholder alignment is uncertain or contested | | 1 |

**Scoring**:
- Calculate weighted score: $Score = \sum (Weight_i \times YesFlag_i)$
- If $Score \geq 8$: BRD is **recommended**. Proceed with generation.
- If $4 \leq Score < 8$: BRD is **optional**. Present recommendation to user and await confirmation.
- If $Score < 4$: BRD is **not recommended**. Suggest proceeding directly to SRS or user story generation. Halt unless user overrides.

Reference: `references/decision-gate.md`

### Step 1: Read Context Files

Read all required input files. Optionally read `elicitation_log.md` and `glossary.md`. Log every file path read. If `vision.md`, `features.md`, or `stakeholder_register.md` is missing, halt execution and report the gap.

### Step 2: Generate Document Header

Write the document header containing:
- Project name (from `vision.md`)
- Version: `1.0`
- Date: current date
- Authors: extracted from context or marked `[AUTHOR-TBD]`
- Document Status: `Draft`
- Approval signatories: extracted from stakeholder register (Sponsor, key stakeholders) or marked `[SIGNATORY-TBD]`

### Step 3: Generate Executive Summary

Write a concise summary (2-3 paragraphs) covering:
- The business problem or opportunity being addressed
- The proposed solution at a high level
- The expected business value and strategic alignment
- Key stakeholder groups affected

Use active voice. Do not include implementation details. Ground every assertion in `vision.md` content.

### Step 4: Generate Business Objectives

For each business goal in `vision.md`, produce a formal business objective:

```
#### BO-XXX: [Objective Title]

- **Description**: [What the business seeks to achieve]
- **Alignment**: [Which strategic goal this supports]
- **Success Metric**: [Quantitative measure of achievement]
- **Target Value**: [Specific threshold]
- **Timeline**: [Target date or milestone]
- **Source**: [Stakeholder ID or context file reference]
```

Flag objectives lacking a measurable success metric with `[METRIC-TBD]`.

### Step 5: Generate Scope Definition

Define the project scope with explicit boundaries:

**In Scope:**
- List every feature from `features.md` that is included in this project phase
- For each item, provide a one-sentence scope statement

**Out of Scope:**
- List features, integrations, or capabilities explicitly excluded
- For each exclusion, provide a rationale

**Scope Assumptions:**
- List assumptions that, if invalidated, would change the scope
- Tag each with `[ASSUMPTION]`

### Step 6: Generate Stakeholder Summary

Summarize stakeholder information from `stakeholder_register.md`:
- Key stakeholder groups and their interests
- Decision-making authority mapping
- Communication and engagement summary
- Conflicts or competing priorities identified during elicitation

### Step 7: Generate Business Requirements

For each business requirement identified from context files and elicitation findings, produce a formal entry:

```
#### BR-XXX: [Requirement Title]

- **Description**: The business shall [requirement statement in active voice].
- **Priority**: Critical | High | Medium | Low
- **Source**: [Stakeholder ID] -- [Elicitation Finding ID if available]
- **Rationale**: [Why this requirement exists]
- **Acceptance Criterion**: [Measurable condition for satisfaction]
- **Dependencies**: [BR-YYY, BR-ZZZ] (if any)
- **Assumptions**: [Related assumptions]
```

Requirements shall use "The business shall..." or "The organization shall..." language (not "The system shall..." which belongs in the SRS).

### Step 8: Generate Business Rules

Document business rules that govern system behavior:

```
#### RULE-XXX: [Rule Name]

- **Statement**: [Formal rule statement]
- **Source**: [Regulatory body, policy document, or stakeholder]
- **Type**: Constraint | Policy | Computation | Inference
- **Example**: [Concrete example of the rule in action]
- **Exceptions**: [Conditions under which the rule does not apply]
```

For computation rules, express the formula in LaTeX notation. Example:
- $LateFee = Balance \times DailyRate \times DaysOverdue$

### Step 9: Generate Process Flows

For each major business process affected by the project:

1. Identify the process name and owner
2. Document the current state (as-is) process steps
3. Document the future state (to-be) process steps
4. Highlight changes and improvements
5. Describe the process using a numbered step sequence

If a process cannot be fully described from available context, flag it with `[PROCESS-INCOMPLETE: Additional elicitation required for {process name}]`.

### Step 10: Generate Success Criteria and Remaining Sections

**Success Criteria:**
- Define 3-7 measurable success criteria linked to business objectives
- Each criterion shall include: metric, baseline, target, measurement method, and review frequency

**Assumptions and Constraints:**
- **Assumptions**: Conditions believed to be true but not yet verified (tag each `[ASSUMPTION]`)
- **Constraints**: Fixed limitations on the project (budget, timeline, technology, regulatory)

**Glossary:**
- Include all domain-specific terms used in the BRD
- Align definitions with IEEE Std 610.12-1990 where applicable
- Reference `glossary.md` if available

Write the completed document to `projects/<ProjectName>/<phase>/<document>/brd.md`. Log the total count of business objectives, requirements, rules, and process flows.

## Output Format Specification

The generated `brd.md` shall follow this structure:

```
# Business Requirements Document: [Project Name]

## Document Header
## 1. Executive Summary
## 2. Business Objectives
## 3. Scope Definition
### 3.1 In Scope
### 3.2 Out of Scope
### 3.3 Scope Assumptions
## 4. Stakeholder Summary
### 4.1 Key Stakeholders
### 4.2 Decision Authority
### 4.3 Communication Summary
## 5. Business Requirements
## 6. Business Rules
## 7. Process Flows
### 7.1 Current State (As-Is)
### 7.2 Future State (To-Be)
## 8. Success Criteria
## 9. Assumptions and Constraints
### 9.1 Assumptions
### 9.2 Constraints
## 10. Glossary
## 11. Standards Traceability
## 12. Approval and Sign-off
## Appendix A: Revision History
```

## Common Pitfalls

- Skipping the decision gate and generating a BRD for projects that do not warrant one, creating unnecessary overhead
- Writing system-level requirements ("The system shall...") instead of business-level requirements ("The business shall...")
- Defining business rules without examples, making them ambiguous and unverifiable
- Listing assumptions without tagging them, causing scope confusion when assumptions prove false
- Omitting the as-is process flow, making it impossible to quantify the improvement the to-be process delivers
- Including implementation details that belong in the SRS rather than the BRD

## Verification Checklist

- [ ] Decision gate was evaluated and the score justified BRD generation
- [ ] All required input files were read and logged
- [ ] Every business goal in `vision.md` maps to at least one business objective with a success metric
- [ ] Every business requirement uses "The business shall..." or "The organization shall..." language
- [ ] Every business requirement has a priority, source, and acceptance criterion
- [ ] Business rules include type classification, examples, and exception conditions
- [ ] Computation rules use LaTeX notation for formulas
- [ ] Process flows include both as-is and to-be states (or are flagged as incomplete)
- [ ] Success criteria are measurable with baseline, target, and method defined
- [ ] All assumptions are tagged with `[ASSUMPTION]`
- [ ] Glossary aligns with IEEE Std 610.12-1990
- [ ] Standards Traceability section maps to IEEE 29148 Section 6.4

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | `01-stakeholder-analysis` | Consumes stakeholder register |
| Upstream | `02-elicitation-toolkit` | Consumes elicitation findings |
| Downstream | `02-requirements-engineering/waterfall/01-initialize-srs` | Feeds business context for SRS |
| Downstream | `02-requirements-engineering/waterfall/05-feature-decomposition` | Business requirements decompose into system features |
| Downstream | `02-requirements-engineering/agile/01-user-story-generation` | Business requirements inform epic/story creation |

## Standards Compliance

| Standard | Governs |
|----------|---------|
| IEEE 29148-2018 Section 6.4 | Business requirements specification process |
| Business Requirements Gathering Ch.2 | Business objective formulation |
| Business Requirements Gathering Ch.3 | Business rule documentation |
| Business Requirements Gathering Ch.4 | Process flow analysis |
| IEEE Std 610.12-1990 | Terminology definitions |

## Resources

- `references/brd-template.md` -- Complete BRD template with examples
- `references/decision-gate.md` -- Decision criteria for BRD necessity
