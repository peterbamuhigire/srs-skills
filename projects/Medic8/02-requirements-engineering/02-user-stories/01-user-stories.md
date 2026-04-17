# User Stories: Medic8 Healthcare Management System

Document ID: Medic8-US-001
Version: 1.0
Date: 2026-04-03
Standard: IEEE 29148-2018, INVEST criteria
Acceptance Criteria Format: Gherkin (Given/When/Then)
Estimation Scale: Modified Fibonacci (1, 2, 3, 5, 8, 13)

---

## Phase 1 Epics (Full Detail)

---

## Epic: Authentication (US-AUTH)

### US-AUTH-001: Web Login

As a Facility Admin
I want to log in to Medic8 via a web browser using my email and password
So that I can access the modules assigned to my role securely

Acceptance Criteria:

- [ ] Given a registered user with valid credentials, When they enter their email and password and click **Login**, Then the system authenticates the user and redirects to the role-specific dashboard within 2 seconds
- [ ] Given a user entering an incorrect password, When they click **Login**, Then the system displays "Invalid email or password" without revealing which field is wrong
- [ ] Given a user who fails login 5 consecutive times, When they attempt a 6th login, Then the account is locked for 15 minutes and an email notification is sent to the Facility Admin
- [ ] Given a locked account, When the lockout period expires, Then the user can attempt login again

Story Points: 5
Priority: Critical
Epic: Authentication
Phase: 1

---

### US-AUTH-002: Mobile JWT Login

As a Doctor
I want to log in to the Medic8 mobile app using JWT-based authentication
So that I can access clinical workflows on my phone with a stateless, secure token

Acceptance Criteria:

- [ ] Given a registered user with valid credentials, When they submit email and password via the mobile app, Then the API returns an access token (short-lived) and a refresh token (long-lived)
- [ ] Given a valid access token, When the mobile app makes an API request, Then the server accepts the request and returns the appropriate response within 500 ms at P95
- [ ] Given an expired access token, When the mobile app makes an API request, Then the server returns HTTP 401 and the app automatically attempts a token refresh (US-AUTH-003)
- [ ] Given invalid credentials, When the user attempts login, Then the API returns HTTP 401 with a generic error message

Story Points: 5
Priority: Critical
Epic: Authentication
Phase: 1

---

### US-AUTH-003: Token Refresh

As a Doctor
I want to have my authentication token refreshed automatically before it expires
So that I am not logged out during an active clinical session

Acceptance Criteria:

- [ ] Given a valid refresh token, When the access token expires, Then the app silently obtains a new access token without user interaction
- [ ] Given an expired refresh token, When the app attempts a token refresh, Then the user is redirected to the login screen with a message "Session expired, please log in again"
- [ ] Given a refresh token that has been revoked (e.g., after password change), When the app attempts a token refresh, Then the request fails with HTTP 401 and the user must re-authenticate

Story Points: 3
Priority: Critical
Epic: Authentication
Phase: 1

---

### US-AUTH-004: Logout

As a Nurse
I want to log out of Medic8 explicitly
So that no unauthorised person can access patient data from my workstation

Acceptance Criteria:

- [ ] Given an authenticated user, When they click **Logout**, Then the session is invalidated server-side and the user is redirected to the login screen
- [ ] Given a mobile app user, When they tap **Logout**, Then the access and refresh tokens are revoked and purged from local storage
- [ ] Given a logged-out user, When they press the browser back button, Then no authenticated content is displayed (cache-control headers prevent this)

Story Points: 2
Priority: Critical
Epic: Authentication
Phase: 1

---

### US-AUTH-005: Session Timeout (15 Minutes)

As a Facility Admin
I want to sessions to expire automatically after 15 minutes of inactivity
So that unattended workstations do not expose patient data (PDPA 2019 Section 24)

Acceptance Criteria:

- [ ] Given an authenticated user with no interaction for 14 minutes, When the 14th minute is reached, Then a 60-second countdown warning modal is displayed
- [ ] Given the warning modal is displayed, When the user clicks **Continue Session**, Then the session timer resets to 15 minutes
- [ ] Given the warning modal is displayed, When the 60-second countdown reaches zero without user interaction, Then the session is invalidated and the user is redirected to the login screen
- [ ] Given a user entering clinical data, When auto-save fires (per BR-DATA-005), Then any unsaved form data is preserved in local storage before the session expires

Story Points: 3
Priority: Critical
Epic: Authentication
Phase: 1

---

### US-AUTH-006: Multi-Factor Authentication (MFA) for Admin Roles

As a Super Admin
I want to be required to complete MFA during login
So that privileged accounts are protected against credential compromise

Acceptance Criteria:

- [ ] Given a user with the Super Admin, Facility Admin, Accountant, or Auditor role, When they successfully enter email and password, Then the system prompts for a 6-digit TOTP code before granting access
- [ ] Given an MFA-enabled user, When they enter a valid TOTP code within its 30-second validity window, Then authentication succeeds and the user is redirected to their dashboard
- [ ] Given an MFA-enabled user, When they enter an incorrect TOTP code 3 times, Then the login attempt is blocked and the Facility Admin is notified
- [ ] Given a new admin user, When their account is created, Then the system enforces MFA setup before first login is permitted

Story Points: 5
Priority: High
Epic: Authentication
Phase: 1

---

## Epic: Patient Registration (US-REG)

### US-REG-001: Register New Patient with Demographics and Photo

As a Receptionist
I want to register a new patient with their demographics, contact information, next-of-kin, and photo
So that the patient has a complete record for all subsequent clinical encounters

Acceptance Criteria:

- [ ] Given the Receptionist opens the registration form, When they enter the mandatory fields (name, sex, date of birth or estimated age, and at least one contact method per BR-DATA-006), Then the **Save** button becomes active
- [ ] Given the Receptionist captures a photo via webcam or uploads a file, When the photo is saved, Then it is displayed on the patient profile and stored compressed (max 512 KB)
- [ ] Given the Receptionist enters next-of-kin details (name, relationship, phone), When the record is saved, Then next-of-kin information is linked to the patient record
- [ ] Given a registration is submitted, When the system saves, Then an MRN is auto-generated (US-REG-002) and the patient is ready for triage assignment

Story Points: 5
Priority: Critical
Epic: Patient Registration
Phase: 1

---

### US-REG-002: Auto-Generate Unique MRN

As a Receptionist
I want to the system to automatically generate a unique Medical Record Number (MRN) for every new patient
So that every patient has a machine-readable, facility-unique identifier without manual entry errors

Acceptance Criteria:

- [ ] Given a new patient record is saved, When the record is committed, Then the system assigns a unique MRN in the facility's configured format (e.g., `MED-2026-00001`)
- [ ] Given two patients are registered simultaneously by different receptionists, When both records are saved, Then each receives a unique MRN with no collision
- [ ] Given a facility has configured a custom MRN format, When a patient is registered, Then the MRN follows the configured prefix, year, and sequence pattern

Story Points: 3
Priority: Critical
Epic: Patient Registration
Phase: 1

---

### US-REG-003: Look Up Returning Patient

As a Receptionist
I want to search for an existing patient by name, phone number, NIN, or fingerprint
So that returning patients are identified quickly without creating duplicate records

Acceptance Criteria:

- [ ] Given the Receptionist enters a search term (name, phone, NIN, MRN, passport, UNHCR ID, or NHIS number), When they press **Search**, Then the system returns matching patients ranked by relevance within 1 second
- [ ] Given the search term is a partial name, When results are returned, Then fuzzy matching (Soundex/Metaphone per BR-PID-001) accounts for spelling variations and compound surnames
- [ ] Given a fingerprint scanner is connected, When the Receptionist scans a patient's fingerprint, Then the system matches against stored biometric data and returns the matching record
- [ ] Given multiple matches are found, When the Receptionist selects one, Then the patient's existing record opens for the current visit

Story Points: 5
Priority: Critical
Epic: Patient Registration
Phase: 1

---

### US-REG-004: Assign Patient Category

As a Receptionist
I want to assign a category to each patient (adult, paediatric, staff, VIP, indigent/sponsored, refugee)
So that billing rules, clinical protocols, and reporting segments apply correctly

Acceptance Criteria:

- [ ] Given the registration form is open, When the Receptionist selects a patient category from the dropdown, Then the category is stored on the patient record
- [ ] Given a patient is categorised as "paediatric" (under 12 years per BR-CLIN-006), When a prescription is written, Then weight-based dosing safeguards are enforced
- [ ] Given a patient is categorised as "indigent/sponsored," When the visit is completed, Then the charity write-off workflow (BR-HOPE-002) is available at billing
- [ ] Given a patient is categorised as "refugee," When the record is saved, Then the UNHCR ID field is promoted as a required identifier

Story Points: 3
Priority: High
Epic: Patient Registration
Phase: 1

---

### US-REG-005: Add Multiple Identifiers

As a Receptionist
I want to store multiple identifiers for a patient (NIN, passport, UNHCR ID, NHIS number, phone numbers)
So that the patient can be looked up using any of their official identifiers (BR-PID-004)

Acceptance Criteria:

- [ ] Given the patient profile is open, When the Receptionist adds an identifier type and value, Then the identifier is stored and indexed for search
- [ ] Given a patient has 3 different identifiers, When any of those identifiers is used in a search (US-REG-003), Then the patient record is returned
- [ ] Given the Receptionist enters a NIN that already belongs to another patient, When they attempt to save, Then the system warns of a potential duplicate and requires confirmation

Story Points: 3
Priority: High
Epic: Patient Registration
Phase: 1

---

### US-REG-006: Link Guardian for Paediatric Patient

As a Receptionist
I want to link a guardian (parent or legal carer) to a paediatric patient's record
So that consent, contact, and billing are directed to the responsible adult

Acceptance Criteria:

- [ ] Given a patient under 12 years is being registered, When the Receptionist enters guardian details (name, relationship, phone, NIN), Then the guardian is linked to the patient record
- [ ] Given the guardian is already registered as a patient, When the Receptionist searches and selects the guardian, Then the records are linked bidirectionally
- [ ] Given a paediatric patient has no guardian linked, When registration is attempted, Then the system displays a mandatory warning requiring guardian information before saving

Story Points: 3
Priority: High
Epic: Patient Registration
Phase: 1

---

### US-REG-007: Record Allergies and Chronic Conditions

