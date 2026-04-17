# Risk Assessment -- Medic8

**Document ID:** Medic8-RISK-001
**Version:** 1.0
**Date:** 2026-04-03
**Author:** Peter Bamuhigire
**Standards:** ISO 31000:2018 (Risk Management), IEEE 1012-2016 (V&V), Uganda PDPA 2019

---

## 1. Risk Assessment Context

### 1.1 Scope

This risk assessment covers the Medic8 multi-tenant SaaS healthcare management system across all planned phases:

- **Phase 1:** Core clinical platform (OPD, lab, pharmacy, billing, appointments, RBAC)
- **Phase 2:** Expansion (IPD, maternity, immunisation, insurance, HR, HMIS, accounting, inventory)
- **Phase 3:** Programmes and patient engagement (ART, TB, antenatal, patient portal, telemedicine)
- **Phase 4:** Advanced specialty (radiology, theatre, blood bank, dental, ophthalmology)

### 1.2 Risk Categories

| Category | Code | Description |
|---|---|---|
| Clinical Safety | R-CS | Risks that could result in patient harm or adverse clinical outcomes |
| Data Security | R-DS | Risks to the confidentiality, integrity, or availability of patient health information |
| Regulatory | R-RG | Risks of non-compliance with laws, regulations, or standards |
| Technical | R-TC | Risks to system reliability, performance, or interoperability |
| Business | R-BS | Risks to commercial viability, market position, or organisational capacity |
| Operational | R-OP | Risks to day-to-day system operation at deployed facilities |

### 1.3 Risk Scoring Methodology

**Likelihood scale:**

| Score | Level | Description |
|---|---|---|
| 1 | Rare | Less than 5% probability within the assessment period |
| 2 | Unlikely | 5-20% probability |
| 3 | Possible | 20-50% probability |
| 4 | Likely | 50-80% probability |
| 5 | Almost certain | Greater than 80% probability |

**Impact scale:**

| Score | Level | Description |
|---|---|---|
| 1 | Negligible | Minor inconvenience; no patient harm; no regulatory consequence |
| 2 | Minor | Limited impact; recoverable without significant effort |
| 3 | Moderate | Noticeable degradation; requires intervention; potential minor regulatory finding |
| 4 | Major | Significant harm, data breach, or regulatory enforcement action |
| 5 | Catastrophic | Patient death or serious harm; large-scale data breach; criminal prosecution |

**Risk score:** $Risk\ Score = Likelihood \times Impact$

**Risk classification:**

| Score Range | Classification | Action Required |
|---|---|---|
| 1-4 | LOW | Accept and monitor |
| 5-9 | MEDIUM | Mitigate and monitor quarterly |
| 10-14 | HIGH | Mitigate urgently; monthly review |
| 15-25 | CRITICAL | Immediate action; weekly review until reduced |

---

## 2. Risk Register

### 2.1 Clinical Safety Risks

