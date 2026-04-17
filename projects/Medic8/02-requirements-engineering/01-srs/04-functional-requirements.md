## Section 4: Functional Requirements

> All requirements in this section conform to IEEE 830-1998 stimulus-response form. Each requirement is uniquely identified, unambiguous, complete, and verifiable. Every requirement includes: a unique identifier, a stimulus (trigger condition), a system response, input specifications, output specifications, applicable business rule cross-references, and a verifiability criterion (test oracle). Phase 1 requirements are specified in full detail; Phase 2-4 requirements are summarised and will be expanded at the start of each phase.

---

### FR-AUTH: Authentication and Session Management

#### FR-AUTH-001: Web Session Login

**Stimulus:** A user submits a POST request to `/auth/login` with `email`, `password`, and a valid `csrf_token` from the login form.

**Response:** The system shall:
1. Validate the CSRF token against the session-stored token. If invalid, return HTTP 403 with `{"error": {"code": "CSRF_INVALID"}}` and log the attempt.
2. Look up the user by `email` in the `users` table, checking `status = active` and `locked = false`.
3. If the account is locked, return HTTP 403 with `{"error": {"code": "ACCOUNT_LOCKED", "message": "Account locked after 5 failed attempts. Contact your facility administrator."}}`.
4. Verify the submitted password against the stored Argon2ID hash.
5. On failure: increment `failed_login_attempts`. If count reaches 5, set `locked = true`, log the lock event. Return HTTP 401 with `{"error": {"code": "INVALID_CREDENTIALS"}}`. Do not reveal whether the email or password was incorrect.
6. On success: reset `failed_login_attempts` to 0. Regenerate the PHP session ID (`session_regenerate_id(true)`). Set session variables using the `medic8_` prefix: `user_id`, `facility_id`, `role`, `full_name`, `last_activity`. Resolve the user's `facility_id` to enforce tenant isolation (BR-DATA-004). Redirect to the role-appropriate dashboard.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `email` | string | Valid email, trimmed |
| `password` | string | 8-255 characters |
| `csrf_token` | string | Must match `$_SESSION['medic8_csrf_token']` |

**Output:** HTTP 302 redirect to role dashboard on success.

**Error conditions:**

| Condition | HTTP Code | Error Code |
|---|---|---|
| CSRF token invalid | 403 | `CSRF_INVALID` |
| Email not found | 401 | `INVALID_CREDENTIALS` |
| Password incorrect | 401 | `INVALID_CREDENTIALS` |
| Account locked | 403 | `ACCOUNT_LOCKED` |
| Account inactive | 403 | `ACCOUNT_INACTIVE` |
| Tenant suspended | 403 | `TENANT_SUSPENDED` |

**Business rules:** BR-DATA-004.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Submit correct credentials for an active facility -> session created, redirect to dashboard (HTTP 302). Submit incorrect password 5 times -> 6th attempt returns HTTP 403 `ACCOUNT_LOCKED`, `locked = true` in database. CSRF token mismatch -> HTTP 403 `CSRF_INVALID`. Attempt login for a suspended facility -> HTTP 403 `TENANT_SUSPENDED`.

---

#### FR-AUTH-002: Mobile / API JWT Login

**Stimulus:** A client sends `POST /api/v1/auth/login` with `email`, `password`, and `device_id` in the JSON body.

**Response:** The system shall:
1. Validate the user credentials identically to FR-AUTH-001 (steps 2-5), excluding CSRF.
2. On success: generate an access token (JWT, HS256, 15-minute expiry) and a refresh token (JWT, HS256, 30-day expiry). Both tokens contain: `sub` (user_id), `fid` (facility_id), `role`, `did` (device_id), `jti` (UUID v4), `exp`, `type`.
3. Persist the refresh token JTI and expiry in `api_refresh_tokens` (user_id, jti, device_id, expires_at, revoked=false).
4. Return HTTP 200 with `{"success": true, "data": {"access_token": "...", "refresh_token": "...", "expires_in": 900, "token_type": "Bearer"}}`.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `email` | string | Required |
| `password` | string | Required |
| `device_id` | string | Required, max 255 chars, identifies the device for token revocation |

**Error conditions:** Same as FR-AUTH-001 (excluding CSRF). Additionally: missing `device_id` -> HTTP 422.

**Business rules:** BR-DATA-004.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Valid credentials -> HTTP 200 with two valid JWT tokens. Decode access token, verify `fid` equals user's `facility_id`, `exp` is 15 minutes from now. Decode refresh token, verify `exp` is 30 days from now. Invalid credentials -> HTTP 401. Locked account -> HTTP 403.

---

#### FR-AUTH-003: JWT Token Refresh

**Stimulus:** A client sends `POST /api/v1/auth/refresh` with a valid, non-expired refresh token in the JSON body or `Authorization: Bearer` header.

**Response:** The system shall:
1. Verify the JWT signature. If invalid, return HTTP 401 `{"error": {"code": "INVALID_TOKEN"}}`.
2. Check the token's `jti` against `api_refresh_tokens`. If the JTI is not found or `revoked = true`, return HTTP 401 `{"error": {"code": "TOKEN_REVOKED"}}`.
3. If the token is valid and not revoked: mark the old JTI as `revoked = true` in `api_refresh_tokens` (refresh token rotation).
4. Generate a new access token and a new refresh token (same structure as FR-AUTH-002).
5. Persist the new refresh token JTI.
6. Return HTTP 200 with the new token pair.

**Error conditions:**

| Condition | HTTP Code | Error Code |
|---|---|---|
| Invalid signature | 401 | `INVALID_TOKEN` |
| Token expired | 401 | `TOKEN_EXPIRED` |
| Token revoked | 401 | `TOKEN_REVOKED` |
| JTI not in database | 401 | `TOKEN_REVOKED` |

**Business rules:** None.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Valid refresh token -> HTTP 200 with new token pair; old JTI row shows `revoked = true`. Revoked token -> HTTP 401 `TOKEN_REVOKED`. Expired token -> HTTP 401 `TOKEN_EXPIRED`. Replay of old refresh token after rotation -> HTTP 401 `TOKEN_REVOKED`.

---

#### FR-AUTH-004: Session and Token Logout

**Stimulus:** An authenticated user sends `POST /auth/logout` (web) or `POST /api/v1/auth/logout` (API) with a valid session or JWT.

**Response (web):** Destroy the session (`session_destroy()`), clear all `medic8_` prefixed session variables, redirect to `/auth/login`.

**Response (API):** Revoke all refresh tokens associated with the `device_id` in `api_refresh_tokens` by setting `revoked = true`. Return HTTP 200 `{"success": true}`.

**Business rules:** None.
**Priority:** Critical
**Phase:** 1
**Verifiability (web):** After logout, sending a request with the old session cookie returns HTTP 302 redirect to login. **Verifiability (API):** After logout, attempting to use the old refresh token returns HTTP 401 `TOKEN_REVOKED`.

---

#### FR-AUTH-005: Idle Session Timeout

**Stimulus:** An authenticated web session exists and `$_SESSION['medic8_last_activity']` is more than 900 seconds (15 minutes) ago at the time of a new request.

**Response:** The system shall invalidate the session (equivalent to logout) and return HTTP 302 redirect to `/auth/login` with `?reason=timeout`. Auto-saved form data (BR-DATA-005) is preserved in local storage for recovery on re-login.

**Business rules:** BR-DATA-004, BR-DATA-005.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Manually set `medic8_last_activity` to `time() - 901`. Send any authenticated request. Receive HTTP 302 to login with `reason=timeout` query parameter.

---

#### FR-AUTH-006: Multi-Factor Authentication for Admin Roles

**Stimulus:** A user with role `facility_admin`, `facility_director`, or `super_admin` attempts to log in.

**Response:** After successful password verification (FR-AUTH-001 steps 2-5), the system shall require a TOTP code or SMS OTP before completing the session. If the MFA challenge fails, the session is not created. If MFA succeeds, the session is created with an additional `mfa_verified = true` flag.

**Error conditions:** Incorrect TOTP -> HTTP 422 `{"error": {"code": "MFA_INVALID"}}`. Expired TOTP window -> HTTP 422 `{"error": {"code": "MFA_EXPIRED"}}`.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Log in as `facility_admin` with correct password; confirm browser is redirected to MFA step, not dashboard. Enter correct TOTP; confirm session created with `medic8_mfa_verified = true`. Attempt to access admin dashboard with session missing `mfa_verified` -> HTTP 302 to MFA page.

---

### FR-TNT: Tenant Management

#### FR-TNT-001: Facility Provisioning

**Stimulus:** A Super Admin submits a POST to `/adminpanel/api/v1/facilities` with facility name, country, subscription tier, and owner contact details.

**Response:** The system shall:
1. Create a record in the `facilities` table with `status = pending`, generate a `facility_id` (auto-increment) and a unique `slug` (URL-safe facility name + numeric suffix if collision).
2. Create the Facility Admin user account with `role = facility_admin`, `facility_id = <new>`, a system-generated password, `force_password_change = true`.
3. Send a welcome email and SMS to the owner with login URL and temporary password.
4. Log the provisioning action: `{super_admin_user_id, action: FACILITY_CREATED, facility_id, timestamp}`.
5. Return HTTP 201 with the new facility record.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `name` | string | 2-150 chars, required |
| `country` | string | ISO 3166-1 alpha-2, required, defaults to `UG` |
| `tier` | enum | `basic`, `pro`, `enterprise`, required |
| `facility_type` | enum | `clinic`, `health_centre_ii`, `health_centre_iii`, `health_centre_iv`, `general_hospital`, `regional_referral`, `national_referral`, required |
| `owner_name` | string | 2-100 chars, required |
| `owner_email` | string | Valid email, unique across all facilities, required |
| `owner_phone` | string | E.164 format, required |

**Business rules:** BR-DATA-004.
**Priority:** Critical
**Phase:** 1
**Verifiability:** POST valid facility data -> HTTP 201, `facilities` row created with `status = pending`, `users` row created with `force_password_change = true`, audit log entry exists, welcome email sent.

---

#### FR-TNT-002: Facility Activation and Deactivation

**Stimulus:** A Super Admin sends `PATCH /adminpanel/api/v1/facilities/{id}` with `{"status": "active"}` or `{"status": "suspended", "reason": "..."}`.

**Response (activation):** Update `facilities.status` to `active`. Log the action. Return HTTP 200.

**Response (suspension):** Update `facilities.status` to `suspended`. Invalidate all active sessions for that facility. Log the action with reason. Return HTTP 200.

**Post-suspension behaviour:** All web and API authentication attempts for suspended-facility users return HTTP 403 `{"error": {"code": "TENANT_SUSPENDED", "message": "Your facility account has been suspended. Contact support."}}`.

**Business rules:** BR-DATA-004.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Suspend a facility. Attempt login as a user of that facility -> HTTP 403 `TENANT_SUSPENDED`. Re-activate -> login succeeds.

---

#### FR-TNT-003: Facility Configuration

**Stimulus:** A Facility Admin sends `PATCH /api/v1/facility/config` with configuration parameters.

**Response:** The system shall update the facility configuration record with the submitted parameters. Configurable items include: enabled modules (per-module activation), pricing tier, default currency, tax settings, MRN format, logo, operating hours, and ward/department structure.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `enabled_modules` | array | Valid module identifiers from the platform module registry |
| `currency` | string | ISO 4217, default `UGX` |
| `tax_rate` | decimal | 0-100, percentage |
| `mrn_format` | string | Pattern string with placeholders, e.g. `{FACILITY}-{YEAR}-{SEQ}` |
| `logo` | file | Max 2 MB, JPEG/PNG |
| `operating_hours` | object | `{start: "08:00", end: "17:00"}` |

**Business rules:** BR-DATA-004.
**Priority:** High
**Phase:** 1
**Verifiability:** Update `enabled_modules` to exclude pharmacy -> pharmacy menu item disappears for all users. Update `currency` to `KES` -> all billing screens display KES. Update `mrn_format` -> next registered patient's MRN follows the new format.

---

#### FR-TNT-004: Country Configuration

**Stimulus:** A Super Admin creates or updates a country configuration record via `POST /adminpanel/api/v1/countries` or `PATCH /adminpanel/api/v1/countries/{code}`.

