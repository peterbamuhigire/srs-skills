# RBAC Permission Matrix — Medic8

> This document defines the complete Role-Based Access Control (RBAC) permission matrix for the Medic8 multi-tenant SaaS healthcare management system. It covers all 18 built-in roles across all platform modules. This matrix is the authoritative reference for middleware, policy, and data-access-layer implementation.
>
> **Standards:** IEEE 29148-2018 (stakeholder requirements traceability), PMBOK 7th Edition (stakeholder engagement assessment matrix).
>
> **Permission Symbols:**
> - C = Create
> - R = Read
> - U = Update
> - D = Delete
> - — = No access
> - R* = Read with restrictions (Attribute-Based Access Control rules apply; see Section 3)

---

## Section 1: Role Definitions

| # | Role Code | Role Name | Description | Clinical Access | Financial Access | Typical Count per Facility |
|---|---|---|---|---|---|---|
| 1 | `SA` | Super Admin | Platform operator (Chwezi Core Systems). Full access across all tenants, global configuration, billing engine, and platform monitoring. | Full | Full | 1-3 (platform-wide) |
| 2 | `FA` | Facility Admin | Facility-level administrator or Medical Director. Manages all modules, staff, configuration, and audit trail within a single tenant. | Full | Full | 1-2 |
| 3 | `DR` | Doctor / Physician | Licensed medical practitioner. Full clinical access for OPD and IPD within the assigned facility. Unrestricted prescribing authority. | Full | None |  2-50 |
| 4 | `CO` | Clinical Officer | Mid-level clinical practitioner. Same clinical scope as Doctor but with restricted prescribing authority per Uganda Allied Health Professionals Council regulations. | Full | None | 2-20 |
| 5 | `NU` | Nurse / Midwife | Nursing and midwifery clinical documentation. Triage, vital signs, drug administration (MAR), maternity/ANC documentation, immunisation. Cannot prescribe. | Limited | None | 5-100 |
| 6 | `PH` | Pharmacist | Pharmacy operations: dispensing, stock management, drug interaction review, narcotic register, formulary management. | Limited | None | 1-5 |
| 7 | `LT` | Lab Technician | Laboratory operations: sample collection, result entry, quality control, critical value alerting, analyser interface management. | Limited | None | 1-10 |
| 8 | `RG` | Radiographer | Radiology operations: worklist management, report entry, image upload, PACS interaction. | Limited | None | 1-5 |
| 9 | `RE` | Receptionist | Patient registration, appointment booking, queue management, file request submission. No clinical data entry. | None | None | 1-5 |
| 10 | `CA` | Cashier / Billing Clerk | Patient billing and payment collection. Receipt generation, cash reconciliation, mobile money verification. | None | Limited | 1-5 |
| 11 | `IC` | Insurance Clerk | Insurance claims processing: member verification, pre-authorisation, claim generation, submission, rejection management, reconciliation. | None | Limited | 1-3 |
| 12 | `AC` | Accountant | Financial accounting and reporting: journal entries, bank reconciliation, financial statements, payroll review, donor fund reporting. | None | Full | 1-3 |
| 13 | `SK` | Store Keeper | Inventory and stores management: GRN, stock transfers, adjustments, NMS ordering, expiry management. | None | None | 1-3 |
| 14 | `RO` | Records Officer | Medical records management: file tracking, certificate generation, HMIS form management, discharge summary archival. Read-only clinical access. | Limited (read-only) | None | 1-3 |
| 15 | `DI` | Director / Owner | Facility director or owner. Aggregate reporting, approval workflows, cross-facility analytics, financial overview. No patient-level clinical access. | None | Full | 1-2 |
| 16 | `AU` | Auditor | Read-only audit and compliance access. All financial records, audit trail, compliance reports, transaction logs. No data modification. | None | Limited (read-only) |  1-2 |
| 17 | `PT` | Patient / Client | Patient portal access. Own records, appointment booking, test results, invoices, payment history, medication reminders. | None (own records only) | None (own records only) | Unlimited |
| 18 | `CHW` | Community Health Worker (VHT/CHW) | CHW mobile app access for assigned community area. Patient registration, referral submission, home visit documentation. | None | None | 5-50 |

---

## Section 2: Permission Matrix

### Section A: Authentication and User Management

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Login | C | C | C | C | C | C | C | C | C | C | C | C | C | C | C | C | C | C |
| Manage own profile | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD |
| Manage staff accounts | CRUD | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Assign roles | CRUD | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Create custom roles | CRUD | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| View audit trail | R | R | — | — | — | — | — | — | — | — | — | — | — | — | R | R | — | — |
| Configure facility settings | CRUD | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