| Risk ID | Risk Description | L | I | Score | Classification | Mitigation Strategy | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| R-CS-001 | Drug interaction missed due to incomplete or unlicensed database. A clinician prescribes a contraindicated drug combination because the interaction is absent from the database, resulting in an adverse drug event. | 3 | 5 | 15 | CRITICAL | Licence a comprehensive, commercially maintained drug interaction database (DrugBank or RxNorm/NLM). Establish a 30-day update cycle. Include Uganda NDA formulary data. Do not build in-house. Implement 4-tier alert system (BR-CLIN-004). Require clinical validation of alert thresholds before production. | Peter | Open -- Gap Analysis HIGH-001 unresolved |
| R-CS-002 | Paediatric overdose from dosing calculation error. A decimal error in weight-based dose calculation (e.g., 50 mg entered as 500 mg) results in a paediatric overdose. | 2 | 5 | 10 | HIGH | Enforce weight-based dosing for patients under 12 (BR-CLIN-006). Flag 10x deviation as decimal error. Apply adult ceiling dose cap. Block prescription if no weight recorded within 24 hours. | Peter | Designed -- FR-PHR-014, NFR-HC-011 |
| R-CS-003 | Critical lab value not escalated. A panic-range lab result (e.g., potassium 7.0 mmol/L) is entered but the requesting doctor is not notified, leading to delayed treatment. | 2 | 5 | 10 | HIGH | Implement timed escalation cascade: notification within 60 seconds, escalation to ward sister at 30 minutes, escalation to Facility Admin at 60 minutes (BR-CLIN-003). Multi-channel delivery: WebSocket, push notification, SMS fallback. Audit all escalation timestamps. | Peter | Designed -- FR-LAB-005, NFR-HC-022 |
| R-CS-004 | Wrong patient record accessed. A clinician opens the wrong patient's record and makes clinical entries (prescriptions, diagnoses) against the incorrect patient. | 3 | 5 | 15 | CRITICAL | Require patient ID confirmation at the start of every encounter. Display patient photo (if available), name, age, and MRN prominently on all clinical screens. Implement barcode/QR patient identification. EMPI duplicate detection at registration reduces identity confusion (FR-REG-009). | Peter | Partially designed -- additional patient confirmation workflow recommended |
| R-CS-005 | CDS alert fatigue leading to override of serious alert. Clinicians routinely override drug interaction alerts due to high alert volume, causing a Tier 3 (Serious) override that results in an adverse event. | 4 | 4 | 16 | CRITICAL | Track override rates per facility and per clinician (NFR-HC-012). Flag override rates exceeding 80% for review. Limit Info-tier alerts to sidebar display only (no modal). Clinician-validated alert thresholds reduce false positives. Monthly override rate reports to Clinical Safety Officer. | Peter | Designed -- NFR-HC-012 |

### 2.2 Data Security Risks

| Risk ID | Risk Description | L | I | Score | Classification | Mitigation Strategy | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| R-DS-001 | Patient data breach. Unauthorised access to the Medic8 database exposes patient health information (demographics, diagnoses, HIV status, billing), triggering PDPA Section 31 breach notification and reputational damage. | 2 | 5 | 10 | HIGH | AES-256-GCM encryption at rest (NFR-HC-002). TLS 1.2+ in transit (NFR-HC-003). 15-minute session timeout (NFR-HC-004). MFA for admin roles (NFR-HC-005). Tamper-proof audit trail (NFR-HC-001). 72-hour breach notification tooling (NFR-HC-008). Regular penetration testing. WAF on all public endpoints. | Peter | Designed |
| R-DS-002 | Cross-tenant data leakage. A bug or SQL injection bypasses tenant isolation, exposing Facility A's patient data to Facility B users. | 1 | 5 | 5 | MEDIUM | `facility_id` WHERE clause enforced at Repository base class (NFR-HC-015). Eloquent global scope as secondary defence. CI audit rule rejects raw SQL without tenant scope. Integration tests verify cross-tenant queries return zero results. Penetration test specifically targeting tenant boundaries. | Peter | Designed -- NFR-HC-015 |
| R-DS-003 | Insider threat: staff member accesses patient records without clinical justification. A staff member with legitimate system access views patient records for personal reasons (curiosity, family disputes, celebrity patients). | 3 | 4 | 12 | HIGH | Tamper-proof audit trail logs all access (NFR-HC-001). ABAC restricts sensitive records to authorised clinicians with active treatment relationships (NFR-HC-010). Break-the-glass access triggers mandatory post-access review and patient SMS notification (FR-RBAC-007). Anomalous access pattern detection (future enhancement). Monthly audit trail sampling by Facility Admin. | Peter | Designed |
| R-DS-004 | Mobile device theft with cached patient data. A healthcare worker's mobile device is stolen, exposing locally cached patient records from the offline queue. | 3 | 3 | 9 | MEDIUM | Encrypt local storage (IndexedDB/Room/SwiftData) with device-level encryption. Remote wipe capability via session revocation (FR-RBAC-004). Auto-lock after 5 minutes of device inactivity. Biometric authentication on mobile app. Limit offline cache to essential clinical data only. | Peter | Partially designed -- remote wipe designed; local encryption enforcement TBD |
| R-DS-005 | Unencrypted backup exposure. A database backup file stored without encryption is accessed by an unauthorised party, exposing patient data in plaintext. | 2 | 4 | 8 | MEDIUM | Encrypt all backup files with AES-256. Restrict backup storage access to Super Admin and automated backup service only. Backup verification testing uses anonymised restore, not production data (NFR-HC-020). Backup storage location access logged. | Peter | Designed -- NFR-HC-020 |

