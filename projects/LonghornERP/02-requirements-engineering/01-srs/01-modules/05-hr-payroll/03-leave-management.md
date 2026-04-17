# Leave Management

## 3.1 Leave Types and Balances

**FR-HR-010** — The system shall support configurable leave types per tenant, each defining: leave name, accrual rate (days per year), maximum carry-forward days, maximum balance cap, and whether the type is paid or unpaid.

**FR-HR-011** — The system shall compute leave balances per employee on a per-annum accrual basis: the system shall increment the employee's leave balance on the first day of each month by `AnnualEntitlement ÷ 12` days, rounded to 2 decimal places, and shall not exceed the maximum balance cap.

**FR-HR-012** — When an employee's fixed-term contract expires without full leave liquidation, the system shall flag the outstanding leave balance for cash-out computation in the exit management workflow.

## 3.2 Leave Requests

**FR-HR-013** — When an employee submits a leave request, the system shall record: leave type, start date, end date, number of working days (excluding public holidays and weekends), and reason narrative; the system shall validate that the requested days do not exceed the current leave balance.

**FR-HR-014** — When a leave request is submitted, the system shall route it to the employee's direct supervisor as defined by the organisational chart; if the supervisor does not act within 24 hours, the system shall escalate the request to the next HR approver in the chain.

**FR-HR-015** — When a leave request is approved, the system shall deduct the approved days from the employee's leave balance, mark the days as absent in the attendance calendar, and send an in-app notification and email to the employee.

**FR-HR-016** — When a leave request is rejected, the system shall restore the leave balance to its pre-request value and notify the employee of the rejection with the rejector's recorded reason.

## 3.3 Leave Calendar

**FR-HR-017** — The system shall maintain a configurable public holiday calendar per tenant country; public holidays shall be excluded from leave day counts and shall block timesheet entry for all employees on those dates.

**FR-HR-018** — The system shall provide a leave calendar view displaying all approved leave requests across a department for a selected month, allowing managers to identify staffing gaps before approving further requests.
