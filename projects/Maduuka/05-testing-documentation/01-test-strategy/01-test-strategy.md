---
title: "Test Strategy — Maduuka POS and Business Management Platform"
author: "Chwezi Core Systems"
date: "2026-04-05"
version: "1.0"
status: "Draft"
---

# Test Strategy: Maduuka POS and Business Management Platform

**Document ID:** MADUUKA-TS-001
**Version:** 1.0
**Status:** Draft
**Prepared by:** Chwezi Core Systems
**Product Owner:** Peter Bamuhigire
**Date:** 2026-04-05

---

## 1. Introduction

### 1.1 Purpose

This Test Strategy defines the testing approach, scope, levels, environments, data management procedures, defect management protocol, and entry/exit criteria for Phase 1 of the Maduuka platform. It governs all testing activities from unit-level verification through User Acceptance Testing (UAT) prior to the Phase 1 production release.

This document is prepared in conformance with IEEE Std 829-2008 (*Standard for Software and System Test Documentation*) and IEEE Std 1012-2016 (*Standard for System, Software, and Hardware Verification and Validation*).

### 1.2 Scope

Phase 1 of Maduuka delivers 10 core modules on 2 client platforms — Android (Kotlin + Jetpack Compose) and Web (PHP 8.3+ / Bootstrap 5 / Tabler) — backed by a single shared REST API. The platform is deployed as a multi-tenant SaaS system, with every data record scoped to an authenticated `franchise_id` per **BR-001**.

This strategy covers all test activities required to validate those 10 modules, both client platforms, the REST API, the offline sale queue and sync mechanism, and multi-tenant data isolation enforcement.

### 1.3 Testing Objectives

The test team shall verify and validate the Maduuka platform against the following IEEE 830 quality criteria:

- **Correctness:** Every implemented behaviour mirrors the stakeholder intent documented in `_context/vision.md` and the business rules defined in `_context/business_rules.md`.
- **Completeness:** Every business rule (**BR-001** through **BR-012**) has at least 1 corresponding test case with a deterministic pass/fail criterion. Every edge case identified during requirements analysis has a corresponding test.
- **Consistency:** Terminology, data types, and behavioural definitions are uniform across Android, Web, and API test suites. A "credit sale" tested on Android and on Web exercises the same API contract and the same enforcement logic.
- **Verifiability:** Every test case defines an explicit expected outcome that can be evaluated without human judgement. Assertions must be binary: pass or fail.

### 1.4 References

| Reference | Title |
|---|---|
| IEEE Std 829-2008 | Standard for Software and System Test Documentation |
| IEEE Std 1012-2016 | Standard for System, Software, and Hardware Verification and Validation |
| IEEE Std 830-1998 | Recommended Practice for Software Requirements Specifications |
| IEEE Std 982.1-2005 | Standard Dictionary of Measures of the Software Aspects of Dependability |
| MADUUKA-SRS-001 | Maduuka Software Requirements Specification (Phase 1) |
| `_context/business_rules.md` | Maduuka Business Rules Register (BR-001 – BR-012) |
| `_context/quality_standards.md` | Maduuka Quality Standards and Performance Thresholds |
| `_context/tech_stack.md` | Maduuka Technology Stack Reference |
| Uganda Data Protection and Privacy Act 2019 | Data protection obligations for personal data in test environments |

---

## 2. Test Scope

### 2.1 In Scope

The following components and modules are in scope for Phase 1 testing:

**Phase 1 Core Modules (Android and Web):**

- **F-001:** Point of Sale (POS)
- **F-002:** Inventory and Stock Management
- **F-003:** Customer Management
- **F-004:** Supplier and Vendor Management
- **F-005:** Expenses and Petty Cash
- **F-006:** Financial Accounts and Cash Flow
- **F-007:** Sales Reporting and Analytics
- **F-008:** HR and Payroll
- **F-009:** Dashboard and Business Health
- **F-010:** Settings and Configuration

**Platforms and Layers:**

- Android application (Kotlin + Jetpack Compose, MVVM + Clean Architecture)
- Web application (PHP 8.3+, Bootstrap 5 / Tabler)
- Shared REST API (JSON over HTTPS)
- Offline sale queue (Room local storage + WorkManager sync)
- Multi-tenant data isolation enforcement (`franchise_id` scoping per **BR-001**)

**Cross-Cutting Concerns:**

