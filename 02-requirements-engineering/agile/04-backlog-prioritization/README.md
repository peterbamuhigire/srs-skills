# 04-Backlog-Prioritization Skill

## Objective

This skill applies MoSCoW classification and Weighted Shortest Job First (WSJF) scoring to an existing user story backlog, producing a ranked backlog and a sprint-allocated release plan. It ensures that prioritization decisions are traceable to business goals defined in `vision.md` and that dependency ordering prevents sprint-level blocking conflicts.

## Execution Steps

1. Read `../output/user_stories.md`, `../project_context/vision.md`, and optionally `../output/story_map.md`. Log all paths.
2. Classify stories by MoSCoW category and score each on four WSJF factors (BV, TC, RR, JS) using a 1-10 scale aligned to business goals.
3. Calculate WSJF = (BV + TC + RR) / JS, sort within MoSCoW tiers, and allocate to sprints at 20 points/sprint default velocity.
4. Write `../output/prioritized_backlog.md` and `../output/release_plan.md` with scoring tables, sprint allocations, and dependency notes.

## Quality Reminder

Every WSJF score must be computed from explicitly documented factor values; do not assign scores without stating the rationale tied to `vision.md` goals. Verify dependency ordering after allocation to ensure no story is scheduled before its prerequisites, and flag any circular dependencies immediately rather than silently reordering.
