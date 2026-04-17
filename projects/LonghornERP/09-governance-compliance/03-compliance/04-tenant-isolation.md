# Tenant Data Isolation Controls

## 4.1 Isolation Model

Longhorn ERP uses row-level tenant isolation implemented via a `tenant_id` foreign key column on every operational table. This model places all tenants in a shared database schema. The security guarantee provided by this model depends entirely on the correctness of `tenant_id` filtering in every query. This section specifies the controls that enforce that guarantee.

**NFR-SEC-001** (sourced from `_context/domain.md`) states: *The system shall ensure that no query, API response, or report returns data belonging to a tenant other than the authenticated tenant. Violation of this requirement is a Critical severity defect.*

## 4.2 Tenant Identity Resolution

### 4.2.1 Source of Truth

The `tenant_id` value used by any service method shall be sourced exclusively from `TenantContext::getTenantId()`. This method reads `tenant_id` from the current server-side session (web) or from the verified `tid` claim of the validated JWT (mobile).

The system shall never read `tenant_id` from:

- URI path segments (e.g., `/api/tenant/42/invoices`).
- Query parameters (e.g., `?tenant_id=42`).
- POST or PUT request body fields.
- HTTP headers supplied by the client.
- Cookie values other than the session identifier that points to server-side storage.

### 4.2.2 Service Layer Enforcement

Every service class method that performs a database read or write shall receive `$tenantId` as its first parameter, sourced from `TenantContext::getTenantId()` at the controller layer. The `$tenantId` parameter shall appear as the first condition in the WHERE clause of every SQL query within that method. No service method shall accept a `$tenantId` parameter supplied by the caller's request input.

Example of the required pattern:

```php
public function getInvoices(int $tenantId, array $filters): array
{
    $sql = 'SELECT * FROM invoices WHERE tenant_id = ? AND ...';
    // $tenantId resolved by TenantContext, not from $request
}
```

### 4.2.3 Query Construction

All database queries shall use PHP Data Objects (PDO) prepared statements. The `tenant_id` binding shall be the first bound parameter in all multi-tenant queries. No query shall construct the `tenant_id` filter by string concatenation.

## 4.3 Cross-Tenant Access Response

When a request resolves to a resource that exists in the database but belongs to a different tenant than the authenticated tenant, the system shall return HTTP 404. The system shall not return HTTP 403 in this scenario. Returning HTTP 403 would confirm the existence of the resource to the requesting tenant, enabling tenant enumeration. HTTP 404 prevents an attacker from distinguishing between "resource does not exist" and "resource exists but belongs to another tenant."

## 4.4 Stored Procedures and Views

All stored procedures and SQL views that access multi-tenant tables shall include `tenant_id` as a parameter or filter condition. No stored procedure shall return a result set that spans multiple tenants. Views used for reporting shall be parameterised or filtered by `tenant_id` at query time; no view shall pre-aggregate data across tenant boundaries.

## 4.5 Background Jobs and Scheduled Tasks

Batch processing jobs (e.g., period-end GL postings, payroll runs, depreciation calculations) shall be scoped to a single `tenant_id` per execution. No background job shall process records from multiple tenants in a single database transaction. Job dispatch shall include `$tenantId` as an explicit, system-resolved parameter — never inferred from the job queue payload supplied by an external caller.

## 4.6 Independent Security Review Requirement

*[CONTEXT-GAP: GAP-004] — An independent second-developer security review of the `tenant_id` enforcement implementation is required before any tenant is onboarded to the production system. Formal written sign-off is required. This review shall verify that every service method, stored procedure, view, and background job satisfies the controls specified in this section. Production deployment shall be blocked until this review is completed and documented.*

The review artefact shall be stored in `09-governance-compliance/02-audit-report/` and referenced in the pre-launch compliance checklist (Section 10).
