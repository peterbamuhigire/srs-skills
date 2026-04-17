# Test Plan — Academia Pro

**Document ID:** AP-TP-001
**Version:** 1.0
**Date:** 2026-04-03
**Author:** Peter Bamuhigire
**Standard:** IEEE 829-2008
**Reference:** AP-TS-001 (Test Strategy v1.0)

---

## 1 Test Scope

### 1.1 In Scope (Phase 1)

All 51 functional requirements (FR-AUTH-001 through FR-APPLY-005, including FR-EMIS-002 and FR-EMIS-003) and 13 non-functional requirements (EDU-NFR-001 through EDU-NFR-005, UG-NFR-001 through UG-NFR-008).

Modules: Authentication, Tenant Management, Student Information, Academics Setup, Fees Management, Attendance, Examinations, Reports, RBAC, EMIS Export, Audit Log, Promotion, Departure, Student History, Record Sharing, Applications.

### 1.2 Out of Scope

- SchoolPay live API (Phase 2), MTN MoMo / Airtel Money (Phase 3+)
- Health records (Phase 7), Library/Transport/Hostel (Phase 9+)
- Pan-Africa localisation (Phase 11), USSD interface (Phase 11)

---

## 2 Test Case Summary

Total: 100 test cases across 16 modules and 3 NFR categories.

