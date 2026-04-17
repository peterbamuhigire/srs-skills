# Inventory and Sales Module Test Cases

This section covers the immutable stock ledger, costing methods (FIFO and Weighted Average Cost), and the full sales invoice workflow including credit notes and partial payment allocation.

## Stock Ledger Immutability

The `stock_ledger` table records every inventory movement as an append-only row. The view `v_current_stock` aggregates the current balance from ledger rows. No UPDATE or DELETE operation may alter a committed ledger row.

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-INV-001 | `StockLedgerTest` | `test_post_grn_increases_stock_balance` | Post a Goods Received Note (GRN) for 50 units | Valid GRN payload; item ID; warehouse ID; quantity = 50 | `stock_ledger` gains exactly 1 new row with `quantity` = 50; `v_current_stock` balance for that item/warehouse increases by 50 |
| TC-INV-002 | `StockLedgerTest` | `test_update_or_delete_stock_ledger_row_is_rejected` | Attempt to UPDATE or DELETE a committed `stock_ledger` row | Raw SQL: `UPDATE stock_ledger SET quantity = 0 WHERE id = ?` and separately `DELETE FROM stock_ledger WHERE id = ?` | Both operations rejected by DB trigger; original row unchanged; trigger fires and raises error |
| TC-INV-003 | `StockLedgerTest` | `test_negative_stock_sale_blocked_when_config_disallows` | Sale quantity exceeds available stock when `allow_negative_stock` = `false` | Sale line: quantity = 100; `v_current_stock` balance = 30; config `allow_negative_stock` = `false` | HTTP 422; `error_code` = `INSUFFICIENT_STOCK`; no ledger row written |

## Costing Methods — FIFO and Weighted Average Cost (WAC)

### FIFO (First-In, First-Out)

The Cost of Goods Sold (COGS) calculation consumes the oldest batch first until the sold quantity is satisfied.

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-INV-004 | `FifoCostingTest` | `test_fifo_cogs_uses_oldest_batch_first` | Sell 10 units across 3 batches: Batch 1 (4 units @ UGX 1,000), Batch 2 (3 units @ UGX 1,100), Batch 3 (5 units @ UGX 1,200); sell 10 | Sale quantity = 10 | COGS = (4 × 1,000) + (3 × 1,100) + (3 × 1,200) = 4,000 + 3,300 + 3,600 = UGX 10,900; Batch 1 fully consumed; Batch 2 fully consumed; Batch 3 has 2 units remaining |

### Weighted Average Cost (WAC)

The WAC formula is: $WAC = \frac{\sum(Quantity_i \times Cost_i)}{\sum Quantity_i}$

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-INV-005 | `WacCostingTest` | `test_wac_recalculated_after_second_grn` | GRN 1: 100 units @ UGX 1,000; GRN 2: 50 units @ UGX 1,200 | Two sequential GRNs for same item | $WAC = \frac{(100 \times 1000) + (50 \times 1200)}{150} = \frac{160000}{150} = 1066$ UGX (integer, rounded down); system stores WAC as integer in UGX |

## Sales Invoice Workflow

### Full Lifecycle

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-SALES-001 | `SalesWorkflowTest` | `test_full_sales_lifecycle_statuses_correct` | Quotation → Order → Invoice → Payment | Step 1: create Quotation; Step 2: convert to Order; Step 3: convert to Invoice; Step 4: record full payment | Statuses at each step: Quotation = `DRAFT`; Order = `CONFIRMED`; Invoice = `POSTED`; after payment = `PAID`; stock ledger row written at invoice post; GL entries posted at each relevant step |

### Credit Note

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-SALES-002 | `CreditNoteTest` | `test_credit_note_reverses_stock_and_gl` | Create credit note against a posted invoice | Posted `invoice_id`; valid authorisation with `invoices.credit_note` permission | Stock ledger gains reversal row (quantity positive, direction = IN); GL reversal entries posted (AR credited, Revenue debited, VAT Input debited); credit note `status` = `POSTED` |

### Partial Payment Allocation

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-SALES-003 | `PaymentAllocationTest` | `test_partial_payment_leaves_correct_outstanding_balance` | Allocate UGX 500,000 payment against a UGX 1,000,000 invoice | `invoice_id` with total = 1,000,000 UGX; payment amount = 500,000 UGX | Invoice `amount_paid` = 500,000; `amount_outstanding` = 500,000; invoice `status` = `PARTIALLY_PAID`; GL: DR Bank 500,000, CR AR 500,000 |
