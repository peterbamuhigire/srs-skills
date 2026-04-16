# Audit Report Skill

## Objective

This skill produces a formal Verification and Validation audit report that assesses all project documentation against IEEE 1012-2016 criteria for correctness, completeness, consistency, and traceability. The report categorizes findings by severity and concludes with a Pass, Conditional Pass, or Fail recommendation.

## Execution Steps

1. Ensure `projects/<ProjectName>/<phase>/<document>/Traceability_Matrix.md` exists (run 01-traceability-matrix first)
2. Ensure `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` exists with finalized requirements
3. Optionally provide `projects/<ProjectName>/_context/quality_standards.md` for quality benchmarks
4. Run this skill
5. Review `projects/<ProjectName>/<phase>/<document>/Audit_Report.md` for findings and recommendation
6. Remediate any `[V&V-FAIL]` tagged findings before proceeding

## Quality Reminder

Every finding SHALL include specific evidence referencing the exact document section, not vague assertions. Severity levels must be applied consistently -- do not inflate cosmetic issues to Critical. The audit must conclude with a formal recommendation; omitting it renders the report incomplete.
