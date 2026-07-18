---
name: hybrid-synchronization
description: "Use when synchronising a Water-Scrum-Fall project so Agile backlog items, DoR/DoD, and delivery evidence remain tied to the approved baseline; use requirements-management for baseline change control itself."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Hybrid Synchronization

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- synchronising a Water-Scrum-Fall project so Agile backlog items, DoR/DoD, and delivery evidence remain tied to the approved baseline; use requirements-management for baseline change control itself.
- Use this procedure when the required source artefacts are available and `Hybrid synchronisation records` is the next lifecycle deliverable.

## Do Not Use When

- Use `requirements-management` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Methodology decision, baseline identifiers, backlog, DoR/DoD, and release evidence | Project context, registries, and delivery owners | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Hybrid synchronisation records`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Hybrid synchronisation records | Product, requirements, delivery, testing, and governance owners | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Hybrid synchronisation records` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A backlog item changes a baselined requirement without an approved trace or change record | Block sprint commitment and route the delta through change control. | Agile delivery drifting from the contractual baseline. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Hybrid synchronisation records` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Hybrid synchronisation records` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `requirements-management` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../docs/skill-authoring-standard.md)
- [Water Scrum Fall Patterns](references/water-scrum-fall-patterns.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## When to use

Invoke after Phase 02 Waterfall SRS is signed off and before the team starts sprint planning. Skip if the project is pure Waterfall or pure Agile.

## Inputs

Read from `projects/<ProjectName>/_context/`:

- `vision.md`
- `features.md`
- `quality-standards.md`
- `methodology.md` (if it exists; otherwise generate from prompts below)

Read from `projects/<ProjectName>/02-requirements-engineering/`:

- the SRS section files (any `*.md` with phase frontmatter `02`)

## Stimulus / Process / Response

1. Read inputs above.
2. Extract every baselined `FR-` and `NFR-` from the SRS sections.
3. Prompt the consultant for: (a) the change-control body, (b) the cadence (sprint length), (c) which features are baseline-locked vs flexible.
4. Render each template with the gathered values:
   - `methodology.md` to `projects/<ProjectName>/_context/methodology.md`
   - `baseline-trace.yaml` to `projects/<ProjectName>/_registry/baseline-trace.yaml`
   - `dor-dod.md` to `projects/<ProjectName>/07-agile-artifacts/definitions/dor-dod.md`
5. Run `python -m engine validate <project>` and report the result.

## Output Contract

After running this skill, the kernel's `HybridSyncGate` MUST pass. If it does not, do not proceed to Phase 07.
