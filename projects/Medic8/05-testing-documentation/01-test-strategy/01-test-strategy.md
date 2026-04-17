# Test Strategy for Medic8 Healthcare Management System

**Project:** Medic8 Multi-Tenant SaaS Healthcare Management System
**Document standard:** IEEE 829-2008, IEEE 29119-1:2013
**Version:** 1.0
**Status:** Draft
**Phase coverage:** Phase 1 (Foundation), with framework applicable to Phases 2-4

---

## 1 Test Strategy Overview

### 1.1 Purpose

This test strategy defines the testing approach, levels, types, and infrastructure required to verify that the Medic8 system meets all 83 functional requirements (FR-AUTH through FR-RBAC), 24 non-functional requirements (NFR-HC-001 through NFR-HC-024), and 67 business rules (BR-CLIN through BR-RX) documented in the Software Requirements Specification. The strategy prioritises clinical safety, patient data integrity, and Uganda regulatory compliance, in that order.

Healthcare software testing is life-critical. A defect in drug interaction checking, paediatric dosing calculation, or critical value escalation can cause patient harm. This strategy treats clinical safety tests as the highest-priority test category, with zero tolerance for undetected failures.

### 1.2 Scope

**In scope for this document:**

- All Phase 1 modules: Authentication, Tenant Management, Patient Registration, OPD, Laboratory, Pharmacy, Billing, Appointments, RBAC
- Clinical Decision Support (CDS) engine: drug interactions, paediatric dosing, NEWS2, Five Rights CPOE, critical value escalation
- Offline clinical resilience and sync
- Multi-tenant data isolation
- Uganda PDPA 2019 compliance
- Mobile app (Android 7.0+, iOS 15.0+) performance and offline capability
- FHIR R4 API compliance

**Out of scope for this document (covered in Phase 2-4 test strategies):**

- IPD, Maternity, Emergency, Immunisation, Insurance, HR, HMIS reporting modules
- HIV/AIDS and TB programme modules
- Patient portal
- Theatre, Blood Bank, Physiotherapy, and other Phase 4 specialty modules

### 1.3 Risk-Based Testing Approach

Test effort allocation follows a risk-based model per ISO 14971 (medical device risk management, applied by analogy). Risk is calculated as:

$$Risk = Severity \times Probability \times Detectability$$

| Risk tier | Modules and features | Test intensity |
|---|---|---|
| Critical (patient safety) | CDS alerts, paediatric dosing, Five Rights, critical value escalation, NEWS2, medication reconciliation | 100% path coverage, boundary value analysis, equivalence partitioning, mutation testing |
| High (data integrity) | Tenant isolation, EMPI duplicate detection, patient merge, audit trail, offline sync, auto-save | 100% requirement coverage, negative testing, concurrency testing |
| High (financial) | Auto-billing, MoMo/Airtel reconciliation, cashier reconciliation, insurance co-pay, missing charge detection | 100% requirement coverage, calculation verification, boundary testing |
| High (regulatory) | HMIS 105/108 accuracy, DHIS2 export, PDPA consent, HIV record access control | 100% requirement coverage, cross-validation against manual counts |
| Medium (functional) | OPD workflow, lab workflow, pharmacy workflow, appointment scheduling | Requirement-based testing, happy path plus key error paths |
| Low (cosmetic) | UI layout, label text, icon consistency | Visual inspection, responsive testing |

---

## 2 Test Pyramid

The Medic8 test suite follows a layered test pyramid to maximise defect detection speed while minimising execution time and maintenance cost.

### 2.1 Distribution

| Layer | Target coverage | Execution time | Scope |
|---|---|---|---|
| Unit tests | 70% of total test cases | Milliseconds per test | Services, repositories, CDS rule engines, dosing calculators, NEWS2 scorer, billing calculators, EMPI matching algorithms, validation logic |
| Integration tests | 20% of total test cases | Seconds per test | API endpoints, database operations (tenant-scoped queries), event-driven flows (critical value escalation), offline queue sync, FHIR resource serialisation, HL7 message parsing |
| End-to-end tests | 10% of total test cases | Minutes per test | Critical clinical workflows (register-consult-prescribe-dispense-result), billing flows (charge-pay-receipt-reconcile), offline full-cycle, cross-facility patient lookup |

