# Regulatory Compliance Documentation -- Medic8

**Document ID:** Medic8-COMP-001
**Version:** 1.0
**Date:** 2026-04-03
**Author:** Peter Bamuhigire
**Standards:** Uganda PDPA 2019, HIV/AIDS Prevention and Control Act 2014, Uganda MoH HMIS Standards, IEEE 1012-2016

---

## 1. Uganda Data Protection and Privacy Act 2019 (PDPA) Compliance

The Medic8 system processes patient health information classified as sensitive personal data under the Uganda Data Protection and Privacy Act 2019. This section maps each applicable PDPA section to the Medic8 implementation controls.

### 1.1 PDPA Compliance Matrix

| PDPA Section | Requirement | Medic8 Implementation | NFR/FR Reference | Status |
|---|---|---|---|---|
| **Section 5** -- Principles of Data Processing | Personal data shall be processed lawfully, fairly, and in a transparent manner. Data shall be collected for specified, explicit, and legitimate purposes and not further processed in a manner incompatible with those purposes. | Medic8 collects patient data solely for the purpose of clinical care delivery, billing, and mandatory public health reporting (HMIS, IDSR). Each data collection point displays a purpose statement. Data is not used for marketing, research, or secondary purposes without explicit consent. The consent engine records the specific purpose for which consent was granted. | NFR-HC-001, FR-REG-001 | Designed |
| **Section 10** -- Consent Requirements | Processing of personal data requires the informed, specific, and freely given consent of the data subject, unless an exemption applies (e.g., medical emergency, public health). | Medic8 implements a configurable consent engine per jurisdiction. At patient registration (FR-REG-001), the system records consent for: routine clinical data processing, cross-facility identity sharing, emergency data access, and HIV status disclosure during emergencies. Consent is revocable. Emergency exemptions are logged per BR-DATA-002 with mandatory post-hoc review. | FR-REG-001, FR-RBAC-006, BR-DATA-002 | Designed |
| **Section 16** -- Rights of Data Subjects | Data subjects have the right to: access their personal data, request correction, request deletion (subject to retention obligations), and obtain a copy in a portable format. | The patient portal (Role 17: Patient/Client) provides: read-only access to own medical records, lab results, prescriptions, and billing history. Patients may request data correction through the portal (flagged for Records Officer review). Data export is available in PDF and FHIR R4 Patient resource format. Deletion requests are subject to the 10-year MoH retention policy (NFR-HC-007). | NFR-HC-007, NFR-HC-014 | Designed |
| **Section 22** -- Security of Personal Data | The data controller shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including encryption and access controls. | Medic8 implements: AES-256-GCM encryption at rest for all patient health data (NFR-HC-002). TLS 1.2+ encryption in transit on all endpoints (NFR-HC-003). Role-based access control with 18 defined roles (FR-RBAC-001). Attribute-based access control for sensitive records -- HIV, mental health, substance abuse, reproductive health (NFR-HC-010, FR-RBAC-003). 15-minute session timeout (NFR-HC-004). MFA for privileged roles (NFR-HC-005). | NFR-HC-002, NFR-HC-003, NFR-HC-004, NFR-HC-005, NFR-HC-010, FR-RBAC-001, FR-RBAC-003 | Designed |
| **Section 24** -- Record of Processing Activities | The data controller shall maintain a record of processing activities, including the categories of data processed, the purposes, and the recipients. | Medic8 maintains a complete, tamper-proof audit trail of all create, read, update, and delete operations on patient health records (NFR-HC-001). Every audit log entry records: `user_id`, `timestamp` (UTC), `action`, `resource_type`, `resource_id`, `facility_id`, `ip_address`, and `outcome`. The audit log is append-only; no role, including Super Admin, can modify or delete entries. | NFR-HC-001, FR-RBAC-005 | Designed |
| **Section 31** -- Breach Notification | The data controller shall notify the Personal Data Protection Office (PDPO) within 72 hours of becoming aware of a data breach and shall notify affected data subjects without undue delay. | Medic8 provides breach notification tooling (NFR-HC-008) that: identifies all affected patient records within 72 hours of breach confirmation, generates a breach impact report (affected count, data categories, timeline, facility identifiers), supports immediate notification to the PDPO, and generates SMS notification drafts for affected patients. | NFR-HC-008 | Designed |
| **Section 34** -- Cross-Border Transfer of Personal Data | Personal data shall not be transferred to a country outside Uganda unless that country has adequate data protection laws or the data subject has consented. | Medic8 enforces data residency per country configuration (NFR-HC-019). Patient data resides in-country unless the regulatory profile explicitly permits cross-border transfer. Cross-border transfer requests via FHIR API or DHIS2 export are validated against the active regulatory profile before execution. Transfers to non-permitted destinations are blocked and logged. | NFR-HC-019 | Designed |