As a Receptionist
I want to record known allergies and chronic conditions during registration
So that clinicians are alerted to critical safety information before prescribing or treating

Acceptance Criteria:

- [ ] Given the registration form is open, When the Receptionist enters an allergy (drug, food, or environmental) with severity, Then the allergy is stored and flagged on the patient banner
- [ ] Given a patient has recorded allergies, When a Doctor opens the consultation screen, Then allergies are displayed prominently in a red-highlighted banner
- [ ] Given the Receptionist records a chronic condition, When the condition is saved, Then it appears in the patient's problem list for all subsequent encounters
- [ ] Given no allergies are known, When the Receptionist confirms "No Known Allergies," Then NKDA is recorded on the patient banner

Story Points: 3
Priority: High
Epic: Patient Registration
Phase: 1

---

### US-REG-008: Merge Duplicate Patient Records

As a Records Officer
I want to merge two duplicate patient records into a single surviving record
So that all clinical history, billing, and encounters are consolidated under one identity (BR-PID-003)

Acceptance Criteria:

- [ ] Given a Records Officer identifies two duplicate records, When they initiate a merge selecting the surviving record, Then all clinical encounters, billing records, and identifiers from the source record are transferred to the surviving record
- [ ] Given a merge is performed, When the merge completes, Then a full audit trail records the merge action, performing user, source records, and surviving record
- [ ] Given a merge was performed within the last 30 days, When the Records Officer initiates an unmerge, Then the records are separated and restored to their pre-merge state
- [ ] Given a user without the Records Officer or Facility Admin role, When they attempt a merge, Then the system denies the action with "Insufficient permissions"

Story Points: 8
Priority: High
Epic: Patient Registration
Phase: 1

---

### US-REG-009: Detect Potential Duplicate at Registration (EMPI)

As a Receptionist
I want to be warned of potential duplicate patients during registration
So that duplicate records are prevented at the point of entry (BR-PID-002)

Acceptance Criteria:

- [ ] Given the Receptionist enters patient demographics, When the name, date of birth, or phone matches an existing record, Then the system displays potential matches with a confidence score
- [ ] Given a match confidence exceeds 80%, When the duplicate warning is displayed, Then it cannot be dismissed without the Receptionist explicitly selecting "Create New Patient" or choosing the existing record
- [ ] Given a match confidence is below 80%, When the warning is displayed, Then the Receptionist may dismiss it and proceed with registration
- [ ] Given fuzzy matching is applied (Soundex/Metaphone per BR-PID-001), When a name with a spelling variation is entered, Then the original record is surfaced as a potential match

Story Points: 8
Priority: High
Epic: Patient Registration
Phase: 1

---

### US-REG-010: Triage Patient and Assign to Queue

As a Nurse
I want to triage a registered patient and assign them to the appropriate doctor's queue based on triage priority
So that patients are seen in order of clinical urgency (BR-CLIN-001)

Acceptance Criteria:

- [ ] Given a patient has been registered, When the Nurse selects a triage level (Emergency, Urgent, Semi-urgent, Non-urgent), Then the patient is placed in the queue at the position corresponding to their triage level
- [ ] Given a patient is triaged as "Emergency," When the assignment is saved, Then the patient jumps to the top of the queue ahead of all non-emergency patients (BR-CLIN-001)
- [ ] Given a patient is triaged as "Urgent," When the assignment is saved, Then the system ensures the patient is seen within 30 minutes
- [ ] Given a patient is triaged as "Non-urgent," When the assignment is saved, Then the patient is placed in queue order behind all higher-priority patients

Story Points: 5
Priority: Critical
Epic: Patient Registration
Phase: 1

---

## Epic: OPD Consultation (US-OPD)

### US-OPD-001: View Doctor's Queue with Triage Priority

As a Doctor
I want to view my real-time patient queue sorted by triage priority and wait time
So that I see the most urgent patients first and monitor queue load

Acceptance Criteria:

- [ ] Given the Doctor opens the OPD queue screen, When patients are in the queue, Then they are listed in order: Emergency first, then Urgent, then Semi-urgent, then Non-urgent, with ties broken by arrival time
- [ ] Given a new patient is triaged and assigned to this Doctor, When the assignment is saved, Then the queue updates in real time without page refresh
- [ ] Given the queue is displayed, When the Doctor views it, Then each entry shows patient name, MRN, triage level, wait time, and patient category
- [ ] Given a patient has waited beyond the threshold for their triage level, When the threshold is exceeded, Then the entry is highlighted with a visual overdue indicator

Story Points: 5
Priority: Critical
Epic: OPD Consultation
Phase: 1

---

### US-OPD-002: Enter Triage Vital Signs

As a Nurse
I want to record a patient's triage vital signs (BP, temperature, pulse, SpO2, weight, height, BMI, MUAC)
So that the clinical team has baseline observations for the consultation and Early Warning Score calculation

Acceptance Criteria:

- [ ] Given the Nurse opens the triage screen for a patient, When they enter BP (systolic/diastolic), temperature, pulse rate, SpO2 percentage, weight (kg), and height (cm), Then all values are saved to the encounter
- [ ] Given weight and height are entered, When the values are saved, Then BMI is auto-calculated and displayed
- [ ] Given the patient is paediatric (under 5 years), When MUAC is entered, Then the system classifies nutritional status (Green/Yellow/Red per WHO guidelines)
- [ ] Given vital signs are entered, When saved, Then NEWS2 score is auto-calculated (US-OPD-015) and displayed alongside the vitals

Story Points: 5
Priority: Critical
Epic: OPD Consultation
Phase: 1

---

### US-OPD-003: Write SOAP Clinical Notes

As a Doctor
I want to write clinical notes using the SOAP format (Subjective, Objective, Assessment, Plan) with both structured and free-text fields
So that the consultation is documented in a standardised, retrievable format

Acceptance Criteria:

- [ ] Given the Doctor opens the consultation screen, When they enter text in each SOAP section, Then the notes are saved with timestamps and the Doctor's identity
- [ ] Given the Objective section, When the Doctor reviews it, Then triage vital signs (US-OPD-002) are pre-populated from the current encounter
- [ ] Given the Assessment section, When the Doctor enters a diagnosis, Then ICD-10 search is available inline (US-OPD-004)
- [ ] Given the Doctor is mid-entry and a power failure occurs, When power is restored, Then auto-saved data (BR-DATA-005) is recovered in the form

Story Points: 5
Priority: Critical
Epic: OPD Consultation
Phase: 1

---

### US-OPD-004: Enter ICD-10 Diagnosis with Search

As a Doctor
I want to select one or more ICD-10 diagnoses from a searchable list
So that all diagnoses are coded to the international standard for reporting and billing (BR-DATA-006)

Acceptance Criteria:

- [ ] Given the Doctor types in the diagnosis field, When they enter 3 or more characters, Then the system displays matching ICD-10 codes with clinical descriptions
- [ ] Given the Doctor selects an ICD-10 code, When it is added, Then the diagnosis appears in the patient's problem list with the code and description
- [ ] Given the Doctor attempts to enter a free-text diagnosis without an ICD-10 code, When they submit, Then the system blocks submission and requires an ICD-10 selection (BR-DATA-006)
- [ ] Given multiple diagnoses are applicable, When the Doctor adds them, Then each is stored with a primary/secondary classification

Story Points: 5
Priority: Critical
Epic: OPD Consultation
Phase: 1

---

### US-OPD-005: Request Lab Investigation with Instant Notification

As a Doctor
I want to request laboratory investigations from the consultation screen and have the lab notified instantly
So that the lab can begin processing without delay

Acceptance Criteria:

- [ ] Given the Doctor opens the investigation request panel, When they select one or more lab tests from the test catalogue, Then a lab request is created linked to the current encounter
- [ ] Given a lab request is submitted, When it is saved, Then the Lab Technician receives an instant notification (in-app and/or push) with the patient name, MRN, and requested tests
- [ ] Given the patient is triaged as "Emergency," When the request is submitted, Then the request is flagged as URGENT in the lab queue (BR-CLIN-001)
- [ ] Given the request includes clinical notes, When the Lab Technician views the request, Then the Doctor's clinical indication is visible

Story Points: 5
Priority: Critical
Epic: OPD Consultation
Phase: 1

---

### US-OPD-006: Request Radiology Investigation

As a Doctor
I want to request a radiology investigation (X-ray, ultrasound, ECG) from the consultation screen
So that imaging studies are ordered electronically and tracked to completion

Acceptance Criteria:

- [ ] Given the Doctor opens the investigation request panel, When they select a radiology modality and body region, Then a radiology request is created linked to the current encounter
- [ ] Given the request is submitted, When it is saved, Then the Radiographer receives a notification with the patient details and requested study
- [ ] Given the request includes clinical indication, When the Radiographer views the request, Then the clinical reason for the study is visible
- [ ] Given the patient is triaged as "Emergency," When the request is submitted, Then the request is flagged as URGENT in the radiology worklist

Story Points: 3
Priority: High
Epic: OPD Consultation
Phase: 1

---

### US-OPD-007: Write Prescription

As a Doctor
I want to write a prescription specifying the drug (generic and brand), dose, frequency, duration, route, and quantity
So that the pharmacy can dispense the correct medication safely

Acceptance Criteria:

- [ ] Given the Doctor opens the prescription panel, When they search for a drug, Then the system returns matching drugs from the facility formulary with generic and brand names
- [ ] Given the Doctor selects a drug, When they enter dose, frequency, duration, and route, Then the total quantity is auto-calculated
- [ ] Given the prescription is for a paediatric patient (under 12 years), When the Doctor enters the drug, Then the system calculates the weight-based dose from the patient's recorded weight (BR-CLIN-006)
- [ ] Given the calculated paediatric dose exceeds 10x the expected dose, When the Doctor submits, Then the system flags a potential decimal error (BR-CLIN-006)
- [ ] Given the patient has no weight recorded within 24 hours, When the Doctor attempts to prescribe, Then the system blocks submission until weight is entered (BR-CLIN-006)

Story Points: 8
Priority: Critical
Epic: OPD Consultation
Phase: 1

---

### US-OPD-008: View Pharmacy Stock Availability During Prescribing

As a Doctor
I want to see the current pharmacy stock level for each drug while writing a prescription
So that I can prescribe available medications or choose alternatives if a drug is out of stock (BR-RX-002)