### 2.2 Unit Test Standards

- Framework: PHPUnit 11.x (backend), Jest (frontend), JUnit 5 + Kotest (Android KMP), XCTest + Swift Testing (iOS)
- Every CDS rule shall have a dedicated test class with minimum 10 test cases covering: normal values, boundary values, edge cases, and invalid inputs
- Every financial calculation shall verify precision to 2 decimal places using integer arithmetic (UGX has no subunits, but insurance co-pay splits require decimal precision)
- Test isolation: no database, no filesystem, no network; all dependencies mocked or stubbed
- Naming convention: `test_[method]_[scenario]_[expectedResult]`

### 2.3 Integration Test Standards

- Framework: PHPUnit with `RefreshDatabase` trait (backend), Espresso + Room (Android), XCTest (iOS)
- Database: MySQL 8.x in Docker container, seeded per test class
- Every API endpoint shall have at minimum: 1 success case, 1 authentication failure case, 1 authorisation failure case, 1 validation failure case, 1 tenant isolation case
- Tenant isolation tests: every tenant-scoped endpoint tested with cross-facility credentials to verify 403 Forbidden response

### 2.4 End-to-End Test Standards

- Framework: Playwright (web), Espresso (Android), XCUITest (iOS)
- Test against staging environment mirroring production configuration
- Clinical workflow tests execute the complete patient journey: registration through discharge
- Offline E2E tests require network simulation (disconnect/reconnect cycle)

---

## 3 Test Categories

### 3.1 Clinical Safety Tests (HIGHEST PRIORITY)

Clinical safety tests verify that the CDS engine, dosing safeguards, and escalation mechanisms function correctly under all conditions. A failure in any clinical safety test blocks the release unconditionally.

#### 3.1.1 Drug Interaction Alert Tests

**Requirement traceability:** FR-OPD-007, NFR-HC-012, BR-CLIN-004

| Test ID | Description | Expected result |
|---|---|---|
| TC-CDS-001 | Prescribe 2 drugs with a Tier 1 (Info) interaction | Info message displayed passively in the prescription sidebar; prescription accepted without clinician action |
| TC-CDS-002 | Prescribe 2 drugs with a Tier 2 (Warning) interaction | Amber banner displayed prominently; clinician may proceed without override; prescription accepted |
| TC-CDS-003 | Prescribe 2 drugs with a Tier 3 (Serious) interaction | Modal alert blocks workflow; prescription blocked until clinician enters documented override reason |
| TC-CDS-004 | Prescribe 2 drugs with a Tier 3 interaction, provide override reason | Prescription accepted; audit log records `clinician_id`, `patient_id`, `alert_id`, `drug_pair`, severity "Serious", `timestamp`, action "overridden", and override reason text |
| TC-CDS-005 | Prescribe 2 drugs with a Tier 4 (Fatal) interaction | Hard stop; no override option available to the prescriber; system prompts for pharmacist intervention |
| TC-CDS-006 | Prescribe 2 drugs with a Tier 4 interaction, pharmacist resolves | Pharmacist intervention logged; prescription accepted only after pharmacist resolution |
| TC-CDS-007 | Prescribe 3 drugs where Drug A + B = Tier 2 and Drug B + C = Tier 3 | Both alerts displayed; the highest-severity alert (Tier 3) governs the workflow blocking behaviour |
| TC-CDS-008 | Prescribe a drug with a known interaction, then cancel the interacting drug | Alert clears; remaining prescription proceeds without interaction warning |
| TC-CDS-009 | Verify override rate tracking per facility | Query the override analytics; verify facility-level override rate calculation is correct |
| TC-CDS-010 | Verify all 4 tiers logged with required audit fields | Query audit log after 1 test per tier; verify all 8 required fields populated for each entry |

