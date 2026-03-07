# 04-Lean-Canvas Skill

## Objective

This skill generates a Lean Canvas, Impact Map, and Hypothesis Board for MVP, startup, or exploratory projects. It serves as a lightweight alternative to the full PRD (`01-prd-generation`) when requirements are uncertain and the team needs rapid strategic alignment before committing to detailed specification.

## Decision Gate

Before executing this skill, score the project against five criteria (MVP status, requirement uncertainty, team size, timeline, budget). A score of 5 or higher indicates the Lean Canvas is appropriate. A score below 5 redirects to the full PRD skill. See `SKILL.md` for the complete scoring table.

## When to Use

- The project is an MVP or first version with no existing production release.
- Requirements are expected to evolve significantly during development.
- The team is small (<10 people) and needs a one-page strategic view.
- Time-to-market is aggressive (<3 months) and a full PRD would delay execution.

## When to Use Full PRD Instead

- The project has established requirements and a stable scope.
- Regulatory or contractual obligations require detailed requirements documentation.
- The team is large (>10 people) and needs a comprehensive coordination artifact.

## Inputs

| File | Required | Source |
|------|----------|--------|
| `vision.md` | Yes | `../project_context/` |
| `features.md` | Recommended | `../project_context/` |
| `stakeholders.md` | Optional | `../project_context/` |

## Output

| File | Location |
|------|----------|
| `Lean_Canvas.md` | `../output/Lean_Canvas.md` |

## Execution Steps

1. Verify `../project_context/vision.md` exists. Halt if missing.
2. Run the decision gate scoring. If score < 5, redirect to `01-prd-generation`.
3. Invoke the skill through your runner. The skill reads context files, populates all nine canvas blocks, generates the Impact Map and Hypothesis Board, and writes `../output/Lean_Canvas.md`.
4. Review the generated document to confirm: Problem block has no solution-bias language; Key Metrics use AARRR framework; Impact Map goal is SMART; hypotheses are ordered by risk.
5. Proceed to `02-business-case` or directly to requirements engineering as appropriate.

## Quality Reminder

Every canvas block shall be grounded in the project context files. Flag unknown values with `[TYPE-TBD]` markers rather than fabricating data. The Lean Canvas is a living document -- define iteration triggers so the team knows when to update it.
