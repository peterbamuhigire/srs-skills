## Section 3: External Interface Requirements

### 3.1 User Interfaces

#### 3.1.1 School Admin Workspace — Web Portal (`/`)

**Primary users:** School Owner/Director, Head Teacher, Class Teacher, Accounts Bursar, Receptionist.

**Technology:** React 18 / TypeScript / Vite, shadcn/ui component library, Tailwind CSS, Zustand state management.

**Layout constraints:**

- Responsive layout. Minimum supported viewport: 360 px wide (mobile web fallback). Optimised for 1,024 px+ desktop.
- Left-side navigation panel collapsed to icon-only below 768 px.
- All data tables support pagination (default 25 rows per page), column sorting, and a global search field that uses Meilisearch full-text results.
- All destructive actions (delete, deactivate, refund approval) require a confirmation dialog before execution.
- All forms validate client-side before submission and display server-side validation errors inline beneath the relevant field.
- All monetary amounts display with the UGX prefix and comma-separated thousands (e.g., `UGX 1,250,000`).

**Accessibility:** WCAG 2.1 Level AA (see NFR `EDU-NFR-002`). All interactive elements keyboard-operable. Minimum colour contrast ratio 4.5:1 for all text.

**Loading states:** Every asynchronous operation displays a loading indicator. Operations exceeding 3 seconds display a progress message. Completed bulk operations display a summary result (e.g., "142 of 143 report cards generated — 1 failed: [student name]").

**Session timeout behaviour:** When the 30-minute idle timeout fires, the system shall display a modal warning 2 minutes before session expiry. If the user does not interact, the session is destroyed and the login screen is displayed with the message: "Your session expired due to inactivity."

#### 3.1.2 Super Admin Panel (`/adminpanel/`)

**Primary users:** Chwezi Core Systems staff only.

**Layout:** Separate single-page application, distinct navigation, no shared components with the school workspace.

**Specific constraints:**

- MFA challenge required on every login (TOTP or SMS OTP). Login without MFA is rejected.
- IP allowlist configurable in platform settings; login from an unlisted IP triggers an additional email confirmation step.
- Every page that displays tenant data shows a persistent banner: "You are viewing [School Name] data in support mode. All actions are logged."
- Impersonation feature (start school admin session as a school user) displays a top-bar indicator and logs start/end with justification text.

#### 3.1.3 End User Portal (`/memberpanel/`)

**Primary users:** Students, Parents/Guardians.

**Layout:** Simplified, mobile-first. Large tap targets (minimum 44 × 44 px per WCAG). Minimal navigation depth (maximum 3 taps to any content). Support for low-bandwidth rendering: images lazy-loaded, lazy-loaded PDF previews.

**Phase 1 scope for end users:**

- Student: view timetable, view results, view fee balance.
- Parent: view child's results, fee balance, attendance summary.

**Language:** English (Phase 1). Luganda toggle planned for Phase 2.

#### 3.1.4 Progressive Web App (PWA) — Offline Attendance and Mark Entry

The web portal installs as a PWA on Chrome/Android. Workbox service worker caches the attendance entry form and mark entry form for offline use.

**Offline behaviour:**

- The user may enter attendance records and exam marks while offline. Entries are stored in browser IndexedDB.
- On network restoration, a background sync job submits all queued entries to the server within 5 minutes.
- Conflict resolution: if the server already has an attendance record for the same student/date submitted by another user during the offline period, the server rejects the offline entry with `{"status": "conflict", "existing_entry": {...}}`. The PWA notifies the user and requires manual resolution.

#### 3.1.5 Android Mobile Application (Phase 6 — Interface Defined Here for Architecture Alignment)

Though the Android app launches in Phase 6, the REST API designed in Phase 1 must support mobile clients from the start. The following constraints apply to the Phase 1 API design:

- All API endpoints must return the standard JSON envelope `{"success": true|false, "data": {...}, "meta": {...}}`.
- Pagination uses `page` and `per_page` query parameters (default `per_page=25`, maximum `per_page=100`).
- JWT authentication (access token 15 min, refresh token 30 days with rotation) must be supported from Phase 1 API launch.
- The Android app will use Jetpack Compose (Kotlin) with MVVM + Repository pattern and Room for offline data.

### 3.2 Hardware Interfaces

#### 3.2.1 Receipt Printer

The bursar's workstation may connect a USB or network thermal receipt printer (common model: 80 mm thermal roll). The system generates printer-friendly HTML layouts that the browser's print dialog sends to any locally installed printer driver. The system does not require a specific printer model or driver; it does not communicate directly with the printer hardware.

#### 3.2.2 Barcode / QR Scanner (Out of Phase 1 Scope)

Library module (Phase 2) may support USB HID barcode scanners. Out of Phase 1 scope.

#### 3.2.3 Mobile Devices (Android — Phase 6+)

Minimum hardware: Android 8.0 (API level 26), 2 GB RAM, 16 GB internal storage, 720 × 1,280 px screen. Offline-capable (Room database + WorkManager). Camera required for QR code attendance (Phase 4 add-on).

### 3.3 Software Interfaces

#### 3.3.1 Africa's Talking SMS Gateway

| Attribute | Value |
|---|---|
| Purpose | Automated SMS alerts: attendance (BR-ATT-002), fee reminders (BR-FEE-006) |
| Protocol | REST API (HTTPS POST) |
| Authentication | API key + username in request headers |
| Phase 1 scope | Outbound SMS only. Inbound SMS (USSD/short-code replies) is Phase 11. |
| Sender ID | Uganda-registered sender ID (to be obtained before Phase 1 launch) |
| Failure handling | Failed SMS delivery is logged with HTTP status and Africa's Talking error code. The system does not retry immediately; a scheduled job retries failed messages once after 15 minutes. |
| Rate limit | Respects Africa's Talking per-account rate limits. The system queues SMS jobs through Laravel Horizon to prevent burst overloads. |