#### 3.1.2 Paediatric Dosing Tests

**Requirement traceability:** NFR-HC-011, BR-CLIN-006

| Test ID | Description | Expected result |
|---|---|---|
| TC-PED-001 | Patient age 2, weight 5 kg, drug dose 10 mg/kg | System calculates dose as 50 mg |
| TC-PED-002 | Calculated dose exceeds adult ceiling (e.g., 600 mg vs 500 mg ceiling) | System rejects prescription with ceiling dose error |
| TC-PED-003 | Calculated dose is 10x expected (decimal error guard) | System flags potential decimal error; blocks submission until clinician provides explicit override with documented reason |
| TC-PED-004 | No weight recorded within 24 hours | System blocks prescription submission with message requiring weight measurement |
| TC-PED-005 | Patient age 11 (under 12 boundary) | Weight-based dosing enforced |
| TC-PED-006 | Patient age 12 (at boundary, adult) | Weight-based dosing NOT enforced; standard adult dosing applies |
| TC-PED-007 | Weight recorded exactly 24 hours ago (boundary) | System accepts weight as valid |
| TC-PED-008 | Weight recorded 24 hours and 1 minute ago (expired) | System blocks prescription; requires fresh weight |
| TC-PED-009 | Dose calculated as exactly the adult ceiling | System accepts (ceiling is inclusive) |
| TC-PED-010 | Dose calculated as 1 mg above adult ceiling | System rejects |

#### 3.1.3 Critical Value Escalation Tests

**Requirement traceability:** NFR-HC-022, BR-CLIN-003

| Test ID | Description | Expected result |
|---|---|---|
| TC-ESC-001 | Lab result exceeds panic threshold (e.g., potassium > 6.5 mmol/L) | Immediate notification sent to requesting doctor |
| TC-ESC-002 | Doctor does not acknowledge within 30 minutes | System escalates to ward sister |
| TC-ESC-003 | Ward sister does not acknowledge within 60 minutes | System escalates to Facility Admin |
| TC-ESC-004 | Doctor acknowledges within 30 minutes | No further escalation occurs |
| TC-ESC-005 | All escalation steps timestamped in audit trail | Query audit log; verify `notification_sent`, `escalation_1`, `escalation_2` timestamps recorded |
| TC-ESC-006 | Multiple critical values for same patient simultaneously | Each critical value triggers its own independent escalation cascade |
| TC-ESC-007 | Critical value for glucose < 2.5 mmol/L (lower bound panic) | Escalation cascade fires identically to upper bound panic values |

#### 3.1.4 Five Rights CPOE Tests

**Requirement traceability:** FR-OPD-007, BR-CLIN-008

| Test ID | Description | Expected result |
|---|---|---|
| TC-5R-001 | Correct patient, drug, dose, route, time | Prescription accepted |
| TC-5R-002 | Wrong patient (patient ID mismatch at order entry) | System blocks submission with "Right Patient" error |
| TC-5R-003 | Wrong drug (drug not on facility formulary) | System blocks submission with "Right Drug" error |
| TC-5R-004 | Wrong dose (outside therapeutic range for drug and patient weight) | System blocks submission with "Right Dose" error |
| TC-5R-005 | Wrong route (invalid administration route for selected drug) | System blocks submission with "Right Route" error |
| TC-5R-006 | Wrong time (clinically inappropriate frequency schedule) | System blocks submission with "Right Time" error |
| TC-5R-007 | Multiple rights violated simultaneously | System reports all failed checks, not just the first |

#### 3.1.5 Medication Reconciliation Tests

**Requirement traceability:** BR-CLIN-005

| Test ID | Description | Expected result |
|---|---|---|
| TC-MR-001 | OPD to IPD admission | System generates reconciliation form listing all active medications with dose, frequency, and route |
| TC-MR-002 | Ward-to-ward transfer | Reconciliation form generated; receiving clinician must confirm before transfer finalised |
| TC-MR-003 | IPD to discharge | Reconciliation form generated; discharge blocked until reconciliation confirmed |
| TC-MR-004 | Facility-to-facility referral | Reconciliation form generated and included in referral letter |
| TC-MR-005 | Attempt to finalise transition without completing reconciliation | System blocks transition with error message |

