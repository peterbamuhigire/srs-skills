# Non-Functional Requirements

## 8.1 Overview

This section defines measurable non-functional requirements (NFRs) for the Sales Agents and Commissions module. Each NFR specifies a threshold, a measurement condition, and a test oracle. Qualitative descriptors such as "fast" or "reliable" are not used without a corresponding IEEE-982.1 metric.

## 8.2 Performance

**NFR-AGENT-001** — The system shall respond to all interactive page load requests (agent list, attribution report, portal dashboard, commission run summary) within 3 seconds at the 95th percentile (P95) under normal load, defined as up to 100 concurrent users per tenant.

**Measurement:** Load test using 100 concurrent virtual users making sequential page requests over a 10-minute period. P95 response time ≤ 3,000 ms is the pass criterion.

---

**NFR-AGENT-002** — The commission run batch calculation shall process up to 500 agents within 120 seconds for a single run. For tenants with more than 500 agents, the system shall process agents in configurable batches of 500 and complete each batch within 120 seconds.

**Measurement:** Time the run from status transition `Calculating` to `Pending Approval` for a tenant seeded with exactly 500 agents and 30 days of attribution data. Elapsed time ≤ 120 seconds is the pass criterion.

---

**NFR-AGENT-003** — The mobile money bulk payment submission shall transmit all payment records to the gateway within 30 seconds of the **Initiate Payment** action for a batch of up to 500 agents.

**Measurement:** Time from user confirmation of **Initiate Payment** to receipt of the gateway batch acceptance acknowledgement. ≤ 30 seconds is the pass criterion.

---

**NFR-AGENT-004** — The agent self-service portal shall remain responsive under 200 concurrent authenticated agent sessions per tenant, with P95 response time ≤ 2 seconds for all portal read operations.

**Measurement:** Load test with 200 concurrent authenticated sessions performing sales view and commission statement reads. P95 ≤ 2,000 ms is the pass criterion.

## 8.3 Reliability and Availability

**NFR-AGENT-005** — The module shall maintain a monthly uptime of ≥ 99.5%, measured as the percentage of minutes in a calendar month during which all core functions (attribution, commission run, portal access) are available. Scheduled maintenance windows (maximum 4 hours per month, communicated 48 hours in advance) are excluded from the uptime calculation.

**Measurement:** Infrastructure monitoring (e.g., UptimeRobot or equivalent) sampling all core endpoint health checks every 60 seconds. Monthly uptime ≥ 99.5% (≤ 216 minutes downtime per month, excluding maintenance) is the pass criterion.

---

**NFR-AGENT-006** — The commission run calculation engine shall be idempotent: re-running a calculation for a run in `Calculating` status (e.g., after a crash recovery) shall produce identical results to the original run without creating duplicate ledger entries.

**Measurement:** Simulate a mid-calculation failure, recover, and re-run. Verify the final ledger row count equals the expected agent count (no duplicates) and all amounts match the expected values.

---

**NFR-AGENT-007** — All financial data writes (attribution records, commission ledger entries, remittance records, payment confirmations) shall be persisted to durable storage within 1 second of the user action that triggered them. Data shall not be lost in the event of an application server failure after this 1-second window.

**Measurement:** Introduce an application server hard stop immediately after a financial write. On recovery, verify the write is present in the database.

## 8.4 Security

**NFR-AGENT-008** — All agent portal data transmissions shall use TLS 1.2 or higher. HTTP (unencrypted) connections to the portal shall be automatically redirected to HTTPS with a 301 status code. The system shall reject any TLS handshake using cipher suites weaker than AES-128.

**Measurement:** SSL Labs scan of the portal domain must return grade A or A+. Attempting HTTP access must return 301. Attempting a connection with a weak cipher must result in a TLS handshake failure.

---

**NFR-AGENT-009** — All Role-Based Access Control (RBAC) enforcement shall occur server-side. No client-side flag, header, or token manipulation shall grant access to data or actions beyond the authenticated user's assigned role. The following roles and their access boundaries shall be enforced:

| Role | Access |
|---|---|
| `AgentAdmin` | Full CRUD on agent records, rules, targets, runs, stock, remittances |
| `CommissionApprover` | Read commission runs; approve or reject runs; no edit on records |
| `TerritoryManager` | Read agents and attribution for assigned territory; read-only on runs |
| `Agent` | Portal only: own sales, commissions, targets, stock balance, daily summaries |

**Measurement:** Attempt to perform a destructive operation (e.g., edit agent record) while authenticated as `Agent` or `CommissionApprover`. The system must return 403 Forbidden for all out-of-role requests.

---

**NFR-AGENT-010** — The system shall retain a complete, immutable audit log of all write operations on agent records, commission rules, attribution records, commission run records, and payment records. Each audit entry shall record the **Timestamp** (UTC), **User ID**, **Tenant ID**, **Entity Type**, **Entity ID**, **Action** (`CREATE`, `UPDATE`, `DELETE`, `APPROVE`, `REJECT`, `PAY`), and the **Previous Value** and **New Value** for any changed fields. Audit log entries shall not be deletable by any user role, including `AgentAdmin`. Logs shall be retained for a minimum of 7 years in line with Uganda's tax record retention requirements under the Income Tax Act.

**Measurement:** Verify no DELETE or TRUNCATE endpoint exists for audit log tables. Confirm logs persist for a test tenant seeded 7 years prior (or simulate with a retention policy dry-run). Confirm every write operation produces a corresponding audit entry.
