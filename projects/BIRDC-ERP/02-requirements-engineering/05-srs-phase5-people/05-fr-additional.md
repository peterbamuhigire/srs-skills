# 3.3 Additional Functional Requirements — Cross-Cutting (People)

## 3.3.1 Integrated Leave Impact on Payroll

**FR-HR-PAY-001**
When approved leave days for an employee include unpaid leave, the payroll run shall automatically deduct the corresponding salary for the unpaid days from the employee's gross earnings before computing statutory deductions. The deduction formula is:

$Unpaid\_Leave\_Deduction = \frac{Gross\_Monthly\_Salary}{Working\_Days\_In\_Month} \times Unpaid\_Leave\_Days$

The unpaid deduction shall appear as a separate line item on the payslip.

**FR-HR-PAY-002**
When the payroll run is executed, the system shall automatically import the approved overtime hours from the attendance module for each employee and compute the overtime earnings based on the employee's configured overtime rate (e.g., 1.5× the hourly rate for hours beyond the standard shift). Overtime hours are sourced exclusively from the biometric attendance module; manual overtime entries require Finance Manager approval (BR-016).

**FR-HR-PAY-003**
When an employee is on approved sick leave and the sick leave entitlement for the current year is exhausted, the system shall automatically flag any additional sick leave days as unpaid and apply the unpaid deduction in the payroll run, notifying the HR Manager of the status change.

## 3.3.2 Acting Allowance

**FR-HR-PAY-004**
When the HR Manager records an acting appointment for an employee (acting in a higher-grade position for a specified period), the system shall add a time-limited acting allowance earnings element to the employee's payroll for the acting period. The acting allowance shall be automatically removed from the payroll run when the acting period end date is reached, without requiring manual intervention.

## 3.3.3 Dual-Mode Payroll GL Allocation

**FR-HR-PAY-005**
When a payroll run includes both PIBID government-funded employees and BIRDC commercially-funded employees, the system shall split the GL auto-posting across the two sets of accounts: PIBID salary expenses post to the parliamentary budget vote cost centres; BIRDC salary expenses post to the commercial GL cost centres. A consolidated payroll GL report and separated payroll GL report shall both be available on demand, satisfying DC-004.

## 3.3.4 HR and Payroll Security

**FR-HR-PAY-006**
When any API request related to payroll approval, payroll lock, or payroll element modification is received, the system shall verify the requesting user's role at the API layer — not solely at the UI layer — and reject unauthorised requests with HTTP 403, logging the attempt. This enforcement is independent of browser-side controls and applies to direct API requests (BR-003).

**FR-HR-PAY-007**
When the Finance Director or IT Administrator role is assigned to a user account, the system shall require TOTP two-factor authentication (Google Authenticator compatible) at every login session initiation. A login without TOTP confirmation for these roles shall be blocked at the authentication layer.

**FR-HR-PAY-008**
When an employee record contains a NIN or salary information, the system shall store the NIN as an encrypted field at rest using AES-256 encryption, decrypting only for authorised role access. Salary fields shall be stored in plain numeric form but access-controlled by the role matrix.

## 3.3.5 Audit and Retention

**FR-HR-PAY-009**
The system shall retain all employee payroll records, leave records, attendance records, and disciplinary records for a minimum of 7 years from the end of the financial year in which they were created, satisfying Uganda Companies Act and Income Tax Act retention requirements (DC-003). Automated deletion of records within the 7-year window shall be architecturally impossible.

**FR-HR-PAY-010**
When the Auditor General (OAG Uganda) or Finance Director initiates a payroll audit trail query for a specific employee or period, the system shall return a complete, time-ordered audit log showing every change to that employee's payroll records, with actor identity, IP address, timestamp, and before/after field values, within 15 seconds.
