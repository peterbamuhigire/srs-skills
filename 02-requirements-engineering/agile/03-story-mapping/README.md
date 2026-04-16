# 03-Story-Mapping Skill

## Objective

This skill converts a flat product backlog into a two-dimensional story map following Jeff Patton's methodology. It identifies backbone user activities from epic groupings, selects a walking skeleton for end-to-end architectural validation, and partitions remaining stories into release slices aligned with IEEE 29148-2018 requirements visualization guidance.

## Execution Steps

1. Ensure `projects/<ProjectName>/<phase>/<document>/user_stories.md` and `projects/<ProjectName>/<phase>/<document>/epic_breakdown.md` exist. Run `01-user-story-generation` first if they are missing.
2. Invoke the skill via `logic.prompt`. The prompt reads both input files, derives backbone activities, defines the walking skeleton, and slices stories into releases.
3. Verify that `projects/<ProjectName>/<phase>/<document>/story_map.md` and `projects/<ProjectName>/<phase>/<document>/story_map.mmd` were generated. Confirm the Mermaid diagram renders without syntax errors.
4. Review the walking skeleton to ensure it covers one complete end-to-end user flow before passing the map downstream to `04-backlog-prioritization`.

## Quality Reminder

Every story in the backlog must appear exactly once in the map; orphan or duplicated stories indicate a mapping defect. The walking skeleton should be the smallest possible set of stories that proves the architecture works end-to-end. Release boundaries must carry explicit rationale so that stakeholders can evaluate scope trade-offs without ambiguity.
