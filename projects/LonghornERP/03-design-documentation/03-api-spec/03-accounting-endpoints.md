# Accounting Module Endpoints

All endpoints in this section require `Authorization: Bearer <token>` and the `accounting` module claim in the JWT. The `tenant_id` is resolved exclusively from the token — it is never accepted as a request parameter.

---

## GET /api/v1/accounting/accounts

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/accounting/accounts` |
| **Auth Required** | Yes — `accounting.read` permission |
| **Description** | Returns the full Chart of Accounts for the authenticated tenant, filtered to the requesting branch where applicable. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `type` | string | No | Filter by account type: `asset`, `liability`, `equity`, `revenue`, `expense`. |
| `search` | string | No | Partial match on account name or account code. |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "acc-uuid-001",
        "code": "1001",
        "name": "Cash at Bank — Stanbic",
        "type": "asset",
        "sub_type": "current_asset",
        "currency": "UGX",
        "is_active": true,
        "balance": 15000000.00
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 84, "total_pages": 4 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`.

---

## POST /api/v1/accounting/journals

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/journals` |
| **Auth Required** | Yes — `accounting.post` permission |
| **Description** | Creates a manual journal entry. The sum of all `debit` values must equal the sum of all `credit` values; the server rejects an unbalanced entry with 422. |

**Request Body:**

```json
{
  "date": "2026-04-05",
  "reference": "JNL-2026-0042",
  "description": "Monthly accrual — office rent",
  "lines": [
    {
      "account_id": "acc-uuid-021",
      "debit": 2500000.00,
      "credit": 0.00,
      "narration": "Rent expense April 2026"
    },
    {
      "account_id": "acc-uuid-043",
      "debit": 0.00,
      "credit": 2500000.00,
      "narration": "Accrued liabilities — rent"
    }
  ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `date` | string (ISO 8601) | Yes | Journal date. Must fall within an open accounting period. |
| `reference` | string | Yes | Unique reference number for this journal. Max 50 characters. |
| `description` | string | No | Narrative description of the journal. |
| `lines` | array | Yes | Journal lines. Minimum 2 lines required. |
| `lines[].account_id` | string (UUID) | Yes | GL account identifier. |
| `lines[].debit` | number | Yes | Debit amount. Set to `0.00` for credit-only lines. |
| `lines[].credit` | number | Yes | Credit amount. Set to `0.00` for debit-only lines. |
| `lines[].narration` | string | No | Line-level narrative. |

**Validation Rule:** $\sum(\text{debit}) = \sum(\text{credit})$. Any deviation returns 422.

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "jnl-uuid-0042",
    "reference": "JNL-2026-0042",
    "status": "draft",
    "total": 2500000.00,
    "created_at": "2026-04-05T09:15:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing required fields or malformed lines array. |
| 409 | `CONFLICT` | `reference` already exists for this tenant. |
| 422 | `UNPROCESSABLE_ENTITY` | Debits do not equal credits, or the journal date falls in a closed period. |

---

## GET /api/v1/accounting/trial-balance

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/accounting/trial-balance` |
| **Auth Required** | Yes — `reports.read` permission |
| **Description** | Returns the trial balance for the tenant, either for a specific accounting period or as at a given date. One of `period_id` or `as_at_date` must be supplied. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `period_id` | string (UUID) | Conditional | Accounting period identifier. Mutually exclusive with `as_at_date`. |
| `as_at_date` | string (ISO 8601) | Conditional | Calculates balances as at this date. Mutually exclusive with `period_id`. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "as_at": "2026-03-31",
    "lines": [
      {
        "account_id": "acc-uuid-001",
        "account_code": "1001",
        "account_name": "Cash at Bank — Stanbic",
        "debit_balance": 15000000.00,
        "credit_balance": 0.00
      }
    ],
    "totals": {
      "total_debit": 245000000.00,
      "total_credit": 245000000.00
    }
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST` (neither or both parameters supplied), 403 `FORBIDDEN`.

---

## GET /api/v1/accounting/invoices

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/accounting/invoices` |
| **Auth Required** | Yes — `accounting.read` permission |
| **Description** | Returns a paginated list of sales invoices for the tenant. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `customer_id` | string (UUID) | No | Filter by customer. |
| `status` | string | No | `draft`, `posted`, `paid`, `overdue`, `cancelled`. |
| `date_from` | string (ISO 8601) | No | Invoice date range start (inclusive). |
| `date_to` | string (ISO 8601) | No | Invoice date range end (inclusive). |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "inv-uuid-0101",
        "invoice_number": "INV-2026-0101",
        "customer_id": "cust-uuid-007",
        "customer_name": "Acme Distributors Ltd",
        "invoice_date": "2026-03-15",
        "due_date": "2026-04-14",
        "total_amount": 5750000.00,
        "amount_paid": 0.00,
        "balance_due": 5750000.00,
        "status": "posted",
        "currency": "UGX"
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 214, "total_pages": 9 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`.

---

## POST /api/v1/accounting/invoices

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/invoices` |
| **Auth Required** | Yes — `accounting.write` permission |
| **Description** | Creates a new sales invoice in `draft` status. The invoice is not posted to the GL until `POST /api/v1/accounting/invoices/{id}/post` is called. |

**Request Body:**

```json
{
  "customer_id": "cust-uuid-007",
  "invoice_date": "2026-04-05",
  "due_date": "2026-05-05",
  "currency": "UGX",
  "lines": [
    {
      "item_id": "item-uuid-012",
      "description": "Office Chair — Ergonomic",
      "quantity": 5,
      "unit_price": 450000.00,
      "tax_code": "VAT18"
    }
  ],
  "notes": "Delivery to Kampala warehouse."
}
```

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "inv-uuid-0215",
    "invoice_number": "INV-2026-0215",
    "status": "draft",
    "subtotal": 2250000.00,
    "tax_total": 405000.00,
    "total_amount": 2655000.00,
    "created_at": "2026-04-05T10:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND` (invalid `customer_id` or `item_id`), 422 `UNPROCESSABLE_ENTITY` (closed period or invalid tax code).

---

## POST /api/v1/accounting/invoices/{id}/post

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/invoices/{id}/post` |
| **Auth Required** | Yes — `accounting.post` permission |
| **Description** | Posts a draft invoice to the General Ledger. Posting is irreversible; a posted invoice can only be reversed by a credit note. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Invoice identifier. |

**Request Body:** None.

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "id": "inv-uuid-0215",
    "status": "posted",
    "gl_entry_id": "jnl-uuid-auto-0215",
    "posted_at": "2026-04-05T10:05:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 404 | `NOT_FOUND` | Invoice does not exist within the tenant. |
| 409 | `CONFLICT` | Invoice is already posted or cancelled. |
| 422 | `UNPROCESSABLE_ENTITY` | Invoice date falls in a closed accounting period. |

---

## POST /api/v1/accounting/payments

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/payments` |
| **Auth Required** | Yes — `accounting.write` permission |
| **Description** | Records a customer payment and allocates it against outstanding invoices. The payment is posted to the GL immediately. |

**Request Body:**

```json
{
  "customer_id": "cust-uuid-007",
  "payment_date": "2026-04-05",
  "amount": 5750000.00,
  "payment_method": "bank_transfer",
  "reference": "TXN-STANBIC-20260405-001",
  "bank_account_id": "acc-uuid-001",
  "allocations": [
    {
      "invoice_id": "inv-uuid-0101",
      "amount_allocated": 5750000.00
    }
  ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `customer_id` | string (UUID) | Yes | Customer making the payment. |
| `payment_date` | string (ISO 8601) | Yes | Date of receipt. |
| `amount` | number | Yes | Total payment amount. Must be > 0. |
| `payment_method` | string | Yes | `cash`, `bank_transfer`, `mobile_money`, `cheque`. |
| `reference` | string | Yes | Bank reference or receipt number. |
| `bank_account_id` | string (UUID) | Yes | GL account to debit (cash/bank account). |
| `allocations` | array | No | Invoice allocations. If omitted, the payment is recorded as an unallocated credit. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "pmt-uuid-0301",
    "reference": "TXN-STANBIC-20260405-001",
    "amount": 5750000.00,
    "unallocated_balance": 0.00,
    "gl_entry_id": "jnl-uuid-auto-0301",
    "created_at": "2026-04-05T11:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 422 `UNPROCESSABLE_ENTITY` (allocated amount exceeds invoice balance or payment amount).

---

## GET /api/v1/accounting/reports/balance-sheet

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/accounting/reports/balance-sheet` |
| **Auth Required** | Yes — `reports.read` permission |
| **Description** | Returns the Balance Sheet for the tenant as at the specified date, structured into Assets, Liabilities, and Equity sections. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `as_at_date` | string (ISO 8601) | Yes | Date for which balances are calculated. |
| `branch_id` | string (UUID) | No | Restrict to a specific branch. Omit for consolidated view. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "as_at": "2026-03-31",
    "assets": {
      "current_assets": { "total": 45000000.00, "lines": [] },
      "non_current_assets": { "total": 120000000.00, "lines": [] },
      "total_assets": 165000000.00
    },
    "liabilities": {
      "current_liabilities": { "total": 18000000.00, "lines": [] },
      "non_current_liabilities": { "total": 22000000.00, "lines": [] },
      "total_liabilities": 40000000.00
    },
    "equity": {
      "total_equity": 125000000.00,
      "lines": []
    },
    "check": {
      "balanced": true,
      "assets_minus_liabilities_equity": 0.00
    }
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST` (missing `as_at_date`), 403 `FORBIDDEN`.

---

## GET /api/v1/accounting/reports/profit-loss

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/accounting/reports/profit-loss` |
| **Auth Required** | Yes — `reports.read` permission |
| **Description** | Returns the Profit and Loss (Income Statement) for the tenant for the specified date range, structured into Revenue and Expense categories. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `period_from` | string (ISO 8601) | Yes | Start of reporting period (inclusive). |
| `period_to` | string (ISO 8601) | Yes | End of reporting period (inclusive). |
| `branch_id` | string (UUID) | No | Restrict to a specific branch. Omit for consolidated view. |
| `compare_prior_period` | boolean | No | If `true`, includes a comparison column for the equivalent prior period. Default: `false`. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "period_from": "2026-01-01",
    "period_to": "2026-03-31",
    "revenue": {
      "total": 98000000.00,
      "lines": []
    },
    "cost_of_sales": {
      "total": 54000000.00,
      "lines": []
    },
    "gross_profit": 44000000.00,
    "operating_expenses": {
      "total": 21000000.00,
      "lines": []
    },
    "net_profit": 23000000.00
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST` (missing date parameters or `period_from` > `period_to`), 403 `FORBIDDEN`.
