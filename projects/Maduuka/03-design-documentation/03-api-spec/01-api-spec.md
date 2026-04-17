---
title: "Maduuka Platform — REST API Specification, Version 1.0"
author: "Chwezi Core Systems"
date: "2026-04-05"
---

# Maduuka Platform REST API Specification

**Document ID:** MADUUKA-API-SPEC-001
**Version:** 1.0
**Status:** Draft
**Owner:** Peter Bamuhigire, Chwezi Core Systems
**Date:** 2026-04-05

---

## 1. Introduction

### 1.1 Purpose

This document specifies the REST API contract for the Maduuka SaaS platform, Version 1. It defines all endpoints, request schemas, response schemas, authentication requirements, error codes, and behavioural constraints that API consumers — Android clients (Phase 1), Web clients (Phase 1), and iOS clients (Phase 2) — must comply with. All endpoint implementations shall conform to IEEE 830 verifiability requirements: each behavioural rule maps to a deterministic stimulus-response pair that permits unambiguous test oracle construction.

### 1.2 Scope

This specification covers:

- Authentication and session management
- All Phase 1 core module endpoints: POS/Sales, Inventory, Customers, Suppliers, Expenses, Financial Accounts, Reports, HR and Payroll, Dashboard, and Settings
- Offline synchronisation protocol
- Request/response conventions, pagination, and error handling
- Rate limiting policy

Phase 2 add-on modules (Restaurant, Pharmacy) and Phase 3 modules (Hotel, Advanced Inventory, EFRIS) are not covered in this version.

### 1.3 Base URL

All API requests shall target the following base URL:

```
https://api.maduuka.app/v1/
```

### 1.4 Versioning Strategy

The API uses URI versioning. The version segment `/v1/` is mandatory in every request path. When a breaking change is introduced, the API shall be published under a new version segment (e.g., `/v2/`) while `/v1/` continues to be served for a minimum deprecation window of 12 months. Non-breaking additions (new optional fields, new endpoints) shall be made within the current version without a version increment.

### 1.5 Transport Security

All requests shall be transmitted over TLS 1.3. The server shall reject connections negotiated under TLS 1.2 or lower with HTTP status `421 Misdirected Request`. Android and iOS clients shall enforce certificate pinning via OkHttp `CertificatePinner` (Android) and `URLSession` with a pinned certificate hash (iOS).

### 1.6 Authentication Overview

The API supports two authentication modes:

- **JWT Bearer tokens** — used by Android and iOS mobile clients. A 15-minute access token and a 30-day refresh token are issued at login.
- **Session cookies + CSRF** — used by the Web client. A `CSRF-Token` header is required on all state-changing requests from the web session.

Every protected endpoint requires the headers described in Section 2.5.

---

## 2. Authentication

### 2.1 POST /v1/auth/login

Authenticates a user and issues a JWT access token and refresh token.

**Auth required:** None

**Request body:**

```json
{
  "email": "string",
  "password": "string",
  "device_id": "string (UUID, required for mobile clients)",
  "device_name": "string (optional, e.g. 'Samsung Galaxy A54')"
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "access_token": "string (JWT, expires in 900 seconds)",
    "refresh_token": "string (opaque, expires in 2592000 seconds)",
    "token_type": "Bearer",
    "expires_in": 900,
    "user": {
      "id": "uuid",
      "name": "string",
      "email": "string",
      "role": "owner | manager | cashier | hr_manager",
      "franchise_id": "uuid",
      "franchise_name": "string",
      "requires_2fa": "boolean"
    }
  }
}
```

**Notes:**

- If `requires_2fa` is `true`, the access token is a provisional token valid only for `POST /v1/auth/2fa/verify`. Full API access is granted only after 2FA verification.
- Passwords are stored as bcrypt hashes; the plaintext password is never logged.

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 401 | `INVALID_CREDENTIALS` | Email or password incorrect |
| 403 | `ACCOUNT_SUSPENDED` | Business account suspended |
| 422 | `VALIDATION_ERROR` | Required field missing or malformed |
| 429 | `RATE_LIMIT_EXCEEDED` | Too many login attempts |

---

### 2.2 POST /v1/auth/refresh

Exchanges a valid refresh token for a new access token and a rotated refresh token.

**Auth required:** None (refresh token in body)

**Request body:**