- Authentication and authorisation (JWT on Android, session + CSRF on Web)
- Role-Based Access Control (RBAC) enforcement at the API layer
- Immutable audit log integrity (**BR-003**)
- Business rule enforcement for all Phase 1 rules (**BR-001** – **BR-012**)

### 2.2 Out of Scope

The following are explicitly excluded from Phase 1 testing:

- Phase 2 modules: Restaurant / Bar (F-011) and Pharmacy / Drug Store (F-012)
- iOS application (Swift + SwiftUI) — Phase 2
- EFRIS Compliance Module (F-015) — Phase 3
- Hotel / Accommodation Module (F-013) — Phase 3
- Advanced Inventory Module (F-014) — Phase 3
- Business rules **BR-013** – **BR-016** (Phase 2 and Phase 3 rules)
- MTN MoMo and Airtel Money live payment gateway integration in production (sandbox testing only in Phase 1)

---

## 3. Test Levels

### 3.1 Unit Tests

Unit tests verify the behaviour of individual classes and functions in isolation, with all external dependencies replaced by test doubles (mocks or stubs).

**Android (Kotlin):**

- Framework: JUnit 5 + Mockito
- Targets: ViewModels, Use Cases, Repository implementations, Room DAOs
- Each ViewModel test shall verify that state emission is correct for both the happy path and all defined error states
- Each Use Case test shall verify business rule enforcement in isolation from the data layer

**Backend API (PHP):**

- Framework: PHPUnit 10
- Targets: Service classes, business rule enforcement methods, database query builders
- Input validation logic shall have 100% branch coverage; all invalid input permutations defined in the SRS must produce a tested assertion

**Coverage Threshold:**

- Minimum 80% line coverage on all business logic classes (Use Cases, Service classes, domain models)
- Coverage is measured per CI run and reported as a build artefact
- A build that drops below the 80% threshold on business logic classes shall be treated as a failing build

**Tools:** JUnit 5, Mockito, PHPUnit 10, JaCoCo (Android coverage), PHP Code Coverage (PHPUnit built-in)

### 3.2 Integration Tests

Integration tests verify the interaction between two or more real components. Mocking the database at this level is prohibited — integration tests must execute against a real (ephemeral) database instance.

**Android:**

- Framework: Hilt test components + AndroidX Test
- Targets: Instrumented DAO tests executing against an in-memory Room database
- Test that Room schema migrations execute without data loss
- Test that the WorkManager sync job enqueues pending records and clears them after a successful API response

**Backend API:**

- Framework: PHPUnit 10 feature tests
- Target: Full request-through-response cycle against a seeded test MySQL database
- The test database is ephemeral: created, seeded, and destroyed per test run in CI

**Multi-Tenant Isolation Test (mandatory — **BR-001**):**

- Seed 2 separate franchise records (Franchise A and Franchise B) with overlapping product names and customer names
- Authenticate as a Franchise A user; assert that all list endpoints return 0 records belonging to Franchise B
- Attempt to fetch a known Franchise B resource ID while authenticated as Franchise A; assert HTTP 403 or HTTP 404
- This test class shall run on every pull request without exception

**Business Rule Integration Tests:**

The following business rules shall each have a dedicated integration test class:

| Rule | Test Assertion |
|---|---|
| **BR-002** (Credit limit enforcement) | A credit sale that would exceed the customer's credit limit returns HTTP 422 with error code `CREDIT_LIMIT_EXCEEDED`; a manager-authenticated override succeeds and records the override in the audit log |
| **BR-005** (Stock adjustment approval threshold) | An adjustment above the configured threshold is created with status `pending_approval`; an adjustment below the threshold is applied immediately with status `applied` |
| **BR-007** (POS session reconciliation) | An attempt to process a sale without an open session returns HTTP 409 with error code `NO_OPEN_SESSION`; a session cannot be closed while pending sales exist |
| **BR-010** (Multi-payment tracking) | A sale settled with 3 payment components (cash, MTN MoMo, credit) records 3 separate payment rows; the sum of all payment amounts equals the total sale amount exactly |

### 3.3 End-to-End (E2E) Tests

E2E tests drive the full application stack through real user interfaces against a deployed staging environment.

**Android (Kotlin + Compose):**

