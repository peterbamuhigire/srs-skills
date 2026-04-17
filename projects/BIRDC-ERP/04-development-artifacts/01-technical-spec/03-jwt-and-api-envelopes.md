# 3. JWT Authentication and API Response Envelopes

## 3.1 JWT Implementation

The BIRDC ERP mobile API uses JWT Bearer tokens for authentication. The web application uses session-based authentication (HttpOnly cookies). JWT is used exclusively for the 6 Android mobile app APIs.

### Algorithm and Key Management

- **Algorithm:** HS256 (HMAC-SHA256).
- **Secret key:** Minimum 256-bit random key. Stored in `.env` as `JWT_SECRET`. Never committed to version control.
- **Key rotation:** The `JWT_SECRET` is rotated annually or immediately if a security incident is suspected. Rotation invalidates all existing tokens — all mobile app users must re-authenticate.

### Token Lifetimes

| Token Type | Lifetime | Storage on Device |
|---|---|---|
| Access Token | 15 minutes | Memory only (not persisted to disk) |
| Refresh Token | 30 days | `EncryptedSharedPreferences` (Android Keystore-backed) |

The 15-minute access token lifetime limits the exposure window if a token is intercepted. The app uses the refresh token to obtain a new access token silently — the user does not need to log in again unless the refresh token has also expired.

### Access Token Payload Structure

```json
{
  "iss": "birdc-erp",
  "sub": "42",
  "iat": 1743839191,
  "exp": 1743840091,
  "userId": 42,
  "role": "sales_agent",
  "agentId": 107,
  "franchiseId": null,
  "permissions": ["pos:write", "remittance:submit", "stock:read"]
}
```

**Field definitions:**

| Field | Type | Description |
|---|---|---|
| `iss` | string | Issuer — always `"birdc-erp"` |
| `sub` | string | Subject — user ID as string (JWT standard) |
| `iat` | integer | Issued at — Unix timestamp |
| `exp` | integer | Expiry — Unix timestamp |
| `userId` | integer | `tbl_users.id` — used for all permission lookups |
| `role` | string | Primary role slug — matches `tbl_roles.slug` |
| `agentId` | integer or null | `tbl_agents.id` — populated for Sales Agent role, null otherwise |
| `franchiseId` | null | Always null — BIRDC ERP is single-tenant. Included in the payload structure for DC-007 replicability. |
| `permissions` | string array | Resolved permission slugs — cached from the RBAC matrix at token issue time |

### Refresh Token Flow

1. Mobile app sends POST `/api/auth/refresh` with the refresh token in the request body.
2. Server validates the refresh token against the `tbl_refresh_tokens` table (stored as a hash — never the raw token).
3. If valid and not expired: issues a new access token (15 min) and a new refresh token (30 days). The old refresh token is invalidated.
4. If the refresh token is expired or revoked: returns `401 Unauthorized` with error code `ERR_TOKEN_EXPIRED`. The app redirects the user to the login screen.

### Token Revocation

The `tbl_refresh_tokens` table supports explicit revocation:

- IT Administrator can revoke all tokens for a specific user (e.g., when an agent's device is lost).
- All tokens for a user are automatically revoked when the account is deactivated.
- Revocation takes effect immediately on the next refresh attempt. The current access token remains valid until its 15-minute expiry.

---

## 3.2 API Error Envelope

Every API response — success or failure — uses a consistent JSON envelope. No API endpoint may return a bare value, bare array, or non-standard error format.

### Error Response Format

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ERR_FLOAT_LIMIT_EXCEEDED",
    "message": "Stock transfer blocked — agent Samuel Okello's float limit of UGX 2,500,000 would be exceeded.",
    "details": [
      "Current agent stock value: UGX 2,200,000",
      "Transfer value: UGX 450,000",
      "Float limit: UGX 2,500,000",
      "Excess: UGX 150,000"
    ]
  },
  "meta": {
    "timestamp": "2026-04-05T09:15:33+03:00",
    "request_id": "req_01jt4k8mabcde12345"
  }
}
```

### Success Response Format

```json
{
  "success": true,
  "data": {
    "invoice_id": 1234,
    "invoice_number": "INV-2026-0123",
    "status": "issued",
    "efris_status": "queued"
  },
  "error": null,
  "meta": {
    "timestamp": "2026-04-05T09:15:33+03:00",
    "request_id": "req_01jt4k8mabcde12345"
  }
}
```

**Envelope fields:**

| Field | Type | Description |
|---|---|---|
| `success` | boolean | `true` for 2xx responses; `false` for all error responses |
| `data` | object or null | The response payload for successful requests; `null` on error |
| `error` | object or null | Error detail for failed requests; `null` on success |
| `error.code` | string | Machine-readable error code — `ERR_` prefix + UPPER_SNAKE_CASE descriptor |
| `error.message` | string | Human-readable description following the DC-001 error message standard (what happened, why, what to do) |
| `error.details` | string array | Optional additional context — list of specific violations, affected fields, or remediation steps |
| `meta.timestamp` | string | ISO 8601 with timezone offset |
| `meta.request_id` | string | Unique per-request ID for log correlation |

### Standard Error Codes

| Code | HTTP Status | Trigger |
|---|---|---|
| `ERR_VALIDATION` | 422 | Request body fails validation rules |
| `ERR_AUTH_REQUIRED` | 401 | No valid token provided |
| `ERR_TOKEN_EXPIRED` | 401 | Access or refresh token has expired |
| `ERR_FORBIDDEN` | 403 | Authenticated user lacks permission for the action |
| `ERR_NOT_FOUND` | 404 | Requested resource does not exist |
| `ERR_DUPLICATE` | 409 | Record already exists (duplicate invoice number, duplicate NIN, etc.) |
| `ERR_FLOAT_LIMIT_EXCEEDED` | 422 | BR-006: agent float limit would be exceeded |
| `ERR_QC_GATE_BLOCKED` | 422 | BR-004: production batch not QC-approved |
| `ERR_MASS_BALANCE_FAIL` | 422 | BR-008: production mass balance outside ±2% tolerance |
| `ERR_SEGREGATION_VIOLATION` | 403 | BR-003: user attempts to approve own transaction |
| `ERR_PAYROLL_LOCKED` | 422 | BR-010: modification attempted on a locked payroll run |
| `ERR_EFRIS_QUEUE_FULL` | 503 | EFRIS retry queue depth exceeds threshold |
| `ERR_INTERNAL` | 500 | Unhandled server exception |

---

## 3.3 Pagination Envelope

All list endpoints that return more than 1 record use cursor-based or offset-based pagination. The pagination metadata is included in the `meta` field of the standard envelope:

```json
{
  "success": true,
  "data": [
    { "id": 1, "invoice_number": "INV-2026-0001", "..." : "..." },
    { "id": 2, "invoice_number": "INV-2026-0002", "..." : "..." }
  ],
  "error": null,
  "meta": {
    "timestamp": "2026-04-05T09:15:33+03:00",
    "request_id": "req_01jt4k8mabcde12345",
    "pagination": {
      "current_page": 1,
      "per_page": 25,
      "total": 1047,
      "last_page": 42
    }
  }
}
```

**Pagination parameters (query string):**

| Parameter | Default | Description |
|---|---|---|
| `page` | `1` | Requested page number |
| `per_page` | `25` | Records per page. Maximum: `100` |
| `sort` | varies by endpoint | Column name to sort by |
| `direction` | `desc` | Sort direction: `asc` or `desc` |

For the farmer list (6,440+ names) and agent list (1,071 agents), the default `per_page` is `50`. DataTables on the web front end drives pagination parameters from the server-side DataTables configuration.