#### 3.1.6 NEWS2 Calculation Tests

**Requirement traceability:** BR-CLIN-007

| Test ID | Description | Expected result |
|---|---|---|
| TC-NEWS-001 | All vitals normal (score 0) | NEWS2 score = 0; routine monitoring |
| TC-NEWS-002 | Score 4 (upper boundary of low risk) | Routine monitoring at standard intervals |
| TC-NEWS-003 | Score 5 (lower boundary of medium risk) | System increases monitoring frequency; notifies responsible doctor |
| TC-NEWS-004 | Score 6 (upper boundary of medium risk) | Same as score 5 |
| TC-NEWS-005 | Score 7 (lower boundary of high risk) | System triggers immediate clinical review alert; flags ICU transfer consideration |
| TC-NEWS-006 | Score 12 (maximum) | Same as score 7 with maximum urgency |
| TC-NEWS-007 | Sub-Saharan Africa adjusted thresholds applied | Verify population-adjusted baselines produce correct scores where clinically validated |

#### 3.1.7 Tall Man Lettering Display Tests

**Requirement traceability:** BR-RX-003

| Test ID | Description | Expected result |
|---|---|---|
| TC-TML-001 | Display hydrOXYzine in drug selection | Differentiating letters "OXY" displayed in uppercase |
| TC-TML-002 | Display hydrALAZINE in drug selection | Differentiating letters "ALAZINE" displayed in uppercase |
| TC-TML-003 | Non-LASA drug displayed | Standard casing; no Tall Man formatting applied |
| TC-TML-004 | LASA drug list updated by pharmacy lead | New LASA pair immediately renders with Tall Man Lettering |

### 3.2 Data Integrity Tests

#### 3.2.1 Tenant Isolation Tests

**Requirement traceability:** NFR-HC-015, BR-DATA-004

| Test ID | Description | Expected result |
|---|---|---|
| TC-TI-001 | Facility A user queries patient list | Zero records from Facility B appear |
| TC-TI-002 | Facility B user attempts API access to Facility A patient clinical record | HTTP 403 Forbidden |
| TC-TI-003 | Raw SQL query without `facility_id` filter in CI pipeline | Build fails with tenant isolation violation error |
| TC-TI-004 | Global patient identity lookup from Facility B | Facility B sees patient exists (name, age, sex, identifiers) but cannot access clinical data |
| TC-TI-005 | Emergency cross-facility access with patient confirmation | Access granted for 24 hours; patient receives SMS notification; access logged |
| TC-TI-006 | Eloquent global scope enforces `facility_id` on all tenant-scoped models | Manually remove repository-level filter; verify Eloquent global scope still filters by `facility_id` |

#### 3.2.2 EMPI Duplicate Detection Tests

**Requirement traceability:** BR-PID-001, BR-PID-002

| Test ID | Description | Expected result |
|---|---|---|
| TC-EMPI-001 | Register patient with identical name and DOB as existing patient | Duplicate warning with confidence score exceeding 80%; mandatory action required |
| TC-EMPI-002 | Register patient with similar name (Soundex match) and same phone | Duplicate warning displayed |
| TC-EMPI-003 | Register patient with identical NIN | Duplicate warning with high confidence score |
| TC-EMPI-004 | Register patient with no matches | No duplicate warning; "New Patient" proceeds |
| TC-EMPI-005 | Fuzzy matching with African naming patterns (compound surnames, clan names) | Algorithm correctly identifies potential duplicates despite spelling variations |

#### 3.2.3 Patient Merge Tests

**Requirement traceability:** BR-PID-003