### 2.3 Regulatory Risks

| Risk ID | Risk Description | L | I | Score | Classification | Mitigation Strategy | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| R-RG-001 | UMDPC software registration required. If Medic8 is classified as a medical device under Uganda regulations because it supports prescribing, dispensing, and clinical decision support, it may require registration with UMDPC before commercial sale. | 3 | 4 | 12 | HIGH | Submit registration enquiry to UMDPC (Gap Analysis HIGH-003). Prepare software classification documentation. Budget for registration fees and compliance audits. Ensure CDS is documented as decision support, not decision making. | Peter | Open -- Gap Analysis HIGH-003 unresolved |
| R-RG-002 | PDPA enforcement action. The Personal Data Protection Office initiates enforcement action against Medic8 for non-compliance with consent, data subject rights, or breach notification requirements. | 2 | 4 | 8 | MEDIUM | Complete PDPA compliance documentation (this document). Engage a Uganda data protection lawyer (Gap Analysis HIGH-002). Register with PDPO. Conduct DPIA for all processing activities. Implement breach notification tooling (NFR-HC-008). Appoint a Data Protection Officer. | Peter | In progress -- compliance documentation drafted; legal review pending |
| R-RG-003 | NHIS API not published. Uganda National Health Insurance Scheme API documentation is not publicly available, blocking insurance claims integration. | 3 | 3 | 9 | MEDIUM | Register with NHIS as licensed healthcare software. Request API documentation. Design insurance module with configurable claims format (Phase 2). Implement manual claims export as interim solution. | Peter | Open -- NHIS engagement not yet initiated |
| R-RG-004 | HIV data disclosure violation. A system defect or misconfiguration exposes a patient's HIV status to a user without the required ABAC permission, violating the HIV/AIDS Prevention and Control Act 2014 Section 18. | 2 | 5 | 10 | HIGH | ABAC sensitive record access tier with 3-attribute check (NFR-HC-010, FR-RBAC-003). Break-the-glass audit with patient SMS notification (FR-RBAC-007). Integration tests verify "[Restricted]" display for unauthorised users. Penetration test targeting HIV data access paths. | Peter | Designed |

### 2.4 Technical Risks

