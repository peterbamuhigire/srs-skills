# Payroll Governance and Controls

This section defines the controls that make payroll a governed operating rhythm rather than a single batch calculation.

**FR-HR-077** - The system shall allow an authorised payroll administrator to configure a payroll calendar per pay group, including period open date, cut-off date, approval deadline, payment date, and statutory submission target date.

**FR-HR-078** - Before a payroll run may be submitted for approval, the system shall generate a payroll validation pack listing at minimum: employees with missing bank or mobile-money payment details, missing statutory identifiers, unapproved attendance exceptions, negative net-pay results, duplicate element assignments, and changes in gross pay greater than a tenant-defined variance threshold.

**FR-HR-079** - The system shall produce a payroll variance review comparing the current run against the most recent prior approved run for the same pay group, showing per-employee and aggregate changes in gross pay, deductions, net pay, headcount, and statutory totals.

**FR-HR-080** - The system shall support a parallel or shadow payroll mode in which authorised users can compute a payroll run using live or imported comparison inputs without creating live GL postings, payment files, statutory submissions, or employee-visible payslips.

**FR-HR-081** - The system shall enforce segregation of duties for payroll release such that the user who computes a payroll run shall not be the final approver for the same run unless the tenant explicitly enables emergency override and records a reason with second-level approval.

**FR-HR-082** - The system shall support off-cycle and retro payroll runs, and each such run shall require a mandatory reason code, linked source event, affected employee scope, and separate approval record distinct from the regular payroll cycle.

**FR-HR-083** - When a payroll run is approved for release, the system shall present a release checklist showing validation-pack status, variance-review sign-off, approval chain completion, statutory readiness status, and disbursement-channel readiness; the run shall not move to `approved` until every mandatory checklist item is satisfied or formally waived by an authorised approver.
