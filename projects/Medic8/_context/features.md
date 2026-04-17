# Medic8 Feature List

Comprehensive feature inventory for Medic8, a multi-tenant SaaS healthcare management system. Features are organised by functional category, with tier eligibility and build phase indicated for each module.

**Tier Key:** All = All tiers | Pro+ = Pro and Enterprise | Enterprise = Enterprise only

**Phase Key:** 1 = Foundation | 2 = Expansion | 3 = Programmes and Patient Engagement | 4 = Advanced Specialty

---

## Core Clinical Modules

### Patient Registration and Master Index

**Tier:** All | **Phase:** 1

- New patient registration: demographics, contact, next-of-kin, photo capture
- Biometric registration: fingerprint or facial recognition (optional hardware)
- Unique Patient ID (MRN) auto-generated, format configurable per facility
- Returning patient lookup: by name, phone, ID number, NIN, or fingerprint
- Patient categories: adult, paediatric, staff, VIP, indigent/sponsored, refugee
- Multiple identifiers: NIN, passport, NIRA, UNHCR ID, insurance member number
- Guardian/next-of-kin linking for paediatric patients
- Patient profile: photo, demographics, blood group, allergies, chronic conditions
- Patient merge: duplicate records with full audit trail
- Triage queue sorted by triage level
- Cross-facility lookup via global patient identity layer
- Africa-first: UNHCR Refugee ID, NIN integration, MoMo phone number as lookup

### Outpatient Department (OPD)

**Tier:** All | **Phase:** 1

- Triage: vital signs (BP, temperature, pulse, SpO2, weight, height, BMI, MUAC)
- Doctor's queue: real-time per doctor/room with triage priority and wait time
- Clinical consultation: SOAP notes, free-text and structured
- Diagnosis entry: ICD-10 and ICD-11 with clinical description
- Investigation requests: lab, radiology, ECG with instant notification
- Prescription writing: generic + brand, dose, frequency, duration, route, quantity
- Stock-aware prescribing: shows pharmacy availability before saving
- Drug interaction checking (four-tier alert: Info/Warning/Serious/Fatal)
- Procedure recording: minor procedures in OPD
- Referral: internal, external, electronic referral letter
- Follow-up appointment booking from consultation
- Clinical notes history: complete visit history in one screen
- Africa-first: HMIS 105 auto-capture, malaria mRDT field, HIV status field, MUAC screening, MOH 5 format

### Inpatient Department (IPD) and Ward Management

**Tier:** All | **Phase:** 2

- Patient admission from OPD, emergency, or direct
- Bed management: visual bed map per ward
- Nursing notes: shift-by-shift with timestamps
- Doctor's ward round notes with clinical progress
- Drug round: medication administration tracking (ordered, given, held, refused)
- Vital signs chart: graphical tracking over admission
- Fluid balance chart: intake and output
- Inpatient investigation requests
- Transfer between wards with receiving nurse acknowledgment
- Discharge: summary, letter generation, DAMA recording
- Inpatient billing: real-time charge accumulation
- Patient census: live count per ward
- Africa-first: HMIS 108 auto-populated, DRG mapping, paediatric weight-based dosing

### Emergency Department (A&E)

**Tier:** All | **Phase:** 2

- Rapid triage with AVPU/GCS
- Emergency patient registration: minimal required fields
- Resuscitation record, trauma assessment
- Emergency orders with URGENT flag
- Time tracking: arrival, triage, seen, disposition
- Mass casualty mode with START triage
- Africa-first: RTA coding, police notification flag, generator/power failure mode

### Maternity, ANC and Reproductive Health

**Tier:** All | **Phase:** 2

- ANC registration with gestational age and EDD
- ANC visit recording (ANC1-ANC8+)
- ANC risk assessment for high-risk pregnancies
- Labour admission with partograph (cervicogram, vitals, FHR, contractions)
- Delivery record: mode, outcome, birth weight, APGAR
- Newborn record linked to mother, neonatal assessment, immunisation at birth
- Postnatal visits (PNC1-PNC3)
- Family planning
- Africa-first: HMIS 105 Section 4, EmONC tracking, PMTCT, Mother Baby Pair linkage

### Immunisation and Vaccination

**Tier:** All | **Phase:** 2

- Uganda EPI schedule pre-loaded
- Vaccine administration: date, name, batch, dose, site
- Missed vaccine alerts with SMS reminders
- Cold chain records, vaccination certificates
- Defaulter tracing, AEFI reporting
- Africa-first: Uganda EPI schedule, COVID-19 tracking, HPV campaigns, DHIS2 Tracker upload

### Laboratory Information System (LIS)

**Tier:** All | **Phase:** 1

