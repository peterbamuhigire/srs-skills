## Section 4: Functional Requirements

> All requirements in this section conform to IEEE 830-1998 stimulus-response form. Each requirement is uniquely identified, unambiguous, complete, and verifiable. Every requirement includes: a unique identifier, a stimulus (trigger condition), a system response, input specifications, output specifications, error conditions, applicable business rule cross-references, and a verifiability criterion (test oracle).

---

### FR-AUTH: Authentication and Session Management

#### FR-AUTH-001: Web Session Login

**Stimulus:** A user submits a POST request to `/auth/login` with `username`, `password`, and a valid `csrf_token` from the login form.

**Response:** The system shall:
1. Validate the CSRF token against the session-stored token. If invalid, return HTTP 403 with `{"error": {"code": "CSRF_INVALID"}}` and log the attempt.
2. Look up the user by `username` in the `tbl_users` table, checking `status = active` and `locked = false`.
3. If the account is locked, return HTTP 403 with `{"error": {"code": "ACCOUNT_LOCKED", "message": "Account locked after 5 failed attempts. Contact your administrator."}}`.
4. Verify the submitted password against the stored Argon2ID hash (using `PASSWORD_PEPPER`).
5. On failure: increment `failed_login_attempts`. If count reaches 5, set `locked = true`, log the lock event. Return HTTP 401 with `{"error": {"code": "INVALID_CREDENTIALS"}}`. Do not reveal whether the username or password was incorrect.
6. On success: reset `failed_login_attempts` to 0. Regenerate the PHP session ID (`session_regenerate_id(true)`). Set session variables using the `academia_pro_` prefix: `user_id`, `tenant_id`, `user_type`, `username`, `full_name`, `last_activity`. Redirect to the role-appropriate dashboard.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `username` | string | 3–100 characters, trimmed |
| `password` | string | 8–255 characters |
| `csrf_token` | string | Must match `$_SESSION['academia_pro_csrf_token']` |

**Output:** HTTP 302 redirect to role dashboard on success.

**Error conditions:**

| Condition | HTTP Code | Error Code |
|---|---|---|
| CSRF token invalid | 403 | `CSRF_INVALID` |
| Username not found | 401 | `INVALID_CREDENTIALS` |
| Password incorrect | 401 | `INVALID_CREDENTIALS` |
| Account locked | 403 | `ACCOUNT_LOCKED` |
| Account inactive | 403 | `ACCOUNT_INACTIVE` |

**Business rules:** BR-RBAC-001.
**Verifiability:** Submit correct credentials → session created, redirect to dashboard (HTTP 302). Submit incorrect password 5 times → 6th attempt returns HTTP 403 `ACCOUNT_LOCKED`, `locked = true` in database. CSRF token mismatch → HTTP 403 `CSRF_INVALID`.

---

#### FR-AUTH-002: API / Mobile JWT Login

**Stimulus:** A client sends `POST /api/v1/auth/login` with `username`, `password`, and `device_id` in the JSON body.

**Response:** The system shall:
1. Validate the user credentials identically to FR-AUTH-001 (steps 2–5), excluding CSRF.
2. On success: generate an access token (JWT, HS256, 15-minute expiry) and a refresh token (JWT, HS256, 30-day expiry) using the `dual-auth-rbac` skill JWT structure. Both tokens contain: `sub` (user_id), `fid` (tenant_id), `ut` (user_type), `did` (device_id), `jti` (UUID v4), `exp`, `type`.
3. Persist the refresh token JTI and expiry in `tbl_api_refresh_tokens` (user_id, jti, device_id, expires_at, revoked=false).
4. Return HTTP 200 with `{"success": true, "data": {"access_token": "...", "refresh_token": "...", "expires_in": 900, "token_type": "Bearer"}}`.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `username` | string | Required |
| `password` | string | Required |
| `device_id` | string | Required, max 255 chars, identifies the device for token revocation |

**Error conditions:** Same as FR-AUTH-001 (excluding CSRF). Additionally: missing `device_id` → HTTP 422.

**Business rules:** BR-RBAC-001, Constraint C-002.
**Verifiability:** Valid credentials → HTTP 200 with two valid JWT tokens. Decode access token, verify `fid` equals user's `tenant_id`, `exp` is 15 minutes from now. Decode refresh token, verify `exp` is 30 days from now. Invalid credentials → HTTP 401. Locked account → HTTP 403.

---

#### FR-AUTH-003: JWT Token Refresh

**Stimulus:** A client sends `POST /api/v1/auth/refresh` with a valid, non-expired refresh token in the JSON body or `Authorization: Bearer` header.

**Response:** The system shall:
1. Verify the JWT signature. If invalid, return HTTP 401 `{"error": {"code": "INVALID_TOKEN"}}`.
2. Check the token's `jti` against `tbl_api_refresh_tokens`. If the JTI is not found or `revoked = true`, return HTTP 401 `{"error": {"code": "TOKEN_REVOKED"}}`.
3. If the token is valid and not revoked: mark the old JTI as `revoked = true` in `tbl_api_refresh_tokens`.
4. Generate a new access token and a new refresh token (same structure as FR-AUTH-002).
5. Persist the new refresh token JTI.
6. Return HTTP 200 with the new token pair.

**Error conditions:**

| Condition | HTTP Code | Error Code |
|---|---|---|
| Invalid signature | 401 | `INVALID_TOKEN` |
| Token expired | 401 | `TOKEN_EXPIRED` |
| Token revoked | 401 | `TOKEN_REVOKED` |
| JTI not in DB | 401 | `TOKEN_REVOKED` |

**Verifiability:** Valid refresh token → HTTP 200 with new token pair; old JTI row shows `revoked = true`. Revoked token → HTTP 401 `TOKEN_REVOKED`. Expired token → HTTP 401 `TOKEN_EXPIRED`. Replay of old refresh token after rotation → HTTP 401 `TOKEN_REVOKED`.

---

#### FR-AUTH-004: Session Logout

**Stimulus:** An authenticated user sends `POST /auth/logout` (web) or `POST /api/v1/auth/logout` (API) with a valid session or JWT.

**Response (web):** Destroy the session (`session_destroy()`), clear all `academia_pro_` prefixed session variables, redirect to `/auth/login`.

**Response (API):** Revoke all refresh tokens associated with the `device_id` in `tbl_api_refresh_tokens` by setting `revoked = true`. Return HTTP 200 `{"success": true}`.

**Verifiability (web):** After logout, sending a request with the old session cookie returns HTTP 302 redirect to login. **Verifiability (API):** After logout, attempting to use the old refresh token returns HTTP 401 `TOKEN_REVOKED`.

---

#### FR-AUTH-005: Idle Session Timeout

**Stimulus:** An authenticated web session exists and `$_SESSION['academia_pro_last_activity']` is more than 1,800 seconds (30 minutes) ago at the time of a new request.

**Response:** The system shall invalidate the session (equivalent to logout), and return HTTP 302 redirect to `/auth/login` with `?reason=timeout`.

**Verifiability:** Manually set `academia_pro_last_activity` to `time() - 1801`. Send any authenticated request. Receive HTTP 302 to login with `reason=timeout` query parameter.

---

#### FR-AUTH-006: Super Admin MFA Requirement

**Stimulus:** A user with `user_type = super_admin` attempts to log in via the Super Admin Panel at `/adminpanel/auth/login`.

**Response:** After successful password verification (FR-AUTH-001 steps 2–5), the system shall require a TOTP code or SMS OTP before completing the session. If the MFA challenge fails, the session is not created. If MFA succeeds, the session is created with an additional `mfa_verified = true` flag.

**Error conditions:** Incorrect TOTP → HTTP 422 `{"error": {"code": "MFA_INVALID"}}`. Expired TOTP window → HTTP 422 `{"error": {"code": "MFA_EXPIRED"}}`.

**Verifiability:** Log in as `super_admin` with correct password; confirm browser is redirected to MFA step, not dashboard. Enter correct TOTP; confirm session created with `academia_pro_mfa_verified = true`. Attempt to access `/adminpanel/dashboard` with session missing `mfa_verified` → HTTP 302 to MFA page.

---

### FR-TNT: Tenant Lifecycle Management

#### FR-TNT-001: Tenant Provisioning

**Stimulus:** A Super Admin submits a POST to `/adminpanel/api/v1/tenants` with school name, country, subscription plan, and owner contact details.

**Response:** The system shall:
1. Create a record in the `tenants` table with `status = pending`, generate a `tenant_id` (auto-increment) and a unique `slug` (URL-safe school name + numeric suffix if collision).
2. Create the School Owner user account with `user_type = owner`, `tenant_id = <new>`, a system-generated password, `force_password_change = true`.
3. Send a welcome email to the owner with login URL and temporary password.
4. Log the provisioning action: `{super_admin_user_id, action: TENANT_CREATED, tenant_id, timestamp}`.
5. Return HTTP 201 with the new tenant record.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `name` | string | 2–150 chars, required |
| `country` | string | ISO 3166-1 alpha-2, required, defaults to `UG` |
| `plan` | enum | `starter`, `standard`, `premium`, required |
| `owner_name` | string | 2–100 chars, required |
| `owner_email` | string | Valid email, unique across all tenants, required |
| `owner_phone` | string | E.164 format, optional |

**Business rules:** BR-MT-001, BR-MT-003.
**Verifiability:** POST valid tenant data → HTTP 201, `tenants` row created with `status = pending`, `tbl_users` row created with `force_password_change = true`, audit log entry exists, welcome email sent (check Mailgun/Postmark delivery log).

---

#### FR-TNT-002: Tenant Activation

**Stimulus:** A Super Admin sends `PATCH /adminpanel/api/v1/tenants/{id}` with `{"status": "active"}`.

**Response:** Update `tenants.status` to `active`. Log the action. Return HTTP 200.

**Verifiability:** School Owner cannot log into an inactive tenant (status=pending). After activation, login succeeds.

---

#### FR-TNT-003: Tenant Suspension

**Stimulus:** A Super Admin sends `PATCH /adminpanel/api/v1/tenants/{id}` with `{"status": "suspended", "reason": "..."}`.

**Response:** Update `tenants.status` to `suspended`. Invalidate all active sessions for that tenant (delete from session storage where `academia_pro_tenant_id = {id}`). Log the action with reason. Return HTTP 200.

**Post-suspension behaviour:** All web and API authentication attempts for suspended-tenant users return HTTP 403 `{"error": {"code": "TENANT_SUSPENDED", "message": "Your school account has been suspended. Contact support."}}`.

**Verifiability:** Suspend a tenant. Attempt login as a user of that tenant → HTTP 403 `TENANT_SUSPENDED`. Re-activate → login succeeds.

---

### FR-SIS: Student Information System

#### FR-SIS-001: Student Admission — New Student

**Stimulus:** An authorised user (Receptionist or Head Teacher role) submits `POST /api/v1/students` with the student's personal details.

**Response:** The system shall:
1. Validate all required fields (see input spec below).
2. Check for an existing student with the same NIN or LIN in `global_students`. If found, trigger FR-SIS-002 (existing identity enrollment) instead.
3. If no match: create a new `global_students` record with a UUID v4 `student_uid`. Create a `school_enrollments` record linking `student_uid` to `tenant_id` with `status = active` and the submitted local admission number, class_id, and enrollment date.
4. Return HTTP 201 with the full student record including `student_uid`.
5. Operation must complete within 500 ms at P95.

**Input specifications — required fields:**

| Field | Type | Constraints |
|---|---|---|
| `first_name` | string | 1–100 chars |
| `last_name` | string | 1–100 chars |
| `date_of_birth` | date | ISO 8601, must be in the past, student must be ≤ 25 years old |
| `gender` | enum | `male`, `female` |
| `class_id` | integer | Must exist in `classes` for this `tenant_id` |
| `enrollment_date` | date | ISO 8601, ≤ today |

**Input specifications — optional fields:** `middle_name`, `nin`, `lin`, `emis_number`, `passport_photo` (max 2 MB, JPEG/PNG), `parent_name`, `parent_phone` (E.164), `parent_email`, `medical_summary`, `address`, `district`, `nationality` (default `UG`), plus up to 27 additional configurable fields to reach the 40-field minimum.

**Error conditions:**

| Condition | HTTP | Code |
|---|---|---|
| Required field missing | 422 | `VALIDATION_ERROR` |
| `class_id` not in this tenant | 422 | `INVALID_CLASS` |
| NIN/LIN already has an active enrollment at another school | 409 | `DUPLICATE_ENROLLMENT` |
| Date of birth in the future | 422 | `INVALID_DOB` |

**Business rules:** BR-STU-001, BR-STU-002, BR-STU-003, BR-STU-004.
**Verifiability:** POST valid new student → HTTP 201, `global_students` row created with UUID `student_uid`, `school_enrollments` row with `tenant_id` = caller's tenant. POST same NIN a second time for a different school while first enrollment is active → HTTP 409 `DUPLICATE_ENROLLMENT`.

---

#### FR-SIS-002: Student Enrollment via Cross-School Identity Lookup

**Stimulus:** An authorised user submits `POST /api/v1/students` where the provided NIN or LIN matches an existing `global_students` record.

**Response:** The system shall:
1. Return the existing global identity record to the user for confirmation: `{"match_found": true, "student": {"student_uid": "...", "full_name": "...", "date_of_birth": "...", "gender": "..."}}`.
2. On confirmation (`POST /api/v1/students/{student_uid}/enroll`): create a `school_enrollments` record for this `tenant_id`. The `global_students` fields (name, DOB, gender) are copied in read-only mode — the enrolling school cannot alter them.
3. If the student already has an active enrollment at any school, return HTTP 409 `DUPLICATE_ENROLLMENT` (BR-STU-004).

