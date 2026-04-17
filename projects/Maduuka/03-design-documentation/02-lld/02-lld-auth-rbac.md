---
title: "Maduuka Platform — Low-Level Design, Section 2: Authentication and RBAC"
author: "Chwezi Core Systems"
date: "2026-04-05"
---

# Authentication and Role-Based Access Control

**Document ID:** MADUUKA-LLD-002
**Version:** 1.0
**Status:** Draft
**Owner:** Peter Bamuhigire, Chwezi Core Systems
**Date:** 2026-04-05

---

## 1. AuthService

`AuthService` orchestrates all authentication operations. It depends on `UserRepository`, `RefreshTokenRepository`, and `JWTService` injected via the constructor.

### 1.1 Method Signatures

```php
class AuthService
{
    /**
     * Validates credentials, issues a JWT access token and refresh token,
     * and records a LOGIN event in the audit log.
     *
     * @throws AuthenticationException if credentials are invalid or account is suspended
     * @throws RateLimitException if login attempts exceed 5 failures within 15 minutes
     */
    public function login(
        string $email,
        string $password,
        string $deviceId,
        string $ipAddress,
        string $userAgent
    ): AuthTokenPair;

    /**
     * Validates the refresh token, issues a new access token,
     * and rotates (replaces) the refresh token.
     *
     * @throws AuthenticationException if refresh token is invalid, expired, or revoked
     */
    public function refreshToken(string $refreshToken): AuthTokenPair;

    /**
     * Revokes the refresh token for the authenticated device
     * and records a LOGOUT event in the audit log.
     */
    public function logout(int $userId, string $deviceId, int $franchiseId): void;

    /**
     * Validates a TOTP code against the user's stored TOTP secret.
     * On success, upgrades the provisional access token to full-access.
     *
     * @throws AuthenticationException if the TOTP code is invalid
     * @throws RateLimitException if TOTP failures exceed 5 within 15 minutes
     */
    public function validateTOTP(int $userId, string $code, int $franchiseId): AuthTokenPair;
}
```

### 1.2 Login Flow

1. Retrieve the user record from `users` table by email, filtered by `is_active = TRUE`.
2. Verify the submitted password against `password_hash` using `password_verify()` (bcrypt, cost factor >= 12).
3. If verification fails, increment the failed-login counter in the rate-limit store (Redis or database-backed). If the counter reaches 5, return `RateLimitException` and lock for 15 minutes.
4. Check `businesses.subscription_status`; if `suspended` or `cancelled`, throw `AuthenticationException` with code `ACCOUNT_SUSPENDED`.
5. If `users.totp_secret` is non-null, issue a provisional access token (scope limited to `POST /v1/auth/2fa/verify`) and return it with `requires_2fa: true`.
6. Otherwise, issue a full-access token via `JWTService::issueAccessToken()`.
7. Generate a refresh token via `JWTService::issueRefreshToken()` and persist it in the `refresh_tokens` table.
8. Fire `UserLoggedIn` domain event; the audit observer writes a `LOGIN` entry.
9. Update `users.last_login_at` to the current UTC timestamp.
10. Return `AuthTokenPair { accessToken, refreshToken, expiresIn: 900 }`.

### 1.3 Refresh Token Rotation

1. Compute `SHA-256(refreshToken)` and query `refresh_tokens` by `token_hash`.
2. If not found or `revoked_at IS NOT NULL` or `expires_at < NOW()`, throw `AuthenticationException`.
3. Mark the current token as revoked by setting `revoked_at = NOW()`.
4. Issue a new access token and a new refresh token; persist the new refresh token.
5. Return `AuthTokenPair`.

---

## 2. JWTService

```php
class JWTService
{
    /**
     * Issues a signed JWT access token with a 900-second TTL.
     */
    public function issueAccessToken(User $user, string $scope = 'full'): string;

    /**
     * Issues an opaque refresh token string and returns its metadata
     * for persistence in the refresh_tokens table.
     */
    public function issueRefreshToken(int $userId, int $franchiseId, string $deviceId): RefreshTokenData;

    /**
     * Validates and decodes a JWT. Returns the decoded payload.
     *
     * @throws AuthenticationException if signature invalid, expired, or malformed
     */
    public function decode(string $token): TokenPayload;
}
```

### 2.1 Access Token Payload

```json
{
  "sub": 42,
  "franchise_id": 7,
  "role": "cashier",
  "branch_id": 3,
  "scope": "full",
  "iat": 1743840000,
  "exp": 1743840900
}
```

- `sub` — `users.id` (integer, not UUID; consistent with database primary keys).
- `franchise_id` — tenant identifier; injected into every query context.
- `role` — the user's single active role for this session.
- `branch_id` — `NULL` for users with access to all branches (Business Owner).
- `scope` — `"full"` for complete API access; `"2fa_pending"` restricts access to the 2FA verification endpoint only.
- Signing algorithm: HS256, using a 256-bit secret stored in the server environment (`JWT_SECRET` environment variable). The secret is never committed to version control.