**Notes:**
1. Super Admin manages staff accounts across all tenants. Facility Admin manages staff accounts within their own tenant only.
2. Facility Admin may create custom roles with any subset of the permissions they themselves hold. Custom roles follow the same priority resolution as built-in roles.
3. Director and Auditor have read-only audit trail access for oversight and compliance purposes.

---

### Section B: Patient Registration and Identity

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Register new patient | C | C | C | C | C | — | — | — | C | — | — | — | — | — | — | — | — | C ¹ |
| Edit patient demographics | — | U | U | U | U | — | — | — | U | — | — | — | — | — | — | — | — | — |
| View patient list | R | R | R | R | R | R* ² | R* ² | R* ² | R | R* ³ | R* ³ | — | — | R | — | — | — | R* ¹ |
| Merge patients | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | CRUD | — | — | — | — |
| Lookup cross-facility | R | R | R | R | — | — | — | — | R | — | — | — | — | R | R | — | — | — |
| View patient photo | R | R | R | R | R | R | R | R | R | R | R | — | — | R | — | — | R ⁴ | — |
| Manage identifiers (NIN, MRN, UNHCR) | CRUD | CRUD | — | — | — | — | — | — | CRU | — | — | — | — | CRU | — | — | — | — |
| Triage assignment | — | C | C | C | C | — | — | — | — | — | — | — | — | — | — | — | — | — |

**Footnotes:**
1. CHW may register patients in their assigned community area only. CHW view is limited to patients they have registered or been assigned.
2. Pharmacist, Lab Technician, and Radiographer see patient name, age, sex, and relevant clinical identifiers only — not full demographic profile.
3. Cashier and Insurance Clerk see patient name, account number, and insurance membership — not clinical data.
4. Patient may view own photo only.

---

### Section C: OPD Consultation

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| View OPD queue | R | R | R | R | R | — | — | — | R | — | — | — | — | — | — | — | — | — |
| Create consultation | — | — | C | C | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Enter vitals | — | — | CU | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Enter diagnosis (ICD-10/11) | — | — | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Write prescription | — | — | CU | CU ⁵ | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Request lab test | — | — | C | C | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Request radiology | — | — | C | C | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Create referral | — | — | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| View clinical history | R | R | R | R | R* ⁶ | R* ² | R* ² | R* ² | — | — | — | — | — | R* ⁷ | — | — | R* ⁴ | — |
| Override drug alert (Tier 3) | — | — | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| End visit | — | — | U | U | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

**Footnotes:**
5. Clinical Officer may prescribe within their gazetted scope of practice only. The system enforces restricted formulary access per BR-CLIN-002.
6. Nurse views clinical history relevant to nursing care (vitals, MAR, nursing notes, allergies, active medications). Does not see full consultation SOAP notes unless assigned to the patient's care team.
7. Records Officer has read-only access to clinical records for file management and certificate generation purposes.

---

### Section D: Laboratory

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| View lab queue | — | R | R | R | R | — | R | — | — | — | — | — | — | — | — | — | — | — |
| Collect sample | — | — | — | — | — | — | CU | — | — | — | — | — | — | — | — | — | — | — |
| Enter result | — | — | — | — | — | — | CU | — | — | — | — | — | — | — | — | — | — | — |
| Validate result | — | R | — | — | — | — | CU ⁸ | — | — | — | — | — | — | — | — | — | — | — |
| View QC records | — | R | — | — | — | — | R | — | — | — | — | — | — | — | — | — | — | — |
| Manage analyser interface | — | CRU | — | — | — | — | CRU | — | — | — | — | — | — | — | — | — | — | — |
| Refer to external lab | — | — | — | — | — | — | CU | — | — | — | — | — | — | — | — | — | — | — |

**Footnotes:**
8. Result validation requires a Lab Technician with supervisor designation. A technician who entered the result cannot validate the same result (four-eyes principle). Facility Admin may validate in exceptional circumstances.

---

### Section E: Pharmacy

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| View prescription queue | — | R | R | R | R | R | — | — | — | — | — | — | — | — | — | — | — | — |
| Dispense drug | — | — | — | — | — | CU | — | — | — | — | — | — | — | — | — | — | — | — |
| Substitute drug (generic) | — | — | — | — | — | CU ⁹ | — | — | — | — | — | — | — | — | — | — | — | — |
| Manage stock (GRN, transfer, adjust) | — | — | — | — | — | CRUD | — | — | — | — | — | — | CRUD | — | — | — | — | — |
| Manage formulary | — | CRUD | — | — | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | — |
| Narcotic register | — | R | — | — | — | CRUD | — | — | — | — | — | — | — | — | — | R | — | — |
| View expiry alerts | — | R | — | — | — | R | — | — | — | — | — | — | R | — | R | — | — | — |