**Verifiability:** Create student at School A with NIN `12345`. Log in as School B, attempt admission with same NIN → system returns match, not a new record. School B confirms → `school_enrollments` created for School B with `student_uid` from School A. Attempt to update `first_name` at School B → HTTP 403 `READ_ONLY_FIELD`.

---

#### FR-SIS-003: Student Search

**Stimulus:** An authorised user sends `GET /api/v1/students?q={query}` where `{query}` is a search string.

**Response:** The system shall query Meilisearch for students matching the `query` against `first_name`, `last_name`, `admission_number`, `nin`, and `lin`, scoped to the caller's `tenant_id`. Return up to 25 results ordered by relevance. Response within 500 ms at P95.

**Error conditions:** Empty `q` parameter → return the first 25 students ordered by `last_name` ascending.

**Verifiability:** Create 100 students. Search `q=ssemakula` → returns only students with "ssemakula" in their name. Confirm all results belong to the caller's `tenant_id` only.

---

#### FR-SIS-004: Student Transfer Out

**Stimulus:** An authorised user (Head Teacher+) sends `PATCH /api/v1/students/{student_uid}/status` with `{"status": "transferred_out", "transfer_date": "YYYY-MM-DD", "destination_school": "..."}`.

**Response:** Update `school_enrollments.status` to `transferred_out` for the calling tenant. Set `end_date = transfer_date`. All historical records (marks, attendance, fees) remain in the database in read-only mode. The `global_students` record is not altered. The student's `status` in global identity becomes available for enrollment at another school.

**Verifiability:** Transfer a student out. Confirm `school_enrollments.status = transferred_out`. Confirm the student can be enrolled at a different school (NIN lookup succeeds and enrollment is permitted).

---

#### FR-SIS-005: Student Record Retention Lock

**Stimulus:** Any attempt to permanently delete a `global_students` record or a `school_enrollments` record for a student whose last active enrollment ended fewer than 7 years ago.

**Response:** The system shall reject the deletion with HTTP 422 `{"error": {"code": "RETENTION_LOCK", "message": "Student records must be retained for 7 years after last enrollment."}}`. The attempted deletion shall be written to the audit log.

**Business rules:** BR-DP-002 (PDPO 2019 retention).
**Verifiability:** Attempt DELETE on a student enrolled 1 year ago → HTTP 422 `RETENTION_LOCK`. Audit log shows the attempt.

---

### FR-ACA: Academics Setup

#### FR-ACA-001: Academic Year Creation

**Stimulus:** An authorised user (Head Teacher+) sends `POST /api/v1/academic-years` with year label and 3 term objects.

**Response:** The system shall:
1. Validate that the `tenant_id` (from JWT/session) is used as the tenant scope.
2. Validate exactly 3 term objects are provided. If fewer or more, return HTTP 422 `{"error": {"code": "TERM_COUNT_INVALID", "message": "Uganda calendar requires exactly 3 terms per academic year."}}`.
3. Validate that all 3 term date ranges are non-overlapping. If any two terms overlap, return HTTP 422 `{"error": {"code": "TERM_OVERLAP", "message": "Term dates must not overlap."}}`.
4. Create the `academic_years` record and 3 `terms` records.
5. Return HTTP 201.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `label` | string | e.g. "2026/2027", required, unique per tenant |
| `terms` | array | Exactly 3 objects |
| `terms[].label` | string | "Term 1", "Term 2", "Term 3" |
| `terms[].start_date` | date | ISO 8601, required |
| `terms[].end_date` | date | ISO 8601, must be after start_date, required |

**Business rules:** BR-CAL-001, BR-CAL-002, UG-NFR-003.
**Verifiability:** POST with 3 non-overlapping terms → HTTP 201. POST with 4 terms → HTTP 422 `TERM_COUNT_INVALID`. POST with 2 overlapping terms → HTTP 422 `TERM_OVERLAP`.

---

#### FR-ACA-002: Class and Stream Configuration

**Stimulus:** An authorised user sends `POST /api/v1/classes` with class name, curriculum type, and optional streams.

**Response:** Create a `classes` record scoped to `tenant_id`. If `streams` array is provided, create `streams` records linked to the class. Return HTTP 201.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `name` | string | e.g. "Primary 7", "S.4 East", required |
| `curriculum_type` | enum | `thematic`, `standard`, `o_level`, `a_level` |
| `streams` | array | Optional; each stream has `name` (string, max 20 chars) |
| `academic_year_id` | integer | Must belong to this tenant |

**Verifiability:** Create class "Primary 7" with `curriculum_type = o_level`; confirm the UNEB O-Level grading schema is automatically associated (FR-ACA-003). Create class with 3 streams → 3 `streams` rows created.

---

#### FR-ACA-003: Automatic UNEB Schema Assignment

**Stimulus:** A class is created or updated with a specific `curriculum_type`.

**Response:** The system shall automatically associate the UNEB assessment schema corresponding to the `curriculum_type`:
- `thematic` → competency descriptors (HC/C/NYC), no numeric grades
- `standard` → numeric marks with teacher-defined maximum
- `o_level` → 9-point scale (D1–F9), aggregate-based divisions
- `a_level` → A–E/O/F grades, point-based

No additional configuration is required from the user.

**Verifiability:** Create a class with `curriculum_type = o_level`. Navigate to mark entry for that class → confirm the mark entry form shows the 9-point grade selector, not a numeric field.

---

#### FR-ACA-004: Subject and Timetable Configuration

**Stimulus:** An authorised user sends `POST /api/v1/timetables` with a list of period assignments.

**Response:** The system shall validate each period assignment for conflicts: same class, same time slot, different subject or teacher. If a conflict is detected, reject the entire submission with HTTP 422 `{"error": {"code": "TIMETABLE_CONFLICT", "details": [{...conflicting periods...}]}}`.

**Business rules:** BR-CAL-002.
**Verifiability:** Submit timetable with two subjects for P6 at 08:00–09:00 on Monday → HTTP 422 `TIMETABLE_CONFLICT` with details. Submit timetable with no conflicts → HTTP 201.

---

### FR-FEE: Fees Management

#### FR-FEE-001: Fee Structure Definition

**Stimulus:** An authorised user (Accounts Bursar or Head Teacher+) sends `POST /api/v1/fee-structures` with a list of fee line items for a class and term.

**Response:** Create `fee_structures` records scoped to `tenant_id`, `class_id`, `term_id`. Multiple line items allowed (tuition, boarding, transport, lunch, etc.) with no restriction on count. Return HTTP 201 with the created structure.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `class_id` | integer | Must belong to this tenant |
| `term_id` | integer | Must belong to this tenant |
| `line_items` | array | Min 1 item |
| `line_items[].label` | string | e.g. "Tuition", required, max 100 chars |
| `line_items[].amount` | integer | Amount in UGX (no decimal), min 0 |

**Business rules:** BR-FEE-001.
**Verifiability:** Create fee structure with 5 line items for P5, Term 1 → HTTP 201, 5 `fee_structure_line_items` rows created with correct `tenant_id`.

---

#### FR-FEE-002: Manual Fee Payment Recording

**Stimulus:** An authorised user (Accounts Bursar) sends `POST /api/v1/fee-payments` with student ID, term ID, amount, payment channel, and date.

**Response:** The system shall:
1. Validate the student belongs to this tenant and has an active enrollment.
2. Check for a duplicate entry: if a payment for the same student, same term, same amount, and same channel was recorded within the last 5 minutes, return HTTP 409 with the existing receipt (BR-FEE-005 Phase 1 scope — manual idempotency).
3. Apply payment to oldest outstanding balance first (BR-FEE-008 from PRD, per KUPAA model).
4. Create a `fee_payments` record with `source = manual`, `external_reference = null`.
5. Generate a sequentially numbered receipt (auto-increment per tenant, non-deletable, immutable).
6. Queue an SMS notification to the parent (if parent phone exists) via Africa's Talking.
7. Return HTTP 201 with the payment record and receipt number.
8. Total response time ≤ 500 ms at P95 (receipt generation is synchronous; PDF generation is queued).

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `student_uid` | UUID | Must belong to this tenant |
| `term_id` | integer | Must belong to this tenant |
| `amount` | integer | Amount in UGX, min 100 (UGX) |
| `channel` | enum | `cash`, `bank_transfer`, `mobile_money` |
| `payment_date` | date | ISO 8601, ≤ today |
| `notes` | string | Optional, max 500 chars |

**Business rules:** BR-FEE-002, BR-FEE-003, BR-FEE-004, BR-FEE-005.
**Verifiability:** Record payment of UGX 500,000 cash → HTTP 201 with receipt number (e.g., `REC-2026-0001`), `fee_payments` row with `source = manual`. Record identical payment within 5 minutes → HTTP 409 with original receipt. Inspect `fee_payments` table → exactly 1 row for the duplicate attempt.

---

#### FR-FEE-003: Receipt Generation and Immutability

**Stimulus:** A fee payment is successfully recorded (FR-FEE-002) or a user sends `GET /api/v1/receipts/{id}`.

**Response:** The system shall:
- Maintain a receipt record with: receipt_number (sequential per tenant), student name and admission number, school name, term, fee line item breakdown, payment channel, amount paid, outstanding balance after payment, bursar name, timestamp.
- Return the receipt as JSON for on-screen display and queue a PDF generation job. The PDF is stored on AWS S3 and a pre-signed URL returned within 5 seconds of the job completing.

**Immutability rule:** No role — including Super Admin — may DELETE or UPDATE a `receipts` row. The receipts table has no soft-delete column. Any attempt to call `DELETE /api/v1/receipts/{id}` returns HTTP 405 `METHOD_NOT_ALLOWED`.

**Business rules:** BR-FEE-004.
**Verifiability:** Attempt `DELETE /api/v1/receipts/1` → HTTP 405. Attempt `UPDATE receipts SET amount = 0 WHERE id = 1` directly in DB → enforce using a MySQL `BEFORE UPDATE` trigger that raises `SIGNAL SQLSTATE '45000'` for amount changes.

---

#### FR-FEE-004: Automated Fee Reminders

**Stimulus:** The daily scheduled job runs at 06:00 EAT and evaluates all tenants' term opening dates.

**Response:** For each tenant:
1. D-7 before `term.start_date`: identify all students with outstanding balance > 0. Queue an SMS to each student's primary parent via Africa's Talking: "Dear [Parent], [Student Name]'s school fees of UGX [balance] are due on [date]. Please pay via SchoolPay or contact the school."
2. D-1: same, for students still outstanding.
3. D+7: same, for students still outstanding.
4. Schools may disable D-1 and D+7 reminders in settings. D-7 may not be disabled (BR-FEE-006).
5. All sent reminders are logged in `fee_reminder_log` with student_uid, parent_phone, timestamp, message_id.

**Business rules:** BR-FEE-006.
**Verifiability:** Set a term's start_date to today + 7 days. Run the scheduled job manually. Confirm: SMS queued for each outstanding student, `fee_reminder_log` row created. Set school settings to disable D-1 → confirm no SMS queued at D-1 for that school. Attempt to disable D-7 via settings API → HTTP 422 `CANNOT_DISABLE_D7_REMINDER`.

---

#### FR-FEE-005: Refund Workflow

**Stimulus:** An Accounts Bursar sends `POST /api/v1/fee-payments/{payment_id}/refund-request` with `amount` and `reason`.

**Response:** Create a `refund_requests` record with `status = pending`, notified School Owner/Director via in-app notification and email. Return HTTP 202 `{"status": "pending_approval"}`.

**Approval:** School Owner/Director sends `POST /api/v1/refund-requests/{id}/approve`. System executes the refund: creates a negative `fee_payments` record, updates the student's balance, generates a credit note receipt. Returns HTTP 200.

**Rejection:** `POST /api/v1/refund-requests/{id}/reject` → sets status to `rejected`, notifies bursar.

**Constraint:** Accounts Bursar role cannot call `/approve` or `/reject`. Attempting to do so returns HTTP 403 `PERMISSION_DENIED`.

**Business rules:** BR-FEE-007.
**Verifiability:** Bursar creates refund request → HTTP 202. Bursar attempts to approve own request → HTTP 403. Owner approves → HTTP 200, negative `fee_payments` row created, student balance updated.

---

#### FR-FEE-006: Fee Balance Inquiry

**Stimulus:** An authorised user sends `GET /api/v1/students/{student_uid}/fee-balance?term_id={id}`.

**Response:** Return:
- Current term fee structure total.
- Total paid to date for this term.
- Outstanding balance.
- Arrears from previous terms.
- Payment history (paginated, 25 per page).

All values in UGX (integer). Response within 500 ms at P95.

**Business rules:** BR-FEE-003.
**Verifiability:** Student has UGX 300,000 structure, has paid UGX 200,000, carries UGX 50,000 arrears from last term → balance response shows `{"structure_total": 300000, "paid": 200000, "outstanding": 100000, "arrears": 50000, "total_due": 150000}`.

---

#### FR-FEE-007: Financial Reports

**Stimulus:** An authorised user (Accounts Bursar or Head Teacher+) sends `GET /api/v1/reports/fee-collection?term_id={id}&format={pdf|csv}`.

**Response:** The system generates a report showing:
- Total fee structure value for the term (sum across all enrolled students).
- Total collected to date.
- Collection rate percentage ($CollectionRate = \frac{TotalCollected}{TotalStructure} \times 100\%$).
- Defaulter list (students with outstanding balance > 0), sorted by outstanding amount descending.
- Per-class breakdown.