| Risk ID | Risk Description | L | I | Score | Classification | Mitigation Strategy | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| R-TC-001 | Offline sync data corruption. After extended offline operation (approaching 72-hour queue limit), the sync process fails or produces corrupted records, leading to data loss or inconsistency. | 2 | 4 | 8 | MEDIUM | Field-level merge with conflict log (BR-DATA-003). Clinical field conflicts preserved side by side (not overwritten). Sync transaction integrity (all-or-nothing per record). Sync progress indicator with retry. Daily sync verification report. 72-hour queue limit with pre-limit warning at 48 hours. | Peter | Designed -- NFR-HC-013 |
| R-TC-002 | HL7 v2 analyser interface incompatibility. A laboratory analyser's HL7 v2 message format deviates from the expected structure, causing result auto-population failures or incorrect result mapping. | 3 | 3 | 9 | MEDIUM | Implement configurable HL7 v2 message parser with per-analyser mapping profiles (HLD 8.2 HL7 v2 Gateway). Validate sample ID before accepting results. Reject unrecognised message formats with notification to Lab Technician. Maintain a compatibility register of tested analyser models. | Peter | Designed -- FR-LAB-008, LLD 3.6 |
| R-TC-003 | FHIR R4 conformance failure. Medic8 FHIR resource responses fail validation against the official HL7 FHIR R4 schema, preventing interoperability with partner systems. | 2 | 3 | 6 | MEDIUM | Validate all 14 resource types against the official FHIR Validator during CI/CD build. Include HTML narrative fallback in every response. SMART on FHIR integration testing. Maintain FHIR conformance test suite as part of regression testing. | Peter | Designed -- NFR-HC-014 |
| R-TC-004 | Performance degradation at scale. As facility count and patient volume grow, API response times exceed the P95 500 ms threshold, degrading clinical workflow speed. | 3 | 3 | 9 | MEDIUM | Tenant-scoped database indexes on all query paths (ERD 13.1). Read replica for reporting queries. Horizontal scaling via container orchestration. Load testing at 50 concurrent users per facility. CDN for static assets. Database query plan monitoring. Performance regression testing in CI. | Peter | Designed |

### 2.5 Business Risks

| Risk ID | Risk Description | L | I | Score | Classification | Mitigation Strategy | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| R-BS-001 | Solo developer capacity. Peter is the sole developer. A single point of failure for all development, architecture, operations, and customer support. Extended illness, burnout, or competing priorities halt all progress. | 4 | 4 | 16 | CRITICAL | Maintain comprehensive documentation (SRS, HLD, LLD, ERD, API spec) to enable onboarding of additional developers. Use standard frameworks (Laravel, Jetpack Compose, SwiftUI) to access a wide hiring pool. Modular architecture enables parallel development. Prioritise Phase 1 MVP ruthlessly. Consider contracting a part-time co-developer for Phase 2. | Peter | Ongoing -- documentation investment is a mitigation strategy |
| R-BS-002 | ClinicMaster pivots to SaaS. ClinicMaster, the dominant Ugandan EMR, launches a cloud-hosted SaaS offering, directly competing with Medic8's value proposition. | 2 | 4 | 8 | MEDIUM | Differentiate on: multi-country support (regulatory profiles), offline-first architecture, FHIR R4 interoperability, modern mobile app, transparent pricing. Target underserved market segment (HC II/III clinics that ClinicMaster does not serve). Accelerate Phase 1 launch to establish market presence. | Peter | Monitoring |
| R-BS-003 | Customer churn from poor onboarding. Facilities abandon Medic8 during the onboarding period because the setup process is too complex or training is insufficient. | 3 | 3 | 9 | MEDIUM | 2-4 hour onboarding target (Quality Standards Section 7). Video-based training materials. Per-module activation (progressive complexity). Onboarding checklist with progress tracking. First-30-day customer success follow-up. | Peter | Designed |
| R-BS-004 | Mobile money API pricing changes. MTN MoMo or Airtel Money increase API transaction fees, reducing margin on billing module payments. | 3 | 2 | 6 | MEDIUM | Abstract payment gateway behind an adapter pattern (LLD 4.5.2 MobileMoneyService). Support multiple payment providers. Pass transaction fees to facility (transparent pricing model). Monitor operator API pricing announcements. | Peter | Designed |
| R-BS-005 | Drug interaction database licensing cost exceeds budget. Commercial drug interaction databases (DrugBank, Lexicomp) require licensing fees that exceed the bootstrapping budget, delaying clinical safety features. | 3 | 3 | 9 | MEDIUM | Evaluate open-source alternatives: RxNorm (NLM, free), OpenFDA drug interactions API (free). Evaluate Uganda NDA formulary as a locally maintained source. Start with a single-source database; expand coverage over time. Budget licensing cost as a recurring operational expense factored into subscription pricing. | Peter | Open -- Gap Analysis HIGH-001 |

