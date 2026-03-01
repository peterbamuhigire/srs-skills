# Phase 04: Development Artifacts

## Purpose

This phase generates development-facing documentation that guides implementation teams from design specifications to working code. It bridges the gap between Phase 03 design documents and Phase 05 testing by producing technical specifications, coding standards, environment setup instructions, and contribution workflows.

## Sub-Skills

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-technical-specification | Technical_Specification.md | IEEE 1016-2009, IEEE 830-1998 |
| 2 | 02-coding-guidelines | Coding_Guidelines.md | IEEE 730 |
| 2 | 03-dev-environment-setup | Dev_Environment_Setup.md | IEEE 1074 |
| 3 | 04-contribution-guide | Contribution_Guide.md | IEEE 1074 |

## Execution Order

Run 01-technical-specification FIRST (it translates LLD module contracts into implementation-ready specifications). Then run 02-coding-guidelines and 03-dev-environment-setup in parallel (they operate on independent concerns: code standards and environment configuration). Once those complete, run 04-contribution-guide (it references both coding standards and environment setup).

## Dependencies

- **Upstream:** Phase 03 (Design Documentation) -- requires `LLD.md` and `HLD.md` in `../output/`
- **Downstream:** Phase 05 (Testing) -- consumes Technical_Specification.md for test derivation. Development teams consume all four artifacts during implementation.

## Input Source

All skills read from `../output/` (LLD.md, HLD.md, SRS_Draft.md) and `../project_context/tech_stack.md`.

## Output Destination

All skills write to `../output/`.
