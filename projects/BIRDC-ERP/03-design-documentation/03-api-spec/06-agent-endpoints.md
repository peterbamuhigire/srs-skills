## Section 5 — Agent Management Endpoints

These endpoints serve the Sales Agent App, giving agents access to their own profile, stock, remittances, and commission statements. Sales Managers and Finance Managers can access all agents.

---

### 5.1 GET /agents/{agent_id}/profile

**Description:** Retrieve the full profile of a sales agent including territory, float limit, commission rate, and account status.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own profile only), `SALES_MANAGER`, `FINANCE_MANAGER`, `DIRECTOR`

**Path parameters:** `agent_id` — integer, agent primary key

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `agent_id` | `integer` | Agent primary key |
| `agent_number` | `string` | Agent code |
| `full_name` | `string` | Agent full name |
| `phone` | `string` | Primary phone number |
| `mobile_money_number` | `string` | MTN MoMo or Airtel Money number for commission payments |
| `territory_id` | `integer` | Assigned territory |
| `territory_name` | `string` | Territory name |
| `float_limit` | `number` | Maximum stock value agent may hold (UGX) |
| `commission_rate` | `number` | Commission percentage (e.g., 5.00) |
| `status` | `string` | `active` or `suspended` |
| `cash_balance` | `number` | Current agent cash liability to BIRDC (UGX) |
| `stock_value` | `number` | Current agent stock value (UGX) — from `tbl_agent_stock_balance` |

---

### 5.2 GET /agents/{agent_id}/cash-balance

**Description:** Retrieve the real-time agent cash balance — total invoiced sales minus total verified remittances. This is BIRDC's live liability register per agent.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own only), `SALES_MANAGER`, `FINANCE_MANAGER`

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `agent_id` | `integer` | Agent primary key |
| `total_invoiced` | `number` | Total value of sales invoices issued to agent's customers |
| `total_remitted_verified` | `number` | Total verified remittances applied |
| `cash_balance` | `number` | Net liability: total_invoiced - total_remitted_verified |
| `outstanding_invoices` | `array` | Unpaid invoices in FIFO order (oldest first) |
| `calculated_at` | `string` | ISO 8601 datetime of calculation |

---

### 5.3 POST /agents/{agent_id}/remittances

**Description:** Submit a cash remittance from an agent. The system allocates the remittance to outstanding invoices in FIFO order via stored procedure `sp_apply_remittance_to_invoices` (BR-002). Remittance is set to `pending_verification` status until a supervisor approves it (BR-003).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own only)

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `remittance_date` | `string` | Required, ISO 8601 date | Date cash was deposited or transferred |
| `amount` | `number` | Required, > 0 | Amount remitted (UGX) |
| `payment_method` | `string` | Required | `cash_deposit`, `mtn_momo`, `airtel_money`, `bank_transfer` |
| `reference` | `string` | Optional, max 100 | Bank or mobile money reference |
| `deposit_slip_url` | `string` | Optional | URL to uploaded deposit slip image |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `remittance_id` | `integer` | Remittance primary key |
| `remittance_number` | `string` | Reference number (REM-YYYY-NNNN) |
| `status` | `string` | `"pending_verification"` |
| `message` | `string` | `"Remittance submitted. Awaiting supervisor verification."` |

---

### 5.4 GET /agents/{agent_id}/remittances

**Description:** Retrieve remittance history for an agent, including verification status and invoice allocations.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own only), `SALES_MANAGER`, `FINANCE_MANAGER`

**Query parameters:** `status` (`pending_verification`, `verified`, `rejected`), `date_from`, `date_to`.

**Response schema (200 OK):** Paginated list with `remittance_number`, `remittance_date`, `amount`, `payment_method`, `status`, `verified_by`, `verified_at`, `allocated_invoices[]`.

---

### 5.5 GET /agents/{agent_id}/commission-statement

**Description:** Retrieve the agent's commission statement for a specified period. Commission is earned only on verified remittances per BR-015.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own only), `SALES_MANAGER`, `FINANCE_MANAGER`

