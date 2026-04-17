# 6 Feature Priority Matrix

This section classifies every Medic8 feature by priority, effort, value, MoSCoW category, and build phase. The matrix drives scope decisions for each phase gate and feeds directly into the Software Requirements Specification (IEEE 29148-2018 Section 5.2.6). Features are sourced from the verified feature inventory (`_context/features.md`) and the literature-driven enhancement register (`_context/literature-insights.md`).

**Column Definitions:**

- **ID**: Unique feature identifier (FT-nnn)
- **Feature**: Specific feature name
- **Module**: Parent module from the feature inventory
- **Priority**: Critical / High / Medium / Low — ranked by business impact and clinical safety risk
- **Effort**: S (< 1 week) / M (1-2 weeks) / L (2-4 weeks) / XL (> 4 weeks)
- **Value**: High / Medium / Low — ranked by direct user benefit
- **MoSCoW**: Must / Should / Could / Won't — ranked by MVP criticality
- **Phase**: 1 / 2 / 3 / 4 build phase
- **Rationale**: One-sentence justification for the classification

---

## Phase 1 MVP Features (Must Have)

Phase 1 delivers the minimum viable clinical workflow: patient registration, outpatient consultation, pharmacy dispensing, basic laboratory, cash billing, appointment scheduling, and supporting infrastructure (authentication, RBAC, tenant management). Phase 1 gate criteria require all 7 HIGH gaps resolved, core clinical workflow tested end-to-end, and medication safety validation complete (see `_context/metrics.md`).

