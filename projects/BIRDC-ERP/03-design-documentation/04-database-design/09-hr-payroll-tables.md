## Section 9 — HR & Payroll Tables

---

### tbl_employees

**Purpose:** Employee master record for all BIRDC and PIBID staff (150+ employees). Supports both government pay scales (PIBID) and commercial pay scales (BIRDC).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `employee_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Employee primary key |
| `employee_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Staff number |
| `user_id` | `INT UNSIGNED` | NULL, UNIQUE, FK → tbl_users | Linked user account (NULL for workers without system access) |
| `full_name` | `VARCHAR(255)` | NOT NULL | Full name |
| `nin` | `VARCHAR(20)` | NOT NULL, UNIQUE | Uganda National Identification Number |
| `date_of_birth` | `DATE` | NULL | Date of birth |
| `gender` | `ENUM('male','female','other')` | NULL | Gender |
| `phone` | `VARCHAR(30)` | NULL | Phone |
| `email` | `VARCHAR(255)` | NULL | Email |
| `department_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_departments | Department |
| `job_title` | `VARCHAR(100)` | NOT NULL | Job title |
| `job_grade` | `VARCHAR(30)` | NULL | Pay grade (government or commercial scale) |
| `pay_scale` | `ENUM('government','commercial')` | NOT NULL | PIBID government or BIRDC commercial |
| `contract_type` | `ENUM('permanent','contract','casual')` | NOT NULL | Contract type |
| `hire_date` | `DATE` | NOT NULL | Employment start date |
| `termination_date` | `DATE` | NULL | Employment end date |
| `mobile_money_number` | `VARCHAR(30)` | NULL | For casual worker mobile money salary |
| `bank_account_number` | `VARCHAR(30)` | NULL | Bank account for salary credit |
| `bank_name` | `VARCHAR(100)` | NULL | Bank name |
| `status` | `ENUM('active','on_leave','suspended','terminated')` | NOT NULL DEFAULT 'active' | Employment status |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(employee_number)`, `UNIQUE(nin)`, `INDEX(department_id)`, `INDEX(status)`, `INDEX(contract_type)`

```sql
CREATE TABLE tbl_employees (
  employee_id        INT UNSIGNED NOT NULL AUTO_INCREMENT,
  employee_number    VARCHAR(20)  NOT NULL,
  user_id            INT UNSIGNED NULL,
  full_name          VARCHAR(255) NOT NULL,
  nin                VARCHAR(20)  NOT NULL,
  date_of_birth      DATE         NULL,
  gender             ENUM('male','female','other') NULL,
  phone              VARCHAR(30)  NULL,
  email              VARCHAR(255) NULL,
  department_id      INT UNSIGNED NOT NULL,
  job_title          VARCHAR(100) NOT NULL,
  job_grade          VARCHAR(30)  NULL,
  pay_scale          ENUM('government','commercial') NOT NULL,
  contract_type      ENUM('permanent','contract','casual') NOT NULL,
  hire_date          DATE         NOT NULL,
  termination_date   DATE         NULL,
  mobile_money_number VARCHAR(30) NULL,
  bank_account_number VARCHAR(30) NULL,
  bank_name          VARCHAR(100) NULL,
  status             ENUM('active','on_leave','suspended','terminated') NOT NULL DEFAULT 'active',
  created_at         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (employee_id),
  UNIQUE KEY uq_employees_number (employee_number),
  UNIQUE KEY uq_employees_nin (nin),
  KEY idx_employees_department (department_id),
  KEY idx_employees_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_leave_types

**Purpose:** Configurable leave type definitions — annual, sick, maternity, paternity, compassionate, study, unpaid.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `leave_type_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Leave type primary key |
| `type_name` | `VARCHAR(50)` | NOT NULL, UNIQUE | Leave type name |
| `annual_entitlement_days` | `TINYINT UNSIGNED` | NOT NULL | Days per year |
| `requires_documentation` | `TINYINT(1)` | NOT NULL DEFAULT 0 | 1 = medical cert or other doc required |
| `is_paid` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Paid or unpaid |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |

---

### tbl_leave_requests

