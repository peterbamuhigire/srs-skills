# Test Report — Academia Pro

**Document ID:** AP-TR-001
**Version:** 1.0
**Date:** [TBD]
**Author:** [TBD]
**Standard:** IEEE 829-2008, Sections 9-10
**Reference:** AP-TP-001 (Test Plan v1.0), AP-TS-001 (Test Strategy v1.0)

---

## 1 Executive Summary

This report documents the results of test execution for Academia Pro Phase 1, covering 98 test cases across 16 functional modules and 3 non-functional requirement categories.

| Metric | Value |
|---|---|
| Total Test Cases | 98 |
| Passed | [TBD] |
| Failed | [TBD] |
| Blocked | [TBD] |
| Skipped | [TBD] |
| Pass Rate | [TBD]% |
| Requirement Coverage | [TBD]% |
| Code Coverage — Backend | [TBD]% (target: ≥80%) |
| Code Coverage — Frontend | [TBD]% (target: ≥70%) |
| UNEB Grading + Fee Calc Coverage | [TBD]% (target: 100%) |
| Critical Defects Open | [TBD] |
| Release Recommendation | [TBD] |

**Test Period:** [TBD] to [TBD]

**Environment:** [TBD — e.g., staging server, Laravel version, PHP version, database]

---

## 2 Test Execution Log

All 98 test cases from AP-TP-001 are listed below, grouped by module. Record each result during execution.

### 2.1 Authentication (10 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-AUTH-001` | Valid login returns JWT | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-002` | Lockout after 5 failed attempts | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-003` | Invalid password returns 401 | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-004` | JWT expires at 15 min | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-005` | Refresh token rotation | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-006` | Expired refresh token rejected | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-007` | Logout invalidates tokens | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-008` | Session timeout 30 min | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-009` | MFA enforced — Super Admin | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUTH-010` | MFA enforced — School Owner | [TBD] | [TBD] | [TBD] | — | |

### 2.2 Tenant Management (4 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-TNT-001` | Create tenant | [TBD] | [TBD] | [TBD] | — | |
| `TC-TNT-002` | Update tenant config | [TBD] | [TBD] | [TBD] | — | |
| `TC-TNT-003` | Suspension blocks logins | [TBD] | [TBD] | [TBD] | — | |
| `TC-TNT-004` | Suspended data intact | [TBD] | [TBD] | [TBD] | — | |

### 2.3 Student Information (6 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-SIS-001` | Admit student, UID assigned | [TBD] | [TBD] | [TBD] | — | |
| `TC-SIS-002` | Duplicate NIN/LIN rejected | [TBD] | [TBD] | [TBD] | — | |
| `TC-SIS-003` | Enroll into academic year | [TBD] | [TBD] | [TBD] | — | |
| `TC-SIS-004` | Update student profile | [TBD] | [TBD] | [TBD] | — | |
| `TC-SIS-005` | Search by name/NIN/LIN | [TBD] | [TBD] | [TBD] | — | |
| `TC-SIS-006` | Photo upload/retrieval | [TBD] | [TBD] | [TBD] | — | |

### 2.4 Academics Setup (4 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-ACA-001` | Create academic year + 3 terms | [TBD] | [TBD] | [TBD] | — | |
| `TC-ACA-002` | Create class/stream | [TBD] | [TBD] | [TBD] | — | |
| `TC-ACA-003` | Assign subjects to class | [TBD] | [TBD] | [TBD] | — | |
| `TC-ACA-004` | Assign class teacher | [TBD] | [TBD] | [TBD] | — | |

### 2.5 Fees Management (12 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-FEE-001` | Define fee structure | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-002` | Negative amount rejected | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-003` | Record manual payment | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-004` | Partial payment no minimum | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-005` | Sequential receipt number | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-006` | Receipt immutability | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-007` | Balance accuracy | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-008` | Arrears carry-forward | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-009` | Double-payment prevention | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-010` | Fee report per term | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-011` | Refund — Owner approval | [TBD] | [TBD] | [TBD] | — | |
| `TC-FEE-012` | Refund — Bursar denied 403 | [TBD] | [TBD] | [TBD] | — | |

### 2.6 Attendance (4 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-ATT-001` | Mark present | [TBD] | [TBD] | [TBD] | — | |
| `TC-ATT-002` | Mark absent with reason | [TBD] | [TBD] | [TBD] | — | |
| `TC-ATT-003` | Term attendance summary | [TBD] | [TBD] | [TBD] | — | |
| `TC-ATT-004` | 3+ absence alert trigger | [TBD] | [TBD] | [TBD] | — | |

