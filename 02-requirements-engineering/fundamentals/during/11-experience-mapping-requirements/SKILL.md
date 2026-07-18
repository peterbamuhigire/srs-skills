---
name: 11-experience-mapping-requirements
description: "Use when converting customer, employee, stakeholder, or ecosystem journeys into traceable requirements across touchpoints, pain points, evidence, and future states; use service-blueprint-requirements for backstage delivery detail."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Experience Mapping Requirements

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- converting customer, employee, stakeholder, or ecosystem journeys into traceable requirements across touchpoints, pain points, evidence, and future states; use service-blueprint-requirements for backstage delivery detail.
- Use this procedure when the required source artefacts are available and `Experience map and traceable requirement set` is the next lifecycle deliverable.

## Do Not Use When

- Use `service-blueprint-requirements` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Research evidence, personas, journey scope, touchpoints, emotions, pain points, and outcomes | Users, service owners, and discovery evidence | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Experience map and traceable requirement set`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Experience map and traceable requirement set | PRD, SRS, UX, testing, rollout, and governance owners | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Experience map and traceable requirement set` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A journey claim has no observation, source, or affected persona | Mark it as a hypothesis and schedule validation. | Designed experiences based on invented behaviour. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Experience map and traceable requirement set` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Experience map and traceable requirement set` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `service-blueprint-requirements` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../../docs/skill-authoring-standard.md)
- [Experience Map To Requirement Conversion](references/experience-map-to-requirement-conversion.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/experience_mapping_requirements.md` with:

1. Mapping scope and evidence base.
2. Current-state journey table.
3. Opportunity and failure analysis.
4. Future-state requirement candidates.
5. Journey-to-requirements trace matrix.
6. Validation hypotheses and open research gaps.
