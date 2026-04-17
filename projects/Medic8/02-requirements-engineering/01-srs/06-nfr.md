# 6 Non-Functional Requirements

This section defines the non-functional requirements (NFRs) for the Medic8 system. Each requirement follows the "The system shall..." format per IEEE 830-1998 and IEEE 29148-2018. Every NFR includes a Verifiability section containing a deterministic test case with a clear pass/fail criterion.

Standards: IEEE 830-1998 Section 3.3, IEEE 29148-2018 Section 6.4.

---

## 6.1 Domain Default Requirements

The following 9 requirements are adapted from the healthcare domain baseline (`domains/healthcare/references/nfr-defaults.md`) for the Uganda regulatory and operational context.

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-001: Patient Data Audit Trail

The system shall maintain a complete, tamper-proof audit log of all create, read, update, and delete operations on patient health records in compliance with the Uganda Data Protection and Privacy Act 2019 Section 24. Every audit log entry shall record: `user_id`, `timestamp` (UTC), `action` (create/read/update/delete), `resource_type`, `resource_id`, `facility_id`, `ip_address`, and `outcome` (success/failure). Audit logs shall be append-only; no user role, including Super Admin, shall have the ability to modify or delete audit log entries.

Verifiability: Execute a read operation on a patient record while authenticated as a clinical user. Query the audit log table and verify that an immutable log entry exists containing all 8 required fields with correct values. Attempt to execute an UPDATE or DELETE statement against the audit log table using a Super Admin database connection; the system shall reject the operation and return an error.

<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-002: Data Encryption at Rest

The system shall encrypt all patient health data stored in the database using AES-256-GCM. Unencrypted patient health data shall not exist on any persistent storage medium, including database files, backup files, and temporary files. Encryption key management shall follow NIST SP 800-57 guidelines. The encryption implementation shall function on low-specification hardware common in Ugandan health facilities (Intel Celeron / ARM Cortex-A53 equivalent processors).

Verifiability: Inspect the raw MySQL data directory files on disk; patient health data fields (name, diagnosis, prescription, lab result) shall be unreadable without the encryption key. Execute a SELECT query on an encrypted column without the application decryption layer; the returned value shall be ciphertext. Measure query performance with encryption enabled on a Celeron-class processor; verify P95 query time remains under 200 ms for single-record retrieval.

<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-003: Data Encryption in Transit

All transmission of patient data shall use TLS 1.2 or higher. TLS 1.0 and TLS 1.1 shall be disabled on all endpoints, including the web application, API, FHIR server, and DHIS2 integration endpoints. Certificate pinning shall be enforced on the Android and iOS mobile applications.

Verifiability: Run `nmap --script ssl-enum-ciphers` against all application endpoints; verify that TLS 1.0 and TLS 1.1 return no supported ciphers. Attempt a connection using TLS 1.1; the system shall refuse the connection. Inspect mobile app network traffic using a proxy; verify that connections fail when the server certificate does not match the pinned certificate.

<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-004: Session Timeout

The system shall automatically terminate inactive clinical user sessions after 15 minutes of inactivity, requiring re-authentication to resume. The system shall display a warning prompt at 13 minutes of inactivity, giving the user 2 minutes to extend the session. Auto-saved form data shall be preserved across session timeouts and restored upon re-authentication.

Verifiability: Authenticate as a clinical user; partially complete an OPD consultation form; remain idle for 13 minutes; verify that a session extension prompt appears. Dismiss the prompt and wait 2 additional minutes; verify redirection to the login screen. Re-authenticate; verify that the partially completed form data is restored from auto-save.

<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-005: Multi-Factor Authentication

