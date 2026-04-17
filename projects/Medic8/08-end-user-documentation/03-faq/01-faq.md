# Medic8 Frequently Asked Questions (FAQ)

**Version:** 1.0
**Product:** Medic8 Healthcare Management System
**Date:** 2026-04-03

---

## 1 General Questions

### 1.1 What is Medic8?

Medic8 is a healthcare management system that helps hospitals and clinics manage patient records, prescriptions, laboratory tests, billing, appointments, and government reporting all in one place. It is built for healthcare facilities in Africa and works even when the internet is unreliable.

### 1.2 How much does Medic8 cost?

Medic8 uses a monthly subscription model. You pay per facility per month, with no upfront server purchase or installation fee. The pricing tiers are:

| Tier | Monthly Fee (UGX) | Best For |
|---|---|---|
| Starter | 150,000 | Small private clinics (1-5 consultation rooms) |
| Growth | 350,000 | Government health centres, mid-size facilities |
| Pro | 700,000 | Mission hospitals, NGO-supported facilities, multi-department hospitals |
| Enterprise | Custom pricing | Hospital networks, national referral hospitals |

All tiers include unlimited users. You pay per facility, not per user.

### 1.3 Do I need to install anything on my computer?

No. Medic8 is a cloud-based system. You open your web browser (Chrome, Firefox, Edge, or Safari), go to `https://app.medic8.com`, and log in. There is nothing to download or install on your computer.

For patients, there is an optional mobile app available on the Google Play Store (Android) and the Apple App Store (iPhone).

### 1.4 What internet speed do I need?

Medic8 is designed for the African context where internet is often slow or unreliable:

- **256 Kbps:** Enough for all clinical work (registration, consultation, prescribing, lab results, billing) in real time.
- **1 Mbps:** Recommended for full data synchronisation and the best experience.
- **No internet at all:** Medic8 continues to work in offline mode. All clinical workflows (registration, consultation, prescribing, dispensing, and lab result entry) function at full capacity. Data syncs automatically when connectivity returns.

### 1.5 Can I use Medic8 on my phone?

Yes. The Medic8 mobile app works on:

- **Android phones:** Android 7.0 or newer, with at least 1 GB of RAM. The app works on budget phones up to 5 years old.
- **iPhones:** iOS 15.0 or newer.

The app includes a Data-Lite Mode that compresses data for use on slow 2G and 3G mobile networks.

### 1.6 Is my patient data safe?

Yes. Medic8 uses multiple layers of protection:

- **Encryption at rest:** All patient health data is encrypted using AES-256-GCM, the same standard used by banks.
- **Encryption in transit:** All data sent between your device and the server is encrypted using TLS 1.2 or higher.
- **Audit trail:** Every action taken on patient data (view, create, edit, delete) is permanently recorded with the user's name and the exact time. This log cannot be altered.
- **PDPA compliance:** Medic8 complies with Uganda's Personal Data Protection Act (PDPA) 2019, including 72-hour breach notification.
- **Session timeout:** Clinical sessions automatically lock after 15 minutes of inactivity to prevent unauthorised access.
- **Two-step verification (MFA):** Required for admin and finance roles; optional for clinical staff.

### 1.7 Can multiple staff use Medic8 at the same time?

Yes. There is no limit on the number of staff who can use the system at the same time. All tiers include unlimited users. A doctor can be consulting in one room while the pharmacist dispenses in the pharmacy and the lab technician enters results in the lab, all simultaneously.

### 1.8 What happens if the internet goes down?

Medic8 has a built-in offline mode. When the internet connection is lost:

- **What keeps working:** Patient registration, OPD consultation, prescribing, dispensing, and lab result entry all continue at full capacity.
- **What pauses:** SMS reminders, mobile money payment verification, insurance membership checks, and DHIS2 report submission are paused until the internet returns.
- **When connectivity returns:** The system detects the connection and immediately syncs all data that was entered offline. No data is lost. The system is also generator-aware and detects power restoration to begin syncing.

### 1.9 How do I get support?

Support channels depend on your subscription tier:

| Channel | Availability |
|---|---|
| WhatsApp support | All tiers |
| Email (support@medic8.com) | All tiers |
| Phone support | Pro and Enterprise tiers |

### 1.10 Can I switch from ClinicMaster or OpenMRS?

Yes. Medic8 includes a data migration tool that imports patient records, clinical history, and financial data from ClinicMaster, OpenMRS, and UgandaEMR. The migration process is:

1. Export your data from the current system.
2. Upload the export file to Medic8.
3. The migration wizard maps the fields and imports the data.
4. Review the imported data for accuracy before going live.

