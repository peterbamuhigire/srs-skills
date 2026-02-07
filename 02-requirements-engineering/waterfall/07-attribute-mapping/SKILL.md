---
name: attribute-mapping
description: Turn the prioritized ISO/IEC 25010 quality characteristics and technology stack into Sections 3.3–3.5.4 by documenting measurable performance, constraints, and software system attributes.
---

# Attribute Mapping Skill Guidance

## Overview
Apply this skill after Sections 1.0–3.2 exist. It produces the non-functional attribute sections (Performance, Design Constraints, Reliability/Availability/Security/Maintainability) by analyzing quality standards and tech stack artifacts, which must already describe ISO/IEC 25010 expectations and the primary database/language arsenal.

## Quick Reference
- Inputs: `../project_context/quality_standards.md`, `../project_context/tech_stack.md`
- Output: `../output/SRS_Draft.md` (Sections 3.3–3.5.4)
- Tone: Human-grade, precise, scenario-driven, no AI filler.

## Core Instructions
1. Run `python attribute_mapping.py` from this directory or invoke this skill through `logic.prompt`. The script logs file reads, infers prioritized ISO/IEC 25010 characteristics, and evaluates the tech stack for hardware ceilings and implementation standards.
2. Section 3.3 must contain quantitative Performance requirements following “The system shall [action] within [time] under [load conditions]” plus a Quality Attribute Scenario that covers Source, Stimulus, Environment, Artifact, Response, and Response Measure (ISO/IEC 25023). Flag missing measurements explicitly.
3. Section 3.4 lists mandatory implementation standards, language versions, and database integrity policies discovered in `tech_stack.md` (e.g., PHP 8.2, MySQL/PostgreSQL safeguards, TLS 1.3). Include any environmental risks such as Intermittent Connectivity or Power Instability noted in the context.
4. Section 3.5 documents Reliability (MTBF), Availability (percentage + downtime), Security (AES-256 + RBAC + auditing), and Maintainability (documentation/modularity) as Quality Attribute Scenarios with ranked importance per IEEE 830 §4.3.5.
5. Preserve existing sections (1.0–3.2, 4.0+) when writing to `../output/SRS_Draft.md`; only replace Sections 3.3–3.5.4.

## Resources
- `README.md`: Quality model rationale and measurement reminders.
- `attribute_mapping.py`: Automation that synthesizes the performance, constraint, and attribute sections.
- `logic.prompt`: LLM instructions that enforce scenario structure, ranking, and ISO/IEC 25023 measurability.