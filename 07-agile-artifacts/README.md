# Phase 07: Agile Artifacts

## Purpose

Generate Scrum ceremony templates and definitions that keep agile teams aligned on process, quality gates, and continuous improvement.

## Skills in This Phase

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-sprint-planning | Sprint_Planning_Template.md | Scrum Guide, IEEE 29148 |
| 2 | 02-definition-of-done | Definition_of_Done.md | Scrum Guide |
| 3 | 03-definition-of-ready | Definition_of_Ready.md | Scrum Guide |
| 4 | 04-retrospective-template | Retrospective_Template.md | Scrum Guide |

## Execution Order

Skills 01-04 are independent and may run in any order. Sprint planning typically comes first to establish the sprint scope, but definitions and retrospectives can be generated at any time.

## Dependencies

- **Upstream:** Phase 02 agile track (user stories, backlog) feeds sprint planning with prioritized work items.
- **Downstream:** Sprint artifacts feed Phase 05 test planning and Phase 09 governance.

## I/O

All skills read from `../project_context/` (vision.md, features.md, quality_standards.md, tech_stack.md) and `../output/` (prioritized_backlog.md, user_stories.md). All skills write to `../output/`.
