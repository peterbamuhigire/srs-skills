## Section 6 — Finance Endpoints

These endpoints serve the Executive Dashboard App and the web Finance module. Financial data is dual-mode: PIBID parliamentary accounting and BIRDC commercial IFRS accounts are available from the same system simultaneously (DC-004). All financial endpoints enforce 7-year read retention; no data is deleted.

---

### 6.1 GET /finance/gl/trial-balance

**Description:** Retrieve a Trial Balance summary as of a specified date. Supports dual-mode output: `commercial` (IFRS) or `parliamentary` (PIBID budget votes) or `both`.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `FINANCE_MANAGER`

**Query parameters:**

| Parameter | Type | Description |
|---|---|---|
| `as_of_date` | `string` | ISO 8601 date — balance as of this date |
| `mode` | `string` | `commercial`, `parliamentary`, or `both` (default: `both`) |
| `level` | `integer` | Account hierarchy depth (1 = top-level only, 3 = full detail) |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `as_of_date` | `string` | Reference date |
| `mode` | `string` | Reporting mode applied |
| `accounts` | `array` | Account list |
| `accounts[].account_code` | `string` | Chart of accounts code |
| `accounts[].account_name` | `string` | Account name |
| `accounts[].account_type` | `string` | `asset`, `liability`, `equity`, `revenue`, `expense` |
| `accounts[].debit_balance` | `number` | Total debits (UGX) |
| `accounts[].credit_balance` | `number` | Total credits (UGX) |
| `accounts[].net_balance` | `number` | Net balance |
| `totals` | `object` | Total debits, total credits, balance check (must be zero) |

---

### 6.2 GET /finance/accounts/{account_id}/balance

**Description:** Retrieve the balance of a specific General Ledger account, with drill-down to journal entry lines.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_DIRECTOR`, `FINANCE_MANAGER`

**Query parameters:** `date_from`, `date_to`, `include_transactions` (boolean, default: `false`).

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `account_id` | `integer` | Account primary key |
| `account_code` | `string` | Chart of accounts code |
| `account_name` | `string` | Account name |
| `opening_balance` | `number` | Balance at `date_from` |
| `total_debits` | `number` | Debits in period |
| `total_credits` | `number` | Credits in period |
| `closing_balance` | `number` | Balance at `date_to` |
| `transactions` | `array\|null` | Journal lines (included if `include_transactions=true`) |

---

### 6.3 GET /finance/budget-vs-actual

**Description:** Retrieve budget versus actual expenditure comparison for a specified period and mode. Used by Executive Dashboard App for variance alerts (BR-014).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `FINANCE_MANAGER`

**Query parameters:** `period` (ISO 8601 date — fiscal period), `mode` (`commercial`, `parliamentary`), `department_id` (optional), `vote_code` (optional — parliamentary mode only).

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `period` | `string` | Reporting period |
| `mode` | `string` | Accounting mode |
| `lines` | `array` | Budget vs actual per account/vote |
| `lines[].account_code` | `string` | Account or vote code |
| `lines[].budget_amount` | `number` | Approved budget (UGX) |
| `lines[].actual_amount` | `number` | Actual expenditure to date |
| `lines[].variance_amount` | `number` | Budget minus actual |
| `lines[].variance_pct` | `number` | Variance as percentage of budget |
| `lines[].alert_level` | `string` | `none`, `warning` (≥ 80%), `critical` (≥ 95%) |

---

### 6.4 GET /finance/cash-position

**Description:** Retrieve BIRDC's current cash and bank position — bank account balances and petty cash imprest balances. Used by Executive Dashboard App.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `FINANCE_MANAGER`

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `bank_accounts` | `array` | Bank account balances |
| `bank_accounts[].account_name` | `string` | Bank account name |
| `bank_accounts[].bank_name` | `string` | Bank name |
| `bank_accounts[].balance` | `number` | Current balance (UGX) |
| `bank_accounts[].last_reconciled` | `string` | Date of last bank reconciliation |
| `imprest_accounts` | `array` | Petty cash float balances |
| `imprest_accounts[].name` | `string` | Imprest account name |
| `imprest_accounts[].balance` | `number` | Current balance (UGX) |
| `total_cash_position` | `number` | Combined bank + imprest balance |
| `calculated_at` | `string` | ISO 8601 datetime |

---

### 6.5 GET /finance/statements/profit-loss

**Description:** Retrieve the Profit and Loss (Income) Statement for a specified period and mode.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `FINANCE_MANAGER`

**Query parameters:** `period_from`, `period_to`, `mode` (`commercial`, `parliamentary`, `both`), `comparative` (boolean — include prior period).

**Response schema (200 OK):** Structured P&L with `revenue_lines[]`, `cost_of_sales_lines[]`, `gross_profit`, `operating_expense_lines[]`, `operating_profit`, `other_income_lines[]`, `other_expense_lines[]`, `net_profit`. All in UGX.

---

### 6.6 GET /finance/statements/balance-sheet

**Description:** Retrieve the Balance Sheet as of a specified date.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`

