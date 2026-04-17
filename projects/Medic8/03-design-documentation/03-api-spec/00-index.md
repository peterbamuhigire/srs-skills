# API Specification Index — Medic8 Phase 1

**Document ID:** DD-03-00
**Project:** Medic8
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Pending Consultant Review

---

## 1. API Overview

This document is the authoritative contract for all Medic8 API endpoints. No endpoint may be
implemented that is not described here. No described endpoint may be omitted from the Phase 1
deliverable without a formal change request.

### 1.1 Base URL

| Environment | Base URL |
|-------------|----------|
| Development | `http://localhost:8000/api/v1` |
| Staging | `https://staging-api.medic8.com/api/v1` |
| Production | `https://api.medic8.com/api/v1` |

Super Admin endpoints use the prefix `/adminpanel/api/v1`.

### 1.2 Authentication

All endpoints (except `POST /auth/login`, `POST /auth/mobile/login`, and `POST /auth/mobile/refresh`) require authentication.

- **Web sessions:** PHP session cookie with `medic8_` prefix. CSRF token required for all state-changing requests.
- **Mobile / API:** `Authorization: Bearer <access_token>` header. Access token is a JWT (HS256, 15-minute expiry). Refresh token is a JWT (HS256, 30-day expiry) with rotation on every refresh.
- **Token management:** Laravel Sanctum. JWT claims: `sub` (user_id), `fid` (facility_id), `role`, `did` (device_id), `jti` (UUID v4), `exp`, `type`.

### 1.3 Content Type

All requests and responses use `application/json` unless stated otherwise (file uploads use `multipart/form-data`).

### 1.4 Response Envelope

All API responses use a consistent envelope.

**Success (single object):**

```json
{
  "success": true,
  "data": {},
  "message": ""
}
```

**Success (list):**

```json
{
  "success": true,
  "data": [],
  "meta": {
    "total": 142,
    "page": 1,
    "per_page": 25,
    "last_page": 6
  }
}
```