### 2.6 Operational Risks

| Risk ID | Risk Description | L | I | Score | Classification | Mitigation Strategy | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| R-OP-001 | Extended power outage at facility exceeds 72-hour offline queue. A prolonged power outage (common in rural Uganda) exceeds the 72-hour offline queue capacity, causing potential data loss or queue overflow. | 2 | 4 | 8 | MEDIUM | 72-hour offline queue with 48-hour pre-limit warning (NFR-HC-013). Auto-save on every interaction (NFR-HC-016). Generator-aware sync (detect power restoration and sync immediately). Compress offline queue to maximise storage. Provide facility guidance on backup power (UPS, generator). | Peter | Designed |
| R-OP-002 | DHIS2 API downtime prevents HMIS submission. The Uganda eHMIS DHIS2 platform (hmis2.health.go.ug) is unavailable during the reporting window, preventing timely HMIS submission. | 3 | 3 | 9 | MEDIUM | Queue HMIS submissions when DHIS2 is unavailable. Retry automatically at configurable intervals. Generate offline HMIS reports in printable format for manual submission as fallback. Track submission status per reporting period (NFR-HC-009). Alert Facility Admin when submissions are overdue. | Peter | Designed |
| R-OP-003 | SMS gateway failure prevents appointment reminders. Africa's Talking or alternative SMS gateway experiences an outage, preventing appointment reminder delivery and breach notification SMS. | 3 | 2 | 6 | MEDIUM | Multi-channel notification: SMS, WhatsApp, push notification, email. Automatic fallback from SMS to alternative channel (NFR-HC-005 fallback pattern). Queue failed SMS for retry. Monitor SMS delivery rates. Secondary SMS provider as failover. | Peter | Designed |

---

## 3. Risk Heat Map

```
                              IMPACT
              1           2           3           4           5
            Negligible    Minor     Moderate     Major    Catastrophic
         +----------+----------+----------+----------+----------+
    5    |          |          |          |          |          |
 Almost  |          |          |          |          |          |
 Certain |          |          |          |          |          |
         +----------+----------+----------+----------+----------+
    4    |          |          |          | R-BS-001 | R-CS-005 |
 Likely  |          |          |          |          |          |
         |          |          |          |          |          |
         +----------+----------+----------+----------+----------+
    3    |          | R-BS-004 | R-BS-003 | R-DS-003 | R-CS-001 |
 Possible|          | R-OP-003 | R-TC-002 | R-RG-001 | R-CS-004 |
         |          |          | R-TC-004 |          |          |
         |          |          | R-OP-002 |          |          |
         |          |          | R-BS-005 |          |          |
         +----------+----------+----------+----------+----------+
    2    |          |          | R-TC-003 | R-DS-005 | R-CS-002 |
 Unlikely|          |          |          | R-TC-001 | R-CS-003 |
         |          |          |          | R-RG-002 | R-DS-001 |
         |          |          |          | R-OP-001 | R-RG-004 |
         +----------+----------+----------+----------+----------+
    1    |          |          | R-RG-003 | R-BS-002 | R-DS-002 |
 Rare    |          |          |          |          |          |
         |          |          |          |          |          |
         +----------+----------+----------+----------+----------+

LEGEND:
  Score 1-4   = LOW (accept and monitor)
  Score 5-9   = MEDIUM (mitigate and monitor quarterly)
  Score 10-14 = HIGH (mitigate urgently; monthly review)
  Score 15-25 = CRITICAL (immediate action; weekly review)
```

---

## 4. Risk Treatment Plan

### 4.1 CRITICAL Risks (Score >= 15)

#### R-CS-001: Drug Interaction Missed Due to Incomplete Database (Score: 15)

