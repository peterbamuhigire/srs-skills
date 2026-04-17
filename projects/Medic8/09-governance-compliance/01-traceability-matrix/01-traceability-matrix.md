# Requirements Traceability Matrix -- Medic8

**Document ID:** Medic8-RTM-001
**Version:** 1.0
**Date:** 2026-04-03
**Author:** Peter Bamuhigire
**Standards:** IEEE 1012-2016, IEEE 830-1998, IEEE 29148-2018

---

## 1. Purpose

This Requirements Traceability Matrix (RTM) maps the full traceability chain for the Medic8 healthcare management system:

**Business Goal** --> **PRD Feature** --> **SRS Functional Requirement** --> **Design (HLD/LLD/ERD)** --> **Test Case** --> **Implementation Status**

The RTM serves 3 functions:

1. **Forward traceability:** confirm every requirement has a design artifact, test case, and implementation target
2. **Backward traceability:** confirm every implemented feature traces back to a documented business goal
3. **Gap identification:** flag any requirement without a design, test, or implementation target as a traceability gap

---

## 2. Forward Traceability (Requirements --> Design --> Test)

### 2.1 FR-AUTH: Authentication and Session Management (6 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-AUTH-001 | Web Session Login | PRD-SEC-001: Secure authentication | HLD 2.2 API Layer | LLD 3.1 Tenant Middleware | `user`, `session`, `audit_log` | `POST /auth/login` | TC-AUTH-001a: Valid login redirect; TC-AUTH-001b: Account lockout after 5 failures; TC-AUTH-001c: CSRF mismatch rejection; TC-AUTH-001d: Suspended tenant rejection | Specified |
| FR-AUTH-002 | Mobile / API JWT Login | PRD-SEC-001: Secure authentication | HLD 2.2 API Layer | LLD 3.1 Tenant Middleware | `user`, `api_refresh_token`, `audit_log` | `POST /auth/mobile/login` | TC-AUTH-002a: Valid JWT issuance; TC-AUTH-002b: Token structure verification; TC-AUTH-002c: Missing device_id rejection | Specified |
| FR-AUTH-003 | JWT Token Refresh | PRD-SEC-002: Token lifecycle | HLD 2.2 API Layer | LLD 3.1 Tenant Middleware | `api_refresh_token` | `POST /auth/mobile/refresh` | TC-AUTH-003a: Token rotation; TC-AUTH-003b: Revoked token rejection; TC-AUTH-003c: Expired token rejection | Specified |
| FR-AUTH-004 | Session and Token Logout | PRD-SEC-003: Session termination | HLD 2.2 API Layer | LLD 3.1 Tenant Middleware | `session`, `api_refresh_token` | `POST /auth/logout` | TC-AUTH-004a: Web session destroyed; TC-AUTH-004b: API tokens revoked | Specified |
| FR-AUTH-005 | Idle Session Timeout | PRD-SEC-004: Inactivity protection | HLD 2.2 API Layer | LLD 3.1 Tenant Middleware; LLD 5.1 Auto-Save | `session` | N/A (server-side middleware) | TC-AUTH-005a: 15-minute timeout redirect; TC-AUTH-005b: Auto-save preservation | Specified |
| FR-AUTH-006 | Multi-Factor Authentication for Admin Roles | PRD-SEC-005: MFA for privileged roles | HLD 2.2 API Layer | LLD 3.1 Tenant Middleware | `user` | `POST /auth/mfa/verify` | TC-AUTH-006a: MFA prompt for admin; TC-AUTH-006b: Correct TOTP grants session; TC-AUTH-006c: Non-admin bypasses MFA | Specified |

### 2.2 FR-TNT: Tenant Management (4 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-TNT-001 | Facility Provisioning | PRD-PLT-001: Multi-tenant provisioning | HLD 3.1 Isolation Strategy | LLD 3.1 Tenant Middleware | `facility`, `user`, `audit_log` | `POST /adminpanel/api/v1/facilities` | TC-TNT-001a: Facility created with pending status; TC-TNT-001b: Admin user created; TC-TNT-001c: Welcome email sent | Specified |
| FR-TNT-002 | Facility Activation and Deactivation | PRD-PLT-002: Tenant lifecycle | HLD 3.1 Isolation Strategy | LLD 3.1 Tenant Middleware | `facility`, `session` | `PATCH /adminpanel/api/v1/facilities/{id}` | TC-TNT-002a: Suspension invalidates sessions; TC-TNT-002b: Suspended user login rejected; TC-TNT-002c: Reactivation restores access | Specified |
| FR-TNT-003 | Facility Configuration | PRD-PLT-003: Per-facility customisation | HLD 3.1 Isolation Strategy | LLD 3.1 Tenant Middleware | `facility` | `PATCH /api/v1/facility/config` | TC-TNT-003a: Module toggle hides menu; TC-TNT-003b: Currency change reflected; TC-TNT-003c: MRN format applied | Specified |
| FR-TNT-004 | Country Configuration | PRD-PLT-004: Multi-country regulatory profiles | HLD 4.4 Country Configuration Layer | LLD 3.1 Tenant Middleware | `country_configuration` | `POST /adminpanel/api/v1/countries` | TC-TNT-004a: Uganda HMIS forms loaded; TC-TNT-004b: Kenya forms differ from Uganda | Specified |