| ID | Feature | Module | Priority | Effort | Value | MoSCoW | Phase | Rationale |
|---|---|---|---|---|---|---|---|---|
| FT-001 | New patient registration with demographics, contact, next-of-kin, and photo capture | Patient Registration | Critical | M | High | Must | 1 | Every clinical workflow starts with patient identification; no downstream module functions without it. |
| FT-002 | Biometric registration (fingerprint or facial recognition) | Patient Registration | Medium | L | Medium | Must | 1 | Reduces duplicate records in populations with inconsistent documentation; hardware dependency makes it optional per facility. |
| FT-003 | Unique Patient ID (MRN) auto-generation, format configurable per facility | Patient Registration | Critical | S | High | Must | 1 | Unique identification is a prerequisite for clinical safety and data integrity across all modules. |
| FT-004 | Returning patient lookup by name, phone, ID number, NIN, or fingerprint | Patient Registration | Critical | M | High | Must | 1 | Reduces duplicate registrations and wait times; core reception workflow. |
| FT-005 | Patient categories (adult, paediatric, staff, VIP, indigent/sponsored, refugee) | Patient Registration | High | S | Medium | Must | 1 | Drives differential pricing, clinical protocols, and reporting segmentation. |
| FT-006 | Multiple identifiers: NIN, passport, NIRA, UNHCR ID, insurance member number | Patient Registration | High | S | High | Must | 1 | Uganda's identification ecosystem requires support for multiple national and international ID types. |
| FT-007 | Guardian/next-of-kin linking for paediatric patients | Patient Registration | High | S | High | Must | 1 | Legal and clinical requirement for paediatric care; consent-by-proxy depends on this linkage. |
| FT-008 | Patient profile: photo, demographics, blood group, allergies, chronic conditions | Patient Registration | Critical | M | High | Must | 1 | Allergy and chronic condition data are clinical safety prerequisites for prescribing and CDS alerts. |
| FT-009 | Patient merge for duplicate records with full audit trail | Patient Registration | High | L | High | Must | 1 | Duplicate records are inevitable; merge capability with audit trail prevents data loss and clinical errors. |
| FT-010 | Triage queue sorted by triage level | Patient Registration | High | M | High | Must | 1 | Ensures critically ill patients are seen first; foundational to OPD and emergency workflows. |
| FT-011 | Cross-facility lookup via global patient identity layer | Patient Registration | High | L | High | Must | 1 | Architectural foundation for multi-facility patient record sharing; must be built into the data model from Phase 1. |
| FT-012 | Africa-first identifiers: UNHCR Refugee ID, NIN integration, MoMo phone number as lookup | Patient Registration | High | M | High | Must | 1 | Differentiation from foreign-built systems; addresses Uganda's specific identification landscape. |
| FT-013 | Triage: vital signs (BP, temperature, pulse, SpO2, weight, height, BMI, MUAC) | OPD | Critical | M | High | Must | 1 | Vital signs capture is a clinical safety requirement; feeds CDS alerts, NEWS2 scoring, and paediatric growth monitoring. |
| FT-014 | Doctor's queue: real-time per doctor/room with triage priority and wait time | OPD | High | M | High | Must | 1 | Reduces patient wait time and ensures triage priority is respected in consultation order. |
| FT-015 | Clinical consultation: SOAP notes, free-text and structured | OPD | Critical | L | High | Must | 1 | Core clinical documentation; structured capture enables CDS, reporting, and audit while free-text preserves clinical narrative. |
| FT-016 | Diagnosis entry: ICD-10 and ICD-11 with clinical description | OPD | Critical | M | High | Must | 1 | Standardised coding is mandatory for HMIS reporting, insurance claims, and disease surveillance. |
| FT-017 | Investigation requests: lab, radiology, ECG with instant notification | OPD | Critical | M | High | Must | 1 | Electronic ordering reduces transcription errors and enables real-time lab/radiology queue management. |
| FT-018 | Prescription writing: generic + brand, dose, frequency, duration, route, quantity | OPD | Critical | L | High | Must | 1 | Core prescribing workflow; structured data enables drug interaction checking, stock-aware prescribing, and pharmacy dispensing. |
| FT-019 | Stock-aware prescribing: shows pharmacy availability before saving | OPD | High | M | High | Must | 1 | Prevents prescribing out-of-stock medications; reduces patient frustration and pharmacy re-work. |
| FT-020 | Drug interaction checking (four-tier alert: Info/Warning/Serious/Fatal) | OPD | Critical | L | High | Must | 1 | Clinical safety requirement; four-tier architecture reduces alert fatigue compared to binary alerts (Rowlands Ch 44). |
| FT-021 | Procedure recording: minor procedures in OPD | OPD | Medium | S | Medium | Must | 1 | Captures revenue-generating procedures and clinical documentation for minor OPD procedures. |
| FT-022 | Referral: internal, external, electronic referral letter | OPD | High | M | High | Must | 1 | Referral is a core clinical workflow; electronic letters reduce handoff errors and support continuity of care. |
| FT-023 | Follow-up appointment booking from consultation | OPD | High | S | High | Must | 1 | Reduces missed follow-ups; integrates with appointment scheduling module. |
| FT-024 | Clinical notes history: complete visit history in one screen | OPD | High | M | High | Must | 1 | Clinicians require longitudinal view to make informed decisions; reduces redundant investigations. |
| FT-025 | Africa-first OPD: HMIS 105 auto-capture, malaria mRDT field, HIV status field, MUAC screening, MOH 5 format | OPD | High | M | High | Must | 1 | Regulatory compliance for Uganda facilities; auto-capture eliminates manual HMIS data extraction. |
| FT-026 | Lab request from OPD/IPD/Emergency | Laboratory (LIS) | Critical | M | High | Must | 1 | Electronic lab ordering is the entry point for the laboratory workflow; eliminates paper request forms. |
| FT-027 | Sample collection with barcode/QR label generation | Laboratory (LIS) | High | M | High | Must | 1 | Barcode labelling prevents sample mislabelling — a critical patient safety control. |
| FT-028 | Specimen tracking: requested, collected, received, processing, result ready | Laboratory (LIS) | High | M | High | Must | 1 | End-to-end tracking reduces lost samples and enables turnaround time measurement. |
| FT-029 | Result entry with reference ranges, auto-flag abnormal (H/L, critical) | Laboratory (LIS) | Critical | M | High | Must | 1 | Abnormal result flagging is a clinical safety requirement; critical values trigger escalation alerts. |
| FT-030 | Critical value alerts with escalation | Laboratory (LIS) | Critical | M | High | Must | 1 | Delayed critical value notification is a patient safety event; escalation ensures clinician acknowledgement. |
| FT-031 | Result validation by lab supervisor | Laboratory (LIS) | High | S | High | Must | 1 | Two-step validation (entry + approval) is standard laboratory quality assurance practice. |
| FT-032 | Africa-first Lab: HMIS 105 Section 2, malaria/HIV/syphilis/pregnancy tests, CD4 tracking, GeneXpert TB | Laboratory (LIS) | High | M | High | Must | 1 | Uganda HMIS reporting requires specific test aggregation; CD4 and GeneXpert are HIV/TB programme essentials. |
| FT-033 | Prescription queue from OPD/IPD/Emergency | Pharmacy | Critical | M | High | Must | 1 | Electronic prescription queue eliminates paper prescriptions and ensures pharmacy receives orders in real time. |
| FT-034 | Dispensing with stock deduction | Pharmacy | Critical | M | High | Must | 1 | Automatic stock deduction at dispensing maintains accurate inventory and prevents stock discrepancies. |
| FT-035 | Generic/brand substitution with doctor notification | Pharmacy | High | M | High | Must | 1 | Enables pharmacist to substitute when prescribed brand is unavailable while maintaining prescriber awareness. |
| FT-036 | Dispensing label generation | Pharmacy | Medium | S | Medium | Must | 1 | Patient medication labels reduce administration errors at home; regulatory requirement in many jurisdictions. |
| FT-037 | Partial dispensing with pending balance | Pharmacy | High | M | High | Must | 1 | Stock shortages are common in SSA; partial dispensing tracks what the patient still needs to collect. |
| FT-038 | Stock management: GRN, transfer, adjust, return | Pharmacy | High | L | High | Must | 1 | Core inventory operations required for accurate stock records and financial reconciliation. |
| FT-039 | Expiry tracking: 90-day flag | Pharmacy | High | S | High | Must | 1 | Expired medication dispensing is a patient safety and financial risk; 90-day flag enables proactive action. |
| FT-040 | Stock valuation: FIFO, weighted average | Pharmacy | Medium | M | Medium | Must | 1 | Financial reporting requires consistent stock valuation methodology. |
| FT-041 | Minimum stock level alerts | Pharmacy | High | S | High | Must | 1 | Stockout prevention is critical for clinical continuity; alerts trigger reorder before stockout occurs. |
| FT-042 | Drug formulary management | Pharmacy | High | M | High | Must | 1 | Facility-specific formulary controls prescribing scope and supports stock-aware prescribing. |
| FT-043 | Narcotic/controlled drug register | Pharmacy | Critical | M | High | Must | 1 | Legal requirement under Uganda National Drug Policy; controlled substances require separate register with audit trail. |
| FT-044 | Africa-first Pharmacy: NMS drug codes, LMIS export, ACT tracking, ARV dispensing, PEPFAR commodity tracking | Pharmacy | High | L | High | Must | 1 | NMS integration and LMIS export are regulatory requirements; ACT and ARV tracking are programme essentials. |
| FT-045 | Patient account with real-time charge accumulation | Billing | Critical | L | High | Must | 1 | Revenue capture depends on accurate, real-time billing; prevents charge leakage from clinical encounters. |
| FT-046 | Configurable price list, patient category pricing | Billing | High | M | High | Must | 1 | Facilities charge different rates for staff, VIP, indigent, and insured patients; configurable pricing is a business requirement. |
| FT-047 | Auto-billing from clinical screens | Billing | Critical | M | High | Must | 1 | Eliminates manual charge entry; every clinical action (consultation, lab, dispensing) generates a billing line automatically. |
| FT-048 | Receipt generation, cash payment, split billing | Billing | High | M | High | Must | 1 | Cash payment with printed receipt is the dominant payment mode in Uganda's private clinics. |
| FT-049 | Deposit management, running bill, credit management | Billing | High | M | High | Must | 1 | Running bills for inpatients and credit for corporate clients are standard hospital financial workflows. |
| FT-050 | Daily cashier reconciliation | Billing | High | M | High | Must | 1 | Financial control requires daily reconciliation; Phase 1 gate requires 95%+ cash billing reconciliation rate. |
| FT-051 | Africa-first Billing: MTN MoMo / Airtel Money API, micro-payment support | Billing | High | L | High | Must | 1 | Mobile money is the dominant non-cash payment channel in Uganda; micro-payment supports low-value clinic visits. |
| FT-052 | Appointment booking, SMS/WhatsApp reminders | Appointments | High | M | High | Must | 1 | Reduces no-show rates and improves clinic scheduling efficiency; SMS/WhatsApp is the primary communication channel in Uganda. |
| FT-053 | Doctor availability calendar, queue management | Appointments | High | M | High | Must | 1 | Prevents double-booking and manages patient flow through the facility. |
| FT-054 | Walk-in integration, online booking | Appointments | Medium | M | Medium | Must | 1 | Walk-in patients represent the majority of visits in Uganda; online booking serves urban, tech-savvy patients. |
| FT-055 | Africa-first Appointments: WhatsApp booking, USSD booking, Africa's Talking SMS | Appointments | High | M | High | Must | 1 | USSD booking reaches patients without smartphones; Africa's Talking is the dominant SMS gateway in East Africa. |
| FT-056 | Multi-tenant architecture with facility_id isolation | Infrastructure | Critical | XL | High | Must | 1 | Architectural foundation; all data access, billing, and configuration are tenant-scoped. |
| FT-057 | Authentication and session management | Infrastructure | Critical | L | High | Must | 1 | Security prerequisite for all system access; must support session-based (web) and JWT (API/mobile) authentication. |
| FT-058 | Role-Based Access Control (RBAC) | Infrastructure | Critical | L | High | Must | 1 | Clinical safety and data protection require strict role-scoped access; pharmacist never sees HR, lab tech never sees payroll. |
| FT-059 | Offline-first architecture for clinical workflows | Infrastructure | Critical | XL | High | Must | 1 | Power and internet instability in SSA make offline capability a clinical safety requirement, not a convenience feature. |
| FT-060 | Country configuration layer (regulatory, clinical, financial, reporting) | Infrastructure | High | XL | High | Must | 1 | Architectural investment that enables multi-country expansion without forking the codebase. |
| FT-061 | Per-module activation (progressive enablement) | Infrastructure | High | M | High | Must | 1 | Facilities start with registration + OPD and add modules progressively; each module must be independently useful. |
| FT-062 | Audit trail for all clinical and financial actions | Infrastructure | Critical | L | High | Must | 1 | Regulatory, legal, and clinical safety requirement; all data modifications are logged with user, timestamp, and action. |
| FT-063 | Quality control: QC records, Levey-Jennings charts | Laboratory (LIS) | Medium | M | Medium | Must | 1 | Laboratory accreditation requires documented QC; Levey-Jennings charts visualise assay performance trends. |
| FT-064 | Equipment interface: HL7 connection to auto-analysers (Cobas, Mindray, Sysmex) | Laboratory (LIS) | Medium | L | Medium | Must | 1 | Auto-analyser integration eliminates manual result transcription and associated errors. |
| FT-065 | External lab referral (Lancet, CPHL) | Laboratory (LIS) | Medium | M | Medium | Must | 1 | Facilities without specialised equipment refer specimens to external labs; tracking referral status is essential. |