### 2.7 Examinations (12 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-EXM-001` | Create examination | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-002` | Enter marks | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-003` | Out-of-range mark rejected | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-004` | Lock mark sheet | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-005` | PLE D1/D2 boundary (12 vs 13) | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-006` | PLE all division boundaries | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-007` | UCE D1-F9 grading | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-008` | UCE D1/D2 boundary (34 vs 35) | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-009` | UACE best 3 principals | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-010` | Thematic HC/C/NYC only | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-011` | Class ranking | [TBD] | [TBD] | [TBD] | — | |
| `TC-EXM-012` | Tied rank handling | [TBD] | [TBD] | [TBD] | — | |

### 2.8 Reports (5 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-RPT-001` | Single report card | [TBD] | [TBD] | [TBD] | — | |
| `TC-RPT-002` | Grades match UNEB engine | [TBD] | [TBD] | [TBD] | — | |
| `TC-RPT-003` | Bulk generation 200 students | [TBD] | [TBD] | [TBD] | — | |
| `TC-RPT-004` | Performance summary | [TBD] | [TBD] | [TBD] | — | |
| `TC-RPT-005` | PDF A4 rendering | [TBD] | [TBD] | [TBD] | — | |

### 2.9 RBAC (5 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-RBAC-001` | Assign role | [TBD] | [TBD] | [TBD] | — | |
| `TC-RBAC-002` | Privilege escalation blocked | [TBD] | [TBD] | [TBD] | — | |
| `TC-RBAC-003` | Permission check | [TBD] | [TBD] | [TBD] | — | |
| `TC-RBAC-004` | Unauthorised 403 | [TBD] | [TBD] | [TBD] | — | |
| `TC-RBAC-005` | Custom permission override | [TBD] | [TBD] | [TBD] | — | |

### 2.10 EMIS Export (2 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-EMIS-001` | Generate EMIS CSV | [TBD] | [TBD] | [TBD] | — | |
| `TC-EMIS-002` | Field mapping accuracy | [TBD] | [TBD] | [TBD] | — | |

### 2.11 Audit Log (3 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-AUD-001` | Create logged with diff | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUD-002` | Log immutability | [TBD] | [TBD] | [TBD] | — | |
| `TC-AUD-003` | Required fields populated | [TBD] | [TBD] | [TBD] | — | |

### 2.12 Promotion (8 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-PROM-001` | Initiate wizard | [TBD] | [TBD] | [TBD] | — | |
| `TC-PROM-002` | Bulk promote | [TBD] | [TBD] | [TBD] | — | |
| `TC-PROM-003` | Mark as repeating | [TBD] | [TBD] | [TBD] | — | |
| `TC-PROM-004` | Final-year departure flag | [TBD] | [TBD] | [TBD] | — | |
| `TC-PROM-005` | Record lock after 30 days | [TBD] | [TBD] | [TBD] | — | |
| `TC-PROM-006` | Locked record mod returns 403 | [TBD] | [TBD] | [TBD] | — | |
| `TC-PROM-007` | Wizard draft persistence | [TBD] | [TBD] | [TBD] | — | |
| `TC-PROM-008` | Term 1 open gate | [TBD] | [TBD] | [TBD] | — | |

### 2.13 Departure (4 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-DEPART-001` | Record transfer | [TBD] | [TBD] | [TBD] | — | |
| `TC-DEPART-002` | Deceased global lock | [TBD] | [TBD] | [TBD] | — | |
| `TC-DEPART-003` | Expelled flag hidden | [TBD] | [TBD] | [TBD] | — | |
| `TC-DEPART-004` | Reason code validation | [TBD] | [TBD] | [TBD] | — | |

### 2.14 Student History (3 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-HIST-001` | View prior-school records | [TBD] | [TBD] | [TBD] | — | |
| `TC-HIST-002` | Fee amounts hidden | [TBD] | [TBD] | [TBD] | — | |
| `TC-HIST-003` | History survives suspension | [TBD] | [TBD] | [TBD] | — | |

### 2.15 Record Sharing (8 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-SHARE-001` | Initiate record request | [TBD] | [TBD] | [TBD] | — | |
| `TC-SHARE-002` | Approve request | [TBD] | [TBD] | [TBD] | — | |
| `TC-SHARE-003` | Disciplinary consent required | [TBD] | [TBD] | [TBD] | — | |
| `TC-SHARE-004` | Shared records read-only | [TBD] | [TBD] | [TBD] | — | |
| `TC-SHARE-005` | Request expiry 30 days | [TBD] | [TBD] | [TBD] | — | |
| `TC-SHARE-006` | Reject with reason | [TBD] | [TBD] | [TBD] | — | |
| `TC-SHARE-007` | Request audit trail | [TBD] | [TBD] | [TBD] | — | |
| `TC-SHARE-008` | Field restriction enforced | [TBD] | [TBD] | [TBD] | — | |

