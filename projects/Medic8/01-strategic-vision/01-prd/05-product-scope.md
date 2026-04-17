# 5 Product Scope

This section defines the functional boundary of the Medic8 platform. Every module listed here is in scope for the product across its 4-phase build sequence. Modules not listed are out of scope. This section is the authoritative module inventory that drives the downstream Software Requirements Specification (SRS), interface control documents, and test plans.

Tier key: All = all subscription tiers (Starter, Growth, Pro, Enterprise) | Pro+ = Pro and Enterprise only | Enterprise = Enterprise only

Phase key: 1 = Foundation (MVP, 6 months) | 2 = Expansion (12 months) | 3 = Programmes and Patient Engagement (18 months) | 4 = Advanced Specialty (24 months)

## 5.1 Module Summary Table

| # | Module | Category | Tier | Phase | Key Capability |
|---|--------|----------|------|-------|----------------|
| 1 | Patient Registration and Master Index | Core Clinical | All | 1 | Unified patient identity with biometric, NIN, and UNHCR ID lookup |
| 2 | Outpatient Department (OPD) | Core Clinical | All | 1 | SOAP consultation, ICD-10/11 diagnosis, stock-aware prescribing, AI Differential Diagnosis |
| 3 | Laboratory Information System (LIS) | Core Clinical | All | 1 | Sample tracking, result validation, auto-analyser interface, feeds AI Outbreak Early Warning |
| 4 | Pharmacy and Dispensary | Core Clinical | All | 1 | Dispensing with stock deduction, expiry tracking, NMS codes |
| 5 | Inpatient Department (IPD) and Ward Management | Core Clinical | All | 2 | Bed management, nursing notes, drug round, discharge workflow |
| 6 | Emergency Department (A&E) | Core Clinical | All | 2 | Rapid triage (AVPU/GCS), mass casualty mode, time tracking |
| 7 | Maternity, ANC and Reproductive Health | Core Clinical | All | 2 | ANC visits, partograph, delivery record, PMTCT |
| 8 | Immunisation and Vaccination | Core Clinical | All | 2 | Uganda EPI schedule, missed vaccine alerts, DHIS2 upload |
| 9 | Radiology and Imaging | Core Clinical | All | 2 | Worklist management, structured reporting, PACS integration |
| 10 | HIV/AIDS Programme Management | Specialty and Programme | All | 3 | ART initiation, viral load tracking, PEPFAR indicators |
| 11 | TB Programme Management | Specialty and Programme | All | 3 | Case registration, DOT tracking, contact tracing |
| 12 | Dental Services | Specialty and Programme | All | 2 | 32-tooth graphical chart, treatment planning, procedure billing |
| 13 | Eye Care and Optical | Specialty and Programme | All | 2 | Visual acuity, refraction, optical dispensing |
| 14 | Theatre and Surgical Management | Specialty and Programme | Pro+ | 4 | Theatre booking, operation notes, anaesthesia record |
| 15 | Blood Bank and Transfusion | Specialty and Programme | Pro+ | 4 | Cross-match, transfusion administration, haemovigilance |
| 16 | Mortuary Management | Specialty and Programme | All | 2 | Death notification, cause of death (ICD-10), MPDSR |
| 17 | Nutrition and Dietetics | Specialty and Programme | Pro+ | 3 | MUAC/WHZ assessment, CMAM enrolment, RUTF dispensing |
| 18 | Physiotherapy and Rehabilitation | Specialty and Programme | Pro+ | 4 | Referral, assessment, treatment plan, session tracking |
| 19 | Appointments and Scheduling | Administrative | All | 1 | Booking, SMS/WhatsApp reminders, walk-in integration |
| 20 | Referral Management | Administrative | All | 2 | Electronic referral letter, outcome tracking, referral hierarchy |
| 21 | Human Resource and Payroll | Administrative | All | 2 | Staff directory, licence tracking, payroll (PAYE/NSSF) |
| 22 | Medical Records and Health Information | Administrative | All | 2 | Paper file tracking, discharge archive, medical certificates, AI ICD Coding Assist |
| 23 | Ambulance Management | Administrative | Pro+ | 4 | Fleet register, trip log, GPS tracking, pre-hospital care |
| 24 | Billing and Revenue Management | Financial | All | 1 | Real-time charge accumulation, mobile money, daily reconciliation |
| 25 | Insurance Management | Financial | All | 2 | Scheme register, pre-authorisation, claim submission, AI Claim Scrubbing |
| 26 | Financial Accounting (Dual Mode) | Financial | All | 2 | Simple and advanced modes, donor fund ring-fencing |
| 27 | Inventory and Stores Management | Financial | All | 2 | Multi-store, GRN, expiry management, NMS ordering |
| 28 | Uganda HMIS Reporting | HMIS and Public Health | All | 2 | HMIS 105/108/033b auto-population, DHIS2 upload |
| 29 | Disease Surveillance and Outbreak Detection | HMIS and Public Health | All | 2 | Priority disease tracking, outbreak flagging, IDSR |
| 30 | Community Health Integration | HMIS and Public Health | Pro+ | 3 | VHT records, community referral, CHW Android app |
| 31 | Patient Portal and Mobile App | Patient Portal and Mobile | All | 3 | Personal health record, test results, mobile money payment, AI Patient Plain-Language Summary |
| 32 | AI Intelligence | AI Add-On | All (credit pack or flat fee, independent of clinical tier) | 2 | 6 tenant-configurable AI capabilities: Clinical Documentation, ICD Coding Assist, Differential Diagnosis, Patient Plain-Language Summary, Claim Scrubbing, Outbreak Early Warning |

Total: 32 modules across 7 categories, 4 build phases, and 3 tier levels.

---

## 5.2 Core Clinical Modules

### 1. Patient Registration and Master Index

**Category:** Core Clinical | **Tier:** All | **Phase:** 1

**Scope Statement:** The Patient Registration and Master Index module provides a single, authoritative source of patient identity across all facilities on the Medic8 platform. It captures demographics, biometric data, and multiple national identifiers, and exposes a global patient identity layer for cross-facility lookup.

**Key Capabilities:**

- Register new patients with demographics, contact details, next-of-kin, and photo capture.
- Support biometric registration via fingerprint or facial recognition hardware.
- Auto-generate a unique Medical Record Number (MRN) in a facility-configurable format.
- Look up returning patients by name, phone number, national ID, NIN, UNHCR ID, or fingerprint.
- Classify patients by category: adult, paediatric, staff, VIP, indigent/sponsored, or refugee.
- Store multiple identifiers per patient: NIN, passport, NIRA, UNHCR ID, insurance member number.
- Link guardian and next-of-kin records to paediatric patients.
- Merge duplicate patient records with a full audit trail.

**Africa-First Enhancements:**

- UNHCR Refugee ID as a first-class identifier for refugee-serving facilities.
- NIN integration with Uganda's National Identification and Registration Authority (NIRA).
- Mobile money (MoMo) phone number as a patient lookup field, reflecting the dominant payment and identity channel in East Africa.
- Multilingual registration form available in English, French, and Kiswahili.

**Interfaces:**

- Outpatient Department (OPD) — patient record feeds consultation workflow.
- Inpatient Department (IPD) — admission references the master patient index.
- Emergency Department (A&E) — rapid registration creates a minimal patient record.
- Billing and Revenue Management — patient account links to the MRN.
- Insurance Management — member verification references the patient record.
- Patient Portal and Mobile App — patient identity anchors the personal health record.
- Uganda HMIS Reporting — patient demographics feed HMIS form population.

**Out of Scope:**

- Clinical decision support (handled by OPD and Pharmacy modules).
- Insurance eligibility verification (handled by Insurance Management).
- Patient scheduling (handled by Appointments and Scheduling).
- Clinical documentation (handled by OPD, IPD, and specialty modules).

---

### 2. Outpatient Department (OPD)

**Category:** Core Clinical | **Tier:** All | **Phase:** 1

**Scope Statement:** The OPD module manages the end-to-end outpatient clinical workflow from triage through consultation, investigation ordering, prescribing, and referral. It is the primary daily workflow for most facilities, auto-captures data required for HMIS 105 reporting, and hosts the AI Clinical Documentation and AI Differential Diagnosis capabilities where enabled.