| Treatment Element | Detail |
|---|---|
| **Controls** | 1. Licence a commercially maintained drug interaction database. 2. Implement 4-tier alert system (Info/Warning/Serious/Fatal). 3. Clinical validation of alert thresholds by a practising clinician. 4. 30-day database update cycle. 5. Terms of Service disclaim clinical liability; CDS is decision support only. |
| **Residual risk after treatment** | Likelihood reduces from 3 to 2 (commercial database covers >95% of interactions). Impact remains 5. Residual score: 10 (HIGH -- cannot fully eliminate because no database covers 100% of interactions). |
| **Monitoring frequency** | Weekly during implementation; monthly post-deployment |
| **Escalation trigger** | Any adverse drug event attributed to a missed interaction. Database vendor discontinues service. |
| **Dependencies** | Gap Analysis HIGH-001 resolution. Budget allocation for licensing. |

#### R-CS-004: Wrong Patient Record Accessed (Score: 15)

| Treatment Element | Detail |
|---|---|
| **Controls** | 1. Patient identity confirmation prompt at encounter start (display photo, name, age, MRN). 2. Barcode/QR patient wristband scanning (Phase 2 IPD). 3. EMPI duplicate detection reduces identity confusion (FR-REG-009). 4. Unique colour-coded patient banners on clinical screens. 5. Patient age prominently displayed to reduce adult/paediatric confusion. |
| **Residual risk after treatment** | Likelihood reduces from 3 to 1 (identity confirmation + barcode). Impact remains 5. Residual score: 5 (MEDIUM). |
| **Monitoring frequency** | Monthly review of wrong-patient incident reports |
| **Escalation trigger** | Any clinical entry made against the wrong patient. |
| **Dependencies** | Patient photo capture capability. Barcode wristband infrastructure at facility. |

#### R-CS-005: CDS Alert Fatigue Leading to Override of Serious Alert (Score: 16)

| Treatment Element | Detail |
|---|---|
| **Controls** | 1. Limit Info-tier alerts to passive sidebar display (no modal interruption). 2. Track override rates per facility and per clinician. 3. Flag override rates exceeding 80% for Clinical Safety Officer review. 4. Clinician-validated alert thresholds to reduce false positives. 5. Monthly override rate reports. 6. Quarterly alert threshold review based on override data. |
| **Residual risk after treatment** | Likelihood reduces from 4 to 2 (reduced false positives + monitoring). Impact remains 4. Residual score: 8 (MEDIUM). |
| **Monitoring frequency** | Monthly override rate reporting; quarterly threshold review |
| **Escalation trigger** | Override rate exceeds 80% at any facility. Any Tier 3 or Tier 4 override that results in an adverse event. |
| **Dependencies** | Clinical Safety Officer designated per facility. Alert threshold validation by practising clinician. |

#### R-BS-001: Solo Developer Capacity (Score: 16)

| Treatment Element | Detail |
|---|---|
| **Controls** | 1. Comprehensive documentation (SRS, HLD, LLD, ERD, API spec, test plans) to enable rapid onboarding. 2. Standard frameworks (Laravel, Jetpack Compose, SwiftUI) for wide hiring pool. 3. Modular architecture enables parallel development by multiple developers. 4. Ruthless Phase 1 MVP prioritisation -- defer non-essential features. 5. CI/CD automation reduces manual operational burden. 6. Evaluate contracting a part-time co-developer for Phase 2. |
| **Residual risk after treatment** | Likelihood reduces from 4 to 3 (documentation + standards reduce dependency). Impact reduces from 4 to 3 (modular architecture enables partial progress). Residual score: 9 (MEDIUM). |
| **Monitoring frequency** | Monthly capacity review; weekly sprint velocity tracking |
| **Escalation trigger** | Sprint velocity drops below 50% of baseline for 2 consecutive sprints. Unplanned absence exceeding 2 weeks. |
| **Dependencies** | Budget for contractor engagement. Documentation maintained to a level sufficient for onboarding. |

### 4.2 HIGH Risks (Score 10-14)

