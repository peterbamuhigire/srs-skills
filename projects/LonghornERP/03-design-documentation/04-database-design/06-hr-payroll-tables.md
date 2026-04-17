# HR and Payroll Module Tables

The HR and Payroll (HR_PAYROLL) module is an add-on module activated per tenant. The tables below support the employee lifecycle, payroll processing, statutory deduction calculation, leave management, and attendance recording.

## `employees`

Master record for each employee. Holds employment identity, organisational placement, and current status.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `employee_number` | VARCHAR(30) | NOT NULL | System-generated unique employee identifier within the tenant. |
| `name` | VARCHAR(255) | NOT NULL | Employee full legal name. |
| `nin` | VARCHAR(20) | NULL | National Identification Number (NIN); required for statutory reporting in Uganda. |
| `branch_id` | BIGINT UNSIGNED | NOT NULL, FK → `branches.id` | Branch to which the employee is assigned. |
| `department_id` | BIGINT UNSIGNED | NULL | Department reference; links to a cost centre or organisational unit. |
| `job_title` | VARCHAR(100) | NULL | Current job title. |
| `hire_date` | DATE | NOT NULL | Date the employee commenced employment. |
| `salary_grade_id` | BIGINT UNSIGNED | NULL | Salary grade reference controlling base pay range. |
| `status` | ENUM('active','on_leave','terminated','suspended') | NOT NULL, DEFAULT 'active' | Employment status; terminated employees are excluded from payroll runs. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `employee_number`), (`tenant_id`, `status`), (`tenant_id`, `branch_id`, `status`).

---

## `payroll_elements`

Defines the earning, deduction, and statutory components used in payroll calculation. Each element carries a formula string evaluated by the Symfony Expression Language at run time.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `code` | VARCHAR(50) | NOT NULL | Unique element code within the tenant (e.g., `BASIC_SALARY`, `NSSF_EMP`). |
| `name` | VARCHAR(255) | NOT NULL | Human-readable element name. |
| `type` | ENUM('EARNING','DEDUCTION','STATUTORY') | NOT NULL | Element classification for payslip grouping and GL mapping. |
| `is_taxable` | TINYINT(1) | NOT NULL, DEFAULT 0 | 1 = this earning is included in the Pay As You Earn (PAYE) taxable income computation. |
| `formula` | TEXT | NULL | Symfony Expression Language formula; NULL for fixed-amount elements entered manually per employee. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `code`).

---

## `payroll_runs`

Header record for a payroll processing run covering a specific month and year.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `run_number` | VARCHAR(30) | NOT NULL | System-generated payroll run reference (e.g., `PAY-2026-04`). |
| `period_month` | TINYINT UNSIGNED | NOT NULL | Payroll month 1–12. |
| `period_year` | SMALLINT UNSIGNED | NOT NULL | Four-digit payroll year. |
| `status` | ENUM('draft','computed','approved','posted','paid') | NOT NULL, DEFAULT 'draft' | Run lifecycle state; GL posting occurs on transition to `posted`. |
| `run_date` | DATE | NOT NULL | Date the payroll run was initiated. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `run_number`), UNIQUE (`tenant_id`, `period_month`, `period_year`).

---

## `payslips`

Header record for each employee's payslip within a payroll run. Stores the computed summary totals.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `run_id` | BIGINT UNSIGNED | NOT NULL, FK → `payroll_runs.id` | Parent payroll run. |
| `employee_id` | BIGINT UNSIGNED | NOT NULL, FK → `employees.id` | The employee this payslip belongs to. |
| `gross_pay` | DECIMAL(15,4) | NOT NULL | Sum of all EARNING elements for the period. |
| `total_deductions` | DECIMAL(15,4) | NOT NULL | Sum of all DEDUCTION and STATUTORY elements for the period. |
| `net_pay` | DECIMAL(15,4) | NOT NULL | `gross_pay` − `total_deductions`. |
| `status` | ENUM('draft','approved','paid') | NOT NULL, DEFAULT 'draft' | Payslip confirmation state. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `run_id`, `employee_id`), (`tenant_id`, `employee_id`).

---

## `payslip_items`

Individual payroll element amounts on a payslip. One row per payroll element per payslip.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `payslip_id` | BIGINT UNSIGNED | NOT NULL, FK → `payslips.id` | Parent payslip. |
| `element_id` | BIGINT UNSIGNED | NOT NULL, FK → `payroll_elements.id` | The payroll element. |
| `amount` | DECIMAL(15,4) | NOT NULL | Computed or manually entered amount for this element on this payslip. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `payslip_id`), (`tenant_id`, `element_id`).

---

## `leave_types`

Defines the categories of leave available within the tenant, with entitlement and carry-forward rules.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `name` | VARCHAR(100) | NOT NULL | Leave type name (e.g., "Annual Leave", "Sick Leave"). |
| `days_per_year` | DECIMAL(5,1) | NOT NULL | Entitlement in working days per leave year. |
| `carry_forward` | TINYINT(1) | NOT NULL, DEFAULT 0 | 1 = unused days carry forward to the next leave year; 0 = days lapse at year end. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `name`).

---

## `leave_requests`

Records each employee leave application and its approval state.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `employee_id` | BIGINT UNSIGNED | NOT NULL, FK → `employees.id` | The employee requesting leave. |
| `leave_type_id` | BIGINT UNSIGNED | NOT NULL, FK → `leave_types.id` | Type of leave requested. |
| `start_date` | DATE | NOT NULL | First day of the leave period. |
| `end_date` | DATE | NOT NULL | Last day of the leave period (inclusive). |
| `status` | ENUM('pending','approved','rejected','cancelled') | NOT NULL, DEFAULT 'pending' | Approval lifecycle state. |
| `approved_by` | BIGINT UNSIGNED | NULL, FK → `users.id` | User who approved or rejected the request; NULL while pending. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `employee_id`, `status`), (`tenant_id`, `status`).

---

## `employee_attendance`

Records each employee's daily attendance event. Attendance may originate from a biometric device, mobile application check-in, or manual entry by an HR officer.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `employee_id` | BIGINT UNSIGNED | NOT NULL, FK → `employees.id` | The employee whose attendance is recorded. |
| `date` | DATE | NOT NULL | The working date. |
| `check_in` | TIME | NULL | Time of first clock-in for the day; NULL if not yet recorded. |
| `check_out` | TIME | NULL | Time of last clock-out for the day; NULL if employee has not yet departed. |
| `source` | ENUM('BIOMETRIC','MOBILE','MANUAL') | NOT NULL | Origin of the attendance record for audit trail purposes. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `employee_id`, `date`), (`tenant_id`, `date`).
