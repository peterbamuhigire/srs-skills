# Risk Assessment Skill

## Objective

This skill produces a systematic risk assessment that identifies, scores, and mitigates risks across technical, operational, compliance, and project categories using the ISO 31000 framework. The output includes a formal risk register with probability-impact scoring, response strategies, residual risk calculations, and a monitoring plan.

## Execution Steps

1. Populate `projects/<ProjectName>/_context/vision.md` with project objectives, constraints, and stakeholder context
2. Optionally provide `projects/<ProjectName>/_context/quality_standards.md` for risk tolerance thresholds
3. Optionally ensure upstream outputs exist (`SRS_Draft.md`, `HLD.md`, `Audit_Report.md`, `Compliance_Docs.md`)
4. Run this skill
5. Review `projects/<ProjectName>/<phase>/<document>/Risk_Assessment.md` for completeness of risk identification and scoring accuracy
6. Iterate if new risk vectors are identified during review

## Quality Reminder

Every risk SHALL have a specific, measurable description -- not vague statements. Probability and impact scores must be evidence-based and use the defined 1-5 scales consistently. Do not omit residual risk assessment; stakeholders need post-mitigation exposure visibility to make informed decisions.
