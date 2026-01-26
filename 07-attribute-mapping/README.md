# 07-Attribute-Mapping Skill

## Objective

This skill anchors Sections 3.3–3.5 of the SRS by aligning the SQuaRE quality model (ISO/IEC 25010, 25023) with the technology stack bounds. It synthesizes `quality_standards.md` and `tech_stack.md` so the Performance, Design Constraint, and Software System Attribute sections declare measurable, ranked attributes before testing or validation work begins.

## Execution Steps

1. Run `python attribute_mapping.py` from this directory. The script reads `../project_context/quality_standards.md` and `../project_context/tech_stack.md`, infers prioritized quality characteristics, evaluates hardware ceilings (e.g., SATA/NVMe storage, CPU counts), and builds Sections 3.3–3.5.4 in `../output/SRS_Draft.md`.
2. Validate that every Performance requirement follows the canonical format, cites an ISO/IEC 25023 measurement method, and states the load and latency ceilings derived from the hardware specifications. Flag missing measurements before moving on.
3. Confirm that Design Constraints capture implementation standards (language versions, security levels, database integrity policies) referenced in the tech stack and that the Software System Attribute entries use Quality Attribute Scenarios (source, stimulus, environment, artifact, response, response measure) with ranked importance.

## Engineering Rigor: The Quality Model

- Quality Attribute Scenarios are required for every Performance and System Attribute statement; list Source, Stimulus, Environment, Artifact, Response, and Response Measure to keep the logic human-verifiable.
- Rank every attribute per IEEE 830 §4.3.5 and mention the ranking explicitly inside each scenario.
- Every measurable statement must cite ISO/IEC 25023 measurement methods (e.g., timed load tests, availability tracking, MTBF monitoring).
- Explicitly surface environmental constraints such as Intermittent Connectivity or Power Instability so downstream teams understand operational risk.

## Quality Reminder

No filler, no vague adjectives. Every clause needs a number, metric, or method. The Quality Model must read like a human-curated script rather than a marketing pitch—precision and traceability keep the document industrial-grade.
