---
name: 04-business-analysis-planning
description: "Use when defining business-analysis governance, decision rights, stakeholder engagement, cadence, artefact plan, and change approach before detailed work; use stakeholder-analysis for the stakeholder register."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Business Analysis Planning Skill

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- defining business-analysis governance, decision rights, stakeholder engagement, cadence, artefact plan, and change approach before detailed work; use stakeholder-analysis for the stakeholder register.
- Use this procedure when the required source artefacts are available and `Business analysis plan` is the next lifecycle deliverable.

## Do Not Use When

- Use `stakeholder-analysis` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Project mandate, delivery method, scope, constraints, governance, and known stakeholders | Sponsor and delivery governance | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Business analysis plan`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Business analysis plan | Business analysts, sponsor, and phase owners | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Business analysis plan` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. This procedure is read-only by default. Editing the reviewed artefact, publishing, production mutation, destructive action, spending, or certification requires explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A decision has no accountable owner or approval path | Stop dependent analysis and assign decision authority. | Unowned requirements and stalled approvals. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Business analysis plan` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Business analysis plan` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `stakeholder-analysis` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../../docs/skill-authoring-standard.md)
- [Governance And Engagement](references/governance-and-engagement.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

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
| **Inputs** | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/<phase>/<document>/stakeholder_register.md` (recommended), `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/_context/constraints.md` (optional) |
| **Output** | `projects/<ProjectName>/<phase>/<document>/business_analysis_plan.md` |
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

Write `projects/<ProjectName>/<phase>/<document>/business_analysis_plan.md` with the sections below. Log the analysis activities planned, the stakeholder groups engaged, and all unresolved governance gaps.

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
