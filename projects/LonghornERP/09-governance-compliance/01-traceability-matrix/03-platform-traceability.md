# 3. Platform Requirements Traceability

This section covers the 6 platform SRS components. Business goal mapping uses the 6 PRD-level goals: BG-001 (Replace manual ERP), BG-002 (Statutory compliance), BG-003 (Multi-country expansion), BG-004 (Financial visibility), BG-005 (Mobile-first), BG-006 (SaaS platform).

*Note on local vs. PRD business goals: The RBAC SRS uses goals BG-PLT-01 through BG-PLT-13; the Audit Log SRS uses BG-01 through BG-07; the Integration Layer SRS uses BG-001 through BG-004; the Multi-Tenancy SRS uses BG-01 through BG-15. These local goals are mapped to PRD goals in the Description column for each FR.*

## 3.1 Multi-Tenancy and Billing (FR-PLAT-*)

*Source: `02-requirements-engineering/01-srs/00-platform/01-multitenancy-billing/07-traceability.md`*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-PLAT-001 | Super admin creates tenant; assigns subdomain and primary contact | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-002 | Tenant subdomain is unique and stable across all URLs and API calls | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-003 | New tenant enters 30-day free trial on provisioning | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-004 | Primary contact credentials delivered; tenant operable on Day 1 | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-005 | Tenant localisation profile assigned at provisioning | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-006 | Core modules (accounting, inventory, sales, procurement) activated by default | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-007 | At least 1 operating branch created at provisioning | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-008 | Chart of accounts pre-seeded from localisation profile at provisioning | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-009 | Tenant admin login credentials functional without support contact | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-010 | All provisioning actions written to audit log | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-011 | Subscription billing period begins on first payment date | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-012 | Platform enforces trial-to-paid conversion without manual intervention | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-013 | Access restricted when subscription payment lapses | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-014 | 7-day grace period before hard suspension on non-payment | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-015 | Tenant suspended after grace period expires | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-016 | Access restored immediately on payment during suspension | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-017 | Suspended tenants retain read-only access to financial records | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-018 | Full payment restores full access without super admin step | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-019 | Tenants inactive for 12+ months archived automatically | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-020 | Archived tenants consume no active compute resources | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-021 | Tenant data retained for 7 years minimum | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-022 | Archived tenants can be reactivated | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-023 | All tenant lifecycle transitions are audited | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-030 | Super admin activates add-on module per tenant subscription | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-031 | Add-on modules deactivated on subscription lapse | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-032 | Module dependency validation on activation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-033 | Navigation renders only activated modules | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-034 | Direct URL access blocked for inactive module endpoints | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-035 | Core modules are non-removable for all tenants | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-036 | Plan-included modules auto-activate on plan assignment | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-037 | Downgrade deactivates out-of-plan modules at cycle end | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-038 | All module activation events written to audit log | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-040 | Subscription plan assignment is the primary billing configuration event | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-041 | User count limits enforced per subscription plan tier | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-042 | Branch limits enforced per subscription plan tier | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-043 | Plan upgrades take effect immediately | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-044 | Plan downgrades take effect at end of billing cycle | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-045 | Annual billing provides 2-month discount incentive | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-046 | Invoice generated 7 days before due date | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-047 | Unpaid arrears carried forward to next invoice | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-048 | Payment recording drives lifecycle state transitions | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-049 | MTN MoMo and M-Pesa accepted for SaaS subscription payment | BG-003, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-050 | Tenant status restored immediately on payment confirmation | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-051 | Annual billing discount formula is auditable | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-052 | A-la-carte module purchase restricted to Small Business and Professional plans | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-053 | A-la-carte charges itemised on invoices | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-054 | Upgrade prompt triggered when a-la-carte cost approaches next tier price | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-055 | POS licensed per terminal, not per organisation | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-056 | All billing events written to audit log | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-057 | Settled invoices are immutable financial records | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-058 | PDF invoices generated for offline payment workflows | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-059 | Invoice delivered by email to reduce time-to-payment | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PLAT-060 | Credits issued to tenant for disputes or platform outages | BG-006 | TC-PENDING | [TRACE-GAP-TC] |

