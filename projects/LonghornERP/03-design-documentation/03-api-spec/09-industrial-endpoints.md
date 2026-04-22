# Industrial Module Endpoints

All endpoints in this section require `Authorization: Bearer <token>` and the corresponding module claim in the JWT. The `tenant_id` is resolved exclusively from the token or the authenticated web session.

---

## GET /api/v1/plm/items

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/plm/items` |
| **Auth Required** | Yes - `plm.read` permission |
| **Description** | Returns a paginated list of PLM-controlled engineering items and their latest revision state. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `item_class` | string | No | Filter by engineering item class. |
| `lifecycle_state` | string | No | Filter by latest revision state. |
| `search` | string | No | Partial match on `item_code` or `name`. |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response - 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "plm-item-001",
        "item_code": "FG-COOKOIL-1L",
        "name": "Refined Cooking Oil 1L",
        "item_class": "FINISHED_GOOD",
        "latest_revision": "C",
        "lifecycle_state": "released",
        "effective_from": "2026-04-01T00:00:00Z"
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 42, "total_pages": 2 }
  },
  "error": null
}
```

---

## POST /api/v1/plm/items

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/plm/items` |
| **Auth Required** | Yes - `plm.manage` permission |
| **Description** | Creates a new engineering item and its first draft revision. |

**Request Body:**

```json
{
  "item_code": "FG-COOKOIL-1L",
  "name": "Refined Cooking Oil 1L",
  "item_class": "FINISHED_GOOD",
  "uom_id": "uom-kg",
  "initial_revision": "A"
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "plm-item-001",
    "revision_id": "plm-rev-001",
    "lifecycle_state": "draft"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 409 `CONFLICT`, 422 `UNPROCESSABLE_ENTITY`.

---

## POST /api/v1/plm/ecrs

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/plm/ecrs` |
| **Auth Required** | Yes - `plm.change.request` permission |
| **Description** | Submits an Engineering Change Request (ECR) against a controlled PLM object. |

**Request Body:**

```json
{
  "target_type": "REVISION",
  "target_id": "plm-rev-001",
  "reason": "Cap diameter updated to new supplier standard.",
  "impact_summary": "Affects bottle cap drawing, BOM line, and line setup instruction.",
  "requested_effective_date": "2026-05-01"
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "ecr-001",
    "status": "submitted"
  },
  "error": null
}
```

---

## POST /api/v1/plm/ecos/{id}/release

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/plm/ecos/{id}/release` |
| **Auth Required** | Yes - `plm.release` permission |
| **Description** | Releases an approved ECO and triggers downstream publication to enabled modules. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | ECO identifier. |

**Success Response - 200 OK:**

```json
{
  "success": true,
  "data": {
    "id": "eco-001",
    "status": "released",
    "publication_state": "pending"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT`, 422 `UNPROCESSABLE_ENTITY`.

---

## GET /api/v1/transportation/shipments

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/transportation/shipments` |
| **Auth Required** | Yes - `transportation.read` permission |
| **Description** | Returns shipment orders available for planning or already assigned to transport flows. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `status` | string | No | Filter by shipment status. |
| `origin_branch_id` | string (UUID) | No | Filter by origin branch. |
| `service_priority` | string | No | `standard`, `urgent`, or `critical`. |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response - 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "ship-001",
        "source_type": "SALES_ORDER",
        "source_id": "so-001",
        "origin_branch_id": "branch-001",
        "requested_ship_date": "2026-04-25",
        "service_priority": "urgent",
        "status": "unplanned"
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 18, "total_pages": 1 }
  },
  "error": null
}
```

---

## POST /api/v1/transportation/routes

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/transportation/routes` |
| **Auth Required** | Yes - `transportation.plan` permission |
| **Description** | Creates a transport route with ordered stops and assigned shipment orders. |

**Request Body:**

```json
{
  "load_id": "load-001",
  "planned_departure_at": "2026-04-25T08:00:00Z",
  "planned_distance_km": 312.4,
  "stops": [
    {
      "stop_sequence": 1,
      "stop_type": "delivery",
      "party_name": "Jinja Wholesale",
      "address_text": "Plot 8 Main Street, Jinja",
      "planned_arrival_at": "2026-04-25T11:15:00Z"
    }
  ]
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "route-001",
    "planning_status": "planned"
  },
  "error": null
}
```

---

## POST /api/v1/transportation/routes/{id}/dispatch

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/transportation/routes/{id}/dispatch` |
| **Auth Required** | Yes - `transportation.dispatch` permission |
| **Description** | Dispatches a planned route using either internal fleet or an external carrier. |

**Request Body:**

```json
{
  "resource_mode": "internal_fleet",
  "vehicle_asset_id": "asset-vehicle-001",
  "driver_user_id": "user-driver-008"
}
```

**Success Response - 200 OK:**

```json
{
  "success": true,
  "data": {
    "trip_id": "trip-001",
    "route_status": "dispatched"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT`, 422 `UNPROCESSABLE_ENTITY`.

---

## POST /api/v1/transportation/trips/{id}/milestones

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/transportation/trips/{id}/milestones` |
| **Auth Required** | Yes - `transportation.execute` permission |
| **Description** | Records a trip milestone, refreshes ETA, and evaluates exception thresholds. |

**Request Body:**

```json
{
  "event_type": "arrived_stop",
  "route_stop_id": "stop-003",
  "event_time": "2026-04-25T11:42:00Z",
  "latitude": 0.4471,
  "longitude": 33.2041,
  "note": "Delayed by heavy traffic."
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "event_id": "trip-event-009",
    "eta_refresh_completed": true,
    "exception_created": true
  },
  "error": null
}
```

---

## POST /api/v1/transportation/trips/{id}/proofs

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/transportation/trips/{id}/proofs` |
| **Auth Required** | Yes - `transportation.execute` permission |
| **Description** | Captures proof of delivery or other stop-completion evidence. |

**Request Body:**

```json
{
  "route_stop_id": "stop-003",
  "proof_type": "signature",
  "signature_name": "Sarah Namukasa"
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "proof_id": "proof-001",
    "captured_at": "2026-04-25T11:45:10Z"
  },
  "error": null
}
```

---

## POST /api/v1/transportation/settlements

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/transportation/settlements` |
| **Auth Required** | Yes - `transportation.settle` permission |
| **Description** | Submits a carrier invoice or internal-trip settlement for audit and posting. |

**Request Body:**

```json
{
  "trip_id": "trip-001",
  "settlement_type": "carrier_invoice",
  "planned_cost_total": 850000.00,
  "actual_cost_total": 920000.00,
  "lines": [
    { "charge_type": "LINEHAUL", "amount": 800000.00 },
    { "charge_type": "TOLL", "amount": 120000.00 }
  ]
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "settlement-001",
    "status": "audit_hold",
    "variance_pct": 8.235
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 422 `UNPROCESSABLE_ENTITY`.
