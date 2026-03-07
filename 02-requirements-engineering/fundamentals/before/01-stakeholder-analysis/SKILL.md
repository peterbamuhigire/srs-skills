---
name: stakeholder-analysis
description: Identify, classify, and prioritize stakeholders using power/interest grids. Generate a stakeholder register with communication preferences per IEEE 29148 and Wiegers Practices 1-3.
---

# Stakeholder Analysis Skill

## Overview

This skill identifies, classifies, and prioritizes all project stakeholders using a Power/Interest grid methodology. It produces a formal stakeholder register that includes communication preferences, engagement levels, and a RACI mapping for requirements activities. The skill ensures that downstream elicitation, requirements gathering, and validation activities target the correct stakeholders with the appropriate engagement strategy.

## When to Use This Skill

- At the start of any new project before requirements elicitation begins
- When a project undergoes significant scope changes that may introduce new stakeholder groups
- When stakeholder engagement issues (e.g., missed reviews, conflicting priorities) indicate a gap in stakeholder identification
- When transitioning between project phases and communication plans require updates

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `../project_context/vision.md`, `../project_context/features.md` |
| **Output** | `../output/stakeholder_register.md` |
| **Tone** | Analytical, objective, no assumptions without grounding |
| **Standards** | IEEE 29148-2018 Section 6.2, Wiegers Practices 1-3 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `../project_context/vision.md` | Yes | Business goals, problem statement, constraints, target audience |
| features.md | `../project_context/features.md` | Yes | Feature list to identify impacted user groups and technical domains |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| stakeholder_register.md | `../output/stakeholder_register.md` | Complete stakeholder register with classification, communication plan, and RACI matrix |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` and `features.md` from `../project_context/`. Log every file path read. If either file is missing, halt execution and report the gap to the user.

### Step 2: Identify Stakeholder Categories

Extract stakeholders from the context files. The skill shall identify individuals or groups in each of the following categories:

| Category | Description | Typical Sources |
|----------|-------------|-----------------|
| **Sponsors** | Fund the project, approve scope and budget | vision.md business goals, constraints |
| **Primary Users** | Direct, daily users of the system | vision.md target audience, features.md user-facing features |
| **Secondary Users** | Occasional or indirect users | features.md reporting, admin, or support features |
| **Regulators** | External bodies imposing compliance requirements | vision.md constraints, domain-specific regulations |
| **Developers** | Engineering team building the system | features.md technical complexity indicators |
| **Testers** | QA personnel validating the system | features.md acceptance-critical features |
| **Operators** | IT/DevOps maintaining the system in production | features.md deployment, monitoring, infrastructure features |
| **Domain Experts** | Subject matter experts providing domain knowledge | vision.md problem statement, domain-specific terminology |

For each identified stakeholder, record:
- **Stakeholder ID**: SH-001, SH-002, etc.
- **Name or Role**: specific role title
- **Category**: from the table above
- **Description**: one-sentence summary of their relationship to the project

If a category yields no stakeholders from the context files, flag it with `[GAP: No stakeholder identified for {category}. Confirm with project team.]`.

### Step 3: Classify Using Power/Interest Grid

Place each stakeholder on the Power/Interest grid using two dimensions:

- **Power** (High/Low): The stakeholder's ability to influence project decisions, budget, scope, or schedule.
- **Interest** (High/Low): The stakeholder's level of concern about project outcomes and deliverables.

Assign an engagement strategy based on quadrant placement:

| Quadrant | Power | Interest | Strategy | Description |
|----------|-------|----------|----------|-------------|
| **Manage Closely** | High | High | Active collaboration, frequent updates, decision involvement | These stakeholders drive project direction. |
| **Keep Satisfied** | High | Low | Regular status reports, escalation channel, periodic check-ins | These stakeholders can block progress if dissatisfied. |
| **Keep Informed** | Low | High | Newsletters, demo invitations, feedback channels | These stakeholders provide valuable input but lack authority. |
| **Monitor** | Low | Low | Minimal engagement, periodic awareness updates | These stakeholders need only basic awareness. |

For each classification, provide a one-sentence rationale grounded in evidence from the context files. If the classification is inferred rather than directly stated, tag it with `[INFERRED]`.

### Step 4: Assess Stakeholder Influence and Impact

For each stakeholder, assess the following attributes on a 1-5 scale:

| Attribute | Scale | Definition |
|-----------|-------|------------|
| **Influence** | 1 (Minimal) to 5 (Decisive) | Ability to affect project decisions |
| **Impact** | 1 (Negligible) to 5 (Critical) | Degree to which the project affects this stakeholder |
| **Engagement Level** | Unaware, Resistant, Neutral, Supportive, Leading | Current posture toward the project |
| **Desired Engagement** | Neutral, Supportive, Leading | Target posture for project success |

Flag any stakeholder where Engagement Level is "Resistant" with `[RISK: Stakeholder resistance -- mitigation required]`.

### Step 5: Generate Communication Plan

For each stakeholder (or stakeholder group), define a communication plan entry:

| Stakeholder | Frequency | Format | Channel | Content | Owner |
|-------------|-----------|--------|---------|---------|-------|
| SH-001: Project Sponsor | Weekly | Status Report | Email + Meeting | Budget, milestones, risks | PM |
| SH-002: Primary Users | Bi-weekly | Demo + Feedback | Workshop | Feature previews, usability | BA |
| SH-003: Regulators | Monthly | Compliance Brief | Formal Document | Regulatory alignment | Compliance Lead |

The communication plan shall cover:
- **Frequency**: Daily, Weekly, Bi-weekly, Monthly, Ad-hoc, or Milestone-based
- **Format**: Meeting, Status Report, Demo, Workshop, Newsletter, Formal Document
- **Channel**: Email, Video Call, In-Person, Collaboration Tool, Formal Submission
- **Content**: What information the stakeholder needs
- **Owner**: Who is responsible for the communication (use role titles; mark `[OWNER-TBD]` if unknown)

### Step 6: Generate RACI Matrix

Produce a RACI matrix mapping stakeholders to key requirements engineering activities:

| Activity | Sponsor | Primary Users | Developers | Testers | Regulators | Operators |
|----------|---------|---------------|------------|---------|------------|-----------|
| Requirements Elicitation | I | R | C | I | C | I |
| Requirements Validation | A | R | C | C | C | I |
| Requirements Approval | A | C | I | I | C | I |
| Change Request Review | A | C | C | I | C | I |
| Acceptance Testing | I | R | C | R | C | I |
| Deployment Sign-off | A | I | R | C | I | R |

RACI definitions per IEEE 29148:
- **R (Responsible)**: Performs the work
- **A (Accountable)**: Owns the decision, one per activity
- **C (Consulted)**: Provides input before the decision
- **I (Informed)**: Notified after the decision

Every activity row shall have exactly one "A" assignment. Flag violations with `[RACI-FAIL: Multiple accountable parties for {activity}]`.

### Step 7: Write Output

Assemble all sections and write the completed document to `../output/stakeholder_register.md`. Log the total stakeholder count, the number of gaps flagged, and the number of risk tags applied.

## Output Format Specification

The generated `stakeholder_register.md` shall follow this structure:

```
# Stakeholder Register: [Project Name]

