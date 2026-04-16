---
name: "sprint-planning"
description: "Generate a sprint planning template with sprint goal, capacity calculation, selected backlog items, task breakdown, and risk tracking per the Scrum Guide and IEEE 29148."
metadata:
  use_when: "Use when the task matches sprint planning skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Sprint Planning Skill

## Overview

This skill produces a reusable sprint planning template that structures the sprint planning ceremony. It defines the sprint goal, team capacity calculation, backlog item selection criteria, task breakdown format, risk and dependency tracking, and a definition of done reference. The output conforms to the Scrum Guide and IEEE 29148 for requirements traceability.

## When to Use This Skill

- After Phase 02 completes and `prioritized_backlog.md` exists in `projects/<ProjectName>/<phase>/<document>/` with ranked work items.
- When `user_stories.md` is present in `projects/<ProjectName>/<phase>/<document>/` with acceptance criteria for candidate stories.
- When `vision.md` is present in `projects/<ProjectName>/_context/` with project goals to derive sprint goals from.
- At the start of each sprint cycle to produce a fresh planning artifact.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/<phase>/<document>/prioritized_backlog.md`, `projects/<ProjectName>/<phase>/<document>/user_stories.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Sprint_Planning_Template.md` |
| **Standard** | Scrum Guide, IEEE 29148 |
| **Time**    | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `projects/<ProjectName>/_context/vision.md` | Yes | Project goals and strategic objectives for sprint goal derivation |
| prioritized_backlog.md | `projects/<ProjectName>/<phase>/<document>/prioritized_backlog.md` | Yes | Ranked backlog items with priority and estimated effort |
| user_stories.md | `projects/<ProjectName>/<phase>/<document>/user_stories.md` | No | User stories with acceptance criteria for task breakdown |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Sprint_Planning_Template.md | `projects/<ProjectName>/<phase>/<document>/Sprint_Planning_Template.md` | Complete sprint planning template with all ceremony sections |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` from `projects/<ProjectName>/_context/` and `prioritized_backlog.md` from `projects/<ProjectName>/<phase>/<document>/`. Optionally read `user_stories.md` from `projects/<ProjectName>/<phase>/<document>/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Define Sprint Goal Section

Generate a sprint goal template that SHALL:
- Derive the goal from project vision objectives in `vision.md`.
- State the goal as a single sentence describing the increment value.
- Include a "Goal Rationale" field linking the goal to a business objective.
- Provide a "Success Criteria" checklist for goal completion.

### Step 3: Define Team Capacity Section

Generate a capacity calculation template that SHALL:
- List each team member with available days in the sprint.
- Account for planned time off, ceremonies, and non-sprint overhead.
- Calculate total available story points or hours.
- Include a capacity formula: $Capacity = AvailableDays \times FocusFactor \times HoursPerDay$.

### Step 4: Define Selected Backlog Items Section

Generate a backlog selection table that SHALL:
- Pull candidate items from `prioritized_backlog.md` by priority order.
- Include columns for ID, title, priority, estimate, and acceptance criteria reference.
- Track cumulative effort against team capacity.
- Flag items that exceed remaining capacity.

### Step 5: Define Task Breakdown Section

Generate a task breakdown template that SHALL:
- Decompose each selected backlog item into implementation tasks.
- Assign each task an estimated duration in hours.
- Identify task dependencies within and across stories.
- Include columns for task ID, description, assignee, estimate, and status.

### Step 6: Define Sprint Risks and Dependencies Section

Generate a risk and dependency tracking section that SHALL:
- List known risks with probability, impact, and mitigation strategy.
- Identify external dependencies with owner and expected resolution date.
- Include a blocked-items tracker for impediments surfaced during planning.

### Step 7: Assemble and Write Output

Assemble all sections into the final template. Include a Definition of Done reference section that points to `Definition_of_Done.md`. Include a Sprint Commitment section for the team to record their commitment. Write the completed document to `projects/<ProjectName>/<phase>/<document>/Sprint_Planning_Template.md`. Log completion.

## Output Format Specification

The generated `Sprint_Planning_Template.md` SHALL contain these sections in order:

1. **Document Header** -- project name, sprint number, date range, standards reference
2. **Sprint Goal** -- goal statement, rationale, success criteria
3. **Team Capacity** -- member availability, capacity calculation, total capacity
4. **Selected Backlog Items** -- prioritized items table with cumulative effort
5. **Task Breakdown** -- decomposed tasks per backlog item
6. **Sprint Risks & Dependencies** -- risk register and dependency tracker
7. **Definition of Done Reference** -- pointer to DoD artifact
8. **Sprint Commitment** -- team sign-off section

## Common Pitfalls

- Sprint goal stated as a task list instead of a value statement -- the goal SHALL describe the increment value, not the work performed.
- Capacity calculated without accounting for ceremonies and overhead -- the template SHALL deduct non-coding time from available hours.
- Backlog items selected beyond capacity -- the template SHALL flag items that exceed remaining capacity.
- Task breakdown missing dependency identification -- every task SHALL note upstream dependencies.
- No risk tracking -- every sprint plan SHALL include at least a risk placeholder section.

## Verification Checklist

1. `Sprint_Planning_Template.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all eight sections populated.
2. Sprint goal is a single value statement with rationale linked to a business objective.
3. Capacity calculation includes the formula and accounts for non-sprint overhead.
4. Selected backlog items table includes cumulative effort tracking.
5. Task breakdown decomposes each selected item into estimated tasks.
6. Risk and dependency section includes probability, impact, and mitigation fields.
7. Definition of Done reference points to `Definition_of_Done.md`.
8. Sprint commitment section provides a team sign-off area.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 02 (backlog, user stories) | Consumes `prioritized_backlog.md` and `user_stories.md` |
| Downstream | 02-definition-of-done | Sprint plan references the DoD artifact |
| Downstream | Phase 05 (test planning) | Sprint scope informs test plan scope |
| Downstream | Phase 09 (governance) | Sprint artifacts feed governance audit trail |

## Standards Compliance

- **Scrum Guide** -- Governs sprint planning ceremony structure, sprint goal definition, and team commitment.
- **IEEE 29148** -- Governs requirements traceability from backlog items through task decomposition.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step sprint planning generation logic.
- `README.md` -- Quick-start guide for this skill.
