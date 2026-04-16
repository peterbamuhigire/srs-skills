# 02-Definition-of-Done Skill

## Objective

This skill produces a Definition of Done checklist that establishes the quality bar for increments. It defines verifiable criteria across code quality, testing, documentation, review, and deployment readiness at item, increment, and release levels to ensure every backlog item meets a consistent standard before it can be considered complete per the Scrum Guide.

## Execution Steps

1. Verify `projects/<ProjectName>/_context/quality_standards.md` exists. Optionally check for `projects/<ProjectName>/_context/tech_stack.md`. Halt if the required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates criteria across six categories and two aggregate levels, then writes `projects/<ProjectName>/<phase>/<document>/Definition_of_Done.md`.
3. Review every criterion to confirm it is verifiable with a clear pass/fail outcome.
4. Verify testing criteria reference the specific coverage threshold from `quality_standards.md`.
5. Iterate if needed, then share the DoD with the team and reference it from sprint planning.

## Quality Reminder

Every criterion SHALL be verifiable with a pass/fail outcome -- avoid vague statements like "code is clean." Testing criteria SHALL reference specific coverage percentages. The DoD SHALL distinguish between item-level, increment-level, and release-level criteria. Flag missing quality standards rather than fabricating thresholds.

## Standards

- Scrum Guide (Definition of Done)
