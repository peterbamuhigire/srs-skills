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

Run `01-deployment-guide` first because it establishes the baseline release procedure. Then run `02-runbook` and `03-monitoring-setup` in parallel because they cover distinct operational concerns.

Run `04-infrastructure-docs` after the deployment and observability picture is clear. Run `05-go-live-readiness` last because it consumes evidence from the other operational skills and turns them into an explicit launch recommendation with blockers, conditions, rollback triggers, and hypercare planning.

## Dependencies

- Upstream: Phase 03 (Design Documentation) provides HLD and related design artifacts in the active project workspace.
- Additional upstream context: testing evidence, transition planning, evaluation results, and quality targets strengthen launch readiness decisions.
- Downstream: Phase 08 (End-User Documentation) and Phase 09 (Governance & Compliance) consume operational outputs and evidence.

## Workspace Model

The canonical runtime workspace for this phase is `projects/<ProjectName>/`.

- Context source of truth: `projects/<ProjectName>/_context/`
- Design and test evidence inputs: `projects/<ProjectName>/03-design-documentation/...` and `projects/<ProjectName>/05-testing-documentation/...`
- Generated operational artifacts: `projects/<ProjectName>/06-deployment-operations/...`

Existing skill-local references to `../project_context/` and `../output/` are compatibility aliases into the active project workspace.

Common inputs include `HLD.md`, `Database_Design.md`, `Deployment_Guide.md`, `Runbook.md`, `Monitoring_Setup.md`, `Infrastructure_Docs.md`, `quality_standards.md`, and `solution_evaluation_transition_plan.md`.