### 1.2 Consent Categories

Medic8 manages consent at a granular level per data sensitivity tier:

| Consent Category | Data Type | Default | Revocable | Legal Basis |
|---|---|---|---|---|
| Routine clinical processing | Demographics, vitals, diagnoses, prescriptions, lab results | Opt-in at registration | Yes (subject to retention period) | PDPA Section 10; Medical treatment necessity |
| Cross-facility identity sharing | Patient name, age, sex, identifiers | Opt-in at registration | Yes | PDPA Section 10 |
| Emergency clinical data access | Allergies, medications, blood group, last 3 diagnoses | Opt-in at registration | Yes | PDPA Section 10; Medical emergency exemption |
| HIV status emergency disclosure | HIV status during emergency access | Explicit opt-in (separate consent) | Yes | HIV/AIDS Act Section 18; PDPA Section 10 |
| HMIS aggregate reporting | De-identified aggregate data | Mandatory (statutory obligation) | No | Public Health Act; MoH HMIS directive |
| PEPFAR MER reporting | De-identified programme data | Mandatory for PEPFAR facilities | No | PEPFAR reporting agreement |
| Research data sharing | Anonymised data sets | Explicit opt-in per study | Yes | PDPA Section 10; Research ethics board approval required |

### 1.3 Data Retention Schedule

| Data Category | Retention Period | Legal Basis | Post-Retention Action |
|---|---|---|---|
| Patient clinical records | 10 years from last encounter | Uganda MoH policy | Archive (not delete); accessible on request |
| Audit logs | 10 years from creation | PDPA Section 24 | Archive |
| Financial records | 7 years from transaction | Uganda Income Tax Act | Archive |
| HMIS submissions | 10 years from reporting period | MoH HMIS directive | Archive |
| Consent records | Duration of patient relationship + 10 years | PDPA Section 10 | Archive |
| Narcotic register | Permanent | NDA regulations | No deletion permitted |
| Breach notification records | 10 years from incident | PDPA Section 31 | Archive |

---

## 2. HIV/AIDS Prevention and Control Act 2014

### 2.1 Section 18: Mandatory Confidentiality of HIV Test Results

The HIV/AIDS Prevention and Control Act 2014 Section 18 mandates that HIV test results shall be kept confidential and shall not be disclosed without the informed consent of the person tested, except in limited circumstances defined by law.

### 2.2 Implementation Controls

| Control | Implementation | Reference |
|---|---|---|
| **Access restriction** | HIV status is classified as a sensitive record. Only clinicians who hold an explicit "HIV programme" permission AND have an active treatment relationship with the patient can view HIV status. All other users see `[Restricted]` in place of the field value. | NFR-HC-010, FR-RBAC-003 |
| **ABAC enforcement** | Attribute-based access control (ABAC) evaluates 3 attributes before granting access: (1) user holds "sensitive record" permission, (2) user has an active treatment relationship with the patient, (3) data category matches user's approved sensitive categories. All 3 must be true. | NFR-HC-010, FR-RBAC-003 |
| **Cross-facility restriction** | HIV status is excluded from cross-facility patient lookup results (FR-REG-010) unless the patient has granted explicit emergency HIV disclosure consent. | FR-REG-010, BR-DATA-002 |
| **Emergency access** | Break-the-glass access may reveal HIV status only if the patient has previously consented to emergency HIV disclosure. Emergency access requires two-factor patient confirmation (name + date of birth), expires after 24 hours, and triggers an immediate SMS notification to the patient. | FR-RBAC-006, FR-RBAC-007, BR-DATA-002 |
| **Audit trail** | All access to HIV records, whether granted or denied, is logged with: viewer identity, timestamp, facility, patient ID, access outcome (granted/denied), and justification. | NFR-HC-001, NFR-HC-010 |
| **Post-access review** | Break-the-glass access to HIV records triggers a mandatory post-access review by the Facility Admin within 48 hours. The review confirms the access was clinically justified. | FR-RBAC-007 |

