# 3. Functional Requirements

## 3.1 F-013: Human Resources

### 3.1.1 Employee Profile Management

**FR-HR-001**
When the HR Manager submits a new employee registration form with all mandatory fields (full name, NIN, date of birth, gender, nationality, contact phone, emergency contact name and phone, department, job title, job grade, contract type, contract start date, contract end date if applicable, and photo), the system shall create a permanent employee record, assign a unique sequential employee ID (format: `EMP-NNNN`), and display the new employee profile within 3 seconds. The employee ID must appear on all subsequent payroll, leave, and attendance records for that employee.

**FR-HR-002**
When the HR Manager opens an existing employee profile and modifies any field, the system shall save the change, record the previous and new values in the immutable audit log together with the actor's user ID, IP address, and timestamp, and confirm the save with a success notification within 2 seconds. The audit record must be non-deletable and non-editable by any user role.

**FR-HR-003**
When the HR Manager searches for an employee by name, NIN, employee ID, or department, the system shall return all matching records within 2 seconds and display them in a paginated list. The search must be case-insensitive and must support partial string matching.

**FR-HR-004**
When a new employee profile is saved, the system shall validate that the NIN field contains exactly 14 characters in the Uganda National Identification and Registration Authority format, and reject the submission with a field-level error message if the format is invalid.

**FR-HR-005**
When the HR Manager assigns an employee to a department and job grade, the system shall enforce referential integrity against the configured department list and job grade table. The system shall reject assignment of a department or grade that does not exist in the configuration tables.

**FR-HR-006**
When the HR Manager records a contract change (promotion, transfer, contract renewal, or change of contract type), the system shall preserve the previous contract record with its effective dates and create a new contract record with the new terms and a new effective start date, maintaining a complete employment history for the employee.

**FR-HR-007**
When any user attempts to view an employee's NIN, salary details, or emergency contact information, the system shall verify that the user holds the HR Manager, Payroll Officer, or Finance Manager role. If the user does not hold one of these roles, the system shall mask the sensitive fields and deny access, logging the access attempt.

### 3.1.2 Organisational Structure

**FR-HR-008**
When the IT Administrator or HR Manager creates a new department record, the system shall store the department name, department code, department head (linked to an employee record), cost centre code (linked to the GL chart of accounts), and parent department for hierarchical reporting. The system shall reject a duplicate department code.

**FR-HR-009**
When the Finance Director or HR Manager creates a job grade record, the system shall store the grade code, grade name, pay scale type (Government — PIBID or Commercial — BIRDC), minimum salary, and maximum salary for that grade. The system shall enforce that the minimum salary is less than or equal to the maximum salary; a violation shall produce a field-level validation error.

**FR-HR-010**
When the HR Manager requests the organisational chart, the system shall generate a hierarchical diagram displaying all departments, their parent-child relationships, headcounts per department, and the department head name, rendered within 5 seconds.

**FR-HR-011**
When the Finance Director configures a salary scale for a government pay grade (PIBID), the system shall store the scale in a configuration table and apply it automatically to all employees assigned that grade during payroll computation. The Finance Director shall be able to update the scale effective from a specified future date without affecting the current pay period.

### 3.1.3 Attendance Management

**FR-HR-012**
When a ZKTeco biometric fingerprint event (clock-in or clock-out) is imported from the device, the system shall parse the device export file, match each record to the corresponding employee by biometric device user ID, and store the clock-in and clock-out timestamps in the attendance table. The import must reject records that cannot be matched to a registered employee and log them as unmatched exceptions for HR review. `[CONTEXT-GAP: GAP-005]`

**FR-HR-013**
When the HR Manager initiates a biometric attendance import for a given date range, the system shall process the import file, create attendance records for all matched employees, calculate the hours worked per employee per day (clock-out timestamp minus clock-in timestamp), and complete the import within 30 seconds for a batch of up to 500 records.

**FR-HR-014**
When an attendance record is imported from the biometric device and the clock-in time is after the employee's configured shift start time by more than a configurable tolerance (default: 5 minutes), the system shall automatically flag that attendance record as "Late Arrival" and include the employee in the late arrivals report for that day.

**FR-HR-015**
When an attendance record shows a clock-out time before the employee's configured shift end time by more than a configurable tolerance (default: 15 minutes), the system shall automatically flag the record as "Early Departure" and include it in the attendance exceptions report.