```json
{
  "refresh_token": "string"
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "access_token": "string (JWT)",
    "refresh_token": "string (rotated)",
    "token_type": "Bearer",
    "expires_in": 900
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 401 | `INVALID_REFRESH_TOKEN` | Token not found, expired, or already rotated |
| 401 | `REFRESH_TOKEN_REVOKED` | Token revoked via device management |

---

### 2.3 POST /v1/auth/logout

Revokes the current access token and refresh token for the authenticated device.

**Auth required:** Yes (Bearer)

**Request body:** Empty.

**Response `204 No Content`:** No body.

---

### 2.4 POST /v1/auth/2fa/verify

Verifies a Time-Based One-Time Password (TOTP) for users with 2FA enabled. On success, the provisional access token is upgraded to a full-access token.

**Auth required:** Provisional Bearer (issued at login when `requires_2fa` is `true`)

**Request body:**

```json
{
  "totp_code": "string (6-digit numeric)"
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "access_token": "string (full-access JWT)",
    "refresh_token": "string",
    "token_type": "Bearer",
    "expires_in": 900
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 401 | `INVALID_TOTP` | Code incorrect or expired |
| 429 | `TOTP_ATTEMPTS_EXCEEDED` | 5 consecutive failures; account locked for 15 minutes |

---

### 2.5 Required Headers on All Protected Endpoints

Every request to a protected endpoint shall include the following headers:

| Header | Format | Description |
|---|---|---|
| `Authorization` | `Bearer <access_token>` | JWT access token |
| `X-Franchise-ID` | UUID | Tenant identifier; must match the `franchise_id` in the JWT payload |
| `Content-Type` | `application/json` | Required for all `POST`, `PUT`, and `PATCH` requests |
| `Accept` | `application/json` | Required on all requests |

The server shall return `403 Forbidden` with code `FRANCHISE_MISMATCH` if the `X-Franchise-ID` header value does not match the `franchise_id` claim in the JWT.

---

## 3. Core Module Endpoints

### 3.1 POS — Sales

#### 3.1.1 POST /v1/pos/sessions

Opens a new POS cashier session. A session must be open before any sale can be processed (BR-007).

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Request body:**

```json
{
  "branch_id": "uuid",
  "device_id": "uuid",
  "opening_float": {
    "currency": "UGX",
    "amount": 50000
  },
  "note": "string (optional)"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "franchise_id": "uuid",
    "branch_id": "uuid",
    "cashier_id": "uuid",
    "device_id": "uuid",
    "opened_at": "2026-04-05T08:00:00Z",
    "opening_float": 50000,
    "status": "open"
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `SESSION_ALREADY_OPEN` | Cashier already has an open session on this device |
| 422 | `VALIDATION_ERROR` | Required field missing |

---

#### 3.1.2 GET /v1/pos/sessions/{id}

Retrieves a POS session by its identifier.

**Auth required:** Yes — roles: `owner`, `manager`, `cashier` (own session only for cashier)

**Path parameters:** `id` — UUID of the session.

**Response `200 OK`:**

```json
{
  "data": {
    "id": "uuid",
    "branch_id": "uuid",
    "cashier_id": "uuid",
    "cashier_name": "string",
    "device_id": "uuid",
    "opened_at": "2026-04-05T08:00:00Z",
    "closed_at": "2026-04-05T18:00:00Z | null",
    "opening_float": 50000,
    "status": "open | closed",
    "total_cash_sales": 380000,
    "total_momo_sales": 120000,
    "total_credit_sales": 45000,
    "total_refunds": 10000,
    "sale_count": 42,
    "void_count": 1
  }
}
```

---

#### 3.1.3 POST /v1/pos/sessions/{id}/close

Closes a POS session and records the reconciliation data.

**Auth required:** Yes — roles: `owner`, `manager`, `cashier` (own session)

**Path parameters:** `id` — UUID of the session.

**Request body:**

```json
{
  "closing_cash_count": 420000,
  "note": "string (optional)"
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "closed",
    "closed_at": "2026-04-05T18:00:00Z",
    "opening_float": 50000,
    "expected_closing_cash": 425000,
    "declared_closing_cash": 420000,
    "variance": -5000,
    "variance_flagged": true
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `SESSION_ALREADY_CLOSED` | Session is not in `open` status |
| 409 | `PENDING_SALES_EXIST` | One or more sales in session are not finalised |

---

#### 3.1.4 POST /v1/sales

Creates a new sale. Accepts a cart of items, a payments array, and an optional customer reference.

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Headers (additional):** `X-Idempotency-Key: <uuid>` — required; prevents duplicate processing on network retry.

**Request body:**

```json
{
  "session_id": "uuid",
  "customer_id": "uuid | null",
  "items": [
    {
      "product_id": "uuid",
      "quantity": 2,
      "unit_price": 5000,
      "discount_amount": 0,
      "batch_id": "uuid | null"
    }
  ],
  "order_discount_amount": 0,
  "payments": [
    {
      "method": "cash | mtn_momo | airtel_money | credit",
      "amount": 10000,
      "reference": "string (MoMo transaction ID, optional)"
    }
  ],
  "note": "string (optional)"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "receipt_number": "string",
    "franchise_id": "uuid",
    "branch_id": "uuid",
    "session_id": "uuid",
    "cashier_id": "uuid",
    "customer_id": "uuid | null",
    "sale_date": "2026-04-05T10:30:00Z",
    "subtotal": 10000,
    "discount_total": 0,
    "tax_total": 0,
    "total": 10000,
    "payments": [
      {
        "method": "cash",
        "amount": 10000
      }
    ],
    "change_due": 0,
    "status": "completed",
    "items": [
      {
        "product_id": "uuid",
        "product_name": "string",
        "quantity": 2,
        "unit_price": 5000,
        "line_total": 10000
      }
    ]
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `NO_OPEN_SESSION` | No open POS session for this cashier/device |
| 409 | `CREDIT_LIMIT_EXCEEDED` | Customer credit limit would be breached (BR-002) |
| 409 | `INSUFFICIENT_STOCK` | One or more items have insufficient stock |
| 409 | `IDEMPOTENCY_CONFLICT` | Idempotency key already used with different payload |
| 422 | `PAYMENT_SUM_MISMATCH` | Sum of payment amounts does not equal the sale total |

---

#### 3.1.5 GET /v1/sales/{id}

Retrieves a completed sale by identifier.

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Path parameters:** `id` — UUID of the sale.

**Response `200 OK`:** Same schema as the `POST /v1/sales` response body, with the addition of:

```json
{
  "data": {
    "void_reason": "string | null",
    "refund_of_sale_id": "uuid | null",
    "audit_trail": [
      {
        "action": "created | voided | refunded",
        "actor_id": "uuid",
        "timestamp": "2026-04-05T10:30:00Z"
      }
    ]
  }
}
```

---

#### 3.1.6 POST /v1/sales/{id}/void

Voids a completed sale. A reason code is mandatory (BR-003).

**Auth required:** Yes — roles: `owner`, `manager`

**Path parameters:** `id` — UUID of the sale.

**Request body:**

```json
{
  "reason_code": "string (e.g. DATA_ENTRY_ERROR | CUSTOMER_CANCELLATION | OTHER)",
  "note": "string (optional)"
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "voided",
    "voided_at": "2026-04-05T11:00:00Z",
    "voided_by": "uuid",
    "reason_code": "DATA_ENTRY_ERROR"
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `SALE_ALREADY_VOIDED` | Sale is already in voided status |
| 409 | `SALE_REFUNDED` | Sale has already been refunded; cannot void |
| 422 | `REASON_CODE_REQUIRED` | `reason_code` is absent |

---

#### 3.1.7 POST /v1/sales/{id}/refund

Records a refund against a completed sale. Stock levels are reversed on refund.

**Auth required:** Yes — roles: `owner`, `manager`

**Path parameters:** `id` — UUID of the original sale.

**Request body:**

```json
{
  "items": [
    {
      "sale_item_id": "uuid",
      "quantity": 1
    }
  ],
  "reason_code": "string",
  "refund_method": "cash | mtn_momo | airtel_money | credit_note",
  "note": "string (optional)"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "refund_id": "uuid",
    "original_sale_id": "uuid",
    "refund_amount": 5000,
    "refund_method": "cash",
    "refunded_at": "2026-04-05T11:15:00Z"
  }
}
```

---

#### 3.1.8 GET /v1/sales/{id}/receipt

Returns receipt data for a completed sale in the requested format.

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Path parameters:** `id` — UUID of the sale.

**Query parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `format` | string | No | `thermal` (default), `pdf`, or `digital` |

**Response `200 OK` (format: thermal or digital):** JSON receipt object containing all fields required for rendering.

**Response `200 OK` (format: pdf):** Returns `Content-Type: application/pdf` with the PDF binary stream.

---

#### 3.1.9 POST /v1/sync/sales

Uploads an array of offline sales that were queued during a connectivity outage (BR-009).

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Headers (additional):** `X-Idempotency-Key: <uuid>` — required per sync batch.

**Request body:**

```json
{
  "sales": [
    {
      "offline_id": "uuid (client-generated)",
      "offline_created_at": "2026-04-05T09:45:00Z",
      "session_id": "uuid",
      "customer_id": "uuid | null",
      "items": [ ],
      "payments": [ ],
      "order_discount_amount": 0,
      "note": "string | null"
    }
  ]
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "processed": 3,
    "failed": 0,
    "id_map": [
      {
        "offline_id": "uuid",
        "server_id": "uuid",
        "status": "synced | duplicate | failed",
        "error": "string | null"
      }
    ]
  }
}
```

**Conflict resolution:** If a sale with the same `offline_id` is submitted more than once, the server returns `status: duplicate` and the previously assigned `server_id`. No duplicate record is created.

---

### 3.2 Inventory

#### 3.2.1 GET /v1/products

Returns a paginated list of products for the authenticated tenant.

**Auth required:** Yes — all roles

**Query parameters:**

| Parameter | Type | Description |
|---|---|---|
| `search` | string | Partial match on name, SKU, or barcode |
| `category_id` | uuid | Filter by category |
| `barcode` | string | Exact barcode match |
| `page` | integer | Page number (default: 1) |
| `per_page` | integer | Results per page (default: 20, max: 100) |

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "name": "string",
      "sku": "string",
      "barcode": "string | null",
      "category_id": "uuid",
      "category_name": "string",
      "uom": "string",
      "cost_price": 3000,
      "retail_price": 5000,
      "wholesale_price": 4000,
      "reorder_level": 10,
      "track_batches": false,
      "status": "active | inactive"
    }
  ],
  "meta": {
    "total": 120,
    "page": 1,
    "per_page": 20,
    "last_page": 6
  }
}
```

---

#### 3.2.2 POST /v1/products

Creates a new product in the catalogue.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "name": "string",
  "sku": "string (unique per franchise)",
  "barcode": "string | null",
  "category_id": "uuid",
  "uom": "string",
  "cost_price": 3000,
  "retail_price": 5000,
  "wholesale_price": 4000,
  "reorder_level": 10,
  "track_batches": false,
  "image_url": "string | null",
  "status": "active"
}
```

