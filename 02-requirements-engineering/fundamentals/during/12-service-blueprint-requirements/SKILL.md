---
name: 12-service-blueprint-requirements
description: "Use when turning a service blueprint into requirements for frontstage UX, backstage operations, support, evidence, handoffs, failures, and recovery; use experience-mapping-requirements for the journey view."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Service Blueprint Requirements

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- turning a service blueprint into requirements for frontstage UX, backstage operations, support, evidence, handoffs, failures, and recovery; use experience-mapping-requirements for the journey view.
- Use this procedure when the required source artefacts are available and `Service-blueprint requirements pack` is the next lifecycle deliverable.

## Do Not Use When

- Use `experience-mapping-requirements` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Approved journey, actors, frontstage steps, backstage processes, support systems, evidence, and policies | Service owners, operators, and discovery artefacts | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Service-blueprint requirements pack`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Service-blueprint requirements pack | SRS, UX, operations, testing, and governance owners | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Service-blueprint requirements pack` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A frontstage promise lacks a backstage owner or recovery mechanism | Block the promise and specify ownership, support, and failure handling. | Service commitments the operation cannot fulfil. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Service-blueprint requirements pack` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Service-blueprint requirements pack` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `experience-mapping-requirements` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../../docs/skill-authoring-standard.md)
- [Service Blueprint Requirement Checklist](references/service-blueprint-requirement-checklist.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/service_blueprint_requirements.md` with:

1. Service scenario and blueprint scope.
2. Blueprint lane table.
3. Handoff, evidence, and failure analysis.
4. Derived requirements by type.
5. Operational acceptance and recovery scripts.
6. Trace matrix and unresolved service risks.