Acceptance Criteria:

- [ ] Given the Doctor is on the prescription screen, When a drug is selected, Then the current stock quantity in the pharmacy is displayed alongside the drug name
- [ ] Given the stock for the selected drug is zero, When the Doctor views it, Then a warning is displayed and available therapeutic alternatives from the same drug class are suggested
- [ ] Given the Doctor prescribes a drug with stock below the prescribed quantity, When the prescription is saved, Then a low-stock warning is shown but the prescription is accepted

Story Points: 3
Priority: High
Epic: OPD Consultation
Phase: 1

---

### US-OPD-009: Receive Drug Interaction Alert (Four Tiers)

As a Doctor
I want to receive a drug interaction alert when I prescribe a medication that interacts with the patient's current medications
So that I can prevent adverse drug events (BR-CLIN-004)

Acceptance Criteria:

- [ ] Given the Doctor adds a drug to the prescription, When a Tier 1 (Info) interaction exists, Then an informational note is displayed passively in the sidebar
- [ ] Given a Tier 2 (Warning) interaction exists, When the Doctor adds the drug, Then an amber banner is displayed prominently; the Doctor may proceed without override
- [ ] Given a Tier 3 (Serious) interaction exists, When the Doctor adds the drug, Then a modal alert blocks the workflow; the Doctor must enter a documented override reason to proceed
- [ ] Given a Tier 4 (Fatal) interaction exists, When the Doctor adds the drug, Then a hard stop prevents the prescription from being saved; a Pharmacist must intervene to resolve the interaction
- [ ] Given a Tier 3 or Tier 4 override occurs, When the Doctor proceeds, Then the override is logged with clinician ID, timestamp, and documented reason

Story Points: 8
Priority: Critical
Epic: OPD Consultation
Phase: 1

---

### US-OPD-010: Override Drug Interaction Alert with Documented Reason

As a Doctor
I want to override a Tier 3 (Serious) drug interaction alert by providing a clinical reason
So that patient treatment is not blocked when the benefit outweighs the risk and the decision is auditable

Acceptance Criteria:

- [ ] Given a Tier 3 interaction modal is displayed, When the Doctor enters a clinical justification (minimum 20 characters), Then the override is accepted and the prescription proceeds
- [ ] Given a Tier 3 override is accepted, When the prescription is saved, Then the override reason, clinician ID, and timestamp are recorded in the audit trail
- [ ] Given the Doctor attempts to override without entering a reason, When they click **Proceed**, Then the button remains disabled and a validation message is shown
- [ ] Given a Tier 4 (Fatal) interaction, When the Doctor attempts override, Then the system does not permit override; only a Pharmacist intervention can resolve it

Story Points: 3
Priority: High
Epic: OPD Consultation
Phase: 1

---

### US-OPD-011: Record OPD Procedure

As a Doctor
I want to record a minor procedure performed during an OPD consultation
So that the procedure is documented clinically and a charge is posted to the patient's account

Acceptance Criteria:

- [ ] Given the Doctor opens the procedure panel, When they select a procedure from the catalogue and enter notes, Then the procedure is recorded against the current encounter
- [ ] Given the procedure has a corresponding price list entry, When the procedure is saved, Then a billing charge is auto-posted to the patient's account (BR-FIN-001)
- [ ] Given the procedure is saved, When the encounter summary is viewed, Then the procedure appears in the clinical timeline

Story Points: 3
Priority: High
Epic: OPD Consultation
Phase: 1

---

### US-OPD-012: Generate Referral Letter

As a Doctor
I want to generate a referral letter (internal or external) from the consultation screen
So that the receiving clinician or facility has a structured summary of the patient's clinical information

Acceptance Criteria:

- [ ] Given the Doctor opens the referral panel, When they select the referral type (internal department or external facility), Then a referral form opens pre-populated with patient demographics, current diagnosis, and clinical notes
- [ ] Given the Doctor completes the referral, When they click **Generate**, Then a formatted referral letter is created and available for print or electronic transmission
- [ ] Given an internal referral, When the referral is saved, Then the receiving department/doctor is notified and the patient appears in their queue

Story Points: 5
Priority: High
Epic: OPD Consultation
Phase: 1

---

### US-OPD-013: Book Follow-Up Appointment from Consultation

As a Doctor
I want to book a follow-up appointment for the patient directly from the consultation screen
So that continuity of care is ensured without the patient visiting the front desk

Acceptance Criteria:

- [ ] Given the Doctor opens the follow-up panel, When they select a date, time, and reason, Then an appointment is booked and linked to the current encounter
- [ ] Given the appointment is booked, When the patient has a phone number on file, Then an SMS confirmation is sent (if SMS integration is active)
- [ ] Given the Doctor selects a date, When the selected slot is unavailable, Then the system shows the next 3 available slots for the same doctor

Story Points: 3
Priority: Medium
Epic: OPD Consultation
Phase: 1

---

### US-OPD-014: View Patient's Complete Visit History

As a Doctor
I want to view a patient's complete visit history on a single screen
So that I have full clinical context before making treatment decisions

Acceptance Criteria:

- [ ] Given the Doctor opens a patient's record, When they navigate to the history tab, Then all past encounters are displayed in reverse chronological order
- [ ] Given the history is displayed, When the Doctor clicks on any encounter, Then the full SOAP notes, diagnoses, prescriptions, investigations, and results for that encounter are expanded
- [ ] Given the patient has encounters across multiple facilities, When the Doctor views history (with consent), Then cross-facility encounters are listed with the originating facility name

Story Points: 5
Priority: High
Epic: OPD Consultation
Phase: 1

---

### US-OPD-015: Calculate Early Warning Score from Vitals

As a Nurse
I want to the system to automatically calculate the NEWS2 Early Warning Score when vital signs are entered
So that deteriorating patients are identified early and escalated (BR-CLIN-007)

Acceptance Criteria:

- [ ] Given the Nurse enters vital signs (respiratory rate, SpO2, systolic BP, pulse, consciousness level, temperature), When the values are saved, Then NEWS2 score is auto-calculated and displayed
- [ ] Given the calculated NEWS2 score is 0-4, When displayed, Then the system indicates routine monitoring
- [ ] Given the calculated NEWS2 score is 5-6, When displayed, Then the system triggers a notification to the responsible Doctor and recommends increased monitoring frequency
- [ ] Given the calculated NEWS2 score is 7 or higher, When displayed, Then the system triggers an urgent alert for immediate clinical review and flags the patient for potential ICU transfer

Story Points: 5
Priority: High
Epic: OPD Consultation
Phase: 1

---

### US-OPD-016: Weight-Based Paediatric Dose Calculation

As a Doctor
I want to the system to calculate drug doses based on the patient's weight for paediatric patients
So that dosing is accurate, safe, and capped at the adult maximum (BR-CLIN-006)

Acceptance Criteria:

- [ ] Given the patient is under 12 years and has a recorded weight, When the Doctor selects a drug, Then the system calculates the dose as (mg/kg x weight) and pre-fills the dose field
- [ ] Given the calculated dose exceeds the adult ceiling dose, When the dose is calculated, Then the system caps it at the adult dose and displays a notice
- [ ] Given the calculated dose exceeds 10x the expected dose for the drug, When the calculation completes, Then the system flags a potential decimal error requiring confirmation
- [ ] Given the patient has no weight recorded within 24 hours, When the Doctor initiates a prescription, Then the system blocks the action and prompts for weight entry

Story Points: 5
Priority: Critical
Epic: OPD Consultation
Phase: 1

---

## Epic: Laboratory (US-LAB)

### US-LAB-001: View Pending Lab Requests Queue

As a Lab Technician
I want to view all pending lab requests in a queue sorted by priority and request time
So that I can process samples in order of clinical urgency

Acceptance Criteria:

- [ ] Given the Lab Technician opens the lab queue, When pending requests exist, Then they are displayed sorted by priority (Emergency > Urgent > Routine) then by request time
- [ ] Given a new request arrives, When it is submitted by a Doctor, Then the queue updates in real time
- [ ] Given the queue is displayed, When the Lab Technician views it, Then each entry shows patient name, MRN, requested tests, requesting doctor, request time, and priority flag

Story Points: 3
Priority: Critical
Epic: Laboratory
Phase: 1

---

### US-LAB-002: Collect Sample and Generate Barcode Label

As a Lab Technician
I want to record sample collection and generate a barcode label for each specimen
So that samples are traceable from collection to result entry

Acceptance Criteria:

- [ ] Given the Lab Technician selects a request from the queue, When they record sample collection (specimen type, collection time, collector ID), Then the request status changes to "Collected"
- [ ] Given sample collection is recorded, When the Lab Technician clicks **Print Label**, Then a barcode label is generated containing the patient MRN, specimen type, collection time, and a unique specimen ID
- [ ] Given the label is printed, When it is scanned at any point in the workflow, Then the system retrieves the associated request and patient details

Story Points: 5
Priority: Critical
Epic: Laboratory
Phase: 1

---

### US-LAB-003: Track Specimen Status

As a Lab Technician
I want to track the status of each specimen through the laboratory workflow
So that every sample's location and processing stage is known at all times

Acceptance Criteria:

- [ ] Given a specimen exists, When its status changes, Then the system records the new status with a timestamp: Requested, Collected, Received at Lab, Processing, Result Ready, Validated
- [ ] Given the Doctor queries the status of a pending investigation, When they check from the clinical screen, Then the current specimen status is displayed
- [ ] Given a specimen has been in "Processing" status for more than 4 hours (configurable), When the threshold is exceeded, Then the Lab Supervisor receives an alert

Story Points: 3
Priority: High
Epic: Laboratory
Phase: 1

---

### US-LAB-004: Enter Lab Result with Reference Ranges

As a Lab Technician
I want to enter lab results alongside reference ranges for each test parameter
So that clinicians can interpret results in context

Acceptance Criteria:

- [ ] Given the Lab Technician opens a request in "Processing" status, When they enter the result value for each parameter, Then the result is stored with the test-specific reference range
- [ ] Given the test has numeric results, When the result is entered, Then the system displays the reference range (e.g., "3.5-5.0 mmol/L") alongside the entered value
- [ ] Given results are entered, When the Lab Technician clicks **Submit**, Then the request status changes to "Result Ready" pending validation

