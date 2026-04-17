# Timesheets and Resource Allocation

## 4.1 Overview

This section specifies requirements for employee time logging against project tasks, timesheet approval, billing rate management, resource allocation to projects, and resource utilisation reporting.

## 4.2 Timesheet Entry

**FR-PROJ-026:** When an employee with the `timesheets.create` permission submits a timesheet line, the system shall create the record and set its status to Submitted. Each timesheet line shall store:

- Employee (lookup to HR employee register; defaults to the logged-in user)
- Project (lookup to active projects; required)
- WBS Task (lookup to tasks within the selected project; required)
- Date (date; must fall within a non-closed timesheet period)
- Hours (numeric, 0.25–24 in 0.25-hour increments)
- Description of Work (text; optional)
- Billable (boolean; default: true for projects with T&M billing, false otherwise)

**FR-PROJ-027:** The system shall prevent an employee from logging more than 24 hours of timesheet entries for a single calendar date across all projects. Any submission that would cause the total to exceed 24 hours shall be rejected with HTTP 422 and the error "Total logged hours for [date] would exceed 24 hours."

**FR-PROJ-028:** When a user submits a timesheet line against a project with status Closed or Cancelled, the system shall reject the submission with HTTP 422 and the error "Cannot log time against a Closed or Cancelled project."

**FR-PROJ-029:** The system shall display a weekly timesheet grid view allowing an employee to enter hours for all their assigned projects across a 7-day week on a single screen. The grid shall show rows by project and task, columns by day, and a running weekly total per row and per day.

## 4.3 Timesheet Approval Workflow

**FR-PROJ-030:** The system shall route submitted timesheet lines to the Project Manager of the associated project for approval. The Project Manager shall have the ability to approve or reject individual lines or all lines for an employee in bulk.

**FR-PROJ-031:** When a Project Manager approves a timesheet line, the system shall set its status to Approved and make it available for cost aggregation (Section 5.2) and T&M billing calculation (Section 5.3).

**FR-PROJ-032:** When a Project Manager rejects a timesheet line, the system shall require a rejection reason (free text, minimum 10 characters), set the line status to Rejected, and notify the employee via the system notification centre with the reason text.

**FR-PROJ-033:** The system shall support a timesheet period configuration (weekly or monthly) per tenant. At the end of each period, the system shall automatically lock all Draft timesheet lines for that period and set them to status Pending Submission, prompting the employee to review and submit.

## 4.4 Billing Rate Management

**FR-PROJ-034:** The system shall maintain a billing rate record for each employee, stored in the HR module employee record, comprising:

- Standard Billing Rate (numeric, currency per hour; required)
- Effective From date (required)
- Effective To date (optional; null = current rate)

**FR-PROJ-035:** When computing T&M billing, the system shall apply the billing rate effective on the timesheet line's date. If no rate record is effective for the employee on that date, the system shall flag the timesheet line with `[CONTEXT-GAP: billing rate not defined for employee on date]` and exclude it from the billing calculation until the rate is resolved.

**FR-PROJ-036:** The system shall allow project-level billing rate overrides per employee. A project rate override record shall supersede the standard HR billing rate for T&M billing on that specific project, while leaving the employee's standard rate unchanged for all other projects.

## 4.5 Resource Allocation

**FR-PROJ-037:** When a Project Manager with `projects.edit` permission adds a resource allocation record, the system shall create it and display the resource in the project's **Team** view. Each allocation record shall store:

- Employee (lookup to HR employee register)
- Project (parent project reference)
- Role on Project (free text; e.g., "Lead Engineer," "Site Supervisor")
- Planned Hours (numeric, ≥ 0; optional)
- Allocation Start Date (date)
- Allocation End Date (date; must be ≥ Allocation Start Date)

**FR-PROJ-038:** The system shall display a resource utilisation summary per employee showing, for each active allocation period: allocated project(s), planned hours, logged hours to date, and utilisation percentage calculated as $Utilisation\% = \frac{LoggedHours}{PlannedHours} \times 100$. If Planned Hours = 0 the utilisation field shall display "N/A."

**FR-PROJ-039:** When an employee is allocated to 2 or more projects whose date ranges overlap, the system shall display an informational indicator on the employee's allocation record: "Employee has overlapping project allocations." This shall not block saving.

## 4.6 Utilisation Report

**FR-PROJ-040:** The system shall provide a Resource Utilisation Report filterable by employee, project, department, and date range. The report shall display for each employee-project pair: planned hours, logged hours, approved hours, billable hours, and utilisation %. The report shall be exportable to Excel (.xlsx) and PDF.