- Framework: Espresso or Jetpack Compose UI Testing (`androidx.compose.ui.test`)
- Critical path coverage required:

  1. Full sale flow: open POS session → search product by name → add to cart → apply discount → process multi-payment (cash + MoMo) → print Bluetooth receipt → close session
  2. Offline sale flow: enable airplane mode → complete sale → restore connectivity → verify sync completes and receipt appears in sales history
  3. POS session open and close: open session with opening float → process 3 sales → close session → verify reconciliation report shows correct expected cash

**Web (PHP / Bootstrap):**

- Framework: Playwright (preferred) or Selenium WebDriver
- Critical path coverage required:

  1. Login → Dashboard → create new sale → apply discount → multi-payment settlement → download PDF invoice
  2. Inventory: add new product → set reorder level → sell below reorder level → verify reorder alert appears on dashboard
  3. Reports: generate daily sales report → export as CSV → verify CSV row count matches transaction count displayed in UI

**Additional E2E Scenarios (cross-platform):**

- Credit sale with limit enforcement: attempt sale that exceeds credit limit as cashier (assert block); repeat with manager override (assert success + audit log entry)
- Stock adjustment with approval: submit adjustment above threshold as cashier → assert pending status → approve as manager → assert stock level updated
- Payroll: define salary structure → run payroll for a staff member → approve → download payslip PDF → verify NSSF and PAYE deductions are correct per Uganda tax tables

### 3.4 Android Instrumented Tests

The following Android capabilities require testing on a real device or a hardware-capable emulator and are treated as a separate test level:

- **CameraX + ML Kit barcode scanning:** Scan a physical EAN-13 barcode and assert that the correct product is added to the cart within ≤ 1 second of scan completion. Test all supported symbologies: EAN-13, EAN-8, Code-128, Code-39, QR.
- **Bluetooth thermal printer connectivity:** Pair with a supported 80mm thermal printer (Epson, Xprinter, or TP-Link); complete a sale; assert that a receipt is printing within ≤ 5 seconds of sale confirmation.
- **WorkManager offline sync scheduling:** Disconnect network; record 5 sales; verify that each sale is persisted locally in Room with status `pending_sync`; reconnect; verify WorkManager enqueues the sync job and all 5 records transition to status `synced` within 30 seconds.
- **Background sync queue drain:** Place the app in background; simulate 15-minute background sync interval; verify that the WorkManager periodic task fires and processes any pending records without requiring the app to be foregrounded.

These tests shall be executed on a physical Android device (minimum API level 26) as part of the pre-release test run. CI execution on a hardware-accelerated emulator is acceptable for barcode and WorkManager tests; Bluetooth printer tests require a physical device.

### 3.5 Offline Resilience Tests

Offline resilience tests verify the system's compliance with **BR-009** (Offline Sale Queue). These tests are executed on Android using a real or emulated network interface and on the API using seeded pending-sync payloads.

**Test scenarios:**

1. **Airplane mode sale sequence:** Enable airplane mode → process N = 10 sales → restore connectivity → assert all 10 sales appear in the server-side sales history with the correct `franchise_id`, amounts, and timestamps. Assert that 0 sales are lost.
2. **Receipt gap detection (**BR-008**):** In a seeded test session, manually delete receipt number 1013 from the local queue simulation → sync → assert that the receipt gap report flags receipt 1013 as missing for manager review.
3. **No sale loss on interruption:** Begin a sale → interrupt connectivity at the point of payment confirmation → assert that the sale is either fully committed locally or fully rolled back. Assert that no partial sale record exists.
4. **Idempotency key deduplication:** Submit the same pending-sync payload twice with an identical `idempotency_key` → assert that the API creates exactly 1 sale record and returns HTTP 200 on the second submission without creating a duplicate.

### 3.6 Performance Tests

Performance tests verify compliance with the thresholds defined in `_context/quality_standards.md`. All thresholds are mandatory; a result that exceeds a threshold constitutes a **S2 defect** unless the threshold is for a POS-critical path, in which case it constitutes a **S1 defect**.

**API Load Tests:**

| Metric | Threshold | Test Condition |
|---|---|---|
| API response time (P95) | ≤ 500 ms | 50 concurrent virtual users, standard product search and cart submission operations |
| API response time (P99) | ≤ 1,000 ms | Same load profile |
| Offline sync endpoint throughput | ≥ 100 sync payloads/minute per tenant | Simulate burst of pending sales after connectivity restoration |

**Android App Performance:**