**Response:** The system shall store the country-level configuration that governs regulatory compliance for all facilities in that country. Configuration includes: HMIS form set, disease surveillance list, EPI schedule, drug scheduling classes, tax rules, insurance scheme catalogue, currency, statutory deductions (PAYE, social security), and clinical coding system preference (ICD-10 vs ICD-11).

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `country_code` | string | ISO 3166-1 alpha-2, unique |
| `country_name` | string | Required |
| `currency` | string | ISO 4217 |
| `hmis_forms` | array | List of HMIS form identifiers |
| `epi_schedule` | object | Vaccine schedule definition |
| `tax_rules` | object | PAYE brackets, social security rates |
| `coding_system` | enum | `icd10`, `icd11`, `both` |

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Create a Uganda country config with HMIS 105/108/033b forms. Create a facility assigned to Uganda. Confirm the facility's HMIS reporting module loads the Uganda form set. Create a Kenya country config with different forms. Confirm a Kenyan facility loads the Kenya form set.

---

### FR-REG: Patient Registration and Identity

#### FR-REG-001: New Patient Registration

**Stimulus:** An authorised user (Receptionist, Nurse, or Records Officer role) submits `POST /api/v1/patients` with the patient's personal details.

**Response:** The system shall:
1. Validate all required fields (see input specifications below).
2. Trigger duplicate detection (FR-REG-009). If the EMPI returns matches with a confidence score exceeding 80%, present matches to the user with a mandatory duplicate warning that cannot be dismissed without action (BR-PID-002).
3. If the user confirms "New Patient": create a new `global_patients` record with a UUID v4 `patient_uid`. Create a `facility_patients` record linking `patient_uid` to `facility_id` with `status = active`.
4. Auto-generate a unique MRN per the facility's configured format (FR-REG-002).
5. Assign the default patient category based on age (adult if >= 12 years, paediatric if < 12 years) unless overridden.
6. Return HTTP 201 with the full patient record including `patient_uid` and `mrn`.
7. Operation must complete within 500 ms at P95.

**Input specifications -- required fields:**

| Field | Type | Constraints |
|---|---|---|
| `first_name` | string | 1-100 chars |
| `last_name` | string | 1-100 chars |
| `sex` | enum | `male`, `female` |
| `date_of_birth` | date | ISO 8601, must be in the past; OR `estimated_age` in years |
| `contact_phone` | string | E.164 format; OR `physical_address` (at least one required) |

**Input specifications -- optional fields:** `middle_name`, `nin` (National Identification Number), `passport_number`, `unhcr_id`, `nhis_number`, `email`, `blood_group` (ABO + Rh), `photo` (max 2 MB, JPEG/PNG), `next_of_kin_name`, `next_of_kin_phone`, `next_of_kin_relationship`, `allergies` (array of allergy objects), `chronic_conditions` (array of ICD-10 codes), `nationality` (default `UG`), `district`, `sub_county`, `village`, `tribe`, `religion`, `occupation`, `marital_status`.

**Error conditions:**

| Condition | HTTP Code | Error Code |
|---|---|---|
| Required field missing | 422 | `VALIDATION_ERROR` |
| No contact method (phone or address) | 422 | `CONTACT_REQUIRED` |
| Date of birth in the future | 422 | `INVALID_DOB` |
| Duplicate detected, user forced to resolve | 409 | `DUPLICATE_DETECTED` |

**Business rules:** BR-PID-001, BR-PID-002, BR-PID-004, BR-DATA-001, BR-DATA-006.
**Priority:** Critical
**Phase:** 1
**Verifiability:** POST valid new patient -> HTTP 201, `global_patients` row created with UUID `patient_uid`, `facility_patients` row with `facility_id` = caller's facility, MRN generated. POST with neither phone nor address -> HTTP 422 `CONTACT_REQUIRED`. POST a patient with matching name and DOB to an existing record -> duplicate warning presented before creation.

---

#### FR-REG-002: Unique Patient ID (MRN) Auto-Generation

**Stimulus:** A new patient record is created (FR-REG-001) or an existing global patient is registered at a new facility.

**Response:** The system shall auto-generate a Medical Record Number (MRN) unique within the facility, following the facility's configured MRN format (e.g., `HMH-2026-00001`). The sequence number is monotonically increasing per facility and is never reused, even if a patient record is merged or deactivated.

**Business rules:** BR-PID-004.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Register 3 patients at Facility A -> MRNs are sequential (e.g., `HMH-2026-00001`, `HMH-2026-00002`, `HMH-2026-00003`). Register the same patient at Facility B -> a different MRN is generated under Facility B's format. Delete patient 2, register a new patient -> MRN is `HMH-2026-00004`, not `HMH-2026-00002`.

---

#### FR-REG-003: Returning Patient Lookup

**Stimulus:** An authorised user sends `GET /api/v1/patients?q={query}` where `{query}` is a search string.

**Response:** The system shall search for patients matching the query against `first_name`, `last_name`, `mrn`, `contact_phone`, `nin`, `passport_number`, `unhcr_id`, and `nhis_number`, scoped to the caller's `facility_id`. Return up to 25 results ordered by relevance. Response within 300 ms at P95.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `q` | string | Min 2 chars, searches across all identifier fields |

**Error conditions:** Empty `q` parameter -> return HTTP 422 `QUERY_REQUIRED`.

**Business rules:** BR-PID-004, BR-DATA-004.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Create 100 patients. Search `q=nakamya` -> returns only patients with "nakamya" in their name. Confirm all results belong to the caller's `facility_id` only. Search by phone number `q=+256700` -> returns matching patients.

---

#### FR-REG-004: Patient Category Assignment

**Stimulus:** An authorised user sends `PATCH /api/v1/patients/{patient_uid}/category` with `{"category": "<category>"}`.

**Response:** The system shall update the patient's category within the facility. Valid categories: `adult`, `paediatric`, `staff`, `vip`, `indigent`, `refugee`. The category determines pricing tier (FR-BIL-003), clinical protocols (e.g., paediatric dosing for paediatric category), and reporting segmentation. Category changes are logged in the audit trail.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `category` | enum | `adult`, `paediatric`, `staff`, `vip`, `indigent`, `refugee` |

**Business rules:** BR-HOPE-002 (indigent/sponsored workflow for write-off).
**Priority:** High
**Phase:** 1
**Verifiability:** Set category to `staff` -> billing screen shows staff pricing. Set category to `indigent` -> charity write-off workflow is available at discharge. Set category to `paediatric` -> prescribing enforces weight-based dosing (BR-CLIN-006).

---

#### FR-REG-005: Multiple Identifier Support

**Stimulus:** An authorised user sends `POST /api/v1/patients/{patient_uid}/identifiers` with one or more identifier records.

**Response:** The system shall store each identifier type-value pair against the patient record. Supported types: `nin`, `mrn`, `passport`, `unhcr_id`, `nhis`, `phone`, `email`. Any stored identifier can be used for patient lookup (FR-REG-003). Duplicate identifiers of the same type across different patients trigger a duplicate warning.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `type` | enum | `nin`, `passport`, `unhcr_id`, `nhis`, `phone`, `email` |
| `value` | string | 1-100 chars, unique per type across the platform |

**Business rules:** BR-PID-004.
**Priority:** High
**Phase:** 1
**Verifiability:** Add NIN `CM12345678ABCDE` to Patient A. Search `q=CM12345678ABCDE` -> returns Patient A. Attempt to add the same NIN to Patient B -> duplicate warning.

---

#### FR-REG-006: Guardian and Next-of-Kin Linking for Paediatric Patients

**Stimulus:** An authorised user submits `POST /api/v1/patients/{patient_uid}/guardians` with guardian details for a patient whose category is `paediatric` or whose age is under 18.

**Response:** The system shall:
1. Store the guardian record linked to the patient. A patient may have multiple guardians.
2. If the guardian is also a registered patient, link by `patient_uid`. Otherwise, store standalone guardian details (name, phone, relationship, NIN).
3. Flag the primary guardian for consent-by-proxy purposes.
4. For paediatric patients, at least one guardian record is required before clinical encounters can proceed.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `guardian_name` | string | Required, 2-100 chars |
| `relationship` | enum | `mother`, `father`, `grandparent`, `sibling`, `uncle`, `aunt`, `other` |
| `phone` | string | E.164 format, required |
| `is_primary` | boolean | Default true for first guardian |
| `linked_patient_uid` | UUID | Optional, if guardian is a registered patient |

**Business rules:** BR-PID-004.
**Priority:** High
**Phase:** 1
**Verifiability:** Register a paediatric patient (age 5). Attempt to start an OPD visit without a guardian record -> system blocks with `GUARDIAN_REQUIRED`. Add a guardian -> OPD visit can proceed. Add a second guardian with `is_primary = true` -> first guardian's `is_primary` is set to false.

---

#### FR-REG-007: Patient Profile

**Stimulus:** An authorised user sends `GET /api/v1/patients/{patient_uid}` to retrieve the patient profile, or `PATCH /api/v1/patients/{patient_uid}` to update profile fields.

**Response:** The system shall return or update the patient's complete profile including: photo, demographics, blood group, allergies (with severity and reaction type), chronic conditions (ICD-10 coded), active medications, and clinical summary. Allergy data is prominently displayed on every clinical screen (OPD, prescription, pharmacy) as a safety alert banner.

**Business rules:** BR-DATA-001, BR-DATA-006.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Add allergy `Penicillin - Anaphylaxis` to patient profile. Open OPD consultation for the same patient -> allergy banner displays `Penicillin - Anaphylaxis` in red. Prescribe Amoxicillin (penicillin class) -> drug interaction alert fires (FR-OPD-008).

---

#### FR-REG-008: Patient Record Merge with Audit Trail

**Stimulus:** An authorised user (Records Officer or Facility Admin role) submits `POST /api/v1/patients/merge` with `source_patient_uid` and `target_patient_uid`.

**Response:** The system shall:
1. Present a side-by-side comparison of both records for review.
2. On confirmation: transfer all clinical encounters, billing records, lab results, prescriptions, and appointments from the source record to the target (surviving) record.
3. Mark the source record as `merged`, retaining it as a redirect pointer.
4. Log the merge with: performing user, timestamp, source patient UID, target patient UID, and all transferred record counts.
5. The merge is reversible (unmerge) within 30 days (BR-PID-003).

**Business rules:** BR-PID-003.
**Priority:** High
**Phase:** 1
**Verifiability:** Create Patient A with 3 visits and Patient B with 2 visits. Merge A into B. Confirm B now shows 5 visits. Search for Patient A's MRN -> redirects to Patient B. Unmerge within 30 days -> both records restored. Attempt unmerge after 30 days -> HTTP 422 `UNMERGE_WINDOW_EXPIRED`.

---

#### FR-REG-009: EMPI Duplicate Detection

**Stimulus:** A new patient registration is submitted (FR-REG-001), or a scheduled batch duplicate scan runs nightly.

**Response:** The system shall:
1. Execute probabilistic matching using the EMPI engine against `first_name`, `last_name`, `date_of_birth`, `nin`, and `contact_phone` (BR-PID-001).
2. Apply Soundex and Metaphone algorithms adapted for African naming patterns (compound surnames, clan names, spelling variations).
3. Return a list of potential matches with confidence scores.
4. Confidence score exceeding 80% triggers a mandatory duplicate warning that cannot be dismissed without explicit user action (BR-PID-002).
5. Confidence score between 60% and 80% generates an advisory notification to the Records Officer.

**Business rules:** BR-PID-001, BR-PID-002.
**Priority:** High
**Phase:** 1
**Verifiability:** Register "John Mukasa" DOB 1990-05-15. Register "Jon Mukasa" DOB 1990-05-15 -> confidence score > 80%, mandatory warning displayed. Register "John Mukasa" DOB 1985-01-01 (different DOB) -> confidence score between 60-80%, advisory notification generated.

---

#### FR-REG-010: Cross-Facility Patient Lookup via Global Identity

**Stimulus:** An authorised clinician at Facility B sends `GET /api/v1/global-patients?q={query}` to search for a patient registered at another facility.

**Response:** The system shall:
1. Search the `global_patients` table (which carries no `facility_id` column) for matching records (BR-DATA-001).
2. Return identity-level data only: name, age, sex, and list of facilities where the patient has been seen.
3. Clinical records (diagnoses, prescriptions, lab results) are not returned unless emergency access is invoked (FR-RBAC-006, BR-DATA-002).

**Business rules:** BR-DATA-001, BR-DATA-002, BR-HOPE-001.
**Priority:** High
**Phase:** 1
**Verifiability:** Register a patient at Facility A. Log in as Facility B clinician. Search by the patient's NIN -> identity data returned, clinical data absent. Invoke emergency access (FR-RBAC-006) -> limited clinical data returned, SMS sent to patient, access logged.

---

#### FR-REG-011: Triage Queue Management

**Stimulus:** A patient completes registration or triage vital signs entry and is assigned a triage level.

