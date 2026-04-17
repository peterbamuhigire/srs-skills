## 3. Task Description Template

Every task assigned to a developer must include a task description using the following structure. Fields marked (Required) must be completed. Fields marked (If applicable) must be completed when the condition applies; if not applicable, write "N/A" with a one-sentence justification.

---

**Task title:** [Short descriptive title — max 80 characters]

**FR reference(s) (Required):** [FR-XXX-NNN, or BR-xxx / DC-xxx if no FR applies]

**Milestone (Required):** [M-001 through M-007]

**Acceptance criteria (Required):**

1. [Deterministic pass/fail criterion — no judgment calls]
2. [Deterministic pass/fail criterion — no judgment calls]
3. [Add as many as needed — minimum 1]

**Applicable business rules (If applicable):** [BR-xxx list with a one-line statement of how each rule applies to this task]

**Database tables affected (Required):** [Table names; for new tables, include draft schema or link to design document]

**GL posting required (Required):** Yes / No
If Yes — Debit: [account code and name] / Credit: [account code and name]

**API endpoints required (If applicable):**

- [HTTP method] [URL path] — [brief description]
  - Request: [field names and types]
  - Response (success): [field names and types, HTTP status]
  - Response (error): [error codes and HTTP status]

**RBAC — roles permitted (Required):** [Role name(s) and any conditions or segregation of duties constraints]

**Audit log event (If applicable):** [Event type string, affected table, record field — or N/A with justification]

**Blocking dependencies (Required):** [Task IDs or "None"]

**External dependency gaps (Required):** [GAP-xxx list with resolution status — or "None"]
If any critical GAP is unresolved, this task is NOT READY. State the gap and its current status.

**Effort estimate (Required):** [N developer-days — confirmed by Peter Bamuhigire on: date]

**Assigned developer (Required):** [Developer name — availability confirmed for: start date]

---

**DoR sign-off:** Peter Bamuhigire confirms this task meets all Definition of Ready criteria: [ ]
