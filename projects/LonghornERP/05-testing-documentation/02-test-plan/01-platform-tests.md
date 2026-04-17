# Platform and Cross-Cutting Concern Test Cases

This section covers tenant isolation, Role-Based Access Control (RBAC), audit log integrity, and session/JWT validation. All tests in this section are classified as critical — no module-level test suite may pass the integration gate if any test in this section fails.

## Tenant Isolation

Tenant isolation is enforced via row-level filtering on `tenant_id`, sourced exclusively from the authenticated session or JWT claim. No test case in this document permits `tenant_id` to be supplied as a request input parameter.

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-PLAT-001 | `TenantIsolationTest` | `test_cross_tenant_invoice_read_returns_404` | Request with Tenant A session reads Tenant B invoice by ID | Tenant A session cookie; Tenant B `invoice_id` | HTTP 404 — record not found in Tenant A scope |
| TC-PLAT-002 | `TenantIsolationTest` | `test_cross_tenant_jwt_on_mobile_endpoint_returns_401` | JWT issued for Tenant A presented to Tenant B mobile endpoint | Tenant A JWT; Tenant B endpoint URL | HTTP 401 — tenant mismatch |
| TC-PLAT-003 | `StaticAnalysisTest` | `test_no_unscoped_tenant_queries_exist` | Static code scan: no SQL query on `invoices` (or any tenant-scoped table) omits `WHERE tenant_id = ?` | Codebase scan of `src/` and `app/` | 0 unscoped query occurrences; test fails on first match |

## RBAC and Permission Enforcement

Permissions are enforced by the `RequirePermission` middleware. Tests assert that the middleware fires before any controller logic executes.

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-PLAT-004 | `RbacMiddlewareTest` | `test_missing_invoices_create_permission_returns_403` | User without `invoices.create` permission POSTs to `/api/invoices` | Valid session lacking `invoices.create`; valid invoice payload | HTTP 403 — permission denied before controller executes |
| TC-PLAT-005 | `RbacMiddlewareTest` | `test_invoices_view_permission_allows_get` | User with `invoices.view` GETs invoice list | Valid session with `invoices.view` | HTTP 200; response body contains invoice array |
| TC-PLAT-006 | `RbacMiddlewareTest` | `test_branch_restricted_user_cannot_access_other_branch_records` | User restricted to Branch A requests records belonging to Branch B | Branch A session; Branch B `branch_id` filter | HTTP 403 — branch scope violation |

## Audit Log Integrity

The `audit_log` table is INSERT-only. Every state-changing action must produce exactly 1 audit row. Tests verify both the row count and the row's content fields.

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-PLAT-007 | `AuditLogTest` | `test_create_invoice_writes_audit_row` | Create an invoice via API | Valid invoice payload with authenticated session | `audit_log` gains exactly 1 row; `action` = `CREATE`; `entity` = `invoice`; `entity_id` matches new invoice ID |
| TC-PLAT-008 | `AuditLogTest` | `test_approve_payroll_run_writes_audit_row_with_state` | Approve a payroll run | Valid payroll run ID; approver session with `payroll.approve` | `audit_log` gains exactly 1 row; `before_state` JSON contains previous status; `after_state` JSON contains `APPROVED` |
| TC-PLAT-009 | `AuditLogTest` | `test_update_audit_log_row_is_rejected_by_db` | Attempt to UPDATE an existing `audit_log` row directly | Raw SQL: `UPDATE audit_log SET action = 'TAMPERED' WHERE id = 1` | DB exception thrown; row unchanged; INSERT-only constraint enforced at database level |

## Session and JWT Validation

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-PLAT-010 | `AuthTokenTest` | `test_expired_jwt_returns_401_with_token_expired_code` | Expired JWT presented to any authenticated endpoint | JWT with `exp` set to a past timestamp | HTTP 401; response body `error_code` = `TOKEN_EXPIRED` |
| TC-PLAT-011 | `AuthTokenTest` | `test_tampered_jwt_signature_returns_401_with_token_invalid_code` | JWT with signature modified after issuance | Valid JWT payload; invalid signature segment | HTTP 401; response body `error_code` = `TOKEN_INVALID` |
| TC-PLAT-012 | `AuthTokenTest` | `test_refresh_token_rotation_rejects_reused_token` | Refresh token used once, then re-used | First use returns new access + refresh tokens; second use of original refresh token | Second use → HTTP 401; original refresh token status = `REVOKED` in token store |