| Test ID | Description | Expected result |
|---|---|---|
| TC-MRG-001 | Merge 2 duplicate patient records | All clinical history, billing records, and encounters consolidated under surviving record |
| TC-MRG-002 | Verify merge audit trail | Audit log records merge action, performing user, source records, surviving record |
| TC-MRG-003 | Unmerge within 30 days | Records separated; original data restored |
| TC-MRG-004 | Attempt unmerge after 30 days | System rejects unmerge request |
| TC-MRG-005 | Merge attempted by non-authorised role (not Records Officer or Facility Admin) | System blocks merge; returns authorisation error |

#### 3.2.4 Audit Trail Immutability Tests

**Requirement traceability:** NFR-HC-001

| Test ID | Description | Expected result |
|---|---|---|
| TC-AUD-001 | Perform CRUD on patient record; verify audit entry | Audit log entry exists with all 8 required fields: `user_id`, `timestamp`, `action`, `resource_type`, `resource_id`, `facility_id`, `ip_address`, `outcome` |
| TC-AUD-002 | Attempt UPDATE on audit log table as Super Admin | System rejects operation; returns error |
| TC-AUD-003 | Attempt DELETE on audit log table as Super Admin | System rejects operation; returns error |
| TC-AUD-004 | Verify append-only constraint at database level | Database trigger or constraint prevents modification of existing audit rows |

#### 3.2.5 Auto-Save and Power Loss Recovery Tests

**Requirement traceability:** NFR-HC-016, BR-DATA-005

| Test ID | Description | Expected result |
|---|---|---|
| TC-AS-001 | Fill OPD form partially; kill browser via Task Manager | Reopen browser; recovery prompt appears with auto-save timestamp |
| TC-AS-002 | Accept recovery | All entered data (chief complaint, diagnoses, prescription) restored exactly |
| TC-AS-003 | Discard recovery | Form opens blank |
| TC-AS-004 | Auto-save on keystroke | IndexedDB updated after each keystroke event |
| TC-AS-005 | Auto-save on dropdown selection | IndexedDB updated after selection change |
| TC-AS-006 | Session timeout with auto-saved data | Data preserved across session timeout; restored after re-authentication |

### 3.3 Financial Tests

#### 3.3.1 Auto-Billing Accuracy Tests

**Requirement traceability:** FR-BIL-001 through FR-BIL-010, BR-FIN-001

| Test ID | Description | Expected result |
|---|---|---|
| TC-FIN-001 | Request lab test from OPD | Lab charge auto-posted to patient account matching price list entry |
| TC-FIN-002 | Dispense drug from pharmacy | Drug charge auto-posted matching price list quantity and unit price |
| TC-FIN-003 | Record OPD procedure | Procedure charge auto-posted |
| TC-FIN-004 | Record bed day (IPD) | Bed day charge auto-posted |
| TC-FIN-005 | Service not in price list | No charge posted; no error |
| TC-FIN-006 | Multiple clinical actions in single encounter | All corresponding charges posted; total equals sum of individual charges |

#### 3.3.2 Mobile Money Reconciliation Tests

**Requirement traceability:** BR-FIN-003

| Test ID | Description | Expected result |
|---|---|---|
| TC-MOMO-001 | MoMo payment received with valid transaction reference | Payment auto-matched to patient account |
| TC-MOMO-002 | Airtel Money payment received with valid reference | Payment auto-matched to patient account |
| TC-MOMO-003 | Payment with unrecognised reference | Posted to suspense account |
| TC-MOMO-004 | Unmatched payment not resolved within 48 hours | Flagged in daily unmatched payments report |
| TC-MOMO-005 | Manual matching by cashier | Payment moved from suspense to correct patient account |

#### 3.3.3 Cashier Reconciliation Tests

**Requirement traceability:** BR-FIN-004

| Test ID | Description | Expected result |
|---|---|---|
| TC-CASH-001 | End-of-session reconciliation with matching totals | Session closes; no discrepancy flagged |
| TC-CASH-002 | Discrepancy exceeding UGX 5,000 | Supervisor review flag triggered |
| TC-CASH-003 | Discrepancy under UGX 5,000 | Session closes normally |
| TC-CASH-004 | Collections by payment mode calculated correctly | Cash + MoMo + Airtel + card = total collections |
| TC-CASH-005 | Opening float + collections - banking = closing float | Calculation verified |

