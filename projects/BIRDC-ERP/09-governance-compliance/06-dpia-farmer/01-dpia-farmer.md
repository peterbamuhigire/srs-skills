---
title: "Data Protection Impact Assessment — Farmer Data Processing"
subtitle: "BIRDC ERP System — Collection and Processing of Personal and Special Personal Data for 6,440+ Cooperative Farmers"
document_ref: "BIRDC-ERP-DPIA-001"
regulation: "Regulation 12, Data Protection and Privacy Regulations 2021"
prepared_by: "Peter Bamuhigire, ICT Consultant (techguypeter.com)"
prepared_for: "PIBID / BIRDC, Nyaruzinga, Bushenyi, Uganda"
version: "1.0 DRAFT"
date: "2026-04-05"
---

# Data Protection Impact Assessment — Farmer Data Processing

BIRDC ERP System — Regulation 12, Data Protection and Privacy Regulations 2021

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com)
**Prepared for:** PIBID / BIRDC, Nyaruzinga, Bushenyi, Uganda
**Document Reference:** BIRDC-ERP-DPIA-001
**Classification:** Confidential — Internal Compliance Document

---

## Section 1 — Processing Operation Description

### 1.1 Operation Name and Purpose

**Operation:** Collection and processing of personal and special personal data for 6,440+ cooperative farmers during farmer registration, farm GPS mapping, delivery recording, and mobile money payment disbursement.

**Purpose:** To register cooperative farmers in the BIRDC ERP system, verify their identity, record banana deliveries against their profile, and disburse payments via MTN MoMo and Airtel Money in compliance with BIRDC's cooperative procurement obligations.

**Modules:** F-010 (Farmer and Cooperative Management), F-009 (Procurement and Purchasing — 5-Stage Cooperative Procurement), F-007 (Accounts Payable — farmer payment), Farmer Delivery App (Android).

---

### 1.2 Data Controller and DPO

| Role | Details |
|---|---|
| Data Controller | BIRDC / PIBID, Nyaruzinga, Bushenyi, Uganda |
| Data Protection Officer | [CONTEXT-GAP: GAP-004 — DPO not yet designated by BIRDC Director] |
| PDPO Registration Number | [CONTEXT-GAP: BIRDC not yet registered with PDPO at NITA-U] |
| ICT Consultant | Peter Bamuhigire, techguypeter.com |

---

### 1.3 Categories of Data Subjects

- **Count:** 6,440+ smallholder cooperative farmers registered in the BIRDC/PIBID cooperative network.
- **Demographics:** Predominantly rural smallholder farmers, Bushenyi and surrounding districts, Western Uganda.
- **Digital literacy:** Limited. Most farmers interact with the system only through the Collections Officer (Patrick persona) using the Farmer Delivery App. Farmers receive SMS payment confirmations.
- **Vulnerability factors:** Rural location, limited formal education, potential language barrier (Runyankore/Rukiga first language), and some farmers may be under 18 years of age (family farms where minors assist with or inherit cooperative membership).
- **Language:** Primary language Runyankore/Rukiga; consent notices must be provided in both English and Runyankore/Rukiga.

---

### 1.4 Data Categories Collected

| Field | Tier | Section 9 Category | Volume |
|---|---|---|---|
| Mobile money number (MTN / Airtel) | **S** | Financial information — Section 9(1) | 6,440+ |
| Payment amounts per farmer | **S** | Financial information — Section 9(1) | 6,440+ (per delivery cycle) |
| National Identification Number (NIN) | P | Identification number — Section 2(c) | 6,440+ |
| GPS farm coordinates | P | Location / identity data — Section 2 | 6,440+ |
| Farmer photograph | P | Identity data — Section 2 | 6,440+ |
| Full name | P | Identification — Section 2 | 6,440+ |
| Contact phone number | P | Identification — Section 2 | 6,440+ |
| Cooperative membership number | P | Identification — Section 2 | 6,440+ |
| Farmer age / date of birth | P | Age — Section 2; Section 8 children safeguard | 6,440+ |
| Delivery weights (batch, dates, quality grades) | N | Cannot identify person in isolation | Per delivery cycle |

---

### 1.5 Processing Activities