The Medic8 team provides hands-on assistance during migration at no extra cost.

### 1.11 Can I try Medic8 before buying?

Yes. Go to `https://medic8.com` and click **Start Free Trial**. You get full access to all features for a trial period so you can evaluate the system with real workflows before committing.

### 1.12 Which languages does Medic8 support?

The Medic8 interface is available in English, French (Français), and Kiswahili. Go to Profile Settings → Language to select your preferred language. The patient plain-language discharge summary is also generated in the patient's preferred language.

### 1.13 Can I use the system if AI features are unavailable?

Yes. All AI features are additive — they assist workflows but do not block them. If an AI service is unavailable, you complete the step manually as normal.

### 1.14 Does the system save AI-generated notes automatically?

No. You must click **Approve Draft** to save any AI-generated text. If you close the draft without approving, nothing is saved.

### 1.15 Can I switch between English, French, and Kiswahili?

Yes. Go to Profile Settings → Language to change your preferred language at any time.

---

## 2 Clinical Questions

### 2.1 How do I find a returning patient?

You can search for a patient using any of the following identifiers:

- Patient name (supports common spelling variations)
- Phone number
- National Identification Number (NIN)
- Medical Record Number (MRN)
- Passport number
- UNHCR refugee ID
- NHIS member number

Use the search bar at the top of any screen or go to **Registration > Find Patient**. The system uses smart matching that accounts for name variations common in African naming patterns (compound surnames, clan names, and spelling differences).

### 2.2 What do the drug interaction alert levels mean?

Medic8 checks every prescription for interactions with the patient's other medications. There are 4 alert levels:

| Level | What You See | What To Do |
|---|---|---|
| **Tier 1 (Info)** | A small note in the sidebar | No action needed. For your awareness only. |
| **Tier 2 (Warning)** | An amber (yellow) banner | Read the warning. You may proceed. Consider whether the combination is appropriate. |
| **Tier 3 (Serious)** | A pop-up that blocks the screen | You must either change the prescription or enter a written reason to proceed. Your reason is permanently recorded. |
| **Tier 4 (Fatal)** | A hard stop. You cannot continue. | Contact the pharmacist immediately. The pharmacist must review and resolve the interaction before the prescription is accepted. |

Tier 3 and Tier 4 overrides are logged with the clinician's name, the time, and the reason.

### 2.3 How does paediatric dosing work?

For patients under 12 years of age, Medic8 enforces weight-based dosing for safety:

1. You enter the dose per kilogram (mg/kg).
2. The system calculates the total dose from the child's recorded weight.
3. If the calculated dose exceeds the adult maximum dose, it is capped automatically.
4. If the dose exceeds 10 times the expected amount (a possible decimal point error), the system blocks submission until you confirm.
5. The child must have a weight recorded within the last 24 hours. Without a recent weight, you cannot submit the prescription.

### 2.4 What is the Early Warning Score?

Medic8 uses the NEWS2 (National Early Warning Score 2) system. It is a standardised score calculated automatically from the vital signs entered by nursing staff (blood pressure, pulse, temperature, oxygen saturation, etc.). The score helps identify patients who are getting sicker:

| Score | Meaning | Action |
|---|---|---|
| 0-4 | Stable | Continue routine monitoring |
| 5-6 | May be deteriorating | Increase monitoring frequency; doctor is notified automatically |
| 7+ | Needs urgent attention | Immediate clinical review; consider ICU transfer |

### 2.5 Can I see a patient's records from another Medic8 facility?

Only in an emergency. Medic8 protects patient privacy by keeping clinical records within each facility. However, in an emergency, a clinician can access limited information from another facility:

1. Confirm the patient's identity using their name and date of birth (two-factor confirmation).
2. Emergency access reveals: allergies, current medications, blood group, HIV status (only if prior consent was given), and the last 3 diagnoses.
3. Emergency access expires after 24 hours.
4. The patient is notified by SMS that their records were accessed.
5. The access is permanently recorded in the audit trail with the clinician's name, facility, time, and reason.

### 2.6 How do I record a diagnosis?

1. During the consultation, click the **Diagnosis** tab.
2. Start typing the name of the condition. The system searches the ICD-10 classification and shows matching options.
3. Select the correct diagnosis from the list.
4. You can add multiple diagnoses if the patient has more than one condition. Mark one as the primary diagnosis.
5. Free-text diagnosis entry is not allowed. All diagnoses must be coded using ICD-10 to ensure accurate data and automated HMIS reporting.

### 2.7 What does "stock-aware prescribing" mean?