**Response `201 Created`:** Full product object as in `GET /v1/products/{id}`.

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `SKU_DUPLICATE` | SKU already exists for this franchise |
| 409 | `BARCODE_DUPLICATE` | Barcode already assigned to another product |

---

#### 3.2.3 GET /v1/products/{id}

Returns a single product record.

**Auth required:** Yes — all roles

**Response `200 OK`:** Full product object including pricing tiers, UOM conversions, and image URL.

---

#### 3.2.4 PUT /v1/products/{id}

Updates a product record. All writable fields are replaceable.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:** Same schema as `POST /v1/products`. All fields optional; only supplied fields are updated.

**Response `200 OK`:** Updated product object.

---

#### 3.2.5 GET /v1/products/{id}/stock

Returns stock levels for a product across all branches and warehouses.

**Auth required:** Yes — all roles

**Response `200 OK`:**

```json
{
  "data": {
    "product_id": "uuid",
    "product_name": "string",
    "locations": [
      {
        "branch_id": "uuid",
        "branch_name": "string",
        "warehouse_id": "uuid",
        "warehouse_name": "string",
        "quantity_on_hand": 45,
        "quantity_in_transit": 0,
        "quantity_reserved": 0,
        "uom": "string"
      }
    ]
  }
}
```

---

#### 3.2.6 POST /v1/stock/adjustments

Records a stock adjustment. Adjustments above the configured monetary threshold are submitted in `pending_approval` status and require manager approval before the stock level is updated (BR-005).

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Request body:**

```json
{
  "product_id": "uuid",
  "branch_id": "uuid",
  "warehouse_id": "uuid",
  "adjustment_type": "increase | decrease",
  "quantity": 10,
  "reason_code": "string (e.g. DAMAGE | THEFT | COUNT_CORRECTION | RETURN)",
  "batch_id": "uuid | null",
  "note": "string (optional)"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "applied | pending_approval",
    "requires_approval": true,
    "estimated_value_impact": 30000
  }
}
```

---

#### 3.2.7 POST /v1/stock/transfers

Initiates a stock transfer between two branches or warehouses.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "from_branch_id": "uuid",
  "from_warehouse_id": "uuid",
  "to_branch_id": "uuid",
  "to_warehouse_id": "uuid",
  "items": [
    {
      "product_id": "uuid",
      "quantity": 5,
      "batch_id": "uuid | null"
    }
  ],
  "note": "string (optional)"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "in_transit",
    "created_at": "2026-04-05T10:00:00Z",
    "items": []
  }
}
```

---

#### 3.2.8 GET /v1/stock/movements

Returns a paginated, filterable list of stock movements.

**Auth required:** Yes — roles: `owner`, `manager`

**Query parameters:**

| Parameter | Type | Description |
|---|---|---|
| `product_id` | uuid | Filter by product |
| `from` | date | Start date (ISO 8601) |
| `to` | date | End date (ISO 8601) |
| `type` | string | `purchase | sale | adjustment | transfer | return` |
| `branch_id` | uuid | Filter by branch |
| `page` | integer | Page number |
| `per_page` | integer | Results per page |

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "product_id": "uuid",
      "product_name": "string",
      "movement_type": "sale",
      "quantity": -2,
      "reference_id": "uuid",
      "reference_type": "sale",
      "actor_id": "uuid",
      "timestamp": "2026-04-05T10:30:00Z",
      "batch_id": "uuid | null"
    }
  ],
  "meta": { }
}
```

---

#### 3.2.9 POST /v1/stock/count

Submits a physical stock count for a branch/warehouse. The count is recorded with a variance report pending manager approval. Stock levels are not updated until the count is approved (BR-004).

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "branch_id": "uuid",
  "warehouse_id": "uuid",
  "count_date": "2026-04-05",
  "items": [
    {
      "product_id": "uuid",
      "counted_quantity": 38,
      "batch_id": "uuid | null"
    }
  ],
  "note": "string (optional)"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "pending_approval",
    "variance_count": 3,
    "total_variance_value": 9000
  }
}
```

---

### 3.3 Customers

#### 3.3.1 GET /v1/customers

Returns a paginated list of customers.

**Auth required:** Yes — all roles

**Query parameters:** `search` (name/phone), `group_id`, `page`, `per_page`.

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "name": "string",
      "phone": "string",
      "email": "string | null",
      "group": "retail | wholesale | vip | staff",
      "credit_limit": 200000,
      "outstanding_balance": 45000,
      "status": "active | inactive"
    }
  ],
  "meta": { }
}
```

---

#### 3.3.2 POST /v1/customers

Creates a new customer record.

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Request body:**

```json
{
  "name": "string",
  "phone": "string (E.164 format)",
  "email": "string | null",
  "district": "string | null",
  "sub_county": "string | null",
  "group": "retail | wholesale | vip | staff",
  "credit_limit": 0,
  "note": "string | null"
}
```

**Response `201 Created`:** Full customer object.

---

#### 3.3.3 GET /v1/customers/{id}

Returns a single customer with current credit balance.

**Auth required:** Yes — all roles

**Response `200 OK`:**

```json
{
  "data": {
    "id": "uuid",
    "name": "string",
    "phone": "string",
    "email": "string | null",
    "district": "string | null",
    "sub_county": "string | null",
    "group": "string",
    "credit_limit": 200000,
    "outstanding_balance": 45000,
    "available_credit": 155000,
    "created_at": "2026-01-15T08:00:00Z"
  }
}
```

---

#### 3.3.4 PUT /v1/customers/{id}

Updates a customer record.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:** Same fields as `POST /v1/customers`, all optional.

**Response `200 OK`:** Updated customer object.

---

#### 3.3.5 GET /v1/customers/{id}/transactions

Returns the transaction history for a customer.

**Auth required:** Yes — all roles

