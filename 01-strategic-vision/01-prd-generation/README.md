# 01-PRD-Generation Skill

## Objective

This skill produces a Product Requirements Document that translates the project vision into a structured, prioritized feature set with measurable objectives. It bridges the gap between strategic intent (Vision Statement) and detailed requirements (SRS or User Stories).

## Execution Steps

1. Verify `../project_context/vision.md` and `../project_context/features.md` exist. Optionally check for `../output/Vision_Statement.md` to enrich the PRD.
2. Invoke `logic.prompt` or trigger the skill. The skill reads context files, generates all PRD sections, and writes `../output/PRD.md`.
3. Review the Feature Priority Matrix to confirm all features from `features.md` are represented with Priority, Effort, Value, and MoSCoW classifications.
4. Proceed to `02-business-case` to generate the financial justification, or to `02-requirements-engineering` for SRS decomposition.

## Quality Reminder

Every objective shall be SMART. Every feature in the priority matrix shall have a rationale. Flag unknowns explicitly rather than fabricating data. The PRD shall read as a decision-making document, not a marketing pitch.

## Standards

- IEEE 29148-2018 (Requirements Engineering)
- IEEE 1233-1998 (System Requirements Specifications)