The system shall require Multi-Factor Authentication (MFA) for the following roles: Super Admin, Facility Admin, Accountant, and Auditor. MFA shall be optional for clinical staff (Doctor, Clinical Officer, Nurse, Pharmacist, Lab Technician). Supported MFA methods shall include: TOTP (authenticator app), SMS OTP (via Africa's Talking), and email OTP. The system shall support fallback from SMS to email OTP when SMS delivery fails within 30 seconds.

Verifiability: Attempt login as Facility Admin with correct username and password only; the system shall not grant access and shall prompt for a second factor. Enter a valid TOTP code; verify access is granted. Attempt login as a Doctor without MFA configured; verify access is granted with password only. Simulate SMS delivery failure during MFA for an Accountant; verify the system falls back to email OTP delivery within 30 seconds.

<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-006: Availability and Offline Resilience

The system shall maintain 99.9% uptime for all cloud-hosted clinical modules, measured monthly (maximum 8.76 hours downtime per year).

$$Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$$

Core clinical modules (patient registration, OPD consultation, prescribing, dispensing, lab result entry) shall function at full capacity with 0% internet connectivity. The system shall detect power restoration and immediately initiate synchronisation of the offline queue. Planned maintenance windows shall be scheduled between 00:00 and 04:00 East Africa Time (EAT) and communicated to facility administrators 48 hours in advance.

Verifiability: Monitor cloud uptime over 30 consecutive days using an external monitoring service (e.g., UptimeRobot); calculate availability percentage; verify it meets or exceeds 99.9%. Disconnect internet on a workstation; register a patient, create an OPD visit, write a prescription, and dispense a drug; verify all operations complete without error. Reconnect internet; verify all records appear in the server database within 5 minutes.

<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-007: Data Retention

The system shall retain patient health records and associated audit logs for a minimum of 10 years from the date of the last clinical encounter, in accordance with Uganda MoH policy. The system shall not permit deletion of patient records that fall within the retention period. After the retention period expires, records shall be archived (not deleted) and accessible to authorised users upon request.

Verifiability: Attempt to delete a patient record where the last encounter occurred less than 10 years ago; the system shall reject the deletion and display a message citing the retention policy. Attempt to delete a patient record where the last encounter occurred more than 10 years ago; the system shall archive the record and confirm the archive action.

<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-008: Breach Notification

The system shall provide tooling to identify and report all patient records affected by a security breach within 72 hours of breach confirmation, in compliance with Uganda PDPA 2019 Section 31. The system shall generate a breach impact report listing: affected patient count, data categories exposed (demographics, clinical, financial), breach timeline, and affected facility identifiers. The system shall support immediate notification to the Personal Data Protection Office (PDPO) and affected patients via SMS.

Verifiability: Simulate a breach event by flagging a user account as compromised. Execute the breach impact report for that account; verify the report is generated within 4 hours of query execution. Verify the report contains all required fields: affected patient count, data categories, timeline, and facility identifiers. Verify the system generates SMS notification drafts for affected patients.

<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md (adapted for Uganda) -->

### NFR-HC-009: HMIS Compliance

The system shall auto-populate HMIS 105 (Outpatient Monthly), HMIS 108 (Inpatient Monthly), and HMIS 033b (Weekly Epidemiological Surveillance) from clinical data without manual re-entry. HMIS form mappings shall be stored in configuration tables, version-controlled, and updatable without code deployment. The system shall support direct API submission to the Uganda DHIS2 platform (`hmis2.health.go.ug`) when internet connectivity is available. The system shall track which reporting periods have been submitted and which are pending.

Verifiability: Record 10 OPD visits with ICD-10 coded diagnoses across 2 age groups and both sexes during a calendar month. Generate the HMIS 105 report for that month; verify that Section 1 tallies match the recorded visits by age group and sex without any manual data entry. Submit the report via DHIS2 API to a test instance; verify successful submission and that the reporting period is marked as "submitted" in the tracking log.

<!-- [END DOMAIN-DEFAULT] -->

---

## 6.2 Healthcare-Specific Non-Functional Requirements

The following NFRs address clinical safety, data isolation, resilience, interoperability, and mobile performance requirements specific to the Medic8 system.

---

### NFR-HC-010: Sensitive Record Access Control

The system shall enforce attribute-based access control (ABAC) for the following sensitive data categories: HIV status, mental health diagnoses, substance abuse records, and reproductive health records. Only clinicians who hold an explicit "sensitive record" permission AND have an active treatment relationship with the patient shall view these fields. All other users shall see "[Restricted]" in place of the field value. All access to sensitive records, whether granted or denied, shall be logged with the viewer's identity, timestamp, facility, and justification.

The system shall implement a "break the glass" emergency access mechanism for sensitive records. Emergency access shall require two-factor patient confirmation (patient name and date of birth), shall expire automatically after 24 hours, and shall trigger an SMS notification to the patient.

Verifiability: Log in as a Doctor without the "sensitive record" permission; navigate to a patient's clinical summary; verify that the HIV status field displays "[Restricted]" instead of the actual value. Log in as a Doctor with "sensitive record" permission and an active treatment relationship; verify the HIV status value is visible. Query the audit log; verify that both the denied and granted access attempts are recorded with user ID, timestamp, facility, and access outcome. Invoke "break the glass" access; verify patient receives an SMS notification within 60 seconds; verify the access expires after 24 hours.

---

### NFR-HC-011: Paediatric Safety — Weight-Based Dosing

The system shall calculate drug doses based on patient weight (mg/kg) for all patients under 12 years. The system shall reject any prescription where the calculated dose exceeds the adult ceiling dose for that drug. The system shall flag any calculated dose that deviates by a factor of 10 or more from the expected dose range as a potential decimal error and require explicit clinician confirmation before proceeding. The system shall block prescription submission if no patient weight has been recorded within 24 hours of the prescribing time.

Verifiability: Create a test patient aged 2 years with a recorded weight of 5 kg. Prescribe a drug with a known mg/kg dose of 10 mg/kg and an adult ceiling dose of 500 mg. Verify the system calculates a dose of 50 mg. Enter a dose of 5000 mg (100x expected); verify the system flags the value as a potential decimal error and blocks submission until the clinician provides an explicit override with documented reason. Enter a dose of 600 mg (exceeds 500 mg adult ceiling); verify the system rejects the prescription. Remove the patient's weight record; attempt to prescribe; verify the system blocks submission with a message requiring weight measurement.

---

### NFR-HC-012: Clinical Decision Support Alert Response

The system shall display drug interaction alerts at 4 severity tiers:

1. Info — passive display in the prescription sidebar; no clinician action required
2. Warning — prominent amber banner display; clinician may proceed without override
3. Serious — modal alert blocking the workflow; clinician must provide a documented override reason to proceed
4. Fatal — hard stop that cannot be overridden by the prescriber; a pharmacist must intervene and resolve the interaction before the prescription is accepted

The system shall log all alert presentations and all override actions with: `clinician_id`, `patient_id`, `alert_id`, `drug_pair`, `severity_tier`, `timestamp`, `action_taken` (acknowledged/overridden/escalated), and `override_reason` (for Tier 3). The system shall track override rates per facility for quality monitoring.

Verifiability: Prescribe two drugs with a known Serious (Tier 3) interaction. Verify that a modal alert appears blocking the workflow. Enter an override reason and confirm; verify the prescription is accepted. Query the audit log; verify the entry contains `clinician_id`, `patient_id`, `alert_id`, the drug pair identifiers, severity "Serious", timestamp, action "overridden", and the override reason text. Prescribe two drugs with a known Fatal (Tier 4) interaction; verify the system blocks the prescription with no override option; verify the system prompts for pharmacist intervention.

---

### NFR-HC-013: Offline Clinical Resilience

Core clinical modules — patient registration, OPD consultation, prescribing, dispensing, and lab result entry — shall function at full capacity with 0% internet connectivity. The system shall queue all transactions locally using IndexedDB (web) or Room/SwiftData (mobile) and synchronise automatically when connectivity resumes. The offline queue shall support a maximum of 72 hours of queued data without data loss.

Offline conflict resolution shall use field-level merge with a conflict log. For non-clinical fields (address, phone, next of kin), last-write-wins applies. For clinical fields (diagnoses, prescriptions, allergies), both versions shall be preserved side by side and flagged for clinician review. No clinical data shall be silently overwritten.

Verifiability: Disconnect internet on a clinical workstation. Register a patient, create an OPD visit, write a prescription, dispense a drug, and enter a lab result. Verify all 5 operations complete without error. Reconnect internet; verify all 5 records appear in the server database within 5 minutes of reconnection. Edit a patient's diagnosis on 2 offline workstations simultaneously; reconnect both; verify the system preserves both versions and flags the conflict for clinician review.

---

### NFR-HC-014: FHIR R4 Compliance

The system shall expose 14 FHIR R4 resource types via a RESTful API:

1. Patient
2. Encounter
3. Observation
4. Condition
5. MedicationRequest
6. MedicationDispense
7. DiagnosticReport
8. ServiceRequest
9. Immunization
10. AllergyIntolerance
11. Procedure
12. Location
13. Practitioner
14. Organization

Every FHIR response shall include a human-readable HTML narrative element within the `text.div` field, ensuring clinical safety when receiving systems cannot fully process structured FHIR data. The system shall support SMART on FHIR for third-party application integration. The system shall generate CDA R2 clinical documents for discharge summaries and referral letters.

Verifiability: Send a GET request to `/fhir/Patient/{id}` for a known patient; validate the response against the HL7 FHIR R4 Patient resource schema using the official FHIR Validator. Verify the response contains a `text` element with a `div` containing human-readable HTML summarising the patient's demographics. Repeat the schema validation for all 14 resource types. Register a SMART on FHIR test app; verify it can authenticate via OAuth 2.0 and retrieve patient data within its granted scopes.

---

### NFR-HC-015: Multi-Tenant Data Isolation

The system shall enforce tenant isolation via a `facility_id` column on every tenant-scoped database table. Every tenant-scoped query shall include a `WHERE facility_id = ?` clause, enforced at the Repository base class level. An Eloquent global scope shall provide secondary defence. Raw SQL queries that do not include a `facility_id` filter shall be rejected by a CI audit rule during the build pipeline. No exception to this rule is permitted.

The global patient identity table (`global_patients`) shall carry no `facility_id` column. Facility B may confirm that a patient exists in the system (identity lookup) but shall not read clinical notes, diagnoses, or prescriptions from Facility A without explicit patient consent or emergency access (BR-DATA-002).

Verifiability: Authenticate as a user belonging to Facility A. Execute a patient list query; verify that zero records from Facility B appear in the results. Attempt to execute a raw SQL query against a tenant-scoped table without a `facility_id` filter in the CI pipeline; verify the build fails with a tenant isolation violation error. Authenticate as Facility B; attempt to access a Facility A patient's clinical records via the API; verify the system returns a 403 Forbidden response.

---

### NFR-HC-016: Auto-Save and Power Loss Recovery

The system shall auto-save form state to local storage (IndexedDB for web, Room/SwiftData for mobile) on every user interaction, including keystrokes, dropdown selections, checkbox toggles, and date picker changes. On power loss, browser crash, or app crash, the system shall restore the last auto-saved state when the user next opens the same form. The restoration prompt shall display the timestamp of the auto-saved data and allow the user to accept or discard the recovered state.

Verifiability: Begin filling an OPD consultation form: enter chief complaint, select 2 diagnoses, prescribe a medication. Terminate the browser process (Task Manager kill, not graceful close). Reopen the browser and navigate to the same form; verify that a recovery prompt appears showing the auto-save timestamp. Accept the recovery; verify all entered data (chief complaint, diagnoses, prescription) is restored exactly as entered. Discard the recovery on a second test; verify the form opens blank.

---

### NFR-HC-017: Mobile App Performance

The Android app shall launch and display the home screen within 3 seconds (cold start) on a device meeting the minimum specification: Android 7.0 (API level 24), 1 GB RAM, and quad-core ARM Cortex-A53 processor. The base installation (APK + initial data) shall consume no more than 50 MB of device storage. Data-lite mode shall function on 2G/EDGE connectivity (64 Kbps). Large result images (radiology) shall download only on WiFi by default.

The iOS app shall launch and display the home screen within 3 seconds (cold start) on the minimum supported device running iOS 15.0.

Verifiability: Install the Android app on a test device meeting minimum specs (Samsung Galaxy J2 Prime or equivalent). Measure cold start time from app icon tap to home screen render using Android Studio profiler; verify the time is under 3 seconds. Measure APK + initial data size; verify it is under 50 MB. Connect the device to a network throttled to 64 Kbps; navigate to the patient list, open a patient record, and submit a form; verify all operations complete without timeout. Verify radiology images display a "Download on WiFi" placeholder when on cellular data.

---

### NFR-HC-018: Nursing Sensitive Outcome Tracking

The system shall track 14 Nursing Sensitive Outcomes (NSOs) as system-level quality indicators per facility per reporting period (monthly):

1. Mortality
2. Urinary tract infection (UTI)
3. Pressure ulcers
4. Pneumonia
5. Deep vein thrombosis / pulmonary embolism (DVT/PE)
6. Gastrointestinal (GI) bleeding
7. Central nervous system (CNS) complications
8. Sepsis
9. Shock / cardiac arrest
10. Wound infection
11. Pulmonary failure
12. Metabolic derangement
13. Failure-to-rescue
14. Length of stay (mean and median, per ward)

NSO data shall be derived automatically from clinical documentation (diagnoses, procedures, discharge status) without manual tallying. The system shall display an NSO dashboard accessible to the Facility Admin and Nursing Director roles, showing trends over time with month-on-month comparison.

Verifiability: Discharge an IPD patient with a recorded diagnosis of pressure ulcer (ICD-10 L89.x) during the current reporting period. Navigate to the NSO dashboard; verify that the pressure ulcer count for the current period has incremented by 1. Discharge a second patient who died during admission; verify the mortality count increments. Verify the dashboard displays month-on-month trend lines for all 14 indicators. Verify the length of stay indicator displays both mean and median values per ward.

---

## 6.3 Data Residency and Backup

---

### NFR-HC-019: Data Residency

The system shall store patient health data in-country (within the borders of the country specified by the tenant's regulatory profile) unless the regulatory profile explicitly permits cross-border transfer. Cross-border data transfer requests via FHIR API or DHIS2 export shall be validated against the active regulatory profile before execution. Transfers to non-permitted destinations shall be blocked and logged.

Verifiability: Configure a tenant with the Uganda regulatory profile. Attempt to export patient data via the FHIR API to a server geolocated outside Uganda without explicit patient consent; verify the system blocks the transfer and logs the attempt. Configure a tenant with the Australia regulatory profile (which permits cross-border transfer under Australian Privacy Principles); verify the export completes.

---

### NFR-HC-020: Backup and Disaster Recovery

The system shall perform automated daily backups with a Recovery Point Objective (RPO) of 24 hours and a Recovery Time Objective (RTO) of 4 hours. Backup verification shall be testable without exposing production patient data (anonymised restore test). The system shall support point-in-time recovery for the MySQL database using binary log replay.

Verifiability: Trigger a manual backup; verify the backup file is created and stored in the designated backup location. Simulate a database failure; initiate a restore from the most recent backup; verify the database is fully operational within 4 hours. Compare the restored data against the pre-failure state; verify no data older than 24 hours is missing. Execute a point-in-time recovery to a timestamp 6 hours before the failure; verify the database state matches the expected state at that timestamp.

---

## 6.4 Localisation and Accessibility

---

### NFR-HC-021: Localisation — String Coverage

The system shall support English (`en`), French (`fr`), and Kiswahili (`sw`) as launch locales. All user-facing labels, error messages, menu items, and system notifications shall be translatable without code changes via locale resource files (`lang/<locale>/` for PHP, `values-<locale>/strings.xml` for Android, `<locale>.lproj/Localizable.strings` for iOS). Date, currency, and number formatting shall be configurable per locale. Clinical terminology (drug names, ICD-10 descriptions) shall remain in English across all locales to prevent clinical errors from translation.

Verifiability: Switch the system language to Kiswahili; verify that all menu items, button labels, and system messages display in Kiswahili. Verify that drug names and ICD-10 descriptions remain in English. Enter a monetary amount; verify it displays in the correct currency format for the configured locale (e.g., UGX 50,000 for Uganda). Switch to French; verify all UI strings render in French with no English fallback visible for strings that have approved French translations.

---

### NFR-HC-022: Critical Lab Value Escalation Timeliness

The system shall deliver critical lab value notifications to the requesting doctor within 60 seconds of result entry. If the notification is not acknowledged within 30 minutes, the system shall escalate to the ward sister. If not acknowledged within 60 minutes, the system shall escalate to the Facility Admin. All escalation steps shall be timestamped in the audit trail. Notification delivery shall function via WebSocket (web), push notification (mobile), and SMS (fallback).

Verifiability: Enter a lab result exceeding the panic threshold (e.g., potassium 7.0 mmol/L). Measure the time from result submission to notification appearance on the requesting doctor's screen; verify it is under 60 seconds. Do not acknowledge the notification; verify the system escalates to the ward sister at the 30-minute mark. Verify the audit trail records the initial notification timestamp, the 30-minute escalation timestamp, and the target user for each step.

---

### NFR-HC-023: Task Resumption After Interruption

The system shall persist the clinician's session state (current form, entered data, cursor position, selected patient context) on every user interaction. When a clinician navigates away from an in-progress form (to handle an emergency, respond to an alert, or view another patient) and returns, the system shall restore the exact prior state, including all entered data and the active field. Incomplete fields shall be highlighted with a visual indicator on return.

Verifiability: Begin an OPD consultation form; enter the chief complaint and 1 diagnosis; navigate to a different patient's record to check a lab result; navigate back to the original patient's OPD form; verify all entered data is present and the cursor is positioned at the last active field. Verify incomplete mandatory fields are highlighted.

---

### NFR-HC-024: Prescribing Authority Enforcement

The system shall enforce role-based prescribing authority per the Uganda Medical and Dental Practitioners Act. Doctors may prescribe all medications on the facility formulary. Clinical Officers may prescribe within their gazetted scope of practice. Nurses shall not prescribe; they may administer prescribed medications only. Prescribing authority rules shall be configurable per country via the country configuration layer.

Verifiability: Log in as a Nurse; attempt to create a new prescription; verify the system blocks the action with a message stating that the Nurse role does not have prescribing authority. Log in as a Clinical Officer; attempt to prescribe a medication outside the gazetted scope; verify the system blocks the prescription. Log in as a Doctor; prescribe any medication on the formulary; verify the prescription is accepted.

---

## 6.5 AI Intelligence Module Non-Functional Requirements

---

### NFR-PERF-AI-001: AI Capability Response Time

The system shall return AI capability responses (clinical note draft, differential diagnosis, ICD code suggestions, patient plain-language summary, claim scrub, outbreak alert) within 8 s at P95 under normal load, defined as 1 concurrent AI request per 10 active clinicians on the same tenant.

Verifiability: Simulate normal load (1 concurrent AI request per 10 active test clinicians on a single tenant). Issue 100 AI clinical note draft requests; measure response time for each. Verify that the 95th percentile response time is ≤ 8 s. Repeat for each of the 6 AI capabilities. The test fails if any capability exceeds 8 s at P95 under the defined normal load condition.

---

### NFR-PERF-AI-002: AI Provider Failover Latency

The system shall complete AI provider failover within 12 s of primary provider timeout. The failover transition shall be transparent to the end user except for a non-blocking "Switching AI provider..." notification.

Verifiability: Configure a primary AI provider with a simulated 10 s timeout (e.g., mock endpoint that never responds). Issue an AI capability request. Measure elapsed time from request initiation to response delivery from the secondary provider. Verify elapsed time is ≤ 12 s. Verify the "Switching AI provider..." notification is visible in the UI during the transition. Verify no modal dialog, blocking spinner, or workflow interruption occurs.

---

### NFR-AVAIL-AI-001: AI Intelligence Module Availability

The AI Intelligence module shall maintain ≥ 99.0% availability, measured as the percentage of AI capability requests that return a valid response or a graceful degradation notification within 15 s, calculated monthly.

Verifiability: Monitor AI capability requests over 30 consecutive days using the platform's `ai_usage_log` table. Count requests where the response time exceeds 15 s or where no response (valid or degradation notification) is delivered. Calculate: $Availability = \frac{valid\ responses + graceful\ degradation\ responses}{total\ requests} \times 100\%$. Verify the result is ≥ 99.0%.

---

### NFR-AVAIL-AI-002: AI Unavailability Isolation

AI Intelligence module unavailability shall not affect the availability of any clinical, administrative, or financial module. Clinical module availability shall remain ≥ 99.9% regardless of AI provider status.

Verifiability: Disable both AI providers for a configured tenant (set both API keys to invalid values). Verify that: (1) the patient registration module accepts new registrations; (2) the OPD consultation module accepts consultations and diagnosis entries; (3) the prescribing module accepts prescriptions; (4) the billing module accepts payments. Measure clinical module availability over a 24-hour window with AI disabled; verify it remains ≥ 99.9%. Verify that AI capability UI elements are hidden or replaced with a "AI unavailable" indicator and no error modal blocks any clinical action.

---

### NFR-I18N-001: Translation Coverage at Ship

100% of user-visible strings in the web portal, Android application, and iOS application shall have approved translations in `en`, `fr`, and `sw` before any module ships to production. Zero `[I18N-GAP]` tags are permitted in a production build.

Verifiability: Execute the build pipeline for the web portal, Android app, and iOS app targeting the production environment. Parse the build log for any `[I18N-GAP: <key>]` entries. The build shall fail if any `[I18N-GAP]` tag is present. Count total string keys in `lang/en/`; verify matching counts exist in `lang/fr/` and `lang/sw/`. Repeat for Android `values-fr/strings.xml`, `values-sw/strings.xml` and iOS `fr.lproj/Localizable.strings`, `sw.lproj/Localizable.strings`.

---

### NFR-I18N-002: Locale Switch Latency

The locale switching operation (user changes their preferred language from the profile screen) shall complete within 500 ms at P95, measured from the user's confirmation action to the re-rendered screen fully displaying in the new locale.

Verifiability: Authenticate as a user with locale set to `en`. Navigate to the profile screen. Switch locale to `fr`. Measure time from confirmation click to complete screen render in French using browser developer tools (page render complete event). Repeat 20 times; calculate P95. Verify P95 ≤ 500 ms. Repeat the test switching from `fr` to `sw`. Verify no full page reload occurs; the locale switch shall complete via a JavaScript re-render without a browser navigation event.

---

### NFR-I18N-003: Clinical Alert Locale Rendering

Clinical severity alert labels (Fatal, Serious, Warning, Info) shall render in the clinician's configured UI language within the same response time as the clinical alert itself. No additional latency shall be introduced by locale resolution for alert rendering.

Verifiability: Configure a clinician's locale to `sw`. Trigger a Warning-level drug interaction alert. Verify the alert banner displays the Kiswahili label for "Warning" within the same render cycle as the alert content. Measure alert render time with locale `en` and with locale `sw`; verify the difference is ≤ 10 ms at P95 across 50 alert triggers. Verify no English label is visible for any severity level when the clinician's locale is `sw` or `fr`.

---

### NFR-SEC-AI-001: AI Provider API Key Security

AI provider API keys shall be stored encrypted at rest using AES-256-GCM. Keys shall never appear in application logs, error messages, or API responses.

Verifiability: Enter an AI provider API key via the AI admin panel. Query the `tenant_settings` table directly in MySQL; verify the stored value is ciphertext, not the plaintext key. Trigger an intentional API error with the key configured (e.g., invalid request body); inspect the error log; verify the API key does not appear in any log entry. Make a GET request to any Medic8 API endpoint as an authenticated user; verify no API key value appears in any response body or response header.

---

### NFR-SEC-AI-002: AI Usage Log Access Control

Token usage logs (`ai_usage_log` table) shall be accessible only to the tenant's AI Administrator role and to Chwezi Core Systems operations staff. No clinical user role shall have read access to the `ai_usage_log` table.

Verifiability: Authenticate as each of the following roles: Doctor, Clinical Officer, Nurse, Pharmacist, Lab Technician, Receptionist, Cashier, Insurance Clerk. Attempt to access the AI usage dashboard (web portal) and issue a direct API request to the AI usage log endpoint for each role. Verify all 8 requests return HTTP 403 Forbidden. Authenticate as AI Administrator; verify the AI usage dashboard loads and displays token usage data. Authenticate as Super Admin (Chwezi Core Systems operations); verify read access is granted.
