# 01-High-Level-Design Skill

## Objective

This skill produces a High-Level Design document that translates verified SRS requirements into a system-level architecture with component boundaries, deployment topology, data flow paths, and technology decisions. It serves as the primary architectural blueprint consumed by all subsequent design skills in Phase 03.

## Execution Steps

1. Verify `../output/SRS_Draft.md` and `../project_context/tech_stack.md` exist. Optionally check for `../output/PRD.md` to enrich architectural context.
2. Invoke `logic.prompt` or trigger the skill. The skill reads input files, generates all HLD sections with Mermaid diagrams, and writes `../output/HLD.md`.
3. Review the Traceability Matrix to confirm every HLD component maps to at least one SRS requirement ID.
4. Proceed to `02-low-level-design` for module-level decomposition, or to `03-api-specification` and `04-database-design` once LLD is complete.

## Quality Reminder

Every Mermaid diagram shall have descriptive labels on all nodes and edges. Every technology decision shall cite a specific SRS constraint in its rationale. Every HLD component shall trace back to at least one SRS requirement. Flag architectural assumptions explicitly rather than presenting them as validated decisions.

## Standards

- IEEE 1016-2009 Sec 5 (Architectural Design Viewpoints)
- ISO/IEC 25010 (Quality Model)