#### 3.3.4 Missing Charge Detection Tests

**Requirement traceability:** BR-FIN-008

| Test ID | Description | Expected result |
|---|---|---|
| TC-MC-001 | OPD visit with no corresponding billing record | Flagged in daily missing charge report |
| TC-MC-002 | Lab result received with no lab charge | Flagged |
| TC-MC-003 | Drug dispensed with no drug charge | Flagged |
| TC-MC-004 | All clinical actions have corresponding charges | Report shows zero missing charges |

#### 3.3.5 Insurance Co-Pay Split Tests

**Requirement traceability:** BR-FIN-002

| Test ID | Description | Expected result |
|---|---|---|
| TC-INS-001 | Patient with active insurance scheme; bill UGX 100,000; benefit covers 80% | Insurer portion = UGX 80,000 posted to receivables ledger; patient co-pay = UGX 20,000 |
| TC-INS-002 | Service exceeds benefit limit | Excess posted entirely to patient co-pay |
| TC-INS-003 | Patient with no active insurance | Entire bill assigned to patient |
| TC-INS-004 | Multiple services with different benefit rates | Each service split according to its benefit schedule entry |

### 3.4 Regulatory Compliance Tests

#### 3.4.1 HMIS Accuracy Tests

**Requirement traceability:** NFR-HC-009, BR-HMIS-001, BR-HMIS-002

| Test ID | Description | Expected result |
|---|---|---|
| TC-HMIS-001 | Record 10 OPD visits across 2 age groups and both sexes | HMIS 105 Section 1 tallies match recorded visits by age group and sex without manual entry |
| TC-HMIS-002 | Record 5 lab tests of different types | HMIS 105 Section 2 tallies match |
| TC-HMIS-003 | Cross-validate auto-tallied data against manual count | Zero discrepancies |
| TC-HMIS-004 | HMIS 108 inpatient data auto-population | Admissions, discharges, deaths match recorded data |

#### 3.4.2 DHIS2 Export Tests

**Requirement traceability:** BR-HMIS-004

| Test ID | Description | Expected result |
|---|---|---|
| TC-DHIS-001 | Export HMIS 105 to DHIS2 format | Output file validates against Uganda eHMIS data schema |
| TC-DHIS-002 | API push to DHIS2 test instance | Successful submission; reporting period marked as "submitted" |
| TC-DHIS-003 | Export with no internet | System queues export; submits when connectivity resumes |

#### 3.4.3 PDPA 2019 Compliance Tests

**Requirement traceability:** NFR-HC-008, NFR-HC-001

| Test ID | Description | Expected result |
|---|---|---|
| TC-PDPA-001 | Patient consent not given for data processing | System blocks data processing for that patient; displays consent requirement |
| TC-PDPA-002 | Data retention period (10 years) enforced | Attempt to delete record within retention period rejected |
| TC-PDPA-003 | Breach notification tooling | Breach impact report generated within 4 hours; lists affected patient count, data categories, timeline, facility identifiers |
| TC-PDPA-004 | SMS notification drafts for affected patients | System generates SMS drafts for all affected patients |

#### 3.4.4 HIV Record Access Control Tests

**Requirement traceability:** NFR-HC-010

| Test ID | Description | Expected result |
|---|---|---|
| TC-HIV-001 | Clinician without "sensitive record" permission views patient | HIV status displays "[Restricted]" |
| TC-HIV-002 | Clinician with permission and active treatment relationship | HIV status value visible |
| TC-HIV-003 | Denied and granted access logged | Audit log contains entries for both outcomes with user ID, timestamp, facility, access outcome |
| TC-HIV-004 | "Break the glass" emergency access | Access granted for 24 hours; patient receives SMS within 60 seconds; access expires after 24 hours |

### 3.5 Performance Tests