### 2.3 Mental Health, Reproductive Health, and Substance Abuse Records

The same ABAC access tier applies to:

- Mental health diagnoses and treatment records
- Reproductive health records (contraception, termination of pregnancy, STI treatment)
- Substance abuse records

Each category has its own permission flag, allowing facilities to grant clinicians access to specific sensitive categories without exposing others.

---

## 3. Uganda HMIS Compliance

### 3.1 Mandatory Reporting Forms

| HMIS Form | Title | Frequency | Data Source | Auto-Population | Reference |
|---|---|---|---|---|---|
| HMIS 105 | Outpatient Monthly Report | Monthly | OPD encounters, lab tests, radiology, maternity, immunisation | Section 1: diagnoses by age/sex from ICD-10 coded visits. Section 2: lab test tallies. Section 3: radiology tallies. Section 4: maternity tallies. Section 5: HIV/AIDS services. Section 6: immunisation. Section 7: dental. Section 8: eye. | BR-HMIS-001, NFR-HC-009 |
| HMIS 108 | Inpatient Monthly Report | Monthly | IPD admissions, discharges, deaths, theatre records | Admissions, discharges, and deaths by diagnosis, age, sex. Bed occupancy rates. Surgical operations. | BR-HMIS-002, NFR-HC-009 |
| HMIS 033b | Weekly Epidemiological Surveillance Report | Weekly | OPD diagnoses matching 27 IDSR priority disease codes | Auto-tallies from weekly OPD diagnoses. | BR-HMIS-003, NFR-HC-009 |

### 3.2 DHIS2 Integration

| Capability | Implementation | Reference |
|---|---|---|
| **Data format** | HMIS data exported in DHIS2 ADX/JSON format compatible with the Uganda eHMIS instance (hmis2.health.go.ug) | BR-HMIS-004, NFR-HC-009 |
| **API push** | Direct API push to DHIS2 when internet connectivity is available | BR-HMIS-004 |
| **Submission tracking** | The system tracks which reporting periods have been submitted and which are pending | NFR-HC-009 |
| **Offline fallback** | When internet is unavailable, HMIS data is queued locally and submitted when connectivity resumes | NFR-HC-013 |

### 3.3 HMIS Form Version Management

| Control | Implementation | Reference |
|---|---|---|
| **Version control** | HMIS form mappings are stored in configuration tables, not hardcoded | NFR-HC-009, Gap Analysis HIGH-007 |
| **Update process** | Subscribe to hmis2.health.go.ug notices for form version changes | Gap Analysis HIGH-007 |
| **Turnaround** | Maximum 30-day turnaround for updating mappings after MoH publishes a new form version | Gap Analysis HIGH-007 |
| **Fallback** | If a new form version is not yet mapped, export data in the previous version with a warning flag | Gap Analysis HIGH-007 |

---

## 4. Clinical Safety Compliance

### 4.1 Drug Interaction Database

| Control | Implementation | Reference |
|---|---|---|
| **Database source** | Licensed third-party drug interaction database (DrugBank, RxNorm/NLM, or Uganda NDA formulary). The database shall NOT be built in-house. | Gap Analysis HIGH-001 |
| **Update frequency** | Database updates applied within 30 days of publication by the source authority | Gap Analysis HIGH-001 |
| **Coverage** | Interactions, contraindications, allergy-prescription conflicts, pregnancy/lactation warnings | BR-CLIN-004, FR-OPD-008 |
| **Liability** | Database vendor assumes data accuracy liability per licensing agreement | Gap Analysis HIGH-001, HIGH-004 |

### 4.2 Clinical Decision Support (CDS)

