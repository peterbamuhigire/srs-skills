# SaaS Tenancy Decision (ADR Template)

ID: `<ADR-NNNN>` · Service: `<service name>` · Date: `<YYYY-MM-DD>` · Status: `proposed | accepted | superseded`

## Context

Describe the service, the workloads it carries, and the SaaS-level forces in play (tenant count, tier mix, ICP, regulatory constraints, data-residency obligations, blast-radius tolerance, cost target, noisy-neighbor sensitivity, migration constraints).

## Decision

State the chosen tenancy pattern: `Full-Stack Silo | Full-Stack Pool | Mixed-Mode (compute pool, storage silo) | Mixed-Mode (compute silo, storage pool) | Pod (N tenants per stack) | Account-per-Tenant | VPC-per-Tenant`.

State the compute placement and the storage placement explicitly.

## Drivers

Each driver shall include a measurable threshold or constraint:

| Driver | Threshold / Constraint | Source |
|--------|------------------------|--------|
| Regulatory | e.g. PCI-DSS data must not co-mingle | SRS-NFR-SEC-014 |
| Blast-radius | P0 fault MUST affect ≤ 10% of tenants | SRS-NFR-REL-007 |
| Cost target | Gross margin ≥ 75% at 1k tenants | PRD §4.2 |
| Noisy-neighbor | Cross-tenant P95 latency interference ≤ 10 ms | SRS-NFR-PERF-021 |
| Performance | Tier Enterprise must achieve P99 ≤ 200 ms | SRS-NFR-PERF-009 |
| Isolation | Cross-tenant data access MUST be 0 in penetration test | SRS-NFR-SEC-019 |
| Migration | Must support silo → pool migration without downtime | PRD §6.1 |
| Data residency | EU-tenant data MUST stay in EU regions | DPA Art.28 |

## Alternatives considered

1. Pattern X — rejected because ...
2. Pattern Y — rejected because ...

## Consequences

- Positive consequences (efficiency, agility, single deploy).
- Negative consequences accepted (cost-attribution complexity, isolation enforcement burden).
- Operational impact (control-plane responsibilities, runbook items).

## Enforcement / Isolation strategy summary

| Layer | Mechanism | Evidence pointer |
|-------|-----------|------------------|
| Network | e.g. shared VPC, per-tenant security group rules | Evidence Pack §3.1 |
| Compute | e.g. shared K8s namespace, per-tenant quota | Evidence Pack §3.2 |
| Storage | e.g. shared DB cluster, row-level security on tenant_id | Evidence Pack §3.3 |
| IAM | e.g. signed JWT with tenant_id claim, validated at every boundary | Evidence Pack §3.4 |
| Code path | e.g. TenantScopedRepository enforces filter; lint rule blocks raw queries | Evidence Pack §3.5 |

## Per-tier SLOs (if pooled)

| Tier | Availability | P95 Latency | Support Response |
|------|--------------|-------------|------------------|
| Bronze | 99.5% | 800 ms | next business day |
| Silver | 99.9% | 400 ms | 4 hours |
| Gold | 99.95% | 200 ms | 1 hour |
| Enterprise | 99.99% | 150 ms | 15 minutes |

## Per-tenant cost attribution (if pooled)

State the metering events, allocation method, reporting destination.

## Migration path

If a future move (silo→pool, pool→pod, pool→silo) is anticipated, name the trigger threshold and the migration runbook reference.

## Sign-off

| Role | Name | Date |
|------|------|------|
| Lead architect | | |
| Security | | |
| Finance / FinOps | | |
| Product | | |
