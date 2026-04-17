---
title: "Test Plan — Maduuka POS and Business Management Platform, Phase 1"
author: "Chwezi Core Systems"
date: "2026-04-05"
version: "1.0"
status: "Draft"
standard: "IEEE Std 829-2008"
---

# Test Plan: Maduuka POS and Business Management Platform — Phase 1

**Document ID:** MADUUKA-TP-001
**Version:** 1.0
**Status:** Draft
**Prepared by:** Chwezi Core Systems
**Product Owner:** Peter Bamuhigire
**Date:** 2026-04-05
**Standard:** IEEE Std 829-2008 — Standard for Software and System Test Documentation

---

## 1. Test Plan Identifier

**Plan ID:** MADUUKA-TP-001
**Revision:** 1.0
**Parent Document:** MADUUKA-TS-001 (Test Strategy — Maduuka Phase 1)
**SRS Reference:** MADUUKA-SRS-001

This test plan is the executable companion to the Test Strategy (MADUUKA-TS-001). Whereas the strategy defines *how* testing is conducted, this plan defines *what* will be tested, *when*, *by whom*, and under *what environmental conditions* for the Phase 1 release of Maduuka.

---

## 2. Introduction

### 2.1 Purpose

This Test Plan governs all planned testing activities for Phase 1 of the Maduuka platform. It specifies the test items, features under test, test approach, pass/fail criteria, deliverables, schedule, environmental requirements, and role responsibilities required to validate the platform prior to Phase 1 production release.

### 2.2 Scope

Phase 1 delivers 10 core modules across 2 client platforms — Android (Kotlin + Jetpack Compose + Room) and Web (PHP 8.3+ / Bootstrap 5 / Tabler) — connected to a shared REST API with JWT authentication. The platform is a multi-tenant Software as a Service (SaaS) system; every data record is scoped to a `franchise_id` per **BR-001**.

This plan covers:

- All 10 Phase 1 modules (F-001 through F-010) on both platforms.
- The shared REST API layer.
- The offline sale queue and WorkManager sync mechanism (Android).
- Multi-tenant data isolation enforcement.
- Mobile money integration (MTN MoMo, Airtel Money) in sandbox mode.
- Payroll statutory compliance: PAYE, NSSF, and Local Service Tax (LST).

### 2.3 References

| Reference | Title |
|---|---|
| IEEE Std 829-2008 | Standard for Software and System Test Documentation |
| IEEE Std 1012-2016 | Standard for System, Software, and Hardware Verification and Validation |
| IEEE Std 830-1998 | Recommended Practice for Software Requirements Specifications |
| MADUUKA-SRS-001 | Maduuka Software Requirements Specification (Phase 1) |
| MADUUKA-TS-001 | Maduuka Test Strategy (Phase 1) |
| `_context/business_rules.md` | Business Rules Register (BR-001 – BR-012) |
| `_context/quality_standards.md` | Quality Standards and Performance Thresholds |
| Uganda Income Tax Act (Cap 340) | PAYE computation basis for 2024/25 tax bands |
| Uganda NSSF Act | NSSF contribution rates |
| Uganda Data Protection and Privacy Act 2019 | PII handling in test environments |

---

## 3. Test Items

The following software items are under test in Phase 1. Each item applies to both the Android application and the Web application unless explicitly noted.

| Item ID | Module | Platform |
|---|---|---|
| F-001 | Point of Sale (POS) | Android + Web |
| F-002 | Inventory and Stock Management | Android + Web |
| F-003 | Customer Management | Android + Web |
| F-004 | Supplier and Vendor Management | Android + Web |
| F-005 | Expenses and Petty Cash | Android + Web |
| F-006 | Financial Accounts and Cash Flow | Android + Web |
| F-007 | Sales Reporting and Analytics | Android + Web |
| F-008 | HR and Payroll | Android + Web |
| F-009 | Dashboard and Business Health | Android + Web |
| F-010 | Settings and Configuration | Android + Web |
| API | Shared REST API (JSON over HTTPS, JWT auth) | Backend |
| SYNC | Offline Sale Queue + WorkManager Sync | Android only |
| MT | Multi-Tenant Data Isolation (`franchise_id` scoping) | API + DB layer |

