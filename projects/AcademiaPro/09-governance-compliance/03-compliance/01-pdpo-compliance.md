# Uganda Data Protection and Privacy Act 2019 — Compliance Document

**Document ID:** GC-03-01
**Project:** Academia Pro
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Requires Legal Review Before School Sign-Up
**Gap Resolved:** HIGH-008
**Reference Act:** Uganda Data Protection and Privacy Act 2019 (PDPA 2019), Uganda Gazette No. 13, Vol. CXII, 25 February 2019.

---

## 1. Purpose

This document specifies Academia Pro's obligations under the Uganda Data Protection and Privacy Act 2019 (PDPA 2019), the implementing regulations, and international best-practice standards. It defines the controls that Chwezi Core Systems must implement before the first school signs a subscription agreement and before any student personal data is processed on the platform.

---

## 2. Roles and Responsibilities Under PDPA 2019

| Party | PDPA 2019 Role | Responsibility |
|---|---|---|
| Chwezi Core Systems Ltd | Data Processor | Operates the Academia Pro platform infrastructure. Processes personal data on behalf of schools. Must register with the Personal Data Protection Office (PDPO Uganda). |
| Each subscribing school | Data Controller | Determines the purposes for which student and staff personal data is processed. Responsible for obtaining lawful basis and data subject consent where required. |
| Students (and parents for minors) | Data Subjects | Hold rights of access, correction, and erasure under Part IV of the PDPA 2019. |

---

## 3. External Actions Required (Peter — Cannot Be Automated)

The following actions must be completed by Chwezi Core Systems before any school signs up:

| Action | Legal Basis | Urgency |
|---|---|---|
| Register as a Data Processor with the Personal Data Protection Office Uganda (pdpo.go.ug) | Section 17, PDPA 2019 | Before first school sign-up |
| Draft and publish Privacy Policy at `https://academiapro.com/privacy` | Section 13, PDPA 2019 | Before first school sign-up |
| Prepare and sign a Data Processing Agreement (DPA) with each school | Section 22, PDPA 2019 | Before each school's data is entered |
| Appoint a Data Protection Officer (DPO) or designate an existing staff member | Section 18, PDPA 2019 | Before first school sign-up |
| Conduct a Data Protection Impact Assessment (DPIA) for the platform | Section 19, PDPA 2019 | Before Phase 1 go-live |

---

## 4. Lawful Basis for Processing

All student personal data processed by Academia Pro schools must have a documented lawful basis. The applicable bases are:

| Data Category | Lawful Basis | Notes |
|---|---|---|
| Student enrollment records (name, DOB, class, admission number) | Contractual necessity (Section 8(1)(b)) | The school–parent/guardian enrollment contract constitutes the lawful basis. |
| National Identification Number (NIN) | Legal obligation (Section 8(1)(c)) | Required by Uganda's National Identification and Registration Act for age 16+. |
| MoES Learner Identification Number (LIN) | Legal obligation / legitimate interest | Required for EMIS reporting to MoES. |
| Guardian contact details | Legitimate interest (Section 8(1)(f)) | Used for fee reminders and emergency contact. |
| Fee payment records | Contractual necessity / legal obligation | Required for financial record-keeping under Uganda tax regulations. |
| Attendance records | Legitimate interest / legal obligation | Required for EMIS reporting and statutory attendance tracking. |
| Examination marks and grades | Legitimate interest / legal obligation | Required for UNEB registration and EMIS compliance. |
| Health records (Phase 7) | Explicit consent (Section 8(1)(a)) + Legal obligation | Special category data — explicit parental/guardian consent required per Section 9, PDPA 2019. |

---

## 5. Data Retention Policy

All data retention periods are implemented via a scheduled Laravel job (`PurgeExpiredDataJob`) that runs nightly.

