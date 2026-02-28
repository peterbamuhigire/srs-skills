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

Run vision-statement FIRST (it establishes the formal vision), then PRD (which builds on the vision to define product requirements), then business-case (which justifies the investment using PRD data).

## Dependencies

- **Upstream:** Phase 00 (Meta-Initialization) — requires methodology.md
- **Downstream:** Phase 02 (Requirements Engineering) — consumes Vision_Statement.md and PRD.md

## Input Source

All skills read from `../project_context/` (vision.md, stakeholders.md, features.md, glossary.md).

## Output Destination

All skills write to `../output/`.