### 2.3 FR-REG: Patient Registration and Identity (11 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-REG-001 | New Patient Registration | PRD-REG-001: Patient intake | HLD 7.1 Data Model | LLD 4.1.1 PatientService | `global_patient`, `patient`, `patient_identifier` | `POST /api/v1/patients` | TC-REG-001a: Patient created with MRN; TC-REG-001b: Minimum fields enforced; TC-REG-001c: Duplicate warning triggered | Specified |
| FR-REG-002 | Unique Patient ID (MRN) Auto-Generation | PRD-REG-002: Unique identification | HLD 7.1 Data Model | LLD 4.1.1 PatientService | `patient`, `facility` | `POST /api/v1/patients` | TC-REG-002a: MRN follows configured format; TC-REG-002b: No MRN collision | Specified |
| FR-REG-003 | Returning Patient Lookup | PRD-REG-003: Quick retrieval | HLD 7.1 Data Model | LLD 4.1.1 PatientService | `patient`, `patient_identifier` | `GET /api/v1/patients` | TC-REG-003a: Search by name returns results; TC-REG-003b: Search by NIN; TC-REG-003c: Search by phone | Specified |
| FR-REG-004 | Patient Category Assignment | PRD-REG-004: Category-based pricing | HLD 7.1 Data Model | LLD 4.1.1 PatientService | `patient` | `PATCH /api/v1/patients/{patient_uid}/category` | TC-REG-004a: Category updated; TC-REG-004b: Billing uses new category pricing | Specified |
| FR-REG-005 | Multiple Identifier Support | PRD-REG-005: Multi-ID system | HLD 7.1 Data Model | LLD 4.1.1 PatientService | `patient_identifier` | `POST /api/v1/patients/{patient_uid}/identifiers` | TC-REG-005a: NIN stored; TC-REG-005b: NHIS stored; TC-REG-005c: Lookup by any ID type | Specified |
| FR-REG-006 | Guardian and Next-of-Kin Linking | PRD-REG-006: Paediatric safeguards | HLD 7.1 Data Model | LLD 4.1.1 PatientService | `patient` | `POST /api/v1/patients/{patient_uid}/guardians` | TC-REG-006a: Guardian linked; TC-REG-006b: Minor without guardian flagged | Specified |
| FR-REG-007 | Patient Profile | PRD-REG-007: Comprehensive patient view | HLD 7.1 Data Model | LLD 4.1.1 PatientService | `patient`, `patient_allergy`, `patient_chronic_condition` | `GET /api/v1/patients/{patient_uid}` | TC-REG-007a: Profile displays demographics, allergies, conditions | Specified |
| FR-REG-008 | Patient Record Merge with Audit Trail | PRD-REG-008: Duplicate resolution | HLD 7.4 Patient Merge | LLD 4.1.1 PatientService | `global_patient`, `patient`, `audit_log` | `POST /api/v1/patients/merge` | TC-REG-008a: Records merged; TC-REG-008b: Audit trail created; TC-REG-008c: Unmerge within 30 days | Specified |
| FR-REG-009 | EMPI Duplicate Detection | PRD-REG-009: Duplicate prevention | HLD 7.2 EMPI Matching | LLD 3.5 EMPI Service | `global_patient`, `patient_identifier` | `GET /api/v1/patients/duplicates` | TC-REG-009a: 80%+ match triggers warning; TC-REG-009b: New patient requires explicit confirmation | Specified |
| FR-REG-010 | Cross-Facility Patient Lookup | PRD-REG-010: Global identity | HLD 7.3 Cross-Facility Privacy | LLD 3.5 EMPI Service | `global_patient` | `GET /api/v1/global-patients` | TC-REG-010a: Identity visible; TC-REG-010b: Clinical data not visible without consent | Specified |
| FR-REG-011 | Triage Queue Management | PRD-REG-011: Priority-based queueing | HLD 2.3 Business Logic Layer | LLD 4.1.2 TriageService | `triage_record`, `encounter` | `POST /api/v1/patients/{patient_uid}/triage` | TC-REG-011a: Emergency jumps queue; TC-REG-011b: Priority ordering correct | Specified |

### 2.4 FR-OPD: Outpatient Department (15 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-OPD-001 | Triage Vital Signs Entry | PRD-OPD-001: Vitals capture | HLD 2.3 Business Logic Layer | LLD 4.1.2 TriageService | `triage_record` | `POST /api/v1/encounters/{id}/vitals` | TC-OPD-001a: Vitals saved; TC-OPD-001b: NEWS2 auto-calculated; TC-OPD-001c: Critical score triggers alert | Specified |
| FR-OPD-002 | Doctor's Queue | PRD-OPD-002: Queue management | HLD 2.3 Business Logic Layer | LLD 4.2.1 EncounterService | `encounter`, `triage_record` | `GET /api/v1/queue/opd` | TC-OPD-002a: Queue ordered by triage priority; TC-OPD-002b: Only assigned doctor's patients shown | Specified |
| FR-OPD-003 | SOAP Clinical Consultation | PRD-OPD-003: Structured consultation | HLD 2.3 Business Logic Layer | LLD 4.2.1 EncounterService | `encounter`, `clinical_note` | `POST /api/v1/encounters` | TC-OPD-003a: SOAP note created; TC-OPD-003b: Auto-save on each field | Specified |
| FR-OPD-004 | ICD-10/ICD-11 Diagnosis Entry | PRD-OPD-004: Coded diagnoses | HLD 2.3 Business Logic Layer | LLD 3.4 Terminology Service | `diagnosis` | `POST /api/v1/encounters/{id}/diagnoses` | TC-OPD-004a: ICD-10 code selected; TC-OPD-004b: Free-text blocked; TC-OPD-004c: HMIS tally incremented | Specified |
| FR-OPD-005 | Investigation Requests (Lab, Radiology) | PRD-OPD-005: Order entry | HLD 2.3 Business Logic Layer | LLD 4.2.4 InvestigationService | `lab_request`, `lab_request_item` | `POST /api/v1/encounters/{id}/investigations` | TC-OPD-005a: Lab request created; TC-OPD-005b: Auto-billing triggered; TC-OPD-005c: Appears in lab worklist | Specified |
| FR-OPD-006 | Prescription Writing | PRD-OPD-006: Prescribing | HLD 2.3 Business Logic Layer | LLD 4.2.2 PrescriptionService | `prescription`, `prescription_item` | `POST /api/v1/encounters/{id}/prescriptions` | TC-OPD-006a: Prescription created; TC-OPD-006b: Drug interaction check fired; TC-OPD-006c: Five Rights validated | Specified |
| FR-OPD-007 | Stock-Aware Prescribing | PRD-OPD-007: Stock visibility at prescribing | HLD 2.3 Business Logic Layer | LLD 4.2.2 PrescriptionService; LLD 4.4.2 StockService | `drug_stock`, `prescription_item` | `POST /api/v1/encounters/{id}/prescriptions` | TC-OPD-007a: Zero-stock warning displayed; TC-OPD-007b: Alternative suggested | Specified |
| FR-OPD-008 | Drug Interaction Checking | PRD-OPD-008: Clinical safety | HLD 2.3 Business Logic Layer | LLD 3.3 CDS Engine | `cds_alert`, `cds_override` | `GET /api/v1/encounters/{id}/prescriptions/{rx_id}/interactions` | TC-OPD-008a: Tier 3 modal blocks; TC-OPD-008b: Tier 4 hard stop; TC-OPD-008c: Override logged | Specified |
| FR-OPD-009 | Procedure Recording | PRD-OPD-009: Procedure documentation | HLD 2.3 Business Logic Layer | LLD 4.2.1 EncounterService | `procedure` | `POST /api/v1/encounters/{id}/procedures` | TC-OPD-009a: Procedure recorded; TC-OPD-009b: Auto-billing posted | Specified |
| FR-OPD-010 | Referral Generation | PRD-OPD-010: Referral workflow | HLD 2.3 Business Logic Layer | LLD 4.2.1 EncounterService | `referral` | `POST /api/v1/encounters/{id}/referrals` | TC-OPD-010a: Referral letter generated; TC-OPD-010b: CDA R2 document created | Specified |
| FR-OPD-011 | Follow-Up Appointment Booking | PRD-OPD-011: Continuity of care | HLD 2.3 Business Logic Layer | LLD 4.6.1 AppointmentService | `appointment` | `POST /api/v1/encounters/{id}/follow-up` | TC-OPD-011a: Appointment created from encounter; TC-OPD-011b: SMS reminder scheduled | Specified |
| FR-OPD-012 | Clinical Notes History | PRD-OPD-012: Longitudinal record | HLD 2.3 Business Logic Layer | LLD 4.2.1 EncounterService | `encounter`, `clinical_note`, `diagnosis` | `GET /api/v1/encounters/{id}/history` | TC-OPD-012a: History displayed chronologically; TC-OPD-012b: Cross-facility records excluded without consent | Specified |
| FR-OPD-013 | Discharge / End of Visit | PRD-OPD-013: Visit closure | HLD 2.3 Business Logic Layer | LLD 4.2.1 EncounterService | `encounter`, `diagnosis` | `POST /api/v1/encounters/{id}/discharge` | TC-OPD-013a: Discharge blocked without ICD-10 diagnosis; TC-OPD-013b: Billing finalised | Specified |
| FR-OPD-014 | Early Warning Score Calculation (NEWS2) | PRD-OPD-014: Early deterioration detection | HLD 2.3 Business Logic Layer | LLD 4.2.1 EncounterService | `triage_record` | `GET /api/v1/encounters/{id}/ews` | TC-OPD-014a: NEWS2 score calculated; TC-OPD-014b: Score 7+ triggers immediate review alert | Specified |
| FR-OPD-015 | Five Rights CPOE Enforcement | PRD-OPD-015: Prescribing safety | HLD 2.3 Business Logic Layer | LLD 4.2.2 PrescriptionService | `prescription`, `prescription_item`, `drug` | `POST /api/v1/encounters/{id}/prescriptions` | TC-OPD-015a: Wrong dose blocked; TC-OPD-015b: Wrong route blocked; TC-OPD-015c: All 5 rights validated | Specified |