---

## Phase 2 Growth Features (Should Have)

Phase 2 expands clinical scope to inpatient care, maternity, immunisation, emergency, insurance, HR/payroll, HMIS reporting, inventory, full lab capabilities, radiology, dental, eye care, mortuary, referral management, medical records, financial accounting, and disease surveillance. Phase 2 gate criteria require Phase 1 in production with 10+ paying facilities and zero patient safety incidents (see `_context/metrics.md`).

| ID | Feature | Module | Priority | Effort | Value | MoSCoW | Phase | Rationale |
|---|---|---|---|---|---|---|---|---|
| FT-066 | Patient admission from OPD, emergency, or direct | IPD | Critical | M | High | Should | 2 | Admission is the gateway to all inpatient workflows; must support multiple admission sources. |
| FT-067 | Bed management: visual bed map per ward | IPD | High | L | High | Should | 2 | Visual bed map reduces bed assignment errors and enables real-time capacity monitoring. |
| FT-068 | Nursing notes: shift-by-shift with timestamps | IPD | High | M | High | Should | 2 | Shift-based nursing documentation is a legal and clinical standard for inpatient care. |
| FT-069 | Doctor's ward round notes with clinical progress | IPD | High | M | High | Should | 2 | Ward round documentation captures clinical decision-making and treatment adjustments. |
| FT-070 | Drug round: medication administration tracking (ordered, given, held, refused) | IPD | Critical | L | High | Should | 2 | Closed-loop medication administration tracking prevents missed doses and documents refusals. |
| FT-071 | Vital signs chart: graphical tracking over admission | IPD | High | M | High | Should | 2 | Trend visualisation enables early detection of clinical deterioration. |
| FT-072 | Fluid balance chart: intake and output | IPD | High | M | High | Should | 2 | Fluid balance monitoring is a nursing standard for surgical, renal, and critically ill patients. |
| FT-073 | Inpatient investigation requests | IPD | High | S | High | Should | 2 | Extends electronic ordering from OPD to inpatient setting; same lab/radiology workflow. |
| FT-074 | Transfer between wards with receiving nurse acknowledgment | IPD | High | M | High | Should | 2 | Ward transfer requires formal handoff to prevent information loss at care transitions. |
| FT-075 | Discharge: summary, letter generation, DAMA recording | IPD | Critical | L | High | Should | 2 | Discharge summary is a legal document; DAMA (Discharge Against Medical Advice) recording protects the facility. |
| FT-076 | Inpatient billing: real-time charge accumulation | IPD | Critical | M | High | Should | 2 | Running bill for inpatients must accumulate charges in real time to prevent revenue leakage at discharge. |
| FT-077 | Patient census: live count per ward | IPD | High | S | Medium | Should | 2 | Bed occupancy data feeds capacity planning, staffing decisions, and HMIS reporting. |
| FT-078 | Africa-first IPD: HMIS 108 auto-populated, DRG mapping, paediatric weight-based dosing | IPD | High | L | High | Should | 2 | HMIS 108 is mandatory for government and government-aided hospitals; DRG mapping supports insurance claims. |
| FT-079 | Rapid triage with AVPU/GCS | Emergency (A&E) | Critical | M | High | Should | 2 | Emergency triage determines treatment priority; AVPU/GCS scores are standard neurological assessments. |
| FT-080 | Emergency patient registration: minimal required fields | Emergency (A&E) | Critical | S | High | Should | 2 | Emergency patients cannot wait for full registration; minimal fields enable rapid clinical access. |
| FT-081 | Resuscitation record, trauma assessment | Emergency (A&E) | High | M | High | Should | 2 | Structured trauma documentation supports clinical handoff and legal defence. |
| FT-082 | Emergency orders with URGENT flag | Emergency (A&E) | High | S | High | Should | 2 | URGENT flag prioritises emergency lab and pharmacy orders above routine OPD queue. |
| FT-083 | Time tracking: arrival, triage, seen, disposition | Emergency (A&E) | High | M | High | Should | 2 | Time-to-treatment metrics are quality indicators for emergency departments. |
| FT-084 | Mass casualty mode with START triage | Emergency (A&E) | Medium | L | Medium | Should | 2 | Mass casualty events (RTAs, building collapse) require simplified triage and resource allocation. |
| FT-085 | Africa-first Emergency: RTA coding, police notification flag, generator/power failure mode | Emergency (A&E) | High | M | High | Should | 2 | Road traffic accidents are a leading cause of emergency admission in Uganda; power failure mode ensures continuity. |
| FT-086 | ANC registration with gestational age and EDD | Maternity | Critical | M | High | Should | 2 | ANC registration initiates the maternal health workflow; gestational age and EDD drive visit scheduling. |
| FT-087 | ANC visit recording (ANC1-ANC8+) | Maternity | High | M | High | Should | 2 | WHO recommends 8+ ANC contacts; structured visit recording tracks compliance and flags missed visits. |
| FT-088 | ANC risk assessment for high-risk pregnancies | Maternity | Critical | M | High | Should | 2 | Early identification of high-risk pregnancies reduces maternal and neonatal mortality. |
| FT-089 | Labour admission with partograph (cervicogram, vitals, FHR, contractions) | Maternity | Critical | L | High | Should | 2 | The partograph is the WHO-recommended tool for labour monitoring; digital partograph improves completion rates. |
| FT-090 | Delivery record: mode, outcome, birth weight, APGAR | Maternity | Critical | M | High | Should | 2 | Birth outcome data feeds HMIS reporting, neonatal care, and maternal mortality surveillance. |
| FT-091 | Newborn record linked to mother, neonatal assessment, immunisation at birth | Maternity | Critical | M | High | Should | 2 | Mother-baby linkage is essential for neonatal care continuity and birth-dose immunisation tracking. |
| FT-092 | Postnatal visits (PNC1-PNC3) | Maternity | High | M | High | Should | 2 | Postnatal visits detect complications in the critical 42-day postpartum period. |
| FT-093 | Family planning | Maternity | High | M | Medium | Should | 2 | Family planning integration within maternity improves uptake and reduces unintended pregnancies. |
| FT-094 | Africa-first Maternity: HMIS 105 Section 4, EmONC tracking, PMTCT, Mother Baby Pair linkage | Maternity | High | L | High | Should | 2 | EmONC signal functions and PMTCT are WHO/MoH requirements for maternity services. |
| FT-095 | Uganda EPI schedule pre-loaded | Immunisation | High | S | High | Should | 2 | Pre-loaded national schedule eliminates manual configuration and reduces setup errors. |
| FT-096 | Vaccine administration: date, name, batch, dose, site | Immunisation | High | M | High | Should | 2 | Structured vaccine recording enables adverse event tracing and dose verification. |
| FT-097 | Missed vaccine alerts with SMS reminders | Immunisation | High | M | High | Should | 2 | Defaulter tracing via SMS improves immunisation coverage rates. |
| FT-098 | Cold chain records, vaccination certificates | Immunisation | Medium | M | Medium | Should | 2 | Cold chain documentation is a quality assurance requirement; certificates are needed for travel and school entry. |
| FT-099 | Defaulter tracing, AEFI reporting | Immunisation | High | M | High | Should | 2 | Adverse Event Following Immunisation reporting is a WHO pharmacovigilance requirement. |
| FT-100 | Africa-first Immunisation: Uganda EPI schedule, COVID-19 tracking, HPV campaigns, DHIS2 Tracker upload | Immunisation | High | M | High | Should | 2 | DHIS2 Tracker integration is required for national immunisation programme reporting. |
| FT-101 | Scheme register (NHIS, AAR, Jubilee, Prudential, etc.) | Insurance | High | M | High | Should | 2 | Uganda has 20+ active insurance schemes; each has different benefit schedules, claim formats, and pre-auth rules. |
| FT-102 | Member verification, benefit schedule | Insurance | High | M | High | Should | 2 | Real-time member verification prevents billing for ineligible patients and reduces claim rejections. |
| FT-103 | Pre-authorisation, claim generation and submission | Insurance | Critical | L | High | Should | 2 | Pre-authorisation is mandatory for most insured admissions; electronic claims reduce processing time from weeks to days. |
| FT-104 | Rejection management, credit reconciliation | Insurance | High | M | High | Should | 2 | Insurance claim rejections require structured follow-up; unresolved rejections are revenue leakage. |
| FT-105 | Africa-first Insurance: NHIS Uganda, corporate medical covers, mission insurance | Insurance | High | M | High | Should | 2 | NHIS integration is a strategic requirement as Uganda rolls out national health insurance. |
| FT-106 | Staff directory, qualification and licence records | HR/Payroll | High | M | High | Should | 2 | Staff credential management is a regulatory requirement; licence expiry alerts prevent unlicensed practice. |
| FT-107 | Licence expiry alerts, attendance, leave | HR/Payroll | High | M | High | Should | 2 | Automated licence expiry alerts prevent regulatory non-compliance; attendance feeds payroll calculations. |
| FT-108 | Payroll: PAYE, NSSF per Uganda statutory | HR/Payroll | High | L | High | Should | 2 | Statutory deductions (PAYE, NSSF) must be calculated per current Uganda Revenue Authority and NSSF rates. |
| FT-109 | Duty roster, staff productivity | HR/Payroll | Medium | M | Medium | Should | 2 | Roster management ensures adequate staffing; productivity metrics inform capacity planning. |
| FT-110 | Africa-first HR: UMDPC/UNMC/PHLB licence tracking, Uganda PAYE/NSSF | HR/Payroll | High | M | High | Should | 2 | Licence tracking per professional body (UMDPC for doctors, UNMC for nurses, PHLB for lab) is Uganda-specific. |
| FT-111 | HMIS 105, 108, 033b auto-populated | HMIS Reporting | Critical | L | High | Should | 2 | HMIS monthly reporting is mandatory for all Uganda health facilities; auto-population eliminates manual compilation. |
| FT-112 | Report validation, DHIS2 upload (export or API push) | HMIS Reporting | Critical | L | High | Should | 2 | DHIS2 is the national health data warehouse; electronic upload replaces manual data entry at the district level. |
| FT-113 | Reporting calendar, DHO portal | HMIS Reporting | Medium | M | Medium | Should | 2 | Reporting calendar tracks submission deadlines; DHO portal enables district-level data access. |
| FT-114 | Africa-first HMIS: All Uganda HMIS forms, PEPFAR MER indicators, IDSR | HMIS Reporting | High | L | High | Should | 2 | Comprehensive HMIS form coverage and PEPFAR MER indicator generation are competitive differentiators. |
| FT-115 | Multi-store: main, pharmacy, theatre, ward, dental | Inventory | High | L | High | Should | 2 | Healthcare facilities manage multiple stores with different stock categories and access controls. |
| FT-116 | GRN, stock transfer, adjustment, minimum/maximum levels | Inventory | High | L | High | Should | 2 | Core inventory operations; minimum/maximum levels trigger reorder alerts and prevent stockouts. |
| FT-117 | Expiry management, NMS ordering, procurement workflow | Inventory | High | L | High | Should | 2 | NMS is the primary supplier for government facilities; procurement workflow supports the full ordering cycle. |
| FT-118 | Africa-first Inventory: NMS commodity codes, PEPFAR commodity tracking, LMIS export, Essential Medicines List | Inventory | High | M | High | Should | 2 | NMS commodity codes and PEPFAR tracking are integration requirements for government and donor-funded facilities. |
| FT-119 | Radiology request from clinical screen | Radiology | High | M | High | Should | 2 | Electronic radiology ordering eliminates paper request forms and enables digital results delivery. |
| FT-120 | Worklist management for radiographer | Radiology | High | M | Medium | Should | 2 | Worklist management organises examination queue and tracks pending reports. |
| FT-121 | Report entry with structured templates per modality | Radiology | High | M | High | Should | 2 | Structured reporting templates improve report consistency and enable data extraction for analytics. |
| FT-122 | Africa-first Radiology: Ultrasound-first workflow, HMIS 105 Section 3, portable ultrasound integration | Radiology | High | M | High | Should | 2 | Ultrasound is the dominant imaging modality in SSA; workflow must prioritise it over CT/MRI. |
| FT-123 | 32-tooth graphical chart, periodontal chart | Dental | Medium | L | Medium | Should | 2 | Visual tooth chart is the standard dental documentation method; enables treatment planning. |
| FT-124 | Dental treatment planning with cost estimates | Dental | Medium | M | Medium | Should | 2 | Treatment plans with cost estimates improve patient communication and revenue forecasting. |
| FT-125 | Dental procedure recording linked to billing | Dental | Medium | M | Medium | Should | 2 | Procedure-to-billing linkage prevents revenue leakage from dental services. |
| FT-126 | Africa-first Dental: HMIS 105 Section 7 | Dental | Medium | S | Medium | Should | 2 | HMIS 105 Section 7 reporting is required for facilities offering dental services. |
| FT-127 | Visual acuity, refraction, optical prescription | Eye Care | Medium | M | Medium | Should | 2 | Core ophthalmology examination workflow; optical prescription drives dispensing. |
| FT-128 | Slit lamp, fundoscopy, IOP | Eye Care | Medium | M | Medium | Should | 2 | Specialised ophthalmic examination recording for glaucoma and retinal disease. |
| FT-129 | Optical dispensing linked to inventory | Eye Care | Medium | M | Medium | Should | 2 | Optical dispensing with stock deduction ensures accurate lens inventory management. |
| FT-130 | Africa-first Eye Care: HMIS 105 Section 8 | Eye Care | Medium | S | Medium | Should | 2 | HMIS 105 Section 8 reporting is required for facilities offering eye care services. |
| FT-131 | Death notification, cause of death (ICD-10) | Mortuary | High | M | High | Should | 2 | Death notification is a legal requirement; ICD-10 cause of death coding feeds mortality surveillance. |
| FT-132 | Death certificate, body storage, autopsy | Mortuary | High | M | Medium | Should | 2 | Death certificate generation and body storage tracking are legal and operational requirements. |
| FT-133 | Africa-first Mortuary: MPDSR, NIRA notification, HMIS 108 deaths | Mortuary | High | M | High | Should | 2 | Maternal and Perinatal Death Surveillance and Response is a WHO/MoH requirement; NIRA notification is legal. |
| FT-134 | Internal and external referral with electronic letter | Referral Management | High | M | High | Should | 2 | Electronic referral letters reduce information loss at care transitions within the health system hierarchy. |
| FT-135 | Referral register, outcome tracking | Referral Management | Medium | M | Medium | Should | 2 | Outcome tracking closes the referral loop and enables referral quality monitoring. |
| FT-136 | Africa-first Referral: Uganda health system referral hierarchy (HC II to National Referral) | Referral Management | High | M | High | Should | 2 | Uganda's tiered health system (HC II, III, IV, General Hospital, Regional Referral, National Referral) drives referral pathways. |
| FT-137 | Paper file tracking, movement log | Medical Records | Medium | M | Medium | Should | 2 | Hybrid paper-digital facilities need to track physical file location to prevent missing records. |
| FT-138 | Missing file report, discharge summary archive | Medical Records | Medium | M | Medium | Should | 2 | Missing file reports trigger retrieval; discharge summary archive supports continuity of care. |
| FT-139 | Medical certificates | Medical Records | Medium | S | Medium | Should | 2 | Sick leave and fitness certificates are frequently requested by patients for employers and schools. |
| FT-140 | Africa-first Medical Records: HMIS form inventory, NIRA birth notification | Medical Records | Medium | M | Medium | Should | 2 | NIRA birth notification is a legal requirement under Uganda's Registration of Persons Act. |
| FT-141 | Simple Mode accounting: money received, spent, outstanding claims, daily summary | Financial Accounting | High | L | High | Should | 2 | Small clinics need basic financial tracking without double-entry complexity. |
| FT-142 | Advanced Mode: chart of accounts, double-entry, trial balance, income statement, balance sheet | Financial Accounting | Medium | XL | High | Should | 2 | Larger hospitals require full financial statements for audit, board reporting, and tax compliance. |
| FT-143 | Healthcare chart of accounts pre-loaded | Financial Accounting | Medium | S | Medium | Should | 2 | Pre-loaded chart of accounts reduces setup time and ensures healthcare-appropriate account structure. |
| FT-144 | Insurance receivables ledger, auto-posting rules | Financial Accounting | High | L | High | Should | 2 | Insurance receivables are a major revenue category; auto-posting from claims reduces manual journal entries. |
| FT-145 | Donor fund accounting: ring-fenced cost centres | Financial Accounting | High | M | High | Should | 2 | PEPFAR and Global Fund require ring-fenced fund accounting with cost centre reporting. |
| FT-146 | Africa-first Accounting: Capitation grant tracking, NSSF/PAYE remittance, donor fund ring-fencing | Financial Accounting | High | M | High | Should | 2 | Capitation grant tracking is specific to Uganda's government health facility funding model. |
| FT-147 | Priority disease tracking with threshold alerts | Disease Surveillance | High | M | High | Should | 2 | Threshold-based alerts enable early outbreak detection for the 57 IDSR-notifiable diseases. |
| FT-148 | Outbreak flagging, weekly surveillance data | Disease Surveillance | High | M | High | Should | 2 | Weekly IDSR reporting and outbreak flagging are mandatory public health requirements. |
| FT-149 | Notifiable disease alerts | Disease Surveillance | High | M | High | Should | 2 | Automated alerts for notifiable diseases ensure timely reporting to the District Rapid Response Team. |
| FT-150 | Africa-first Surveillance: Uganda IDSR 57 diseases, One Health, DRRT notification | Disease Surveillance | High | M | High | Should | 2 | Uganda's IDSR programme covers 57 priority diseases with weekly reporting and immediate notification thresholds. |
| FT-151 | PACS integration for DICOM image management | Radiology | Medium | XL | Medium | Should | 2 | PACS integration enables digital image storage and retrieval; deferred to Phase 2 due to infrastructure requirements. |

