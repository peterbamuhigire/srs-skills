# Non-Functional Requirements for the Project Management Module

## 8.1 Overview

Non-functional requirements (NFRs) define the quality and constraint envelope within which all functional behaviour specified in Sections 2 through 7 must operate. Each NFR is assigned a unique identifier in the `NFR-PROJ-NNN` series and is stated with a specific, measurable metric per IEEE 982.1.

## 8.2 Performance

**NFR-PROJ-001:** The system shall render the Gantt chart for a project containing up to 200 WBS tasks in ≤ 3 seconds at P95, measured from request initiation to full chart paint in the browser under a concurrent load of 30 active sessions on the same tenant.

**NFR-PROJ-002:** The system shall load the Portfolio Dashboard displaying up to 100 projects in ≤ 4 seconds at P95 under a concurrent load of 20 active sessions.

**NFR-PROJ-003:** The system shall complete a T&M billing calculation (FR-PROJ-044) for a project with up to 500 timesheet lines in ≤ 5 seconds at P95.

**NFR-PROJ-004:** The system shall load any individual project detail screen (including P&L summary, cost ledger, and milestone list) in ≤ 2 seconds at P95 under a concurrent load of 50 active sessions on the same tenant.

**NFR-PROJ-005:** The system shall complete a Project P&L refresh (FR-PROJ-051) in ≤ 5 seconds at P95 for a project with up to 1,000 cost ledger entries and 200 invoice lines.

**NFR-PROJ-006:** The system shall update the project cost ledger upon PO, payroll, or expense reversal (FR-PROJ-042) within 60 seconds of the source document reversal being confirmed, with no user action required.

## 8.3 Data Integrity

**NFR-PROJ-007:** The system shall enforce referential integrity between project cost ledger entries and their source documents (PO lines, payroll timesheet lines, expense claim lines). Any attempt to delete a source document that has cost ledger entries in a confirmed project shall be rejected at the database layer with a foreign key constraint error.

**NFR-PROJ-008:** The system shall ensure that all billed timesheet lines (status = Billed) are immutable. Any attempt to modify the hours, rate, or date of a billed timesheet line via the application API shall be rejected with HTTP 422 and the error "Cannot modify a billed timesheet line."

**NFR-PROJ-009:** The system shall prevent concurrent modification conflicts on the project master record using optimistic locking. If 2 users attempt to save conflicting edits to the same project record simultaneously, the second save shall return HTTP 409 with the error "Project record has been modified by another user. Please reload and re-apply your changes."

## 8.4 Availability

**NFR-PROJ-010:** The Project Management module shall be available 99.5% of each calendar month, excluding scheduled maintenance windows announced ≥ 48 hours in advance. Availability is measured as the ratio of successful health-check responses to total health-check requests over the month.

## 8.5 Security

**NFR-PROJ-011:** All Project Management module API endpoints shall require a valid authenticated session token. Unauthenticated requests shall return HTTP 401 within ≤ 200 ms.

**NFR-PROJ-012:** Role-based access control checks for project operations (create project, approve timesheet, initiate billing, view portfolio) shall be enforced server-side on every request. Client-side UI hiding of controls does not satisfy this requirement.

**NFR-PROJ-013:** Project data belonging to Tenant A shall never be accessible to users of Tenant B. All project queries shall include a `tenant_id` filter enforced at the data access layer. Violation of tenant isolation shall be treated as a critical security incident.

**NFR-PROJ-014:** All project management API traffic shall be transmitted over TLS 1.2 or higher. Unencrypted HTTP connections shall be rejected with HTTP 301 redirect to HTTPS.

## 8.6 Auditability

**NFR-PROJ-015:** Every write operation on the `projects`, `project_tasks`, `project_milestones`, `project_cost_ledger`, `project_timesheets`, `project_billing_events`, and `project_subcontractors` tables shall produce an audit log entry within the same database transaction, recording table, record ID, operation (INSERT/UPDATE), changed fields, old values, new values, user ID, and timestamp.

**NFR-PROJ-016:** Audit log entries for the Project Management module shall be retained for a minimum of 7 years, consistent with the Uganda Companies Act statutory record-keeping requirement. Entries older than 7 years may be archived to cold storage but must remain retrievable within 72 hours of a retrieval request.

## 8.7 Scalability

**NFR-PROJ-017:** The system shall support a single tenant operating up to 500 concurrent active projects without performance degradation below the thresholds specified in Section 8.2.

**NFR-PROJ-018:** The system shall support a WBS with up to 1,000 tasks per project without degradation in the task list load time beyond ≤ 3 seconds at P95.