- Lab request from OPD/IPD/Emergency
- Sample collection with barcode/QR label generation
- Specimen tracking: requested, collected, received, processing, result ready
- Result entry with reference ranges, auto-flag abnormal (H/L, critical)
- Critical value alerts with escalation
- Result validation by lab supervisor
- Quality control: QC records, Levey-Jennings charts
- Equipment interface: HL7 connection to auto-analysers (Cobas, Mindray, Sysmex)
- External lab referral (Lancet, CPHL)
- Africa-first: HMIS 105 Section 2, malaria/HIV/syphilis/pregnancy tests, CD4 tracking, GeneXpert TB

### Radiology and Imaging

**Tier:** All | **Phase:** 2

- Radiology request from clinical screen
- Worklist management for radiographer
- Report entry with structured templates per modality
- PACS integration for DICOM image management
- Africa-first: Ultrasound-first workflow, HMIS 105 Section 3, portable ultrasound integration

### Pharmacy and Dispensary

**Tier:** All | **Phase:** 1

- Prescription queue from OPD/IPD/Emergency
- Dispensing with stock deduction
- Generic/brand substitution with doctor notification
- Dispensing label generation
- Partial dispensing with pending balance
- Stock management: GRN, transfer, adjust, return
- Expiry tracking: 90-day flag
- Stock valuation: FIFO, weighted average
- Minimum stock level alerts
- Drug formulary management
- Narcotic/controlled drug register
- Africa-first: NMS drug codes, LMIS export, ACT tracking, ARV dispensing, PEPFAR commodity tracking

---

## Specialty and Programme Modules

### HIV/AIDS Programme Management

**Tier:** All | **Phase:** 3

- HIV testing and counselling, programme enrolment
- ART initiation: WHO staging, CD4, regimen
- ARV dispensing with adherence tracking
- Viral load tracking with suppression status
- PMTCT, missed appointment tracking
- Africa-first: Uganda MoH ART card, PEPFAR indicators (TX_CURR, TX_NEW, TX_PVLS), HMIS 105 Section 5, UgandaEMR+ integration

### TB Programme Management

**Tier:** All | **Phase:** 3

- TB case registration, treatment regimen
- DOT tracking, sputum/culture/GeneXpert results
- Treatment outcome recording
- Contact tracing
- Africa-first: NTLP quarterly report, MDR-TB management

### Dental Services

**Tier:** All | **Phase:** 2

- 32-tooth graphical chart, periodontal chart
- Treatment planning with cost estimates
- Procedure recording linked to billing
- Africa-first: HMIS 105 Section 7

### Eye Care and Optical

**Tier:** All | **Phase:** 2

- Visual acuity, refraction, optical prescription
- Slit lamp, fundoscopy, IOP
- Optical dispensing linked to inventory
- Africa-first: HMIS 105 Section 8

### Theatre and Surgical Management

**Tier:** Pro+ | **Phase:** 4

- Theatre booking, schedule, pre-op checklist
- Operation notes, anaesthesia record
- Surgical count (swab, instrument, needle)
- Theatre billing
- Africa-first: HMIS 108 surgical section, EmONC CS tracking

### Blood Bank and Transfusion

**Tier:** Pro+ | **Phase:** 4

- Blood request, cross-match, issue
- Transfusion administration and reaction recording
- Blood stock management
- Africa-first: UBTS integration, haemovigilance

### Mortuary Management

**Tier:** All | **Phase:** 2

- Death notification, cause of death (ICD-10)
- Death certificate, body storage, autopsy
- Africa-first: MPDSR, NIRA notification, HMIS 108 deaths

### Nutrition and Dietetics

**Tier:** Pro+ | **Phase:** 3

- Nutritional assessment (MUAC, WHZ)
- SAM/MAM classification, CMAM enrolment
- RUTF dispensing, counselling
- Africa-first: HMIS nutrition section, RUTF tracking

### Physiotherapy and Rehabilitation

**Tier:** Pro+ | **Phase:** 4

- Physiotherapy referral, assessment, treatment plan
- Session notes, programme tracking
- Africa-first: WHO RHIS rehabilitation indicators

---

## Administrative Modules

### Appointments and Scheduling

**Tier:** All | **Phase:** 1

- Appointment booking, SMS/WhatsApp reminders
- Doctor availability calendar, queue management
- Walk-in integration, online booking
- Africa-first: WhatsApp booking, USSD booking, Africa's Talking SMS

### Referral Management

**Tier:** All | **Phase:** 2

- Internal and external referral with electronic letter
- Referral register, outcome tracking
- Africa-first: Uganda health system referral hierarchy (HC II to National Referral)