**Key Capabilities:**

- Capture triage vital signs: blood pressure, temperature, pulse, SpO2, weight, height, BMI, and MUAC.
- Maintain a real-time doctor's queue per doctor/room with triage priority and wait time.
- Record clinical consultations using SOAP notes in free-text and structured formats.
- Enter diagnoses using ICD-10 and ICD-11 codes with clinical descriptions.
- Request investigations (laboratory, radiology, ECG) with instant notification to the receiving department.
- Write prescriptions with generic and brand names, dose, frequency, duration, route, and quantity.
- Display pharmacy stock availability before the clinician saves the prescription (stock-aware prescribing).
- Check drug interactions with a 4-tier alert system: Info, Warning, Serious, Fatal.

**Africa-First Enhancements:**

- HMIS 105 data fields auto-captured during consultation without additional data entry.
- Malaria mRDT result field embedded in the consultation screen for high-endemicity settings.
- HIV status field for routine provider-initiated testing and counselling (PITC).
- MUAC screening integrated into triage for malnutrition detection.
- MOH 5 (Health Unit Outpatient Monthly Report) format compliance.

**Interfaces:**

- Patient Registration and Master Index — receives patient identity and demographics.
- Laboratory Information System (LIS) — sends investigation requests, receives results.
- Radiology and Imaging — sends imaging requests, receives reports.
- Pharmacy and Dispensary — sends prescriptions for dispensing.
- Billing and Revenue Management — auto-posts consultation and procedure charges.
- Inpatient Department (IPD) — transfers patient to admission when required.
- Appointments and Scheduling — books follow-up appointments from the consultation screen.
- Referral Management — generates referral letters.
- Uganda HMIS Reporting — feeds HMIS 105 aggregation.
- AI Intelligence — consumes AI Clinical Documentation (SOAP notes, referral letters) and AI Differential Diagnosis where the AI Intelligence module is enabled.

**Out of Scope:**

- Inpatient clinical documentation (handled by IPD).
- Pharmacy stock management and dispensing workflow (handled by Pharmacy and Dispensary).
- Laboratory sample processing and result entry (handled by LIS).
- Surgical procedures requiring theatre booking (handled by Theatre and Surgical Management).

**Localisation Flags:**

- `opd.triage.chief_complaint_label` — Kiswahili value: *malalamiko makuu* (contextually accurate). Literal translation *malalamiko ya kwanza* is clinically ambiguous and is prohibited.

---

### 3. Laboratory Information System (LIS)

**Category:** Core Clinical | **Tier:** All | **Phase:** 1

**Scope Statement:** The LIS module manages the laboratory workflow from test request through sample collection, processing, result entry, validation, and reporting. It interfaces with auto-analysers via HL7 and supports external lab referrals. LIS result data feeds the AI Outbreak Early Warning capability.

**Key Capabilities:**

- Receive lab requests from OPD, IPD, and Emergency.
- Generate barcode and QR labels for sample collection.
- Track specimen status through a defined workflow: requested, collected, received, processing, result ready.
- Enter results with reference ranges and auto-flag abnormal values (High, Low, Critical).
- Escalate critical value alerts to the ordering clinician.
- Validate results through a lab supervisor approval step.
- Record quality control data and generate Levey-Jennings charts.
- Interface with auto-analysers (Cobas, Mindray, Sysmex) via HL7.

**Africa-First Enhancements:**

- HMIS 105 Section 2 (Laboratory) data auto-populated from test results.
- Pre-configured test panels for malaria, HIV, syphilis, and pregnancy tests reflecting the highest-volume tests in the region.
- CD4 count tracking for HIV programme monitoring.
- GeneXpert TB result integration for tuberculosis diagnosis.

**Interfaces:**

- Outpatient Department (OPD) — receives test requests, returns results to the consultation screen.
- Inpatient Department (IPD) — receives inpatient test requests, returns results.
- Emergency Department (A&E) — receives urgent test requests with URGENT flag.
- Billing and Revenue Management — auto-posts test charges.
- HIV/AIDS Programme Management — feeds CD4 and viral load results.
- TB Programme Management — feeds GeneXpert and sputum results.
- Uganda HMIS Reporting — feeds HMIS 105 Section 2 data.
- AI Intelligence — LIS diagnosis result aggregation feeds the AI Outbreak Early Warning anomaly detection model.

**Out of Scope:**

- Radiology and imaging workflows (handled by Radiology and Imaging).
- Blood bank cross-matching and transfusion (handled by Blood Bank and Transfusion).
- Point-of-care test result entry by clinicians (handled by OPD consultation screen).

---

### 4. Pharmacy and Dispensary

**Category:** Core Clinical | **Tier:** All | **Phase:** 1

**Scope Statement:** The Pharmacy and Dispensary module manages the medication dispensing workflow, drug stock management, and formulary maintenance. It connects to the clinical prescribing workflow to ensure stock-aware dispensing and tracks controlled substances in a dedicated register.

**Key Capabilities:**

- Receive prescriptions from OPD, IPD, and Emergency into a dispensing queue.
- Dispense medications with automatic stock deduction.
- Support generic/brand substitution with notification to the prescribing clinician.
- Generate dispensing labels.
- Handle partial dispensing with a pending balance for out-of-stock items.
- Manage stock: goods received notes (GRN), inter-store transfers, adjustments, and returns.
- Flag items approaching expiry within 90 days.
- Alert on minimum stock levels.
- Maintain a drug formulary and a narcotic/controlled drug register.

**Africa-First Enhancements:**

- NMS (National Medical Stores) drug codes mapped to the formulary for government supply chain compatibility.
- LMIS (Logistics Management Information System) export for NMS ordering and reporting.
- ACT (Artemisinin-based Combination Therapy) tracking for malaria treatment compliance.
- ARV dispensing workflow integrated with the HIV/AIDS Programme Management module.
- PEPFAR commodity tracking for donor-funded drug supplies.

**Interfaces:**

- Outpatient Department (OPD) — receives prescriptions, provides stock availability data.
- Inpatient Department (IPD) — receives inpatient prescriptions and drug round orders.
- Emergency Department (A&E) — receives emergency prescriptions.
- Billing and Revenue Management — auto-posts dispensing charges.
- Inventory and Stores Management — shares stock data across multi-store configuration.
- HIV/AIDS Programme Management — feeds ARV dispensing and adherence data.
- Uganda HMIS Reporting — feeds pharmacy data to HMIS 105.

**Out of Scope:**

- Clinical prescribing decision support (handled by OPD drug interaction checks).
- Procurement and supplier management beyond NMS ordering (handled by Inventory and Stores Management).
- Blood product management (handled by Blood Bank and Transfusion).

---

### 5. Inpatient Department (IPD) and Ward Management

**Category:** Core Clinical | **Tier:** All | **Phase:** 2

**Scope Statement:** The IPD module manages patient admission, bed allocation, nursing and medical documentation, medication administration, and discharge. It provides real-time bed visibility and charge accumulation throughout the admission. AI Clinical Documentation generates discharge summaries for clinician review and approval.

**Key Capabilities:**

- Admit patients from OPD, Emergency, or direct admission.
- Display a visual bed map per ward for bed management.
- Record nursing notes shift-by-shift with timestamps.
- Record doctor's ward round notes with clinical progress.
- Track medication administration through the drug round: ordered, given, held, refused.
- Display graphical vital signs tracking over the course of admission.
- Maintain a fluid balance chart (intake and output).
- Generate discharge summaries and letters, record DAMA (Discharge Against Medical Advice).

**Africa-First Enhancements:**

- HMIS 108 (Inpatient Monthly Report) auto-populated from admission and discharge data.
- DRG (Diagnosis-Related Group) mapping for facilities implementing case-based financing.
- Paediatric weight-based dosing calculations integrated into the drug round workflow.

**Interfaces:**

