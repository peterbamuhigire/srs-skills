# Sales and Procurement Modules — Low-Level Design

## Overview

Sales and Procurement share a symmetric document flow: Sales progresses from Quotation → Sales Order → Sales Invoice → Receipt; Procurement progresses from Requisition → LPO → GRN → Supplier Invoice → Supplier Payment. Both flows post to the GL through stored procedures. Three-way matching in Procurement links the LPO, GRN, and Supplier Invoice before payment is released.

---

## CustomerService

**Namespace:** `App\Modules\Sales`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createCustomer(array $data): int` | Associative array of customer attributes (`name`, `tin`, `email`, `phone`, `credit_limit`, `payment_terms_days`, etc.) | New `customers.id` | Validates TIN uniqueness per tenant. Inserts one row into `customers`. Logs to `AuditService`. |
| `getCreditLimit(int $customerId): array` | Customer primary key | `['limit' => float, 'used' => float, 'available' => float]` | Reads `customers.credit_limit`. Calculates `used` as the sum of `invoices.balance_due WHERE customer_id = :customerId AND status = 'posted'`. |
| `getAgingReport(int $customerId): array` | Customer primary key | Array of aging buckets (`current`, `1–30`, `31–60`, `61–90`, `90+`) | Queries `v_customer_aging` filtered by `customer_id` and `tenant_id`. |

**Views read:** `v_customer_aging`

**Tables read/written:** `customers`

---

## QuotationService

**Namespace:** `App\Modules\Sales`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `TaxService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createQuotation(int $customerId, array $lines, ?string $expiryDate = null): int` | Customer primary key, array of `['item_id', 'qty', 'unit_price', 'tax_code']` entries, optional ISO 8601 expiry date | New `quotations.id` | Calculates line totals via `TaxService::calculateVAT()`. Inserts `quotations` header and `quotation_lines`. Status is `draft`. |
| `convertToOrder(int $quotationId): int` | Quotation primary key | New `sales_orders.id` | Copies header and line data from `quotations` to `sales_orders`. Sets `quotations.status = 'converted'`. Delegates to `SalesOrderService::createOrder()` with pre-populated data. |

**Tables read/written:** `quotations`, `quotation_lines`

---

## SalesOrderService

**Namespace:** `App\Modules\Sales`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `ItemService`, `StockLedgerService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createOrder(int $customerId, array $lines): int` | Customer primary key, array of `['item_id', 'qty', 'unit_price', 'tax_code']` entries | New `sales_orders.id` | Checks credit availability via `CustomerService::getCreditLimit()`. Inserts `sales_orders` header and `sales_order_lines`. Status is `confirmed`. |
| `allocateStock(int $orderId): void` | Sales order primary key | `void` | For each order line, reserves stock by inserting rows into `stock_reservations`. Throws `InsufficientStockException` if the available balance (on-hand minus existing reservations) is insufficient. |
| `fulfillOrder(int $orderId): int` | Sales order primary key | New `delivery_notes.id` | Releases reservations. Posts `SALE` movements via `StockLedgerService::postMovement()` for each line. Inserts a `delivery_notes` row and sets `sales_orders.status = 'fulfilled'`. |

**Tables read/written:** `sales_orders`, `sales_order_lines`, `stock_reservations`, `delivery_notes`

---

## SalesInvoiceService

**Namespace:** `App\Modules\Sales`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `TaxService`, `InvoiceService`, `EFRISService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createInvoice(int $orderId): int` | Sales order primary key | New `invoices.id` | Copies lines from the fulfilled sales order. Calculates taxes via `TaxService::calculateVAT()`. Inserts `invoices` and `invoice_lines` with status `draft`. |
| `postToGL(int $invoiceId): void` | Invoice primary key | `void` | Delegates to `InvoiceService::postInvoiceToGL(int $invoiceId)`, which calls `sp_post_invoice_to_gl`. |
| `submitToEFRIS(int $invoiceId): string` | Invoice primary key | EFRIS fiscal document number | [CONTEXT-GAP: GAP-001] Calls `EFRISService::submitInvoice()` with the invoice payload. Stores the returned fiscal document number in `invoices.efris_fiscal_doc_number`. |

**Tables read/written:** `invoices`, `invoice_lines`

**Stored procedures called (via InvoiceService):** `sp_post_invoice_to_gl`

---

## ReceiptService

**Namespace:** `App\Modules\Sales`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `PaymentService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createReceipt(int $customerId, float $amount, string $paymentMethod, ?string $reference = null): int` | Customer primary key, amount received, payment method code (`CASH`, `BANK`, `MOMO`), optional external reference | New `receipts.id` | Inserts a row into `receipts`. Posts a debit to the cash/bank GL account and a credit to the accounts-receivable control account via `AccountingService::postJournal()`. |
| `allocateToInvoice(int $receiptId, int $invoiceId, float $amount): void` | Receipt primary key, invoice primary key, allocation amount | `void` | Delegates to `PaymentService::allocatePayment()`. |

**Tables read/written:** `receipts`

---

## SupplierService

**Namespace:** `App\Modules\Procurement`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createSupplier(array $data): int` | Associative array of supplier attributes (`name`, `tin`, `email`, `phone`, `payment_terms_days`, `wht_applicable`, etc.) | New `suppliers.id` | Validates TIN uniqueness per tenant. Inserts one row into `suppliers`. Logs to `AuditService`. |
| `getAgingReport(int $supplierId): array` | Supplier primary key | Array of aging buckets (`current`, `1–30`, `31–60`, `61–90`, `90+`) | Queries `v_supplier_aging` filtered by `supplier_id` and `tenant_id`. |

