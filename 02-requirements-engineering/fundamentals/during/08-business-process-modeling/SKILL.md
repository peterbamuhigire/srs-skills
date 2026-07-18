---
name: 08-business-process-modeling
description: "Use when modelling as-is and to-be workflows, actors, handoffs, controls, events, and exceptions to expose requirements; use service-blueprint-requirements for frontstage/backstage service delivery."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Business Process Modeling Skill

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- modelling as-is and to-be workflows, actors, handoffs, controls, events, and exceptions to expose requirements; use service-blueprint-requirements for frontstage/backstage service delivery.
- Use this procedure when the required source artefacts are available and `Business process models and requirement implications` is the next lifecycle deliverable.

## Do Not Use When

- Use `service-blueprint-requirements` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Process scope, stakeholders, policies, observed evidence, events, and pain points | Process owners, operators, and elicitation records | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Business process models and requirement implications`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Business process models and requirement implications | Requirements analysis, service design, controls, and automation teams | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Business process models and requirement implications` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A handoff has no owner, trigger, completion signal, or exception path | Keep the process unresolved and assign those fields before approval. | Automation built on an incomplete workflow. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Business process models and requirement implications` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Business process models and requirement implications` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `service-blueprint-requirements` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../../docs/skill-authoring-standard.md)
- [Modeling Patterns](references/modeling-patterns.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview

This skill turns workflow knowledge into structured process models that expose roles, handoffs, triggers, decisions, exceptions, controls, and improvement opportunities. It complements use cases and user stories by modeling the business flow itself rather than only system interactions.

## When to Use

- When the solution changes or automates existing business processes
- When handoffs, approvals, queues, or exception handling are central to the problem
- When stakeholders disagree on current-state workflow or future-state ownership
- Before detailed requirements for multi-role workflows are finalized

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/<phase>/<document>/elicitation_log.md`, `projects/<ProjectName>/<phase>/<document>/stakeholder_register.md`, `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/_context/business_rules.md` (optional) |
| **Output** | `projects/<ProjectName>/<phase>/<document>/business_process_models.md` |
| **Tone** | Analytical, operational, role-aware |
| **Standards** | BPM-inspired process analysis, PMI BA practice guidance |

## Core Instructions

### Step 1: Inventory Target Processes

Identify each high-value or high-risk business process affected by the project. For each process, define:
- trigger event
- primary actor
- downstream actors
- business outcome
- business cost if the process fails

### Step 2: Model the Current State

For each process, document the current workflow:
- start trigger
- ordered activities
- actor ownership
- decisions and branching
- data created or consumed
- manual work, delays, and rework points

### Step 3: Model the Future State

Create the target workflow showing:
- what is automated
- what remains manual
- new controls or approvals
- new exception flows
- changed ownership or timing

See `references/modeling-patterns.md` for notation guidance.

### Step 4: Capture Exceptions and Negative Paths

Every process model shall include:
- alternate paths
- exception paths
- abandoned or failed flow handling
- escalation or override conditions

If the model only describes the happy path, flag it with `[PROCESS-GAP: exception handling missing]`.

### Step 5: Extract Requirement Implications

For each process step or decision point, derive:
- candidate functional requirements
- business rules that require separate capture
- interfaces or notifications
- audit or traceability needs
- metrics or SLAs implied by the process

### Step 6: Validate with Stakeholders

Record validation questions for each process:
- Is the current state accurate?
- Is the future state acceptable?
- What exceptions are still missing?
- Which controls are mandatory vs negotiable?

### Step 7: Write Output

Write `projects/<ProjectName>/<phase>/<document>/business_process_models.md` containing current-state and future-state models, exception flows, and requirement implications.

## Output Format

1. Process inventory
2. As-is models
3. To-be models
4. Exceptions and control points
5. Requirement implications
6. Open questions
7. Standards traceability

## Common Pitfalls

- Modeling only screens or APIs instead of the business flow
- Ignoring manual workarounds, queues, and approvals
- Omitting exception paths and escalation rules
- Failing to connect process steps to requirements or controls

## Verification Checklist

- [ ] Every target process has a trigger, actors, and outcome.
- [ ] Current-state and future-state workflows are both documented.
- [ ] Exceptions and control points are explicit.
- [ ] Requirement implications are extracted from the models.
- [ ] Stakeholder validation questions are included.

## References

- `references/modeling-patterns.md` -- As-is/to-be workflow and exception modeling guidance