**Query parameters:** `from`, `to`, `type` (sale | payment | refund), `page`, `per_page`.

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "type": "sale | payment | refund",
      "amount": 25000,
      "running_balance": 45000,
      "reference_id": "uuid",
      "date": "2026-04-01T14:00:00Z",
      "recorded_by": "string"
    }
  ],
  "meta": { }
}
```

---

#### 3.3.6 GET /v1/customers/{id}/statement

Returns a customer account statement for a date range.

**Auth required:** Yes — roles: `owner`, `manager`

**Query parameters:** `from` (required), `to` (required), `format` (json | pdf).

**Response `200 OK` (json):** Opening balance, list of transactions, closing balance.

**Response `200 OK` (pdf):** `Content-Type: application/pdf` with statement PDF.

---

#### 3.3.7 POST /v1/customers/{id}/payments

Records a credit payment received from a customer.

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Request body:**

```json
{
  "amount": 25000,
  "payment_method": "cash | mtn_momo | airtel_money | bank",
  "reference": "string (MoMo or bank reference, optional)",
  "payment_date": "2026-04-05",
  "note": "string | null"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "customer_id": "uuid",
    "amount": 25000,
    "new_outstanding_balance": 20000,
    "payment_date": "2026-04-05"
  }
}
```

---

### 3.4 Suppliers

#### 3.4.1 GET /v1/suppliers

Returns a paginated list of suppliers.

**Auth required:** Yes — roles: `owner`, `manager`

**Query parameters:** `search`, `page`, `per_page`.

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "name": "string",
      "phone": "string",
      "email": "string | null",
      "payment_terms_days": 30,
      "outstanding_balance": 150000,
      "status": "active | inactive"
    }
  ],
  "meta": { }
}
```

---

#### 3.4.2 POST /v1/suppliers

Creates a new supplier record.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "name": "string",
  "phone": "string",
  "email": "string | null",
  "address": "string | null",
  "payment_terms_days": 30,
  "bank_name": "string | null",
  "bank_account_number": "string | null",
  "tin": "string | null",
  "note": "string | null"
}
```

**Response `201 Created`:** Full supplier object.

---

#### 3.4.3 GET /v1/suppliers/{id}

Returns a single supplier record.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:** Full supplier object with `outstanding_balance`.

---

#### 3.4.4 PUT /v1/suppliers/{id}

Updates a supplier record.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:** Same fields as `POST /v1/suppliers`, all optional.

**Response `200 OK`:** Updated supplier object.

---

#### 3.4.5 GET /v1/suppliers/{id}/transactions

Returns the purchase and payment history for a supplier.

**Auth required:** Yes — roles: `owner`, `manager`

**Query parameters:** `from`, `to`, `page`, `per_page`.

**Response `200 OK`:** Paginated list of transactions with `type` (purchase | payment), `amount`, `running_balance`, `reference_id`, and `date`.

---

#### 3.4.6 POST /v1/purchase-orders

Creates a purchase order (PO).

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "supplier_id": "uuid",
  "branch_id": "uuid",
  "expected_delivery_date": "2026-04-12",
  "items": [
    {
      "product_id": "uuid",
      "quantity": 20,
      "unit_cost": 3000
    }
  ],
  "note": "string | null"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "po_number": "string",
    "supplier_id": "uuid",
    "status": "draft | sent",
    "total_amount": 60000,
    "created_at": "2026-04-05T09:00:00Z"
  }
}
```

---

#### 3.4.7 GET /v1/purchase-orders/{id}

Returns a purchase order with line items and current receipt status.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:** Full PO object including items, quantities ordered, quantities received, and status.

---

#### 3.4.8 POST /v1/purchase-orders/{id}/receive

Records a goods receipt against a purchase order. Partial receipts are supported.

**Auth required:** Yes — roles: `owner`, `manager`

**Path parameters:** `id` — UUID of the purchase order.

**Request body:**

```json
{
  "received_date": "2026-04-12",
  "items": [
    {
      "po_item_id": "uuid",
      "quantity_received": 15,
      "batch_number": "string | null",
      "expiry_date": "2027-06-30 | null",
      "unit_cost_actual": 3000
    }
  ],
  "supplier_invoice_number": "string | null",
  "note": "string | null"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "grn_id": "uuid",
    "po_id": "uuid",
    "status": "partial | fully_received",
    "three_way_match_status": "matched | discrepancy",
    "discrepancies": [
      {
        "product_id": "uuid",
        "field": "unit_cost | quantity",
        "po_value": 3000,
        "received_value": 3100
      }
    ]
  }
}
```

**Notes:** Three-way matching (BR-011) is executed automatically. Any unit cost or quantity discrepancy greater than UGX 0 sets `three_way_match_status` to `discrepancy` and requires manager resolution before stock is posted.

---

#### 3.4.9 POST /v1/suppliers/{id}/payments

Records a payment made to a supplier.

**Auth required:** Yes — roles: `owner`, `manager`

**Path parameters:** `id` — UUID of the supplier.

**Request body:**

```json
{
  "amount": 60000,
  "payment_method": "cash | bank | mtn_momo | airtel_money",
  "reference": "string | null",
  "payment_date": "2026-04-12",
  "note": "string | null"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "supplier_id": "uuid",
    "amount": 60000,
    "new_outstanding_balance": 90000,
    "payment_date": "2026-04-12"
  }
}
```

---

### 3.5 Expenses

#### 3.5.1 GET /v1/expenses

Returns a paginated, filterable list of expenses.

**Auth required:** Yes — roles: `owner`, `manager`

**Query parameters:** `from`, `to`, `category_id`, `payment_method`, `status` (pending | approved | rejected), `page`, `per_page`.

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "category_id": "uuid",
      "category_name": "string",
      "amount": 15000,
      "payment_method": "cash | mtn_momo | airtel_money | bank",
      "expense_date": "2026-04-05",
      "description": "string",
      "status": "pending | approved | rejected",
      "receipt_url": "string | null",
      "recorded_by": "uuid",
      "approved_by": "uuid | null"
    }
  ],
  "meta": { }
}
```

---

#### 3.5.2 POST /v1/expenses

Records a new expense. Supports an optional receipt photo URL (upload separately to Wasabi S3, then reference the URL).

**Auth required:** Yes — roles: `owner`, `manager`, `cashier`

**Request body:**

```json
{
  "category_id": "uuid",
  "amount": 15000,
  "payment_method": "cash | mtn_momo | airtel_money | bank",
  "expense_date": "2026-04-05",
  "description": "string",
  "receipt_url": "string | null",
  "tax_deductible": false,
  "note": "string | null"
}
```

**Response `201 Created`:** Expense object. If the amount exceeds the configured approval threshold, `status` is `pending`; otherwise `status` is `approved`.

---

#### 3.5.3 GET /v1/expenses/{id}

Returns a single expense record.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:** Full expense object.

---

#### 3.5.4 PUT /v1/expenses/{id}/approve

Approves or rejects a pending expense.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "action": "approve | reject",
  "note": "string (required when action is reject)"
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "approved | rejected",
    "actioned_by": "uuid",
    "actioned_at": "2026-04-05T12:00:00Z"
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `EXPENSE_ALREADY_ACTIONED` | Expense is not in `pending` status |

---

#### 3.5.5 GET /v1/expense-categories

Returns all expense categories for the franchise.

**Auth required:** Yes — all roles

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "name": "string",
      "description": "string | null"
    }
  ]
}
```

---

#### 3.5.6 POST /v1/expense-categories