**Purpose:** Employee leave applications with approval workflow.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `request_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Leave request primary key |
| `request_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Reference number |
| `employee_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_employees | Applicant |
| `leave_type_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_leave_types | Leave type |
| `start_date` | `DATE` | NOT NULL | Leave start |
| `end_date` | `DATE` | NOT NULL | Leave end (inclusive) |
| `days_requested` | `DECIMAL(4,1)` | NOT NULL | Calculated working days |
| `status` | `ENUM('pending_approval','approved','rejected','cancelled')` | NOT NULL DEFAULT 'pending_approval' | Status |
| `approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Approver |
| `approved_at` | `DATETIME` | NULL | Approval timestamp |
| `reason` | `TEXT` | NULL | Reason |
| `supporting_doc_url` | `VARCHAR(500)` | NULL | Document URL |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_attendance

**Purpose:** Employee attendance records. `source` column distinguishes biometric (authoritative per BR-016) from manual entries.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `attendance_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Attendance primary key |
| `employee_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_employees | Employee |
| `attendance_date` | `DATE` | NOT NULL | Date |
| `check_in` | `DATETIME` | NOT NULL | Check-in time |
| `check_out` | `DATETIME` | NULL | Check-out time |
| `hours_worked` | `DECIMAL(4,2)` | NULL | Calculated hours |
| `source` | `ENUM('biometric','manual')` | NOT NULL DEFAULT 'biometric' | BR-016: biometric is authoritative |
| `status` | `ENUM('approved','pending_approval','rejected')` | NOT NULL DEFAULT 'approved' | Manual entries require approval |
| `reason_for_manual` | `TEXT` | NULL | Required for manual entries (BR-016) |
| `approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Finance Manager approval for manual |
| `device_serial` | `VARCHAR(50)` | NULL | ZKTeco device serial number |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `INDEX(employee_id, attendance_date)`, `INDEX(source)`, `UNIQUE(employee_id, attendance_date, source)` — prevents duplicate biometric import.

---

### tbl_payroll_runs

**Purpose:** Payroll run header. Once the Finance Manager approves and locks a run, no modification is permitted (BR-010).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `run_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Payroll run primary key |
| `pay_period_year` | `SMALLINT UNSIGNED` | NOT NULL | Year |
| `pay_period_month` | `TINYINT UNSIGNED` | NOT NULL | Month (1–12) |
| `pay_scale` | `ENUM('government','commercial','all')` | NOT NULL | Which employees included |
| `total_gross` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Total gross pay (UGX) |
| `total_paye` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Total PAYE deducted |
| `total_nssf_employee` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Employee NSSF (5%) |
| `total_nssf_employer` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Employer NSSF (10%) |
| `total_lst` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Total LST deducted |
| `total_deductions` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | All deductions combined |
| `total_net_pay` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Total net pay (UGX) |
| `employee_count` | `INT UNSIGNED` | NOT NULL DEFAULT 0 | Employees in run |
| `status` | `ENUM('draft','pending_approval','approved','locked')` | NOT NULL DEFAULT 'draft' | BR-010: locked = immutable |
| `approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Finance Manager |
| `approved_at` | `DATETIME` | NULL | Lock timestamp — BR-010 |
| `gl_journal_id` | `INT UNSIGNED` | NULL, FK → tbl_journals | Auto-posted payroll GL journal |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Note (BR-010):** A database trigger enforces that `status = 'locked'` rows cannot be updated. Any attempt to UPDATE a locked payroll run returns an error.

---

### tbl_payroll_lines

**Purpose:** Per-employee gross-to-net calculation within a payroll run.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `line_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Line primary key |
| `run_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_payroll_runs | Parent run |
| `employee_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_employees | Employee |
| `gross_pay` | `DECIMAL(18,4)` | NOT NULL | Gross salary |
| `paye` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | PAYE withheld |
| `nssf_employee` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Employee NSSF 5% |
| `nssf_employer` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Employer NSSF 10% |
| `lst` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Local Service Tax |
| `loan_deductions` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Staff loan repayments |
| `other_deductions` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Other deductions |
| `total_deductions` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | All deductions combined |
| `net_pay` | `DECIMAL(18,4)` | NOT NULL | gross_pay - total_deductions |
| `payment_method` | `ENUM('bank_transfer','mobile_money','cash')` | NOT NULL | Disbursement method |

---

### tbl_payroll_elements

**Purpose:** Configurable payroll element definitions — all earnings and deductions. No hardcoded elements (DC-002). Finance Director configures PAYE bands, NSSF rates, allowances, and deductions without developer involvement.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `element_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Element primary key |
| `element_code` | `VARCHAR(30)` | NOT NULL, UNIQUE | Element code (e.g., `BASIC_SALARY`, `HOUSING_ALLOWANCE`, `PAYE`) |
| `element_name` | `VARCHAR(100)` | NOT NULL | Human-readable name |
| `element_type` | `ENUM('earning','deduction','employer_contribution')` | NOT NULL | Type |
| `calculation_type` | `ENUM('fixed','percentage_of_gross','formula','statutory')` | NOT NULL | How it is calculated |
| `rate_or_amount` | `DECIMAL(10,4)` | NULL | Fixed amount or percentage |
| `formula` | `TEXT` | NULL | Formula expression (for complex calculations) |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |
| `updated_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Last updated by (Finance Director) |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | |

---