**FR-HR-016**
When an employee's attendance record shows total hours worked exceeding the standard shift duration by more than a configurable overtime threshold (default: 30 minutes), the system shall automatically flag the record as "Overtime" and calculate the overtime hours for inclusion in the payroll run.

**FR-HR-017**
When the biometric device is offline and attendance is recorded manually by the HR Manager, the system shall store the manual record with a status of "Manual — Pending Biometric Reconciliation" and require Finance Manager approval before the record is treated as authoritative (BR-016). The Finance Manager approval shall be logged in the audit trail with the reason.

**FR-HR-018**
When biometric data becomes available after a period of device downtime, the system shall compare manual attendance records with the imported biometric records for the same date range and present a reconciliation report listing discrepancies. The HR Manager shall confirm or override each discrepancy before the reconciliation is closed.

**FR-HR-019**
When the HR Manager requests a monthly attendance summary report for a department or for all staff, the system shall produce a report showing each employee's total days present, days absent, late arrivals, early departures, overtime hours, and approved leave days for the period, exportable to PDF and Excel within 10 seconds.

### 3.1.4 Leave Management

**FR-HR-020**
When a staff member opens the HR Self-Service App and submits a leave application specifying leave type, start date, end date, and reason, the system shall validate that the requested duration does not exceed the employee's available leave balance for that leave type, record the application with status "Pending Supervisor Approval", and send a push notification to the employee's line supervisor within 60 seconds.

**FR-HR-021**
When a supervisor receives a leave application notification and approves the request in the system, the system shall update the application status to "Approved", deduct the approved leave days from the employee's leave balance in real time, notify the Finance Manager of the approved leave for payroll impact awareness, and send a confirmation notification to the employee within 60 seconds.

**FR-HR-022**
When a supervisor rejects a leave application, the system shall update the status to "Rejected", record the rejection reason, restore the leave balance to its pre-application state, and notify the employee within 60 seconds.

**FR-HR-023**
When the Finance Director or HR Manager configures leave entitlements for a leave type and job grade combination, the system shall store the annual entitlement (in calendar days or working days, as configured), the accrual frequency (annual or monthly), the maximum carry-forward days, and the maximum encashment days. The system shall apply these entitlements automatically to all employees matching the grade at the start of each leave year.

**FR-HR-024**
The system shall support the following leave types as configurable records, each with independent entitlement rules: Annual Leave, Sick Leave, Maternity Leave, Paternity Leave, Compassionate Leave, Study Leave, and Unpaid Leave. Additional leave types shall be addable by the HR Manager via the configuration UI without developer involvement (DC-002).

**FR-HR-025**
When an employee's leave balance is queried via the HR Self-Service App or the web ERP, the system shall return the real-time balance reflecting all approved leave, taken leave, and pending applications for the current leave year, with the response delivered within 3 seconds.

**FR-HR-026**
When an employee's contract end date or resignation date is recorded, the system shall automatically compute the employee's leave encashment entitlement based on the remaining approved annual leave balance and the employee's daily rate, and include this figure in the exit clearance final pay calculation.

### 3.1.5 Factory Worker Registry

**FR-HR-027**
When the HR Manager or Production Supervisor registers a new factory (casual) worker, the system shall create a worker record separate from the permanent payroll, storing: full name, NIN, phone number, skill category (from a configurable skill matrix), daily rate, and registration date. The worker record shall be assigned a unique worker ID (format: `WKR-NNNN`).

**FR-HR-028**
When a Production Supervisor assigns a casual worker to a production order for a given date, the system shall record the worker ID, production order reference, date, shift, and task assigned. The assignment shall be visible in the Factory Floor App in real time.

**FR-HR-029**
When daily attendance is recorded for a casual worker (via the Factory Floor App or web ERP), the system shall store the worker ID, date, attendance status (Present / Absent / Half-Day), and hours worked. The system shall calculate the daily wage payable (hours worked × daily rate, or daily rate for a full day) and accumulate it in a period-end casual payroll register.

**FR-HR-030**
When the Production Supervisor records production completion quantities for a production order, the system shall link the output quantity to the casual workers assigned to that order on that date, enabling per-worker productivity metrics (kg output per worker per shift) to be computed and displayed in the HR module.

**FR-HR-031**
When the HR Manager requests a casual worker productivity report for a date range, the system shall display each worker's total attendance days, total hours worked, total wage payable, total production output linked to their shifts, and productivity ratio, exportable to PDF and Excel within 10 seconds.