---

## Phase 3 Programme Features (Could Have for MVP)

Phase 3 extends the platform to vertical health programmes (HIV/AIDS, TB), patient engagement (patient app, CHW app), interoperability (FHIR API), telemedicine, nutrition, community health, and social determinants. Phase 3 gate criteria require FHIR R4 conformance tested against ONC criteria and PEPFAR MER indicators validated with less than 1% variance (see `_context/metrics.md`).

| ID | Feature | Module | Priority | Effort | Value | MoSCoW | Phase | Rationale |
|---|---|---|---|---|---|---|---|---|
| FT-152 | HIV testing and counselling, programme enrolment | HIV/AIDS Programme | Critical | M | High | Could | 3 | HIV programme enrolment initiates the ART care cascade; Uganda has 1.4 million PLHIV. |
| FT-153 | ART initiation: WHO staging, CD4, regimen | HIV/AIDS Programme | Critical | L | High | Could | 3 | ART initiation data drives PEPFAR TX_NEW indicator and clinical treatment monitoring. |
| FT-154 | ARV dispensing with adherence tracking | HIV/AIDS Programme | Critical | L | High | Could | 3 | ARV adherence tracking feeds PEPFAR reporting and triggers defaulter interventions. |
| FT-155 | Viral load tracking with suppression status | HIV/AIDS Programme | Critical | M | High | Could | 3 | Viral load suppression (TX_PVLS) is the primary PEPFAR treatment outcome indicator. |
| FT-156 | PMTCT, missed appointment tracking | HIV/AIDS Programme | High | M | High | Could | 3 | PMTCT prevents mother-to-child HIV transmission; missed appointment tracking reduces loss to follow-up. |
| FT-157 | Africa-first HIV: Uganda MoH ART card, PEPFAR indicators (TX_CURR, TX_NEW, TX_PVLS), HMIS 105 Section 5, UgandaEMR+ integration | HIV/AIDS Programme | High | L | High | Could | 3 | PEPFAR indicator generation is the primary requirement for implementing partner adoption. |
| FT-158 | TB case registration, treatment regimen | TB Programme | High | M | High | Could | 3 | TB programme registration initiates the treatment workflow; Uganda has 90,000+ new TB cases annually. |
| FT-159 | DOT tracking, sputum/culture/GeneXpert results | TB Programme | High | M | High | Could | 3 | Directly Observed Therapy tracking improves treatment completion rates and feeds programme reporting. |
| FT-160 | Treatment outcome recording | TB Programme | High | M | High | Could | 3 | Treatment outcomes (cured, completed, failed, defaulted, died) are mandatory NTLP reporting indicators. |
| FT-161 | Contact tracing | TB Programme | High | M | High | Could | 3 | TB contact tracing identifies exposed individuals for screening; WHO End TB Strategy requirement. |
| FT-162 | Africa-first TB: NTLP quarterly report, MDR-TB management | TB Programme | High | M | High | Could | 3 | NTLP quarterly reports and MDR-TB management are specific to Uganda's TB programme requirements. |
| FT-163 | FHIR R4 native API | Interoperability | Critical | XL | High | Could | 3 | FHIR R4 API enables integration with national health information exchanges and third-party applications. |
| FT-164 | SMART on FHIR for third-party app substitutability | Interoperability | Medium | L | Medium | Could | 3 | SMART on FHIR enables authorised third-party apps to access clinical data through a standardised framework. |
| FT-165 | FHIR HTML narrative fallback | Interoperability | Medium | M | Medium | Could | 3 | HTML narrative in FHIR responses ensures clinical safety when receiving systems cannot process structured data (Rowlands Ch 46). |
| FT-166 | VHT records, community referral tracking | Community Health | High | M | High | Could | 3 | Village Health Team data capture extends Medic8's reach to community-level care delivery. |
| FT-167 | Community health events, home visits | Community Health | Medium | M | Medium | Could | 3 | Home visit recording supports CHW supervision and programme monitoring. |
| FT-168 | CHW Android app | Community Health | High | XL | High | Could | 3 | Simplified Android app for CHWs on low-end devices over 2G serves as a go-to-market channel for government/NGO contracts. |
| FT-169 | Africa-first Community Health: Uganda VHT programme, DHIS2 Tracker CHW data | Community Health | High | M | High | Could | 3 | DHIS2 Tracker integration is required for national community health programme reporting. |
| FT-170 | Personal health record: visits, diagnoses, treatments, investigations | Patient App | High | L | High | Could | 3 | Patient access to their own health records improves engagement and supports continuity across facilities. |
| FT-171 | Test results, appointments, fee balance, payment history | Patient App | High | M | High | Could | 3 | Self-service access to results and billing reduces phone calls to the facility and improves patient satisfaction. |
| FT-172 | Mobile money payment from app | Patient App | High | M | High | Could | 3 | In-app mobile money payment enables patients to pay bills without visiting the facility. |
| FT-173 | Medication reminders, immunisation schedule | Patient App | High | M | High | Could | 3 | Automated medication and immunisation reminders improve adherence and reduce missed doses. |
| FT-174 | Health education, secure messaging | Patient App | Medium | M | Medium | Could | 3 | Health education content and secure clinician messaging enhance patient engagement. |
| FT-175 | Multiple family members, offline access | Patient App | Medium | L | Medium | Could | 3 | Family member profiles enable parents to manage children's health records from a single account. |
| FT-176 | Africa-first Patient App: Android-first, data-lite mode, USSD/SMS fallback, Luganda interface, low-spec device support | Patient App | High | L | High | Could | 3 | Data-lite mode and USSD fallback are essential for reaching patients with limited internet and low-end devices. |
| FT-177 | Nutritional assessment (MUAC, WHZ) | Nutrition | High | M | High | Could | 3 | MUAC and Weight-for-Height Z-scores are the WHO standard for malnutrition classification. |
| FT-178 | SAM/MAM classification, CMAM enrolment | Nutrition | High | M | High | Could | 3 | Community Management of Acute Malnutrition enrolment triggers therapeutic feeding protocols. |
| FT-179 | RUTF dispensing, counselling | Nutrition | Medium | M | Medium | Could | 3 | Ready-to-Use Therapeutic Food dispensing tracking supports programme commodity accountability. |
| FT-180 | Africa-first Nutrition: HMIS nutrition section, RUTF tracking | Nutrition | Medium | M | Medium | Could | 3 | HMIS nutrition reporting and RUTF commodity tracking are programme reporting requirements. |
| FT-181 | Store-and-forward telemedicine for dermatology, radiology, pathology | Telemedicine | Medium | L | High | Could | 3 | Store-and-forward telemedicine reduces unnecessary referrals by 68% (Coiera Ch 21); high value for rural facilities. |
| FT-182 | ICD-10 Z-codes for social determinants of health | SDoH Integration | Medium | M | Medium | Could | 3 | SDoH coding captures housing, food security, and education factors that account for 40% of health outcomes. |

