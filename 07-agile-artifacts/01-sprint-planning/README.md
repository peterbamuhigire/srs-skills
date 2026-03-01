# 01-Sprint-Planning Skill

## Objective

This skill produces a reusable sprint planning template that structures the sprint planning ceremony. It defines sprint goal derivation, team capacity calculation, backlog item selection, task breakdown, and risk tracking to ensure each sprint starts with a clear, capacity-aware plan aligned to project vision per the Scrum Guide and IEEE 29148.

## Execution Steps

1. Verify `../project_context/vision.md` and `../output/prioritized_backlog.md` exist. Optionally check for `../output/user_stories.md`. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates sprint goal, capacity, backlog selection, task breakdown, and risk sections, then writes `../output/Sprint_Planning_Template.md`.
3. Review the sprint goal to confirm it is a value statement linked to a business objective, not a task list.
4. Verify capacity calculation accounts for ceremonies and non-sprint overhead.
5. Iterate if needed, then proceed to other Phase 07 skills or downstream phases.

## Quality Reminder

Every sprint goal SHALL be a value statement, not a list of tasks. Capacity calculations SHALL deduct ceremony time and planned absences. Backlog selection SHALL flag items that exceed remaining capacity. Flag planning gaps rather than fabricating sprint details.

## Standards

- Scrum Guide (Sprint Planning Ceremony)
- IEEE 29148 (Requirements Traceability)