Creates a new expense category.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "name": "string",
  "description": "string | null"
}
```

**Response `201 Created`:** Category object.

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `CATEGORY_NAME_DUPLICATE` | Category name already exists for this franchise |

---

### 3.6 Financial Accounts

#### 3.6.1 GET /v1/accounts

Returns all defined payment accounts with current balances.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "name": "string",
      "type": "cash_till | mtn_momo | airtel_money | bank | sacco",
      "currency": "UGX",
      "current_balance": 2500000,
      "branch_id": "uuid"
    }
  ]
}
```

---

#### 3.6.2 POST /v1/accounts/transfers

Records a transfer of funds between two internal payment accounts.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "from_account_id": "uuid",
  "to_account_id": "uuid",
  "amount": 500000,
  "transfer_date": "2026-04-05",
  "reference": "string | null",
  "note": "string | null"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "from_account_new_balance": 2000000,
    "to_account_new_balance": 1200000,
    "transfer_date": "2026-04-05"
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `INSUFFICIENT_BALANCE` | Source account balance is less than transfer amount |
| 409 | `SAME_ACCOUNT_TRANSFER` | Source and destination account are identical |

---

#### 3.6.3 GET /v1/accounts/{id}/transactions

Returns the transaction log for a payment account.

**Auth required:** Yes — roles: `owner`, `manager`

**Query parameters:** `from`, `to`, `page`, `per_page`.

**Response `200 OK`:** Paginated list of transactions with `type`, `amount`, `running_balance`, `reference_id`, `reference_type`, and `timestamp`.

---

#### 3.6.4 POST /v1/accounts/{id}/deposits

Records a deposit into a payment account.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "amount": 1000000,
  "deposit_date": "2026-04-05",
  "source": "string",
  "reference": "string | null",
  "note": "string | null"
}
```

**Response `201 Created`:** Deposit record with updated `account_balance`.

---

#### 3.6.5 POST /v1/accounts/{id}/withdrawals

Records a withdrawal from a payment account.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "amount": 200000,
  "withdrawal_date": "2026-04-05",
  "purpose": "string",
  "reference": "string | null",
  "note": "string | null"
}
```

**Response `201 Created`:** Withdrawal record with updated `account_balance`.

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `INSUFFICIENT_BALANCE` | Account balance is less than the withdrawal amount |

---

#### 3.6.6 POST /v1/accounts/reconcile

Initiates a bank reconciliation for a specified account and period.

**Auth required:** Yes — roles: `owner`, `manager`

**Request body:**

```json
{
  "account_id": "uuid",
  "statement_from": "2026-04-01",
  "statement_to": "2026-04-30",
  "statement_closing_balance": 3200000,
  "items": [
    {
      "transaction_id": "uuid",
      "matched": true
    }
  ]
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "reconciliation_id": "uuid",
    "status": "balanced | unbalanced",
    "book_balance": 3200000,
    "statement_balance": 3200000,
    "difference": 0,
    "unmatched_count": 0
  }
}
```

---

### 3.7 Reports

All report endpoints share the following common query parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `from` | date (ISO 8601) | Yes | Report start date |
| `to` | date (ISO 8601) | Yes | Report end date |
| `branch_id` | uuid | No | Filter to a specific branch; omit for all branches |
| `format` | string | No | `json` (default), `csv`, or `pdf` |

When `format` is `pdf` or `csv`, the response carries the appropriate `Content-Type` and a `Content-Disposition: attachment` header.

---

#### 3.7.1 GET /v1/reports/sales/daily

Returns a day-level summary of sales for the specified date range.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": [
    {
      "date": "2026-04-05",
      "revenue": 850000,
      "transactions": 72,
      "cash": 620000,
      "momo": 180000,
      "credit": 50000,
      "refunds": 10000,
      "voids": 2
    }
  ]
}
```

---

#### 3.7.2 GET /v1/reports/sales/summary

Returns an aggregate sales summary for the specified date range.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": {
    "from": "2026-04-01",
    "to": "2026-04-30",
    "total_revenue": 18500000,
    "total_collected": 16200000,
    "total_outstanding_credit": 2300000,
    "transaction_count": 1240,
    "average_transaction_value": 14919,
    "refund_count": 12,
    "refund_total": 95000,
    "void_count": 8
  }
}
```

---

#### 3.7.3 GET /v1/reports/sales/by-product

Returns sales totals broken down by product.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": [
    {
      "product_id": "uuid",
      "product_name": "string",
      "sku": "string",
      "quantity_sold": 120,
      "revenue": 600000,
      "cogs": 360000,
      "gross_margin": 240000,
      "gross_margin_pct": 40.0
    }
  ],
  "meta": { }
}
```

---

#### 3.7.4 GET /v1/reports/sales/top-sellers

Returns the top N products by revenue or quantity sold.

**Auth required:** Yes — roles: `owner`, `manager`

**Query parameters (additional):** `limit` (default: 10, max: 50), `sort_by` (revenue | quantity).

**Response `200 OK`:** Same structure as `GET /v1/reports/sales/by-product`, ordered by the specified sort field descending.

---

#### 3.7.5 GET /v1/reports/sales/voids

Returns a list of voided and refunded transactions.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": [
    {
      "sale_id": "uuid",
      "type": "void | refund",
      "receipt_number": "string",
      "amount": 10000,
      "reason_code": "string",
      "actioned_by": "string",
      "actioned_at": "2026-04-05T11:00:00Z"
    }
  ],
  "meta": { }
}
```

---

#### 3.7.6 GET /v1/reports/sales/receipt-gaps

Identifies gaps in sequential receipt numbering within sessions during the specified date range (BR-008).

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": [
    {
      "session_id": "uuid",
      "cashier_name": "string",
      "session_date": "2026-04-05",
      "expected_receipt": "R-1013",
      "gap_before": "R-1012",
      "gap_after": "R-1014"
    }
  ]
}
```

---

#### 3.7.7 GET /v1/reports/margin

Returns gross margin analysis by product, category, or period.

**Auth required:** Yes — roles: `owner`, `manager`

**Query parameters (additional):** `group_by` (product | category | day | week | month).

**Response `200 OK`:**

```json
{
  "data": [
    {
      "group_label": "string",
      "revenue": 850000,
      "cogs": 510000,
      "gross_margin": 340000,
      "gross_margin_pct": 40.0
    }
  ]
}
```

---

### 3.8 HR and Payroll

#### 3.8.1 GET /v1/staff

Returns a paginated list of staff members.

**Auth required:** Yes — roles: `owner`, `manager`, `hr_manager`

**Query parameters:** `search`, `branch_id`, `department`, `employment_type`, `status`, `page`, `per_page`.

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "name": "string",
      "phone": "string",
      "job_title": "string",
      "department": "string",
      "branch_id": "uuid",
      "employment_type": "full_time | part_time | contract",
      "hire_date": "2025-01-15",
      "status": "active | inactive | terminated"
    }
  ],
  "meta": { }
}
```

---

#### 3.8.2 POST /v1/staff

Creates a new staff profile.

**Auth required:** Yes — roles: `owner`, `manager`, `hr_manager`

**Request body:**