## Document Header
- Project: [Name]
- Version: 1.0
- Date: [Current Date]
- Status: Draft

## 1. Stakeholder Inventory
### 1.1 Stakeholder List
### 1.2 Identification Gaps

## 2. Power/Interest Classification
### 2.1 Grid Summary
### 2.2 Quadrant Details

## 3. Influence and Impact Assessment

## 4. Communication Plan
### 4.1 Communication Schedule
### 4.2 Escalation Procedures

## 5. RACI Matrix

## 6. Stakeholder Risks and Mitigations

## 7. Standards Traceability

## Appendix A: Glossary
## Appendix B: Revision History
```

## Common Pitfalls

- Identifying only obvious stakeholders (sponsors, users) and missing regulators, operators, or domain experts who surface late in the project
- Classifying all stakeholders as "High Power / High Interest," which dilutes engagement focus and overloads communication plans
- Producing a communication plan without assigned owners, making it unenforceable
- Omitting the RACI matrix, which leads to ambiguous accountability during requirements reviews
- Making stakeholder classifications without grounding them in context file evidence

## Verification Checklist

- [ ] All required input files were read and logged
- [ ] All eight stakeholder categories were evaluated (with gaps flagged where applicable)
- [ ] Every stakeholder has a Power/Interest quadrant assignment with rationale
- [ ] Influence and Impact scores use the defined 1-5 scale consistently
- [ ] Communication plan specifies frequency, format, channel, content, and owner for every stakeholder
- [ ] RACI matrix has exactly one "A" per activity row
- [ ] Resistant stakeholders are flagged with risk tags
- [ ] No subjective adjectives appear without a defined metric or evidence reference
- [ ] Standards Traceability section maps to IEEE 29148 Section 6.2

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | `01-strategic-vision/01-prd-generation` | Consumes vision and feature context |
| Downstream | `02-elicitation-toolkit` | Feeds stakeholder register for technique selection |
| Downstream | `03-brd-generation` | Feeds stakeholder data for BRD stakeholder section |
| Downstream | `02-requirements-engineering/waterfall/02-context-engineering` | Stakeholder context for SRS |

## Standards Compliance

| Standard | Governs |
|----------|---------|
| IEEE 29148-2018 Section 6.2 | Stakeholder identification and requirements sources |
| Wiegers Practice 1 | Stakeholder identification techniques |
| Wiegers Practice 2 | Stakeholder classification and prioritization |
| Wiegers Practice 3 | Stakeholder engagement planning |
| IEEE Std 610.12-1990 | Terminology definitions for stakeholder roles |

## Resources

- `references/stakeholder-map-template.md` -- Power/Interest grid template with quadrant definitions
- `references/raci-matrix.md` -- RACI matrix template with usage guide
