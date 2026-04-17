# Security Architecture

## 6.1 Security Model Overview

The Longhorn ERP security model addresses four threat surfaces: web browser clients, mobile native clients, the REST API, and the shared-database multi-tenant data layer. Each surface has a distinct authentication and authorisation mechanism. The model is designed to satisfy OWASP Top 10 (2021), NIST SP 800-63B authentication assurance levels, and the Uganda Data Protection and Privacy Act 2019.

## 6.2 Web Authentication

**Mechanism:** Session-based authentication.

**Session cookie:** `LONGHORN_ERP_SESSION`

**Cookie attributes:**

| Attribute | Value | Rationale |
|---|---|---|
| `HttpOnly` | `true` | Prevents JavaScript access; mitigates XSS token theft. |
| `SameSite` | `Strict` | Prevents cross-site request forgery (CSRF) via browser-level enforcement. |
| `Secure` | `true` (production) | Transmits cookie only over TLS. |
| `Path` | `/public/` | Scopes cookie to the tenant workspace path. |

**Session invalidation:** The system shall invalidate all active sessions for a user within 5 seconds of an administrator disabling that user's account (NFR-SEC-003).

**Two-factor authentication (2FA):** Supported via time-based one-time password (TOTP) per NIST SP 800-63B AAL2. 2FA enforcement is configurable per tenant role.

## 6.3 Mobile Authentication

**Mechanism:** JSON Web Token (JWT) Bearer token using the `firebase/php-jwt` 7.0 library.

**JWT claims:**

| Claim | Key | Description |
|---|---|---|
| Tenant identifier | `tid` | The tenant's unique identifier. |
| User identifier | `uid` | The authenticated user's identifier. |
| Role | `role` | The user's primary role code. |
| Active modules | `modules` | Array of module codes active for the tenant. |
| Expiry | `exp` | Standard JWT expiry timestamp. |

**Refresh rotation:** Access tokens expire in 15 minutes. Refresh tokens expire in 30 days and rotate on each use (the old refresh token is immediately invalidated). Refresh token records are stored server-side so that a compromised refresh token can be revoked.

**Token revocation:** Revoked token identifiers are stored in a blocklist table checked on every authenticated API request.

## 6.4 CSRF Protection

All state-changing web requests (HTTP POST, PUT, DELETE, and PATCH to `/public/api/`) must include a valid `X-CSRF-Token` header. The token is a cryptographically random value tied to the user's session, generated at session creation and regenerated after each successful authentication.

The CSRF token is injected into each page by the PHP renderer as a JavaScript variable. All page-level JavaScript files read this variable and include the header on every AJAX request. Requests missing or bearing an invalid CSRF token are rejected with HTTP 403.

CSRF protection does not apply to the Mobile API (`/public/api/mobile/v1/`) because mobile clients are stateless and authenticate via JWT Bearer token, which is inherently CSRF-resistant.

## 6.5 Rate Limiting

Rate limiting uses a token bucket algorithm applied at two granularities:

| Limit Type | Scope | Default Limit |
|---|---|---|
| Per-tenant | All requests from a single `tenant_id` | Configurable per subscription plan |
| Per-user | All requests from a single `user_id` | 300 requests per minute |

When a limit is exceeded, the system returns HTTP 429 Too Many Requests with a `Retry-After` header. Rate limit counters shall be stored in a sub-millisecond key-value store (e.g., Redis or APCu) and shall reset on the rolling window boundary.

## 6.6 Audit Log Immutability

The audit log is INSERT-only (NFR-SEC-002). No `UPDATE` or `DELETE` statement shall be executed against the `audit_log` table by any code path, including super administrator operations. The MySQL 9.1 user account used by the application shall be granted only `INSERT` and `SELECT` privileges on `audit_log` — `UPDATE` and `DELETE` privileges are withheld at the database level.

Every Create, Read (sensitive), Update, Delete (CRUD), and approval action shall generate an audit log entry recording:

- `tenant_id`, `branch_id`, `user_id`
- Event type, affected entity type, affected entity identifier
- Old values (JSON), new values (JSON)
- Client IP address
- Timestamp (UTC)

Audit records shall be retained for a minimum of 7 years per the AUDIT module specification, satisfying Uganda Companies Act requirements.

## 6.7 Transport and Storage Encryption

- **In transit:** TLS 1.3 for all external connections (browser, mobile app, webhook callbacks).
- **At rest:** AES-256 encryption for sensitive fields. Fields subject to field-level encryption include: user passwords (bcrypt, cost factor ≥ 12), API keys, mobile money gateway credentials, SMTP passwords, and any Personally Identifiable Information (PII) fields flagged in the database schema.
- **Database backups** shall be encrypted using AES-256 before writing to storage.

## 6.8 OWASP Top 10 Compliance Requirements

The following requirements are derived from NFR-SEC-001 through NFR-SEC-003 and the OWASP Top 10 (2021) standard:

| OWASP Risk | Mitigation |
|---|---|
| A01 — Broken Access Control | Middleware pipeline enforces `RequirePermission` on every request; `tenant_id` from session only; cross-tenant returns 404. |
| A02 — Cryptographic Failures | TLS 1.3 in transit; AES-256 at rest; bcrypt (cost ≥ 12) for passwords; no MD5 or SHA-1. |
| A03 — Injection | PDO prepared statements only; no raw SQL concatenation; output HTML-escaped via `htmlspecialchars()`. |
| A04 — Insecure Design | Service layer enforces business rule validation via `respect/validation` 2.3; no trust of client-supplied data. |
| A05 — Security Misconfiguration | `.env` via `vlucas/phpdotenv` 5.6; no credentials in source code; error details suppressed in production. |
| A06 — Vulnerable Components | Composer dependency audit in CI pipeline; PHPStan 1.11 static analysis enforced. |
| A07 — Authentication Failures | NIST SP 800-63B AAL2 for admin roles; 2FA support; session invalidation within 5 seconds of account disable (NFR-SEC-003). |
| A08 — Software Integrity Failures | Composer lock file committed; no `--no-verify` bypasses in deployment scripts. |
| A09 — Logging Failures | Immutable INSERT-only audit log; all CRUD and approval events logged (NFR-SEC-002). |
| A10 — SSRF | Outbound HTTP calls (integrations) use an allowlist of permitted external domains. |
