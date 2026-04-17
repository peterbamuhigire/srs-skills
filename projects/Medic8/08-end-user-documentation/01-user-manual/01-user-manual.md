# Medic8 User Manual

**Version:** 1.0
**Product:** Medic8 Healthcare Management System
**Applicable Phase:** Phase 1 (Foundation)
**Date:** 2026-04-03

---

## 1 Getting Started

This section helps you set up Medic8 and learn the basics before you begin your daily work.

### 1.1 What You Need to Use Medic8

Medic8 runs in your web browser. You do not need to install any software on your computer. Make sure your setup meets the following:

- **Web browser:** Google Chrome 90 or newer, Mozilla Firefox 88 or newer, Microsoft Edge 90 or newer, or Apple Safari 14 or newer.
- **Screen size:** Your screen must be at least 1024 pixels wide and 768 pixels tall. A standard laptop or desktop monitor meets this requirement. For clinical workstations, two monitors side by side are recommended so you can view the patient record on one screen while writing notes on the other.
- **Internet connection:** Medic8 works on connections as slow as 256 Kbps (a basic 3G connection). For the best experience and full data synchronisation, a connection of 1 Mbps or faster is recommended. If your internet goes down completely, Medic8 continues to work in offline mode (see Section 11.2).
- **Mobile device (optional):** If you use the Medic8 mobile app, you need an Android phone running Android 7.0 or newer with at least 1 GB of memory (RAM), or an Apple iPhone running iOS 15.0 or newer.

### 1.2 Logging In

#### From a Computer (Web Browser)

1. Open your web browser.
2. Go to `https://app.medic8.com`.
3. Enter your email address or username.
4. Enter your password.
5. If your account uses two-step verification (also called MFA), the system sends a code to your phone. Enter that code when asked.
6. Select your facility from the list if you work at more than one location.
7. You are now on your home screen.

#### From a Phone (Mobile App)

1. Open the Medic8 app on your phone.
2. Enter your email address or username.
3. Enter your password.
4. If prompted, enter your two-step verification code.
5. Select your facility.
6. The app opens to your personal dashboard.

### 1.3 Navigating the Interface

Medic8 has three main navigation areas:

- **Sidebar (left side):** This is your main menu. It shows only the modules that match your role. A doctor sees clinical modules; a cashier sees billing modules. Click any menu item to open that module.
- **Top bar:** Shows your name, your facility name, and quick shortcuts for notifications (the bell icon), help (the question mark icon), and your profile settings (your initials or photo).
- **Breadcrumbs (below the top bar):** A trail of links showing where you are in the system. For example: Home > OPD > Patient Queue. Click any link in the trail to go back to that screen.

### 1.4 Setting Up Your Profile and Password

1. Click your initials or photo in the top-right corner of the screen.
2. Select **My Profile**.
3. Update your name, phone number, and photo if needed.
4. To change your password, click **Change Password**. Enter your current password, then enter your new password twice to confirm.
5. Click **Save**.

### 1.5 Understanding Your Role and Permissions

Medic8 uses roles to control what each person can see and do. Your Facility Administrator assigns your role when they create your account. Each role opens a different set of modules:

- A **Receptionist** sees patient registration, appointments, and the queue.
- A **Doctor** sees the OPD queue, consultations, prescribing, and patient history.
- A **Pharmacist** sees prescriptions, dispensing, and pharmacy stock.
- A **Lab Technician** sees lab requests, sample tracking, and result entry.
- A **Cashier** sees patient accounts, payments, and receipts.

You cannot access modules outside your role. This protects patient privacy and keeps the system simple for everyone.

### 1.6 Getting Help

- **In-app help:** Click the question mark icon in the top bar. A help panel opens on the right side of the screen with guidance for the page you are on.
- **Video tutorials:** Each module includes short video walkthroughs. Access them from Help > Video Tutorials in the sidebar.
- **WhatsApp support:** Send a message to the Medic8 support number provided by your facility. Support hours depend on your facility's subscription tier.
- **Email support:** Send an email to support@medic8.com with your facility name and a description of the problem.
- **Phone support:** Available for Pro and Enterprise tier facilities. The support number is listed in Help > Contact Support.

---

## 2 Facility Administrator Guide

The Facility Administrator sets up and manages the Medic8 system for the facility. This chapter covers all configuration tasks.

### 2.1 Initial Facility Setup Wizard

When your facility account is first created, Medic8 walks you through a 5-step setup wizard. Complete all 5 steps to make the system ready for use. The target is to have your facility operational within 2-4 hours.

1. **Facility profile:** Enter your facility name, physical address, phone number, email address, and timezone. Upload your facility logo (this appears on receipts and reports).
2. **Modules:** Choose which modules to activate. Start with the modules your facility needs today. You can add more modules later without losing any data. Phase 1 modules include Patient Registration, OPD, Pharmacy, Lab, Billing, and Appointments.
3. **Staff accounts:** Create user accounts for your staff. For each person, enter their name, email, phone number, and assign a role (Receptionist, Doctor, Nurse, Pharmacist, Lab Technician, Cashier, etc.). Each person receives a login email with instructions to set their password.
4. **Price list:** Enter the prices for your services. This includes consultation fees, lab test prices, drug prices, and procedure charges. Medic8 uses this list to automatically calculate patient bills.
5. **Review and finish:** Review all your settings. Click **Complete Setup** to begin using Medic8.