### 2.5 FR-LAB: Laboratory Information System (10 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-LAB-001 | Lab Request from Clinical Screens | PRD-LAB-001: Order entry integration | HLD 2.3 Business Logic Layer | LLD 4.3.1 LabService | `lab_request`, `lab_request_item` | `POST /api/v1/lab/requests` | TC-LAB-001a: Request appears in lab worklist; TC-LAB-001b: Auto-billing triggered | Specified |
| FR-LAB-002 | Sample Collection with Barcode/QR | PRD-LAB-002: Specimen identification | HLD 2.3 Business Logic Layer | LLD 4.3.1 LabService | `lab_sample` | `POST /api/v1/lab/samples/{id}/collect` | TC-LAB-002a: Barcode generated; TC-LAB-002b: Sample linked to request | Specified |
| FR-LAB-003 | Specimen Tracking | PRD-LAB-003: Chain of custody | HLD 2.3 Business Logic Layer | LLD 4.3.1 LabService | `lab_sample` | `PATCH /api/v1/lab/samples/{id}/status` | TC-LAB-003a: Status transitions logged; TC-LAB-003b: Reject triggers notification | Specified |
| FR-LAB-004 | Result Entry with Reference Ranges | PRD-LAB-004: Result management | HLD 2.3 Business Logic Layer | LLD 4.3.1 LabService | `lab_result`, `lab_test` | `POST /api/v1/lab/results` | TC-LAB-004a: Result saved with ranges; TC-LAB-004b: Abnormal flagged automatically | Specified |
| FR-LAB-005 | Critical Value Alerts with Escalation | PRD-LAB-005: Clinical safety alerts | HLD 5.1 Core Domain Events | LLD 4.3.1 LabService | `lab_result`, `audit_log` | `POST /api/v1/lab/results/{id}/escalate` | TC-LAB-005a: Panic value triggers notification within 60s; TC-LAB-005b: 30-minute escalation to ward sister; TC-LAB-005c: 60-minute escalation to admin | Specified |
| FR-LAB-006 | Result Validation by Lab Supervisor | PRD-LAB-006: Quality assurance | HLD 2.3 Business Logic Layer | LLD 4.3.1 LabService | `lab_result` | `POST /api/v1/lab/results/{id}/validate` | TC-LAB-006a: Validated result visible to clinician; TC-LAB-006b: Unvalidated result hidden from clinician | Specified |
| FR-LAB-007 | Quality Control Records and Levey-Jennings | PRD-LAB-007: QC compliance | HLD 2.3 Business Logic Layer | LLD 4.3.2 QualityControlService | `lab_qc_record` | `POST /api/v1/lab/qc` | TC-LAB-007a: QC record saved; TC-LAB-007b: Levey-Jennings chart renders | Specified |
| FR-LAB-008 | HL7 v2 Analyser Interface | PRD-LAB-008: Analyser integration | HLD 8.2 HL7 v2 Gateway | LLD 3.6 HL7 Gateway Service | `lab_result`, `lab_sample` | N/A (HL7 v2 TCP/IP) | TC-LAB-008a: HL7 OUL message received; TC-LAB-008b: Result auto-populated; TC-LAB-008c: Unknown sample ID rejected | Specified |
| FR-LAB-009 | External Lab Referral | PRD-LAB-009: Referral lab workflow | HLD 2.3 Business Logic Layer | LLD 4.3.1 LabService | `lab_request` | `POST /api/v1/lab/requests/{id}/refer-external` | TC-LAB-009a: Referral form generated; TC-LAB-009b: Result manually entered on return | Specified |
| FR-LAB-010 | LOINC-Coded Test Definitions | PRD-LAB-010: Standardised test catalogue | HLD 2.3 Business Logic Layer | LLD 3.4 Terminology Service | `lab_test` | `POST /api/v1/lab/tests` | TC-LAB-010a: Test created with LOINC code; TC-LAB-010b: LOINC search returns results | Specified |