**Query parameters:** `as_of_date`, `mode` (`commercial`, `parliamentary`, `both`).

**Response schema (200 OK):** Structured balance sheet with `assets[]` (current and non-current), `liabilities[]` (current and non-current), `equity[]`, and balance check (`total_assets = total_liabilities + total_equity`).

---

### 6.7 GET /finance/statements/cash-flow

**Description:** Retrieve the Cash Flow Statement (IAS 7 indirect method) for a specified period.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`

**Query parameters:** `period_from`, `period_to`.

**Response schema (200 OK):** IAS 7 structured cash flow with `operating_activities`, `investing_activities`, `financing_activities`, `net_change_in_cash`, `opening_cash`, `closing_cash`.

---

### 6.8 POST /finance/journals

**Description:** Create a manual journal entry. Auto-generated operational journals (from invoices, POS, inventory adjustments) are created by the system — this endpoint is for correction entries only. Enforces balanced debit/credit (zero net) before acceptance.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_MANAGER` (creator), `FINANCE_DIRECTOR` (approver — see BR-003)

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `journal_date` | `string` | Required, ISO 8601 date | Entry date |
| `description` | `string` | Required, min 10 | Journal description |
| `lines` | `array` | Required, min 2 | Journal lines |
| `lines[].account_id` | `integer` | Required | GL account |
| `lines[].debit` | `number` | Optional, ≥ 0 | Debit amount |
| `lines[].credit` | `number` | Optional, ≥ 0 | Credit amount |
| `lines[].description` | `string` | Optional | Line description |
| `mode` | `string` | Required | `commercial` or `parliamentary` |
| `parliamentary_vote_code` | `string` | Conditional | Required if `mode = parliamentary` |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `journal_id` | `integer` | Journal primary key |
| `journal_number` | `string` | Sequential JE number (JE-YYYY-NNNN) |
| `status` | `string` | `"draft"` |
| `hash` | `string` | Cryptographic hash of this entry (BR-013) |

---

### 6.9 GET /finance/gl/hash-chain/verify

**Description:** Run a hash chain integrity check across the entire GL or a specified account. Returns any broken links — evidence of tampering per BR-013.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_DIRECTOR`, `IT_ADMIN`

**Query parameters:** `account_id` (optional — check specific account only), `date_from`, `date_to`.

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `chain_status` | `string` | `"intact"` or `"broken"` |
| `entries_checked` | `integer` | Total GL entries verified |
| `broken_links` | `array` | List of broken links with `journal_id`, `expected_hash`, `actual_hash` |
| `verified_at` | `string` | ISO 8601 datetime of verification run |

---

### 6.10 GET /finance/accounts

**Description:** Retrieve the full chart of accounts. Supports hierarchical display and filtering by type.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_DIRECTOR`, `FINANCE_MANAGER`, `IT_ADMIN`

**Query parameters:** `type` (`asset`, `liability`, `equity`, `revenue`, `expense`), `mode` (`commercial`, `parliamentary`, `both`), `active_only` (boolean, default: `true`).

**Response schema (200 OK):** Hierarchical account list with `account_id`, `account_code`, `account_name`, `parent_account_id`, `type`, `mode`, `parliamentary_segment`, `is_active`.

---
