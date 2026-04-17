# 7. Non-Functional Requirements — Phase 2 Financial Core

## 7.1 Performance Requirements

### NFR-PERF-001

The Trial Balance for all 1,307 accounts must be generated and rendered within 3,000 ms at the 95th percentile (P95) under normal operating load (defined as ≤ 25 concurrent web sessions on BIRDC server hardware).

### NFR-PERF-002

GL Journal Entry list queries filtered to a 12-month date range must return results within 1,000 ms at P95 under normal load.

### NFR-PERF-003

The AR Aging dashboard for all active customer accounts must render within 2,000 ms at P95. The AP Aging dashboard for all vendors must render within 2,000 ms at P95.

### NFR-PERF-004

Account lookup via Select2 searchable dropdown (FR-GL-039) must return matching results within 300 ms at P95 for search strings of 3+ characters against the full 1,307-account Chart of Accounts.

### NFR-PERF-005

Financial statement generation (P&L, Balance Sheet, Cash Flow) must complete within 5,000 ms at P95 for a full fiscal year's data.

### NFR-PERF-006

The GL hash chain integrity check for a single account's 12-month transaction history must complete within 60,000 ms (60 seconds). A full system-wide integrity check may run as a background job with no UI timeout constraint.

## 7.2 Security Requirements

### NFR-SEC-001

All Phase 2 module API endpoints enforce the 8-layer authorisation model (Role → Page → API endpoint → UI element → Location → Time → Conditional rules → Object ownership). No financial transaction endpoint is accessible without a valid authenticated session or JWT token.

### NFR-SEC-002

The segregation of duties constraint (BR-003) is enforced at the API layer for all Phase 2 operations: journal entry approval, vendor payment authorisation, remittance verification, budget override. A direct API request constructed to bypass the UI must be rejected with HTTP 403 if the SOD constraint is violated.

### NFR-SEC-003

All Phase 2 financial data is stored on BIRDC-owned servers in Uganda (DC-006). No financial data is transmitted to or stored on external cloud infrastructure.

### NFR-SEC-004

The Finance Director, BIRDC Director, and IT Administrator accounts require Two-Factor Authentication (TOTP, Google Authenticator compatible) for all Phase 2 module access.

### NFR-SEC-005

GL audit log records (`tbl_audit_log`) cannot be updated or deleted by any application user at any permission level. DELETE and UPDATE operations on the audit log table are denied at the database level via MySQL 9.1 row-level permissions.

### NFR-SEC-006

All financial data in transit between client browser and server is encrypted with TLS 1.3. All REST API calls from the Executive Dashboard mobile app use HTTPS with TLS 1.3.

### NFR-SEC-007

SQL injection is prevented across all Phase 2 database queries via 100% PDO prepared statements. No string-concatenated SQL queries exist in any Phase 2 service or repository class.

## 7.3 Reliability and Availability Requirements

### NFR-REL-001

The BIRDC ERP financial modules must maintain a daily automated database backup. The backup must be tested for restore capability monthly. Backup retention: 90 days on-site plus an encrypted offsite copy (USB or remote).

### NFR-REL-002

GL auto-posting from operational modules (FR-GL-012 through FR-GL-018) must execute within the same database transaction as the originating operational record. If the GL posting fails, the originating transaction (invoice confirmation, payment, etc.) must be rolled back entirely — partial commits that create GL orphans are not permitted.

### NFR-REL-003

The farmer bulk payment API call (FR-AP-015) must implement exponential backoff retry logic with a maximum of 3 retry attempts per farmer record in the event of API timeout. After 3 failures, the farmer is placed in the `manual_payment_required` queue; the system does not silently discard failed payments.

## 7.4 Maintainability Requirements

### NFR-MAIN-001

All Phase 2 financial services (GL posting service, payment service, budget utilisation service) must achieve ≥ 80% PHPUnit test coverage for all financial calculation paths (GL balance updates, WHT calculation, FX conversion, budget utilisation percentage, FIFO remittance allocation).

### NFR-MAIN-002

All business rules configurable via DC-002 (WHT rate, budget alert thresholds, payment authorisation limits, FX rates, fiscal year dates, vote code mappings, GL posting rules) must be stored in named configuration tables, not in PHP constants, `.env` variables, or hardcoded values in service classes.

### NFR-MAIN-003

The GL auto-posting rule table (`tbl_gl_posting_rules`) must be documented with a configuration guide that describes how to add a new module's posting rule without developer assistance. This guide is a deliverable of Phase 2.

## 7.5 Audit and Compliance Requirements

### NFR-COMP-001

All financial records (GL entries, invoices, payments, budget records) must be retained for a minimum of 7 years from the date of creation, per Uganda Companies Act Cap 110 and Uganda Income Tax Act Cap 340. Automated deletion or archival that would remove records within the 7-year retention window is prohibited.

### NFR-COMP-002

The GL hash chain (BR-013) must use SHA-256 as the hashing algorithm. The hash input must be a deterministic serialisation of the GL entry fields: entry ID, account code, debit amount, credit amount, date, JE number, and the previous entry hash. The serialisation format must be documented in the technical specification so the Finance Director or OAG auditor can independently verify the chain.

### NFR-COMP-003

Withholding Tax calculations must comply with the Uganda Income Tax Act Cap 340 at the rate currently configured in the system. The Finance Director must update the WHT rate configuration whenever URA publishes a rate change; the configuration audit trail records the date of any rate change.

### NFR-COMP-004

The system must generate a parliamentary budget utilisation report in a format acceptable for submission to the Parliament Budget Committee (STK-004) and OAG Uganda (STK-026) without manual reformatting. The report format is defined collaboratively with the Finance Director during Phase 2 UAT.

## 7.6 Usability Requirements

### NFR-USE-001

Per Design Covenant DC-001, a newly hired Accounts Assistant must be able to post a balanced journal entry correctly on their first attempt without reading a manual. The journal entry screen must provide: real-time debit/credit running total display, inline error messages for unbalanced entries, and account search with account type labelling.

### NFR-USE-002

All financial reports must be accessible within 3 clicks from the module's main dashboard. No financial report requires more than 3 sequential navigation steps.

### NFR-USE-003

Error messages returned to users on failed transactions must state: what happened, why it was blocked, and what the user must do to resolve the issue. Error codes (e.g., `ERR_THREE_WAY_MATCH_INCOMPLETE`) are for developer reference; the user-facing message must be plain English.