### Human Resource and Payroll

**Tier:** All | **Phase:** 2

- Staff directory, qualification and licence records
- Licence expiry alerts, attendance, leave
- Payroll: PAYE, NSSF per Uganda statutory
- Duty roster, staff productivity
- Africa-first: UMDPC/UNMC/PHLB licence tracking, Uganda PAYE/NSSF

### Medical Records and Health Information

**Tier:** All | **Phase:** 2

- Paper file tracking, movement log
- Missing file report, discharge summary archive
- Medical certificates
- Africa-first: HMIS form inventory, NIRA birth notification

### Ambulance Management

**Tier:** Pro+ | **Phase:** 4

- Fleet register, trip log, pre-hospital care
- Patient handover, GPS tracking
- Africa-first: KCCA integration, USSD ambulance request

---

## Financial Modules

### Billing and Revenue Management

**Tier:** All | **Phase:** 1

- Patient account with real-time charge accumulation
- Configurable price list, patient category pricing
- Auto-billing from clinical screens
- Receipt generation, cash payment, split billing
- Deposit management, running bill, credit management
- Daily cashier reconciliation
- Africa-first: MTN MoMo / Airtel Money API, micro-payment support

### Insurance Management

**Tier:** All | **Phase:** 2

- Scheme register (NHIS, AAR, Jubilee, Prudential, etc.)
- Member verification, benefit schedule
- Pre-authorisation, claim generation and submission
- Rejection management, credit reconciliation
- Africa-first: NHIS Uganda, corporate medical covers, mission insurance

### Financial Accounting (Dual Mode)

**Tier:** All | **Phase:** 2

- Simple Mode: money received, spent, outstanding claims, daily summary
- Advanced Mode: chart of accounts, double-entry, trial balance, income statement, balance sheet
- Healthcare chart of accounts pre-loaded
- Insurance receivables ledger, auto-posting rules
- Donor fund accounting: ring-fenced cost centres
- Africa-first: Capitation grant tracking, NSSF/PAYE remittance, donor fund ring-fencing

### Inventory and Stores Management

**Tier:** All | **Phase:** 2

- Multi-store: main, pharmacy, theatre, ward, dental
- GRN, stock transfer, adjustment, minimum/maximum levels
- Expiry management, NMS ordering, procurement workflow
- Africa-first: NMS commodity codes, PEPFAR commodity tracking, LMIS export, Essential Medicines List

---

## Uganda HMIS and Public Health Reporting

### Uganda HMIS Reporting

**Tier:** All | **Phase:** 2

- HMIS 105, 108, 033b auto-populated
- Report validation, DHIS2 upload (export or API push)
- Reporting calendar, DHO portal
- Africa-first: All Uganda HMIS forms, PEPFAR MER indicators, IDSR

### Disease Surveillance and Outbreak Detection

**Tier:** All | **Phase:** 2

- Priority disease tracking with threshold alerts
- Outbreak flagging, weekly surveillance data
- Notifiable disease alerts
- Africa-first: Uganda IDSR 57 diseases, One Health, DRRT notification

### Community Health Integration

**Tier:** Pro+ | **Phase:** 3

- VHT records, community referral tracking
- Community health events, home visits
- CHW Android app
- Africa-first: Uganda VHT programme, DHIS2 Tracker CHW data

---

## Patient Portal and Mobile App

**Tier:** All | **Phase:** 3

- Personal health record: visits, diagnoses, treatments, investigations
- Test results, appointments, fee balance, payment history
- Mobile money payment from app
- Medication reminders, immunisation schedule
- Health education, secure messaging
- Multiple family members, offline access
- Africa-first: Android-first, data-lite mode, USSD/SMS fallback, Luganda interface, low-spec device support

## AI Clinical Intelligence Module (Phase 3 Add-On)

**Tier:** Starter and above (tiered) | **Phase:** 3 (add-on, off by default)

- At-risk patient early warning: hourly modified Early Warning Score (EWS) computed from vitals trends across all admitted patients; alerts dispatched when EWS rises by 3+ points
- AI-assisted differential diagnosis support: suggests up to 5 ranked ICD-10/ICD-11 differential diagnoses from presenting symptoms and vitals — decision aid only, clinical responsibility remains with the treating clinician
- Automated clinical note summarisation: generates structured SOAP summary from free-text consultation notes; requires explicit clinician approval before saving to patient record
- Pharmacy demand forecasting: nightly stockout-risk report predicting days of stock remaining per drug based on 28-day adjusted consumption rate
- Disease surveillance and outbreak detection: 6-hourly scan flagging ICD-10 diagnosis clusters that exceed 2 standard deviations above 30-day baseline