```json
{
  "name": "string",
  "phone": "string",
  "email": "string | null",
  "nin": "string (National Identification Number)",
  "job_title": "string",
  "department": "string",
  "branch_id": "uuid",
  "employment_type": "full_time | part_time | contract",
  "hire_date": "2026-04-05",
  "basic_salary": 600000,
  "role": "owner | manager | cashier | hr_manager"
}
```

**Response `201 Created`:** Full staff profile object.

---

#### 3.8.3 GET /v1/staff/{id}

Returns a full staff profile including salary structure, leave balance, and employment details.

**Auth required:** Yes — roles: `owner`, `manager`, `hr_manager`

**Response `200 OK`:** Full staff object including `basic_salary`, `allowances`, `deductions`, `leave_balance`, and contract details.

---

#### 3.8.4 PUT /v1/staff/{id}

Updates a staff profile.

**Auth required:** Yes — roles: `owner`, `manager`, `hr_manager`

**Request body:** Any subset of the `POST /v1/staff` fields.

**Response `200 OK`:** Updated staff object.

---

#### 3.8.5 POST /v1/payroll/runs

Creates a monthly payroll run for all active staff in the franchise.

**Auth required:** Yes — roles: `owner`, `hr_manager`

**Request body:**

```json
{
  "payroll_month": "2026-04",
  "branch_id": "uuid | null (null = all branches)"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "payroll_month": "2026-04",
    "status": "draft",
    "staff_count": 12,
    "gross_total": 8400000,
    "nssf_employer_total": 840000,
    "paye_total": 320000,
    "net_total": 7820000
  }
}
```

---

#### 3.8.6 GET /v1/payroll/runs/{id}

Returns the payroll run with a summary and line-by-line breakdown per staff member.

**Auth required:** Yes — roles: `owner`, `hr_manager`

**Response `200 OK`:** Full payroll run object including `status`, totals, and a `lines` array with one entry per staff member.

---

#### 3.8.7 POST /v1/payroll/runs/{id}/approve

Approves a payroll run. Once approved, payslip amounts are locked (BR-012).

**Auth required:** Yes — roles: `owner`

**Request body:** Empty.

**Response `200 OK`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "approved",
    "approved_by": "uuid",
    "approved_at": "2026-04-30T10:00:00Z"
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `PAYROLL_ALREADY_APPROVED` | Run is not in `draft` status |

---

#### 3.8.8 GET /v1/payroll/runs/{id}/payslips/{staff_id}

Returns the payslip for a specific staff member within an approved payroll run.

**Auth required:** Yes — roles: `owner`, `hr_manager`

**Query parameters:** `format` (json | pdf).

**Response `200 OK` (json):**

```json
{
  "data": {
    "payroll_run_id": "uuid",
    "staff_id": "uuid",
    "staff_name": "string",
    "payroll_month": "2026-04",
    "basic_salary": 600000,
    "allowances": [],
    "gross_salary": 650000,
    "nssf_employee": 32500,
    "paye": 28000,
    "lst": 5000,
    "other_deductions": 0,
    "net_pay": 584500
  }
}
```

---

#### 3.8.9 POST /v1/leave/requests

Submits a leave request.

**Auth required:** Yes — all roles (own request)

**Request body:**

```json
{
  "staff_id": "uuid",
  "leave_type_id": "uuid",
  "start_date": "2026-04-10",
  "end_date": "2026-04-12",
  "note": "string | null"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "pending",
    "days_requested": 3,
    "leave_balance_before": 14
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `INSUFFICIENT_LEAVE_BALANCE` | Requested days exceed staff leave entitlement |

---

#### 3.8.10 PUT /v1/leave/requests/{id}/approve

Approves or rejects a leave request.

**Auth required:** Yes — roles: `owner`, `manager`, `hr_manager`

**Request body:**

```json
{
  "action": "approve | reject",
  "note": "string (required when action is reject)"
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "id": "uuid",
    "status": "approved | rejected",
    "actioned_by": "uuid",
    "actioned_at": "2026-04-06T09:00:00Z"
  }
}
```

---

#### 3.8.11 GET /v1/attendance

Returns attendance records.

**Auth required:** Yes — roles: `owner`, `manager`, `hr_manager`

**Query parameters:** `staff_id`, `from`, `to`, `branch_id`, `page`, `per_page`.

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "staff_id": "uuid",
      "staff_name": "string",
      "clock_in_at": "2026-04-05T08:02:00Z",
      "clock_out_at": "2026-04-05T17:05:00Z | null",
      "hours_worked": 9.05,
      "clock_in_lat": "0.3476",
      "clock_in_lng": "32.5825"
    }
  ],
  "meta": { }
}
```

---

#### 3.8.12 POST /v1/attendance/clock-in

Records a staff clock-in event.

**Auth required:** Yes — all roles (own record)

**Request body:**

```json
{
  "staff_id": "uuid",
  "latitude": "0.3476",
  "longitude": "32.5825",
  "device_id": "uuid"
}
```

**Response `201 Created`:**

```json
{
  "data": {
    "id": "uuid",
    "staff_id": "uuid",
    "clock_in_at": "2026-04-05T08:02:00Z"
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `ALREADY_CLOCKED_IN` | Staff member has an open clock-in record |

---

#### 3.8.13 POST /v1/attendance/clock-out

Records a staff clock-out event, closing the open clock-in record.

**Auth required:** Yes — all roles (own record)

**Request body:**

```json
{
  "staff_id": "uuid",
  "latitude": "0.3476",
  "longitude": "32.5825",
  "device_id": "uuid"
}
```

**Response `200 OK`:**

```json
{
  "data": {
    "id": "uuid",
    "staff_id": "uuid",
    "clock_in_at": "2026-04-05T08:02:00Z",
    "clock_out_at": "2026-04-05T17:05:00Z",
    "hours_worked": 9.05
  }
}
```

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 409 | `NOT_CLOCKED_IN` | No open clock-in record found for this staff member |

---

### 3.9 Dashboard

#### 3.9.1 GET /v1/dashboard/kpis

Returns real-time key performance indicator values for the authenticated user's franchise.

**Auth required:** Yes — all roles

**Query parameters:** `branch_id` (optional — if omitted, returns aggregate for all branches).

**Response `200 OK`:**

```json
{
  "data": {
    "as_of": "2026-04-05T14:30:00Z",
    "branch_id": "uuid | null",
    "today_revenue": 1240000,
    "today_transaction_count": 98,
    "today_revenue_vs_yesterday_pct": 12.5,
    "outstanding_credit": 3800000,
    "cash_position": 2150000,
    "low_stock_count": 4,
    "pending_approvals_count": 2,
    "open_sessions_count": 2
  }
}
```

---

#### 3.9.2 GET /v1/dashboard/alerts

Returns active alerts requiring attention.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": {
    "low_stock": [
      {
        "product_id": "uuid",
        "product_name": "string",
        "quantity_on_hand": 2,
        "reorder_level": 10,
        "branch_name": "string"
      }
    ],
    "pending_approvals": [
      {
        "type": "expense | stock_adjustment | leave | payroll",
        "id": "uuid",
        "description": "string",
        "submitted_by": "string",
        "submitted_at": "2026-04-05T09:00:00Z"
      }
    ],
    "expiring_batches": [
      {
        "product_id": "uuid",
        "product_name": "string",
        "batch_number": "string",
        "expiry_date": "2026-05-01",
        "quantity": 10
      }
    ]
  }
}
```