**Response:** The system shall add the patient to the facility's triage queue, sorted by triage priority (BR-CLIN-001): Emergency patients appear at the top of all queues. Urgent patients are positioned above semi-urgent and non-urgent. Within the same triage level, patients are ordered by arrival time (FIFO). The queue updates in real time via WebSocket or polling.

**Business rules:** BR-CLIN-001.
**Priority:** High
**Phase:** 1
**Verifiability:** Register 3 patients: Patient A (non-urgent, 09:00), Patient B (urgent, 09:05), Patient C (emergency, 09:10). Queue order: C, B, A. Add Patient D (urgent, 09:15) -> queue order: C, B, D, A.

---

### FR-OPD: Outpatient Department

#### FR-OPD-001: Triage Vital Signs Entry

**Stimulus:** A Nurse selects a patient from the registration queue and opens the triage form.

**Response:** The system shall present a vital signs entry form and record all submitted values against the patient's visit. BMI is auto-calculated from weight and height. For patients under 12, MUAC (Mid-Upper Arm Circumference) is displayed as a required field. For patients under 5, Z-scores (weight-for-age, height-for-age, weight-for-height) are auto-calculated against WHO growth standards. The system calculates the NEWS2 Early Warning Score from the entered vitals (FR-OPD-014) and assigns a triage level.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `systolic_bp` | integer | 40-300 mmHg |
| `diastolic_bp` | integer | 20-200 mmHg |
| `temperature` | decimal | 30.0-45.0 C |
| `pulse` | integer | 20-250 bpm |
| `spo2` | integer | 50-100 % |
| `respiratory_rate` | integer | 4-60 breaths/min |
| `weight` | decimal | 0.3-300 kg |
| `height` | decimal | 20-250 cm |
| `muac` | decimal | 5-40 cm (required if age < 12) |
| `triage_level` | enum | `emergency`, `urgent`, `semi_urgent`, `non_urgent` |

**Output:** Calculated fields: `bmi` (weight / height^2), `news2_score`, `triage_level` (auto-suggested from NEWS2, overridable by nurse).

**Business rules:** BR-CLIN-001, BR-CLIN-007.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Enter vitals with SpO2 = 91%, pulse = 130, temp = 39.5 -> NEWS2 score >= 7, triage auto-suggests `emergency`. Enter normal vitals -> NEWS2 score 0-4, triage auto-suggests `non_urgent`. Enter weight and height -> BMI auto-calculated. Patient age 3, enter MUAC = 11.0 cm -> Z-score flagged as malnutrition risk.

---

#### FR-OPD-002: Doctor's Queue

**Stimulus:** A doctor opens the OPD queue screen, or a triaged patient is assigned to a doctor.

**Response:** The system shall display a real-time queue for the logged-in doctor showing: patient name, MRN, triage level (colour-coded: red = emergency, orange = urgent, yellow = semi-urgent, green = non-urgent), wait time since triage, and chief complaint (if entered at triage). The queue is sorted by triage priority then by arrival time. Emergency patients jump to the top of the queue (BR-CLIN-001). Queue count badge is visible on the doctor's navigation bar.

**Business rules:** BR-CLIN-001.
**Priority:** High
**Phase:** 1
**Verifiability:** Triage 5 patients with varying priority levels. Open doctor's queue -> patients displayed in priority order. Add an emergency patient -> patient appears at position 1 immediately. Doctor completes a consultation -> patient removed from queue. Wait time displays correctly relative to triage timestamp.

---

#### FR-OPD-003: SOAP Clinical Consultation

**Stimulus:** A Doctor or Clinical Officer selects a patient from their queue and opens the consultation screen.

**Response:** The system shall display a clinical workspace with:
1. **Patient summary banner:** name, MRN, age, sex, photo, allergies (red alert), chronic conditions, blood group, patient category.
2. **Current vitals** from triage (FR-OPD-001).
3. **SOAP form:**
   - **S (Subjective):** Free-text chief complaint and history of presenting illness. Previous visit notes are visible in a collapsible sidebar.
   - **O (Objective):** Examination findings with structured templates (body system checklists) and free-text. Additional vital signs may be recorded.
   - **A (Assessment):** ICD-10/ICD-11 diagnosis entry (FR-OPD-004). Multiple diagnoses allowed, one must be marked primary.
   - **P (Plan):** Investigation requests (FR-OPD-005), prescriptions (FR-OPD-006), procedures (FR-OPD-009), referrals (FR-OPD-010), follow-up (FR-OPD-011), and disposition (admit, discharge, refer).
4. All form fields auto-save to local storage at configurable intervals (BR-DATA-005).

**Business rules:** BR-DATA-005, BR-DATA-006.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Open consultation for a patient with allergy `Penicillin` -> red allergy banner visible. Enter SOAP notes, close browser without saving -> re-open browser, navigate to same patient -> auto-saved data recovered. Complete SOAP and submit -> visit record persisted, patient removed from queue.

---

#### FR-OPD-004: ICD-10/ICD-11 Diagnosis Entry

**Stimulus:** A clinician types in the Assessment section of the SOAP form or a dedicated diagnosis field.

**Response:** The system shall provide a searchable ICD-10/ICD-11 lookup that:
1. Supports search by code (e.g., `B50`) and by clinical description (e.g., `malaria`).
2. Maps common local terms to ICD codes (e.g., "red weepy eyes" -> `H10.1 Acute atopic conjunctivitis`).
3. Auto-suggests diagnoses based on entered symptoms and the patient's demographic (age, sex).
4. Returns results within 200 ms at P95.
5. Stores the diagnosis with both the ICD code and the clinician's free-text description.
6. Free-text-only diagnosis entry is not permitted (BR-DATA-006).

**Business rules:** BR-DATA-006, BR-HMIS-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Type `malaria` -> ICD-10 code `B50` and variants appear. Select `B50.9 Plasmodium falciparum malaria, unspecified`. Attempt to save a diagnosis without an ICD code -> HTTP 422 `ICD_CODE_REQUIRED`. Diagnosis auto-tallies to HMIS 105 Section 1 by age group and sex.

---

#### FR-OPD-005: Investigation Requests (Lab, Radiology)

**Stimulus:** A clinician submits investigation orders from the Plan section of the SOAP form.