### 2.6 FR-PHR: Pharmacy and Dispensing (15 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-PHR-001 | Prescription Queue | PRD-PHR-001: Dispensing workflow | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService | `prescription` | `GET /api/v1/pharmacy/queue` | TC-PHR-001a: Pending prescriptions listed; TC-PHR-001b: Emergency prescriptions prioritised | Specified |
| FR-PHR-002 | Dispensing with Automatic Stock Deduction | PRD-PHR-002: Stock-integrated dispensing | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService; LLD 4.4.2 StockService | `dispensing_record`, `drug_stock` | `POST /api/v1/pharmacy/dispense` | TC-PHR-002a: Stock decremented; TC-PHR-002b: Dispensing label generated; TC-PHR-002c: Below-minimum alert | Specified |
| FR-PHR-003 | Generic/Brand Substitution | PRD-PHR-003: Cost-effective dispensing | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService | `dispensing_record`, `prescription_item` | `POST /api/v1/pharmacy/substitute` | TC-PHR-003a: Substitution logged; TC-PHR-003b: Doctor notified | Specified |
| FR-PHR-004 | Dispensing Label Generation | PRD-PHR-004: Patient safety labelling | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService | `dispensing_record` | `POST /api/v1/pharmacy/dispense` | TC-PHR-004a: Label contains patient name, drug, dose, frequency, route | Specified |
| FR-PHR-005 | Partial Dispensing with Pending Balance | PRD-PHR-005: Stock shortage handling | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService | `dispensing_record`, `prescription_item` | `POST /api/v1/pharmacy/dispense` | TC-PHR-005a: Partial qty recorded; TC-PHR-005b: Pending balance visible | Specified |
| FR-PHR-006 | Inpatient Drug Round Tracking | PRD-PHR-006: MAR integration | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService | `dispensing_record` | `POST /api/v1/pharmacy/drug-round` | TC-PHR-006a: Drug round timestamp recorded; TC-PHR-006b: Missed dose flagged | Specified |
| FR-PHR-007 | Stock Management (GRN, Transfer, Adjust, Return) | PRD-PHR-007: Inventory control | HLD 2.3 Business Logic Layer | LLD 4.4.2 StockService | `goods_received_note`, `drug_stock`, `store` | `POST /api/v1/pharmacy/stock/grn`; `POST /api/v1/pharmacy/stock/transfer`; `POST /api/v1/pharmacy/stock/adjust` | TC-PHR-007a: GRN increases stock; TC-PHR-007b: Transfer between stores; TC-PHR-007c: Adjustment logged | Specified |
| FR-PHR-008 | Expiry Tracking with 90-Day Alert | PRD-PHR-008: Expiry management | HLD 2.3 Business Logic Layer | LLD 4.4.2 StockService | `drug_stock` | `GET /api/v1/pharmacy/expiring` | TC-PHR-008a: 90-day alert generated; TC-PHR-008b: Expired stock blocked from dispensing | Specified |
| FR-PHR-009 | Minimum Stock Level Alerts | PRD-PHR-009: Reorder point | HLD 2.3 Business Logic Layer | LLD 4.4.2 StockService | `drug_stock`, `drug` | `GET /api/v1/pharmacy/stock` | TC-PHR-009a: Below-minimum notification sent; TC-PHR-009b: Critical stock highlighted | Specified |
| FR-PHR-010 | Drug Formulary Management | PRD-PHR-010: Formulary governance | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService | `drug` | `POST /api/v1/pharmacy/formulary` | TC-PHR-010a: Drug added to formulary; TC-PHR-010b: Non-formulary prescribing blocked | Specified |
| FR-PHR-011 | Narcotic/Controlled Drug Register | PRD-PHR-011: Controlled substance compliance | HLD 2.3 Business Logic Layer | LLD 4.4.3 NarcoticService | `narcotic_register` | `POST /api/v1/pharmacy/narcotic` | TC-PHR-011a: Register entry created; TC-PHR-011b: Running balance maintained; TC-PHR-011c: Discrepancy alert | Specified |
| FR-PHR-012 | Pharmacy Revenue Auto-Billing | PRD-PHR-012: Revenue capture | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService; LLD 4.5.1 BillingService | `charge`, `dispensing_record` | `POST /api/v1/pharmacy/dispense` | TC-PHR-012a: Charge posted on dispense; TC-PHR-012b: Charge amount matches price list | Specified |
| FR-PHR-013 | Tall Man Lettering Display | PRD-PHR-013: LASA drug safety | HLD 2.3 Business Logic Layer | LLD 4.4.4 TallManService | `drug` | `GET /api/v1/pharmacy/formulary` | TC-PHR-013a: LASA drugs display Tall Man Lettering; TC-PHR-013b: List maintainable by pharmacy lead | Specified |
| FR-PHR-014 | Weight-Based Paediatric Dosing | PRD-PHR-014: Paediatric safety | HLD 2.3 Business Logic Layer | LLD 4.2.3 PaediatricDosingService | `prescription_item`, `patient` | `POST /api/v1/encounters/{id}/prescriptions` | TC-PHR-014a: Dose calculated from weight; TC-PHR-014b: Adult ceiling enforced; TC-PHR-014c: 10x deviation flagged; TC-PHR-014d: No weight blocks prescription | Specified |
| FR-PHR-015 | Medication Reconciliation at Transitions | PRD-PHR-015: Transition safety | HLD 2.3 Business Logic Layer | LLD 4.4.1 PharmacyService | `prescription`, `prescription_item` | `POST /api/v1/pharmacy/medication-reconciliation` | TC-PHR-015a: Reconciliation form generated; TC-PHR-015b: Transition blocked without reconciliation | Specified |

