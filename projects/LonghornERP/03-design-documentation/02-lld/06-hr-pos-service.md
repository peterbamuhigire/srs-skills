# HR & Payroll and POS Modules — Low-Level Design

## Overview

The HR & Payroll module manages the employee lifecycle from onboarding through payslip generation and GL posting. The POS module operates within the tenant workspace and supports cash, mobile money, and card transactions from a browser-based session. Both modules are add-ons; `ModuleRegistry::isActive()` must be checked at controller dispatch time.

---

## EmployeeService

**Namespace:** `App\Modules\HR`

**Module guard:** `ModuleRegistry::isActive('HR_PAYROLL', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createEmployee(array $data): int` | Associative array of employee attributes (`first_name`, `last_name`, `nssf_number`, `tin`, `department_id`, `job_title_id`, `gross_salary`, `employment_type`, `start_date`, etc.) | New `employees.id` | Validates NSSF and TIN uniqueness per tenant. Inserts one row into `employees` with `status = 'active'`. Logs to `AuditService`. |
| `getPayslip(int $employeeId, int $payrollRunId): array` | Employee primary key, payroll run primary key | Payslip data as associative array | Reads from `payroll_run_lines` joined to `payroll_deductions` and `payroll_earnings` for the given run and employee. |
| `terminateEmployee(int $employeeId, string $terminationDate, string $reason): void` | Employee primary key, ISO 8601 termination date, free-text reason | `void` | Sets `employees.status = 'terminated'`, writes `terminated_at` and `termination_reason`. Triggers `LeaveService` to expire remaining leave balances. Logs to `AuditService`. |

**Tables read/written:** `employees`

---

## LeaveService

**Namespace:** `App\Modules\HR`

