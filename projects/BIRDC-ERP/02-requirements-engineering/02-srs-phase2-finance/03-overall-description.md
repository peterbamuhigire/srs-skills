# 2. Overall Description

## 2.1 Product Perspective

The Financial Core (Phase 2) is the accounting backbone of the BIRDC ERP. It is not a standalone subsystem — it is an integrated financial engine that receives automated GL posting triggers from all 17 operational modules across all 7 delivery phases. Phase 2 modules operate within the broader BIRDC ERP single-tenant web application deployed on BIRDC-owned infrastructure at Nyaruzinga, Bushenyi.

The system implements IFRS for SMEs double-entry accounting for BIRDC commercial reporting and simultaneously tracks PIBID parliamentary budget votes per Design Covenant DC-004. Every financial transaction in the system — regardless of originating module — produces a balanced journal entry in the GL automatically (DC-003).

The Executive Dashboard Android app (Mobile App 4) provides the Finance Director and Director with real-time read-only access to Trial Balance summary, P&L snapshot, cash position, and budget variance alerts via push notification.

## 2.2 Product Functions Summary

Phase 2 delivers the following primary functions:

- **F-005 — Financial Accounting and General Ledger:** Double-entry bookkeeping engine; Chart of Accounts management; Journal Entry lifecycle management; GL hash chain integrity; financial statement generation (P&L, Balance Sheet, Cash Flow, Trial Balance); multi-currency with FX gain/loss; dual-mode reporting; accounting period control.
- **F-006 — Accounts Receivable:** Customer and agent AR tracking; AR aging analysis; agent receivable tracking distinct from customer AR; credit control and credit hold workflow; customer statements; payment receipt allocation.
- **F-007 — Accounts Payable:** Vendor invoice registration with three-way matching; AP aging and payment scheduling; vendor payments with WHT; farmer bulk payment via mobile money; payment authorisation workflow; vendor credit notes.
- **F-008 — Budget Management:** Parliamentary budget vote management (July–June); commercial budget management; simultaneous dual-mode tracking; budget vs. actual variance on demand; threshold alerts at 80%, 95%, and 100%; Director-override with audit log; budget import via Excel and revision workflow.

## 2.3 User Classes and Characteristics

| User Class | Module Access | Technical Proficiency |
|---|---|---|
| Finance Director (STK-002) | All Phase 2 modules; GL integrity check; period close; budget approval | High — ICPAU-certified accountant |
| Finance Manager (STK-002 proxy) | Journal entry approval; payment authorisation; payroll lock (Phase 5) | High |
| Accounts Assistants (STK-018, ~8 users) | AR, AP data entry; payment receipts; journal entry drafting | Medium — daily ERP users |
| Director (STK-001) | Budget override; executive dashboards; Director-level approvals | Medium — management user |
| Parliament Budget Committee (STK-004) | Parliamentary vote reports (read-only, exported) | Low — report recipients |
| Auditor General (OAG, STK-026) | GL hash chain integrity report; full audit trail; exported statements | High — audit professional |
| IT Administrator (STK-003) | System administration; period configuration; chart of accounts structure | High — technical |

Per Design Covenant DC-001, every screen an Accounts Assistant uses daily must be self-discoverable. A newly hired Accounts Assistant must post a journal entry correctly without reading a manual.

## 2.4 Operating Environment

- **Deployment:** Single-tenant, on-premise, BIRDC Nyaruzinga server
- **Backend:** PHP 8.3+, MySQL 9.1 InnoDB, PSR-4/PSR-12, Service/Repository pattern
- **Frontend:** Bootstrap 5, Tabler admin UI, jQuery, Alpine.js, ApexCharts
- **PDF output:** mPDF (financial statements, payment vouchers, WHT certificates)
- **Excel/CSV:** PhpSpreadsheet (budget import, payment files, GL export)
- **Email delivery:** PHPMailer with SMTP TLS (statements, alerts, notifications)
- **Mobile access:** Executive Dashboard Android app (Kotlin, Jetpack Compose, JWT API)
- **Minimum Android version:** Android 8.0 (API 26)

## 2.5 Design and Implementation Constraints

All Phase 2 requirements must satisfy the 7 Design Covenants:

| DC | Constraint Applied to Phase 2 |
|---|---|
| DC-001 | Zero mandatory training — GL posting, AR/AP entry, and budget review screens must be self-discoverable |
| DC-002 | Chart of accounts structure, WHT rates, FX rates, budget vote codes, and accounting periods configurable via UI by Finance Director — no developer involvement |
| DC-003 | Every financial transaction creates an immutable audit trail automatically — 7-year retention enforced |
| DC-004 | PIBID parliamentary votes and BIRDC commercial IFRS accounts tracked simultaneously; separated and consolidated reporting always available |
| DC-005 | Not applicable to Phase 2 web modules (offline-first applies to POS and field apps) |
| DC-006 | All financial data stored on BIRDC's own servers in Uganda — no cloud financial data |
| DC-007 | All business rules (WHT rates, budget thresholds, FX rates) in configuration tables, not code |

## 2.6 Assumptions and Dependencies

- Phase 1 modules (F-001 to F-004) are deployed and operational as GL posting sources before Phase 2 go-live.
- The Finance Director resolves GAP-012 (Chart of Accounts structure — 1,307 accounts) before GL database design is finalised.
- GAP-014 (legacy accounting software data migration) is resolved before go-live cutover.
- MTN MoMo Business API and Airtel Money API credentials (GAP-002, GAP-003) are obtained before farmer payment testing.
- The Uganda Income Tax Act WHT rate of 6% is the current applicable rate; Finance Director confirms this before build.