| Control | Implementation | Reference |
|---|---|---|
| **CDS classification** | Medic8 CDS is decision support only, not decision making. Clinical liability remains with the prescribing clinician. | Gap Analysis HIGH-004 |
| **Terms of Service** | The Medic8 Terms of Service explicitly disclaim clinical liability. CDS alerts are advisory; the clinician retains full prescribing authority and responsibility. | Gap Analysis HIGH-004 |
| **Alert configuration** | CDS rules are data-driven (configuration table, not hardcoded). Alert types: Info, Warning (overridable), Serious (overridable with documented reason), Fatal (not overridable by prescriber). | BR-CLIN-004, NFR-HC-012 |
| **Override audit** | Every alert fired and every override action is audited with: clinician ID, timestamp, reason text, patient ID, alert ID. | NFR-HC-012 |
| **Override monitoring** | Override rates are tracked per facility for quality monitoring. | NFR-HC-012 |
| **Clinical validation** | A practising clinician shall validate alert categories and thresholds before production deployment. | Gap Analysis HIGH-004 |

### 4.3 Medication Error Prevention

| Control | Implementation | Reference |
|---|---|---|
| **Five Rights CPOE** | Every prescription validates: right patient, right drug, right dose, right route, right time. Failure blocks submission. | BR-CLIN-008, FR-OPD-015 |
| **Paediatric dosing** | Weight-based dosing (mg/kg) for patients under 12. Adult ceiling dose cap. 10x deviation decimal error flag. No weight within 24 hours blocks prescription. | BR-CLIN-006, NFR-HC-011, FR-PHR-014 |
| **Tall Man Lettering** | LASA drug names display differentiating letters in uppercase (e.g., hydrOXYzine vs hydrALAZINE). | BR-RX-003, FR-PHR-013 |
| **Stock-aware prescribing** | Zero-stock warning at prescribing point with therapeutic alternatives. | BR-RX-002, FR-OPD-007 |
| **Controlled substances** | Narcotic register with running balance, witness requirement, discrepancy alert. | BR-RX-001, FR-PHR-011 |

### 4.4 Incident Reporting

| Control | Implementation | Reference |
|---|---|---|
| **Medication error reporting** | Incident module for reporting medication errors, near-misses, and adverse drug reactions. | Gap Analysis HIGH-004 |
| **Clinical safety officer** | Each facility shall designate a Clinical Safety Officer responsible for reviewing CDS override patterns, medication error reports, and critical value escalation compliance. | Operational Governance |
| **Investigation workflow** | Reported incidents trigger a structured investigation: root cause analysis, corrective action, preventive action, and closure with sign-off. | Operational Governance |

### 4.5 Clinical Safety Framework Alignment

The following 45-point clinical safety framework (adapted from Rowlands) is applied to the Medic8 system:

