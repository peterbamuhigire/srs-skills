# 9. Security Architecture

## 9.1 8-Layer Authorisation Model

The BIRDC ERP authorisation system evaluates 8 permission layers in sequence. A request must pass all applicable layers before access is granted. Any layer returning `false` immediately rejects the request.

| Layer | Name | Evaluation Logic |
|---|---|---|
| L1 | Role | Does the authenticated user hold a role that is granted access to this resource? |
| L2 | Page | Is the target page/route included in this role's allowed page list? |
| L3 | API Endpoint | Is the specific API endpoint (method + route) in this role's allowed endpoint list? |
| L4 | UI Element | Is the specific UI element (button, field, action) visible and active for this role? |
| L5 | Location-Based | Is the user's IP address or device within an allowed location for this action? (e.g., Admin panel blocked from external IP) |
| L6 | Time-Based | Is the current time within the allowed time window for this role and action? |
| L7 | Conditional Rules | Does this action satisfy all configured conditional business rules? (e.g., segregation of duties: creator ≠ approver per BR-003) |
| L8 | Object Ownership | Does the user have ownership or explicit access rights to this specific record? (e.g., agent can only see their own invoices) |

The permission matrix is stored in `tbl_rbac_permissions` and is fully configurable by the IT Administrator via the admin panel — no code change required for permission changes (DC-002).

## 9.2 Authentication

| Concern | Web Application | Mobile API |
|---|---|---|
| Method | Session-based: PHP session with `HttpOnly`, `SameSite=Lax` cookies | JWT Bearer tokens: `Authorization: Bearer <access_token>` header |
| Session management | Session ID regenerated on login; old session invalidated | Access token: 15-minute TTL; Refresh token: 30-day TTL stored in `EncryptedSharedPreferences` |
| Password hashing | Argon2id (preferred) or bcrypt — never MD5/SHA1 | Same credential store |
| Account lockout | 5 failed attempts → configurable lockout (default 30 minutes) | Same; tracked per device fingerprint |
| 2FA | TOTP (RFC 6238 — Google Authenticator compatible) mandatory for: Director, Finance Director, IT Administrator | Not required for agents on mobile app; required for executive dashboard app users |
| Session expiry | Configurable idle timeout (default 60 minutes for staff; 15 minutes for admin panel) | Refresh token rotation on each use |

## 9.3 Audit Trail Architecture

Every state-changing action (INSERT, UPDATE, DELETE) on audited tables is captured in `tbl_audit_log` via database AFTER triggers (`trg_audit_insert`, `trg_audit_update`). The audit log is append-only — no UPDATE or DELETE privilege is granted to the application database user on `tbl_audit_log`.

| Column | Type | Description |
|---|---|---|
| `id` | BIGINT | Append-only sequential ID |
| `user_id` | INT | Actor's user ID (NULL for system-generated actions) |
| `user_email` | VARCHAR(255) | Actor's email at time of action (denormalised for immutability) |
| `ip_address` | VARCHAR(45) | Actor's IP address |
| `action` | VARCHAR(20) | `INSERT`, `UPDATE`, `DELETE` |
| `table_name` | VARCHAR(100) | Target table |
| `record_id` | BIGINT | Primary key of the affected record |
| `old_values` | JSON | Full row snapshot before the change (NULL for INSERT) |
| `new_values` | JSON | Full row snapshot after the change (NULL for DELETE) |
| `created_at` | TIMESTAMP | UTC timestamp |

Audit log retention: 7 years (aligned to Uganda Companies Act and Income Tax Act requirements — DC-003).

## 9.4 Segregation of Duties Enforcement (BR-003)

Segregation of duties (SoD) is enforced at Layer 7 of the authorisation model (Conditional Rules). It is enforced at the API layer, not merely at the UI layer — a direct API call cannot bypass it.

| Transaction | Creator | Approver / Verifier | SoD Check |
|---|---|---|---|
| Journal Entry | Accounts Assistant | Finance Manager | `journal.created_by ≠ current_user.id` |
| Purchase Order | Procurement Officer | Finance Manager | `lpo.created_by ≠ current_user.id` |
| Stock Adjustment | Store Clerk | Store Manager | `adjustment.created_by ≠ current_user.id` |
| Agent Remittance | Cashier (receives cash) | Supervisor | `remittance.created_by ≠ current_user.id` |
| Payroll Run | Payroll Officer | Finance Manager | `payroll_run.created_by ≠ current_user.id` |
| Agent Stock Issuance | Storekeeper | Store Manager | `issuance.created_by ≠ current_user.id` |

## 9.5 Additional Security Controls

| Control | Implementation |
|---|---|
| SQL injection | 100% PDO prepared statements; no string concatenation in queries |
| XSS prevention | `htmlspecialchars()` on all output; Content Security Policy header |
| CSRF | CSRF tokens on all state-changing forms; validated before controller execution |
| Sensitive fields at rest | TLS 1.3 in transit; sensitive database fields (NIN, mobile money numbers) encrypted at rest using AES-256 |
| Database credentials | Stored in `.env` file only; never committed to version control; application DB user has minimum required privileges |
| OWASP Top 10 | Full remediation verified during Phase 7 security hardening and penetration test |
| Error handling | Production error pages never expose stack traces, query strings, or file paths to the browser |