---

## Phase 4 Enterprise Features (Won't in MVP)

Phase 4 targets hospital networks, national referral hospitals, and enterprise-grade capabilities: theatre/surgical management, blood bank, PACS, ambulance management, physiotherapy, multi-facility Director platform, and advanced analytics. Phase 4 gate criteria require 50+ active facilities, insurance claims validated with 3+ insurers, and enterprise SLA defined (see `_context/metrics.md`).

| ID | Feature | Module | Priority | Effort | Value | MoSCoW | Phase | Rationale |
|---|---|---|---|---|---|---|---|---|
| FT-183 | Theatre booking, schedule, pre-op checklist | Theatre/Surgical | High | L | High | Won't | 4 | Theatre management is required for hospitals performing elective and emergency surgery. |
| FT-184 | Operation notes, anaesthesia record | Theatre/Surgical | High | L | High | Won't | 4 | Structured operative notes and anaesthesia records are legal and clinical documentation requirements. |
| FT-185 | Surgical count (swab, instrument, needle) | Theatre/Surgical | Critical | M | High | Won't | 4 | Surgical count verification prevents retained foreign objects — a patient safety event. |
| FT-186 | Theatre billing | Theatre/Surgical | High | M | High | Won't | 4 | Theatre procedures are high-value billing items; accurate capture prevents significant revenue leakage. |
| FT-187 | Africa-first Theatre: HMIS 108 surgical section, EmONC CS tracking | Theatre/Surgical | High | M | High | Won't | 4 | EmONC caesarean section tracking is a WHO signal function indicator for comprehensive emergency obstetric care. |
| FT-188 | Blood request, cross-match, issue | Blood Bank | High | L | High | Won't | 4 | Blood transfusion workflow requires cross-match verification before issue — a patient safety requirement. |
| FT-189 | Transfusion administration and reaction recording | Blood Bank | High | M | High | Won't | 4 | Transfusion reaction recording is a haemovigilance requirement; enables adverse event tracking. |
| FT-190 | Blood stock management | Blood Bank | Medium | M | Medium | Won't | 4 | Blood products have short shelf lives and strict storage requirements; stock management prevents wastage. |
| FT-191 | Africa-first Blood Bank: UBTS integration, haemovigilance | Blood Bank | Medium | M | Medium | Won't | 4 | Uganda Blood Transfusion Service integration ensures compliance with national blood safety standards. |
| FT-192 | Ambulance fleet register, trip log, pre-hospital care | Ambulance | Medium | L | Medium | Won't | 4 | Fleet management and pre-hospital care documentation support ambulance service operations. |
| FT-193 | Patient handover, GPS tracking | Ambulance | Medium | M | Medium | Won't | 4 | GPS tracking enables dispatch optimisation; patient handover documentation ensures continuity of care. |
| FT-194 | Africa-first Ambulance: KCCA integration, USSD ambulance request | Ambulance | Medium | M | Medium | Won't | 4 | KCCA ambulance integration is specific to Kampala; USSD request enables ambulance calling without a smartphone. |
| FT-195 | Physiotherapy referral, assessment, treatment plan | Physiotherapy | Medium | M | Medium | Won't | 4 | Physiotherapy workflow supports rehabilitation services at larger hospitals. |
| FT-196 | Session notes, programme tracking | Physiotherapy | Medium | M | Medium | Won't | 4 | Treatment programme tracking monitors patient progress across multiple physiotherapy sessions. |
| FT-197 | Africa-first Physiotherapy: WHO RHIS rehabilitation indicators | Physiotherapy | Low | S | Low | Won't | 4 | WHO rehabilitation indicators are relevant only for facilities with formal physiotherapy departments. |
| FT-198 | Multi-site Director platform: consolidated reporting | Director Platform | High | XL | High | Won't | 4 | Hospital networks require cross-facility dashboards for financial, clinical, and operational metrics. |
| FT-199 | Advanced AI analytics | Analytics | High | XL | High | Won't | 4 | Predictive analytics for patient flow, revenue forecasting, and clinical outcome trends differentiate enterprise tier. |
| FT-200 | RPA-ready task automation layer for billing/claims | Automation | Medium | L | Medium | Won't | 4 | Bot-driven claims follow-up automates repetitive insurance reconciliation tasks (Volpe Ch 9). |
| FT-201 | Drug supply chain hash-chain for counterfeit detection | Supply Chain | Medium | XL | Medium | Won't | 4 | Counterfeit medicines are a major SSA problem; lightweight blockchain for pharmacy stock provenance. |
| FT-202 | India market entry: HL7 v2.5, CDA, DICOM support | International Expansion | Low | XL | Medium | Won't | 4 | India's fragmented market has no entrenched competitor; requires HL7 v2.5 and CDA compliance (Sinha Ch 25). |