**Footnotes:**
9. Generic substitution requires that the prescribing doctor is notified and the substitution is logged per BR-CLIN-002. Tier 4 drug interaction blocks cannot be overridden by the Pharmacist alone.

---

### Section F: Inpatient Department (IPD)

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Admit patient | — | C | C | C | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Assign bed | — | CU | CU | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Enter nursing notes | — | — | — | — | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Enter ward round notes | — | — | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Order drug round (MAR) | — | — | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Administer drug round (MAR) | — | — | — | — | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Transfer patient | — | CU | CU | CU | CU ¹⁰ | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Discharge patient | — | U | U | U | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| View bed map | — | R | R | R | R | — | — | — | R | — | — | — | — | — | — | — | — | — |
| Manage ward | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

**Footnotes:**
10. Nurse may initiate a transfer request; transfer completion requires receiving nurse acknowledgement per the ward transfer workflow.

---

### Section G: Maternity and ANC

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Register ANC | — | C | C | C | C | — | — | — | C | — | — | — | — | — | — | — | — | — |
| Enter ANC visit | — | — | CU | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Admit in labour | — | — | C | C | C | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Enter partograph | — | — | CU | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Record delivery | — | — | CU | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Link newborn | — | — | CU | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Enter postnatal visit | — | — | CU | CU | CU | — | — | — | — | — | — | — | — | — | — | — | — | — |

---

### Section H: Billing and Finance

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| View patient account | — | R | — | — | — | — | — | — | — | R | R | R | — | — | R | R | R ⁴ | — |
| Collect payment | — | CU | — | — | — | — | — | — | — | CU | — | — | — | — | — | — | — | — |
| Generate receipt | — | C | — | — | — | — | — | — | — | C | — | — | — | — | — | — | — | — |
| Manage price list | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Reconcile cashier | — | R | — | — | — | — | — | — | — | CRU | — | R | — | — | R | R | — | — |
| Manage credits | — | CRUD ¹¹ | — | — | — | — | — | — | — | R | — | R | — | — | R | R | — | — |
| Write-off debt | — | CU ¹² | — | — | — | — | — | — | — | — | — | — | — | — | CU ¹² | — | — | — |
| View financial reports | — | R | — | — | — | — | — | — | — | — | — | R | — | — | R | R | — | — |

**Footnotes:**
11. All credit arrangements require Facility Admin approval per BR-FIN-005.
12. Write-off approval follows tiered authority per BR-FIN-006: amounts under UGX 500,000 require Facility Admin approval; amounts of UGX 500,000 or above require Director approval.

---

### Section I: Insurance

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Verify member | — | R | — | — | — | — | — | — | R | R | R | — | — | — | — | — | — | — |
| Request pre-auth | — | CU | CU | CU | — | — | — | — | — | — | CU | — | — | — | — | — | — | — |
| Generate claim | — | R | — | — | — | — | — | — | — | — | C | — | — | — | — | — | — | — |
| Submit claim | — | R | — | — | — | — | — | — | — | — | CU | — | — | — | — | — | — | — |
| Manage rejections | — | R | — | — | — | — | — | — | — | — | CRU | — | — | — | — | — | — | — |
| Reconcile insurance payment | — | R | — | — | — | — | — | — | — | — | CRU | R | — | — | R | R | — | — |
| View insurer reports | — | R | — | — | — | — | — | — | — | — | R | R | — | — | R | R | — | — |

---

### Section J: HR and Payroll

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| View staff list | — | R | — | — | — | — | — | — | — | — | — | — | — | — | R | R | — | — |
| Add/edit staff | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Manage leave | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | R | — | — | — |
| Run payroll | — | CRU | — | — | — | — | — | — | — | — | — | R | — | — | CRU ¹³ | — | — | — |
| View payslips | — | R | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R ¹⁴ | R | R | — | — |
| Manage duty roster | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| View licence expiry | — | R | — | — | — | — | — | — | — | — | — | — | — | — | R | R | — | — |

**Footnotes:**
13. Director may approve payroll runs. Accountant may review payroll calculations (read-only).
14. Staff members may view their own payslips only.

---

