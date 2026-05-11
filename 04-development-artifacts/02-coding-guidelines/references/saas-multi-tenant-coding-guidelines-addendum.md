# SaaS Multi-Tenant Coding Guidelines Addendum

Supplements the generic `02-coding-guidelines` skill when the project is a multi-tenant SaaS.

## A. Tenant-context propagation

1. Every inbound request from a tenant-facing service MUST resolve `tenant_id` from the signed context and place it on a request-scoped object (e.g. `RequestContext.tenant_id`).
2. Every outbound call (HTTP, gRPC, async queue) MUST propagate the tenant context (`X-Tenant-Context` header, gRPC metadata, queue-message envelope).
3. Background jobs MUST carry the originating tenant context in their payload; jobs without it MUST be rejected by the worker.

## B. Repository / data-access rules

1. A base `TenantScopedRepository` class wraps every tenant-scoped data access. Direct ORM access bypassing it is forbidden.
2. Every SQL query touching tenant-scoped tables MUST include `WHERE tenant_id = :tenant_id`. Enforce by static-analysis rule that fails CI on missing tenant filter.
3. Use row-level security (RLS) as defence-in-depth where the database supports it.
4. Cross-tenant queries (analytics, batch jobs) MUST be in a separate, audited code path that is explicitly tagged.

## C. Tenant-scoped logging

1. Every log line emitted in the request scope MUST include `tenant_id`.
2. PII MUST NOT appear in logs except in the auth-and-audit subsystem; mask with a deterministic hash elsewhere.
3. Audit logs (cross-tenant access by support, admin impersonation, sensitive actions) go to an immutable append-only store.

## D. Fail-safe on missing context

1. A service receiving a request without a valid tenant context MUST reject with HTTP 401/403 (or gRPC `UNAUTHENTICATED`).
2. The rejection MUST emit an audit-log entry.
3. No fall-back to a "default" tenant exists in code.

## E. Cache keys

1. Every cache key MUST be prefixed with `tenant_id`.
2. A bug that leaks cache between tenants is a SEV1.
3. Time-windowed cache MUST be tenant-partitioned.

## F. Feature flags & tier gates

1. Gate decisions evaluated server-side from `tenant.tier`, never client-side.
2. A flag default MUST be the safest tier (typically "off"); promotion to higher tiers is explicit.

## G. Testing

1. Negative-path test: request without tenant ctx → expect 401/403.
2. Tampered-context test: forged `tenant_id` claim → expect 401/403.
3. Cross-tenant fuzz test: tenant A's session attempts tenant B operations → expect denial + audit entry.
4. CI fails any PR that adds a query without a tenant-scoped repository path.

## H. Anti-patterns to reject in code review

- Hard-coded `tenant_id`.
- `WHERE tenant_id = ?` not present on tenant-scoped query.
- Client-side feature gate.
- Logging without `tenant_id`.
- Cache key without `tenant_id` prefix.
- Migration that adds a tenant-scoped table without `tenant_id` column.
- Background job pulled from a queue that does not carry tenant context.
- "TODO: scope this query" merged to main.

## I. References

- Multi_Tenancy_Architecture_Spec.md
- SaaS NFR Catalog (Phase 02 ref)
- Golding (2024) Ch.8 (SaaS microservices)
