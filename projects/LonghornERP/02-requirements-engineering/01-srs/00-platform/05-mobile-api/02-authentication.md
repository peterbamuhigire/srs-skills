## 2. Authentication and Token Lifecycle

This section specifies the JWT-based authentication model for the Mobile API. All requirements conform to RFC 7519, RFC 6750, NIST SP 800-63B Authenticator Assurance Level 2, and OWASP API Security Top 10 (2023) item API2: Broken Authentication.

### 2.1 Token Issuance

**FR-MAPI-001:** The system shall issue a JWT access token and a refresh token when a mobile user authenticates with valid credentials via `POST /api/mobile/v1/auth/login`.

- Test oracle: A `POST` request with correct `username` and `password` returns HTTP 200 with a JSON body containing `access_token`, `refresh_token`, and `expires_in` fields. An incorrect password returns HTTP 401.

**FR-MAPI-002:** The JWT access token shall contain the following claims: `tid` (tenant identifier), `uid` (user identifier), `role` (user's active role code), `modules` (JSON array of enabled module codes for the tenant), `iat` (issued-at timestamp), and `exp` (expiry timestamp).

- Test oracle: Decode the issued JWT; assert all 6 claims are present with non-null, correctly typed values.

**FR-MAPI-003:** The system shall source the `tid` claim value from the database record of the authenticated user's account. The `tid` value shall never be read from the login request body or any client-supplied request parameter.

- Test oracle: Submit a login request with a fabricated `tenant_id` field in the request body; assert the issued JWT contains the database-sourced `tid`, not the submitted value.

**FR-MAPI-004:** The system shall rotate the refresh token on each access token refresh operation. The previously issued refresh token shall be invalidated within 1 second of a successful rotation.

- Test oracle: Perform 2 sequential refresh calls using the same refresh token; assert the second call returns HTTP 401 with error code `token_already_rotated`.

### 2.2 Token Expiry and Configuration

**FR-MAPI-005:** The system shall allow a super administrator to configure the JWT access token lifetime and refresh token lifetime per deployment via environment variables `JWT_ACCESS_TTL_SECONDS` and `JWT_REFRESH_TTL_SECONDS`. The default access token lifetime shall be 900 seconds (15 minutes); the default refresh token lifetime shall be 2592000 seconds (30 days).

- Test oracle: Set `JWT_ACCESS_TTL_SECONDS=60`; issue a token; wait 61 seconds; assert any authenticated request with that token returns HTTP 401.

**FR-MAPI-006:** The system shall return HTTP 401 with JSON body `{"error": "token_expired"}` for any request bearing an expired JWT access token.

- Test oracle: Issue a token; advance the system clock beyond `exp`; assert the next request returns HTTP 401 with the specified error body.

**FR-MAPI-007:** The system shall return HTTP 401 with JSON body `{"error": "token_invalid"}` for any request bearing a JWT with an invalid signature, malformed structure, or unrecognised algorithm.

- Test oracle: Submit a request with a tampered JWT (one character changed in the signature segment); assert HTTP 401 with `token_invalid`.

**FR-MAPI-008:** The system shall return HTTP 401 with JSON body `{"error": "token_revoked"}` for any request bearing a JWT that has been blacklisted via logout or account deactivation.

- Test oracle: Log out; assert the next request with the revoked access token returns HTTP 401 with `token_revoked`.

### 2.3 Account Deactivation Propagation

**FR-MAPI-009:** The system shall invalidate all active JWT access tokens for a user within 5 seconds of an administrator disabling that user's account, by adding all active token identifiers (`jti` claims) for that user to the token blacklist.

- Test oracle: Disable a user account; wait 5 seconds; assert any in-flight request with that user's token returns HTTP 401 with `token_revoked`.

*Note: This requirement aligns with NFR-SEC-003 (session invalidation within 5 seconds of account deactivation) applied to the JWT context.*

### 2.4 Logout and Token Blacklisting

**FR-MAPI-010:** The system shall blacklist the submitted access token and the associated refresh token when a mobile user calls `POST /api/mobile/v1/auth/logout`. The endpoint shall return HTTP 204 No Content on success.

- Test oracle: Call logout; assert HTTP 204; assert all subsequent requests with that access token return HTTP 401 with `token_revoked`.

**FR-MAPI-011:** The system shall store token blacklist entries in a server-side store with a time-to-live (TTL) equal to the token's remaining validity period, so that expired tokens are automatically evicted without manual cleanup.

- Test oracle: Blacklist a token with 30 seconds remaining; assert the entry is present at T+29 s and absent at T+31 s.

### 2.5 Token Refresh

**FR-MAPI-012:** The system shall issue a new JWT access token and a new refresh token when a mobile client submits a valid, non-expired, non-revoked refresh token to `POST /api/mobile/v1/auth/refresh`.

- Test oracle: Submit a valid refresh token; assert HTTP 200 with new `access_token`, new `refresh_token`, and updated `expires_in`.

**FR-MAPI-013:** The system shall return HTTP 401 for a token refresh request that presents an expired or revoked refresh token.

- Test oracle: Submit an expired refresh token; assert HTTP 401 with `{"error": "refresh_token_expired"}`.

### 2.6 Device Registration

**FR-MAPI-014:** The system shall register a mobile device's push notification token when a mobile client submits a `POST /api/mobile/v1/devices` request containing a valid JWT, a `device_token` string, and a `platform` field with value `android` or `ios`.

- Test oracle: Submit a valid device registration request; assert HTTP 201 Created; assert the device token is retrievable in the `mobile_devices` table scoped to the authenticated user and tenant.

**FR-MAPI-015:** The system shall update an existing device registration record rather than creating a duplicate when a mobile client registers a device token that already exists for the same user and tenant.

- Test oracle: Register the same device token twice for the same user; assert the `mobile_devices` table contains exactly 1 record for that token; assert HTTP 200 on the second call.
