# Stored Procedures Specification

Stored procedures in Longhorn ERP encapsulate business logic that must be atomic and consistent across multiple tables. All procedures are defined with `DEFINER = 'app_user'@'localhost'` and use `SQL SECURITY DEFINER`. Callers must supply validated, typed parameters; no raw string assembly occurs inside any procedure body.

## `sp_post_invoice_to_gl(invoice_id BIGINT UNSIGNED)`

### Purpose

Generates and posts a double-entry General Ledger (GL) journal for a sales invoice. This procedure is the authoritative mechanism for converting a posted sales invoice into GL entries; no other code path is permitted to write accounting entries for sales invoices.

### Input Parameters

| Parameter | Type | Description |
|---|---|---|
| `invoice_id` | BIGINT UNSIGNED | Primary key of the invoice to be posted. The invoice status must be `posted` before this procedure is called. |

### Output

No result set is returned. On success, the procedure inserts one `gl_journal_entries` row and two or more `gl_journal_lines` rows, and updates the corresponding `account_ledgers` balances. The `invoice` status is not modified by this procedure; status transitions are managed by the application service layer before calling the procedure.

### Business Logic Summary

1. Read the invoice header to obtain `tenant_id`, `invoice_date`, `subtotal`, `tax_amount`, and `total`.
2. Call `sp_generate_entry_number(tenant_id, 'SALES')` to obtain a unique journal entry number.
3. Insert one `gl_journal_entries` row with status `posted`.
4. For each `invoice_items` line:
   a. Call `sp_get_account_mapping(tenant_id, 'SALES_INVOICE', item_id, category_id)` to resolve the debit (Accounts Receivable) and credit (Revenue or inventory-specific income) accounts.
   b. Insert a debit line to the Accounts Receivable account for `line_total`.
   c. Insert a credit line to the Revenue account for `line_total`.
5. If `tax_amount` > 0, insert a debit line to the Accounts Receivable account and a credit line to the VAT Payable account for the total tax amount.
6. Update `account_ledgers` balances for each affected account.
7. Commit the transaction.

### Error Conditions

| Condition | Behaviour |
|---|---|
| Invoice not found | Procedure raises SQLSTATE `45000` with message `"Invoice not found"`. |
| Invoice status is not `posted` | Procedure raises SQLSTATE `45000` with message `"Invoice must be in posted status before GL posting"`. |
| Account mapping not resolved for any line | Procedure raises SQLSTATE `45000` with message `"Account mapping missing for event SALES_INVOICE"`. Entire transaction is rolled back. |
| Debit total ≠ credit total on completion | Procedure raises SQLSTATE `45000` with message `"Journal does not balance"`. Entire transaction is rolled back. |

---

## `sp_post_purchase_to_gl(purchase_invoice_id BIGINT UNSIGNED)`

### Purpose

Generates and posts a GL journal for a supplier purchase invoice. Called after the purchase invoice passes three-way matching verification and is approved for payment.

### Input Parameters

| Parameter | Type | Description |
|---|---|---|
| `purchase_invoice_id` | BIGINT UNSIGNED | Primary key of the `purchase_invoices` record to be posted. |

### Output

No result set is returned. On success, one `gl_journal_entries` row and two or more `gl_journal_lines` rows are inserted, and `account_ledgers` balances are updated.

### Business Logic Summary

1. Read the purchase invoice to obtain `tenant_id`, `supplier_id`, `invoice_date`, and `total`.
2. Call `sp_generate_entry_number(tenant_id, 'PURCHASE')` for the journal entry number.
3. Insert one `gl_journal_entries` row with status `posted`.
4. For each item line on the linked Goods Receipt Note (GRN):
   a. Call `sp_get_account_mapping(tenant_id, 'PURCHASE_INVOICE', item_id, category_id)` to resolve the debit (Inventory or Expense account) and credit (Accounts Payable) accounts.
   b. Insert a debit line to the Inventory or Expense account for the line cost.
   c. Insert a credit line to the Accounts Payable account for the line cost.
5. If Withholding Tax (WHT) is applicable (supplier `wht_applicable = 1`), insert an additional debit to Accounts Payable and credit to WHT Payable for the computed WHT amount.
6. Update `account_ledgers` balances.
7. Commit the transaction.

### Error Conditions

| Condition | Behaviour |
|---|---|
| Purchase invoice not found | Raises SQLSTATE `45000`: `"Purchase invoice not found"`. |
| Purchase invoice not in `approved` status | Raises SQLSTATE `45000`: `"Purchase invoice must be approved before GL posting"`. |
| Account mapping missing | Raises SQLSTATE `45000`: `"Account mapping missing for event PURCHASE_INVOICE"`. Transaction rolled back. |
| Journal does not balance | Raises SQLSTATE `45000`: `"Journal does not balance"`. Transaction rolled back. |

---

## `sp_post_return_to_gl(return_id BIGINT UNSIGNED)`

### Purpose

