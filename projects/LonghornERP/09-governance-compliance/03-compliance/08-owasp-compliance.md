# OWASP Top 10 (2021) Compliance Requirements

## 8.1 Scope

This section maps each of the ten vulnerability categories defined in the Open Web Application Security Project (OWASP) Top 10 (2021 edition) to the specific controls implemented in Longhorn ERP. For each category, the system requirement is stated using "the system shall" language and is therefore verifiable.

## 8.2 A01 — Broken Access Control

Broken access control occurs when users can act outside their intended permissions — accessing another user's data, elevating privileges, or bypassing function restrictions.

**Controls implemented:**

- RBAC enforcement at the middleware layer, as specified in Section 3. Every request resolves tenant identity, module activation, function permission, and branch restriction before executing.
- Tenant isolation at the data layer: all queries filter by `tenant_id` sourced from `TenantContext::getTenantId()`, never from request input, as specified in Section 4.
- Cross-tenant access returns HTTP 404 to prevent tenant enumeration (Section 4.3).
- Super admin impersonation is session-scoped, time-limited, and fully audited (Section 3.6).

**Measurable requirement:** The system shall reject 100% of requests where the authenticated `tenant_id` does not match the `tenant_id` of the requested resource, verified by penetration test.

## 8.3 A02 — Cryptographic Failures

Cryptographic failures include transmitting sensitive data in plaintext, using weak algorithms, and storing passwords without sufficient hashing.

**Controls implemented:**

- TLS 1.3 required for all connections in transit (Section 7.1). TLS 1.2 is the minimum fallback.
- AES-256 encryption at rest for all sensitive field categories: salary data, NIN, bank account numbers, biometric identifiers (Section 6.3).
- Passwords stored using Bcrypt with a minimum cost factor of 12. No plaintext passwords written to any storage, log, or API response.
- Sensitive field values excluded from audit log records; masked representations used where audit context requires them (Section 5.4).
- No sensitive data included in JWT claims beyond the minimum required for authorisation (`tid`, `uid`, `role`, `modules`).

**Measurable requirement:** A static analysis scan of the codebase shall produce 0 findings of plaintext password storage, hardcoded cryptographic keys, or use of MD5/SHA-1 for security-sensitive operations.

## 8.4 A03 — Injection

Injection flaws occur when untrusted data is sent to an interpreter as part of a query or command.

**Controls implemented:**

- All database queries shall use PDO prepared statements. String concatenation to form SQL queries is prohibited. PHPStan static analysis at level 8 shall flag any direct string interpolation into SQL.
- All output rendered in HTML templates shall pass through `htmlspecialchars()` with `ENT_QUOTES | ENT_HTML5` before rendering. This prevents cross-site scripting (XSS) injection.
- The `respect/validation` library is used for all input validation before data reaches the service layer. Unexpected field types and lengths are rejected before query execution.
- Command execution functions (`exec`, `shell_exec`, `system`, `passthru`) shall not be used in application code. If required for a specific operation, their use must be reviewed and approved, and all arguments must be escaped using `escapeshellarg()`.

**Measurable requirement:** PHPStan at level 8 shall produce 0 injection-related findings on the production codebase. A penetration test shall confirm 0 exploitable SQL injection or XSS vulnerabilities.

## 8.5 A04 — Insecure Design

Insecure design occurs when security controls are not built into the architecture from the beginning.

**Controls implemented:**

- Middleware stack enforces authentication, CSRF validation, module gating, RBAC, and branch restrictions in a defined, immutable sequence on every request (Section 3.3).
- Approval workflows with separation of duties controls prevent the same user from creating and approving the same transaction (Section 3.4).
- Module gating prevents access to features the tenant has not purchased, reducing the attack surface to the tenant's subscribed feature set.
- Zero-trust tenant boundary design: `tenant_id` is never trusted from caller input (Section 4.2).
- All new security controls require a code review by a second developer before merge to the main branch.

**Measurable requirement:** The security design review checklist (referenced in Section 10) shall be completed and signed off before any module is released to production.

## 8.6 A05 — Security Misconfiguration

Security misconfiguration includes leaving default credentials in place, enabling debug output in production, and overly permissive file permissions.

**Controls implemented:**

- PHP `display_errors` and `display_startup_errors` shall be set to `Off` in the production `php.ini`. Errors shall be written to a server-side log only.
- PHP `expose_php` shall be set to `Off` to suppress the `X-Powered-By: PHP/x.x.x` response header.
- Apache directory listing shall be disabled. The `Options -Indexes` directive shall be set for all document root directories.
- The `.env` file containing environment variables shall not be accessible via HTTP. An Apache `<Files .env> Deny from all </Files>` directive shall be enforced.
- File permissions for the application codebase shall be set to 644 for files and 755 for directories. The `.env` file shall be 600.
- A security hardening checklist shall be completed and signed off as part of every production deployment. The checklist shall be maintained in the deployment guide (`08-end-user-documentation/02-installation-guide/`).