## 3.2 Role-Based Access Control (FR-RBAC-*)

*Source: `02-requirements-engineering/01-srs/00-platform/02-rbac/06-traceability.md`*

*TC identifiers are sourced from the RBAC SRS traceability table, which was authored before the central test plan. These TCs are valid and require reconciliation with the central test plan.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-RBAC-001 | Create user with name, email, role, branch, and initial password | BG-001, BG-006 | TC-RBAC-001 | |
| FR-RBAC-002 | Enforce email uniqueness per tenant | BG-001, BG-006 | TC-RBAC-002 | |
| FR-RBAC-003 | Enforce password policy at account creation | BG-006 | TC-RBAC-003 | |
| FR-RBAC-004 | New account flagged pending; activation email sent | BG-001, BG-006 | TC-RBAC-004 | |
| FR-RBAC-005 | Activate account via time-limited email token | BG-001, BG-006 | TC-RBAC-005 | |
| FR-RBAC-006 | Deactivate account and terminate all sessions immediately | BG-006 | TC-RBAC-006 | |
| FR-RBAC-007 | Reactivate a previously deactivated account | BG-001, BG-006 | TC-RBAC-007 | |
| FR-RBAC-008 | Self-service password reset via email token | BG-006 | TC-RBAC-008 | |
| FR-RBAC-008a | Complete self-service reset; invalidate existing sessions | BG-006 | TC-RBAC-008A | |
| FR-RBAC-008b | Admin-initiated password reset for any user | BG-001, BG-006 | TC-RBAC-008B | |
| FR-RBAC-009 | Enforce configurable password policy (length, complexity, expiry, history) | BG-006 | TC-RBAC-009 | |
| FR-RBAC-010 | Force password change on expiry at next login | BG-006 | TC-RBAC-010 | |
| FR-RBAC-011 | Enforce configurable maximum concurrent sessions per user | BG-006 | TC-RBAC-011 | |
| FR-RBAC-012 | Terminate idle session after configurable timeout | BG-006 | TC-RBAC-012 | |
| FR-RBAC-013 | Reset idle timeout counter on each authenticated request | BG-006 | TC-RBAC-013 | |
| FR-RBAC-014 | Admin-triggered forced logout invalidates all user sessions | BG-006 | TC-RBAC-014 | |
| FR-RBAC-015 | Display "Session terminated by administrator" on post-logout request | BG-006 | TC-RBAC-015 | |
| FR-RBAC-016 | Lock account after N consecutive failed login attempts | BG-006 | TC-RBAC-016 | |
| FR-RBAC-017 | Prevent login to locked account until auto-unlock or admin unlock | BG-006 | TC-RBAC-017 | |
| FR-RBAC-018 | Reset failed-attempt counter on successful login | BG-006 | TC-RBAC-018 | |
| FR-RBAC-019 | Log every failed login attempt in audit log | BG-002, BG-006 | TC-RBAC-019 | |
| FR-RBAC-020 | Email notification on account lockout to user and admin | BG-006 | TC-RBAC-020 | |
| FR-RBAC-030 | Create role with name, description, and initial permission set | BG-001, BG-006 | TC-RBAC-030 | |
| FR-RBAC-031 | Enforce role name uniqueness within tenant | BG-001, BG-006 | TC-RBAC-031 | |
| FR-RBAC-032 | Clone existing role with independent permission copy | BG-001, BG-006 | TC-RBAC-032 | |
| FR-RBAC-033 | Assign role to user; apply permissions immediately | BG-001, BG-006 | TC-RBAC-033 | |
| FR-RBAC-034 | Support exactly 1 active role per user; invalidate cache on reassignment | BG-001, BG-006 | TC-RBAC-034 | |
| FR-RBAC-035 | Enforce function × action permission matrix (view/create/edit/approve/delete) | BG-001, BG-006 | TC-RBAC-035 | |
| FR-RBAC-036 | Return HTTP 403 and "Access Denied" for unauthorised function/action | BG-001, BG-006 | TC-RBAC-036 | |
| FR-RBAC-037 | Hide non-permitted UI elements; do not merely disable | BG-001, BG-006 | TC-RBAC-037 | |
| FR-RBAC-038 | Restrict data access to user's assigned branches | BG-001, BG-006 | TC-RBAC-038 | |
| FR-RBAC-039 | Allow admin to update branch assignments; apply within cache window | BG-001, BG-006 | TC-RBAC-039 | |
| FR-RBAC-040 | Exempt "All Branches" flag holders from branch restriction | BG-001, BG-006 | TC-RBAC-040 | |
| FR-RBAC-041 | Enforce per-user per-transaction-type approval limits (UGX) | BG-004, BG-006 | TC-RBAC-041 | |
| FR-RBAC-042 | Allow admin to set, update, or remove approval limits | BG-004, BG-006 | TC-RBAC-042 | |
| FR-RBAC-043 | Audit log entry for every approval limit change | BG-002, BG-006 | TC-RBAC-043 | |
| FR-RBAC-044 | Deny access to functions in non-activated modules | BG-006 | TC-RBAC-044 | |
| FR-RBAC-045 | Re-evaluate module gates in real time on subscription change | BG-006 | TC-RBAC-045 | |
| FR-RBAC-046 | Super admin initiates impersonation session for any tenant user | BG-006 | TC-RBAC-046 | |
| FR-RBAC-047 | Log all impersonation session actions with impersonation flag | BG-002, BG-006 | TC-RBAC-047 | |
| FR-RBAC-048 | Display persistent impersonation banner with End Impersonation control | BG-006 | TC-RBAC-048 | |
| FR-RBAC-049 | Auto-terminate impersonation session after 30 minutes | BG-006 | TC-RBAC-049 | |
| FR-RBAC-050 | Restrict privileged operations within impersonation session | BG-006 | TC-RBAC-050 | |
| FR-RBAC-060 | Generate TOTP shared secret and QR code on 2FA enrollment | BG-006 | TC-RBAC-060 | |
| FR-RBAC-061 | Complete 2FA enrollment on valid TOTP code submission | BG-006 | TC-RBAC-061 | |
| FR-RBAC-062 | Generate 10 single-use backup codes on 2FA enrollment | BG-006 | TC-RBAC-062 | |
| FR-RBAC-063 | Mark backup code as used; block re-use | BG-006 | TC-RBAC-063 | |
| FR-RBAC-064 | Require TOTP or backup code on every login when 2FA is enabled | BG-006 | TC-RBAC-064 | |
| FR-RBAC-065 | Admin can mandate 2FA enrollment for specific roles | BG-006 | TC-RBAC-065 | |
| FR-RBAC-066 | Admin or user can disable 2FA per tenant policy | BG-006 | TC-RBAC-066 | |
| FR-RBAC-067 | Receive biometric authentication events from Zkteco devices | BG-005, BG-006 | TC-RBAC-067 | |
| FR-RBAC-068 | Record attendance and optionally create session on valid Zkteco event | BG-005, BG-006 | TC-RBAC-068 | |
| FR-RBAC-069 | Reject and audit-log invalid or unregistered Zkteco events | BG-005, BG-006 | TC-RBAC-069 | |
| FR-RBAC-070 | Admin configures per-user biometric session creation policy | BG-005, BG-006 | TC-RBAC-070 | |
| FR-RBAC-071 | Authenticate USSD session by caller mobile number match | BG-005, BG-006 | TC-RBAC-071 | |
| FR-RBAC-072 | USSD stock lookup by item code returns name and quantity | BG-005 | TC-RBAC-072 | |
| FR-RBAC-073 | USSD GRN confirmation updates GRN status and audit log | BG-005 | TC-RBAC-073 | |
| FR-RBAC-074 | Terminate USSD session for unregistered or unauthorised caller | BG-005, BG-006 | TC-RBAC-074 | |
| FR-RBAC-075 | Terminate USSD session on timeout or gateway close; discard partial state | BG-005, BG-006 | TC-RBAC-075 | |