| TC-ID | Requirement | Description | Priority | Level |
|---|---|---|---|---|
| TC-AUTH-001 | FR-AUTH-001 | Valid login returns JWT | Critical | Integration |
| TC-AUTH-002 | FR-AUTH-001 | Lockout after 5 failed attempts | Critical | Integration |
| TC-AUTH-003 | FR-AUTH-001 | Invalid password returns 401 | Critical | Integration |
| TC-AUTH-004 | FR-AUTH-002 | JWT expires at 15 min | Critical | Unit |
| TC-AUTH-005 | FR-AUTH-003 | Refresh token rotation | Critical | Integration |
| TC-AUTH-006 | FR-AUTH-003 | Expired refresh token rejected | Critical | Integration |
| TC-AUTH-007 | FR-AUTH-004 | Logout invalidates tokens | High | Integration |
| TC-AUTH-008 | FR-AUTH-005 | Session timeout 30 min | High | E2E |
| TC-AUTH-009 | FR-AUTH-006 | MFA enforced — Super Admin | Critical | Integration |
| TC-AUTH-010 | FR-AUTH-006 | MFA enforced — School Owner | Critical | Integration |
| TC-TNT-001 | FR-TNT-001 | Create tenant | High | Integration |
| TC-TNT-002 | FR-TNT-002 | Update tenant config | High | Integration |
| TC-TNT-003 | FR-TNT-003 | Suspension blocks logins | Critical | Integration |
| TC-TNT-004 | FR-TNT-003 | Suspended data intact | Critical | Integration |
| TC-SIS-001 | FR-SIS-001 | Admit student, UID assigned | High | Integration |
| TC-SIS-002 | FR-SIS-001 | Duplicate NIN/LIN rejected | Critical | Integration |
| TC-SIS-003 | FR-SIS-002 | Enroll into academic year | High | Integration |
| TC-SIS-004 | FR-SIS-003 | Update student profile | Medium | Integration |
| TC-SIS-005 | FR-SIS-004 | Search by name/NIN/LIN | Medium | Integration |
| TC-SIS-006 | FR-SIS-005 | Photo upload/retrieval | Low | Integration |
| TC-ACA-001 | FR-ACA-001 | Create academic year + 3 terms | High | Integration |
| TC-ACA-002 | FR-ACA-002 | Create class/stream | High | Integration |
| TC-ACA-003 | FR-ACA-003 | Assign subjects to class | Medium | Integration |
| TC-ACA-004 | FR-ACA-004 | Assign class teacher | Medium | Integration |
| TC-FEE-001 | FR-FEE-001 | Define fee structure | Critical | Integration |
| TC-FEE-002 | FR-FEE-001 | Negative amount rejected | Critical | Unit |
| TC-FEE-003 | FR-FEE-002 | Record manual payment | Critical | Integration |
| TC-FEE-004 | FR-FEE-002 | Partial payment no minimum | Critical | Integration |
| TC-FEE-005 | FR-FEE-003 | Sequential receipt number | Critical | Integration |
| TC-FEE-006 | FR-FEE-003 | Receipt immutability | Critical | Integration |
| TC-FEE-007 | FR-FEE-004 | Balance accuracy | Critical | Unit |
| TC-FEE-008 | FR-FEE-004 | Arrears carry-forward | Critical | Unit |
| TC-FEE-009 | FR-FEE-005 | Double-payment prevention | Critical | Integration |
| TC-FEE-010 | FR-FEE-006 | Fee report per term | High | Integration |
| TC-FEE-011 | FR-FEE-007 | Refund — Owner approval | Critical | Integration |
| TC-FEE-012 | FR-FEE-007 | Refund — Bursar denied 403 | Critical | Integration |
| TC-ATT-001 | FR-ATT-001 | Mark present | High | Integration |
| TC-ATT-002 | FR-ATT-002 | Mark absent with reason | High | Integration |
| TC-ATT-003 | FR-ATT-003 | Term attendance summary | Medium | Integration |
| TC-ATT-004 | FR-ATT-004 | 3+ absence alert trigger | High | Unit |
| TC-EXM-001 | FR-EXM-001 | Create examination | High | Integration |
| TC-EXM-002 | FR-EXM-002 | Enter marks | High | Integration |
| TC-EXM-003 | FR-EXM-002 | Out-of-range mark rejected | Critical | Unit |
| TC-EXM-004 | FR-EXM-003 | Lock mark sheet | High | Integration |
| TC-EXM-005 | FR-EXM-004 | PLE D1/D2 boundary (12 vs 13) | Critical | Unit |
| TC-EXM-006 | FR-EXM-004 | PLE all division boundaries | Critical | Unit |
| TC-EXM-007 | FR-EXM-005 | UCE D1-F9 grading | Critical | Unit |
| TC-EXM-008 | FR-EXM-005 | UCE D1/D2 boundary (34 vs 35) | Critical | Unit |
| TC-EXM-009 | FR-EXM-006 | UACE best 3 principals | Critical | Unit |
| TC-EXM-010 | FR-EXM-007 | Thematic HC/C/NYC only | Critical | Unit |
| TC-EXM-011 | FR-EXM-008 | Class ranking | High | Unit |
| TC-EXM-012 | FR-EXM-008 | Tied rank handling | High | Unit |
| TC-RPT-001 | FR-RPT-001 | Single report card | High | Integration |
| TC-RPT-002 | FR-RPT-001 | Grades match UNEB engine | Critical | Integration |
| TC-RPT-003 | FR-RPT-002 | Bulk generation 200 students | High | Integration |
| TC-RPT-004 | FR-RPT-003 | Performance summary | Medium | Integration |
| TC-RPT-005 | FR-RPT-004 | PDF A4 rendering | Medium | E2E |
| TC-RBAC-001 | FR-RBAC-001 | Assign role | High | Integration |
| TC-RBAC-002 | FR-RBAC-002 | Privilege escalation blocked | Critical | Integration |
| TC-RBAC-003 | FR-RBAC-003 | Permission check | High | Integration |
| TC-RBAC-004 | FR-RBAC-004 | Unauthorised 403 | High | Integration |
| TC-RBAC-005 | FR-RBAC-005 | Custom permission override | Medium | Integration |
| TC-EMIS-001 | FR-EMIS-001 | Generate EMIS CSV | High | Integration |
| TC-EMIS-002 | FR-EMIS-001 | Field mapping accuracy | High | Unit |
| TC-EMIS-003 | FR-EMIS-002 | EMIS staff export generates valid .xlsx with teaching and non-teaching staff separated by nationality; NIN format validation; IPPS number inclusion for govt payroll staff | Medium | System |
| TC-EMIS-004 | FR-EMIS-003 | EMIS learner summary form export produces correct headcount by class and gender for selected academic year and term; totals match enrollment count | Medium | System |
| TC-AUD-001 | FR-AUD-001 | Create logged with diff | Critical | Integration |
| TC-AUD-002 | FR-AUD-001 | Log immutability | Critical | Integration |
| TC-AUD-003 | FR-AUD-001 | Required fields populated | Critical | Unit |
| TC-PROM-001 | FR-PROM-001 | Initiate wizard | High | E2E |
| TC-PROM-002 | FR-PROM-002 | Bulk promote | High | Integration |
| TC-PROM-003 | FR-PROM-003 | Mark as repeating | High | Integration |
| TC-PROM-004 | FR-PROM-004 | Final-year departure flag | High | Integration |
| TC-PROM-005 | FR-PROM-005 | Record lock after 30 days | Critical | Integration |
| TC-PROM-006 | FR-PROM-005 | Locked record mod returns 403 | Critical | Integration |
| TC-PROM-007 | FR-PROM-006 | Wizard draft persistence | Medium | Integration |
| TC-PROM-008 | FR-PROM-007 | Term 1 open gate | High | Integration |
| TC-DEPART-001 | FR-DEPART-001 | Record transfer | High | Integration |
| TC-DEPART-002 | FR-DEPART-002 | Deceased global lock | Critical | Integration |
| TC-DEPART-003 | FR-DEPART-003 | Expelled flag hidden | Critical | Integration |
| TC-DEPART-004 | FR-DEPART-004 | Reason code validation | Medium | Unit |
| TC-HIST-001 | FR-HIST-001 | View prior-school records | High | Integration |
| TC-HIST-002 | FR-HIST-002 | Fee amounts hidden | Critical | Integration |
| TC-HIST-003 | FR-HIST-003 | History survives suspension | Critical | Integration |
| TC-SHARE-001 | FR-SHARE-001 | Initiate record request | High | Integration |
| TC-SHARE-002 | FR-SHARE-002 | Approve request | High | Integration |
| TC-SHARE-003 | FR-SHARE-003 | Disciplinary consent required | Critical | Integration |
| TC-SHARE-004 | FR-SHARE-004 | Shared records read-only | High | Integration |
| TC-SHARE-005 | FR-SHARE-005 | Request expiry 30 days | Medium | Unit |
| TC-SHARE-006 | FR-SHARE-006 | Reject with reason | Medium | Integration |
| TC-SHARE-007 | FR-SHARE-007 | Request audit trail | High | Integration |
| TC-SHARE-008 | FR-SHARE-008 | Field restriction enforced | Critical | Integration |
| TC-APPLY-001 | FR-APPLY-001 | Submit application | High | Integration |
| TC-APPLY-002 | FR-APPLY-002 | School reviews application | High | Integration |
| TC-APPLY-003 | FR-APPLY-003 | Accept — auto-enroll | High | Integration |
| TC-APPLY-004 | FR-APPLY-004 | Reject with reason | Medium | Integration |
| TC-APPLY-005 | FR-APPLY-005 | Status visible to parent | Medium | E2E |
| TC-NFR-001 | UG-NFR-007 | Dashboard P95 ≤ 2,000 ms | High | Performance |
| TC-NFR-002 | UG-NFR-007 | CRUD API P95 ≤ 500 ms | High | Performance |
| TC-NFR-003 | UG-NFR-005 | OWASP Top 10 zero critical | Critical | Security |
| TC-NFR-004 | UG-NFR-008 | AES-256 PII at rest | Critical | Security |
| TC-NFR-005 | UG-NFR-008 | TLS 1.3 enforced | Critical | Security |
| TC-NFR-006 | EDU-NFR-002 | WCAG 2.1 AA zero violations | High | Accessibility |
| TC-NFR-007 | EDU-NFR-002 | Keyboard navigation complete | High | Accessibility |
| TC-NFR-008 | UG-NFR-005 | PDPO data export complete | High | Security |