| Metric | Threshold | Measurement Method |
|---|---|---|
| POS sale completion (end-to-end) | ≤ 3 seconds | Android Profiler; time from "Confirm Payment" tap to receipt display. Measured on a UGX 250,000-class Android device on a 3G network connection. |
| Barcode scan to cart add | ≤ 1 second | Android Profiler; time from barcode decode event to cart update UI render |
| Product search (10,000 SKU catalogue) | ≤ 1 second | Espresso `IdlingResource`; measure from keystroke to results list rendered |
| Dashboard load time (P95, 3G) | ≤ 4 seconds | Android Profiler network trace; from screen open to all KPI cards rendered |
| Receipt print (Bluetooth) | ≤ 5 seconds | Timer from sale confirmation to first print line on thermal printer |
| Background sync interval | ≤ 15 minutes | WorkManager periodic task; verify scheduling precision under battery-optimisation conditions |
| Offline queue drain on reconnect | ≤ 30 seconds | All pending transactions synced from the moment connectivity is restored |

**Tools:** k6 or Apache JMeter for API load tests; Android Profiler (`CPU`, `Memory`, `Network` tracks) for Android app performance; Espresso `IdlingResource` for UI timing assertions.

### 3.7 Security Tests

Security testing verifies the platform's compliance with the security baselines defined in `_context/tech_stack.md` and `_context/quality_standards.md`.

**Authentication and Token Management:**

- Verify that an access token expires after exactly 15 minutes; assert that a request made with an expired access token returns HTTP 401.
- Verify that a valid refresh token generates a new access token; assert that a refresh token older than 30 days is rejected with HTTP 401.
- Verify that using a refresh token invalidates it (rotation); assert that replaying the same refresh token a second time returns HTTP 401.

**Multi-Tenant Isolation (API layer):**

- Authenticate as Franchise A; attempt GET, POST, PUT, and DELETE requests against resource IDs belonging to Franchise B; assert HTTP 403 on every attempt.
- Attempt SQL injection patterns in `franchise_id` parameter; assert that the API returns HTTP 400 and that no Franchise B data is exposed.

**RBAC Enforcement:**

- Authenticate as a cashier-role user; attempt to approve a stock adjustment; assert HTTP 403.
- Authenticate as a cashier-role user; attempt to access the payroll module endpoints; assert HTTP 403.
- Authenticate as a manager-role user; execute a manager override on a credit limit block; assert that the override is recorded in the audit log with the manager's user ID, timestamp, and reason code.

**Web Application Security:**

- Submit a state-changing POST request without a CSRF token; assert HTTP 403.
- Submit a state-changing POST request with an invalid (replayed) CSRF token; assert HTTP 403.
- Execute an automated SQL injection scan on all web form inputs using OWASP ZAP or an equivalent DAST tool; assert 0 confirmed SQL injection findings.
- Verify that all session cookies carry the `HttpOnly`, `Secure`, and `SameSite=Strict` attributes.

**Android Security:**

- Attempt to bypass certificate pinning using a proxy (e.g., Burp Suite with a custom CA installed on the device); assert that the app rejects the connection and does not transmit data.
- Verify that JWT tokens and sensitive user data are stored in `EncryptedSharedPreferences` (AES-256-GCM); assert that plain-text credentials do not appear in the device filesystem.
- Verify that root detection fires at app launch on a rooted test device; assert that the app displays a warning and restricts sensitive operations.

**Password Storage:**

- Inspect the database for any user record; assert that the `password` column contains a bcrypt hash with a cost factor ≥ 12 and that no plain-text or MD5/SHA-1 variants exist.

### 3.8 User Acceptance Testing (UAT)

UAT verifies that the platform satisfies real-world business workflows as experienced by representative end users. UAT is the final gate before Phase 1 release.

**Test Personas:**

| Persona | Role | Modules Under Test |
|---|---|---|
| Nakato | Shop owner (single branch) | Dashboard, Reports, Expenses, Settings, HR/Payroll |
| Wasswa | Cashier | POS, Inventory (read), Customer credit |
| Namukasa | Multi-branch owner | Dashboard (branch switcher), Reports (by branch), Financial Accounts |
| Apio | HR manager | HR/Payroll, Leave management, Attendance |

**UAT Environment:**

- Dedicated staging server with anonymised, production-like data
- Seeded with: 100 products across 5 categories, 50 customers (mix of cash and credit accounts), 30 days of historical sales data, 5 staff members with defined salary structures
- No real customer Personally Identifiable Information (PII) in the UAT environment (Uganda Data Protection and Privacy Act 2019 compliance)