- Patient Registration and Master Index — references the master patient index at admission.
- Outpatient Department (OPD) — receives admission transfers from OPD.
- Emergency Department (A&E) — receives emergency admissions.
- Laboratory Information System (LIS) — sends inpatient investigation requests, receives results.
- Radiology and Imaging — sends inpatient imaging requests, receives reports.
- Pharmacy and Dispensary — sends inpatient prescriptions and drug round orders.
- Billing and Revenue Management — feeds real-time charge accumulation.
- Maternity, ANC and Reproductive Health — handles maternity admissions and deliveries.
- Theatre and Surgical Management — sends patients to theatre, receives post-operative notes.
- Mortuary Management — handles death notifications from the ward.
- Uganda HMIS Reporting — feeds HMIS 108 data.
- AI Intelligence — AI Clinical Documentation generates discharge summary drafts for clinician review and explicit approval.

**Out of Scope:**

- Theatre scheduling and operation notes (handled by Theatre and Surgical Management).
- Neonatal intensive care unit (NICU) specialised workflows (future scope).
- Long-term care or rehabilitation ward management (handled by Physiotherapy and Rehabilitation for session-based care).

---

### 6. Emergency Department (A&E)

**Category:** Core Clinical | **Tier:** All | **Phase:** 2

**Scope Statement:** The Emergency Department module provides a rapid-registration, time-tracked workflow for acute and emergency patients. It supports mass casualty triage and operates with minimal required fields to avoid delays in life-threatening situations.

**Key Capabilities:**

- Perform rapid triage using AVPU and Glasgow Coma Scale (GCS).
- Register emergency patients with minimal required fields (name and sex sufficient).
- Record resuscitation events and trauma assessments.
- Flag emergency orders as URGENT for priority processing by laboratory and pharmacy.
- Track time points: arrival, triage, clinician seen, and disposition.
- Activate mass casualty mode with START (Simple Triage and Rapid Treatment) triage protocol.

**Africa-First Enhancements:**

- Road Traffic Accident (RTA) coding for facilities near major highways.
- Police notification flag for medico-legal cases.
- Generator and power failure mode enabling continued operation during power outages.

**Interfaces:**

- Patient Registration and Master Index — creates minimal patient records for unknown patients.
- Outpatient Department (OPD) — discharges stable patients to OPD follow-up.
- Inpatient Department (IPD) — admits emergency patients requiring inpatient care.
- Laboratory Information System (LIS) — sends urgent investigation requests.
- Pharmacy and Dispensary — sends emergency prescriptions.
- Billing and Revenue Management — auto-posts emergency charges.
- Maternity, ANC and Reproductive Health — handles obstetric emergencies.

**Out of Scope:**

- Pre-hospital ambulance care documentation (handled by Ambulance Management).
- Disaster management coordination beyond the facility's own mass casualty protocol.
- Forensic documentation for police cases (the system flags cases but does not generate police reports).

---

### 7. Maternity, ANC and Reproductive Health

**Category:** Core Clinical | **Tier:** All | **Phase:** 2

**Scope Statement:** The Maternity module manages the continuum of reproductive health from antenatal care through labour, delivery, postnatal care, and family planning. It links mother and newborn records and tracks emergency obstetric and neonatal care (EmONC) indicators.

**Key Capabilities:**

- Register ANC clients with gestational age and expected date of delivery (EDD).
- Record ANC visits (ANC1 through ANC8+) with structured visit data.
- Assess ANC risk for high-risk pregnancies.
- Manage labour admission with a digital partograph (cervicogram, vitals, fetal heart rate, contractions).
- Record delivery outcomes: mode, outcome, birth weight, APGAR scores.
- Create a newborn record linked to the mother with neonatal assessment and immunisation at birth.
- Record postnatal visits (PNC1 through PNC3).
- Manage family planning services and counselling.

**Africa-First Enhancements:**

- HMIS 105 Section 4 (Maternal Health) data auto-populated from ANC and delivery records.
- EmONC (Emergency Obstetric and Neonatal Care) signal function tracking.
- PMTCT (Prevention of Mother-to-Child Transmission) workflow for HIV-positive mothers.
- Mother-Baby Pair linkage for programmes tracking maternal and infant outcomes together.

**Interfaces:**

- Patient Registration and Master Index — creates both mother and newborn records.
- Inpatient Department (IPD) — handles maternity ward admissions.
- Emergency Department (A&E) — receives obstetric emergencies.
- Laboratory Information System (LIS) — sends ANC investigation requests (HIV, syphilis, haemoglobin).
- Pharmacy and Dispensary — dispenses ANC medications (iron, folic acid, ARVs for PMTCT).
- Immunisation and Vaccination — triggers immunisation at birth (BCG, OPV0).
- HIV/AIDS Programme Management — feeds PMTCT data.
- Billing and Revenue Management — auto-posts maternity charges.
- Uganda HMIS Reporting — feeds HMIS 105 Section 4 data.

**Out of Scope:**

- Gynaecological surgery (handled by Theatre and Surgical Management).
- Neonatal intensive care beyond initial newborn assessment (future scope).
- Assisted reproduction services (not in the Medic8 scope).

**Localisation Flags:**

- `maternity.registration.birth_attendant_label` — French: *accoucheuse*; Kiswahili: *mkunga*. These represent different professional categories per country context. Do not use generic "attendant."

---

### 8. Immunisation and Vaccination

**Category:** Core Clinical | **Tier:** All | **Phase:** 2

**Scope Statement:** The Immunisation module manages vaccine administration, schedule adherence, cold chain documentation, and adverse event reporting. It pre-loads the Uganda Expanded Programme on Immunisation (EPI) schedule and supports campaign-based vaccination.

**Key Capabilities:**

- Pre-load the Uganda EPI schedule with all routine childhood vaccines.
- Record vaccine administration: date, vaccine name, batch number, dose number, site.
- Generate alerts for missed vaccines with SMS reminders to caregivers.
- Maintain cold chain temperature records.
- Generate vaccination certificates.
- Trace defaulters who miss scheduled doses.
- Report Adverse Events Following Immunisation (AEFI).

**Africa-First Enhancements:**

- Uganda EPI schedule as the default immunisation calendar.
- COVID-19 vaccination tracking.
- HPV campaign vaccination support.
- DHIS2 Tracker upload for national immunisation data.

**Interfaces:**

- Patient Registration and Master Index — references the patient (child) and guardian records.
- Maternity, ANC and Reproductive Health — receives newborn records for birth-dose immunisation.
- Appointments and Scheduling — schedules follow-up vaccination appointments.
- Uganda HMIS Reporting — feeds immunisation data to HMIS 105.
- Patient Portal and Mobile App — displays immunisation schedule and sends reminders.

**Out of Scope:**

- Vaccine procurement and cold chain logistics beyond facility-level recording (national supply chain is external).
- Travel vaccination advisory services.
- Vaccine research and clinical trial management.

---

### 9. Radiology and Imaging

**Category:** Core Clinical | **Tier:** All | **Phase:** 2

**Scope Statement:** The Radiology module manages imaging requests, radiographer worklists, structured report entry, and PACS integration. It supports modality-specific report templates and prioritises ultrasound workflows given its prevalence in African healthcare settings.

**Key Capabilities:**

- Receive radiology requests from clinical screens (OPD, IPD, Emergency).
- Manage a radiographer worklist with request prioritisation.
- Enter radiology reports using structured templates per modality (X-ray, ultrasound, CT, MRI).
- Integrate with Picture Archiving and Communication Systems (PACS) for DICOM image storage and retrieval.

**Africa-First Enhancements:**

- Ultrasound-first workflow design reflecting the most common imaging modality in East African facilities.
- HMIS 105 Section 3 (Radiology) data auto-populated from completed reports.
- Portable ultrasound device integration for facilities without fixed imaging suites.

**Interfaces:**

- Outpatient Department (OPD) — receives imaging requests, returns reports.
- Inpatient Department (IPD) — receives inpatient imaging requests, returns reports.
- Emergency Department (A&E) — receives urgent imaging requests.
- Billing and Revenue Management — auto-posts imaging charges.
- Uganda HMIS Reporting — feeds HMIS 105 Section 3 data.

**Out of Scope:**

- Advanced imaging modalities (PET, nuclear medicine) — not present in the target market.
- Teleradiology with external radiologists (future scope).
- AI-assisted image interpretation (future scope).

