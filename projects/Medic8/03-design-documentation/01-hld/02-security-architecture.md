# Security Architecture — Medic8

**Document ID:** DD-01-02
**Project:** Medic8
**Author:** Chwezi Core Systems
**Date:** 2026-04-03
**Version:** 1.0
**Status:** Draft — Pending Consultant Review

---

## 1. Authentication

### 1.1 Dual Authentication Strategy

Medic8 operates two authentication mechanisms in parallel, matched to client type:

| Client | Mechanism | Token Type | Storage |
|---|---|---|---|
| Web UI (staff, patient portal) | Session-based | Laravel session cookie (encrypted, HttpOnly, SameSite=Lax) | Server-side session store (Redis) |
| Android app | JWT | Bearer token in `Authorization` header | EncryptedSharedPreferences |
| iOS app | JWT | Bearer token in `Authorization` header | Keychain |
| FHIR/API clients | JWT | Bearer token in `Authorization` header | Client-managed |
| SMART on FHIR apps | OAuth 2.0 | Access token + refresh token | Client-managed |

**Session authentication (web):**

1. User submits username + password via HTTPS POST
2. Server validates credentials against `users` table (password hashed with bcrypt, cost factor 12)
3. If MFA is required for the role (Section 1.2), server returns MFA challenge
4. On success, server creates a session, stores `user_id`, `facility_id`, `role`, `permissions[]` in the session
5. Session ID returned as an encrypted cookie
6. CSRF token generated and bound to the session; every state-changing request must include the CSRF token

**JWT authentication (mobile/API):**

1. Client sends credentials to `POST /api/v1/auth/login`
2. Server validates credentials, returns an access token (15-minute expiry) and a refresh token (7-day expiry)
3. Access token payload: `user_id`, `facility_id`, `role`, `iat`, `exp`
4. Refresh token is stored in the `refresh_tokens` table with a hash; each use invalidates the previous refresh token and issues a new pair (rotation)
5. If the same refresh token is used twice (replay detection), all tokens for that user are invalidated and the user must re-authenticate

### 1.2 Multi-Factor Authentication (NFR-HC-005)