**Acceptance Criteria:**

- All critical user journeys defined for each persona complete without a blocker-level (S1) defect.
- No S2 defect remains unresolved or undeferred at the time of sign-off.
- The product owner (Peter Bamuhigire) executes or witnesses the full POS sale flow, credit sale with limit enforcement, offline sale and sync, and the monthly payroll run before signing off.

**UAT Sign-Off:**

- Formal written sign-off from Peter Bamuhigire is required before any Phase 1 production deployment proceeds. Sign-off is conditional on all exit criteria (Section 7) being met.

---

## 4. Test Environments

| Environment | Purpose | Data | Access |
|---|---|---|---|
| Local Dev | Unit tests, DAO tests, service-class tests | Seeded in-memory or local test database | Developer only |
| CI (GitHub Actions) | Automated unit + integration test suite on every pull request | Ephemeral test database, created and destroyed per run | CI pipeline |
| Staging | E2E tests, performance tests, security scans, UAT | Anonymised production-like data (no real PII) | Dev team + product owner |
| Production | Post-deploy smoke tests only | Live data (read-only assertions, no data mutation) | Product owner + platform admin |

**Environment Parity Requirements:**

- The Staging environment shall use the same database engine version (MySQL 8.x), PHP version (8.3+), and Android API level targets as the Production environment.
- Any deviation between Staging and Production configuration shall be documented in the test run report.
- CI ephemeral databases shall use the same schema migration scripts used in Production; schema divergence between environments constitutes a blocking defect.

---

## 5. Test Data Management

**Seed Data Standards:**

- All non-production environments shall be seeded using deterministic seed scripts version-controlled in the repository.
- Standard seed factories shall generate the following baseline data per test franchise:
  - 100 products across 5 categories, each with a defined cost price, selling price, and reorder level
  - 50 customers: 30 cash-account customers and 20 credit-account customers with defined credit limits
  - 30 days of historical sales data (minimum 10 transactions per day)
  - 5 staff members with defined salary structures, including NSSF and PAYE deductions
  - 3 supplier records with purchase history

**Multi-Tenant Test Isolation:**

- Each test run that exercises multi-tenant logic shall use a dedicated `franchise_id` generated at test-setup time.
- Shared `franchise_id` values across concurrent test runs are prohibited; each parallel CI job shall generate its own isolated franchise.
- After a test run completes, the test franchise and all its associated records shall be deleted or the ephemeral database dropped.

**PII Compliance (Uganda Data Protection and Privacy Act 2019):**

- No real customer names, phone numbers, email addresses, National Identification Numbers (NIDs), or financial data shall appear in any non-production environment.
- Seeded customer records shall use synthetic names (e.g., "Test Customer 001") and randomised but structurally valid Ugandan phone numbers (format: `+2567XXXXXXXX`).
- Anonymisation is applied before any production data snapshot is used for staging. The anonymisation script is version-controlled and run as a mandatory step before staging refresh.

---

## 6. Defect Management

### 6.1 Severity Classification

| Severity | Label | Definition |
|---|---|---|
| S1 | Blocker | Prevents a critical user journey from completing. No workaround exists. Blocks release. |
| S2 | Critical | Prevents a non-critical feature from working. A documented workaround exists. |
| S3 | Major | Feature works but produces incorrect or sub-optimal output. Does not block a user journey. |
| S4 | Minor | Cosmetic issue, typo, or negligible UI inconsistency with no functional impact. |

**Examples of S1 defects:**

- POS sale cannot be completed on Android
- Offline sale is lost and does not appear in sales history after sync
- Franchise A can read Franchise B data (multi-tenant isolation failure)
- Credit limit block does not fire (BR-002 failure)
- Approved payroll amounts are modifiable without a reversal entry (BR-012 failure)

### 6.2 Defect Tracking

- All defects shall be logged as GitHub Issues in the Maduuka repository.
- Mandatory labels: `bug`, and one of `severity:s1`, `severity:s2`, `severity:s3`, or `severity:s4`.
- Each defect issue shall include: steps to reproduce, actual result, expected result, environment (Android/Web/API), and the failing test case ID where applicable.

### 6.3 Resolution SLA

