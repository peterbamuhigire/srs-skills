# Target Users for the Medic8 Healthcare Management System

## 4.1 User Role Matrix

The following 18 roles define the complete access model for the Medic8 platform. Roles are scoped by functional domain to enforce the principle that each user sees only the modules relevant to their responsibilities.

### 4.1.1 Platform Level

| Role | Category | Access Scope | Primary Workflows | Technical Proficiency |
|---|---|---|---|---|
| Super Admin | Platform | Full platform access across all tenants | Tenant provisioning, subscription billing, global patient identity management, platform monitoring, feature flag management | Advanced |

### 4.1.2 Facility Management

| Role | Category | Access Scope | Primary Workflows | Technical Proficiency |
|---|---|---|---|---|
| Facility Admin / Medical Director | Management | Full facility management within a single tenant | Staff onboarding, module configuration, report review, audit trail review, facility settings | Intermediate to Advanced |
| Facility Director / Owner | Management | Director platform with aggregate and cross-facility view | Financial overview, cross-facility analytics, approval workflows, strategic reporting | Intermediate |

### 4.1.3 Clinical Staff

| Role | Category | Access Scope | Primary Workflows | Technical Proficiency |
|---|---|---|---|---|
| Doctor / Physician | Clinical | Full clinical access for Outpatient Department (OPD) and Inpatient Department (IPD) within assigned facility | OPD consultation, prescribing, ordering investigations, ward rounds, discharge summaries, referral letters | Intermediate |
| Clinical Officer | Clinical | Same as Doctor within scope of practice; restricted prescribing authority per Uganda Allied Health Professionals Council regulations | OPD consultation, prescribing (within regulatory scope), ordering investigations, ward rounds, discharge, referrals | Intermediate |
| Nurse / Midwife | Clinical | Nursing and midwifery clinical documentation | Triage, vital signs recording, drug round (Medication Administration Record), nursing notes, maternity/ANC documentation, immunisation | Basic to Intermediate |

### 4.1.4 Diagnostics

| Role | Category | Access Scope | Primary Workflows | Technical Proficiency |
|---|---|---|---|---|
| Pharmacist | Diagnostics | Pharmacy operations | Dispensing, stock management, drug interaction review, narcotic register maintenance, expiry tracking | Intermediate |
| Lab Technician | Diagnostics | Laboratory operations | Sample collection, result entry, quality control, critical value alerting, worklist management | Intermediate |
| Radiographer | Diagnostics | Radiology operations | Worklist management, report entry, image upload, study tracking | Intermediate |

### 4.1.5 Administrative

| Role | Category | Access Scope | Primary Workflows | Technical Proficiency |
|---|---|---|---|---|
| Receptionist / Front Desk | Administrative | Patient registration and scheduling | Patient registration, appointment booking, queue management, file requests, visitor management | Basic |
| Records Officer | Administrative | Medical records management (read-only on clinical records) | File tracking, certificate generation, HMIS form management, discharge summary archival, records retrieval | Basic to Intermediate |

### 4.1.6 Financial

| Role | Category | Access Scope | Primary Workflows | Technical Proficiency |
|---|---|---|---|---|
| Cashier / Billing Clerk | Financial | Patient billing and payment collection | Payment collection, receipt printing, daily cash reconciliation, mobile money (MoMo) payment verification, invoice generation | Basic |
| Insurance Clerk | Financial | Insurance claims processing | Member verification, pre-authorisation, claim generation, claim submission, rejection management, insurer reconciliation | Intermediate |
| Accountant | Financial | Financial accounting and reporting (read-only on billing data) | Journal entries, bank reconciliation, financial statement preparation, donor fund reporting, payroll review | Intermediate to Advanced |
| Store Keeper | Financial | Inventory and stores management | Goods Received Note (GRN), stock transfer, expiry management, National Medical Stores (NMS) ordering, stock count reconciliation | Basic to Intermediate |
| Auditor | Financial | Read-only audit and compliance access | Audit trail review, compliance verification, financial audit, transaction sampling, exception reporting | Advanced |