### 2.7 FR-BIL: Billing and Revenue Management (10 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-BIL-001 | Patient Account with Real-Time Charge Accumulation | PRD-BIL-001: Patient billing | HLD 2.3 Business Logic Layer | LLD 4.5.1 BillingService | `patient_account`, `charge` | `GET /api/v1/billing/accounts/{patient_uid}` | TC-BIL-001a: Charges accumulate in real time; TC-BIL-001b: Balance reflects all posted charges | Specified |
| FR-BIL-002 | Configurable Price List per Service Category | PRD-BIL-002: Price management | HLD 2.3 Business Logic Layer | LLD 4.5.1 BillingService | `price_list` | `POST /api/v1/billing/pricelist` | TC-BIL-002a: Price list entry created; TC-BIL-002b: Charges use correct price | Specified |
| FR-BIL-003 | Patient Category Pricing | PRD-BIL-003: Differential pricing | HLD 2.3 Business Logic Layer | LLD 4.5.1 BillingService | `price_list`, `patient` | `GET /api/v1/billing/pricelist` | TC-BIL-003a: Category price applied; TC-BIL-003b: Staff discount reflected | Specified |
| FR-BIL-004 | Auto-Billing from Clinical Screens | PRD-BIL-004: Revenue capture | HLD 5.2 Event Listener Mappings | LLD 4.5.1 BillingService | `charge` | `POST /api/v1/billing/charges` | TC-BIL-004a: Lab request posts lab charge; TC-BIL-004b: Drug dispense posts drug charge; TC-BIL-004c: No manual entry needed | Specified |
| FR-BIL-005 | Receipt Generation | PRD-BIL-005: Payment documentation | HLD 2.3 Business Logic Layer | LLD 4.5.1 BillingService | `receipt`, `payment` | `GET /api/v1/billing/receipts/{id}` | TC-BIL-005a: Receipt generated with correct totals; TC-BIL-005b: Printable format | Specified |
| FR-BIL-006 | Cash Payment with Change Calculation | PRD-BIL-006: Cash handling | HLD 2.3 Business Logic Layer | LLD 4.5.1 BillingService | `payment`, `receipt`, `patient_account` | `POST /api/v1/billing/payments` | TC-BIL-006a: Payment recorded; TC-BIL-006b: Change calculated correctly; TC-BIL-006c: Balance updated | Specified |
| FR-BIL-007 | Mobile Money Payment with Auto-Reconciliation | PRD-BIL-007: Mobile money integration | HLD 2.3 Business Logic Layer | LLD 4.5.2 MobileMoneyService | `payment`, `patient_account` | `POST /api/v1/billing/payments/momo` | TC-BIL-007a: MoMo callback processed; TC-BIL-007b: Auto-matched to patient; TC-BIL-007c: Unmatched to suspense | Specified |
| FR-BIL-008 | Daily Cashier Reconciliation | PRD-BIL-008: Cash controls | HLD 2.3 Business Logic Layer | LLD 4.5.1 BillingService | `cashier_session` | `POST /api/v1/billing/reconciliation` | TC-BIL-008a: Session closed with totals; TC-BIL-008b: Discrepancy > UGX 5,000 flagged | Specified |
| FR-BIL-009 | Missing Charge Detection | PRD-BIL-009: Revenue assurance | HLD 2.3 Business Logic Layer | LLD 5.4 Missing Charge Detection | `charge`, `encounter`, `lab_result`, `dispensing_record` | `GET /api/v1/billing/missing-charges` | TC-BIL-009a: Encounter without charge flagged; TC-BIL-009b: Daily report generated | Specified |
| FR-BIL-010 | Credit Management | PRD-BIL-010: Credit facility | HLD 2.3 Business Logic Layer | LLD 4.5.1 BillingService | `patient_account` | `POST /api/v1/billing/credits` | TC-BIL-010a: Credit arrangement created; TC-BIL-010b: Ageing report generated; TC-BIL-010c: Write-off requires approval | Specified |

### 2.8 FR-APT: Appointment Management (5 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-APT-001 | Appointment Booking | PRD-APT-001: Scheduling | HLD 2.3 Business Logic Layer | LLD 4.6.1 AppointmentService | `appointment`, `doctor_availability` | `POST /api/v1/appointments` | TC-APT-001a: Appointment created; TC-APT-001b: Double-booking prevented; TC-APT-001c: Confirmation SMS sent | Specified |
| FR-APT-002 | SMS/WhatsApp Appointment Reminder | PRD-APT-002: Patient communication | HLD 5.2 Event Listener Mappings | LLD 4.6.2 ReminderService | `appointment` | N/A (scheduled job) | TC-APT-002a: Reminder sent 24h before; TC-APT-002b: WhatsApp fallback to SMS | Specified |
| FR-APT-003 | Doctor Availability Calendar | PRD-APT-003: Schedule management | HLD 2.3 Business Logic Layer | LLD 4.6.1 AppointmentService | `doctor_availability` | `GET /api/v1/appointments/calendar/{doctor_id}` | TC-APT-003a: Available slots displayed; TC-APT-003b: Blocked slots excluded | Specified |
| FR-APT-004 | Queue Management (Appointment to OPD Queue) | PRD-APT-004: Queue integration | HLD 2.3 Business Logic Layer | LLD 4.6.1 AppointmentService | `appointment`, `encounter` | `POST /api/v1/appointments/{id}/arrive` | TC-APT-004a: Arrived patient joins OPD queue; TC-APT-004b: Priority maintained | Specified |
| FR-APT-005 | Walk-In Integration | PRD-APT-005: Walk-in handling | HLD 2.3 Business Logic Layer | LLD 4.6.1 AppointmentService | `appointment`, `encounter` | `POST /api/v1/appointments` | TC-APT-005a: Walk-in appointment created; TC-APT-005b: Walk-in joins queue behind scheduled patients | Specified |

### 2.9 FR-RBAC: Access Control and Audit (7 Requirements)

| FR ID | Title | Source (PRD) | HLD Section | LLD Service | ERD Table(s) | API Endpoint | Test Case(s) | Status |
|---|---|---|---|---|---|---|---|---|
| FR-RBAC-001 | Role-Based Permission Resolution | PRD-RBAC-001: Access control | HLD 2.3 Business Logic Layer | LLD 4.7.1 PermissionService | `role`, `permission`, `role_permission`, `user_role` | `GET /api/v1/roles/{id}/permissions` | TC-RBAC-001a: Role permissions enforced; TC-RBAC-001b: Unauthorised action rejected | Specified |
| FR-RBAC-002 | Custom Role Creation per Facility | PRD-RBAC-002: Role flexibility | HLD 3.1 Isolation Strategy | LLD 4.7.1 PermissionService | `role`, `permission`, `role_permission` | `POST /api/v1/roles` | TC-RBAC-002a: Custom role created; TC-RBAC-002b: Permissions assigned; TC-RBAC-002c: Role scoped to facility | Specified |
| FR-RBAC-003 | Attribute-Based Access Control for Sensitive Records | PRD-RBAC-003: Sensitive data protection | HLD 3.1 Isolation Strategy | LLD 4.7.1 PermissionService | `user_role`, `patient`, `audit_log` | N/A (middleware enforcement) | TC-RBAC-003a: HIV status hidden without permission; TC-RBAC-003b: Access logged | Specified |
| FR-RBAC-004 | Session Management (Device-Level) | PRD-RBAC-004: Device control | HLD 2.2 API Layer | LLD 4.7.1 PermissionService | `session`, `api_refresh_token` | `GET /api/v1/users/{id}/sessions`; `DELETE /api/v1/users/{id}/sessions/{session_id}` | TC-RBAC-004a: Active sessions listed; TC-RBAC-004b: Remote session terminated | Specified |
| FR-RBAC-005 | Immutable Audit Trail | PRD-RBAC-005: Audit compliance | HLD 2.3 Business Logic Layer | LLD 4.7.2 AuditService | `audit_log` | `GET /api/v1/audit-trail` | TC-RBAC-005a: Audit entry created on every action; TC-RBAC-005b: UPDATE/DELETE on audit_log rejected | Specified |
| FR-RBAC-006 | Emergency Access to Cross-Facility Records | PRD-RBAC-006: Emergency access | HLD 7.3 Cross-Facility Privacy | LLD 4.7.3 EmergencyAccessService | `emergency_access_log`, `audit_log` | `POST /api/v1/emergency-access` | TC-RBAC-006a: Two-factor confirmation required; TC-RBAC-006b: Data revealed per specification; TC-RBAC-006c: 24-hour expiry; TC-RBAC-006d: Patient SMS sent | Specified |
| FR-RBAC-007 | Break-the-Glass Access with Mandatory Reason | PRD-RBAC-007: Break-glass protocol | HLD 7.3 Cross-Facility Privacy | LLD 4.7.3 EmergencyAccessService | `emergency_access_log`, `audit_log` | `POST /api/v1/break-the-glass` | TC-RBAC-007a: Reason required; TC-RBAC-007b: Full audit trail; TC-RBAC-007c: Post-access review triggered | Specified |