---

## Literature-Driven Features

Features derived from the 10 health informatics books analysed in `_context/literature-insights.md` that are not present in the original feature specification but address documented gaps in clinical safety, data quality, and adoption. Each feature is grounded in peer-reviewed evidence or expert consensus.

| ID | Feature | Module | Priority | Effort | Value | MoSCoW | Phase | Rationale |
|---|---|---|---|---|---|---|---|---|
| FT-203 | Four-tier CDS alert architecture (Info/Warning/Serious/Fatal) with override logging and per-facility override rate tracking | Clinical Decision Support | Critical | L | High | Must | 1 | Binary on/off alerts produce 90%+ override rates; tiered severity with logged overrides reduces alert fatigue while maintaining safety (Rowlands Ch 44, Volpe Ch 5). |
| FT-204 | Tall Man Lettering for look-alike/sound-alike drugs (e.g., hydrOXYzine vs hydrALAZINE) | Pharmacy/Prescribing | High | M | High | Must | 1 | Look-alike drug name confusion causes medication errors; Tall Man Lettering is an ISMP-recommended safety practice, particularly critical in SSA where multiple generics share similar names (Volpe Ch 6). |
| FT-205 | Barcode Medication Administration (BCMA): scan patient wristband + drug barcode before administering | IPD/Drug Rounds | High | L | High | Should | 2 | BCMA closes the loop on the Five Rights of medication administration at the bedside; prevents wrong-patient and wrong-drug errors (Volpe Ch 6, Hussey Ch 3). |
| FT-206 | NEWS2 Early Warning Scores calibrated for Sub-Saharan Africa populations | IPD/Vital Signs | Critical | M | High | Should | 2 | Western NEWS2 thresholds produce false alerts in SSA populations (Wheeler et al. 2013, Blantyre); calibrated scoring improves specificity for clinical deterioration prediction (Rivas Ch 7). |
| FT-207 | FMEA (Failure Mode and Effects Analysis) framework for medication workflow safety | Clinical Safety | High | M | High | Must | 1 | FMEA's severity x occurrence x detection scoring identifies which medication workflow steps carry the highest error risk and prioritises safety controls accordingly (Lehmann Ch 29). |
| FT-208 | C-HOBIC minimum nursing dataset at admission, shift handover, and discharge | IPD/Nursing | High | M | High | Should | 2 | Standardised nursing data collection (functional status, continence, symptoms, safety outcomes) enables evidence-based staffing and quality benchmarking (Hussey Ch 3). |
| FT-209 | 14 Nursing Sensitive Outcomes as system quality indicators | IPD/Quality | High | M | High | Should | 2 | Each additional patient per nurse increases mortality by 7%; 10% more RN hours reduces pressure ulcers by 19% and sepsis by 15% — NSO tracking quantifies this relationship (Hussey Ch 9). |
| FT-210 | PRAPARE Social Determinants of Health screening embedded in patient intake | Patient Registration | Medium | M | High | Could | 3 | Social determinants account for 40% of health outcomes; PRAPARE is a validated SDoH screening tool for clinical settings (Volpe Ch 24). |
| FT-211 | Patient Activation Measure (PAM) scoring in patient portal | Patient App | Medium | M | Medium | Could | 3 | PAM scoring identifies patients who need more engagement support; gamification hooks improve portal adoption and self-management (Volpe Ch 2). |
| FT-212 | Downtime kit generation: pre-printable patient lists, medication sheets, census forms | Infrastructure | High | M | High | Must | 1 | Power and internet failures are routine in SSA; pre-generated offline forms ensure clinical continuity during system downtime (WHO Ch 4). |
| FT-213 | Parallel-run mode: printable ward sheets and MAR forms mirroring paper formats | Infrastructure | High | M | High | Must | 1 | Facilities transitioning from paper to digital need parallel-run capability; printable forms matching existing paper formats reduce adoption resistance (Rowlands Ch 50). |

