# 09-Use-Case-Modeling Skill

## Objective

This skill transforms SRS Section 3.2 functional requirements into a complete UML use case model. It produces actor catalogs, use case diagrams, fully-dressed use case descriptions with stimulus-response scenarios, and activity diagrams for complex multi-actor workflows. The output conforms to UML 2.5.1 and IEEE 29148-2018.

## When to Use

Run this skill after `05-feature-decomposition` has generated Section 3.2 in `SRS_Draft.md`. Use it when the project requires a behavioral view of system interactions that goes beyond individual stimulus-response pairs -- particularly for systems with multiple actor types, complex decision logic, or parallel workflows.

## Inputs

| File | Required | Source |
|------|----------|--------|
| `SRS_Draft.md` (Sections 3.1-3.2) | Yes | `projects/<ProjectName>/<phase>/<document>/` |
| `features.md` | Yes | `projects/<ProjectName>/_context/` |
| `business_rules.md` | Recommended | `projects/<ProjectName>/_context/` |
| `stakeholder_register.md` | Optional | `projects/<ProjectName>/_context/` |

## Output

| File | Location |
|------|----------|
| `Use_Case_Model.md` | `projects/<ProjectName>/<phase>/<document>/Use_Case_Model.md` |

## Execution Steps

1. Verify `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` contains Sections 3.1 and 3.2 and that `projects/<ProjectName>/_context/features.md` exists. Halt if either is missing.
2. Invoke the skill through your runner. The skill reads context files, identifies actors, extracts use cases, generates diagrams and descriptions, and writes `projects/<ProjectName>/<phase>/<document>/Use_Case_Model.md`.
3. Review the generated model to confirm: every actor is classified (Primary, Supporting, Offstage); every use case has a fully-dressed description with stimulus-response steps; activity diagrams cover complex workflows; the traceability matrix maps all Section 3.2 requirements.
4. Resolve any `[TRACE-FAIL]` or `[V&V-FAIL]` tags before proceeding to `06-logic-modeling`.

## Integration with Waterfall Pipeline

This skill occupies Phase 09 in the waterfall pipeline. It depends on the output of Phase 05 (Feature Decomposition) and feeds into Phase 06 (Logic Modeling) and Phase 08 (Semantic Auditing). The traceability matrix produced by this skill provides auditable links between functional requirements and behavioral models.

## Quality Reminder

Every use case step shall use active voice ("The system shall..."). Do not embed UI-specific details in use case flows. If a business rule or data requirement is unavailable in the context files, flag it with the appropriate `[TBD]` marker rather than fabricating content.