**Requirement traceability:** NFR-HC-006, NFR-HC-017, quality_standards.md Section 2

| Test ID | Description | Threshold | Tool |
|---|---|---|---|
| TC-PERF-001 | API response time under normal load | P95 < 500 ms at 50 concurrent users per facility | k6 / Locust |
| TC-PERF-002 | Web page load time | < 2 seconds on 1 Mbps connection | Lighthouse / WebPageTest |
| TC-PERF-003 | Database query execution time | P95 < 200 ms for single-record retrieval | MySQL slow query log analysis |
| TC-PERF-004 | Android cold start time | < 3 seconds on 1 GB RAM device (Android 7.0) | Android Studio profiler |
| TC-PERF-005 | iOS cold start time | < 3 seconds on minimum supported device (iOS 15.0) | Xcode Instruments |
| TC-PERF-006 | APK + initial data size | < 50 MB | Build output measurement |
| TC-PERF-007 | Data-lite mode on 64 Kbps | Patient list loads, record opens, form submits without timeout | Network throttling (Charles Proxy) |
| TC-PERF-008 | Encrypted column query performance on Celeron-class CPU | P95 < 200 ms for single-record retrieval | MySQL profiler on test hardware |

### 3.6 Offline and Sync Tests

**Requirement traceability:** NFR-HC-013, NFR-HC-006, BR-DATA-003, BR-DATA-005

| Test ID | Description | Expected result |
|---|---|---|
| TC-OFF-001 | Full clinical workflow offline: register patient | Operation completes without error |
| TC-OFF-002 | Full clinical workflow offline: create OPD visit | Operation completes without error |
| TC-OFF-003 | Full clinical workflow offline: write prescription | Operation completes without error |
| TC-OFF-004 | Full clinical workflow offline: dispense drug | Operation completes without error |
| TC-OFF-005 | Full clinical workflow offline: enter lab result | Operation completes without error |
| TC-OFF-006 | Sync after reconnection | All 5 queued records appear in server database within 5 minutes |
| TC-OFF-007 | Conflict resolution: clinical field edited on 2 offline workstations | Both versions preserved side by side; flagged for clinician review; no clinical data silently overwritten |
| TC-OFF-008 | Conflict resolution: non-clinical field edited on 2 offline workstations | Last-write-wins applied |
| TC-OFF-009 | 72-hour offline queue | Queue data for 72 hours of clinical operations without data loss; sync all records after reconnection |
| TC-OFF-010 | Generator-aware sync: power restoration detected | System immediately initiates sync of offline queue |

---

## 4 Test Environments

| Environment | Purpose | Database | Network | Access |
|---|---|---|---|---|
| Local development | Unit tests, rapid feedback | SQLite in-memory (unit tests) / MySQL 8.x Docker (integration) | Localhost | Developer workstation |
| CI (GitHub Actions) | Automated test suite on every push | MySQL 8.x in Docker container | Internal | Automated, triggered by git push/PR |
| Staging | E2E tests, performance tests, security tests | MySQL 8.x, production-mirror schema and sample data | Cloud-hosted, throttleable | Development team |
| UAT | Facility pilot testing, clinical workflow validation | MySQL 8.x, production-mirror with anonymised data | Production-equivalent | 3 pilot facilities (Tororo, Kasanje, 1 additional) |

### 4.1 Environment Configuration Requirements

- **Staging** shall mirror production in: MySQL version, PHP version, server OS, Nginx configuration, SSL/TLS settings, and encryption-at-rest configuration
- **UAT** shall run on hardware equivalent to the lowest-specification facility deployment target
- **CI** shall execute the full unit and integration test suite in under 10 minutes
- **Local** development environment shall support running all unit tests without Docker or network access

---

## 5 Test Data Management

### 5.1 Test Data Generation

- Laravel model factories shall exist for every Eloquent model in the system
- Factories shall produce valid, internally consistent data that passes all validation rules
- Seeder shall generate: 10 facilities (tenants), 100 patients per facility, 500 OPD encounters, 300 lab requests with results, 400 prescriptions with dispensing records, 200 billing transactions
- Every factory-generated patient shall have: name, sex, age/DOB, at least 1 contact method, and a facility assignment