---

## 3 Detailed Test Cases — Critical Modules

This section provides full test specifications for the 4 highest-risk areas. All other test cases follow the same structure; the summary table in Section 2 defines their scope.

### 3.1 Authentication

**TC-AUTH-001 — Valid Login**
- **REQ:** FR-AUTH-001 | **Priority:** Critical
- **Pre:** User account `status = active` with valid password hash.
- **Steps:** (1) `POST /api/auth/login` with valid credentials. (2) Assert HTTP 200. (3) Assert `access_token` and `refresh_token` in body. (4) Assert JWT payload contains `tenant_id`, `user_id`.
- **Pass:** JWT pair returned with correct claims.

**TC-AUTH-002 — Lockout After 5 Failures**
- **REQ:** FR-AUTH-001 | **Priority:** Critical
- **Pre:** User account `status = active`.
- **Steps:** (1) Send 5 login attempts with wrong password. (2) 6th attempt with correct password. (3) Assert HTTP 423.
- **Pass:** Account locked. Correct password rejected on 6th attempt.

**TC-AUTH-009 — MFA Enforced for Super Admin**
- **REQ:** FR-AUTH-006 | **Priority:** Critical
- **Pre:** Super Admin account.
- **Steps:** (1) `POST /api/auth/login` — assert `mfa_required = true`, no `access_token`. (2) `POST /api/auth/mfa/verify` with valid TOTP. (3) Assert JWT returned.
- **Pass:** No JWT issued without MFA verification.