**Version under test:** Phase 1 build (version to be confirmed at test cycle start — record in Test Run Report).

**Known blockers at plan publication date:**

- MTN MoMo Business API sandbox credentials are pending (GAP-001). All MTN MoMo and Airtel Money test cases are documented but tagged `[BLOCKED: GAP-001]` and cannot be executed until sandbox access is granted.

---

## 4. Features to be Tested

### 4.1 F-001 — Point of Sale

- Product search by name, SKU, and barcode (FR-POS-001)
- ML Kit barcode scan to cart add (FR-POS-002) — Android only
- Category grid view with filter (FR-POS-003)
- Out-of-stock indicator and override (FR-POS-004)
- Cart line item add, quantity update, duplicate prevention (FR-POS-005)
- Over-stock quantity warning (FR-POS-006)
- Per-item percentage and fixed discount (FR-POS-007)
- Order-level discount (FR-POS-008)
- Hold sale — suspend, assign reference, restore (FR-POS-009, FR-POS-010)
- Cash payment change calculation (FR-POS-011)
- MTN MoMo push payment: success, failure, timeout (FR-POS-012) `[BLOCKED: GAP-001]`
- Airtel Money push payment (FR-POS-013) `[BLOCKED: GAP-001]`
- Credit sale with limit enforcement and manager override (FR-POS-014)
- Multi-payment tracking and total reconciliation (FR-POS-015)
- Stock decrement on sale completion (FR-POS-016)
- Receipt generation with all required fields (FR-POS-017)
- Bluetooth thermal printer receipt (FR-POS-018) — Android only
- WhatsApp receipt sharing (FR-POS-019)
- SMS receipt via Africa's Talking (FR-POS-020)
- Session open with opening float (FR-POS-021)
- Session close with reconciliation report (FR-POS-022)
- Receipt gap detection on session close (FR-POS-023, BR-008)
- Sale void by manager with audit log (FR-POS-024)
- Product return / refund (FR-POS-025)
- Offline sale processing with Room local storage (FR-POS-026)
- Offline sync via WorkManager on reconnect (FR-POS-027)
- Weight-based product line total calculation (FR-POS-028)
- Service item — no stock decrement (FR-POS-029)
- Web barcode scanner keyboard-event mode (FR-POS-030)

### 4.2 F-002 — Inventory and Stock Management

- Product create with required and optional fields (FR-INV-001)
- Multi-tier pricing and automatic POS price selection (FR-INV-002)
- Multiple selling units with base-unit stock conversion (FR-INV-003)
- CSV product import with validation and error reporting (FR-INV-004)
- Stock decrement on sale with immutable movement record (FR-INV-005)
- Stock increment on purchase receipt with status update (FR-INV-006)
- Reorder level alert — push notification and dashboard badge (FR-INV-007)
- Stock transfer with in-transit status and receiving confirmation (FR-INV-008)
- Stock adjustment with approval threshold enforcement (FR-INV-009, BR-005)
- Batch receipt with batch number, manufacturing date, and expiry date (FR-INV-010)
- FEFO batch selection on sale, with manager override (FR-INV-011, BR-006)
- Near-expiry batch alert at 30/60/90-day thresholds (FR-INV-012)
- Stock valuation by FIFO and weighted average cost (FR-INV-013)
- Physical stock count with freeze, variance calculation, and pending adjustment (FR-INV-014)
- Supplier return with stock decrement and credit note creation (FR-INV-015)
- Customer return with stock increment and credit note creation (FR-INV-016)
- Stock movement history report for a product (FR-INV-017)
- Slow-moving items report with configurable threshold (FR-INV-018)

### 4.3 F-003 — Customer Management

- Customer create with required and optional fields (FR-CUS-001)
- Customer group price tier auto-application at POS (FR-CUS-002)
- Customer deactivation — transaction history preserved, new sales blocked (FR-CUS-003)
- Credit sale balance increment and payment decrement in real time (FR-CUS-004)
- Payment recording against outstanding balance with receipt (FR-CUS-005)
- Debtors ageing report by 30/60/90/90+ day buckets (FR-CUS-006)
- Customer statement generation with running balance (FR-CUS-007)
- Magic link generation and delivery via WhatsApp or SMS (FR-CUS-008)
- Customer portal — read-only balance and statement access (FR-CUS-009)
- Customer map with Leaflet.js pins (FR-CUS-010) — Web only