### 2.2 Configuring Modules

1. Go to **Settings > Modules**.
2. Each module has an on/off switch. Turn on the modules your facility uses. Turn off modules you do not need.
3. When you activate a new module, the system displays a brief guided setup for that module.
4. Deactivating a module hides it from all users but does not delete any data. You can reactivate it at any time.

### 2.3 Managing Staff Accounts and Roles

1. Go to **Settings > Staff Management**.
2. To add a new staff member, click **Add Staff**. Enter their details and assign a role.
3. To change a staff member's role, click their name, then click **Edit Role**. Select the new role from the list.
4. To deactivate a staff member who has left, click their name, then click **Deactivate**. Their account is locked but their activity history is preserved for audit purposes.
5. Roles available in Medic8: Facility Admin, Doctor, Clinical Officer, Nurse/Midwife, Pharmacist, Lab Technician, Radiographer, Receptionist, Records Officer, Cashier, Insurance Clerk, Accountant, Store Keeper, and Auditor.

### 2.4 Setting Up the Price List

1. Go to **Settings > Price List**.
2. The price list is organised by category: Consultation, Laboratory, Pharmacy, Radiology, Procedures, and Bed Charges.
3. Click a category to see the items. Enter the price for each item in Uganda Shillings (UGX) or your facility's local currency.
4. You can set different prices for different patient categories (Adult, Paediatric, Staff, VIP, Indigent/Sponsored).
5. Click **Save** after entering your prices.

### 2.5 Configuring the Drug Formulary

1. Go to **Settings > Drug Formulary**.
2. Medic8 comes pre-loaded with a standard drug list including generic names, brand names, strengths, and forms. This list follows the Uganda National Drug Authority Essential Medicines List.
3. Review the list and adjust it for your facility. You can add drugs, remove drugs you do not stock, or update prices.
4. Mark controlled substances (narcotics) so the system tracks them in the narcotic register.
5. The Look-Alike/Sound-Alike (LASA) drug list is pre-configured. LASA drugs are pairs of medicines with similar names that could be confused (for example, hydrOXYzine and hydrALAZINE). The system highlights the different letters in capital letters to prevent mix-ups.

### 2.6 Setting Up the Lab Test Catalogue

1. Go to **Settings > Lab Test Catalogue**.
2. A standard list of lab tests is pre-loaded with reference ranges (the normal expected values).
3. Review and update the list to match the tests your laboratory can perform.
4. For each test, check that the reference ranges match your lab's validated ranges.
5. Set critical value thresholds (panic values) for tests that require urgent attention. For example, potassium above 6.5 mmol/L or glucose below 2.5 mmol/L.

### 2.7 Managing Insurance Schemes

1. Go to **Settings > Insurance Schemes**.
2. Click **Add Scheme** to add an insurance company (for example, NHIS, AAR, Jubilee, Prudential).
3. For each scheme, enter the benefit schedule. This defines what the insurance covers and the co-pay percentage the patient must pay.
4. Configure the claim submission format for each insurer. Medic8 generates claims in the format each insurer requires.

### 2.8 System Settings