### 2.16 Applications (5 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-APPLY-001` | Submit application | [TBD] | [TBD] | [TBD] | — | |
| `TC-APPLY-002` | School reviews application | [TBD] | [TBD] | [TBD] | — | |
| `TC-APPLY-003` | Accept — auto-enroll | [TBD] | [TBD] | [TBD] | — | |
| `TC-APPLY-004` | Reject with reason | [TBD] | [TBD] | [TBD] | — | |
| `TC-APPLY-005` | Status visible to parent | [TBD] | [TBD] | [TBD] | — | |

### 2.17 Non-Functional Requirements (8 TCs)

| TC-ID | Test Case Name | Result | Date | Tester | Defect Ref | Notes |
|---|---|---|---|---|---|---|
| `TC-NFR-001` | Dashboard P95 ≤ 2,000 ms | [TBD] | [TBD] | [TBD] | — | |
| `TC-NFR-002` | CRUD API P95 ≤ 500 ms | [TBD] | [TBD] | [TBD] | — | |
| `TC-NFR-003` | OWASP Top 10 zero critical | [TBD] | [TBD] | [TBD] | — | |
| `TC-NFR-004` | AES-256 PII at rest | [TBD] | [TBD] | [TBD] | — | |
| `TC-NFR-005` | TLS 1.3 enforced | [TBD] | [TBD] | [TBD] | — | |
| `TC-NFR-006` | WCAG 2.1 AA zero violations | [TBD] | [TBD] | [TBD] | — | |
| `TC-NFR-007` | Keyboard navigation complete | [TBD] | [TBD] | [TBD] | — | |
| `TC-NFR-008` | PDPO data export complete | [TBD] | [TBD] | [TBD] | — | |

---

## 3 Defect Log

Record all defects discovered during test execution. Assign a sequential `DEF-nnn` identifier.

| DEF-ID | Severity | Priority | Status | Summary | Steps to Reproduce | Linked TC-ID | Assigned To | Resolution Date |
|---|---|---|---|---|---|---|---|---|
| `DEF-001` | Major | P2 | Open | PLACEHOLDER: Arrears carry-forward calculates incorrectly when Term 1 has partial refund | 1. Create fee UGX 450,000. 2. Pay UGX 400,000. 3. Process refund UGX 50,000. 4. Open Term 2. 5. Observe balance. | `TC-FEE-008` | [TBD] | — |
| `DEF-002` | Critical | P1 | Open | PLACEHOLDER: MFA bypass when TOTP clock skew exceeds 90 seconds | 1. Set device clock +2 min. 2. Login as Super Admin. 3. Submit expired TOTP. 4. Observe JWT issued. | `TC-AUTH-009` | [TBD] | — |
| `DEF-003` | Minor | P3 | Resolved | PLACEHOLDER: Class ranking display truncates tied students at position 10 | 1. Enter identical marks for 3 students. 2. Generate ranking for class of 40. 3. Observe positions 10-12. | `TC-EXM-012` | [TBD] | [TBD] |

**Severity Definitions:**

- **Critical** — System crash, data loss, security breach, or financial calculation error. Blocks release.
- **Major** — Feature broken or produces incorrect results. Workaround may exist.
- **Minor** — Cosmetic issue, minor usability problem, or edge case with low impact.
- **Trivial** — Typo, alignment issue, or documentation discrepancy.

**Priority Definitions:**

- **P1** — Fix immediately. Blocks current test cycle.
- **P2** — Fix before release candidate.
- **P3** — Fix in next sprint.
- **P4** — Backlog; fix when convenient.

---

## 4 Coverage Metrics

### 4.1 Requirement Coverage

| Category | Total Requirements | Requirements with Executed TCs | Coverage |
|---|---|---|---|
| Functional (FR-*) | 49 | [TBD] | [TBD]% |
| Non-Functional (NFR-*) | 13 | [TBD] | [TBD]% |
| **Total** | **62** | **[TBD]** | **[TBD]%** |

### 4.2 Feature Coverage

| Module | Total TCs | Executed | Passed | Failed | Blocked | Skipped |
|---|---|---|---|---|---|---|
| Authentication | 10 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Tenant Management | 4 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Student Information | 6 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Academics Setup | 4 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Fees Management | 12 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Attendance | 4 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Examinations | 12 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Reports | 5 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| RBAC | 5 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| EMIS Export | 2 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Audit Log | 3 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Promotion | 8 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Departure | 4 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Student History | 3 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Record Sharing | 8 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Applications | 5 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| NFR | 8 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| **Total** | **98** | **[TBD]** | **[TBD]** | **[TBD]** | **[TBD]** | **[TBD]** |