**Views read:** `v_supplier_aging`

**Tables read/written:** `suppliers`

---

## RequisitionService

**Namespace:** `App\Modules\Procurement`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createRequisition(array $lines, string $justification): int` | Array of `['item_id', 'qty', 'estimated_unit_cost']` entries, free-text justification | New `requisitions.id` | Inserts `requisitions` header (status `pending`) and `requisition_lines`. |
| `approveRequisition(int $requisitionId): void` | Requisition primary key | `void` | Verifies the approving user holds the `APPROVE_REQUISITION` permission. Sets `requisitions.status = 'approved'` and records `approved_by` and `approved_at`. Logs to `AuditService`. |

**Tables read/written:** `requisitions`, `requisition_lines`

---

## LPOService

**Namespace:** `App\Modules\Procurement`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createLPO(int $supplierId, int $requisitionId, array $lines): int` | Supplier primary key, approved requisition primary key, array of `['item_id', 'qty', 'unit_price', 'tax_code']` entries | New `lpos.id` | Validates that the requisition status is `approved`. Inserts `lpos` header and `lpo_lines`. Status is `draft`. |
| `approveLPO(int $lpoId): void` | LPO primary key | `void` | Verifies the approving user holds the `APPROVE_LPO` permission. Sets `lpos.status = 'approved'` and records approval metadata. |
| `matchGRN(int $lpoId, int $grnId, int $supplierInvoiceId): array` | LPO primary key, GRN primary key, supplier invoice primary key | Array of match result rows with `['item_id', 'lpo_qty', 'grn_qty', 'invoice_qty', 'match_status']` | **Three-way matching logic:** For each line, compares `lpo_lines.qty` vs `grn_lines.qty_received` vs `supplier_invoice_lines.qty`. Sets `match_status` to `MATCHED` if all three quantities agree within the configured tolerance (default 0%). Sets `match_status` to `VARIANCE` if any discrepancy exceeds tolerance. Matching results are stored in `three_way_match_results`. Payment release requires all lines to carry `MATCHED` status unless a variance override is recorded. |

**Tables read/written:** `lpos`, `lpo_lines`, `three_way_match_results`

---

## SupplierInvoiceService

**Namespace:** `App\Modules\Procurement`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `TaxService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createSupplierInvoice(int $supplierId, int $grnId, array $lines): int` | Supplier primary key, GRN primary key, array of `['item_id', 'qty', 'unit_price', 'tax_code']` entries | New `supplier_invoices.id` | Inserts `supplier_invoices` header and `supplier_invoice_lines`. Calculates input VAT via `TaxService::calculateVAT()`. Status is `draft`. |
| `postToGL(int $supplierInvoiceId): void` | Supplier invoice primary key | `void` | Calls `CALL sp_post_purchase_to_gl(:supplier_invoice_id, :tenant_id)`. Sets `supplier_invoices.status = 'posted'`. Calls `AuditService::log()` inside the same transaction. |

**Tables read/written:** `supplier_invoices`, `supplier_invoice_lines`

**Stored procedures called:** `sp_post_purchase_to_gl`

---

## SupplierPaymentService

**Namespace:** `App\Modules\Procurement`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `TaxService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createPayment(int $supplierId, float $grossAmount, int $supplierInvoiceId, string $paymentMethod): int` | Supplier primary key, gross payment amount, supplier invoice primary key, payment method code | New `supplier_payments.id` | Calls `TaxService::calculateWHT()` if the supplier is flagged `wht_applicable`. Posts a debit to accounts-payable and a credit to the bank/cash account via `AccountingService::postJournal()`. WHT amount is posted to the WHT payable account. Inserts a `supplier_payments` row. |
| `deductWHT(int $paymentId): float` | Supplier payment primary key | WHT amount deducted | Returns `supplier_payments.wht_amount` for the given payment. Used by reporting services to reconcile WHT certificates. |

**Tables read/written:** `supplier_payments`
