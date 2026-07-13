---
name: 02-context-engineering
description: "Use when defining the system boundary, actors, external systems, interfaces, assumptions, and context after an SRS workspace exists; use descriptive-modeling for detailed behavioural views."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

> **[MISSING FILE FALLBACK]**
> This skill references auxiliary files (`logic.prompt`, Python scripts) for automated execution.
> **If those files are unavailable in your environment**, Claude can execute this skill directly:
> 1. Read all files in `projects/<ProjectName>/_context/`
> 2. Follow the step-by-step instructions in the **Manual Execution** section below (or ask Claude to generate the relevant SRS section by describing the context inline)
> 3. Write output to `projects/<ProjectName>/02-requirements-engineering/01-srs/<section-file>.md`
>
> _This skill is fully executable without Python or logic.prompt by providing context directly to Claude._

# Context Engineering Skill Guidance

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- defining the system boundary, actors, external systems, interfaces, assumptions, and context after an SRS workspace exists; use descriptive-modeling for detailed behavioural views.
- Use this procedure when the required source artefacts are available and `System context model` is the next lifecycle deliverable.

## Do Not Use When

- Use `descriptive-modeling` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Initialised SRS, stakeholders, business context, constraints, and known external systems | Project context and system owners | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `System context model`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| System context model | Requirements, architecture, interface, security, and test owners | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `System context model` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| An external dependency has no owner, contract, or failure behaviour | Mark it unresolved and block dependent interface requirements. | Hidden boundary assumptions. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `System context model` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `System context model` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `descriptive-modeling` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview
Use this skill once the project context templates have been populated. It turns `vision.md` and `glossary.md` into Section 1.0 of the SRS, emphasizing the legal/technical boundaries, definitions, and governing standards before downstream requirements are generated.

## Quick Reference
- Input files: `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/_context/glossary.md`
- Output file: `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` (Section 1.0 only)
- Tone: Standardized Document Header + active engineering prose; avoid conversational phrases.
- Traceability: Each scope bullet must refer back to a Stakeholder Need entry in `vision.md`.

## Core Instructions
1. Run `python context_engineering.py` from within this directory or trigger the `logic.prompt` via your skill runner.
2. The script reads the problem statement, stakeholder needs, and system constraints to separate Business Intent from Technical Scope, then builds Section 1.0 with the required subsections.
3. The glossary table drives Section 1.3 (Definitions, Acronyms, and Abbreviations) so that IEEE 610.12 and ISO/IEC 15504-1 terms are standardized and unambiguous.
4. References include the required IEEE and ISO/IEC standards plus the project context files used for traceability.
5. Always keep the Standardized Document Header in place; do not allow the section to drift into conversational or promotional language.
6. Validate that `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` exists and contains the new introduction before closing the skill run.

### Out of Scope

The following items are explicitly **excluded** from this project's scope. Listing exclusions prevents false assumptions and scope creep.

| # | Out-of-Scope Item | Reason / Notes |
|---|-------------------|----------------|
| 1 | [Item] | [Why excluded or deferred] |

**Generation rule:** For every major feature area mentioned in the project description, explicitly state whether it is IN or OUT of scope. If something a stakeholder might reasonably expect is not being built, list it here. A blank Out of Scope table is a red flag — revisit with stakeholders.

**Audit tag:** If this section is empty or absent, Skill 08 (Semantic Auditing) shall flag `[CONTEXT-GAP: Out of Scope not defined]`.

## Resources
- `README.md`: Provides the synthesis intent for this skill.
- `context_engineering.py`: The automation script that performs the extraction, synthesis, and file writing described above.
- `logic.prompt`: Instructions for Claude to orchestrate this skill with the required tone, standards, and logging.