| Data Category | Retention Period | Basis | Platform Action After Expiry |
|---|---|---|---|
| Active student enrollment records | Duration of enrollment + 7 years | Uganda education statutory requirement | Archived to cold storage; accessible to school owner on request |
| Departed student records | 7 years from departure date | Uganda education statutory requirement | Auto-purge after 7 years |
| Fee payment receipts | 7 years from payment date | Uganda Income Tax Act record-keeping requirement (Section 143) | Auto-purge after 7 years |
| Audit log entries | 7 years | Legal defensibility | Auto-purge after 7 years |
| Application records (in-platform school applications) | 2 years from creation | BR-APPLY-004 | Auto-purge after 2 years |
| Revoked authentication tokens | 90 days | Security best practice | Purged by nightly job |
| Import job error logs | 1 year | Operational necessity | Purged by nightly job |
| Breach incident records | 10 years | PDPA 2019 accountability obligations | Manual review required before purge |

---

## 6. Data Subject Rights Implementation

The following rights are guaranteed under Part IV of the PDPA 2019 and must be implemented in the platform.

### 6.1 Right of Access (Section 25)

Any data subject (student, parent, or guardian) may request a copy of all personal data held about them. The platform provides:

- A data export function accessible to the School Owner/Director role via **Settings → Data Export → Student Data Export**.
- The export produces a JSON file containing all `school_enrollments`, `attendance_records`, `exam_results`, and `fee_payments` records for the named student.
- Export requests are completed within 30 days (PDPA 2019 Section 25(2)).
- The export is logged in `audit_logs` with `action = STUDENT_DATA_EXPORTED`.

**API Endpoint:** `GET /students/{id}/data-export` — returns a pre-signed S3 download URL for the JSON export.

### 6.2 Right to Correction (Section 26)

Any role with the `students.edit` permission may correct student personal data. All corrections are logged in `audit_logs` with `before` and `after` snapshots.

Global identity fields (name, DOB, gender) may only be corrected by the school that created the global record (BR-STU-003). Other schools enrolling the same student must contact the originating school directly.

### 6.3 Right to Erasure (Section 27)

A school owner may initiate a student data erasure request. The platform implements a two-stage erasure:

**Stage 1 — Soft Delete (immediate):**
- Sets `school_enrollments.status = deleted` and anonymises personal identifiers in the school's enrollment record (first_name, last_name, date_of_birth replaced with placeholder values; guardian phone and NIN/LIN removed).
- The student's global identity record (`global_students`) is not altered at this stage, as other schools may hold an active enrollment for the same student.

**Stage 2 — Hard Delete (scheduled):**
- The nightly `PurgeExpiredDataJob` hard-deletes soft-deleted enrollment records after the 7-year retention period has passed.
- If the student has no active or soft-deleted enrollments at any school after Stage 1, the `global_students` record is soft-deleted immediately and hard-deleted after 7 years.

The erasure action is logged with `action = STUDENT_DATA_ERASED`. Receipts and audit logs are retained per their own retention schedule (legal obligation supersedes erasure right for financial and audit records — Section 27(3), PDPA 2019).

### 6.4 Right to Object (Section 29)

A data subject may object to processing for direct marketing purposes. Academia Pro does not use student data for marketing. Fee reminder SMS messages are a legitimate interest communication related to the enrollment contract and are not subject to the right to object. Schools may disable automated SMS reminders per their platform configuration.

---

## 7. Data Breach Notification Procedure

Under Section 20 of the PDPA 2019, a Data Controller (the school) must notify the PDPO Office within **72 hours** of becoming aware of a personal data breach that is likely to result in risk to the rights and freedoms of data subjects.

Chwezi Core Systems (as Data Processor) must:

1. Notify the affected school(s) **within 24 hours** of detecting or being notified of a breach.
2. Provide the school with: nature of the breach, categories and approximate number of data subjects affected, likely consequences, measures taken or proposed to address the breach.
3. Document the breach in an internal incident register, regardless of whether notification to the PDPO is required.
4. Cooperate with the school in preparing the PDPO notification.

The platform's incident register is maintained in `09-governance-compliance/05-incidents/`. Each incident record must contain: date detected, date notified to school, categories of data affected, root cause, remediation actions, and PDPO notification status.

---

## 8. Technical and Organisational Safeguards

### 8.1 Encryption