---

## 5.3 Specialty and Programme Modules

### 10. HIV/AIDS Programme Management

**Category:** Specialty and Programme | **Tier:** All | **Phase:** 3

**Scope Statement:** The HIV/AIDS module manages the complete HIV care cascade from testing and counselling through ART initiation, adherence monitoring, viral load tracking, and PMTCT. It generates PEPFAR MER indicators and integrates with UgandaEMR+ for sites transitioning from legacy systems.

**Key Capabilities:**

- Record HIV testing and counselling (HTC) results.
- Enrol patients into the HIV care programme.
- Initiate ART with WHO clinical staging, CD4 count, and regimen selection.
- Dispense ARVs with adherence tracking (pill counts, visit adherence).
- Track viral load results and suppression status.
- Manage PMTCT for HIV-positive pregnant and breastfeeding women.
- Track missed appointments with defaulter tracing alerts.

**Africa-First Enhancements:**

- Uganda Ministry of Health ART card format for clinical documentation.
- PEPFAR MER indicators: TX_CURR (currently on treatment), TX_NEW (newly initiated), TX_PVLS (viral load suppression).
- HMIS 105 Section 5 (HIV/AIDS) data auto-populated.
- UgandaEMR+ integration for data exchange with PEPFAR-supported sites.

**Interfaces:**

- Patient Registration and Master Index — identifies HIV-enrolled patients.
- Outpatient Department (OPD) — HIV status field in the consultation screen.
- Laboratory Information System (LIS) — receives CD4 and viral load results.
- Pharmacy and Dispensary — sends ARV prescriptions, receives dispensing and adherence data.
- Maternity, ANC and Reproductive Health — receives PMTCT referrals.
- Uganda HMIS Reporting — feeds HMIS 105 Section 5 and PEPFAR MER indicators.
- Community Health Integration — receives community-level HTC and adherence data.

**Out of Scope:**

- HIV research and clinical trial management.
- Pre-Exposure Prophylaxis (PrEP) programme management (future scope).
- HIV self-test kit distribution tracking.

---

### 11. TB Programme Management

**Category:** Specialty and Programme | **Tier:** All | **Phase:** 3

**Scope Statement:** The TB module manages tuberculosis case registration, treatment regimens, directly observed therapy (DOT), and treatment outcomes. It supports contact tracing and generates the National Tuberculosis and Leprosy Programme (NTLP) quarterly report.

**Key Capabilities:**

- Register TB cases with classification (pulmonary, extra-pulmonary, new, relapse).
- Record treatment regimen with drug combinations and duration.
- Track DOT with daily administration records.
- Record sputum, culture, and GeneXpert results linked to the case.
- Document treatment outcomes (cured, completed, failed, died, lost to follow-up).
- Trace contacts of confirmed TB cases.

**Africa-First Enhancements:**

- NTLP quarterly report auto-generated from case data.
- MDR-TB (Multi-Drug Resistant TB) management workflow with second-line regimen tracking.

**Interfaces:**

- Patient Registration and Master Index — identifies TB-enrolled patients.
- Laboratory Information System (LIS) — receives GeneXpert, sputum smear, and culture results.
- Pharmacy and Dispensary — dispenses TB medications.
- HIV/AIDS Programme Management — manages TB/HIV co-infection cases.
- Uganda HMIS Reporting — feeds TB data to HMIS forms.
- Community Health Integration — receives community-level contact tracing data.

**Out of Scope:**

- Drug-susceptibility testing laboratory workflow (handled by LIS).
- TB vaccine research.
- MDR-TB hospitalisation workflow beyond treatment tracking (handled by IPD).

---

### 12. Dental Services

**Category:** Specialty and Programme | **Tier:** All | **Phase:** 2

**Scope Statement:** The Dental Services module provides a graphical tooth-charting interface, treatment planning with cost estimates, and procedure recording linked to the billing system. It supports the standard 32-tooth adult and paediatric dental charting.

**Key Capabilities:**

- Display a 32-tooth graphical chart with per-tooth condition recording.
- Record periodontal charting data.
- Create treatment plans with itemised cost estimates.
- Record dental procedures with automatic billing linkage.
- Maintain a dental visit history per patient.

**Africa-First Enhancements:**

- HMIS 105 Section 7 (Dental) data auto-populated from procedure records.

**Interfaces:**

- Patient Registration and Master Index — references the patient record.
- Billing and Revenue Management — auto-posts dental procedure charges.
- Pharmacy and Dispensary — sends prescriptions for dental medications.
- Appointments and Scheduling — books dental follow-up appointments.
- Uganda HMIS Reporting — feeds HMIS 105 Section 7 data.

**Out of Scope:**

- Orthodontic treatment planning and appliance tracking.
- Maxillofacial surgery (handled by Theatre and Surgical Management).
- Dental laboratory work order management.

---

### 13. Eye Care and Optical

**Category:** Specialty and Programme | **Tier:** All | **Phase:** 2

**Scope Statement:** The Eye Care module manages ophthalmic assessments (visual acuity, refraction, slit lamp, fundoscopy, intraocular pressure), optical prescription generation, and optical dispensing linked to inventory.

**Key Capabilities:**

- Record visual acuity measurements (Snellen/LogMAR).
- Perform refraction and generate optical prescriptions.
- Record slit lamp examination findings.
- Record fundoscopy findings.
- Measure and record intraocular pressure (IOP).
- Dispense optical items (spectacles, contact lenses) linked to inventory.

**Africa-First Enhancements:**

- HMIS 105 Section 8 (Eye Care) data auto-populated from ophthalmic records.

**Interfaces:**

- Patient Registration and Master Index — references the patient record.
- Billing and Revenue Management — auto-posts eye care charges and optical sales.
- Inventory and Stores Management — manages optical inventory (frames, lenses).
- Appointments and Scheduling — books follow-up eye care appointments.
- Uganda HMIS Reporting — feeds HMIS 105 Section 8 data.

**Out of Scope:**

- Ophthalmic surgery (cataract, glaucoma) — theatre workflow handled by Theatre and Surgical Management.
- Low-vision rehabilitation services.
- Optometry franchise management.

---

### 14. Theatre and Surgical Management

**Category:** Specialty and Programme | **Tier:** Pro+ | **Phase:** 4

**Scope Statement:** The Theatre module manages the surgical workflow from theatre booking and scheduling through pre-operative checklists, operation notes, anaesthesia records, and surgical counts. It is restricted to Pro+ tiers given the infrastructure requirements.

**Key Capabilities:**

- Book and schedule theatre sessions with surgeon, anaesthetist, and support staff.
- Complete pre-operative checklists (WHO Surgical Safety Checklist compliant).
- Record operation notes with procedure details, findings, and complications.
- Record anaesthesia information: type, agents, monitoring, airway management.
- Perform surgical counts: swabs, instruments, and needles (pre- and post-procedure).
- Generate theatre-specific billing.

**Africa-First Enhancements:**

- HMIS 108 surgical section data auto-populated from operation records.
- EmONC caesarean section tracking for maternal health signal function reporting.

**Interfaces:**

- Inpatient Department (IPD) — receives surgical patients, returns post-operative notes.
- Laboratory Information System (LIS) — receives pre-operative investigation results.
- Pharmacy and Dispensary — receives anaesthesia drug requisitions.
- Billing and Revenue Management — auto-posts theatre and surgical charges.
- Blood Bank and Transfusion — receives cross-match results for surgical cases.
- Maternity, ANC and Reproductive Health — handles caesarean section deliveries.
- Uganda HMIS Reporting — feeds HMIS 108 surgical data.

**Out of Scope:**

- Day surgery unit as a separate administrative entity (managed within the general theatre schedule).
- Surgical instrument sterilisation tracking (future scope).
- Robotic surgery integration.

---

### 15. Blood Bank and Transfusion

**Category:** Specialty and Programme | **Tier:** Pro+ | **Phase:** 4

**Scope Statement:** The Blood Bank module manages blood product requests, cross-matching, issuing, transfusion administration, and adverse reaction recording. It maintains a blood stock register and integrates with Uganda Blood Transfusion Service (UBTS).

