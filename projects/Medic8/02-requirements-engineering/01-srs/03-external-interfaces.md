# 3 External Interfaces

## 3.1 User Interfaces

### 3.1.1 Web Application (Staff-Facing)

The Medic8 web application uses the Bootstrap 5 / Tabler UI framework to deliver a responsive, professional interface for all staff-facing modules.

General UI requirements:

- The system shall render correctly at a minimum viewport resolution of 1024 x 768 pixels.
- The system shall support responsive layout scaling from 1024 px to 2560 px viewport width without horizontal scrolling.
- The system shall use AJAX for all data operations. Full page reloads shall occur only on module navigation, not on data submission or retrieval within a module.
- The system shall use DataTables.js for all tabular data displays, providing sorting, filtering, pagination, and CSV/Excel/PDF export.
- The system shall use SweetAlert2 for all confirmation dialogs, success notifications, error alerts, and destructive action confirmations.
- The system shall use Flatpickr for all date and time input fields, configured per the facility's locale (dd/MM/yyyy for Uganda, MM/dd/yyyy for US-funded facilities).

Clinical UI requirements:

- *Single-Page OPD Summary:* The OPD consultation screen shall display patient demographics, allergy flags, current medications, vital signs, visit history (last 5 encounters), active diagnoses, and the SOAP note entry form on a single scrollable page without tab switching for the core consultation workflow.
- *Four-Tier Alert Display:* Clinical alerts shall be displayed using 4 severity levels with distinct visual treatment, rendered in the clinician's configured UI language (see **CONSTRAINT-I18N-003**):
  - Info — blue banner, auto-dismisses after 5 seconds
  - Warning — amber banner, requires acknowledgement click to dismiss
  - Serious — red modal dialog, requires clinician to select an override reason from a predefined list before proceeding
  - Fatal — red modal dialog with no override option; the action is blocked until the triggering condition is resolved
- *Tall Man Lettering:* Look-Alike/Sound-Alike (LASA) drug names shall be displayed using Tall Man Lettering (e.g., hydrOXYzine vs. hydrALAzine) in all prescription, dispensing, and drug interaction screens per WHO/ISMP conventions.
- *Task Resumption:* If a clinician navigates away from an in-progress consultation, prescription, or order, the system shall preserve the unsaved state and present a "Resume Draft" prompt on return. Auto-save shall fire on every form interaction, not only on explicit save.
- *One-Handed Tablet Mode (Nursing):* The nursing documentation screens (vital signs entry, drug round MAR, fluid balance chart) shall provide a one-handed tablet mode with enlarged touch targets (minimum 48 x 48 dp), bottom-anchored action buttons, and swipe navigation between patients in the ward list.

### 3.1.2 Android Mobile Application

The Medic8 Android application uses Kotlin with Jetpack Compose and Material 3 design guidelines.

- The system shall support Android 7.0 (API level 24) and above on devices with 1 GB RAM minimum.
- The system shall operate in data-lite mode on 2G/3G networks, deferring image downloads to WiFi by default.
- The system shall store the last synced data set in Room database for offline access.
- The system shall support biometric authentication (fingerprint, face recognition) as an optional login gate alongside PIN/password.
- The system shall use Retrofit for all API communication with automatic retry on transient network failures.
- Navigation shall follow single-activity architecture with Compose Navigation.

### 3.1.3 iOS Mobile Application

The Medic8 iOS application uses Swift with SwiftUI and follows Apple Human Interface Guidelines.

- The system shall support iOS 15.0 and above.
- The system shall store the last synced data set in Core Data / SwiftData for offline access.
- The system shall support Face ID and Touch ID as an optional biometric login gate.
- The system shall use async/await for all asynchronous operations.

### 3.1.4 Patient Portal

The patient portal shall be accessible via web browser (responsive, mobile-optimised) and the Medic8 Android application.

