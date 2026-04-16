# Phase 01: Strategic Vision

## Purpose

This phase generates the strategic foundation documents that define project direction before detailed requirements engineering begins. It produces the business justification, product vision, and requirements overview.

## Sub-Skills

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 03-vision-statement | Vision_Statement.md | IEEE 29148 Sec 6.2 |
| 2 | 01-prd-generation | PRD.md | IEEE 29148, IEEE 1233 |
| 3 | 02-business-case | Business_Case.md | IEEE 1058 |

## Execution Order

Run vision-statement first because it establishes the formal product and stakeholder direction. Run PRD next to convert that direction into scoped capabilities and quality expectations. Run business-case last so investment logic uses the current vision and PRD assumptions.

## Dependencies

- Upstream: Phase 00 (Meta-Initialization) establishes methodology and workspace targeting.
- Downstream: Phase 02 (Requirements Engineering) consumes the strategic outputs to derive formal requirements or Agile stories.

## Workspace Model

The canonical runtime workspace for this phase is `projects/<ProjectName>/`.

- Context source of truth: `projects/<ProjectName>/_context/`
- Generated artifacts: `projects/<ProjectName>/01-strategic-vision/...`

<!-- alias-block start -->
Existing skill-local references to `../project_context/` and `../output/` are compatibility aliases into the active project workspace, not a second architecture.
<!-- alias-block end -->
