# Exit Management

## 9.1 Separation Workflow

**FR-HR-057** — When a user initiates an employee exit, the system shall record: exit type (resignation, redundancy, dismissal, end of contract, retirement), last working date, notice period compliance status, and any exit interview notes.

**FR-HR-058** — When an exit is initiated, the system shall trigger a clearance checklist workflow requiring sign-off from: IT (equipment return), Finance (outstanding advances), Procurement (assets), and HR (final documents); the exit shall not be finalised until all clearance items are checked off.

## 9.2 Terminal Benefits Calculation

**FR-HR-059** — When a user computes terminal benefits for a departing employee, the system shall calculate the following components:

- Gratuity (where applicable per contract): $Gratuity = YearsOfService \times MonthlyBasic \times GratuityRate$
- Accrued leave pay: $LeavePay = (UnusedLeaveDays \div 22) \times MonthlyBasic$
- Notice pay (if notice not worked): $NoticePay = NoticePeriodDays \times DailyRate$
- Outstanding salary for the final partial month: $FinalSalary = (DaysWorked \div WorkingDaysInMonth) \times MonthlyBasic$

**FR-HR-060** — The terminal benefits computation shall display each component, the applicable formula, the computed value, and the total gross terminal benefit; PAYE shall be applied to taxable components before the final net amount is posted to payroll.

## 9.3 Record Archiving

**FR-HR-061** — When an employee exit is finalised, the system shall transition the employee record to "Inactive" status, preserve all payroll history, payslips, leave records, and attendance data in read-only mode, and retain the records for a minimum of 10 years.

**FR-HR-062** — The system shall prevent reassignment of an inactive employee's ID to a new employee for a minimum of 3 years after exit.