1. **Collection:** Collections Officer (Patrick) collects farmer data at cooperative collection points using the Farmer Delivery App (offline-capable Android app). Data is entered manually or captured via GPS sensor and camera.
2. **Storage:** Data syncs to BIRDC ERP server at Nyaruzinga when connectivity is available. All S-tier and P-tier fields encrypted at rest (AES-256-GCM for S-tier; AES-128-GCM for P-tier).
3. **Use:** Data is used for identity verification, delivery recording, payment calculation, and PPDA-compliant audit trail.
4. **Disclosure:** Mobile money numbers and payment amounts are transmitted to MTN MoMo and/or Airtel Money APIs for bulk payment disbursement. Phone numbers transmitted to Africa's Talking for SMS payment confirmation.
5. **Retention:** Retained for duration of cooperative membership + 7 years per Income Tax Act Cap 340.
6. **Destruction:** De-identified at retention expiry per FR-DPPA-020.

---

### 1.6 Lawful Basis

| Data Category | Lawful Basis (Section 7) |
|---|---|
| Personal identification data (name, NIN, phone, photo) | Consent + legal obligation (PPDA cooperative procurement audit requirements) |
| GPS farm coordinates | Consent + performance of contract (traceability obligation) |
| Mobile money number (S-tier) | Consent + legal obligation (cooperative payment obligation; Income Tax Act payment records) |
| Payment amounts (S-tier) | Legal obligation (Income Tax Act Cap 340 — 7-year financial records; PPDA audit trail) |
| Farmer age | Consent + Section 8 children safeguard |

---

### 1.7 Data Processors Involved

| Processor | Data Transmitted | Written Contract |
|---|---|---|
| MTN Uganda (MTN MoMo API) | Farmer mobile money numbers, payment amounts | [CONTEXT-GAP: GAP-002 — contract cannot be executed until API credentials obtained] |
| Airtel Uganda (Airtel Money API) | Farmer mobile money numbers, payment amounts | [CONTEXT-GAP: GAP-003 — contract cannot be executed until API credentials obtained] |
| Africa's Talking (SMS API) | Farmer phone numbers, SMS content (payment confirmation) | [CONTEXT-GAP: GAP-004 — contract template pending legal review] |

Per Section 21 DPPA 2019, no data shall be transmitted to these processors until written contracts are executed.

---

### 1.8 Cross-Border Transfer

All BIRDC ERP data is processed and stored on-premise on BIRDC's own servers at Nyaruzinga, Bushenyi, Uganda. No data is stored or processed outside Uganda. Design Covenant DC-006 (Data Sovereignty) prohibits cloud storage. No cross-border transfer adequacy assessment is required.

---

## Section 2 — Necessity and Proportionality Assessment

### 2.1 Necessity

| Field | Necessary? | Justification |
|---|---|---|
| NIN | Yes — cannot omit | Required for NIRA identity verification and PPDA-compliant farmer payment audit trail. URA requires NIN on payment records for tax purposes. |
| GPS farm coordinates | Partially — review scope | A single GPS centroid point is sufficient for farm verification and traceability. Full polygon GPS mapping of each farm plot may exceed what is strictly necessary. *Data minimisation recommendation: collect centroid point only; defer polygon mapping to Phase 3 extension justified by additional traceability need.* |
| Farmer photograph | Yes — with time limit | Required for identity verification at collection point. *Data minimisation recommendation: consider whether photograph may be deleted after NIN validation is confirmed, rather than retaining for full 7-year period.* |
| Mobile money number (S-tier) | Yes — cannot omit | Required for payment disbursement. No alternative payment mechanism is available at scale for rural farmers. |
| Payment amounts (S-tier) | Yes — cannot omit | Required for Income Tax Act 7-year payment record retention and PPDA cooperative procurement audit trail. |
| Contact phone | Yes | Required for SMS payment confirmation and farmer communication. |
| Delivery weights and grades | Yes | N-tier — no personal data concern. Required for PPDA cooperative procurement and mass balance. |

### 2.2 Proportionality

The scale of data collection (6,440+ farmers, S-tier financial data, NIN, GPS, photo) is proportionate to the operational purpose: paying cooperative farmers for banana deliveries at industrial scale while maintaining PPDA and Income Tax Act compliance. The same data is routinely collected by Uganda's cooperative sector for government-linked agro-processors.

### 2.3 Data Minimisation Flags

- **GPS polygon vs. centroid:** Collecting the full polygon boundary of each farm plot collects more location data than strictly necessary for delivery verification. Defer polygon detail unless required for traceability certification. Flag: data minimisation principle (Section 3 DPPA).
- **Photograph retention:** Retaining the photograph for 7 years after NIN is validated may exceed necessity. Explore whether photograph can be deleted after identity verification and NIN confirmed, subject to legal counsel opinion. [CONTEXT-GAP: GAP-004]

### 2.4 Purpose Limitation

Farmer data shall not be used for any purpose other than cooperative procurement management and payment. Secondary use (e.g., marketing, third-party research) is prohibited without separate consent. Statistical use of anonymised aggregate data (total deliveries by cooperative, average price per grade) is permitted under Section 17 provided identity is not revealed.