**FR-HR-032**
When the HR Manager opens the skill matrix configuration, the system shall display all defined skill categories with the count of workers holding each skill. The HR Manager shall be able to add, rename, or deactivate skill categories without developer involvement.

### 3.1.6 Staff Loans and Advances

**FR-HR-033**
When the HR Manager records a staff loan or salary advance for an employee, the system shall store the loan ID (format: `LOAN-NNNN`), employee reference, loan amount, disbursement date, repayment schedule (monthly instalment amount and number of instalments), and interest rate (if applicable). The disbursement amount shall be posted to the GL as DR Staff Loans Receivable / CR Cash or Bank.

**FR-HR-034**
When a payroll run is executed for a period, the system shall automatically include the configured monthly loan or advance instalment as a deduction element for every employee with an outstanding loan balance, without requiring manual entry by the Payroll Officer. The deduction shall reduce the outstanding loan balance and post to the GL as DR Employee Payable / CR Staff Loans Receivable.

**FR-HR-035**
When the HR Manager opens a staff loan record, the system shall display the full repayment schedule, all deductions applied to date, the current outstanding balance, and the projected clearance date.

**FR-HR-036**
When a staff loan balance reaches zero following a payroll deduction, the system shall automatically mark the loan as "Fully Repaid", cease the deduction element in subsequent payroll runs without manual intervention, and notify the HR Manager.

### 3.1.7 Disciplinary Records

**FR-HR-037**
When the HR Manager records a disciplinary action for an employee (written warning, final written warning, suspension, or fine), the system shall store the disciplinary record ID, employee reference, incident date, action type, description, issuing officer, and outcome, linked to the employee's permanent profile.

**FR-HR-038**
When a disciplinary action includes a monetary fine, the HR Manager shall be able to specify the fine amount, and the system shall automatically include this as a deduction element in the employee's next payroll run, posting to the GL as DR Employee Payable / CR Disciplinary Fines Income. The deduction shall appear on the payslip with the description "Disciplinary Fine — [Reference]".

**FR-HR-039**
When the HR Manager requests a disciplinary record report for a department or date range, the system shall generate a report listing all disciplinary actions with their status and financial impact, exportable to PDF within 5 seconds.

### 3.1.8 Exit Clearance

**FR-HR-040**
When the HR Manager initiates an exit clearance workflow for an employee (triggered by resignation or termination), the system shall generate a multi-department clearance checklist with configurable items per department (Finance, IT, Stores, Procurement, HR). Each checklist item shall require sign-off by the designated department head before the clearance can be completed.

**FR-HR-041**
When all departmental clearance items are signed off, the system shall compute the employee's final pay, comprising: outstanding net salary for the current partial pay period, approved leave encashment balance at the daily rate, and net of any outstanding loan or advance deductions. The final pay figure shall be presented for Finance Manager review before processing.

**FR-HR-042**
When the exit clearance is completed and the final pay is approved by the Finance Manager, the system shall trigger the IT Administrator to deactivate the employee's system account, preventing all further logins to the web ERP and the HR Self-Service App. This deactivation shall occur within 24 hours of clearance completion confirmation.

**FR-HR-043**
When an employee's system account is deactivated as part of exit clearance, the system shall preserve all historical records (attendance, payroll, leave, disciplinary) associated with that employee. No employee data shall be deleted; deactivated employees shall be clearly marked in all reports.

### 3.1.9 HR Self-Service App (Android)

**FR-HR-044**
When a staff member logs into the HR Self-Service App using their employee credentials, the system shall authenticate the request via a JWT Bearer token (15-minute access, 30-day refresh), establish a session, and present the home screen within 3 seconds on a 4G LTE connection.

**FR-HR-045**
When network connectivity is unavailable, the HR Self-Service App shall serve the last-synced payslips, leave balance, and attendance records from the local Room (SQLite) cache, and queue any submitted leave applications for background sync when connectivity is restored via WorkManager. The app shall display a clear "Offline Mode" indicator on every screen while offline.

**FR-HR-046**
When a staff member views their attendance record in the HR Self-Service App for a selected month, the system shall display each working day with the clock-in time, clock-out time, hours worked, and any attendance flag (Late Arrival, Early Departure, Overtime, Absent), drawn from the authoritative biometric attendance data.