| # | Domain | Control Area | Medic8 Implementation |
|---|---|---|---|
| 1 | Governance | Clinical safety officer designated per facility | Operational requirement; enforced during facility onboarding |
| 2 | Governance | Clinical safety incident reporting process | Incident module with structured investigation workflow |
| 3 | Governance | Clinical safety risk register maintained | Risk assessment document (Medic8-RISK-001) |
| 4 | Governance | Clinical safety policy published | Facility-level policy template provided |
| 5 | Governance | Clinical safety training for all clinical users | Training materials requirement (Phase 1 onboarding) |
| 6 | Prescribing | Drug interaction checking (4 tiers) | FR-OPD-008, NFR-HC-012, BR-CLIN-004 |
| 7 | Prescribing | Allergy-prescription conflict detection | FR-OPD-008, Gap Analysis HIGH-001 |
| 8 | Prescribing | Paediatric dosing safeguards | FR-PHR-014, NFR-HC-011, BR-CLIN-006 |
| 9 | Prescribing | Prescribing authority enforcement | NFR-HC-024, BR-CLIN-002 |
| 10 | Prescribing | Five Rights CPOE validation | FR-OPD-015, BR-CLIN-008 |
| 11 | Prescribing | Stock-aware prescribing with alternatives | FR-OPD-007, BR-RX-002 |
| 12 | Prescribing | Tall Man Lettering for LASA drugs | FR-PHR-013, BR-RX-003 |
| 13 | Prescribing | Controlled substance register | FR-PHR-011, BR-RX-001 |
| 14 | Prescribing | Generic/brand substitution with notification | FR-PHR-003 |
| 15 | Dispensing | Dispensing label with patient name, drug, dose, frequency, route | FR-PHR-004 |
| 16 | Dispensing | Partial dispensing with pending balance tracking | FR-PHR-005 |
| 17 | Dispensing | Expiry tracking with 90-day alert | FR-PHR-008 |
| 18 | Dispensing | Minimum stock level alerts | FR-PHR-009 |
| 19 | Dispensing | Inpatient drug round tracking (MAR) | FR-PHR-006 |
| 20 | Laboratory | Critical value alerts with timed escalation | FR-LAB-005, NFR-HC-022, BR-CLIN-003 |
| 21 | Laboratory | Result validation by supervisor before clinician visibility | FR-LAB-006 |
| 22 | Laboratory | Quality control with Levey-Jennings charts | FR-LAB-007 |
| 23 | Laboratory | Barcode/QR specimen identification | FR-LAB-002 |
| 24 | Laboratory | Specimen chain of custody tracking | FR-LAB-003 |
| 25 | Laboratory | HL7 v2 analyser interface | FR-LAB-008 |
| 26 | Laboratory | LOINC-coded test definitions | FR-LAB-010 |
| 27 | Clinical | ICD-10 coded diagnoses (no free text) | FR-OPD-004, BR-DATA-006 |
| 28 | Clinical | SOAP note structure | FR-OPD-003 |
| 29 | Clinical | NEWS2 early warning score | FR-OPD-014, BR-CLIN-007 |
| 30 | Clinical | Medication reconciliation at transitions | FR-PHR-015, BR-CLIN-005 |
| 31 | Clinical | Discharge completeness enforcement | FR-OPD-013, BR-CLIN-009 |
| 32 | Clinical | Referral letter generation (CDA R2) | FR-OPD-010 |
| 33 | Clinical | Nursing sensitive outcome tracking (14 NSOs) | NFR-HC-018 |
| 34 | Identity | EMPI duplicate detection | FR-REG-009, BR-PID-002 |
| 35 | Identity | Patient merge with audit trail | FR-REG-008, BR-PID-003 |
| 36 | Identity | Triage priority queue enforcement | FR-REG-011, BR-CLIN-001 |
| 37 | Access | RBAC with 18 defined roles | FR-RBAC-001 |
| 38 | Access | ABAC for sensitive records (HIV, mental health) | FR-RBAC-003, NFR-HC-010 |
| 39 | Access | Break-the-glass with mandatory reason and SMS | FR-RBAC-007 |
| 40 | Access | Emergency cross-facility access with 24-hour expiry | FR-RBAC-006, BR-DATA-002 |
| 41 | Data | Auto-save on every form interaction | NFR-HC-016, BR-DATA-005 |
| 42 | Data | Offline clinical resilience (72-hour queue) | NFR-HC-013 |
| 43 | Data | Clinical conflict resolution (both versions preserved) | NFR-HC-013, BR-DATA-003 |
| 44 | Data | Task resumption after interruption | NFR-HC-023 |
| 45 | Audit | Tamper-proof audit trail for all PHI operations | NFR-HC-001, FR-RBAC-005 |

---

## 5. Global Regulatory Readiness

### 5.1 Multi-Jurisdiction Compliance Matrix