### 4.1.7 External

| Role | Category | Access Scope | Primary Workflows | Technical Proficiency |
|---|---|---|---|---|
| Patient / Client | External | Patient portal (own records only) | View test results, book appointments, pay fees, receive medication reminders, download records | Basic (assumes smartphone literacy) |
| Community Health Worker (VHT/CHW) | External | CHW mobile app for assigned community area only | Patient registration, referral submission, home visit documentation, activity reporting | Basic |

---

## 4.2 Detailed Personas

### 4.2.1 Dr. Sarah Nakamya — Private Clinic Owner

| Attribute | Detail |
|---|---|
| Name | Dr. Sarah Nakamya |
| Title | Owner / Director |
| Facility | Nakamya Medical Centre |
| Facility Type | Private clinic |
| Location | Kampala, Uganda |
| Size | 3 consultation rooms, pharmacy, basic lab, 8 staff |
| Current System | ClinicMaster (desktop version) |
| Target Tier | Starter (UGX 150,000/month) |

**Current System and Pain Points:**

Dr. Nakamya operates ClinicMaster's desktop version. Server maintenance costs are high and require on-site IT support that she must contract externally. The system has no mobile money integration; patients must pay cash or visit the bank. No patient-facing app exists for appointment booking or result access, leading to walk-in congestion that wastes patient time and overloads the receptionist. HMIS 105 tallying is done manually at the end of each month, consuming 2+ staff-days that could be spent on patient care.

**What She Wants from Medic8:**

- SaaS delivery with no on-premise server to maintain — eliminates IT contractor dependency
- Integrated mobile money (MTN MoMo, Airtel Money) payment collection with auto-reconciliation
- Patient appointment booking app to reduce walk-in congestion and improve daily scheduling
- Automated HMIS 105 report generation from clinical data, reducing month-end reporting from 2+ days to minutes

**Key Modules:** OPD, Pharmacy, Lab, Billing, Appointments

**Expected Monthly Cost:** UGX 150,000 (Starter tier)

**Success Criteria (Renewal Triggers):**

1. Server maintenance cost drops to zero within 30 days of migration
2. Mobile money payment reconciliation operates without manual intervention
3. HMIS 105 report generation completes in under 15 minutes without manual tallying
4. Walk-in congestion decreases as patients adopt the appointment booking app

---

### 4.2.2 Sr. Margaret Akello — Mission Hospital Medical Director

| Attribute | Detail |
|---|---|
| Name | Sr. Margaret Akello |
| Title | Medical Director |
| Facility | St. Joseph's Mission Hospital |
| Facility Type | Mission hospital (80-bed) |
| Location | Eastern Uganda |
| Size | Maternity, lab, pharmacy, HIV programme, 45 staff |
| Current System | OpenMRS (donated by NGO partner) |
| Target Tier | Pro (UGX 700,000/month) |

**Current System and Pain Points:**

St. Joseph's runs OpenMRS, donated by an NGO partner. OpenMRS has no billing module; the facility uses a separate Excel spreadsheet for billing and revenue tracking, creating reconciliation gaps. No insurance management capability exists; claims are processed manually via paper forms, leading to high rejection rates and delayed reimbursements. Java developer costs for OpenMRS customisation are prohibitive at USD 80-120 per hour. Training requires external trainers who must travel to Eastern Uganda, adding cost and scheduling delays.

**What She Wants from Medic8:**

- Integrated billing and insurance claims management in a single platform, eliminating the Excel workaround
- Donor fund accounting to track and report on restricted programme funds (Global Fund, PEPFAR) with ring-fenced cost centres
- Prevention of Mother-to-Child Transmission (PMTCT) tracking for the HIV/AIDS programme with Ministry of Health (MoH)-compliant indicators
- Local Uganda-based support team with direct knowledge of MoH reporting requirements

**Key Modules:** OPD, IPD, Maternity, HIV/AIDS, Pharmacy, Lab, Billing, Insurance, Accounting

