# Phase 03: Design Documentation

## Purpose

This phase generates design documentation that translates verified requirements into implementable system blueprints. It now covers core software architecture plus UX, infrastructure, and IoT-specific design so the engine can support both conventional systems and connected products.

## Sub-Skills

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-high-level-design | HLD.md | IEEE 1016-2009 Sec 5 |
| 2 | 02-low-level-design | LLD.md | IEEE 1016-2009 Sec 6 |
| 3 | 03-api-specification | API_Specification.md, openapi.yaml | OpenAPI 3.0 |
| 3 | 04-database-design | Database_Design.md, erd.mmd | IEEE 1016 Sec 6.7 |
| 3 | 05-ux-specification | UX_Specification.md | UX and interaction design practices |
| 4 | 06-infrastructure-design | Infrastructure_Design.md | IEEE 1016, ISO/IEC 25010 |
| 4 | 07-iot-system-design | IoT_System_Design.md | IEEE 1016, IoT architecture practices |

## Execution Order

Run `01-high-level-design` first because it establishes the architecture and system boundaries. Run `02-low-level-design` after that to decompose the architecture into modules and interfaces.

Once the architectural baseline exists:

- `03-api-specification`, `04-database-design`, and `05-ux-specification` can proceed in parallel when their inputs are ready.
- `06-infrastructure-design` should run when performance, availability, and deployment architecture need explicit treatment.
- `07-iot-system-design` should run for connected-device products after HLD exists and the requirements clearly describe device, edge, gateway, or fleet behavior.

## Dependencies

- **Upstream:** Phase 02 (Requirements Engineering) requires `SRS_Draft.md` in `../output/`.
- **Additional upstream context:** business process models, rule catalogs, and discovery outputs improve the quality of design decisions when available.
- **Downstream:** Phase 04 (Development) consumes HLD, LLD, API, database, UX, infrastructure, and IoT design outputs as applicable. Phase 05 (Testing) uses these artifacts to derive test strategy and detailed test assets. Phase 06 (Deployment & Operations) consumes infrastructure and IoT operational assumptions.

## Input Source

All skills read from `../output/` and `../project_context/`, with `SRS_Draft.md` and `tech_stack.md` as the common baseline inputs.

Additional high-value inputs include:

- `business_process_models.md`
- `business_rules_catalog.md`
- `solution_discovery_report.md`
- `quality_standards.md`

## Output Destination

All skills write to `../output/`.