## 3.3 Audit Log (FR-AUDIT-*)

*Source: `02-requirements-engineering/01-srs/00-platform/03-audit-log/07-traceability.md`*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-AUDIT-001 | Every state-changing event captured as an audit record | BG-002, BG-006 | TC-PLAT-007 | |
| FR-AUDIT-002 | Audit record captures all 12 mandatory fields | BG-002, BG-006 | TC-PLAT-007 | |
| FR-AUDIT-003 | old_values/new_values stored on UPDATE events | BG-002 | TC-PLAT-008 | |
| FR-AUDIT-004 | Action field constrained to defined enumeration | BG-002 | TC-PLAT-007 | |
| FR-AUDIT-005 | tenant_id sourced from session context only; never from request body | BG-002, BG-006 | TC-PLAT-003 | |
| FR-AUDIT-006 | Login attempt (success and failure) logged | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-007 | Failed login logged without recording password value | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-008 | Logout event logged | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-009 | Impersonation session start logged | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-010 | Impersonation session end logged | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-011 | Super admin identity attributed during impersonation actions | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-012 | Each row in a bulk operation logged individually | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-013 | bulk_operation_id groups all rows of one bulk action | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-014 | Mobile API state-changing requests logged | BG-002, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-015 | API user_agent captured in audit record | BG-002, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-016 | Background job state changes logged | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-017 | job_execution_id groups all rows of one job run | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-018 | Tenant configuration changes logged | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-019 | RBAC changes (role, permission, user) logged | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-020 | Tenant account lifecycle events logged | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-030 | No UPDATE or DELETE permitted on audit_log table | BG-002 | TC-PLAT-009 | |
| FR-AUDIT-031 | INSERT-only privilege granted to application role | BG-002 | TC-PLAT-009 | |
| FR-AUDIT-032 | Database trigger enforces INSERT-only as second layer | BG-002 | TC-PLAT-009 | |
| FR-AUDIT-033 | SHA-256 hash computed and stored at INSERT | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-034 | Tamper verification report identifies mismatched hashes | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-035 | Tamper report shows flagged record ID and expected vs. actual hash | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-036 | Tamper report execution itself logged in audit log | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-037 | All audit writes pass through AuditLogService exclusively | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-038 | AuditLogService public interface exposes no direct write methods | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-039 | Dedicated connection pool for audit writes | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-040 | Durable queue buffers audit writes during DB failure | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-050 | Audit log read restricted by role | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-051 | external_auditor role defined with read-only audit access | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-052 | Audit log queries scoped to requesting tenant | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-053 | Audit log search accepts multiple independent filter dimensions | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-054 | Filters combined with AND logic independently | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-055 | Default 30-day date range applied on search | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-056 | Search results include all 12 defined columns | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-057 | Server-side pagination applied to search results | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-058 | Export to CSV format | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-059 | Export to Excel (.xlsx) format | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-060 | Export to PDF with header metadata | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-061 | All 12 fields present in all export formats | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-062 | Export action itself logged | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-063 | Record detail view renders JSON old_values/new_values | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-064 | Direct URL shareable per audit record | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-065 | Hyperlink on affected entity navigates to the record | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-070 | 7-year minimum retention enforced | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-071 | Retention period visible in admin UI | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-072 | Records older than retention threshold archived to audit_log_archive | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-073 | audit_log_archive is immutable | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-074 | Search spans both live and archived records transparently | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-075 | Super admin deletion requires confirmation phrase | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-076 | Deletion event logged before execution | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AUDIT-077 | Deletion blocked before 7-year retention period expires | BG-002 | TC-PENDING | [TRACE-GAP-TC] |