| Market | Regulation | Key Requirements | Medic8 Readiness | Gap |
|---|---|---|---|---|
| **Uganda** | Data Protection and Privacy Act 2019 (PDPA) | Consent, data subject rights, breach notification (72h), data residency, record of processing | Designed: consent engine, audit trail, breach tooling, data residency per tenant | Legal review pending (Gap Analysis HIGH-002). Data protection lawyer engagement required. |
| **Kenya** | Data Protection Act 2019 | Consent, data subject rights, breach notification (72h), DPIA requirement, cross-border transfer safeguards | Partially ready: consent engine reusable; country configuration supports Kenya regulatory profile | Kenya-specific consent wording and DPIA template not yet created |
| **India** | Digital Information Security in Healthcare Act (DISHA, draft) | Health data protection, health information exchange standards, ABDM interoperability, ABHA health ID | Partially ready: FHIR R4 API enables interoperability; ABHA integration not yet specified | ABHA health ID integration not designed. DISHA is still in draft; requirements may change. |
| **Australia** | Privacy Act 1988 (Australian Privacy Principles) | 13 APPs, My Health Records Act compliance, notifiable data breach scheme (72h) | Partially ready: data residency configurable; breach notification tooling exists | APP compliance mapping not completed. My Health Records integration not designed. |
| **Nigeria** | Nigeria Data Protection Act 2023 (NDPA) | Consent, DPIA, data subject rights, breach notification, data residency | Partially ready: consent engine reusable; country configuration supports Nigeria | NDPA-specific DPIA template not created. NHIA integration not specified. |
| **USA (PEPFAR)** | HIPAA Privacy Rule and Security Rule | PHI safeguards, access controls, audit trail, breach notification, BAA requirements | Partially ready: AES-256 encryption, RBAC, audit trail, breach tooling meet HIPAA technical safeguards | Business Associate Agreement (BAA) template not created. HIPAA-specific administrative safeguards not documented. PEPFAR MER indicator compliance designed (BR-HMIS-005). |

### 5.2 Regulatory Profile Architecture

Each Medic8 deployment activates a country-specific regulatory profile at tenant configuration time (FR-TNT-004). The system shall not permit operation without an assigned regulatory profile. The regulatory profile controls:

- Required consent categories and wording
- Data residency enforcement rules
- HMIS form set and reporting obligations
- Drug scheduling classes and prescribing authority rules
- Tax and insurance rules
- Clinical coding system preference (ICD-10 vs ICD-11)
- Cross-border transfer permissions

---

## 6. Data Processing Impact Assessment (DPIA) Template

Per Uganda PDPA 2019 Section 22, a Data Processing Impact Assessment shall be conducted for any processing activity that is likely to result in high risk to the rights and freedoms of data subjects. The following template shall be completed for each major processing activity within Medic8.

---

### DPIA-[SEQUENCE]: [Processing Activity Name]

**DPIA ID:** DPIA-[SEQUENCE]
**Date:** [YYYY-MM-DD]
**Assessor:** [Name and role]
**Approved by:** [Data Protection Officer name]

#### 6.1 Processing Activity Description

| Field | Value |
|---|---|
| **Processing activity** | [e.g., "Patient clinical record creation and management"] |
| **Purpose** | [e.g., "Delivery of clinical care, continuity of care across encounters"] |
| **System module** | [e.g., "OPD Module, Patient Registration"] |
| **Frequency** | [e.g., "Continuous during facility operating hours"] |

#### 6.2 Personal Data Categories

| Data Category | Sensitivity Level | Examples |
|---|---|---|
| Demographics | Standard PII | Name, date of birth, sex, address, phone, NIN |
| Clinical records | Sensitive PHI | Diagnoses (ICD-10), prescriptions, lab results, vitals, clinical notes |
| HIV status | Highly sensitive PHI | HIV test results, ART status, viral load |
| Mental health | Highly sensitive PHI | Psychiatric diagnoses, counselling notes |
| Reproductive health | Highly sensitive PHI | Contraception records, antenatal care, STI treatment |
| Substance abuse | Highly sensitive PHI | Treatment records, screening results |
| Financial | Standard PII | Billing records, insurance details, mobile money transactions |
| Biometric | Sensitive PII | Fingerprint (if used for patient identification) |

#### 6.3 Legal Basis for Processing

| Legal Basis | PDPA Section | Justification |
|---|---|---|
| Consent | Section 10 | Patient provides informed consent at registration |
| Medical treatment necessity | Section 10 exemption | Processing necessary for clinical care delivery |
| Public health obligation | Section 10 exemption | HMIS reporting, disease surveillance (IDSR) |
| Legal obligation | Section 10 exemption | Narcotic register (NDA), tax records (URA) |

#### 6.4 Data Recipients