### 5.2 PHI Masking

- Test data shall never contain real patient information
- Patient names shall be generated using Faker library with African naming locale
- NIN, phone numbers, and addresses shall be synthetically generated
- Any dataset imported from a real facility for UAT shall be anonymised using a documented de-identification procedure before import

### 5.3 Tenant-Aware Testing

- Every test shall execute within an explicit facility context
- Tests that verify tenant isolation shall operate across 2 or more facility contexts
- Test setup shall create a fresh facility tenant and tear it down after the test class completes
- No test shall depend on the state of another test's facility

### 5.4 CDS Test Data

- A dedicated drug interaction test dataset shall contain known drug pairs for all 4 severity tiers
- A paediatric dosing test dataset shall contain drugs with known mg/kg doses, adult ceiling doses, and expected calculated doses for test patient weights
- A critical value test dataset shall contain lab analytes with known panic thresholds (e.g., potassium > 6.5 mmol/L, glucose < 2.5 mmol/L)

---

## 6 Defect Management

### 6.1 Severity Classification

| Severity | Definition | Examples | Response |
|---|---|---|---|
| Critical (S1) | Patient safety risk or system-wide outage | CDS alert not firing, paediatric dosing miscalculation, tenant data leakage, audit trail modifiable | Immediate fix; blocks release; root cause analysis mandatory |
| High (S2) | Data loss, data corruption, or major functional failure | Offline sync data loss, billing miscalculation, EMPI false negative (missed duplicate), HMIS miscount | Fix within 24 hours; blocks release |
| Medium (S3) | Functional defect with workaround available | Appointment booking error with manual workaround, report formatting issue | Fix within current sprint |
| Low (S4) | Cosmetic or minor usability issue | Misaligned label, spelling error, icon inconsistency | Fix when capacity allows |

### 6.2 Clinical Safety Defect Protocol

All defects classified as Critical (S1) shall follow an enhanced resolution process:

1. Defect reported with full reproduction steps, affected module, and patient safety impact assessment
2. Development halted on non-critical work until fix is implemented
3. Root cause analysis (RCA) completed and documented before the fix is merged
4. Fix verified by a second reviewer (clinical advisor if available)
5. Regression test added to the CDS test suite to prevent recurrence
6. Post-incident report filed in the project safety register

### 6.3 Defect Tracking

- All defects tracked in GitHub Issues with severity label, module label, and phase label
- Critical and High defects assigned immediately upon creation
- Defect metrics reported weekly: open count by severity, mean time to resolution by severity, defect discovery rate by test phase

---

## 7 Test Automation and CI/CD Integration

### 7.1 Continuous Integration Pipeline

1. **Pre-commit:** Linting (PHP CS Fixer, ESLint), static analysis (PHPStan level 8), tenant isolation audit (raw SQL scan)
2. **On push:** Unit tests (all), integration tests (all), code coverage report
3. **On PR to main:** Full test suite including E2E smoke tests, security scanning (Snyk/Trivy), dependency vulnerability check
4. **Pre-release:** Performance test suite, FHIR validation suite, HMIS accuracy validation

### 7.2 Coverage Thresholds

| Module | Minimum line coverage | Minimum branch coverage |
|---|---|---|
| CDS engine (drug interactions, dosing, NEWS2) | 100% | 100% |
| Authentication and RBAC | 95% | 90% |
| Billing and financial calculations | 95% | 90% |
| Patient registration and EMPI | 90% | 85% |
| All other modules | 80% | 75% |

### 7.3 Test Reporting

- Test results published to GitHub Actions summary on every CI run
- Code coverage report generated via Xdebug/PCOV and published alongside test results
- Failing tests block PR merge
- Flaky test policy: a test that fails intermittently is treated as a defect and fixed within 48 hours; no test is permanently skipped
