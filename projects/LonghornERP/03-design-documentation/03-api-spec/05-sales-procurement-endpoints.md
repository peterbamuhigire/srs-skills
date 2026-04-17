# Sales and Procurement Module Endpoints

All endpoints in this section require `Authorization: Bearer <token>`. Sales endpoints require the `sales` module claim; procurement endpoints require the `procurement` module claim. The `tenant_id` is resolved exclusively from the token.

---

## Sales Endpoints

### GET /api/v1/sales/customers

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/sales/customers` |
| **Auth Required** | Yes — `sales.read` permission |
| **Description** | Returns a paginated list of customers for the authenticated tenant. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `search` | string | No | Partial match on customer name, phone, or email. |
| `customer_type` | string | No | `individual`, `company`. |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "cust-uuid-007",
        "name": "Acme Distributors Ltd",
        "customer_type": "company",
        "tin": "1002345678",
        "email": "accounts@acme.co.ug",
        "phone": "+256700000001",
        "credit_limit": 20000000.00,
        "outstanding_balance": 5750000.00,
        "currency": "UGX",
        "is_active": true
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 88, "total_pages": 4 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`.

---

### POST /api/v1/sales/customers

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/sales/customers` |
| **Auth Required** | Yes — `sales.write` permission |
| **Description** | Creates a new customer record for the tenant. |

**Request Body:**

```json
{
  "name": "Pearl Foods Uganda Ltd",
  "customer_type": "company",
  "tin": "1009876543",
  "email": "purchasing@pearlfoodsug.com",
  "phone": "+256772000002",
  "address": "Plot 15, Nakawa Industrial Area, Kampala",
  "credit_limit": 10000000.00,
  "currency": "UGX",
  "payment_terms_days": 30
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Customer name. Max 200 characters. |
| `customer_type` | string | Yes | `individual` or `company`. |
| `tin` | string | No | URA Tax Identification Number. Must be unique within the tenant. |
| `email` | string | No | Contact email address. |
| `phone` | string | No | Contact phone number in E.164 format. |
| `credit_limit` | number | No | Maximum outstanding balance permitted. |
| `payment_terms_days` | integer | No | Default payment due days (e.g., 30 for Net 30). |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "cust-uuid-089",
    "name": "Pearl Foods Uganda Ltd",
    "created_at": "2026-04-05T09:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 409 `CONFLICT` (duplicate TIN).

---

### POST /api/v1/sales/quotations

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/sales/quotations` |
| **Auth Required** | Yes — `sales.write` permission |
| **Description** | Creates a new sales quotation. Quotations do not affect inventory or GL until converted to a sales order and subsequently invoiced. |

**Request Body:**

```json
{
  "customer_id": "cust-uuid-007",
  "quotation_date": "2026-04-05",
  "valid_until": "2026-04-19",
  "currency": "UGX",
  "lines": [
    {
      "item_id": "item-uuid-012",
      "description": "Office Chair — Ergonomic",
      "quantity": 10,
      "unit_price": 450000.00,
      "discount_percent": 5.0,
      "tax_code": "VAT18"
    }
  ],
  "notes": "Prices valid for 14 days."
}
```

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "quot-uuid-0033",
    "quotation_number": "QUO-2026-0033",
    "status": "draft",
    "subtotal": 4275000.00,
    "tax_total": 769500.00,
    "total_amount": 5044500.00,
    "created_at": "2026-04-05T09:30:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND` (invalid `customer_id` or `item_id`).

---

### POST /api/v1/sales/quotations/{id}/convert

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/sales/quotations/{id}/convert` |
| **Auth Required** | Yes — `sales.write` permission |
| **Description** | Converts an accepted quotation to a Sales Order. The quotation status changes to `converted`; a new sales order is created. Stock is reserved against the order. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Quotation identifier. |

**Request Body:**

```json
{
  "customer_po_reference": "PO-ACME-2026-0015",
  "requested_delivery_date": "2026-04-20"
}
```

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "sales_order_id": "so-uuid-0077",
    "sales_order_number": "SO-2026-0077",
    "quotation_id": "quot-uuid-0033",
    "status": "confirmed",
    "created_at": "2026-04-05T10:00:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 404 | `NOT_FOUND` | Quotation not found within the tenant. |
| 409 | `CONFLICT` | Quotation is already converted, expired, or cancelled. |
| 422 | `UNPROCESSABLE_ENTITY` | Quotation validity date has passed. |

---

### GET /api/v1/sales/orders

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/sales/orders` |
| **Auth Required** | Yes — `sales.read` permission |
| **Description** | Returns a paginated list of sales orders for the tenant. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `customer_id` | string (UUID) | No | Filter by customer. |
| `status` | string | No | `confirmed`, `partially_fulfilled`, `fulfilled`, `cancelled`. |
| `date_from` | string (ISO 8601) | No | Order date range start (inclusive). |
| `date_to` | string (ISO 8601) | No | Order date range end (inclusive). |
| `page` | integer | No | Page number (default: 1). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "so-uuid-0077",
        "order_number": "SO-2026-0077",
        "customer_id": "cust-uuid-007",
        "customer_name": "Acme Distributors Ltd",
        "order_date": "2026-04-05",
        "delivery_date": "2026-04-20",
        "total_amount": 5044500.00,
        "status": "confirmed",
        "currency": "UGX"
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 55, "total_pages": 3 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`.

---

### POST /api/v1/sales/invoices/{id}/submit-efris

<!-- [CONTEXT-GAP: GAP-001] EFRIS integration details — URA API endpoint, authentication mechanism (certificate or API key), EFRIS invoice fields (fiscal document number, QR code, verification URL), error response codes from URA, handling of EFRIS retries and offline scenarios — are not yet documented in `_context/`. This endpoint specification is a stub. Full implementation details must be provided before development begins. -->

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/sales/invoices/{id}/submit-efris` |
| **Auth Required** | Yes — `sales.efris` permission |
| **Description** | Submits a posted sales invoice to the Uganda Revenue Authority Electronic Fiscal Receipting and Invoicing Solution (EFRIS). On success, the invoice is stamped with the URA fiscal document number and QR code. `[CONTEXT-GAP: GAP-001]` |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Invoice identifier. The invoice must already be in `posted` status. |

**Request Body:** None.

**Success Response — 200 OK (stub — subject to URA EFRIS API response contract):**

```json
{
  "success": true,
  "data": {
    "invoice_id": "inv-uuid-0215",
    "efris_status": "accepted",
    "fiscal_document_number": "FDN-UG-2026-XXXXXXX",
    "qr_code_url": "https://efris.ura.go.ug/verify/FDN-UG-2026-XXXXXXX",
    "submitted_at": "2026-04-05T10:10:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 404 | `NOT_FOUND` | Invoice not found within tenant. |
| 409 | `CONFLICT` | Invoice has already been submitted to EFRIS. |
| 422 | `UNPROCESSABLE_ENTITY` | Invoice is in `draft` status; must be posted first. |
| 502 | `BAD_GATEWAY` | URA EFRIS API returned an error or was unreachable. `[CONTEXT-GAP: GAP-001]` |

---

## Procurement Endpoints

### POST /api/v1/procurement/requisitions

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/procurement/requisitions` |
| **Auth Required** | Yes — `procurement.write` permission |
| **Description** | Creates a Purchase Requisition (PR). The requisition enters a configurable approval workflow before an LPO can be raised. |

**Request Body:**

```json
{
  "branch_id": "branch-uuid-001",
  "requested_date": "2026-04-10",
  "lines": [
    {
      "item_id": "item-uuid-012",
      "qty": 20,
      "estimated_unit_cost": 350000.00,
      "reason": "Replenishment — below reorder level."
    }
  ],
  "notes": "Urgent — stock depleted at Kampala branch."
}
```

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "pr-uuid-0055",
    "reference": "PR-2026-0055",
    "status": "pending_approval",
    "created_at": "2026-04-05T08:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND` (invalid `branch_id` or `item_id`).

---

### POST /api/v1/procurement/lpos

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/procurement/lpos` |
| **Auth Required** | Yes — `procurement.write` permission |
| **Description** | Creates a Local Purchase Order (LPO) against an approved requisition or directly. The LPO is sent to the supplier and used as the basis for three-way matching against the GRN and supplier invoice. |

**Request Body:**

```json
{
  "supplier_id": "supp-uuid-005",
  "requisition_id": "pr-uuid-0055",
  "lpo_date": "2026-04-06",
  "expected_delivery_date": "2026-04-10",
  "currency": "UGX",
  "lines": [
    {
      "item_id": "item-uuid-012",
      "qty": 20,
      "unit_cost": 350000.00,
      "tax_code": "VAT18"
    }
  ],
  "terms": "Payment 30 days after delivery."
}
```

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "lpo-uuid-0088",
    "lpo_number": "LPO-2026-0088",
    "status": "sent",
    "total_amount": 8260000.00,
    "created_at": "2026-04-06T08:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 422 `UNPROCESSABLE_ENTITY` (requisition not in `approved` status).

---

### GET /api/v1/procurement/lpos/{id}

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/procurement/lpos/{id}` |
| **Auth Required** | Yes — `procurement.read` permission |
| **Description** | Returns the full detail of an LPO including its three-way match status: LPO line quantities versus GRN received quantities versus supplier invoice quantities. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | LPO identifier. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "id": "lpo-uuid-0088",
    "lpo_number": "LPO-2026-0088",
    "supplier_id": "supp-uuid-005",
    "supplier_name": "Uganda Office Supplies Ltd",
    "status": "partially_received",
    "three_way_match": {
      "status": "partial",
      "lines": [
        {
          "item_id": "item-uuid-012",
          "item_name": "Office Chair — Ergonomic",
          "lpo_qty": 20,
          "grn_qty": 20,
          "invoice_qty": 0,
          "match_status": "grn_pending_invoice"
        }
      ]
    }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`, 404 `NOT_FOUND`.

---

### POST /api/v1/procurement/supplier-invoices/{id}/match

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/procurement/supplier-invoices/{id}/match` |
| **Auth Required** | Yes — `procurement.match` permission |
| **Description** | Triggers three-way matching for a supplier invoice against the linked LPO and GRN. The system compares quantities and amounts. Discrepancies beyond the configured tolerance threshold are flagged and must be resolved before the invoice can be approved for payment. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Supplier invoice identifier. |

**Request Body:** None.

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "supplier_invoice_id": "sinv-uuid-0044",
    "match_status": "matched",
    "discrepancies": [],
    "approved_for_payment": true,
    "matched_at": "2026-04-07T11:00:00Z"
  },
  "error": null
}
```

When discrepancies are found:

```json
{
  "success": true,
  "data": {
    "supplier_invoice_id": "sinv-uuid-0044",
    "match_status": "discrepancy",
    "discrepancies": [
      {
        "item_id": "item-uuid-012",
        "field": "unit_cost",
        "lpo_value": 350000.00,
        "invoice_value": 365000.00,
        "variance": 15000.00,
        "variance_percent": 4.29
      }
    ],
    "approved_for_payment": false,
    "matched_at": "2026-04-07T11:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT` (invoice already matched), 422 `UNPROCESSABLE_ENTITY` (no linked LPO or GRN).

---

### POST /api/v1/procurement/payments

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/procurement/payments` |
| **Auth Required** | Yes — `procurement.pay` permission |
| **Description** | Records a payment to a supplier. If the supplier is subject to Withholding Tax (WHT), the WHT deduction is calculated automatically and posted to the WHT payable GL account. The net payment amount is the gross amount minus the WHT deduction. |

**Request Body:**

```json
{
  "supplier_id": "supp-uuid-005",
  "payment_date": "2026-04-08",
  "gross_amount": 8260000.00,
  "wht_rate_percent": 6.0,
  "payment_method": "bank_transfer",
  "reference": "PMT-SUPP-2026-0088",
  "bank_account_id": "acc-uuid-001",
  "allocations": [
    {
      "supplier_invoice_id": "sinv-uuid-0044",
      "amount_allocated": 8260000.00
    }
  ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `supplier_id` | string (UUID) | Yes | Supplier being paid. |
| `payment_date` | string (ISO 8601) | Yes | Payment date. |
| `gross_amount` | number | Yes | Gross invoice amount before WHT deduction. |
| `wht_rate_percent` | number | No | WHT rate as a percentage (e.g., `6.0` for 6%). If 0 or omitted, no WHT is deducted. |
| `payment_method` | string | Yes | `cash`, `bank_transfer`, `cheque`. |
| `reference` | string | Yes | Payment reference number. |
| `bank_account_id` | string (UUID) | Yes | GL account to credit (cash/bank account). |

**WHT Calculation:** $\text{WHT Amount} = \text{Gross Amount} \times \dfrac{\text{WHT Rate}}{100}$

$\text{Net Payment} = \text{Gross Amount} - \text{WHT Amount}$

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "spmt-uuid-0088",
    "reference": "PMT-SUPP-2026-0088",
    "gross_amount": 8260000.00,
    "wht_amount": 495600.00,
    "net_payment": 7764400.00,
    "wht_gl_entry_id": "jnl-uuid-wht-0088",
    "payment_gl_entry_id": "jnl-uuid-pmt-0088",
    "created_at": "2026-04-08T10:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 422 `UNPROCESSABLE_ENTITY` (supplier invoice not approved for payment; allocated amount exceeds invoice balance).
