# Inventory Module Endpoints

All endpoints in this section require `Authorization: Bearer <token>` and the `inventory` module claim in the JWT. The `tenant_id` is resolved exclusively from the token.

---

## GET /api/v1/inventory/items

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/inventory/items` |
| **Auth Required** | Yes — `inventory.read` permission |
| **Description** | Returns a paginated list of inventory items for the authenticated tenant. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `category_id` | string (UUID) | No | Filter items by category. |
| `search` | string | No | Partial match on item name, SKU, or barcode. |
| `low_stock_only` | boolean | No | If `true`, returns only items where the current quantity is at or below the reorder level. |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "item-uuid-012",
        "sku": "CHAIR-ERG-001",
        "barcode": "0000012345678",
        "name": "Office Chair — Ergonomic",
        "category_id": "cat-uuid-003",
        "category_name": "Furniture",
        "unit_of_measure": "piece",
        "cost_price": 350000.00,
        "selling_price": 450000.00,
        "currency": "UGX",
        "reorder_level": 5,
        "total_qty_on_hand": 22,
        "is_active": true
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 310, "total_pages": 13 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`.

---

## GET /api/v1/inventory/items/{id}/stock-balance

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/inventory/items/{id}/stock-balance` |
| **Auth Required** | Yes — `inventory.read` permission |
| **Description** | Returns the current on-hand quantity and stock valuation for the specified item, broken down by branch. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Item identifier. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "item_id": "item-uuid-012",
    "item_name": "Office Chair — Ergonomic",
    "valuation_method": "weighted_average",
    "balances": [
      {
        "branch_id": "branch-uuid-001",
        "branch_name": "Kampala Head Office",
        "qty_on_hand": 15,
        "qty_on_order": 20,
        "qty_reserved": 3,
        "qty_available": 12,
        "average_cost": 352000.00,
        "total_value": 5280000.00
      },
      {
        "branch_id": "branch-uuid-002",
        "branch_name": "Jinja Branch",
        "qty_on_hand": 7,
        "qty_on_order": 0,
        "qty_reserved": 0,
        "qty_available": 7,
        "average_cost": 352000.00,
        "total_value": 2464000.00
      }
    ],
    "totals": {
      "total_qty_on_hand": 22,
      "total_value": 7744000.00
    }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`, 404 `NOT_FOUND` (item does not exist within the tenant).

---