Story Points: 5
Priority: Critical
Epic: Laboratory
Phase: 1

---

### US-LAB-005: Auto-Flag Abnormal and Critical Results

As a Lab Technician
I want to the system to automatically flag results that fall outside the reference range
So that abnormal and critical values are immediately visible to clinicians

Acceptance Criteria:

- [ ] Given a result value is entered, When it falls outside the normal reference range, Then the system flags it with "H" (high) or "L" (low) indicators
- [ ] Given a result value exceeds the critical/panic threshold (e.g., potassium > 6.5 mmol/L per BR-CLIN-003), When it is saved, Then the system flags it as "Critical" with a red indicator
- [ ] Given a critical result is flagged, When the flag is applied, Then the critical value escalation workflow (US-LAB-006) is triggered automatically

Story Points: 3
Priority: Critical
Epic: Laboratory
Phase: 1

---

### US-LAB-006: Escalate Critical Value to Requesting Doctor

As a Lab Technician
I want to the system to immediately notify the requesting Doctor when a critical result is recorded
So that the Doctor can take urgent clinical action (BR-CLIN-003)

Acceptance Criteria:

- [ ] Given a critical result is flagged, When the result is saved, Then an immediate notification (in-app, push, and/or SMS) is sent to the requesting Doctor
- [ ] Given the notification is not acknowledged within 30 minutes, When the timeout is reached, Then the system escalates to the Ward Sister/Nurse in charge
- [ ] Given the second notification is not acknowledged within 60 minutes, When the timeout is reached, Then the system escalates to the Facility Admin
- [ ] Given any escalation step occurs, When the notification is sent, Then the escalation is timestamped in the audit trail

Story Points: 5
Priority: Critical
Epic: Laboratory
Phase: 1

---

### US-LAB-007: Validate and Release Result (Supervisor)

As a Lab Technician (Supervisor)
I want to review and validate lab results before they are released to the requesting Doctor
So that only quality-assured results reach the clinical team

Acceptance Criteria:

- [ ] Given a result is in "Result Ready" status, When the Lab Supervisor opens it, Then they can review the entered values, reference ranges, and flags
- [ ] Given the Lab Supervisor approves the result, When they click **Validate**, Then the result status changes to "Validated" and is visible to the requesting Doctor
- [ ] Given the Lab Supervisor rejects the result, When they click **Reject** with a reason, Then the result is returned to the entering Lab Technician for correction
- [ ] Given a result is validated, When the Doctor opens the patient's record, Then the validated result appears in the investigation results section

Story Points: 3
Priority: High
Epic: Laboratory
Phase: 1

---

### US-LAB-008: Enter Quality Control Record

As a Lab Technician
I want to enter quality control (QC) records for each analytical run
So that the laboratory meets internal and external quality assurance standards

Acceptance Criteria:

- [ ] Given the Lab Technician opens the QC module, When they enter QC values (control lot, expected range, observed value, date), Then the record is saved
- [ ] Given the QC value falls outside the acceptable range, When it is saved, Then the system flags the QC failure and recommends re-running the controls before reporting patient results
- [ ] Given QC records are accumulated over time, When the Lab Supervisor views QC trends, Then Levey-Jennings charts are generated for trend analysis

Story Points: 5
Priority: Medium
Epic: Laboratory
Phase: 1

---

### US-LAB-009: Receive Result from HL7-Connected Analyser

As a Lab Technician
I want to receive results automatically from HL7-connected laboratory analysers (Cobas, Mindray, Sysmex)
So that manual transcription is eliminated and result turnaround time is reduced

Acceptance Criteria:

- [ ] Given an analyser is connected via HL7 interface, When a result is produced, Then the system receives the HL7 message and maps it to the corresponding lab request using the specimen barcode
- [ ] Given an auto-received result is mapped, When it is stored, Then it appears in the result entry screen pre-populated with the analyser values
- [ ] Given the auto-received result cannot be matched to a request (barcode mismatch), When it arrives, Then the system queues it as "Unmatched" for manual reconciliation by the Lab Technician

Story Points: 13
Priority: High
Epic: Laboratory
Phase: 1

---

### US-LAB-010: Refer Sample to External Lab (CPHL)

As a Lab Technician
I want to refer a sample to an external laboratory (e.g., CPHL, Lancet) when the test cannot be performed in-house
So that the patient receives specialised testing and results are tracked within Medic8

Acceptance Criteria:

- [ ] Given a test is not available in-house, When the Lab Technician selects "Refer to External Lab," Then a referral record is created with the external lab name, tests requested, and referral date
- [ ] Given a referral is created, When the external lab returns results, Then the Lab Technician enters the results against the original request
- [ ] Given a referred sample is outstanding for more than 7 days (configurable), When the threshold is exceeded, Then the system generates an overdue alert for follow-up

Story Points: 3
Priority: Medium
Epic: Laboratory
Phase: 1

---

## Epic: Pharmacy (US-PHR)

### US-PHR-001: View Prescription Queue

As a Pharmacist
I want to view all pending prescriptions in a queue sorted by priority and time
So that I can dispense medications in order of clinical urgency

Acceptance Criteria:

- [ ] Given the Pharmacist opens the dispensing queue, When pending prescriptions exist, Then they are displayed sorted by priority (Emergency > Urgent > Routine) then by prescription time
- [ ] Given a new prescription is submitted, When it arrives, Then the queue updates in real time
- [ ] Given the queue is displayed, When the Pharmacist views it, Then each entry shows patient name, MRN, prescribing doctor, number of items, and priority flag

Story Points: 3
Priority: Critical
Epic: Pharmacy
Phase: 1

---

### US-PHR-002: Dispense Drug with Stock Deduction

As a Pharmacist
I want to dispense a prescribed drug and have the stock automatically deducted
So that the patient receives their medication and inventory is accurately maintained

Acceptance Criteria:

- [ ] Given the Pharmacist selects a prescription from the queue, When they confirm dispensing for each drug item, Then the dispensed quantity is deducted from pharmacy stock
- [ ] Given the dispensing is confirmed, When the stock deduction occurs, Then the system uses FIFO to deduct from the earliest received batch
- [ ] Given dispensing is complete, When the Pharmacist clicks **Complete**, Then the prescription status changes to "Dispensed" and a billing charge is auto-posted (BR-FIN-001)
- [ ] Given the prescribed quantity exceeds available stock, When the Pharmacist attempts to dispense, Then the system allows partial dispensing (US-PHR-005)

Story Points: 5
Priority: Critical
Epic: Pharmacy
Phase: 1

---

### US-PHR-003: Substitute Generic Equivalent

As a Pharmacist
I want to substitute a prescribed brand-name drug with its generic equivalent when the brand is unavailable
So that the patient receives an effective alternative and the prescribing Doctor is notified (BR-CLIN-002)

Acceptance Criteria:

- [ ] Given a prescribed brand-name drug is out of stock, When the Pharmacist selects "Substitute," Then the system lists available generic equivalents from the same drug class
- [ ] Given the Pharmacist selects a substitute, When the substitution is confirmed, Then the prescribing Doctor is notified of the change
- [ ] Given the substitution is logged, When the dispensing record is viewed, Then both the original prescription and the substituted drug are shown with the substitution reason

Story Points: 3
Priority: High
Epic: Pharmacy
Phase: 1

---

### US-PHR-004: Generate Dispensing Label

As a Pharmacist
I want to generate a dispensing label for each medication dispensed
So that the patient has clear instructions on their medication container

Acceptance Criteria:

- [ ] Given a drug is dispensed, When the Pharmacist clicks **Print Label**, Then a label is generated containing: patient name, drug name, dose, frequency, route, duration, quantity, dispensing date, and facility name
- [ ] Given the label is printed, When applied to the medication container, Then the text is legible at standard reading distance
- [ ] Given the drug is a controlled substance, When the label is generated, Then "CONTROLLED DRUG" is printed prominently on the label

Story Points: 3
Priority: High
Epic: Pharmacy
Phase: 1

---

### US-PHR-005: Partially Dispense with Pending Balance

As a Pharmacist
I want to partially dispense a prescription when full stock is unavailable and track the pending balance
So that the patient receives available medication and can collect the remainder later

Acceptance Criteria:

- [ ] Given a prescribed quantity exceeds stock, When the Pharmacist enters the dispensed quantity (less than prescribed), Then the system records the partial dispensing and calculates the pending balance
- [ ] Given a partial dispensing is recorded, When the prescription is viewed, Then it shows status "Partially Dispensed" with the remaining quantity
- [ ] Given stock is replenished, When the patient returns, Then the Pharmacist can dispense the remaining balance against the original prescription

Story Points: 5
Priority: High
Epic: Pharmacy
Phase: 1

---

### US-PHR-006: Record Narcotic Dispensing in Controlled Drug Register

As a Pharmacist
I want to record every dispensing event for controlled substances in a digital narcotic register
So that Schedule I-V drug dispensing is compliant with regulatory requirements (BR-RX-001)

Acceptance Criteria:

- [ ] Given a controlled substance is dispensed, When the Pharmacist confirms dispensing, Then a register entry is created: patient name, drug name/strength, quantity dispensed, prescribing doctor, dispensing pharmacist, and witness
- [ ] Given the register entry is saved, When the running balance is updated, Then the system calculates the new stock balance for that controlled substance
- [ ] Given the physical count differs from the system balance, When the discrepancy is recorded, Then an immediate alert is sent to the Facility Admin
- [ ] Given any register entry is saved, When it is stored, Then it is immutable and cannot be edited or deleted

Story Points: 5
Priority: Critical
Epic: Pharmacy
Phase: 1

---

### US-PHR-007: Receive Stock (GRN)

As a Pharmacist
I want to receive incoming drug stock and record a Goods Received Note (GRN)
So that the pharmacy inventory is updated with the new stock quantities, batch numbers, and expiry dates

Acceptance Criteria:

- [ ] Given a drug delivery arrives, When the Pharmacist creates a GRN, Then they enter: supplier, delivery note number, and for each item: drug name, batch number, expiry date, quantity, and unit cost
- [ ] Given the GRN is saved, When it is committed, Then stock levels are incremented by the received quantities
- [ ] Given the GRN is saved, When the stock is updated, Then the system calculates stock valuation using the configured method (FIFO or weighted average)

Story Points: 5
Priority: High
Epic: Pharmacy
Phase: 1

