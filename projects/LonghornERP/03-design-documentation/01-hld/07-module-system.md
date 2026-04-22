# Module System

## 7.1 Module Registry

The module system uses two database tables to manage the global module catalogue and per-tenant activation:

### `module_registry` Table

The `module_registry` table is the global catalogue of all modules available on the platform. It is seeded at deployment time and updated by Chwezi operators when new modules are released. Tenants cannot modify this table.

| Column | Type | Description |
|---|---|---|
| `code` | `VARCHAR(50) PK` | Unique module identifier (e.g., `HR_PAYROLL`). |
| `name` | `VARCHAR(100)` | Human-readable module name. |
| `description` | `TEXT` | Brief capability summary. |
| `is_core` | `TINYINT(1)` | `1` if the module is always active; `0` if it is an add-on. |
| `dependencies` | `JSON` | Array of module codes that must be active before this module can be activated. |
| `is_active` | `TINYINT(1)` | `1` if the module is available for activation on the platform. |

### `tenant_modules` Table

The `tenant_modules` table records which modules are active for each tenant.

| Column | Type | Description |
|---|---|---|
| `id` | `BIGINT UNSIGNED PK` | Auto-increment identifier. |
| `tenant_id` | `INT UNSIGNED FK` | References `tenants(id)`. |
| `module_code` | `VARCHAR(50) FK` | References `module_registry(code)`. |
| `activated_at` | `DATETIME` | Timestamp of activation. |
| `activated_by` | `INT UNSIGNED` | Super admin user who activated the module. |
| `is_active` | `TINYINT(1)` | `1` if currently active; `0` if deactivated. |

## 7.2 Core Modules

The following 6 modules are always active for every tenant and cannot be disabled:

| Module Name | Code |
|---|---|
| Accounting & General Ledger | `ACCOUNTING` |
| Inventory Management | `INVENTORY` |
| Sales | `SALES` |
| Procurement | `PROCUREMENT` |
| User Management & RBAC | `USER_MGMT` |
| Audit Log | `AUDIT` |

Core module status (`is_core = 1`) is enforced by the `requireModuleAccess()` function: if called for a core module code, the function always returns without redirecting, regardless of the `tenant_modules` table.

## 7.3 Add-On Modules

The following 13 add-on modules are available for per-tenant activation based on the tenant's subscription plan:

| Module Name | Code |
|---|---|
| Advanced Inventory | `ADV_INVENTORY` |
| Manufacturing | `MANUFACTURING` |
| HR & Payroll | `HR_PAYROLL` |
| Point of Sale | `POS` |
| Sales & CRM | `SALES_CRM` |
| Sales Agents & Commissions | `SALES_AGENTS` |
| Cooperative Procurement | `COOPERATIVE` |
| Project Management | `PROJECTS` |
| Strategy & Balanced Scorecard | `STRATEGY_BSC` |
| Asset Management | `ASSETS` |
| AI Intelligence | `AI_INTELLIGENCE` |
| Product Lifecycle Management | `PLM` |
| Transportation & Fleet Operations | `TRANSPORTATION` |

## 7.4 Module Activation Gate

Every page belonging to an add-on module shall include the following call as the first operation after the middleware pipeline:

```php
requireModuleAccess('MODULE_CODE');
```

The `requireModuleAccess()` function performs two checks in sequence:

1. Calls `TenantContext::isModuleActive($moduleCode)` - checks the `tenant_modules` table for an active record.
2. If no active record exists, redirects the user to the module upgrade page (`/public/billing/upgrade.php?module=MODULE_CODE`) and terminates execution.

The function shall be implemented as a standalone helper in `src/Platform/ModuleGate.php` and shall be available throughout the tenant workspace without additional imports.

## 7.5 Module Dependency Rules

Certain add-on modules depend on other modules being active before they can be activated. The dependency rules enforced at activation time are:

| Module | Dependency |
|---|---|
| `MANUFACTURING` | Requires `ADV_INVENTORY` to be active. |
| `COOPERATIVE` | Requires `INVENTORY` to be active (core - always satisfied). |
| `PLM` | No hard activation dependency; downstream publication targets depend on whichever operational modules the tenant has enabled. |
| `TRANSPORTATION` | Requires `SALES` and `INVENTORY` to be active (both core - always satisfied). Internal-fleet mode additionally requires `ASSETS` for vehicle reference data. |

*Note:* A formal dependency map covering all add-on modules shall still be maintained in the Super Admin Panel configuration. The rules above represent the confirmed dependencies that must be enforced at activation time.

## 7.6 Starter Plan Module Lock

Tenants on the Starter subscription plan (UGX 250,000/month) have access to the 6 core modules only. The `requireModuleAccess()` function will redirect Starter tenants to the upgrade page regardless of whether a `tenant_modules` record exists. The Starter plan restriction is enforced by the subscription plan evaluation logic within `TenantContext`, not by the absence of `tenant_modules` records.

## 7.7 Platform Services

In addition to the user-facing modules, the following platform services are always active and are not subject to the `requireModuleAccess()` gate:

| Service | Code | Description |
|---|---|---|
| Localisation Engine | `LOCALISATION` | Per-tenant configuration-driven localisation. |
| Mobile API | `MOBILE_API` | JWT-secured REST API for Android and iOS clients. |
| Integration Layer | `INTEGRATIONS` | Mobile money, government fiscal, and SMS gateway integrations. |
| Billing & Subscriptions | `BILLING` | Subscription plan management and tenant lifecycle. |