#### R-CS-002: Paediatric Overdose from Dosing Calculation Error (Score: 10)

| Treatment Element | Detail |
|---|---|
| **Controls** | Weight-based dosing enforced for patients under 12 (BR-CLIN-006, NFR-HC-011). 10x deviation flag. Adult ceiling cap. No-weight block within 24 hours. |
| **Residual risk** | L:1, I:5. Residual score: 5 (MEDIUM). |
| **Monitoring** | Monthly review of dosing error flags and overrides |

#### R-CS-003: Critical Lab Value Not Escalated (Score: 10)

| Treatment Element | Detail |
|---|---|
| **Controls** | 60-second notification, 30-minute and 60-minute escalation cascade (BR-CLIN-003, NFR-HC-022). Multi-channel delivery. Audit trail timestamps. |
| **Residual risk** | L:1, I:5. Residual score: 5 (MEDIUM). |
| **Monitoring** | Monthly review of escalation compliance rates |

#### R-DS-001: Patient Data Breach (Score: 10)

| Treatment Element | Detail |
|---|---|
| **Controls** | AES-256-GCM at rest, TLS 1.2+ in transit, MFA, session timeout, audit trail, breach tooling, WAF, penetration testing. |
| **Residual risk** | L:1, I:5. Residual score: 5 (MEDIUM). |
| **Monitoring** | Quarterly penetration tests. Real-time intrusion detection. |

#### R-DS-003: Insider Threat (Score: 12)

| Treatment Element | Detail |
|---|---|
| **Controls** | Audit trail, ABAC, post-access review, override monitoring, anomalous pattern detection. |
| **Residual risk** | L:2, I:4. Residual score: 8 (MEDIUM). |
| **Monitoring** | Monthly audit trail sampling by Facility Admin |

#### R-RG-001: UMDPC Software Registration Required (Score: 12)

| Treatment Element | Detail |
|---|---|
| **Controls** | Submit registration enquiry. Prepare classification documentation. Document CDS as decision support. Budget for fees. |
| **Residual risk** | L:2, I:4. Residual score: 8 (MEDIUM) after enquiry submission. |
| **Monitoring** | Monthly follow-up with UMDPC until determination received |

#### R-RG-004: HIV Data Disclosure Violation (Score: 10)

| Treatment Element | Detail |
|---|---|
| **Controls** | ABAC 3-attribute check, break-the-glass audit with SMS, integration tests, penetration testing. |
| **Residual risk** | L:1, I:5. Residual score: 5 (MEDIUM). |
| **Monitoring** | Quarterly security audit of HIV data access paths |

---

## 5. Risk Review Schedule

### 5.1 Review Cadence

| Review Type | Frequency | Scope | Participants |
|---|---|---|---|
| HIGH/CRITICAL risk review | Monthly | All risks scored 10+ | Project Owner, Clinical Safety Officer (when designated), Lead Developer |
| Full risk register review | Quarterly | All risks across all categories | Project Owner, all stakeholders |
| Risk assessment refresh | Annually | Full risk assessment context, methodology, and register | Project Owner, independent reviewer |
| Post-incident review | Ad-hoc (within 48 hours) | Any clinical safety incident, data breach, or regulatory event | Project Owner, Clinical Safety Officer, affected facility staff |

### 5.2 Risk Review Checklist

Each review shall assess:

1. Has the likelihood or impact of any risk changed since the last review?
2. Have any new risks been identified?
3. Have any risk treatments been completed?
4. Are residual risk scores within acceptable thresholds?
5. Have any escalation triggers been activated?
6. Are risk owners still appropriate and engaged?

### 5.3 Risk Reporting

| Report | Audience | Frequency |
|---|---|---|
| Risk summary dashboard (CRITICAL + HIGH risks) | Project Owner | Monthly |
| Full risk register | All stakeholders | Quarterly |
| Clinical safety risk summary | Clinical Safety Officer, Facility Admin | Monthly |
| Regulatory compliance risk status | Data Protection Officer | Quarterly |

