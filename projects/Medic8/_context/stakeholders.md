# Stakeholder Register: Medic8

This register defines the 18 built-in roles for the Medic8 platform. Each role specifies the access scope, permitted and restricted areas, and key workflows. Roles are grouped by functional domain.

---

## Platform Level

### 1. Super Admin

| Attribute | Detail |
|---|---|
| Role Name | Super Admin |
| Access Scope | Full platform access across all tenants |
| Can Access | All modules, all tenants, global configuration, billing engine, platform monitoring dashboards, global patient identity registry |
| Cannot Access | No restrictions |
| Key Workflows | Tenant provisioning, subscription billing, global patient identity management, platform monitoring, feature flag management |

---

## Facility Management

### 2. Facility Admin / Medical Director

| Attribute | Detail |
|---|---|
| Role Name | Facility Admin / Medical Director |
| Access Scope | Full facility management within a single tenant |
| Can Access | All modules within their facility, all facility reports, staff management, system configuration, audit trail |
| Cannot Access | Other tenants, platform-level billing, global configuration |
| Key Workflows | Staff onboarding, module configuration, report review, audit trail review, facility settings management |

### 3. Facility Director / Owner

| Attribute | Detail |
|---|---|
| Role Name | Facility Director / Owner |
| Access Scope | Director platform with aggregate and cross-facility view |
| Can Access | Aggregate reports, approval workflows, cross-facility analytics, financial overview dashboards |
| Cannot Access | Clinical records (patient-level), direct module configuration, other tenants |
| Key Workflows | Financial overview, cross-facility analytics, approval workflows, strategic reporting |

---

## Clinical Staff

### 4. Doctor / Physician

| Attribute | Detail |
|---|---|
| Role Name | Doctor / Physician |
| Access Scope | Full clinical access for OPD and IPD within assigned facility |
| Can Access | OPD consultation, IPD ward rounds, orders (lab, radiology, procedures), prescriptions, referrals, investigation results, patient history |
| Cannot Access | Billing, HR, payroll, accounting, system configuration, other facility data |
| Key Workflows | OPD consultation, prescribing, ordering investigations, ward rounds, discharge summaries, referral letters |

### 5. Clinical Officer

| Attribute | Detail |
|---|---|
| Role Name | Clinical Officer |
| Access Scope | Same as Doctor within scope of practice |
| Can Access | OPD consultation, IPD ward rounds, orders, referrals, investigation results, patient history |
| Cannot Access | Billing, HR, payroll, accounting, system configuration. Restricted prescribing authority per Uganda Allied Health Professionals Council regulations |
| Key Workflows | OPD consultation, prescribing (within regulatory scope), ordering investigations, ward rounds, discharge, referrals |

### 6. Nurse / Midwife

| Attribute | Detail |
|---|---|
| Role Name | Nurse / Midwife |
| Access Scope | Nursing and midwifery clinical documentation |
| Can Access | Nursing notes, vital signs entry, drug administration (MAR), maternity records, immunisation records, triage |
| Cannot Access | Prescribing, billing, HR, payroll, accounting, system configuration |
| Key Workflows | Triage, vital signs recording, drug round (MAR), nursing notes, maternity/ANC documentation, immunisation |

---

## Diagnostics

### 7. Pharmacist

| Attribute | Detail |
|---|---|
| Role Name | Pharmacist |
| Access Scope | Pharmacy operations |
| Can Access | Prescription queue, dispensing workflow, pharmacy stock management, narcotic register, drug interaction alerts |
| Cannot Access | Clinical notes beyond prescription details, billing, HR, payroll, accounting |
| Key Workflows | Dispensing, stock management, drug interaction review, narcotic register maintenance, expiry tracking |

### 8. Lab Technician

| Attribute | Detail |
|---|---|
| Role Name | Lab Technician |
| Access Scope | Laboratory operations |
| Can Access | Lab request queue, sample collection records, result entry, QC records, critical value alerting |
| Cannot Access | Billing, HR, payroll, accounting, clinical notes beyond lab requests |
| Key Workflows | Sample collection, result entry, quality control, critical value alerting, worklist management |

### 9. Radiographer

