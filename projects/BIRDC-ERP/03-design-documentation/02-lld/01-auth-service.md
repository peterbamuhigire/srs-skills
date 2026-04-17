# 1. AuthService

**Namespace:** `App\Services\Auth\AuthService`
**Dependencies:** `UserRepository`, `SessionManager`, `JWTService`, `TotpService`, `AuditLogService`
**Test coverage required:** 100% (security-critical)

## 1.1 Method Signatures

```php
final class AuthService
{
    /**
     * Authenticate a user by email and password.
     *
     * @param string $email     Plaintext email address
     * @param string $password  Plaintext password (bcrypt/Argon2id verified against stored hash)
     *
     * @return AuthResult  On success: user DTO, access token, refresh token, expiry.
     *
     * @throws AuthenticationException  If credentials are invalid.
     * @throws AccountLockedException   If the account is locked after 5 failed attempts.
     * @throws TotpRequiredException    If TOTP 2FA is enabled for this user's role —
     *                                  caller must follow up with validateTOTP().
     *
     * Business rules:
     *   - Password compared using password_verify() against Argon2id/bcrypt hash.
     *   - Increments tbl_users.failed_login_count on failure.
     *   - Locks account after 5 consecutive failures (configurable).
     *   - Logs login attempt (success or failure) to AuditLogService.
     *   - For web: creates PHP session and sets HttpOnly SameSite=Lax cookie.
     *   - For API: returns JWT TokenPair only (no session).
     */
    public function login(string $email, string $password): AuthResult;

    /**
     * Issue a new access token using a valid refresh token.
     *
     * @param string $refreshToken  The refresh token stored in EncryptedSharedPreferences (mobile)
     *                              or in tbl_refresh_tokens (web sessions).
     *
     * @return TokenPair  New access token and rotated refresh token.
     *
     * @throws InvalidTokenException   If refresh token signature is invalid or not found.
     * @throws TokenExpiredException   If refresh token TTL (30 days) has elapsed.
     * @throws AccountLockedException  If user account was deactivated since token was issued.
     *
     * Business rules:
     *   - Refresh token rotation: old token is invalidated on use.
     *   - New access token TTL: 15 minutes.
     *   - New refresh token TTL: 30 days from issue.
     *   - Logs token refresh to AuditLogService.
     */
    public function refreshToken(string $refreshToken): TokenPair;

    /**
     * Invalidate a user's current session and/or JWT tokens.
     *
     * @param int $userId  The user whose session is to be terminated.
     *
     * @return void
     *
     * Business rules:
     *   - Destroys PHP session if web context.
     *   - Inserts refresh token into tbl_token_blacklist (JWT stateless invalidation).
     *   - Logs logout to AuditLogService.
     */
    public function logout(int $userId): void;

    /**
     * Validate a TOTP code for two-factor authentication.
     *
     * Required for roles: Director, Finance Director, IT Administrator.
     *
     * @param int    $userId  The authenticated user (password already verified).
     * @param string $code    6-digit TOTP code from Google Authenticator.
     *
     * @return bool  true if the code is valid and within the 30-second window (±1 window tolerance).
     *
     * @throws TotpException  If TOTP is not configured for this user.
     *
     * Business rules:
     *   - Validates using RFC 6238 TOTP with ±1 time-step tolerance (90-second window).
     *   - Replay protection: each code can only be used once within its window
     *     (stored in tbl_totp_used_codes with TTL).
     *   - Failed TOTP attempt is logged to AuditLogService.
     */
    public function validateTOTP(int $userId, string $code): bool;
}
```

## 1.2 JWT Payload Structure

All JWT tokens issued by `JWTService` carry the following payload:

```json
{
  "sub": 42,
  "email": "agent@birdc.ug",
  "role": "SALES_AGENT",
  "panel": "AGENT_PORTAL",
  "iat": 1743840000,
  "exp": 1743840900,
  "jti": "550e8400-e29b-41d4-a716-446655440000"
}
```

| Claim | Type | Description |
|---|---|---|
| `sub` | int | `tbl_users.id` — subject (user ID) |
| `email` | string | User email at time of token issuance |
| `role` | string | Primary role code (e.g., `SALES_AGENT`, `FINANCE_MANAGER`) |
| `panel` | string | `MAIN_ERP`, `AGENT_PORTAL`, or `ADMIN_PANEL` |
| `iat` | int | Issued At — Unix timestamp UTC |
| `exp` | int | Expiry — `iat + 900` (15 minutes) |
| `jti` | string | JWT ID — UUID v4 for replay prevention |

Algorithm: `HS256`. Signing secret stored in `.env` as `JWT_SECRET` (minimum 256-bit random string). Never committed to version control.
