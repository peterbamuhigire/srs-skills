---
name: retrospective-template
description: Generate a sprint retrospective template with multiple facilitation formats, action item tracking, and continuous improvement metrics per the Scrum Guide.
---

# Retrospective Template Skill

## Overview

This skill produces a reusable sprint retrospective template that structures the retrospective ceremony. It provides multiple facilitation formats (Start-Stop-Continue, 4Ls, Sailboat), action item tracking with ownership and deadlines, and continuous improvement metrics to ensure retrospectives drive measurable process improvement. The output conforms to the Scrum Guide.

## When to Use This Skill

- When establishing or refreshing the team's retrospective ceremony structure.
- After `vision.md` is present in `../project_context/` for project context.
- At the end of each sprint to generate a fresh retrospective artifact.
- When the team wants to rotate facilitation formats to prevent ceremony fatigue.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../project_context/vision.md` |
| **Output**  | `../output/Retrospective_Template.md` |
| **Standard** | Scrum Guide |
| **Time**    | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `../project_context/vision.md` | Yes | Project goals and context for grounding retrospective themes |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Retrospective_Template.md | `../output/Retrospective_Template.md` | Complete retrospective template with facilitation formats, action tracking, and metrics |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` from `../project_context/`. Log the absolute path of each file read. Halt if the required file is missing.

### Step 2: Define Sprint Summary Section

Generate a sprint summary template that SHALL:
- Record the sprint number, date range, and sprint goal.
- Record team members who participated.
- Summarize sprint outcome (goal met, partially met, not met).
- Note velocity and any significant sprint events.

### Step 3: Define What Went Well Section

Generate a "What Went Well" section that SHALL:
- Provide a structured space for team members to record positive observations.
- Categorize observations by theme (process, collaboration, technical, delivery).
- Include a voting mechanism to identify top positive themes.
- Encourage specific examples rather than general statements.

### Step 4: Define What Could Be Improved Section

Generate a "What Could Be Improved" section that SHALL:
- Provide a structured space for team members to record improvement areas.
- Categorize observations by theme (process, collaboration, technical, delivery).
- Include a voting mechanism to prioritize improvement areas.
- Require specific, observable descriptions rather than blame-oriented statements.

### Step 5: Define Action Items Section

Generate an action item tracking section that SHALL:
- Capture each action item with a unique identifier.
- Assign an owner responsible for follow-through.
- Set a target completion date (typically before the next retrospective).
- Define a measurable success criterion for each action.
- Track status (open, in progress, completed, deferred).

### Step 6: Define Facilitation Formats

Generate three alternative facilitation formats the team can rotate through:

**Start-Stop-Continue:** Three columns for new practices to start, current practices to stop, and effective practices to continue. Each column SHALL require specific, actionable entries.

**4Ls (Liked, Learned, Lacked, Longed For):** Four quadrants capturing what the team liked, what they learned, what was lacking, and what they longed for. Each quadrant SHALL link observations to potential actions.

**Sailboat:** Visual metaphor with wind (helping forces), anchors (hindering forces), rocks (risks ahead), and island (sprint goal). Each element SHALL map to a concrete team experience from the sprint.

### Step 7: Define Improvement Metrics and Write Output

Generate a continuous improvement metrics section that SHALL:
- Track action item completion rate across sprints.
- Track recurring themes to identify systemic issues.
- Measure team satisfaction or morale trend (optional anonymous survey).
- Include a follow-up tracking table for previous sprint action items.
Assemble all sections into the final template. Write to `../output/Retrospective_Template.md`. Log completion.

## Output Format Specification

The generated `Retrospective_Template.md` SHALL contain these sections in order:

1. **Document Header** -- project name, sprint number, date, standards reference
2. **Sprint Summary** -- sprint goal, outcome, participants, velocity
3. **What Went Well** -- categorized positive observations with voting
4. **What Could Be Improved** -- categorized improvement areas with voting
5. **Action Items** -- tracked items with owner, deadline, success criteria, status
6. **Facilitation Formats** -- Start-Stop-Continue, 4Ls, Sailboat templates
7. **Improvement Metrics** -- action completion rate, recurring themes, satisfaction trend
8. **Follow-Up Tracking** -- status of previous sprint action items

## Common Pitfalls

- Action items without owners or deadlines -- every action SHALL have an assigned owner and target date.
- Improvement areas stated as blame -- observations SHALL focus on process and outcomes, not individuals.
- No follow-up on previous actions -- the template SHALL include a section to review prior sprint actions.
- Single facilitation format causing ceremony fatigue -- the template SHALL provide at least three rotation options.
- Metrics not tracked across sprints -- the template SHALL include fields for cross-sprint trend tracking.

## Verification Checklist

1. `Retrospective_Template.md` exists in `../output/` with all eight sections populated.
2. Sprint summary captures goal, outcome, participants, and velocity.
3. "What Went Well" and "What Could Be Improved" sections include categorization and voting.
4. Every action item has an owner, deadline, and measurable success criterion.
5. At least three facilitation formats are documented with instructions.
6. Improvement metrics section tracks action completion rate and recurring themes.
7. Follow-up tracking section references previous sprint action items.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Project context (vision.md) | Consumes project goals for retrospective context |
| Lateral | 01-sprint-planning | Retrospective actions may inform next sprint planning |
| Lateral | 02-definition-of-done | Retrospective may refine DoD criteria |
| Downstream | Phase 09 (governance) | Retrospective metrics feed governance reporting |

## Standards Compliance

- **Scrum Guide** -- Governs the Sprint Retrospective as a ceremony for inspecting and adapting the team's process.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step retrospective template generation logic.
- `README.md` -- Quick-start guide for this skill.