### 2.5 Storage Limitation

Retention period: duration of cooperative membership + 7 years from last payment (Income Tax Act). De-identification method per FR-DPPA-020. Automated DPO expiry alert at 90 days before expiry per FR-DPPA-019.

---

## Section 3 — Risk Assessment

**Risk Rating Matrix:**

| Likelihood | Low Impact | Medium Impact | High Impact |
|---|---|---|---|
| Unlikely | Low | Low | Medium |
| Possible | Low | Medium | High |
| Likely | Medium | High | Critical |

**Risk Register:**

| # | Risk | Description | Likelihood | Impact | Rating |
|---|---|---|---|---|---|
| R-1 | Financial data breach | Farmer mobile money numbers (S-tier) accessed by unauthorised staff or via system vulnerability | Possible | High | **HIGH** |
| R-2 | GPS misuse | Farm GPS coordinates enable physical targeting of rural farmers (theft, extortion) | Unlikely | High | **MEDIUM** |
| R-3 | NIN breach | Mass NIN exposure (6,440+) enables large-scale identity fraud | Possible | High | **HIGH** |
| R-4 | No valid consent | Farmer data collected without a valid, informed consent process — current paper process has no digital record | Possible | High | **HIGH** |
| R-5 | Third-party data sharing | MTN MoMo / Airtel Money retains farmer payment data beyond the scope of the payment instruction | Likely | Medium | **HIGH** |
| R-6 | Breach not immediately notified | PDPO notification delayed due to lack of breach detection workflow or unclear DPO responsibility | Possible | High | **HIGH** |
| R-7 | Retention not enforced | Historical farmer data not de-identified at 7-year expiry — ongoing liability | Possible | Medium | **MEDIUM** |
| R-8 | Child farmer without guardian consent | Farmers under 18 registered without parental or guardian consent | Possible | Medium | **MEDIUM** |
| R-9 | Cross-border transfer | Cloud backup or remote access transfers farmer data outside Uganda without adequacy or consent | Unlikely | High | **LOW** |
| R-10 | Rights not fulfilled | Farmer objection or deletion requests not responded to within 30 calendar days | Possible | Medium | **MEDIUM** |

---

## Section 4 — Control Measures

Controls for all risks rated MEDIUM and above:

| Risk | Control Measure | FR / NFR Reference | Owner | Status |
|---|---|---|---|---|
| R-1 | AES-256-GCM encryption of all S-tier fields (mobile money numbers, payment amounts) at rest; role restriction to Finance Director, Payroll Officer, IT Administrator; every S-tier access logged with user ID and timestamp | NFR-DPPA-001, NFR-DPPA-004, NFR-DPPA-005 | Dev Lead | Planned |
| R-2 | GPS farm coordinates stored AES-128-GCM encrypted; access restricted to Procurement Manager, Finance Director, IT Administrator; GPS data not displayed on any public-facing screen or report | NFR-DPPA-002, NFR-DPPA-004 | Dev Lead | Planned |
| R-3 | NIN stored AES-128-GCM encrypted; displayed masked in all UI (last 4 digits only); NIRA validation performed via API without storing NIRA response beyond confirmation flag; access restricted to named roles | NFR-DPPA-002, NFR-DPPA-004 | Dev Lead | Planned |
| R-4 | Farmer consent notice (English + Runyankore/Rukiga) displayed before any data entry field is enabled in Farmer Delivery App; consent record persisted to `tbl_consent_register` before farmer profile is saved; printable consent form generated at completion | FR-DPPA-001, FR-DPPA-002, FR-DPPA-009 | Dev Lead | Planned |
| R-5 | Written data processor contracts with MTN MoMo and Airtel Money required before any S-tier data is transmitted; system blocks payment run if no executed processor contract is recorded; contract clauses must prohibit secondary use and require deletion on contract end | NFR-DPPA-007, NFR-DPPA-008 | BIRDC Legal / Peter | [CONTEXT-GAP: GAP-002/003 — contracts pending API credentials] |
| R-6 | Breach detection triggers generate immediate DPO dashboard alert; DPO confirms breach classification; system generates PDPO notification form pre-populated with all Section 23 required fields; `notified_pdpo_at` timestamp recorded; form accessible in 3 clicks | FR-DPPA-023, FR-DPPA-024 | Dev Lead | Planned |
| R-7 | System calculates retention expiry for each farmer record; DPO alert fired at 90 days before expiry; de-identification executed per FR-DPPA-020 on DPO confirmation; destruction audit log created | FR-DPPA-019, FR-DPPA-020, FR-DPPA-021 | Dev Lead | Planned |
| R-8 | Date of birth field in farmer registration; system calculates age; if age < 18: Section 8 guardian consent alert displayed; guardian name, relationship, and consent timestamp required before registration proceeds | FR-DPPA-004, FR-DPPA-005 | Dev Lead | Planned |
| R-9 | On-premise only deployment confirmed (DC-006 Data Sovereignty); no cloud backup outside Uganda; server location at Nyaruzinga documented; IT Administrator policy: remote access only via VPN to BIRDC network | NFR-DPPA-003 (TLS 1.3 for transit) | BIRDC IT | Pending confirmation |
| R-10 | Data subject rights request log in `tbl_data_subject_requests`; 30-calendar-day SLA enforced; DPO dashboard displays overdue requests; written rejection with reasons stored if unable to comply | FR-DPPA-014, FR-DPPA-018 | Dev Lead | Planned |

