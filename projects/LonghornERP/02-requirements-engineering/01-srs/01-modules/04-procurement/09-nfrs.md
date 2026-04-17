# Non-Functional Requirements — Procurement

## 9.1 Performance

**NFR-PROC-001** — The system shall load the purchase order list view with ≤ 500 ms response time at the P95 percentile for a tenant dataset of ≤ 50,000 POs under normal operating load (up to 50 concurrent users).

**NFR-PROC-002** — The three-way match calculation for a single supplier invoice shall complete within 2 seconds regardless of the number of linked PO and GRN lines.

## 9.2 Reliability

**NFR-PROC-003** — The Procurement module shall maintain 99.5% uptime measured monthly, excluding scheduled maintenance windows of ≤ 4 hours per month announced ≥ 24 hours in advance.

**NFR-PROC-004** — All GRN confirmations and payment posting operations shall be executed within a single database transaction; if any step fails, the system shall roll back the entire transaction and return the records to their pre-submission state.

## 9.3 Security

**NFR-PROC-005** — Access to supplier bank account details shall be restricted to users with the `finance.supplier_banking.view` permission; bank account numbers shall be masked (showing last 4 digits only) in list views and reports unless the user holds `finance.supplier_banking.full` permission.

**NFR-PROC-006** — The system shall enforce role-based approval thresholds; any attempt to approve a PO or payment above the approver's authorised limit shall be rejected with an HTTP 403 response and an audit log entry.

## 9.4 Auditability

**NFR-PROC-007** — Every state transition in the procurement workflow (PR submission, PR approval, PO creation, PO approval, GRN, invoice capture, three-way match override, payment) shall generate an immutable audit log record containing: entity type, entity ID, old status, new status, acting user ID, IP address, and UTC timestamp.

**NFR-PROC-008** — Supplier invoice and payment records shall be retained for a minimum of 10 years in compliance with the Uganda Companies Act and URA audit requirements; deletion of these records shall be prohibited at the application layer.

## 9.5 Usability

**NFR-PROC-009** — A trained procurement officer shall be able to create and issue a complete PO (from approved PR) without assistance within 5 minutes, as measured by user acceptance testing with at least 5 representative users.

**NFR-PROC-010** — The procurement dashboard shall display: (a) PRs awaiting the current user's approval, (b) POs pending issuance, (c) GRNs awaiting match, and (d) overdue supplier payments — all loaded within 1 second on page access.
