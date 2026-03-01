# Traceability Matrix Skill

## Objective

This skill produces a bidirectional Requirements Traceability Matrix (RTM) that maps every requirement to its originating business goal, design artifact, test case, and implementation status. The RTM is the foundational governance artifact required for audit readiness and IEEE 1012-2016 compliance.

## Execution Steps

1. Populate `../project_context/` with `vision.md` containing business goals and stakeholder needs
2. Ensure `../output/SRS_Draft.md` exists with uniquely identified requirements
3. Optionally provide `../output/HLD.md`, `../output/LLD.md`, and `../output/user_stories.md` for richer traceability
4. Run this skill
5. Review `../output/Traceability_Matrix.md` for completeness and accuracy
6. Resolve any `[V&V-FAIL]` tagged requirements before proceeding to 02-audit-report

## Quality Reminder

Every requirement SHALL have a unique identifier and at least one upstream link (to a business goal) and one downstream link (to a test case). Orphan detection is mandatory -- do not skip it. Coverage metrics must use correct denominators reflecting the total requirement count, not just the linked subset.