## POST /api/v1/inventory/grn

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/inventory/grn` |
| **Auth Required** | Yes — `inventory.receive` permission |
| **Description** | Creates a Goods Received Note (GRN), updating on-hand quantities and posting the stock receipt to the GL. If `po_id` is supplied, the GRN is matched against the corresponding Local Purchase Order. |

**Request Body:**

```json
{
  "supplier_id": "supp-uuid-005",
  "po_id": "lpo-uuid-0088",
  "received_date": "2026-04-05",
  "branch_id": "branch-uuid-001",
  "reference": "GRN-2026-0055",
  "lines": [
    {
      "item_id": "item-uuid-012",
      "qty": 20,
      "unit_cost": 350000.00,
      "batch_number": "BATCH-2026-04",
      "expiry_date": null
    }
  ],
  "notes": "Received in good condition."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `supplier_id` | string (UUID) | Yes | Supplier delivering the goods. |
| `po_id` | string (UUID) | No | Linked Local Purchase Order. If supplied, received quantities are validated against ordered quantities. |
| `received_date` | string (ISO 8601) | Yes | Date goods were physically received. |
| `branch_id` | string (UUID) | Yes | Receiving branch. |
| `reference` | string | Yes | GRN reference number. |
| `lines` | array | Yes | Minimum 1 line. |
| `lines[].item_id` | string (UUID) | Yes | Item being received. |
| `lines[].qty` | number | Yes | Quantity received. Must be > 0. |
| `lines[].unit_cost` | number | Yes | Unit cost at time of receipt. Must be > 0. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "grn-uuid-0055",
    "reference": "GRN-2026-0055",
    "status": "posted",
    "gl_entry_id": "jnl-uuid-auto-grn-0055",
    "total_cost": 7000000.00,
    "created_at": "2026-04-05T14:00:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing required fields. |
| 404 | `NOT_FOUND` | Invalid `supplier_id`, `po_id`, or `item_id`. |
| 409 | `CONFLICT` | `reference` already exists for this tenant. |
| 422 | `UNPROCESSABLE_ENTITY` | Received quantity exceeds PO quantity; or receiving date falls in a closed period. |

---

## POST /api/v1/inventory/adjustments

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/inventory/adjustments` |
| **Auth Required** | Yes — `inventory.adjust` permission |
| **Description** | Records a manual stock adjustment for a single item at a specified branch. Positive `qty_change` increases stock; negative decreases it. The adjustment is posted to the GL using the stock adjustment account configured for the tenant. |

**Request Body:**

```json
{
  "item_id": "item-uuid-012",
  "branch_id": "branch-uuid-001",
  "adjustment_date": "2026-04-05",
  "qty_change": -3,
  "reason_code": "DAMAGED",
  "notes": "3 units found damaged during stock count."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `item_id` | string (UUID) | Yes | Item to adjust. |
| `branch_id` | string (UUID) | Yes | Branch where adjustment occurs. |
| `adjustment_date` | string (ISO 8601) | Yes | Effective date of the adjustment. |
| `qty_change` | number | Yes | Signed quantity change. Non-zero. |
| `reason_code` | string | Yes | Predefined reason code: `DAMAGED`, `EXPIRED`, `THEFT`, `FOUND`, `CORRECTION`. |
| `notes` | string | No | Free-text explanation. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "adj-uuid-0021",
    "item_id": "item-uuid-012",
    "branch_id": "branch-uuid-001",
    "qty_change": -3,
    "new_qty_on_hand": 12,
    "gl_entry_id": "jnl-uuid-auto-adj-0021",
    "created_at": "2026-04-05T14:30:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 422 `UNPROCESSABLE_ENTITY` (resulting stock would go below zero where negative stock is not permitted; or adjustment date falls in a closed period).

---

## POST /api/v1/inventory/transfers

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/inventory/transfers` |
| **Auth Required** | Yes — `inventory.transfer` permission |
| **Description** | Initiates an inter-branch stock transfer. Stock is decremented from `from_branch_id` and incremented at `to_branch_id`. Both branches must belong to the authenticated tenant. |

**Request Body:**

```json
{
  "from_branch_id": "branch-uuid-001",
  "to_branch_id": "branch-uuid-002",
  "transfer_date": "2026-04-05",
  "reference": "TRF-2026-0014",
  "lines": [
    {
      "item_id": "item-uuid-012",
      "qty": 5
    },
    {
      "item_id": "item-uuid-019",
      "qty": 10
    }
  ],
  "notes": "Replenishment for Jinja Branch."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `from_branch_id` | string (UUID) | Yes | Source branch. Must differ from `to_branch_id`. |
| `to_branch_id` | string (UUID) | Yes | Destination branch. |
| `transfer_date` | string (ISO 8601) | Yes | Effective transfer date. |
| `reference` | string | Yes | Transfer reference number. |
| `lines` | array | Yes | Minimum 1 line. Each `qty` must be > 0. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "trf-uuid-0014",
    "reference": "TRF-2026-0014",
    "status": "completed",
    "lines_transferred": 2,
    "created_at": "2026-04-05T15:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 422 `UNPROCESSABLE_ENTITY` (insufficient stock at source branch; `from_branch_id` equals `to_branch_id`).

---

## GET /api/v1/inventory/stock-count/sessions

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/inventory/stock-count/sessions` |
| **Auth Required** | Yes — `inventory.read` permission |
| **Description** | Returns a paginated list of physical stock count sessions for the tenant. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `branch_id` | string (UUID) | No | Filter by branch. |
| `status` | string | No | `open`, `in_progress`, `closed`. |
| `page` | integer | No | Page number (default: 1). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "sc-uuid-0007",
        "reference": "STKCNT-2026-Q1",
        "branch_id": "branch-uuid-001",
        "branch_name": "Kampala Head Office",
        "status": "in_progress",
        "opened_at": "2026-03-31T08:00:00Z",
        "closed_at": null,
        "items_counted": 142,
        "items_total": 310
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 3, "total_pages": 1 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`.

---

## POST /api/v1/inventory/stock-count/sessions/{id}/counts

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/inventory/stock-count/sessions/{id}/counts` |
| **Auth Required** | Yes — `inventory.count` permission |
| **Description** | Submits a physical count entry for a single item within an open stock count session. The system records the counted quantity alongside the system quantity at the time of counting and calculates the variance. Posting the session reconciles the variance and creates GL adjustment entries. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Stock count session identifier. |

**Request Body:**

```json
{
  "item_id": "item-uuid-012",
  "counted_qty": 14,
  "notes": "2 units found in receiving area, not yet in system."
}
```

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "cnt-uuid-0142",
    "session_id": "sc-uuid-0007",
    "item_id": "item-uuid-012",
    "system_qty": 15,
    "counted_qty": 14,
    "variance": -1,
    "created_at": "2026-04-05T09:00:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 404 | `NOT_FOUND` | Session or item not found within tenant. |
| 409 | `CONFLICT` | A count entry for this item already exists in the session. Use PUT to update. |
| 422 | `UNPROCESSABLE_ENTITY` | Session status is not `open` or `in_progress`. |
