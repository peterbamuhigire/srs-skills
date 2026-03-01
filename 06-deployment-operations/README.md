# Phase 06: Deployment & Operations

## Purpose

This phase generates deployment and operational documentation that prepares the system for production readiness. It produces deployment procedures, operational runbooks, monitoring configurations, and infrastructure documentation to ensure reliable, repeatable, and observable production operations.

## Sub-Skills

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-deployment-guide | Deployment_Guide.md | IEEE 1062 |
| 2 | 02-runbook | Runbook.md | SRE Best Practices |
| 2 | 03-monitoring-setup | Monitoring_Setup.md | ISO/IEC 25010 |
| 3 | 04-infrastructure-docs | Infrastructure_Docs.md | IEEE 1016-2009 |

## Execution Order

Run 01-deployment-guide FIRST (it establishes the deployment procedure that downstream skills reference). Then run 02-runbook and 03-monitoring-setup in parallel (they address independent operational concerns: incident response and observability). Once those complete, run 04-infrastructure-docs (it synthesizes deployment, runbook, and monitoring context into a unified infrastructure view).

## Dependencies

- **Upstream:** Phase 03 (Design Documentation) -- requires `HLD.md` in `../output/`. Phase 04 (Development Artifacts) -- consumes tech specs for deployment context.
- **Downstream:** Phase 08 (User Documentation) -- consumes operational docs for administrator guides.

## I/O

All skills read from `../output/` (HLD.md, Database_Design.md) and `../project_context/` (tech_stack.md, quality_standards.md). All skills write to `../output/`.
