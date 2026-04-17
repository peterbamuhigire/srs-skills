## Global Conventions

### Authentication

All endpoints (except `POST /auth/login` and `POST /auth/password/reset-request`) require a valid JWT Bearer token in the `Authorization` header:

```
Authorization: Bearer <access_token>
```

Access tokens have a 15-minute validity. Refresh tokens have a 30-day validity. The Android client must call `POST /auth/refresh` before expiry to obtain a new access token.

### JWT Payload Structure

Every issued access token carries the following claims:

| Claim | Type | Description |
|---|---|---|
| `sub` | `integer` | User ID (`tbl_users.user_id`) |
| `name` | `string` | Full name of the authenticated user |
| `role_id` | `integer` | Primary role ID (`tbl_roles.role_id`) |
| `role_code` | `string` | Role code (e.g., `SALES_AGENT`, `FINANCE_MANAGER`, `DIRECTOR`) |
| `agent_id` | `integer\|null` | Agent ID if the user is a registered agent; `null` otherwise |
| `permissions` | `string[]` | Array of permission codes granted to this user's role |
| `iat` | `integer` | Issued-at timestamp (Unix epoch) |
| `exp` | `integer` | Expiry timestamp (Unix epoch) |
| `jti` | `string` | JWT ID — unique identifier for this token (used for revocation) |

### Standard Response Envelope

All successful responses use the following envelope:

```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "timestamp": "2026-04-05T08:00:00Z",
    "request_id": "uuid-v4"
  }
}
```

For list endpoints, `data` is an array and a `pagination` key is added at the root level (see Pagination section).

### Standard Error Envelope

All error responses use the following envelope, regardless of HTTP status code:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable description of the error.",
    "field": "field_name_if_validation_error"
  },
  "meta": {
    "timestamp": "2026-04-05T08:00:00Z",
    "request_id": "uuid-v4"
  }
}
```

Standard error codes:

| HTTP Status | Error Code | Meaning |
|---|---|---|
| 400 | `VALIDATION_ERROR` | Request body failed validation |
| 401 | `UNAUTHENTICATED` | No valid JWT token provided |
| 401 | `TOKEN_EXPIRED` | JWT access token has expired |
| 403 | `FORBIDDEN` | Authenticated user lacks the required permission |
| 403 | `SEGREGATION_VIOLATION` | The requesting user is the creator of the record and cannot approve it (BR-003) |
| 404 | `NOT_FOUND` | The requested resource does not exist |
| 409 | `CONFLICT` | The operation conflicts with current resource state |
| 422 | `BUSINESS_RULE_VIOLATION` | A business rule (BR-001 to BR-018) blocks the operation |
| 429 | `RATE_LIMITED` | Too many requests |
| 500 | `SERVER_ERROR` | Unhandled server error — logged for investigation |

### Pagination Envelope

All list endpoints support cursor-based pagination via `page` and `per_page` query parameters. The response includes:

```json
{
  "success": true,
  "data": [ ... ],
  "pagination": {
    "current_page": 1,
    "per_page": 50,
    "total_records": 1071,
    "total_pages": 22,
    "has_next": true,
    "has_prev": false
  },
  "meta": {
    "timestamp": "2026-04-05T08:00:00Z",
    "request_id": "uuid-v4"
  }
}
```

Default `per_page` is 50. Maximum `per_page` is 200.

### Offline Sync Convention

Endpoints that support offline sync include a `sync_token` query parameter. The server returns only records created or modified after the timestamp encoded in the sync token. The Android client stores the returned `next_sync_token` and passes it on the next sync call.

### RBAC Role Codes

The following role codes are used throughout this specification:

| Role Code | Description |
|---|---|
| `DIRECTOR` | BIRDC/PIBID Director |
| `FINANCE_DIRECTOR` | Finance Director |
| `FINANCE_MANAGER` | Finance Manager |
| `SALES_MANAGER` | Sales Manager |
| `SALES_AGENT` | Field Sales Agent (1,071 agents) |
| `PROCUREMENT_OFFICER` | Procurement Officer |
| `WAREHOUSE_STAFF` | Warehouse / Store Keeper |
| `PRODUCTION_SUPERVISOR` | Production / Factory Supervisor |
| `QC_OFFICER` | Quality Control Officer |
| `HR_OFFICER` | Human Resources Officer |
| `PAYROLL_OFFICER` | Payroll Officer |
| `FIELD_OFFICER` | Farmer Delivery Field Collection Officer |
| `IT_ADMIN` | IT Administrator |
| `STAFF` | General Staff (leave, payslip self-service) |

---