| Attribute | Detail |
|---|---|
| Role Name | Radiographer |
| Access Scope | Radiology operations |
| Can Access | Radiology request queue, report entry, image upload, worklist |
| Cannot Access | Billing, HR, payroll, accounting, clinical notes beyond radiology requests |
| Key Workflows | Worklist management, report entry, image upload, study tracking |

---

## Administrative

### 10. Receptionist / Front Desk

| Attribute | Detail |
|---|---|
| Role Name | Receptionist / Front Desk |
| Access Scope | Patient registration and scheduling |
| Can Access | Patient registration, appointment booking, queue management, file request submission |
| Cannot Access | Clinical notes, billing beyond initial fee collection (if configured), HR, payroll, accounting |
| Key Workflows | Patient registration, appointment booking, queue management, file requests, visitor management |

### 11. Records Officer

| Attribute | Detail |
|---|---|
| Role Name | Records Officer |
| Access Scope | Medical records management |
| Can Access | File tracking, discharge summary archive, medical certificate generation, HMIS form management. Read-only access on clinical records |
| Cannot Access | Clinical data entry, billing, HR, payroll, accounting |
| Key Workflows | File tracking, certificate generation, HMIS form management, discharge summary archival, records retrieval |

---

## Financial

### 12. Cashier / Billing Clerk

| Attribute | Detail |
|---|---|
| Role Name | Cashier / Billing Clerk |
| Access Scope | Patient billing and payment collection |
| Can Access | Patient accounts, payment collection, receipt generation, cash reconciliation, mobile money (MoMo) verification |
| Cannot Access | Clinical notes, HR, payroll, accounting journals, system configuration |
| Key Workflows | Payment collection, receipt printing, daily cash reconciliation, MoMo payment verification, invoice generation |

### 13. Insurance Clerk

| Attribute | Detail |
|---|---|
| Role Name | Insurance Clerk |
| Access Scope | Insurance claims processing |
| Can Access | Insurance member verification, pre-authorisation requests, claim generation, claim submission, rejection management, reconciliation |
| Cannot Access | Direct billing operations, clinical notes, HR, payroll, accounting |
| Key Workflows | Member verification, pre-authorisation, claim generation, claim submission, rejection management, insurer reconciliation |

### 14. Accountant

| Attribute | Detail |
|---|---|
| Role Name | Accountant |
| Access Scope | Financial accounting and reporting |
| Can Access | Financial accounting module, journal entries, bank reconciliation, financial statements, payroll review, donor fund reporting. Read-only access on billing data |
| Cannot Access | Clinical records, direct billing operations, system configuration |
| Key Workflows | Journal entries, bank reconciliation, financial statement preparation, donor fund reporting, payroll review |

### 15. Store Keeper

| Attribute | Detail |
|---|---|
| Role Name | Store Keeper |
| Access Scope | Inventory and stores management |
| Can Access | Inventory receiving (GRN), stock transfers, stock adjustments, stock counts, expiry management, NMS ordering |
| Cannot Access | Clinical records, billing, financial accounting, HR, payroll |
| Key Workflows | Goods Received Note (GRN), stock transfer, expiry management, NMS ordering, stock count reconciliation |

### 16. Auditor

| Attribute | Detail |
|---|---|
| Role Name | Auditor |
| Access Scope | Read-only audit and compliance access |
| Can Access | All financial records (read-only), audit trail, compliance reports, transaction logs |
| Cannot Access | Clinical records, data modification of any kind, system configuration |
| Key Workflows | Audit trail review, compliance verification, financial audit, transaction sampling, exception reporting |

---

## External

### 17. Patient / Client

| Attribute | Detail |
|---|---|
| Role Name | Patient / Client |
| Access Scope | Patient portal (own records only) |
| Can Access | Own medical records, appointment booking, test results, invoices, payment history, medication reminders |
| Cannot Access | Other patients' records, staff-facing modules, administrative functions, billing management |
| Key Workflows | View test results, book appointments, pay fees, receive medication reminders, download records |

### 18. Community Health Worker (VHT/CHW)

| Attribute | Detail |
|---|---|
| Role Name | Community Health Worker (VHT/CHW) |
| Access Scope | CHW mobile app for assigned community area only |
| Can Access | Patient registration (community), referral submission, home visit records for assigned area |
| Cannot Access | Facility-level clinical records, billing, HR, payroll, accounting, records outside assigned area |
| Key Workflows | Patient registration, referral submission, home visit documentation, activity reporting |
