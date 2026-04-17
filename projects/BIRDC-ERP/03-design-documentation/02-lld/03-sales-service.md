# 3. SalesService

**Namespace:** `App\Services\Sales\SalesService`
**Dependencies:** `InvoiceRepository`, `CustomerRepository`, `GLService`, `EFRISService`, `InventoryService`, `AuditLogService`, `NotificationService`
**Test coverage required:** ≥ 80%

## 3.1 Method Signatures

```php
final class SalesService
{
    /**
     * Create a new sales invoice in DRAFT status.
     *
     * @param array $data {
     *   customer_id: int,
     *   price_list_id: int,
     *   territory_id: int,
     *   lines: [{product_id: int, quantity: float, unit_price: Money, discount_pct: float}],
     *   notes: string|null,
     *   due_date: DateString|null,
     *   idempotency_key: Uuid,     // Prevents duplicate invoices on retry
     * }
     *
     * @return Invoice  The created invoice DTO in DRAFT status.
     *
     * @throws CustomerNotFoundException     If customer_id does not exist.
     * @throws ProductNotFoundException      If any product_id in lines does not exist.
     * @throws CreditLimitExceededException  If customer's credit limit would be breached.
     * @throws DuplicateRequestException     If idempotency_key was already processed.
     *
     * Business rules:
     *   - Invoice number NOT assigned at draft stage — assigned on confirmation (BR-009).
     *   - Credit limit check: CustomerCreditBalance + InvoiceTotal ≤ customer.credit_limit.
     *   - Status lifecycle: DRAFT → PENDING_EFRIS → ISSUED.
     */
    public function createInvoice(array $data): Invoice;

    /**
     * Confirm a DRAFT invoice: assign sequential invoice number, post GL entries,
     * and submit to URA EFRIS.
     *
     * @param int $invoiceId
     *
     * @return void
     *
     * @throws InvoiceNotFoundException       If invoiceId does not exist.
     * @throws InvalidInvoiceStatusException  If invoice is not in DRAFT status.
     * @throws InsufficientStockException     If any line item has insufficient warehouse stock.
     * @throws GLPostingException             If the GL journal fails to balance.
     *
     * Business rules:
     *   - Assigns sequential invoice number (BR-009): triggers trg_invoice_number_seq.
     *   - Reduces warehouse stock via InventoryService::recordMovement(SALE).
     *   - FEFO batch allocation enforced (BR-007).
     *   - GL auto-post: DR Accounts Receivable / CR Revenue; DR COGS / CR Inventory.
     *   - EFRIS submission via EFRISService::submitDocument() — status set to
     *     PENDING_EFRIS; updated to ISSUED on FDN receipt.
     *   - Sends daily sales summary push notification via NotificationService.
     */
    public function confirmInvoice(int $invoiceId): void;

    /**
     * Void a confirmed invoice.
     *
     * A voided invoice retains its number (BR-009) and is permanently marked VOID.
     * A credit note is automatically generated if the invoice had payments allocated.
     *
     * @param int    $invoiceId
     * @param string $reason    Mandatory void reason (logged to audit trail).
     *
     * @return void
     *
     * @throws InvoiceNotFoundException       If invoiceId does not exist.
     * @throws InvalidInvoiceStatusException  If invoice is already VOID or PAID.
     * @throws PermissionException            If current user did not create the invoice
     *                                        AND is not Finance Manager (SoD check L7).
     *
     * Business rules:
     *   - GL reversal posted: DR Revenue / CR Accounts Receivable; DR Inventory / CR COGS.
     *   - EFRIS credit note submitted via EFRISService.
     *   - Invoice status set to VOID; void reason and actor stored.
     *   - Number is never recycled (BR-009).
     */
    public function voidInvoice(int $invoiceId, string $reason): void;

    /**
     * Calculate the Cost of Goods Sold for a confirmed invoice using FIFO/moving average.
     *
     * @param int $invoiceId
     *
     * @return Money  Total COGS in UGX for all lines on the invoice.
     *
     * @throws InvoiceNotFoundException  If invoiceId does not exist.
     *
     * Business rules:
     *   - Uses the FIFO/moving average cost of the specific batches allocated
     *     to this invoice at confirmation time (from tbl_inventory_movements).
     *   - Returns the sum of (batch_cost_per_unit × quantity) across all lines.
     */
    public function calculateCOGS(int $invoiceId): Money;
}
```