**Measurable requirement:** The deployment hardening checklist shall produce 0 open items at launch. An automated configuration scan shall confirm PHP error display is disabled and directory listing is disabled.

## 8.7 A06 — Vulnerable and Outdated Components

Vulnerable components are third-party libraries with known security vulnerabilities.

**Controls implemented:**

- All PHP dependencies are managed by Composer. The `composer.lock` file is committed to version control to pin exact dependency versions.
- `composer audit` shall be run as part of the CI/CD pipeline on every build. A build with known high-severity vulnerabilities in direct dependencies shall not be deployed to production.
- Composer dependencies shall be reviewed and updated on a monthly schedule. Security patches for direct dependencies shall be applied within 7 days of public disclosure.
- Frontend JavaScript libraries (jQuery, Bootstrap, DataTables, etc.) shall be updated on a quarterly schedule or within 14 days of a high-severity CVE disclosure.

**Measurable requirement:** `composer audit` shall report 0 high or critical severity advisories for direct dependencies at any production deployment.

## 8.8 A07 — Identification and Authentication Failures

Authentication failures include weak passwords, missing multi-factor authentication, and inadequate session management.

**Controls implemented:**

- Password policy compliant with NIST SP 800-63B: minimum 12 characters, no complexity rules (character class requirements), breach-checked against known compromised password lists at registration, no forced periodic rotation.
- Two-factor authentication (2FA) via time-based one-time password (TOTP) is available for all user accounts. Tenant administrators may make 2FA mandatory for their users.
- Session tokens are cryptographically random, server-side, and bound to `tenant_id` and `user_id` (Section 2.2).
- Login attempt throttling: after 5 consecutive failed login attempts for an account, the system shall enforce a 15-minute lockout for that account. Lockout events are logged in the audit log.
- Active sessions are invalidated within 5 seconds of account deactivation (NFR-SEC-003).
- JWT refresh token rotation prevents replay of stolen refresh tokens (Section 2.3.4).

**Measurable requirement:** Penetration testing shall confirm that session tokens are not predictable, that account lockout engages after ≤ 5 failed attempts, and that disabled accounts cannot authenticate within a 5-second window.

## 8.9 A08 — Software and Data Integrity Failures

Integrity failures include deploying unsigned code and accepting unverified serialised data.

**Controls implemented:**

- The `composer.lock` file pins exact package versions and includes content hashes. Composer verifies package integrity against these hashes at install time.
- Deployment pipelines shall use the locked dependency set. `composer install --no-dev` (not `composer update`) shall be used for all production deployments.
- PHP serialisation (`serialize()` / `unserialize()`) shall not be used for user-supplied data. JSON is used for all data exchange. If `unserialize()` is required for a specific purpose, the `allowed_classes` parameter shall be set to `false` or a specific whitelist.
- Signed deployments: the deployment runbook shall specify a checksum verification step for production release packages.

**Measurable requirement:** The CI/CD pipeline shall verify Composer lock file integrity on every build. Any discrepancy between `composer.lock` and `vendor/` content shall halt the build.

## 8.10 A09 — Security Logging and Monitoring Failures

Logging failures occur when security events are not recorded or monitored, allowing breaches to go undetected.

**Controls implemented:**

- Immutable audit log captures all state-changing events, authentication events, and impersonation events (Section 5.3).
- Application-layer errors are written to a structured error log (not displayed to users) in a format compatible with log aggregation tools.
- Login failures, rate limit events, and refresh token reuse events are logged with IP address and timestamp.
- The audit log provides a searchable, exportable record for post-incident forensics.
- Audit log retention for 7 years ensures historical evidence is available for delayed investigations (Section 5.6).

**Measurable requirement:** The audit log shall capture 100% of the event types listed in Section 5.3. This shall be verified by integration test cases that exercise each event type and confirm a corresponding record exists in `audit_log`.

## 8.11 A10 — Server-Side Request Forgery

Server-Side Request Forgery (SSRF) occurs when the application makes HTTP requests to an attacker-controlled URL, potentially exposing internal network resources.

**Controls implemented:**

- All URL parameters accepted from user input (e.g., webhook callback URLs, external API endpoint configurations) shall be validated against an allowlist of permitted domains and schemes before any outbound HTTP request is made.
- The allowlist shall be maintained in the platform configuration and shall include only explicitly approved external API domains (e.g., URA EFRIS, MTN MoMo, Safaricom Daraja).
- HTTP redirects from external API responses shall not be automatically followed unless the final destination is also on the allowlist.
- Requests to private IP address ranges (RFC 1918: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), loopback addresses (127.0.0.1, ::1), and link-local addresses shall be rejected.
- The `file://`, `ftp://`, and `gopher://` URL schemes shall be rejected for all external HTTP client calls.

**Measurable requirement:** Penetration testing shall confirm that a request to an internal IP address via a user-supplied URL parameter is rejected with an appropriate error. The allowlist shall be reviewed and updated as part of each new external API integration.
