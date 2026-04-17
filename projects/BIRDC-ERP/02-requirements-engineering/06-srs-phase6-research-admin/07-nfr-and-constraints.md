# 4. Non-Functional Requirements — Phase 6

## 4.1 Performance

**NFR-P6-001**
The PPDA procurement register export (Excel, up to 500 rows) shall generate within 15 seconds measured from the Export button click to the file download initiation in the browser. Measurement: timed in a browser integration test with a 500-transaction seed dataset.

**NFR-P6-002**
The audit log search (any filter combination) shall return results within 3 seconds for a result set of up to 10,000 records. Measurement: MySQL EXPLAIN analysis confirming index coverage on all filterable columns (user_id, action, created_at, table_name, record_id).

**NFR-P6-003**
The system health dashboard real-time metrics shall refresh within 2 seconds of the configured refresh interval trigger, with server-side metric collection completing within 1 second. Measurement: browser timing API measurement of dashboard API response time.

**NFR-P6-004**
Asset depreciation GL auto-posting at period end shall process all active depreciable assets and complete GL entries for all of them within 60 seconds for an asset register of up to 500 assets. Measurement: timed in a PHPUnit integration test with a 500-asset seed dataset.

## 4.2 Security

**NFR-P6-005**
The system administration panel at `/public/admin/` shall enforce IP address allowlisting configured by the IT Administrator. Access attempts from IP addresses outside the allowlist shall receive HTTP 403 at the web server level, before reaching the application layer. `[CONTEXT-GAP: GAP-013]`

**NFR-P6-006**
All external integration API credentials (EFRIS, MTN MoMo, Airtel Money, Africa's Talking) stored in the database shall be encrypted with AES-256. The encryption key shall reside in the server `.env` file and shall not be accessible to the application database user. Any credentials in `.env` files shall be excluded from version control via `.gitignore`.

**NFR-P6-007**
The role and permission matrix enforcement at API layer shall be validated by a PHPUnit test suite covering: access to each protected endpoint with an insufficient role (expected: HTTP 403), access with the correct role (expected: HTTP 200), and access with an expired JWT (expected: HTTP 401). Minimum 80% coverage of permission enforcement code paths.

## 4.3 Reliability

**NFR-P6-008**
Backup execution shall not interfere with user activity. MySQL `mysqldump` shall run with `--single-transaction` flag for InnoDB tables to produce a consistent snapshot without locking tables. Verification: a PHPUnit test confirms that database writes during a backup run complete successfully without deadlock.

**NFR-P6-009**
Scheduled report delivery failures shall not propagate to other scheduled reports. Each report delivery runs in an independent PHP process; a fatal error in one report generation shall not prevent other scheduled reports from executing in the same run window.

## 4.4 Maintainability

**NFR-P6-010**
All external integration connectors (EFRIS, MTN MoMo, Airtel Money, ZKTeco, Africa's Talking) shall implement a common PHP interface `IntegrationConnectorInterface` with methods: `testConnection()`, `send()`, `getStatus()`, and `getErrorLog()`. Adding a new integration provider shall require only a new connector class implementing this interface and a configuration record; no changes to existing connectors are required (DC-007).

**NFR-P6-011**
All document management operations (upload, version, access check, audit log write) shall be encapsulated in a `DocumentService` class. No other module shall write directly to document tables; all access shall be mediated through this service, maintaining architectural integrity and enabling testing in isolation.

## 4.5 Auditability

**NFR-P6-012**
The complete system audit log shall satisfy the requirements of Uganda Companies Act 2012 (7-year retention), Uganda Income Tax Act (7-year retention for financial records), and Uganda Data Protection and Privacy Act 2019 (access records for personal data). The IT Administrator shall be able to generate a PPDA-audit-ready export of all procurement document activity for any financial year within 60 seconds.

# 5. External Interface Requirements

## 5.1 PPDA Audit Interface

The PPDA procurement register export (FR-ADM-005) shall produce an Excel file formatted for direct submission to PPDA auditors. The column layout shall match the PPDA standard procurement register format. `[CONTEXT-GAP: GAP-007]`

## 5.2 OAG Audit Interface

The audit log export (FR-IT-013) shall produce a PDF report usable by OAG Uganda auditors without further transformation. The report format shall include a cover page with BIRDC entity details, audit period, and the certification statement that the log is system-generated and unmodified.

## 5.3 Africa's Talking SMS Gateway

The system shall integrate with Africa's Talking SMS API for sending payment confirmation SMS messages to farmers and casual workers. API credentials are configured in the IT Administration panel (FR-IT-027). The integration shall use HTTPS POST to the Africa's Talking messaging endpoint and log all delivery receipts.

## 5.4 EFRIS Queue Interface

The EFRIS submission queue status visible in the system health dashboard (FR-IT-033) is read from the EFRIS integration module (F-018). F-017 provides a read-only view; the EFRIS submission logic resides in F-018. This interface is an internal service call between modules.

# 6. Open Items and Context Gaps

The following gaps must be resolved before the tagged requirements can be fully specified or tested:

| Gap ID | Requirement(s) Affected | Description | Owner |
|---|---|---|---|
| GAP-007 | FR-ADM-001, FR-ADM-005, FR-ADM-006 | Exact PPDA procurement threshold values (UGX) for BIRDC/PIBID | BIRDC Administration / Peter |
| GAP-013 | NFR-P6-005, FR-IT-031 | Server hardware specifications at BIRDC Nyaruzinga | BIRDC IT |