### 4.4 F-004 — Supplier and Vendor Management

- Supplier create and profile view (FR-SUP-001, FR-SUP-002)
- Purchase order creation with PDF generation (FR-SUP-003)
- Goods receipt against PO with partial receipt and stock update (FR-SUP-004)
- Three-way purchase matching: PO vs receipt vs invoice (FR-SUP-005, BR-011)
- Supplier payment recording with partial payment support (FR-SUP-006)
- Supplier statement generation (FR-SUP-007)

### 4.5 F-005 — Expenses and Petty Cash

- Expense recording with required fields and receipt photo (FR-EXP-001, FR-EXP-002)
- Expense approval threshold enforcement and pending-approval routing (FR-EXP-003)
- Expense approval with financial account posting (FR-EXP-004)
- Petty cash disbursement and replenishment (FR-EXP-005, FR-EXP-006)
- Petty cash balance and disbursement view (FR-EXP-007)
- Recurring expense draft generation (FR-EXP-008)

### 4.6 F-006 — Financial Accounts and Cash Flow

- Payment account create (FR-FIN-001)
- Real-time account balance update on all transaction types (FR-FIN-002)
- Inter-account cash transfer with dual movement records (FR-FIN-003)
- Bank reconciliation — manual match and CSV import auto-match (FR-FIN-004, FR-FIN-005)
- Cash flow summary by account and total (FR-FIN-006)
- Daily summary — opening balance, inflows, outflows, closing balance (FR-FIN-007)

### 4.7 F-007 — Sales Reporting and Analytics

- Daily sales report grouped by payment method (FR-REP-001)
- Sales summary for date range with period comparison (FR-REP-002)
- Sales by product with revenue, cost, and gross margin (FR-REP-003)
- Top 20 sellers by revenue and quantity (FR-REP-004)
- Sales by branch with percentage share (FR-REP-005)
- Sales by cashier with void and refund counts (FR-REP-006)
- Voids and refunds report (FR-REP-007)
- Receipt gap report for closed sessions (FR-REP-008)
- CSV and PDF export within 30 seconds (FR-REP-009)
- Scheduled report delivery by email (FR-REP-010)

### 4.8 F-008 — HR and Payroll

- Staff profile create (FR-HR-001)
- Fixed-term contract with expiry reminder (FR-HR-002)
- SMS staff invitation with one-time PIN (FR-HR-003)
- Leave type definition (FR-HR-004)
- Leave request submission and push notification (FR-HR-005)
- Leave approval/rejection with balance deduction (FR-HR-006)
- Leave balances report (FR-HR-007)
- Clock-in/out with GPS timestamp and duplicate warning (FR-HR-008)
- Manual daily attendance recording (FR-HR-009)
- Salary structure configuration (FR-HR-010)
- Monthly payroll run: gross pay, PAYE, NSSF, net pay calculation (FR-HR-011, FR-HR-012)
- Payroll immutability after approval (FR-HR-013, BR-012)
- PDF payslip generation (FR-HR-014)
- Payslip delivery via WhatsApp and SMS fallback (FR-HR-015)
- NSSF schedule generation (FR-HR-016)
- PAYE return generation (FR-HR-017)
- Bank salary payment file generation (FR-HR-018)
- Salary advance with automatic repayment deduction (FR-HR-019)
- Disciplinary record with automatic fine deduction (FR-HR-020)

### 4.9 F-009 — Dashboard and Business Health

- Four KPI cards on open: today's revenue, transaction count, outstanding credit, cash position (FR-DASH-001)
- Revenue comparison cards with directional indicator (FR-DASH-002)
- Auto-refresh every 2 minutes on Web (FR-DASH-003)
- Low-stock badge and expandable panel (FR-DASH-004)
- Pending approvals badge and action links (FR-DASH-005)
- Branch switcher with KPI update within 2 seconds (FR-DASH-006)
- Business health score RAG indicator (FR-DASH-007)

