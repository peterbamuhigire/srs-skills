# Test Strategy — Academia Pro

**Document ID:** AP-TS-001
**Version:** 1.0
**Date:** 2026-04-03
**Author:** Peter Bamuhigire
**Standard:** IEEE 829-2008

---

## 1 Purpose and Scope

This document defines the overall test strategy for Academia Pro, a multi-tenant SaaS school management platform targeting primary and secondary schools in Uganda. The strategy governs all testing activities across the Software Development Life Cycle and applies to every phase of the product roadmap.

The strategy addresses the following system characteristics that carry elevated risk:

- Multi-tenant architecture with strict tenant isolation (BR-MT-001)
- Financial transactions in Uganda Shillings with zero tolerance for double-payment (BR-FEE-005)
- UNEB grading engine with 4 distinct curriculum grading formulas (BR-UNEB-001 through BR-UNEB-004)
- Student personal data protection under the Uganda Data Protection and Privacy Act 2019 (BR-DP-001)
- Academic year lifecycle operations that lock historical records permanently (BR-PROM-005)
- Cross-school student identity lookup with global uniqueness constraints (BR-STU-001)

---

## 2 Test Pyramid

All testing activities follow the test pyramid distribution model. The ratios below apply to the total test case count across the project.

| Layer | Proportion | Tools | Scope |
|---|---|---|---|
| Unit tests | 70% | PHPUnit (backend), Vitest (frontend) | Individual functions, methods, computations, validators |
| Integration tests | 20% | PHPUnit (feature tests), Playwright (API) | Module interactions, database operations, API endpoints, tenant-scoped queries |
| End-to-end tests | 10% | Playwright (browser) | Critical user flows spanning multiple modules |

### 2.1 Unit Test Coverage Targets

| Module | Minimum Line Coverage |
|---|---|
| UNEB grading engine (FR-EXM-004 through FR-EXM-007) | 100% |
| Fee calculation and receipt logic (FR-FEE-001 through FR-FEE-007) | 100% |
| All other backend modules | 80% |
| Frontend components (Vitest) | 70% |

### 2.2 Integration Test Coverage Targets

Every API endpoint defined in the functional requirements (FR-AUTH through FR-APPLY) shall have at least one integration test covering the success path and one covering each documented error condition.

### 2.3 End-to-End Test Coverage

The following critical user flows require Playwright E2E tests:

1. Student admission and enrollment (FR-SIS-001, FR-SIS-002)
2. Fee structure definition, payment recording, and receipt generation (FR-FEE-001, FR-FEE-002, FR-FEE-003)
3. Mark entry, grade computation, and report card generation (FR-EXM-002, FR-EXM-004, FR-RPT-001)
4. Year-start promotion wizard full cycle (FR-PROM-001 through FR-PROM-007)
5. Login, session timeout, and logout (FR-AUTH-001, FR-AUTH-004, FR-AUTH-005)
6. EMIS export generation (FR-EMIS-001)
7. Inter-school record request workflow (FR-SHARE-001 through FR-SHARE-008)
8. In-platform school application workflow (FR-APPLY-001 through FR-APPLY-005)

---

## 3 Test Categories

### 3.1 Data Integrity Testing

Data integrity testing validates that computation outputs match authoritative reference values and that tenant boundaries are never breached.

#### 3.1.1 Tenant Isolation

**Risk:** Cross-school data leakage is a critical security and legal violation under the Uganda PDPO 2019.

**Strategy:**

1. Every tenant-scoped database query shall be verified by an automated PHPUnit test that asserts `WHERE tenant_id = ?` is present in the generated SQL. The Repository layer's global scope (BR-MT-001) shall be tested by attempting to fetch records belonging to Tenant B while authenticated as Tenant A; the expected result is an empty result set.
2. A dedicated integration test suite (`TenantIsolationTest`) shall provision 2 test tenants and verify isolation across all 16 FR groups: authentication, students, fees, attendance, examinations, report cards, RBAC, EMIS export, audit trail, promotion, departures, history, record sharing, and applications.
3. Super Admin cross-tenant read access (BR-MT-003) shall be tested separately, verifying that every cross-tenant read creates an audit log entry with `user_id`, `target_tenant_id`, `timestamp`, and `access_reason`.
4. Global identity tables (`global_students`, `student_identifiers`) shall be tested to confirm they carry no `tenant_id` and that write access is restricted to the owning school (BR-MT-002).

**Pass criterion:** Zero cross-tenant data leakage across all test runs. Any single leakage failure blocks release.