**Module guard:** `ModuleRegistry::isActive('HR_PAYROLL', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `applyLeave(int $employeeId, string $leaveType, string $startDate, string $endDate): int` | Employee primary key, leave type code (`ANNUAL`, `SICK`, `MATERNITY`, `PATERNITY`), ISO 8601 start date, ISO 8601 end date | New `leave_applications.id` | Calculates the number of working days. Validates that the requested days do not exceed the available balance. Inserts `leave_applications` with `status = 'pending'`. |
| `approveLeave(int $applicationId): void` | Leave application primary key | `void` | Verifies the approving user holds `APPROVE_LEAVE`. Sets `leave_applications.status = 'approved'`. Deducts days from `leave_balances`. Logs to `AuditService`. |
| `getLeaveBalance(int $employeeId, string $leaveType): float` | Employee primary key, leave type code | Remaining leave days as float | Reads `leave_balances WHERE employee_id = :employeeId AND leave_type = :leaveType AND tenant_id = :tenant_id`. |

**Tables read/written:** `leave_applications`, `leave_balances`

---

## AttendanceService

**Namespace:** `App\Modules\HR`

**Module guard:** `ModuleRegistry::isActive('HR_PAYROLL', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `recordAttendance(int $employeeId, string $date, string $checkIn, ?string $checkOut = null): int` | Employee primary key, ISO 8601 date, check-in time (`HH:MM:SS`), optional check-out time | New `attendance_records.id` | Inserts one row into `attendance_records`. Allows null `check_out` for open-ended records (employee has checked in but not yet checked out). |
| `generateAttendanceSummary(int $employeeId, string $periodStart, string $periodEnd): array` | Employee primary key, ISO 8601 start date, ISO 8601 end date | Array of daily summary rows with `['date', 'hours_worked', 'late_minutes', 'absent']` | Aggregates `attendance_records` for the date range. Marks a day absent if no attendance record exists and no approved leave covers it. |

**Tables read/written:** `attendance_records`

---

## PayrollService

**Namespace:** `App\Modules\HR`

**Module guard:** `ModuleRegistry::isActive('HR_PAYROLL', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AttendanceService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `initiatePayrollRun(int $periodId, string $payrollMonth): int` | Accounting period primary key, payroll month in `YYYY-MM` format | New `payroll_runs.id` | Creates a `payroll_runs` row with `status = 'draft'`. Copies all active employees into `payroll_run_lines`. |
| `calculateGross(int $runId): void` | Payroll run primary key | `void` | For each `payroll_run_lines` row, reads `employees.gross_salary`. Applies prorations from `AttendanceService::generateAttendanceSummary()` if the employee's contract type is `hourly`. Writes `payroll_run_lines.gross_amount`. |
| `deductPAYE(int $runId): void` | Payroll run primary key | `void` | Applies Uganda Revenue Authority PAYE tax bands from `paye_bands` table to each employee's gross. Writes `payroll_run_lines.paye_amount`. $PAYE = f(gross, bands)$ per URA bands in force for the payroll month. |
| `deductNSSF(int $runId): void` | Payroll run primary key | `void` | Applies NSSF rate: employee contribution = $gross \times 0.05$, employer contribution = $gross \times 0.10$. Writes `payroll_run_lines.nssf_employee` and `payroll_run_lines.nssf_employer`. |
| `approveRun(int $runId): void` | Payroll run primary key | `void` | Verifies the approving user holds `APPROVE_PAYROLL`. Sets `payroll_runs.status = 'approved'`. |
| `postToGL(int $runId): void` | Payroll run primary key | `void` | Opens a transaction. For each run line, posts salary expense debits and the corresponding credit entries to wages payable, PAYE payable, NSSF payable via `AccountingService::postJournal()`. Sets `payroll_runs.status = 'posted'`. Calls `AuditService::log()` inside the same transaction. |
| `generatePaymentFile(int $runId, string $format): string` | Payroll run primary key, file format code (`CSV`, `MTN_MOMO`, `AIRTEL_MOMO`) | Absolute path to the generated file | Reads approved `payroll_run_lines`. Formats the disbursement file per the requested format. Writes to `storage/payroll/<runId>.<ext>`. Returns the file path. |

**Tables read/written:** `payroll_runs`, `payroll_run_lines`, `payroll_deductions`, `paye_bands`

---

## POSService

**Namespace:** `App\Modules\POS`

**Module guard:** `ModuleRegistry::isActive('POS', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `StockLedgerService`, `SalesInvoiceService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `openSession(int $userId, int $branchId, float $openingFloat): int` | User primary key, branch primary key, cash float amount at session open | New `pos_sessions.id` | Inserts a `pos_sessions` row with `status = 'open'` and records `opening_float`. Only one open session per user per branch is permitted. |
| `recordTransaction(int $sessionId, array $lines, string $paymentMethod): int` | POS session primary key, array of `['item_id', 'qty', 'unit_price']` entries, payment method code | New `pos_transactions.id` | Inserts `pos_transactions` header and `pos_transaction_lines`. Delegates to `POSPaymentService` based on `$paymentMethod`. Posts `SALE` movements via `StockLedgerService::postMovement()`. Creates a sales invoice via `SalesInvoiceService::createInvoice()` and immediately posts it to GL. |
| `closeSession(int $sessionId, float $closingFloat): array` | POS session primary key, physical cash count at close | Session summary as associative array with `['total_sales', 'expected_cash', 'actual_cash', 'variance']` | Calculates expected cash = `opening_float` + sum of cash transactions. Sets `pos_sessions.status = 'closed'` and records `closing_float` and `closed_at`. |

**Tables read/written:** `pos_sessions`, `pos_transactions`, `pos_transaction_lines`

---

## POSPaymentService

**Namespace:** `App\Modules\POS`

**Module guard:** `ModuleRegistry::isActive('POS', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`, `MoMoService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `processCash(int $transactionId, float $tendered, float $total): float` | POS transaction primary key, cash amount tendered, transaction total | Change due as float | Posts a debit to the POS cash account via `AccountingService::postJournal()`. Returns `tendered - total`. |
| `processMoMo(int $transactionId, float $amount, string $phoneNumber): string` | POS transaction primary key, amount, customer phone number | MoMo transaction reference | [CONTEXT-GAP: GAP-011] Calls `MoMoService::verifyPayment()`. Posts a debit to the MoMo settlement account via `AccountingService::postJournal()`. |
| `printReceipt(int $transactionId): string` | POS transaction primary key | HTML receipt string | Reads transaction and line data. Applies the tenant's receipt template from `pos_receipt_templates`. Returns rendered HTML for browser-print or thermal-printer output. |

**Tables read/written:** `pos_transactions`
