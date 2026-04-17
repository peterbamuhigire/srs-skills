## 2. Readiness Criteria

A feature or task is READY to be assigned to a developer only when ALL of the following criteria are satisfied and documented in the task description.

### 2.1 Requirements Reference

- The task description cites the functional requirement identifier(s) from the relevant BIRDC ERP Software Requirements Specification document (e.g., FR-SAL-001, FR-POS-003).
- If a task has no corresponding FR identifier, it must be traced to a business rule (BR-xxx), a design constraint (DC-xxx), or a documented gap resolution — or it must not be implemented.

### 2.2 Acceptance Criteria

- Acceptance criteria are written as deterministic pass/fail statements — no judgment calls allowed.
- Each criterion must be testable by an automated test or a specific, reproducible manual test procedure.
- Examples of unacceptable acceptance criteria: "the report looks correct"; "the system feels fast". These fail the verifiability standard.
- Examples of acceptable acceptance criteria: "the Trial Balance debit total equals the credit total to 2 decimal places"; "product search returns results within 500 ms at P95 under simulated load of 50 concurrent users".

### 2.3 Applicable Business Rules

- All business rules (BR-001 through BR-018) that govern the task's behaviour are explicitly listed in the task description.
- For each listed business rule, the task description states how compliance will be verified.

### 2.4 Database Tables Affected

- Every database table that will be created, altered, or read by this task is identified by name.
- For new tables, a draft schema (column names, data types, constraints, foreign keys) is included in the task description or linked design document.
- For existing tables, the specific columns affected by the task are named.

### 2.5 GL Posting Requirement

- The task description explicitly states whether this task involves a General Ledger posting: **Yes** or **No**.
- If Yes, the debit account(s) and credit account(s) are named using the BIRDC Chart of Accounts account codes and names (e.g., "DR 1300 Trade Receivables / CR 4100 Revenue from Tooke Sales").
- If Yes, the task is not Ready until the GL posting logic is confirmed by Peter Bamuhigire.

### 2.6 API Endpoints Required

- Every API endpoint required by this task is listed with:
  - HTTP method (GET, POST, PUT, PATCH, DELETE).
  - Full URL path (e.g., `POST /api/v1/sales/invoices`).
  - Request payload schema (field names and data types).
  - Response schema (field names, data types, and HTTP status codes for success and error cases).

### 2.7 RBAC — Roles Permitted

- The task description specifies which system roles are permitted to perform each action exposed by this task.
- Role names must correspond to the BIRDC ERP Role and Permission Matrix (F-017).
- If a role is permitted to perform the action only under a condition (e.g., only within their assigned territory, or only for records they created), that condition is explicitly stated.
- If the action is restricted by segregation of duties (BR-003), the restriction is explicitly stated: "the user who created this record must not be the user who approves it."

### 2.8 Audit Log Event

- The task description specifies the event type string that `AuditLogService` must record for each state-changing operation in this task.
- Example: "On invoice confirmation: log event type `invoice.confirmed`, affected table `tbl_invoices`, record `invoice_id`."
- If the task has no state-changing operations, this field is marked "N/A" with justification.

### 2.9 Blocking Dependencies

- All tasks that must be completed before this task can begin are listed by task ID or feature name.
- A task with unresolved blocking dependencies is not Ready and must not be assigned.

### 2.10 External Dependency Gaps

- All open gap items (GAP-xxx from the Gap Analysis document) that affect this task are listed.
- If a listed gap is critical (i.e., the task cannot be implemented or tested without the gap being resolved), the task is **not Ready** until the gap is closed.
- If a listed gap is non-critical (i.e., the task can be implemented with a mock and swapped in when the gap is resolved), this is explicitly noted and the mock approach is described.
- The current resolution status of each listed gap is documented in the task description.

### 2.11 Effort Estimate

- The effort estimate for this task in developer-days is agreed between Peter Bamuhigire and the assigned developer before the task is marked Ready.
- The estimate accounts for: implementation, unit tests, integration tests, PHPDoc, staging deployment, and smoke test.
- An estimate that has not been reviewed and agreed is not valid — an unreviewed estimate from a developer without Peter Bamuhigire's confirmation means the task is not Ready.

### 2.12 Developer Availability Confirmed

- The developer assigned to this task has confirmed availability to begin work on the specified start date.
- If the developer is shared across multiple tasks, the time allocation is explicitly stated (e.g., "50% of working hours for this task from [date] to [date]").
- A task assigned to a developer who has not confirmed availability is not Ready.