### 4.10 F-010 — Settings and Configuration

- Business profile update with immediate receipt reflection (FR-SET-001)
- Receipt template customisation (FR-SET-002)
- Tax rate creation and assignment (FR-SET-003)
- Functional currency configuration (FR-SET-004)
- User creation with role assignment and RBAC enforcement (FR-SET-005, FR-SET-006)
- Subscription screen with usage vs plan limits (FR-SET-007)
- Full data export as ZIP within 10 minutes (FR-SET-008)
- Account deletion with 30-day retention and final export (FR-SET-009)
- Notification preference configuration (FR-SET-010)
- 2FA TOTP setup, login enforcement, and device revocation (FR-SET-011, FR-SET-012)

---

## 5. Features NOT to be Tested in Phase 1

The following features and modules are explicitly excluded from Phase 1 testing. Their absence from the test suite is intentional and is not a defect.

| Excluded Feature | Reason |
|---|---|
| Restaurant / Bar Module (F-011) | Phase 2 — not yet developed |
| Pharmacy / Drug Store Module (F-012) | Phase 2 — not yet developed |
| Hotel / Accommodation Module (F-013) | Phase 3 — not yet developed |
| Advanced Inventory Module (F-014) | Phase 3 — not yet developed |
| EFRIS Compliance Module (F-015) | Phase 3 — URA EFRIS API integration pending |
| iOS Application (Swift + SwiftUI) | Phase 2 — development not started |
| Business rules BR-013 through BR-016 | Phase 2 / Phase 3 rules — no implementation in Phase 1 |
| MTN MoMo and Airtel Money live production gateway | Sandbox testing only in Phase 1; live gateway requires GAP-001 resolution and production API keys |
| Multi-currency conversion | Functional currency is single-currency in Phase 1 |
| Advanced analytics and ML-based forecasting | Phase 2 roadmap feature |

---

## 6. Test Approach

Testing follows a layered progression from lowest-level unit verification to user acceptance. Each level must meet its entry criteria before the next level begins.

### 6.1 Level Progression

1. **Unit Testing** — Isolated verification of individual classes and functions. Business logic classes require ≥ 80% line coverage. Frameworks: JUnit 5 + Mockito (Android), PHPUnit 10 (PHP API).

2. **Integration Testing** — Interaction between 2 or more real components against an ephemeral MySQL test database. Mandatory classes: multi-tenant isolation (BR-001), credit limit enforcement (BR-002), POS session lock (BR-007), and multi-payment balance check (BR-010).

3. **System Testing (End-to-End)** — Full application stack driven through real UIs against a seeded staging environment. Android: Espresso / Compose UI Testing. Web: Playwright.

4. **Android Instrumented Testing** — Device-level tests for ML Kit barcode scan, Bluetooth thermal printer pairing, and WorkManager offline sync. Minimum device: API level 26, ARM32, 2 GB RAM.

5. **Offline Resilience Testing** — Airplane-mode sale sequences, receipt gap injection, idempotency key deduplication, and no-loss interruption testing per BR-008 and BR-009.

6. **Performance Testing** — Load profile: 50 concurrent virtual users. Tool: k6 or Apache JMeter (API); Android Profiler (Android). All thresholds in Section 8 are mandatory.

7. **Security Testing** — JWT expiry and rotation, multi-tenant isolation at API layer, SQL injection (OWASP ZAP), CSRF enforcement, certificate pinning bypass, and bcrypt password storage verification.

8. **User Acceptance Testing (UAT)** — Representative end-user personas (Nakato, Wasswa, Namukasa, Apio) executing real-world business journeys on the staging environment. Final gate before production release.

### 6.2 Test Execution Priority

Test cases are prioritised as follows:

- **Critical:** POS sale flow, offline sync, multi-tenant isolation, credit limit enforcement, payroll PAYE/NSSF accuracy, receipt gap detection. A failing Critical test case blocks the release.
- **High:** All BR-001 through BR-012 enforcement, all S1-severity defect areas, performance thresholds.
- **Medium:** Reporting, export, secondary UI flows.

---

## 7. Pass/Fail Criteria

All criteria are mandatory. A test cycle may not advance to the next level until all applicable criteria for the current level are met.