#### 3.1.2 UNEB Grading Engine Accuracy

**Risk:** Incorrect grade computation directly affects student academic outcomes and school credibility.

**Strategy:**

1. Maintain a reference dataset of manually verified UNEB sample mark sheets (sourced from UNEB — see quality_standards.md). The dataset shall cover boundary values for every division threshold.
2. Unit tests shall verify every grading formula:
   - PLE (BR-UNEB-001): grade scale 1--4 per subject, aggregate 4--36, Division I (4--12), Division II (13--23), Division III (24--29), Division IV (30--34), Ungraded (35--36)
   - UCE O-Level (BR-UNEB-002): D1--F9 per subject, aggregate divisions I (7--34), II (35--46), III (47--58), IV (59--70), Unclassified (>70)
   - UACE A-Level (BR-UNEB-003): principal A--F, subsidiary O, points A=6/B=5/C=4/D=3/E=2/O=1/F=0, best 3 principal subjects
   - Thematic Curriculum P1--P3 (BR-UNEB-004): competency descriptors HC/C/NYC only, no numeric grades
3. Boundary value analysis: test every division boundary (e.g., PLE aggregate 12 = Division I, aggregate 13 = Division II).
4. Mark entry validation: verify that out-of-range marks are rejected at the API layer (BR-UNEB-005).

**Pass criterion:** 100% match with manually verified UNEB sample mark sheets. Zero tolerance for grading errors.

#### 3.1.3 Fee Calculation Accuracy

**Risk:** Financial miscalculation erodes school trust and may constitute fraud.

**Strategy:**

1. Fee structure tests: verify term-based billing per class per term (BR-FEE-001), partial payment acceptance with no minimum floor (BR-FEE-002), and arrears carry-forward (BR-FEE-003).
2. Double-payment prevention (BR-FEE-005): submit identical payment codes within a 5-minute window and verify the second transaction returns status `DUPLICATE` with the original receipt.
3. Receipt immutability (FR-FEE-003): verify that receipts are sequentially numbered per school and that no API or database operation can delete a receipt.
4. Balance accuracy: after a series of partial payments, verify that `outstanding_balance = total_fees - sum(payments)` with UGX precision (no floating-point rounding errors; use integer arithmetic in cents or smallest currency unit).
5. Refund workflow: verify that only the School Owner/Director role can approve a refund (BR-FEE-007); the bursar role's approval attempt shall be rejected with HTTP 403.

**Pass criterion:** 0 duplicate receipts per 10,000 payment events. Balance calculations match expected values to the nearest UGX 1.

### 3.2 Functional Testing

Functional tests validate that every stimulus-response pair defined in Section 4 of the SRS produces the documented output for valid inputs and the documented error response for invalid inputs.

**Strategy:**

1. Each functional requirement (FR-AUTH-001 through FR-APPLY-005) shall have a minimum of 1 positive test case (valid input, expected output) and 1 negative test case per documented error condition.
2. Test cases shall reference the FR ID, stimulus, expected response, and business rule cross-references from the SRS.
3. RBAC-gated operations shall be tested with at least 2 roles: one authorised role and one unauthorised role.
4. API tests shall validate HTTP status codes, response body structure, and error codes as specified in the SRS.

### 3.3 Performance Testing

Performance tests validate that the system meets the quantitative targets in `quality_standards.md`.

**Strategy:**

| Test Scenario | Tool | Target | Concurrency |
|---|---|---|---|
| Dashboard page load (P95) | Playwright with 3G throttle | $\leq$ 2,000 ms | 50 concurrent users |
| Standard CRUD API (P95) | k6 | $\leq$ 500 ms | 200 concurrent requests |
| Single student report card generation (P95) | k6 | $\leq$ 3,000 ms | 10 concurrent requests |
| Bulk report card generation (200 students) | PHPUnit timed test | $\leq$ 120 seconds | 1 (sequential) |
| UNEB grade computation (500 students) | PHPUnit timed test | $\leq$ 5 seconds | 1 (sequential) |
| Database query (P99) | Laravel Telescope query log analysis | $\leq$ 200 ms | Under normal load |

**Load profile:** Performance tests shall simulate a school with 2,000 students and 80 staff users to represent the upper range of the target market.

**Environment:** Performance tests shall run against the staging environment with production-equivalent hardware specifications. Network throttling to 10 Mbps simulates typical Ugandan school internet connectivity.

### 3.4 Security Testing

