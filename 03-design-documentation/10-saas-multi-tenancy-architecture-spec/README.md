# 10-SaaS-Multi-Tenancy-Architecture-Spec Skill

## Objective

Produce the Multi-Tenancy Architecture Specification — the SaaS-distinctive Phase 03 artefact. Augments the generic HLD with two-plane decomposition, per-microservice tenancy-pattern matrix, tenant-context spec, isolation strategy, noisy-neighbor controls, per-tenant cost attribution, and ADR seeds. Sourced from Tod Golding, *Building Multi-Tenant SaaS Architectures* (O'Reilly, 2024).

## Execution Steps

1. Verify `SRS_Draft.md`, `HLD.md`, `tech_stack.md` exist in the project workspace.
2. Invoke `logic.prompt`. The skill reads inputs, fills the tenancy matrix, writes the spec, and emits ADR seeds.
3. Review the per-microservice matrix with the architect — every row must cite drivers with measurable thresholds.
4. Promote ADR seeds to the formal ADR register via `09-governance-compliance/05-architecture-decision-records`.

## Quality Reminder

Every microservice appears in the matrix. Every pooled service has noisy-neighbor controls, per-tier SLOs, and a per-tenant cost-attribution method. Every tenant-touching service has a fail-safe behaviour when context is missing. Isolation is *shown* (evidence path), not asserted.

## Standards

- IEEE 1016-2009 Sec 5
- ISO/IEC 25010
- AWS Well-Architected SaaS Lens
- Golding (2024) silo / pool / mixed / pod taxonomy
