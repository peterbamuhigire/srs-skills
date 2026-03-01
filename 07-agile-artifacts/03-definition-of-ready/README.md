# 03-Definition-of-Ready Skill

## Objective

This skill produces a Definition of Ready checklist that establishes the minimum refinement standard for backlog items before they can be committed to a sprint. It covers story completeness, acceptance criteria format, sizing, dependency resolution, and design clarity to prevent poorly defined work from entering a sprint per the Scrum Guide.

## Execution Steps

1. Verify `../project_context/vision.md` exists. Optionally check for `../project_context/features.md`. Halt if the required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates readiness criteria across five categories plus a refinement process, then writes `../output/Definition_of_Ready.md`.
3. Review acceptance criteria requirements to confirm they mandate Given-When-Then or equivalent testable format.
4. Verify sizing criteria require items to fit within a single sprint.
5. Iterate if needed, then share the DoR with the team and reference it during backlog refinement.

## Quality Reminder

Every readiness criterion SHALL be verifiable before sprint commitment. Acceptance criteria SHALL mandate a testable format such as Given-When-Then. Sizing criteria SHALL enforce a single-sprint size limit. Flag missing context rather than fabricating readiness standards.

## Standards

- Scrum Guide (Backlog Refinement, Sprint Commitment)