Security tests validate compliance with the OWASP Top 10, the Uganda PDPO 2019, and the security standards in `quality_standards.md`.

**Strategy:**

1. **Penetration testing:** Conduct a full OWASP Top 10 penetration test before every major release. Zero critical or high findings are permitted.
2. **Authentication tests:**
   - Verify account lockout after 5 failed login attempts (FR-AUTH-001)
   - Verify MFA enforcement for Super Admin and School Owner roles (FR-AUTH-006)
   - Verify session timeout at 30 minutes inactivity for web (FR-AUTH-005)
   - Verify JWT access token expiry at 15 minutes and refresh token rotation (FR-AUTH-002, FR-AUTH-003)
3. **Authorisation tests:**
   - Verify that no user can assign a role with higher privilege than their own (BR-RBAC-002)
   - Verify Super Admin cross-tenant access is read-only and logged (BR-MT-003)
   - Verify health records (Phase 7) are accessible only to nurse/doctor and linked parent (BR-DP-003)
4. **Encryption verification:**
   - Confirm AES-256 encryption at rest for all PII fields (BR-DP-004)
   - Confirm TLS 1.3 for all connections; TLS 1.2 only for USSD integration
5. **Audit trail completeness:** Verify that every create/update/delete action on student, fee, and health records produces an immutable audit log entry with `user_id`, `tenant_id`, `timestamp`, and before/after values (FR-AUD-001).
6. **PDPO compliance tests:**
   - Verify data export produces complete JSON for all student personal data (BR-DP-002)
   - Verify soft-delete pathway removes personal data from active queries (BR-DP-002)
   - Verify disciplinary record requires separate explicit consent (BR-SHARE-003)

### 3.5 Academic Year Lifecycle Testing

Academic year lifecycle operations are irreversible and affect the entire school's data. Testing must cover the full promotion-to-lock sequence.

**Strategy:**

1. **Promotion wizard:** Test bulk promotion, selective override (repeating), departure at final-year classes (P7, S.4, S.6), wizard draft persistence, and the Term 1 open gate (FR-PROM-001 through FR-PROM-007).
2. **Historical record lock:** Verify that marks, attendance, and payment records become immutable 30 days after the last term's configured end date (BR-PROM-005). Attempt to modify a locked record via API and verify HTTP 403 or equivalent rejection.
3. **Departure model:** Verify each departure reason code creates the correct record, that deceased students are globally locked, and that expelled flag privacy is maintained in NIN/LIN lookup (FR-DEPART-001 through FR-DEPART-004).
4. **Cross-tenant student history:** Verify that a transferred student can view prior-school records, that fee amounts are hidden (only clearance status shown), and that history survives tenant suspension (FR-HIST-001 through FR-HIST-003, BR-HIST-001 through BR-HIST-004).

### 3.6 EMIS Export Format Compliance Testing

**Risk:** Non-compliant EMIS exports prevent schools from meeting Ministry of Education and Sports (MoES) reporting obligations.

**Strategy:**

1. Generate EMIS headcount exports (FR-EMIS-001) and validate the output against the MoES-specified CSV/XML schema.
2. Verify field mappings: student count by class, gender, age band, and special needs category.
3. Validate with an MoES officer before Phase 8 go-live (per Phase 8 roadmap).

### 3.7 Report Card Generation Testing

**Strategy:**

1. Verify single student report card accuracy: correct marks, computed grades, class rank, head teacher comments, and school logo (FR-RPT-001).
2. Verify bulk report card generation for an entire class (200 students) completes within 120 seconds (FR-RPT-002).
3. Verify school performance summary aggregation: class averages, subject averages, pass rates (FR-RPT-003).
4. Verify PDF export renders correctly on A4 paper with correct formatting.
5. Cross-reference report card grades with UNEB grading engine output to confirm consistency.

### 3.8 Payment Reconciliation Testing

**Strategy:**

1. **Phase 1 (manual payments):** Verify that manual cash and bank transfer entries produce sequential receipts, update balances correctly, and appear in financial reports (FR-FEE-002, FR-FEE-003, FR-FEE-007).
2. **Phase 2 (SchoolPay integration):** Verify webhook payment notifications update the student's fee balance in real time. Verify nightly reconciliation polling detects and resolves discrepancies. Verify payment code uniqueness per student.
3. **MoMo/Airtel Money (Phase 11):** Test mobile money payment flow end to end, including timeout handling and partial settlement scenarios.

---

## 4 Test Environments

