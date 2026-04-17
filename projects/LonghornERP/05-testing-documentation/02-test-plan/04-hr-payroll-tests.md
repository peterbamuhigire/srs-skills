# HR and Payroll Module Test Cases

This section covers payroll calculation (PAYE, NSSF, net pay), leave management, and payroll run approval with GL posting. All monetary assertions use integer arithmetic in UGX.

## Payroll Calculation

All deduction calculations must use integer arithmetic. Floating-point intermediate values are prohibited. PAYE is calculated on the taxable income per the Uganda Revenue Authority (URA) graduated tax bands. NSSF contributions are calculated on gross pay.

> *[CONTEXT-GAP: GAP-002 — confirm current PAYE band thresholds with URA before finalising TC-HR-001. The thresholds below reflect the bands cited in the project brief and must be verified against the current tax year's gazette.]*

### PAYE Calculation

The PAYE formula applied to monthly taxable income is:

$$PAYE = \sum_{b=1}^{n} (min(Income, Band_b^{upper}) - Band_b^{lower}) \times Rate_b$$

where $b$ is each applicable band.

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-HR-001 | `PayeCalculationTest` | `test_paye_on_ugx_2_000_000_gross` | Employee gross = UGX 2,000,000/month; PAYE bands: UGX 0–235,000 = 0%; UGX 235,001–335,000 = 10%; UGX 335,001–410,000 = 20%; UGX 410,001+ = 30% *[CONTEXT-GAP: GAP-002 — verify band thresholds]* | `gross_pay` = 2000000 | Band 1 tax: 0; Band 2 tax: (335,000 − 235,000) × 10% = 10,000; Band 3 tax: (410,000 − 335,000) × 20% = 15,000; Band 4 tax: (2,000,000 − 410,000) × 30% = 477,000; Total PAYE = 502,000 UGX (integer match) |

### NSSF Contributions

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-HR-002 | `NssfCalculationTest` | `test_nssf_contributions_exact_integer` | NSSF employer = 10% of gross; NSSF employee = 5% of gross | `gross_pay` = 2,000,000 | Employer NSSF = 200,000 UGX; Employee NSSF = 100,000 UGX; both values integer; no rounding error |

### Net Pay

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-HR-003 | `NetPayCalculationTest` | `test_net_pay_equals_gross_minus_deductions` | Net pay = Gross − PAYE − NSSF employee − other deductions | `gross_pay` = 2,000,000; PAYE = 502,000; NSSF employee = 100,000; other deductions = 50,000 | Net pay = 2,000,000 − 502,000 − 100,000 − 50,000 = 1,348,000 UGX (integer match); no floating-point intermediate |

## Leave Management

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-HR-004 | `LeaveManagementTest` | `test_approved_leave_reduces_balance` | Employee applies for 5 days; current balance = 10 days | `employee_id`; `leave_days` = 5; current `leave_balance` = 10 | Leave request approved; `leave_balance` = 5; leave record `status` = `APPROVED` |
| TC-HR-005 | `LeaveManagementTest` | `test_leave_exceeding_balance_returns_422` | Employee applies for leave exceeding their remaining balance | `employee_id`; `leave_days` = 15; current `leave_balance` = 10 | HTTP 422; `error_code` = `INSUFFICIENT_LEAVE_BALANCE`; balance unchanged |

## Payroll Run Lifecycle

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-HR-006 | `PayrollRunTest` | `test_initiate_run_creates_payslips_for_all_employees` | Initiate payroll run for 3 active employees in the same pay group | `pay_group_id`; `pay_period` = current month; 3 active employees | Exactly 3 payslip records created; total net pay on run summary = sum of individual employee net pays (integer match) |
| TC-HR-007 | `PayrollRunTest` | `test_approve_run_posts_gl_and_updates_status` | Approve a payroll run | `payroll_run_id` with status = `PENDING_APPROVAL`; session with `payroll.approve` | GL entries posted: DR Payroll Expense (total gross), CR Payroll Payable (total net), CR PAYE Payable, CR NSSF Payable; payroll run `status` = `APPROVED`; audit log row written |
