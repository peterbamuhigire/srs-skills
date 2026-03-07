# Long-Running Operations (LRO) Reference

**Source:** API Design Patterns (JJ Geewax, Manning 2021)
**Standards:** OpenAPI 3.0, RFC 7231 (HTTP Semantics), IEEE 29148-2018

---

## When to Use LRO

Implement the Long-Running Operation pattern when an API operation cannot return a final result within a normal HTTP request timeout. Apply LRO when any of these conditions hold:

| Condition | Example |
|-----------|---------|
| Processing time exceeds 10 seconds | PDF report generation, video transcoding |
| File processing with variable duration | CSV/Excel import, bulk image resizing |
| Batch imports affecting many records | Importing 10,000+ customer records |
| Report generation with complex aggregation | Monthly financial reports, analytics dashboards |
| Machine learning training or inference | Model training, batch prediction jobs |
| External system integration with unknown latency | Third-party payment settlement, shipping label generation |

## LRO Pattern

### Request Flow

1. **Client submits the request:**
   ```
   POST /reports:generate
   Content-Type: application/json

   { "report_type": "monthly_sales", "month": "2025-03" }
   ```

2. **Server returns 202 Accepted with an operation resource:**
   ```
   HTTP/1.1 202 Accepted
   Location: /operations/op_abc123
   Content-Type: application/json

   {
     "id": "op_abc123",
     "status": "PENDING",
     "progress_percent": 0,
     "created_at": "2025-03-15T10:00:00Z"
   }
   ```

3. **Client polls for status:**
   ```
   GET /operations/op_abc123
   ```

4. **Server returns current status until completion.**

## Operation Resource Schema

```json
{
  "id": "op_abc123",
  "status": "RUNNING",
  "progress_percent": 45,
  "result": null,
  "error": null,
  "created_at": "2025-03-15T10:00:00Z",
  "updated_at": "2025-03-15T10:02:30Z",
  "metadata": {
    "resource_type": "report",
    "action": "generate",
    "initiated_by": "user_456"
  }
}
```

### Operation States

| State | Description | Terminal |
|-------|-------------|----------|
| `PENDING` | Operation accepted but not yet started (queued) | No |
| `RUNNING` | Operation actively processing | No |
| `SUCCEEDED` | Operation completed successfully; `result` field contains the output | Yes |
| `FAILED` | Operation failed; `error` field contains failure details | Yes |
| `CANCELLED` | Operation was cancelled by the client or system | Yes |

### Completed Operation (Success)

```json
{
  "id": "op_abc123",
  "status": "SUCCEEDED",
  "progress_percent": 100,
  "result": {
    "resource_id": "report_789",
    "download_url": "/reports/report_789/download",
    "expires_at": "2025-03-16T10:00:00Z"
  },
  "error": null,
  "created_at": "2025-03-15T10:00:00Z",
  "updated_at": "2025-03-15T10:05:00Z",
  "metadata": {
    "resource_type": "report",
    "action": "generate",
    "initiated_by": "user_456"
  }
}
```

### Failed Operation

```json
{
  "id": "op_abc123",
  "status": "FAILED",
  "progress_percent": 67,
  "result": null,
  "error": {
    "code": "PROCESSING_ERROR",
    "message": "Failed to aggregate sales data for region EU-West",
    "details": [
      { "field": "region", "issue": "Data source timeout after 30s" }
    ]
  },
  "created_at": "2025-03-15T10:00:00Z",
  "updated_at": "2025-03-15T10:03:45Z",
  "metadata": {
    "resource_type": "report",
    "action": "generate",
    "initiated_by": "user_456"
  }
}
```

## Webhook Callbacks

For clients that prefer push-based notification over polling, support webhook callbacks.

### Registration

The client registers a callback URL when submitting the operation:

```json
POST /reports:generate
{
  "report_type": "monthly_sales",
  "month": "2025-03",
  "callback": {
    "url": "https://client.example.com/webhooks/operations",
    "events": ["SUCCEEDED", "FAILED"]
  }
}
```

### Delivery

When the operation reaches a terminal state, the server sends an HTTP POST to the callback URL with the full operation resource as the body.

### Delivery Guarantees

| Aspect | Specification |
|--------|--------------|
| **Retry policy** | Retry on 5xx and timeout; exponential backoff starting at 5s; max 5 retries over 1 hour |
| **Timeout** | 10-second connection timeout per delivery attempt |
| **Idempotency** | Include `X-Webhook-ID` header so the client can deduplicate repeated deliveries |
| **Ordering** | Deliver callbacks in the order operations complete; do not guarantee FIFO across operations |

### Signature Verification (HMAC-SHA256)

Sign every webhook payload so the client can verify authenticity:

1. Server computes: `signature = HMAC-SHA256(shared_secret, request_body)`
2. Server includes: `X-Webhook-Signature: sha256=<hex_digest>`
3. Client recomputes the HMAC using the shared secret and compares signatures.

Reject any callback where the signatures do not match.

## Polling Strategy

### Exponential Backoff

Clients that poll shall use exponential backoff to avoid overwhelming the server:

| Poll Attempt | Wait Before Poll |
|-------------|-----------------|
| 1 | 1 second |
| 2 | 2 seconds |
| 3 | 4 seconds |
| 4 | 8 seconds |
| 5 | 16 seconds |
| 6+ | 30 seconds (max) |

### Retry-After Header

The server shall include a `Retry-After` header in every non-terminal operation response:

```
HTTP/1.1 200 OK
Retry-After: 5

{ "id": "op_abc123", "status": "RUNNING", "progress_percent": 45 }
```

The client shall wait at least the specified number of seconds before the next poll.

## Cancellation

### Cancellation Endpoint

```
POST /operations/{id}:cancel
```

Or alternatively:

```
DELETE /operations/{id}
```

### Cancellation Behavior

- Cancellation is **idempotent**: cancelling an already-cancelled or already-completed operation returns 200 (not an error).
- Cancellation is **best-effort**: the server attempts to stop processing but does not guarantee immediate termination.
- The operation status transitions to `CANCELLED` once processing stops.
- Any partial results may be discarded or retained depending on the operation type (document this per endpoint).

## Expiration

### TTL and Garbage Collection

- Completed operations (SUCCEEDED, FAILED, CANCELLED) shall expire after a configurable TTL (default: 7 days).
- The server shall return 404 for expired operation IDs.
- Clients that need the result after expiration must re-submit the operation.
- Document the TTL in the API specification and include `expires_at` in the operation resource.

### Cleanup

Run a background garbage collection process to remove expired operations from the data store. Schedule cleanup during low-traffic periods to minimize database load.

---

**Cross-references:**
- `references/advanced-api-patterns.md` -- Custom methods that trigger LROs
- `references/batch-operations.md` -- Batch imports that return LROs
- `SKILL.md` Step 5 (Endpoint Details) -- Document LRO endpoints alongside standard endpoints
