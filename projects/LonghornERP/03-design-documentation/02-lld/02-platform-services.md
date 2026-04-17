# Platform Services — Low-Level Design

## Overview

Platform services are tenant-agnostic infrastructure components shared by all modules. They are registered in the PHP-DI container at bootstrap time and injected into module services via constructor injection. No module service may instantiate a platform service directly with `new`.

---

## RouterService

**Namespace:** `App\Platform\Routing`

`RouterService` maps incoming HTTP request paths to controller class names and action methods. It supports three panel prefixes and delegates to the appropriate controller.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `register(string $method, string $pattern, string $controller, string $action): void` | HTTP verb, URL pattern with named segments, fully-qualified controller class, action method name | `void` | Registers one route entry in the internal route table. |
| `dispatch(string $method, string $uri): mixed` | HTTP verb, request URI | Controller action return value | Matches the URI against registered routes and invokes the matched controller action. Throws `RouteNotFoundException` when no match exists. |
| `redirect(string $uri, int $status = 302): void` | Target URI, HTTP status code | `void` | Emits a Location header and halts execution. |

**Panel prefixes:**

- `/public/` — tenant workspace (`TenantPanel`)
- `/public/superadmin/` — platform administration (`SuperAdminPanel`)
- `/public/portal/` — self-service portal (`PortalPanel`)

Each panel prefix maps to a dedicated controller namespace: `App\Controllers\Tenant`, `App\Controllers\SuperAdmin`, `App\Controllers\Portal`.

---

## MiddlewareChain

**Namespace:** `App\Platform\Middleware`

The middleware chain executes in the fixed order shown below. Each middleware class implements `MiddlewareInterface` and exposes a single `handle()` method. If a check fails the middleware emits a redirect or JSON error response and halts the chain.

### EnsureAuthenticated

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `handle(Request $request, callable $next): Response` | Current request object, next middleware callable | `Response` | Verifies that `$_SESSION['user_id']` is set and that the session has not expired. Redirects to the login page on failure. |

### EnsureTenantSelected

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `handle(Request $request, callable $next): Response` | Current request object, next middleware callable | `Response` | Verifies that `$_SESSION['tenant_id']` is set. Redirects to the tenant-selection screen on failure. |

### EnsureTenantActive

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `handle(Request $request, callable $next): Response` | Current request object, next middleware callable | `Response` | Calls `TenantService::getActiveTenant(int $tenantId)`. If the tenant status is not `active`, redirects to a suspension notice page. |

### EnsureBranchSelected

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `handle(Request $request, callable $next): Response` | Current request object, next middleware callable | `Response` | Verifies that `$_SESSION['branch_id']` is set. Redirects to the branch-selection screen on failure. |

### RequirePermission

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `handle(Request $request, callable $next): Response` | Current request object, next middleware callable | `Response` | Reads the required permission code from the route metadata. Queries `role_permissions` joined to `user_roles` for the current `user_id` and `tenant_id`. Returns HTTP 403 if the permission code is absent. |

**Chain execution order:** `EnsureAuthenticated → EnsureTenantSelected → EnsureTenantActive → EnsureBranchSelected → RequirePermission`

---

## ContainerFactory

**Namespace:** `App\Platform\DI`

`ContainerFactory` bootstraps the PHP-DI 7.0 container and returns a configured `DI\Container` instance. It is called once in `public/index.php` and the resulting container is stored in a request-scoped registry.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `build(): Container` | None | `DI\Container` | Reads `config/container.php`, registers all service bindings, and compiles the container if a compiled container path is configured. |

**Key bindings in `config/container.php`:**

- `PDO` — singleton; constructed from `config/database.php` credentials; `PDO::ATTR_ERRMODE` set to `PDO::ERRMODE_EXCEPTION`
- `SessionService` — singleton
- `AuditService` — singleton; receives `PDO` and `SessionService`
- `TenantService` — singleton; receives `PDO`
- `ModuleRegistry` — singleton; receives `PDO`
- All module services — per-request; receive `PDO`, `SessionService`, `AuditService`, and any module-specific dependencies

