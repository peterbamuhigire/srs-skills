---
name: 03-descriptive-modeling
description: "Use when modelling requirement behaviour with scenarios, flows, states, activities, and domain views after the system context is known; use logic-modeling for formal decision logic."
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

# Descriptive Modeling Skill Guidance

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- modelling requirement behaviour with scenarios, flows, states, activities, and domain views after the system context is known; use logic-modeling for formal decision logic.
- Use this procedure when the required source artefacts are available and `Descriptive behaviour models` is the next lifecycle deliverable.

## Do Not Use When

- Use `logic-modeling` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| System context, actors, requirements evidence, events, states, and business processes | Context engineering and domain owners | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Descriptive behaviour models`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Descriptive behaviour models | Feature decomposition, interface, logic, and test design | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Descriptive behaviour models` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A model path has no initiating event or observable outcome | Reject the path until trigger and outcome are explicit. | Diagrams that cannot yield requirements or tests. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Descriptive behaviour models` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Descriptive behaviour models` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `logic-modeling` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview
Invoke this skill after initializing the project context and generating Section 1.0. It reads the technology stack, feature set, and quality standards to produce Section 2.0 (Descriptive Modeling) with technical realism, block diagram descriptions, and constraint traceability.

## Quick Reference
- Inputs: `projects/<ProjectName>/_context/tech_stack.md`, `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/_context/quality_standards.md`
- Output: `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` (Section 2.0 only)
- Tone: Engineering prose using SHALL statements; System Block Diagram descriptions must mention actual infrastructure components (OCI, HP Z440, MySQL 8.0, etc.).

## Core Instructions
1. Run `python descriptive_modeling.py` from this directory or trigger `logic.prompt` through your skill runner.
2. The script analyzes the tech stack keywords, groups features into Major Capability buckets, reads quality constraints, and writes Section 2.0 with subsections 2.1–2.5.
3. Ensure the script replaces any existing Section 2.0 block in `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` and leaves the rest of the document untouched.
4. Verify the new section includes ALL IEEE 830 §5.2 subsections:
   - 2.1 Product Perspective with all eight sub-items (§5.2.1.1–§5.2.1.8): System Interfaces, User Interfaces, Hardware Interfaces, Software Interfaces, Communications Interfaces, Memory Constraints, Operations, Site Adaptation Requirements.
   - 2.2 Product Functions, 2.3 User Characteristics, 2.4 Constraints (including ISO/IEC 25051 and environmental factors), 2.5 Assumptions and Dependencies.
   - **2.6 Apportioning of Requirements** (IEEE 830 §5.2.6) — lists requirements deferred to future versions, or explicitly states none are deferred.
5. Confirm Section 2.0 references the governance standards and maintains traceability back to vision-derived stakeholder needs.
6. Reference `../ieee-830-compliance-checklist.md` (IDs IEEE830-5.2.1 through IEEE830-5.2.6) for compliance verification.

## Resources
- `README.md`: Skill intent, environmental mapping, and quality reminders.
- `descriptive_modeling.py`: Automation script that synthesizes Section 2.0.
- `logic.prompt`: Meta instructions for language models to orchestrate the process with the required tone and logging.