### 7.1 Unit and Integration Tests

| Criterion | Threshold |
|---|---|
| Business logic line coverage (Use Cases, Service classes) | ≥ 80% per CI coverage report |
| Multi-tenant isolation integration tests | 0 failures; 100% pass rate |
| Business rule integration tests (BR-001 – BR-012) | 0 failures; 100% pass rate |
| CI build status | Green (passing) on every pull request |

### 7.2 System and E2E Tests

| Criterion | Threshold |
|---|---|
| Critical-path E2E tests (Android + Web) | 0 failures; 100% pass rate |
| Open S1 defects at release gate | 0 |
| Open S2 defects at release gate | 0 undeferred; any deferred S2 requires written product owner sign-off |

### 7.3 Performance Tests

| Metric | Threshold | Severity if Failed |
|---|---|---|
| API P95 response time | ≤ 500 ms at 50 concurrent virtual users | S1 (POS critical path); S2 (other endpoints) |
| API P99 response time | ≤ 1,000 ms at 50 concurrent virtual users | S2 |
| POS sale completion (Android, end-to-end) | ≤ 3 seconds on UGX 250,000-class device on 3G | S1 |
| Barcode scan to cart add | ≤ 1 second | S2 |
| Product search (10,000 SKU catalogue) | ≤ 500 ms from last keystroke to results rendered | S2 |
| Dashboard load (Web, P95, 3G equivalent) | ≤ 4 seconds | S2 |
| Bluetooth receipt print | ≤ 5 seconds from sale confirmation | S2 |
| Offline queue drain on reconnect | ≤ 30 seconds for up to 500 pending transactions | S1 |
| Offline sync endpoint throughput | ≥ 100 sync payloads per minute per tenant | S2 |

### 7.4 Security Tests

| Criterion | Pass Condition |
|---|---|
| OWASP ZAP automated SQL injection scan | 0 confirmed SQL injection findings |
| OWASP ZAP XSS scan | 0 confirmed Cross-Site Scripting (XSS) findings |
| Multi-tenant cross-access (Franchise A vs B) | HTTP 403 or HTTP 404 on every cross-tenant request |
| Expired access token rejection | HTTP 401 returned for tokens older than 15 minutes |
| Bcrypt cost factor | ≥ 12; no plain-text or MD5/SHA-1 hashes in the database |
| Certificate pinning | App rejects connection when a proxy CA is installed |

### 7.5 UAT

| Criterion | Threshold |
|---|---|
| Critical user journeys completed without S1 defect | 100% of defined persona journeys |
| Product owner sign-off | Written sign-off from Peter Bamuhigire required |

---

## 8. Test Deliverables

The following artefacts shall be produced and stored in `projects/Maduuka/05-testing-documentation/`:

| Deliverable | Owner | Storage Path |
|---|---|---|
| Test Plan (this document) | QA Lead | `02-test-plan/` |
| Test Cases — POS, INV, CUS | QA Lead | `02-test-plan/02-test-cases-pos-inv-cus.md` |
| Test Cases — SUP, EXP, FIN | QA Lead | `02-test-plan/03-test-cases-sup-exp-fin.md` |
| Test Cases — REP, HR, DASH, SET | QA Lead | `02-test-plan/04-test-cases-rep-hr-dash-set.md` |
| Non-Functional Test Cases | QA Lead | `02-test-plan/05-non-functional-test-cases.md` |
| CI Coverage Report | Developer | GitHub Actions run summary (per pull request) |
| E2E Test Suite (code) | QA Engineer | Application source repository |
| Performance Test Report | QA Engineer | `05-testing-documentation/` (per sprint) |
| Security Scan Report (OWASP ZAP HTML) | QA Engineer | `05-testing-documentation/` (pre-release) |
| UAT Sign-Off Record | Product Owner | `05-testing-documentation/` |
| Test Run Report | QA Engineer | `05-testing-documentation/` (per E2E/UAT cycle) |

---

## 9. Testing Schedule