PDF or CSV returned within 5,000 ms.

**Verifiability:** Generate report for a term with 100 students, 70 fully paid, 30 with arrears. Confirm: collection rate = 70%± (accounting for partial payments), defaulter list has 30 entries, per-class breakdown sums correctly.

---

### FR-ATT: Attendance

#### FR-ATT-001: Daily Attendance Entry

**Stimulus:** An authorised Class Teacher sends `POST /api/v1/attendance` with an array of student attendance records for their class and a specific date.

**Response:** The system shall:
1. Validate the teacher has `attendance:submit` permission for the submitted `class_id`.
2. Validate the date is not in the future.
3. Check for duplicate entries: if any student already has an attendance record for this date and class, reject the submission for that student with `{"student_uid": "...", "error": "DUPLICATE_ATTENDANCE"}` and continue processing the remaining records.
4. Accept valid statuses only: `present`, `absent`, `late`, `excused`.
5. Create `attendance_records` rows for all valid entries.
6. Return HTTP 201 with `{"created": N, "duplicates": [{...}], "errors": [{...}]}`.
7. Trigger FR-ATT-003 check for consecutive absences.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `class_id` | integer | Teacher must have permission for this class |
| `date` | date | ISO 8601, ≤ today |
| `records` | array | Min 1 entry |
| `records[].student_uid` | UUID | Must belong to this tenant and this class |
| `records[].status` | enum | `present`, `absent`, `late`, `excused` |

**Business rules:** BR-ATT-001.
**Verifiability:** Submit attendance for 40 students → HTTP 201, 40 `attendance_records` rows created. Submit same date/class again → HTTP 201 with 40 entries in `duplicates` array, no new rows created.

---

#### FR-ATT-002: Consecutive Absence Alert

**Stimulus:** An attendance record with `status = absent` is saved, and the system detects that the same student has `absent` records on the 2 immediately preceding school days within the current term.

**Response:** The system shall queue an SMS via Africa's Talking to the student's primary parent/guardian within 5 minutes of the triggering record being saved. SMS content: "Dear [Parent], [Student Name] has been absent from [School Name] for 3 consecutive days. Please contact the school."

**Conditions:** "Consecutive" means 3 sequential school days in the `school_calendar` (weekends and public holidays excluded). If a school has not configured its school calendar, consecutive days default to calendar days.

**Business rules:** BR-ATT-002.
**Verifiability:** Record student absent on Day 1, Day 2, Day 3 → on saving Day 3's record, SMS job appears in Horizon queue within 5 minutes, `sms_log` row created for the parent's phone number.

---

#### FR-ATT-003: Attendance Record Amendment

**Stimulus:** An authorised user sends `PATCH /api/v1/attendance/{record_id}` with an updated status.

**Response:**
- If the record's `created_at` is within 48 hours: accept the amendment if the requesting user has the `attendance:amend_own` permission. Log the amendment: `{amended_by, old_status, new_status, timestamp}`.
- If the record is older than 48 hours: require the `attendance:amend_any` permission (Head Teacher role and above). Require a `reason` field in the request body (min 10 chars). Log: `{amended_by, old_status, new_status, reason, timestamp}`.
- If the requesting user has insufficient permission for the record age, return HTTP 403 `PERMISSION_DENIED`.

**Business rules:** BR-ATT-003.
**Verifiability:** Teacher amends record within 48h → HTTP 200, amendment log created. Teacher attempts amendment of 3-day-old record → HTTP 403. Head Teacher amends 3-day-old record with reason → HTTP 200, amendment log with `reason` field.

---

#### FR-ATT-004: Monthly Attendance Report

**Stimulus:** An authorised user sends `GET /api/v1/reports/attendance?class_id={id}&year_month={YYYY-MM}&format={pdf|csv}`.

**Response:** The system generates a table showing each enrolled student's attendance counts (Present, Absent, Late, Excused) for the specified calendar month. Report includes school name, class name, month, and generation timestamp. Returns within 3,000 ms.

**Verifiability:** Class of 45 students, 20 school days in the month. Report shows 45 rows with correct status counts. Verify totals match `attendance_records` query for the same class and month.

---

### FR-EXM: Examinations and UNEB Grading Engine

#### FR-EXM-001: Exam Configuration

**Stimulus:** An authorised user (Head Teacher+) sends `POST /api/v1/exams` with exam details.

**Response:** Create an `exams` record linked to `class_id`, `term_id`, and `tenant_id`. Return HTTP 201.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `name` | string | e.g. "End of Term 1 Exams", required |
| `class_id` | integer | Must belong to this tenant |
| `term_id` | integer | Must belong to this tenant |
| `subjects` | array | Each subject has `subject_id` and `max_mark` (integer, 10–100) |
| `submission_deadline` | datetime | ISO 8601, must be in the future |

**Verifiability:** Create exam with 8 subjects → HTTP 201, 8 `exam_subjects` rows. `max_mark` of 0 → HTTP 422.

---

#### FR-EXM-002: Mark Entry Validation

**Stimulus:** An authorised Class Teacher sends `POST /api/v1/exam-marks` with an array of student marks for a specific exam subject.

**Response:** The system shall:
1. Validate each mark: `0 ≤ mark ≤ max_mark` for the exam subject. Marks outside this range → reject that entry with `{"student_uid": "...", "error": "MARK_OUT_OF_RANGE", "max": N}`.
2. Check submission deadline: if `now() > exam.submission_deadline` and the requesting user does not have `exams:unlock` permission → reject all entries with HTTP 423 `{"error": {"code": "MARK_ENTRY_LOCKED", "message": "Mark entry deadline has passed."}}`.
3. Accept valid entries and create `exam_results` rows.
4. Return HTTP 201 with `{"created": N, "errors": [{...}]}`.

**Business rules:** BR-UNEB-005, BR-CAL-003.
**Verifiability:** Submit mark of 85 for subject with max 80 → entry rejected with `MARK_OUT_OF_RANGE`. Submit mark of 75 → accepted. Submit marks after deadline without unlock → HTTP 423.

---

#### FR-EXM-003: Deadline Unlock by Head Teacher

**Stimulus:** A Head Teacher sends `POST /api/v1/exams/{id}/unlock-marks` with `{"reason": "..."}`.

**Response:** Set `exams.marks_locked = false`. Log: `{unlocked_by, exam_id, reason, timestamp}`. Return HTTP 200.

**Error:** Non-Head-Teacher role → HTTP 403.

**Business rules:** BR-CAL-003, BR-UNEB-005.
**Verifiability:** Exam past deadline → mark entry returns HTTP 423. Head Teacher calls unlock with reason → HTTP 200. Mark entry re-attempted → HTTP 201 accepted.

---

#### FR-EXM-004: PLE Grade Computation

**Stimulus:** A Head Teacher sends `POST /api/v1/exams/{id}/compute-grades` for a P7 class with `curriculum_type = standard` (PLE scope).

**Response:** The system shall compute for each student:
1. Subject grade for each of the 4 compulsory subjects (English, Mathematics, Science, Social Studies & Religious Education): grade 1 (mark ≥ 80%) to grade 4 (mark < 40%).
2. Aggregate = sum of 4 subject grades (range 4–16).
3. Division assignment per BR-UNEB-001: I (4–12), II (13–23), III (24–29), IV (30–34), Ungraded (35–36).
4. Store results in `ple_results`: `student_uid`, `exam_id`, `aggregate`, `division`, computed subject grades.
5. Return HTTP 200 with summary: `{students_computed: N, errors: []}`.
6. Computation for 500 students must complete within 5 seconds.

**Business rules:** BR-UNEB-001.
**Verifiability:** Load 100 known student marks from UNEB sample dataset. Run computation. Compare every aggregate and division output against manually computed expected values. Zero discrepancies is pass criterion. Confirm 500-student run completes within 5,000 ms.

---

#### FR-EXM-005: UCE O-Level Grade Computation

**Stimulus:** `POST /api/v1/exams/{id}/compute-grades` for a class with `curriculum_type = o_level`.

**Response:** The system shall compute for each student:
1. Subject grade per subject on the 9-point scale (D1 = highest, F9 = fail), per UNEB UCE marking rules.
2. Aggregate across best 8 subjects.
3. Division per BR-UNEB-002: I (7–34), II (35–46), III (47–58), IV (59–70), Unclassified (>70).
4. Store in `uce_results`.
5. Response within 5 seconds for 500 students.

**Business rules:** BR-UNEB-002.
**Verifiability:** UNEB sample UCE mark sheets (minimum 100 candidates) → zero discrepancies between system output and manually computed expected results.

---

#### FR-EXM-006: UACE A-Level Grade Computation

**Stimulus:** `POST /api/v1/exams/{id}/compute-grades` for a class with `curriculum_type = a_level`.

**Response:** The system shall compute for each student:
1. Principal subject grades (A, B, C, D, E, F) and subsidiary grades (O, F).
2. Points: A=6, B=5, C=4, D=3, E=2, O=1, F=0 (BR-UNEB-003).
3. University entry points: sum of best 3 principal subject points.
4. Store in `uace_results`.

**Business rules:** BR-UNEB-003.
**Verifiability:** UNEB sample UACE mark sheets → zero discrepancies on all grade assignments and point totals.

---

#### FR-EXM-007: Thematic Curriculum Assessment

**Stimulus:** `POST /api/v1/exams/{id}/compute-grades` for a class with `curriculum_type = thematic`.

**Response:** The system shall assign competency descriptors per subject per student:
- Mark ≥ 80%: Highly Competent (HC)
- Mark 50–79%: Competent (C)
- Mark < 50%: Not Yet Competent (NYC)

No numeric aggregate is computed. No division is assigned. The report card for thematic classes displays only descriptors.

**Business rules:** BR-UNEB-004.
**Verifiability:** Student with English mark 82/100 → grade = HC. Student with Science mark 49/100 → grade = NYC. Confirm no aggregate or division field is populated in `thematic_results`.

---

#### FR-EXM-008: UNEB Candidate Registration Export

**Stimulus:** An authorised user (Head Teacher+) sends `GET /api/v1/exports/uneb-registration?exam_type={ple|uce|uace}&academic_year_id={id}`.

**Response:** The system shall assemble candidate registration data for all eligible students (enrolled, active, in the appropriate class level for the specified exam type) and return an Excel workbook (.xlsx) containing the following columns:

| Column | Source | Format |
|---|---|---|
| UNEB Centre Number | School's registered UNEB centre number (`schools.uneb_centre_number`) | String |
| Index Number | Student's UNEB-assigned index number (`students.uneb_index_number`) | String |
| Exam Year | Year of the examination sitting (`students.uneb_exam_year`) | 4-digit year |
| First Name | `students.first_name` | String |
| Surname | `students.surname` | String |
| Other Names | `students.other_names` | String (may be empty) |
| Gender | `students.gender` | M / F |
| Subject Entries | Comma-separated list of registered examination subjects per the student's subject combination | String |

AcademiaPro shall store `uneb_index_number` and `uneb_exam_year` per student record. These fields are populated when the school receives the UNEB registration confirmation. The EMIS system verifies learners against the UNEB database using the PLE/UCE Index Number and Exam Year combination.

Export for 500 candidates shall complete within 30 seconds.

*`[CONTEXT-NOTE: Final UNEB registration column specification to be confirmed via UNEB liaison. Core fields documented.]`*

**Verifiability:** Generate UNEB registration export for a school with 100 candidates (exam type = UCE) → workbook contains all 8 columns. Every row has a non-empty Index Number and Exam Year. Subject Entries column contains at least 1 subject per candidate. File opens without error in Microsoft Excel and LibreOffice Calc.

---

### FR-RPT: Report Card Generation

#### FR-RPT-001: Single Student Report Card

**Stimulus:** An authorised user sends `GET /api/v1/report-cards?student_uid={uid}&term_id={id}`.