---

## Feature Count Summary

| Phase | Category | Feature Count |
|---|---|---|
| Phase 1 | MVP (Must Have) | 65 |
| Phase 2 | Growth (Should Have) | 86 |
| Phase 3 | Programme (Could Have) | 31 |
| Phase 4 | Enterprise (Won't in MVP) | 20 |
| Literature | Literature-Driven Additions | 11 |

---

## FR-AI: AI Clinical Intelligence Module — Intelligent Healthcare Add-On

> **Positioning:** The AI Clinical Intelligence Module is a paid add-on sold separately from the core Medic8 subscription. It is off by default. Facility owners and medical directors activate it when they are ready to invest in predictive and decision-support intelligence. Every feature is described in terms that a medical director or hospital administrator will understand immediately.

> **Pricing (indicative):** Starter — UGX 200,000/month; Growth — UGX 600,000/month; Enterprise — UGX 1,500,000/month. All plans include a configurable monthly token budget. The system enforces the budget and alerts the facility owner at 80% consumption.

---

### AI Feature 1: Know Which Patients Are About to Deteriorate — Before It Is Too Late

**Who benefits:** Nurses, Medical Officers, Hospital Administrators.

**The problem it solves:** Manual bedside monitoring misses early warning signs. A patient's vitals may trend downward for 6 hours before anyone notices. By the time a clinical emergency is declared, the window for simple intervention has closed.

**What it does:** Every hour, the system scores every admitted patient on a modified Early Warning Score (EWS) using recorded vitals: blood pressure, temperature, pulse rate, SpO₂, respiratory rate, and GCS. Patients whose total EWS rises by 3 or more points compared to their previous score trigger an alert to the duty nurse and attending doctor with the patient's name, bed number, current EWS, and the component driving the largest increase. No clinical diagnosis is made — only the alert.

**Why facility owners pay for it:** Early deterioration alerts reduce ICU admissions and preventable deaths. Facilities using systematic early warning demonstrate better outcomes, which attracts donor funding and insurance contracts.

**Pricing tier:** Growth and above.

**FR-AI-001** — see SRS Section 4, FR-AI-001 for full technical specification.

---

### AI Feature 2: Differential Diagnosis Support for Overstretched Clinicians

**Who benefits:** Clinical officers, general practitioners, rotating doctors.

**The problem it solves:** A clinical officer in a rural health centre sees 80 patients per day. For uncommon presentations, they need a second opinion — which is rarely available in under-resourced settings.

**What it does:** After entering presenting symptoms, duration, and key vitals, the clinician clicks "Suggest Diagnoses." The system returns up to 5 ranked ICD-10 differential diagnoses with a brief rationale and the most differentiating investigation to confirm or exclude each. It is a decision aid — the clinician remains responsible for the final diagnosis and the system displays this disclaimer on every response.

**Why facility owners pay for it:** It reduces missed diagnoses, improves investigation ordering efficiency, and provides clinical support in under-resourced settings. NGO and government clients specifically request this for community health worker programmes.

**Pricing tier:** Growth and above.

**FR-AI-002** — see SRS Section 4, FR-AI-002 for full technical specification.

---

### AI Feature 3: Write the Clinical Note Summary Automatically

**Who benefits:** Doctors, clinical officers, discharge coordinators.

**The problem it solves:** A doctor seeing 60 patients per day spends 20–30% of consultation time writing notes. Notes written under time pressure are terse and miss key information. Referral letters and discharge summaries take 10–15 minutes each to write manually.

**What it does:** After a consultation, the doctor clicks "Summarise." The system generates a structured SOAP summary — Subjective, Objective, Assessment, Plan — from the free-text notes entered during the visit. The doctor reviews, edits if needed, and clicks Approve. Only the approved version is saved in the patient record. It also generates a draft referral letter or discharge summary on request.

**Why facility owners pay for it:** A doctor who saves 15 minutes per patient across 60 patients recovers 15 hours of clinical time per week — time that goes back to patients.

**Pricing tier:** Starter and above.

**FR-AI-003** — see SRS Section 4, FR-AI-003 for full technical specification.

---

### AI Feature 4: Know Which Drugs Will Run Out Before They Actually Do

**Who benefits:** Pharmacy managers, procurement officers, hospital administrators.

**The problem it solves:** Drug stockouts are discovered when a pharmacist reaches for a medication and finds an empty shelf. By then, patients have already been turned away or prescribed alternatives. Emergency procurement is expensive and slow.

**What it does:** Every morning, the system analyses current pharmacy stock levels against average daily consumption for the past 28 days, adjusted for seasonal disease patterns. It produces a Stockout Risk report: drugs with fewer than 14 days of stock remaining are flagged with the projected stockout date and a recommended order quantity calculated to cover 45 days of adjusted consumption. The procurement officer places the order before the stockout, not after.

**Why facility owners pay for it:** A single avoided stockout of an essential drug — antimalarials, ORS, or ARVs — more than pays for the entire AI module for a month. Donor-funded facilities are penalised for stockouts by their funders.

**Pricing tier:** Starter and above.

**FR-AI-004** — see SRS Section 4, FR-AI-004 for full technical specification.

---

### AI Feature 5: Detect a Disease Outbreak Before It Becomes a Crisis

**Who benefits:** Medical Officers, Public Health Officers, Hospital Directors.

**The problem it solves:** An unusual cluster of cases begins in one ward. By the time it is confirmed as an outbreak, the public health response has been delayed because no one was monitoring cross-patient patterns — only individual cases.

**What it does:** The system continuously monitors diagnosis patterns across all patients. When any ICD-10 diagnosis code appears more than 2 standard deviations above its 30-day baseline within a 72-hour window, it generates a Cluster Alert for the Medical Officer with the diagnosis, case count, baseline value, ratio, and geographic breakdown of patient districts. The Medical Officer decides how to respond.

**Why facility owners pay for it:** Early outbreak detection protects the community, protects the facility from being the documented source of an outbreak, and enables proactive Ministry of Health notification — which is a legal requirement under the Public Health Act.

**Pricing tier:** Enterprise only.

**FR-AI-005** — see SRS Section 4, FR-AI-005 for full technical specification.

---

### AI Clinical Intelligence Module Packaging Summary

| Feature | Starter (UGX 200K/mo) | Growth (UGX 600K/mo) | Enterprise (UGX 1.5M/mo) |
|---|---|---|---|
| Clinical Note Summarisation | Yes | Yes | Yes |
| Pharmacy Demand Forecasting | Yes | Yes | Yes |
| At-Risk Patient Early Warning | — | Yes | Yes |
| Differential Diagnosis Support | — | Yes | Yes |
| Disease Surveillance / Outbreak Detection | — | — | Yes |

**All features are off by default within the purchased plan.** The Medical Director enables each feature individually from the AI Module settings screen.
| **Total** | | **213** |
