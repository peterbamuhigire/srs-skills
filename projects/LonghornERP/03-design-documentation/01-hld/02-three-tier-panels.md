# Three-Tier Panel Architecture

Longhorn ERP exposes three distinct web panels, each serving a different class of user at a different URL path. All three panels run within the same PHP application but enforce separate authentication scopes, session contexts, and permission models.

## 2.1 Panel Summary

| Panel | URL Path | Primary Users | Authentication |
|---|---|---|---|
| Tenant Workspace | `/public/` | All tenant staff | Session — `LONGHORN_ERP_SESSION` |
| Super Admin Panel | `/public/superadmin/` | Chwezi platform operators | Separate super admin session |
| End-User Portal | `/public/portal/` | Employees, customers, agents, farmers | Separate portal session |

---

## 2.2 Tenant Workspace (`/public/`)

### URL Path

`/public/`

### Primary Users

All staff users who belong to an active tenant: accountants, sales representatives, procurement officers, warehouse staff, HR managers, branch managers, and any other role defined within the tenant's Role-Based Access Control (RBAC) configuration.

### Key Capabilities

- Full access to all modules the tenant has activated under its subscription plan.
- Branch-scoped operations: every session is bound to a branch, and all data entry and reporting is branch-aware.
- Granular RBAC: every page and API endpoint enforces `RequirePermission` middleware checks against the authenticated user's role.
- Multi-currency transactions, localised tax computation, and statutory deduction processing driven by the tenant's active localisation profile.
- Real-time dashboard, data-entry forms, approval workflows, and reporting across all active modules.

### Authentication Method

Session-based authentication using the `LONGHORN_ERP_SESSION` cookie (HttpOnly, SameSite=Strict). The full middleware pipeline — `EnsureAuthenticated → EnsureTenantSelected → EnsureTenantActive → EnsureBranchSelected → RequirePermission` — executes on every request to this panel. See Section 4 for the complete middleware specification.

---

## 2.3 Super Admin Panel (`/public/superadmin/`)

### URL Path

`/public/superadmin/`

### Primary Users

Chwezi Core Systems platform operators responsible for managing the SaaS platform itself. Super admin users do not belong to any tenant and operate outside the tenant isolation boundary.

### Key Capabilities

- Tenant provisioning: create, configure, and onboard new tenants.
- Subscription management: assign subscription plans, activate or deactivate add-on modules, set billing cycles.
- Tenant lifecycle management: transition tenants through Trial → Active → Overdue → Suspended → Archived states.
- Billing and invoice generation for all tenants.
- Platform-wide monitoring: tenant activity, error rates, storage usage.
- Super admin user management: create and manage Chwezi operator accounts.
- Read-only access to tenant data for support escalations (access is logged in the audit trail).

### Authentication Method

Dedicated super admin session (separate cookie scope from tenant sessions). Super admin credentials are stored in an isolated user table with no `tenant_id`. All super admin API calls route through `/public/superadmin/api/` and enforce super admin session validation on every request.

---

## 2.4 End-User Portal (`/public/portal/`)

### URL Path

`/public/portal/`

### Primary Users

Four classes of external or limited-access users who require read-only or self-service access to specific data:

1. *Employees* — access payslips, leave balances, leave applications, and attendance records via the Employee Self-Service (ESS) interface.
2. *Customers* — access account statements, invoice history, and outstanding balances.
3. *Agents* — access commission statements, target progress, and payment history via the Sales Agents portal.
4. *Farmers / Outgrowers* — access commodity intake records, input loan balances, and payment statements via the Cooperative Procurement farmer portal.

### Key Capabilities

- Read-only views of tenant data relevant to the authenticated end-user's identity.
- PDF download of payslips, statements, and commission summaries.
- Leave application submission (employees only).
- Responsive, mobile-optimised layout for low-bandwidth access.
- Localised currency and date formatting driven by the tenant's localisation profile.

### Authentication Method

Dedicated portal session scoped to the end-user's identity class (employee, customer, agent, or farmer). Portal users authenticate with a credential set issued by the tenant. The portal session enforces the tenant context so that a portal user can only retrieve data belonging to their own tenant and their own identity record.