**Query parameters:** `period_from` (ISO 8601 date, required), `period_to` (ISO 8601 date, required).

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `agent_id` | `integer` | Agent primary key |
| `period_from` | `string` | Statement start date |
| `period_to` | `string` | Statement end date |
| `commission_lines` | `array` | Per-remittance commission detail |
| `commission_lines[].remittance_number` | `string` | Remittance reference |
| `commission_lines[].verified_date` | `string` | Date remittance was verified |
| `commission_lines[].invoiced_amount` | `number` | Invoice value cleared by remittance |
| `commission_lines[].commission_rate` | `number` | Applied commission rate (%) |
| `commission_lines[].commission_earned` | `number` | Commission earned (UGX) |
| `total_commission_earned` | `number` | Total for period (UGX) |
| `total_commission_paid` | `number` | Amount already paid |
| `commission_payable` | `number` | Outstanding commission (UGX) |

---

### 5.6 GET /agents/{agent_id}/stock-balance

**Description:** Retrieve the agent's current stock balance from `tbl_agent_stock_balance`. This is entirely separate from warehouse stock (BR-001).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own only), `SALES_MANAGER`, `WAREHOUSE_STAFF`

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `agent_id` | `integer` | Agent primary key |
| `stock_lines` | `array` | Per-product stock detail |
| `stock_lines[].stock_item_id` | `integer` | Product ID |
| `stock_lines[].item_name` | `string` | Product name |
| `stock_lines[].quantity` | `number` | Quantity held |
| `stock_lines[].unit_cost` | `number` | Cost per unit |
| `stock_lines[].total_value` | `number` | Total value (UGX) |
| `float_limit` | `number` | Agent's configured float limit |
| `total_stock_value` | `number` | Total agent stock value (UGX) |
| `float_utilisation_pct` | `number` | Percentage of float limit used |

---

### 5.7 GET /agents/performance

**Description:** Retrieve comparative agent performance across territories — revenue, remittance compliance rate, outstanding balances. Used by Sales Manager and Executive Dashboard App.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `SALES_MANAGER`

**Query parameters:** `territory_id` (optional), `period_from`, `period_to`, `sort_by` (`revenue`, `outstanding_balance`, `compliance_rate`).

**Response schema (200 OK):** Paginated agent list with `agent_name`, `territory`, `total_sales`, `total_remitted`, `outstanding_balance`, `remittance_compliance_rate`, `commission_earned`, `performance_rank`.

---

### 5.8 GET /agents

**Description:** Retrieve the paginated list of all agents. Supports search and filtering by territory, status, and outstanding balance threshold.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_MANAGER`, `FINANCE_MANAGER`, `DIRECTOR`

**Query parameters:** `search` (string), `territory_id`, `status` (`active`, `suspended`), `balance_above` (number — filter agents with outstanding cash balance above threshold).

**Response schema (200 OK):** Paginated list with core agent profile fields and current cash and stock balances.

---

### 5.9 POST /agents/{agent_id}/remittances/{remittance_id}/verify

**Description:** Verify (approve) a pending agent remittance. Triggers FIFO invoice allocation via `sp_apply_remittance_to_invoices` and posts AR receipt GL entries. Enforces BR-003 (verifier ≠ creator).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_MANAGER`, `FINANCE_MANAGER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `notes` | `string` | Optional | Verification notes |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `remittance_id` | `integer` | Remittance primary key |
| `status` | `string` | `"verified"` |
| `invoices_cleared` | `array` | Invoices fully or partially cleared |
| `journal_entry_id` | `integer` | GL entry posted |
| `commission_accrued` | `number` | Commission accrued on this remittance (UGX) |

---

### 5.10 GET /agents/{agent_id}/statement

**Description:** Retrieve a full agent statement — all invoices, remittances, and balance movements for a period.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own only), `SALES_MANAGER`, `FINANCE_MANAGER`

**Query parameters:** `date_from`, `date_to`.

**Response schema (200 OK):** Chronological statement with opening balance, all transactions, and closing balance.

---
