# Test Plan for Medic8 Phase 1 MVP

**Project:** Medic8 Multi-Tenant SaaS Healthcare Management System
**Document standard:** IEEE 829-2008, IEEE 29119-3:2013
**Version:** 1.0
**Status:** Draft
**Phase:** Phase 1 (Foundation)

---

## 1 Test Scope

### 1.1 Modules in Scope

Phase 1 delivers 9 functional modules covering patient registration through billing. All modules listed below are included in this test plan.

| Module | FR Group | Description |
|---|---|---|
| Authentication and Session Management | FR-AUTH | Web login, JWT API login, token refresh, logout, MFA, session management |
| Tenant Management | FR-TNT | Facility provisioning, configuration, suspension, tenant-scoped data access |
| Patient Registration and Identity | FR-REG | Registration, EMPI matching, duplicate detection, patient merge, multi-identifier lookup |
| Outpatient Department | FR-OPD | Triage, consultation, SOAP notes, diagnosis (ICD-10), prescribing, CDS, referral |
| Laboratory Information System | FR-LAB | Lab requests, sample collection, specimen tracking, result entry, critical value alerts, QC |
| Pharmacy and Dispensary | FR-PHR | Prescription queue, dispensing, stock deduction, substitution, partial dispensing, stock management, expiry tracking, controlled substances |
| Billing and Revenue | FR-BIL | Patient accounts, auto-billing, receipt generation, payment processing, deposit management, cashier reconciliation |
| Appointments and Scheduling | FR-APT | Booking, reminders (SMS/WhatsApp), doctor availability, queue management, walk-in integration |
| Access Control | FR-RBAC | Role management, permission assignment, ABAC for sensitive records, prescribing authority enforcement |

### 1.2 Requirements Coverage

| Category | Count | ID range |
|---|---|---|
| Functional requirements (Phase 1) | 83 | FR-AUTH-001 through FR-RBAC-007 |
| Non-functional requirements | 24 | NFR-HC-001 through NFR-HC-024 |
| Business rules | 67 | BR-CLIN-001 through BR-RX-003 |
| **Total requirements** | **174** | |

### 1.3 Out of Scope

- Phase 2 modules: IPD, Maternity, Emergency, Immunisation, Insurance, HR, Radiology, HMIS Reporting, Mortuary, Dental, Eye Care
- Phase 3 modules: HIV/AIDS Programme, TB Programme, Patient Portal, Nutrition, Community Health
- Phase 4 modules: Theatre, Blood Bank, Physiotherapy, Ambulance

---

## 2 Test Case Summary

### 2.1 Test Case Distribution by FR Group

| FR Group | FR count | Test cases | Priority | Rationale |
|---|---|---|---|---|
| FR-AUTH | 6 | 15 | High | Authentication is a security gateway; failures expose all patient data |
| FR-TNT | 4 | 12 | Critical | Tenant isolation failures cause cross-facility data leakage |
| FR-REG | 11 | 30 | Critical | Patient identity errors propagate to every downstream module |
| FR-OPD | 15 | 45 | Critical | Contains CDS engine (drug interactions, Five Rights, paediatric dosing) with direct patient safety impact |
| FR-LAB | 10 | 25 | Critical | Critical value escalation failure can delay life-saving intervention |
| FR-PHR | 15 | 40 | Critical | Dispensing errors, controlled substance tracking, stock integrity |
| FR-BIL | 10 | 25 | High | Financial accuracy; auto-billing, reconciliation, co-pay splits |
| FR-APT | 5 | 12 | Medium | Scheduling errors do not cause patient harm but affect service delivery |
| FR-RBAC | 7 | 20 | Critical | Access control failures expose sensitive records (HIV, mental health) |
| NFR (all) | 24 | 48 | High-Critical | Performance, security, offline resilience, regulatory compliance |
| **Total** | **107** | **272** | | |

### 2.2 Test Case Distribution by Test Level

| Test level | Test case count | Percentage |
|---|---|---|
| Unit tests | 190 | 70% |
| Integration tests | 54 | 20% |
| End-to-end tests | 28 | 10% |
| **Total** | **272** | **100%** |

### 2.3 Test Case Distribution by Priority

| Priority | Test case count | Pass threshold for release |
|---|---|---|
| Critical | 142 | 100% must pass |
| High | 86 | 95% must pass |
| Medium | 44 | 90% must pass |
| **Total** | **272** | |

---

## 3 Entry and Exit Criteria

### 3.1 Entry Criteria

Testing shall not commence until all of the following conditions are satisfied:

1. Code freeze declared for the Phase 1 release candidate
2. All unit tests passing in the CI pipeline (zero failures)
3. Static analysis (PHPStan level 8) reports zero errors
4. Tenant isolation CI audit rule passing (no raw SQL without `facility_id` filter)
5. Staging environment deployed with production-mirror configuration
6. Test data seeded: 10 facilities, 100 patients per facility, sample encounters, prescriptions, lab results
7. CDS test dataset loaded: drug interaction pairs (all 4 tiers), paediatric dosing drugs, critical value thresholds
8. All test cases reviewed and approved

### 3.2 Exit Criteria

The Phase 1 release shall not proceed until all of the following conditions are satisfied:

| Criterion | Threshold |
|---|---|
| Critical test cases passed | 100% (142/142) |
| High test cases passed | 95% (82/86 minimum) |
| Medium test cases passed | 90% (40/44 minimum) |
| Open Critical (S1) defects | 0 |
| Open High (S2) defects | 0 |
| Open patient safety defects | 0 |
| CDS engine code coverage (line) | 100% |
| CDS engine code coverage (branch) | 100% |
| Authentication/RBAC code coverage (line) | 95% |
| Billing code coverage (line) | 95% |
| Performance: API P95 response time | < 500 ms at 50 concurrent users |
| Performance: page load time | < 2 seconds on 1 Mbps |
| Offline: full clinical workflow | 5/5 operations complete without error |
| Offline: sync after reconnection | All queued records synced within 5 minutes |
| UAT: clinical advisor sign-off | Received |
| UAT: pilot facility sign-off | Received from all 3 pilot facilities |

### 3.3 Suspension Criteria

Testing shall be suspended if any of the following occur:

- A Critical (S1) patient safety defect is discovered that invalidates other test results
- The staging environment becomes unavailable for more than 4 hours
- Test data integrity is compromised (e.g., tenant isolation breach in test environment)
- More than 5 Critical defects are open simultaneously

Testing resumes only after the suspension trigger is resolved and the entry criteria are re-verified.

---

## 4 Test Schedule

| Phase | Duration | Start condition | Focus |
|---|---|---|---|
| Unit testing | Continuous | From first line of code | All services, repositories, CDS rules, calculators; runs on every commit |
| Integration testing | 2 weeks | Code freeze declared | API endpoints, database operations, tenant isolation, event flows, FHIR serialisation |
| System testing | 2 weeks | Integration test exit criteria met | Full clinical workflows end-to-end, cross-module data flow, billing accuracy |
| UAT | 2 weeks | System test exit criteria met | 3 pilot facilities execute clinical workflows with real-world scenarios |
| Performance testing | 1 week | Staging deployed with load test configuration | API response times, page load, database queries, mobile cold start, offline queue stress |
| Security testing | 1 week | Parallel with performance testing | Penetration testing, OWASP Top 10, tenant isolation verification, encryption validation |

### 4.1 Total Estimated Test Duration

- Pre-release testing (integration through security): 8 weeks elapsed
- Unit testing is continuous and does not add elapsed time
- UAT, performance, and security testing may overlap where independent

### 4.2 Test Milestones

| Milestone | Definition of done |
|---|---|
| M1: Unit test baseline | All 190 unit tests passing; CDS engine at 100% coverage |
| M2: Integration test complete | All 54 integration tests passing; tenant isolation verified |
| M3: System test complete | All 28 E2E tests passing; full clinical workflow verified |
| M4: UAT sign-off | Clinical advisor and all 3 pilot facilities approve |
| M5: Performance verified | All 8 performance thresholds met |
| M6: Security verified | Zero Critical or High security findings; penetration test report clean |
| M7: Release decision | All exit criteria met; go/no-go recommendation issued |

---

## 5 Roles and Responsibilities

| Role | Person | Responsibilities |
|---|---|---|
| Developer and test author | Peter (sole developer) | Write unit tests, integration tests, E2E tests; fix all defects; maintain CI pipeline; execute performance tests |
| Clinical advisor | TBD (contracted) | Review CDS test cases for clinical accuracy; validate paediatric dosing thresholds; sign off on clinical safety test results; participate in root cause analysis for patient safety defects |
| Pilot facility staff (Tororo) | Facility clinical team | Execute UAT test scripts for OPD, Lab, Pharmacy workflows; report defects; provide sign-off |
| Pilot facility staff (Kasanje) | Facility clinical team | Execute UAT test scripts; validate multi-tenant isolation from user perspective; provide sign-off |
| Pilot facility staff (TBD) | Facility clinical team | Execute UAT test scripts; provide sign-off |