**Key Capabilities:**

- Receive blood product requests from clinical modules.
- Record cross-match results.
- Issue blood products with traceability to the recipient.
- Record transfusion administration with start time, volume, and vital signs.
- Document transfusion reactions with severity classification.
- Manage blood stock by product type, blood group, and expiry date.

**Africa-First Enhancements:**

- UBTS (Uganda Blood Transfusion Service) integration for blood product ordering and supply tracking.
- Haemovigilance reporting for transfusion adverse events.

**Interfaces:**

- Inpatient Department (IPD) — receives transfusion requests from the ward.
- Theatre and Surgical Management — receives pre-operative blood requests.
- Emergency Department (A&E) — receives emergency transfusion requests.
- Laboratory Information System (LIS) — receives blood group and cross-match results.
- Billing and Revenue Management — auto-posts blood product charges.

**Out of Scope:**

- Blood donation and donor recruitment management.
- Blood component separation and processing.
- External blood bank operations beyond the facility's internal stock.

---

### 16. Mortuary Management

**Category:** Specialty and Programme | **Tier:** All | **Phase:** 2

**Scope Statement:** The Mortuary module manages the workflow from death notification through body storage, cause-of-death certification, autopsy recording, and regulatory notifications. It generates documentation required by NIRA and supports maternal and perinatal death surveillance.

**Key Capabilities:**

- Record death notification with date, time, and circumstances.
- Assign cause of death using ICD-10 coding.
- Generate death certificates.
- Manage body storage with compartment tracking.
- Record autopsy findings when performed.
- Notify relevant authorities.

**Africa-First Enhancements:**

- MPDSR (Maternal and Perinatal Death Surveillance and Response) workflow for maternal and perinatal deaths.
- NIRA (National Identification and Registration Authority) death notification for civil registration.
- HMIS 108 deaths section data auto-populated.

**Interfaces:**

- Inpatient Department (IPD) — receives death notifications from the ward.
- Emergency Department (A&E) — receives death notifications from A&E.
- Patient Registration and Master Index — updates the patient record status.
- Billing and Revenue Management — generates final account and mortuary storage charges.
- Uganda HMIS Reporting — feeds HMIS 108 death data.

**Out of Scope:**

- Forensic pathology investigations beyond basic autopsy recording.
- Funeral arrangement services.
- Organ donation coordination.

---

### 17. Nutrition and Dietetics

**Category:** Specialty and Programme | **Tier:** Pro+ | **Phase:** 3

**Scope Statement:** The Nutrition module manages nutritional assessment, classification of acute malnutrition, enrolment into Community-based Management of Acute Malnutrition (CMAM) programmes, and therapeutic food dispensing. It targets the high burden of childhood malnutrition in the region.

**Key Capabilities:**

- Perform nutritional assessment using MUAC (Mid-Upper Arm Circumference) and WHZ (Weight-for-Height Z-score).
- Classify patients as SAM (Severe Acute Malnutrition) or MAM (Moderate Acute Malnutrition).
- Enrol patients into CMAM programmes with treatment protocols.
- Dispense RUTF (Ready-to-Use Therapeutic Food) with quantity tracking.
- Record nutrition counselling sessions.

**Africa-First Enhancements:**

- HMIS nutrition section data auto-populated from assessment records.
- RUTF stock tracking for donor-funded nutrition programmes.

**Interfaces:**

- Patient Registration and Master Index — references the patient (typically paediatric) record.
- Outpatient Department (OPD) — receives referrals from MUAC screening at triage.
- Inpatient Department (IPD) — manages inpatient therapeutic feeding.
- Pharmacy and Dispensary — dispenses therapeutic products.
- Community Health Integration — receives community-level MUAC screening data.
- Uganda HMIS Reporting — feeds nutrition data to HMIS forms.

**Out of Scope:**

- Hospital kitchen and meal planning management.
- Adult obesity management programmes.
- Parenteral nutrition compounding.

---

### 18. Physiotherapy and Rehabilitation

**Category:** Specialty and Programme | **Tier:** Pro+ | **Phase:** 4

**Scope Statement:** The Physiotherapy module manages rehabilitation referrals, patient assessments, treatment plans, and session-by-session progress notes. It supports programme-based tracking for patients with multi-session treatment courses.

**Key Capabilities:**

- Receive physiotherapy referrals from clinical modules.
- Perform initial assessment with functional evaluation.
- Create treatment plans with goals and expected duration.
- Record session notes with interventions performed.
- Track programme progress against treatment goals.

**Africa-First Enhancements:**

- WHO Rehabilitation Health Information System (RHIS) indicator generation.

**Interfaces:**

- Patient Registration and Master Index — references the patient record.
- Outpatient Department (OPD) — receives referrals from the OPD consultation.
- Inpatient Department (IPD) — receives referrals for inpatient rehabilitation.
- Billing and Revenue Management — auto-posts physiotherapy session charges.
- Appointments and Scheduling — schedules follow-up physiotherapy sessions.

**Out of Scope:**

- Occupational therapy as a separate discipline.
- Prosthetics and orthotics fitting and supply chain.
- Speech and language therapy.

---

## 5.4 Administrative Modules

### 19. Appointments and Scheduling

**Category:** Administrative | **Tier:** All | **Phase:** 1

**Scope Statement:** The Appointments module manages patient appointment booking, clinician availability calendars, queue management, and automated reminders. It supports walk-in integration and self-service booking through multiple channels.

**Key Capabilities:**

- Book patient appointments with date, time, clinician, and service type.
- Send SMS and WhatsApp appointment reminders.
- Maintain a doctor availability calendar with working hours and leave.
- Manage patient queues with real-time wait time display.
- Integrate walk-in patients into the appointment queue.
- Support online self-service booking.

**Africa-First Enhancements:**

- WhatsApp booking for patients who prefer messaging over phone calls.
- USSD booking for patients without smartphones or internet access.
- Africa's Talking SMS gateway integration for bulk reminders.
- Appointment confirmation SMS sent in patient's preferred language (English, French, or Kiswahili).

**Interfaces:**

- Patient Registration and Master Index — references the patient record for booking.
- Outpatient Department (OPD) — feeds the doctor's queue from booked appointments.
- Immunisation and Vaccination — schedules vaccination follow-ups.
- Dental Services — schedules dental appointments.
- Eye Care and Optical — schedules eye care appointments.
- Physiotherapy and Rehabilitation — schedules rehabilitation sessions.
- Patient Portal and Mobile App — exposes booking functionality to patients.

**Out of Scope:**

- Resource scheduling for rooms, equipment, or vehicles (handled by individual modules).
- Theatre scheduling (handled by Theatre and Surgical Management).
- Staff shift scheduling (handled by Human Resource and Payroll).

---

### 20. Referral Management

**Category:** Administrative | **Tier:** All | **Phase:** 2

**Scope Statement:** The Referral Management module manages internal and external patient referrals with electronic referral letters, tracks referral outcomes, and maintains a referral register aligned with Uganda's health facility referral hierarchy.

**Key Capabilities:**

- Create internal referrals between departments within the same facility.
- Create external referrals to other facilities with electronic referral letters.
- Maintain a referral register with referral status tracking.
- Track referral outcomes (accepted, seen, counter-referred, lost to follow-up).

**Africa-First Enhancements:**

- Uganda health system referral hierarchy support: HC II to HC III to HC IV to General Hospital to Regional Referral to National Referral.

**Interfaces:**

- Outpatient Department (OPD) — generates referral letters from the consultation screen.
- Emergency Department (A&E) — generates emergency referrals.
- Patient Registration and Master Index — identifies referring and receiving facilities.
- Uganda HMIS Reporting — feeds referral data to HMIS reports.

**Out of Scope:**

- Telemedicine consultations (future add-on).
- Health facility directory management (referral targets are configured, not dynamically discovered).
- Inter-facility patient record transfer (the referral letter summarises the record; the full EHR is not transferred).

---

### 21. Human Resource and Payroll

**Category:** Administrative | **Tier:** All | **Phase:** 2

