# 03-Descriptive-Modeling Skill

## Objective

This skill synthesizes Section 2.0 (Descriptive Modeling) of the SRS by analyzing `tech_stack.md`, `features.md`, and `quality_standards.md`. It captures the system context (Product Perspective), major capabilities (Product Functions), user personas, constraints, and external dependencies so the Introduction skill can hand off a fully grounded Section 2.0.

## Execution Steps

1. Run `python descriptive_modeling.py` from this directory. The script accesses `../project_context/tech_stack.md`, `features.md`, and `quality_standards.md`, then updates `../output/SRS_Draft.md` by replacing Section 2.0 with freshly synthesized content.
2. The output includes a System Block Diagram description, separates hardware + memory constraints, and groups features into Major Capability summaries.
3. Constraints include ISO/IEC 25051 Ready-to-Use principles and local environmental factors (e.g., Uganda power/internet stability). Technical realism is enforced—HP Z440 mentions produce on-premise descriptions, and adjectives are avoided.
4. Verify the new section in `../output/SRS_Draft.md` and ensure the diagrams, constraints, assumptions, and dependencies align with the governing standards.

## Quality Commitment

Use active, direct voice. Each scope or constraint statement SHALL map back to a specific stakeholder need or context entry. System block diagram descriptions must reference real infrastructure components (OCI, HP Z440, MySQL 8.0, etc.).
