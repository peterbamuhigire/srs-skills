# Phase 06: Deployment & Operations

## Purpose

This phase generates deployment and operational documentation that prepares the system for real production use. It covers deployment procedures, runbooks, observability, infrastructure documentation, and explicit go-live readiness so the engine can support launch decisions rather than stopping at technical setup.

## Sub-Skills

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-deployment-guide | Deployment_Guide.md | IEEE 1062 |
| 2 | 02-runbook | Runbook.md | SRE best practices |
| 2 | 03-monitoring-setup | Monitoring_Setup.md | ISO/IEC 25010 |
| 3 | 04-infrastructure-docs | Infrastructure_Docs.md | IEEE 1016-2009 |
| 4 | 05-go-live-readiness | Go_Live_Readiness.md | Production readiness and transition governance practices |

## Execution Order

Run `01-deployment-guide` first because it establishes the baseline release procedure. Then run `02-runbook` and `03-monitoring-setup` in parallel, since they cover distinct operational concerns.

Run `04-infrastructure-docs` after the deployment and observability picture is clear. Run `05-go-live-readiness` last, because it consumes evidence from the other operational skills and turns them into an explicit launch recommendation with blockers, conditions, rollback triggers, and hypercare planning.

## Dependencies

- **Upstream:** Phase 03 (Design Documentation) requires `HLD.md` and other design artifacts in `../output/`.
- **Additional upstream context:** transition planning, evaluation results, and quality targets strengthen launch readiness decisions when present.
- **Downstream:** Phase 08 (User Documentation) consumes operational outputs for administrator and support guidance. Release governance and product stakeholders consume the go-live readiness report directly.

## I/O

All skills read from `../output/` and `../project_context/`. Common inputs include:

- `HLD.md`
- `Database_Design.md`
- `Deployment_Guide.md`
- `Runbook.md`
- `Monitoring_Setup.md`
- `Infrastructure_Docs.md`
- `quality_standards.md`
- `solution_evaluation_transition_plan.md`

All skills write to `../output/`.