**Scope Statement:** The HR and Payroll module manages staff records, professional licence tracking, attendance, leave, payroll processing with Uganda statutory deductions, and duty rosters. It provides staff productivity reporting for facility management.

**Key Capabilities:**

- Maintain a staff directory with personal details, qualifications, and employment history.
- Record and track professional licence expiry dates with alerts.
- Track attendance and leave balances.
- Process payroll with PAYE (Pay As You Earn) and NSSF (National Social Security Fund) deductions per Uganda statutory requirements.
- Create and manage duty rosters.
- Report staff productivity metrics.

**Africa-First Enhancements:**

- UMDPC (Uganda Medical and Dental Practitioners Council) licence tracking.
- UNMC (Uganda Nurses and Midwives Council) licence tracking.
- PHLB (Pharmacy and Herbal Licence Board) licence tracking.
- Uganda PAYE tax tables and NSSF contribution rates pre-configured.

**Interfaces:**

- Billing and Revenue Management — staff salary data feeds financial reports.
- Financial Accounting (Dual Mode) — payroll journal entries post to accounting.
- All clinical modules — staff identity used for audit trails and user access control.

**Out of Scope:**

- Recruitment and applicant tracking.
- Performance appraisal management.
- Staff training and continuing professional development tracking (future scope).

---

### 22. Medical Records and Health Information

**Category:** Administrative | **Tier:** All | **Phase:** 2

**Scope Statement:** The Medical Records module manages the physical file tracking workflow for facilities that maintain paper records alongside the electronic system. It tracks file movements, generates missing file reports, and archives discharge summaries. AI ICD Coding Assist reduces manual coding burden during discharge summary archival.

**Key Capabilities:**

- Track paper file location with movement logs (issued to, returned from, date/time).
- Generate missing file reports for files not returned to the records room.
- Archive discharge summaries in the electronic system.
- Generate medical certificates (sick notes, fitness certificates).

**Africa-First Enhancements:**

- HMIS form inventory management (tracking which paper HMIS forms are in stock).
- NIRA birth notification generation for newborns delivered at the facility.

**Interfaces:**

- Patient Registration and Master Index — maps physical file numbers to electronic patient records.
- Inpatient Department (IPD) — receives discharge summaries for archiving.
- Maternity, ANC and Reproductive Health — generates NIRA birth notifications.
- Uganda HMIS Reporting — tracks HMIS form inventory.
- AI Intelligence — AI ICD Coding Assist surfaces suggested ICD-10/11 codes during discharge summary archival, reducing manual coding time.

**Out of Scope:**

- Document scanning and digitisation workflow.
- Health information exchange (HIE) with external systems (future scope via FHIR).
- Research data extraction and anonymisation.

---

### 23. Ambulance Management

**Category:** Administrative | **Tier:** Pro+ | **Phase:** 4

**Scope Statement:** The Ambulance Management module manages the ambulance fleet register, trip logs, pre-hospital care documentation, and patient handover to the emergency department. It supports GPS tracking for fleet visibility.

**Key Capabilities:**

- Maintain a fleet register with vehicle details, maintenance schedules, and insurance.
- Log ambulance trips with origin, destination, crew, and patient details.
- Record pre-hospital care interventions during transport.
- Document patient handover to the receiving facility's emergency department.
- Track ambulance location via GPS integration.

**Africa-First Enhancements:**

- KCCA (Kampala Capital City Authority) ambulance service integration.
- USSD-based ambulance request for callers without smartphones.

**Interfaces:**

- Emergency Department (A&E) — delivers patients and handover documentation.
- Patient Registration and Master Index — creates or links patient records at handover.
- Billing and Revenue Management — posts ambulance service charges.

**Out of Scope:**

- Emergency dispatch coordination across multiple facilities.
- Air ambulance operations.
- Vehicle maintenance and fleet management beyond basic register and scheduling.

---

## 5.5 Financial Modules

### 24. Billing and Revenue Management

**Category:** Financial | **Tier:** All | **Phase:** 1

**Scope Statement:** The Billing module manages patient accounts, charge accumulation from clinical encounters, payment processing, and daily cashier reconciliation. It supports cash, mobile money, and split billing across payers, and provides the revenue backbone for all clinical modules.

**Key Capabilities:**

- Maintain a patient account with real-time charge accumulation from all clinical modules.
- Support a configurable price list with patient category-specific pricing.
- Auto-bill from clinical screens (consultation, lab, pharmacy, radiology, procedures).
- Generate receipts for cash payments.
- Process split billing across multiple payers (patient, insurance, sponsor).
- Manage deposits and running bills.
- Handle credit management for corporate and insurance accounts.
- Perform daily cashier reconciliation with shift-end cash-up.

**Africa-First Enhancements:**

- MTN Mobile Money (MoMo) API integration for patient payments.
- Airtel Money API integration for patient payments.
- Micro-payment support for facilities that accept partial payments on outstanding balances.

**Interfaces:**

- Patient Registration and Master Index — links charges to the patient account via MRN.
- Outpatient Department (OPD) — receives consultation and procedure charges.
- Inpatient Department (IPD) — receives inpatient charge accumulation.
- Emergency Department (A&E) — receives emergency charges.
- Laboratory Information System (LIS) — receives test charges.
- Pharmacy and Dispensary — receives dispensing charges.
- Radiology and Imaging — receives imaging charges.
- Dental Services — receives dental procedure charges.
- Eye Care and Optical — receives eye care and optical sales charges.
- Theatre and Surgical Management — receives theatre and surgical charges.
- Insurance Management — sends insurance-covered charges for claim generation.
- Financial Accounting (Dual Mode) — posts revenue journal entries.
- Patient Portal and Mobile App — exposes balance and payment functionality.

**Out of Scope:**

- Insurance claim submission and reconciliation (handled by Insurance Management).
- General ledger and financial statements (handled by Financial Accounting).
- Procurement and supplier payments (handled by Inventory and Stores Management).

**Localisation Flags:**

- Number formatting: French locale uses a space thousands separator (1 500 000 UGX); English and Kiswahili locales use a comma separator (1,500,000 UGX).

---

### 25. Insurance Management

**Category:** Financial | **Tier:** All | **Phase:** 2

**Scope Statement:** The Insurance Management module manages insurance scheme registration, member eligibility verification, benefit schedule enforcement, pre-authorisation, claim generation, and claim reconciliation. It supports the diverse insurance landscape in Uganda including the forthcoming National Health Insurance Scheme (NHIS). The AI Claim Scrubbing capability is surfaced within this module at the claim review step.

**Key Capabilities:**

- Register insurance schemes with benefit schedules and price agreements (AAR, Jubilee, Prudential, and others).
- Verify member eligibility and benefit limits at the point of care.
- Manage pre-authorisation requests for services requiring insurer approval.
- Generate claims from patient encounters with itemised charge details.
- Submit claims to insurers (electronic or batch export).
- Track claim rejections and manage re-submission.
- Reconcile insurance credit balances with payments received.

**Africa-First Enhancements:**

- NHIS Uganda readiness for the forthcoming national scheme.
- Corporate medical cover schemes common in Ugandan private sector.
- Mission hospital insurance arrangements with faith-based organisations.

**Interfaces:**

- Patient Registration and Master Index — verifies patient insurance membership.
- Billing and Revenue Management — receives insurance-eligible charges.
- Financial Accounting (Dual Mode) — posts insurance receivable journal entries.
- All clinical modules — enforces benefit schedule limits during ordering.
- AI Intelligence — AI Claim Scrubbing panel displayed at the claim review step, before the **Submit Claim** action, where the AI Intelligence module is enabled.

**Out of Scope:**

- Insurance underwriting and policy management.
- Direct insurer system integration via API (claims are generated for export; real-time API integration is future scope).
- Health maintenance organisation (HMO) capitation management.

---

### 26. Financial Accounting (Dual Mode)

**Category:** Financial | **Tier:** All | **Phase:** 2

**Scope Statement:** The Financial Accounting module operates in 2 modes. Simple Mode provides money-in, money-out, and outstanding claims tracking suitable for small clinics. Advanced Mode provides a full double-entry accounting system with chart of accounts, trial balance, income statement, and balance sheet for facilities that require formal financial reporting.