**FR-HR-047**
When a staff member views their leave balance in the HR Self-Service App, the system shall display the current balance for each leave type (entitled, taken, pending approval, remaining) for the current leave year, updated in real time when connectivity is available.

**FR-HR-048**
When a staff member submits a leave application via the HR Self-Service App and the application is rejected by the supervisor, the system shall notify the employee via push notification within 60 seconds of the supervisor action, displaying the rejection reason in the app.

---

## 3.2 F-014: Payroll

### 3.2.1 Payroll Element Configuration

**FR-PAY-001**
When the Finance Director or Payroll Officer opens the payroll element configuration screen and creates a new earnings element, the system shall store the element name, element code, element type (Earnings), calculation method (Fixed Amount, Percentage of Basic, Percentage of Gross, Formula), formula expression if applicable, taxability flag (PAYE-taxable: Yes / No), NSSF-includable flag, GL debit account, and effective date. The Finance Director shall be able to create, modify, and deactivate any element without developer involvement (DC-002).

**FR-PAY-002**
When the Finance Director or Payroll Officer creates a new deduction element, the system shall store the element name, element code, element type (Deduction), calculation method, statutory flag (PAYE / NSSF / LST / Non-statutory), priority order for sequential deduction (where multiple deductions may exhaust the net pay), GL credit account, and effective date.

**FR-PAY-003**
When the Payroll Officer assigns payroll elements to an employee, the system shall allow any combination of configured earning and deduction elements to be assigned, each with its own value, effective date, and end date. No payroll element shall be hardcoded in the application code; all elements shall be data-driven (DC-002). Verification: a PHPUnit test shall confirm that adding a new earnings element via the UI results in its inclusion in the payroll computation without any code change.

**FR-PAY-004**
When the Finance Director updates the value or rate of a payroll element effective from a future date, the system shall store the new value with the effective date and continue to apply the old value to payroll runs whose period end date precedes the effective date. Payroll runs in the new period shall automatically apply the updated value.

### 3.2.2 Uganda PAYE Computation

**FR-PAY-005**
When the Finance Director opens the PAYE tax band configuration screen and enters new tax bands published by URA, the system shall store each band as a record comprising: lower income threshold (UGX), upper income threshold (UGX or "unlimited"), and marginal tax rate (%). The Finance Director shall be able to update bands without developer involvement. The updated bands shall apply to payroll runs from the effective date specified. `[CONTEXT-GAP: GAP-008]`

**FR-PAY-006**
When a payroll run is executed for an employee, the system shall compute PAYE by applying the configured progressive tax bands to the employee's chargeable income (gross taxable earnings minus allowable deductions per the Uganda Income Tax Act), summing the tax liability across all applicable bands. The computed PAYE must satisfy the formula:

$PAYE = \sum_{i=1}^{n} \min(Taxable\_Income - Lower_i, Band\_Width_i) \times Rate_i$

where $n$ is the number of applicable tax bands, $Lower_i$ is the lower threshold of band $i$, $Band\_Width_i$ is the width of band $i$, and $Rate_i$ is the marginal rate for band $i$.

**FR-PAY-007**
When a payroll run produces a PAYE computation for an employee, the system shall display the tax band breakdown (income falling in each band, rate applied, tax per band, total PAYE) on the payroll computation detail screen and on the employee's payslip, enabling verification by the Payroll Officer before approval.

**FR-PAY-008**
When the Payroll Officer requests the monthly PAYE remittance schedule, the system shall generate a summary report listing: total PAYE deducted per employee, total employer PAYE payable to URA, and the URA remittance reference, formatted for submission to URA by the 15th of the following month.

### 3.2.3 Uganda NSSF Computation

**FR-PAY-009**
When a payroll run is executed, the system shall compute NSSF contributions for each eligible employee as: employee contribution = 5% of gross salary; employer contribution = 10% of gross salary. The formula is:

$Employee\_NSSF = Gross\_Salary \times 0.05$

$Employer\_NSSF = Gross\_Salary \times 0.10$

Both amounts shall be stored against the employee's payroll record for the period.

**FR-PAY-010**
When the Payroll Officer requests the NSSF contribution schedule for a completed payroll run, the system shall generate the schedule in the exact format required by NSSF Uganda for employer remittance, including: employee name, NIN, NSSF membership number, gross salary, employee contribution, employer contribution, and total contribution. The schedule shall be exportable as a PDF and as a `.csv` file compatible with the NSSF employer self-service portal. `[CONTEXT-GAP: GAP-009]`