### Section K: Inventory and Stores

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Receive stock (GRN) | — | CU | — | — | — | CU ¹⁵ | — | — | — | — | — | — | CU | — | — | — | — | — |
| Transfer stock | — | CU | — | — | — | CU ¹⁵ | — | — | — | — | — | — | CU | — | — | — | — | — |
| Adjust stock | — | CU | — | — | — | CU ¹⁵ | — | — | — | — | — | — | CU | — | — | — | — | — |
| Manage suppliers | — | CRUD | — | — | — | — | — | — | — | — | — | — | CRUD | — | — | — | — | — |
| Create purchase order | — | CRUD | — | — | — | — | — | — | — | — | — | — | CRU | — | CRU ¹⁶ | — | — | — |
| View stock reports | — | R | — | — | — | R | — | — | — | — | — | R | R | — | R | R | — | — |
| Manage NMS orders | — | CRUD | — | — | — | CRUD | — | — | — | — | — | — | CRUD | — | — | — | — | — |

**Footnotes:**
15. Pharmacist manages stock within the pharmacy store only. Store Keeper manages all stores (main, theatre, ward, dental).
16. Director may approve purchase orders above a configurable threshold.

---

### Section L: HMIS Reporting

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Generate HMIS 105 | — | CR | — | — | — | — | — | — | — | — | — | — | — | CR | — | — | — | — |
| Generate HMIS 108 | — | CR | — | — | — | — | — | — | — | — | — | — | — | CR | — | — | — | — |
| Submit to DHIS2 | — | CU | — | — | — | — | — | — | — | — | — | — | — | CU ¹⁷ | — | — | — | — |
| View PEPFAR MER indicators | — | R | R | R | — | — | — | — | — | — | — | — | — | R | R | — | — | — |
| Manage HMIS form configuration | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

**Footnotes:**
17. Records Officer may submit to DHIS2 only after Facility Admin has reviewed and approved the report.

---

### Section M: Administration

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Manage appointments | — | CRUD | CRU | CRU | CRU | — | — | — | CRUD | — | — | — | — | — | — | — | — | — |
| Manage referrals | — | CRUD | CRUD | CRUD | R | — | — | — | R | — | — | — | — | R | — | — | — | CU ¹⁸ |
| Track medical records/files | — | R | R | R | — | — | — | — | CRU | — | — | — | — | CRUD | — | — | — | — |
| Generate certificates | — | CU | CU | CU | — | — | — | — | — | — | — | — | — | CU | — | — | — | — |
| Manage ambulance | — | CRUD | R | R | R | — | — | — | CRU | — | — | — | — | — | — | — | — | — |

**Footnotes:**
18. CHW may submit community referrals via the CHW mobile app for patients in their assigned area only.

---

### Section N: Patient Portal

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| View own records | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | R | — |
| View own results | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | R | — |
| Book appointment | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | CU | — |
| Pay fees | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | CU | — |
| View payment history | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | R | — |
| Manage family members | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | CRUD ¹⁹ | — |

**Footnotes:**
19. Patient may link family members (spouse, children, dependants) to view their records and manage appointments. Each linked family member must confirm the link via SMS or app confirmation.

---

### Section O: Platform Administration

| Permission | SA | FA | DR | CO | NU | PH | LT | RG | RE | CA | IC | AC | SK | RO | DI | AU | PT | CHW |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Provision tenant | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Configure subscription tier | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Manage global settings | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| View cross-tenant analytics | R | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Manage country configuration | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

---

## Section 3: Sensitive Record Access (ABAC Rules)

Attribute-Based Access Control (ABAC) rules govern access to sensitive clinical data categories. These rules are evaluated at the data access layer, not the UI layer, and override the general RBAC permissions defined in Section 2.

### 3.1 HIV Status

| Attribute | Rule |
|---|---|
| Permitted roles | Doctor (`DR`), Clinical Officer (`CO`) |
| Additional condition | The clinician must be a member of the patient's treating care team **and** hold the explicit `hiv_programme` permission flag |
| Denied scenario | A Doctor not assigned to the HIV programme cannot view HIV status even though they have full clinical access |
| Audit | Every access to HIV status is logged with clinician ID, patient ID, timestamp, and access context |

### 3.2 Mental Health Diagnoses

| Attribute | Rule |
|---|---|
| Permitted roles | Doctor (`DR`), Clinical Officer (`CO`) |
| Additional condition | The clinician must be the treating clinician for the current encounter or explicitly assigned to the patient's mental health care plan |
| Denied scenario | A Doctor reviewing lab results for the same patient does not see mental health diagnoses unless they are the treating clinician |
| Audit | Every access is logged with clinician ID, patient ID, timestamp, and access context |

### 3.3 Reproductive Health Records

| Attribute | Rule |
|---|---|
| Permitted roles | Doctor (`DR`), Clinical Officer (`CO`), Nurse/Midwife (`NU`) |
| Additional condition | The clinician must be a member of the patient's treating care team for the current maternity, ANC, or reproductive health encounter |
| Denied scenario | A Lab Technician processing a pregnancy test result does not see the patient's reproductive health history |
| Audit | Every access is logged with clinician ID, patient ID, timestamp, and access context |

