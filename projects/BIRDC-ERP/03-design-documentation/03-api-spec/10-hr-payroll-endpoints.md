## Section 9 — HR & Payroll Endpoints

These endpoints serve the HR Self-Service App and Factory Floor App. Leave management, payslips, and attendance records are exposed here. Biometric attendance from ZKTeco devices is authoritative per BR-016.

---

### 9.1 GET /hr/employees/{employee_id}

**Description:** Retrieve the full employee profile.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `STAFF` (own profile only), `HR_OFFICER`, `PAYROLL_OFFICER`, `DIRECTOR`

**Path parameters:** `employee_id` — integer

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `employee_id` | `integer` | Employee primary key |
| `employee_number` | `string` | Staff number |
| `full_name` | `string` | Full name |
| `nin` | `string` | National Identification Number |
| `department` | `string` | Department name |
| `job_title` | `string` | Job title |
| `pay_scale` | `string` | `government` (PIBID) or `commercial` (BIRDC) |
| `contract_type` | `string` | `permanent`, `contract`, `casual` |
| `hire_date` | `string` | ISO 8601 date |
| `mobile_money_number` | `string\|null` | For casual worker salary disbursements |
| `leave_balance` | `object` | Leave days remaining per leave type |

---

### 9.2 POST /hr/leave/apply

**Description:** Submit a leave application. The application routes to the employee's line manager for approval.

**Auth required:** JWT Bearer

**RBAC roles permitted:** All authenticated staff (`STAFF` and above)

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `leave_type_id` | `integer` | Required | Type of leave (annual, sick, maternity, paternity, etc.) |
| `start_date` | `string` | Required, ISO 8601 date | Leave start date |
| `end_date` | `string` | Required, ISO 8601 date | Leave end date (inclusive) |
| `reason` | `string` | Optional, max 500 | Reason for leave |
| `supporting_doc_url` | `string` | Optional | URL to uploaded medical certificate or other document |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `leave_request_id` | `integer` | Leave application primary key |
| `leave_request_number` | `string` | Reference number |
| `days_requested` | `number` | Calculated leave days (excluding weekends and public holidays) |
| `leave_balance_before` | `number` | Available days before this application |
| `status` | `string` | `"pending_approval"` |

---

### 9.3 GET /hr/leave/balance

**Description:** Retrieve the authenticated employee's current leave balance per leave type.

**Auth required:** JWT Bearer

**RBAC roles permitted:** All authenticated staff

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `employee_id` | `integer` | Employee primary key |
| `balances` | `array` | Leave balance per type |
| `balances[].leave_type` | `string` | Leave type name (e.g., Annual Leave) |
| `balances[].entitlement_days` | `number` | Annual entitlement |
| `balances[].taken_days` | `number` | Days taken this year |
| `balances[].pending_days` | `number` | Days in pending applications |
| `balances[].available_days` | `number` | Remaining days |

---

### 9.4 GET /hr/payroll/payslips/{employee_id}

**Description:** Retrieve a list of the employee's payslips. Each payslip is downloadable as a PDF.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `STAFF` (own payslips only), `HR_OFFICER`, `PAYROLL_OFFICER`

**Query parameters:** `year` (integer, filter by year), `month` (integer, 1–12).

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `payslips` | `array` | List of payslip records |
| `payslips[].payroll_run_id` | `integer` | Payroll run primary key |
| `payslips[].pay_period` | `string` | Month/year (e.g., `March 2026`) |
| `payslips[].gross_pay` | `number` | Gross salary (UGX) |
| `payslips[].total_deductions` | `number` | Total deductions (PAYE, NSSF, LST, loans) |
| `payslips[].net_pay` | `number` | Net take-home pay (UGX) |
| `payslips[].pdf_url` | `string` | URL to downloadable payslip PDF |
| `payslips[].is_locked` | `boolean` | `true` if payroll run is approved and locked (BR-010) |

---

### 9.5 POST /hr/attendance

**Description:** Submit a manual attendance record. Only permitted when the ZKTeco biometric device is offline (BR-016). Requires Finance Manager approval and is flagged for later reconciliation with biometric data.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `HR_OFFICER`, `PRODUCTION_SUPERVISOR`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `employee_id` | `integer` | Required | Employee whose attendance is being recorded |
| `attendance_date` | `string` | Required, ISO 8601 date | Date of attendance |
| `check_in` | `string` | Required, ISO 8601 datetime | Check-in time |
| `check_out` | `string` | Optional, ISO 8601 datetime | Check-out time |
| `reason_for_manual` | `string` | Required, min 10 | Justification for manual entry (biometric device offline) |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `attendance_id` | `integer` | Attendance record primary key |
| `source` | `string` | `"manual"` |
| `status` | `string` | `"pending_approval"` — requires Finance Manager approval (BR-016) |

---

### 9.6 GET /hr/attendance/{employee_id}

**Description:** Retrieve attendance records for an employee. Shows both biometric (authoritative) and manual records with source flags.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `STAFF` (own records only), `HR_OFFICER`, `PRODUCTION_SUPERVISOR`

**Query parameters:** `date_from`, `date_to`, `source` (`biometric`, `manual`, `all`).

**Response schema (200 OK):** Paginated list with `attendance_date`, `check_in`, `check_out`, `hours_worked`, `source`, `status`.

---

### 9.7 GET /hr/leave/requests

**Description:** Retrieve leave requests for review (manager view) or history (employee view).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `STAFF` (own requests only), `HR_OFFICER`, `DIRECTOR`

**Query parameters:** `status` (`pending_approval`, `approved`, `rejected`), `employee_id` (HR/Director only), `date_from`, `date_to`.

**Response schema (200 OK):** Paginated list with `leave_request_number`, `employee_name`, `leave_type`, `start_date`, `end_date`, `days_requested`, `status`.

---

### 9.8 GET /hr/payroll/runs

**Description:** Retrieve payroll run history. Used by Payroll Officer and Finance Manager.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PAYROLL_OFFICER`, `FINANCE_MANAGER`, `FINANCE_DIRECTOR`

**Query parameters:** `year`, `month`, `status` (`draft`, `pending_approval`, `approved`, `locked`).

**Response schema (200 OK):** Paginated list with `run_id`, `pay_period`, `employee_count`, `total_gross`, `total_deductions`, `total_net`, `status`, `approved_by`, `approved_at`.

---
