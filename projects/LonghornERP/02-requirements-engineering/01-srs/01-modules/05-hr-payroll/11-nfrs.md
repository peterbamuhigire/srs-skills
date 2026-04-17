# Non-Functional Requirements — HR and Payroll

## 11.1 Performance

**NFR-HR-001** — A payroll run for ≤ 500 active employees shall complete within 60 seconds from initiation to confirmation-ready state, measured under normal database load.

**NFR-HR-002** — The ESS portal payslip list view shall load within 1 second at P95 for a single authenticated employee session.

**NFR-HR-003** — The attendance monthly summary report for a department of ≤ 200 employees shall render within 3 seconds.

## 11.2 Reliability

**NFR-HR-004** — Payroll run computation shall execute within a single database transaction; if any employee's computation fails, the system shall roll back all computations for the entire run and present a descriptive error identifying the failing employee record.

**NFR-HR-005** — The HR and Payroll module shall maintain 99.5% uptime measured monthly, excluding scheduled maintenance windows announced ≥ 24 hours in advance.

## 11.3 Security and Privacy

**NFR-HR-006** — Employee salary, TIN, national ID, and bank account data shall be encrypted at rest using AES-256; these fields shall not be exposed in API responses to users lacking the corresponding RBAC permission.

**NFR-HR-007** — The ESS portal shall enforce session timeout of ≤ 30 minutes of inactivity; all ESS API endpoints shall require a valid JWT with the `ess.employee` scope.

**NFR-HR-008** — In compliance with the Uganda Data Protection and Privacy Act 2019, employee personal data shall not be shared with third parties except for statutory reporting to URA, NSSF, and NITA; the system shall log every export of employee data including destination, exported fields, and acting user `[CONTEXT-GAP: GAP-007 — data protection compliance specification]`.

## 11.4 Auditability

**NFR-HR-009** — Every payroll run shall produce an immutable payroll journal in the GL, an immutable payslip PDF per employee, and an audit log entry recording: run ID, acting user, total employees processed, total gross pay, total PAYE, total net pay, and UTC timestamp.

**NFR-HR-010** — All employee data changes, leave approvals, and payroll approvals shall generate audit log records with old value, new value, acting user, and timestamp; these records shall be retained for 10 years.

## 11.5 Compliance

**NFR-HR-011** — The system shall surface a compliance dashboard showing: PAYE e-return status (submitted/pending) per period, NSSF schedule status per period, and any outstanding statutory obligations; overdue items shall be flagged with a visual alert.
