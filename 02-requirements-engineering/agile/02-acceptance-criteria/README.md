# 02-Acceptance-Criteria Skill

## Objective

This skill formalizes acceptance criteria for every user story produced by `01-user-story-generation`. It transforms each "As a / I want / So that" triad into 3--5 Gherkin-format (Given-When-Then) criteria that yield deterministic, binary pass/fail test outcomes. The output shall comply with IEEE 29148-2018 Section 6.4.5 verifiability requirements.

## Execution Steps

1. Read `projects/<ProjectName>/<phase>/<document>/user_stories.md` and extract all user stories by their US-XXX identifiers, parsing the role-action-value triad from each.
2. Generate 3--5 acceptance criteria per story in Given-When-Then format, covering the happy path, error/edge cases, and boundary conditions. If `projects/<ProjectName>/_context/quality_standards.md` exists, append NFR criteria with measurable thresholds.
3. Flag stories that cannot produce testable criteria with `[AC-FAIL]` and include a remediation note identifying the gap.
4. Write the complete criteria set to `projects/<ProjectName>/<phase>/<document>/acceptance_criteria.md` with cross-references back to each originating story and epic.

## Quality Reminder

Every acceptance criterion shall be atomic and deterministic -- a tester shall be able to execute it and arrive at an unambiguous pass or fail. Avoid subjective language such as "fast," "intuitive," or "user-friendly"; replace these with concrete, measurable thresholds drawn from the project quality standards.