---

## 3. NFR Traceability

| NFR ID | Title | Source | Design Section | Test Strategy Section | Verification Method | Status |
|---|---|---|---|---|---|---|
| NFR-HC-001 | Patient Data Audit Trail | Uganda PDPA 2019 Section 24 | HLD 2.3 Business Logic Layer; LLD 4.7.2 AuditService; ERD 4.8 `audit_log` | Test Strategy 3.1: Security Testing | Inspection: query audit log after CRUD operation; confirm all 8 fields present. Penetration: attempt UPDATE/DELETE on audit_log; confirm rejection. | Specified |
| NFR-HC-002 | Data Encryption at Rest | Uganda PDPA 2019 Section 22; NIST SP 800-57 | HLD 2.5 Data Layer; ERD Section 1.2 Architectural Constraints | Test Strategy 3.2: Security Testing | Inspection: read raw MySQL data files; confirm ciphertext. Performance: measure P95 query time on Celeron-class hardware; confirm under 200 ms. | Specified |
| NFR-HC-003 | Data Encryption in Transit | Uganda PDPA 2019 Section 22 | HLD 2.2 API Layer | Test Strategy 3.2: Security Testing | Scan: `nmap --script ssl-enum-ciphers`; confirm TLS 1.0/1.1 disabled. Test: attempt TLS 1.1 connection; confirm refusal. Mobile: verify certificate pinning. | Specified |
| NFR-HC-004 | Session Timeout | Quality Standards Section 3 | HLD 2.2 API Layer; LLD 3.1 Tenant Middleware | Test Strategy 3.3: Functional Testing | Test: idle for 13 minutes; confirm warning prompt. Idle 2 more minutes; confirm logout. Re-authenticate; confirm auto-saved data restored. | Specified |
| NFR-HC-005 | Multi-Factor Authentication | Quality Standards Section 3 | HLD 2.2 API Layer; LLD 3.1 Tenant Middleware | Test Strategy 3.3: Functional Testing | Test: admin login without MFA denied. Valid TOTP grants access. Clinical staff bypasses MFA. SMS failure falls back to email within 30s. | Specified |
| NFR-HC-006 | Availability and Offline Resilience | Quality Standards Section 1, 2 | HLD 6.1 Scope; HLD 6.2 Offline Storage | Test Strategy 3.4: Reliability Testing | Monitor: external uptime check for 30 days; confirm >= 99.9%. Offline: disconnect internet; complete 5 clinical operations; reconnect; confirm sync within 5 minutes. | Specified |
| NFR-HC-007 | Data Retention | Uganda MoH Policy | ERD Section 1.2 Architectural Constraints | Test Strategy 3.5: Compliance Testing | Test: attempt deletion of record with last encounter < 10 years ago; confirm rejection. Attempt deletion > 10 years; confirm archive action. | Specified |
| NFR-HC-008 | Breach Notification | Uganda PDPA 2019 Section 31 | HLD 2.3 Business Logic Layer | Test Strategy 3.2: Security Testing | Simulate: flag user as compromised; execute breach report; confirm generation within 4 hours with all required fields. Verify SMS notification drafts. | Specified |
| NFR-HC-009 | HMIS Compliance | Uganda MoH HMIS Standards | HLD 8.3 DHIS2 Integration; ERD 11.6 HMIS Reporting | Test Strategy 3.5: Compliance Testing | Test: record 10 OPD visits; generate HMIS 105; verify tallies match without manual entry. Submit to DHIS2 test instance; confirm success. | Specified |
| NFR-HC-010 | Sensitive Record Access Control | HIV/AIDS Prevention and Control Act 2014 Section 18; Uganda PDPA 2019 | HLD 3.1 Isolation Strategy; LLD 4.7.1 PermissionService | Test Strategy 3.2: Security Testing | Test: doctor without permission sees "[Restricted]". Doctor with permission sees value. Both accesses logged. Break-the-glass triggers SMS within 60s. Expires after 24h. | Specified |
| NFR-HC-011 | Paediatric Safety -- Weight-Based Dosing | BR-CLIN-006; WHO Essential Medicines List | HLD 2.3 Business Logic Layer; LLD 4.2.3 PaediatricDosingService | Test Strategy 3.3: Functional Testing | Test: prescribe for 5 kg child at 10 mg/kg; confirm 50 mg calculated. Enter 5000 mg; confirm decimal error flag. Enter above adult ceiling; confirm rejection. Remove weight; confirm prescription blocked. | Specified |
| NFR-HC-012 | Clinical Decision Support Alert Response | BR-CLIN-004; Gap Analysis HIGH-004 | HLD 2.3 Business Logic Layer; LLD 3.3 CDS Engine | Test Strategy 3.3: Functional Testing | Test: prescribe Tier 3 interaction; confirm modal. Override with reason; confirm audit entry with all required fields. Prescribe Tier 4; confirm hard stop with no override. | Specified |
| NFR-HC-013 | Offline Clinical Resilience | Quality Standards Section 1 | HLD 6.1-6.6 Offline Architecture | Test Strategy 3.4: Reliability Testing | Test: disconnect; complete 5 operations; reconnect; confirm sync within 5 minutes. Concurrent offline edits; confirm conflict flagged, not silently overwritten. | Specified |
| NFR-HC-014 | FHIR R4 Compliance | HL7 FHIR R4 Standard | HLD 8.1 FHIR R4 API; API Spec 2.10 | Test Strategy 3.6: Interoperability Testing | Validate: all 14 resource types against FHIR Validator. Confirm HTML narrative in text.div. Verify SMART on FHIR OAuth flow. | Specified |
| NFR-HC-015 | Multi-Tenant Data Isolation | BR-DATA-004 | HLD 3.1-3.4 Multi-Tenancy Architecture; ERD Section 13.1 Tenant Indexes | Test Strategy 3.2: Security Testing | Test: Facility A user queries patients; confirm zero Facility B records. Raw SQL without facility_id fails CI build. API cross-tenant access returns 403. | Specified |
| NFR-HC-016 | Auto-Save and Power Loss Recovery | BR-DATA-005 | HLD 6.6 Auto-Save; LLD 5.1 Auto-Save | Test Strategy 3.3: Functional Testing | Test: enter data; kill browser process; reopen; confirm recovery prompt with timestamp. Accept recovery; confirm data restored. Discard; confirm blank form. | Specified |
| NFR-HC-017 | Mobile App Performance | Quality Standards Section 4 | HLD 2.1 Presentation Layer | Test Strategy 3.7: Performance Testing | Measure: cold start under 3s on minimum spec device. APK under 50 MB. 64 Kbps data-lite mode functional. Radiology images WiFi-only. | Specified |
| NFR-HC-018 | Nursing Sensitive Outcome Tracking | Clinical Quality Standards | HLD 2.3 Business Logic Layer | Test Strategy 3.5: Compliance Testing | Test: discharge patient with pressure ulcer ICD-10 L89.x; confirm NSO dashboard increments. Verify all 14 indicators tracked. Verify month-on-month trend lines. | Specified |
| NFR-HC-019 | Data Residency | Uganda PDPA 2019 Section 34; Domain Regulatory Superset | HLD 2.5 Data Layer | Test Strategy 3.2: Security Testing | Test: Uganda tenant exports to non-Uganda server without consent; confirm block and log. Australia tenant exports per APPs; confirm success. | Specified |
| NFR-HC-020 | Backup and Disaster Recovery | Quality Standards Section 1 | HLD 2.5 Data Layer | Test Strategy 3.4: Reliability Testing | Test: trigger backup; simulate failure; restore within 4 hours; confirm RPO <= 24 hours. Verify point-in-time recovery via binary log replay. | Specified |
| NFR-HC-021 | Localisation | Quality Standards Section 5 | HLD 2.1 Presentation Layer | Test Strategy 3.3: Functional Testing | Test: switch to Luganda; confirm UI translated. Confirm drug names remain English. Confirm currency formatting per locale. | Specified |
| NFR-HC-022 | Critical Lab Value Escalation Timeliness | BR-CLIN-003 | HLD 5.1 Core Domain Events; LLD 4.3.1 LabService | Test Strategy 3.3: Functional Testing | Test: enter panic value; confirm notification within 60s. Confirm 30-minute escalation. Confirm 60-minute escalation. Confirm audit trail timestamps. | Specified |
| NFR-HC-023 | Task Resumption After Interruption | Clinical Workflow Requirements | HLD 2.3 Business Logic Layer; LLD 5.2 Task Resumption | Test Strategy 3.3: Functional Testing | Test: begin OPD form; navigate away; return; confirm data and cursor position restored. Confirm incomplete fields highlighted. | Specified |
| NFR-HC-024 | Prescribing Authority Enforcement | Uganda Medical and Dental Practitioners Act; BR-CLIN-002 | HLD 2.3 Business Logic Layer; LLD 4.7.1 PermissionService | Test Strategy 3.3: Functional Testing | Test: Nurse attempts prescription; confirm blocked. Clinical Officer prescribes outside scope; confirm blocked. Doctor prescribes any formulary drug; confirm accepted. | Specified |