---

### US-PHR-008: Transfer Stock Between Stores

As a Pharmacist
I want to transfer drug stock between stores (e.g., main pharmacy to ward pharmacy)
So that drugs are available where they are needed without creating stock discrepancies

Acceptance Criteria:

- [ ] Given the Pharmacist initiates a transfer, When they select the source store, destination store, and items with quantities, Then a transfer request is created
- [ ] Given the transfer request is created, When the receiving store acknowledges receipt, Then stock is deducted from the source and added to the destination
- [ ] Given a transfer is completed, When the transaction is viewed, Then the full audit trail shows source, destination, items, quantities, and timestamps

Story Points: 5
Priority: High
Epic: Pharmacy
Phase: 1

---

### US-PHR-009: View Expiring Drugs (90-Day Alert)

As a Pharmacist
I want to view a list of drugs expiring within the next 90 days
So that I can prioritise dispensing near-expiry stock and arrange returns or write-offs

Acceptance Criteria:

- [ ] Given the Pharmacist opens the expiry report, When it is generated, Then all drugs with expiry dates within 90 days are listed with drug name, batch number, quantity, and expiry date
- [ ] Given a drug expires within 30 days, When the report is displayed, Then it is highlighted in red
- [ ] Given the daily system check runs, When drugs within the 90-day window are detected, Then an automated alert is sent to the Pharmacist

Story Points: 3
Priority: High
Epic: Pharmacy
Phase: 1

---

### US-PHR-010: Set Minimum Stock Level Alert

As a Pharmacist
I want to configure minimum stock levels for each drug and receive alerts when stock falls below the threshold
So that reorders are triggered before stockouts occur

Acceptance Criteria:

- [ ] Given the Pharmacist opens the formulary management screen, When they set a minimum stock level for a drug, Then the threshold is saved
- [ ] Given a drug's stock drops below its minimum level, When the threshold is crossed, Then the Pharmacist receives an alert (in-app notification and/or email)
- [ ] Given a minimum stock report is generated, When the Pharmacist views it, Then all drugs below their minimum level are listed with current stock, minimum level, and deficit

Story Points: 3
Priority: High
Epic: Pharmacy
Phase: 1

---

### US-PHR-011: Display Tall Man Lettering for LASA Drugs

As a Pharmacist
I want to see Tall Man Lettering applied to look-alike/sound-alike (LASA) drug names in all drug selection interfaces
So that selection errors between similar drug names are reduced (BR-RX-003)

Acceptance Criteria:

- [ ] Given a drug in the LASA list is displayed in any search or selection interface, When the name is rendered, Then differentiating letters are shown in uppercase (e.g., hydrOXYzine vs hydrALAZINE)
- [ ] Given the LASA drug list is maintained by the pharmacy lead, When a new LASA pair is added, Then Tall Man Lettering is applied across all interfaces immediately
- [ ] Given two LASA drugs appear in search results, When the Pharmacist views them, Then the visual differentiation is unambiguous

Story Points: 3
Priority: High
Epic: Pharmacy
Phase: 1

---

### US-PHR-012: Manage Drug Formulary

As a Facility Admin
I want to manage the drug formulary (add, edit, deactivate drugs) for my facility
So that clinicians prescribe from an approved, up-to-date list of medications

Acceptance Criteria:

- [ ] Given the Facility Admin opens the formulary management screen, When they add a new drug, Then they enter: generic name, brand name(s), drug class, strength(s), route(s), and default dose
- [ ] Given an existing drug is edited, When changes are saved, Then the updated information is reflected in all prescribing and dispensing screens
- [ ] Given a drug is deactivated, When a Doctor searches for it in the prescription panel, Then it no longer appears in search results

Story Points: 5
Priority: High
Epic: Pharmacy
Phase: 1

---

## Epic: Billing (US-BIL)

### US-BIL-001: View Patient Account with Accumulated Charges

As a Cashier
I want to view a patient's billing account showing all accumulated charges for the current visit
So that I can collect the correct payment amount

Acceptance Criteria:

- [ ] Given the Cashier searches for a patient, When the account is opened, Then all charges for the current visit are displayed: service description, department, quantity, unit price, and total per line
- [ ] Given charges have been auto-posted from clinical screens (BR-FIN-001), When the account is viewed, Then all auto-posted charges appear without manual entry
- [ ] Given the patient has an outstanding balance from a previous visit, When the account is viewed, Then the prior balance is displayed separately from current charges

Story Points: 5
Priority: Critical
Epic: Billing
Phase: 1

---

### US-BIL-002: Configure Price List per Service

As a Facility Admin
I want to configure the price list for all services, drugs, and procedures
So that billing charges are posted at the correct rates for my facility

Acceptance Criteria:

- [ ] Given the Facility Admin opens the price list management screen, When they add or edit a service entry, Then they set: service name, category, unit price, and applicable patient categories
- [ ] Given different patient categories have different pricing, When a charge is posted, Then the system applies the price corresponding to the patient's category
- [ ] Given a price change is saved, When new charges are posted, Then they use the updated price; previously posted charges remain unchanged

Story Points: 5
Priority: Critical
Epic: Billing
Phase: 1

---

### US-BIL-003: Collect Cash Payment with Change Calculation

As a Cashier
I want to record a cash payment and have the system calculate change due
So that payments are accurately recorded and the patient receives correct change

Acceptance Criteria:

- [ ] Given the patient's bill total is displayed, When the Cashier enters the cash amount tendered, Then the system calculates and displays the change due
- [ ] Given the cash tendered is less than the total, When the Cashier attempts to submit, Then the system warns of underpayment and prompts for confirmation (partial payment or credit)
- [ ] Given the payment is submitted, When it is recorded, Then the patient account balance is reduced by the payment amount and a receipt can be generated (US-BIL-005)

Story Points: 3
Priority: Critical
Epic: Billing
Phase: 1

---

### US-BIL-004: Collect Mobile Money Payment (MoMo/Airtel)

As a Cashier
I want to record and verify a mobile money payment (MTN MoMo or Airtel Money)
So that cashless payments are accepted and reconciled against the patient's account (BR-FIN-003)

Acceptance Criteria:

- [ ] Given the patient pays via mobile money, When the Cashier selects the mobile money payment mode and enters the transaction reference, Then the system verifies the payment via the MoMo/Airtel API
- [ ] Given the API confirms the payment, When verification succeeds, Then the patient account balance is reduced and the payment is recorded with the mobile money reference
- [ ] Given the payment cannot be auto-matched (BR-FIN-003), When verification fails, Then the payment is posted to a suspense account for manual reconciliation within 48 hours
- [ ] Given a daily reconciliation is run, When unmatched payments exist, Then the system generates an unmatched payments report

Story Points: 8
Priority: Critical
Epic: Billing
Phase: 1

---

### US-BIL-005: Generate and Print Receipt

As a Cashier
I want to generate and print a payment receipt
So that the patient has proof of payment and the facility has a billing record

Acceptance Criteria:

- [ ] Given a payment is recorded, When the Cashier clicks **Print Receipt**, Then a receipt is generated containing: facility name, receipt number, patient name, MRN, date, payment mode, amount paid, balance remaining, and cashier name
- [ ] Given the receipt is generated, When it is printed, Then it is formatted for the facility's configured receipt printer (A4, thermal, or A5)
- [ ] Given a receipt is generated, When the receipt number is issued, Then it is unique and sequential within the facility

Story Points: 3
Priority: Critical
Epic: Billing
Phase: 1

---

### US-BIL-006: Perform Daily Cashier Reconciliation

As a Cashier
I want to reconcile my daily collections at the end of each shift
So that discrepancies between expected and actual collections are identified (BR-FIN-004)

Acceptance Criteria:

- [ ] Given the Cashier initiates reconciliation, When the reconciliation form opens, Then it displays: opening float, system-calculated collections by payment mode (cash, MTN MoMo, Airtel Money, card), and expected total
- [ ] Given the Cashier enters the actual cash count and banking amount, When they submit, Then the system calculates the variance between expected and actual
- [ ] Given the variance exceeds UGX 5,000, When the reconciliation is submitted, Then the system flags the session for supervisor review
- [ ] Given the reconciliation is submitted, When it is saved, Then the session is closed and a reconciliation report is available for the Facility Admin

Story Points: 5
Priority: High
Epic: Billing
Phase: 1

---

### US-BIL-007: Detect Missing Charges

As a Facility Admin
I want to receive a daily report identifying clinical encounters with no corresponding billing charge
So that revenue leakage is minimised (BR-FIN-008)

Acceptance Criteria:

- [ ] Given the daily automated report runs, When encounters (OPD visits, lab results, drugs dispensed, procedures) have no matching charge, Then they are flagged in the missing charges report
- [ ] Given the report is generated, When the Billing Clerk views it, Then each entry shows: patient name, MRN, service type, encounter date, and reason for the gap
- [ ] Given a missing charge is identified, When the Billing Clerk adds the charge manually, Then the entry is removed from the next day's report

Story Points: 5
Priority: High
Epic: Billing
Phase: 1

---

### US-BIL-008: Manage Patient Credit

As a Facility Admin
I want to approve and track credit extended to patients (staff, corporate, mission)
So that outstanding debts are managed with proper authorisation and ageing visibility (BR-FIN-005)

Acceptance Criteria:

- [ ] Given a patient requests credit, When the Cashier submits a credit request, Then it is routed to the Facility Admin for approval
- [ ] Given the Facility Admin approves the credit, When the approval is recorded, Then the patient's bill is marked as credit with the approved amount and terms
- [ ] Given credit has been extended, When the monthly ageing report runs, Then credit balances are categorised into 0-30, 31-60, 61-90, and 90+ day buckets (BR-FIN-005)
- [ ] Given an uncollectable debt is identified, When a write-off is requested, Then tiered approval is enforced: under UGX 500,000 by Facility Admin, UGX 500,000 or above by Facility Director (BR-FIN-006)

Story Points: 5
Priority: High
Epic: Billing
Phase: 1

---

## Epic: Appointments (US-APT)

### US-APT-001: Book Appointment

As a Receptionist
I want to book an appointment for a patient with a specific doctor on a specific date and time
So that the patient has a confirmed slot and the doctor's schedule is managed

Acceptance Criteria:

- [ ] Given the Receptionist opens the appointment booking screen, When they select a doctor, date, and time slot, Then the appointment is created and linked to the patient record
- [ ] Given the selected slot is already occupied, When the Receptionist attempts to book, Then the system displays a conflict warning and suggests the next 3 available slots
- [ ] Given the appointment is booked, When it is confirmed, Then a confirmation message is available for the patient (SMS if phone is on file)

Story Points: 5
Priority: High
Epic: Appointments
Phase: 1

---

### US-APT-002: Send SMS Reminder 24 Hours Before

As a Patient
I want to receive an SMS reminder 24 hours before my appointment
So that I am reminded to attend and can reschedule if needed

Acceptance Criteria:

- [ ] Given an appointment is booked and the patient has a phone number on file, When 24 hours remain before the appointment, Then an SMS is sent containing: facility name, doctor name, date, time, and a contact number for rescheduling
- [ ] Given the SMS is sent, When delivery status is available, Then the system records whether the SMS was delivered or failed
- [ ] Given the patient does not have a phone number, When the 24-hour mark is reached, Then no SMS is sent and no error is raised

Story Points: 3
Priority: Medium
Epic: Appointments
Phase: 1

---

### US-APT-003: Set Doctor Availability Calendar

As a Facility Admin
I want to configure each doctor's availability calendar (days, hours, slot duration)
So that appointments can only be booked within the doctor's available times

Acceptance Criteria:

- [ ] Given the Facility Admin opens the availability settings for a doctor, When they set available days, start/end times, and slot duration, Then the configuration is saved
- [ ] Given availability is configured, When the Receptionist attempts to book outside available hours, Then the system blocks the booking and shows available alternatives
- [ ] Given the doctor's schedule changes, When the Facility Admin updates availability, Then future bookings are not affected but new bookings follow the updated schedule

Story Points: 3
Priority: High
Epic: Appointments
Phase: 1

---

### US-APT-004: Convert Arrival to OPD Queue

As a Receptionist
I want to mark a patient as arrived and move them into the OPD queue
So that the patient transitions from the appointment schedule to the doctor's active queue

Acceptance Criteria:

- [ ] Given a patient with a booked appointment arrives, When the Receptionist clicks **Mark Arrived**, Then the patient's appointment status changes to "Arrived" and they are added to the assigned doctor's OPD queue
- [ ] Given the patient is added to the OPD queue, When the Doctor views their queue (US-OPD-001), Then the patient appears at the appropriate triage-priority position
- [ ] Given the patient does not arrive within 30 minutes of the appointment time, When the threshold is exceeded, Then the appointment status changes to "No Show"

Story Points: 3
Priority: High
Epic: Appointments
Phase: 1

---

### US-APT-005: Add Walk-In to Queue

As a Receptionist
I want to add a walk-in patient (no appointment) directly to the OPD queue
So that unscheduled patients are seen without requiring a formal appointment booking

Acceptance Criteria:

- [ ] Given a walk-in patient is registered (or an existing patient is found), When the Receptionist selects "Walk-In" and assigns a doctor, Then the patient is added to the doctor's OPD queue
- [ ] Given the walk-in patient is triaged, When the triage level is set, Then the patient is positioned in the queue according to triage priority (BR-CLIN-001)
- [ ] Given walk-in patients and appointment patients are in the same queue, When the queue is displayed, Then triage priority is the primary sort; arrival time is the tiebreaker

Story Points: 2
Priority: High
Epic: Appointments
Phase: 1

---

## Epic: Access Control (US-RBAC)

### US-RBAC-001: Assign Role to Staff Member

As a Facility Admin
I want to assign one or more roles to a staff member
So that each user has access only to the modules and actions their role permits

Acceptance Criteria:

- [ ] Given the Facility Admin opens the staff management screen, When they select a staff member and assign a role (e.g., Doctor, Nurse, Pharmacist), Then the staff member's permissions are updated to match the role's access scope as defined in stakeholders.md
- [ ] Given a role is assigned, When the staff member logs in, Then they see only the modules and menu items permitted by their role
- [ ] Given a role is removed from a staff member, When the change is saved, Then access to the removed role's modules is revoked immediately

Story Points: 3
Priority: Critical
Epic: Access Control
Phase: 1

---

### US-RBAC-002: Create Custom Role with Specific Permissions

As a Facility Admin
I want to create a custom role with a specific set of module-level and action-level permissions
So that the facility can define roles beyond the 18 built-in roles to match its organisational structure

Acceptance Criteria:

- [ ] Given the Facility Admin opens the role management screen, When they create a new role and select permissions from the permission matrix, Then the custom role is saved
- [ ] Given a custom role is created, When it is assigned to a staff member, Then that staff member's access matches exactly the selected permissions
- [ ] Given a custom role is edited, When permissions are updated, Then all staff members with that role immediately inherit the updated permissions

Story Points: 5
Priority: High
Epic: Access Control
Phase: 1

---

### US-RBAC-003: Restrict HIV/Mental Health Records (ABAC)

As a Facility Admin
I want to restrict access to sensitive records (HIV status, mental health, sexual health) using attribute-based access control
So that these records are visible only to clinicians directly involved in the patient's care

Acceptance Criteria:

- [ ] Given a patient has HIV, mental health, or sexual health records, When a staff member without the appropriate attribute/programme assignment views the patient chart, Then those sensitive sections are hidden
- [ ] Given a Doctor is assigned to the HIV programme, When they view a patient enrolled in the programme, Then HIV records are visible
- [ ] Given a Receptionist views a patient profile, When the patient has HIV records, Then the HIV status field is hidden and no indication of HIV programme enrolment is visible

Story Points: 8
Priority: Critical
Epic: Access Control
Phase: 1

---

### US-RBAC-004: Emergency Access with Break-the-Glass

As a Doctor
I want to access a patient's restricted records in a clinical emergency using a "break-the-glass" mechanism
So that critical clinical information is available when the patient's life is at risk (BR-DATA-002)

Acceptance Criteria:

- [ ] Given a Doctor needs emergency access to restricted records, When they initiate "Break the Glass," Then they must provide patient name and date of birth as two-factor confirmation
- [ ] Given emergency access is granted, When the Doctor views the records, Then only allergies, current medications, blood group, HIV status (if prior consent exists), and the last 3 diagnoses are revealed
- [ ] Given emergency access is used, When the access occurs, Then the access is logged with clinician ID, facility, timestamp, and documented reason in an immutable audit trail
- [ ] Given emergency access is granted, When 24 hours elapse, Then the emergency access expires automatically
- [ ] Given emergency access is used, When the event is logged, Then the patient is notified via SMS

Story Points: 8
Priority: Critical
Epic: Access Control
Phase: 1

---

### US-RBAC-005: View Immutable Audit Trail

As a Facility Admin
I want to view an immutable audit trail of all actions performed on patient data
So that the facility meets PDPA 2019 Section 24 compliance and can investigate any data access incident

Acceptance Criteria:

- [ ] Given the Facility Admin opens the audit trail, When they search by date range, user, or patient, Then all matching CRUD operations are displayed with: user, action, resource, timestamp, and IP address
- [ ] Given an audit entry exists, When any user attempts to modify or delete it, Then the system prevents the action; audit entries are immutable
- [ ] Given the Auditor role accesses the audit trail, When they view it, Then they have read-only access to all audit records for compliance review

Story Points: 5
Priority: Critical
Epic: Access Control
Phase: 1

---

## Phase 2 Epics (Summary Level)

---

## Epic: Inpatient Department (US-IPD)

### US-IPD-001: Admit Patient from OPD or Emergency

As a Doctor
I want to admit a patient to a ward from OPD or the emergency department
So that the patient transitions to inpatient care with a bed assignment and admission record

Story Points: 8
Priority: High
Epic: Inpatient
Phase: 2

---

### US-IPD-002: Manage Ward Beds and Transfers

As a Nurse
I want to view a visual bed map, assign beds, and transfer patients between wards
So that bed occupancy is tracked in real time and patient placement is optimised

Story Points: 8
Priority: High
Epic: Inpatient
Phase: 2

---

### US-IPD-003: Discharge Patient with Summary and Billing Settlement

As a Doctor
I want to discharge a patient with a completed discharge summary, medication reconciliation, and billing settlement
So that discharge documentation is complete per BR-CLIN-009 and the patient's account is settled

Story Points: 8
Priority: High
Epic: Inpatient
Phase: 2

---

## Epic: Maternity (US-MAT)

### US-MAT-001: Register ANC Patient and Record Visits

As a Nurse/Midwife
I want to register a patient for antenatal care, calculate gestational age and EDD, and record ANC visits (ANC1-ANC8+)
So that the pregnancy is tracked from booking to delivery with risk assessment

Story Points: 8
Priority: High
Epic: Maternity
Phase: 2

---

### US-MAT-002: Record Delivery and Newborn Outcome

As a Nurse/Midwife
I want to record the delivery (mode, outcome, birth weight, APGAR) and link the newborn record to the mother
So that maternal and neonatal outcomes are documented for clinical care and HMIS 105 Section 4 reporting

Story Points: 8
Priority: High
Epic: Maternity
Phase: 2

---

### US-MAT-003: Record Postnatal Visits

As a Nurse/Midwife
I want to record postnatal care visits (PNC1-PNC3) for both mother and baby
So that postnatal complications are identified early and care continuity is maintained

Story Points: 5
Priority: High
Epic: Maternity
Phase: 2

---

## Epic: Immunisation (US-IMM)

### US-IMM-001: Administer Vaccine per EPI Schedule

As a Nurse
I want to administer a vaccine from the pre-loaded Uganda EPI schedule and record the administration details (date, vaccine, batch, dose, site)
So that the child's immunisation record is complete and HMIS 105 Section 6 is auto-populated

Story Points: 5
Priority: High
Epic: Immunisation
Phase: 2

---

### US-IMM-002: Alert Missed Vaccines and Send SMS Reminders

As a Nurse
I want to receive alerts for missed vaccines and send SMS reminders to caregivers
So that defaulters are traced and immunisation coverage is maximised

Story Points: 5
Priority: High
Epic: Immunisation
Phase: 2

---

### US-IMM-003: Generate Catch-Up Schedule and Vaccination Certificate

As a Nurse
I want to generate a catch-up immunisation schedule for children with missed doses and print a vaccination certificate
So that children are brought up to date and caregivers have an official record