Generates and posts a GL journal for either a sales return (credit note) or a purchase return, reversing the original income and inventory entries.

### Input Parameters

| Parameter | Type | Description |
|---|---|---|
| `return_id` | BIGINT UNSIGNED | Primary key of the return document. The procedure reads the `return_type` field of the referenced record to determine whether to apply sales-return or purchase-return logic. |

### Output

No result set is returned. On success, reversal GL journal entries are inserted and balances updated.

### Business Logic Summary

1. Determine return type (`SALES_RETURN` or `PURCHASE_RETURN`) by reading the return record.
2. Retrieve the original invoice or purchase invoice that the return references.
3. Call `sp_generate_entry_number(tenant_id, 'RETURN')`.
4. Insert a `gl_journal_entries` row with description referencing the original entry number.
5. For each returned item line, mirror the original journal lines with debits and credits swapped.
6. For `SALES_RETURN`: debit Revenue, credit Accounts Receivable. For `PURCHASE_RETURN`: debit Accounts Payable, credit Inventory or Expense.
7. Repost inventory movement via an `RETURN_IN` or `RETURN_OUT` movement type in `stock_ledger` and update `stock_balance`.
8. Commit the transaction.

### Error Conditions

| Condition | Behaviour |
|---|---|
| Return record not found | Raises SQLSTATE `45000`: `"Return document not found"`. |
| Original document already reversed | Raises SQLSTATE `45000`: `"Original document has already been reversed"`. |
| Account mapping missing | Raises SQLSTATE `45000` with mapping details. Transaction rolled back. |

---

## `sp_generate_entry_number(tenant_id BIGINT UNSIGNED, type VARCHAR(20))`

### Purpose

Generates a thread-safe, sequential document reference number for a given tenant and document type. Uses `SELECT ... FOR UPDATE` to prevent duplicate numbers under concurrent load.

### Input Parameters

| Parameter | Type | Description |
|---|---|---|
| `tenant_id` | BIGINT UNSIGNED | The tenant for whom the number is generated. |
| `type` | VARCHAR(20) | Document type code (e.g., `SALES`, `PURCHASE`, `JE`, `GRN`, `LPO`, `RETURN`). |

### Output

Returns a single VARCHAR value: the formatted entry number (e.g., `INV-2026-000042`). The format is `<prefix>-<YYYY>-<6-digit-padded-sequence>`.

### Business Logic Summary

1. Lock the sequence row for `(tenant_id, type, current_year)` using `SELECT ... FOR UPDATE`.
2. If no row exists for this combination, insert a new row with `last_sequence = 1`.
3. Otherwise, increment `last_sequence` by 1 and update the row.
4. Format and return the number as `<type_prefix>-<year>-LPAD(last_sequence, 6, '0')`.

### Error Conditions

| Condition | Behaviour |
|---|---|
| Deadlock detected | MySQL will automatically retry. The caller's outer transaction handles the rolled-back state and may retry. |

---

## `sp_get_account_mapping(tenant_id BIGINT UNSIGNED, event_type VARCHAR(50), item_id BIGINT UNSIGNED, category_id BIGINT UNSIGNED)`

### Purpose

Resolves the debit and credit GL accounts for a given business event using the 3-level hierarchy in `account_mappings`. Returns the most specific match: item-level if it exists, otherwise category-level, otherwise the DEFAULT for the event type.

### Input Parameters

| Parameter | Type | Description |
|---|---|---|
| `tenant_id` | BIGINT UNSIGNED | Tenant scope. |
| `event_type` | VARCHAR(50) | Business event code (e.g., `SALES_INVOICE`, `STOCK_ISSUE`). |
| `item_id` | BIGINT UNSIGNED | The specific item ID; pass 0 or NULL to skip item-level lookup. |
| `category_id` | BIGINT UNSIGNED | The item's category ID; pass 0 or NULL to skip category-level lookup. |

### Output

Returns a single-row result set with columns:

| Column | Type | Description |
|---|---|---|
| `debit_account_id` | BIGINT UNSIGNED | Resolved debit account. |
| `credit_account_id` | BIGINT UNSIGNED | Resolved credit account. |
| `mapping_level` | ENUM('ITEM','CATEGORY','DEFAULT') | The resolution level that was applied. |

### Business Logic Summary

1. Attempt item-level lookup: `WHERE tenant_id = ? AND event_type = ? AND item_id = ? AND level = 'ITEM'`.
2. If no row found, attempt category-level lookup: `WHERE tenant_id = ? AND event_type = ? AND category_id = ? AND level = 'CATEGORY'`.
3. If no row found, attempt default lookup: `WHERE tenant_id = ? AND event_type = ? AND level = 'DEFAULT'`.
4. Return the first matching row's `debit_account_id`, `credit_account_id`, and `mapping_level`.

### Error Conditions

| Condition | Behaviour |
|---|---|
| No mapping found at any level | Returns an empty result set. The calling procedure must handle this and raise its own error. |