---

## 4. Business Rule Traceability

| BR ID | Rule | FR Cross-Reference | Test Coverage |
|---|---|---|---|
| BR-CLIN-001 | Triage priority determines queue position; emergency jumps all queues | FR-REG-011, FR-OPD-002, FR-LAB-001 | TC-REG-011a: Emergency jumps queue; TC-OPD-002a: Queue ordered by triage priority |
| BR-CLIN-002 | Prescribing authority is role-restricted (Doctor, CO, Nurse, Pharmacist) | FR-OPD-006, NFR-HC-024 | TC-OPD-006c: Five Rights validated; TC-RBAC-001a: Role permissions enforced |
| BR-CLIN-003 | Critical value escalation follows timed cascade (30 min, 60 min) | FR-LAB-005, NFR-HC-022 | TC-LAB-005a-c: Panic value triggers escalation cascade |
| BR-CLIN-004 | Drug interaction alerts use 4-tier severity classification | FR-OPD-008, NFR-HC-012 | TC-OPD-008a-c: Tier 3 modal, Tier 4 hard stop, override logged |
| BR-CLIN-005 | Medication reconciliation mandatory at every transition of care | FR-PHR-015 | TC-PHR-015a-b: Reconciliation form generated; transition blocked without reconciliation |
| BR-CLIN-006 | Paediatric dosing safeguards for patients under 12 years | FR-PHR-014, NFR-HC-011 | TC-PHR-014a-d: Weight-based dosing, adult ceiling, decimal error, no-weight block |
| BR-CLIN-007 | Early Warning Score uses NEWS2 framework | FR-OPD-014 | TC-OPD-014a-b: NEWS2 calculated; score 7+ triggers immediate review |
| BR-CLIN-008 | Five Rights enforcement in CPOE | FR-OPD-015 | TC-OPD-015a-c: All 5 rights validated; failures block submission |
| BR-CLIN-009 | Discharge documentation completeness enforced | FR-OPD-013 | TC-OPD-013a: Discharge blocked without ICD-10 diagnosis |
| BR-FIN-001 | Auto-billing posts charges for every clinical action | FR-BIL-004 | TC-BIL-004a-c: Lab, drug, procedure charges auto-posted |
| BR-FIN-002 | Insurance co-pay splitting when patient has active scheme | FR-BIL-003 | TC-BIL-003a: Category price applied |
| BR-FIN-003 | Mobile money reconciliation (MTN MoMo, Airtel Money) | FR-BIL-007 | TC-BIL-007a-c: Auto-match, suspense account for unmatched |
| BR-FIN-004 | Daily cashier reconciliation mandatory; discrepancy > UGX 5,000 flagged | FR-BIL-008 | TC-BIL-008a-b: Session closed; discrepancy flagged |
| BR-FIN-005 | Credit management with facility admin approval | FR-BIL-010 | TC-BIL-010a-c: Credit created; ageing report; write-off approval |
| BR-FIN-006 | Write-off requires tiered approval (under/above UGX 500,000) | FR-BIL-010 | TC-BIL-010c: Write-off requires approval |
| BR-FIN-007 | Deposit on admission required for inpatient | Phase 2 (IPD) | [TRACE-GAP: Phase 2 requirement -- not yet specified] |
| BR-FIN-008 | Missing charge detection runs daily | FR-BIL-009 | TC-BIL-009a-b: Encounters without charge flagged |
| BR-DATA-001 | Global patient identity maintained at platform level | FR-REG-001, FR-REG-010 | TC-REG-001a: Patient created; TC-REG-010a-b: Identity visible, clinical data hidden |
| BR-DATA-002 | Emergency access requires two-factor confirmation | FR-RBAC-006, FR-RBAC-007 | TC-RBAC-006a-d: Two-factor, data revealed, expiry, SMS sent |
| BR-DATA-003 | Offline conflict resolution uses field-level merge | NFR-HC-013 | TC-NFR-013: Concurrent offline edits flagged for clinician review |
| BR-DATA-004 | Tenant isolation enforced via `facility_id` WHERE clause and global scope | FR-AUTH-001, FR-TNT-001, NFR-HC-015 | TC-NFR-015: Zero cross-tenant records; raw SQL without facility_id fails CI |
| BR-DATA-005 | Auto-save protects against data loss from power failure | NFR-HC-016 | TC-NFR-016: Kill browser; reopen; confirm recovery prompt |
| BR-DATA-006 | Data quality enforcement requires structured input for clinical fields | FR-OPD-004, FR-REG-001 | TC-OPD-004b: Free-text diagnosis blocked; TC-REG-001b: Minimum fields enforced |
| BR-HMIS-001 | HMIS 105 auto-populated from clinical data | NFR-HC-009 | TC-NFR-009: 10 OPD visits tallied without manual entry |
| BR-HMIS-002 | HMIS 108 auto-populated from IPD data | NFR-HC-009 | [TRACE-GAP: Phase 2 requirement -- IPD module not yet specified] |
| BR-HMIS-003 | HMIS 033b auto-tallies 27 IDSR priority diseases | NFR-HC-009 | TC-NFR-009: Epidemiological surveillance auto-tally |
| BR-HMIS-004 | DHIS2 submission in compatible format | NFR-HC-009 | TC-NFR-009: DHIS2 API push to test instance |
| BR-HMIS-005 | PEPFAR MER indicator calculation | NFR-HC-009 | [TRACE-GAP: Phase 2 requirement -- ART module not yet specified] |
| BR-PID-001 | EMPI matching uses probabilistic algorithms | FR-REG-009 | TC-REG-009a-b: Fuzzy match with confidence score |
| BR-PID-002 | Duplicate detection triggered at registration | FR-REG-009 | TC-REG-009b: 80%+ match triggers mandatory warning |
| BR-PID-003 | Patient merge allows consolidation, reversible within 30 days | FR-REG-008 | TC-REG-008a-c: Merge, audit, unmerge |
| BR-PID-004 | Multiple patient identifiers supported | FR-REG-005 | TC-REG-005a-c: NIN, NHIS, lookup by any ID type |
| BR-INS-001 | Pre-authorisation required for admissions exceeding benefit limit | Phase 2 (Insurance) | [TRACE-GAP: Phase 2 requirement -- insurance module not yet specified] |
| BR-INS-002 | Claim generation automated on discharge/visit completion | Phase 2 (Insurance) | [TRACE-GAP: Phase 2 requirement -- insurance module not yet specified] |
| BR-INS-003 | Rejection management with resubmission | Phase 2 (Insurance) | [TRACE-GAP: Phase 2 requirement -- insurance module not yet specified] |
| BR-INS-004 | Insurance receivables ageing tracked per insurer | Phase 2 (Insurance) | [TRACE-GAP: Phase 2 requirement -- insurance module not yet specified] |
| BR-RX-001 | Controlled substances require narcotic register entry | FR-PHR-011 | TC-PHR-011a-c: Register entry, running balance, discrepancy alert |
| BR-RX-002 | Stock-aware prescribing displays stock levels | FR-OPD-007 | TC-OPD-007a-b: Zero-stock warning; alternative suggested |
| BR-RX-003 | Tall Man Lettering for LASA drugs | FR-PHR-013 | TC-PHR-013a-b: LASA display; list maintainable |
| BR-HOPE-001 | Multi-site management (Tororo and Kasanje as separate tenants) | FR-TNT-001, FR-REG-010, BR-DATA-001 | TC-TNT-001a: Facility created; TC-REG-010a-b: Cross-facility lookup |
| BR-HOPE-002 | Indigent/sponsored patient charity write-off workflow | FR-BIL-010 | TC-BIL-010c: Write-off requires approval |