### 3.4 Substance Abuse Records

| Attribute | Rule |
|---|---|
| Permitted roles | Doctor (`DR`), Clinical Officer (`CO`) |
| Additional condition | The clinician must be the treating clinician for the substance abuse programme or current encounter |
| Denied scenario | A Pharmacist dispensing medication does not see substance abuse treatment history |
| Audit | Every access is logged with clinician ID, patient ID, timestamp, and access context |

### 3.5 Emergency Override (Break-the-Glass)

| Attribute | Rule |
|---|---|
| Permitted roles | Doctor (`DR`), Clinical Officer (`CO`) |
| Trigger | Clinician invokes the "Emergency Access" function and provides a documented reason |
| Scope revealed | Allergies, current medications, blood group, HIV status (only if prior patient consent exists per BR-DATA-002), and the last 3 recorded diagnoses |
| Expiry | Access expires automatically after 24 hours |
| Patient notification | Patient is notified via SMS that their records were accessed under emergency override |
| Audit | Clinician ID, facility, patient ID, timestamp, reason, and all records accessed are logged. Break-the-glass events are flagged in the weekly compliance report for Facility Admin review |

---

## Section 4: Privilege Hierarchy

For the purpose of role assignment, permission escalation review, and approval workflows, the privilege levels are:

| Level | Role(s) | Scope |
|---|---|---|
| 7 (highest) | Super Admin (`SA`) | Platform-wide, all tenants |
| 6 | Facility Admin (`FA`) | All modules, single tenant |
| 5 | Director / Owner (`DI`) | Aggregate reporting, approval workflows, financial oversight |
| 4 | Doctor (`DR`), Clinical Officer (`CO`) | Full clinical scope within assigned facility |
| 3 | Nurse/Midwife (`NU`), Pharmacist (`PH`), Lab Technician (`LT`), Radiographer (`RG`) | Domain-specific clinical scope |
| 2 | Receptionist (`RE`), Cashier (`CA`), Insurance Clerk (`IC`), Accountant (`AC`), Store Keeper (`SK`), Records Officer (`RO`), Auditor (`AU`) | Administrative and financial scope |
| 1 (lowest) | Patient (`PT`), Community Health Worker (`CHW`) | Own records or assigned community only |

A user may only assign roles at levels strictly below their own level. A Facility Admin (level 6) may assign levels 1-5 but not level 6 or 7. The Super Admin is the only role that can create Facility Admin accounts.

---

## Section 5: Implementation Notes

1. **Permission resolution at login:** All resolved permissions for the authenticated user are loaded into a permission cache (Redis, 15-minute TTL per `(user_id, facility_id)` key). On any role or permission change, the affected user's cache key is deleted immediately.

2. **Custom roles:** Facility Admin may create custom roles that inherit from a built-in role. Custom roles may add or remove permissions from the base role, but cannot exceed the Facility Admin's own permission set. Custom role definitions are tenant-scoped and do not propagate across tenants.

3. **ABAC evaluation layer:** Sensitive record access rules (Section 3) are enforced at the data access layer (Eloquent global scopes and Repository base class), not at the UI layer. The UI may hide elements for usability, but the authoritative access check occurs server-side. All ABAC rule evaluations are logged.

4. **Audit trail for permission changes:** Every permission grant, revocation, role assignment, role creation, and custom role modification is recorded in the audit trail with: performing user, target user, permission/role affected, timestamp, and facility context.

5. **Cross-facility access:** A user authenticated at Facility A cannot access clinical or financial data at Facility B unless they hold an explicit cross-facility permission grant. Cross-facility identity lookup (patient EMPI) is permitted for roles at privilege level 4 and above plus Receptionist and Records Officer. Cross-facility clinical data access requires emergency override (Section 3.5) or explicit patient consent.

6. **Default deny:** Any permission not explicitly granted via a role assignment is denied. Requests targeting resources in a different tenant return HTTP 404 (not 403) to prevent tenant enumeration, per BR-DATA-004.

7. **Tenant isolation enforcement:** Every tenant-scoped database query includes `WHERE facility_id = ?` enforced at the Repository base class level. An Eloquent global scope provides secondary defence. Platform-level tables (global patient identity, tenant registry) are excluded from tenant scoping but are accessible only to Super Admin.

8. **Offline permission cache:** For offline-first clinical workflows, the permission set is cached locally on the client device at login. Permissions are re-validated on sync. Any permission change made while offline takes effect on the next successful sync.