### 3.2 Tenant Isolation

**TC-TNT-003 — Suspension Blocks Logins**
- **REQ:** FR-TNT-003 | **Priority:** Critical
- **Pre:** Tenant with active users.
- **Steps:** (1) Super Admin sets `status = suspended`. (2) Tenant user attempts login. (3) Assert HTTP 403 `TENANT_SUSPENDED`.
- **Pass:** All tenant logins blocked.

**TC-TNT-004 — Data Intact After Suspension**
- **REQ:** FR-TNT-003 | **Priority:** Critical
- **Pre:** Suspended tenant with student/fee records.
- **Steps:** (1) Reactivate tenant. (2) Login. (3) Query students and fees. (4) Assert records match pre-suspension state.
- **Pass:** Zero data loss during suspension.

### 3.3 Fees Management

**TC-FEE-004 — Partial Payment No Minimum**
- **REQ:** FR-FEE-002 | **Priority:** Critical
- **Pre:** Fee total = UGX 450,000.
- **Steps:** (1) `POST /api/payments` with `amount = 1000`. (2) Assert HTTP 201. (3) Assert `outstanding_balance = 449,000`.
- **Pass:** UGX 1,000 accepted. Balance correct.

**TC-FEE-006 — Receipt Immutability**
- **REQ:** FR-FEE-003 | **Priority:** Critical
- **Pre:** Receipt exists.
- **Steps:** (1) `DELETE /api/receipts/{id}` — assert 403. (2) `PATCH /api/receipts/{id}` — assert 403.
- **Pass:** Receipts cannot be deleted or modified.

**TC-FEE-007 — Balance Accuracy**
- **REQ:** FR-FEE-004 | **Priority:** Critical
- **Pre:** Fee = UGX 450,000. Payments = 200,000 + 100,000 + 50,000.
- **Steps:** (1) `GET /api/students/{uid}/balance`. (2) Assert `outstanding_balance = 100,000`. (3) Verify integer arithmetic (no float rounding).
- **Pass:** Balance = total - sum(payments) = UGX 100,000 exact.