---

## 5. Gap Analysis

### 5.1 Phase 1 Traceability Gaps

All 83 Phase 1 functional requirements (FR-AUTH through FR-RBAC) have been mapped to:

- Source (PRD feature)
- HLD section
- LLD service
- ERD table(s)
- API endpoint (where applicable)
- Test case(s)

**No Phase 1 forward traceability gaps exist at the specification level.**

### 5.2 Business Rule Gaps (Deferred to Phase 2+)

The following business rules reference modules not yet specified in Phase 1:

| BR ID | Rule | Gap Type | Resolution Timeline |
|---|---|---|---|
| BR-FIN-007 | Deposit on admission (IPD) | No implementing FR in Phase 1 | Phase 2: IPD module specification |
| BR-HMIS-002 | HMIS 108 auto-population (IPD) | No implementing FR in Phase 1 | Phase 2: IPD module specification |
| BR-HMIS-005 | PEPFAR MER indicator calculation | No implementing FR in Phase 1 | Phase 2: ART/HIV programme module |
| BR-INS-001 | Insurance pre-authorisation | No implementing FR in Phase 1 | Phase 2: Insurance module specification |
| BR-INS-002 | Claim generation automated | No implementing FR in Phase 1 | Phase 2: Insurance module specification |
| BR-INS-003 | Rejection management | No implementing FR in Phase 1 | Phase 2: Insurance module specification |
| BR-INS-004 | Insurance receivables ageing | No implementing FR in Phase 1 | Phase 2: Insurance module specification |

### 5.3 Implementation Status Summary

| Status | Count | Percentage |
|---|---|---|
| Specified (requirements, design, and test cases documented) | 83 FR + 24 NFR = 107 | 100% |
| Designed (HLD + LLD + ERD complete) | 107 | 100% |
| Test cases defined | 107 | 100% |
| Implemented | 0 | 0% |
| Tested | 0 | 0% |

*Phase 1 development has not yet commenced. All traceability artifacts are at the specification stage.*