---

## Appendix A: Risk Register Summary (Sorted by Score)

| Rank | Risk ID | Category | Score | Classification | Description (abbreviated) |
|---|---|---|---|---|---|
| 1 | R-CS-005 | Clinical Safety | 16 | CRITICAL | CDS alert fatigue leading to serious override |
| 2 | R-BS-001 | Business | 16 | CRITICAL | Solo developer capacity |
| 3 | R-CS-001 | Clinical Safety | 15 | CRITICAL | Drug interaction missed (incomplete database) |
| 4 | R-CS-004 | Clinical Safety | 15 | CRITICAL | Wrong patient record accessed |
| 5 | R-DS-003 | Data Security | 12 | HIGH | Insider threat (access without justification) |
| 6 | R-RG-001 | Regulatory | 12 | HIGH | UMDPC software registration required |
| 7 | R-CS-002 | Clinical Safety | 10 | HIGH | Paediatric overdose from dosing error |
| 8 | R-CS-003 | Clinical Safety | 10 | HIGH | Critical lab value not escalated |
| 9 | R-DS-001 | Data Security | 10 | HIGH | Patient data breach |
| 10 | R-RG-004 | Regulatory | 10 | HIGH | HIV data disclosure violation |
| 11 | R-DS-004 | Data Security | 9 | MEDIUM | Mobile device theft with cached data |
| 12 | R-TC-002 | Technical | 9 | MEDIUM | HL7 v2 analyser incompatibility |
| 13 | R-TC-004 | Technical | 9 | MEDIUM | Performance degradation at scale |
| 14 | R-BS-003 | Business | 9 | MEDIUM | Customer churn from poor onboarding |
| 15 | R-OP-002 | Operational | 9 | MEDIUM | DHIS2 API downtime |
| 16 | R-RG-003 | Regulatory | 9 | MEDIUM | NHIS API not published |
| 17 | R-BS-005 | Business | 9 | MEDIUM | Drug interaction database licensing cost |
| 18 | R-DS-005 | Data Security | 8 | MEDIUM | Unencrypted backup exposure |
| 19 | R-TC-001 | Technical | 8 | MEDIUM | Offline sync data corruption |
| 20 | R-RG-002 | Regulatory | 8 | MEDIUM | PDPA enforcement action |
| 21 | R-OP-001 | Operational | 8 | MEDIUM | Extended power outage exceeds 72-hour queue |
| 22 | R-BS-002 | Business | 8 | MEDIUM | ClinicMaster pivots to SaaS |
| 23 | R-TC-003 | Technical | 6 | MEDIUM | FHIR R4 conformance failure |
| 24 | R-BS-004 | Business | 6 | MEDIUM | Mobile money API pricing changes |
| 25 | R-OP-003 | Operational | 6 | MEDIUM | SMS gateway failure |
| 26 | R-DS-002 | Data Security | 5 | MEDIUM | Cross-tenant data leakage |

---

## Appendix B: Gap Analysis Cross-Reference

The following unresolved gaps from `_context/gap-analysis.md` are directly linked to risk register entries:

| Gap ID | Gap Description | Risk ID(s) | Priority |
|---|---|---|---|
| HIGH-001 | Drug interaction database source not specified | R-CS-001, R-BS-005 | CRITICAL |
| HIGH-002 | PDPA healthcare data compliance not documented | R-RG-002 | HIGH |
| HIGH-003 | UMDPC software registration unknown | R-RG-001 | HIGH |
| HIGH-004 | CDS specificity not defined | R-CS-005, R-CS-001 | CRITICAL |
| HIGH-005 | HIV confidential record access not specified | R-RG-004 | HIGH |
| HIGH-006 | Emergency cross-facility access not specified | R-CS-004 | HIGH |
| HIGH-007 | HMIS form version management not specified | R-OP-002 | MEDIUM |