| Severity | Resolution Target |
|---|---|
| S1 | Fix and retest within 24 hours of logging |
| S2 | Fix and retest within 48 hours of logging |
| S3 | Fixed within the current sprint or the following sprint |
| S4 | Fixed at the team's discretion; batched with routine maintenance |

---

## 7. Entry and Exit Criteria

### 7.1 Entry Criteria (Before a Test Phase Begins)

The following conditions must be satisfied before the test team begins a test phase:

1. The feature branch has been merged to the designated test branch.
2. All unit tests pass with a green CI status.
3. The target test environment is deployed, accessible, and seeded with the standard test data set.
4. No unresolved S1 defects exist from a prior test phase on the same feature set.
5. The test plan for the phase has been reviewed and acknowledged by the product owner.

### 7.2 Exit Criteria (Before Phase 1 Release)

The following conditions must all be met before a Phase 1 production deployment is authorised:

1. All S1 defects are resolved, retested, and closed.
2. All S2 defects are either resolved and retested, or formally deferred with written justification signed by the product owner.
3. Business logic unit test coverage is ≥ 80% line coverage on all Use Case and Service classes, verified by the CI coverage report.
4. All multi-tenant isolation integration tests pass with 0 failures.
5. All business rule integration tests (**BR-001** – **BR-012**) pass with 0 failures.
6. API P95 response time ≤ 500 ms under the defined load profile (Section 3.6).
7. POS sale completion time ≤ 3 seconds end-to-end on the target Android device profile (Section 3.6).
8. All Phase 1 critical-path E2E tests pass with 0 failures on both Android and Web.
9. The OWASP ZAP automated scan reports 0 confirmed SQL injection or Cross-Site Scripting (XSS) findings.
10. UAT sign-off received in writing from Peter Bamuhigire (product owner).

---

## 8. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Developer | Write and maintain unit tests and integration tests for all owned classes. Fix all defects assigned to them. Maintain ≥ 80% line coverage on business logic classes. |
| QA Engineer (or developer in QA role) | Author and maintain E2E test scripts for Android and Web. Execute UAT test scripts against the staging environment. Log all defects in GitHub Issues with the required labels and reproduction steps. Produce the test run report after each E2E and UAT cycle. |
| Product Owner (Peter Bamuhigire) | Review and approve UAT test scripts before execution. Execute or witness the mandatory UAT sign-off journeys (Section 3.8). Make priority and deferral decisions on S2 defects. Provide written UAT sign-off before Phase 1 release proceeds. |

---

## 9. Test Schedule

| Test Activity | Trigger / Cadence | Environment |
|---|---|---|
| Unit tests | Every commit; evaluated by CI on every pull request | CI (ephemeral) |
| Integration tests | Every pull request; CI pipeline | CI (ephemeral) |
| E2E tests (Android + Web) | Nightly on the `staging` branch | Staging |
| Android instrumented tests (device) | Once per sprint on a physical device | Staging / local device |
| Performance tests | Once per sprint on staging | Staging |
| Security scan (OWASP ZAP) | Once before Phase 1 release; re-run after any security-relevant change | Staging |
| Certificate pinning bypass test | Once before Phase 1 release | Physical Android device |
| UAT | At the end of each Phase 1 milestone sprint and immediately before the release build | Staging |
| Production smoke tests | Immediately after each production deployment | Production (read-only) |

---

## 10. Test Deliverables

The test team shall produce the following artefacts:

- **Test Strategy (this document):** Defines the overall approach. Version-controlled in the project repository.
- **Test Cases:** Individual test case specifications for E2E and UAT scenarios. Stored in `projects/Maduuka/05-testing-documentation/02-test-cases/`.
- **Automated Test Suite:** Unit, integration, and E2E test code version-controlled alongside application source code.
- **CI Coverage Report:** Generated per pull request; attached to the GitHub Actions run summary.
- **Performance Test Report:** Generated once per sprint; stored in `projects/Maduuka/05-testing-documentation/`.
- **Security Scan Report:** OWASP ZAP HTML report; stored in `projects/Maduuka/05-testing-documentation/`.
- **UAT Sign-Off Record:** Written sign-off from the product owner; stored in `projects/Maduuka/05-testing-documentation/`.
- **Test Run Report:** Summary of pass/fail counts, open defects, and coverage per E2E or UAT cycle; generated by the QA engineer after each cycle.

---

*End of Document — MADUUKA-TS-001 v1.0*