---

#### 3.9.3 GET /v1/dashboard/health-score

Returns the business health score with Red-Amber-Green (RAG) status indicators derived from gross margin percentage, expense ratio, stock turnover rate, and credit collection rate.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": {
    "overall_rag": "green | amber | red",
    "as_of": "2026-04-05T14:30:00Z",
    "indicators": [
      {
        "name": "gross_margin_pct",
        "value": 38.5,
        "rag": "green",
        "threshold_amber": 25.0,
        "threshold_red": 15.0
      },
      {
        "name": "expense_ratio_pct",
        "value": 18.2,
        "rag": "amber",
        "threshold_amber": 20.0,
        "threshold_red": 30.0
      },
      {
        "name": "stock_turnover_days",
        "value": 21,
        "rag": "green",
        "threshold_amber": 45,
        "threshold_red": 60
      },
      {
        "name": "credit_collection_rate_pct",
        "value": 72.0,
        "rag": "amber",
        "threshold_amber": 75.0,
        "threshold_red": 50.0
      }
    ]
  }
}
```

---

### 3.10 Settings

#### 3.10.1 GET /v1/settings

Returns all configuration settings for the franchise.

**Auth required:** Yes — roles: `owner`, `manager`

**Response `200 OK`:**

```json
{
  "data": {
    "business_name": "string",
    "business_logo_url": "string | null",
    "address": "string",
    "tin": "string | null",
    "currency": "UGX",
    "language": "en | sw",
    "financial_year_start_month": 7,
    "vat_rate_pct": 18.0,
    "vat_mode": "inclusive | exclusive",
    "expense_approval_threshold": 100000,
    "stock_adjustment_approval_threshold": 50000,
    "receipt_header": "string | null",
    "receipt_footer": "string | null",
    "sms_gateway": "africas_talking",
    "2fa_enabled": true
  }
}
```

---

#### 3.10.2 PUT /v1/settings

Updates one or more franchise configuration settings. Partial updates are supported; only supplied fields are modified.

**Auth required:** Yes — roles: `owner`

**Request body:** Any subset of the fields returned by `GET /v1/settings`.

**Response `200 OK`:** Updated settings object.

---

#### 3.10.3 GET /v1/devices

Returns all devices (mobile and web sessions) registered to the franchise.

**Auth required:** Yes — roles: `owner`

**Response `200 OK`:**

```json
{
  "data": [
    {
      "id": "uuid",
      "device_name": "string",
      "device_type": "android | ios | web",
      "last_seen_at": "2026-04-05T14:00:00Z",
      "is_current": true
    }
  ]
}
```

---

#### 3.10.4 DELETE /v1/devices/{id}

Revokes a registered device, invalidating its refresh token immediately.

**Auth required:** Yes — roles: `owner`

**Path parameters:** `id` — UUID of the device.

**Response `204 No Content`:** No body.

**Error codes:**

| HTTP Status | Error Code | Condition |
|---|---|---|
| 403 | `CANNOT_REVOKE_CURRENT_DEVICE` | Attempt to revoke the device on which this request originates |

---

#### 3.10.5 POST /v1/data/export

Requests a full data export for the franchise. The export is generated asynchronously and delivered via email as a password-protected ZIP archive.

**Auth required:** Yes — roles: `owner`

**Request body:** Empty.

**Response `202 Accepted`:**

```json
{
  "data": {
    "export_id": "uuid",
    "status": "queued",
    "estimated_delivery_minutes": 15
  }
}
```

---

## 4. Request and Response Conventions

### 4.1 Content Type

All request bodies shall be encoded as `application/json`. All responses shall be returned as `application/json` unless the `format` query parameter specifies `pdf` (returns `application/pdf`) or `csv` (returns `text/csv`).

### 4.2 Pagination Envelope

All list endpoints that return variable-length result sets shall use the following pagination query parameters and response envelope:

**Query parameters:**

| Parameter | Default | Maximum |
|---|---|---|
| `page` | 1 | — |
| `per_page` | 20 | 100 |

**Response envelope:**

```json
{
  "data": [],
  "meta": {
    "total": 120,
    "page": 1,
    "per_page": 20,
    "last_page": 6
  }
}
```

### 4.3 Error Response Format

All error responses shall use the following structure:

```json
{
  "error": {
    "code": "CREDIT_LIMIT_EXCEEDED",
    "message": "The sale amount of UGX 250,000 would cause the customer's balance to exceed the credit limit of UGX 200,000.",
    "details": {
      "current_balance": 180000,
      "credit_limit": 200000,
      "sale_amount": 70000
    }
  }
}
```

The `code` field is a machine-readable string constant. The `message` field is a human-readable description in English. The `details` object is optional and may contain structured context to assist the client in rendering informative error UI.

### 4.4 Standard HTTP Status Codes

| Code | Meaning | When Used |
|---|---|---|
| 200 | OK | Successful GET, PUT, or action endpoint |
| 201 | Created | Successful POST that creates a resource |
| 202 | Accepted | Asynchronous operation queued |
| 204 | No Content | Successful DELETE or logout |
| 400 | Bad Request | Malformed JSON body |
| 401 | Unauthorized | Missing, expired, or invalid access token |
| 403 | Forbidden | Valid token but insufficient role or franchise mismatch |
| 404 | Not Found | Resource does not exist or belongs to another tenant |
| 409 | Conflict | Business rule violation or state conflict |
| 422 | Unprocessable Entity | Validation error (missing required field, invalid format) |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Unexpected server-side error |

### 4.5 Date and Time Format

All date-time values in request bodies and response payloads shall use ISO 8601 format with UTC timezone designator: `YYYY-MM-DDTHH:MM:SSZ`. Date-only values (e.g., leave dates, payroll month) shall use the format `YYYY-MM-DD`.

### 4.6 Currency Format

All monetary values shall be expressed as integers representing the minor currency unit. For Ugandan Shillings (UGX), which has no decimal subdivision, the integer value is the shilling amount directly. Example: UGX 10,500 is represented as `10500`. No currency symbol or decimal point shall appear in the value field; currency is conveyed separately in the `currency` field where applicable.

### 4.7 Idempotency

`POST /v1/sales` and `POST /v1/sync/sales` require the `X-Idempotency-Key` header containing a client-generated UUID. The server shall process the request exactly once for a given key. If the same key is submitted a second time with an identical payload, the server shall return the original response without creating a duplicate record. If the same key is submitted with a different payload, the server shall return `409 IDEMPOTENCY_CONFLICT`.

The idempotency key is stored for a minimum of 24 hours after first use.

---

## 5. Rate Limiting

The API enforces per-franchise rate limiting at the following thresholds:

| Tier | Requests per Hour |
|---|---|
| Standard | 1,000 |
| Enterprise | 10,000 |

All responses include the following rate limit headers:

| Header | Description |
|---|---|
| `X-RateLimit-Limit` | The maximum number of requests permitted per hour for this tier |
| `X-RateLimit-Remaining` | The number of requests remaining in the current window |
| `X-RateLimit-Reset` | Unix timestamp indicating when the current window resets |

When the rate limit is exceeded, the server shall respond with `429 Too Many Requests` and the error code `RATE_LIMIT_EXCEEDED`. The `X-RateLimit-Reset` header shall indicate when the client may retry.

---

## 6. Offline Sync Protocol

### 6.1 Overview

The Maduuka Android client operates in offline-first mode (BR-009). When internet connectivity is unavailable, all sale transactions are persisted to the local Room database and marked with `sync_status: pending_sync`. The WorkManager background task monitors for connectivity restoration and triggers the sync process automatically.

### 6.2 Sync Endpoint

**Endpoint:** `POST /v1/sync/sales`

The sync payload is a batch of up to 100 pending sales. Each sale object in the array must include:

| Field | Type | Description |
|---|---|---|
| `offline_id` | UUID | Client-generated identifier assigned at the time of offline recording |
| `offline_created_at` | ISO 8601 datetime | Timestamp when the sale was recorded on the device |

### 6.3 Server Response and ID Mapping

The server processes each sale in the order submitted (ascending by `offline_created_at`) and returns a mapping of `offline_id` to `server_id`:

```json
{
  "data": {
    "processed": 5,
    "failed": 0,
    "id_map": [
      {
        "offline_id": "c3f8a2d1-...",
        "server_id": "9b12e4f0-...",
        "status": "synced",
        "error": null
      },
      {
        "offline_id": "d7a1b9e3-...",
        "server_id": "4c88f2a1-...",
        "status": "duplicate",
        "error": null
      }
    ]
  }
}
```

The Android client shall update its local Room database to replace `offline_id` references with the `server_id` values returned by the server.

### 6.4 Conflict Resolution Rules

- **Duplicate submission:** If a sale with the same `offline_id` is received more than once, the server treats the second submission as a duplicate, returns the original `server_id`, and takes no further action.
- **Session validation:** If the referenced `session_id` was closed before the `offline_created_at` timestamp, the sale is accepted and linked to the session; no rejection occurs, as sessions may close before sync completes.
- **Stock deduction:** Stock levels are decremented at sync time using the `offline_created_at` timestamp to order movements correctly within FIFO/FEFO batch selection (BR-006).

### 6.5 Sync Error Handling

If an individual sale within a batch fails validation (e.g., product deleted, customer not found), it is returned with `status: failed` and an `error` message. The remaining sales in the batch are processed normally. The client shall surface failed records for operator review.

---

## Appendix A: RBAC Permission Matrix

The following table summarises which roles may invoke each endpoint group. `Y` denotes permission granted; `-` denotes permission denied.

| Endpoint Group | owner | manager | cashier | hr_manager |
|---|---|---|---|---|
| Auth | Y | Y | Y | Y |
| POS / Sessions | Y | Y | Y | - |
| POS / Sales (create, view) | Y | Y | Y | - |
| POS / Void, Refund | Y | Y | - | - |
| Inventory / Products (read) | Y | Y | Y | - |
| Inventory / Products (write) | Y | Y | - | - |
| Inventory / Adjustments | Y | Y | Y (below threshold) | - |
| Inventory / Transfers | Y | Y | - | - |
| Customers (read) | Y | Y | Y | - |
| Customers (write) | Y | Y | Y | - |
| Suppliers | Y | Y | - | - |
| Purchase Orders | Y | Y | - | - |
| Expenses (create) | Y | Y | Y | - |
| Expenses (approve) | Y | Y | - | - |
| Financial Accounts | Y | Y | - | - |
| Reports | Y | Y | - | - |
| Staff / Payroll | Y | Y (limited) | - | Y |
| Payroll Approve | Y | - | - | - |
| Attendance (own) | Y | Y | Y | Y |
| Dashboard KPIs | Y | Y | Y | Y |
| Dashboard Alerts | Y | Y | - | - |
| Settings (read) | Y | Y | - | - |
| Settings (write) | Y | - | - | - |
| Devices | Y | - | - | - |
| Data Export | Y | - | - | - |

---

## Appendix B: Standard Error Code Reference

| Code | HTTP Status | Description |
|---|---|---|
| `INVALID_CREDENTIALS` | 401 | Email or password is incorrect |
| `TOKEN_EXPIRED` | 401 | Access token has expired |
| `TOKEN_INVALID` | 401 | Access token is malformed or signature invalid |
| `INVALID_REFRESH_TOKEN` | 401 | Refresh token not found, expired, or already rotated |
| `REFRESH_TOKEN_REVOKED` | 401 | Refresh token revoked via device management |
| `INVALID_TOTP` | 401 | TOTP code is incorrect or has expired |
| `TOTP_ATTEMPTS_EXCEEDED` | 429 | 5 consecutive TOTP failures; account locked for 15 minutes |
| `INSUFFICIENT_PERMISSIONS` | 403 | User role does not permit this action |
| `FRANCHISE_MISMATCH` | 403 | `X-Franchise-ID` header does not match JWT claim |
| `ACCOUNT_SUSPENDED` | 403 | Business account has been suspended |
| `CANNOT_REVOKE_CURRENT_DEVICE` | 403 | Attempt to revoke the requesting device |
| `NOT_FOUND` | 404 | Resource does not exist or belongs to another tenant |
| `SESSION_ALREADY_OPEN` | 409 | Duplicate open POS session |
| `SESSION_ALREADY_CLOSED` | 409 | POS session is not in open status |
| `PENDING_SALES_EXIST` | 409 | Open session has unfinished sales |
| `NO_OPEN_SESSION` | 409 | No open POS session for this cashier/device |
| `CREDIT_LIMIT_EXCEEDED` | 409 | Sale would breach customer credit limit |
| `INSUFFICIENT_STOCK` | 409 | Product stock is below the requested sale quantity |
| `IDEMPOTENCY_CONFLICT` | 409 | Idempotency key reused with a different payload |
| `SALE_ALREADY_VOIDED` | 409 | Sale is already in voided status |
| `SALE_REFUNDED` | 409 | Sale cannot be voided after a refund |
| `EXPENSE_ALREADY_ACTIONED` | 409 | Expense approval already completed |
| `INSUFFICIENT_BALANCE` | 409 | Account balance is below the withdrawal or transfer amount |
| `SAME_ACCOUNT_TRANSFER` | 409 | Source and destination accounts are identical |
| `SKU_DUPLICATE` | 409 | SKU already exists for this franchise |
| `BARCODE_DUPLICATE` | 409 | Barcode already assigned to another product |
| `CATEGORY_NAME_DUPLICATE` | 409 | Expense category name already exists |
| `PAYROLL_ALREADY_APPROVED` | 409 | Payroll run is not in draft status |
| `ALREADY_CLOCKED_IN` | 409 | Staff has an open clock-in record |
| `NOT_CLOCKED_IN` | 409 | No open clock-in record for this staff member |
| `INSUFFICIENT_LEAVE_BALANCE` | 409 | Requested leave days exceed entitlement |
| `REASON_CODE_REQUIRED` | 422 | `reason_code` is absent on a void or refund request |
| `PAYMENT_SUM_MISMATCH` | 422 | Sum of payment amounts does not equal the sale total |
| `VALIDATION_ERROR` | 422 | One or more required fields are missing or malformed |
| `RATE_LIMIT_EXCEEDED` | 429 | Per-franchise request rate limit exceeded |