| Role | MFA Requirement | Supported Methods |
|---|---|---|
| Super Admin | Mandatory | TOTP (authenticator app) |
| Facility Admin | Mandatory | TOTP, SMS OTP (Africa's Talking), Email OTP |
| Accountant | Mandatory | TOTP, SMS OTP, Email OTP |
| Auditor | Mandatory | TOTP, SMS OTP, Email OTP |
| Doctor, Clinical Officer, Nurse, Pharmacist, Lab Technician, Radiographer | Optional | TOTP, SMS OTP, Email OTP |
| Receptionist, Cashier, Insurance Clerk, Store Keeper, Records Officer | Optional | TOTP, SMS OTP, Email OTP |
| Patient | Optional | SMS OTP |
| CHW | Optional | SMS OTP |

**TOTP implementation:** RFC 6238 compliant. Secret stored encrypted (AES-256-GCM) in the `users` table. QR code generated for authenticator app enrolment. Recovery codes (10, single-use) generated at enrolment and displayed once.

**SMS OTP fallback:** If SMS delivery fails (Africa's Talking returns non-200), the system falls back to email OTP within 30 seconds. If both fail, the user is directed to contact their Facility Admin.

### 1.3 Session Timeout (NFR-HC-004)

- Inactive session timeout: **15 minutes**
- Warning prompt at **13 minutes** of inactivity, giving 2 minutes to extend
- Auto-saved form data is preserved across session timeouts and restored on re-authentication (see NFR-HC-016)
- Active session timeout: **12 hours** (maximum session duration regardless of activity)
- Concurrent session limit: configurable per role (default: 1 for clinical staff, 3 for Super Admin)

### 1.4 Device-Level Session Management

Each authenticated session records:

- `session_id`
- `user_id`
- `facility_id`
- `device_fingerprint` (user agent + screen resolution hash for web; device ID for mobile)
- `ip_address`
- `login_timestamp`
- `last_activity_timestamp`

Users can view and terminate their active sessions from the profile page. Facility Admins can view and terminate all sessions for users within their facility. Super Admins can terminate any session platform-wide.

---

## 2. Authorization (RBAC + ABAC)

### 2.1 Role-Based Access Control (RBAC)

Medic8 ships with **18 built-in roles** (see RBAC Permission Matrix, DD-REQ-03-01). Each role maps to a set of permissions. Permissions are granular and follow the pattern `module.action` (e.g., `opd.create_consultation`, `pharmacy.dispense_drug`, `billing.collect_payment`).

**Permission resolution at login:**

1. User authenticates
2. Server loads the user's role(s) from the `user_roles` table
3. For each role, the server loads all permissions from `role_permissions`
4. Permissions are merged (union) and cached in Redis with key `permissions:{user_id}:{facility_id}`, TTL 15 minutes
5. The cached permission set is checked on every API request by the `CheckPermission` middleware

**Custom roles:** Facility Admins may create unlimited custom roles per facility. A custom role may contain any subset of the permissions held by the Facility Admin role. Custom roles are tenant-scoped (stored with `facility_id`).

### 2.2 Attribute-Based Access Control (ABAC) — NFR-HC-010

ABAC applies an additional access layer on top of RBAC for sensitive data categories:

| Sensitive Category | ABAC Policy | Visible To |
|---|---|---|
| HIV status | `sensitive_record` permission AND active treatment relationship | Treating clinician only |
| Mental health diagnoses | `sensitive_record` permission AND active treatment relationship | Treating clinician only |
| Substance abuse records | `sensitive_record` permission AND active treatment relationship | Treating clinician only |
| Reproductive health records | `sensitive_record` permission AND active treatment relationship | Treating clinician only |

**Implementation:**

1. Sensitive data fields are stored with a `sensitivity_category` column (enum: `hiv`, `mental_health`, `substance_abuse`, `reproductive_health`, `none`)
2. The `SensitiveRecordPolicy` middleware intercepts read requests for records where `sensitivity_category != 'none'`
3. The policy checks:
   - Does the requesting user have the `sensitive_record` permission? (RBAC check)
   - Does the requesting user have an active treatment relationship with this patient? (ABAC check — verified via `treatment_relationships` table: `user_id`, `patient_id`, `facility_id`, `start_date`, `end_date`)
4. If both checks pass: field value returned
5. If either check fails: field value replaced with `[Restricted]` in the API response
6. All access attempts (granted and denied) are logged to the audit trail

### 2.3 Break-the-Glass Emergency Access (BR-DATA-002)

When a clinician needs emergency access to a patient's sensitive records or cross-facility clinical data without an existing treatment relationship:

1. Clinician invokes "Emergency Access" from the patient record
2. System requires two-factor patient confirmation: patient **name** and **date of birth**
3. Clinician provides a mandatory **reason** for emergency access (free-text, minimum 10 characters)
4. System grants access to: allergies, current medications, blood group, HIV status (only if prior consent was given), last 3 diagnoses
5. Access expires automatically after **24 hours**
6. Patient receives an **SMS notification** within 60 seconds: "Your medical records were accessed in an emergency at [Facility] by [Clinician Name] on [Date]. Contact [Facility Phone] for questions."
7. Full audit trail recorded: `clinician_id`, `patient_id`, `facility_id`, `reason`, `timestamp`, `expiry_timestamp`, `data_categories_accessed[]`

### 2.4 Permission Resolution Order

When a request is evaluated, permissions are resolved in this order:

1. **RBAC base:** Does the user's role grant the requested permission?
2. **ABAC overlay:** If the data is sensitive, does the user satisfy the attribute policy?
3. **Emergency override:** If RBAC or ABAC denies access, has an active break-the-glass session been established?

If all 3 layers deny access, the request returns `403 Forbidden`.

---

## 3. Data Protection

### 3.1 Encryption at Rest (NFR-HC-002)

- **Algorithm:** AES-256-GCM for all patient health data
- **Scope:** All columns containing patient health information (names, diagnoses, prescriptions, lab results, clinical notes, allergies, addresses, phone numbers)
- **Implementation:** MySQL InnoDB tablespace encryption with keyring plugin, supplemented by application-level field encryption for the most sensitive columns (HIV status, substance abuse notes)
- **Key management:** Per-tenant encryption keys derived from a master key using HKDF (HMAC-based Key Derivation Function). Master key stored in AWS KMS (cloud) or a hardware security module (local server mode). Key rotation: annually or on suspected compromise
- **Performance constraint:** P95 single-record retrieval under 200 ms on Celeron-class processors (NFR-HC-002)

### 3.2 Encryption in Transit (NFR-HC-003)

- **Protocol:** TLS 1.2+ on all endpoints (web, API, FHIR, DHIS2, HL7 v2)
- **Disabled:** TLS 1.0, TLS 1.1 — no ciphers offered
- **Certificate pinning:** Enforced on Android (OkHttp CertificatePinner) and iOS (URLSession delegate) mobile apps
- **HL7 v2 exception:** MLLP/TCP connections to laboratory analysers on the local network may use unencrypted TCP if the analyser does not support TLS. These connections must be on an isolated VLAN with no internet routing

### 3.3 Key Management

| Key Type | Storage | Rotation | Access |
|---|---|---|---|
| Master encryption key | AWS KMS / HSM | Annual or on compromise | Super Admin (via KMS API, not directly) |
| Tenant-derived keys | Derived at runtime via HKDF, never stored | Derived from master key | Application runtime only |
| JWT signing key | Environment variable (encrypted at rest) | Every 90 days | Application runtime only |
| TOTP secrets | `users` table, encrypted with tenant-derived key | On user MFA reset | Application runtime only |
| API keys (DHIS2, Africa's Talking, MoMo) | `.env` file (encrypted at rest), never in source | On credential rotation | Application runtime only |

### 3.4 Data Retention (NFR-HC-007)

- **Minimum retention:** 10 years from the date of the last clinical encounter (Uganda MoH policy)
- **Deletion prohibition:** Patient records within the retention period cannot be deleted by any role, including Super Admin
- **Post-retention:** Records are archived (compressed, encrypted, moved to cold storage), not deleted. Archived records remain accessible to authorised users upon request
- **Audit logs:** Same 10-year retention as clinical data

### 3.5 Data Residency (NFR-HC-019)

- Patient health data is stored in-country (within the borders of the country specified by the tenant's regulatory profile)
- Cross-border data transfers via FHIR API or DHIS2 export are validated against the active regulatory profile
- Transfers to non-permitted destinations are blocked and logged
- Country profiles define permitted transfer destinations (e.g., Australia permits cross-border under Australian Privacy Principles; Uganda requires in-country storage under PDPA 2019)

---

## 4. Audit Trail

### 4.1 Audit Log Structure (NFR-HC-001)

Every create, read, update, and delete operation on patient health records generates an audit log entry:

| Field | Type | Description |
|---|---|---|
| `id` | BIGINT (PK) | Auto-incrementing, immutable |
| `user_id` | INT | Authenticated user who performed the action |
| `timestamp` | DATETIME(6) | UTC, microsecond precision |
| `action` | ENUM | `create`, `read`, `update`, `delete` |
| `resource_type` | VARCHAR(100) | Entity name (e.g., `patient`, `prescription`, `lab_result`) |
| `resource_id` | INT | Primary key of the affected record |
| `facility_id` | INT | Tenant context of the action |
| `ip_address` | VARCHAR(45) | IPv4 or IPv6 address |
| `outcome` | ENUM | `success`, `failure`, `denied` |
| `old_value` | JSON (nullable) | Previous state (for updates) |
| `new_value` | JSON (nullable) | New state (for creates and updates) |
| `user_agent` | VARCHAR(500) | Browser or app identifier |
| `session_id` | VARCHAR(100) | Session or JWT token identifier |

### 4.2 Tamper-Proof Storage

- Audit logs are stored in a **separate database** (or separate MySQL instance) from the transactional database
- The audit log table uses an **append-only** storage engine configuration: `INSERT` is permitted; `UPDATE` and `DELETE` are blocked at the database user permission level
- The application database user for audit writes has `INSERT` only privilege on the audit tables
- Super Admin database connections are explicitly denied `UPDATE` and `DELETE` on audit tables
- Daily integrity check: a scheduled job computes a SHA-256 hash chain over the day's audit entries and stores the hash in a separate integrity table

### 4.3 Retention

Audit logs follow the same 10-year retention policy as clinical data (NFR-HC-007). Audit logs older than 2 years are compressed and moved to cold storage but remain queryable via an archive query interface.

### 4.4 Anomaly Detection

The audit system flags the following patterns for Facility Admin review:

- Access to patient records outside the user's assigned ward (ward-patient mismatch)
- Access to patient records outside the user's assigned facility (cross-tenant attempt)
- Access outside normal working hours (configurable per facility: default 06:00-22:00)
- High-volume record access (more than 50 patient records read in 1 hour by a single user)
- Repeated failed login attempts (5+ failures in 10 minutes)
- Break-the-glass access (all instances flagged regardless of pattern)

Anomaly alerts are delivered via the in-app notification system and, for critical anomalies (cross-tenant attempts, high-volume access), via SMS to the Facility Admin.

---

## 5. Clinical Safety Security

### 5.1 CDS Alert Logging (BR-CLIN-004, NFR-HC-012)

Every Clinical Decision Support alert presentation and every override action is logged:

| Field | Type | Description |
|---|---|---|
| `alert_id` | INT (PK) | Unique alert instance identifier |
| `clinician_id` | INT | User who received the alert |
| `patient_id` | INT | Patient the alert pertains to |
| `drug_pair` | VARCHAR(200) | Drug A + Drug B identifiers (for interaction alerts) |
| `severity_tier` | ENUM | `info`, `warning`, `serious`, `fatal` |
| `alert_type` | ENUM | `drug_interaction`, `allergy`, `dosing`, `five_rights`, `duplicate_therapy` |
| `timestamp` | DATETIME(6) | When the alert was presented |
| `action_taken` | ENUM | `acknowledged`, `overridden`, `escalated`, `blocked` |
| `override_reason` | TEXT (nullable) | Mandatory for Tier 3 overrides; null for others |
| `facility_id` | INT | Tenant context |

**Override rate tracking:** A monthly report calculates the override rate per facility (overrides / total alerts) broken down by severity tier. Override rates exceeding 80% for Tier 3 alerts trigger a review flag for the Facility Admin and the clinical pharmacist.

### 5.2 Prescribing Authority Enforcement (NFR-HC-024, BR-CLIN-002)

| Role | Prescribing Authority | Enforcement |
|---|---|---|
| Doctor / Physician | Full formulary access | No restrictions |
| Clinical Officer | Gazetted scope of practice | System restricts formulary to the CO-permitted subset; prescriptions outside scope are blocked with error message citing the regulatory restriction |
| Nurse / Midwife | No prescribing authority | "Create Prescription" action is hidden from the UI and returns `403 Forbidden` from the API |
| Pharmacist | No prescribing; may substitute generics | Substitution logged; original prescriber notified (BR-CLIN-002) |

Prescribing authority rules are stored in the country configuration layer and are configurable per country (e.g., the Clinical Officer scope differs between Uganda, Kenya, and India).

### 5.3 Weight-Based Dosing Validation (NFR-HC-011, BR-CLIN-006)

For all patients under 12 years:

1. System retrieves the patient's most recent weight (must be within 24 hours of prescribing; if absent, prescription submission is blocked)
2. System calculates dose: `dose = weight_kg * mg_per_kg`
3. System applies the adult ceiling dose cap from the formulary
4. System checks for 10x deviation: if `entered_dose / expected_dose >= 10`, the system flags a potential decimal error and requires explicit clinician override with documented reason
5. All dose calculations and overrides are logged in the CDS alert log

### 5.4 Critical Value Escalation Cascade (NFR-HC-022, BR-CLIN-003)

When a lab result exceeds the panic threshold (configurable per test, stored in the `lab_tests` table):

| Elapsed Time | Action | Delivery Channel |
|---|---|---|
| 0 minutes | Notify requesting doctor | WebSocket (web), push notification (mobile), SMS (fallback) |
| 30 minutes (unacknowledged) | Escalate to ward sister | WebSocket, push, SMS |
| 60 minutes (unacknowledged) | Escalate to Facility Admin | WebSocket, push, SMS |

Each step is timestamped in the audit trail. The escalation timer is managed by a scheduled Laravel job that checks unacknowledged critical values every 5 minutes.

---

## 6. Multi-Tenant Security

### 6.1 Tenant Isolation Enforcement

Tenant isolation is the highest-priority security control in Medic8. It is enforced at 4 layers (see System Architecture, Section 3.1):

1. **Repository layer:** `TenantAwareRepository` base class — `WHERE facility_id = ?` on every query method. Methods are `final` to prevent override
2. **Model layer:** Eloquent `TenantScope` global scope — secondary defence that catches queries bypassing the repository
3. **CI pipeline:** Static analysis rule — rejects any raw SQL query in the codebase that does not include `facility_id` in the WHERE clause. Pull requests with violations are blocked
4. **API response:** `StripTenantId` middleware — removes `facility_id` from all outbound JSON to prevent client-side tenant identifier leakage

### 6.2 Cross-Tenant Data Leakage Prevention

- Queue jobs inherit `facility_id` from the dispatching context via `TenantAwareJob` base class (System Architecture, Section 3.3)
- Event listeners resolve `facility_id` from the event payload, not from the container (prevents stale context)
- Database migrations include a CI check that verifies every new tenant-scoped table has a `facility_id` column with a NOT NULL constraint and an index
- API rate limiting is per-tenant: 1000 requests per minute per `facility_id` to prevent one tenant's load from affecting others

### 6.3 Super Admin Audit

Super Admin cross-tenant access is permitted only through the `withoutTenantScope($facilityId)` method, which:

1. Logs the access with `action = 'cross_tenant_read'` in the audit trail
2. Records the target `facility_id`, the Super Admin `user_id`, and the resources accessed
3. Is reviewed weekly by the platform security lead
4. Cannot be used for write operations — Super Admin cross-tenant access is read-only. Write operations require the Super Admin to impersonate a Facility Admin (which is separately logged)

---

## 7. Breach Response

### 7.1 Detection

- **Anomaly detection:** Automated flags from the audit system (Section 4.4)
- **Access pattern monitoring:** Unusual cross-facility lookups, after-hours access, bulk data exports
- **Infrastructure monitoring:** Failed login spikes, unusual API traffic patterns, database connection anomalies
- **External reporting:** Staff or patient reports of suspicious activity

### 7.2 Notification Timeline (NFR-HC-008, PDPA 2019 Section 31)

| Milestone | SLA | Action |
|---|---|---|
| Breach confirmed | T+0 | Incident response team activated |
| Breach impact report generated | T+4 hours | System generates report: affected patient count, data categories exposed (demographics, clinical, financial), breach timeline, affected facility identifiers |
| PDPO notified | T+72 hours | Notification to Uganda Personal Data Protection Office with breach details |
| Affected patients notified | T+72 hours | SMS notification to all affected patients via Africa's Talking |
| Remediation complete | T+30 days | Root cause addressed, controls strengthened |

### 7.3 Breach Impact Report Tooling

The system provides a breach impact analysis function that, given a compromised user account or session:

1. Queries the audit trail for all records accessed by the compromised account within the breach window
2. Enumerates affected patients by `patient_id`
3. Categorises exposed data (demographics, clinical notes, lab results, prescriptions, financial records)
4. Identifies affected facilities by `facility_id`
5. Generates a downloadable report in PDF format
6. Generates SMS notification drafts for all affected patients

---

## 8. Mobile Security

### 8.1 Authentication

- **JWT with refresh token rotation:** Access token (15-minute expiry), refresh token (7-day expiry). Each refresh invalidates the previous token. Replay detection invalidates all tokens for the user (Section 1.1)
- **Biometric authentication (optional):** Android (BiometricPrompt API — fingerprint, face), iOS (LocalAuthentication — Face ID, Touch ID). Biometric unlocks the locally stored JWT; it does not replace server authentication

### 8.2 Transport Security

- **Certificate pinning:** Android (OkHttp `CertificatePinner` configured with SHA-256 public key pins), iOS (URLSession delegate with `SecTrustEvaluateWithError` and pinned certificates)
- **Pin update:** Certificate pins are bundled in the app binary and updated via app store releases. A fallback pin is included for certificate rotation
- **TLS 1.2+:** Enforced on all API connections. The app refuses connections on TLS versions below 1.2

### 8.3 Local Storage Security

| Platform | Technology | Scope |
|---|---|---|
| Android | `EncryptedSharedPreferences` (Jetpack Security) | JWT tokens, user preferences, MFA state |
| Android | Room with SQLCipher | Offline clinical data queue |
| iOS | Keychain Services | JWT tokens, MFA state |
| iOS | Core Data with file-level encryption (Data Protection: Complete) | Offline clinical data queue |

### 8.4 Offline Permission Cache

- When the mobile app authenticates, the server returns the user's full permission set alongside the JWT
- Permissions are cached locally in encrypted storage with a TTL of **24 hours**
- If the cache expires and the device is offline, the app operates in **read-only mode** — no data mutations are permitted until permissions are refreshed
- On reconnection, the app re-fetches permissions before allowing write operations

### 8.5 App-Level Security Controls

- **Screen capture prevention:** Disabled on clinical screens (Android: `FLAG_SECURE`; iOS: `UITextField` overlay technique)
- **Clipboard restriction:** Clinical data fields prevent copy-to-clipboard on Android and iOS
- **Root/jailbreak detection:** App warns the user on rooted/jailbroken devices; does not block usage (clinical emergency access must be preserved)
- **Inactivity timeout:** Same 15-minute timeout as web, enforced at the app level. Biometric re-authentication on resume if configured
- **Remote wipe:** Facility Admin can remotely invalidate all tokens for a user, forcing re-authentication and clearing the local offline cache on next app launch
