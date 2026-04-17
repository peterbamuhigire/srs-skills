## Section 10 — Reports & System Endpoints

These endpoints cover scheduled report generation, system health monitoring, and administrative operations. They serve the Executive Dashboard App, the web admin panel, and CI/CD health checks.

---

### 10.1 POST /reports/generate

**Description:** Trigger on-demand generation of a named report. Reports are generated asynchronously and a download URL is returned when complete. Used by the Executive Dashboard App and the web scheduling engine.

**Auth required:** JWT Bearer

**RBAC roles permitted:** Varies by report type — see `required_role` in response.

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `report_code` | `string` | Required | Report identifier (e.g., `trial_balance`, `agent_performance`, `budget_vs_actual`, `payslip_batch`, `farmer_payment_schedule`) |
| `parameters` | `object` | Conditional | Report-specific parameters (date ranges, filters, modes) |
| `format` | `string` | Required | `pdf`, `xlsx`, or `csv` |
| `email_to` | `string[]` | Optional | Email recipients for automatic delivery |

**Response schema (202 Accepted):**

| Field | Type | Description |
|---|---|---|
| `job_id` | `string` | Async job identifier |
| `status` | `string` | `"queued"` |
| `estimated_seconds` | `integer` | Estimated generation time |
| `poll_url` | `string` | URL to poll for completion status |

---

### 10.2 GET /reports/jobs/{job_id}

**Description:** Poll the status of an asynchronous report generation job.

**Auth required:** JWT Bearer

**RBAC roles permitted:** The user who initiated the job (or IT Admin).

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `job_id` | `string` | Job identifier |
| `status` | `string` | `"queued"`, `"processing"`, `"completed"`, `"failed"` |
| `download_url` | `string\|null` | Available when status is `"completed"` |
| `expires_at` | `string\|null` | ISO 8601 datetime when the download URL expires |
| `error` | `string\|null` | Error description if `status = "failed"` |

---

### 10.3 GET /system/health

**Description:** Return the system health status — database connectivity, queue depth, disk usage, and active sessions. Used by uptime monitoring tools and the web admin dashboard.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `IT_ADMIN`

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `status` | `string` | `"healthy"`, `"degraded"`, or `"down"` |
| `database` | `object` | `connected` (boolean), `response_ms` (integer), `slow_query_count` (integer — last 24h) |
| `queue` | `object` | `depth` (integer — pending jobs), `failed_jobs` (integer — last 24h) |
| `disk` | `object` | `used_gb` (number), `total_gb` (number), `usage_pct` (number) |
| `active_sessions` | `integer` | Current authenticated API sessions |
| `efris_queue` | `object` | `pending` (integer), `failed` (integer) — EFRIS submission queue status |
| `uptime_seconds` | `integer` | Server uptime since last restart |
| `checked_at` | `string` | ISO 8601 datetime of health check |

---

### 10.4 GET /system/audit-log

**Description:** Retrieve the system-wide audit log. Every create, update, delete, and status change is logged with actor, IP address, timestamp, old values, and new values.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `IT_ADMIN`, `FINANCE_DIRECTOR`

**Query parameters:** `user_id`, `action` (`create`, `update`, `delete`, `login`, `logout`, `approve`, `void`), `table_name`, `date_from`, `date_to`, `ip_address`.

**Response schema (200 OK):** Paginated log with `log_id`, `actor_name`, `actor_role`, `action`, `table_name`, `record_id`, `old_values` (JSON), `new_values` (JSON), `ip_address`, `timestamp`.

---

### 10.5 POST /system/efris/retry

**Description:** Manually trigger a retry for failed EFRIS submissions. Normally retried automatically up to 3 times; this endpoint allows the Finance Manager to force an immediate retry or mark a record as permanently failed.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_MANAGER`, `IT_ADMIN`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `efris_queue_ids` | `integer[]` | Required, min 1 | IDs of failed EFRIS queue records to retry |
| `action` | `string` | Required | `retry` or `mark_failed` |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `processed` | `integer` | Number of records processed |
| `retried` | `integer` | Number queued for retry |
| `marked_failed` | `integer` | Number marked permanently failed |

---