**Key Capabilities:**

- Simple Mode: record money received, money spent, outstanding insurance claims, and daily summary.
- Advanced Mode: maintain a chart of accounts, record double-entry journal entries, generate trial balance, income statement, and balance sheet.
- Pre-load a healthcare-specific chart of accounts.
- Maintain an insurance receivables ledger with ageing analysis.
- Apply auto-posting rules to convert clinical transactions into journal entries.
- Track donor funds in ring-fenced cost centres with restricted spending rules.

**Africa-First Enhancements:**

- Capitation grant tracking for government-aided facilities receiving PHC (Primary Health Care) grants.
- NSSF and PAYE remittance tracking and reporting.
- Donor fund ring-fencing for PEPFAR, Global Fund, and NGO-funded facilities.

**Interfaces:**

- Billing and Revenue Management — receives revenue transactions for posting.
- Insurance Management — receives insurance receivable transactions.
- Human Resource and Payroll — receives payroll journal entries.
- Inventory and Stores Management — receives procurement and stock valuation entries.

**Out of Scope:**

- Tax filing and URA (Uganda Revenue Authority) return generation.
- External audit management.
- Fixed asset register and depreciation (future scope).

---

### 27. Inventory and Stores Management

**Category:** Financial | **Tier:** All | **Phase:** 2

**Scope Statement:** The Inventory module manages multi-store stock across the facility (main store, pharmacy, theatre, ward, dental), handles goods receipt, inter-store transfers, expiry management, and procurement workflows. It integrates with the NMS ordering system for government-supplied commodities.

**Key Capabilities:**

- Manage multiple stores: main store, pharmacy, theatre, ward, and dental.
- Process goods received notes (GRN) with supplier details and batch tracking.
- Transfer stock between stores with approval workflow.
- Adjust stock with reason codes and audit trail.
- Set minimum and maximum stock levels per item per store.
- Track item expiry dates with configurable alert windows.
- Generate NMS orders based on stock levels and consumption data.
- Manage the procurement workflow: requisition, approval, purchase order, receipt.

**Africa-First Enhancements:**

- NMS (National Medical Stores) commodity codes for seamless government supply chain integration.
- PEPFAR commodity tracking for donor-funded drug and supply programmes.
- LMIS (Logistics Management Information System) export for national supply chain reporting.
- Essential Medicines List compliance checking.

**Interfaces:**

- Pharmacy and Dispensary — shares pharmacy stock data, receives dispensing deductions.
- Theatre and Surgical Management — manages theatre consumable stock.
- Dental Services — manages dental supply stock.
- Financial Accounting (Dual Mode) — posts procurement and stock valuation entries.
- Billing and Revenue Management — provides cost data for pricing.

**Out of Scope:**

- Supplier relationship management and tendering.
- Warehouse management for distribution centres.
- Fixed asset tracking (furniture, equipment, vehicles).

---

## 5.6 HMIS and Public Health Reporting

### 28. Uganda HMIS Reporting

**Category:** HMIS and Public Health | **Tier:** All | **Phase:** 2

**Scope Statement:** The HMIS Reporting module aggregates clinical, laboratory, pharmacy, maternity, and programme data from all modules to auto-populate Uganda Ministry of Health HMIS forms. It supports validation, DHIS2 upload, and a reporting calendar to ensure timely submission.

**Key Capabilities:**

- Auto-populate HMIS 105 (Outpatient Monthly Report) from clinical module data.
- Auto-populate HMIS 108 (Inpatient Monthly Report) from IPD and mortality data.
- Auto-populate HMIS 033b (Weekly Epidemiological Report) from surveillance data.
- Validate reports against business rules before submission (completeness, range checks).
- Upload reports to DHIS2 via export file or direct API push.
- Maintain a reporting calendar with submission deadlines and status tracking.
- Provide a DHO (District Health Officer) portal view for supervisory oversight.

**Africa-First Enhancements:**

- All Uganda HMIS forms pre-configured as the default reporting framework.
- PEPFAR MER (Monitoring, Evaluation, and Reporting) indicator generation.
- IDSR (Integrated Disease Surveillance and Response) weekly report generation.

**Interfaces:**

- All clinical modules — aggregates data from OPD, IPD, LIS, Pharmacy, Maternity, Immunisation, Radiology, and programme modules.
- HIV/AIDS Programme Management — feeds PEPFAR MER indicators.
- TB Programme Management — feeds NTLP reporting data.
- Disease Surveillance and Outbreak Detection — feeds IDSR data.

**Out of Scope:**

- Custom report builder for ad hoc queries (future scope).
- Non-Uganda HMIS frameworks (country-specific configurations are future expansion).
- Data warehouse and business intelligence analytics (future scope).

---

### 29. Disease Surveillance and Outbreak Detection

**Category:** HMIS and Public Health | **Tier:** All | **Phase:** 2

**Scope Statement:** The Disease Surveillance module monitors priority diseases with configurable threshold alerts, flags potential outbreaks, and generates weekly surveillance data for the Integrated Disease Surveillance and Response (IDSR) system. It sends notifiable disease alerts to the District Health Officer. The AI Outbreak Early Warning capability (Module 32) provides facility-level anomaly detection before IDSR national thresholds are crossed, and is complementary to — not a replacement for — the IDSR reporting workflow.

**Key Capabilities:**

- Track priority diseases against configurable threshold values.
- Flag threshold breaches as potential outbreaks.
- Generate weekly surveillance data summaries.
- Send notifiable disease alerts to designated public health authorities.

**Africa-First Enhancements:**

- Uganda IDSR 57 priority diseases pre-configured.
- One Health surveillance approach for zoonotic diseases.
- DRRT (District Rapid Response Team) notification workflow.

**Interfaces:**

- Outpatient Department (OPD) — receives diagnosis data for surveillance.
- Inpatient Department (IPD) — receives admission diagnosis data.
- Laboratory Information System (LIS) — receives confirmed laboratory results for priority diseases.
- Uganda HMIS Reporting — feeds HMIS 033b and IDSR weekly report data.

**Out of Scope:**

- Epidemiological modelling and forecasting.
- Environmental health surveillance (water quality, sanitation).
- Cross-border disease surveillance coordination.

---

### 30. Community Health Integration

**Category:** HMIS and Public Health | **Tier:** Pro+ | **Phase:** 3

**Scope Statement:** The Community Health Integration module extends the platform to Village Health Teams (VHTs) and Community Health Workers (CHWs) through a dedicated Android application. It captures community-level referrals, home visits, and health event data for integration with the facility-based clinical record.

**Key Capabilities:**

- Maintain VHT (Village Health Team) member records with assigned catchment areas.
- Track community-to-facility referrals and their outcomes.
- Record community health events (outreach campaigns, health education sessions).
- Log home visit records with assessment findings.
- Provide a CHW Android application for offline data capture.

**Africa-First Enhancements:**

- Uganda VHT programme structure and reporting requirements pre-configured.
- DHIS2 Tracker upload for community health worker data.

**Interfaces:**

- Patient Registration and Master Index — links community-identified patients to facility records.
- HIV/AIDS Programme Management — receives community-level HTC and adherence data.
- TB Programme Management — receives contact tracing data.
- Nutrition and Dietetics — receives community-level MUAC screening data.
- Immunisation and Vaccination — receives defaulter tracing and outreach vaccination data.
- Uganda HMIS Reporting — feeds community health data to HMIS aggregation.

**Out of Scope:**

- CHW training and certification management.
- Community-based health insurance enrolment.
- mHealth interventions beyond the CHW data capture application.

---

## 5.7 Patient Portal and Mobile App

### 31. Patient Portal and Mobile App

**Category:** Patient Portal and Mobile | **Tier:** All | **Phase:** 3

**Scope Statement:** The Patient Portal provides patients with access to their personal health records, investigation results, appointment management, billing information, and health education through a mobile application. It surfaces AI Patient Plain-Language Summaries in the patient's preferred language (English, French, or Kiswahili) after clinician approval.

**Key Capabilities:**

