# Audit Log Security Requirements

## 5.1 Purpose

The audit log is the authoritative record of all state-changing activity within Longhorn ERP. It serves three functions: regulatory compliance (Uganda Companies Act 7-year retention requirement), security forensics (breach investigation, privilege abuse detection), and tenant accountability (tenant administrators reviewing activity on their own data). The audit log is a security control, not a reporting convenience.

**NFR-SEC-002** (sourced from `_context/domain.md`) states: *The system shall ensure that no audit log record can be updated or deleted by any user, including super administrators. The audit log table shall be INSERT-only.*

## 5.2 Immutability Enforcement

### 5.2.1 Database Privilege Control

The application database user shall hold INSERT privilege only on the `audit_log` table. UPDATE and DELETE privileges on `audit_log` shall not be granted to the application database user, the super admin database user, or any application-layer role. This restriction shall be enforced by the database server's privilege system, not solely by application logic.

### 5.2.2 No Soft Delete

The `audit_log` table shall not contain a `deleted_at` column, an `is_deleted` flag, or any mechanism that marks records as inactive. Every row written to `audit_log` remains permanently readable.

### 5.2.3 No Bulk Export and Delete Workflow

The system shall not provide any interface — administrative, API-based, or scripted — that exports audit log data and then deletes the source records. Archival of audit log data shall duplicate records to an archive store; it shall not remove records from the live `audit_log` table within the 7-year retention window.

### 5.2.4 Verification

Audit log immutability shall be verified by penetration test before production launch. The penetration test shall attempt UPDATE and DELETE operations on `audit_log` from the application database user and from a simulated super admin user, and shall confirm both are rejected at the database level. The test result shall be documented in `09-governance-compliance/02-audit-report/`.

## 5.3 Events Captured

The system shall write an audit record for every occurrence of the following event types:

| Event Type | Fields Logged |
|---|---|
| Record created | `tenant_id`, `user_id`, `module`, `action = CREATE`, `record_id`, new values (JSON), IP address, timestamp |
| Record updated | `tenant_id`, `user_id`, `module`, `action = UPDATE`, `record_id`, old values (JSON), new values (JSON), IP address, timestamp |
| Record deleted | `tenant_id`, `user_id`, `module`, `action = DELETE`, `record_id`, old values (JSON), IP address, timestamp |
| Approval action | `tenant_id`, `user_id`, `module`, `action = APPROVE` or `REJECT`, `record_id`, approval level, comment, IP address, timestamp |
| Login | `tenant_id`, `user_id`, `action = LOGIN`, authentication method (web session / JWT mobile), IP address, timestamp |
| Logout | `tenant_id`, `user_id`, `action = LOGOUT`, IP address, timestamp |
| Login failure | `tenant_id`, supplied username (no password), `action = LOGIN_FAILED`, failure reason code, IP address, timestamp |
| Super admin impersonation start | `tenant_id`, `super_admin_user_id`, `action = IMPERSONATE_START`, `super_admin_origin = TRUE`, IP address, timestamp |
| Super admin impersonation end | `tenant_id`, `super_admin_user_id`, `action = IMPERSONATE_END`, session duration, IP address, timestamp |
| Role change | `tenant_id`, `admin_user_id`, `affected_user_id`, `action = ROLE_CHANGE`, old role, new role, IP address, timestamp |
| Account enable/disable | `tenant_id`, `admin_user_id`, `affected_user_id`, `action = ACCOUNT_STATUS_CHANGE`, old status, new status, IP address, timestamp |
| Refresh token reuse detected | `tenant_id`, `user_id`, `action = REFRESH_TOKEN_REUSE_DETECTED`, IP address, timestamp |

## 5.4 Sensitive Data in Audit Records

The system shall not write plaintext passwords, full bank account numbers, or biometric data to the audit log. For sensitive fields subject to encryption at rest (see Section 6), the audit log shall record a masked representation (e.g., the last 4 digits of a bank account number, not the full value). Old and new value JSON blobs shall exclude fields designated as audit-masked in the schema definition.

## 5.5 External Auditor Access

The system shall provide a named database role `external_auditor_ro` with the following access profile:

- SELECT on `audit_log`.
- Access to the audit log search and export interface in the Tenant Workspace.
- No INSERT, UPDATE, or DELETE permission on any table.
- No access to operational data tables (invoices, payroll records, inventory transactions, etc.) except through aggregate reporting views explicitly scoped for audit purposes.

Assignment of the `external_auditor_ro` role to a user account is an administrative action logged in the audit log.

## 5.6 Retention Policy

The system shall retain all audit log records for a minimum of 7 years from the date of the recorded event, consistent with the Uganda Companies Act retention requirement. The minimum compliant retention period is 5 years; the 7-year default provides a 2-year buffer for regulatory changes. Tenant offboarding shall not result in deletion of audit log records within the retention window. Section 6.6 specifies the data deletion procedure for tenant offboarding and its interaction with audit retention obligations.