**TC-FEE-008 — Arrears Carry-Forward**
- **REQ:** FR-FEE-004 | **Priority:** Critical
- **Pre:** Term 1 unpaid = UGX 50,000. Term 2 fee = UGX 450,000.
- **Steps:** (1) Query Term 2 balance. (2) Assert `outstanding_balance = 500,000`.
- **Pass:** Arrears carried forward correctly.

**TC-FEE-009 — Double-Payment Prevention**
- **REQ:** FR-FEE-005 | **Priority:** Critical
- **Pre:** Payment `PAY-20260403-001` already recorded.
- **Steps:** (1) Submit identical payment within 5 min. (2) Assert `DUPLICATE` status. (3) Assert original receipt returned. (4) Assert balance unchanged.
- **Pass:** Duplicate rejected. Zero double charges.

**TC-FEE-012 — Bursar Refund Denied**
- **REQ:** FR-FEE-007 | **Priority:** Critical
- **Pre:** Authenticated as Bursar.
- **Steps:** (1) `POST /api/refunds` with `payment_id`. (2) Assert HTTP 403.
- **Pass:** Bursar lacks refund permission.

### 3.4 UNEB Grading Engine

**TC-EXM-005 — PLE Division I/II Boundary**
- **REQ:** FR-EXM-004 | **Priority:** Critical
- **Steps:** (1) Compute aggregate = 12. Assert Division I. (2) Compute aggregate = 13. Assert Division II.
- **Pass:** Boundary values produce correct divisions.

**TC-EXM-006 — PLE All Division Boundaries**
- **REQ:** FR-EXM-004 | **Priority:** Critical
- **Steps:** (1) Aggregate 4 = Div I, 12 = Div I. (2) 13 = Div II, 23 = Div II. (3) 24 = Div III, 29 = Div III. (4) 30 = Div IV, 34 = Div IV. (5) 35 = Ungraded, 36 = Ungraded.
- **Pass:** 100% match with UNEB reference data.

**TC-EXM-008 — UCE Division I/II Boundary**
- **REQ:** FR-EXM-005 | **Priority:** Critical
- **Steps:** (1) Aggregate = 34 → Division I. (2) Aggregate = 35 → Division II.
- **Pass:** UCE boundary correct.

**TC-EXM-009 — UACE Best 3 Principals**
- **REQ:** FR-EXM-006 | **Priority:** Critical
- **Pre:** Student with 4 principal subjects: A(6), B(5), D(3), E(2).
- **Steps:** (1) Compute points. (2) Assert best 3 = A+B+D = 14. (3) Assert subsidiary scored separately.
- **Pass:** Points from best 3 principal subjects only.

**TC-EXM-010 — Thematic Curriculum Descriptors**
- **REQ:** FR-EXM-007 | **Priority:** Critical
- **Steps:** (1) Enter HC, C, NYC for P2 student. (2) Assert no numeric grades stored. (3) Submit invalid descriptor `A`. (4) Assert HTTP 422.
- **Pass:** Only HC/C/NYC accepted. No numeric grades.

**TC-RPT-002 — Report Card Matches UNEB Engine**
- **REQ:** FR-RPT-001 | **Priority:** Critical
- **Pre:** UCE student with marks graded.
- **Steps:** (1) Generate report card. (2) Cross-reference every grade with direct engine output. (3) Assert 100% match.
- **Pass:** Zero discrepancies between report card and engine.

---

## 4 Non-Functional Test Cases

**TC-NFR-001 — Dashboard Load (Performance)**
- **REQ:** UG-NFR-007 | **Tool:** Playwright + 3G throttle
- **Steps:** (1) 50 concurrent logins on staging (2,000 students). (2) Measure P95 load.
- **Pass:** P95 ≤ 2,000 ms.

**TC-NFR-002 — API Response (Performance)**
- **REQ:** UG-NFR-007 | **Tool:** k6
- **Steps:** (1) 200 concurrent `GET /api/students`. (2) Measure P95.
- **Pass:** P95 ≤ 500 ms.