| Phase | Activities | Environment | Trigger |
|---|---|---|---|
| Setup | Seed test data; deploy staging; configure CI pipeline; obtain MTN MoMo sandbox (GAP-001) | CI + Staging | Sprint 1, Week 1 |
| Unit + Integration Execution | Run full unit and integration test suite on every pull request | CI (ephemeral) | Per pull request |
| E2E Execution | Drive Android and Web critical paths via Espresso and Playwright | Staging | Nightly on `staging` branch |
| Android Instrumented Tests | Barcode, Bluetooth printer, WorkManager sync on physical device | Physical device / Staging | Once per sprint |
| Performance Testing | k6 / JMeter load test at 50 concurrent virtual users | Staging | Once per sprint |
| Security Testing | OWASP ZAP automated scan; certificate pinning bypass; bcrypt inspection | Staging + Physical device | Once before release |
| Offline Resilience Testing | Airplane-mode sequences, sync drain, idempotency deduplication | Staging + Android device | Once per sprint |
| UAT | Persona-driven journeys; product owner witness | Staging | End of each milestone sprint and pre-release |
| Regression | Re-run all failed and fixed test cases after S1/S2 defect resolution | Staging | After each S1/S2 fix |
| Production Smoke Tests | Read-only assertions on live environment immediately post-deploy | Production | After each production deployment |

---

## 10. Environmental Needs

### 10.1 Android

- Android emulator or physical device: minimum API level 26 (Android 8.0), ARM32 architecture, 2 GB RAM
- Android Profiler enabled for performance trace capture
- Physical device required for: Bluetooth thermal printer pairing tests, certificate pinning bypass tests
- Hardware-capable emulator acceptable for: ML Kit barcode tests, WorkManager tests

### 10.2 Web Browser Matrix

All Web UI test cases shall be executed and pass on the following browsers:

| Browser | Version |
|---|---|
| Google Chrome | Latest stable |
| Mozilla Firefox | Latest stable |
| Microsoft Edge | Latest stable |
| Mobile Chrome (Android) | Latest stable |

### 10.3 Backend and Database

- PHP 8.3+ (matches production)
- MySQL 8.x (matches production schema; CI ephemeral database uses same migration scripts)
- Staging server: same OS and web server configuration as production

### 10.4 Third-Party Sandbox Accounts

| Service | Status |
|---|---|
| MTN MoMo Business API sandbox | Pending — GAP-001 |
| Airtel Money API sandbox | Pending — GAP-001 |
| Africa's Talking (SMS/WhatsApp) sandbox | Required before FR-POS-019, FR-POS-020, FR-HR-015 |
| OWASP ZAP (automated scanner) | Required before security test phase |

### 10.5 Test Data

The staging environment shall be seeded with:

- 100 products across 5 categories, each with cost price, selling price, and reorder level
- 50 customers: 30 cash-account and 20 credit-account with defined credit limits
- 30 days of historical sales data (minimum 10 transactions per day)
- 5 staff members with defined salary structures (basic salary, allowances, PAYE, NSSF)
- 3 supplier records with purchase history
- 2 separate franchise records for multi-tenant isolation tests (Franchise A, Franchise B)
- All PII in the test environment is synthetic (Uganda Data Protection and Privacy Act 2019)

---

## 11. Responsibilities

| Role | Person / Team | Responsibilities |
|---|---|---|
| Product Owner | Peter Bamuhigire | Review and approve test plan. Approve UAT test scripts before execution. Witness mandatory UAT sign-off journeys. Approve or defer S2 defects. Provide written UAT sign-off before production release. |
| QA Lead | Chwezi Core Systems QA | Author and maintain all test case documents. Coordinate test schedule. Produce Test Run Reports. Execute or delegate E2E and UAT test execution. Manage OWASP ZAP and performance test runs. |
| Developer | Chwezi Core Systems Dev | Write and maintain unit and integration tests. Fix defects within SLA. Maintain ≥ 80% line coverage on all business logic classes. Escalate GAP-001 resolution to unblock MTN MoMo test cases. |
| QA Engineer | Chwezi Core Systems QA | Author and maintain Espresso and Playwright E2E test scripts. Execute UAT scripts against staging. Log all defects in GitHub Issues with required labels, steps to reproduce, actual result, expected result, environment, and failing test case ID. |

---

*End of MADUUKA-TP-001 v1.0 — Test Plan Overview*
