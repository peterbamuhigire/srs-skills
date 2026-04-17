# Section 2: Uganda Data Protection and Privacy Act 2019

*This section is a Conditional Compliance section. The system architecture implements the technical controls described below; however, the lawful basis determination and data subject rights procedures require legal review by counsel familiar with the DPPA 2019 before go-live. See [CONTEXT-GAP: GAP-004].*

## 2.1 Personal Data Collected by the System

The BIRDC ERP system collects and processes the following categories of personal data:

### 2.1.1 Farmer Personal Data

| Data Element | Module | Sensitivity | Retention Period |
|---|---|---|---|
| Full name | F-010 Farmer Management | Standard | Duration of cooperative membership + 7 years |
| National Identification Number (NIN) | F-010, F-009 | Sensitive | Duration of cooperative membership + 7 years |
| GPS farm coordinates (farm polygon) | F-010 | Standard — geolocation | Duration of cooperative membership + 7 years |
| Photo | F-010 | Biometric-adjacent | Duration of cooperative membership + 7 years |
| Mobile money number | F-010, F-007 | Financial | Duration of cooperative membership + 7 years |
| Contact phone number | F-010 | Standard | Duration of cooperative membership + 7 years |
| Delivery history and payment records | F-009, F-007 | Financial | 7 years per Income Tax Act |

**Lawful basis:** [CONTEXT-GAP: GAP-004] — To be confirmed by legal counsel. Likely candidates: consent (signed farmer registration form) and/or legitimate interest (necessary for cooperative procurement and payment). The Finance Director must confirm the lawful basis before farmer registration module goes live.

### 2.1.2 Employee Personal Data

| Data Element | Module | Sensitivity | Retention Period |
|---|---|---|---|
| Full name, contact, address | F-013 HR | Standard | Duration of employment + 7 years |
| National Identification Number (NIN) | F-013 HR | Sensitive | Duration of employment + 7 years |
| Contract type, salary, job grade | F-013, F-014 Payroll | Financial | Duration of employment + 7 years (Income Tax Act) |
| Biometric fingerprint data | F-013 (ZKTeco device) | Biometric — highly sensitive | Duration of employment; delete on exit |
| Leave records, disciplinary records | F-013 HR | HR sensitive | Duration of employment + 7 years |
| Payroll records, payslips | F-014 Payroll | Financial | 7 years per Income Tax Act |
| Bank account details | F-014 Payroll | Financial | Duration of employment + 7 years |

**Lawful basis:** Employment contract and legal obligation (Income Tax Act, NSSF Act) provide lawful basis for most employee data. Biometric fingerprint data requires explicit consent or a specific legal basis under DPPA 2019. [CONTEXT-GAP: GAP-004]

## 2.2 Technical Controls Implemented by the System

### 2.2.1 Encryption at Rest

FR-FAR-001 mandates that all farmer PII fields (NIN, GPS coordinates, mobile money number, and photo) are encrypted at rest in the database. The same standard applies to employee NIN and bank account details in the HR and Payroll modules. The encryption mechanism shall use AES-256 symmetric encryption with keys stored separately from the encrypted data fields.

### 2.2.2 Access Controls

FR-FAR-009 restricts access to farmer PII to authorised Procurement and Finance roles only. This is enforced through the 8-layer authorisation model (FR-SYS-001), which controls access at the API endpoint level — not just the UI level. A user who does not have the Procurement or Finance role cannot retrieve farmer NIN, GPS coordinates, or mobile money data through any system interface.

Employee biometric data is not stored in the application database; it resides on the ZKTeco device only. The system receives only attendance timestamps (in/out times) from the device, not raw fingerprint templates.

### 2.2.3 Audit Trail for Personal Data Access

Every access to a farmer or employee profile record is logged in the system audit trail (FR-SYS-003) with the user identity, action, and timestamp. The Finance Director or IT Administrator can query all access events for any specific data subject's record at any time.

### 2.2.4 Data Retention Enforcement

FR-SYS-004 blocks automated deletion of any record within the 7-year retention period. Data subject deletion requests during the retention period must be evaluated against the Income Tax Act and NSSF Act obligations, which require retention of financial and employment records for 7 years regardless of a deletion request. [CONTEXT-GAP: GAP-004 — legal advice required on how to handle a farmer's deletion request where the financial records must be retained.]

### 2.2.5 Data Sovereignty

FR-SYS-006 mandates that all BIRDC data is stored on BIRDC's own servers at Nyaruzinga, Bushenyi. No personal data is transmitted to or stored on external SaaS vendor infrastructure. This satisfies the DPPA 2019 data localisation requirement for Ugandan personal data.

## 2.3 Data Subject Rights

The Uganda Data Protection and Privacy Act 2019 grants data subjects the following rights. The table records how the system supports each right.

| Right | DPPA 2019 Provision | System Support |
|---|---|---|
| Right to access | S.27 — data subject may request a copy of their data | IT Administrator can generate a farmer or employee data export from the profile screen; HR Self-Service App allows employees to view their own data |
| Right to correction | S.28 — data subject may request correction of inaccurate data | Any authorised user can update farmer and employee profile fields; all changes are logged in the audit trail with previous and new values |
| Right to deletion | S.29 — data subject may request deletion | System supports deactivation of farmer and employee accounts; full deletion of financial records is constrained by 7-year statutory retention; legal advice required on the correct procedure for deletion requests [CONTEXT-GAP: GAP-004] |
| Right to object to processing | S.30 | No automated processing for profiling or marketing; all processing is operational (cooperative procurement, payroll); objection procedure requires legal guidance [CONTEXT-GAP: GAP-004] |
| Right to data portability | S.31 | Farmer delivery history and employee payslips are exportable in PDF and CSV formats |

## 2.4 DPPA Compliance Summary

The system implements all technical privacy controls required by the DPPA 2019. The outstanding compliance item is the legal confirmation of lawful basis and the drafting of data subject rights procedures (privacy notice, consent form for farmer registration, employee biometric consent). These are legal and procedural tasks — not system development tasks — and must be completed by BIRDC's legal counsel before the farmer registration module goes live.