### 5.1 Solo Developer Risk Mitigation

Peter is the sole developer, test author, and test executor. The following mitigations address the single-point-of-failure risk:

1. **Automated testing covers 90% of test execution:** the CI pipeline runs all unit and integration tests on every push, eliminating manual regression testing
2. **CDS test suite is deterministic:** every clinical safety test has an explicit expected result derived from business rules, not from developer judgment
3. **Clinical advisor provides independent validation:** the clinical advisor reviews CDS test cases and UAT results, providing a second pair of eyes on patient safety
4. **UAT delegates execution to facility staff:** pilot facility staff execute real-world workflows, discovering usability and workflow defects that developer testing misses
5. **Code coverage enforcement:** CI blocks merges below coverage thresholds, preventing untested code from reaching production

---

## 6 Risk Mitigation

### 6.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Solo tester: defects missed due to author bias | High | High | Automated CI (90% coverage), clinical advisor review, UAT with facility staff |
| Clinical safety defect reaches production | Low | Critical | 100% CDS test coverage, mandatory clinical advisor sign-off, zero-tolerance exit criterion |
| Regulatory non-compliance (HMIS inaccuracy) | Medium | High | HMIS accuracy tests cross-validated against manually tallied facility data from pilot sites |
| Offline sync data loss | Medium | Critical | 72-hour offline queue stress test, conflict resolution verification, field-level merge tests |
| Tenant data leakage | Low | Critical | CI audit rule (raw SQL scan), Eloquent global scope, cross-facility API access tests, penetration testing |
| Performance degradation under load | Medium | High | k6 load tests at 50 concurrent users, database query profiling, Celeron-class hardware test for encryption |
| Test data contamination with real PHI | Low | High | Synthetic data generation via Faker; de-identification procedure for any imported facility data; no PHI in git repository |
| Pilot facility unavailability during UAT | Medium | Medium | Schedule UAT across 3 facilities; 2 of 3 sign-offs sufficient for release with documented risk acceptance |

### 6.2 Contingency Plans

- **If clinical advisor is unavailable:** defer UAT sign-off; do not release without clinical safety validation
- **If fewer than 3 pilot facilities available:** proceed with minimum 2 facilities; document reduced UAT coverage as a known risk
- **If performance thresholds not met:** profile and optimise; re-test; extend performance testing by 1 week before escalating to architecture review

---

## 7 Test Deliverables

| Deliverable | Format | Produced by | Timing |
|---|---|---|---|
| Test strategy | Markdown (this repository) | Peter | Before development |
| Test plan | Markdown (this repository) | Peter | Before development |
| Test cases (unit) | PHPUnit / Jest / JUnit test classes | Peter | During development |
| Test cases (integration) | PHPUnit test classes | Peter | During development |
| Test cases (E2E) | Playwright / Espresso / XCUITest scripts | Peter | Post code freeze |
| Test report | Markdown (this repository) | Peter | After each test cycle |
| UAT scripts | Step-by-step procedures (printed) | Peter | Before UAT |
| UAT sign-off forms | Signed PDF | Pilot facility leads | After UAT |
| Clinical safety sign-off | Signed PDF | Clinical advisor | After UAT |
| Performance test report | k6 / Lighthouse output + summary | Peter | After performance testing |
| Security test report | Penetration test output + summary | Peter / external assessor | After security testing |
| Release decision report | Markdown | Peter | Before release |

---

## 8 AI Intelligence Test Cases

### Group: AI Clinical Documentation (TC-AI-001 through TC-AI-004)

| Test Case | Input | Expected Result | Pass Criterion |
|---|---|---|---|
| **TC-AI-001**: Draft note generated | Structured encounter with ICD code J22, vitals, medications | HTTP 200; `draft_id` and `content` returned; no write to patient record | Draft content non-empty; `patient_clinical_notes` count unchanged |
| **TC-AI-002**: Draft approved and saved | Same encounter; request includes `approved = true` | HTTP 200; draft written to `patient_clinical_notes` | Row count in `patient_clinical_notes` increases by 1 |
| **TC-AI-003**: Draft discarded | Draft generated; no approve action | No write to patient record after session expires | `patient_clinical_notes` count unchanged |
| **TC-AI-004**: Provider unavailable | Primary and failover adapters both timeout | HTTP 503; body contains `"error": "ai_unavailable"` | Clinical workflow (encounter save) remains unaffected |

### Group: AI ICD Coding Assist (TC-AI-005 through TC-AI-007)