**FR-PAY-011**
When the Finance Director updates the NSSF contribution rates (should statutory rates change), the system shall store the new rates with an effective date and apply them to payroll runs from that date forward, without requiring any code change (DC-002).

### 3.2.4 Local Service Tax (LST) Computation

**FR-PAY-012**
When the Finance Director configures LST tiers for a local government authority (Bushenyi District or Kampala), the system shall store each tier as: annual income lower threshold (UGX), annual income upper threshold (UGX), and annual LST amount (UGX). The Finance Director shall add, modify, and deactivate tiers without developer involvement.

**FR-PAY-013**
When a payroll run is executed, the system shall determine each employee's applicable LST tier based on their annual gross salary and deduct the corresponding LST amount from their monthly pay (annual LST amount ÷ 12, rounded to the nearest UGX). The LST deduction shall be zero for employees with annual income below the minimum chargeable threshold.

**FR-PAY-014**
When the Payroll Officer requests the LST remittance report for a completed payroll run, the system shall generate a summary per local government authority showing total LST collected and due, formatted for submission to the relevant local government within the statutory deadline.

### 3.2.5 Payroll Run

**FR-PAY-015**
When the Payroll Officer initiates a new payroll run, the system shall require the Payroll Officer to specify: pay period (month and year), payroll type (Permanent Staff or Casual Workers), and the set of employees to include (all active employees, a specific department, or a custom selection). The system shall prevent a second payroll run of the same type from being created for a period where a run already exists with status "Approved" or "Locked" (BR-010).

**FR-PAY-016**
When a payroll run is initiated, the system shall compute gross-to-net for each included employee in the following sequence: (1) sum all active earnings elements; (2) compute statutory deductions (PAYE, NSSF, LST) on the gross; (3) sum all non-statutory deductions (loans, advances, disciplinary fines, custom deductions); (4) compute net pay as Gross Earnings minus all deductions. If net pay is negative for any employee, the system shall flag that employee with a "Net Pay Negative — Review Required" warning and exclude them from the payment run until the Payroll Officer resolves the issue.

**FR-PAY-017**
When the payroll computation is complete, the system shall present a payroll summary screen to the Payroll Officer showing: total employees processed, total gross earnings, total PAYE, total NSSF (employee), total NSSF (employer), total LST, total other deductions, and total net pay. The summary must display within 10 seconds for a batch of up to 200 employees.

**FR-PAY-018**
When the Payroll Officer submits the payroll run for approval, the system shall enforce segregation of duties: the Finance Manager who approves the run must be a different user account from the Payroll Officer who submitted it (BR-003). If the Finance Manager and Payroll Officer share an account, the system shall block approval and display a segregation of duties violation message.

**FR-PAY-019**
When the Finance Manager reviews the payroll summary and approves the run, the system shall lock the payroll run (status: "Approved — Locked"), record the Finance Manager's user ID, IP address, and timestamp as the approver, and prevent any further modification to that run. No user role — including IT Administrator and Finance Director — shall be able to edit or delete a locked payroll run (BR-010). Corrections shall be processed as adjustment runs in a subsequent period.

**FR-PAY-020**
When a payroll run is locked, the system shall automatically trigger GL auto-posting with the following entries per department cost centre:

- DR Salary Expense — [Department Cost Centre] (gross salary)
- CR PAYE Payable (total PAYE deducted)
- CR NSSF Payable — Employee (employee NSSF deducted)
- CR NSSF Payable — Employer (employer NSSF contribution)
- CR LST Payable (total LST deducted)
- CR Loan Deductions Payable (loan instalment deducted)
- CR Employee Net Payable (total net pay payable to staff)

No manual journal entry shall be required. The GL posting shall be traceable to the payroll run reference.

**FR-PAY-021**
When a payroll run is locked and GL auto-posting fails for any reason (e.g., unmapped GL account for a department), the system shall roll back the lock, restore the payroll run to "Pending Approval" status, and alert the Finance Manager with the specific GL mapping error. The payroll lock shall not complete until GL posting is confirmed successful.

### 3.2.6 Payslip Generation and Delivery