#### 3.3.2 SchoolPay API (Phase 2 — Interface Defined for Phase 1 Architecture Alignment)

SchoolPay integration is explicitly out of Phase 1 scope (deferred to Phase 2 per decision 2026-03-28). However, the Phase 1 `fee_payments` table schema must include the `external_reference` column with a `UNIQUE` constraint to support idempotency when SchoolPay integration is added. No SchoolPay API calls are made in Phase 1.

#### 3.3.3 Anthropic Claude API

| Attribute | Value |
|---|---|
| Purpose | AI-assisted analytics: predictive fee defaulter alerts, attendance pattern analysis, natural-language report commentary (Phase 2+) |
| Model | `claude-sonnet-4-6` (latest available at implementation time) |
| Phase 1 scope | Not invoked in Phase 1. API client library included as a dependency for Phase 2. |
| Authentication | `ANTHROPIC_API_KEY` environment variable |

#### 3.3.4 AWS S3

| Attribute | Value |
|---|---|
| Purpose | Persistent storage of generated PDF report cards, student passport photos, uploaded documents |
| SDK | AWS SDK for PHP (Laravel Flysystem S3 adapter) |
| Bucket configuration | Separate buckets for `production`, `staging`, `development` |
| Access | Private bucket; all URLs are pre-signed with 1-hour expiry for user-facing downloads |
| File naming | `{tenant_id}/{year}/{document_type}/{uuid}.{ext}` |

#### 3.3.5 Firebase Cloud Messaging (FCM)

| Attribute | Value |
|---|---|
| Purpose | Web push notifications for PWA (attendance reminders, mark entry deadlines) |
| Phase 1 scope | Push notification infrastructure bootstrapped in Phase 1; teacher-facing notifications for mark entry deadline |
| SDK | Firebase Admin SDK for PHP (server-side), Firebase JS SDK (client-side) |
| Fallback | If push notification delivery fails, the system falls back to displaying a persistent in-app banner on next login |

#### 3.3.6 Meilisearch

| Attribute | Value |
|---|---|
| Purpose | Full-text search for student names, staff names, and document content |
| Integration | Laravel Scout driver |
| Phase 1 scope | Student search (name, admission number, NIN, LIN), staff search |
| Index update | Synchronous on create/update in development; asynchronous via queue in production |

#### 3.3.7 Mailgun / Postmark

| Attribute | Value |
|---|---|
| Purpose | Transactional email (password reset, welcome emails, invoice copies) |
| Phase 1 scope | Password reset emails, new user welcome emails |
| Configuration | `MAIL_MAILER`, `MAIL_HOST`, `MAIL_USERNAME`, `MAIL_PASSWORD` environment variables |

### 3.4 Communications Interfaces

#### 3.4.1 REST API

The system exposes a versioned REST API at `/api/v1/`. All endpoints:

- Accept and return `application/json`.
- Include `Content-Type: application/json` in all responses.
- Return the standard JSON envelope:

```json
{
  "success": true,
  "data": {},
  "meta": {
    "page": 1,
    "per_page": 25,
    "total": 100
  }
}
```

Error responses:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable description",
    "details": {
      "field_name": ["Validation message"]
    }
  }
}
```

Standard HTTP status codes:

| Code | Meaning in this API |
|---|---|
| 200 | Success (GET, PUT, PATCH) |
| 201 | Resource created (POST) |
| 204 | Success, no body (DELETE) |
| 400 | Bad request (malformed JSON, missing required field) |
| 401 | Unauthenticated (no token, expired token) |
| 403 | Forbidden (authenticated but insufficient permission) |
| 404 | Resource not found (or cross-tenant access attempt — return 404, not 403, to prevent tenant enumeration) |
| 409 | Conflict (duplicate unique key) |
| 422 | Unprocessable entity (business rule violation, validation error with detail) |
| 429 | Rate limit exceeded |
| 500 | Internal server error |

#### 3.4.2 API Rate Limiting

Aligned with `multi-tenant-saas-architecture` skill:

| Scope | Limit |
|---|---|
| Per tenant | 1,000 requests per minute |
| Per authenticated user | 100 requests per minute |
| Per IP address (unauthenticated) | 60 requests per minute |
| Admin endpoints (`/adminpanel/api/`) | 50 requests per minute |

Rate limit responses return HTTP 429 with `Retry-After` header in seconds and `X-RateLimit-Remaining: 0`.

#### 3.4.3 Transport Security

- All HTTP → HTTPS redirects enforced at the web server layer (Nginx/Caddy).
- HSTS header: `Strict-Transport-Security: max-age=31536000; includeSubDomains`.
- TLS 1.0 and TLS 1.1: disabled at the server cipher configuration.
- TLS 1.2 and TLS 1.3: accepted.
- Minimum cipher suite: ECDHE with AES-128-GCM-SHA256 or stronger.

#### 3.4.4 Webhook Receivers (Phase 2 — Defined for Phase 1 Architecture Alignment)

SchoolPay sends payment notifications via HTTPS POST webhooks. Although Phase 1 does not integrate SchoolPay, the webhook receiver endpoint (`POST /api/v1/webhooks/schoolpay`) shall be scaffolded in Phase 1 and return HTTP 200 with `{"status": "not_configured"}` until Phase 2 activates it. This prevents SchoolPay from being unable to deliver future webhooks once integration is enabled.

#### 3.4.5 CORS Policy

Cross-Origin Resource Sharing (CORS) is restricted to the platform's own domains. Wildcard `*` origins are prohibited. The allowed-origins list is configured per deployment environment via the `CORS_ALLOWED_ORIGINS` environment variable.