Story Points: 5
Priority: Medium
Epic: Immunisation
Phase: 2

---

## Epic: Emergency Department (US-EMR)

### US-EMR-001: Rapid Triage with AVPU/GCS

As a Nurse
I want to perform rapid triage using AVPU and GCS scales with minimal required fields for emergency registration
So that patients in critical condition are assessed and queued within 2 minutes

Story Points: 5
Priority: High
Epic: Emergency
Phase: 2

---

### US-EMR-002: Place Emergency Orders with URGENT Flag

As a Doctor
I want to place lab, radiology, and pharmacy orders marked URGENT from the emergency screen
So that emergency orders jump queues across all departments (BR-CLIN-001)

Story Points: 5
Priority: High
Epic: Emergency
Phase: 2

---

### US-EMR-003: Track Emergency Disposition and Time Milestones

As a Facility Admin
I want to track time milestones (arrival, triage, seen by doctor, disposition) for every emergency patient
So that emergency department performance is measurable and auditable

Story Points: 5
Priority: Medium
Epic: Emergency
Phase: 2

---

## Epic: Insurance Management (US-INS)

### US-INS-001: Verify Insurance Member and Check Benefits

As a Insurance Clerk
I want to verify a patient's insurance membership and check their benefit schedule
So that the facility confirms coverage before rendering services

Story Points: 5
Priority: High
Epic: Insurance
Phase: 2

---

### US-INS-002: Generate and Submit Insurance Claim

As a Insurance Clerk
I want to auto-generate an insurance claim from a completed visit/admission and submit it to the insurer
So that the facility receives timely reimbursement (BR-INS-002)

Story Points: 8
Priority: High
Epic: Insurance
Phase: 2

---

### US-INS-003: Track Claim Rejections and Resubmit

As a Insurance Clerk
I want to view rejected claims with rejection reasons, correct errors, and resubmit
So that claim recovery rate is maximised and rejection trends are analysed (BR-INS-003)

Story Points: 5
Priority: High
Epic: Insurance
Phase: 2

---

## Epic: HR and Payroll (US-HR)

### US-HR-001: Maintain Staff Registry with Qualifications and Licence Tracking

As a Facility Admin
I want to maintain a staff directory with qualifications, professional licence numbers, and licence expiry alerts
So that the facility is compliant with UMDPC/UNMC/PHLB licensing requirements

Story Points: 5
Priority: High
Epic: HR/Payroll
Phase: 2

---

### US-HR-002: Process Monthly Payroll with Statutory Deductions

As a Accountant
I want to process monthly payroll with PAYE and NSSF statutory deductions per Uganda law
So that staff are paid accurately and statutory obligations are met

Story Points: 8
Priority: High
Epic: HR/Payroll
Phase: 2

---

### US-HR-003: Manage Duty Roster

As a Facility Admin
I want to create and manage duty rosters for clinical staff
So that shift coverage is planned and visible to all staff

Story Points: 5
Priority: Medium
Epic: HR/Payroll
Phase: 2

---

## Epic: HMIS Reporting (US-HMIS)

### US-HMIS-001: Auto-Populate HMIS 105 and 108 Reports

As a Records Officer
I want to generate HMIS 105 (outpatient) and HMIS 108 (inpatient) monthly reports auto-populated from clinical data
So that manual tallying is eliminated and report accuracy improves (BR-HMIS-001, BR-HMIS-002)

Story Points: 13
Priority: High
Epic: HMIS
Phase: 2

---

### US-HMIS-002: Submit Reports to DHIS2

As a Records Officer
I want to submit validated HMIS reports to the Uganda DHIS2 platform via API or export
So that the facility meets its monthly MoH reporting obligations (BR-HMIS-004)

Story Points: 8
Priority: High
Epic: HMIS
Phase: 2

---

## Epic: Inventory Management (US-INV)

### US-INV-001: Manage Multi-Store Inventory with GRN and Expiry Tracking

As a Store Keeper
I want to manage inventory across multiple stores (main, pharmacy, theatre, ward) with GRN receiving, stock transfers, and expiry management
So that stock levels are accurate and expiring items are identified before wastage

Story Points: 8
Priority: High
Epic: Inventory
Phase: 2

---

### US-INV-002: Generate NMS Order Based on Consumption Data

As a Store Keeper
I want to generate a National Medical Stores (NMS) order based on consumption patterns and current stock levels
So that orders reflect actual demand and minimise stockouts

Story Points: 5
Priority: High
Epic: Inventory
Phase: 2

---

### US-INV-003: Set Minimum/Maximum Stock Levels per Store

As a Store Keeper
I want to configure minimum and maximum stock levels per item per store and receive alerts when thresholds are crossed
So that reorders are triggered proactively and overstocking is avoided

Story Points: 3
Priority: Medium
Epic: Inventory
Phase: 2

---

## Phase 3 Epics (Summary Level)

---

## Epic: HIV/AIDS Programme (US-HIV)

### US-HIV-001: Enrol Patient in HIV Programme and Initiate ART

As a Doctor
I want to enrol a patient in the HIV/AIDS programme with WHO staging, CD4, and ART regimen initiation
So that the patient's treatment is tracked and PEPFAR MER indicators (TX_CURR, TX_NEW) are auto-calculated

Story Points: 13
Priority: High
Epic: HIV/AIDS
Phase: 3

---

### US-HIV-002: Track Viral Load and Adherence

As a Doctor
I want to track viral load results and ARV adherence over time
So that suppression status is monitored and non-adherent patients are flagged for intervention (TX_PVLS)

Story Points: 8
Priority: High
Epic: HIV/AIDS
Phase: 3

---

## Epic: TB Programme (US-TB)

### US-TB-001: Register TB Case and Track Treatment

As a Doctor
I want to register a TB case, record the treatment regimen, and track DOT completion
So that treatment outcomes are recorded and NTLP quarterly reports are generated

Story Points: 8
Priority: High
Epic: TB
Phase: 3

---

### US-TB-002: Conduct Contact Tracing

As a Nurse
I want to record and track TB contact tracing activities for household and close contacts
So that new cases are identified early and prophylaxis is offered where appropriate

Story Points: 5
Priority: Medium
Epic: TB
Phase: 3

---

## Epic: Patient Portal and Mobile App (US-PAT)

### US-PAT-001: View Personal Health Record and Test Results

As a Patient
I want to view my medical records, test results, prescriptions, and upcoming appointments via a mobile app
So that I have access to my health information without visiting the facility

Story Points: 13
Priority: High
Epic: Patient Portal
Phase: 3

---

### US-PAT-002: Pay Bills via Mobile Money from App

As a Patient
I want to pay outstanding bills via MTN MoMo or Airtel Money through the patient app
So that I can settle my account without visiting the facility cashier

Story Points: 8
Priority: Medium
Epic: Patient Portal
Phase: 3

---

## Phase 4 Epics (Summary Level)

---

## Epic: Theatre and Surgical Management (US-SUR)

### US-SUR-001: Book Theatre, Record Operation Notes and Surgical Count

As a Doctor
I want to book a theatre slot, complete a pre-operative checklist, record operation notes with anaesthesia details, and document the surgical count (swabs, instruments, needles)
So that surgical care is fully documented, billed, and auditable per HMIS 108

Story Points: 13
Priority: High
Epic: Theatre/Surgical
Phase: 4

---

## Epic: Blood Bank (US-BLB)

### US-BLB-001: Manage Blood Requests, Cross-Match, and Transfusion Recording

As a Lab Technician
I want to process blood requests, perform cross-matching, issue blood units, and record transfusion outcomes including adverse reactions
So that blood transfusion safety is maintained and haemovigilance data is captured

Story Points: 13
Priority: High
Epic: Blood Bank
Phase: 4

---

## Epic: Director Platform (US-DIR)

### US-DIR-001: View Cross-Facility Analytics Dashboard

As a Facility Director
I want to view a consolidated dashboard with cross-facility analytics (revenue, patient volumes, bed occupancy, clinical indicators)
So that I can make data-driven strategic decisions across all facilities in the group

Story Points: 13
Priority: High
Epic: Director Platform
Phase: 4

---

## Epic: AI Intelligence (US-AI)

### US-AI-001: AI Clinical Note Draft

As a Doctor, I want to request an AI draft of my clinical note after completing a consultation, so that I spend less time on documentation and more time with patients.

Acceptance Criteria:

- [ ] Given a Doctor has completed a consultation, when they click **Draft with AI**, then the AI draft is generated and displayed within 8 s.
- [ ] Given the AI draft is generated, when it is displayed, then it appears in a clearly labelled "AI Draft" panel with **Approve** and **Discard** actions.
- [ ] Given the "AI Draft" panel is displayed, when the Doctor clicks **Approve**, then the draft is saved to the patient record.
- [ ] Given the "AI Draft" panel is displayed, when the Doctor clicks **Discard**, then the draft is removed without any write operation.
- [ ] Given any AI draft event occurs, when the action completes, then an audit log entry records the draft generation, approval or discard, clinician ID, and token count.

Story Points: 8
Priority: High
Epic: AI Intelligence
Phase: 2

---

### US-AI-002: AI ICD Code Suggestions

As a Doctor, I want to see AI-suggested ICD-10/11 codes as I type my clinical note, so that I can code diagnoses accurately without needing a dedicated medical coder.

Acceptance Criteria:

- [ ] Given a Doctor is typing a clinical note, when they enter text in the diagnosis field, then AI suggestions appear as a selectable list alongside the field.
- [ ] Given suggestions are displayed, when the list renders, then the top 3–5 suggestions are shown, each with a confidence score.
- [ ] Given suggestions are displayed, when the Doctor chooses not to use them, then they can dismiss all suggestions and type a manual search query.
- [ ] Given suggestions are displayed, when the Doctor selects a suggestion, then the ICD code is added to the diagnosis list.
- [ ] Given any suggestion interaction occurs, when the Doctor accepts or rejects a suggestion, then the event is logged for acceptance rate reporting.

Story Points: 8
Priority: High
Epic: AI Intelligence
Phase: 2

---

### US-AI-003: AI Differential Diagnosis

As a Doctor, I want to see a ranked differential diagnosis list derived from the patient's symptoms, vitals, and recent labs, so that I can consider alternatives I may not have immediately thought of.

Acceptance Criteria:

- [ ] Given a Doctor is on the consultation screen with a presenting complaint entered, when the AI differential panel loads, then a collapsible panel appears below the presenting complaint field with a ranked differential list.
- [ ] Given the differential list is displayed, when the Doctor views an entry, then it shows: condition name, ICD-11 code, top 3 contributing factors, and rank position.
- [ ] Given the differential panel is displayed, when it renders, then the panel header reads "AI Differential — for clinician review only. Not a diagnosis."
- [ ] Given the differential list is displayed, when the Doctor dismisses an individual suggestion, then the dismissed suggestion is not written to the patient record.
- [ ] Given the differential list is displayed, when the Doctor does not actively select a suggestion as a diagnosis, then no suggestion is written to the patient record.

Story Points: 8
Priority: High
Epic: AI Intelligence
Phase: 2

---

### US-AI-004: AI Patient Plain-Language Summary

As a Patient, I want to receive a plain-language summary of my discharge notes in my preferred language (English, French, or Kiswahili), so that I understand my condition and follow-up instructions without medical jargon.

Acceptance Criteria:

- [ ] Given a clinician approves a patient discharge, when the approval is saved, then the plain-language summary is displayed in the patient portal app within 10 s.
- [ ] Given the summary is displayed, when it renders, then it is rendered in the patient's preferred locale as set in their profile.
- [ ] Given the summary is displayed, when the Doctor reviews it, then it contains no ICD codes, drug abbreviations, or clinical acronyms.
- [ ] Given the summary is displayed, when it renders, then a "This summary was generated by AI and reviewed by your care team" disclosure appears below the summary.

Story Points: 8
Priority: High
Epic: AI Intelligence
Phase: 2

---

### US-AI-005: AI Claim Scrubbing

As an Insurance Liaison, I want the system to flag claim line items with a high rejection probability before I submit the claim, so that I can correct issues before they are rejected by the insurer.

Acceptance Criteria:

- [ ] Given an Insurance Liaison is preparing to submit a claim, when they click **Analyse Claim**, then the system displays a "Claim Risk Analysis" step showing risk indicators per line item within 8 s.
- [ ] Given the risk analysis is displayed, when a high-risk item is present, then it is highlighted in red with the specific rejection reason predicted.
- [ ] Given the risk analysis is displayed, when a medium-risk item is present, then it is highlighted in amber.
- [ ] Given the risk analysis is displayed, when the liaison reviews the warnings, then they can proceed to submit despite warnings with an acknowledgement override.
- [ ] Given the liaison clicks **Analyse Claim**, when the analysis runs, then it completes and results are displayed within 8 s.

Story Points: 8
Priority: High
Epic: AI Intelligence
Phase: 2

---

### US-AI-006: AI Outbreak Early Warning

As a Medical Officer, I want to receive an alert when the system detects an unusual clustering of diagnosis codes at my facility, so that I can investigate a potential outbreak before it crosses the national IDSR threshold.

Acceptance Criteria:

- [ ] Given diagnoses are being recorded at a facility, when the count for a single disease code exceeds 2 standard deviations above the 90-day rolling baseline, then an outbreak alert is generated.
- [ ] Given an outbreak alert is generated, when it is displayed, then it names the disease code, the current count, the baseline, and the deviation.
- [ ] Given an outbreak alert is generated, when the threshold is crossed, then the alert is delivered to the Medical Officer via in-app notification and SMS within 5 min.
- [ ] Given an outbreak alert is delivered, when the Medical Officer reviews it, then they can dismiss it with a reason or escalate it to the District Health Officer.
- [ ] Given outbreak alerts are generated over time, when the AI admin panel is viewed, then the false positive rate is tracked and reported.

Story Points: 13
Priority: High
Epic: AI Intelligence
Phase: 2

---

### US-AI-007: AI Provider Configuration

As an AI Administrator, I want to configure which AI provider is used for each tenant, so that I can optimise for cost, latency, or regulatory compliance.

Acceptance Criteria:

- [ ] Given the AI Administrator opens the AI admin panel, when the provider configuration section loads, then a provider selection dropdown is displayed with options: OpenAI, Anthropic, DeepSeek, Gemini.
- [ ] Given the AI Administrator enters an API key, when it is saved, then the key is stored encrypted and is never displayed in plain text again.
- [ ] Given the primary provider is configured, when the AI Administrator configures the failover provider, then a secondary provider can be set independently from the primary.
- [ ] Given a provider is configured, when the AI Administrator tests the connection, then a health check request is sent and the response status is displayed.
- [ ] Given a provider change is saved, when the change is committed, then it takes effect within 60 s.

Story Points: 5
Priority: High
Epic: AI Intelligence
Phase: 2

---

### US-AI-008: AI Token Usage Dashboard

As an AI Administrator, I want to view real-time token usage and credit balance for my tenant's AI Intelligence module, so that I can top up credits before they are exhausted and avoid service interruptions.

Acceptance Criteria:

- [ ] Given the AI Administrator opens the admin panel, when the usage dashboard loads, then it displays: current credit balance, estimated days remaining at current consumption rate, and a usage breakdown by capability for the current billing period.
- [ ] Given the credit balance falls below the user-set threshold, when the threshold is crossed, then a low-balance alert email is sent to the AI Administrator.
- [ ] Given credits reach zero, when the balance hits zero, then AI features are paused automatically while clinical features remain unaffected.
- [ ] Given the AI Administrator views the usage dashboard, when they need to top up, then a **Top Up Credits** button is displayed and links to the billing portal.

Story Points: 5
Priority: High
Epic: AI Intelligence
Phase: 2

---

## Epic: Internationalisation (US-I18N)

### US-I18N-001: Kiswahili UI for Receptionist

As a Clinic Receptionist, I want to use the Medic8 web portal in Kiswahili, so that I can work more efficiently in my primary language.

Acceptance Criteria:

- [ ] Given a Receptionist is in their profile settings, when they select Kiswahili from the language selector, then the locale is saved to their profile.
- [ ] Given a Receptionist's locale is set to Kiswahili, when they use the registration and OPD modules, then all UI labels, buttons, form fields, and navigation items render in Kiswahili.
- [ ] Given the Receptionist changes their locale, when the change is confirmed, then it takes effect within 500 ms without a full page reload.
- [ ] Given a clinician's preferred locale is `sw`, when a clinical alert is displayed, then the severity labels (Fatal, Serious, Warning, Info) render in Kiswahili.
- [ ] Given a string has an approved Kiswahili translation, when the UI renders in Kiswahili, then no English fallback string is visible for that string.

Story Points: 5
Priority: High
Epic: Internationalisation
Phase: 2

---

### US-I18N-002: French-Language Patient Communications (Amina Hassan Persona)

As a French-speaking DRC patient, I want to receive my appointment reminders and lab results in French, so that I understand my health information without needing a translator.

Acceptance Criteria:

- [ ] Given a patient's preferred locale is set to `fr`, when the patient portal loads, then the portal detects the `fr` locale from their profile and renders content in French.
- [ ] Given a patient's locale is `fr` and an appointment is booked, when the appointment reminder SMS is sent, then it is sent in French.
- [ ] Given a patient's locale is `fr`, when lab result summaries are displayed in the patient portal, then they are displayed in French.
- [ ] Given a patient's locale is `fr`, when the AI plain-language summary of discharge notes is generated, then it is generated in French at an appropriate reading level.

Story Points: 5
Priority: High
Epic: Internationalisation
Phase: 2

---

## Backlog Summary

### Story Counts by Phase

| Phase | Epic Count | Story Count | Total Story Points |
|---|---|---|---|
| Phase 1 | 8 | 67 | 307 |
| Phase 2 | 8 | 22 | 141 |
| Phase 3 | 3 | 6 | 55 |
| Phase 4 | 3 | 3 | 39 |
| Total | 22 | 98 | 542 |

### Phase 1 Breakdown by Epic

| Epic | Stories | Story Points |
|---|---|---|
| Authentication (US-AUTH) | 6 | 23 |
| Patient Registration (US-REG) | 10 | 46 |
| OPD Consultation (US-OPD) | 16 | 77 |
| Laboratory (US-LAB) | 10 | 48 |
| Pharmacy (US-PHR) | 12 | 49 |
| Billing (US-BIL) | 8 | 39 |
| Appointments (US-APT) | 5 | 17 |
| Access Control (US-RBAC) | 5 | 29 |
| Phase 1 Total | 72 | 328 |

### Sprint Recommendations (Phase 1)

Assuming 2-week sprints with a team velocity of approximately 30-40 story points per sprint.

Sprint 1: Authentication and Patient Registration (46 points)

- US-AUTH-001 through US-AUTH-006 (23 points)
- US-REG-001, US-REG-002, US-REG-003, US-REG-004 (16 points)
- US-RBAC-001 (3 points) — needed for all role-based testing
- Stretch: US-REG-005 (3 points)

Sprint 2: Registration Completion and OPD Core (40 points)

- US-REG-005 through US-REG-010 (remaining registration, ~30 points)
- US-OPD-001, US-OPD-002 (10 points) — queue and triage vitals

Sprint 3: OPD Consultation (40 points)

- US-OPD-003 through US-OPD-010 (40 points) — SOAP notes, diagnosis, prescribing, drug interactions

Sprint 4: OPD Completion and Laboratory (37 points)

- US-OPD-011 through US-OPD-016 (26 points) — procedures, referrals, follow-up, history, EWS, paediatric dosing
- US-LAB-001, US-LAB-002 (8 points) — lab queue and sample collection

Sprint 5: Laboratory (40 points)

- US-LAB-003 through US-LAB-010 (40 points) — specimen tracking, results, QC, HL7, external referral

Sprint 6: Pharmacy (49 points)

- US-PHR-001 through US-PHR-012 (49 points) — full pharmacy epic

Sprint 7: Billing (39 points)

- US-BIL-001 through US-BIL-008 (39 points) — full billing epic

Sprint 8: Appointments, Access Control, and Hardening (46 points)

- US-APT-001 through US-APT-005 (17 points)
- US-RBAC-002 through US-RBAC-005 (26 points)
- Integration testing and hardening buffer (3 points)

Estimated Phase 1 Duration: 8 sprints (16 weeks / 4 months), consistent with the 6-month Phase 1 target with buffer for QA, UAT, and pilot deployment.