## 3.4 Localisation and Statutory Compliance (FR-LOC-*)

*Source: `02-requirements-engineering/01-srs/00-platform/04-localisation/08-traceability.md`*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-LOC-001 | Maintain localisation profile record per tenant | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-002 | Active profile applied to all calculations and formatting | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-003 | Super admin assigns profile at tenant provisioning | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-004 | Super admin updates profile without code deployment | BG-003, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-005 | New market entry via new profile record only; no code change | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-006 | Version entry created on every profile update | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-007 | Full profile version history viewable | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-008 | Previous profile version restorable as new version | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-009 | Two-level profile hierarchy (base profile + override) | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-010 | Override-first resolution of effective parameter value | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-011 | Base profile created with is_base = true | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-012 | Required parameters validated before profile assignment | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-013 | Inconsistent parameter combinations rejected | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-014 | Resolved effective profile provided as read-only object per request | BG-003, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-015 | Profile read access logged in audit log | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-020 | Monetary values displayed per profile currency fields | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-021 | Monetary values stored as DECIMAL(19,4) in base currency | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-022 | Base currency designated per profile | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-023 | Exchange rate records stored per tenant | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-024 | Most recent rate on or before transaction date applied | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-025 | FX revaluation at period end per IFRS IAS 21 | BG-002, BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-026 | UI strings loaded from language file per profile | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-027 | Minimum required language codes supported | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-028 | Fall back to en-UG on missing language file | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-029 | Dates formatted per date_format profile field | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-030 | Dates stored as UTC in DATE/DATETIME columns | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-031 | Non-currency numbers formatted per profile separators | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-032 | Numeric values stored in standard decimal notation | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-033 | Financial year start derived from financial_year_start_month | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-034 | Accounting periods labelled "Period N — [Month] [Year]" | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-035 | Posting to closed periods rejected | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-050 | VAT/tax rate and name applied from profile | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-051 | Jurisdiction-specific tax name displayed on documents | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-052 | Multiple tax rates per profile supported via tax_rates table | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-053 | VAT return export generated in authority-required format | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-054 | PAYE calculated from paye_config_json band array | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-055 | Statutory deductions calculated from statutory_deductions_json | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-056 | WHT calculated from wht_rate on supplier payments | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-057 | Fiscal receipt routed to EFRIS/eTIMS per profile | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-058 | Fiscal receipt credentials resolved from vault | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-059 | Failed fiscal receipt queued for retry; invoice marked fiscal_pending | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-060 | Payroll statutory filing routed to provider per profile | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-061 | Payroll statutory API credentials resolved from vault | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-062 | Statutory payroll export generated per provider format | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-063 | Data retention enforced per data_retention_years | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-064 | WHT displayed as separate line on supplier payment documents | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-065 | WHT certificate generated per deduction | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-066 | WHT summary return export produced | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-067 | Exempt/zero-rated tax applied from tax_rates table | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-068 | Tax rate name and percentage shown per differing invoice line | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-069 | Document tax = sum of per-line tax amounts | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-070 | Rate breakdown table included in VAT return export | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-080 | COA starter template loaded at tenant provisioning | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-081 | COA templates sourced from coa_templates table | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-082 | Tenant admin modifies COA after provisioning without affecting others | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-083 | invoice_legal_text appended as footer on invoices | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-084 | invoice_legal_text rendered without modification | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-085 | PPDA approval workflow activated when ppda_workflow_enabled = true | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-086 | PPDA thresholds enforced from tenant PPDA config record | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-087 | PPDA workflow bypassed when ppda_workflow_enabled = false | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-088 | Address fields rendered per address_format_json order | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-089 | address_format_json used for both entry forms and read-only display | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-090 | city and country fields validated present in address format | BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-095 | SMS routed through provider per sms_gateway_provider | BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-096 | SMS credentials resolved from vault | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-097 | Every outbound SMS attempt logged in audit log | BG-002, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-098 | Mobile money payments routed per mobile_money_providers_json | BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-099 | Mobile money credentials resolved from vault | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-100 | All gateway credentials stored in vault only | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-101 | Vault credentials encrypted at rest with AES-256 | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-102 | Credentials rotatable without profile version bump | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-103 | Core ERP functions continue when gateway is unavailable | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-104 | Failed gateway requests queued with exponential back-off | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-LOC-105 | Transactions marked gateway_pending; cleared on gateway success | BG-001, BG-004, BG-006 | TC-PENDING | [TRACE-GAP-TC] |