**Response:** The system shall assemble and return a report card containing:
- School name, logo, and address.
- Student name, admission number, class, and term.
- All subject marks and grades (computed per the class's curriculum type).
- UNEB aggregate and division (for PLE/UCE/UACE classes).
- Class position (ranked by aggregate among all students in the class for the same term).
- Term attendance summary (Present count, Absent count, Attendance %).
- Head teacher comment field (editable text, max 500 chars).
- Report generation timestamp and generating user.

The report card is returned as JSON for on-screen display. A PDF is queued for generation and stored on AWS S3. A pre-signed download URL is included in the response once available (polling endpoint: `GET /api/v1/report-cards/{id}/status`).

Single report card response within 3,000 ms at P95.

**Business rules:** BR-CAL-001.
**Verifiability:** Generate report card for a student in an O-Level class → JSON response contains all required fields. PDF URL becomes available within 10 seconds. Confirm class position is correct by cross-checking all students' aggregates.

---

#### FR-RPT-002: Bulk Report Card Generation

**Stimulus:** An authorised user (Head Teacher+) sends `POST /api/v1/report-cards/bulk` with `class_id` and `term_id`.

**Response:** The system shall:
1. Validate the user has `reports:generate_bulk` permission.
2. Queue a bulk generation job via Laravel Horizon.
3. Return HTTP 202 `{"job_id": "...", "status": "queued", "student_count": N}`.
4. The job generates individual PDF report cards for all enrolled students in the class.
5. On completion, a notification is sent to the requesting user (in-app + email): "142 report cards generated. 1 failed: [student name] — missing marks for Mathematics."
6. Bulk generation for a class of 200 students must complete within 120 seconds.
7. A bulk download zip is staged on S3 with a 24-hour expiry pre-signed URL.

**Business rules:** UG-NFR-007 (report card ≤ 3,000 ms per student, so 200 × 3 s = 600 s budget; 120 s target requires parallel job processing).
**Verifiability:** Class of 50 students, all marks entered → bulk job completes within 120 s, 50 PDFs on S3, zip download available. Introduce 1 student with missing marks → completion notification lists 1 failure.

---

#### FR-RPT-003: School Performance Summary Report

**Stimulus:** An authorised user sends `GET /api/v1/reports/school-performance?term_id={id}&format={pdf|csv}`.

**Response:** The system generates a class-by-class summary:
- Class name, curriculum type.
- Number of students, number who sat the exam.
- Mean aggregate, median aggregate.
- Division distribution (Division I %, Division II %, etc.) for UNEB classes.
- Attendance rate %.
- Pass rate % (students with Division I–III for UNEB; students ≥ 50% average for standard).

Returned within 5,000 ms.

**Verifiability:** School with 10 classes → report has 10 rows. Verify mean aggregate for a class against manual calculation from `exam_results` table.

---

#### FR-RPT-004: Head Teacher Comment Entry

**Stimulus:** An authorised user (Head Teacher+) sends `PATCH /api/v1/report-cards/{id}/comment` with `{"comment": "..."}`.

**Response:** Update `report_cards.head_teacher_comment`. Re-queue PDF regeneration for the affected report card. Return HTTP 200.

**Constraints:** Comment max 500 chars. After the term's report card release date (configurable per school), comments may not be changed by Class Teacher or Bursar roles; only Head Teacher and above may amend.

**Verifiability:** Set comment → re-queued PDF includes updated comment. Attempt comment by Bursar after release date → HTTP 403.

---

### FR-RBAC: Role-Based Access Control

#### FR-RBAC-001: Permission Resolution

**Stimulus:** Any authenticated request to any protected endpoint.

**Response:** The system shall evaluate permissions using the following priority order (per `dual-auth-rbac` skill):
1. If user is `super_admin`: grant all permissions.
2. If a user-level explicit denial exists for this permission: deny (HTTP 403).
3. If a user-level explicit grant exists for this permission: grant.
4. If a tenant-level role override disables the permission for this role in this tenant: deny.
5. If the user's assigned role(s) include this permission: grant.
6. Default: deny (HTTP 403).

Permission cache TTL: 15 minutes (Redis). Cache is invalidated immediately on role or permission change for the affected user.

**Business rules:** BR-RBAC-001, BR-RBAC-002.
**Verifiability:** Assign role with permission A but not B to a user. Request endpoint requiring A → HTTP 200. Request endpoint requiring B → HTTP 403. Grant explicit user-level permission B → HTTP 200. Add user-level denial for A → HTTP 403 despite role having A.

---

#### FR-RBAC-002: Role Assignment

**Stimulus:** An authorised user sends `POST /api/v1/users/{user_id}/roles` with `{"role_id": N}`.

**Response:** The system shall:
1. Check that the requesting user's role has equal or higher privilege level than the target role. If not, return HTTP 403 `{"error": {"code": "INSUFFICIENT_PRIVILEGE"}}`.
2. Create a `tbl_user_roles` record: `user_id`, `tenant_id`, `role_id`.
3. Invalidate the target user's permission cache in Redis.
4. Return HTTP 201.

**Business rules:** BR-RBAC-002.
**Verifiability:** Head Teacher attempts to assign School Owner role to another user → HTTP 403 `INSUFFICIENT_PRIVILEGE`. School Owner assigns Head Teacher role → HTTP 201, permission cache invalidated.

---

#### FR-RBAC-003: User Invitation and Onboarding

**Stimulus:** An authorised user (School Owner or Head Teacher) sends `POST /api/v1/users/invite` with invitee email and intended role.

**Response:** Create a `user_invitations` record with a 48-hour token. Send invitation email with a registration link. Return HTTP 202.

On the invitee clicking the link: present a registration form (name, password). On submission: create the user, assign the role, invalidate the invitation token.

**Verifiability:** Invite a Class Teacher → invitation email sent, invitation row created. Invitee completes registration → user created with correct role, invitation token marked used. Attempt to use the same link a second time → HTTP 410 `INVITATION_EXPIRED`.

---

#### FR-RBAC-004: Session and Token Expiry

**Stimulus:** A web session's `academia_pro_last_activity` exceeds 1,800 seconds (see FR-AUTH-005), OR an API refresh token's `expires_at` is in the past.

**Response (web):** Session destroyed, redirect to login.

**Response (API):** Refresh token rejected with HTTP 401 `TOKEN_EXPIRED`. User must re-authenticate via FR-AUTH-002.

*Note: This SRS adopts the `dual-auth-rbac` skill standard of 30-day API refresh tokens. The 7-day value stated in the PRD is superseded.*

**Verifiability:** See FR-AUTH-005 and FR-AUTH-003 verifiability criteria.

---

#### FR-RBAC-005: Super Admin Cross-Tenant Access Logging

**Stimulus:** A Super Admin authenticates (with MFA) and accesses any endpoint scoped to a specific tenant's data.

**Response:** Before returning any data, the system shall write an audit log entry:
```json
{
  "actor_user_id": 1,
  "actor_type": "super_admin",
  "action": "CROSS_TENANT_READ",
  "target_tenant_id": 42,
  "endpoint": "/api/v1/students",
  "ip_address": "...",
  "timestamp": "2026-01-01T10:00:00Z"
}
```

**Business rules:** BR-MT-003.
**Verifiability:** Super Admin requests `GET /api/v1/students` for Tenant 42 → audit log entry created BEFORE the response body is returned. Verify by checking log timestamp precedes response timestamp.

---

### FR-EMIS: Government Data Export

#### FR-EMIS-001: EMIS Learner Data Export

**Stimulus:** An authorised user (Head Teacher+) sends `POST /api/v1/exports/emis-learners` with `academic_year_id`, `term_id`, and `learner_category` (one of: `ugandan`, `foreign_non_refugee`, `refugee`).

**Response:** The system shall generate an Excel workbook (.xlsx) matching the MoES EMIS bulk upload template structure for the specified learner category. The EMIS portal (`https://emis.go.ug/`) accepts learner data via Excel workbook upload. Three separate templates exist — one per learner category — and the system shall produce the template corresponding to the requested `learner_category`.

The workbook shall contain an institution identification header row:

| Header Field | Source |
|---|---|
| School Name | `schools.name` |
| EMIS Number | `schools.emis_number` |
| District | `schools.district` |
| Sub-county | `schools.sub_county` |
| Education Level | `schools.education_level` (Primary / Secondary) |

Each data row shall contain the following learner fields per the 2023 Learner EMIS Registration Form:

| Column | Source | Format |
|---|---|---|
| First Name | `students.first_name` | String |
| Surname | `students.surname` | String |
| Other Name | `students.other_names` | String (may be empty) |
| Sex | `students.gender` | Male / Female |
| Nationality | `students.nationality` | String |
| Date of Birth | `students.date_of_birth` | dd/mm/yyyy |
| District of Birth | `students.district_of_birth` | String |
| ID Type | `students.id_type` | NIN / Student Pass / Refugee ID |
| ID Number | `students.id_number` | NIN format: CM748383480F83; Student Pass: ST1234567; Refugee ID: RM1-23456789 |
| Is Orphan | `students.is_orphan` | Yes / No |
| Familiar Language | `students.familiar_language` | String |
| Class of Study | Mapped from `classes.name` to EMIS class codes via `emis_class_mappings` lookup table | String |
| Special Needs | `students.special_needs` | String (may be empty) |
| Health Issues | `students.health_issues` | String (may be empty) |
| Talents | `students.talents` | String (may be empty) |
| Practical Skills | `students.practical_skills` | String (may be empty) |
| Exam Year | `students.uneb_exam_year` | 4-digit year (conditional — secondary students with PLE/UCE results only) |
| Index Number | `students.uneb_index_number` | String (conditional — secondary students with PLE/UCE results only) |

Parent/Guardian fields (Father and Mother recorded separately):

| Column | Source | Format |
|---|---|---|
| Father First Name | `guardians.first_name` (where `relationship` = father) | String |
| Father Surname | `guardians.surname` | String |
| Father Nationality | `guardians.nationality` | String |
| Father ID Type | `guardians.id_type` | NIN / Passport / Refugee ID |
| Father ID Number | `guardians.id_number` | String |
| Father Mobile Phone | `guardians.mobile_phone` | String |
| Mother First Name | `guardians.first_name` (where `relationship` = mother) | String |
| Mother Surname | `guardians.surname` | String |
| Mother Nationality | `guardians.nationality` | String |
| Mother ID Type | `guardians.id_type` | NIN / Passport / Refugee ID |
| Mother ID Number | `guardians.id_number` | String |
| Mother Mobile Phone | `guardians.mobile_phone` | String |

All data shall be sourced from existing AcademiaPro records — no re-entry required. The system shall filter students by the specified `learner_category` based on nationality and refugee status fields. Export for schools of up to 2,000 students shall complete within 30 seconds.

**Verifiability:** Generate EMIS learner export (category = `ugandan`) for a test school with 500 students → workbook contains institution header with correct EMIS Number. Every row contains non-empty First Name, Surname, Sex, Date of Birth, and Class of Study. Date of Birth is in dd/mm/yyyy format. Class of Study values match EMIS class codes (not AcademiaPro internal class names). Upload the generated workbook to the EMIS portal staging environment → zero validation errors.

---

#### FR-EMIS-002: EMIS Staff Export

**Stimulus:** An authorised user (Head Teacher+) sends `POST /api/v1/exports/emis-staff` with `academic_year_id`, `term_id`, `staff_type` (one of: `teaching`, `non_teaching`), and `nationality_category` (one of: `ugandan`, `foreign`).

**Response:** The system shall generate an Excel workbook (.xlsx) matching the MoES EMIS staff upload template for the specified staff type and nationality category (separate templates exist for Ugandan and Foreign staff).

For Teaching Staff, each data row shall contain:

| Column | Source | Format |
|---|---|---|
| NIN / Work Permit | `staff.id_number` | String |
| First Name | `staff.first_name` | String |
| Surname | `staff.surname` | String |
| Other Names | `staff.other_names` | String (may be empty) |
| Date of Birth | `staff.date_of_birth` | dd/mm/yyyy |
| Gender | `staff.gender` | Male / Female |
| Religion | `staff.religion` | String |
| Marital Status | `staff.marital_status` | String |
| Teacher Type | `staff.teacher_type` | Trained / Qualified |
| Weekly Teaching Periods | `staff.weekly_teaching_periods` | Integer |
| Government Payroll | `staff.govt_payroll` | Yes / No |
| IPPS Number | `staff.ipps_number` | String (may be empty) |
| TMIS Number | `staff.tmis_number` | String (may be empty) |
| Employment Status | `staff.employment_status` | String |
| Highest Education Level | `staff.highest_education_level` | String |
| Highest Teaching Qualification | `staff.highest_teaching_qualification` | String |
| Designation | `staff.designation` | String |

For Non-Teaching Staff, each data row shall contain the same fields excluding Teacher Type, Weekly Teaching Periods, Highest Teaching Qualification, and TMIS Number.

The workbook shall include the same institution identification header as FR-EMIS-001. Export for schools with up to 200 staff members shall complete within 10 seconds.

**Verifiability:** Generate EMIS teaching staff export (nationality = `ugandan`) for a test school with 50 teachers → workbook contains all 17 columns. Every row has a non-empty NIN/Work Permit, First Name, Surname, and Gender. Date of Birth is in dd/mm/yyyy format. Generate non-teaching staff export → workbook omits Teacher Type, Weekly Teaching Periods, Highest Teaching Qualification, and TMIS Number columns. Upload both workbooks to the EMIS portal staging environment → zero validation errors.

---

#### FR-EMIS-003: EMIS Learner Summary Form Export

**Stimulus:** An authorised user (Head Teacher+) sends `GET /api/v1/exports/emis-summary?academic_year_id={id}&term_id={id}`.

**Response:** The system shall generate an Excel workbook (.xlsx) containing the termly learner headcount summary required by the EMIS portal. The summary shall present total learners by class and gender for the specified academic year and term.

The workbook shall contain:

| Column | Description |
|---|---|
| Class | EMIS class code (mapped from AcademiaPro class names via `emis_class_mappings`) |
| Male | Count of enrolled male students in the class for the specified term |
| Female | Count of enrolled female students in the class for the specified term |
| Total | Sum of Male + Female |

The workbook shall include the institution identification header (School Name, EMIS Number, District, Sub-county, Education Level) and a summary row with grand totals across all classes.

All counts shall be derived from active enrolment records for the specified term — students with `status = withdrawn` or `status = transferred` before the term start date shall be excluded. Export shall complete within 5 seconds.

**Verifiability:** Generate EMIS summary for a test school with 500 students across 7 classes → workbook contains 7 data rows plus 1 summary row. Male + Female = Total for every row. Grand total matches the count of active students returned by `GET /api/v1/students?academic_year_id={id}&term_id={id}&status=active`. Upload to EMIS portal staging environment → zero validation errors.

---

### FR-AUD: Audit Trail

#### FR-AUD-001: Immutable Audit Log

**Stimulus:** Any of the following events occurs: user login (success/failure), user logout, permission change, role assignment, student record create/update/delete attempt, fee payment create, refund request or approval, Super Admin cross-tenant access, tenant status change, mark entry lock/unlock, report card release.

**Response:** The system shall write an `audit_logs` record within 100 ms of the triggering event:

| Field | Content |
|---|---|
| `id` | UUID v4 |
| `timestamp` | UTC datetime, microsecond precision |
| `actor_user_id` | Authenticated user's `user_id` (null for system jobs) |
| `actor_type` | `super_admin`, `owner`, `staff`, `member`, `system` |
| `tenant_id` | Tenant scope (null for platform-level events) |
| `action` | Uppercase string, e.g. `STUDENT_CREATED` |
| `resource_type` | Table name, e.g. `students` |
| `resource_id` | Primary key of affected record |
| `old_value` | JSON snapshot before change (null for create) |
| `new_value` | JSON snapshot after change (null for delete) |
| `ip_address` | Request IP |

**Immutability:** The `audit_logs` table has no UPDATE or DELETE routes. The application never exposes these operations. A MySQL trigger enforces immutability: any `UPDATE` or `DELETE` on `audit_logs` raises `SIGNAL SQLSTATE '45000'`.

**Retention:** Audit logs retained for 7 years (aligned with `multi-tenant-saas-architecture` skill audit retention standard and Uganda education record retention requirement).

**Verifiability:** Create a student record → audit log entry with `action = STUDENT_CREATED`, `new_value` = student JSON. Attempt `DELETE FROM audit_logs WHERE id = 1` directly → MySQL signal fires. Attempt `DELETE /api/v1/audit-logs/1` via API → HTTP 405.

---

> **Amendment — 2026-03-29:** The following FR groups were added following approval of the design document `docs/plans/2026-03-29-academia-pro-student-promotion-portability-design.md`. They resolve gap HIGH-004 and extend the student portability architecture.

---

### FR-PROM: Year-Start Promotion Wizard

#### FR-PROM-001: Class-to-Class Promotion Mapping

**Stimulus:** An authorised user (Head Teacher+) sends `PUT /api/v1/classes/{id}/promotion-mapping` with a `promotes_to_class_id` value.

**Response:** The system shall store the destination class for this class. If `promotes_to_class_id` is `null`, the class is marked as a departure class (final year). If the destination class does not belong to the same tenant, return HTTP 422 `INVALID_DESTINATION`. Return HTTP 200.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `promotes_to_class_id` | integer or null | Must belong to same tenant, or null |

**Business rules:** BR-PROM-002.
**Verifiability:** Set P5 `promotes_to_class_id = P6.id` → HTTP 200. Set P7 `promotes_to_class_id = null` → HTTP 200. Set P5 `promotes_to_class_id = 99999` (non-existent) → HTTP 422 `INVALID_DESTINATION`.

---

#### FR-PROM-002: Promotion Wizard Launch

**Stimulus:** An authorised user (Head Teacher+) creates a new academic year via `POST /api/v1/academic-years` (FR-ACA-001).

**Response:** Immediately after academic year creation, the system shall:
1. Create a `promotion_wizard_sessions` record with `status = in_progress` for the new academic year.
2. Build the class queue: one entry per class in the tenant with the prior academic year's student counts.
3. Mark all entries `status = pending_promotion`.
4. Return the wizard session ID in the academic year creation response: `{"academic_year": {...}, "promotion_wizard_id": "..."}`.

The new academic year's Term 1 `open` action is blocked (`HTTP 423 PROMOTION_INCOMPLETE`) until the wizard session reaches `status = complete`.

**Business rules:** BR-PROM-001.
**Verifiability:** Create academic year → `promotion_wizard_sessions` row created, all classes at `pending_promotion`. Attempt `POST /api/v1/terms/{id}/open` before wizard complete → HTTP 423 `PROMOTION_INCOMPLETE`.

---

#### FR-PROM-003: Bulk Promotion with Selective Override

**Stimulus:** An authorised user sends `POST /api/v1/promotion-wizard/{wizard_id}/classes/{class_id}/promote` with a list of student UIDs to promote and a list to mark as repeating.

**Response:** The system shall:
1. Validate the destination class exists and belongs to this tenant.
2. For each **promoted** student: create a new `school_enrollments` record (`class_id = destination`, `academic_year_id = new year`, `status = active`). Update the old enrollment: `status = completed`, `end_date = last term end date`.
3. For each **repeating** student: create a new `school_enrollments` record in the **same class** for the new year. Update old enrollment: `status = completed`.
4. Mark the class entry in `promotion_wizard_sessions` as `status = done`.
5. Check if all class entries are `done` or `skipped`. If so, set wizard `status = complete`.
6. Create a `promotion_events` audit record.
7. Return HTTP 200 with summary: `{"promoted": N, "repeating": N}`.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `promote` | UUID array | Student UIDs to promote to destination class |
| `repeat` | UUID array | Student UIDs to re-enrol in same class |

All student UIDs in both arrays must belong to this tenant and this class. `promote` + `repeat` must account for every enrolled student in the class (no student left unclassified).

**Business rules:** BR-PROM-003, BR-PROM-004, BR-PROM-006.
**Verifiability:** Promote 44 students, repeat 1. Confirm: 44 new `school_enrollments` rows with destination class, 1 new row with same class. All 45 old enrollments have `status = completed`. Promotion event audit row created. Attempt to leave 2 students unclassified → HTTP 422 `UNCLASSIFIED_STUDENTS`.

---

#### FR-PROM-004: Wizard Skip

**Stimulus:** An authorised user sends `POST /api/v1/promotion-wizard/{wizard_id}/classes/{class_id}/skip` with `{"reason": "..."}`.

**Response:** Mark the class entry `status = skipped`. Log the skip with reason and user. If all entries are `done` or `skipped`, set wizard `status = complete`. Return HTTP 200.

**Constraint:** A class that has enrolled students from the prior year cannot be skipped without an explicit `force: true` flag and a Head Teacher role. If `force: true` is used without `reason`, return HTTP 422.

**Business rules:** BR-PROM-007.
**Verifiability:** Skip a class with zero prior-year students → HTTP 200, no confirmation needed. Skip a class with 30 students without `force: true` → HTTP 422. Skip with `force: true` and reason → HTTP 200, skip logged with reason.

---

#### FR-PROM-005: Historical Record Lock

**Stimulus:** The daily scheduled job runs and finds a completed academic year whose final term's `end_date` is more than 30 days in the past and whose records are not yet locked.

**Response:** The system shall set `academic_years.records_locked = true` for that year. After locking:
- Any `PATCH` to `exam_results`, `attendance_records`, or `report_cards` for records in this year returns HTTP 423 `YEAR_LOCKED`.
- Fee records remain editable only for refund processing (refunds may post after year-end).
- The lock job writes an audit log entry: `{action: ACADEMIC_YEAR_LOCKED, academic_year_id, locked_at}`.

No manual trigger exists for this lock. It is system-only.

**Business rules:** BR-PROM-005.
**Verifiability:** Set final term `end_date = today - 31 days`. Run the job. Confirm `records_locked = true`. Attempt `PATCH /api/v1/exam-results/1` → HTTP 423 `YEAR_LOCKED`. Confirm audit log entry exists.

---

#### FR-PROM-006: Promotion Wizard Draft Persistence

**Stimulus:** An authorised user partially completes the wizard (some classes done, some pending) and closes the browser.

**Response:** The wizard session persists in `promotion_wizard_sessions` with `status = in_progress`. The per-class progress is stored; no data is lost. On returning to the Academic Year setup screen, the system presents a "Continue Promotion" prompt linking to the in-progress wizard.

**Verifiability:** Complete 3 of 5 classes in wizard. Close session. Log back in. Confirm wizard resumes at the same state with 3 classes showing `done` and 2 showing `pending_promotion`.

---

#### FR-PROM-007: Term 1 Open Gate

**Stimulus:** An authorised user attempts to open Term 1 of a new academic year via `POST /api/v1/terms/{id}/open`.

**Response:** The system shall check whether the linked `promotion_wizard_sessions` record has `status = complete`. If not, return HTTP 423 `{"error": {"code": "PROMOTION_INCOMPLETE", "message": "Complete the Year-Start Promotion Wizard before opening Term 1.", "pending_classes": [...]}}` listing the classes still pending.

If the wizard is complete, allow Term 1 to open normally.

**Business rules:** BR-PROM-001.
**Verifiability:** With wizard incomplete → HTTP 423, response body lists pending class names. After completing wizard → `POST /api/v1/terms/{id}/open` succeeds (HTTP 200).

---

### FR-DEPART: Student Departure Model

#### FR-DEPART-001: Student Departure Recording

**Stimulus:** A departure is triggered either (a) by the Head Teacher explicitly via `POST /api/v1/students/{student_uid}/depart`, or (b) automatically by the Promotion Wizard when a student in a final-year class is marked as departing (FR-PROM-003).

**Response:** The system shall:
1. Create a `school_departures` record: `student_uid`, `tenant_id`, `reason_code`, `departure_date`, `notes` (optional), `recorded_by`.
2. Update the student's `school_enrollments` record: `status = archived`, `end_date = departure_date`.
3. The student's `global_students` record remains unchanged and available for future enrolment — except when `reason_code = deceased` (see FR-DEPART-002).
4. All records at the departing school become read-only for that student.
5. Return HTTP 200.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `reason_code` | enum | `completed`, `transferred_platform`, `transferred_external`, `scholarship`, `expelled`, `withdrawn`, `deceased`, `other` |
| `departure_date` | date | ISO 8601, ≤ today |
| `notes` | string | Optional, max 500 chars |

**Business rules:** BR-DEPART-001, BR-DEPART-002, BR-DEPART-004.
**Verifiability:** Record departure with `reason_code = withdrawn`. Confirm `school_enrollments.status = archived`. Confirm student can be enrolled at another school via NIN/LIN lookup. Attempt `PATCH /api/v1/exam-results/{id}` for a departed student's record → HTTP 423 `STUDENT_DEPARTED`.

---

#### FR-DEPART-002: Deceased Student Lock

**Stimulus:** A departure is recorded with `reason_code = deceased`.

**Response:** In addition to FR-DEPART-001 standard behaviour, the system shall set `global_students.status = deceased`. Any future attempt to enrol a student with this `student_uid` at any school returns HTTP 422 `{"error": {"code": "STUDENT_DECEASED"}}`.

**Business rules:** BR-DEPART-002.
**Verifiability:** Record deceased departure. Attempt NIN/LIN lookup and enrolment at any tenant → HTTP 422 `STUDENT_DECEASED`. Confirm `global_students.status = deceased`.

---

#### FR-DEPART-003: Expelled Flag Privacy

**Stimulus:** Any authenticated school user performs a NIN/LIN student lookup (`GET /api/v1/global-students?nin={nin}`) for a student who has a prior `school_departures` record with `reason_code = expelled`.

**Response:** The system shall return the student's global identity fields (name, DOB, gender) and their availability for enrolment. The response shall **not** include the departure reason or any indication of expulsion. The response is identical to a lookup for a student who departed with any other reason code.

The expelled status is accessible only via an approved inter-school record request (FR-SHARE group) with student/parent consent.

**Business rules:** BR-DEPART-003.
**Verifiability:** Record expelled departure for Student A. Perform NIN lookup from a different tenant → response contains global identity fields only, no `departure_reason` field, no expulsion indicator. Confirm via direct DB check that the `school_departures.reason_code = expelled` row exists but is not exposed in the API response.

---

#### FR-DEPART-004: Departure Reason Update

**Stimulus:** An authorised user (Head Teacher+) sends `PATCH /api/v1/students/{student_uid}/departure` with an updated `reason_code` or `notes`.

**Response:** Update the `school_departures` record. Log the amendment with `old_reason`, `new_reason`, `amended_by`, `timestamp`. Return HTTP 200.

**Constraint:** `reason_code = deceased` cannot be changed once set. Attempting to update a deceased record returns HTTP 422 `CANNOT_AMEND_DECEASED`.

**Verifiability:** Change reason from `withdrawn` to `transferred_external` → HTTP 200, amendment logged. Attempt to change `deceased` reason → HTTP 422 `CANNOT_AMEND_DECEASED`.

---

### FR-HIST: Cross-Tenant Student History

#### FR-HIST-001: Student History Tab — School List

**Stimulus:** An authenticated student user sends `GET /api/v1/me/academic-history`.

**Response:** The system shall query `school_enrollments` by the authenticated user's `student_uid` (no `tenant_id` filter — this is a global identity query via `withStudentSelfScope()`). Return a list of all schools the student has been enrolled at, ordered by most recent first:

```json
[
  {
    "tenant_id": 12,
    "school_name": "Kingsway S.S.",
    "from_year": "2025/2026",
    "to_year": "2025/2026",
    "status": "active",
    "available_records": ["report_cards", "attendance_summary", "fee_clearance"]
  },
  {
    "tenant_id": 5,
    "school_name": "St. Mary's Primary",
    "from_year": "2018/2019",
    "to_year": "2024/2025",
    "status": "completed",
    "available_records": ["report_cards", "attendance_summary", "fee_clearance"]
  }
]
```

Every call to this endpoint writes an audit log entry: `{action: STUDENT_SELF_HISTORY_LIST, student_uid, viewer_user_id, timestamp}`.

**Business rules:** BR-HIST-001, BR-HIST-002.
**Verifiability:** Student enrolled at 3 schools → response contains 3 entries, all with `student_uid` matching the authenticated user. Confirm audit log entry created. Attempt to access another student's history by manipulating request → HTTP 403 (scope is locked to own `student_uid` extracted from JWT, not a request parameter).

---

#### FR-HIST-002: Student History — Record Access

**Stimulus:** An authenticated student sends `GET /api/v1/me/academic-history/{tenant_id}/report-cards` (or `attendance-summary`, `fee-clearance`).

**Response:** The system shall:
1. Confirm the `tenant_id` in the path is one the student has a `school_enrollments` record for (using `withStudentSelfScope()`). If not, return HTTP 403.
2. Fetch the requested records from the target tenant's data in read-only mode.
3. Return the records.
4. Write an audit log entry: `{action: STUDENT_SELF_HISTORY_READ, student_uid, viewer_user_id, source_tenant_id, target_tenant_id, record_type, timestamp}`.

**Fee records:** Fee payment amounts are not returned. Only a clearance status (`{"cleared": true}` or `{"cleared": false, "note": "Outstanding balance at time of departure"}`) is returned. See BR-HIST-003.

**Suspended/archived tenants:** Records are returned even if the target tenant is suspended or archived. See BR-HIST-004.

**Business rules:** BR-HIST-001, BR-HIST-002, BR-HIST-003, BR-HIST-004.
**Verifiability:** Student fetches report cards from old school → HTTP 200, records returned, audit log entry created. Student attempts to fetch records from a school they were never enrolled at → HTTP 403. Student fetches fee records → response contains `cleared` boolean only, no amounts.

---

#### FR-HIST-003: Student History — Read-Only Enforcement

**Stimulus:** An authenticated student attempts any non-GET request (`POST`, `PUT`, `PATCH`, `DELETE`) against any endpoint within their historical school's data via the `academic-history` path.

**Response:** HTTP 405 `METHOD_NOT_ALLOWED`. No write operation is permitted on historical records via the student history interface.

**Verifiability:** Student attempts `PATCH /api/v1/me/academic-history/5/report-cards/1` → HTTP 405.

---

### FR-SHARE: Inter-School Record Request

#### FR-SHARE-001: Record Request Creation

**Stimulus:** An authorised user (Head Teacher+) at School B sends `POST /api/v1/record-requests` specifying a target student and the items requested.

**Response:** The system shall:
1. Validate the student exists in `global_students` via `student_uid`, `nin`, or `lin`.
2. Validate all requested `items` are in the platform-defined canonical shareable list.
3. Validate `access_window_days` is 7, 14, or 30.
4. Create a `record_requests` record: `requesting_tenant_id`, `student_uid`, `items` (JSON array), `reason`, `access_window_days`, `status = awaiting_student_consent`.
5. Send an SMS and in-portal notification to the student (and parent if student is under 18): "School B has requested your academic records from School A. They are requesting: [item list]. You have 7 days to respond."
6. Return HTTP 201 with the request ID.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `student_uid` | UUID | Must exist in `global_students` |
| `items` | string array | Each item must be in canonical list |
| `reason` | string | Required, max 500 chars |
| `access_window_days` | integer | 7, 14, or 30 |

**Business rules:** BR-SHARE-001, BR-SHARE-002.
**Verifiability:** Create valid request → HTTP 201, `record_requests` row with `status = awaiting_student_consent`, SMS queued to student/parent. Include non-canonical item → HTTP 422 `INVALID_SHAREABLE_ITEM`. Include `access_window_days = 10` → HTTP 422.

---

#### FR-SHARE-002: Student Consent Response

**Stimulus:** An authenticated student (or parent) sends `POST /api/v1/record-requests/{id}/consent` with per-item consent decisions.

**Response:** The system shall:
1. Validate the request belongs to a school the authenticated student was enrolled at (the *source* school).
2. Record the consent decision for each item: `approved` or `declined`.
3. `disciplinary_record` requires an explicit separate boolean field `disciplinary_explicit_consent: true` — if this field is absent or false while `disciplinary_record` is in the approved list, return HTTP 422 `DISCIPLINARY_EXPLICIT_CONSENT_REQUIRED`.
4. Update `record_requests.status = awaiting_source_school_review`.
5. Notify the source school (School A) Head Teacher: "A student has responded to a record request. Review and approve within your portal."
6. Return HTTP 200.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `consents` | object | Key = item code, value = `approved` or `declined` |
| `disciplinary_explicit_consent` | boolean | Required and must be `true` if `disciplinary_record` is approved |

**Business rules:** BR-SHARE-002, BR-SHARE-003.
**Verifiability:** Student approves 2 items, declines 1 → HTTP 200, consent decisions recorded per item, status = `awaiting_source_school_review`. Student approves `disciplinary_record` without `disciplinary_explicit_consent: true` → HTTP 422. Request with no student response after 7 days → scheduled job sets `status = expired`.

---

#### FR-SHARE-003: Student Consent Expiry

**Stimulus:** The daily scheduled job finds a `record_requests` record with `status = awaiting_student_consent` whose `created_at` is more than 7 days ago.

**Response:** Set `status = expired`. Notify School B: "The record request for [Student] has expired — student did not respond within 7 days." Write audit log entry. School B may submit a new request if needed.

**Business rules:** BR-SHARE-002.
**Verifiability:** Create request, advance clock 8 days, run job → `status = expired`, School B notification queued.

---

#### FR-SHARE-004: Source School Approval

**Stimulus:** An authorised user (Head Teacher+) at School A sends `POST /api/v1/record-requests/{id}/approve` with per-item approval decisions and an access window.

**Response:** The system shall:
1. Validate the request is addressed to this tenant (School A is the source school for the student's prior enrollment).
2. Validate School A's approved items are a subset of the student-consented items. School A cannot approve an item the student declined. Return HTTP 422 `EXCEEDS_STUDENT_CONSENT` if violated.
3. Set `access_window_days` to the submitted value (≤ the originally requested duration).
4. Set `status = approved` or `status = partially_approved` (if some items declined by School A).
5. Set `access_expires_at = now() + access_window_days`.
6. Notify School B: "Your record request has been approved. Records available until [date]."
7. Return HTTP 200.

**Business rules:** BR-SHARE-004, BR-SHARE-005.
**Verifiability:** Student approved items A and B. School A approves only A → HTTP 200 `partially_approved`. School A attempts to approve item B which student declined → HTTP 422 `EXCEEDS_STUDENT_CONSENT`. Confirm `access_expires_at` set correctly.

---

#### FR-SHARE-005: Source School Denial

**Stimulus:** School A sends `POST /api/v1/record-requests/{id}/deny` with an optional reason.

**Response:** Set `status = denied`. Notify School B. Return HTTP 200. The student is also notified that School A declined the request.

**Verifiability:** Deny request → HTTP 200, `status = denied`, both School B and student notified.

---

#### FR-SHARE-006: School B Record Access

**Stimulus:** An authorised user at School B sends `GET /api/v1/record-requests/{id}/records/{item_code}` within the access window.

**Response:** The system shall:
1. Validate `status = approved` or `partially_approved` and `access_expires_at > now()`.
2. Validate the requested `item_code` is in the approved items list for this request.
3. Return the records in read-only JSON form (or a pre-signed PDF URL for `report_cards`).
4. Write an audit log entry: `{action: RECORD_REQUEST_ACCESSED, request_id, accessor_user_id, requesting_tenant_id, item_code, timestamp}`.

**Error conditions:** Access after expiry → HTTP 410 `ACCESS_WINDOW_EXPIRED`. Access to non-approved item → HTTP 403 `ITEM_NOT_APPROVED`.

**Business rules:** BR-SHARE-005, BR-SHARE-006.
**Verifiability:** Access approved item within window → HTTP 200, audit log entry. Access same item after `access_expires_at` → HTTP 410. Access item School A did not approve → HTTP 403.

---

#### FR-SHARE-007: Access Window Expiry

**Stimulus:** The daily scheduled job finds `record_requests` records where `access_expires_at < now()` and `status` is `approved` or `partially_approved`.

**Response:** Set `status = expired`. Any subsequent access attempt returns HTTP 410 `ACCESS_WINDOW_EXPIRED`. Notify School B: "Your access to [Student]'s records has expired." Write audit log entry.

**Verifiability:** Set `access_expires_at = now() - 1 hour`. Run job → `status = expired`. Subsequent GET → HTTP 410.

---

#### FR-SHARE-008: Student Record Request History

**Stimulus:** An authenticated student sends `GET /api/v1/me/record-requests`.

**Response:** Return all `record_requests` records where `student_uid` matches the authenticated student's UID, ordered by `created_at` descending. Each entry shows: requesting school name, items requested, consent decisions, approval decisions, current status, access window dates.

**Business rules:** BR-SHARE-007.
**Verifiability:** Create 3 requests for a student across different stages. Student fetches history → all 3 returned with correct status and item details. Student cannot see requests made for other students.

---

### FR-APPLY: In-Platform School Application

#### FR-APPLY-001: School Directory Listing

**Stimulus:** An authenticated student or parent sends `GET /api/v1/schools?district={d}&type={t}&curriculum={c}`.

**Response:** Return a paginated list of active (`status = active`) tenants that have opted into directory listing (`schools.directory_listed = true`). Each entry shows: school name, district, school type, curriculum types offered, boarding/day, and a `can_apply` boolean (false if applications are closed for the requested class/year). Response within 500 ms at P95.

**Verifiability:** 3 active tenants with directory listing enabled → GET returns 3 results. 1 tenant with `directory_listed = false` → not in results. Filter by district → only matching schools returned.

---

#### FR-APPLY-002: Application Submission

**Stimulus:** An authenticated student or parent sends `POST /api/v1/schools/{tenant_id}/applications` with the application details.

**Response:** The system shall:
1. Validate the target school is active and `directory_listed = true`.
2. Validate the student does not already have 5 pending applications (`status = under_review`). Return HTTP 422 `MAX_APPLICATIONS_REACHED` if exceeded.
3. Validate the target class is accepting applications for the requested academic year.
4. Create a `school_applications` record: `student_uid`, `target_tenant_id`, `requested_class_id`, `requested_year`, `personal_statement` (optional, max 500 words), `status = under_review`, `attached_record_request_id` (nullable — if student attached records).
5. Notify the target school's Head Teacher: "New application received for [Student Name] — [Class] [Year]."
6. Return HTTP 201.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `requested_class_id` | integer | Must be a valid class at target school |
| `requested_academic_year` | string | e.g. `2026/2027` |
| `personal_statement` | string | Optional, max 2,500 chars |
| `attached_record_request_id` | UUID | Optional; must be a completed, approved record request for this student |

**Business rules:** BR-APPLY-001, BR-APPLY-002, BR-APPLY-003.
**Verifiability:** Submit valid application → HTTP 201, `school_applications` row created, Head Teacher notified. Submit 6th application while 5 are under review → HTTP 422 `MAX_APPLICATIONS_REACHED`.

---

#### FR-APPLY-003: Admissions Queue (School Side)

**Stimulus:** An authorised user (Head Teacher+) at School B sends `GET /api/v1/applications?status={status}`.

**Response:** Return a paginated list of `school_applications` for this tenant, filtered by status (`under_review`, `accepted`, `interview_requested`, `declined`). Each entry shows student name, requested class, personal statement, attached records link (if any), and application date.

**Verifiability:** 5 applications at various statuses → GET returns correct filtered results per status. Confirm no applications from other tenants appear.

---

#### FR-APPLY-004: Application Decision

**Stimulus:** An authorised user (Head Teacher+) sends `PATCH /api/v1/applications/{id}` with a decision.

**Response:** Update `school_applications.status` to `accepted`, `interview_requested`, or `declined`. Notify the student/parent via SMS and portal notification with the outcome and any notes. Return HTTP 200.

If `accepted`: the school proceeds with the normal NIN/LIN enrolment workflow (FR-SIS-002) to formally enrol the student. The application record is linked to the resulting `school_enrollments` record.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `status` | enum | `accepted`, `interview_requested`, `declined` |
| `notes` | string | Optional, max 500 chars (shared with student/parent) |

**Verifiability:** Accept application → HTTP 200, student notified, `status = accepted`. Decline → student notified, `status = declined`. Confirm Head Teacher at School A cannot see or action applications at School B.

---

#### FR-APPLY-005: Application Retention Purge

**Stimulus:** The daily scheduled job finds `school_applications` records where `created_at < now() - 2 years`.

**Response:** Permanently delete the records. Write an audit log entry for the batch purge: `{action: APPLICATIONS_PURGED, count: N, oldest_record_date: ..., timestamp}`. Return no user-facing output.

**Business rules:** BR-APPLY-004.
**Verifiability:** Create application with `created_at = now() - 730 days - 1 day`. Run job → record deleted, audit log entry exists. Application at exactly 730 days → not deleted (purge threshold is strictly greater than 2 years).

---

### FR-ELEARN: Class Library and E-Learning (Phase 2)

> All requirements in this section apply to the Module 21 e-learning suite delivered in Phase 2. The BrightSoma API integration (FR-ELEARN-012) is scoped to Phase 3.

---

#### FR-ELEARN-001: Study Material File Upload

**Stimulus:** A teacher submits a POST request to `/api/v1/elearn/materials` with a file attachment, resource type, subject ID, class ID(s), term ID, and optional topic tag.

**Response:** The system shall:
1. Validate the file size against the school's configured per-file limit (default 20 MB for PDFs; 200 MB for MP4).
2. Scan the file for malware using the configured scanning service. If malware is detected, quarantine the file, send an in-app alert to the teacher, and return HTTP 422 with `{"error": {"code": "FILE_QUARANTINED"}}`.
3. Compute the file hash (SHA-256). If an identical hash exists in the school's storage, reference the existing object (deduplication) rather than storing a second copy.
4. Write the file to Wasabi object storage under the school's tenant partition. Increment the school's storage usage counter.
5. Generate a CDN-backed download URL and create a `learning_materials` record with `resource_type`, `subject_id`, `class_ids[]`, `term_id`, `topic_tag`, `file_url`, `file_size_bytes`, `uploaded_by`, `tenant_id`.
6. Return HTTP 200 with the `learning_materials` record within 10,000 ms for files up to 20 MB.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `file` | binary | Required for file upload types; max size per school config |
| `resource_type` | enum | `pdf`, `video_link`, `mp4`, `audio`, `pptx`, `image`, `external_link`, `typed_note` |
| `subject_id` | integer | Required; must belong to the teacher's assigned subjects |
| `class_ids` | array | Required; at least 1 class ID; must be classes the teacher teaches |
| `term_id` | integer | Required; must be the current or a past term in the school's academic year |
| `topic_tag` | string | Optional; max 100 characters |

**Error conditions:**

| Condition | HTTP Code | Error Code |
|---|---|---|
| File exceeds size limit | 422 | `FILE_TOO_LARGE` |
| Malware detected | 422 | `FILE_QUARANTINED` |
| Storage quota exceeded | 422 | `QUOTA_EXCEEDED` |
| Subject not assigned to teacher | 403 | `SUBJECT_NOT_ASSIGNED` |

**Business rules:** BR-ELEARN-008, BR-ELEARN-009.
**Verifiability:** Upload a PDF of 5 MB → HTTP 200; record in `learning_materials`; file retrievable via CDN URL. Upload a file exceeding limit → HTTP 422 `FILE_TOO_LARGE`. Upload a known malware test file → HTTP 422 `FILE_QUARANTINED`; no download URL generated.

---

#### FR-ELEARN-002: Study Material Access Log

**Stimulus:** A student opens a study material resource (PDF, audio, or MP4) from their class library.

**Response:** The system shall:
1. Verify the student is enrolled in a class associated with the `learning_materials` record.
2. Return the CDN-backed file URL or embed URL.
3. Create a `material_access_log` record with `material_id`, `student_uid`, `tenant_id`, `accessed_at`, and `access_type` (`viewed`, `downloaded`).

**Business rules:** BR-MT-001.
**Verifiability:** Student opens a material → `material_access_log` record created within 1,000 ms. Student from a different class attempts to access the material → HTTP 403. Teacher queries access log for a material → sees correct student name and timestamp.

---

#### FR-ELEARN-003: Assignment Creation and Publication

**Stimulus:** A teacher submits a POST request to `/api/v1/elearn/assignments` with all required fields and clicks Publish.

**Response:** The system shall:
1. Validate all required fields (title, subject_id, class_ids, due_date, submission_type).
2. Create an `assignments` record with `title`, `instructions`, `subject_id`, `class_ids[]`, `due_date`, `submission_type`, `marks_total`, `assignment_type`, `late_policy`, `rubric` (JSON, optional), `tenant_id`, `created_by`.
3. Set assignment `status = published`.
4. Dispatch a push notification (FCM) to all enrolled students in the target class(es) within 5 minutes.
5. For students without push notifications enabled, queue an SMS via Africa's Talking if the school has SMS enabled.
6. Return HTTP 200 with the assignment record within 500 ms at P95.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `title` | string | Required; max 200 characters |
| `subject_id` | integer | Required; must belong to the teacher's assigned subjects |
| `class_ids` | array | Required; at least 1 class ID |
| `due_date` | datetime | Required; must be a future date |
| `submission_type` | enum | `text`, `file`, `both`, `none` |
| `marks_total` | integer | Required; ≥ 1 |
| `assignment_type` | enum | `Homework`, `Classwork`, `CAT`, `Project`, `Practical` |
| `late_policy` | enum | `accept`, `deduct`, `reject` |
| `deduct_rate` | decimal | Required when `late_policy = deduct`; percentage per day; 1–50 |
| `rubric` | JSON array | Optional; each criterion: `{"name": string, "max_marks": integer}` |

**Error conditions:**

| Condition | HTTP Code | Error Code |
|---|---|---|
| `due_date` is in the past | 422 | `INVALID_DUE_DATE` |
| `deduct_rate` missing when `late_policy = deduct` | 422 | `DEDUCT_RATE_REQUIRED` |
| Rubric criterion marks exceed `marks_total` | 422 | `RUBRIC_EXCEEDS_TOTAL` |

**Business rules:** BR-ELEARN-001.
**Verifiability:** Create an assignment with `late_policy = reject` and `due_date = tomorrow`. Submit as a student after the due date → submission rejected with `{"error": {"code": "SUBMISSION_REJECTED_LATE"}}`. Create an assignment with rubric; student opens assignment → rubric criteria visible before submission.

---

#### FR-ELEARN-004: Student Assignment Submission

**Stimulus:** A student submits a POST request to `/api/v1/elearn/submissions` with their assignment response.

**Response:** The system shall:
1. Verify the student is enrolled in the assignment's target class.
2. Apply the late submission policy: if `due_date` has passed and `late_policy = reject`, return HTTP 422 with `{"error": {"code": "SUBMISSION_REJECTED_LATE"}}`. If `late_policy = deduct` or `accept`, record the submission with `is_late = true`.
3. Record a server-side `submitted_at` timestamp (immutable; not derived from client).
4. Create a `submissions` record with `assignment_id`, `student_uid`, `text_content` (nullable), `file_attachments[]` (up to 5 files), `submitted_at`, `is_late`, `status = submitted`, `tenant_id`.
5. Store all uploaded files in Wasabi under the school's quota. Apply the same malware scanning as FR-ELEARN-001.
6. Return HTTP 200 with submission confirmation and the `submitted_at` timestamp.

**Business rules:** BR-ELEARN-001, BR-ELEARN-002, BR-ELEARN-009.
**Verifiability:** Student submits before due date → `is_late = false`; `submitted_at` is server time. Student submits after due date with `late_policy = reject` → HTTP 422 `SUBMISSION_REJECTED_LATE`. Student submits with 5 files → all 5 stored; submission record references all 5 file URLs.

---

#### FR-ELEARN-005: Plagiarism Detection on Text Submissions

**Stimulus:** A student submits a text response to an assignment. A prior submission exists from another student in the same class for the same assignment.

**Response:** The system shall:
1. After saving the submission, asynchronously compute the Jaccard token similarity between the new submission's `text_content` and each existing submission's `text_content` for the same `assignment_id` and `tenant_id`.
2. If any pair's similarity ratio exceeds 0.80 (80%), set `plagiarism_flag = true` on both submissions and create a `plagiarism_alerts` record linking the two `submission_id` values, the computed similarity ratio, and the detection timestamp.
3. Send an in-app notification to the teacher: "Possible plagiarism detected in [Assignment Title] — [Student A] and [Student B] (similarity: X%)."
4. Do not notify the students, alter the submission status, or reduce the score automatically.

**Business rules:** BR-ELEARN-005.
**Verifiability:** Submit two identical text responses → both flagged `plagiarism_flag = true`; teacher notified; student submission status unchanged. Submit two unique responses → no flag raised. Similarity ratio of 0.79 → no flag.

---

#### FR-ELEARN-006: Teacher Marking and Gradebook Auto-Post

**Stimulus:** A teacher opens a submission, enters scores (per rubric criterion if applicable), adds feedback, and clicks Publish.

**Response:** The system shall:
1. Validate that the total score does not exceed the assignment's `marks_total`.
2. If rubric is configured, validate that the sum of criterion scores equals the entered total. If not, return HTTP 422 with `{"error": {"code": "RUBRIC_SCORE_MISMATCH"}}`.
3. Set `submission.status = marked`; store `score`, `feedback_text`, `feedback_audio_url` (nullable), `marked_at`, `marked_by`.
4. Write to the `marks_register` table: `student_uid`, `subject_id`, `assignment_type`, `score`, `marks_total`, `term_id`, `source = assignment`, `source_id = assignment_id`, `tenant_id`. This auto-post constitutes gradebook integration.
5. Send a push notification to the student: "Your [assignment title] has been marked: [score]/[marks_total]."
6. Return HTTP 200 within 3,000 ms.

**Input specifications:**

| Field | Type | Constraints |
|---|---|---|
| `score` | integer | Required; 0 ≤ score ≤ `marks_total` |
| `criterion_scores` | JSON array | Required if rubric attached; must sum to `score` |
| `feedback_text` | string | Optional; max 5,000 characters |
| `feedback_audio_url` | string | Optional; Wasabi URL to a pre-uploaded audio file |

**Business rules:** BR-ELEARN-003, BR-ELEARN-004.
**Verifiability:** Teacher publishes mark of 14/20 → `marks_register` record created with `score = 14`, `marks_total = 20`, `assignment_type = Homework` (or whichever type was configured); student receives push notification "14/20". Student who did not submit → `marks_register` record with `status = not_submitted` (NSubmit).

---

#### FR-ELEARN-007: Online Quiz Creation

**Stimulus:** A teacher submits a POST request to `/api/v1/elearn/quizzes` with quiz configuration and question list.

**Response:** The system shall:
1. Validate all required fields and each question's structure.
2. Create a `quizzes` record with `title`, `subject_id`, `class_ids[]`, `opens_at`, `closes_at`, `time_limit_minutes` (nullable), `attempts_allowed`, `shuffle_questions`, `shuffle_answers`, `show_review_after_close`, `tenant_id`.
3. Create `quiz_questions` records for each question with `question_type` (`mcq`, `multi_select`, `true_false`, `short_answer`, `numeric`), `question_text`, `answer_options[]` (for MCQ/multi_select/true_false), `correct_answers[]`, `marks`.
4. Add questions to the `question_bank` for the subject if they do not already exist.
5. Return HTTP 200 with the quiz record within 500 ms at P95.

**Business rules:** BR-ELEARN-007.
**Verifiability:** Create a quiz with 10 MCQ questions and a 20-minute timer. Two students start the quiz → each sees a different question order. Both complete the quiz → MCQ scores computed immediately.

---

#### FR-ELEARN-008: Auto-Grading of MCQ, True/False, and Numeric Answers

**Stimulus:** A student submits a quiz attempt with answers to MCQ, True/False, or Numeric questions.

**Response:** The system shall:
1. For each `mcq` and `true_false` question: compare the student's selected answer against `correct_answers[]`. Award the question's `marks` value if correct; award 0 if incorrect.
2. For each `numeric` question: compare the student's submitted number against `correct_answers[0]` with an exact match (no tolerance unless configured). Award marks on exact match.
3. Compute the total auto-graded score.
4. Set `quiz_attempt.auto_graded_score` and `quiz_attempt.status = auto_graded` (if no short-answer questions) or `status = pending_manual_grading` (if short-answer questions exist).
5. Return the result to the student within 1,000 ms.

**Business rules:** BR-ELEARN-007.
**Verifiability:** Student answers 8 of 10 MCQ correctly → system awards marks for 8 within 1,000 ms; result displayed immediately. Quiz with 2 short-answer questions → `status = pending_manual_grading`; MCQ score visible; short-answer questions shown as Pending.

---

#### FR-ELEARN-009: Quiz Timer Persistence Through Connectivity Loss

**Stimulus:** A student loses internet connectivity while an active quiz timer is running.

**Response:** The system shall:
1. The client application shall cache the quiz progress (all answered questions and current elapsed time) in local storage every 30 seconds.
2. When connectivity is restored, the client shall resume from the cached state. The elapsed time shall continue from the cached checkpoint — it shall not reset.
3. If the timer expires while the student is offline, the client shall automatically submit the cached progress when connectivity returns. The system shall accept this submission as valid if the student lost connectivity before the timer expired.
4. The `quiz_attempts` record shall record `connectivity_lost = true` and `submitted_via_cache = true` for auditing.

**Business rules:** BR-ELEARN-006.
**Verifiability:** Student starts a 30-minute quiz at minute 10; connection drops. Connection restores at minute 25. Timer shows 25 minutes elapsed (not reset). Student submits at minute 30; submission accepted as on-time.

---

#### FR-ELEARN-010: Head Teacher E-Learning Compliance Report

**Stimulus:** A Head Teacher submits a GET request to `/api/v1/elearn/compliance-report?week=YYYY-WNN` specifying a calendar week.

**Response:** The system shall return a JSON object within 5,000 ms containing, for each teacher assigned to at least one class in the school:
- `teacher_id`, `teacher_name`
- `materials_posted` — count of study materials created during the specified week
- `assignments_set` — count of assignments published during the week
- `assignments_fully_marked` — count of assignments where all submitted student work has a `status = marked`
- `avg_marking_turnaround_hours` — mean time in hours between `submitted_at` and `marked_at` across all marked submissions for the week (null if no submissions marked)

**Business rules:** None — read-only aggregate, tenant-scoped.
**Verifiability:** Teacher A posted 3 materials, set 2 assignments, marked all in average 18 hours → report shows `materials_posted: 3`, `assignments_set: 2`, `avg_marking_turnaround_hours: 18.0`. Teacher B posted nothing → row shows zeros.

---

#### FR-ELEARN-011: Storage Quota Enforcement

**Stimulus:** A teacher uploads a file that would cause the school's total storage usage to exceed the configured quota.

**Response:** The system shall:
1. After malware scanning passes, calculate `current_usage_bytes + new_file_size_bytes`.
2. If the result exceeds the school's `storage_quota_bytes`, reject the upload: return HTTP 422 with `{"error": {"code": "QUOTA_EXCEEDED", "current_gb": X, "quota_gb": Y}}` and send an in-app alert to the School Owner/Director.
3. Do not store the file.
4. When `current_usage_bytes / storage_quota_bytes ≥ 0.90`, send a warning in-app notification to the School Owner/Director. This warning fires once per day until usage drops below 90%.

**Business rules:** BR-ELEARN-008.
**Verifiability:** Set quota to 1 GB; upload files totalling 950 MB → Owner receives 90% warning. Upload a 100 MB file → HTTP 422 `QUOTA_EXCEEDED`; no file stored; Owner receives alert.


---

### FR-AI: AI Module — Artificial Intelligence Features

> **Gate constraint (AI-GATE-001):** Every requirement in this section is conditionally active. No AI feature executes unless the tenant has an active `tenant_ai_modules` record (`status = 'active'`) AND the specific `feature_slug` is enabled in `tenant_ai_features`. Tenants without the AI add-on are entirely unaffected by this section. The gate check precedes every AI API call; failure returns HTTP 402 `AI_MODULE_INACTIVE`.

> **Cost constraint (AI-COST-001):** The system shall enforce the tenant `monthly_budget_ugx` ceiling before every AI call. If the budget is exhausted, the call is rejected with HTTP 402 `AI_BUDGET_EXCEEDED` and the user sees: "Your school's AI budget for this month has been reached. Contact your administrator to review."

> **Business rationale:** School owners pay for the AI module because each feature replaces hours of manual work by teachers or administrators — or gives the owner information they cannot obtain without it. Features are described in school-operational language so non-technical buyers understand the value immediately.

---

#### FR-AI-001: At-Risk Student Alert

**Feature slug:** `at_risk_students`

**Plain-English value:** Every Monday morning, the Head Teacher sees a ranked list of students likely to fail before exam season — with the specific reason why. Teachers can intervene while there is still time to make a difference.

**Stimulus:** The weekly batch job (Monday 05:00 EAT) runs for every tenant with `at_risk_students` enabled and an active AI module.

**Response:** The system shall:
1. Query the preceding 8 weeks per student: attendance rate, average mark (where available), days since last portal login, missed homework submissions (if E-Learning module active).
2. Batch up to 50 students per API call using the at-risk classification prompt template (see `ai-predictive-analytics` skill, student risk template).
3. Classify each student as `high_risk`, `medium_risk`, or `low_risk` with a signal phrase not exceeding 12 words (e.g., "Attendance 54% and average mark 38% this term").
4. Write results to `nlp_results` with `nlp_task = 'risk_scoring'` and `period = YYYY-MM`.
5. Display the `high_risk` list on the Head Teacher and Owner dashboards under the AI Insights panel (Zone 3).
6. Log each call to `ai_usage_log` and `ai_audit_log`.

**PII in prompt:** Student UIDs only. No names are sent to the AI. Student names are joined from the database at display time.

**Cost estimate:** ~1,000 tokens per class per week (Haiku model). A 10-class school costs approximately $0.32/month.

**Output schema:**

| Field | Type | Description |
|---|---|---|
| `student_uid` | UUID | Identifies the student (name joined at display layer) |
| `risk_level` | enum | `high_risk`, `medium_risk`, or `low_risk` |
| `signal` | string | Max 12-word explanation |
| `attendance_pct` | integer | Attendance percentage over the scoring window |
| `avg_mark_pct` | integer | Average mark percentage over the scoring window |
| `days_since_login` | integer | Days since last portal login; null if portal not used |

**Error conditions:**

| Condition | HTTP Code | Error Code |
|---|---|---|
| AI module inactive | 402 | `AI_MODULE_INACTIVE` |
| Budget exhausted | 402 | `AI_BUDGET_EXCEEDED` |
| Fewer than 4 weeks of data | — | Job skips class; logs `INSUFFICIENT_DATA` |
| LLM API unavailable | — | Job retries 3× with exponential backoff; logs `PROVIDER_UNAVAILABLE` |

**Business rules:** AI-GATE-001, AI-COST-001.
**Verifiability:** Enable `at_risk_students` for a test tenant with 50 students. Pre-seed 5 students with attendance below 60% and marks below 45%. Run batch job. Confirm: (a) 5 students appear in `nlp_results` with `risk_level = 'high_risk'`; (b) dashboard AI Insights panel shows the list; (c) no student name appears in `ai_audit_log.prompt_hash` source (`pii_scrubbed = 1`); (d) disabling the AI module causes the job to skip the tenant entirely.

---

#### FR-AI-002: Report Card Comment Generator

**Feature slug:** `report_card_narrative`

**Plain-English value:** Instead of every class teacher spending 2–3 hours writing 40 individual report card comments, the system suggests a comment for each student in seconds. The teacher reviews and approves — saving 80% of the time while remaining in full control.

**Stimulus:** An authorised user (Class Teacher+) sends `POST /api/v1/ai/report-card-comments` with `class_id` and `term_id`, after marks are finalised for the term.

**Response:** The system shall:
1. Gate check and budget check.
2. Collect per-student: class, term, subject marks, attendance %, UNEB aggregate and division where applicable.
3. Batch 10 students per API call.
4. Generate a 2–3 sentence professional comment in formal East African English per student: one achievement, one area for improvement, one encouragement.
5. Return suggested comments to the UI as draft values — not saved automatically.
6. Teacher must explicitly Accept, Edit, or Reject each comment. Only accepted or edited comments are written to `report_cards.head_teacher_comment` on the teacher's Save action.
7. Record Accept/Edit as `ai_feedback_log.rating = 'positive'`; Reject as `'negative'`.

**Human oversight level:** Hard Gate — no AI-generated content is saved without explicit teacher approval per comment (per `ai-ux-patterns` skill).

**Cost estimate:** ~400 tokens per student (Haiku). A 40-student class costs approximately $0.032/term. Negligible.

**Error condition:** LLM unavailable — UI displays: "AI comment generation is temporarily unavailable. Please write comments manually." This does not block the report card workflow.

**Business rules:** AI-GATE-001, AI-COST-001, BR-CAL-001.
**Verifiability:** Enable feature. Finalise marks for a class of 10. Click "Generate AI Comments." Confirm: (a) 10 suggested comments returned within 20 s; (b) no comment written to `report_cards` before teacher Save; (c) 10 rows in `ai_usage_log`; (d) each feedback action creates a row in `ai_feedback_log`.

---

#### FR-AI-003: School Owner Weekly Briefing

**Feature slug:** `daily_attendance_summary`

**Plain-English value:** Every Monday at 7am, the School Owner receives one paragraph in plain English describing how the school performed last week — attendance, fees, exam trends, and any alerts — without needing to log in and navigate reports.

**Stimulus:** The Monday 06:00 EAT batch job runs for every tenant with `daily_attendance_summary` enabled.

**Response:** The system shall:
1. Gate check and budget check.
2. Aggregate the past week: school-wide attendance rate, count of students with 3+ consecutive absences, fee collection percentage, top and bottom class by average mark, count of high-risk AI alerts.
3. Send aggregated statistics only to the LLM. No student PII in the prompt — aggregated figures only.
4. Generate a 3–4 sentence briefing in formal English suitable for a school director.
5. Deliver as an in-app notification to all `owner` and `head_teacher` role users for the tenant.
6. Display on the Owner dashboard as an AI Summary Narrative Card.
7. Log to `ai_usage_log` and `ai_audit_log` (prompt hash only — Constraint AI-DB-003, DPPA 2019 compliance).

**Cost estimate:** ~800 tokens per school per week (Haiku). Approximately $0.033/school/month.

**Error condition:** LLM unavailable — briefing is skipped silently for this week; no user-visible error.

**Business rules:** AI-GATE-001, AI-COST-001, DPPA 2019 (aggregated data only — no PII).
**Verifiability:** Enable feature. Seed prior-week attendance and fee data. Run Monday job. Confirm: (a) in-app notification delivered to owner; (b) narrative is 3–4 sentences; (c) contains no student UIDs or names; (d) `ai_audit_log` shows `pii_scrubbed = 1`.

---

#### FR-AI-004: Fee Default Prediction

**Feature slug:** `fee_default_prediction`

**Plain-English value:** One week before term opens, the Bursar sees a list of parents historically likely to delay or miss payment — so the school can contact them early, arrange payment plans, and reduce mid-term fee disputes.

**Stimulus:** The batch job runs on Tuesday, 7 days before each term `open_date`, for tenants with `fee_default_prediction` enabled and at least 2 full terms of payment history in `fee_payments`.

**Response:** The system shall:
1. Gate check and budget check.
2. Query per student: terms in arrear at term start, on-time full payments, KUPAA partial payment patterns, average days-late for first payment per term. Use `student_uid` as the identifier in the prompt — no student names.
3. Batch 30 students per API call.
4. Classify as `high_risk` (likely to default), `medium_risk` (likely to pay late), or `low_risk`.
5. Write results to `nlp_results` (`nlp_task = 'fee_default_prediction'`).
6. Display the `high_risk` list on the Bursar dashboard as "Fee Risk Report."
7. Allow CSV export: student name and parent contact joined from the database at export time — names are not included in the AI prompt.

**PII constraint (DPPA-CRITICAL):** Student names, parent names, and phone numbers shall NOT be sent to the AI. Financial payment history qualifies as special personal data under DPPA 2019 Schedule. Anonymisation in the prompt is mandatory. The `ai_audit_log` must record `pii_scrubbed = 1` for every call under this feature.

**Cost estimate:** ~500 tokens per 30 students (Haiku). A 500-student school costs approximately $0.007/term.

**Error condition:** Fewer than 2 terms of payment history — job skips tenant; logs `INSUFFICIENT_DATA`.

**Business rules:** AI-GATE-001, AI-COST-001, DPPA 2019 (financial data = special personal data).
**Verifiability:** Pre-seed 3 terms of payment data: 10 students with consistent late payment and arrears. Run batch job. Confirm: (a) 10 students classified `high_risk`; (b) `ai_audit_log` shows `pii_scrubbed = 1`; (c) Bursar dashboard shows "10 students: High Fee Risk"; (d) CSV export contains student name from database join, not from AI output.

---

#### FR-AI-005: Parent Feedback Sentiment Analysis

**Feature slug:** `parent_sentiment`

**Plain-English value:** After a parent feedback round, instead of reading 200 messages, the School Owner sees what percentage of parents are happy, the top 3 complaints, and the top 3 things parents praise — on one screen, generated in under 30 seconds.

**Stimulus:** Triggered automatically when a parent feedback batch exceeds 10 new submissions within 24 hours, OR on demand from the Owner Feedback Analytics screen.

**Response:** The system shall:
1. Gate check and budget check.
2. Collect feedback responses submitted since the last sentiment run.
3. Strip parent names from text using `PIIScrubber` before sending to the AI.
4. Batch 40 responses per API call. Classify: `sentiment` (positive/neutral/negative), `intensity` (strong/moderate/mild), `key_phrase` (max 8 words).
5. Run a theme detection call across the full batch: identify 3–7 recurring themes.
6. Store per-response results in `nlp_results` (`nlp_task = 'sentiment'`).
7. Store the theme summary in `nlp_results` (`nlp_task = 'themes'`).
8. Display on Owner dashboard: sentiment breakdown donut chart + top 3 positive and negative themes.
9. Accept Luganda, Swahili, and English without pre-translation.

**Cost estimate:** ~200 tokens per response (Haiku). 100 responses: $0.008/run.

**Business rules:** AI-GATE-001, AI-COST-001, DPPA 2019 (parent names scrubbed before dispatch).
**Verifiability:** Submit 20 feedback responses (mix of English and Luganda; 8 negative, 10 positive, 2 neutral). Trigger run. Confirm: (a) 20 rows in `nlp_results` with correct sentiment; (b) theme summary produced; (c) dashboard donut chart updates; (d) `ai_audit_log` shows `pii_scrubbed = 1` for all calls.

---

#### FR-AI-006: AI Module Activation

**Stimulus:** A Super Admin sends `POST /adminpanel/api/v1/tenants/{id}/ai-module` with `plan` and `monthly_budget_ugx`.

**Response:** The system shall:
1. Create or update the `tenant_ai_modules` record with `status = 'active'`.
2. Seed `tenant_ai_features` rows for all features included in the purchased plan, all with `is_enabled = 0` by default — the School Owner activates individual features.
3. Return HTTP 201 with the AI module record.

**Error condition:** Tenant already has an active AI module — HTTP 409 `AI_MODULE_ALREADY_ACTIVE`.

**Verifiability:** POST activation — `tenant_ai_modules` row created, status = active. Verify 9 `tenant_ai_features` rows seeded with `is_enabled = 0`. POST same tenant again — HTTP 409.

---

#### FR-AI-007: AI Budget Alert and Enforcement

**Stimulus:** A token cost is recorded in `ai_usage_monthly` causing `total_cost_ugx` to cross the `alert_threshold_pct` (default 80%) or 100% of `tenant_ai_modules.monthly_budget_ugx` for the current billing period.

**Response:**
- At 80%: in-app notification to School Owner — "Your school has used 80% of this month's AI budget (UGX X of UGX Y)."
- At 100%: in-app notification and email to School Owner. All subsequent AI calls for the tenant return HTTP 402 `AI_BUDGET_EXCEEDED` for the remainder of the billing period.
- Write one row to `ai_budget_alerts` per threshold crossed. The `UNIQUE(tenant_id, billing_period, threshold_pct)` constraint prevents duplicate alerts within the same period.

**Business rules:** AI-GATE-001, AI-COST-001.
**Verifiability:** Set `monthly_budget_ugx = UGX 10,000`. Simulate AI calls totalling UGX 8,001. Confirm: 80% alert delivered; `ai_budget_alerts` row created. Simulate total reaching UGX 10,001. Confirm: 100% alert delivered; next AI call returns HTTP 402 `AI_BUDGET_EXCEEDED`.
