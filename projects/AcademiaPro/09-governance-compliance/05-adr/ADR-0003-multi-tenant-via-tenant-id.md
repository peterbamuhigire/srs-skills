# ADR-0003 Multi-tenancy via tenant_id + Eloquent TenantScope

- Status: accepted
- Date: 2026-04-17

## Context

Three tenancy models were considered: database-per-tenant, schema-per-tenant, shared-schema-with-tenant_id. Ugandan Tier-2 schools pay USD 3–15 per month; database-per-tenant would break unit economics (NFR-COST-001). Schema-per-tenant on MySQL lacks tooling; migration-at-scale is a liability.

## Decision

Shared schema. Every tenant-scoped table carries a non-null `tenant_id` column with a foreign key to `tenants.id`. Enforcement is dual-layer:

1. Eloquent global scope `TenantScope` applied to every tenant-scoped model. Injects `WHERE tenant_id = :current_tenant` on every query.
2. Repository-layer check. Repositories assert the caller's tenant matches the row's tenant before returning; throws `TenantLeakException` on mismatch.

## Consequences

- Positive: single database, single migration path, cheapest ops; unit economics target met.
- Negative: one bug in `TenantScope` leaks data across schools. Mitigation: mandatory repository layer (second defence); integration tests enforce cross-tenant query returns empty across every resource endpoint.
- Security: this decision is the highest-risk control in the system. ISO 27001 A.9 applies directly.

## Affects

- Every FR that touches tenant-scoped data (approximately 85 of 98 FRs).
- CTRL-ISO-A9, CTRL-UG-002.
- `03-design-documentation/04-database-design/01-erd.md` (`tenant_id` column mandatory on every tenant-scoped table).
- `05-testing-documentation/` — dedicated tenant-isolation test suite required.
