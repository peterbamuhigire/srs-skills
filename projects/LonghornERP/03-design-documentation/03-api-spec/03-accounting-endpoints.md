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

**Success Response - 200 OK:**

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

---

## POST /api/v1/accounting/close-runs

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/close-runs` |
| **Auth Required** | Yes - `accounting.close.manage` permission |
| **Description** | Starts a controlled finance close run for an entity scope or a reporting-group scope. The server snapshots the selected close template into run-level tasks so later template edits do not mutate the active close. |

**Request Body:**

```json
{
  "period_id": "prd-uuid-2026-03",
  "scope": "entity",
  "group_id": null,
  "template_code": "MONTH_END_STANDARD",
  "target_close_at": "2026-04-03T18:00:00Z",
  "notes": "March 2026 month-end close"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `period_id` | string (UUID) | Yes | Accounting period identifier. |
| `scope` | string | Yes | `entity` or `group`. |
| `group_id` | string (UUID) | Conditional | Required when `scope = group`. Omit for entity close. |
| `template_code` | string | No | Close-template code. Defaults to the tenant's standard template for the selected scope. |
| `target_close_at` | string (ISO 8601) | No | Planned close deadline for SLA tracking. |
| `notes` | string | No | Optional run narrative. |

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "close-uuid-0001",
    "period_id": "prd-uuid-2026-03",
    "scope": "entity",
    "status": "in_progress",
    "total_tasks": 38,
    "mandatory_tasks": 24,
    "started_at": "2026-04-01T06:30:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 409 `CONFLICT` (active close run already exists), 422 `UNPROCESSABLE_ENTITY` (period is not eligible for close orchestration).

---

## POST /api/v1/accounting/close-runs/{id}/tasks/{task_id}/complete

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/close-runs/{id}/tasks/{task_id}/complete` |
| **Auth Required** | Yes - `accounting.close.execute` permission |
| **Description** | Completes a close task, attaches evidence, and triggers certification or approval workflow where the task definition requires it. |

**Request Body:**

```json
{
  "note": "Bank reconciliations completed and reviewed.",
  "evidence": [
    {
      "type": "attachment",
      "file_id": "file-uuid-bankrec-001",
      "reference": "March bank rec pack"
    }
  ],
  "checklist": [
    {
      "code": "BANK_REC_SIGNOFF",
      "result": "pass",
      "comment": "Matched to statement ending 2026-03-31"
    }
  ]
}
```

**Success Response - 200 OK:**

```json
{
  "success": true,
  "data": {
    "close_run_id": "close-uuid-0001",
    "task_id": "task-uuid-0017",
    "status": "completed",
    "approval_status": "not_required",
    "remaining_blockers": 6,
    "completed_at": "2026-04-01T13:40:00Z"
  },
  "error": null
}
```

**Error Codes:** 403 `FORBIDDEN`, 404 `NOT_FOUND`, 409 `CONFLICT` (task dependencies not complete), 422 `UNPROCESSABLE_ENTITY` (required evidence or checklist items missing).

---

## POST /api/v1/accounting/recurring-journal-templates

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/recurring-journal-templates` |
| **Auth Required** | Yes - `accounting.config.manage` permission |
| **Description** | Creates a recurring journal template with cadence, posting policy, reversal rules, and line-level calculation logic. Templates are controlled finance configuration and must be auditable. |

**Request Body:**

```json
{
  "code": "RENT_ACCRUAL",
  "description": "Monthly office rent accrual",
  "cadence": "monthly",
  "approval_policy_code": "JOURNAL_THRESHOLD_STANDARD",
  "auto_reversal": true,
  "lines": [
    {
      "account_id": "acc-uuid-rent-expense",
      "entry_type": "debit",
      "amount_mode": "fixed",
      "amount_value": 2500000.00
    },
    {
      "account_id": "acc-uuid-accruals",
      "entry_type": "credit",
      "amount_mode": "fixed",
      "amount_value": 2500000.00
    }
  ]
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "rjt-uuid-0004",
    "code": "RENT_ACCRUAL",
    "status": "active",
    "cadence": "monthly",
    "next_run_date": "2026-05-01"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 409 `CONFLICT` (template code already exists), 422 `UNPROCESSABLE_ENTITY` (template lines are unbalanced or invalid).

---

## POST /api/v1/accounting/recurring-journal-templates/{id}/generate

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/recurring-journal-templates/{id}/generate` |
| **Auth Required** | Yes - `accounting.post` permission |
| **Description** | Generates a frozen recurring-journal run for a target period. The run can then move through approval and posting without being affected by later template edits. |

**Request Body:**

```json
{
  "period_id": "prd-uuid-2026-04",
  "run_date": "2026-04-30",
  "parameters": {
    "amount_override": 2500000.00
  },
  "auto_submit_for_approval": true
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "run_id": "rjr-uuid-0021",
    "template_id": "rjt-uuid-0004",
    "status": "pending_approval",
    "total_debit": 2500000.00,
    "total_credit": 2500000.00,
    "approval_id": "apr-uuid-0901"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT` (run already exists for template and period), 422 `UNPROCESSABLE_ENTITY` (period closed, formula failure, or unbalanced result).

---

## POST /api/v1/accounting/consolidation-runs

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/consolidation-runs` |
| **Auth Required** | Yes - `reports.consolidation.manage` permission |
| **Description** | Starts a consolidation run for a reporting group, snapshots participating entities and FX settings, and prepares the run for entity load, eliminations, and certification. |

**Request Body:**

```json
{
  "group_id": "grp-uuid-east-africa",
  "period_id": "prd-uuid-2026-03",
  "basis": "statutory",
  "rate_set_id": "fxset-uuid-2026-03",
  "include_intercompany_matching": true
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "conrun-uuid-0003",
    "status": "in_progress",
    "basis": "statutory",
    "entities_expected": 7,
    "entities_loaded": 0,
    "reporting_currency": "USD"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 409 `CONFLICT` (active run already exists for group and period), 422 `UNPROCESSABLE_ENTITY` (missing group structure, reporting currency, or FX-rate set).

---

## POST /api/v1/accounting/consolidation-runs/{id}/adjustments

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/consolidation-runs/{id}/adjustments` |
| **Auth Required** | Yes - `reports.consolidation.adjust` permission |
| **Description** | Creates a consolidation-only adjustment such as an intercompany elimination, ownership adjustment, reclass, or top-side entry. These adjustments do not post back to entity ledgers. |

**Request Body:**

```json
{
  "category": "intercompany_elimination",
  "description": "Eliminate March intercompany sales between UG and KE entities",
  "lines": [
    {
      "account_id": "acc-uuid-ic-sales",
      "entity_id": "ent-uuid-ug",
      "debit": 18500000.00,
      "credit": 0.00
    },
    {
      "account_id": "acc-uuid-ic-cogs",
      "entity_id": "ent-uuid-ke",
      "debit": 0.00,
      "credit": 18500000.00
    }
  ]
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "conadj-uuid-0012",
    "status": "pending_approval",
    "category": "intercompany_elimination",
    "approval_id": "apr-uuid-0942",
    "created_at": "2026-04-02T15:10:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 409 `CONFLICT`, 422 `UNPROCESSABLE_ENTITY` (unbalanced lines, invalid entity participation, or locked run).

---

## POST /api/v1/accounting/approvals

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/approvals` |
| **Auth Required** | Yes - `accounting.approvals.submit` permission |
| **Description** | Submits a finance document into the configured approval workflow. This endpoint is shared by manual journals, recurring-journal runs, period reopen requests, and consolidation adjustments. |

**Request Body:**

```json
{
  "document_type": "manual_journal",
  "document_id": "jnl-uuid-0042",
  "policy_code": "JOURNAL_THRESHOLD_STANDARD",
  "context": {
    "amount": 2500000.00,
    "currency": "UGX",
    "branch_id": "br-uuid-001"
  }
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "approval_id": "apr-uuid-0951",
    "document_type": "manual_journal",
    "document_id": "jnl-uuid-0042",
    "status": "pending",
    "current_step": 1
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 404 `NOT_FOUND`, 409 `CONFLICT` (document already has an active approval), 422 `UNPROCESSABLE_ENTITY` (no approval policy matched).

---

## POST /api/v1/accounting/approvals/{id}/actions

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/approvals/{id}/actions` |
| **Auth Required** | Yes - `accounting.approvals.act` permission |
| **Description** | Records an approval decision and advances, rejects, or returns the finance workflow item according to the configured policy. |

**Request Body:**

```json
{
  "action": "approve",
  "comment": "Reviewed support and threshold policy. Approved."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `action` | string | Yes | `approve`, `reject`, or `request_changes`. |
| `comment` | string | No | Approver note recorded in the immutable approval audit trail. |

**Success Response - 200 OK:**

```json
{
  "success": true,
  "data": {
    "approval_id": "apr-uuid-0951",
    "status": "approved",
    "document_status": "released",
    "acted_at": "2026-04-02T16:45:00Z"
  },
  "error": null
}
```

**Error Codes:** 403 `FORBIDDEN`, 404 `NOT_FOUND`, 409 `CONFLICT` (approval already completed), 422 `UNPROCESSABLE_ENTITY` (invalid action for current step).

---

## POST /api/v1/accounting/control-workflows/{workflow_type}/{workflow_id}/certifications

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/accounting/control-workflows/{workflow_type}/{workflow_id}/certifications` |
| **Auth Required** | Yes - `accounting.controls.certify` permission |
| **Description** | Captures finance control-workflow certification for a close run, journal batch, bank reconciliation, or consolidation run. Failed checklist items create tracked control exceptions rather than remaining as informal notes. |

**Request Body:**

```json
{
  "items": [
    {
      "code": "JOURNAL_SUPPORT_ATTACHED",
      "result": "pass",
      "comment": "All support uploaded to the journal packet."
    },
    {
      "code": "THRESHOLD_REVIEW_COMPLETE",
      "result": "pass",
      "comment": "Controller review complete."
    }
  ],
  "certifier_note": "Finance control gate satisfied."
}
```

**Success Response - 201 Created:**

```json
{
  "success": true,
  "data": {
    "certification_id": "fcc-uuid-0104",
    "workflow_type": "close_run",
    "workflow_id": "close-uuid-0001",
    "status": "passed",
    "exceptions_created": 0
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 403 `FORBIDDEN`, 404 `NOT_FOUND`, 422 `UNPROCESSABLE_ENTITY` (invalid workflow type or incomplete checklist).