| Recipient | Data Shared | Legal Basis | Transfer Mechanism |
|---|---|---|---|
| Treating clinicians (same facility) | Full clinical record | Treatment necessity | Internal system access (RBAC) |
| Clinicians (other facility) | Identity only (name, age, sex, identifiers) | Patient consent | Cross-facility lookup API (FR-REG-010) |
| Clinicians (emergency access) | Allergies, medications, blood group, last 3 diagnoses | Emergency exemption | Break-the-glass access (FR-RBAC-006) |
| Uganda MoH (DHIS2) | De-identified aggregate data | Public health obligation | DHIS2 API push (NFR-HC-009) |
| PEPFAR (DATIM) | De-identified programme indicators | Reporting agreement | MER indicator export (BR-HMIS-005) |
| Insurance providers | Claim data (diagnosis, services, amounts) | Contract performance | Insurance claims API (Phase 2) |
| Patient (portal) | Own records only | Data subject right | Patient portal (read-only) |

#### 6.5 Data Retention

| Data Type | Retention Period | Basis |
|---|---|---|
| [Refer to Section 1.3 Data Retention Schedule] | | |

#### 6.6 Security Measures

| Measure | Implementation |
|---|---|
| Encryption at rest | AES-256-GCM for all patient health data (NFR-HC-002) |
| Encryption in transit | TLS 1.2+ on all endpoints (NFR-HC-003) |
| Access control | RBAC (18 roles) + ABAC (sensitive records) (FR-RBAC-001, NFR-HC-010) |
| Session management | 15-minute timeout, MFA for admins (NFR-HC-004, NFR-HC-005) |
| Audit trail | Tamper-proof log of all PHI operations (NFR-HC-001) |
| Tenant isolation | `facility_id` WHERE clause + Eloquent global scope (NFR-HC-015) |
| Backup | Daily automated backup, RPO 24h, RTO 4h (NFR-HC-020) |
| Breach response | 72-hour breach impact report, SMS notification (NFR-HC-008) |

#### 6.7 Risk Assessment

| Risk | Likelihood (1-5) | Impact (1-5) | Risk Score | Mitigation |
|---|---|---|---|---|
| Unauthorised access to clinical records | 2 | 5 | 10 | RBAC, ABAC, MFA, session timeout, audit trail |
| Cross-tenant data leakage | 1 | 5 | 5 | Tenant isolation at repository, global scope, and CI audit rule |
| HIV status disclosure | 2 | 5 | 10 | ABAC sensitive record tier, break-the-glass audit, patient SMS notification |
| Insider threat (staff accessing without justification) | 3 | 4 | 12 | Audit trail, ABAC, post-access review, override monitoring |
| Data loss from power failure | 2 | 4 | 8 | Auto-save, offline queue (72h), daily backup |
| Cross-border transfer without consent | 1 | 4 | 4 | Data residency enforcement per regulatory profile |

#### 6.8 Mitigation Measures

| Risk Score >= 12 | Specific Controls |
|---|---|
| Insider threat (12) | All PHI access logged. ABAC restricts sensitive records. Post-access review for break-the-glass. Override rate monitoring per facility. Anomalous access patterns trigger Facility Admin alert. |

#### 6.9 DPIA Decision

| Decision | Criteria |
|---|---|
| **Proceed** | All risks mitigated to acceptable level (score < 12 after controls) |
| **Proceed with conditions** | Residual risks >= 12 have approved monitoring plans |
| **Do not proceed** | Unmitigated critical risks exist |

**Decision:** [Proceed / Proceed with conditions / Do not proceed]
**DPO Sign-off:** [Name, date]

---

## Appendix A: Regulatory Contact Register

| Authority | Contact Purpose | Status |
|---|---|---|
| Uganda Medical and Dental Practitioners Council (UMDPC) | Software registration enquiry (Gap Analysis HIGH-003) | [CONTEXT-GAP: Enquiry not yet submitted] |
| National Drug Authority (NDA), Kampala | Drug interaction database licensing; software guidance for prescribing/dispensing | [CONTEXT-GAP: Enquiry not yet submitted] |
| Personal Data Protection Office (PDPO), Uganda | PDPA compliance registration; breach notification protocol | [CONTEXT-GAP: Registration not yet completed] |
| Uganda MoH eHealth Division | HMIS form version updates; DHIS2 integration approval | [CONTEXT-GAP: Engagement not yet initiated] |
| Data protection lawyer (Uganda) | Health data legal review (Gap Analysis HIGH-002) | [CONTEXT-GAP: Lawyer not yet engaged] |