### 2.2 Refresh Token Storage

The refresh token itself is a cryptographically random 64-byte string (128 hex characters), generated via `random_bytes(64)`. Only the `SHA-256` hash of this value is stored in `refresh_tokens.token_hash`. The plaintext token is transmitted to the client once at issuance and never stored server-side in plaintext.

```
refresh_tokens row:
  user_id         = <users.id>
  franchise_id    = <businesses.id>
  token_hash      = SHA-256(<plaintext_token>)
  device_name     = <from login request>
  ip_address      = <client IP>
  expires_at      = NOW() + 30 days
  revoked_at      = NULL
  created_at      = NOW()
```

---

## 3. RBAC Middleware

### 3.1 Execution Pipeline

The `RBACMiddleware` executes as the first middleware on every protected route, before the controller is invoked:

1. Extract the `Authorization: Bearer <token>` header.
2. Call `JWTService::decode(token)` to validate signature and expiry.
3. Retrieve the required permission string for the current route from the permission registry (a PHP array keyed by `METHOD::/v1/path`).
4. Query the `role_permissions` table: `SELECT 1 FROM role_permissions rp JOIN permissions p ON rp.permission_id = p.id WHERE rp.role_id = :roleId AND p.name = :requiredPermission`.
5. If the permission is not held, return HTTP `403` with body `{ "error": "FORBIDDEN", "message": "Insufficient permissions." }` immediately.
6. Construct `AuthContext { userId, franchiseId, role, branchId }` from the decoded token payload.
7. Bind `AuthContext` to the request container; it is available to all service classes via dependency injection.

### 3.2 Role Hierarchy

```
Platform Admin
    └── Business Owner
            └── Branch Manager
                    ├── Cashier
                    ├── Stock Manager
                    ├── Accountant
                    └── HR Manager
```

Role hierarchy is informational only; permission enforcement is explicit via the `role_permissions` pivot table. A Branch Manager does not automatically inherit all Cashier permissions; permissions must be granted explicitly per role.

### 3.3 Permission Matrix

The table below maps the primary endpoint groups to the roles that hold write (`W`) or read (`R`) access. Endpoints not listed for a role return `403`.

| Endpoint Group | Business Owner | Branch Manager | Cashier | Stock Manager | Accountant | HR Manager |
|---|---|---|---|---|---|---|
| `POST /v1/pos/sessions` | W | W | W | - | - | - |
| `POST /v1/pos/sales` | W | W | W | - | - | - |
| `POST /v1/pos/sales/{id}/void` | W | W | - | - | - | - |
| `GET /v1/pos/sessions/{id}` | R | R | R | - | - | - |
| `POST /v1/inventory/products` | W | W | - | W | - | - |
| `GET /v1/inventory/products` | R | R | R | R | R | - |
| `POST /v1/inventory/stock-movements` | W | W | - | W | - | - |
| `POST /v1/inventory/stock-counts` | W | W | - | W | - | - |
| `POST /v1/inventory/adjustments/{id}/approve` | W | W | - | - | - | - |
| `GET /v1/customers` | R | R | R | - | R | - |
| `POST /v1/customers` | W | W | W | - | W | - |
| `GET /v1/suppliers` | R | R | - | R | R | - |
| `POST /v1/suppliers/purchase-orders` | W | W | - | W | - | - |
| `POST /v1/purchase-orders/{id}/approve` | W | W | - | - | - | - |
| `GET /v1/finance/accounts` | R | R | - | - | R | - |
| `POST /v1/finance/expenses` | W | W | - | - | W | - |
| `POST /v1/finance/expenses/{id}/approve` | W | W | - | - | - | - |
| `GET /v1/reports/*` | R | R | - | R (inventory only) | R | R (HR only) |
| `POST /v1/hr/payroll/run` | W | - | - | - | - | W |
| `POST /v1/hr/payroll/{id}/approve` | W | - | - | - | - | - |
| `GET /v1/hr/staff` | R | R | - | - | - | R |
| `POST /v1/hr/staff` | W | - | - | - | - | W |
| `GET /v1/dashboard` | R | R | - | - | R | - |
| `GET /v1/settings` | R | R (branch) | - | - | - | - |
| `PUT /v1/settings` | W | W (branch) | - | - | - | - |

**Platform Admin** holds a super-permission (`platform.admin.all`) that bypasses the role check for all endpoints. Every Platform Admin action targets a specific tenant via the impersonation token mechanism defined in the HLD and is recorded in `support_audit_log`.

### 3.4 Branch Scoping

When `AuthContext.branchId` is non-null, the middleware appends an additional branch scope check. A Cashier assigned to Branch A cannot read sales data for Branch B, even within the same tenant. The `BaseRepository::scopeToTenant()` method checks for a non-null `branchId` and adds `AND branch_id = :branchId` when present.

Business Owners and Accountants have `branchId = NULL` in their token, granting cross-branch read access within their tenant.
