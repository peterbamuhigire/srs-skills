# Authorization Model

## 3.1 Role-Based Access Control Architecture

Longhorn ERP implements Role-Based Access Control (RBAC) at two scopes: tenant-scoped roles for all regular users and platform-scoped roles for super administrators. These two scopes are strictly separated — no tenant-scoped role grants any access to super admin functions, and no super admin session grants access to tenant data outside of the audited impersonation mechanism defined in Section 3.6.

## 3.2 Tenant-Scoped Roles

### 3.2.1 Role Definition

Roles are defined per tenant. Each tenant provisions its own role set through the Tenant Workspace role management interface. Roles defined by one tenant are invisible to and have no effect on any other tenant.

### 3.2.2 Permission Matrix

Each role is assigned permissions through a function × action matrix. The axes of this matrix are:

- **Function** — a named feature or operation within a module (e.g., `invoice.create`, `payroll.approve`, `stocktransfer.edit`).
- **Action** — one of five standard action verbs: `view`, `create`, `edit`, `approve`, `delete`.

A permission entry is a boolean grant for a specific function-action pair. No implicit inheritance exists between action levels — granting `edit` does not imply `view` unless `view` is also explicitly granted.

### 3.2.3 Branch Restrictions

Each user account may be restricted to one or more branches. When branch restrictions are active for a user, the system shall:

- Return only records belonging to the user's permitted branches in all list and report views.
- Reject any attempt to create or modify records for a branch outside the user's permitted set with HTTP 403.
- Apply branch restrictions after tenant isolation — a branch restriction check shall never bypass the `tenant_id` filter.

### 3.2.4 Approval Limits

Each user may be assigned monetary approval limits per transaction type (e.g., purchase order approval, payment voucher approval, expense claim approval). Approval limit configuration is stored in the `user_approval_limits` table, keyed by `tenant_id`, `user_id`, and `transaction_type`. The system shall reject any approval action where the transaction amount exceeds the approving user's configured limit for that transaction type.

## 3.3 Module Gating

A user shall not access any function within a module that the authenticated tenant has not activated, regardless of the permissions granted to the user's role. Module gating is enforced at the middleware layer before any role permission check is evaluated.

The enforcement sequence for every request is:

1. Authenticate the session or token (resolve `tenant_id` and `user_id`).
2. Check whether the requested module is active for the authenticated tenant (`module_subscriptions` table). If inactive, return HTTP 404.
3. Check whether the user's role includes the required function-action permission. If not, return HTTP 403.
4. Check branch restrictions. If the target record's branch is outside the user's permitted set, return HTTP 403.
5. Execute the requested operation.

The `modules` claim in the JWT access token carries the list of activated module identifiers at login time. Mobile clients shall use this claim to suppress navigation to inactive modules at the UI layer. The server shall re-validate module activation on every request and shall not rely solely on the claim value.

## 3.4 Separation of Duties

The system shall support the following separation of duties controls, which tenant administrators may enforce through role configuration:

- A user who creates a transaction shall not be permitted to approve the same transaction.
- A user who approves a payment shall not be the same user who created the associated purchase order, unless the tenant has explicitly disabled this control.

Separation of duties violations shall be detected and rejected at the approval action layer, not at the UI layer only.

## 3.5 Platform-Scoped Super Admin Roles

The Super Admin Panel operates under a separate role set defined by the Chwezi platform team. Super admin roles are not visible to, configurable by, or affected by any tenant. Super admin authentication uses a dedicated session (`LONGHORN_SUPERADMIN_SESSION`) stored separately from tenant workspace sessions.

## 3.6 Super Administrator Impersonation

Super administrators may impersonate a tenant user to investigate support issues. The impersonation mechanism shall enforce all of the following controls:

- Impersonation is initiated only from the Super Admin Panel and requires the super admin's active authenticated session.
- The system shall create a distinct, time-limited impersonation session. The impersonation session expires after 60 minutes or upon explicit termination by the super admin.
- Every action performed during an impersonation session shall be logged in the `audit_log` table under the impersonated tenant's data, with both the `user_id` of the impersonated user and a boolean flag `super_admin_origin = TRUE`.
- The impersonated tenant shall be able to view all actions performed on their data, including those performed via impersonation, through the standard audit log interface.
- Super admin impersonation sessions shall not be used to export bulk tenant data. Any attempt to call a data export endpoint during an impersonation session shall be logged and shall require a secondary confirmation step.
