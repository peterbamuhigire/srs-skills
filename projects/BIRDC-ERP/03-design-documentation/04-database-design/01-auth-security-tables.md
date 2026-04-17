## Section 1 — Authentication & Security Tables

---

### tbl_users

**Purpose:** Stores all system user accounts — BIRDC/PIBID staff, IT administrators, and field sales agents.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `user_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | User primary key |
| `username` | `VARCHAR(100)` | NOT NULL, UNIQUE | Login username |
| `email` | `VARCHAR(255)` | NOT NULL, UNIQUE | Email address |
| `password_hash` | `VARCHAR(255)` | NOT NULL | Argon2id password hash |
| `full_name` | `VARCHAR(255)` | NOT NULL | Full name |
| `phone` | `VARCHAR(30)` | NULL | Phone number |
| `role_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_roles | Primary role |
| `agent_id` | `INT UNSIGNED` | NULL, FK → tbl_agents | Linked agent (NULL for non-agent users) |
| `employee_id` | `INT UNSIGNED` | NULL, FK → tbl_employees | Linked employee (NULL for non-staff users) |
| `status` | `ENUM('active','suspended','locked')` | NOT NULL DEFAULT 'active' | Account status |
| `failed_login_count` | `TINYINT UNSIGNED` | NOT NULL DEFAULT 0 | Consecutive failed login attempts |
| `locked_until` | `DATETIME` | NULL | Account lockout expiry |
| `totp_secret` | `VARCHAR(64)` | NULL | TOTP secret key (encrypted at rest) |
| `totp_enabled` | `TINYINT(1)` | NOT NULL DEFAULT 0 | TOTP 2FA active flag |
| `last_login_at` | `DATETIME` | NULL | Last successful login |
| `photo_url` | `VARCHAR(500)` | NULL | Profile photo URL |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | Row created timestamp |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Row updated timestamp |

**Relationships:** `role_id` → `tbl_roles.role_id`, `agent_id` → `tbl_agents.agent_id`, `employee_id` → `tbl_employees.employee_id`

**Indexes:** `UNIQUE(username)`, `UNIQUE(email)`, `INDEX(role_id)`, `INDEX(status)`

