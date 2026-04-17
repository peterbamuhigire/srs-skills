# Authentication Model

## 2.1 Overview

Longhorn ERP implements two distinct authentication models: session-based authentication for web clients and JSON Web Token (JWT) Bearer token authentication for mobile clients. Both models are tenant-scoped — every authenticated session or token is bound to a single `tenant_id` resolved on the server at login.

## 2.2 Web Session-Based Authentication

Web session-based authentication applies to the Tenant Workspace (`/public/`) and the Super Admin Panel (`/public/superadmin/`).

### 2.2.1 Session Cookie Specification

The system shall issue a session cookie named `LONGHORN_ERP_SESSION` upon successful authentication. The cookie shall be configured with all of the following attributes:

- `HttpOnly` — the cookie shall not be accessible to client-side JavaScript.
- `Secure` — the cookie shall be transmitted only over HTTPS connections.
- `SameSite=Strict` — the cookie shall not be sent on cross-site requests, preventing cross-site request forgery (CSRF) via cookie leakage.
- No explicit domain scoping broader than the serving domain.

### 2.2.2 Server-Side Session Binding

The system shall store `tenant_id` and `user_id` exclusively in server-side session storage. These values shall not be read from, echoed from, or validated against any value in the request URI, query parameters, POST body, or HTTP headers. Session data shall be the single authoritative source of tenant and user identity for all web requests.

### 2.2.3 CSRF Protection

All state-changing web API requests (`/public/api/`, `/public/superadmin/api/`) shall require a valid `X-CSRF-Token` header. The system shall validate the token against the current session. Requests missing or presenting an invalid token shall receive HTTP 403 and shall not be processed.

### 2.2.4 Session Invalidation

The system shall invalidate all active sessions for a user within 5 seconds of an administrator disabling that user's account. This requirement is stated as **NFR-SEC-003** in `_context/domain.md`. Session invalidation shall also be triggered by: explicit logout, role change by an administrator, and tenant deactivation by a super administrator.

### 2.2.5 Session Timeout

The system shall expire an idle web session after a configurable inactivity period. The default inactivity timeout shall be 30 minutes. The maximum configurable timeout shall be 8 hours. Timeout values shall be stored in the tenant configuration table and shall not be overridable by the end user.

## 2.3 Mobile JWT Bearer Token Authentication

JWT Bearer token authentication applies to all mobile API endpoints at `/public/api/mobile/v1/`.

### 2.3.1 Token Issuance

The system shall issue a JWT access token and a JWT refresh token upon successful mobile login. Both tokens shall be signed using the RS256 algorithm (RSA Signature with SHA-256). The private signing key shall reside on the server and shall never be transmitted to any client.

### 2.3.2 JWT Claims Specification

Every access token issued shall contain the following registered and private claims:

| Claim | Type | Description |
|---|---|---|
| `iss` | String | Token issuer — the platform domain |
| `sub` | String | Subject — the `user_id` value |
| `iat` | Integer | Issued-at timestamp (Unix epoch) |
| `exp` | Integer | Expiry timestamp (Unix epoch) |
| `tid` | String | `tenant_id` of the authenticated tenant |
| `uid` | String | `user_id` of the authenticated user |
| `role` | String | The user's current role identifier within the tenant |
| `modules` | Array | List of module identifiers enabled for the authenticated tenant |

The `tid` claim shall be set from server-side tenant resolution at login. No client-supplied `tenant_id` value shall influence the `tid` claim.

### 2.3.3 Token Lifetime Policy

Token lifetime values shall be configurable per deployment environment via environment variables. The following defaults shall apply:

| Parameter | Environment Variable | Default Value |
|---|---|---|
| Access token lifetime | `JWT_ACCESS_TOKEN_TTL` | 15 minutes |
| Refresh token lifetime | `JWT_REFRESH_TOKEN_TTL` | 30 days |

These values shall be enforced server-side at token validation. A client presenting an expired access token shall receive HTTP 401 with error code `TOKEN_EXPIRED`.

### 2.3.4 Refresh Token Rotation

The system shall implement refresh token rotation. When a client exchanges a valid refresh token for a new access token, the system shall:

1. Issue a new access token signed with the current server key.
2. Issue a new refresh token and store its hash in the `mobile_refresh_tokens` table.
3. Immediately invalidate the previous refresh token.

Reuse of an already-rotated refresh token shall be treated as a potential token theft event. The system shall invalidate all refresh tokens for the affected `user_id` and shall log the event in the audit log with action type `REFRESH_TOKEN_REUSE_DETECTED`.

### 2.3.5 Token Revocation

The system shall maintain a server-side revocation record for all issued refresh tokens. Explicit logout, role change, account deactivation, and tenant deactivation shall revoke all active refresh tokens for the affected user. Revoked access tokens remain invalid until their `exp` claim is reached; the short access token lifetime (15 minutes by default) limits the exposure window.
