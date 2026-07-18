---
name: 06-logic-modeling
description: "Use when formalising decisions, calculations, state transitions, constraints, and exception logic for Waterfall requirements; use descriptive-modeling for narrative flows and views."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Logic Modeling Skill Guidance

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- formalising decisions, calculations, state transitions, constraints, and exception logic for Waterfall requirements; use descriptive-modeling for narrative flows and views.
- Use this procedure when the required source artefacts are available and `Formal logic models and derived requirements` is the next lifecycle deliverable.

## Do Not Use When

- Use `descriptive-modeling` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Approved rules, states, events, calculations, exceptions, and requirement identifiers | Business-rules analysis and descriptive models | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Formal logic models and derived requirements`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Formal logic models and derived requirements | SRS, design, implementation, and testing teams | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Formal logic models and derived requirements` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A decision table has uncovered or conflicting condition combinations | Stop and resolve completeness or precedence with the rule owner. | Ambiguous or contradictory system behaviour. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Formal logic models and derived requirements` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Formal logic models and derived requirements` from assumed context. Fix: cite the project source or mark the scope blocked.
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
Use this skill after Sections 1.0–3.1 exist. It reads `business_rules.md`, `tech_stack.md`, and `quality_standards.md` to produce the logical and mathematical foundations required by IEEE 1016 before moving on to validation, traceability, or testing chapters.

## Quick Reference
- Inputs: `projects/<ProjectName>/_context/business_rules.md`, `projects/<ProjectName>/_context/tech_stack.md`, `projects/<ProjectName>/_context/quality_standards.md`
- Output: `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` (Sections 3.2.2–3.2.4)
- Tone: Precise, formal, transition-model oriented. Use IF-THEN-ELSE prose where logic branches exist, and avoid subjective adjectives.

## Core Instructions
1. Run `python logic_modeling.py` from this directory or trigger the `logic.prompt`; the script logs each read and writes only the logic sections without deleting previously authored content.
2. Confirm the technology stack contains either MySQL or PostgreSQL so the script can assign `DECIMAL(19,4)` or `NUMERIC(19,4)` types, respectively. Document this dialect choice in the log output.
3. Each process description must list Input, Algorithm (with structured IF-THEN-ELSE paths), and Affected Entities, mention the ISO/IEC 25010 reliability and analysability targets, and enclose calculations in LaTeX.
4. The Data Construct Specifications section describes each record type that supports the Transition Models, and the Data Dictionary tabulates every field with its representation, units/format, and range/accuracy.
5. Track precision behavior explicitly: any monetary or derived numeric value shall be described with the phrase “The system shall round the result to the nearest 2 decimal places using the 'Round Half Up' method.”

## Resources
- `README.md`: Intent, steps, and quality reminders for this skill.
- `logic_modeling.py`: The automation that builds the logic model sections from business rules and technology stack files.
- `logic.prompt`: LLM instructions that enforce reliability/analysability checks, LaTeX formulas, and transition-model thinking.