```sql
CREATE TABLE tbl_users (
  user_id       INT UNSIGNED NOT NULL AUTO_INCREMENT,
  username      VARCHAR(100) NOT NULL,
  email         VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  full_name     VARCHAR(255) NOT NULL,
  phone         VARCHAR(30)  NULL,
  role_id       INT UNSIGNED NOT NULL,
  agent_id      INT UNSIGNED NULL,
  employee_id   INT UNSIGNED NULL,
  status        ENUM('active','suspended','locked') NOT NULL DEFAULT 'active',
  failed_login_count TINYINT UNSIGNED NOT NULL DEFAULT 0,
  locked_until  DATETIME     NULL,
  totp_secret   VARCHAR(64)  NULL,
  totp_enabled  TINYINT(1)   NOT NULL DEFAULT 0,
  last_login_at DATETIME     NULL,
  photo_url     VARCHAR(500) NULL,
  created_at    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id),
  UNIQUE KEY uq_users_username (username),
  UNIQUE KEY uq_users_email (email),
  KEY idx_users_role (role_id),
  KEY idx_users_status (status),
  CONSTRAINT fk_users_role FOREIGN KEY (role_id) REFERENCES tbl_roles (role_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_roles

**Purpose:** Defines the role taxonomy for RBAC — 8-layer authorisation system.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `role_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Role primary key |
| `role_code` | `VARCHAR(50)` | NOT NULL, UNIQUE | Machine-readable role code (e.g., `SALES_AGENT`) |
| `role_name` | `VARCHAR(100)` | NOT NULL | Human-readable role name |
| `description` | `TEXT` | NULL | Role description |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(role_code)`

```sql
CREATE TABLE tbl_roles (
  role_id    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  role_code  VARCHAR(50)  NOT NULL,
  role_name  VARCHAR(100) NOT NULL,
  description TEXT         NULL,
  is_active  TINYINT(1)   NOT NULL DEFAULT 1,
  created_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (role_id),
  UNIQUE KEY uq_roles_code (role_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_permissions

**Purpose:** Defines individual permission codes that can be assigned to roles.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `permission_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Permission primary key |
| `permission_code` | `VARCHAR(100)` | NOT NULL, UNIQUE | Permission code (e.g., `invoices.confirm`, `agents.verify_remittance`) |
| `module` | `VARCHAR(50)` | NOT NULL | Module this permission belongs to |
| `description` | `VARCHAR(255)` | NULL | Human-readable description |

**Junction table:** `tbl_role_permissions(role_id, permission_id)` — many-to-many.

---

### tbl_user_sessions

**Purpose:** Tracks active JWT refresh tokens per user and device. Enables logout-all and remote session revocation.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `session_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Session primary key |
| `user_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | Session owner |
| `refresh_token_hash` | `CHAR(64)` | NOT NULL, UNIQUE | SHA-256 hash of the refresh token |
| `device_id` | `VARCHAR(255)` | NOT NULL | Android device identifier |
| `device_name` | `VARCHAR(255)` | NULL | Human-readable device name |
| `ip_address` | `VARCHAR(45)` | NULL | IP address at session creation |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | Session start |
| `expires_at` | `DATETIME` | NOT NULL | Refresh token expiry (30 days) |
| `revoked_at` | `DATETIME` | NULL | Set on logout or admin revocation |

**Indexes:** `UNIQUE(refresh_token_hash)`, `INDEX(user_id)`, `INDEX(expires_at)`

```sql
CREATE TABLE tbl_user_sessions (
  session_id         INT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id            INT UNSIGNED NOT NULL,
  refresh_token_hash CHAR(64)     NOT NULL,
  device_id          VARCHAR(255) NOT NULL,
  device_name        VARCHAR(255) NULL,
  ip_address         VARCHAR(45)  NULL,
  created_at         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  expires_at         DATETIME     NOT NULL,
  revoked_at         DATETIME     NULL,
  PRIMARY KEY (session_id),
  UNIQUE KEY uq_sessions_token (refresh_token_hash),
  KEY idx_sessions_user (user_id),
  KEY idx_sessions_expiry (expires_at),
  CONSTRAINT fk_sessions_user FOREIGN KEY (user_id) REFERENCES tbl_users (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_audit_log

**Purpose:** Immutable system-wide audit trail. Every create, update, delete, approval, void, login, and logout is recorded here. 7-year retention per DC-003. The `hash_chain_prev` column provides a tamper-evident chain for audit log entries (mirrors the GL hash chain concept from BR-013).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `log_id` | `BIGINT UNSIGNED` | PK, AUTO_INCREMENT | Log entry primary key (BIGINT — high volume) |
| `actor_user_id` | `INT UNSIGNED` | NULL, FK → tbl_users | User who performed the action (NULL for system actions) |
| `action` | `VARCHAR(50)` | NOT NULL | Action type: `create`, `update`, `delete`, `approve`, `void`, `login`, `logout` |
| `table_name` | `VARCHAR(100)` | NOT NULL | Affected table |
| `record_id` | `INT UNSIGNED` | NULL | Primary key of the affected record |
| `old_values` | `JSON` | NULL | Snapshot of the row before the change |
| `new_values` | `JSON` | NULL | Snapshot of the row after the change |
| `ip_address` | `VARCHAR(45)` | NULL | Actor's IP address |
| `user_agent` | `VARCHAR(500)` | NULL | Client user agent |
| `hash_chain_prev` | `CHAR(64)` | NULL | SHA-256 hash of the previous audit log entry — tamper detection |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | Immutable creation timestamp |

**Indexes:** `INDEX(actor_user_id)`, `INDEX(table_name, record_id)`, `INDEX(created_at)`, `INDEX(action)`

**Important:** No `UPDATE` or `DELETE` privilege is granted to the application database user on this table. Rows are insert-only.

```sql
CREATE TABLE tbl_audit_log (
  log_id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  actor_user_id   INT UNSIGNED    NULL,
  action          VARCHAR(50)     NOT NULL,
  table_name      VARCHAR(100)    NOT NULL,
  record_id       INT UNSIGNED    NULL,
  old_values      JSON            NULL,
  new_values      JSON            NULL,
  ip_address      VARCHAR(45)     NULL,
  user_agent      VARCHAR(500)    NULL,
  hash_chain_prev CHAR(64)        NULL,
  created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (log_id),
  KEY idx_audit_actor (actor_user_id),
  KEY idx_audit_table_record (table_name, record_id),
  KEY idx_audit_created (created_at),
  KEY idx_audit_action (action)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---