When you write a prescription, Medic8 shows you the current pharmacy stock level for each drug directly on the prescription screen. If a drug is out of stock (zero in pharmacy), the system warns you immediately and suggests available alternatives from the same drug class. This prevents you from prescribing a drug the patient cannot receive, saving both your time and the patient's time.

### 2.8 How are HMIS reports generated?

Medic8 automatically counts and tallies clinical data into the standard Uganda Ministry of Health HMIS reports:

- **HMIS 105 (Outpatient Monthly):** OPD diagnoses, lab tests, radiology, maternity, HIV/AIDS, immunisation, dental, and eye services are tallied automatically by age group and sex.
- **HMIS 108 (Inpatient Monthly):** Admissions, discharges, deaths, bed occupancy, and surgical operations are tallied automatically.
- **HMIS 033b (Weekly Surveillance):** The 27 priority diseases for IDSR surveillance are tallied automatically from OPD diagnoses.

No manual tallying is required. When the report is ready, you can submit it directly to DHIS2 (the national health information system) via API or export it for manual upload.

### 2.9 What is medication reconciliation?

Medication reconciliation is the process of reviewing all of a patient's current medications whenever they move between care settings. Medic8 makes this mandatory at every transition:

- OPD to inpatient admission
- Ward to ward transfer
- Inpatient to discharge
- Facility to facility referral

The system generates a list of all active medications, and the receiving clinician must review and confirm it before the transition is completed. This prevents medications from being accidentally continued, duplicated, or dropped during handover.

### 2.10 What are the "Five Rights" that Medic8 checks?

Every prescription in Medic8 is validated against 5 safety checks before it is accepted:

1. **Right patient:** The patient ID is confirmed at the point of entry.
2. **Right drug:** The drug is selected from the facility formulary (not free text).
3. **Right dose:** The dose is within the safe therapeutic range for the drug and the patient's weight.
4. **Right route:** The administration route is valid for the selected drug.
5. **Right time:** The frequency schedule is clinically appropriate.

If any of these checks fails, the prescription is blocked and a specific error message tells you which check failed and why.

---

## 3 Billing and Payment Questions

### 3.1 How does auto-billing work?

Every clinical action that has a corresponding price in your facility's price list automatically generates a charge on the patient's account. For example:

- A doctor orders a lab test and a lab charge appears on the patient's bill.
- The pharmacist dispenses a drug and a drug charge appears.
- An inpatient occupies a bed and a daily bed charge is posted.
- A procedure is performed and a procedure charge appears.

No one needs to manually enter these charges. The system generates a daily Missing Charge Detection report that compares clinical encounters against billing records and flags any service that was delivered but not billed.

### 3.2 Can patients pay with mobile money?

Yes. Medic8 supports both MTN Mobile Money (MoMo) and Airtel Money through API integration. Patients can pay:

- **At the facility:** The cashier selects the mobile money payment method and enters the transaction reference number. The system verifies the payment.
- **From the patient app:** The patient taps **Pay**, selects MoMo or Airtel Money, and confirms the payment on their phone.

Payments are automatically matched to patient accounts. Unmatched payments are posted to a suspense account and must be resolved within 48 hours.

### 3.3 How do I reconcile my cash at end of day?

1. Go to **Billing > Reconciliation** at the end of your shift.
2. Enter your opening float, the amount you are banking, and your closing float.
3. The system shows your total collections broken down by payment method (cash, MoMo, Airtel, card).
4. The system calculates the expected amounts and compares them with your entries.
5. If the difference is UGX 5,000 or less, the reconciliation is accepted.
6. If the difference exceeds UGX 5,000, the system flags it for supervisor review and you must provide an explanation.

### 3.4 How do insurance claims work?

When an insured patient completes their OPD visit or is discharged from inpatient care, Medic8 automatically generates an insurance claim that includes:

- All services rendered with procedure codes
- ICD-10 diagnosis codes
- Itemised drug list with quantities
- Total amount

The Insurance Clerk reviews the claim and submits it to the insurer. The claim format is configured per insurer to match their specific requirements. Rejected claims can be corrected and resubmitted.

### 3.5 What if a mobile money payment comes in but does not match a patient?

Unmatched payments are posted to a suspense account. The system generates a daily Unmatched Payments Report. The cashier or accountant must identify the patient and manually match the payment within 48 hours. Common reasons for unmatched payments include: the patient used a different phone number, the transaction reference was entered incorrectly, or the patient paid before registering.

### 3.6 What is the difference between Simple Mode and Advanced Mode in accounting?

