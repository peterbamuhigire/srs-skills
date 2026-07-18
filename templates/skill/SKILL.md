---
name: skill
description: Use when creating the named SDLC artefact; use the nearest phase neighbour when it owns a different decision or deliverable.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Skill name

State the procedure's purpose and the concrete SDLC deliverable it controls.

<!-- dual-compat-start -->
## Use When

- Name a concrete positive trigger.
- Name the lifecycle state that makes this procedure applicable.

## Do Not Use When

- Name the nearest neighbour and the condition that routes there.
- Do not run when a required decision owner or source artefact is absent.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Project context | `projects/<ProjectName>/_context/` | Yes | Stop and identify the missing source file. |

## Workflow

1. Inspect the required inputs and record the sources used.
2. Apply the domain decisions and produce the named artefact.
3. Stop when a required source, decision owner, or test oracle is absent.
4. Recover by returning the narrowest qualified draft and a specific gap list.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Named deliverable | Downstream phase owner | Required sections, trace links, and deterministic acceptance checks are present. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source and validation record | Delivery reviewer | Paths, checks, failures, and unresolved gaps are recorded. |
<!-- dual-compat-end -->

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises document creation or repair. Publishing, production mutation, destructive action, spending, and certification claims require explicit authority.

## Degraded mode

If a required file, tool, network source, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the check `not assessed`; never convert it into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| Required source is present and current | Continue and cite it in the evidence record. | Unsupported requirements. |
| Required source is absent | Stop or issue a qualified draft with the gap named. | Fabricated context. |

## Quality Standards

- Tie each requirement or decision to project context and a deterministic review or test oracle.
- Apply the repository anti-slop gate before release.

## Anti-Patterns

- Inventing a missing requirement. Fix: stop and request or flag the source gap.
- Treating a template heading as evidence. Fix: cite the populated project artefact.
- Declaring an unexecuted check passed. Fix: mark it `not assessed`.
- Hiding a neighbour collision. Fix: state the routing boundary in the description and triggers.
- Publishing or mutating production without authority. Fix: return a reviewable draft or plan.

## References

- [Skill authoring and release standard](../../docs/skill-authoring-standard.md)