### 4.3 Code Coverage

| Metric | Target | Actual | Status |
|---|---|---|---|
| Backend (PHPUnit/Pest) | ≥80% | [TBD]% | [TBD] |
| Frontend (Vitest) | ≥70% | [TBD]% | [TBD] |
| UNEB Grading Engine | 100% | [TBD]% | [TBD] |
| Fee Calculation Module | 100% | [TBD]% | [TBD] |

### 4.4 Coverage Gaps

List all test cases that were not executed and the reason for non-execution.

| TC-ID | Reason for Non-Execution | Planned Resolution |
|---|---|---|
| [TBD] | [TBD] | [TBD] |

---

## 5 Failed Test Analysis

Document root cause analysis for each failed test case. Add one entry per failure.

### Failure 1 (Example)

| Field | Value |
|---|---|
| **TC-ID** | `TC-FEE-008` |
| **Test Case Name** | Arrears carry-forward |
| **Failure Description** | Outstanding balance from Term 1 (UGX 50,000) was not added to Term 2 fee total. Term 2 balance displayed UGX 450,000 instead of expected UGX 500,000. |
| **Root Cause Category** | Defect |
| **Root Cause Detail** | `FeeCalculationService::getOutstandingBalance()` queries only the current term. Missing cross-term arrears aggregation query. |
| **Impact Assessment** | Financial — schools would under-bill students with outstanding balances. Affects all fee reports and statements. |
| **Linked Defect** | `DEF-001` |
| **Remediation Action** | Add `previous_term_arrears` column to balance query. Update `FeeCalculationService` to sum across terms. Rerun `TC-FEE-007` and `TC-FEE-008`. |
| **Remediation Owner** | [TBD] |
| **Target Fix Date** | [TBD] |

### Failure 2 (Example)

| Field | Value |
|---|---|
| **TC-ID** | `TC-AUTH-009` |
| **Test Case Name** | MFA enforced — Super Admin |
| **Failure Description** | JWT was issued without MFA verification when TOTP validation service returned a timeout error instead of a rejection. |
| **Root Cause Category** | Defect |
| **Root Cause Detail** | `MfaVerificationService::verify()` treats timeout exceptions as successful verification due to missing error-type check in the catch block. |
| **Impact Assessment** | Security — Super Admin accounts could be accessed without MFA under degraded TOTP service conditions. Critical severity. |
| **Linked Defect** | `DEF-002` |
| **Remediation Action** | Modify catch block to treat all non-success responses (including timeouts) as MFA failure. Add dedicated timeout test case. Rerun `TC-AUTH-009` and `TC-AUTH-010`. |
| **Remediation Owner** | [TBD] |
| **Target Fix Date** | [TBD] |

---

## 6 Recommendations

### 6.1 Release Readiness Decision

| Decision | [TBD: Go / No-Go / Conditional] |
|---|---|
| **Rationale** | [TBD — summarise pass rate, open critical defects, coverage gaps] |

**Conditions for Conditional Release (if applicable):**

- [TBD — e.g., "All P1 defects resolved and verified"]
- [TBD — e.g., "UNEB grading engine achieves 100% coverage"]
- [TBD — e.g., "OWASP ZAP scan returns zero critical findings"]

### 6.2 Outstanding Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [TBD — e.g., Untested SchoolPay integration] | [TBD] | [TBD] | [TBD] |
| [TBD — e.g., Performance under 3G not validated with production data] | [TBD] | [TBD] | [TBD] |
| [TBD — e.g., UAT conducted with synthetic data only] | [TBD] | [TBD] | [TBD] |

### 6.3 Required Follow-up Actions

| Action | Owner | Target Date | Status |
|---|---|---|---|
| Resolve all open Critical and Major defects | [TBD] | [TBD] | [TBD] |
| Rerun failed test cases after defect fixes | [TBD] | [TBD] | [TBD] |
| Complete regression suite before release candidate | [TBD] | [TBD] | [TBD] |
| Obtain UAT sign-off from pilot school administrator | [TBD] | [TBD] | [TBD] |

---

## 7 Sign-Off

Approval confirms that test execution is complete, results are accurately recorded, and the release readiness recommendation has been reviewed.

| Role | Name | Date | Signature |
|---|---|---|---|
| QA Lead | [TBD] | [TBD] | ________________ |
| Project Manager | [TBD] | [TBD] | ________________ |
| Product Owner | [TBD] | [TBD] | ________________ |

---

*End of Test Report Template — AP-TR-001*
