# POS and Mobile Module Endpoints

All endpoints in this section require `Authorization: Bearer <token>`. POS endpoints require the `pos` module claim; mobile sync endpoints are available to any authenticated user on the mobile API. The `tenant_id` is resolved exclusively from the token.

---

## Point of Sale Endpoints

### POST /api/v1/pos/sessions

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/pos/sessions` |
| **Auth Required** | Yes — `pos.open_session` permission |
| **Description** | Opens a new POS session for the authenticated cashier at the specified till. Only one active session per till is permitted at any time. The cashier declares the opening float amount at session open. |

**Request Body:**

```json
{
  "till_id": "till-uuid-003",
  "opening_float": 200000.00,
  "notes": "Morning shift — Kampala Head Office."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `till_id` | string (UUID) | Yes | Till (POS terminal) identifier. Must belong to the tenant's branch. |
| `opening_float` | number | Yes | Cash float declared at session open. Must be ≥ 0. |
| `notes` | string | No | Optional session notes. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "pos-sess-uuid-0041",
    "reference": "POS-2026-0041",
    "till_id": "till-uuid-003",
    "cashier_id": "emp-uuid-0055",
    "opening_float": 200000.00,
    "status": "open",
    "opened_at": "2026-04-05T08:00:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing required fields. |
| 404 | `NOT_FOUND` | `till_id` does not exist within the tenant. |
| 409 | `CONFLICT` | An active session already exists on this till. |

---

### POST /api/v1/pos/sessions/{id}/transactions

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/pos/sessions/{id}/transactions` |
| **Auth Required** | Yes — `pos.sell` permission |
| **Description** | Records a POS sale transaction within an open session. The transaction decrements inventory quantities, posts revenue and tax entries to the GL, and records the payment split. Split tender (multiple payment methods) is supported. The sum of `payments[].amount` must equal the transaction total. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | POS session identifier. Session must be `open`. |

**Request Body:**

```json
{
  "transaction_date": "2026-04-05",
  "customer_id": null,
  "lines": [
    {
      "item_id": "item-uuid-012",
      "qty": 2,
      "unit_price": 450000.00,
      "discount_amount": 0.00,
      "tax_code": "VAT18"
    },
    {
      "item_id": "item-uuid-034",
      "qty": 1,
      "unit_price": 85000.00,
      "discount_amount": 5000.00,
      "tax_code": "VAT18"
    }
  ],
  "payments": [
    {
      "method": "mobile_money",
      "amount": 985000.00,
      "reference": "MTN-TXN-20260405-001"
    }
  ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `lines` | array | Yes | Sale lines. Minimum 1 line. Each `qty` must be > 0. |
| `lines[].item_id` | string (UUID) | Yes | Item sold. |
| `lines[].qty` | number | Yes | Quantity sold. |
| `lines[].unit_price` | number | Yes | Selling price per unit at time of sale. |
| `lines[].discount_amount` | number | No | Line-level discount amount. Default: 0. |
| `lines[].tax_code` | string | Yes | Applicable tax code. |
| `payments` | array | Yes | Payment method(s). Sum of all `amount` values must equal the transaction total. |
| `payments[].method` | string | Yes | `cash`, `mobile_money`, `card`, `credit`. |
| `payments[].amount` | number | Yes | Amount paid via this method. |
| `customer_id` | string (UUID) | No | Optional customer for invoice attachment or loyalty tracking. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "pos-txn-uuid-0301",
    "receipt_number": "RCP-2026-0301",
    "session_id": "pos-sess-uuid-0041",
    "subtotal": 980000.00,
    "tax_total": 176400.00,
    "discount_total": 5000.00,
    "total_amount": 985000.00,
    "change_due": 0.00,
    "gl_entry_id": "jnl-uuid-pos-0301",
    "created_at": "2026-04-05T09:45:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 404 | `NOT_FOUND` | Session or item not found. |
| 409 | `CONFLICT` | POS session is not in `open` status. |
| 422 | `UNPROCESSABLE_ENTITY` | Payment amounts do not sum to the transaction total; insufficient stock for an item. |

---

### POST /api/v1/pos/sessions/{id}/close

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/pos/sessions/{id}/close` |
| **Auth Required** | Yes — `pos.close_session` permission |
| **Description** | Closes an open POS session. The cashier declares the closing cash count. The system calculates the expected cash balance from the opening float plus cash sales and reports the variance. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | POS session identifier. |

**Request Body:**

```json
{
  "closing_cash_count": 985000.00,
  "notes": "End of morning shift."
}
```

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "id": "pos-sess-uuid-0041",
    "status": "closed",
    "opening_float": 200000.00,
    "expected_cash": 1050000.00,
    "declared_cash": 985000.00,
    "cash_variance": -65000.00,
    "total_sales": 8450000.00,
    "transaction_count": 14,
    "closed_at": "2026-04-05T14:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT` (session already closed).

---

### GET /api/v1/pos/sessions/{id}/summary

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/pos/sessions/{id}/summary` |
| **Auth Required** | Yes — `pos.read` permission |
| **Description** | Returns a summary report for a POS session, including a breakdown of sales by payment method, tax collected, and top-selling items. Available for both open and closed sessions. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | POS session identifier. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "session_id": "pos-sess-uuid-0041",
    "reference": "POS-2026-0041",
    "cashier_name": "Cashier One",
    "status": "closed",
    "opened_at": "2026-04-05T08:00:00Z",
    "closed_at": "2026-04-05T14:00:00Z",
    "transaction_count": 14,
    "total_sales": 8450000.00,
    "total_tax": 1520700.00,
    "total_discounts": 120000.00,
    "payment_breakdown": [
      { "method": "cash", "amount": 3200000.00 },
      { "method": "mobile_money", "amount": 4250000.00 },
      { "method": "card", "amount": 1000000.00 }
    ],
    "cash_variance": -65000.00
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`, 404 `NOT_FOUND`.

---

## Mobile-Specific Endpoints

### GET /api/v1/mobile/sync

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/mobile/sync` |
| **Auth Required** | Yes (`Authorization: Bearer <token>`) |
| **Description** | Delta synchronisation endpoint. Returns all records in the specified module that have been created or modified since the `last_sync_timestamp`. The mobile client stores the returned `sync_timestamp` and uses it on the next call. Only records within the authenticated tenant and permitted modules are returned. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `module` | string | Yes | Module to sync: `inventory`, `pos`, `hr`, `sales`. |
| `last_sync_timestamp` | integer (Unix epoch ms) | Yes | Timestamp of the last successful sync. Pass `0` for initial full sync. |
| `page` | integer | No | Page number for large delta sets (default: 1). |
| `per_page` | integer | No | Records per page (default: 100, max: 500). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "module": "inventory",
    "sync_timestamp": 1775000000000,
    "has_more": false,
    "records": [
      {
        "id": "item-uuid-012",
        "entity_type": "inventory_item",
        "operation": "update",
        "data": {
          "sku": "CHAIR-ERG-001",
          "name": "Office Chair — Ergonomic",
          "qty_on_hand": 22,
          "cost_price": 350000.00,
          "selling_price": 450000.00,
          "updated_at": "2026-04-05T08:30:00Z"
        }
      }
    ]
  },
  "error": null
}
```

The `operation` field values are `create`, `update`, or `delete`. For `delete` operations, only the `id` and `entity_type` are returned.

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing `module` or `last_sync_timestamp`. |
| 403 | `FORBIDDEN` | The JWT does not include the requested module. |

---

### POST /api/v1/mobile/sync/push

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/mobile/sync/push` |
| **Auth Required** | Yes (`Authorization: Bearer <token>`) |
| **Description** | Pushes offline-created or offline-modified records from the mobile client to the server. The server processes each record and returns per-record results. Conflicts (where the server version is newer than the client version) are reported per record; the client must resolve conflicts locally. |

**Request Body:**

```json
{
  "module": "pos",
  "device_id": "device-uuid-android-0077",
  "records": [
    {
      "client_id": "local-txn-001",
      "entity_type": "pos_transaction",
      "operation": "create",
      "data": {
        "session_id": "pos-sess-uuid-0041",
        "lines": [],
        "payments": [],
        "created_offline_at": "2026-04-05T11:30:00Z"
      }
    }
  ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `module` | string | Yes | Module the records belong to. |
| `device_id` | string | Yes | Unique device identifier for conflict tracking and audit. |
| `records` | array | Yes | Offline records to push. Maximum 100 records per request. |
| `records[].client_id` | string | Yes | Client-generated temporary ID used to correlate results. |
| `records[].entity_type` | string | Yes | Entity type of the record. |
| `records[].operation` | string | Yes | `create` or `update`. |
| `records[].data` | object | Yes | Record data conforming to the entity's API schema. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "processed": 1,
    "results": [
      {
        "client_id": "local-txn-001",
        "status": "accepted",
        "server_id": "pos-txn-uuid-0315",
        "error": null
      }
    ]
  },
  "error": null
}
```

When a conflict is detected:

```json
{
  "client_id": "local-item-002",
  "status": "conflict",
  "server_id": "item-uuid-012",
  "error": {
    "code": "SYNC_CONFLICT",
    "message": "Server version updated at 2026-04-05T12:00:00Z is newer than client version updated at 2026-04-05T11:30:00Z.",
    "server_data": {}
  }
}
```

**Error Codes:** 400 `BAD_REQUEST` (malformed records array), 413 `PAYLOAD_TOO_LARGE` (more than 100 records in a single push).

---

### POST /api/v1/mobile/push-tokens

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/mobile/push-tokens` |
| **Auth Required** | Yes (`Authorization: Bearer <token>`) |
| **Description** | Registers or updates the device push notification token for the authenticated user. The token is used to deliver in-app notifications (leave approvals, payroll ready, stock alerts). If a token for the same `device_id` already exists, it is updated. |

**Request Body:**

```json
{
  "device_id": "device-uuid-android-0077",
  "platform": "android",
  "push_token": "fcm-device-token-string-here",
  "app_version": "1.4.2"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `device_id` | string | Yes | Unique device identifier. |
| `platform` | string | Yes | `android` or `ios`. |
| `push_token` | string | Yes | FCM (Android) or APNs (iOS) device token. |
| `app_version` | string | No | Mobile app version for diagnostic logging. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "device_id": "device-uuid-android-0077",
    "registered_at": "2026-04-05T08:05:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST` (missing required fields), 401 `UNAUTHORIZED`.
