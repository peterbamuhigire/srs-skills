# Multi-Tenancy Design

## 5.1 Architecture Pattern: Shared Database, Row-Level Isolation

Longhorn ERP adopts a shared-database multi-tenancy model. All tenants reside in the same MySQL 9.1 database instance. Tenant data isolation is enforced at the application layer through:

1. A `tenant_id` foreign key on every operational table.
2. The middleware pipeline, which populates `TenantContext` from the authenticated session before any page handler or service executes.
3. The convention that every SQL query against an operational table includes a `WHERE tenant_id = ?` clause parameterised from `$this->tenantContext->getTenantId()`.

This approach was selected for operational simplicity and cost efficiency (see ADR-001 in Section 12).

## 5.2 The `tenant_id` Rule

*The `tenant_id` value used in any SQL query shall always be sourced from `$_SESSION['tenant_id']` as provided by the `TenantContext` object. It shall never be sourced from `$_GET`, `$_POST`, `$_COOKIE`, request headers, URL path parameters, or any other client-supplied input.*

Violation of this rule is a Critical severity defect (NFR-SEC-001). The `TenantContext` class is the single authorised accessor.

## 5.3 Cross-Tenant Access Attempts

When a request attempts to retrieve a record that exists but belongs to a different tenant, the system shall return HTTP 404 Not Found rather than HTTP 403 Forbidden. This behaviour prevents tenant enumeration: an attacker cannot distinguish "this record exists but belongs to another tenant" from "this record does not exist."

All such events are logged in the audit trail with a `CROSS_TENANT_ATTEMPT` event type, regardless of whether the attempt was malicious or the result of a misconfigured request.

## 5.4 Module-Level Gating

Every page belonging to an add-on module shall call `requireModuleAccess('MODULE_CODE')` as the first operation in the page handler, after the middleware pipeline completes. If the module is not active for the current tenant, the function redirects the user to the module upgrade/activation page. The check uses `TenantContext::isModuleActive(string $moduleCode)` internally.

Core modules (ACCOUNTING, INVENTORY, SALES, PROCUREMENT, USER\_MGMT, AUDIT) are always active for all tenants and do not require `requireModuleAccess` gating, but the function is idempotent for these codes and will not block access if called.

## 5.5 Tenant Lifecycle States

The tenant lifecycle is a finite state machine with the following states and transitions:

```
Trial ──────────────────────────────────────▶ Active
  │                                              │
  │ (payment not received by trial end)          │ (payment not received by due date)
  ▼                                              ▼
Suspended ◀────────────────────────────── Overdue
  │               (manually by Chwezi)          │
  │                                              │ (paid)
  ▼                                              ▼
Archived                                      Active
```

| State | Login Permitted | Data Access | Billing |
|---|---|---|---|
| `trial` | Yes | Full | No charge |
| `active` | Yes | Full | Charged |
| `overdue` | Blocked (notice shown) | Read-only export only | Overdue |
| `suspended` | Blocked (notice shown) | None | Suspended |
| `archived` | Blocked | None | Closed |

Tenant lifecycle transitions are initiated from the Super Admin Panel and are recorded in the platform audit log.

## 5.6 Per-Tenant Configuration

Each tenant record carries a configuration profile that governs all jurisdiction-specific and business-specific behaviour. The configuration profile includes:

- **Currency:** ISO 4217 currency code (e.g., `UGX`, `KES`, `TZS`).
- **Timezone:** IANA timezone identifier (e.g., `Africa/Kampala`).
- **Chart of Accounts (COA):** The COA starter template applied at tenant provisioning, customisable post-provisioning.
- **Roles and permissions:** Tenant-defined roles built on top of the platform RBAC framework.
- **Branches:** One or more branches with individual location data, contact details, and branch-level configuration.
- **Enabled modules:** The set of module codes active for this tenant under their current subscription plan.
- **Localisation profile:** See Section 10 for the full localisation profile specification.

Configuration is managed via the Tenant Workspace settings area and the Super Admin Panel. Configuration changes take effect on the next page load (no application restart required).

## 5.7 Data Schema Convention

Every operational table in the Longhorn ERP schema follows this convention:

```sql
-- Illustrative table structure (prospective)
CREATE TABLE invoices (
    id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    tenant_id   INT UNSIGNED    NOT NULL,
    branch_id   INT UNSIGNED    NOT NULL,
    -- domain columns ...
    created_at  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by  INT UNSIGNED    NOT NULL,
    PRIMARY KEY (id),
    INDEX idx_tenant (tenant_id),
    CONSTRAINT fk_invoice_tenant FOREIGN KEY (tenant_id) REFERENCES tenants(id)
);
```

The `tenant_id` column is indexed on all operational tables to ensure that tenant-scoped queries execute with a predictable execution plan that does not degrade as the number of tenants grows.