- Display a personal health record: visit history, diagnoses, treatments, and investigation results.
- Show laboratory and radiology results with historical trends.
- Manage appointments: view, book, reschedule, and cancel.
- Display fee balance and payment history.
- Process mobile money payments from within the app.
- Send medication reminders and immunisation schedule notifications.
- Deliver health education content.
- Support multiple family members under a single account.
- Provide offline access to cached health records.
- Display AI Patient Plain-Language Summary in the patient's preferred locale after clinician approval.

**Africa-First Enhancements:**

- Android-first design given the dominant mobile platform in the region.
- Data-lite mode that minimises bandwidth consumption on 2G/3G connections.
- USSD and SMS fallback for patients without smartphones.
- Low-specification device support (Android 8.0+, 1 GB RAM minimum).
- Full French and Kiswahili interface including all navigation labels, error messages, and clinical summaries.

**Interfaces:**

- Patient Registration and Master Index — authenticates the patient and retrieves the health record.
- Outpatient Department (OPD) — displays visit history and clinical notes.
- Laboratory Information System (LIS) — displays test results.
- Radiology and Imaging — displays radiology reports.
- Pharmacy and Dispensary — displays medication history.
- Immunisation and Vaccination — displays immunisation schedule and sends reminders.
- Appointments and Scheduling — exposes booking functionality.
- Billing and Revenue Management — displays balance and accepts payments.
- AI Intelligence — AI Patient Plain-Language Summary displayed in the patient's preferred locale after the clinician approves the discharge summary.

**Out of Scope:**

- Telemedicine video consultations (future add-on).
- Prescription refill requests from the app.
- Integration with wearable health devices.
- Health record portability and export to other systems (future FHIR-based scope).

**Localisation Flags:**

- AI Patient Plain-Language Summary: Kiswahili summaries target a lower Flesch-Kincaid reading level than French or English equivalents, reflecting health literacy distribution in the primary Kiswahili-speaking patient population.

---

## 5.8 AI Intelligence Module

### 32. AI Intelligence

**Category:** AI Add-On | **Tier:** All (credit pack or flat fee, independent of clinical tier) | **Phase:** 2

**Scope Statement:** The AI Intelligence module provides 6 tenant-configurable AI capabilities powered by a provider-agnostic adapter layer. It is billed independently of the clinical subscription and can be activated or deactivated per tenant from the admin panel. Individual capabilities are toggled independently.

**Key Capabilities:**

- AI Clinical Documentation: draft SOAP notes, discharge summaries, and referral letters from structured encounter data; clinician reviews and clicks **Approve Draft** before any text is saved to the patient record.
- AI ICD Coding Assist: suggest top 3-5 ICD-10/11 codes from free-text clinical notes with confidence scores; clinician selects or dismisses each suggestion.
- AI Differential Diagnosis: surface a ranked differential diagnosis list from symptoms, vitals, and recent lab results at the point of care; presented as a clinical prompt, not a decision.
- AI Patient Plain-Language Summary: translate the approved clinical discharge note into a plain-language summary in the patient's preferred locale (`en`, `fr`, or `sw`) for display in the patient portal.
- AI Claim Scrubbing: predict rejection probability per claim line item using the facility's historical rejection data before submission; flag red-risk items for billing clerk correction.
- AI Outbreak Early Warning: detect anomalous clustering of diagnosis codes before IDSR national thresholds are crossed; alert the Medical Officer daily with disease code, patient volume, and percentage deviation from the 90-day baseline.

**Provider Architecture:**

- A single `AIProviderInterface` is implemented by 4 concrete adapter classes: `OpenAIAdapter` (GPT-4o, GPT-4o-mini), `AnthropicAdapter` (Claude Sonnet, Claude Haiku), `DeepSeekAdapter` (DeepSeek-V3, DeepSeek-R1), and `GeminiAdapter` (Gemini 1.5 Pro, Gemini 1.5 Flash).
- Per-tenant configuration selects the primary provider and an optional failover provider; switching providers requires no code change — only a tenant configuration update in the admin panel.
- If the primary provider does not respond within 10 seconds, the system retries via the failover provider; if the failover also fails, the AI capability returns a graceful degradation message and all clinical workflows proceed manually without interruption.

**Billing Model:**

- Credit pack model: credits are token-denominated; AI features pause automatically when the credit balance reaches zero; clinical features are unaffected.
- Flat fee model: fixed monthly add-on charged alongside the clinical subscription; all 6 capabilities available within a defined fair-use ceiling; available on Pro and Enterprise tiers only.
- Token consumption is metered per request, per capability, per tenant, and logged in `ai_usage_log` for billing reconciliation.

**Safety Guardrails:**

- AI Clinical Documentation drafts are never auto-saved; the clinician must click **Approve Draft** before any text is written to the patient record.
- AI Differential Diagnosis suggestions are never written to the patient record unless the clinician explicitly selects the condition as an active diagnosis.
- No patient personally identifiable information (NIN, full legal name, NIRA number) is included in prompts sent to AI providers; encounter data is referenced by anonymised encounter ID.

**Interfaces:**

- Outpatient Department (OPD) — consumes AI Clinical Documentation (SOAP notes, referral letters) and AI Differential Diagnosis at the point of consultation.
- Inpatient Department (IPD) — consumes AI Clinical Documentation for discharge summary drafts.
- Medical Records and Health Information — consumes AI ICD Coding Assist during discharge archival.
- Laboratory Information System (LIS) — LIS diagnosis result aggregation feeds the AI Outbreak Early Warning detection model.
- Insurance Management — consumes AI Claim Scrubbing at the claim review step before submission.
- Patient Portal and Mobile App — displays AI Patient Plain-Language Summary in the patient's preferred locale.

**Out of Scope:**

- AI training on patient data.
- Autonomous clinical decisions without clinician review.
- AI capabilities that persist output without explicit clinician approval.

---

## 5.9 Cross-Cutting Concerns

The following capabilities span multiple modules and are not enumerated as standalone modules, but their scope boundaries are documented here to prevent ambiguity.

### 5.9.1 Multi-Tenancy and Tenant Isolation

All modules operate within a centralised multi-tenant architecture using `facility_id` isolation. Tenant data is never shared between facilities unless the facility belongs to a multi-facility network with explicit cross-facility access enabled. Multi-tenancy is an architectural constraint, not a user-facing module.

### 5.9.2 Offline-First Operation

All clinical workflows (OPD, IPD, Emergency, Pharmacy, LIS) support offline operation with local data caching and synchronisation upon connectivity restoration. The offline-first capability is embedded in each module's implementation, not delivered as a separate module.

### 5.9.3 FHIR R4 API

The FHIR R4 API exposes patient, encounter, observation, medication, and diagnostic data as FHIR resources. It is available from Phase 3 for Pro and Enterprise tiers. The API enables integration with external systems but does not constitute a standalone user-facing module.

### 5.9.4 Country Configuration Layer

The country configuration layer adapts regulatory, clinical, financial, and reporting requirements per tenant. Uganda is the launch configuration. Kenya, Tanzania, Rwanda, DRC, Nigeria, India, and Australia configurations are planned. The configuration layer is an architectural mechanism, not a module.

### 5.9.5 Multi-Language (i18n) Architecture

All UI layers (PHP/Laravel web, Android, iOS) support English (`en`), French (`fr`), and Kiswahili (`sw`) as launch languages. String keys follow the `module.context.label` convention. The locale fallback chain is: `sw → en`, `fr → en`. A missing string never falls through to machine translation — it renders the English fallback and emits `[I18N-GAP: <key>]` to the build log. No `[I18N-GAP]` tag may remain unresolved in any production release.

### 5.9.6 AI Analytics

AI-powered analytics (predictive patient volumes, drug demand forecasting, revenue optimisation) are available as an add-on for Growth tier and included in Pro and Enterprise tiers. AI Analytics operates as a cross-cutting data layer consuming data from all modules, not as a standalone clinical or administrative module.

### 5.9.7 Director Platform (Multi-Facility)

The Director Platform provides consolidated dashboards, patient record sharing, and group-level reporting for multi-facility networks. It is available as an add-on for Pro tier and included in Enterprise tier. It consumes data from all modules at the facility level and aggregates to the network level.
