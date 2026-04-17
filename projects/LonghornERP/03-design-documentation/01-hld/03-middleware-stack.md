# Middleware Stack

## 3.1 Request Processing Pipeline

Every page request to the Tenant Workspace (`/public/`) passes through the following middleware layers in strict sequence before the page handler executes:

```
EnsureAuthenticated
        │
        ▼
EnsureTenantSelected
        │
        ▼
EnsureTenantActive
        │
        ▼
EnsureBranchSelected
        │
        ▼
RequirePermission
        │
        ▼
   Page Handler
```

No page handler executes unless all five layers pass. A failure at any layer terminates the request and returns the appropriate response — no downstream layers run.

---

## 3.2 Layer Specifications

### Layer 1 — EnsureAuthenticated

**What it checks:** Whether a valid, non-expired session exists for the requesting user (`$_SESSION['user_id']` is set and the session has not timed out).

**On failure:** Destroys the session, clears the session cookie, and redirects the user to the login page (`/public/login.php`). The original requested URL is stored in `$_SESSION['redirect_after_login']` so the user is returned to their intended destination after successful authentication.

**Data provided downstream:** `$_SESSION['user_id']`, `$_SESSION['user_role']`, `$_SESSION['user_permissions']`, and `$_SESSION['user_branches']` are available to all subsequent layers and the page handler.

---

### Layer 2 — EnsureTenantSelected

**What it checks:** Whether `$_SESSION['tenant_id']` is set. A tenant context must be established before any data operation can proceed.

**On failure:** Redirects the user to the tenant selection screen if their account is associated with more than one tenant, or initiates automatic tenant binding if their account has exactly 1 tenant association. If no tenant association exists, the session is destroyed and the user is redirected to the login page with an error notification.

**Data provided downstream:** `$_SESSION['tenant_id']` is confirmed as set. The `TenantContext` object is populated with the tenant's configuration (currency, timezone, localisation profile, enabled modules, active branches) and injected into the dependency injection (DI) container for the duration of the request.

*Critical:* `tenant_id` is ALWAYS sourced from `$_SESSION['tenant_id']`. It is never read from `$_GET`, `$_POST`, `$_COOKIE`, or any other request parameter. Any attempt to override `tenant_id` via a request parameter shall be silently ignored — the session value is authoritative.

---

### Layer 3 — EnsureTenantActive

**What it checks:** Whether the tenant's lifecycle state permits login. The tenant's `status` field must be one of: `trial`, `active`.

**On failure:** The behaviour depends on the tenant's lifecycle state:

| Tenant State | Response |
|---|---|
| `overdue` | Redirects to a payment overdue notice page. The user cannot proceed until the outstanding balance is settled. |
| `suspended` | Redirects to a suspension notice page with a contact prompt for the Chwezi support team. |
| `archived` | Redirects to an archived account notice. No login is permitted. |

**Data provided downstream:** Confirmed that the tenant is in an active-access state. The `TenantContext` object is enriched with the tenant's subscription plan and the list of activated module codes.

---

### Layer 4 — EnsureBranchSelected

**What it checks:** Whether `$_SESSION['branch_id']` is set and whether the branch belongs to the authenticated tenant.

**On failure:** Redirects the user to the branch selection screen. If the user's RBAC profile restricts them to specific branches, only those branches appear in the selection list. If the user is restricted to a single branch, the system auto-selects it and continues without displaying the selection screen.

**Data provided downstream:** `$_SESSION['branch_id']` is confirmed as set and validated against `$_SESSION['tenant_id']`. All subsequent data operations scope their queries to the selected branch unless the user's role grants cross-branch visibility (e.g., management reports).

---

### Layer 5 — RequirePermission

**What it checks:** Whether the authenticated user holds the specific permission code required by the requested page. Each page declares its required permission constant (e.g., `PERM_SALES_INVOICE_CREATE`). The middleware resolves this constant against `$_SESSION['user_permissions']`.

**On failure:** Returns an HTTP 403 Forbidden response with a standardised "Access Denied" page. The user is not redirected to the login page — they remain authenticated but unauthorised for this specific resource.

**Data provided downstream:** Confirmed authorisation. The page handler receives the full request context and may proceed with data access and rendering.

---

## 3.3 TenantContext Injection

The `TenantContext` class is populated during the `EnsureTenantSelected` and `EnsureTenantActive` layers and registered as a singleton in the PHP-DI 7.0 container for the lifetime of the request. Every service in `src/Services/[Domain]/` receives `TenantContext` via constructor injection. The context exposes:

- `getTenantId()` — the authoritative `tenant_id` for all SQL queries.
- `getCurrency()` — the tenant's configured currency code (ISO 4217).
- `getTimezone()` — the tenant's timezone identifier.
- `getLocalisationProfile()` — the full localisation configuration object.
- `isModuleActive(string $moduleCode)` — returns `true` if the given module code is activated for this tenant.
- `getBranchId()` — the session-active branch identifier.

No service may construct or override a `TenantContext` from request parameters. The only authorised source is the session-validated middleware pipeline.