**TC-NFR-003 — OWASP Top 10 (Security)**
- **REQ:** UG-NFR-005 | **Tool:** OWASP ZAP
- **Steps:** (1) Pen test all endpoints on staging.
- **Pass:** Zero critical or high findings.

**TC-NFR-004 — PII Encryption at Rest**
- **REQ:** UG-NFR-008
- **Steps:** (1) Query raw `guardian_nin` column. (2) Assert AES-256 ciphertext. (3) Assert app decryption returns original.
- **Pass:** PII encrypted, not plaintext.

**TC-NFR-005 — TLS 1.3 Enforced**
- **REQ:** UG-NFR-008
- **Steps:** (1) TLS 1.1 connection refused. (2) TLS 1.2 refused (except USSD). (3) TLS 1.3 succeeds.
- **Pass:** Only TLS 1.3 on standard endpoints.

**TC-NFR-006 — WCAG 2.1 AA (Accessibility)**
- **REQ:** EDU-NFR-002 | **Tool:** Axe
- **Steps:** (1) Scan all portal pages. (2) Assert zero violations.
- **Pass:** Full WCAG 2.1 AA automated compliance.

**TC-NFR-007 — Keyboard Navigation**
- **REQ:** EDU-NFR-002
- **Steps:** (1) Navigate all interactive elements via Tab/Enter/Escape/Arrow only. (2) Assert visible focus indicator.
- **Pass:** All elements operable without pointer.

**TC-NFR-008 — PDPO Data Export**
- **REQ:** UG-NFR-005
- **Steps:** (1) `GET /api/students/{uid}/data-export`. (2) Assert complete JSON with all personal, academic, attendance, and fee data.
- **Pass:** Full data export for PDPO compliance.

---

## 5 Test Data Requirements

| Data Set | Description | Source |
|---|---|---|
| 3 test tenants | School A, B, C with distinct configs | `database/seeders/testing/TenantSeeder.php` |
| 2,000 students | Across 3 tenants, 14 classes (P1-P7, S1-S6) | `database/seeders/testing/StudentSeeder.php` |
| 80 staff users | Roles: Owner, Head Teacher, Teacher, Bursar, Admin | `database/seeders/testing/UserSeeder.php` |
| UNEB reference marks | Boundary values for PLE, UCE, UACE, Thematic | `tests/fixtures/uneb-reference-marks.json` |
| Fee scenarios | Partial payments, arrears, double-payment | `tests/fixtures/fee-scenarios.json` |
| Transfer scenarios | Cross-tenant enrollment history | `database/seeders/testing/TransferSeeder.php` |

All test data is synthetic. No real student names, NIN, LIN, or contact information permitted.

---

## 6 Schedule

| Phase | Activities | Sprints | Duration |
|---|---|---|---|
| A — Unit tests | Grading engine, fee calc, validators | 1-2 | 2 weeks |
| B — Integration tests | API tests for all 16 FR modules | 2-4 | 3 weeks |
| C — E2E tests | 8 critical Playwright flows | 4-5 | 2 weeks |
| D — NFR tests | k6 performance, OWASP ZAP, Axe | 5 | 1 week |
| E — UAT | School admin acceptance testing | 6 | 1 week |
| F — Regression | Full suite before release candidate | 6 | 3 days |

---

## 7 Resources

| Role | Responsibility |
|---|---|
| Peter Bamuhigire (Lead) | Plan approval, S1 triage, release decision |
| Backend Developer | PHPUnit/Pest tests, k6 scripts |
| Frontend Developer | Vitest components, Playwright E2E |
| QA Tester (contract) | Execution, defect reporting, UAT coordination |
| School Administrator | UAT against real workflows (Sprint 6) |

**Tools:** PHPUnit 10.x, Vitest, Playwright, k6, Axe, OWASP ZAP, Laravel Telescope, GitHub Actions.

---

## 8 Traceability Matrix

