# 02-Business-Case Skill

## Objective

This skill produces a Business Case document that provides decision-makers with the financial justification, risk assessment, and go/no-go criteria needed to approve or reject the project investment. It transforms strategic vision and product requirements into quantitative analysis.

## Execution Steps

1. Verify `../project_context/vision.md` exists. Optionally check for `../output/PRD.md` and `../output/Vision_Statement.md` to enrich the analysis.
2. Invoke `logic.prompt` or trigger the skill. The skill reads context files, generates financial analysis with LaTeX formulas, and writes `../output/Business_Case.md`.
3. Review all financial figures to confirm they are flagged with data sources or marked as `[COST-TBD]`. No fabricated numbers shall appear in the final document.
4. Present the Business Case to stakeholders for go/no-go decision before proceeding to Phase 02.

## Quality Reminder

Flag unknown costs and projections explicitly. Use LaTeX for all financial formulas. The business case shall be a decision document -- every assertion shall be traceable to context files or flagged as an assumption requiring validation.