---

## SessionService

**Namespace:** `App\Platform\Session`

`SessionService` wraps PHP's native session functions. All session reads and writes in the application go through this service; no module may access `$_SESSION` directly.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `get(string $key): mixed` | Session key | Session value or `null` | Returns the value stored at `$key`, or `null` if absent. |
| `set(string $key, mixed $value): void` | Session key, value | `void` | Stores `$value` at `$key`. |
| `destroy(): void` | None | `void` | Calls `session_destroy()` and clears the `$_SESSION` superglobal. |
| `getTenantId(): int` | None | `int` | Returns `$_SESSION['tenant_id']`. Throws `SessionException` if not set. |
| `getBranchId(): int` | None | `int` | Returns `$_SESSION['branch_id']`. Throws `SessionException` if not set. |
| `getUserId(): int` | None | `int` | Returns `$_SESSION['user_id']`. Throws `SessionException` if not set. |

---

## AuditService

**Namespace:** `App\Platform\Audit`

`AuditService` writes immutable audit records to the `audit_logs` table. Records are INSERT-only; the table carries no UPDATE or DELETE grants for the application database user. The service is called inside the same database transaction as the state-changing write it records.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `log(string $action, string $entity, int $entityId, array $before, array $after): void` | Action verb (`CREATE`, `UPDATE`, `DELETE`, `POST`, `VOID`), entity name (e.g., `Invoice`), primary key of the affected row, state snapshot before the change (empty array for creates), state snapshot after the change (empty array for deletes) | `void` | Serialises `$before` and `$after` to JSON and inserts one row into `audit_logs` with `user_id`, `tenant_id`, `branch_id`, `ip_address`, and `created_at` sourced from `SessionService`. |

**Table written:** `audit_logs`

**Columns written:** `tenant_id`, `user_id`, `branch_id`, `action`, `entity`, `entity_id`, `before_state` (JSON), `after_state` (JSON), `ip_address`, `created_at`

`AuditService` has no read methods. Audit reporting is handled by a dedicated read-only `AuditReportService`.

---

## TenantService

**Namespace:** `App\Platform\Tenant`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `getActiveTenant(int $tenantId): array` | Tenant primary key | Tenant row as associative array | Reads one row from `tenants` by primary key. Throws `TenantNotFoundException` if the row is absent. |
| `suspendTenant(int $tenantId, string $reason): void` | Tenant primary key, free-text reason | `void` | Sets `tenants.status = 'suspended'` and writes `suspended_reason` and `suspended_at`. Logs to `AuditService`. |
| `reactivateTenant(int $tenantId): void` | Tenant primary key | `void` | Sets `tenants.status = 'active'` and clears `suspended_reason`. Logs to `AuditService`. |

**Tables read/written:** `tenants`

---

## ModuleRegistry

**Namespace:** `App\Platform\Module`

`ModuleRegistry` controls which add-on modules are active for a given tenant. Module availability gates are checked at controller dispatch time via this service.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `isActive(string $moduleCode, int $tenantId): bool` | Module code constant (e.g., `MANUFACTURING`), tenant primary key | `bool` | Returns `true` if a row exists in `tenant_modules` where `module_code = :moduleCode AND tenant_id = :tenantId AND status = 'active'`. |
| `activate(string $moduleCode, int $tenantId): void` | Module code, tenant primary key | `void` | Inserts or updates a row in `tenant_modules` setting `status = 'active'` and `activated_at = NOW()`. Logs to `AuditService`. |
| `deactivate(string $moduleCode, int $tenantId): void` | Module code, tenant primary key | `void` | Sets `tenant_modules.status = 'inactive'` for the matching row. Logs to `AuditService`. |

**Tables read/written:** `tenant_modules`
