# Compliance Documentation Skill

## Objective

This skill produces regulatory compliance documentation that maps project requirements and architecture to applicable frameworks including GDPR, HIPAA, and SOC2. It performs an applicability assessment, data classification, controls mapping, and gap analysis to establish the project's compliance posture.

## Execution Steps

1. Populate `../project_context/vision.md` with project domain, data subjects, and geographic scope
2. Optionally provide `../project_context/quality_standards.md` with security requirements
3. Optionally ensure `../output/SRS_Draft.md` and `../output/HLD.md` exist for richer controls mapping
4. Run this skill
5. Review `../output/Compliance_Docs.md` for applicability determinations and gap analysis
6. Resolve any `[ASSESSMENT-PENDING]` items by providing additional project context

## Quality Reminder

Compliance documentation SHALL be grounded in actual project artifacts, not boilerplate templates. Every compliance claim must reference a specific control or requirement. When evidence is insufficient, tag the item as `[ASSESSMENT-PENDING]` rather than asserting compliance without basis.