| Environment | Purpose | Data | Infrastructure |
|---|---|---|---|
| Local development | Developer-run unit and integration tests | SQLite in-memory or MySQL 8.x Docker container with seeded test data | Developer workstation |
| CI/CD (GitHub Actions) | Automated test suite on every pull request | MySQL 8.x service container, seeded fixtures | GitHub-hosted runner |
| Staging | Pre-release integration, performance, and E2E tests | Anonymised copy of production schema with synthetic data (2,000 students, 80 staff, 3 tenants) | Production-equivalent cloud instance (Africa region) |
| UAT | User acceptance testing by school administrators | Synthetic data representing a realistic Uganda school | Staging infrastructure, separate database |
| Production | Post-deployment smoke tests only | Live data (no destructive tests permitted) | Production infrastructure |

### 4.1 Environment Promotion Rules

1. Code shall not be promoted from CI/CD to staging until all unit and integration tests pass with 0 failures.
2. Code shall not be promoted from staging to production until all E2E tests pass and performance benchmarks meet the targets in Section 3.3.
3. UAT sign-off by the designated school administrator is required before production deployment.

---

## 5 Test Data Management

### 5.1 Principles

1. **No production data in non-production environments.** All test data is synthetic or anonymised.
2. **Deterministic seed data.** Test fixtures are version-controlled in the repository under `database/seeders/testing/` and produce identical datasets on every run.
3. **Tenant-aware seeding.** The test seeder provisions a minimum of 3 tenants (School A, School B, School C) to enable tenant isolation testing.
4. **UNEB reference data.** A `tests/fixtures/uneb-reference-marks.json` file contains manually verified mark sheets for PLE, UCE, UACE, and Thematic Curriculum boundary cases.
5. **Fee reference data.** A `tests/fixtures/fee-scenarios.json` file contains partial payment sequences, arrears carry-forward, and double-payment attempts.

### 5.2 Data Refresh

1. The staging database is rebuilt from seed data before every release candidate test cycle.
2. CI test databases are ephemeral: created at the start of each test run and destroyed at completion.

### 5.3 Sensitive Data Handling

1. Test data shall never contain real student names, NIN, LIN, or contact information.
2. Payment test data shall use clearly artificial amounts (e.g., UGX 100,000) and payment codes (e.g., `TEST-PAY-001`).

---

## 6 Defect Management

### 6.1 Severity Classification

| Severity | Definition | SLA (Time to Fix) |
|---|---|---|
| S1 — Critical | System unavailable, data loss, cross-tenant data leakage, financial miscalculation, incorrect UNEB grades | 4 hours |
| S2 — High | Major feature broken, security vulnerability, EMIS export failure, report card errors | 24 hours |
| S3 — Medium | Minor feature degradation, UI rendering issue on supported viewport, non-critical validation gap | 72 hours |
| S4 — Low | Cosmetic defect, documentation error, minor UX improvement | Next sprint |

### 6.2 Defect Lifecycle

1. **Reported:** Tester logs defect with: title, severity, steps to reproduce, expected result, actual result, FR ID reference, screenshots or logs.
2. **Triaged:** Project lead assigns severity and priority within 4 hours of report.
3. **In Progress:** Developer acknowledges and begins fix.
4. **Fixed:** Developer commits fix with regression test covering the defect scenario.
5. **Verified:** Tester re-runs the failing test case on the fix branch.
6. **Closed:** Merged to main branch after verification.

### 6.3 Defect Tracking Tool

Defects are tracked in the project's GitHub Issues with the label `bug` and a severity label (`S1-critical`, `S2-high`, `S3-medium`, `S4-low`).

### 6.4 Release-Blocking Criteria

A release shall not proceed if any of the following remain open:

- Any S1 defect
- Any S2 defect older than 24 hours
- Any defect affecting tenant isolation, UNEB grading accuracy, or fee calculation accuracy
- Any defect tagged with a `[V&V-FAIL]` flag from the SRS audit

---

## 7 Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Project Lead (Peter Bamuhigire) | Test strategy approval, release go/no-go decision, S1 defect triage |
| Backend Developer | Unit tests, integration tests, performance test scripts, defect fixes |
| Frontend Developer | Component tests (Vitest), E2E test scripts (Playwright), UI defect fixes |
| QA Tester (contract/automated) | Test case execution, defect reporting, regression testing, UAT coordination |
| School Administrator (UAT) | User acceptance testing against real school workflows |

---

## 8 Tools Summary

