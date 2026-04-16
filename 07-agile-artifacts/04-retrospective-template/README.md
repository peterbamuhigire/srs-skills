# 04-Retrospective-Template Skill

## Objective

This skill produces a reusable sprint retrospective template that structures the retrospective ceremony with multiple facilitation formats. It provides Start-Stop-Continue, 4Ls, and Sailboat formats alongside action item tracking with ownership and deadlines, and continuous improvement metrics to ensure retrospectives drive measurable process improvement per the Scrum Guide.

## Execution Steps

1. Verify `projects/<ProjectName>/_context/vision.md` exists. Halt if the required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates sprint summary, observation sections, action tracking, facilitation formats, and metrics, then writes `projects/<ProjectName>/<phase>/<document>/Retrospective_Template.md`.
3. Review action item fields to confirm each requires an owner, deadline, and success criterion.
4. Verify at least three facilitation formats are present with clear instructions.
5. Iterate if needed, then use the template at the end of each sprint ceremony.

## Quality Reminder

Every action item SHALL have an assigned owner and a target completion date. Improvement observations SHALL focus on process and outcomes, not individuals. The template SHALL provide multiple facilitation formats to prevent ceremony fatigue. Flag missing context rather than fabricating retrospective data.

## Standards

- Scrum Guide (Sprint Retrospective Ceremony)