**Expected Monthly Cost:** UGX 700,000 (Pro tier)

**Success Criteria (Renewal Triggers):**

1. Insurance claim rejection rate decreases by at least 50% within 6 months of deployment
2. Donor fund reports generate directly from the system without manual compilation
3. PMTCT indicators align with MoH reporting requirements without manual calculation
4. Total cost of system operation (Medic8 subscription) is lower than the prior OpenMRS customisation and support costs

---

### 4.2.3 Dr. James Okello — Government Health Centre In-Charge

| Attribute | Detail |
|---|---|
| Name | Dr. James Okello |
| Title | In-Charge |
| Facility | Gulu HC IV |
| Facility Type | Government Health Centre IV |
| Location | Northern Uganda |
| Size | 30 beds, 25 staff |
| Current System | Paper registers + manual DHIS2 entry |
| Target Tier | Growth (UGX 350,000/month) |

**Current System and Pain Points:**

Gulu HC IV operates on paper registers for all clinical documentation. HMIS manual tallying consumes 2-3 staff-days per month — time that clinical staff cannot spend on patient care in an understaffed facility. Drug stockouts occur because there is no visibility into consumption patterns or stock levels; orders to NMS are based on estimates rather than data. Capitation grant tracking is done manually with no audit trail, creating accountability risks. Most staff have limited computer skills, making complex software unusable without extensive training.

**What He Wants from Medic8:**

- Automated HMIS 105/108 report generation with direct DHIS2 submission, eliminating double entry
- NMS ordering integration with consumption-based demand forecasting to prevent drug stockouts
- Offline-first architecture that works reliably with intermittent internet connectivity in Northern Uganda
- Simple interface designed for staff with limited digital literacy — guided onboarding, role-scoped views, progressive disclosure

**Key Modules:** OPD, Maternity, Immunisation, Pharmacy, HMIS Reporting, Inventory

**Expected Monthly Cost:** UGX 350,000 (Growth tier)

**Success Criteria (Renewal Triggers):**

1. HMIS reporting time decreases from 2-3 staff-days to under 1 hour per month
2. Drug stockout incidents decrease by at least 60% within 12 months through consumption-based forecasting
3. System remains operational during internet outages lasting up to 72 hours
4. Staff with limited digital literacy complete onboarding and operate the system without external trainer support

---

### 4.2.4 Mr. Rajesh Patel — Multi-Facility Hospital Network CEO

| Attribute | Detail |
|---|---|
| Name | Mr. Rajesh Patel |
| Title | CEO |
| Facility | Patel Hospital Group |
| Facility Type | Multi-facility hospital network (5 hospitals) |
| Location | Mumbai, Pune, Bangalore, India |
| Size | 500+ beds total, 800 staff |
| Current System | Legacy on-premise Hospital Information System (HIS) |
| Target Tier | Enterprise (custom pricing) |

**Current System and Pain Points:**

Patel Hospital Group operates a legacy on-premise HIS across 5 hospitals. No cross-facility patient record sharing exists; patients must re-register at each hospital, duplicating demographic data entry and losing clinical history. No consolidated analytics dashboard exists; each facility reports independently, preventing group-level strategic decisions. Separate billing systems per hospital create no unified revenue view. Expensive vendor lock-in with the current on-premise vendor limits negotiating power and innovation adoption.

**What He Wants from Medic8:**

- Director Platform with cross-facility analytics and unified dashboards for group-level decision-making
- Unified patient identity across all 5 facilities, eliminating re-registration and enabling continuity of care
- DRG-based billing for insurance integration across the Indian market
- FHIR R4 API for interoperability with external systems, research institutions, and future integrations with India's Ayushman Bharat Digital Mission (ABDM)

**Key Modules:** All clinical modules, Billing, Insurance, Accounting, Director Platform, FHIR API

**Expected Monthly Cost:** Enterprise (custom pricing based on facility count and bed capacity)

**Success Criteria (Renewal Triggers):**