**Error:**

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The given data was invalid.",
    "details": {
      "field_name": ["Validation message."]
    }
  },
  "errors": []
}
```

### 1.5 Pagination

Offset-based pagination on all list endpoints:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Page number (1-indexed) |
| `per_page` | integer | 25 | Results per page (max 100) |

### 1.6 Rate Limiting

- 60 requests per minute per authenticated user.
- Rate-limited responses return HTTP 429 with `Retry-After` header (seconds).

### 1.7 Tenant Isolation

Every tenant-scoped request resolves `facility_id` from the authenticated session or JWT claim `fid`. The Repository layer enforces `WHERE facility_id = ?` on every query (BR-DATA-004). No endpoint returns data from another tenant unless explicitly documented (cross-facility lookup, emergency access).

---

## 2. Endpoint Registry

All Phase 1 API endpoints organised by FR group. Each endpoint specifies: HTTP method, path, FR cross-reference, description, authentication type, request body, response body, and status codes.

**Auth Key:** S = Session (web) | J = JWT (mobile/API) | S/J = Both | P = Public (no auth)

---

### 2.1 Authentication (FR-AUTH)

#### POST /auth/login

- **FR:** FR-AUTH-001
- **Description:** Web session login with CSRF protection.
- **Auth:** P (creates session)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `email` | string | Yes | Valid email, trimmed |
| `password` | string | Yes | 8-255 characters |
| `csrf_token` | string | Yes | Must match `$_SESSION['medic8_csrf_token']` |

- **Response:** HTTP 302 redirect to role-appropriate dashboard on success.
- **Status codes:**

| Code | Condition |
|------|-----------|
| 302 | Login success, redirect to dashboard |
| 401 | Invalid credentials (email not found or wrong password) |
| 403 | CSRF invalid (`CSRF_INVALID`), account locked (`ACCOUNT_LOCKED`), account inactive (`ACCOUNT_INACTIVE`), tenant suspended (`TENANT_SUSPENDED`) |
| 422 | Validation error |

---

#### POST /auth/mobile/login

- **FR:** FR-AUTH-002
- **Description:** JWT login for mobile and API clients. Returns access + refresh token pair.
- **Auth:** P (creates token)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `email` | string | Yes | Valid email |
| `password` | string | Yes | 8-255 characters |
| `device_id` | string | Yes | Max 255 chars, identifies the device |

- **Response (200):**

```json
{
  "success": true,
  "data": {
    "access_token": "eyJ...",
    "refresh_token": "eyJ...",
    "expires_in": 900,
    "token_type": "Bearer"
  }
}
```

- **Status codes:**

| Code | Condition |
|------|-----------|
| 200 | Login success |
| 401 | Invalid credentials |
| 403 | Account locked, inactive, or tenant suspended |
| 422 | Missing `device_id` or validation error |

---

#### POST /auth/mobile/refresh

- **FR:** FR-AUTH-003
- **Description:** Refresh token rotation. Revokes the old refresh token and issues a new token pair.
- **Auth:** J (refresh token in body or `Authorization` header)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `refresh_token` | string | Yes | Valid, non-expired, non-revoked JWT |

- **Response (200):** Same structure as `POST /auth/mobile/login`.
- **Status codes:**

| Code | Condition |
|------|-----------|
| 200 | Refresh success |
| 401 | Invalid token (`INVALID_TOKEN`), expired (`TOKEN_EXPIRED`), revoked (`TOKEN_REVOKED`) |

---

#### POST /auth/logout

- **FR:** FR-AUTH-004
- **Description:** Logout. Destroys web session or revokes all JWT refresh tokens for the device.
- **Auth:** S/J
- **Request body (API):**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `device_id` | string | No | If omitted, revokes tokens for the device in the current JWT |

- **Response (web):** HTTP 302 redirect to `/auth/login`.
- **Response (API, 200):** `{"success": true}`
- **Status codes:** 200 (API), 302 (web), 401 (unauthenticated).

---

#### POST /auth/mfa/verify

- **FR:** FR-AUTH-006
- **Description:** Multi-Factor Authentication verification for admin roles (`facility_admin`, `facility_director`, `super_admin`). Called after successful password verification.
- **Auth:** S (partial session, pre-MFA)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `totp_code` | string | Yes | 6-digit TOTP or SMS OTP |

- **Response (200):** Session upgraded with `mfa_verified = true`. Redirect to admin dashboard.
- **Status codes:**

| Code | Condition |
|------|-----------|
| 200 | MFA verified |
| 422 | Invalid code (`MFA_INVALID`), expired code (`MFA_EXPIRED`) |

---

### 2.2 Tenants (FR-TNT)

#### POST /adminpanel/api/v1/facilities

- **FR:** FR-TNT-001
- **Description:** Provision a new facility (tenant). Creates facility record, Facility Admin user account, sends welcome email and SMS.
- **Auth:** S (Super Admin only)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `name` | string | Yes | 2-150 chars |
| `country` | string | Yes | ISO 3166-1 alpha-2, default `UG` |
| `tier` | enum | Yes | `basic`, `pro`, `enterprise` |
| `facility_type` | enum | Yes | `clinic`, `health_centre_ii`, `health_centre_iii`, `health_centre_iv`, `general_hospital`, `regional_referral`, `national_referral` |
| `owner_name` | string | Yes | 2-100 chars |
| `owner_email` | string | Yes | Valid email, unique across all facilities |
| `owner_phone` | string | Yes | E.164 format |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Facility ID |
| `slug` | string | URL-safe facility identifier |
| `status` | string | `pending` |
| `owner_user_id` | integer | Created admin user ID |

- **Status codes:** 201 (created), 403 (not Super Admin), 422 (validation error), 409 (duplicate `owner_email`).

---

#### PATCH /adminpanel/api/v1/facilities/{id}

- **FR:** FR-TNT-002
- **Description:** Activate, suspend, or update a facility. Suspension invalidates all sessions and blocks login.
- **Auth:** S (Super Admin only)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `status` | enum | No | `active`, `suspended` |
| `reason` | string | Conditional | Required when `status = suspended` |
| `name` | string | No | 2-150 chars |
| `tier` | enum | No | `basic`, `pro`, `enterprise` |

- **Response (200):** Updated facility record.
- **Status codes:** 200, 403, 404, 422.

---

#### POST /adminpanel/api/v1/facilities/{id}/activate

- **FR:** FR-TNT-002
- **Description:** Convenience endpoint to set facility status to `active`.
- **Auth:** S (Super Admin only)
- **Response (200):** `{"success": true, "data": {"status": "active"}}`
- **Status codes:** 200, 403, 404.

---

#### POST /adminpanel/api/v1/facilities/{id}/deactivate

- **FR:** FR-TNT-002
- **Description:** Convenience endpoint to suspend a facility. Invalidates all active sessions.
- **Auth:** S (Super Admin only)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `reason` | string | Yes | 10-500 chars |

- **Response (200):** `{"success": true, "data": {"status": "suspended"}}`
- **Status codes:** 200, 403, 404, 422.

---

#### PATCH /api/v1/facility/config

- **FR:** FR-TNT-003
- **Description:** Update the current facility's configuration (modules, currency, MRN format, logo, operating hours).
- **Auth:** S/J (Facility Admin only)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `enabled_modules` | array | No | Valid module identifiers |
| `currency` | string | No | ISO 4217, default `UGX` |
| `tax_rate` | decimal | No | 0-100 |
| `mrn_format` | string | No | Pattern with placeholders, e.g. `{FACILITY}-{YEAR}-{SEQ}` |
| `logo` | file | No | Max 2 MB, JPEG/PNG (`multipart/form-data`) |
| `operating_hours` | object | No | `{"start": "08:00", "end": "17:00"}` |

- **Response (200):** Updated facility configuration.
- **Status codes:** 200, 403, 422.

---

#### POST /adminpanel/api/v1/countries

- **FR:** FR-TNT-004
- **Description:** Create a country configuration record (HMIS forms, EPI schedule, tax rules, coding system).
- **Auth:** S (Super Admin only)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `country_code` | string | Yes | ISO 3166-1 alpha-2, unique |
| `country_name` | string | Yes | 2-100 chars |
| `currency` | string | Yes | ISO 4217 |
| `hmis_forms` | array | No | HMIS form identifiers |
| `epi_schedule` | object | No | Vaccine schedule definition |
| `tax_rules` | object | No | PAYE brackets, social security rates |
| `coding_system` | enum | No | `icd10`, `icd11`, `both` |

- **Response (201):** Created country configuration.
- **Status codes:** 201, 403, 409 (duplicate `country_code`), 422.

---

#### PATCH /adminpanel/api/v1/countries/{code}

- **FR:** FR-TNT-004
- **Description:** Update a country configuration record.
- **Auth:** S (Super Admin only)
- **Request body:** Same fields as POST (all optional).
- **Response (200):** Updated country configuration.
- **Status codes:** 200, 403, 404, 422.

---

### 2.3 Patients (FR-REG)

#### POST /api/v1/patients

- **FR:** FR-REG-001
- **Description:** Register a new patient. Triggers EMPI duplicate detection (FR-REG-009). Auto-generates MRN (FR-REG-002). P95 response time: 500 ms.
- **Auth:** S/J (Receptionist, Nurse, Records Officer)
- **Request body (required):**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `first_name` | string | Yes | 1-100 chars |
| `last_name` | string | Yes | 1-100 chars |
| `sex` | enum | Yes | `male`, `female` |
| `date_of_birth` | date | Conditional | ISO 8601, must be in the past; OR `estimated_age` |
| `estimated_age` | integer | Conditional | Required if `date_of_birth` not provided |
| `contact_phone` | string | Conditional | E.164; at least one of `contact_phone` or `physical_address` required |
| `physical_address` | string | Conditional | At least one contact method required |

- **Request body (optional):** `middle_name`, `nin`, `passport_number`, `unhcr_id`, `nhis_number`, `email`, `blood_group`, `photo`, `next_of_kin_name`, `next_of_kin_phone`, `next_of_kin_relationship`, `allergies[]`, `chronic_conditions[]`, `nationality`, `district`, `sub_county`, `village`, `tribe`, `religion`, `occupation`, `marital_status`.
- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `patient_uid` | UUID | Global patient identifier |
| `mrn` | string | Facility-scoped Medical Record Number |
| `facility_id` | integer | Registering facility |
| `category` | string | Auto-assigned (`adult` or `paediatric`) |

- **Status codes:**

| Code | Condition |
|------|-----------|
| 201 | Patient created |
| 409 | Duplicate detected (`DUPLICATE_DETECTED`), must resolve before proceeding |
| 422 | Validation error, `CONTACT_REQUIRED`, `INVALID_DOB` |

---

#### GET /api/v1/patients

- **FR:** FR-REG-003
- **Description:** List and search patients within the caller's facility. Searches across name, MRN, phone, NIN, passport, UNHCR ID, NHIS number. P95 response time: 300 ms.
- **Auth:** S/J
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `q` | string | Yes | Min 2 chars, search query |
| `page` | integer | No | Default 1 |
| `per_page` | integer | No | Default 25, max 100 |

- **Response (200):** Paginated list of patient records scoped to `facility_id`.
- **Status codes:** 200, 422 (`QUERY_REQUIRED` if `q` is empty).

---

#### GET /api/v1/patients/{patient_uid}

- **FR:** FR-REG-007
- **Description:** Retrieve the full patient profile including demographics, photo, blood group, allergies, chronic conditions, active medications, and clinical summary.
- **Auth:** S/J
- **Response (200):** Full patient profile object.
- **Status codes:** 200, 404.

---

#### PATCH /api/v1/patients/{patient_uid}

- **FR:** FR-REG-007
- **Description:** Update patient profile fields (demographics, allergies, chronic conditions, photo).
- **Auth:** S/J (Receptionist, Nurse, Records Officer, Doctor)
- **Request body:** Any patient field (same as POST, all optional).
- **Response (200):** Updated patient profile.
- **Status codes:** 200, 404, 422.

---

#### PATCH /api/v1/patients/{patient_uid}/category

- **FR:** FR-REG-004
- **Description:** Update patient category. Determines pricing tier and clinical protocols.
- **Auth:** S/J (Receptionist, Records Officer, Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `category` | enum | Yes | `adult`, `paediatric`, `staff`, `vip`, `indigent`, `refugee` |

- **Response (200):** Updated patient with new category.
- **Status codes:** 200, 404, 422.

---

#### POST /api/v1/patients/merge

- **FR:** FR-REG-008
- **Description:** Merge two duplicate patient records. Transfers all clinical, billing, and encounter data from source to target. Reversible within 30 days.
- **Auth:** S/J (Records Officer, Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `source_patient_uid` | UUID | Yes | Patient to be merged (source) |
| `target_patient_uid` | UUID | Yes | Surviving patient (target) |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `surviving_patient_uid` | UUID | Target patient UID |
| `merged_records` | object | Counts of transferred encounters, billing lines, lab results |
| `unmerge_deadline` | datetime | 30 days from merge |

- **Status codes:** 200, 403, 404, 422 (`UNMERGE_WINDOW_EXPIRED` for late unmerge attempts).

---

#### POST /api/v1/patients/unmerge

- **FR:** FR-REG-008
- **Description:** Reverse a patient merge within the 30-day window.
- **Auth:** S/J (Records Officer, Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `source_patient_uid` | UUID | Yes | Originally merged patient |
| `target_patient_uid` | UUID | Yes | Surviving patient |

- **Response (200):** Both patient records restored.
- **Status codes:** 200, 403, 422 (`UNMERGE_WINDOW_EXPIRED`).

---

#### GET /api/v1/patients/duplicates

- **FR:** FR-REG-009
- **Description:** EMPI duplicate detection. Returns potential duplicate patients with confidence scores using Soundex and Metaphone algorithms adapted for African naming patterns.
- **Auth:** S/J (Records Officer, Receptionist)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `first_name` | string | Yes | Min 1 char |
| `last_name` | string | Yes | Min 1 char |
| `date_of_birth` | date | No | ISO 8601 |
| `nin` | string | No | National ID |
| `contact_phone` | string | No | E.164 |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `matches[]` | array | Potential duplicates |
| `matches[].patient_uid` | UUID | Existing patient UID |
| `matches[].confidence` | decimal | 0-100 match score |
| `matches[].match_fields` | array | Fields that matched |

- **Status codes:** 200, 422.

---

#### GET /api/v1/patients/{patient_uid}/identifiers

- **FR:** FR-REG-005
- **Description:** List all identifiers for a patient (NIN, passport, UNHCR ID, NHIS, phone, email).
- **Auth:** S/J
- **Response (200):** Array of identifier objects with `type`, `value`, and `created_at`.
- **Status codes:** 200, 404.

---

#### POST /api/v1/patients/{patient_uid}/identifiers

- **FR:** FR-REG-005
- **Description:** Add one or more identifiers to a patient record.
- **Auth:** S/J (Receptionist, Records Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `type` | enum | Yes | `nin`, `passport`, `unhcr_id`, `nhis`, `phone`, `email` |
| `value` | string | Yes | 1-100 chars, unique per type across the platform |

- **Response (201):** Created identifier record.
- **Status codes:** 201, 404, 409 (duplicate identifier), 422.

---

#### POST /api/v1/patients/{patient_uid}/guardians

- **FR:** FR-REG-006
- **Description:** Add a guardian/next-of-kin for a paediatric patient. At least one guardian is required before clinical encounters can proceed.
- **Auth:** S/J (Receptionist, Nurse, Records Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `guardian_name` | string | Yes | 2-100 chars |
| `relationship` | enum | Yes | `mother`, `father`, `grandparent`, `sibling`, `uncle`, `aunt`, `other` |
| `phone` | string | Yes | E.164 format |
| `is_primary` | boolean | No | Default `true` for first guardian |
| `linked_patient_uid` | UUID | No | If guardian is a registered patient |

- **Response (201):** Created guardian record.
- **Status codes:** 201, 404, 422.

---

#### POST /api/v1/patients/{patient_uid}/triage

- **FR:** FR-REG-011
- **Description:** Assign a triage level and add the patient to the facility triage queue, sorted by priority (BR-CLIN-001).
- **Auth:** S/J (Nurse)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `triage_level` | enum | Yes | `emergency`, `urgent`, `semi_urgent`, `non_urgent` |
| `assigned_doctor_id` | integer | No | Target doctor for OPD queue |
| `chief_complaint` | string | No | Max 500 chars |

- **Response (200):** Queue position and estimated wait time.
- **Status codes:** 200, 404, 422.

---

#### GET /api/v1/global-patients

- **FR:** FR-REG-010
- **Description:** Cross-facility patient lookup via the global patient identity layer. Returns identity data only (name, age, sex, facility list). Clinical records excluded unless emergency access is invoked.
- **Auth:** S/J (clinician roles)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `q` | string | Yes | Min 2 chars, searches name, NIN, phone |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `patient_uid` | UUID | Global patient UID |
| `name` | string | Full name |
| `age` | integer | Age in years |
| `sex` | string | `male` or `female` |
| `facilities` | array | List of facility names where registered |

- **Status codes:** 200, 422.

---

### 2.4 OPD Encounters (FR-OPD)

#### POST /api/v1/encounters

- **FR:** FR-OPD-003
- **Description:** Create a new OPD encounter (visit) for a patient. Opens the SOAP consultation workspace.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `patient_uid` | UUID | Yes | Must exist, must be in doctor's queue |
| `encounter_type` | enum | No | `opd`, `follow_up`, default `opd` |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `encounter_id` | integer | Unique encounter ID |
| `patient_uid` | UUID | Patient UID |
| `clinician_id` | integer | Consulting doctor |
| `status` | string | `in_progress` |
| `created_at` | datetime | Encounter start time |

- **Status codes:** 201, 403, 404, 422 (`GUARDIAN_REQUIRED` for paediatric patients without guardian).

---

#### GET /api/v1/encounters/{id}

- **FR:** FR-OPD-003
- **Description:** Retrieve encounter details including SOAP notes, vitals, diagnoses, prescriptions, investigations, and procedures.
- **Auth:** S/J
- **Response (200):** Full encounter object with nested clinical data.
- **Status codes:** 200, 404.

---

#### PATCH /api/v1/encounters/{id}

- **FR:** FR-OPD-003
- **Description:** Update SOAP notes and encounter fields. Auto-saved to local storage (BR-DATA-005).
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `subjective` | string | No | Chief complaint, HPI |
| `objective` | string | No | Examination findings |
| `assessment` | string | No | Clinical assessment narrative |
| `plan` | string | No | Treatment plan narrative |

- **Response (200):** Updated encounter.
- **Status codes:** 200, 403, 404, 422.

---

#### POST /api/v1/encounters/{id}/vitals

- **FR:** FR-OPD-001
- **Description:** Record triage vital signs for an encounter. Auto-calculates BMI and NEWS2. For patients under 12, MUAC is required. For patients under 5, WHO Z-scores are auto-calculated.
- **Auth:** S/J (Nurse)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `systolic_bp` | integer | Yes | 40-300 mmHg |
| `diastolic_bp` | integer | Yes | 20-200 mmHg |
| `temperature` | decimal | Yes | 30.0-45.0 C |
| `pulse` | integer | Yes | 20-250 bpm |
| `spo2` | integer | Yes | 50-100 % |
| `respiratory_rate` | integer | Yes | 4-60 breaths/min |
| `weight` | decimal | Yes | 0.3-300 kg |
| `height` | decimal | Yes | 20-250 cm |
| `muac` | decimal | Conditional | 5-40 cm, required if patient age < 12 |
| `triage_level` | enum | No | `emergency`, `urgent`, `semi_urgent`, `non_urgent` (auto-suggested from NEWS2, overridable) |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `bmi` | decimal | Auto-calculated |
| `news2_score` | integer | National Early Warning Score 2 |
| `suggested_triage` | string | NEWS2-derived triage suggestion |
| `z_scores` | object | WHO Z-scores (patients < 5 only) |

- **Status codes:** 201, 404, 422.

---

#### POST /api/v1/encounters/{id}/diagnoses

- **FR:** FR-OPD-004
- **Description:** Add an ICD-10/ICD-11 coded diagnosis. Free-text-only diagnoses are prohibited (BR-DATA-006). Multiple diagnoses allowed; one must be marked primary.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `icd_code` | string | Yes | Valid ICD-10 or ICD-11 code |
| `description` | string | Yes | Clinician's description |
| `is_primary` | boolean | No | Default `false` |

- **Response (201):** Created diagnosis record.
- **Status codes:** 201, 404, 422 (`ICD_CODE_REQUIRED`).

---

#### GET /api/v1/icd/search

- **FR:** FR-OPD-004
- **Description:** Searchable ICD-10/ICD-11 lookup by code or clinical description. P95 response time: 200 ms.
- **Auth:** S/J
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `q` | string | Yes | Min 2 chars, searches code and description |
| `coding_system` | enum | No | `icd10`, `icd11`, `both` (default from facility config) |

- **Response (200):** Array of ICD code matches with code, description, and synonyms.
- **Status codes:** 200, 422.

---

#### POST /api/v1/encounters/{id}/prescriptions

- **FR:** FR-OPD-006
- **Description:** Write a prescription. Validates Five Rights (FR-OPD-015), checks drug interactions (FR-OPD-008), enforces weight-based paediatric dosing (FR-PHR-014), and shows stock levels (FR-OPD-007). Auto-generates billing charge (BR-FIN-001). Pushes to pharmacy queue (FR-PHR-001).
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `drug_id` | integer | Yes | Must exist in facility formulary |
| `dose` | decimal | Yes | > 0 |
| `dose_unit` | enum | Yes | `mg`, `ml`, `g`, `mcg`, `IU`, `units` |
| `frequency` | enum | Yes | `od`, `bd`, `tds`, `qid`, `stat`, `prn`, `nocte`, `mane` |
| `duration` | integer | Yes | Days, > 0 |
| `route` | enum | Yes | `oral`, `iv`, `im`, `sc`, `topical`, `rectal`, `inhaled`, `sublingual`, `ophthalmic`, `otic` |
| `quantity` | integer | No | Auto-calculated from dose x frequency x duration, overridable |
| `instructions` | string | No | Max 500 chars |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `prescription_id` | integer | Prescription record ID |
| `calculated_quantity` | integer | System-calculated quantity |
| `stock_available` | integer | Current pharmacy stock |
| `interactions` | array | Drug interaction alerts (if any) |
| `billing_charge_id` | integer | Auto-posted billing line |

- **Status codes:**

| Code | Condition |
|------|-----------|
| 201 | Prescription created |
| 404 | Encounter or drug not found |
| 422 | Validation error, `DRUG_NOT_IN_FORMULARY`, `WEIGHT_REQUIRED`, `DOSE_EXCEEDS_MAXIMUM`, `INVALID_ROUTE` |
| 460 | CDS Alert — drug interaction (Tier 3/4) requiring override or pharmacist intervention |
| 461 | Prescribing authority violation (nurse attempting to prescribe) |

---

#### GET /api/v1/encounters/{id}/prescriptions/{rx_id}/interactions

- **FR:** FR-OPD-008
- **Description:** Check drug interactions for a specific prescription against all active medications. Returns tiered alerts (Info/Warning/Serious/Fatal).
- **Auth:** S/J (Doctor, Clinical Officer, Pharmacist)
- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `interactions[]` | array | List of interactions |
| `interactions[].tier` | integer | 1 (Info), 2 (Warning), 3 (Serious), 4 (Fatal) |
| `interactions[].drug_a` | string | Prescribed drug |
| `interactions[].drug_b` | string | Conflicting active medication |
| `interactions[].description` | string | Interaction description |
| `interactions[].action` | string | `info`, `warn`, `override_required`, `hard_stop` |

- **Status codes:** 200, 404.

---

#### POST /api/v1/encounters/{id}/prescriptions/{rx_id}/override

- **FR:** FR-OPD-008
- **Description:** Override a Tier 3 (Serious) drug interaction alert with a documented reason. Logged with clinician ID and timestamp.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `reason` | string | Yes | Min 20 chars |

- **Response (200):** Override recorded, prescription proceeds.
- **Status codes:** 200, 403, 404, 422 (reason too short), 460 (Tier 4 cannot be overridden).

---

#### POST /api/v1/encounters/{id}/investigations

- **FR:** FR-OPD-005
- **Description:** Request lab or radiology investigations. Creates queue entries, sends real-time notification to Lab Technician/Radiographer, posts billing charges.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `tests[]` | array | Yes | At least 1 test |
| `tests[].test_id` | integer | Yes | Must exist in facility test catalogue |
| `tests[].clinical_indication` | string | No | Max 500 chars |
| `tests[].urgency` | enum | Yes | `routine`, `urgent`, `emergency` |
| `tests[].specimen_type` | enum | Conditional | For lab: `blood`, `urine`, `stool`, `sputum`, `csf`, `swab`, `other` |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `requests[]` | array | Created investigation requests |
| `requests[].request_id` | integer | Lab/radiology request ID |
| `requests[].lan` | string | Lab Accession Number |
| `requests[].status` | string | `requested` |
| `billing_charges[]` | array | Auto-posted billing line IDs |

- **Status codes:** 201, 404, 422.

---

#### POST /api/v1/encounters/{id}/procedures

- **FR:** FR-OPD-009
- **Description:** Record a minor OPD procedure. Auto-generates billing charge.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `procedure_id` | integer | Yes | Must exist in procedure catalogue |
| `indication` | string | Yes | Max 500 chars |
| `findings` | string | No | Max 1000 chars |
| `complications` | string | No | Max 500 chars |
| `materials` | array | No | List of materials used |

- **Response (201):** Created procedure record with billing charge ID.
- **Status codes:** 201, 404, 422.

---

#### POST /api/v1/encounters/{id}/referrals

- **FR:** FR-OPD-010
- **Description:** Create a referral (internal or external). For internal referrals, adds patient to destination department queue. For external referrals, generates a printable referral letter with clinical summary.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `referral_type` | enum | Yes | `internal`, `external` |
| `destination_department` | string | Conditional | Required for internal |
| `destination_facility` | string | Conditional | Required for external |
| `reason` | string | Yes | Max 1000 chars |
| `urgency` | enum | Yes | `routine`, `urgent`, `emergency` |
| `clinical_summary` | string | No | Auto-populated from visit, editable |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `referral_id` | integer | Referral record ID |
| `referral_letter_url` | string | PDF download URL (external referrals) |

- **Status codes:** 201, 404, 422.

---

#### POST /api/v1/encounters/{id}/discharge

- **FR:** FR-OPD-013
- **Description:** End the OPD visit. Records disposition, verifies pending orders, finalises billing, removes patient from all queues.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `disposition` | enum | Yes | `discharged`, `admitted`, `referred`, `left_without_being_seen` |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `visit_summary_url` | string | Printable visit summary PDF |
| `billing_finalised` | boolean | Billing status |
| `pending_orders` | array | Unresolved orders (if any, warning only) |

- **Status codes:** 200, 404, 422.

---

#### POST /api/v1/encounters/{id}/follow-up

- **FR:** FR-OPD-011
- **Description:** Book a follow-up appointment from the consultation screen. Creates an appointment record and schedules an SMS/WhatsApp reminder.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `follow_up_date` | date | Yes | Must be in the future |
| `department` | string | No | Defaults to current department |
| `doctor_id` | integer | No | Defaults to current clinician |
| `notes` | string | No | Max 500 chars |

- **Response (201):** Created appointment record.
- **Status codes:** 201, 404, 422.

---

#### GET /api/v1/encounters/{id}/history

- **FR:** FR-OPD-012
- **Description:** Retrieve the patient's complete chronological visit history within the current facility. Loads within 1 second for patients with up to 100 visits.
- **Auth:** S/J
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `date_from` | date | No | ISO 8601 |
| `date_to` | date | No | ISO 8601 |
| `department` | string | No | Filter by department |
| `clinician_id` | integer | No | Filter by clinician |

- **Response (200):** Paginated array of encounter summaries (date, clinician, department, diagnoses, prescriptions, investigations, procedures, referrals).
- **Status codes:** 200, 404.

---

#### GET /api/v1/encounters/{id}/ews

- **FR:** FR-OPD-014
- **Description:** Calculate and return the NEWS2 Early Warning Score from the most recent vitals.
- **Auth:** S/J
- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `news2_score` | integer | Calculated score |
| `risk_level` | string | `low` (0-4), `medium` (5-6), `high` (7+) |
| `recommendation` | string | Clinical recommendation |
| `parameters` | object | Individual parameter scores |

- **Status codes:** 200, 404.

---

#### GET /api/v1/queue/opd

- **FR:** FR-OPD-002
- **Description:** Doctor's OPD queue. Real-time list of patients awaiting consultation, sorted by triage priority then arrival time.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `doctor_id` | integer | No | Defaults to authenticated user |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `queue[]` | array | Queued patients |
| `queue[].patient_uid` | UUID | Patient UID |
| `queue[].patient_name` | string | Full name |
| `queue[].mrn` | string | Medical Record Number |
| `queue[].triage_level` | string | `emergency`, `urgent`, `semi_urgent`, `non_urgent` |
| `queue[].wait_minutes` | integer | Minutes since triage |
| `queue[].chief_complaint` | string | If entered at triage |
| `queue[].position` | integer | Queue position |

- **Status codes:** 200, 403.

---

### 2.5 Laboratory (FR-LAB)

#### GET /api/v1/lab/requests

- **FR:** FR-LAB-001
- **Description:** List pending lab requests, sorted by urgency then request time. Emergency requests appear first.
- **Auth:** S/J (Lab Technician, Lab Supervisor)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `status` | enum | No | `requested`, `collected`, `received`, `processing`, `result_ready`, `validated` |
| `urgency` | enum | No | `routine`, `urgent`, `emergency` |
| `page` | integer | No | Default 1 |
| `per_page` | integer | No | Default 25 |

- **Response (200):** Paginated list of lab requests with patient details, test name, urgency, and status.
- **Status codes:** 200.

---

#### POST /api/v1/lab/requests

- **FR:** FR-LAB-001
- **Description:** Create a lab request directly (alternative to encounter-based investigation ordering). Posts billing charge.
- **Auth:** S/J (Doctor, Clinical Officer, Lab Technician)
- **Request body:** Same as `POST /encounters/{id}/investigations` tests array.
- **Response (201):** Created lab request with LAN.
- **Status codes:** 201, 422.

---

#### POST /api/v1/lab/samples/{id}/collect

- **FR:** FR-LAB-002
- **Description:** Mark a lab request as collected. Generates a barcode/QR label (25 mm x 50 mm) for the specimen.
- **Auth:** S/J (Lab Technician)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `specimen_type` | enum | Yes | `blood`, `urine`, `stool`, `sputum`, `csf`, `swab`, `other` |
| `collection_notes` | string | No | Max 500 chars |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | `collected` |
| `barcode` | string | Barcode value |
| `label_url` | string | Printable label URL |
| `collected_at` | datetime | Collection timestamp |
| `collected_by` | string | Technician name |

- **Status codes:** 200, 404, 422.

---

#### PATCH /api/v1/lab/samples/{id}/status

- **FR:** FR-LAB-003
- **Description:** Update specimen tracking status through the laboratory workflow: `received`, `processing`.
- **Auth:** S/J (Lab Technician)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `status` | enum | Yes | `received`, `processing` |

- **Response (200):** Updated specimen record with timestamp.
- **Status codes:** 200, 404, 422 (invalid status transition).

---

#### POST /api/v1/lab/results

- **FR:** FR-LAB-004
- **Description:** Enter lab results for a collected specimen. Auto-flags abnormal values (H/L/HH/LL). Critical values (HH/LL) trigger escalation cascade (FR-LAB-005). Status set to `result_ready_pending_validation`.
- **Auth:** S/J (Lab Technician)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `request_id` | integer | Yes | Lab request ID |
| `parameters[]` | array | Yes | At least 1 result parameter |
| `parameters[].parameter_id` | integer | Yes | From test definition |
| `parameters[].value` | string | Yes | Numeric for quantitative, coded for qualitative |
| `parameters[].unit` | string | Yes | Must match parameter definition |
| `parameters[].comment` | string | No | Max 500 chars |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `result_id` | integer | Result record ID |
| `flags[]` | array | Abnormal flags per parameter (`H`, `L`, `HH`, `LL`) |
| `critical_alert_triggered` | boolean | Whether escalation was triggered |
| `status` | string | `result_ready_pending_validation` |

- **Status codes:** 201, 404, 422, 409 (`QC_OUT_OF_CONTROL` if assay QC is failed).

---

#### POST /api/v1/lab/results/{id}/validate

- **FR:** FR-LAB-006
- **Description:** Lab Supervisor validates or rejects a pending result. Only validated results are visible to clinicians.
- **Auth:** S/J (Lab Supervisor)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `action` | enum | Yes | `approve`, `reject` |
| `rejection_reason` | string | Conditional | Required if `action = reject`, max 500 chars |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | `validated` or `rejected` |
| `validated_by` | string | Supervisor name |
| `validated_at` | datetime | Validation timestamp |

- **Status codes:** 200, 403, 404, 422.

---

#### POST /api/v1/lab/results/{id}/escalate

- **FR:** FR-LAB-005
- **Description:** Manually trigger or acknowledge a critical value escalation. Records acknowledgement with timestamp.
- **Auth:** S/J (Doctor, Clinical Officer, Nurse, Lab Supervisor)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `action` | enum | Yes | `acknowledge`, `escalate` |
| `notes` | string | No | Max 500 chars |

- **Response (200):** Escalation status updated.
- **Status codes:** 200, 404, 422.

---

#### GET /api/v1/lab/qc

- **FR:** FR-LAB-007
- **Description:** List QC records for a specified assay/analyser. Returns Levey-Jennings chart data and Westgard rule violations.
- **Auth:** S/J (Lab Technician, Lab Supervisor)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `assay_id` | integer | Yes | Assay/test identifier |
| `date_from` | date | No | ISO 8601 |
| `date_to` | date | No | ISO 8601 |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `qc_records[]` | array | QC entries with value, mean, SD, date |
| `westgard_violations[]` | array | Rule violations (1-2s, 1-3s, 2-2s, R-4s, 4-1s, 10x) |
| `assay_status` | string | `in_control` or `out_of_control` |

- **Status codes:** 200, 404.

---

#### POST /api/v1/lab/qc

- **FR:** FR-LAB-007
- **Description:** Enter a QC sample result for an assay. Applies Westgard rules; out-of-control flag blocks patient result entry.
- **Auth:** S/J (Lab Technician)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `assay_id` | integer | Yes | Assay/test identifier |
| `level` | enum | Yes | `normal`, `abnormal` |
| `value` | decimal | Yes | QC sample result |
| `lot_number` | string | Yes | QC lot number |
| `analyser_id` | integer | No | Analyser identifier |

- **Response (201):** QC entry with Westgard evaluation result.
- **Status codes:** 201, 422.

---

#### POST /api/v1/lab/requests/{id}/refer-external

- **FR:** FR-LAB-009
- **Description:** Mark a lab request for external referral (e.g., Lancet, CPHL).
- **Auth:** S/J (Lab Technician, Lab Supervisor)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `external_lab_name` | string | Yes | Max 200 chars |
| `expected_tat_days` | integer | No | Expected turnaround in days |

- **Response (200):** Request status set to `referred_external`, printable referral form URL.
- **Status codes:** 200, 404, 422.

---

#### POST /api/v1/lab/tests

- **FR:** FR-LAB-010
- **Description:** Create or import a test definition into the facility test catalogue with LOINC coding.
- **Auth:** S/J (Lab Supervisor, Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `test_name` | string | Yes | Max 200 chars |
| `loinc_code` | string | No | Valid LOINC code |
| `specimen_type` | enum | Yes | `blood`, `urine`, `stool`, `sputum`, `csf`, `swab`, `other` |
| `parameters[]` | array | Yes | At least 1 parameter with name, unit, reference range |
| `tat_target_hours` | integer | No | Target turnaround time |

- **Response (201):** Created test definition.
- **Status codes:** 201, 403, 422.

---

### 2.6 Pharmacy (FR-PHR)

#### GET /api/v1/pharmacy/queue

- **FR:** FR-PHR-001
- **Description:** Prescription queue for the pharmacy. Sorted by urgency then prescription time. Real-time updates.
- **Auth:** S/J (Pharmacist)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `status` | enum | No | `pending`, `dispensed`, `partial` |
| `urgency` | enum | No | `routine`, `urgent`, `emergency` |
| `page` | integer | No | Default 1 |
| `per_page` | integer | No | Default 25 |

- **Response (200):** Paginated list of prescriptions with patient name, MRN, prescriber, item count, urgency, and time since prescription.
- **Status codes:** 200.

---

#### POST /api/v1/pharmacy/dispense

- **FR:** FR-PHR-002
- **Description:** Dispense a prescription. Deducts stock (FIFO), records batch number and expiry, generates dispensing label (FR-PHR-004), auto-posts billing charge (FR-PHR-012). Supports partial dispensing (FR-PHR-005).
- **Auth:** S/J (Pharmacist)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `prescription_id` | integer | Yes | Must be a pending prescription |
| `quantity_dispensed` | integer | Yes | > 0, <= prescribed quantity |
| `batch_number` | string | Yes | Stock batch identifier |
| `expiry_date` | date | Yes | Must not be in the past |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `dispensed_quantity` | integer | Quantity dispensed |
| `pending_balance` | integer | Remaining quantity (0 if fully dispensed) |
| `stock_remaining` | integer | Drug stock after dispensing |
| `label_url` | string | Printable dispensing label URL |
| `billing_charge_id` | integer | Auto-posted billing line |

- **Status codes:**

| Code | Condition |
|------|-----------|
| 200 | Dispensed successfully |
| 404 | Prescription not found |
| 409 | `BATCH_EXPIRED` (expired batch) |
| 422 | Validation error, insufficient stock |

---

#### POST /api/v1/pharmacy/substitute

- **FR:** FR-PHR-003
- **Description:** Generic substitution for a branded drug prescription. Notifies the prescribing doctor.
- **Auth:** S/J (Pharmacist)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `prescription_id` | integer | Yes | Branded drug prescription |
| `substitute_drug_id` | integer | Yes | Generic equivalent from formulary |
| `reason` | string | Yes | Max 500 chars |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `original_drug` | string | Original branded drug name |
| `substitute_drug` | string | Generic substitute name |
| `doctor_notified` | boolean | Notification sent to prescriber |

- **Status codes:** 200, 404, 422.

---

#### GET /api/v1/pharmacy/stock

- **FR:** FR-PHR-007, FR-PHR-009
- **Description:** Current stock levels for all drugs in the pharmacy. Includes minimum stock alerts, expiry flags, and stock valuation.
- **Auth:** S/J (Pharmacist, Store Keeper, Facility Admin)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `drug_id` | integer | No | Filter by drug |
| `store_id` | integer | No | Filter by store (main, ward, etc.) |
| `alert` | enum | No | `low_stock`, `expiring`, `expired` |
| `page` | integer | No | Default 1 |
| `per_page` | integer | No | Default 25 |

- **Response (200):** Paginated list of stock items with drug name, batch, quantity, expiry, minimum level, alert status, and valuation.
- **Status codes:** 200.

---

#### POST /api/v1/pharmacy/stock/grn

- **FR:** FR-PHR-007
- **Description:** Record a Goods Received Note (GRN). Increases stock balance.
- **Auth:** S/J (Pharmacist, Store Keeper)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `drug_id` | integer | Yes | Must exist in formulary |
| `supplier` | string | Yes | Max 200 chars |
| `invoice_number` | string | Yes | Max 100 chars |
| `batch_number` | string | Yes | Max 50 chars |
| `expiry_date` | date | Yes | Must be in the future |
| `quantity` | integer | Yes | > 0 |
| `unit_cost` | decimal | Yes | >= 0 |

- **Response (201):** Created GRN record with updated stock balance.
- **Status codes:** 201, 422.

---

#### POST /api/v1/pharmacy/stock/transfer

- **FR:** FR-PHR-007
- **Description:** Transfer stock between stores (e.g., main pharmacy to ward pharmacy). Receiving store must acknowledge receipt.
- **Auth:** S/J (Pharmacist, Store Keeper)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `drug_id` | integer | Yes | Must exist in formulary |
| `batch_number` | string | Yes | Must exist in source store |
| `quantity` | integer | Yes | > 0, <= available in source |
| `source_store_id` | integer | Yes | Source store |
| `destination_store_id` | integer | Yes | Destination store |

- **Response (201):** Transfer record with source and destination balances.
- **Status codes:** 201, 422 (insufficient stock).

---

#### POST /api/v1/pharmacy/stock/adjust

- **FR:** FR-PHR-007
- **Description:** Stock adjustment with documented reason (breakage, expiry, theft, count correction). Approval required for adjustments exceeding facility threshold.
- **Auth:** S/J (Pharmacist, Store Keeper)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `drug_id` | integer | Yes | Must exist in formulary |
| `batch_number` | string | Yes | Must exist in store |
| `quantity_change` | integer | Yes | Positive (increase) or negative (decrease) |
| `reason` | string | Yes | `breakage`, `expiry`, `theft`, `count_correction`, `other` |
| `notes` | string | No | Max 500 chars |

- **Response (200):** Adjustment record with updated stock balance.
- **Status codes:** 200, 422, 403 (requires approval if above threshold).

---

#### GET /api/v1/pharmacy/expiring

- **FR:** FR-PHR-008
- **Description:** Drugs expiring within 90 days or already expired.
- **Auth:** S/J (Pharmacist, Store Keeper)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `days` | integer | No | Default 90, look-ahead window |
| `store_id` | integer | No | Filter by store |

- **Response (200):** List of expiring/expired stock with drug name, batch, expiry date, quantity, and status (`expiring_soon` or `expired`).
- **Status codes:** 200.

---

#### GET /api/v1/pharmacy/formulary

- **FR:** FR-PHR-010
- **Description:** Facility drug formulary listing all active drugs with ATC codes, dosage forms, strengths, LASA flags, and interaction profiles.
- **Auth:** S/J
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `q` | string | No | Search by generic name, brand name, or ATC code |
| `drug_class` | string | No | Filter by drug class |
| `page` | integer | No | Default 1 |
| `per_page` | integer | No | Default 25 |

- **Response (200):** Paginated list of formulary entries.
- **Status codes:** 200.

---

#### POST /api/v1/pharmacy/formulary

- **FR:** FR-PHR-010
- **Description:** Add or update a drug in the facility formulary.
- **Auth:** S/J (Pharmacist, Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `generic_name` | string | Yes | Max 200 chars |
| `brand_names` | array | No | Array of brand name strings |
| `atc_code` | string | No | ATC classification code |
| `drug_class` | string | No | e.g., "Penicillins" |
| `dosage_forms` | array | No | e.g., `["tablet", "capsule"]` |
| `strengths` | array | No | e.g., `["250mg", "500mg"]` |
| `routes` | array | No | Valid administration routes |
| `max_dose` | decimal | No | Maximum single dose |
| `lasa_flag` | boolean | No | Tall Man Lettering required |

- **Response (201):** Created/updated formulary entry.
- **Status codes:** 201, 403, 422.

---

#### POST /api/v1/pharmacy/narcotic

- **FR:** FR-PHR-011
- **Description:** Record a narcotic/controlled drug register entry. Immutable. Tracks running balance per controlled substance with witness.
- **Auth:** S/J (Pharmacist)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `prescription_id` | integer | Yes | Linked prescription |
| `drug_id` | integer | Yes | Controlled substance |
| `quantity_dispensed` | integer | Yes | > 0 |
| `witness_name` | string | Yes | 2-100 chars |
| `physical_count` | integer | No | If provided, compared to system balance |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `entry_id` | integer | Register entry ID |
| `running_balance` | integer | System balance after dispensing |
| `discrepancy` | boolean | `true` if physical count differs from system |

- **Status codes:** 201, 422.

---

#### POST /api/v1/pharmacy/drug-round

- **FR:** FR-PHR-006
- **Description:** Record an inpatient medication administration event (drug round).
- **Auth:** S/J (Nurse)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `prescription_id` | integer | Yes | Active inpatient prescription |
| `scheduled_time` | datetime | Yes | Scheduled dose time |
| `status` | enum | Yes | `given`, `held`, `refused`, `not_given` |
| `reason` | string | Conditional | Required if status is `held`, `refused`, or `not_given` |

- **Response (201):** MAR entry record.
- **Status codes:** 201, 404, 422.

---

#### POST /api/v1/pharmacy/medication-reconciliation

- **FR:** FR-PHR-015
- **Description:** Record medication reconciliation at a transition of care. Lists all active medications; receiving clinician must confirm.
- **Auth:** S/J (Doctor, Clinical Officer, Nurse)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `patient_uid` | UUID | Yes | Patient UID |
| `transition_type` | enum | Yes | `opd_to_ipd`, `ward_transfer`, `ipd_to_discharge`, `facility_referral` |
| `medications[]` | array | Yes | Active medications with review status |
| `medications[].drug_id` | integer | Yes | Drug identifier |
| `medications[].action` | enum | Yes | `continue`, `discontinue`, `modify` |
| `medications[].new_dose` | string | Conditional | If `action = modify` |

- **Response (200):** Reconciliation record; transition unblocked.
- **Status codes:** 200, 404, 422 (`RECONCILIATION_REQUIRED`).

---

### 2.7 Billing (FR-BIL)

#### GET /api/v1/billing/accounts/{patient_uid}

- **FR:** FR-BIL-001
- **Description:** Retrieve the patient's billing account with real-time running balance and itemised charges.
- **Auth:** S/J (Cashier, Doctor, Nurse, Facility Admin)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `date_from` | date | No | Filter charges by date |
| `date_to` | date | No | Filter charges by date |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `patient_uid` | UUID | Patient UID |
| `balance` | decimal | Outstanding balance |
| `charges[]` | array | Itemised billing lines |
| `charges[].description` | string | Service description |
| `charges[].amount` | decimal | Charge amount |
| `charges[].source` | string | Module that posted the charge |
| `charges[].created_at` | datetime | Charge timestamp |
| `payments[]` | array | Payment records |
| `category_pricing` | string | Applied pricing tier |

- **Status codes:** 200, 404.

---

#### POST /api/v1/billing/charges

- **FR:** FR-BIL-004, FR-BIL-001
- **Description:** Manually add a billing charge (for services not auto-billed). Links to price list for amount calculation. Category pricing applied automatically.
- **Auth:** S/J (Cashier, Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `patient_uid` | UUID | Yes | Valid patient |
| `service_code` | string | Yes | Must exist in facility price list |
| `quantity` | integer | No | Default 1 |
| `notes` | string | No | Max 500 chars |

- **Response (201):** Created billing line with computed amount.
- **Status codes:** 201, 404, 422.

---

#### POST /api/v1/billing/payments

- **FR:** FR-BIL-006
- **Description:** Record a cash payment. Calculates change, supports partial payments, generates a receipt (FR-BIL-005).
- **Auth:** S/J (Cashier)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `patient_uid` | UUID | Yes | Valid patient |
| `amount_tendered` | decimal | Yes | > 0 |
| `payment_method` | enum | Yes | `cash`, `card` |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `payment_id` | integer | Payment record ID |
| `amount_paid` | decimal | Applied to balance |
| `change_due` | decimal | Change returned |
| `new_balance` | decimal | Updated outstanding balance |
| `receipt_url` | string | Printable receipt URL |
| `receipt_number` | string | Unique receipt number |

- **Status codes:** 200, 404, 422.

---

#### POST /api/v1/billing/payments/momo

- **FR:** FR-BIL-007
- **Description:** Initiate a mobile money payment (MTN MoMo or Airtel Money). Sends a payment request to the patient's phone via the mobile money API.
- **Auth:** S/J (Cashier)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `patient_uid` | UUID | Yes | Valid patient |
| `amount` | decimal | Yes | > 0 |
| `phone_number` | string | Yes | E.164 format |
| `provider` | enum | Yes | `mtn_momo`, `airtel_money` |

- **Response (202):**

| Field | Type | Description |
|-------|------|-------------|
| `transaction_ref` | string | Mobile money transaction reference |
| `status` | string | `pending` (awaiting patient confirmation) |

- **Callback:** On payment confirmation, the system auto-matches to the patient account, updates balance, and generates a receipt. Unmatched payments go to the suspense account.
- **Status codes:** 202 (accepted, pending confirmation), 404, 422.

---

#### GET /api/v1/billing/receipts/{id}

- **FR:** FR-BIL-005
- **Description:** Retrieve or reprint a receipt. Reprints are marked "REPRINT".
- **Auth:** S/J (Cashier, Facility Admin)
- **Response (200):** Receipt object with facility name, receipt number, patient details, itemised services, payment details, and cashier name.
- **Status codes:** 200, 404.

---

#### POST /api/v1/billing/reconciliation

- **FR:** FR-BIL-008
- **Description:** Submit daily cashier reconciliation. Flags discrepancies exceeding UGX 5,000.
- **Auth:** S/J (Cashier)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `opening_float` | decimal | Yes | >= 0 |
| `cash_collections` | decimal | Yes | >= 0 |
| `momo_collections` | decimal | Yes | >= 0 |
| `airtel_collections` | decimal | Yes | >= 0 |
| `card_collections` | decimal | Yes | >= 0 |
| `banking_amount` | decimal | Yes | >= 0 |
| `closing_float` | decimal | Yes | >= 0 |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `expected_total` | decimal | System-calculated total |
| `actual_total` | decimal | Submitted total |
| `discrepancy` | decimal | Difference |
| `flagged` | boolean | `true` if discrepancy > UGX 5,000 |

- **Status codes:** 200, 422.

---

#### GET /api/v1/billing/missing-charges

- **FR:** FR-BIL-009
- **Description:** Missing charge detection report. Compares clinical encounters against billing records.
- **Auth:** S/J (Cashier, Facility Admin, Auditor)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `date` | date | No | Default today |

- **Response (200):** Array of encounters with no corresponding billing charge (patient name, MRN, encounter type, date, expected charge).
- **Status codes:** 200.

---

#### POST /api/v1/billing/credits

- **FR:** FR-BIL-010
- **Description:** Create or update a credit arrangement for a patient, staff member, corporation, or mission.
- **Auth:** S/J (Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `debtor_name` | string | Yes | 2-200 chars |
| `debtor_type` | enum | Yes | `staff`, `corporate`, `mission` |
| `credit_limit` | decimal | Yes | > 0 |

- **Response (201):** Created credit arrangement record.
- **Status codes:** 201, 403, 422.

---

#### GET /api/v1/billing/pricelist

- **FR:** FR-BIL-002
- **Description:** Retrieve the facility price list, organised by service category.
- **Auth:** S/J
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `category` | string | No | `consultation`, `laboratory`, `radiology`, `pharmacy`, `procedures`, `bed_charges`, `misc` |
| `q` | string | No | Search by service name |

- **Response (200):** Paginated price list entries with service name, code, base price, and effective date.
- **Status codes:** 200.

---

#### POST /api/v1/billing/pricelist

- **FR:** FR-BIL-002
- **Description:** Create or update a price list entry.
- **Auth:** S/J (Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `service_name` | string | Yes | Max 200 chars |
| `service_code` | string | Yes | Unique per facility |
| `category` | enum | Yes | Service category |
| `base_price` | decimal | Yes | >= 0 |
| `effective_date` | date | Yes | ISO 8601 |

- **Response (201):** Created/updated price list entry.
- **Status codes:** 201, 403, 422.

---

### 2.8 Appointments (FR-APT)

#### POST /api/v1/appointments

- **FR:** FR-APT-001
- **Description:** Book an appointment. Checks doctor availability (FR-APT-003). Sends SMS confirmation and schedules a 24-hour reminder.
- **Auth:** S/J (Receptionist, Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `patient_uid` | UUID | Yes | Valid patient |
| `department` | string | Yes | Valid department |
| `doctor_id` | integer | No | Defaults to any available doctor |
| `appointment_date` | datetime | Yes | Must be in the future |
| `appointment_type` | enum | Yes | `first_visit`, `follow_up`, `procedure` |

- **Response (201):**

| Field | Type | Description |
|-------|------|-------------|
| `appointment_id` | integer | Appointment record ID |
| `status` | string | `booked` |
| `sms_sent` | boolean | Confirmation SMS sent |

- **Status codes:** 201, 409 (slot taken, `suggested_alternatives[]` returned), 422.

---

#### GET /api/v1/appointments

- **FR:** FR-APT-001
- **Description:** List appointments with filters.
- **Auth:** S/J
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `patient_uid` | UUID | No | Filter by patient |
| `doctor_id` | integer | No | Filter by doctor |
| `date_from` | date | No | ISO 8601 |
| `date_to` | date | No | ISO 8601 |
| `status` | enum | No | `booked`, `arrived`, `completed`, `cancelled`, `no_show` |
| `page` | integer | No | Default 1 |
| `per_page` | integer | No | Default 25 |

- **Response (200):** Paginated list of appointments.
- **Status codes:** 200.

---

#### PATCH /api/v1/appointments/{id}

- **FR:** FR-APT-001
- **Description:** Reschedule or cancel an appointment.
- **Auth:** S/J (Receptionist, Doctor)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `appointment_date` | datetime | No | Must be in the future (reschedule) |
| `status` | enum | No | `cancelled` |
| `cancellation_reason` | string | Conditional | Required if cancelling |

- **Response (200):** Updated appointment record.
- **Status codes:** 200, 404, 409 (new slot taken), 422.

---

#### GET /api/v1/appointments/calendar/{doctor_id}

- **FR:** FR-APT-003
- **Description:** Doctor availability calendar showing available, booked, blocked, and walk-in slots.
- **Auth:** S/J
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `date_from` | date | No | Default today |
| `date_to` | date | No | Default today + 30 days |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `doctor_id` | integer | Doctor ID |
| `schedule` | object | Working days, start/end times, slot duration |
| `slots[]` | array | Date, time, status (`available`, `booked`, `blocked`, `walk_in`) |

- **Status codes:** 200, 404.

---

#### POST /api/v1/appointments/{id}/arrive

- **FR:** FR-APT-004
- **Description:** Mark a booked appointment as arrived. Adds patient to the OPD triage queue.
- **Auth:** S/J (Receptionist)
- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | `arrived` |
| `queue_position` | integer | Position in triage queue |

- **Status codes:** 200, 404, 422 (already arrived or completed).

---

### 2.9 RBAC and Audit (FR-RBAC)

#### GET /api/v1/roles

- **FR:** FR-RBAC-001, FR-RBAC-002
- **Description:** List all roles (built-in and custom) available to the facility.
- **Auth:** S/J (Facility Admin)
- **Response (200):** Array of role objects with `id`, `name`, `type` (`built_in` or `custom`), `permission_count`, and `user_count`.
- **Status codes:** 200, 403.

---

#### POST /api/v1/roles

- **FR:** FR-RBAC-002
- **Description:** Create a custom role scoped to the current facility. Custom roles cannot exceed Facility Admin permissions.
- **Auth:** S/J (Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `role_name` | string | Yes | 2-50 chars, unique per facility |
| `permissions` | array | Yes | Valid permission identifiers |
| `description` | string | No | Max 200 chars |

- **Response (201):** Created role with assigned permissions.
- **Status codes:** 201, 403, 409 (duplicate name), 422.

---

#### GET /api/v1/roles/{id}/permissions

- **FR:** FR-RBAC-001
- **Description:** List all permissions assigned to a role.
- **Auth:** S/J (Facility Admin)
- **Response (200):** Array of permission objects with `id`, `module`, `action`, and `description`.
- **Status codes:** 200, 403, 404.

---

#### POST /api/v1/users/{id}/roles

- **FR:** FR-RBAC-001
- **Description:** Assign a role to a user.
- **Auth:** S/J (Facility Admin)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `role_id` | integer | Yes | Valid role within the facility |

- **Response (200):** Updated user with assigned role.
- **Status codes:** 200, 403, 404, 422.

---

#### GET /api/v1/audit-trail

- **FR:** FR-RBAC-005
- **Description:** Query the immutable audit trail. Entries cannot be modified or deleted.
- **Auth:** S/J (Facility Admin, Auditor)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `user_id` | integer | No | Filter by user |
| `action` | enum | No | `CREATE`, `UPDATE`, `DELETE`, `VIEW` |
| `resource_type` | string | No | e.g., `patient`, `encounter`, `prescription` |
| `date_from` | datetime | No | ISO 8601 |
| `date_to` | datetime | No | ISO 8601 |
| `page` | integer | No | Default 1 |
| `per_page` | integer | No | Default 25 |

- **Response (200):** Paginated audit log entries with `user_id`, `facility_id`, `action`, `resource_type`, `resource_id`, `old_value`, `new_value`, `ip_address`, `user_agent`, and `timestamp`.
- **Status codes:** 200, 403.

---

#### POST /api/v1/emergency-access

- **FR:** FR-RBAC-006
- **Description:** Invoke emergency access to a cross-facility patient's clinical records. Requires name + DOB verification. Reveals limited clinical data. Expires after 24 hours. Sends SMS notification to the patient.
- **Auth:** S/J (Doctor, Clinical Officer)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `patient_uid` | UUID | Yes | Global patient UID |
| `patient_name` | string | Yes | Must match recorded name |
| `date_of_birth` | date | Yes | Must match recorded DOB |
| `reason` | string | Yes | Min 20 chars |

- **Response (200):**

| Field | Type | Description |
|-------|------|-------------|
| `allergies` | array | Patient allergies |
| `current_medications` | array | Active medications |
| `blood_group` | string | Blood group |
| `hiv_status` | string | Only if prior consent was given |
| `recent_diagnoses` | array | Last 3 diagnoses |
| `expires_at` | datetime | Access expiry (24 hours) |

- **Status codes:** 200, 403 (name/DOB mismatch), 404.

---

#### POST /api/v1/break-the-glass

- **FR:** FR-RBAC-007
- **Description:** Break-the-glass access to a restricted record (VIP, sensitive diagnosis) within the same facility. Grants temporary read-only access. Notifies Facility Admin.
- **Auth:** S/J (clinician roles)
- **Request body:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `patient_uid` | UUID | Yes | Restricted patient UID |
| `resource_type` | string | Yes | e.g., `diagnosis`, `prescription` |
| `reason` | string | Yes | Min 20 chars |

- **Response (200):** Restricted record data (read-only).
- **Status codes:** 200, 403, 404, 422 (reason too short).

---

#### GET /api/v1/users/{id}/sessions

- **FR:** FR-RBAC-004
- **Description:** List active sessions for a user (device type, IP, last activity).
- **Auth:** S/J (user themselves, Facility Admin)
- **Response (200):** Array of session objects.
- **Status codes:** 200, 403, 404.

---

#### DELETE /api/v1/users/{id}/sessions/{session_id}

- **FR:** FR-RBAC-004
- **Description:** Revoke a specific active session.
- **Auth:** S/J (user themselves, Facility Admin)
- **Response (200):** `{"success": true}`
- **Status codes:** 200, 403, 404.

---

### 2.10 FHIR R4 Interoperability

FHIR endpoints serve standardised clinical resources for interoperability with external systems, government health information exchanges, and SMART on FHIR third-party applications. All FHIR responses include an HTML narrative fallback.

---

#### GET /api/v1/fhir/Patient/{id}

- **FR:** FR-REG-001 (FHIR representation)
- **Description:** FHIR R4 Patient resource. Maps Medic8 patient demographics to the FHIR Patient resource structure.
- **Auth:** J (SMART on FHIR scope: `patient/*.read`)
- **Response (200):** FHIR Patient resource (JSON, `application/fhir+json`).
- **Status codes:** 200, 404.

---

#### GET /api/v1/fhir/Encounter/{id}

- **FR:** FR-OPD-003 (FHIR representation)
- **Description:** FHIR R4 Encounter resource. Maps OPD/IPD encounters.
- **Auth:** J (SMART on FHIR scope: `patient/Encounter.read`)
- **Response (200):** FHIR Encounter resource.
- **Status codes:** 200, 404.

---

#### GET /api/v1/fhir/Observation

- **FR:** FR-OPD-001, FR-LAB-004 (FHIR representation)
- **Description:** FHIR R4 Observation resources (vitals, lab results).
- **Auth:** J (SMART on FHIR scope: `patient/Observation.read`)
- **Request parameters:**

| Parameter | Type | Required | Constraints |
|-----------|------|----------|-------------|
| `patient` | string | Yes | Patient FHIR ID |
| `category` | string | No | `vital-signs`, `laboratory` |
| `code` | string | No | LOINC code |
| `date` | string | No | FHIR date search parameter |

- **Response (200):** FHIR Bundle of Observation resources.
- **Status codes:** 200.

---

#### GET /api/v1/fhir/Condition/{id}

- **FR:** FR-OPD-004 (FHIR representation)
- **Description:** FHIR R4 Condition resource. Maps ICD-10/ICD-11 diagnoses.
- **Auth:** J (SMART on FHIR scope: `patient/Condition.read`)
- **Response (200):** FHIR Condition resource.
- **Status codes:** 200, 404.

---

#### GET /api/v1/fhir/MedicationRequest/{id}

- **FR:** FR-OPD-006 (FHIR representation)
- **Description:** FHIR R4 MedicationRequest resource. Maps prescriptions.
- **Auth:** J (SMART on FHIR scope: `patient/MedicationRequest.read`)
- **Response (200):** FHIR MedicationRequest resource.
- **Status codes:** 200, 404.

---

#### GET /api/v1/fhir/MedicationDispense/{id}

- **FR:** FR-PHR-002 (FHIR representation)
- **Description:** FHIR R4 MedicationDispense resource. Maps dispensing records.
- **Auth:** J (SMART on FHIR scope: `patient/MedicationDispense.read`)
- **Response (200):** FHIR MedicationDispense resource.
- **Status codes:** 200, 404.

---

#### GET /api/v1/fhir/DiagnosticReport/{id}

- **FR:** FR-LAB-004 (FHIR representation)
- **Description:** FHIR R4 DiagnosticReport resource. Maps lab and radiology reports.
- **Auth:** J (SMART on FHIR scope: `patient/DiagnosticReport.read`)
- **Response (200):** FHIR DiagnosticReport resource.
- **Status codes:** 200, 404.

---

#### GET /api/v1/fhir/Immunization/{id}

- **FR:** FR-IMM (FHIR representation, Phase 2 data)
- **Description:** FHIR R4 Immunization resource. Maps vaccination records.
- **Auth:** J (SMART on FHIR scope: `patient/Immunization.read`)
- **Response (200):** FHIR Immunization resource.
- **Status codes:** 200, 404.

---

#### GET /api/v1/fhir/AllergyIntolerance/{id}

- **FR:** FR-REG-007 (FHIR representation)
- **Description:** FHIR R4 AllergyIntolerance resource. Maps patient allergy records.
- **Auth:** J (SMART on FHIR scope: `patient/AllergyIntolerance.read`)
- **Response (200):** FHIR AllergyIntolerance resource.
- **Status codes:** 200, 404.

---

#### GET /api/v1/fhir/metadata

- **Description:** FHIR Capability Statement. Declares supported resources, operations, search parameters, and security configuration (SMART on FHIR).
- **Auth:** P (public)
- **Response (200):** FHIR CapabilityStatement resource.
- **Status codes:** 200.

---

## 3. Error Response Format

### 3.1 Standard HTTP Error Codes

| HTTP Code | Error Code | Meaning |
|-----------|-----------|---------|
| 400 | `BAD_REQUEST` | Malformed request syntax |
| 401 | `UNAUTHENTICATED` | No valid session or token |
| 401 | `TOKEN_EXPIRED` | Access token expired |
| 401 | `TOKEN_REVOKED` | Refresh token revoked |
| 403 | `FORBIDDEN` | Authenticated but insufficient permission |
| 403 | `TENANT_SUSPENDED` | Facility account suspended |
| 403 | `ACCOUNT_LOCKED` | User account locked after failed login attempts |
| 404 | `NOT_FOUND` | Resource not found |
| 409 | `CONFLICT` | State conflict (duplicate, merge conflict) |
| 409 | `DUPLICATE_DETECTED` | EMPI duplicate patient match |
| 422 | `VALIDATION_ERROR` | Request body failed validation |
| 429 | `RATE_LIMITED` | Rate limit exceeded (60 req/min) |
| 500 | `SERVER_ERROR` | Unexpected server error |

### 3.2 Healthcare-Specific Error Codes

| HTTP Code | Error Code | Meaning |
|-----------|-----------|---------|
| 460 | `CDS_ALERT` | Clinical Decision Support alert — drug interaction (Tier 3/4) |
| 461 | `PRESCRIBING_AUTHORITY_VIOLATION` | User role lacks prescribing authority (BR-CLIN-002) |
| 462 | `TENANT_ISOLATION_VIOLATION` | Cross-tenant data access attempted without authorisation (BR-DATA-004) |

### 3.3 Domain-Specific Validation Codes

| Error Code | Context | Meaning |
|-----------|---------|---------|
| `CSRF_INVALID` | Auth | CSRF token mismatch |
| `INVALID_CREDENTIALS` | Auth | Email or password incorrect |
| `MFA_INVALID` | Auth | TOTP code incorrect |
| `MFA_EXPIRED` | Auth | TOTP window expired |
| `CONTACT_REQUIRED` | Registration | No phone or address provided |
| `INVALID_DOB` | Registration | Date of birth in the future |
| `GUARDIAN_REQUIRED` | OPD | Paediatric patient missing guardian |
| `ICD_CODE_REQUIRED` | Diagnosis | Free-text diagnosis without ICD code |
| `DRUG_NOT_IN_FORMULARY` | Prescription | Drug not in facility formulary |
| `DOSE_EXCEEDS_MAXIMUM` | Prescription | Dose exceeds therapeutic maximum |
| `INVALID_ROUTE` | Prescription | Invalid administration route for drug |
| `WEIGHT_REQUIRED` | Prescription | Paediatric patient missing weight (BR-CLIN-006) |
| `RECONCILIATION_REQUIRED` | Transitions | Medication reconciliation not completed |
| `QC_OUT_OF_CONTROL` | Lab | Assay QC failed Westgard rules |
| `BATCH_EXPIRED` | Pharmacy | Dispensing from expired batch blocked |
| `CREDIT_LIMIT_EXCEEDED` | Billing | Credit arrangement limit reached |
| `UNMERGE_WINDOW_EXPIRED` | Registration | 30-day unmerge window has passed |

---

## 4. Phase 2-4 Endpoint Summary

The following endpoint groups are planned for future phases. Detailed specifications will be expanded at the start of each phase.

### Phase 2 — Expansion

| Module | Endpoint Group Prefix | Key Operations |
|--------|-----------------------|----------------|
| Inpatient (FR-IPD) | `/api/v1/admissions`, `/api/v1/wards`, `/api/v1/beds` | Admission, bed management, nursing notes, ward rounds, drug rounds, transfers, discharge |
| Maternity (FR-MAT) | `/api/v1/anc`, `/api/v1/deliveries` | ANC registration, visit recording, partograph, delivery, newborn linkage, PMTCT, PNC |
| Immunisation (FR-IMM) | `/api/v1/immunisations` | EPI schedule, vaccine recording, missed dose alerts, AEFI, DHIS2 Tracker upload |
| Insurance (FR-INS) | `/api/v1/insurance` | Scheme register, member verification, pre-authorisation, claim generation, rejection management |
| HMIS (FR-HMIS) | `/api/v1/hmis` | HMIS 105/108/033b auto-generation, DHIS2 upload, PEPFAR MER indicators |
| HR (FR-HR) | `/api/v1/staff`, `/api/v1/payroll` | Staff registry, licence tracking, payroll, duty roster |
| Inventory | `/api/v1/inventory` | Multi-store GRN, transfer, adjustment, NMS ordering, procurement |
| Emergency (A&E) | `/api/v1/emergency` | Rapid triage, emergency registration, resuscitation record, mass casualty |
| Radiology | `/api/v1/radiology` | Worklist, report entry, PACS/DICOM integration |

### Phase 3 — Programmes and Patient Engagement

| Module | Endpoint Group Prefix | Key Operations |
|--------|-----------------------|----------------|
| HIV/AIDS (FR-HIV) | `/api/v1/hiv` | HTS, ART initiation, ARV dispensing, viral load tracking, PMTCT, PEPFAR indicators |
| TB (FR-TB) | `/api/v1/tb` | Case registration, treatment regimen, DOT tracking, contact tracing, NTLP reporting |
| Patient Portal (FR-PAT) | `/api/v1/portal` | Personal health record, test results, appointments, billing, medication reminders |
| Community Health | `/api/v1/community` | VHT records, community referrals, CHW app sync |
| Nutrition | `/api/v1/nutrition` | Nutritional assessment, SAM/MAM, CMAM, RUTF tracking |

### Phase 4 — Advanced Specialty

| Module | Endpoint Group Prefix | Key Operations |
|--------|-----------------------|----------------|
| Theatre (Surgery) | `/api/v1/theatre` | Theatre booking, operation notes, anaesthesia record, surgical count |
| Blood Bank | `/api/v1/blood-bank` | Blood request, cross-match, issue, transfusion reaction, UBTS integration |
| Physiotherapy | `/api/v1/physio` | Referral, assessment, treatment plan, session tracking |
| Ambulance | `/api/v1/ambulance` | Fleet register, trip log, pre-hospital care, GPS tracking |

---

## 5. File Structure

Future API specification files in this directory will follow this structure:

| File | Endpoints Covered | FR Groups |
|------|-------------------|-----------|
| `00-index.md` | Overview, registry, and error codes | All |
| `01-auth.yaml` | Authentication and session management | FR-AUTH-001 -- FR-AUTH-006 |
| `02-tenants.yaml` | Tenant lifecycle (Super Admin) | FR-TNT-001 -- FR-TNT-004 |
| `03-patients.yaml` | Patient registration and identity | FR-REG-001 -- FR-REG-011 |
| `04-opd.yaml` | Outpatient encounters | FR-OPD-001 -- FR-OPD-015 |
| `05-laboratory.yaml` | Laboratory Information System | FR-LAB-001 -- FR-LAB-010 |
| `06-pharmacy.yaml` | Pharmacy and dispensary | FR-PHR-001 -- FR-PHR-015 |
| `07-billing.yaml` | Billing and revenue | FR-BIL-001 -- FR-BIL-010 |
| `08-appointments.yaml` | Appointments and scheduling | FR-APT-001 -- FR-APT-005 |
| `09-rbac-audit.yaml` | RBAC, audit trail, emergency access | FR-RBAC-001 -- FR-RBAC-007 |
| `10-fhir.yaml` | FHIR R4 interoperability layer | Cross-cutting |
| `11-schemas.yaml` | Shared reusable components and schemas | All |