## 3.5 Mobile API (FR-MAPI-*)

*Source: `02-requirements-engineering/01-srs/00-platform/05-mobile-api/10-traceability.md`*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-MAPI-001 | Issue JWT access token and refresh token on valid login | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-002 | JWT contains tid, uid, role, modules, iat, exp claims | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-003 | tid sourced from database; never from request body | BG-005, BG-006 | TC-PLAT-002 | |
| FR-MAPI-004 | Refresh token rotation on each use | BG-005, BG-006 | TC-PLAT-012 | |
| FR-MAPI-005 | Configurable JWT access and refresh token TTL | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-006 | HTTP 401 for expired JWT | BG-005, BG-006 | TC-PLAT-010 | |
| FR-MAPI-007 | HTTP 401 for invalid JWT signature or malformed token | BG-005, BG-006 | TC-PLAT-011 | |
| FR-MAPI-008 | HTTP 401 for revoked JWT | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-009 | All user tokens invalidated within 5 s of account disable | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-010 | Access and refresh tokens blacklisted on logout | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-011 | Blacklist entry TTL equals token remaining validity | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-012 | New token pair issued on valid refresh token | BG-005, BG-006 | TC-PLAT-012 | |
| FR-MAPI-013 | HTTP 401 for expired or revoked refresh token | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-014 | Device push token registered on first login | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-015 | Device token registration upserted; no duplicates | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-020 | tenant_id sourced exclusively from JWT tid claim | BG-005, BG-006 | TC-PLAT-002 | |
| FR-MAPI-021 | All queries scoped by JWT tid | BG-005, BG-006 | TC-PLAT-003 | |
| FR-MAPI-022 | HTTP 404 returned for cross-tenant resource access | BG-005, BG-006 | TC-PLAT-001 | |
| FR-MAPI-023 | Audit log entry for cross-tenant access attempts | BG-002, BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-024 | HTTP 403 for disabled-module endpoints | BG-005, BG-006 | TC-PLAT-004 | |
| FR-MAPI-025 | No module endpoint leakage in API discovery responses | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-030 | API versioning via /api/mobile/v{N}/ URL path | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-031 | At least 2 active API versions simultaneously | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-032 | No breaking changes within a version | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-033 | Minimum 90-day deprecation window before version sunset | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-034 | GET /api/mobile/versions discovery endpoint | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-035 | Deprecation and Sunset headers on deprecated version responses | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-040 | Offline data collection for 72+ hours (Cooperative Procurement) | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-041 | All pending records synced within 60 s of reconnection | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-042 | Delta sync via last_sync_at timestamp protocol | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-043 | Conflict detection without silent overwrite | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-044 | Sync status endpoint available | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-045 | UUID v4 idempotency key per offline transaction | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-046 | mobile_sync_log audit trail per synced transaction | BG-002, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-047 | HTTP 207 partial batch on validation failure | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-048 | Maximum batch size of 500 records per sync | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-049 | Offline mode restricted to Cooperative Procurement in v1 | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-050 | Module capabilities endpoint for offline eligibility | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-051 | Reference data snapshot endpoint for offline form population | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-052 | data_version hash in reference data snapshot | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-053 | AES-256 encrypted local offline database | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-054 | Visual sync status indicator updates within 2 s | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-055 | Sync rejected on expired/revoked JWT during offline period | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-060 | Push notifications delivered for 5 defined event types | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-061 | Standard 6-field notification payload | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-062 | No sensitive data in push notification payload | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-063 | Device token registered via POST /api/mobile/v1/devices | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-064 | Device tokens deregistered on account disable or explicit delete | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-065 | APNs/FCM token refresh upserted | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-066 | 3-attempt exponential backoff on push delivery failure | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-067 | SMS fallback via Africa's Talking after 3 push failures | BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-068 | notification_log audit trail | BG-002, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-069 | Per-event-type notification preferences | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-070 | Quiet hours notification deferral | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-080 | Token bucket rate limiting per tenant and user | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-081 | HTTP 429 with Retry-After header on rate limit exceeded | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-082 | Rate limit rule precedence (most specific wins) | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-083 | X-RateLimit-* headers on all responses | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-084 | Default 120 req/60 s platform-wide rate limit | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-085 | Rate limit rules updated via Super Admin API; effective within 30 s | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-090 | Data-lite mode reduces payload by ≥ 40% via X-Data-Lite: true | BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-091 | Essential fields retained in data-lite mode | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-092 | X-Data-Lite: applied confirmation header | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MAPI-093 | Data-lite applied at serialisation layer; audit log unaffected | BG-002, BG-005 | TC-PENDING | [TRACE-GAP-TC] |