1. Patient lookup across all 5 facilities completes in under 1 second
2. Consolidated revenue dashboard provides real-time group-level financial visibility
3. Patient re-registration at secondary facilities drops to zero through unified patient identity
4. Vendor lock-in eliminated through FHIR R4 API enabling data portability

---

### 4.2.5 Jane Achieng — PEPFAR Programme Manager

| Attribute | Detail |
|---|---|
| Name | Jane Achieng |
| Title | PEPFAR Programme Manager |
| Facility | Health Access Uganda (NGO) |
| Facility Type | NGO supporting 20 health facilities |
| Location | Western Uganda |
| Size | 20 supported facilities under USAID PEPFAR funding |
| Current System | UgandaEMR (OpenMRS fork) |
| Target Tier | Pro (UGX 700,000/month x 20 facilities) |

**Current System and Pain Points:**

Health Access Uganda runs UgandaEMR (an OpenMRS fork) across 20 PEPFAR-funded facilities. No integrated billing module exists; facilities use a separate system for revenue, creating reconciliation gaps. OpenMRS customisation costs approximately USD 15,000 per year. PEPFAR Monitoring, Evaluation, and Reporting (MER) indicator calculation (TX_CURR, TX_NEW, TX_PVLS) is done manually, consuming significant programme staff time and introducing calculation errors that risk audit findings. Staff turnover at supported facilities means constant retraining on a complex system.

**What She Wants from Medic8:**

- Automated PEPFAR MER indicator calculation (TX_CURR, TX_NEW, TX_PVLS) validated against manual tallies, eliminating calculation errors
- Donor fund tracking with restricted fund accounting and donor-specific reporting for USAID compliance
- Data migration from OpenMRS/UgandaEMR with validated import, ensuring no patient records are lost during transition
- Lower total cost of ownership compared to the current OpenMRS support contract (currently USD 15,000/year customisation + server costs + external training)

**Key Modules:** HIV/AIDS, TB, Lab, Pharmacy, HMIS, Donor Fund Accounting

**Expected Monthly Cost:** UGX 700,000/month x 20 facilities = UGX 14,000,000/month

**Success Criteria (Renewal Triggers):**

1. PEPFAR MER indicator reports match or exceed the accuracy of manual calculation, verified against baseline data
2. Total annual cost of Medic8 subscription across 20 facilities is lower than the combined OpenMRS customisation, server, and training costs
3. Data migration from UgandaEMR completes with zero patient record loss, validated by record count reconciliation
4. Staff at supported facilities complete onboarding without external trainer travel

---

### 4.2.6 Prof. Edward Ssali — National Referral Hospital IT Director

| Attribute | Detail |
|---|---|
| Name | Prof. Edward Ssali |
| Title | IT Director |
| Facility | Mulago National Referral Hospital |
| Facility Type | National referral hospital |
| Location | Kampala, Uganda |
| Size | 1,500+ beds, 50+ departments, 3,000+ staff |
| Current System | Patchwork of disconnected systems |
| Target Tier | Enterprise (Phase 4 target) |

**Current System and Pain Points:**

Mulago operates a patchwork of disconnected systems with no unified patient record across departments. Patients carry physical files between departments; files are frequently misfiled or lost during inter-departmental transfer. Laboratory results are lost during transfer between the lab and the requesting ward. Radiology images are stored on CD-ROMs with no digital archive or PACS, making historical image comparison impossible. Insurance claims are processed manually with high rejection rates due to incomplete documentation and coding errors.

**What He Wants from Medic8:**

- Enterprise-scale EHR with a unified patient record across all 50+ departments, eliminating physical file transfer
- PACS integration for digital radiology image storage and retrieval, replacing CD-ROM archiving
- HL7 v2 interfaces for automated analyser connectivity in the laboratory, eliminating manual transcription of results
- FHIR R4 API for research data extraction and interoperability with the Ministry of Health, academic institutions, and international research networks
- Real-time bed management dashboard across all wards for capacity planning and patient flow optimisation

**Key Modules:** All modules, PACS, HL7 v2, FHIR API, Director Platform