**Response:** The system shall:
1. Accept one or more investigation requests per visit. Each request specifies: test/examination name (from the facility's test catalogue), clinical indication, and urgency (routine, urgent, emergency).
2. On submission, create records in the lab or radiology request queue immediately.
3. Send a real-time notification (WebSocket push or in-app notification) to the Lab Technician or Radiographer.
4. Auto-generate a billing charge for each requested investigation (BR-FIN-001).
5. Emergency-priority requests jump to the top of the lab/radiology queue (BR-CLIN-001).

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `test_id` | integer | Must exist in facility test catalogue |
| `clinical_indication` | string | Optional free text |
| `urgency` | enum | `routine`, `urgent`, `emergency` |
| `specimen_type` | enum | For lab: `blood`, `urine`, `stool`, `sputum`, `csf`, `swab`, `other` |

**Business rules:** BR-FIN-001, BR-CLIN-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Order a CBC with urgency `emergency` -> lab queue shows the request at position 1. Billing account shows a charge for CBC. Lab technician receives notification within 5 seconds.

---

#### FR-OPD-006: Prescription Writing

**Stimulus:** A Doctor or Clinical Officer adds medications in the Plan section of the SOAP form.

**Response:** The system shall:
1. Present a drug search interface querying the facility formulary. Search by generic name, brand name, or drug code.
2. For each drug, capture: drug name, dose, dose unit, frequency, duration, route, and calculated quantity.
3. Display current pharmacy stock for each drug (FR-OPD-007, BR-RX-002).
4. Execute drug interaction checking against all active medications (FR-OPD-008, BR-CLIN-004).
5. For paediatric patients, enforce weight-based dosing (FR-PHR-014, BR-CLIN-006).
6. Validate Five Rights (FR-OPD-015, BR-CLIN-008) before submission.
7. On submission, create prescription records and push to the pharmacy queue (FR-PHR-001).
8. Auto-generate a billing charge for each prescribed medication (BR-FIN-001).

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `drug_id` | integer | Must exist in facility formulary |
| `dose` | decimal | > 0 |
| `dose_unit` | enum | `mg`, `ml`, `g`, `mcg`, `IU`, `units` |
| `frequency` | enum | `od`, `bd`, `tds`, `qid`, `stat`, `prn`, `nocte`, `mane` |
| `duration` | integer | Days, > 0 |
| `route` | enum | `oral`, `iv`, `im`, `sc`, `topical`, `rectal`, `inhaled`, `sublingual`, `ophthalmic`, `otic` |
| `quantity` | integer | Auto-calculated from dose x frequency x duration, overridable |
| `instructions` | string | Optional, max 500 chars |

**Business rules:** BR-CLIN-002, BR-CLIN-004, BR-CLIN-006, BR-CLIN-008, BR-RX-002, BR-FIN-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Prescribe Amoxicillin 500 mg TDS x 7 days -> quantity auto-calculated as 21 capsules. Stock level displayed beside the drug. Prescription appears in pharmacy queue within 5 seconds. Billing charge posted to patient account.

---

#### FR-OPD-007: Stock-Aware Prescribing

**Stimulus:** A clinician searches for a drug in the prescription form (FR-OPD-006).

**Response:** The system shall display the current pharmacy stock level for each drug alongside the search results. If stock for a prescribed drug is zero, the system shall:
1. Display a warning: "Out of stock. Available alternatives: [list]".
2. Suggest available therapeutic alternatives from the same drug class.
3. Allow the clinician to proceed with the out-of-stock prescription (for external pharmacy fill) or switch to an alternative.

**Business rules:** BR-RX-002.
**Priority:** High
**Phase:** 1
**Verifiability:** Set Amoxicillin stock to 0. Prescribe Amoxicillin -> warning displayed with alternatives (e.g., Ampicillin). Set Amoxicillin stock to 10. Prescribe 21 capsules -> warning: "Insufficient stock (10 available)".

---

#### FR-OPD-008: Drug Interaction Checking

**Stimulus:** A clinician adds a drug to the prescription (FR-OPD-006) while the patient has active medications (current prescription or historical active medications).

**Response:** The system shall check the new drug against all active medications using the drug interaction database and apply the four-tier alert classification:
1. **Tier 1 (Info):** Displayed passively in the prescription sidebar. No action required.
2. **Tier 2 (Warning):** Displayed prominently with an amber banner. Clinician may proceed without override.
3. **Tier 3 (Serious):** Modal alert blocks the workflow. Clinician must provide a documented override reason to proceed. Override logged with clinician ID, timestamp, and reason.
4. **Tier 4 (Fatal):** Hard stop. Prescription cannot proceed. A pharmacist must intervene and resolve the interaction before the prescription is accepted.

**Business rules:** BR-CLIN-004.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Patient on Warfarin. Prescribe Aspirin -> Tier 3 (Serious) modal appears, clinician must enter override reason. Prescribe Methotrexate with Trimethoprim -> Tier 4 (Fatal) hard stop, clinician cannot override, pharmacist intervention required. All Tier 3 and Tier 4 events recorded in audit trail with clinician ID and reason.

---

#### FR-OPD-009: Procedure Recording

**Stimulus:** A clinician records a minor OPD procedure in the Plan section of the SOAP form.

**Response:** The system shall capture: procedure name (from procedure catalogue), procedure date, clinical indication, findings, complications (if any), and materials used. Auto-generate a billing charge for the procedure (BR-FIN-001). The procedure is recorded against the visit and visible in clinical history.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `procedure_id` | integer | Must exist in procedure catalogue |
| `indication` | string | Required, max 500 chars |
| `findings` | string | Optional, max 1000 chars |
| `complications` | string | Optional, max 500 chars |
| `materials` | array | Optional, list of items used |

**Business rules:** BR-FIN-001.
**Priority:** Medium
**Phase:** 1
**Verifiability:** Record a wound suturing procedure -> billing charge posted. Procedure visible in patient's clinical history with indication and findings.

---

#### FR-OPD-010: Referral Generation

**Stimulus:** A clinician initiates a referral from the Plan section of the SOAP form.

**Response:** The system shall:
1. Capture referral type: internal (to another department within the facility), external (to another facility), or self-referral.
2. For external referrals, capture the destination facility (from a facility registry) and the referring reason.
3. Generate an electronic referral letter containing: patient demographics, clinical summary, diagnosis, current medications, investigation results, and reason for referral.
4. The referral letter is printable and exportable as PDF.
5. Internal referrals add the patient to the destination department's queue.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `referral_type` | enum | `internal`, `external` |
| `destination_department` | string | Required for internal referrals |
| `destination_facility` | string | Required for external referrals |
| `reason` | string | Required, max 1000 chars |
| `urgency` | enum | `routine`, `urgent`, `emergency` |
| `clinical_summary` | string | Auto-populated from current visit, editable |

**Business rules:** BR-CLIN-005 (medication reconciliation at facility-to-facility referral).
**Priority:** High
**Phase:** 1
**Verifiability:** Create an internal referral to Lab -> patient appears in lab queue. Create an external referral -> referral letter generated with diagnosis, medications, and lab results. Print referral letter -> formatted PDF with facility letterhead.

---

#### FR-OPD-011: Follow-Up Appointment Booking from Consultation

**Stimulus:** A clinician specifies a follow-up date in the Plan section of the SOAP form.

**Response:** The system shall create an appointment record for the patient with the specified date, department, and doctor (defaulting to the current clinician). The appointment integrates with the scheduling module (FR-APT-001). An SMS/WhatsApp reminder is scheduled for 24 hours before the appointment (FR-APT-002).

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `follow_up_date` | date | Must be in the future |
| `department` | string | Defaults to current department |
| `doctor_id` | integer | Defaults to current clinician |
| `notes` | string | Optional, max 500 chars |

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Set follow-up for 14 days from today -> appointment created. Patient receives SMS reminder 24 hours before the appointment date.

---

#### FR-OPD-012: Clinical Notes History

**Stimulus:** A clinician opens the patient's visit history from the consultation screen or patient profile.

**Response:** The system shall display the complete chronological visit history in a single scrollable screen, including: visit date, clinician, department, SOAP notes, diagnoses (ICD-10 coded), prescriptions, investigation results, procedures, and referrals. Each visit is collapsible/expandable. Filter options: by date range, by department, by clinician. The display loads within 1 second for patients with up to 100 visits.

**Business rules:** BR-DATA-004 (only visits within the current facility unless emergency access is granted).
**Priority:** High
**Phase:** 1
**Verifiability:** Patient with 50 visits -> all 50 displayed in chronological order. Filter by date range -> only matching visits shown. Load time < 1 second for 100 visits.

---

#### FR-OPD-013: Discharge / End of Visit

**Stimulus:** A clinician marks a visit as complete by selecting a disposition: `discharged`, `admitted` (triggers FR-IPD admission in Phase 2), `referred`, or `left_without_being_seen`.

**Response:** The system shall:
1. Record the disposition and timestamp.
2. If `discharged`: verify all pending orders are resolved (prescriptions sent to pharmacy, lab results received or acknowledged as pending). Generate a visit summary printable for the patient.
3. If `referred`: ensure a referral record exists (FR-OPD-010).
4. Remove the patient from all active queues (OPD, lab, pharmacy).
5. Auto-billing is finalised for the visit (BR-FIN-001).

**Business rules:** BR-FIN-001.
**Priority:** High
**Phase:** 1
**Verifiability:** Discharge a patient -> removed from all queues. Visit summary available for printing. All charges finalised in billing. Attempt to discharge with unresolved lab orders -> warning displayed.

---

#### FR-OPD-014: Early Warning Score Calculation (NEWS2)

**Stimulus:** Vital signs are entered for a patient during triage (FR-OPD-001) or ward round.

**Response:** The system shall automatically calculate the NEWS2 (National Early Warning Score 2) from the entered vital signs:
- Score 0-4: Routine monitoring. No alert.
- Score 5-6: Increase monitoring frequency. Notify the responsible doctor via in-app notification.
- Score 7+: Immediate clinical review required. Red alert on the patient's record. Page the responsible doctor and ward sister. Suggest ICU transfer consideration.

Population-adjusted thresholds for Sub-Saharan Africa baselines are applied where clinically validated (e.g., adjusted SpO2 thresholds for altitude).

**Business rules:** BR-CLIN-007.
**Priority:** High
**Phase:** 1
**Verifiability:** Enter vitals: RR=25, SpO2=91%, systolic BP=90, pulse=130, temp=39.5, consciousness=confused -> NEWS2 >= 7, red alert triggered, doctor notified. Enter normal vitals -> NEWS2 = 0, no alert.

---

#### FR-OPD-015: Five Rights CPOE Enforcement

**Stimulus:** A clinician submits a prescription via the CPOE (Computerised Physician Order Entry) system (FR-OPD-006).

**Response:** The system shall validate all Five Rights before accepting the prescription:
1. **Right Patient:** Patient ID confirmed at the point of entry (patient banner matches the consultation context).
2. **Right Drug:** Drug selected from the facility formulary (free-text drug entry is not permitted).
3. **Right Dose:** Dose is within the therapeutic range for the drug and patient weight. For paediatric patients, dose calculated as mg/kg with adult ceiling dose cap (BR-CLIN-006).
4. **Right Route:** Administration route is valid for the selected drug.
5. **Right Time:** Frequency schedule is clinically appropriate for the drug.

Failure of any right blocks prescription submission with a specific error message identifying the failed check.

**Business rules:** BR-CLIN-008, BR-CLIN-006.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Prescribe Amoxicillin 5000 mg (exceeds max dose) -> blocked with `DOSE_EXCEEDS_MAXIMUM`. Prescribe IV Metformin (invalid route for oral-only drug) -> blocked with `INVALID_ROUTE`. Prescribe Paracetamol for a child without weight on file -> blocked with `WEIGHT_REQUIRED` (BR-CLIN-006).

---

### FR-LAB: Laboratory Information System

#### FR-LAB-001: Lab Request from Clinical Screens

**Stimulus:** A clinician submits a lab investigation request from OPD (FR-OPD-005), IPD, or Emergency.

**Response:** The system shall:
1. Create a lab request record with status `requested`, linked to the patient visit, requesting clinician, and facility.
2. Assign a unique Lab Accession Number (LAN) to the request.
3. Add the request to the laboratory queue, sorted by urgency (emergency > urgent > routine) then by request time.
4. Notify the Lab Technician via real-time notification.
5. Post a billing charge for each requested test (BR-FIN-001).

**Business rules:** BR-FIN-001, BR-CLIN-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Clinician orders CBC and Malaria RDT -> two lab queue entries created, Lab Technician notified, billing charges posted. Emergency request -> appears at top of lab queue.

---

#### FR-LAB-002: Sample Collection with Barcode/QR Generation

**Stimulus:** A Lab Technician selects a pending lab request and initiates sample collection.

**Response:** The system shall:
1. Update the request status from `requested` to `collected`.
2. Generate a unique barcode or QR code label for the specimen. The label includes: patient name, MRN, LAN, test name, collection date/time, and specimen type.
3. The label is printable on standard lab label stock (25 mm x 50 mm).
4. Record the collecting technician, collection timestamp, and specimen type.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Collect a sample for a CBC request -> status changes to `collected`, barcode label generated. Print the label -> label contains patient name, MRN, and test name. Scan the barcode -> returns the correct lab request.

---

#### FR-LAB-003: Specimen Tracking

**Stimulus:** A specimen moves through the laboratory workflow stages.

**Response:** The system shall track each specimen through 5 status transitions: `requested` -> `collected` -> `received` (at the lab bench) -> `processing` -> `result_ready`. Each transition records the timestamp and the user who performed the action. Turnaround time (TAT) is calculated as the duration from `requested` to `result_ready`.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Collect a sample at 09:00, receive at lab at 09:15, start processing at 09:30, result ready at 10:00 -> TAT = 60 minutes. Specimen tracking screen shows all 5 statuses with timestamps.

---

#### FR-LAB-004: Result Entry with Reference Ranges and Abnormal Flagging

**Stimulus:** A Lab Technician enters results for a collected specimen.

**Response:** The system shall:
1. Display the test panel with expected parameters and reference ranges (age- and sex-specific where applicable).
2. Accept numeric or coded results per parameter.
3. Auto-flag results outside the reference range: `H` (high), `L` (low), `HH` (critically high), `LL` (critically low).
4. Critical values (HH/LL) trigger the critical value alert (FR-LAB-005).
5. Update the request status to `result_ready` (pending validation).
6. Notify the requesting clinician that results are available.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `parameter_id` | integer | From test definition |
| `value` | decimal or string | Numeric for quantitative, coded for qualitative |
| `unit` | string | Must match parameter definition |
| `comment` | string | Optional, max 500 chars |

**Business rules:** BR-CLIN-003 (critical value thresholds).
**Priority:** Critical
**Phase:** 1
**Verifiability:** Enter potassium = 7.0 mmol/L (reference: 3.5-5.0) -> flagged `HH`, critical value alert triggered. Enter haemoglobin = 14.0 g/dL for an adult male (reference: 13.0-17.0) -> no flag. Enter WBC = 2.0 x10^9/L (reference: 4.0-11.0) -> flagged `L`.

---

#### FR-LAB-005: Critical Value Alerts with Escalation

**Stimulus:** A lab result exceeds a panic threshold (FR-LAB-004 flags `HH` or `LL`).

**Response:** The system shall execute a timed escalation cascade:
1. **Immediate:** Send a push notification and in-app alert to the requesting clinician with the critical value, test name, and patient identifier.
2. **30 minutes:** If the clinician has not acknowledged the alert, escalate to the ward sister (or department head for OPD).
3. **60 minutes:** If still unacknowledged, escalate to the Facility Admin.
4. All escalation steps are timestamped in the audit trail.
5. The alert remains active until acknowledged by a clinician.

**Business rules:** BR-CLIN-003.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Enter critical potassium result (> 6.5 mmol/L) -> requesting doctor receives notification immediately. Wait 30 minutes without acknowledgement -> ward sister receives escalation. Wait 60 minutes -> Facility Admin receives escalation. Doctor acknowledges -> alert cleared, acknowledgement timestamped.

---

#### FR-LAB-006: Result Validation by Lab Supervisor

**Stimulus:** A Lab Supervisor reviews results entered by a Lab Technician.

**Response:** The system shall require a two-step validation process:
1. Lab Technician enters the result (FR-LAB-004) -> status = `result_ready_pending_validation`.
2. Lab Supervisor reviews and either approves (status = `validated`) or rejects with a reason (status = `rejected`, returned to technician).
3. Only validated results are visible to clinicians. Pending results show as "Awaiting validation" on clinical screens.
4. The validating supervisor's identity and timestamp are recorded.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Technician enters result -> clinician sees "Awaiting validation". Supervisor approves -> clinician sees the result value. Supervisor rejects with reason "QC out of range" -> technician receives the rejection and must re-enter.

---

#### FR-LAB-007: Quality Control Records and Levey-Jennings Charts

**Stimulus:** A Lab Technician records daily QC results for an analyser/assay.

**Response:** The system shall:
1. Accept QC sample results (level 1 normal, level 2 abnormal) per assay per day.
2. Plot results on a Levey-Jennings chart showing the mean, +/- 1 SD, +/- 2 SD, and +/- 3 SD lines.
3. Apply Westgard rules (1-2s warning, 1-3s reject, 2-2s, R-4s, 4-1s, 10x) to flag out-of-control assays.
4. An out-of-control flag blocks result entry for that assay until the QC issue is resolved and documented.

**Business rules:** None.
**Priority:** Medium
**Phase:** 1
**Verifiability:** Enter QC result 3.1 SD above mean -> 1-3s rule violated, assay flagged out-of-control. Attempt to enter patient results for that assay -> blocked with `QC_OUT_OF_CONTROL`. Resolve QC, enter acceptable result -> patient result entry re-enabled.

---

#### FR-LAB-008: HL7 v2 Analyser Interface

**Stimulus:** A laboratory analyser sends an ORM (Order Request Message) or ORU (Observation Result Unsolicited) message via the HL7 v2.x interface.

**Response:** The system shall:
1. Accept inbound ORU messages containing test results from connected analysers (Cobas, Mindray, Sysmex).
2. Parse the HL7 message, extract patient identifier and result values, and match to the corresponding lab request using the Lab Accession Number (LAN).
3. Auto-populate the result entry form with analyser values.
4. If no matching LAN is found, queue the result for manual matching.
5. Send outbound ORM messages to the analyser when a new lab request is created (if the analyser supports bidirectional communication).

**Business rules:** None.
**Priority:** Medium
**Phase:** 1
**Verifiability:** Send a valid ORU message with LAN `LAB-2026-0001` -> result auto-populated against the matching request. Send an ORU with an unknown LAN -> queued for manual matching. Configure a bidirectional analyser -> new lab request triggers an ORM message to the analyser.

---

#### FR-LAB-009: External Lab Referral

**Stimulus:** A Lab Technician or clinician marks a test for external referral (e.g., to Lancet Laboratories or Central Public Health Laboratories).

**Response:** The system shall:
1. Update the request status to `referred_external`.
2. Record the external lab name, referral date, and expected turnaround time.
3. Generate a printable referral form with patient details, requested tests, and clinical indication.
4. Track the referred specimen until results are received and entered manually.
5. Auto-calculate the external lab TAT separately from internal TAT.

**Business rules:** None.
**Priority:** Medium
**Phase:** 1
**Verifiability:** Refer a GeneXpert TB test to CPHL -> status = `referred_external`, referral form generated. Enter the external result 5 days later -> result linked to original request, external TAT = 5 days.

---

#### FR-LAB-010: LOINC-Coded Test Definitions

**Stimulus:** A Facility Admin or Lab Supervisor creates or imports test definitions into the facility's test catalogue.

**Response:** The system shall store each test definition with: test name, LOINC code, specimen type, method, reference ranges (age- and sex-stratified), unit of measurement, and turnaround time target. LOINC coding enables interoperability with external systems and standardises test identification across facilities.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `test_name` | string | Required, max 200 chars |
| `loinc_code` | string | Valid LOINC code, recommended |
| `specimen_type` | enum | `blood`, `urine`, `stool`, `sputum`, `csf`, `swab`, `other` |
| `parameters` | array | At least 1 parameter with name, unit, and reference range |
| `tat_target_hours` | integer | Target turnaround time in hours |

**Business rules:** None.
**Priority:** Medium
**Phase:** 1
**Verifiability:** Create a test "Full Blood Count" with LOINC code `58410-2` and 5 parameters (WBC, RBC, Hb, Plt, Hct) with reference ranges. Order the test for a patient -> result entry form shows all 5 parameters with reference ranges.

---

### FR-PHR: Pharmacy and Dispensary

#### FR-PHR-001: Prescription Queue

**Stimulus:** A clinician submits a prescription from OPD, IPD, or Emergency (FR-OPD-006).

**Response:** The system shall add the prescription to the pharmacy queue in real time. The queue displays: patient name, MRN, prescribing clinician, number of items, urgency, and time since prescription. The queue is sorted by urgency (emergency > urgent > routine) then by prescription time. A notification badge shows the queue count on the pharmacist's navigation bar.

**Business rules:** BR-CLIN-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Clinician submits a prescription -> appears in pharmacy queue within 5 seconds. Emergency prescription -> appears at top of queue. Pharmacist can see all pending prescriptions with item count.

---

#### FR-PHR-002: Dispensing with Automatic Stock Deduction

**Stimulus:** A Pharmacist selects a prescription from the queue and initiates dispensing.

**Response:** The system shall:
1. Display the prescription details: drug name, dose, frequency, duration, quantity, route, and any special instructions.
2. On dispensing confirmation, deduct the dispensed quantity from the pharmacy stock.
3. Update the prescription status to `dispensed`.
4. Record the dispensing pharmacist, timestamp, batch number, and expiry date of the dispensed stock.
5. Apply FIFO (First In, First Out) stock deduction by default -- the oldest batch (nearest expiry) is deducted first.

**Business rules:** BR-FIN-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Stock = 100 Amoxicillin capsules. Dispense 21 -> stock = 79. Dispensing record shows pharmacist name, batch, and expiry. FIFO applied: batch with nearest expiry deducted first.

---

#### FR-PHR-003: Generic/Brand Substitution with Doctor Notification

**Stimulus:** A Pharmacist selects a branded drug prescription where the branded drug is unavailable but a generic equivalent is in stock.

**Response:** The system shall:
1. Suggest the generic equivalent with stock availability.
2. On pharmacist confirmation, substitute the brand with the generic.
3. Send a notification to the prescribing doctor: "Prescription for [Brand] substituted with [Generic] for patient [Name] by [Pharmacist]. Reason: branded drug out of stock."
4. Log the substitution in the prescription record with the substitution reason and notified doctor.

**Business rules:** BR-CLIN-002.
**Priority:** High
**Phase:** 1
**Verifiability:** Prescribe Augmentin (brand). Set Augmentin stock to 0, Amoxicillin/Clavulanate (generic) stock > 0. Pharmacist substitutes -> doctor receives notification. Prescription record shows: original = Augmentin, dispensed = Amoxicillin/Clavulanate, reason = "Brand out of stock".

---

#### FR-PHR-004: Dispensing Label Generation

**Stimulus:** A Pharmacist dispenses a medication (FR-PHR-002).

**Response:** The system shall generate a printable dispensing label containing: patient name, drug name, dose, frequency, duration, route, quantity dispensed, "Take as directed" instructions, facility name, dispensing date, and pharmacist name. Label format is configurable per facility. Labels are printable on standard pharmacy label stock.

**Business rules:** None.
**Priority:** Medium
**Phase:** 1
**Verifiability:** Dispense Amoxicillin 500 mg TDS x 7 days -> label generated with all required fields. Print label -> formatted for pharmacy label stock.

---

#### FR-PHR-005: Partial Dispensing with Pending Balance

**Stimulus:** A Pharmacist has insufficient stock to fulfil the full prescribed quantity.

**Response:** The system shall:
1. Allow the pharmacist to dispense a partial quantity.
2. Record the dispensed quantity and the pending balance (prescribed minus dispensed).
3. Create a pending balance record visible in the pharmacy queue for future fulfilment.
4. Notify the prescribing clinician of the partial dispensing.
5. When stock is replenished, the pending balance appears as a priority item in the pharmacy queue.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Prescribe 21 Amoxicillin. Stock = 10. Dispense 10 -> pending balance = 11. Receive new stock -> pending balance item appears in pharmacy queue. Dispense remaining 11 -> pending balance cleared.

---

#### FR-PHR-006: Inpatient Drug Round Tracking

**Stimulus:** A Nurse administers a scheduled medication to an inpatient during a drug round.

**Response:** The system shall record each administration event with status: `given` (with timestamp and administering nurse), `held` (with reason), `refused` (with reason and patient/guardian signature if available), or `not_given` (with reason). The Medication Administration Record (MAR) displays all scheduled doses for the ward, colour-coded by status.

**Business rules:** BR-CLIN-002 (nurses administer, do not prescribe).
**Priority:** High
**Phase:** 1
**Verifiability:** Schedule Amoxicillin TDS for an inpatient. Nurse marks 08:00 dose as `given` -> recorded with nurse ID and timestamp. Nurse marks 14:00 dose as `held` with reason "Patient vomiting" -> recorded. MAR shows: 08:00 green (given), 14:00 yellow (held), 20:00 grey (pending).

---

#### FR-PHR-007: Stock Management (GRN, Transfer, Adjust, Return)

**Stimulus:** A Pharmacist or Store Keeper performs a stock operation.

**Response:** The system shall support four stock operations:
1. **Goods Received Note (GRN):** Record incoming stock with supplier, invoice number, batch number, expiry date, quantity, and unit cost. Stock balance increases.
2. **Transfer:** Move stock between stores (e.g., main pharmacy to ward pharmacy). Source store decreases, destination store increases. Receiving store must acknowledge receipt.
3. **Adjustment:** Correct stock discrepancies with a documented reason (breakage, expiry, theft, count correction). Approval required for adjustments exceeding a configurable threshold.
4. **Return:** Return stock to supplier with reason (defective, recalled, near-expiry). Stock balance decreases.

All operations are recorded in the stock movement ledger with user, timestamp, and reason.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** GRN 500 Paracetamol -> stock increases by 500. Transfer 100 to ward pharmacy -> main stock = 400, ward stock += 100. Adjust -5 with reason "breakage" -> stock = 395, audit trail shows adjustment. Return 50 to supplier -> stock = 345.

---

#### FR-PHR-008: Expiry Tracking with 90-Day Alert

**Stimulus:** The system runs a daily scheduled job to check stock expiry dates.

**Response:** The system shall:
1. Flag all stock items with expiry dates within 90 days as `expiring_soon`.
2. Flag all stock items past their expiry date as `expired`.
3. Generate a daily expiry alert report for the Pharmacist and Store Keeper.
4. Expired stock is blocked from dispensing. Attempting to dispense an expired batch returns an error.
5. Expiring-soon items are highlighted in yellow on the dispensing screen.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Add a batch expiring in 60 days -> flagged `expiring_soon`, appears on daily report. Add a batch expired yesterday -> flagged `expired`. Attempt to dispense the expired batch -> blocked with `BATCH_EXPIRED`.

---

#### FR-PHR-009: Minimum Stock Level Alerts

**Stimulus:** Stock for any drug falls below the configured minimum stock level.

**Response:** The system shall:
1. Generate an in-app notification to the Pharmacist and Facility Admin.
2. Add the item to the reorder list with current stock, minimum level, and suggested reorder quantity.
3. The alert persists until stock is replenished above the minimum level.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Set minimum stock for Amoxicillin = 50. Current stock = 45 -> alert generated, item appears on reorder list. Receive GRN for 100 Amoxicillin -> stock = 145, alert cleared.

---

#### FR-PHR-010: Drug Formulary Management

**Stimulus:** A Pharmacist or Facility Admin creates, updates, or deactivates drugs in the facility formulary.

**Response:** The system shall maintain a facility-level formulary containing: drug name (generic), brand names, ATC code, drug class, dosage forms, strengths, default dose, maximum dose, routes, contraindications, interaction profile, and LASA (Look-Alike/Sound-Alike) flag. Only drugs in the active formulary can be prescribed (FR-OPD-006). The formulary can be pre-loaded from a national Essential Medicines List.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `generic_name` | string | Required, max 200 chars |
| `brand_names` | array | Optional |
| `atc_code` | string | ATC classification code |
| `drug_class` | string | e.g., "Penicillins", "NSAIDs" |
| `dosage_forms` | array | e.g., `["tablet", "capsule", "suspension"]` |
| `strengths` | array | e.g., `["250mg", "500mg"]` |
| `routes` | array | Valid administration routes |
| `max_dose` | decimal | Maximum single dose |
| `lasa_flag` | boolean | If true, Tall Man Lettering applies (FR-PHR-013) |

**Business rules:** BR-CLIN-008.
**Priority:** High
**Phase:** 1
**Verifiability:** Add Amoxicillin to formulary. Prescribe Amoxicillin -> succeeds. Deactivate Amoxicillin. Prescribe Amoxicillin -> blocked with `DRUG_NOT_IN_FORMULARY`.

---

#### FR-PHR-011: Narcotic/Controlled Drug Register

**Stimulus:** A Pharmacist dispenses a controlled substance (Schedule I-V).

**Response:** The system shall create a narcotic register entry containing: patient name, drug name and strength, quantity dispensed, prescribing doctor, dispensing pharmacist, witness name, date/time, and running balance. A discrepancy between the physical count and the system balance triggers an immediate alert to the Facility Admin.

**Business rules:** BR-RX-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Dispense 10 tablets of Morphine -> narcotic register entry created with running balance = previous - 10. Enter physical count 2 less than system balance -> discrepancy alert sent to Facility Admin. Register entries are immutable (cannot be edited or deleted).

---

#### FR-PHR-012: Pharmacy Revenue Auto-Billing

**Stimulus:** A medication is dispensed (FR-PHR-002).

**Response:** The system shall automatically post a billing charge to the patient's account for the dispensed medication. The charge is calculated from the facility price list based on the drug, strength, and quantity dispensed. Partial dispensing generates a proportional charge.

**Business rules:** BR-FIN-001.
**Priority:** High
**Phase:** 1
**Verifiability:** Dispense 21 Amoxicillin 500 mg at UGX 500 per capsule -> billing charge of UGX 10,500 posted to patient account. Partial dispense 10 -> billing charge = UGX 5,000.

---

#### FR-PHR-013: Tall Man Lettering Display

**Stimulus:** A clinician or pharmacist views a drug name flagged as LASA (Look-Alike/Sound-Alike) in any drug selection interface.

**Response:** The system shall display the differentiating letters in uppercase to reduce selection errors. Example: `hydrOXYzine` vs `hydrALAZINE`, `predniSONE` vs `prednisoLONE`. The LASA drug list is maintainable by the pharmacy lead via the formulary management screen (FR-PHR-010).

**Business rules:** BR-RX-003.
**Priority:** High
**Phase:** 1
**Verifiability:** Flag Hydroxyzine and Hydralazine as LASA pair. Open the drug search -> `hydrOXYzine` and `hydrALAZINE` displayed with Tall Man Lettering. Unflag -> normal display.

---

#### FR-PHR-014: Weight-Based Paediatric Dosing

**Stimulus:** A clinician prescribes a medication for a patient under 12 years (FR-OPD-006).

**Response:** The system shall:
1. Require a weight on file within 24 hours. If no weight is on file, block prescription submission with `WEIGHT_REQUIRED`.
2. Calculate the dose from the patient's recorded weight using mg/kg dosing.
3. Apply the adult ceiling dose cap (the calculated dose must not exceed the standard adult dose).
4. Flag any calculated dose that exceeds 10x the expected dose as a potential decimal error.
5. Display the calculated dose alongside the manually entered dose for clinician verification.

**Business rules:** BR-CLIN-006.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Patient weight = 20 kg. Prescribe Amoxicillin at 25 mg/kg -> calculated dose = 500 mg. Enter 5000 mg -> flagged as potential decimal error (10x). Patient weight = 60 kg, prescribed dose would exceed adult max -> adult ceiling dose applied. No weight on file -> `WEIGHT_REQUIRED` error.

---

#### FR-PHR-015: Medication Reconciliation at Transitions of Care

**Stimulus:** A patient transitions between care settings: OPD to IPD admission, ward-to-ward transfer, IPD to discharge, or facility-to-facility referral.

**Response:** The system shall:
1. Auto-generate a medication reconciliation form listing all active medications with their dosages, frequencies, and routes.
2. The receiving clinician must review and confirm the reconciliation before the transition is finalised.
3. Discrepancies (new medications, discontinued medications, dose changes) are highlighted for explicit clinician review.
4. The reconciliation record is stored in the patient's clinical history.
5. The transition cannot be finalised until medication reconciliation is complete.

**Business rules:** BR-CLIN-005.
**Priority:** High
**Phase:** 1
**Verifiability:** Admit a patient from OPD with 3 active medications -> reconciliation form shows all 3. Clinician confirms -> admission proceeds. Attempt to finalise admission without reconciliation -> blocked with `RECONCILIATION_REQUIRED`. Discharge a patient -> reconciliation form generated with active inpatient medications.

---

### FR-BIL: Billing and Revenue

#### FR-BIL-001: Patient Account with Real-Time Charge Accumulation

**Stimulus:** A clinical action is performed that has a corresponding entry in the facility price list (consultation, lab test, drug dispensed, procedure).

**Response:** The system shall automatically post a billing line to the patient's account in real time. Each billing line records: service description, quantity, unit price, total amount, posting source (module and action), timestamp, and the user who triggered the clinical action. The patient's running balance is updated immediately and visible on the billing screen.

**Business rules:** BR-FIN-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Doctor orders a CBC (UGX 15,000) and prescribes Amoxicillin 21 caps (UGX 10,500) -> patient account shows two billing lines, running balance = UGX 25,500. Pharmacist dispenses -> drug charge already posted (no double billing).

---

#### FR-BIL-002: Configurable Price List per Service Category

**Stimulus:** A Facility Admin creates or updates the facility price list via `POST /api/v1/pricelist` or `PATCH /api/v1/pricelist/{id}`.

**Response:** The system shall maintain a price list organised by service category: consultation, laboratory, radiology, pharmacy, procedures, bed charges, and miscellaneous. Each entry has: service name, service code, base price, and effective date. Price changes take effect from the effective date and do not retroactively alter existing charges.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Set CBC price to UGX 15,000 effective 2026-04-01. Order a CBC on 2026-04-02 -> charge = UGX 15,000. Update price to UGX 20,000 effective 2026-05-01. Order a CBC on 2026-04-15 -> charge = UGX 15,000. Order a CBC on 2026-05-02 -> charge = UGX 20,000.

---

#### FR-BIL-003: Patient Category Pricing

**Stimulus:** A billing charge is posted for a patient with a non-default category (staff, VIP, indigent, refugee).

**Response:** The system shall apply category-specific pricing multipliers or fixed prices as configured per facility. For example: staff = 50% discount, VIP = standard price, indigent = facility-defined reduced rate. The pricing tier is determined by the patient's assigned category (FR-REG-004).

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Configure staff discount = 50%. Post a consultation charge (UGX 20,000) for a staff-category patient -> charge = UGX 10,000. Post the same charge for a standard patient -> charge = UGX 20,000.

---

#### FR-BIL-004: Auto-Billing from Clinical Screens

**Stimulus:** A clinician performs a billable action: OPD consultation, lab request, drug dispensing, procedure recording.

**Response:** The system shall post the corresponding billing charge to the patient account without requiring manual charge entry by the cashier. The billing line is linked to the clinical action record for audit traceability. No manual charge entry is required for standard services listed in the facility price list.

**Business rules:** BR-FIN-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Complete an OPD consultation -> consultation fee posted. Order lab tests -> lab charges posted. Dispense drugs -> drug charges posted. No manual cashier action required for any of these charges.

---

#### FR-BIL-005: Receipt Generation

**Stimulus:** A Cashier confirms a payment and requests a receipt.

**Response:** The system shall generate a receipt containing: facility name, receipt number (sequential, unique), patient name, MRN, date, itemised services with amounts, total amount, amount paid, payment method, change due (for cash), and cashier name. The receipt is printable on thermal receipt paper (80 mm) or A4 paper. A digital copy is stored against the patient account.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Patient pays UGX 25,000 for 2 services -> receipt shows itemised services, total = UGX 25,000, payment method = cash, change = UGX 0. Receipt number is unique. Reprint the receipt -> identical content, marked "REPRINT".

---

#### FR-BIL-006: Cash Payment with Change Calculation

**Stimulus:** A Cashier selects a patient account and initiates a cash payment.

**Response:** The system shall:
1. Display the patient's outstanding balance with itemised charges.
2. Accept the amount tendered by the patient.
3. Calculate and display the change due.
4. On confirmation, record the payment, update the patient balance, and generate a receipt (FR-BIL-005).
5. Support partial payments (patient pays less than the full balance; remaining balance stays outstanding).

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Balance = UGX 25,000. Patient tenders UGX 30,000 -> change = UGX 5,000. Balance after payment = UGX 0. Patient tenders UGX 15,000 (partial) -> balance after payment = UGX 10,000.

---

#### FR-BIL-007: Mobile Money Payment with Auto-Reconciliation

**Stimulus:** A patient initiates payment via MTN MoMo or Airtel Money at the cashier or self-service kiosk.

**Response:** The system shall:
1. Generate a payment request via the MoMo/Airtel Money API with the patient's phone number and the amount.
2. The patient confirms the payment on their phone.
3. On receiving the payment callback, auto-match the payment to the patient account using the transaction reference number.
4. Update the patient balance and generate a receipt.
5. Unmatched payments (callback received but no matching patient account) are posted to a suspense account and flagged for manual matching within 48 hours (BR-FIN-003).
6. Generate a daily unmatched payments report.

**Business rules:** BR-FIN-003.
**Priority:** High
**Phase:** 1
**Verifiability:** Initiate MoMo payment for UGX 25,000 -> patient receives MoMo prompt. Patient confirms -> payment auto-matched, balance updated, receipt generated. Simulate an unmatched callback -> payment posted to suspense, appears on daily report.

---

#### FR-BIL-008: Daily Cashier Reconciliation

**Stimulus:** A Cashier ends their session or the system triggers end-of-day processing.

**Response:** The system shall:
1. Record the session parameters: opening float, collections by payment mode (cash, MTN MoMo, Airtel Money, card), total collections, banking amount, and closing float.
2. Calculate expected totals from recorded transactions.
3. Flag discrepancies exceeding UGX 5,000 for supervisor review with a mandatory explanation.
4. Generate a reconciliation report for the Facility Admin.

**Business rules:** BR-FIN-004.
**Priority:** High
**Phase:** 1
**Verifiability:** Cashier collects UGX 500,000 cash during the session. Enter closing float = UGX 50,000, banking = UGX 440,000 -> discrepancy = UGX 10,000 (exceeds UGX 5,000), flagged for supervisor review. Enter banking = UGX 450,000 -> no discrepancy.

---

#### FR-BIL-009: Missing Charge Detection

**Stimulus:** The system runs a daily automated report at end of business.

**Response:** The system shall compare clinical encounters (OPD visits, lab results received, drugs dispensed, procedures performed) against billing records. Encounters with no corresponding billing charge are flagged for review by the billing officer with: patient name, MRN, encounter type, date, and missing charge details.

**Business rules:** BR-FIN-008.
**Priority:** High
**Phase:** 1
**Verifiability:** Complete an OPD visit and manually delete the billing charge. Run the missing charge report -> the OPD visit appears as a missing charge. All encounters with charges -> no items on the report.

---

#### FR-BIL-010: Credit Management

**Stimulus:** A Facility Admin approves a credit arrangement for a patient, staff member, corporation, or mission/NGO.

**Response:** The system shall:
1. Record the credit arrangement with: debtor name, debtor type (staff, corporate, mission), credit limit, approval date, and approving officer.
2. Allow services to be rendered and billed without immediate payment, up to the credit limit.
3. Generate a monthly credit ageing report with buckets: 0-30 days, 31-60 days, 61-90 days, and 90+ days overdue (BR-FIN-005).
4. Alert the Facility Admin when any credit account reaches 90+ days overdue.

**Business rules:** BR-FIN-005, BR-FIN-006.
**Priority:** High
**Phase:** 1
**Verifiability:** Approve a credit arrangement for Corporation X, limit = UGX 5,000,000. Post charges of UGX 3,000,000 -> accepted. Post charges of UGX 3,000,000 -> blocked: "Credit limit exceeded". Monthly report shows UGX 3,000,000 in the 0-30 day bucket. After 35 days without payment -> moves to 31-60 day bucket.

---

### FR-APT: Appointments and Scheduling

#### FR-APT-001: Appointment Booking

**Stimulus:** A Receptionist, clinician, or patient (via portal/app in Phase 3) submits an appointment booking request.

**Response:** The system shall:
1. Accept the appointment with: patient identifier, department, doctor (optional), preferred date/time, and appointment type (first visit, follow-up, procedure).
2. Check doctor availability (FR-APT-003). If the slot is taken, suggest the next 3 available slots.
3. Create the appointment record with status `booked`.
4. Send an SMS confirmation to the patient's phone number.
5. Schedule an SMS/WhatsApp reminder for 24 hours before the appointment (FR-APT-002).

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `patient_uid` | UUID | Required, valid patient |
| `department` | string | Required |
| `doctor_id` | integer | Optional |
| `appointment_date` | datetime | Must be in the future |
| `appointment_type` | enum | `first_visit`, `follow_up`, `procedure` |

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Book an appointment for tomorrow 10:00 -> appointment created, SMS sent. Book another appointment for the same doctor at 10:00 -> conflict detected, alternative slots suggested.

---

#### FR-APT-002: SMS/WhatsApp Appointment Reminder

**Stimulus:** An appointment is booked (FR-APT-001) and the appointment date is 24 hours away.

**Response:** The system shall send a reminder via SMS (primary) or WhatsApp (if the patient has WhatsApp enabled) containing: patient name, appointment date/time, doctor name, department, and facility name. The message includes a reply option to confirm or cancel.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Book an appointment for 2026-04-05 10:00. On 2026-04-04 10:00, patient receives SMS: "Reminder: Your appointment at [Facility] with Dr [Name] is tomorrow at 10:00 AM. Reply 1 to confirm, 2 to cancel."

---

#### FR-APT-003: Doctor Availability Calendar

**Stimulus:** A user views the appointment booking screen or the doctor's schedule management page.

**Response:** The system shall display a calendar view showing: available slots (green), booked slots (blue), blocked/leave slots (grey), and walk-in windows (yellow). Each doctor's schedule is configurable: working days, start/end times, consultation duration, and maximum appointments per session.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Configure Dr Nakamya: Monday-Friday, 08:00-13:00, 30-minute slots, max 10 patients. View calendar -> 10 green slots per day, Monday-Friday. Book 10 appointments for Monday -> all slots blue, no more bookings accepted for Monday.

---

#### FR-APT-004: Queue Management (Appointment to OPD Queue)

**Stimulus:** A patient with a booked appointment arrives at the facility and checks in at reception.

**Response:** The system shall:
1. The Receptionist marks the appointment as `arrived`.
2. The patient is added to the OPD triage queue (FR-REG-011) with their appointment time preserved as a priority factor.
3. Patients with appointments are interleaved with walk-ins based on their scheduled time and triage priority.

**Business rules:** BR-CLIN-001.
**Priority:** High
**Phase:** 1
**Verifiability:** Patient with 09:00 appointment arrives at 08:55 -> marked `arrived`, added to triage queue. Walk-in patient arrives at 08:50 -> both appear in queue; appointment patient scheduled for 09:00 is not prioritised over a walk-in triaged as `urgent`.

---

#### FR-APT-005: Walk-In Integration

**Stimulus:** A patient arrives without a prior appointment and is registered at reception.

**Response:** The system shall add the patient to the OPD triage queue as a walk-in. Walk-in patients are triaged and queued using the same priority rules as appointment patients (BR-CLIN-001). No appointment record is created; the visit is tracked as a walk-in encounter.

**Business rules:** BR-CLIN-001.
**Priority:** Medium
**Phase:** 1
**Verifiability:** Register a walk-in patient and triage as `non_urgent` -> added to queue after all emergency/urgent patients. Walk-in triaged as `emergency` -> jumps to top of queue.

---

### FR-RBAC: Access Control

#### FR-RBAC-001: Role-Based Permission Resolution

**Stimulus:** An authenticated user attempts to access a module, screen, or API endpoint.

**Response:** The system shall resolve the user's permissions based on their assigned role. The platform supports 18 built-in roles (see stakeholders.md): Super Admin, Facility Admin, Facility Director, Doctor, Clinical Officer, Nurse/Midwife, Pharmacist, Lab Technician, Radiographer, Receptionist, Records Officer, Cashier, Insurance Clerk, Accountant, Store Keeper, Auditor, Patient, and CHW. Each role has a predefined set of module access permissions. Access to a module or endpoint not in the role's permission set returns HTTP 403.

**Business rules:** BR-DATA-004.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Login as Pharmacist -> pharmacy module accessible, HR module returns HTTP 403. Login as Doctor -> OPD accessible, payroll returns HTTP 403. Login as Super Admin -> all modules accessible.

---

#### FR-RBAC-002: Custom Role Creation per Facility

**Stimulus:** A Facility Admin creates a custom role via `POST /api/v1/roles` with a name and a permission set.

**Response:** The system shall create a facility-scoped custom role with the specified permissions. Custom roles cannot exceed the permissions of the Facility Admin role. Users assigned to custom roles inherit the defined permission set. Custom roles are visible only within the creating facility.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `role_name` | string | Required, 2-50 chars, unique per facility |
| `permissions` | array | Array of permission identifiers from the platform permission registry |
| `description` | string | Optional, max 200 chars |

**Business rules:** BR-DATA-004.
**Priority:** High
**Phase:** 1
**Verifiability:** Create custom role "Senior Nurse" with permissions: nursing notes, vital signs, drug administration, triage, but not prescribing. Assign to a user -> user can access triage but not prescription writing.

---

#### FR-RBAC-003: Attribute-Based Access Control for Sensitive Records

**Stimulus:** A clinician attempts to access a patient record flagged as sensitive (HIV status, mental health, sexual health).

**Response:** The system shall enforce ABAC policies layered on top of RBAC. Sensitive record categories are configurable per facility. Access rules: only the treating clinician (who created the record or is listed as the patient's assigned provider) can view sensitive records. Other clinicians within the same facility see the record exists but cannot view its content without explicit patient consent or emergency access (FR-RBAC-006).

**Business rules:** BR-DATA-001, BR-DATA-002.
**Priority:** High
**Phase:** 1
**Verifiability:** Doctor A records an HIV diagnosis for Patient X. Doctor B at the same facility opens Patient X's record -> sees "Sensitive record exists" but cannot view the HIV diagnosis. Doctor A -> can view the full record. Patient provides consent for Doctor B -> Doctor B can view.

---

#### FR-RBAC-004: Session Management (Device-Level)

**Stimulus:** An authenticated user logs in from a new device while an existing session is active.

**Response:** The system shall support concurrent sessions across devices (web and mobile). Each session is tracked with: device type, IP address, last activity timestamp, and login timestamp. The user can view and revoke active sessions from their profile. The Facility Admin can view and revoke all sessions for users within their facility.

**Business rules:** None.
**Priority:** High
**Phase:** 1
**Verifiability:** Login from desktop browser and mobile app simultaneously -> two active sessions listed. Revoke the desktop session from mobile -> desktop session invalidated, next request redirects to login.

---

#### FR-RBAC-005: Immutable Audit Trail

**Stimulus:** Any user performs a create, update, or delete action on clinical or financial data.

**Response:** The system shall write an immutable audit log entry containing: user_id, facility_id, action (CREATE, UPDATE, DELETE, VIEW for sensitive records), resource type, resource ID, old value (for updates), new value, IP address, user agent, and timestamp. Audit log entries cannot be modified or deleted by any user, including Super Admin. The audit log is queryable by Facility Admin and Auditor roles with filters: user, date range, action type, and resource type.

**Business rules:** BR-DATA-004, BR-PID-003, BR-RX-001.
**Priority:** Critical
**Phase:** 1
**Verifiability:** Update a patient's phone number -> audit log entry shows old phone and new phone, with user ID and timestamp. Attempt to delete an audit log entry via direct SQL -> rejected by database trigger. Query audit log for all actions by User X on 2026-04-03 -> returns matching entries.

---

#### FR-RBAC-006: Emergency Access to Cross-Facility Records

**Stimulus:** A clinician invokes emergency access for a patient registered at another facility.

**Response:** The system shall:
1. Require two-factor patient confirmation: patient name and date of birth (BR-DATA-002).
2. On verification, reveal limited clinical data: allergies, current medications, blood group, HIV status (only if prior consent was given), and the last 3 recorded diagnoses.
3. Log the emergency access: accessing clinician, facility, timestamp, and documented reason.
4. Send an SMS notification to the patient: "Your medical records were accessed at [Facility] on [Date] by [Clinician] for emergency care."
5. Emergency access expires automatically after 24 hours.

**Business rules:** BR-DATA-002, BR-HOPE-001.
**Priority:** High
**Phase:** 1
**Verifiability:** Invoke emergency access with correct name and DOB -> limited clinical data returned. Invoke with incorrect DOB -> access denied. Check patient's phone -> SMS notification received. After 24 hours -> access automatically expires, subsequent requests require re-invocation.

---

#### FR-RBAC-007: Break-the-Glass Access with Mandatory Reason

**Stimulus:** A clinician attempts to access a restricted record (e.g., a VIP patient, a sensitive diagnosis) for which they do not have standard ABAC permission.

**Response:** The system shall:
1. Display a "Break the Glass" confirmation dialog explaining that this access is outside normal permissions and will be audited.
2. Require the clinician to enter a mandatory reason for access (minimum 20 characters).
3. On confirmation, grant temporary read-only access to the restricted record.
4. Log the break-the-glass event with: clinician, patient, timestamp, reason, and duration of access.
5. Notify the Facility Admin of the break-the-glass event.

**Business rules:** BR-DATA-002.
**Priority:** High
**Phase:** 1
**Verifiability:** Doctor attempts to access VIP patient's record without permission -> break-the-glass dialog appears. Enter reason "Emergency consultation for cardiac arrest" -> access granted, Facility Admin notified. Attempt with reason "test" (< 20 chars) -> rejected.

---

### FR-IPD: Inpatient Department (Phase 2)

The Inpatient Department module manages the full admission-to-discharge lifecycle for hospitalised patients.

**Key requirements (to be expanded at Phase 2 start):**

- **Admission:** Patient admission from OPD, emergency, or direct admission with bed assignment, deposit collection (BR-FIN-007), and medication reconciliation (BR-CLIN-005).
- **Bed management:** Visual bed map per ward showing occupied, available, reserved, and under-maintenance beds. Real-time bed census per ward.
- **Nursing documentation:** Shift-by-shift nursing notes with timestamps. Semi-structured templates (coded + free-text). C-HOBIC minimum dataset at admission, shift handover, and discharge.
- **Ward rounds:** Doctor's ward round notes with clinical progress documentation. Investigation ordering and prescription updates from the ward.
- **Drug round:** Medication administration tracking with statuses: ordered, given, held, refused. Barcode Medication Administration (BCMA) for patient-drug verification. MAR display per ward.
- **Vital signs and fluid balance:** Graphical vital signs trending over the admission period. Fluid balance chart (intake vs output). NEWS2 auto-calculation at every vital signs entry (BR-CLIN-007).
- **Transfers:** Ward-to-ward transfer with formal handoff and receiving nurse acknowledgement. Medication reconciliation at transfer (BR-CLIN-005).
- **Discharge:** Discharge documentation completeness enforcement (BR-CLIN-009): diagnosis, summary, medication reconciliation, follow-up plan, billing settlement. Discharge summary auto-generation. DAMA (Discharge Against Medical Advice) recording with patient signature.
- **Census:** Live patient count per ward. Bed occupancy rate calculation for HMIS 108 reporting (BR-HMIS-002).

**Business rules:** BR-CLIN-005, BR-CLIN-007, BR-CLIN-009, BR-FIN-001, BR-FIN-007, BR-HMIS-002.
**Priority:** Critical
**Phase:** 2

---

### FR-MAT: Maternity, ANC, and Reproductive Health (Phase 2)

The Maternity module covers the antenatal, intrapartum, and postnatal care continuum.

**Key requirements (to be expanded at Phase 2 start):**

- **ANC registration:** Record gestational age, expected date of delivery (EDD), gravida, parity. Risk factor assessment at first visit.
- **ANC visits:** Structured recording for ANC1 through ANC8+ per WHO recommendations. Vital signs, fundal height, foetal heart rate, urinalysis, blood tests. Risk reassessment at each visit.
- **Risk assessment:** Flag high-risk pregnancies (previous CS, multiple gestation, pre-eclampsia, HIV-positive, age extremes) for specialist referral.
- **Partograph:** Digital partograph with cervicogram, maternal vitals, foetal heart rate, contractions, and alert/action lines.
- **Delivery record:** Mode of delivery, outcome (live birth, stillbirth), birth weight, APGAR scores at 1 and 5 minutes.
- **Newborn-mother linkage:** Automatic creation of a neonatal patient record linked to the mother's record at birth. Handle temporary names ("Baby of [Mother]") and twin disambiguation.
- **PMTCT:** Prevention of Mother-to-Child Transmission tracking integrated with HIV programme.
- **Postnatal:** PNC1-PNC3 visits with structured assessment templates.
- **Family planning:** Method recording, counselling, follow-up scheduling.

**Business rules:** BR-HMIS-001 (Section 4), BR-CLIN-005.
**Priority:** Critical
**Phase:** 2

---

### FR-IMM: Immunisation (Phase 2)

The Immunisation module tracks vaccine administration per national schedules.

**Key requirements (to be expanded at Phase 2 start):**

- **EPI schedule:** Uganda Expanded Programme on Immunisation schedule pre-loaded with all childhood vaccines. Configurable per country.
- **Vaccine recording:** Date, vaccine name, batch number, dose number, site of administration, administering nurse.
- **Missed dose alerts:** Automated alerts for missed doses with SMS reminders to guardians.
- **Catch-up schedule:** Auto-generated catch-up schedule when doses are missed, per national guidelines.
- **AEFI reporting:** Adverse Event Following Immunisation reporting with severity grading.
- **DHIS2 Tracker:** Upload individual vaccination events to DHIS2 Tracker for national reporting.

**Business rules:** BR-HMIS-001 (Section 6).
**Priority:** High
**Phase:** 2

---

### FR-INS: Insurance Management (Phase 2)

The Insurance module handles scheme registration, claims processing, and receivables tracking.

**Key requirements (to be expanded at Phase 2 start):**

- **Scheme register:** Maintain a catalogue of insurance schemes (NHIS, AAR, Jubilee, Prudential, corporate covers, mission insurance) with benefit schedules and claim formats.
- **Member verification:** Real-time verification of patient's insurance membership and benefit eligibility at registration.
- **Pre-authorisation:** Generate and submit pre-authorisation requests for admissions and procedures exceeding benefit limits (BR-INS-001).
- **Claim generation:** Auto-generate insurance claims from patient accounts at visit completion or discharge, with ICD-10 codes, procedure codes, and itemised drug lists (BR-INS-002).
- **Rejection management:** Track claim outcomes, display rejection reasons, enable correction and resubmission (BR-INS-003).
- **Credit ageing:** Insurance receivables ageing report by insurer with 0-30, 31-60, 61-90, and 90+ day buckets (BR-INS-004).

**Business rules:** BR-INS-001, BR-INS-002, BR-INS-003, BR-INS-004, BR-FIN-002.
**Priority:** High
**Phase:** 2

---

### FR-HR: Human Resources and Payroll (Phase 2)

The HR module manages staff records, credentials, scheduling, and payroll processing.

**Key requirements (to be expanded at Phase 2 start):**

- **Staff registry:** Staff directory with personal details, qualifications, employment history, and assigned roles.
- **Licence tracking:** Professional licence records per regulatory body (UMDPC for doctors, UNMC for nurses, PHLB for lab technicians). Automated licence expiry alerts at 90, 60, and 30 days before expiry.
- **Payroll:** Monthly payroll calculation with Uganda statutory deductions: PAYE (per URA rates), NSSF (employer 10%, employee 5%). Net pay calculation and payslip generation.
- **Duty roster:** Shift scheduling per department/ward. Staff availability calendar. Overtime tracking.

**Business rules:** None specific (Uganda statutory PAYE/NSSF rates apply).
**Priority:** High
**Phase:** 2

---

### FR-HMIS: Uganda HMIS Reporting (Phase 2)

The HMIS module auto-generates statutory health reports from clinical data.

**Key requirements (to be expanded at Phase 2 start):**

- **HMIS 105:** Monthly outpatient report auto-populated from clinical data. Sections: diagnoses by age/sex (Section 1), lab tests (Section 2), radiology (Section 3), maternity (Section 4), HIV/AIDS (Section 5), immunisation (Section 6), dental (Section 7), eye (Section 8) (BR-HMIS-001).
- **HMIS 108:** Monthly inpatient report auto-populated from IPD data. Admissions, discharges, deaths by diagnosis/age/sex, bed occupancy, surgical operations (BR-HMIS-002).
- **HMIS 033b:** Weekly epidemiological surveillance report auto-tallying 27 IDSR priority diseases from OPD diagnoses (BR-HMIS-003).
- **DHIS2 upload:** Export HMIS data in DHIS2-compatible format. Direct API push to Uganda eHMIS (hmis2.health.go.ug) when internet is available (BR-HMIS-004).
- **PEPFAR MER indicators:** Auto-calculate TX_CURR, TX_NEW, TX_PVLS, HTS_TST, VMMC from clinical data for PEPFAR-supported facilities (BR-HMIS-005).

**Business rules:** BR-HMIS-001, BR-HMIS-002, BR-HMIS-003, BR-HMIS-004, BR-HMIS-005.
**Priority:** Critical
**Phase:** 2

---

### FR-HIV: HIV/AIDS Programme (Phase 3)

The HIV module manages the full ART care cascade from testing to viral suppression monitoring.

**Key requirements (to be expanded at Phase 3 start):**

- **HIV testing and counselling:** HTS registration, testing (rapid, confirmatory), results documentation, and programme enrolment.
- **ART initiation:** WHO clinical staging, baseline CD4, regimen selection per national guidelines. ART card (Uganda MoH format).
- **ARV dispensing:** Dispensing with adherence tracking (pill counts, appointment keeping). Multi-month dispensing support.
- **Viral load tracking:** Viral load results with suppression status classification. Alerts for unsuppressed patients.
- **PMTCT integration:** Mother-baby pair tracking for PMTCT cascade.
- **Missed appointment tracking:** Defaulter identification with SMS/call follow-up triggers.
- **PEPFAR indicators:** Auto-calculation of TX_CURR, TX_NEW, TX_PVLS from ART records.
- **UgandaEMR+ integration:** Data exchange with UgandaEMR+ for PEPFAR reporting at implementing partner sites.

**Business rules:** BR-HMIS-001 (Section 5), BR-HMIS-005, BR-DATA-001 (HIV data sensitivity).
**Priority:** Critical
**Phase:** 3

---

### FR-TB: TB Programme (Phase 3)

The TB module manages case registration through treatment completion.

**Key requirements (to be expanded at Phase 3 start):**

- **Case registration:** TB case registration with classification (new, relapse, treatment after failure/default), anatomical site, and drug susceptibility.
- **Treatment regimen:** Standard regimen recording (2RHZE/4RH) and MDR-TB regimens. Treatment start and expected end dates.
- **DOT tracking:** Directly Observed Therapy adherence recording.
- **Diagnostic results:** Sputum smear, culture, GeneXpert/Xpert MTB/RIF results linked to the case.
- **Treatment outcomes:** Cured, completed, failed, died, lost to follow-up, not evaluated. Outcome recording at treatment end.
- **Contact tracing:** Index case contacts registered with screening status and outcomes.
- **NTLP reporting:** Auto-generation of National TB and Leprosy Programme quarterly report.

**Business rules:** BR-HMIS-001.
**Priority:** High
**Phase:** 3

---

### FR-PAT: Patient Portal and Mobile App (Phase 3)

The Patient Portal provides patients with access to their own health records and self-service features.

**Key requirements (to be expanded at Phase 3 start):**

- **Personal health record:** View visit history, diagnoses, treatments, investigation results, and prescriptions across all facilities where the patient is registered.
- **Test results:** View validated lab and radiology results with reference ranges and flags.
- **Appointments:** Book, reschedule, and cancel appointments. View upcoming and past appointments.
- **Billing:** View fee balance, payment history. Pay via mobile money from the app.
- **Medication reminders:** Configurable reminders for active medication schedules.
- **Immunisation schedule:** View immunisation history and upcoming doses for self and dependents.
- **Health education:** Curated health education content relevant to the patient's conditions.
- **Secure messaging:** Send messages to the treating clinician (asynchronous, not real-time chat).
- **Family members:** Manage multiple family member profiles under one account (guardian access).
- **Offline access:** Cache recent records for offline viewing.
- **Africa-first:** Android-first, data-lite mode (< 1 MB per session), USSD/SMS fallback for non-smartphone users, local language interface (Luganda), low-spec device support (Android 8+, 1 GB RAM).

**Business rules:** BR-DATA-001, BR-DATA-002.
**Priority:** High
**Phase:** 3

---

## Traceability Summary

| FR Group | Count | Phase | Key Business Rules |
|---|---|---|---|
| FR-AUTH | 6 | 1 | BR-DATA-004, BR-DATA-005 |
| FR-TNT | 4 | 1 | BR-DATA-004 |
| FR-REG | 11 | 1 | BR-PID-001 to BR-PID-004, BR-DATA-001, BR-DATA-006 |
| FR-OPD | 15 | 1 | BR-CLIN-001 to BR-CLIN-008, BR-DATA-005, BR-DATA-006, BR-FIN-001, BR-RX-002 |
| FR-LAB | 10 | 1 | BR-CLIN-001, BR-CLIN-003, BR-FIN-001 |
| FR-PHR | 15 | 1 | BR-CLIN-002, BR-CLIN-005, BR-CLIN-006, BR-CLIN-008, BR-RX-001 to BR-RX-003, BR-FIN-001 |
| FR-BIL | 10 | 1 | BR-FIN-001, BR-FIN-003 to BR-FIN-006, BR-FIN-008 |
| FR-APT | 5 | 1 | BR-CLIN-001 |
| FR-RBAC | 7 | 1 | BR-DATA-001, BR-DATA-002, BR-DATA-004 |
| FR-IPD | Summary | 2 | BR-CLIN-005, BR-CLIN-007, BR-CLIN-009, BR-FIN-001, BR-FIN-007, BR-HMIS-002 |
| FR-MAT | Summary | 2 | BR-HMIS-001, BR-CLIN-005 |
| FR-IMM | Summary | 2 | BR-HMIS-001 |
| FR-INS | Summary | 2 | BR-INS-001 to BR-INS-004, BR-FIN-002 |
| FR-HR | Summary | 2 | None specific |
| FR-HMIS | Summary | 2 | BR-HMIS-001 to BR-HMIS-005 |
| FR-HIV | Summary | 3 | BR-HMIS-001, BR-HMIS-005, BR-DATA-001 |
| FR-TB | Summary | 3 | BR-HMIS-001 |
| FR-PAT | Summary | 3 | BR-DATA-001, BR-DATA-002 |
| **Total Phase 1** | **83** | | |

---

### FR-AI: AI Clinical Intelligence Module

---

#### FR-AI-001: At-Risk Patient Early Warning System

**FR-AI-001:** When the hourly early warning job runs and a currently admitted patient has at least 3 vital sign observations recorded within the current admission episode, the system shall compute a modified Early Warning Score (EWS) using the configured scoring matrix — blood pressure, temperature, pulse rate, SpO₂, respiratory rate, and GCS, each component scored 0–3 per the facility's configured thresholds — sum the component scores into a total EWS, store the result in `patient_ews_log` with patient ID, ward, bed number, timestamp, total EWS, and per-component scores, and — when the total EWS has increased by 3 or more points compared to the patient's most recent prior EWS record — dispatch an in-app alert to the assigned nurse and the attending doctor within 60 seconds of score computation. The alert shall display the patient's name, bed number, current EWS, previous EWS, and the component contributing the largest increase. The alert shall include the fixed disclaimer: "This is a monitoring alert, not a clinical diagnosis." The system shall not make a clinical diagnosis. The hourly scoring pass for all admitted patients shall complete within 5 minutes of the scheduled trigger for up to 500 concurrently admitted patients.

---

#### FR-AI-002: Differential Diagnosis Support

**FR-AI-002:** When a clinician submits a differential diagnosis request containing at least 3 of the following inputs — presenting complaint (free text), symptom duration, patient age, patient sex, and 2 or more vital sign readings — the system shall return within 3,000 ms at P95 a ranked list of up to 5 ICD-10 diagnosis codes, each with: rank, ICD-10 code and description, probability indicator (High / Medium / Low — not a numeric percentage), a one-sentence clinical rationale, and the single most differentiating investigation recommended to confirm or exclude that diagnosis. The system shall display the fixed disclaimer on every response: "This is a decision aid. Clinical responsibility remains with the treating clinician." The system shall not store any AI-generated differential diagnosis suggestions in the patient's clinical record without the clinician explicitly selecting and approving one or more suggestions via a named approval action.

---

#### FR-AI-003: Automated Clinical Note Summarisation

**FR-AI-003a:** When a clinician requests a SOAP summary for a consultation that contains at least 50 characters of free-text clinical notes, the system shall generate a structured SOAP summary — Subjective, Objective, Assessment, Plan — within 5,000 ms at P95 and display it in a draft review panel. The clinician shall be able to edit any section of the draft. When the clinician clicks **Approve**, the system shall save the approved SOAP text as the consultation's structured note, linked to the consultation ID, with an `ai_generated: true` flag, and the clinician's user ID and approval timestamp. The system shall not save any AI-generated text to the patient record without an explicit clinician approval action; dismissing the draft without approval shall discard the suggestion with no record written.

**FR-AI-003b:** When a clinician requests a discharge summary draft for an inpatient episode, the system shall aggregate the admission note, ward round notes, investigation results, and active prescriptions from the episode, generate a draft discharge summary containing: Diagnosis, Summary of Hospital Course, Discharge Medications, and Follow-up Instructions within 8,000 ms at P95, and present it in the same draft-review-approve workflow defined in FR-AI-003a.

---

#### FR-AI-004: Pharmacy Demand Forecasting

**FR-AI-004:** When the nightly pharmacy forecast job runs, the system shall — for each active drug in the pharmacy catalogue with at least 28 days of dispensing history — compute the mean daily dispensing rate for the preceding 28 days, apply a seasonal adjustment factor derived from the facility's historical same-period dispensing data for the 2 preceding years (or the full available history if less than 2 years), compute projected days of stock remaining as `current_stock_quantity ÷ adjusted_daily_rate`, and write a forecast record to `pharmacy_forecast_log` with drug ID, current stock, adjusted daily rate, projected days of stock remaining, and forecast timestamp. For any drug with projected days of stock remaining ≤ 14 days, the system shall generate a Stockout Risk alert visible to the Pharmacy Manager role, displaying: drug name, current stock quantity, projected stockout date, and a recommended order quantity equal to `(45 × adjusted_daily_consumption) − current_stock` (floored at zero). The nightly job shall complete processing for up to 500 active drugs within 10 minutes of the scheduled trigger.

---

#### FR-AI-005: Disease Surveillance and Outbreak Detection

**FR-AI-005:** When the 6-hourly surveillance scan runs, the system shall — for each ICD-10 code recorded in the current facility's patient records in the preceding 72 hours — compute the count of new diagnoses with that code, retrieve the 30-day rolling baseline (mean and standard deviation) for that code, and — when the 72-hour count exceeds the value `(30-day mean + 2 × standard deviation)` — create a `surveillance_alert` record with: ICD-10 code, ICD-10 description, alert trigger count, 30-day baseline mean, ratio of trigger count to baseline mean, 72-hour window start and end timestamps, and a geographic breakdown listing the top 3 patient districts by diagnosis count. The system shall dispatch an in-app alert to all users holding the Medical Officer or Hospital Director role within 5 minutes of alert creation. The alert shall include the disclaimer: "This is a statistical cluster alert. Confirmation of an outbreak requires clinical and epidemiological investigation." The system shall not automatically notify any external party — including the Ministry of Health or DHIS2 — without an explicit Medical Officer action.
| **Total (all phases)** | **83 detailed + 9 summary groups** | | |