| Data State | Standard | Implementation |
|---|---|---|
| Data in transit | TLS 1.3 minimum | Enforced at load balancer; HTTP Strict Transport Security (HSTS) header applied |
| Data at rest (database) | AES-256 | MySQL Transparent Data Encryption (TDE) enabled on production RDS instance |
| Data at rest (file storage) | AES-256 | AWS S3 server-side encryption (SSE-S3) enabled on all buckets |
| Backup files | AES-256 | RDS automated backups inherit TDE; S3 backup bucket has SSE-S3 |

### 8.2 Access Controls

- Role-based access control (RBAC) limits data access to the minimum necessary per role (least privilege principle — see `02-requirements-engineering/03-stakeholder-analysis/01-rbac-matrix.md`).
- Super Admin cross-tenant access is logged per BR-MT-003.
- Health records (Phase 7) are restricted to nurse/doctor role, student, and linked parent (BR-DP-003).
- All authentication attempts, role changes, and data exports are logged in `audit_logs` (immutable — FR-AUD-001).

### 8.3 Data Minimisation

The platform collects only the fields required for the documented purposes. Optional fields (NIN, LIN, middle name, guardian phone) are not required at admission — they are collected progressively as needed for UNEB registration or EMIS reporting.

### 8.4 Multi-Tenancy Isolation

Each school's data is logically isolated by `tenant_id` enforced at the repository layer and via an Eloquent global scope (see `03-design-documentation/01-hld/02-security-architecture.md`). No school may access another school's data under any circumstances (BR-MT-001).

---

## 9. Data Processing Agreement (DPA) Summary

Every school that signs up for Academia Pro must execute a Data Processing Agreement with Chwezi Core Systems. The DPA establishes:

- The school as Data Controller and Chwezi Core Systems as Data Processor.
- The subject matter, duration, nature, and purpose of processing.
- The categories of personal data processed (student personal details, financial records, academic records).
- The categories of data subjects (students, parents/guardians, staff).
- Processor obligations: process data only on documented instructions from the Controller; ensure persons authorised to process data are bound by confidentiality; implement technical and organisational security measures; assist the Controller in responding to data subject rights requests; delete or return all personal data at the end of the service relationship.
- Sub-processor list: AWS (hosting and storage), Africa's Talking (SMS), SchoolPay (payments — Phase 2).

The DPA template is maintained at `09-governance-compliance/04-legal-templates/01-dpa-template.md`.

---

## 10. Privacy Notice (Summary for Platform)

The full Privacy Policy is published at `https://academiapro.com/privacy`. The following is the minimum content required before first school sign-up:

1. **Identity of the Data Controller:** [Each school's name and contact details] — displayed in the school's enrollment forms.
2. **Identity of the Data Processor:** Chwezi Core Systems Ltd, [registered address], DPO contact email.
3. **Data Collected:** Student personal details, guardian contacts, fee payment records, attendance records, examination results.
4. **Purpose of Processing:** School administration, EMIS government reporting, UNEB examination registration, fee billing, attendance monitoring.
5. **Lawful Basis:** Contractual necessity (enrollment contract), legal obligation (EMIS, UNEB, tax).
6. **Data Retention:** 7 years post-departure for student records; 7 years for financial records.
7. **Data Subject Rights:** Access, correction, erasure, objection — exercised through the school owner.
8. **Data Transfers:** Data is stored on AWS servers. Chwezi Core Systems will only host data on servers located within Uganda or the EAC region once Uganda-hosted cloud capacity is available at acceptable cost.
9. **Changes to Privacy Policy:** Schools will be notified by email 30 days before material changes take effect.

---

## 11. Special Category Data (Health Records — Phase 7)

Health records are classified as special category personal data under Section 9 of the PDPA 2019. The following additional controls apply from Phase 7 onwards:

- Explicit, per-student, per-data-type consent from the parent/guardian is required before any health record is created.
- Access is restricted to the nurse/doctor role, the student themselves, and the student's linked parent (BR-DP-003).
- No other role — including the School Owner — may access individual health records without an emergency override, which is separately logged.
- Health records are encrypted with a per-tenant encryption key (separate from the standard AES-256 database encryption) stored in AWS KMS.
- A separate DPIA is required before Phase 7 health records go live.

---

## 12. Compliance Checklist

| Control | Status | Owner | Due |
|---|---|---|---|
| Register with PDPO Uganda | 🔲 Not done | Peter | Before first school sign-up |
| Appoint Data Protection Officer | 🔲 Not done | Peter | Before first school sign-up |
| Complete Platform DPIA | 🔲 Not done | Peter + DPO | Before Phase 1 go-live |
| Publish Privacy Policy at `/privacy` | 🔲 Not done | Peter | Before first school sign-up |
| Finalise DPA Template | 🔲 Not done | Peter + Legal | Before first school sign-up |
| Implement TLS 1.3 on production | 🔲 Development | Backend team | Before Phase 1 go-live |
| Enable MySQL TDE on production RDS | 🔲 Development | DevOps | Before Phase 1 go-live |
| Enable S3 SSE-S3 on all buckets | 🔲 Development | DevOps | Before Phase 1 go-live |
| Implement `/students/{id}/data-export` API endpoint | 🔲 Development | Backend team | Phase 1 |
| Implement student soft-delete erasure pathway | 🔲 Development | Backend team | Phase 1 |
| Implement `PurgeExpiredDataJob` | 🔲 Development | Backend team | Phase 1 |
| Set up breach incident register | 🔲 Not done | Peter | Before first school sign-up |
| Train school onboarding staff on PDPA obligations | 🔲 Not done | Peter | Before first school sign-up |
| Phase 7 — Obtain per-student health consent | 🔲 Phase 7 | Backend team | Before Phase 7 go-live |
| Phase 7 — AWS KMS per-tenant health data key | 🔲 Phase 7 | DevOps | Before Phase 7 go-live |
| Phase 7 — Health data DPIA | 🔲 Phase 7 | Peter + DPO | Before Phase 7 go-live |


---

## AI Module — DPPA 2019 Compliance Addendum

This section addresses DPPA 2019 obligations introduced by the AI Module add-on. All processing described below is conditional on the tenant activating the AI module (`tenant_ai_modules.status = 'active'`). Tenants without the AI module have no additional DPPA exposure beyond the existing compliance framework.

### AI Data Flows Subject to DPPA 2019

The AI Module introduces one new category of processing: transmitting school data (in anonymised or aggregated form) to an external AI API provider (Anthropic / Claude API, hosted outside Uganda). This transmission is governed by DPPA 2019 Section 19 (international data transfers) and Section 5 (lawful basis).

| Data Flow | Personal Data Involved | DPPA Classification | Control Applied |
|---|---|---|---|
| At-risk student scoring prompt | Attendance counts, mark averages — referenced by `student_uid` only, no name | Pseudonymous (not directly identifying without the database join) | `PIIScrubber` enforces UID-only transmission; names never sent |
| Fee default prediction prompt | Payment timing history — referenced by `student_uid` only | Special personal data (financial information — DPPA 2019 Schedule) | UID-only transmission; `PIIScrubber` enforced; `pii_scrubbed = 1` required in `ai_audit_log` |
| Parent sentiment analysis | Parent feedback text — names stripped before dispatch | Personal data (text may contain identifying context) | `PIIScrubber` strips names matched against `guardians` table before dispatch |
| Weekly owner briefing | Aggregated statistics only (no individual identifiers) | Not personal data (aggregated, anonymised) | No scrubbing required; verified by pre-dispatch assertion |
| Report card comment generation | Student first name (for personalisation), mark summary, attendance | Personal data (student academic record) | Transmitted under legitimate interest for educational purposes; student names are included only in the per-student comment generation call, not in batch contexts |

### Lawful Basis for AI Processing

| Processing Activity | Lawful Basis (DPPA 2019 Section 5) | Documentation Required |
|---|---|---|
| At-risk student scoring | Legitimate interests — improving student academic outcomes (educational purpose) | Disclosed in school's privacy notice to parents under DPPA Section 12 |
| Fee default prediction | Legitimate interests — financial management of the school (operational purpose) | Disclosed in school's privacy notice |
| Parent sentiment analysis | Legitimate interests — improving school services based on parent feedback | Feedback form includes disclosure: "Responses may be analysed using AI tools" |
| Report card comment generation | Legitimate interests — improving quality and consistency of teacher communications | Disclosed in school's privacy notice |
| Weekly owner briefing | Not applicable — aggregated data only, no personal data transmitted | No consent or disclosure required |

### International Transfer Controls (DPPA 2019 Section 19)

The AI Module transmits pseudonymised data to the Anthropic Claude API, which is hosted outside Uganda. DPPA 2019 Section 19 requires that international transfers meet one of the permitted grounds:

- **Adequacy decision:** The Ugandan PDPO has not yet issued an adequacy decision for Anthropic's jurisdiction. This ground is not applicable at the time of writing.
- **Appropriate safeguards:** Chwezi Core Systems shall execute a Data Processing Agreement (DPA) with Anthropic before activating the AI module for any production tenant. The DPA must include: data minimisation obligations, prohibition on model training on customer data, deletion timelines, and incident notification within 24 hours.
- **Contractual clause:** The Academia Pro Terms of Service (Section on AI Module) must inform school owners that pseudonymised student data is processed by an international AI provider, and obtain explicit written acknowledgement before activating the AI module for the school.

**Action items before AI module goes live:**
- [ ] Execute DPA with Anthropic — Chwezi Core Systems legal obligation
- [ ] Add AI data transfer disclosure to Academia Pro Terms of Service
- [ ] Add "AI features" section to the school-facing Privacy Notice template
- [ ] Obtain written school owner acknowledgement during AI module activation flow

### AI Audit Log as DPPA Evidence

The `ai_audit_log` table (Section 4.8.8 of the ERD) provides DPPA-compliant evidence that:
1. Every AI API call was preceded by PII scrubbing (`pii_scrubbed = 1`).
2. No plaintext prompt content was persisted (SHA-256 hash only — data minimisation, DPPA Section 7).
3. The outcome of every AI call is recorded for audit purposes.

The `ai_audit_log` is retained for 7 years (AI-NFR-008) and is immutable (append-only, MySQL trigger enforced). The PDPO may request access to this log under DPPA 2019 Section 26 (supervisory authority powers).

### DPPA Fail Tags for AI Module

In addition to the existing DPPA fail tags, the following apply to AI module pull requests:

- `[DPPA-FAIL: AI prompt contains NIN]` — a Uganda NIN pattern was found in a prompt string without being scrubbed.
- `[DPPA-FAIL: AI prompt contains parent phone]` — a Ugandan mobile number found in a prompt without scrubbing.
- `[DPPA-FAIL: financial data sent to AI without anonymisation]` — fee payment records transmitted to the AI API without UID-only anonymisation.
- `[DPPA-FAIL: no international transfer disclosure]` — AI module activated for a tenant without written acknowledgement of international data transfer.
- `[DPPA-FAIL: pii_scrubbed = 0 in ai_audit_log]` — an AI call was recorded with `pii_scrubbed = 0`, indicating the scrubber was bypassed.

### DPIA Trigger Assessment — AI Module

**[DPIA-REQUIRED: At-scale AI processing of student academic and financial records]**

The AI module processes data for potentially thousands of students across hundreds of schools. The combination of: (a) pseudonymised student data, (b) financial information (special personal data), and (c) international transfer to an AI provider meets the DPPA 2019 threshold for a mandatory Data Protection Impact Assessment (DPIA) under Regulation 12.

A DPIA for the AI Module must be completed and reviewed by the Data Protection Officer before the AI module is commercially launched. The `dpia-generator` skill shall be invoked to produce the DPIA document for the AI Module processing activity.

**Action item:** `[DPIA-REQUIRED: AI Module — international transfer of pseudonymised student and financial data]` — invoke `dpia-generator` skill before Phase 2 AI module go-live.