**Expected Monthly Cost:** Enterprise (Phase 4 custom pricing based on department count, bed capacity, and integration scope)

**Success Criteria (Renewal Triggers):**

1. Patient file loss between departments drops to zero through digital record unification
2. Laboratory result turnaround time decreases by at least 40% through automated analyser connectivity
3. Radiology images are retrievable within 5 seconds from the PACS archive, replacing CD-ROM retrieval
4. Insurance claim rejection rate decreases by at least 50% through automated coding and documentation completeness checks

---

## 4.3 User Journey Summary

### 4.3.1 Dr. Sarah Nakamya — Private Clinic Owner

**A typical day without Medic8:**

Dr. Nakamya arrives at Nakamya Medical Centre at 08:00. The receptionist has already started registering walk-in patients in ClinicMaster's desktop application. The server, located in a back room, crashed overnight; the IT contractor is called and arrives 2 hours later (UGX 100,000 call-out fee). During the downtime, the receptionist registers patients in a paper notebook. Three patients ask to pay via MTN MoMo; the receptionist explains that only cash is accepted. Dr. Nakamya sees 25 patients, writing prescriptions by hand and passing them to the pharmacy. At month-end, 2 staff members spend 2 full days tallying HMIS 105 data from registers, cross-checking against ClinicMaster records, and manually entering totals into DHIS2.

**A typical day with Medic8:**

Dr. Nakamya arrives at 08:00. The system is running — there is no server to crash because Medic8 operates as cloud SaaS. Three patients booked appointments through the Medic8 patient app overnight; the receptionist confirms them and manages the queue digitally. Five patients pay consultation fees via MTN MoMo from their phones; receipts generate automatically and reconcile to patient accounts without cashier intervention. Dr. Nakamya prescribes electronically; the pharmacy receives the prescription queue in real time with drug interaction alerts. At month-end, she clicks "Generate HMIS 105" — the report compiles from clinical data in under 15 minutes and pushes directly to DHIS2.

---

### 4.3.2 Sr. Margaret Akello — Mission Hospital Medical Director

**A typical day without Medic8:**

Sr. Akello reviews the facility's finances using an Excel spreadsheet maintained by the accounts clerk. Three insurance claim rejections arrived by post from Jubilee Health Insurance — the claims were rejected because diagnosis codes were missing from the paper forms. The HIV programme coordinator spends the morning manually calculating TX_CURR (currently on treatment) counts from patient registers for the quarterly PEPFAR report. The OpenMRS system displays a database error that requires a Java developer to diagnose; the closest available developer charges USD 100/hour and is based in Kampala, 5 hours away.

**A typical day with Medic8:**

Sr. Akello opens the Medic8 dashboard and reviews facility revenue, outstanding insurance claims, and donor fund balances in a single view. The insurance module flags 3 claims that were auto-rejected by Jubilee due to missing pre-authorisation; the insurance clerk corrects them and resubmits electronically within 30 minutes. The HIV programme coordinator opens the PEPFAR MER dashboard — TX_CURR, TX_NEW, and TX_PVLS indicators are calculated automatically from clinical data. The system is SaaS; there is no database to crash locally. Support issues are resolved by the Medic8 Uganda team via in-app chat.

---

### 4.3.3 Dr. James Okello — Government Health Centre In-Charge

**A typical day without Medic8:**

Dr. Okello arrives at Gulu HC IV. The outpatient register is a hardcover exercise book. Each patient visit is recorded by hand: name, age, sex, diagnosis, treatment. The pharmacy store keeper reports that 3 essential medicines are out of stock; the last NMS order was submitted 6 weeks ago based on estimated quantities. A nurse spends 20 minutes searching for a returning patient's previous visit record in a stack of registers. At month-end, Dr. Okello and 2 clinical officers spend 3 days tallying HMIS 105 data from 12 different registers, then manually entering totals into DHIS2 over a slow internet connection that drops 4 times during the process.

**A typical day with Medic8:**