- **Simple Mode:** Shows money received, money spent, outstanding insurance claims, and a daily financial summary. Suitable for small clinics that need basic financial tracking.
- **Advanced Mode:** Full double-entry accounting with chart of accounts, journal entries, trial balance, income statement, and balance sheet. Suitable for hospitals with an accountant on staff.

Both modes use the same underlying data. You can switch from Simple to Advanced at any time without losing any financial records.

### 3.7 Can I give patients credit?

Yes. Credit can be extended to staff, corporations, and mission organisations (NGOs, churches). All credit arrangements require prior approval from the Facility Admin. The system tracks credit ageing in buckets: 0-30 days, 31-60 days, 61-90 days, and 90+ days overdue. A monthly credit ageing report is generated automatically.

### 3.8 What happens with deposits for admitted patients?

A deposit is required for all inpatient admissions. The deposit amount is set by the facility and can vary by ward and patient category. During the stay, charges accumulate in real time. At discharge:

- If the final bill exceeds the deposit, the patient pays the remaining balance.
- If the deposit exceeds the final bill, the patient receives a refund.

---

## 4 Technical Questions

### 4.1 What browsers are supported?

| Browser | Minimum Version |
|---|---|
| Google Chrome | 90 |
| Mozilla Firefox | 88 |
| Microsoft Edge | 90 |
| Apple Safari | 14 |

Chrome is recommended. Keep your browser updated to the latest version for the best security and performance.

### 4.2 What are the minimum device requirements?

**For computers (web browser):**

- Screen resolution: 1024 x 768 pixels minimum
- Any modern laptop or desktop from the last 5 years
- Recommended: dual monitor for clinical workstations

**For Android phones/tablets:**

- Android 7.0 or newer
- 1 GB RAM minimum
- Works on budget phones up to 5 years old

**For iPhones/iPads:**

- iOS 15.0 or newer
- iPhone 6s or newer

### 4.3 How do I set up a barcode scanner?

Medic8 works with any USB barcode scanner that uses the HID (Human Interface Device) standard. This is the most common type.

1. Plug the scanner into a USB port on your computer.
2. It works immediately with no driver installation. The scanner acts like a keyboard and types the barcode value into whatever field is active on screen.
3. Test by clicking a search field in Medic8 and scanning a barcode.

### 4.4 How do I print receipts?

Medic8 supports 80mm thermal receipt printers that use the ESC/POS standard (this includes most receipt printers sold in Uganda).

1. Connect the printer to your computer via USB.
2. Install the printer driver from the manufacturer.
3. In Medic8, go to **Settings > Printing** and select your printer.
4. Print a test receipt to confirm it works.

You can also print receipts on regular A4 paper using any standard printer.

### 4.5 What happens to my data if I cancel my subscription?

Your data remains available for export for 90 days after cancellation. During this period you can download all patient records, financial data, and reports in a standard format. After 90 days, data is retained in encrypted archive for the minimum statutory retention period of 10 years (as required by Uganda Ministry of Health policy) but is no longer accessible through the Medic8 interface. Contact support@medic8.com to request archived data during the retention period.

### 4.6 How often is the system updated?

Medic8 is updated regularly with new features, improvements, and security patches. Updates are applied automatically with zero downtime. You do not need to do anything. When a new feature is added, a notification appears in the system with a brief explanation of what has changed.

### 4.7 Is there an API for connecting other systems?

Yes. Medic8 provides a FHIR R4 API (Fast Healthcare Interoperability Resources, Release 4). This is the international standard for health data exchange. The API exposes 14 resource types and supports SMART on FHIR for third-party app integration. The FHIR API is available on Pro and Enterprise tiers.

The laboratory module also supports HL7 v2 interfaces for connecting auto-analysers (Cobas, Mindray, Sysmex).

### 4.8 Can Medic8 connect to DHIS2?

Yes. Medic8 can submit HMIS reports directly to the Uganda DHIS2 platform (hmis2.health.go.ug) via API when internet connectivity is available. You can also export reports in DHIS2-compatible format for manual upload. The system tracks which reporting periods have been submitted and which are still pending.

### 4.9 How is data backed up?

Automatic daily backups are enabled by default for all cloud-hosted facilities. For local server installations, backups are saved to the local drive and synced to the cloud when internet is available. You can verify your backup schedule in **Settings > Backup**.

### 4.10 What happens if two people edit the same patient record while offline?

The system uses a smart merging process:

- **Non-clinical fields** (address, phone number, next of kin): The most recent change is kept.
- **Clinical fields** (diagnoses, prescriptions, allergies): Both versions are saved side by side and a clinician is asked to review the conflict. No clinical data is silently overwritten.

This ensures that no important clinical information is ever lost.