| Category | Tool | Version |
|---|---|---|
| Unit testing (PHP) | PHPUnit | 10.x |
| Static analysis (PHP) | PHPStan | Level 8 |
| Unit testing (TypeScript) | Vitest | Latest |
| E2E / browser testing | Playwright | Latest |
| Performance / load testing | k6 | Latest |
| API performance profiling | Laravel Telescope | Latest |
| Code style (PHP) | PHP CS Fixer (PSR-12) | Latest |
| Code style (TypeScript) | ESLint + Prettier | Latest |
| CI/CD | GitHub Actions | N/A |
| Defect tracking | GitHub Issues | N/A |
| Accessibility scanning | Axe | Latest |

---

## 9 Risk Register for Testing

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| UNEB reference mark sheets unavailable for validation | Medium | High | Use publicly available UNEB grading rules; flag as `[CONTEXT-GAP]` until official samples are obtained |
| Limited internet bandwidth for performance testing from Uganda | High | Medium | Run performance tests from an Africa-region cloud instance; use network throttling to simulate 3G |
| Solo developer team limits test parallelism | High | Medium | Prioritise automated test suite; defer manual exploratory testing to UAT phase |
| SchoolPay sandbox unavailable for integration testing (Phase 2) | Medium | High | Build a mock SchoolPay API server for CI; test against live sandbox only in staging |
| Exam-period traffic spikes exceed load test scenarios | Low | High | Include spike test scenarios at 2x normal concurrency in k6 test suite |


---

## AI Module Testing Strategy

### AI Provider Mock Pattern

All AI feature unit tests use `MockAIProvider` — a deterministic implementation of the `AIProvider` interface that returns fixture responses without making external API calls. This ensures:
- Tests are fast (no network latency).
- Tests are deterministic (same input → same output).
- Tests can simulate error conditions (provider unavailable, budget exceeded, malformed JSON).

```php
// In TestCase::setUp()
$this->app->bind(AIProvider::class, MockAIProvider::class);

// MockAIProvider fixture registration
MockAIProvider::register('at_risk_students', [
    ['student_uid' => 'uuid-1', 'risk_level' => 'high_risk', 'signal' => 'Attendance 54%'],
    ['student_uid' => 'uuid-2', 'risk_level' => 'low_risk', 'signal' => 'No concerns'],
]);
```

### Shadow Testing in Staging

Before releasing any new AI feature to production, the feature runs in shadow mode in the staging environment for one full week:
1. The feature executes against real staging data.
2. Results are written to a shadow table (`nlp_results_shadow`) — not the live table.
3. A developer manually reviews 10% of the shadow results for accuracy.
4. The feature is promoted to production only if accuracy meets the acceptance threshold (≥ 80% correct classifications for predictive features).

### AI-Specific Test Cases (Minimum Required)

| Test | What It Verifies |
|---|---|
| TC-AI-001a | Gate blocks AI call when `tenant_ai_modules.status = 'suspended'` |
| TC-AI-001b | Gate blocks AI call when `feature_slug` is disabled (`is_enabled = 0`) |
| TC-AI-001c | At-risk classification: 5 high-risk students correctly identified from seeded data |
| TC-AI-001d | No student name appears in the prompt string (inspected via MockAIProvider call log) |
| TC-AI-002a | Report card comment: 10 comments generated; none saved without Accept action |
| TC-AI-002b | LLM unavailable: UI shows graceful error; report card workflow not blocked |
| TC-AI-004a | Fee risk: `pii_scrubbed = 1` in all `ai_audit_log` rows for fee prediction calls |
| TC-AI-007a | Budget 80% alert fires exactly once per billing period |
| TC-AI-007b | Budget 100% block: subsequent AI call returns HTTP 402 `AI_BUDGET_EXCEEDED` |
| TC-AI-SEC-01 | `PIIScrubber` removes NIN from test string (unit test, 1,000 patterns) |
| TC-AI-SEC-02 | Malformed LLM JSON response: no DB write, `ai_audit_log.outcome = 'error'` |
| TC-AI-SEC-03 | Prompt injection string: `AIInputSanitiser` strips injection; call proceeds with cleaned text |

### Hallucination Rate Acceptance Criterion

For the at-risk student classification feature: a maximum of 20% false positives (students classified `high_risk` who did not fail the term) is acceptable in the first 6 months. Above 20%, the prompt is tuned before the next weekly run. For fee default prediction: maximum 25% false positives (the cost of unnecessary contact is low; the cost of a missed default is high).
