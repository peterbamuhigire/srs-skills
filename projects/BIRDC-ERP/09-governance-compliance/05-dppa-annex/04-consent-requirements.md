# Section 4 — Consent Requirements (Sections 7, 8, 13, DPPA 2019)

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

## 4.1 Farmer Registration Consent

### FR-DPPA-001 — Consent Capture Before Data Collection

When a Collections Officer initiates a new farmer registration in the Farmer Delivery App, the system shall display the consent notice (purpose, data categories collected, right of access, right of rectification per Section 13) before any personal data field is enabled for input. The system shall require the Collections Officer to record the farmer's consent acknowledgement before the registration form fields become active. The system shall not save any farmer personal data if consent has not been recorded.

**Stimulus:** Collections Officer opens the "Register New Farmer" screen.
**Response:** System displays consent notice in English and Runyankore/Rukiga before any data entry field is enabled. Data entry fields remain locked until consent is recorded.

### FR-DPPA-002 — Consent Record Storage

When farmer consent is recorded, the system shall persist a consent record to `tbl_consent_register` with the following fields:

| Column | Value |
|---|---|
| `data_subject_id` | Farmer ID (assigned at consent step) |
| `data_subject_type` | `'farmer'` |
| `purpose` | "Cooperative farmer registration, delivery recording, and payment disbursement — BIRDC/PIBID cooperative procurement" |
| `legal_basis` | `'consent'` |
| `data_categories` | JSON: `["name","NIN","contact_phone","GPS_coordinates","photograph","mobile_money_number"]` |
| `consent_given_at` | UTC timestamp |
| `consent_given_by` | User ID of Collections Officer |

### FR-DPPA-003 — Consent Withdrawal Mechanism

When a farmer requests withdrawal of consent (in person at cooperative collection point or in writing to BIRDC), the IT Administrator shall be able to record the withdrawal in the system. The system shall set `consent_withdrawn_at` and `withdrawal_method` on the consent record. The system shall flag the farmer record as "consent withdrawn — processing restricted" and prevent any new data collection for that farmer. The system shall retain existing financial records for the legally required 7-year period under the Income Tax Act notwithstanding withdrawal (financial records are also covered by legal obligation basis).

**Stimulus:** IT Administrator selects "Record Consent Withdrawal" for a farmer record.
**Response:** System records withdrawal timestamp and method; marks farmer profile as restricted; prevents new data entry; displays retention notice: "Financial payment records retained for 7 years per Income Tax Act Cap 340."

---

## 4.2 Children's Data Safeguard (Section 8, DPPA 2019)

### FR-DPPA-004 — Age Verification at Farmer Registration

When a Collections Officer enters a farmer's date of birth during registration, the system shall calculate the farmer's age. If age is under 18, the system shall display an alert: "This farmer is under 18 years of age. Under Section 8, DPPA 2019, consent from a parent or guardian is required before collecting this farmer's personal data."

**Stimulus:** Collections Officer enters date of birth resulting in calculated age < 18 years.
**Response:** System displays Section 8 guardian consent alert. The system shall require the Collections Officer to record the guardian's name, relationship to farmer, and confirmation of consent before proceeding. The guardian consent is recorded as a separate consent record linked to the farmer.

### FR-DPPA-005 — Guardian Consent Record

When a farmer under 18 is registered, the system shall create a linked guardian consent record in `tbl_consent_register` with `data_subject_type = 'farmer_guardian'` and record guardian name, relationship, and consent timestamp.

---

## 4.3 Employee Registration Consent

### FR-DPPA-006 — Employee Photograph Consent

When HR creates a new employee profile and uploads an employee photograph, the system shall require confirmation that explicit photograph consent has been obtained. The system shall not save the photograph if consent confirmation is not checked.

**Stimulus:** HR records an employee photograph during onboarding.
**Response:** System displays consent confirmation checkbox: "I confirm that [Employee Name] has given explicit written consent for their photograph to be collected and stored for identity verification purposes." System blocks photograph save unless checkbox is checked.

### FR-DPPA-007 — Biometric Attendance Consent (ZKTeco)

When HR activates biometric attendance for an employee in the ZKTeco device, the system shall require recording of explicit biometric consent. The biometric template is stored on the ZKTeco device only and is never transmitted to or stored in the application database. The system shall record: employee ID, consent to biometric attendance collection, timestamp, and the confirming HR user ID.

**Stimulus:** HR user activates an employee for ZKTeco biometric attendance.
**Response:** System requires biometric consent confirmation before the activation is saved. System stores consent record. System displays notice: "Biometric template stored on ZKTeco device only. Not stored in application database."

---

## 4.4 Notice at Collection (Section 13, DPPA 2019)

### FR-DPPA-008 — Notice at Collection — All Data Subjects

When the system displays any consent notice at data collection (farmer registration, employee onboarding, agent registration), the notice shall include:

1. The purpose for which the data is being collected.
2. The categories of data being collected.
3. The lawful basis for collection.
4. The data subject's right to access their personal data (Section 14).
5. The data subject's right to request rectification or erasure (Section 16).
6. The contact details of the BIRDC Data Protection Officer.
7. The PDPO registration number (once registered).

---

## 4.5 Consent Form Generation

### FR-DPPA-009 — Printable Consent Form

When a Collections Officer completes a farmer registration, the system shall generate a printable consent form in English and Runyankore/Rukiga. The form shall include: farmer name, farmer ID, data categories collected, purpose, DPO contact, and a signature field. The form shall be printable from the Farmer Delivery App via Bluetooth printer connection.

**Stimulus:** Collections Officer completes farmer registration and selects "Print Consent Form."
**Response:** System generates a consent form pre-populated with the registered farmer's data and displays it for Bluetooth printing. Form language defaults to Runyankore/Rukiga with English parallel columns.
