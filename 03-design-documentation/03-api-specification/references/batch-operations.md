# Batch Operations Reference

**Source:** API Design Patterns (JJ Geewax, Manning 2021)
**Standards:** OpenAPI 3.0, RFC 7231 (HTTP Semantics), RFC 4918 (207 Multi-Status), IEEE 29148-2018

---

## Batch Create

Create multiple resources in a single request.

### Endpoint

```
POST /resources:batchCreate
```

### Request

```json
{
  "items": [
    { "name": "Widget A", "price": 19.99, "category": "hardware" },
    { "name": "Widget B", "price": 29.99, "category": "hardware" },
    { "name": "Widget C", "price": 9.99, "category": "software" }
  ]
}
```

### Response (HTTP 200 or 207)

```json
{
  "results": [
    { "status": "SUCCESS", "resource": { "id": "prod_001", "name": "Widget A", "price": 19.99 } },
    { "status": "SUCCESS", "resource": { "id": "prod_002", "name": "Widget B", "price": 29.99 } },
    { "status": "FAILURE", "error": { "code": "DUPLICATE_NAME", "message": "A product named 'Widget C' already exists" } }
  ],
  "summary": { "total": 3, "succeeded": 2, "failed": 1 }
}
```

Each item in the request maps to a corresponding item in the results array. The server preserves the order.

## Batch Update

Update multiple resources in a single request, with per-item field masks.

### Endpoint

```
POST /resources:batchUpdate
```

### Request

```json
{
  "items": [
    {
      "id": "prod_001",
      "update_mask": ["price"],
      "price": 24.99
    },
    {
      "id": "prod_002",
      "update_mask": ["price", "category"],
      "price": 34.99,
      "category": "premium"
    }
  ]
}
```

### Response

Each item returns the updated resource or an error. The `update_mask` limits which fields the server modifies, preventing accidental overwrites of fields not included in the mask.

## Batch Delete

Delete multiple resources in a single request.

### Endpoint

```
POST /resources:batchDelete
```

### Request

```json
{
  "ids": ["prod_001", "prod_002", "prod_003"]
}
```

### Response

```json
{
  "results": [
    { "id": "prod_001", "status": "SUCCESS" },
    { "id": "prod_002", "status": "SUCCESS" },
    { "id": "prod_003", "status": "SUCCESS" }
  ],
  "summary": { "total": 3, "succeeded": 3, "failed": 0 }
}
```

### Idempotent Deletion

Deleting an already-deleted resource returns `SUCCESS`, not an error. This makes batch delete safe to retry without side effects.

## Import / Export

For large datasets that exceed batch size limits, use import/export operations backed by Long-Running Operations.

### Import

```
POST /resources:import
Content-Type: multipart/form-data

file: customers.csv
format: csv
on_conflict: skip | update | fail
```

**Response:** Returns HTTP 202 Accepted with an LRO resource (see `references/long-running-operations.md`).

```json
{
  "operation_id": "op_import_456",
  "status": "PENDING",
  "progress_percent": 0,
  "created_at": "2025-03-15T10:00:00Z"
}
```

**Supported formats:** CSV, JSON Lines (JSONL), Excel (.xlsx). Document accepted formats and column mappings in the API specification.

**Conflict resolution strategies:**

| Strategy | Behavior |
|----------|----------|
| `skip` | Skip rows that conflict with existing records; report skipped count |
| `update` | Update existing records with imported data; report updated count |
| `fail` | Abort the entire import on first conflict; roll back all changes |

### Export

```
POST /resources:export
Content-Type: application/json

{
  "format": "csv",
  "filters": { "created_after": "2025-01-01" },
  "fields": ["id", "name", "email", "created_at"]
}
```

**Response:** Returns HTTP 202 Accepted with an LRO resource. When the operation succeeds, the `result` field contains a download URL:

```json
{
  "operation_id": "op_export_789",
  "status": "SUCCEEDED",
  "result": {
    "download_url": "/exports/exp_789/download",
    "file_size_bytes": 2048576,
    "row_count": 15420,
    "expires_at": "2025-03-16T10:00:00Z"
  }
}
```

## Partial Failure Handling

Batch operations can succeed for some items and fail for others. Use HTTP 207 Multi-Status to communicate mixed results.

### Response Structure

```json
{
  "results": [
    {
      "status": "SUCCESS",
      "resource": { "id": "res_001", "name": "Item A" }
    },
    {
      "status": "FAILURE",
      "error": {
        "code": "VALIDATION_ERROR",
        "message": "Field 'email' is required",
        "details": [{ "field": "email", "issue": "missing" }]
      }
    }
  ],
  "summary": {
    "total": 2,
    "succeeded": 1,
    "failed": 1
  }
}
```

### HTTP Status Codes for Batch Operations

| Code | Condition |
|------|-----------|
| 200 | All items succeeded |
| 207 | Some items succeeded, some failed (Multi-Status) |
| 400 | The batch request itself is malformed (invalid JSON, missing required fields) |
| 413 | Batch exceeds the maximum allowed size |
| 422 | All items failed validation |
| 429 | Rate limit exceeded |

## Rate Limiting for Batch Operations

Batch endpoints consume more server resources than single-resource endpoints. Apply stricter rate limits accordingly.

| Parameter | Single-Resource Endpoint | Batch Endpoint |
|-----------|------------------------|----------------|
| Requests per minute | 600 | 60 |
| Max items per request | 1 | 100-1000 (configurable) |
| Concurrent operations | Unlimited (within rate limit) | 5 per client |

### Maximum Batch Size

Set a maximum number of items per batch request to prevent resource exhaustion:

| Use Case | Recommended Max |
|----------|----------------|
| Simple creates/deletes | 1000 items |
| Complex updates with validation | 100 items |
| Import with file upload | 100,000 rows (use LRO) |
| Export | Unlimited rows (use LRO with streaming) |

Return HTTP 413 Payload Too Large if the client exceeds the maximum batch size.

## Atomic vs Non-Atomic Batches

### Atomic (All-or-Nothing)

All items in the batch succeed or all fail. The server wraps the batch in a database transaction.

**When to use:**
- Financial operations (transfer funds between multiple accounts)
- Inventory adjustments that must remain consistent
- Configuration changes that depend on each other

**Trade-offs:**
- Higher latency (transaction lock duration scales with batch size)
- Single failure rolls back all successful items
- Limited batch size (transaction timeout constraints)

### Non-Atomic (Partial Success)

Each item processes independently. Some items may succeed while others fail.

**When to use:**
- Bulk data imports where partial progress is acceptable
- Batch notifications or emails
- Independent record updates with no cross-item dependencies

**Trade-offs:**
- Client must handle partial failure (retry failed items)
- No guarantee of consistency across items
- Higher throughput (no transaction coordination)

### Signaling Atomicity

Let the client choose atomicity per request:

```json
{
  "atomic": true,
  "items": [...]
}
```

When `atomic: true`, the server returns 200 (all succeeded) or rolls back and returns 422 (all failed). When `atomic: false` (default), the server returns 200 or 207 with per-item results.

---

**Cross-references:**
- `references/advanced-api-patterns.md` -- Custom methods, field masks for batch updates
- `references/long-running-operations.md` -- LRO pattern for import/export operations
- `SKILL.md` Step 5 (Endpoint Details) -- Document batch endpoints alongside CRUD endpoints
- `SKILL.md` Step 7 (Rate Limiting) -- Apply batch-specific rate limits
