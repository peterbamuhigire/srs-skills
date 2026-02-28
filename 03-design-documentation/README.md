# Phase 03: Design Documentation

## Purpose

This phase generates design documentation that translates verified requirements from Phase 02 into implementable architecture, component specifications, API contracts, and data models. It produces the technical blueprint that development teams use to build the system.

## Sub-Skills

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-high-level-design | HLD.md | IEEE 1016-2009 Sec 5 |
| 2 | 02-low-level-design | LLD.md | IEEE 1016-2009 Sec 6 |
| 3 | 03-api-specification | API_Specification.md, openapi.yaml | OpenAPI 3.0 |
| 3 | 04-database-design | Database_Design.md, erd.mmd | IEEE 1016 Sec 6.7 |

## Execution Order

Run 01-high-level-design FIRST (it establishes the system architecture and component boundaries). Then run 02-low-level-design (which decomposes HLD components into module-level detail). Once LLD is complete, 03-api-specification and 04-database-design can run in parallel since they operate on independent design concerns.

## Dependencies

- **Upstream:** Phase 02 (Requirements Engineering) -- requires `SRS_Draft.md` in `../output/`
- **Downstream:** Phase 04 (Development) -- consumes HLD.md, LLD.md, API_Specification.md, and Database_Design.md. Phase 05 (Testing) -- uses design documents to derive test plans.

## Input Source

All skills read from `../output/SRS_Draft.md` and `../project_context/tech_stack.md`.

## Output Destination

All skills write to `../output/`.