- The portal shall display: personal health record (visits, diagnoses, treatments, investigations), test results, upcoming and past appointments, fee balance, payment history, and medication reminders.
- The portal shall support mobile money payment (MTN MoMo, Airtel Money) for outstanding invoices.
- The portal shall support multiple family members under a single login (parent/guardian accessing children's records).
- The portal shall provide a data-lite mode for low-specification devices and 2G/3G networks.
- The portal shall support USSD/SMS fallback for appointment confirmation and basic result notification on feature phones.
- The portal shall render in the patient's configured locale (en, fr, sw); the locale is set in the patient's profile and persists across sessions.

---

## 3.2 Software Interfaces

The following table defines all external software systems with which Medic8 exchanges data.

| System | Protocol | Direction | Purpose | Phase |
|---|---|---|---|---|
| DHIS2 (Uganda MoH) | REST API (ADX/JSON) | Outbound | HMIS aggregate report submission (105, 108, 033b). Organisation unit mapping per facility. | 2 |
| MTN Mobile Money | REST API (MTN MoMo Open API) | Bidirectional | Patient payment collection, payment verification via callback, refund processing. | 1 |
| Airtel Money | REST API (Airtel Money API) | Bidirectional | Patient payment collection, payment verification via callback, refund processing. | 1 |
| Africa's Talking | REST API | Outbound | SMS delivery (appointment reminders, medication alerts, missed appointment follow-ups), USSD session handling (patient lookup, appointment booking on feature phones). | 1 |
| HL7 FHIR R4 | RESTful API (JSON) | Bidirectional | Interoperability with external EHR systems, third-party clinical applications (via SMART on FHIR), and health information exchanges. 14 resource types exposed: Patient, Encounter, Observation, Condition, MedicationRequest, MedicationDispense, DiagnosticReport, ServiceRequest, Immunization, AllergyIntolerance, Procedure, Location, Practitioner, Organization. | 3 |
| HL7 v2 | MLLP/TCP | Bidirectional | Laboratory analyser interface. ORM messages (outbound orders) and ORU messages (inbound results). | 1 |
| ASTM E1394 | Serial (RS-232) / TCP | Inbound | Legacy laboratory analyser result import for instruments that do not support HL7 v2. | 1 |
| DICOM 3.0 | TCP | Bidirectional | Radiology image management. MWL (outbound scheduling), C-STORE (inbound images), C-FIND/C-MOVE (query/retrieve). | 2 |
| NIRA (Uganda) | REST API | Outbound (query) | National Identification Number (NIN) verification for patient identity confirmation. | 1 |
| NHIS Uganda | REST API (TBD) | Bidirectional | Insurance member verification, pre-authorisation submission, claim submission, rejection notification, reconciliation. API specification is a dependency (see DEP-007). | 2 |
| UBTS (Uganda Blood Transfusion Service) | TBD | TBD | Blood supply availability query, cross-match request, transfusion outcome reporting. Integration specification is a dependency (see DEP-010). | 4 |
| AI Provider APIs | HTTPS REST | Outbound | AI capability request and response (clinical note draft, differential diagnosis, ICD code suggestion, plain-language summary, claim scrub, outbreak alert). Up to 2 providers per tenant (primary + failover). | 2 |

### Software Interface Detail — DHIS2

- Authentication: OAuth2 or Basic Auth per DHIS2 instance configuration.
- Data Format: ADX (Aggregate Data Exchange) XML or JSON payload.
- Frequency: Monthly batch submission aligned with HMIS reporting calendar; on-demand re-submission for corrections.
- Error Handling: The system shall log submission failures, retry 3 times with exponential backoff, and alert the Records Officer if submission fails after all retries.

### Software Interface Detail — Mobile Money (MTN MoMo, Airtel Money)

- Authentication: API key + OAuth2 bearer token.
- Transaction Flow: Medic8 initiates a payment request with amount, payer phone number, and reference ID. The provider sends a callback on payment success or failure. Medic8 reconciles the callback against the pending transaction.
- Idempotency: Each payment request carries a unique reference ID to prevent duplicate charges.
- Timeout: If no callback is received within 120 seconds, the transaction is marked as pending and the cashier is prompted to verify manually.

### Software Interface Detail — HL7 FHIR R4

- Base URL: `https://{tenant-domain}/fhir/r4/`
- Authentication: OAuth2 (SMART on FHIR launch) or API key for server-to-server integration.
- Supported Operations: READ, SEARCH, CREATE, UPDATE on all 14 resource types. DELETE is not supported for clinical resources (soft-delete with status change only).
- Narrative: Every FHIR response shall include an HTML narrative (`text.div`) rendering the resource in human-readable format per FHIR R4 narrative requirements.
- Versioning: Resource versioning via `meta.versionId`. History operation supported per resource.

### Software Interface Detail — HL7 v2 (Laboratory)

- Transport: MLLP (Minimum Lower Layer Protocol) over TCP. Default port configurable per analyser (typically 2575).
- Message Types: ORM^O01 (outbound order), ORU^R01 (inbound result).
- Character Encoding: UTF-8.
- Acknowledgment: ACK message returned for every received ORU. Negative ACK triggers retry with configurable retry count (default 3).

### Software Interface Detail — AI Provider APIs

The AI Intelligence module integrates with up to 2 AI provider APIs per tenant: a primary provider and an optional secondary failover provider.

Interface specification for each provider:

- Protocol: HTTPS REST.
- Authentication: Bearer token (API key stored encrypted using AES-256-GCM in the tenant settings table; key never appears in logs, error messages, or API responses).
- Request timeout: 10 s; failover to the secondary provider triggers automatically on timeout or HTTP 5xx response.
- Supported providers:
  - OpenAI — `api.openai.com`
  - Anthropic — `api.anthropic.com`
  - DeepSeek — `api.deepseek.com`
  - Google Gemini — `generativelanguage.googleapis.com`
- Data minimisation constraint: Prompts shall not contain patient NIN, full legal name, or NIRA registration number. Anonymised encounter IDs are used in place of patient identifiers (see **CONSTRAINT-AI-002**).

### Software Interface Detail — Africa's Talking (SMS Gateway)

- Protocol: HTTPS REST API.
- Authentication: API key per tenant, stored in tenant settings.
- Capabilities: SMS delivery (appointment reminders, medication alerts, missed appointment follow-ups, low-credit alerts); USSD session management (patient lookup, appointment booking on feature phones).
- SMS content: No patient health information (PHI) shall appear in SMS body text. Messages direct the patient to the portal or facility for clinical details.
- Internationalisation: SMS messages are sent in the patient's configured locale (en, fr, sw).

---

## 3.3 Hardware Interfaces

### 3.3.1 Barcode and QR Code Scanners

| Attribute | Specification |
|---|---|
| Connection | USB HID (keyboard emulation), Bluetooth SPP |
| Symbologies | Code 128, Code 39, QR Code, DataMatrix |
| Use Cases | Patient wristband scanning, lab sample identification, pharmacy dispensing verification, inventory GRN |
| Input Method | Scanner output is received as keyboard input; no driver installation required for USB HID devices |

### 3.3.2 Thermal Receipt Printers

| Attribute | Specification |
|---|---|
| Paper Width | 80 mm |
| Protocol | ESC/POS |
| Connection | USB, Bluetooth (mobile dispensing), network (Ethernet/WiFi for cashier stations) |
| Use Cases | Billing receipts, pharmacy dispensing labels, lab sample labels, patient queue tickets |
| Encoding | UTF-8 for multi-language receipt content (English, French, Kiswahili) |

### 3.3.3 Fingerprint Scanners

| Attribute | Specification |
|---|---|
| Connection | USB |
| Integration | SDK-based integration (vendor-specific SDK; system architecture abstracts scanner vendor behind a common interface) |
| Use Cases | Patient biometric registration, returning patient lookup, staff attendance |
| Template Storage | Fingerprint templates stored as encrypted binary blobs; raw fingerprint images are never stored |

### 3.3.4 Laboratory Analysers

| Attribute | Specification |
|---|---|
| Protocol (Primary) | HL7 v2 (ORM for orders, ORU for results) over MLLP/TCP |
| Protocol (Legacy) | ASTM E1394 over RS-232 serial or TCP |
| Connection | TCP/IP (networked analysers), RS-232 serial (legacy analysers via serial-to-TCP converter) |
| Supported Analysers | Cobas (Roche), Mindray (chemistry, haematology), Sysmex (haematology), GeneXpert (TB) |
| Data Flow | Outbound: order messages (ORM) from Medic8 to analyser worklist. Inbound: result messages (ORU/ASTM) from analyser to Medic8 LIS. |
| Result Handling | Auto-populated into pending result queue; flagged for technician validation before clinical release |

### 3.3.5 DICOM Imaging Devices

| Attribute | Specification |
|---|---|
| Protocol | DICOM 3.0 over TCP |
| Services | Modality Worklist (MWL), Storage Commitment, Query/Retrieve (C-FIND, C-MOVE, C-STORE) |
| Modalities | X-ray, ultrasound, CT (where available), dental panoramic |
| Data Flow | Outbound: MWL scheduling from Medic8 to modality. Inbound: DICOM images from modality to PACS via Medic8 DICOM gateway. |
| Image Storage | Images reside in PACS; Medic8 stores study metadata (patient ID, study UID, modality, date, report status) |

### 3.3.6 NFC/RFID Wristband Scanners

| Attribute | Specification |
|---|---|
| Technology | NFC (ISO 14443), RFID (ISO 15693) |
| Connection | USB HID, Bluetooth |
| Use Cases | Inpatient wristband identification, newborn-mother pairing, blood transfusion patient verification |
| Data Encoded | Patient MRN and facility ID encoded on wristband; clinical data is never stored on the wristband |

---

## 3.4 Communications Interfaces

### 3.4.1 HTTPS / TLS

All web application traffic, API communication, and mobile application data exchange shall use HTTPS with TLS 1.2 or higher. TLS 1.0 and TLS 1.1 shall be disabled on all endpoints. Certificate pinning shall be implemented on the Android and iOS mobile applications to prevent man-in-the-middle attacks. All API responses shall honour the `Accept-Language` request header; supported locale values are `en`, `fr`, and `sw`. Where a requested locale is not supported, the system shall fall back to `en`.

### 3.4.2 WebSocket

The system shall use WebSocket connections for real-time clinical notifications that require immediate delivery without polling:

- Critical laboratory value alerts (e.g., potassium > 6.5 mmol/L) pushed to the ordering clinician's active session.
- Emergency department patient arrival notifications pushed to the on-call doctor.
- Bed availability changes pushed to the admissions desk.
- Drug interaction Fatal-level alerts pushed to the prescribing clinician and supervising pharmacist.

WebSocket connections shall authenticate using the same JWT token as the API session. Connections shall auto-reconnect on network interruption with exponential backoff (1 s, 2 s, 4 s, max 30 s).

### 3.4.3 SMTP (Email)

The system shall send email notifications via SMTP for:

- Password reset requests
- Account activation
- Monthly HMIS report generation confirmation
- Audit trail export delivery
- Insurance claim batch submission confirmation

Email shall use TLS-encrypted SMTP (port 587 STARTTLS or port 465 implicit TLS). Plain-text SMTP (port 25) shall not be used.

### 3.4.4 SMS (Africa's Talking)

The system shall send SMS messages via the Africa's Talking REST API for:

- Appointment reminders (configurable: 24 hours and/or 2 hours before appointment)
- Missed appointment follow-up (sent within 24 hours of missed appointment)
- Test result availability notification (no clinical data in SMS body; patient directed to portal)
- Medication refill reminders
- Immunisation schedule reminders (EPI defaulter tracing)

SMS content shall not include any patient health information (PHI). Messages shall direct the patient to the portal or facility for clinical details. SMS sender ID shall be configurable per facility. SMS messages shall be composed in the patient's configured locale (en, fr, sw).

### 3.4.5 USSD (Africa's Talking)

The system shall support USSD sessions via Africa's Talking for feature phone users who cannot access the web portal or mobile application:

- Patient appointment confirmation and rescheduling
- Queue position check
- Basic test result notification (result ready / not ready; no clinical values)
- Mobile money payment initiation

USSD sessions shall time out after 180 seconds of inactivity per Africa's Talking platform limits.

### 3.4.6 Push Notifications

The system shall deliver push notifications to mobile application users:

| Platform | Service | Use Cases |
|---|---|---|
| Android | Firebase Cloud Messaging (FCM) | Appointment reminders, test result availability, medication reminders, payment confirmation, clinical alerts (staff app) |
| iOS | Apple Push Notification service (APNs) | Appointment reminders, test result availability, medication reminders, payment confirmation, clinical alerts (staff app) |

Push notification payloads shall not contain PHI. The notification body shall contain a generic prompt (e.g., "Your test results are ready. Open the app to view.") with the clinical detail accessible only after authentication within the application.

### 3.4.7 HL7 v2 / MLLP

Laboratory analyser communication shall use the Minimum Lower Layer Protocol (MLLP) over TCP as defined in Section 3.2. MLLP wraps HL7 v2 messages with start-of-block (0x0B), end-of-block (0x1C), and carriage return (0x0D) delimiters. The Medic8 integration engine shall maintain persistent TCP connections to configured analysers and handle connection drops with automatic reconnection.

### 3.4.8 DICOM / TCP

Radiology device communication shall use the DICOM protocol over TCP as defined in Section 3.2. The Medic8 DICOM gateway shall operate as both a Service Class User (SCU) for query/retrieve operations and a Service Class Provider (SCP) for storage operations. Association negotiation shall support the following transfer syntaxes: Implicit VR Little Endian, Explicit VR Little Endian, and JPEG 2000 Lossless for compressed image transfer.