1. Go to **Settings > General**.
2. Update your facility name, logo, and contact information.
3. Set your receipt format (header text, footer text, receipt size).
4. Set your timezone (default: East Africa Time, UTC+3).
5. Configure the SMS gateway (Africa's Talking) for appointment reminders and notifications.
6. Configure mobile money API keys for MTN MoMo and Airtel Money if your facility accepts mobile money payments.
7. Set the backup schedule (automatic daily backups are enabled by default).

---

## 3 Receptionist Guide

The receptionist is the first person a patient meets. This chapter covers patient registration, appointment management, and queue management.

### 3.1 Registering a New Patient

Follow these steps to register a patient visiting your facility for the first time:

1. Click **Registration > New Patient** in the sidebar.
2. Enter the patient's full name (surname and given names).
3. Select the patient's sex.
4. Enter their date of birth. If the patient does not know their exact date of birth, enter an estimated age and the system calculates an approximate date of birth.
5. Enter at least one contact method: a phone number or a physical address. The phone number is important because it is used for appointment reminders and mobile money payments.
6. Select the patient category: Adult, Paediatric (under 12 years), Staff, VIP, or Indigent/Sponsored.
7. Enter optional details if available: National Identification Number (NIN), next-of-kin name and phone, blood group, known allergies, and chronic conditions.
8. For paediatric patients, link the child to their guardian's record.
9. Take a photo of the patient using the camera icon (optional but recommended for identification).
10. Click **Save**. The system generates a unique Medical Record Number (MRN) automatically. This number identifies the patient across all visits.

*Note: The system requires at minimum a name, sex, age or date of birth, and at least one contact method. A registration cannot be saved without these fields.*

### 3.2 Looking Up a Returning Patient

1. Click **Registration > Find Patient** in the sidebar, or use the search bar at the top of any screen.
2. Search by any of the following: patient name, phone number, NIN, MRN, passport number, or UNHCR refugee ID.
3. The system displays matching results. Click the correct patient to open their record.
4. Confirm the patient's identity by checking their name, photo, and date of birth.

### 3.3 Managing Patient Identifiers

Each patient can have multiple identifiers stored in their record:

- MRN (assigned automatically by the system)
- NIN (National Identification Number)
- Passport number
- UNHCR refugee ID
- NHIS number (National Health Insurance Scheme)
- Phone number
- Email address

Any of these identifiers can be used to search for the patient. To add or update an identifier, open the patient's record and click **Edit Identifiers**.

### 3.4 Handling Duplicate Patient Detection

When you register a new patient, Medic8 automatically checks for possible duplicate records. The system compares the name, date of birth, NIN, and phone number against existing records using a smart matching method that accounts for spelling variations and alternative name formats common in African naming patterns.

- If the system finds a possible match with a confidence score above 80%, a warning appears that you cannot dismiss without action.
- Review the potential match carefully. If the patient already exists, click **Select Existing** to use the existing record.
- If you are certain this is a new patient, click **Confirm New Patient** to create a new record.
- If duplicate records are discovered later, only the Records Officer or Facility Admin can merge them. A merge combines all clinical history, billing records, and visit data under one record with a full audit trail. Merges can be reversed within 30 days.

### 3.5 Booking Appointments

1. Click **Appointments > New Appointment**.
2. Search for the patient by name, phone, or MRN.
3. Select the doctor or department.
4. View the doctor's availability calendar and select a date and time.
5. Click **Book**. The patient receives an SMS or WhatsApp reminder automatically (if configured).
6. To reschedule, open the appointment and click **Reschedule**. To cancel, click **Cancel Appointment**.

### 3.6 Managing the OPD Queue

1. Click **OPD > Queue** in the sidebar.
2. The queue shows all patients who have checked in for today's OPD visits. Patients are sorted by triage priority level:
   - **Emergency:** Immediate attention. These patients jump to the top of every queue.
   - **Urgent:** Must be seen within 30 minutes of triage.
   - **Semi-urgent:** Must be seen within 60 minutes of triage.
   - **Non-urgent:** Seen in the order they arrived.
3. When a patient arrives, click **Check In** next to their appointment, or click **Walk-In** to add a patient without an appointment.
4. The patient moves to the triage queue, then to the doctor's queue after triage is completed.

### 3.7 Walk-In Patients

Walk-in patients do not have a scheduled appointment. To add a walk-in:

1. Register the patient (or look them up if they are a returning patient).
2. Click **OPD > Walk-In** and select the patient.
3. The patient is added to the triage queue with the current time as their arrival time.

---

## 4 Doctor and Clinical Officer Guide

This chapter covers the clinical workflow from seeing a patient in the OPD through to completing the visit.

### 4.1 Viewing the OPD Queue

1. Click **OPD > My Queue** in the sidebar.
2. Your queue shows patients assigned to you, sorted by triage priority and wait time. Emergency patients appear at the top with a red marker. The wait time since triage is shown for each patient.
3. Click a patient's name to begin the consultation.

### 4.2 Starting a Consultation

1. Click the patient's name in your queue.
2. The consultation screen opens with the patient's profile summary on the left: name, age, sex, photo, blood group, allergies, and chronic conditions.
3. The main area shows tabs for the consultation workflow: Vitals, SOAP Notes, Diagnosis, Prescriptions, Investigations, Procedures, and Referral.

### 4.3 Recording Vital Signs and Triage

If the nurse has already recorded vital signs during triage, they appear on the Vitals tab. If you need to record or update vitals:

1. Click the **Vitals** tab.
2. Enter the readings: blood pressure (BP), temperature, pulse rate, oxygen saturation (SpO2), weight, height, and BMI (calculated automatically from weight and height).
3. For children, enter the Mid-Upper Arm Circumference (MUAC) for nutritional screening.
4. Click **Save Vitals**.

### 4.4 Writing SOAP Clinical Notes

SOAP stands for Subjective, Objective, Assessment, and Plan. This is the standard format for clinical notes.

1. Click the **SOAP Notes** tab.
2. **Subjective:** Record what the patient tells you about their complaint. Use either free-text or the structured template.
3. **Objective:** Record your examination findings.
4. **Assessment:** Enter your clinical impression.
5. **Plan:** Record the treatment plan, including medications, investigations, procedures, and follow-up.
6. Click **Save Notes**. Notes are auto-saved as you type to prevent loss from power failures or browser crashes.

### 4.5 Entering Diagnoses (ICD-10 Search)

1. Click the **Diagnosis** tab.
2. Start typing the diagnosis name. Medic8 searches the ICD-10 classification and shows matching options. ICD-10 is the international standard code system for diseases and health conditions.
3. Select the correct diagnosis from the list. You may add multiple diagnoses if the patient has more than one condition.
4. Mark one diagnosis as the primary diagnosis.
5. Free-text diagnosis entry is not permitted. All diagnoses must use ICD-10 codes. This ensures accurate HMIS reporting and data quality.

### 4.6 Writing Prescriptions (Stock-Aware, Drug Interaction Alerts)

1. Click the **Prescriptions** tab.
2. Start typing the drug name. Medic8 shows matching drugs from the facility formulary.
3. For each drug, the system displays the current pharmacy stock level. If stock is zero, a warning appears and the system suggests available alternatives from the same drug class.
4. Enter the dose, frequency (for example, "twice daily"), duration (for example, "5 days"), route (for example, "oral"), and quantity.
5. The system automatically checks for drug interactions with the patient's other medications and allergies.
6. Click **Save Prescription**. The prescription is sent to the pharmacy queue.

### 4.7 Handling Drug Interaction Alerts (4 Tiers)

Medic8 uses a 4-tier alert system to warn about drug interactions. Here is what each tier means and what you should do:

1. **Tier 1 (Info):** A small note appears in the prescription sidebar. This is for your information only. No action is needed. You may proceed normally.
2. **Tier 2 (Warning):** An amber (yellow) banner appears at the top of the prescription. Read the warning. You may proceed without taking any extra step, but consider whether the combination is appropriate for this patient.
3. **Tier 3 (Serious):** A pop-up window blocks the screen. You cannot continue until you either change the prescription or provide a written reason why you choose to proceed despite the risk. Your reason, name, and the time are recorded in the system permanently.
4. **Tier 4 (Fatal):** The system stops completely. You cannot override this alert. A pharmacist must review and resolve the interaction before the prescription is accepted. Contact the pharmacist immediately.

### 4.8 Paediatric Prescribing (Weight-Based Dosing)

For patients under 12 years of age, Medic8 applies special safety rules:

- All prescriptions must use weight-based dosing. You enter the dose per kilogram (mg/kg), and the system calculates the total dose based on the child's recorded weight.
- The system applies an adult maximum dose cap. If the calculated dose exceeds the adult maximum, it is automatically capped and you are notified.
- If the calculated dose exceeds 10 times the expected dose, the system flags this as a potential decimal point error and blocks submission until you confirm.
- The child must have a weight recorded within the last 24 hours. If no recent weight is on file, the system blocks prescription submission until a weight is entered.

### 4.9 Requesting Lab Investigations

1. Click the **Investigations** tab.
2. Click **Lab Request**.
3. Search for the test (for example, "Full Blood Count" or "Malaria mRDT").
4. Select the test and add any clinical notes for the lab team.
5. Click **Send Request**. The lab team receives an instant notification. The charge is automatically added to the patient's bill.

### 4.10 Requesting Radiology Investigations

1. Click the **Investigations** tab.
2. Click **Radiology Request**.
3. Select the type of imaging (for example, X-ray, Ultrasound).
4. Enter the body part and clinical reason.
5. Click **Send Request**. The radiology team receives an instant notification.

### 4.11 Recording Procedures

1. Click the **Procedures** tab.
2. Select the procedure performed from the list.
3. Enter a brief description of the procedure and the outcome.
4. Click **Save**. The charge is automatically added to the patient's bill.

### 4.12 Creating Referrals

1. Click the **Referral** tab.
2. Select the type: internal (to another department in your facility) or external (to another hospital or specialist).
3. Select the receiving department or enter the external facility name.
4. Enter the reason for referral and any relevant clinical details.
5. Click **Send Referral**. The system generates an electronic referral letter.

### 4.13 Ending a Visit and Discharge

1. When the consultation is complete, click **End Visit** at the bottom of the consultation screen.
2. If the patient is being discharged from inpatient care, the system requires that the following are completed before discharge can be finalised:
   - Diagnosis (ICD-10 coded)
   - Discharge summary
   - Medication reconciliation (review of all active medications)
   - Follow-up plan with a date and responsible clinician
   - Billing settlement (balance paid or credit approved by the Facility Admin)
3. Click **Confirm End Visit**. The patient is removed from your queue.

### 4.14 Viewing Patient History

1. From any patient's record, click the **History** tab.
2. The complete visit history appears in one screen, with the most recent visit at the top.
3. Each visit shows the date, diagnoses, prescriptions, lab results, and clinical notes.
4. Use the filter to narrow by date range or visit type.

### 4.15 Understanding the Early Warning Score (NEWS2)

NEWS2 stands for National Early Warning Score 2. It is a scoring system that helps identify patients who are getting sicker and need urgent attention. Medic8 calculates the NEWS2 score automatically from the vital signs entered by nursing staff.

- **Score 0-4:** The patient is stable. Continue routine monitoring.
- **Score 5-6:** The patient may be deteriorating. The system increases the monitoring frequency alert and notifies you (the responsible doctor).
- **Score 7 or higher:** The patient needs immediate review. Consider transferring the patient to intensive care. The system generates an urgent alert.

---

## 5 Nurse and Midwife Guide

This chapter covers nursing workflows including triage, vital signs, drug administration, and bedside tablet use.

### 5.1 Triage Workflow

Triage means assessing how urgently a patient needs care. Follow these steps:

1. Click **OPD > Triage Queue** in the sidebar.
2. Select the next patient waiting for triage.
3. Record vital signs: blood pressure, temperature, pulse rate, oxygen saturation (SpO2), weight, and height.
4. For children, record the Mid-Upper Arm Circumference (MUAC) for nutritional screening.
5. Assign a triage level based on your clinical assessment:
   - **Emergency:** Life-threatening. The patient must be seen immediately.
   - **Urgent:** Needs care within 30 minutes.
   - **Semi-urgent:** Needs care within 60 minutes.
   - **Non-urgent:** Can wait and will be seen in queue order.
6. Click **Complete Triage**. The patient moves to the doctor's queue, positioned according to their triage level. Emergency patients jump to the top.

### 5.2 Recording Nursing Notes

1. Open the patient's record.
2. Click the **Nursing Notes** tab.
3. Enter your observations and any care provided. Each note is timestamped automatically with your name and the current time.
4. For inpatients, record notes at every shift change.
5. Click **Save**. Notes are auto-saved as you type.

### 5.3 Drug Administration (MAR)

MAR stands for Medication Administration Record. It is the record of every dose of medicine given to a patient.

1. Click **IPD > Drug Round** in the sidebar (for inpatients), or open the patient's record and click the **MAR** tab.
2. The screen shows all medications currently ordered for the patient, with the scheduled times.
3. For each medication at the current time:
   - Click **Given** if you administered the dose.
   - Click **Held** if you withheld the dose for a clinical reason (enter the reason).
   - Click **Refused** if the patient refused to take the medication (record this in the notes).
4. Your name and the exact time are recorded automatically.

### 5.4 Understanding the Drug Round Workflow

The drug round has 4 possible statuses for each scheduled dose:

- **Ordered:** The doctor has prescribed the medication but it has not been administered yet.
- **Given:** The nurse has administered the medication to the patient.
- **Held:** The nurse withheld the medication for a clinical reason (for example, the patient's blood pressure was too low). The reason must be documented.
- **Refused:** The patient refused to take the medication. This must be documented and the doctor should be informed.

### 5.5 Vital Signs Charting

1. Open the patient's record and click the **Vital Signs Chart** tab.
2. A graphical chart shows the patient's vital signs over time (blood pressure, temperature, pulse, oxygen saturation).
3. To add new readings, click **Record Vitals** and enter the current measurements.
4. The system calculates the NEWS2 score automatically from the readings. If the score reaches 5 or above, the system alerts the responsible doctor.
5. For inpatients, the fluid balance chart (intake and output) is accessible from the same screen.

### 5.6 Using the Tablet at Bedside (One-Handed Mode)

Medic8 includes a one-handed mode designed for nurses using a tablet at the bedside:

- Large buttons and touch targets for easy use while standing or holding the tablet in one hand.
- Quick vital signs entry with large number keys.
- Drug round screen optimised for tap-and-confirm workflow: tap **Given**, **Held**, or **Refused** with one finger.
- To enable one-handed mode, tap the hand icon in the top bar of the mobile or tablet interface.

---

## 6 Pharmacist Guide

This chapter covers the pharmacy workflow from receiving prescriptions to dispensing drugs and managing stock.

### 6.1 Viewing the Prescription Queue

1. Click **Pharmacy > Prescription Queue** in the sidebar.
2. The queue shows all prescriptions awaiting dispensing, sorted by time received. Prescriptions marked URGENT appear at the top.
3. Each entry shows the patient name, the prescribing doctor, and a list of prescribed drugs.

### 6.2 Dispensing Workflow

Follow these 4 steps for each prescription:

1. **Verify:** Click the prescription to open it. Review the drugs, doses, frequencies, routes, and quantities. Check for drug interaction alerts. If anything is unclear, contact the prescribing doctor.
2. **Dispense:** For each drug, confirm the quantity dispensed. The system deducts the quantity from pharmacy stock automatically.
3. **Label:** Print a dispensing label for each drug. The label shows the patient name, drug name, dose, frequency, and instructions. Click **Print Label**.
4. **Next:** Click **Complete** to mark the prescription as dispensed. Move to the next prescription in the queue.

### 6.3 Handling Partial Dispensing

If the pharmacy does not have enough stock to fill the full prescription:

1. Enter the quantity you are dispensing now (less than the prescribed quantity).
2. The system creates a pending balance for the remaining quantity.
3. When new stock arrives, the pending balance appears in the **Partial Dispense Pending** list.
4. Dispense the remaining quantity when available.

### 6.4 Generic Substitution

If a prescribed branded drug is not in stock but a generic equivalent is available:

1. Click **Substitute** next to the drug.
2. Select the generic equivalent from the suggested alternatives.
3. The prescribing doctor receives a notification about the substitution.
4. The substitution is recorded in the dispensing record.

### 6.5 Managing Pharmacy Stock

1. Go to **Pharmacy > Stock Management**.
2. **Receiving stock (GRN):** When a new delivery arrives, click **Goods Received Note**. Enter the supplier, drug names, quantities, batch numbers, expiry dates, and costs. Click **Save**. Stock levels are updated immediately.
3. **Transfers:** To move stock between stores (for example, from the main pharmacy to a ward pharmacy), click **Transfer**. Select the source store, destination store, drugs, and quantities.
4. **Adjustments:** If a physical count does not match the system count, click **Adjustment**. Enter the actual count and the reason for the difference (for example, breakage, spillage, or theft).

### 6.6 Tracking Expiring Drugs

1. Go to **Pharmacy > Expiry Tracker**.
2. The system flags drugs that will expire within 90 days with a warning.
3. Drugs are listed by expiry date, with the soonest to expire at the top.
4. Take action to use, return, or dispose of expiring stock before the expiry date.
5. Minimum stock level alerts also appear here. When a drug falls below the minimum level you have set, the system sends an alert to the pharmacist and facility administrator.

### 6.7 Narcotic Register (Controlled Substances)

Controlled substances (narcotics and other scheduled drugs) have extra tracking requirements by law:

1. Go to **Pharmacy > Narcotic Register**.
2. Every time you dispense a controlled substance, the system automatically records: patient name, drug name and strength, quantity dispensed, prescribing doctor, dispensing pharmacist, and the witness.
3. A running balance is maintained for each controlled substance.
4. If the physical count does not match the system balance, the system immediately alerts the Facility Administrator.
5. Print the register at any time for inspection by regulatory authorities.

### 6.8 Understanding Tall Man Lettering for LASA Drugs

LASA stands for Look-Alike/Sound-Alike. These are drug pairs with names that look or sound similar and could easily be confused. To prevent dispensing errors, Medic8 displays the different letters in TALL (capital) letters wherever drug names appear.

Examples:

- hydr**OXYZ**ine vs hydr**ALAZ**INE
- chlorpr**OPAM**IDE vs chlorpr**OMAZ**INE

When you see tall letters in a drug name, pay extra attention to confirm you are selecting the correct drug. The list of LASA drugs is maintained by the pharmacy lead and can be updated in Settings.

---

## 7 Lab Technician Guide

This chapter covers the laboratory workflow from receiving requests to delivering results.

### 7.1 Viewing Pending Lab Requests

1. Click **Lab > Pending Requests** in the sidebar.
2. The list shows all lab requests from OPD, IPD, and Emergency, sorted by time. Requests marked URGENT appear at the top. Emergency patients' requests jump all queues.
3. Each request shows the patient name, the test ordered, the requesting doctor, and the time the request was made.

### 7.2 Collecting Samples and Printing Barcode Labels

1. Click the request to open it.
2. Record the sample type (blood, urine, sputum, etc.) and the time of collection.
3. Click **Print Label**. A barcode label prints with the patient name, MRN, test name, date, and a unique barcode for tracking.
4. Attach the label to the sample container.
5. The sample status changes from "Requested" to "Collected."

### 7.3 Updating Specimen Status

Track the sample through the laboratory process by updating its status:

1. **Requested:** The doctor has ordered the test (set automatically).
2. **Collected:** The sample has been collected from the patient (you set this during collection).
3. **Received:** The sample has arrived at the lab bench (set this when the sample reaches the processing area).
4. **Processing:** The test is being performed (set this when you begin the analysis).
5. **Result Ready:** The result has been entered and is awaiting validation.

Update the status by clicking the status button in the request. This helps clinical staff track where their patient's sample is in the process.

### 7.4 Entering Lab Results

1. Open the test request.
2. Click **Enter Result**.
3. Enter the result value for each parameter. The reference range (normal expected values) is displayed next to each field.
4. If your lab has an auto-analyser connected to Medic8 (via HL7 interface), results are imported automatically. Review the imported results for accuracy.
5. Click **Save Result**.

### 7.5 Understanding Auto-Flagged Abnormal and Critical Results

Medic8 automatically compares each result against the reference ranges:

- **High (H):** The result is above the normal range. It is marked with an "H" flag.
- **Low (L):** The result is below the normal range. It is marked with an "L" flag.
- **Critical:** The result exceeds the critical value threshold (panic value). For example, potassium above 6.5 mmol/L or glucose below 2.5 mmol/L. A red alert appears immediately.

### 7.6 Escalating Critical Values

When a result exceeds the critical threshold, the system triggers a timed escalation:

1. An immediate notification is sent to the requesting doctor.
2. If the doctor does not acknowledge the notification within 30 minutes, the system escalates to the ward sister.
3. If still not acknowledged within 60 minutes, the system escalates to the Facility Administrator.
4. All escalation steps are timestamped and recorded in the audit trail.

You should also attempt to contact the doctor by phone if the result is life-threatening.

### 7.7 Result Validation (Supervisor Workflow)

1. After you enter a result, it goes to the lab supervisor for validation.
2. The supervisor reviews the result in **Lab > Pending Validation**.
3. If the result is acceptable, the supervisor clicks **Validate**. The result becomes visible to the requesting doctor.
4. If the result needs re-testing, the supervisor clicks **Reject** with a reason. The test returns to the processing queue.

### 7.8 QC Record Entry

Quality Control (QC) means running control samples to verify that lab equipment is giving accurate results.

1. Go to **Lab > Quality Control**.
2. Enter the QC results for each control level (low, normal, high).
3. The system plots the results on a Levey-Jennings chart. This chart shows whether your equipment is performing within acceptable limits over time.
4. If a QC result falls outside the acceptable range, the system flags it. Investigate and resolve the issue before running patient samples.

---

## 8 Cashier and Billing Clerk Guide

This chapter covers patient billing, payment collection, and daily reconciliation.

### 8.1 Looking Up a Patient Account

1. Click **Billing > Find Patient** in the sidebar.
2. Search by patient name, phone number, NIN, or MRN.
3. Click the patient's name to open their account.
4. The account shows all charges (services received), payments made, and the current balance.

### 8.2 Understanding Auto-Billing

Medic8 automatically generates charges for every clinical action that has a corresponding entry in the facility price list:

- A lab test request generates a lab charge.
- A drug dispensed generates a drug charge.
- A bed day generates a bed charge (for inpatients).
- A procedure performed generates a procedure charge.

You do not need to enter charges manually for standard services. The charges appear in the patient's account in real time as clinical staff perform their work.

### 8.3 Collecting Cash Payments

1. Open the patient's account.
2. Click **Receive Payment**.
3. Select **Cash** as the payment method.
4. Enter the amount received.
5. Click **Save**. The payment is recorded and the balance is updated.
6. Print the receipt (see Section 8.5).

### 8.4 Collecting Mobile Money Payments (MoMo/Airtel)

1. Open the patient's account.
2. Click **Receive Payment**.
3. Select **MTN MoMo** or **Airtel Money** as the payment method.
4. Enter the transaction reference number from the mobile money confirmation message.
5. The system verifies the payment against the mobile money API.
6. Click **Save**. The payment is recorded.
7. If the payment cannot be automatically matched to the patient (for example, the reference number does not correspond to this patient), the payment is posted to a suspense account. You or the accountant must manually match it within 48 hours. The system generates a daily unmatched payments report.

### 8.5 Generating and Printing Receipts

1. After recording a payment, click **Print Receipt**.
2. The receipt shows the facility name, logo, patient name, services received, amount paid, payment method, date, and receipt number.
3. If your facility uses a thermal receipt printer (80mm ESC/POS), the receipt prints automatically. Otherwise, it opens as a printable page on your screen.

### 8.6 Daily Cashier Reconciliation (End-of-Day)

At the end of each shift or at the end of the day, every cashier must reconcile their collections:

1. Click **Billing > Reconciliation**.
2. Enter your opening float (the amount of cash you started the day with).
3. The system shows all collections for your session, broken down by payment method: cash, MTN MoMo, Airtel Money, and card.
4. Enter the amount you are banking (depositing to the bank or safe).
5. Enter your closing float.
6. The system calculates the expected totals and compares them with what you have entered.
7. If there is a discrepancy exceeding UGX 5,000, the system flags it for supervisor review.
8. Click **Submit Reconciliation**. Your supervisor reviews and approves the reconciliation.

### 8.7 Handling Discrepancies

Common causes of discrepancies and what to do:

- **Over-collection:** You collected more cash than the system expected. Check if you missed recording a payment. If the excess cannot be explained, report it to your supervisor.
- **Under-collection:** You collected less cash than the system expected. Check if a patient left without paying, or if you gave incorrect change. Report it to your supervisor.
- **Unmatched mobile money payments:** A payment came in via MoMo or Airtel but has not been matched to a patient account. Open the unmatched payments report, identify the patient, and match the payment manually.

---

## 9 Insurance Clerk Guide

This chapter covers insurance verification, claims processing, and rejection management.

### 9.1 Verifying Patient Insurance Membership

1. When a patient presents an insurance card, go to the patient's record and click the **Insurance** tab.
2. Click **Verify Membership**.
3. Enter the insurance scheme (for example, NHIS, AAR, Jubilee) and the member number.
4. The system checks the membership status:
   - **Active:** The patient is covered. Proceed with the visit.
   - **Expired:** The patient's coverage has ended. Inform the patient that they must pay directly.
   - **Suspended:** The coverage is temporarily paused. Contact the insurer for clarification.

### 9.2 Understanding Benefit Schedules and Co-Pay

Each insurance scheme has a benefit schedule that defines:

- Which services are covered (for example, OPD consultation, lab tests, drugs).
- The maximum amount the insurer will pay for each service.
- The co-pay percentage, which is the portion the patient must pay themselves.

When an insured patient receives services, the system automatically splits the bill:

- The insurer's portion is posted to the insurance receivables ledger.
- The patient's co-pay portion is collected at the point of service.

### 9.3 Generating Insurance Claims

1. When a patient's visit is complete (OPD) or when they are discharged (IPD), the system automatically generates an insurance claim.
2. The claim includes: all services rendered with procedure codes, ICD-10 diagnosis codes, an itemised list of drugs with quantities, and the total amount.
3. Go to **Insurance > Pending Claims** to review generated claims before submission.
4. Check that the diagnosis codes and service codes are correct.

### 9.4 Submitting Claims to Insurers

1. Go to **Insurance > Pending Claims**.
2. Select the claims ready for submission.
3. Click **Submit**. The system formats the claim in the format required by each specific insurer and submits it electronically where supported. For insurers that require paper submission, the system generates a printable claim form.
4. The claim status changes to "Submitted."

### 9.5 Managing Rejected Claims

1. When an insurer rejects a claim, the rejection reason is displayed in **Insurance > Rejected Claims**.
2. Review the rejection reason (for example, "member not covered for this service," "incorrect diagnosis code," or "claim submitted after deadline").
3. Correct the issue in the claim.
4. Click **Resubmit**.
5. The system tracks rejection rates per insurer for performance analysis.

### 9.6 Tracking Insurance Receivables

1. Go to **Insurance > Receivables**.
2. The ageing report shows outstanding claims by insurer, grouped into time buckets:
   - 0-30 days
   - 31-60 days
   - 61-90 days
   - 90+ days overdue
3. Follow up with insurers on overdue claims, starting with the oldest.
4. A monthly ageing report is automatically generated for the Facility Accountant and Facility Administrator.

---

## 10 Patient Guide (Mobile App)

This chapter is for patients who use the Medic8 mobile app to access their own health information.

### 10.1 Downloading and Setting Up the App

1. **Android:** Open the Google Play Store on your phone. Search for "Medic8." Tap **Install**. Your phone must be running Android 7.0 or newer and have at least 1 GB of RAM.
2. **iPhone:** Open the Apple App Store. Search for "Medic8." Tap **Get**. Your iPhone must be running iOS 15.0 or newer.
3. Open the app after installation.
4. Enter your phone number or email address.
5. Enter the one-time code sent to your phone via SMS to verify your identity.
6. Create a password.
7. Select the facility (or facilities) where you receive care.

### 10.2 Viewing Your Health Records

1. Open the app and go to **My Health**.
2. You can see: past visits (dates, doctors seen, diagnoses), treatments prescribed, procedures performed, and referral letters.
3. Records are organised by visit date, with the most recent at the top.
4. You can only see your own records. No one else can access your records through your app unless you add them as a family member (see Section 10.8).

### 10.3 Viewing Lab Results

1. Go to **My Health > Lab Results**.
2. Your results are listed by date. Tap a result to see the details.
3. Results that are outside the normal range are highlighted.
4. If you have questions about a result, contact your doctor.
5. Large files like radiology images download only on WiFi by default to save your mobile data.

### 10.4 Booking an Appointment

1. Go to **Appointments > Book New**.
2. Select the facility.
3. Select the department or doctor.
4. View available dates and times.
5. Tap a slot to book. You receive an SMS or WhatsApp confirmation.
6. To cancel or reschedule, go to **Appointments > My Appointments**, select the appointment, and tap **Cancel** or **Reschedule**.

### 10.5 Paying Fees via Mobile Money

1. Go to **Payments > Pay Bill**.
2. You can see your outstanding balance for each facility.
3. Tap **Pay**.
4. Select **MTN MoMo** or **Airtel Money**.
5. Enter your mobile money number. A payment prompt is sent to your phone.
6. Confirm the payment on your phone.
7. The payment is recorded instantly and your balance is updated. A receipt is available in **Payments > Receipts**.

### 10.6 Setting Medication Reminders

1. Go to **Medications > Active Prescriptions**.
2. Tap a medication to see the schedule (for example, "take 1 tablet twice daily").
3. Tap **Set Reminder**. The app sends you a notification at the scheduled times to remind you to take your medicine.
4. You can adjust reminder times to match your daily routine.

### 10.7 Managing Family Members' Records

1. Go to **My Family**.
2. Tap **Add Family Member**.
3. Enter the family member's name and their relationship to you (for example, child, spouse, parent).
4. The family member must confirm the link from their phone, or you can do it at the facility reception.
5. Once linked, you can view their health records, book appointments on their behalf, and pay their bills from your app.

### 10.8 Offline Access to Your Records

The Medic8 app stores your most recent health records on your phone so you can view them even when you have no internet connection. The records sync automatically the next time your phone connects to the internet.

To reduce data usage:

1. Go to **Settings > Data**.
2. Enable **Data-Lite Mode**. This compresses all data and avoids downloading images over mobile data.
3. Large files (such as radiology images) download only on WiFi.

---

## 11 Troubleshooting

This section helps you solve common problems.

### 11.1 "I Cannot Log In"

- **Forgotten password:** Click **Forgot Password** on the login screen. Enter your email address. A password reset link is sent to your email. Click the link and set a new password.
- **Two-step verification (MFA) code not working:** Make sure your phone's clock is set to automatic time. If the code still fails, contact your Facility Administrator to reset your MFA.
- **Account locked:** After 5 failed login attempts, your account is locked for 15 minutes. Wait and try again, or contact your Facility Administrator to unlock your account.

### 11.2 "The System is Offline"

Medic8 is designed to continue working when the internet goes down. In offline mode:

- **What still works:** Patient registration, OPD consultation, prescribing, dispensing, and lab result entry continue at full capacity.
- **What is paused:** SMS/WhatsApp reminders, mobile money payment verification, insurance membership verification, and DHIS2 report submission are paused until the internet returns.
- **What happens when the internet returns:** The system detects connectivity and immediately syncs all data entered during the offline period. No data is lost.
- If two staff members edited the same patient record while offline, the system merges changes by field. For non-clinical fields (address, phone number), the most recent change is kept. For clinical fields (diagnoses, prescriptions, allergies), both versions are saved side by side and a clinician is asked to review the conflict.

### 11.3 "I See the Wrong Patient's Data"

**This is a security incident. Act immediately:**

1. Do not make any changes to the record.
2. Note the patient name and MRN displayed on your screen.
3. Log out immediately.
4. Report the incident to your Facility Administrator at once.
5. The Facility Administrator will investigate using the audit trail and contact the Medic8 support team.

### 11.4 "A Drug Interaction Alert is Blocking My Prescription"

- **Tier 3 (Serious) alert:** You can override this alert, but you must enter a written reason explaining why you choose to proceed. Click **Override**, type your reason, and click **Confirm**. Your name, the time, and your reason are permanently recorded.
- **Tier 4 (Fatal) alert:** You cannot override this alert. Contact the pharmacist. The pharmacist must review the interaction and resolve it before the prescription can be accepted. This is a safety measure to protect the patient.

### 11.5 "My Cashier Reconciliation Does Not Balance"

Common causes and how to fix them:

- **You forgot to record a payment:** Check if any patients paid but the payment was not entered in the system. Enter the missing payment.
- **Incorrect change given:** If you gave a patient too much or too little change, the cash in hand will not match the expected total. Note the discrepancy and report it to your supervisor.
- **Unmatched mobile money payment:** A payment came in via MTN MoMo or Airtel Money but was not matched to a patient. Open the **Unmatched Payments** report, find the payment, and match it to the correct patient.
- **Double entry:** Check if the same payment was recorded twice. If so, void one of the entries (supervisor approval required).
- If the discrepancy is less than UGX 5,000, the system accepts the reconciliation. If it exceeds UGX 5,000, the system flags it for supervisor review and you must provide an explanation before the reconciliation is accepted.