Dr. Okello arrives and opens Medic8 on a tablet. The system loaded overnight via the offline sync; internet connectivity is intermittent but the system operates without interruption. Patient registration takes 2 minutes; returning patients are found instantly by name or national ID. The pharmacy dashboard shows real-time stock levels; the system generated an NMS order last week based on consumption data from the previous 3 months. At month-end, Dr. Okello taps "Generate HMIS 105" — the report compiles from clinical data and queues for DHIS2 submission. When internet connectivity resumes, the report pushes automatically.

---

### 4.3.4 Mr. Rajesh Patel — Multi-Facility Hospital Network CEO

**A typical day without Medic8:**

Mr. Patel reviews financial reports from 5 hospitals. Each hospital emails a separate Excel spreadsheet. His finance team spends 2 days consolidating the data into a group-level report. A patient referred from the Mumbai hospital to the Pune hospital must re-register because the two systems do not share patient records. The patient's medication history is unavailable; the admitting physician calls Mumbai to request it by phone. Mr. Patel requests a cross-facility bed occupancy report; the IT team estimates 1 week to compile it manually.

**A typical day with Medic8:**

Mr. Patel opens the Director Platform dashboard. Group-level revenue, bed occupancy, and patient volume are displayed in real time across all 5 hospitals. A patient referred from Mumbai to Pune is identified instantly through the unified patient identity layer; their full clinical history, current medications, and allergy information are available to the admitting physician within seconds. Mr. Patel drills into the bed occupancy report by facility, department, and time period without waiting for manual compilation.

---

### 4.3.5 Jane Achieng — PEPFAR Programme Manager

**A typical day without Medic8:**

Jane visits 1 of her 20 supported facilities. The facility's UgandaEMR instance shows a Java error that has prevented data entry for 2 days; patient visits during the outage were recorded in paper registers that must now be back-entered. She reviews the quarterly PEPFAR MER report: the programme data officer spent 4 days calculating TX_CURR across 20 facilities by exporting CSV files from UgandaEMR, cleaning data in Excel, and running pivot tables. Two facilities submitted conflicting TX_CURR counts that must be reconciled before the report is submitted to USAID. The OpenMRS support contract is due for renewal at USD 15,000/year.

**A typical day with Medic8:**

Jane opens the Medic8 programme dashboard. TX_CURR, TX_NEW, and TX_PVLS indicators are calculated automatically across all 20 facilities and displayed in a consolidated view. She drills into a facility that shows a TX_PVLS decline and identifies that viral load sample collection dropped last month — she schedules a support visit. The system is SaaS; there are no Java errors to debug. The annual Medic8 subscription across 20 facilities (UGX 700,000 x 20 x 12 = UGX 168,000,000, approximately USD 45,000) includes billing, donor fund accounting, and local support — replacing the USD 15,000/year OpenMRS customisation cost plus separate billing and accounting systems.

---

### 4.3.6 Prof. Edward Ssali — National Referral Hospital IT Director

**A typical day without Medic8:**

Prof. Ssali manages IT for a 1,500-bed hospital with 50+ departments. A patient's physical file is missing — last recorded location was the radiology department 3 days ago. The lab reports that 12 results from the automated analyser were manually transcribed into the system; 2 contained transcription errors that were caught during clinical review. A radiologist needs to compare a current chest X-ray with one taken 6 months ago; the CD-ROM archive is searched for 45 minutes before the disc is located. The insurance department reports that 35% of claims submitted last month were rejected due to incomplete ICD coding.

**A typical day with Medic8:**

Prof. Ssali monitors the Medic8 dashboard. All patient records are digital; physical file transfer between departments does not occur. Laboratory results flow automatically from analysers to patient records via HL7 v2 interfaces, eliminating manual transcription. A radiologist opens the PACS viewer and compares the current chest X-ray with the prior study stored in the digital archive — retrieval takes under 5 seconds. The insurance module auto-codes diagnoses using ICD-11 and flags incomplete claims before submission, reducing rejection rates. The bed management dashboard shows real-time occupancy across all wards, enabling admissions to route patients to available beds without phone calls between ward managers.
