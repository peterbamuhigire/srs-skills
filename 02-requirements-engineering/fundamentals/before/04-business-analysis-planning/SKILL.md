---
name: "business-analysis-planning"
description: "Plan business analysis governance, stakeholder engagement, decision rights, work cadence, and artifact strategy before detailed requirements work begins."
metadata:
  use_when: "Use when the task matches business analysis planning and this skill's local workflow."
  do_not_use_when: "Do not use when detailed elicitation or specification has already started and a narrower downstream skill owns the work."
  required_inputs: "Provide the target project, context files, stakeholder information, delivery constraints, and governance assumptions."
  workflow: "Follow the ordered planning, governance, stakeholder, and work-definition steps in this file before moving into elicitation."
  quality_standards: "Keep outputs grounded in project context, explicit about decision rights, and specific enough to guide real analysis work."
  anti_patterns: "Do not invent governance structures, skip decision ownership, or treat business analysis as informal note-taking."
  outputs: "Produce a business analysis plan with governance, engagement, work plan, artifacts, and decision gates."
  references: "Use `references/` when deeper detail is needed."
---

# Business Analysis Planning Skill

## Overview

This skill establishes how requirements and business analysis work will be run before detailed discovery begins. It defines governance, stakeholder engagement, BA work cadence, artifact scope, decision rights, and review gates so the engine can perform analysis consistently instead of improvising artifact by artifact.

## When to Use

- After stakeholder identification is available or can be inferred from `vision.md`
- Before heavy elicitation, workshops, prototypes, or formal specification work begins
- When the project has multiple decision-makers, compliance obligations, or high coordination risk
- When the team needs a defensible plan for who decides what, when, and based on which artifacts

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `../project_context/vision.md`, `../output/stakeholder_register.md` (recommended), `../project_context/features.md`, `../project_context/constraints.md` (optional) |
| **Output** | `../output/business_analysis_plan.md` |
| **Tone** | Operational, governance-oriented, precise |
| **Standards** | PMI Business Analysis for Practitioners, IEEE 29148 |

## Core Instructions

### Step 1: Read Context and Stakeholder Inputs

Read the available project context and stakeholder artifacts. If `stakeholder_register.md` is missing, infer provisional stakeholder groups from `vision.md` and flag them as provisional.

### Step 2: Define Analysis Governance

Specify:
- sponsor and product decision owner
- requirements approval authority
- change review authority
- escalation path for unresolved conflicts
- artifact review and sign-off sequence

Every decision category shall have exactly one accountable owner.

### Step 3: Define Stakeholder Engagement Approach

For each key stakeholder group, document:
- engagement objective
- preferred format: workshop, interview, demo, review, async document feedback
- expected cadence
- participation trigger conditions
- risk if the group becomes unavailable

See `references/governance-and-engagement.md` for an engagement matrix pattern.

### Step 4: Plan Business Analysis Work

Create a work plan covering:
- discovery activities
- modeling activities
- prototyping activities
- validation and review cycles
- baselining points
- dependencies on design, testing, or compliance work

Use milestone-based sequencing instead of vague dates when exact scheduling is not known.

### Step 5: Define Artifact Strategy

State which artifacts are required, optional, or conditional for this project:
- BRD
- process models
- business rules catalog
- conceptual data model
- prototypes
- SRS or user-story outputs
- traceability matrix
- go/no-go evidence

For each artifact, define owner, purpose, entry criteria, and exit criteria.

### Step 6: Define Review and Decision Gates

Document at minimum:
- discovery-complete gate
- scope-freeze or baseline gate
- design-ready gate
- go/no-go gate for implementation or release

Each gate shall state required evidence and approvers.

### Step 7: Write Output

Write `../output/business_analysis_plan.md` with the sections below. Log the analysis activities planned, the stakeholder groups engaged, and all unresolved governance gaps.

## Output Format

The generated `business_analysis_plan.md` shall contain:

1. Purpose and scope
2. Governance model
3. Stakeholder engagement approach
4. Business analysis work plan
5. Artifact strategy
6. Review and decision gates
7. Risks and assumptions
8. Standards traceability

## Common Pitfalls

- Treating workshops and interviews as interchangeable without matching them to stakeholder types
- Allowing multiple approvers to own the same decision without an escalation rule
- Producing analysis artifacts without entry and exit criteria
- Skipping explicit go/no-go evidence until late delivery

## Verification Checklist

- [ ] Governance roles are explicit and non-overlapping.
- [ ] Stakeholder engagement approach exists for every key decision group.
- [ ] Artifact strategy states required vs optional outputs.
- [ ] Review and decision gates have entry evidence and approvers.
- [ ] Risks and unresolved governance gaps are documented.

## References

- `references/governance-and-engagement.md` -- Governance, engagement, and decision-right patterns