| REQ-ID | TC-IDs |
|---|---|
| FR-AUTH-001 | TC-AUTH-001, TC-AUTH-002, TC-AUTH-003 |
| FR-AUTH-002 | TC-AUTH-004 |
| FR-AUTH-003 | TC-AUTH-005, TC-AUTH-006 |
| FR-AUTH-004 | TC-AUTH-007 |
| FR-AUTH-005 | TC-AUTH-008 |
| FR-AUTH-006 | TC-AUTH-009, TC-AUTH-010 |
| FR-TNT-001 | TC-TNT-001 |
| FR-TNT-002 | TC-TNT-002 |
| FR-TNT-003 | TC-TNT-003, TC-TNT-004 |
| FR-SIS-001 | TC-SIS-001, TC-SIS-002 |
| FR-SIS-002 | TC-SIS-003 |
| FR-SIS-003 | TC-SIS-004 |
| FR-SIS-004 | TC-SIS-005 |
| FR-SIS-005 | TC-SIS-006 |
| FR-ACA-001 | TC-ACA-001 |
| FR-ACA-002 | TC-ACA-002 |
| FR-ACA-003 | TC-ACA-003 |
| FR-ACA-004 | TC-ACA-004 |
| FR-FEE-001 | TC-FEE-001, TC-FEE-002 |
| FR-FEE-002 | TC-FEE-003, TC-FEE-004 |
| FR-FEE-003 | TC-FEE-005, TC-FEE-006 |
| FR-FEE-004 | TC-FEE-007, TC-FEE-008 |
| FR-FEE-005 | TC-FEE-009 |
| FR-FEE-006 | TC-FEE-010 |
| FR-FEE-007 | TC-FEE-011, TC-FEE-012 |
| FR-ATT-001 | TC-ATT-001 |
| FR-ATT-002 | TC-ATT-002 |
| FR-ATT-003 | TC-ATT-003 |
| FR-ATT-004 | TC-ATT-004 |
| FR-EXM-001 | TC-EXM-001 |
| FR-EXM-002 | TC-EXM-002, TC-EXM-003 |
| FR-EXM-003 | TC-EXM-004 |
| FR-EXM-004 | TC-EXM-005, TC-EXM-006 |
| FR-EXM-005 | TC-EXM-007, TC-EXM-008 |
| FR-EXM-006 | TC-EXM-009 |
| FR-EXM-007 | TC-EXM-010 |
| FR-EXM-008 | TC-EXM-011, TC-EXM-012 |
| FR-RPT-001 | TC-RPT-001, TC-RPT-002 |
| FR-RPT-002 | TC-RPT-003 |
| FR-RPT-003 | TC-RPT-004 |
| FR-RPT-004 | TC-RPT-005 |
| FR-RBAC-001 | TC-RBAC-001 |
| FR-RBAC-002 | TC-RBAC-002 |
| FR-RBAC-003 | TC-RBAC-003 |
| FR-RBAC-004 | TC-RBAC-004 |
| FR-RBAC-005 | TC-RBAC-005 |
| FR-EMIS-001 | TC-EMIS-001, TC-EMIS-002 |
| FR-EMIS-002 | TC-EMIS-003 |
| FR-EMIS-003 | TC-EMIS-004 |
| FR-AUD-001 | TC-AUD-001, TC-AUD-002, TC-AUD-003 |
| FR-PROM-001 | TC-PROM-001 |
| FR-PROM-002 | TC-PROM-002 |
| FR-PROM-003 | TC-PROM-003 |
| FR-PROM-004 | TC-PROM-004 |
| FR-PROM-005 | TC-PROM-005, TC-PROM-006 |
| FR-PROM-006 | TC-PROM-007 |
| FR-PROM-007 | TC-PROM-008 |
| FR-DEPART-001 | TC-DEPART-001 |
| FR-DEPART-002 | TC-DEPART-002 |
| FR-DEPART-003 | TC-DEPART-003 |
| FR-DEPART-004 | TC-DEPART-004 |
| FR-HIST-001 | TC-HIST-001 |
| FR-HIST-002 | TC-HIST-002 |
| FR-HIST-003 | TC-HIST-003 |
| FR-SHARE-001 | TC-SHARE-001 |
| FR-SHARE-002 | TC-SHARE-002 |
| FR-SHARE-003 | TC-SHARE-003 |
| FR-SHARE-004 | TC-SHARE-004 |
| FR-SHARE-005 | TC-SHARE-005 |
| FR-SHARE-006 | TC-SHARE-006 |
| FR-SHARE-007 | TC-SHARE-007 |
| FR-SHARE-008 | TC-SHARE-008 |
| FR-APPLY-001 | TC-APPLY-001 |
| FR-APPLY-002 | TC-APPLY-002 |
| FR-APPLY-003 | TC-APPLY-003 |
| FR-APPLY-004 | TC-APPLY-004 |
| FR-APPLY-005 | TC-APPLY-005 |
| UG-NFR-005 | TC-NFR-003, TC-NFR-008 |
| UG-NFR-007 | TC-NFR-001, TC-NFR-002 |
| UG-NFR-008 | TC-NFR-004, TC-NFR-005 |
| EDU-NFR-002 | TC-NFR-006, TC-NFR-007 |