---

## Section 5 — Residual Risk Assessment

After implementation of all controls:

| Risk | Pre-Control Rating | Residual Rating | Residual Rationale |
|---|---|---|---|
| R-1 Financial data breach | HIGH | LOW | AES-256-GCM + RBAC + audit log provides strong technical control |
| R-2 GPS misuse | MEDIUM | LOW | Encryption + access restriction reduces physical targeting risk |
| R-3 NIN breach | HIGH | LOW | Encryption + masking + NIRA API (no bulk NIN storage in plaintext) |
| R-4 No consent | HIGH | **MEDIUM** | Consent workflow planned but not yet implemented or legally reviewed — residual risk until FR-DPPA-001/002/009 are built and consent form approved by legal counsel |
| R-5 Third-party sharing | HIGH | **MEDIUM** | Data processor contracts planned but cannot be executed until API credentials obtained — residual risk pending GAP-002/003 resolution |
| R-6 Breach notification | HIGH | LOW | Automated breach workflow with immediate PDPO notification addresses risk once DPO is designated |
| R-7 Retention not enforced | MEDIUM | LOW | Automated retention expiry and de-identification system addresses risk |
| R-8 Child farmer | MEDIUM | LOW | Age verification and guardian consent workflow in registration addresses risk |
| R-9 Cross-border | LOW | LOW | On-premise only deployment confirmed |
| R-10 Rights not fulfilled | MEDIUM | LOW | 30-day DPO dashboard alert and rights request log addresses risk |

**Overall residual risk: MEDIUM** — driven by R-4 (consent form pending legal review) and R-5 (data processor contracts pending API credentials). Both risks are expected to reduce to LOW upon completion of the 4 recommended actions in the DPPA Compliance Annex (Section 11.4).

PDPO consultation is not mandated at this residual risk level under Regulation 12. However, PDPO consultation is **recommended** given the scale of processing (6,440+ farmers, S-tier financial data). BIRDC should notify PDPO of these DPIA findings as part of its mandatory PDPO registration.

---

## Section 6 — PDPO Consultation Determination

**Residual risk level:** MEDIUM (after controls).

**Determination:** PDPO prior consultation is not mandated under Regulation 12 at MEDIUM residual risk. Regulation 12 requires prior consultation only when residual risk remains HIGH or CRITICAL after controls.

**Recommendation:** PDPO consultation is strongly recommended, not merely because of the residual risk level, but because of:

1. The scale of processing: 6,440+ rural farmers with limited digital literacy.
2. The nature of data: S-tier financial information (mobile money numbers and payment amounts) for a vulnerable population.
3. BIRDC's public accountability as a government-linked entity funded by UGX 200 billion in parliamentary appropriations.
4. The replicability intent (DC-007): this system will be a template for other Uganda government agro-processors. Establishing PDPO cooperation early creates a compliance precedent.

**Action:** BIRDC should submit the DPIA findings to the PDPO as part of the mandatory PDPO registration process. Request a PDPO consultation meeting before Phase 3 go-live.

---

## Section 7 — Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Data Protection Officer | [CONTEXT-GAP: GAP-004 — DPO not yet designated] | | |
| ICT Consultant / System Architect | Peter Bamuhigire, ICT Consultant, techguypeter.com | 2026-04-05 | |
| Finance Director (Client Authorising Officer) | [Finance Director to sign before Phase 3 go-live — BIRDC Finance] | | |

---

*This DPIA was prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com), from BIRDC ERP context files as of 2026-04-05. It is a draft compliance document, not legal advice. Qualified Uganda DPPA 2019 legal counsel must review this document before Phase 3 go-live.* [CONTEXT-GAP: GAP-004]
