# 16. API Contracts — Error Envelope, Pagination, and Cross-Cutting Formats

## 16.1 Standard API Error Envelope

All API responses (success and failure) use a consistent JSON envelope. No response returns raw data or raw error strings outside this structure.

### 16.1.1 Success Response

```json
{
  "success": true,
  "data": { },
  "meta": {
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-04-05T14:30:00Z"
  }
}
```

### 16.1.2 Error Response

```json
{
  "success": false,
  "error": {
    "code": "INSUFFICIENT_STOCK",
    "message": "Insufficient stock for product ID 42 at location Warehouse A. Available: 10 kg; requested: 25 kg.",
    "details": [
      {
        "field": "items[0].quantity",
        "issue": "Requested quantity 25 kg exceeds available stock 10 kg for batch B2026-001."
      }
    ]
  },
  "meta": {
    "request_id": "550e8400-e29b-41d4-a716-446655440001",
    "timestamp": "2026-04-05T14:30:01Z"
  }
}
```

### 16.1.3 Error Code Registry

| HTTP Status | Error Code | Trigger |
|---|---|---|
| 400 | `VALIDATION_ERROR` | Input validation failure (missing field, wrong type) |
| 400 | `UNBALANCED_JOURNAL` | GL journal debit ≠ credit |
| 400 | `MASS_BALANCE_VIOLATION` | Production order outputs do not balance to inputs (BR-008) |
| 401 | `UNAUTHENTICATED` | Missing or invalid Bearer token / session |
| 401 | `TOKEN_EXPIRED` | Access token TTL elapsed |
| 401 | `TOTP_REQUIRED` | TOTP 2FA required before access is granted |
| 403 | `PERMISSION_DENIED` | 8-layer RBAC check failed |
| 403 | `SEGREGATION_OF_DUTIES` | Creator = approver violation (BR-003) |
| 403 | `PAYROLL_LOCKED` | Attempt to modify a locked payroll run (BR-010) |
| 404 | `NOT_FOUND` | Requested resource does not exist |
| 409 | `DUPLICATE_REQUEST` | Idempotency key already processed |
| 409 | `ACTIVE_SESSION_EXISTS` | Cashier already has an open POS session |
| 409 | `CHAIN_BROKEN` | GL account hash chain is broken; posting blocked (BR-013) |
| 422 | `CREDIT_LIMIT_EXCEEDED` | Customer credit limit breach |
| 422 | `FLOAT_LIMIT_EXCEEDED` | Agent stock float limit breach (BR-006) |
| 422 | `INSUFFICIENT_STOCK` | Stock quantity < requested quantity |
| 422 | `QC_GATE_BLOCKED` | Batch not QC-approved; transfer blocked (BR-004) |
| 422 | `FIFO_VIOLATION` | Manual batch selection violates FEFO order (BR-007) |
| 422 | `FARMER_CONTRIBUTION_INCOMPLETE` | Batch cannot advance; not all weight attributed (BR-011) |
| 500 | `INTERNAL_ERROR` | Unhandled exception (production: no stack trace exposed) |
| 503 | `EFRIS_UNAVAILABLE` | URA EFRIS API unreachable; sale queued for retry |

## 16.2 Pagination Format

All list endpoints use cursor-based or offset-based pagination. The default is offset-based.

### 16.2.1 Request Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `page` | int | 1 | 1-indexed page number |
| `per_page` | int | 50 | Records per page; max 200 |
| `sort_by` | string | `created_at` | Column to sort by |
| `sort_dir` | string | `desc` | `asc` or `desc` |

### 16.2.2 Paginated Response Envelope

```json
{
  "success": true,
  "data": [ ],
  "pagination": {
    "current_page": 1,
    "per_page": 50,
    "total_records": 6440,
    "total_pages": 129,
    "has_next_page": true,
    "has_prev_page": false
  },
  "meta": {
    "request_id": "550e8400-e29b-41d4-a716-446655440002",
    "timestamp": "2026-04-05T14:30:02Z"
  }
}
```

## 16.3 Idempotency

All state-changing POST endpoints (invoice creation, sale, remittance, payment) accept an `X-Idempotency-Key` header containing a UUID v4. The server stores processed idempotency keys in `tbl_idempotency_keys` with a 24-hour TTL. A duplicate request within 24 hours returns the original response with HTTP 200 (not 409 — the 409 `DUPLICATE_REQUEST` is returned only when the original request is still in-flight).

## 16.4 Date and Currency Formats in API

| Type | Format | Example |
|---|---|---|
| Date | ISO 8601: `YYYY-MM-DD` | `"2026-04-05"` |
| Datetime | ISO 8601 UTC: `YYYY-MM-DDTHH:MM:SSZ` | `"2026-04-05T14:30:00Z"` |
| Money | Integer UGX (no decimal) | `5000000` |
| Percentage | Float | `14.5` |
| Weight | Float kg | `1250.75` |

All money values in API requests and responses are integer UGX. Fractional shillings are not used. The application layer rounds at the point of computation using `intdiv()` with banker's rounding where required.