**FR-PAY-022**
When the Finance Manager approves and locks a payroll run, the system shall generate a PDF payslip for each employee using mPDF. The payslip shall include: BIRDC logo, employee name, employee ID, department, job grade, pay period, itemised earnings (each element name and amount), itemised deductions (each element name and amount), gross pay, total deductions, and net pay. The PAYE tax band breakdown shall appear as a sub-table on the payslip.

**FR-PAY-023**
When the Payroll Officer initiates payslip delivery for a completed payroll run, the system shall send each employee's payslip PDF by email via PHPMailer to the employee's registered email address, or deliver it via WhatsApp to the employee's registered phone number, based on the employee's configured delivery preference. Delivery shall be completed within 30 minutes for a batch of 200 employees.

**FR-PAY-024**
When a staff member opens the HR Self-Service App and navigates to the payslip section, the system shall display a list of all payroll periods for which payslips exist, and on selection, render the payslip PDF within 3 seconds. Payslips shall be downloadable to the device for offline access.

**FR-PAY-025**
When a payslip delivery attempt by email or WhatsApp fails for a specific employee, the system shall log the failure with the employee ID, delivery channel, error code, and timestamp, and present the failure in a delivery exception report accessible to the Payroll Officer.

### 3.2.7 Bank Transfer and Mobile Money Salary Payment

**FR-PAY-026**
When the Payroll Officer requests the bank transfer file for a completed and locked payroll run, the system shall generate a bulk credit transfer file in the format required by BIRDC's bank, containing: employee name, account number, bank code, branch code, and net pay amount for each permanent employee with a bank account on record. The file shall be exportable via PhpSpreadsheet in the bank's required format. `[CONTEXT-GAP: GAP-006]`

**FR-PAY-027**
When the Payroll Officer processes casual worker salary payments via mobile money, the system shall compile a payment batch containing: each casual worker's NIN, registered phone number (MTN or Airtel), and net wage payable for the period, and submit the batch to the MTN MoMo Business API or Airtel Money API. The system shall log each transaction's API response status (Success / Failed / Pending) against the worker's payment record. `[CONTEXT-GAP: GAP-002]`

**FR-PAY-028**
When a mobile money salary disbursement fails for one or more workers in a batch, the system shall present a failure report to the Payroll Officer listing the affected workers, phone numbers, amounts, and API error codes, without blocking successful disbursements to other workers in the same batch.

**FR-PAY-029**
When a mobile money salary disbursement is confirmed as successful by the API callback, the system shall mark that worker's payment status as "Paid", record the mobile money transaction reference, and post the corresponding GL entry: DR Employee Net Payable / CR Cash — Mobile Money Suspense.

### 3.2.8 Payroll Adjustment and Correction

**FR-PAY-030**
When an error is discovered in a locked payroll run, the Payroll Officer shall initiate a correction by creating a new payroll run with type "Adjustment" for the next pay period, referencing the original run. The adjustment run shall include only the affected employees and shall contain counter-entries (positive or negative amounts) that correct the error when combined with the original run. The original locked run shall remain unchanged (BR-010).

**FR-PAY-031**
When an adjustment payroll run is completed and locked, the system shall generate adjustment payslips for affected employees showing the original amounts, the correction amounts, and the net adjustment, delivered via the same channel as the original payslip.

### 3.2.9 Payroll Reporting

**FR-PAY-032**
When the Finance Manager or Payroll Officer requests a payroll cost report by department for a specified period, the system shall generate a report showing total gross salary, total statutory deductions, total employer NSSF, and total net salary per department and in aggregate, within 10 seconds, exportable to PDF and Excel.

**FR-PAY-033**
When the Finance Director requests the year-to-date payroll summary for audit purposes, the system shall generate a report showing, for each employee, their total gross earnings, total PAYE deducted, total NSSF (employee and employer), total LST, total other deductions, and total net pay for the financial year to date, within 15 seconds for a workforce of 200.

**FR-PAY-034**
When the Finance Manager requests the PAYE remittance certificate for a completed month, the system shall generate a URA-formatted P9 equivalent annual PAYE deduction schedule per employee, listing the monthly PAYE amounts for all 12 months of the tax year, exportable as a PDF.

**FR-PAY-035**
When the Payroll Officer requests a payroll audit trail report for a specific run, the system shall display every user action on that run — creation, element additions, submission for approval, approval, and GL posting — with actor, timestamp, IP address, and before/after values, satisfying DC-003 and Uganda Income Tax Act 7-year retention requirements.