| Test Case | Input | Expected Result | Pass Criterion |
|---|---|---|---|
| **TC-AI-005**: Fever and cough | Free text: "patient presented with fever and cough for 3 days" | ICD-10 J22 or J06 in top 3 suggestions | At least one of J22, J06 appears in `suggestions` array |
| **TC-AI-006**: Confidence scores returned | Any clinical text | Each suggestion includes a `confidence` float 0.0–1.0 | All `confidence` values are in range [0.0, 1.0] |
| **TC-AI-007**: Credit exhausted | Credit balance = 0 | HTTP 402; no API call made to AI provider | `ai_usage_log` count unchanged after request |

### Group: AI Differential Diagnosis (TC-AI-008 through TC-AI-010)

| Test Case | Input | Expected Result | Pass Criterion |
|---|---|---|---|
| **TC-AI-008**: Ranked list returned | Encounter with symptoms: headache, fever, neck stiffness | Ranked differential list with at least 3 entries; Meningitis appears in top 3 | `differentials` array length ≥ 3; rank 1, 2, or 3 entry contains "Meningitis" |
| **TC-AI-009**: Differential not written to record | Differential list returned | No diagnosis written to patient record unless clinician selects it | `patient_diagnoses` count unchanged |
| **TC-AI-010**: AI disclosure label | Differential list shown in UI | Label "AI Differential — for clinician review only. Not a diagnosis." visible on the same screen | Label text present in rendered HTML/view |

### Group: AI Patient Plain-Language Summary (TC-AI-011 through TC-AI-013)

| Test Case | Input | Expected Result | Pass Criterion |
|---|---|---|---|
| **TC-AI-011**: Kiswahili summary | Patient locale = `sw`; discharge note approved | Summary returned in Kiswahili | Response `locale` field = `sw`; summary text passes language detection as Kiswahili |
| **TC-AI-012**: French summary | Patient locale = `fr` | Summary returned in French | Response `locale` field = `fr` |
| **TC-AI-013**: English fallback | Patient locale = `sw`; Kiswahili generation fails | Summary returned in English; patient portal shows "Summary available in English only" | Response `locale` field = `en`; portal note displayed |

### Group: AI Claim Scrubbing (TC-AI-014 through TC-AI-016)

| Test Case | Input | Expected Result | Pass Criterion |
|---|---|---|---|
| **TC-AI-014**: Red flag detected | Claim with known rejection-trigger field (procedure code + insurer combination with > 30% historical rejection) | Line item flagged `red`; top 2 rejection reasons returned | `risk_level` = `red`; `top_reasons` array length = 2 |
| **TC-AI-015**: Green flag | Claim with no known rejection history | All line items flagged `green` | All `risk_level` values = `green` |
| **TC-AI-016**: Submit with red flag override | Claim with red flag; clerk enters override reason and submits | Claim submitted; override reason logged | Claim status = `submitted`; override reason recorded in `claim_audit_log` |

### Group: AI Outbreak Early Warning (TC-AI-017 through TC-AI-019)

| Test Case | Input | Expected Result | Pass Criterion |
|---|---|---|---|
| **TC-AI-017**: Anomaly detected | 15 malaria (ICD A09) diagnoses recorded within 24 hours (threshold: 7-day count > 2 SD above 90-day baseline) | Alert generated for Facility Admin and Medical Officer on duty | Alert record created in `ai_outbreak_alerts`; notification sent to both roles |
| **TC-AI-018**: No anomaly below threshold | 3 malaria diagnoses in 7 days (within normal range) | No alert generated | `ai_outbreak_alerts` count unchanged |
| **TC-AI-019**: Alert content accuracy | Alert generated | Alert contains: disease code, 7-day count, 90-day baseline average, % deviation, link to patient list | All 5 fields present in alert record |

### Group: i18n (TC-I18N-001 through TC-I18N-003)

| Test Case | Input | Expected Result | Pass Criterion |
|---|---|---|---|
| **TC-I18N-001**: Locale switch to Kiswahili | User switches locale to `sw` in profile | All visible UI strings on OPD triage screen render in Kiswahili | No English string visible in non-alert UI elements on that screen |
| **TC-I18N-002**: Locale fallback | String `opd.triage.blood_pressure_label` missing in `lang/sw/` | English string rendered; `[I18N-GAP]` logged | English "Blood Pressure" visible; build log contains `[I18N-GAP: opd.triage.blood_pressure_label]` |
| **TC-I18N-003**: Provider failover latency | Primary provider timeout injected | Failover adapter called; total response time ≤ 12 s from first request | Response received within 12 s; `was_failover = true` in log |