## 3.6 Integration Layer (FR-INTG-*)

*Source: `02-requirements-engineering/01-srs/00-platform/06-integration-layer/08-traceability.md`*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-INTG-001 | Submit sales invoice to EFRIS before customer delivery | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-002 | Submit credit note to EFRIS before customer delivery | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-003 | Construct EFRIS payload per URA field mapping | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-004 | Include TIN, line items, and tax amounts in EFRIS payload | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-005 | Transmit EFRIS payloads over TLS 1.2+ | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-006 | Parse fiscal document number and QR code from EFRIS response | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-007 | Store fiscal document number and QR code on invoice record | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-008 | Embed fiscal document number and QR code in printed invoice | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-009 | Mark invoice EFRIS_SUBMITTED on successful response | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-010 | Retry failed EFRIS submission with exponential backoff (3 attempts) | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-011 | Queue payload; mark invoice EFRIS_QUEUED after 3 failures | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-012 | Invoicing workflow not blocked when EFRIS submission is queued | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-013 | Queued EFRIS payloads retained for 72 hours | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-014 | EFRIS status indicator displayed on invoice record | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-015 | Offline queue auto-processed on EFRIS endpoint reconnection | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-016 | Invoice updated to EFRIS_SUBMITTED after queued submission succeeds | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-017 | Daily EFRIS reconciliation report generated | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-018 | Manual resubmission of EFRIS_FAILED invoices allowed | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-019 | EFRIS credentials retrieved from encrypted store only | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-020 | EFRIS credentials never logged in plaintext | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-021 | Provider-plugin architecture for mobile money adapters | BG-003, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-022 | Provider plugins activated without modifying Integration Layer core | BG-003, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-023 | MTN MoMo activated for profiles UG/RW | BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-024 | Airtel Money activated for profiles UG/KE/TZ | BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-025 | M-Pesa Daraja activated for profiles KE/TZ | BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-026 | SaaS subscription fee collected via mobile money | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-027 | Customer invoice payment collected via mobile money | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-028 | Supplier payment disbursed via mobile money | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-029 | Amount, currency, mobile number, and reference transmitted on initiation | BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-030 | UUID v4 reference assigned to every mobile money request | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-031 | Provider transaction ID recorded alongside internal reference | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-032 | Provider status polled at 15s, 30s, 60s when no callback received | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-033 | Transaction marked TIMEOUT; polling ceases after 5 minutes | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-034 | Tenant-isolated inbound callback endpoint per provider | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-035 | Provider callback signature validated before processing | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-036 | Payment ledger updated to PAID within 3 s of successful callback | BG-001, BG-004, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-037 | Transaction updated to FAILED on declined callback | BG-004, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-038 | Daily mobile money reconciliation report per provider | BG-004, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-039 | Reconciliation anomalies flagged for Finance administrator review | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-040 | Reversal request submitted to provider on authorised refund | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-041 | Record updated to REVERSED; credit entry posted on confirmed reversal | BG-001, BG-004, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-042 | Timed-out transactions placed in manual review queue | BG-004, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-043 | Mobile money credentials stored with AES-256 encryption | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-044 | Credentials retrieved from encrypted store at runtime only | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-045 | Mobile money credentials never logged in plaintext | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-046 | Submit sales invoice to KRA eTIMS before customer delivery | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-047 | Submit credit note to KRA eTIMS before customer delivery | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-048 | Construct eTIMS payload per KRA field mapping | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-049 | Include KRA PIN, HS codes, and tax amounts in eTIMS payload | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-050 | Transmit eTIMS payloads over TLS 1.2+ | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-051 | Parse CUIN and QR code from eTIMS response | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-052 | Store CUIN and QR code on invoice record | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-053 | Embed CUIN and QR code in printed invoice | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-054 | Mark invoice ETIMS_SUBMITTED on successful response | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-055 | Retry failed eTIMS submission with exponential backoff (3 attempts) | BG-002, BG-003, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-056 | Queue payload; mark invoice ETIMS_QUEUED after 3 failures | BG-002, BG-003, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-057 | Invoicing workflow not blocked when eTIMS submission is queued | BG-001, BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-058 | Queued eTIMS payloads retained for 72 hours | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-059 | eTIMS status indicator displayed on invoice record | BG-002, BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-060 | Offline queue auto-processed on eTIMS endpoint reconnection | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-061 | eTIMS credentials retrieved from encrypted store only | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-062 | eTIMS credentials never logged in plaintext | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-063 | NSSF adapter activated when HR & Payroll active and profile is UG/KE | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-064 | Jurisdiction-specific NSSF rules applied per localisation profile | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-065 | Monthly NSSF contribution file generated from payroll close | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-066 | Contribution file formatted per NSSF-specified schema | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-067 | Payroll administrator can preview file before submission | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-068 | Contribution file submitted via NSSF REST API or SFTP | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-069 | NSSF submission reference number and status recorded | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-070 | NSSF portal validation errors surfaced to Payroll administrator | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-071 | Correction and resubmission of rejected NSSF records allowed | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-072 | NSSF contribution files retained for 7 years | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-073 | Tenant administrator registers webhook endpoint with URL, secret, events | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-074 | Webhook URL validated as syntactically valid HTTPS URL | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-075 | Webhook activated/deactivated without deletion | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-076 | Webhook URL, secret, and event subscriptions updatable | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-077 | Webhook secret key stored with AES-256 encryption | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-078 | Standard event types supported for webhook subscription | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-079 | New event types registered without modifying webhook core | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-080 | Webhooks delivered as HTTP POST with Content-Type: application/json | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-081 | Payload includes event_type, event_id, tenant_id, timestamp, data | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-082 | Outbound webhook payload signed with HMAC-SHA256 in X-Longhorn-Signature | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-083 | HMAC-SHA256 verification procedure documented in developer reference | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-084 | Webhook dispatched within 10 s at P95 | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-085 | Delivery considered successful on HTTP 2xx within 10 s | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-086 | Failed webhook delivery retried with exponential backoff (3 attempts) | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-087 | Payload moved to DLQ after 3 failed delivery attempts | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-088 | DLQ entries retained for 7 days and surfaced to tenant administrator | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-089 | Manual re-delivery of DLQ entries allowed | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-090 | Delivery log entry recorded for every webhook dispatch attempt | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INTG-091 | Webhook delivery logs retained for 30 days | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
