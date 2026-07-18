---
name: 07-attribute-mapping
description: "Use when assigning priority, source, rationale, risk, stability, verification method, owner, and other governed attributes to requirements; use traceability-engineering for lifecycle links."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Attribute Mapping Skill Guidance

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- assigning priority, source, rationale, risk, stability, verification method, owner, and other governed attributes to requirements; use traceability-engineering for lifecycle links.
- Use this procedure when the required source artefacts are available and `Requirement attribute register` is the next lifecycle deliverable.

## Do Not Use When

- Use `traceability-engineering` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Atomic requirements, attribute schema, owners, priorities, risks, and verification strategy | Requirements owner and governance standards | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Requirement attribute register`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Requirement attribute register | Requirements management, design, testing, and governance | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Requirement attribute register` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A mandatory attribute has no evidence or accountable owner | Mark the requirement incomplete and withhold baseline approval. | Unowned or unverifiable requirements. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Requirement attribute register` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Requirement attribute register` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `traceability-engineering` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview
Apply this skill after Sections 1.0–3.2 exist. It produces the non-functional attribute sections (Performance, Design Constraints, Reliability/Availability/Security/Maintainability) by analyzing quality standards and tech stack artifacts, which must already describe ISO/IEC 25010 expectations and the primary database/language arsenal.

## Quick Reference
- Inputs: `projects/<ProjectName>/_context/quality_standards.md`, `projects/<ProjectName>/_context/tech_stack.md`
- Output: `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` (Sections 3.3–3.6)
- Tone: Human-grade, precise, scenario-driven, no AI filler.

## Core Instructions
1. Run `python attribute_mapping.py` from this directory or invoke this skill through `logic.prompt`. The script logs file reads, infers prioritized ISO/IEC 25010 characteristics, and evaluates the tech stack for hardware ceilings and implementation standards.
2. Section 3.3 must contain quantitative Performance requirements following “The system shall [action] within [time] under [load conditions]” plus a Quality Attribute Scenario that covers Source, Stimulus, Environment, Artifact, Response, and Response Measure (ISO/IEC 25023). Flag missing measurements explicitly.
3. Section 3.4 lists mandatory implementation standards, language versions, and database integrity policies discovered in `tech_stack.md` (e.g., PHP 8.2, MySQL/PostgreSQL safeguards, TLS 1.3). Include any environmental risks such as Intermittent Connectivity or Power Instability noted in the context.
4. Section 3.5 documents Reliability (MTBF), Availability (percentage + downtime), Security (AES-256 + RBAC + auditing), and Maintainability (documentation/modularity) as Quality Attribute Scenarios with ranked importance per IEEE 830 §4.3.5.
5. Generate **Section 3.5.5 – Standards Compliance** (IEEE 830 §5.3.5.1) listing requirements derived from standards/regulations: report formats, data naming, accounting procedures, audit tracing.
6. Generate **Section 3.6 – Other Requirements** (IEEE 830 §5.3.8) for requirements not fitting 3.1–3.5 (portability, installation, localization). If none, state "No additional requirements beyond those specified in Sections 3.1–3.5 have been identified."
7. Reference `../ieee-830-compliance-checklist.md` (IDs IEEE830-5.3.3 through IEEE830-5.3.7) for compliance verification.
8. Preserve existing sections (1.0–3.2, 4.0+) when writing to `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`; only replace Sections 3.3–3.6.

## Resources
- `README.md`: Quality model rationale and measurement reminders.
- `attribute_mapping.py`: Automation that synthesizes the performance, constraint, and attribute sections.
- `logic.prompt`: LLM instructions that enforce scenario structure, ranking, and ISO/IEC 25023 measurability.
