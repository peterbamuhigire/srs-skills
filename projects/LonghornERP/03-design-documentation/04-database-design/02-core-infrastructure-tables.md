# Core Infrastructure Tables

The tables in this section form the platform foundation shared across all modules. They manage tenant identity, user authentication, role-based access control (RBAC), branch hierarchy, auditing, session management, billing, and module activation.

## `tenants`

Stores one record per subscriber organisation. This is the root of the multi-tenancy model; all other operational tables reference `tenants.id` via `tenant_id`.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `name` | VARCHAR(255) | NOT NULL | Legal or trading name of the tenant organisation. |
| `slug` | VARCHAR(100) | NOT NULL, UNIQUE | URL-safe identifier used in subdomain routing. |
| `status` | ENUM('trial','active','overdue','suspended','archived') | NOT NULL, DEFAULT 'trial' | Tenant lifecycle state. |
| `plan` | ENUM('starter','small_business','professional','business','enterprise') | NOT NULL | Subscription tier controlling available modules and seat limits. |
| `created_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Timestamp when the tenant record was first created. |

**Indexes:** PRIMARY (`id`), UNIQUE (`slug`).

---

## `users`

Stores authenticated user accounts scoped to a tenant. A user may belong to one branch and one role. The super-admin panel maintains its own separate user store.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `name` | VARCHAR(255) | NOT NULL | Full display name. |
| `email` | VARCHAR(255) | NOT NULL | Login credential; unique within a tenant. |
| `password_hash` | VARCHAR(255) | NOT NULL | bcrypt hash of the user's password. |
| `role_id` | BIGINT UNSIGNED | NOT NULL, FK → `roles.id` | The role assigned to this user. |
| `branch_id` | BIGINT UNSIGNED | NULL, FK → `branches.id` | The branch to which this user is restricted; NULL means all branches. |
| `status` | ENUM('active','inactive','locked') | NOT NULL, DEFAULT 'active' | Account state; locked after repeated failed login attempts. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `email`), (`tenant_id`, `status`), (`tenant_id`, `role_id`).

---

## `roles`

Defines named permission roles within a tenant. Roles are unlimited and fully custom per tenant.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `name` | VARCHAR(100) | NOT NULL | Human-readable role name (e.g., "Accounts Officer"). |
| `description` | TEXT | NULL | Optional explanation of the role's intended responsibilities. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `name`).

---

## `role_permissions`

Maps a role to a specific permission code and allowed action. The application evaluates this table on every protected request.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `role_id` | BIGINT UNSIGNED | NOT NULL, FK → `roles.id` | The role being granted the permission. |
| `permission_code` | VARCHAR(100) | NOT NULL | Dot-separated permission code (e.g., `invoices.create`). |
| `action` | ENUM('allow','deny') | NOT NULL, DEFAULT 'allow' | Explicit allow or deny; deny takes precedence if both are present. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `role_id`, `permission_code`).

---

## `branches`

Represents physical or logical business locations within a tenant organisation.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `name` | VARCHAR(255) | NOT NULL | Branch display name. |
| `address` | TEXT | NULL | Physical address of the branch. |
| `is_active` | TINYINT(1) | NOT NULL, DEFAULT 1 | 1 = active; 0 = deactivated. Deactivated branches are excluded from new transactions. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `is_active`).

---

## `audit_log`

Records every create, update, delete, and approval action across all modules. This table is INSERT-only; no UPDATE or DELETE operations are permitted by any application role or database user. Retention is 7 years, enforced by the platform archival job.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `user_id` | BIGINT UNSIGNED | NOT NULL | ID of the user who performed the action; denormalised to preserve history if the user record is later deactivated. |
| `module` | VARCHAR(50) | NOT NULL | Module code (e.g., `ACCOUNTING`, `INVENTORY`). |
| `action` | VARCHAR(50) | NOT NULL | Action type (e.g., `CREATE`, `UPDATE`, `DELETE`, `APPROVE`). |
| `record_table` | VARCHAR(100) | NOT NULL | Name of the table where the affected record lives. |
| `record_id` | BIGINT UNSIGNED | NOT NULL | Primary key of the affected record. |
| `old_values` | JSON | NULL | Serialised pre-change field values; NULL for CREATE actions. |
| `new_values` | JSON | NULL | Serialised post-change field values; NULL for DELETE actions. |
| `ip_address` | VARCHAR(45) | NOT NULL | IPv4 or IPv6 address of the request origin. |
| `created_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Timestamp of the event; indexed for time-range queries by auditors. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `created_at`), (`tenant_id`, `module`, `created_at`), (`tenant_id`, `record_table`, `record_id`).

**Constraint:** The database user account used by the PHP application will be granted INSERT-only privileges on `audit_log`. No UPDATE or DELETE grant will be issued.

---

## `sessions`

Stores active web session tokens. Mobile JWT sessions are stateless and are not stored here.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `user_id` | BIGINT UNSIGNED | NOT NULL, FK → `users.id` | The authenticated user. |
| `token_hash` | VARCHAR(255) | NOT NULL, UNIQUE | SHA-256 hash of the session token; the plaintext token lives only in the HttpOnly cookie. |
| `expires_at` | DATETIME | NOT NULL | Expiry timestamp; sessions past this value will be rejected and purged. |
| `ip_address` | VARCHAR(45) | NOT NULL | IP address at session creation. |
| `user_agent` | VARCHAR(500) | NULL | Browser user-agent string for anomaly detection. |

**Indexes:** PRIMARY (`id`), UNIQUE (`token_hash`), (`tenant_id`, `user_id`, `expires_at`).

---

## `subscriptions`

Records the active billing subscription for each tenant. One active subscription per tenant at any time.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `plan` | ENUM('starter','small_business','professional','business','enterprise') | NOT NULL | Active plan. |
| `status` | ENUM('trial','active','overdue','suspended','cancelled') | NOT NULL | Current billing state. |
| `billing_cycle` | ENUM('monthly','annual') | NOT NULL | Determines renewal frequency and discount application. |
| `start_date` | DATE | NOT NULL | Date the subscription period began. |
| `next_billing_date` | DATE | NOT NULL | Date the next invoice will be generated. |
| `amount_ugx` | DECIMAL(15,2) | NOT NULL | Amount in Ugandan Shillings (UGX) for the current cycle. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `status`).

---

## `tenant_modules`

Records which add-on modules have been activated for a tenant and when. Core modules do not require a record here; they are always available.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `module_code` | VARCHAR(50) | NOT NULL | Module code matching `module_registry.code`. |
| `activated_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Timestamp of activation. |
| `activated_by` | BIGINT UNSIGNED | NOT NULL | Super-admin user ID who activated the module. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `module_code`).

---

## `module_registry`

Canonical list of all modules known to the platform. Maintained by the super-admin panel; not editable by tenants.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `code` | VARCHAR(50) | NOT NULL, UNIQUE | System-wide module identifier (e.g., `HR_PAYROLL`). |
| `name` | VARCHAR(255) | NOT NULL | Human-readable module name. |
| `is_core` | TINYINT(1) | NOT NULL, DEFAULT 0 | 1 = core module always active; 0 = add-on requiring activation. |
| `dependencies` | JSON | NULL | Array of module codes that must be active before this module can be activated. |

**Indexes:** PRIMARY (`id`), UNIQUE (`code`).
