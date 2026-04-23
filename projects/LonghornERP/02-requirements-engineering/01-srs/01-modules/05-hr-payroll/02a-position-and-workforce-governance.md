# Position and Workforce Governance

This section strengthens the HR core beyond basic employee records. It defines the governed structures required for manager accountability, headcount control, and effective-dated workforce truth.

**FR-HR-070** - The system shall allow an authorised HR administrator to define a job architecture consisting of job families, job levels, grades, and approved job titles, and every employee assignment shall reference an active job-architecture record.

**FR-HR-071** - When position control is enabled for a tenant, the system shall require every active employee assignment to be linked to an approved position record containing at minimum: position code, job title, department, branch, reporting manager position, planned cost centre, and budget status.

**FR-HR-072** - The system shall store all employee organisational assignments, manager changes, grade changes, and position changes as effective-dated records such that the platform can reconstruct what was true for any employee on any historical date.

**FR-HR-073** - When an authorised user submits a position change, transfer, promotion, or salary-grade change, the system shall route the request through an approval workflow that records initiator, approver, effective date, reason code, and approval outcome before the change becomes active.

**FR-HR-074** - The system shall provide an onboarding checklist workflow for each newly hired employee, with checklist items assignable to HR, IT, Finance, Procurement, and the line manager; the employee status shall remain `pending_onboarding` until all mandatory checklist items are completed or explicitly waived by an authorised approver.

**FR-HR-075** - The system shall support probation management by storing probation start date, expected confirmation date, reviewer, decision status, and decision notes, and it shall notify the responsible manager and HR officer 14 calendar days before the confirmation decision is due.

**FR-HR-076** - The system shall provide a manager-initiated workforce transaction workbench through which an authorised line manager may submit requests for leave approval, transfer, confirmation, disciplinary status change, or compensation change only for employees within that manager's current reporting scope.