**Coverage:** 51/51 FRs covered (100%). 4/13 NFRs have dedicated test cases; remaining NFRs verified through code quality gates (PHPStan Level 8, coverage thresholds) and operational monitoring.


---

## AI Module Test Cases

| TC ID | Requirement | Test Steps | Expected Result |
|---|---|---|---|
| TC-AI-006 | FR-AI-006 | POST `/adminpanel/api/v1/tenants/{id}/ai-module` with plan = growth | HTTP 201; `tenant_ai_modules` row created; 9 `tenant_ai_features` rows seeded with `is_enabled = 0` |
| TC-AI-006b | FR-AI-006 | Repeat the same POST for the same tenant | HTTP 409 `AI_MODULE_ALREADY_ACTIVE` |
| TC-AI-GATE-01 | FR-AI-001 | Call at-risk API for tenant with `status = 'suspended'` | HTTP 402 `AI_MODULE_INACTIVE` |
| TC-AI-GATE-02 | FR-AI-001 | Call at-risk API for tenant with module active but `at_risk_students` feature `is_enabled = 0` | HTTP 402 `AI_MODULE_INACTIVE` |
| TC-AI-BUDGET-01 | FR-AI-007 | Set budget to UGX 10,000; simulate usage of UGX 8,001 | In-app notification delivered to owner; `ai_budget_alerts` row with `threshold_pct = 80` created |
| TC-AI-BUDGET-02 | FR-AI-007 | Continue simulating usage to UGX 10,001 | In-app + email notification; next AI call returns HTTP 402 `AI_BUDGET_EXCEEDED` |
| TC-AI-BUDGET-03 | FR-AI-007 | Attempt to create a second 80% alert in the same billing period | Only 1 row in `ai_budget_alerts` for that threshold (UNIQUE constraint prevents duplicate) |
| TC-AI-PII-01 | FR-AI-004 | Run fee default prediction batch; inspect `ai_audit_log` | `pii_scrubbed = 1` for all rows; no NIN or phone number found in prompt hashes when decoded |
| TC-AI-PII-02 | FR-AI-005 | Run parent sentiment with a response containing a parent name | Scrubbed name replaced by `[NAME-REDACTED]` in prompt; `pii_scrubbed = 1` |
| TC-AI-NFR-01 | AI-NFR-001 | Load Owner dashboard with AI features enabled; measure time to full AI panel | Skeleton within 500 ms; full panel within 8,000 ms at P95 (k6 load test, 50 users) |
| TC-AI-NFR-05 | AI-NFR-005 | Run `PIIScrubber::scrub()` against 1,000 strings containing NIN, mobile, email, and names | Zero false negatives; all 6 identifier types removed in every test case |
