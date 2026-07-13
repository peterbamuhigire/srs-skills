---
name: 04-interface-specification
description: "Use when specifying system-level user, software, hardware, communication, and external interfaces in the SRS; use api-specification for an implementation-ready OpenAPI contract."
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

# Interface Specification Skill Guidance

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- specifying system-level user, software, hardware, communication, and external interfaces in the SRS; use api-specification for an implementation-ready OpenAPI contract.
- Use this procedure when the required source artefacts are available and `SRS interface specification` is the next lifecycle deliverable.

## Do Not Use When

- Use `api-specification` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| System context, external actors, data concepts, protocols, constraints, and error expectations | Context engineering, stakeholders, and integration owners | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `SRS interface specification`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| SRS interface specification | Architecture, API, UX, integration, and testing teams | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `SRS interface specification` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| An interface lacks ownership, validation, error, timeout, or version behaviour | Block approval and complete the interface contract. | Integration failure hidden behind a happy path. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `SRS interface specification` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `SRS interface specification` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `api-specification` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview
Use this skill after Sections 1.0 and 2.0 are generated. It analyzes the technology stack, feature set, and quality standards to produce Section 3.1 (Interface Specification), ensuring the project transitions from descriptive modeling to explicit connectivity requirements.

## Quick Reference
- Inputs: `projects/<ProjectName>/_context/tech_stack.md`, `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/_context/quality_standards.md`
- Output: `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` (Section 3.1 only)
- Tone: Technical, precise, employing SHALL statements; avoid subjective adjectives and mention standards such as ISO/IEC 25010 and ISO/IEC 25062.

## Core Instructions
1. Run `python interface_specification.py` from this directory or invoke the `logic.prompt` through your skill runner.
2. Detect infrastructure keywords (Ubuntu, OCI, MySQL, HP Z440, etc.), extract external actors from feature user stories, and log all parsing steps.
3. Write Section 3.1 with subsections 3.1.1–3.1.4. Include Markdown tables for hardware and software interfaces when applicable, list ports/protocols explicitly (e.g., 443/TLS 1.3, 3306, 5432, IEEE 802.11ax, RFC 7519 JWT), and describe the communication stack connectivity map.
4. Confirm Section 3.1 references ISO/IEC 25062 input validation and ISO/IEC 25010 usability, and mention ISO/IEC 25051 Ready-to-Use expectations if needed.
5. Validate that the updated `SRS_Draft.md` retains Sections 1.0 and 2.0 content while replacing or appending Section 3.1.

## Resources
- `README.md`: Explains the intent and quality expectation for this skill.
- `interface_specification.py`: Automation script that performs detection, grouping, and writing of Section 3.1.
- `logic.prompt`: Provides meta instructions for Claude to orchestrate the process.
