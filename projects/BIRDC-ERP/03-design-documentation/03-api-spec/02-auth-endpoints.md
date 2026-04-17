## Section 1 — Authentication Endpoints

These endpoints handle identity verification, token lifecycle, password management, and multi-factor authentication. No authentication token is required for `POST /auth/login` and `POST /auth/password/reset-request`.

---

### 1.1 POST /auth/login

**Description:** Authenticate a user with username and password. Returns an access token and refresh token on success.

**Auth required:** No

**RBAC roles permitted:** All (public endpoint — no token needed)

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `username` | `string` | Required, max 100 | Username or email address |
| `password` | `string` | Required, min 8 | Plaintext password (TLS encrypted in transit) |
| `device_id` | `string` | Required, max 255 | Unique Android device identifier — stored in `tbl_user_sessions` |
| `device_name` | `string` | Optional, max 255 | Human-readable device name (e.g., "Samsung A34 — Agent Okello") |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `access_token` | `string` | JWT access token — 15-minute validity |
| `refresh_token` | `string` | JWT refresh token — 30-day validity |
| `token_type` | `string` | Always `"Bearer"` |
| `expires_in` | `integer` | Access token validity in seconds (900) |
| `requires_totp` | `boolean` | `true` if the user's role requires TOTP 2FA — client must redirect to `/auth/totp/verify` before granting access |
| `user` | `object` | User profile summary (see JWT Payload Structure) |

**Business rules enforced:**

- Account lockout after 5 consecutive failures (configurable duration) per DC-002.
- Argon2id password verification.

---

### 1.2 POST /auth/refresh

**Description:** Exchange a valid refresh token for a new access token. Used by Android `WorkManager` before the current access token expires.

**Auth required:** Refresh token in request body (no Bearer header)

**RBAC roles permitted:** All authenticated users

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `refresh_token` | `string` | Required | The refresh token obtained from `/auth/login` |
| `device_id` | `string` | Required | Must match the device ID used at login |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `access_token` | `string` | New JWT access token |
| `expires_in` | `integer` | Validity in seconds (900) |

**Error conditions:** Returns `401 TOKEN_EXPIRED` if the refresh token has expired or been revoked. The user must re-authenticate.

---

### 1.3 POST /auth/logout

**Description:** Revoke the current session — invalidates the refresh token stored in `tbl_user_sessions`. The access token is short-lived and expires naturally.

**Auth required:** JWT Bearer

**RBAC roles permitted:** All authenticated users

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `refresh_token` | `string` | Required | The refresh token to revoke |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `message` | `string` | `"Session terminated successfully."` |

---

### 1.4 POST /auth/totp/verify

**Description:** Verify a TOTP one-time code for accounts that require 2FA (Director, Finance Director, IT Administrator roles). Must be called after `/auth/login` when `requires_totp` is `true` in the login response.

**Auth required:** JWT Bearer (the initial access token returned by `/auth/login` before TOTP verification)

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `IT_ADMIN`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `totp_code` | `string` | Required, 6 digits | Time-based one-time password from Google Authenticator |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `verified` | `boolean` | `true` on successful verification |
| `access_token` | `string` | New full-access JWT token (TOTP-verified claim added) |

**Error conditions:** Returns `401 UNAUTHENTICATED` after 5 consecutive wrong TOTP codes. Lockout is logged in `tbl_audit_log`.

---

### 1.5 POST /auth/password/reset-request

**Description:** Initiate a password reset. Sends a one-time reset link to the user's registered email address. Used when a user cannot log in.

**Auth required:** No

**RBAC roles permitted:** All (public endpoint)

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `email` | `string` | Required, valid email | Registered email address |

**Response schema (200 OK):**

Always returns success regardless of whether the email exists (prevents email enumeration).

| Field | Type | Description |
|---|---|---|
| `message` | `string` | `"If this email is registered, a reset link has been sent."` |

---

### 1.6 POST /auth/password/reset

**Description:** Set a new password using a valid reset token delivered via email.

**Auth required:** No (reset token in body authenticates the request)

**RBAC roles permitted:** All

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `reset_token` | `string` | Required | Token from the password reset email |
| `new_password` | `string` | Required, min 8 | New password (Argon2id hashed on server) |
| `confirm_password` | `string` | Required | Must match `new_password` |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `message` | `string` | `"Password updated successfully. Please log in."` |

---

### 1.7 GET /auth/me

**Description:** Retrieve the authenticated user's profile, roles, and permissions. Called by Android apps at startup to load user context.

**Auth required:** JWT Bearer

**RBAC roles permitted:** All authenticated users

**Request body:** None (GET request)

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `user_id` | `integer` | User primary key |
| `name` | `string` | Full name |
| `username` | `string` | Login username |
| `email` | `string` | Email address |
| `role_code` | `string` | Role code (e.g., `SALES_AGENT`) |
| `role_name` | `string` | Human-readable role name |
| `permissions` | `string[]` | Array of permission codes |
| `agent_id` | `integer\|null` | Linked agent ID if applicable |
| `photo_url` | `string\|null` | Profile photo URL |
| `last_login` | `string` | ISO 8601 datetime of last successful login |

---

### 1.8 POST /auth/biometric/register

**Description:** Register a device's biometric credential (fingerprint / face) for future passwordless login using Android `BiometricPrompt`. The server stores a device-bound public key.

**Auth required:** JWT Bearer (user must already be authenticated via password on this device)

**RBAC roles permitted:** All authenticated users

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `device_id` | `string` | Required | Android device identifier |
| `public_key` | `string` | Required | Base64-encoded RSA public key generated on device (private key stays in Android Keystore) |
| `biometric_type` | `string` | Required | `"fingerprint"` or `"face"` |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `credential_id` | `integer` | Server-assigned credential ID |
| `registered_at` | `string` | ISO 8601 datetime |
| `message` | `string` | `"Biometric credential registered successfully."` |

---
