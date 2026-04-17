# 4. POSService

**Namespace:** `App\Services\POS\POSService`
**Dependencies:** `POSSessionRepository`, `InvoiceRepository`, `InventoryService`, `AgentService`, `GLService`, `EFRISService`, `MobileMoneyService`, `AuditLogService`
**Test coverage required:** ≥ 80%

## 4.1 Method Signatures

```php
final class POSService
{
    /**
     * Open a new POS session for a cashier.
     *
     * @param int   $cashierId     The user ID of the cashier opening the session.
     * @param Money $openingFloat  Cash amount counted and recorded at session open.
     *
     * @return Session  The opened session DTO with session_id, opened_at, and opening_float.
     *
     * @throws ActiveSessionExistsException  If cashier already has an open session.
     * @throws PermissionException           If user does not hold CASHIER or SALES_AGENT role.
     *
     * Business rules:
     *   - Only one active session per cashier at a time.
     *   - Session context determines which stock track is used:
     *       Factory gate / showroom → warehouse stock (tbl_stock_balance).
     *       Agent checkout → agent stock (tbl_agent_stock_balance).
     *   - Opening float is recorded in tbl_pos_sessions.opening_float.
     */
    public function openSession(int $cashierId, Money $openingFloat): Session;

    /**
     * Process a completed POS sale within an open session.
     *
     * @param int   $sessionId
     * @param array $cartItems  [{product_id: int, quantity: float, batch_id: int|null}]
     * @param array $payments   [{method: string, amount: Money, reference: string|null}]
     *                          Methods: 'CASH', 'MTN_MOMO', 'AIRTEL_MONEY', 'CHEQUE', 'BANK_DEPOSIT'
     *
     * @return Sale  The completed sale DTO with receipt number and payment breakdown.
     *
     * @throws SessionNotFoundException       If sessionId does not exist or is not open.
     * @throws InsufficientStockException     If any cart item has insufficient stock
     *                                        in the session's stock track.
     * @throws PaymentMismatchException       If sum of payments ≠ sale total.
     * @throws EFRISSubmissionException       Non-fatal: sale is completed but EFRIS
     *                                        submission is queued for retry.
     *
     * Business rules:
     *   - FEFO batch selection enforced (BR-007) unless batch_id is explicitly specified.
     *   - For factory gate / showroom context: decrements tbl_stock_balance.
     *   - For agent context: see agentProcessSale() — uses agent stock.
     *   - GL auto-post: DR Cash / CR Revenue; DR COGS / CR Inventory.
     *   - EFRIS submission triggered immediately; failure queues retry (non-blocking).
     *   - Receipt generated (thermal 80mm or A4 PDF) with FDN/QR once EFRIS confirms.
     *   - Offline mode: if no server connection, sale is stored locally with
     *     status PENDING_SYNC; sync occurs via WorkManager when connectivity returns.
     */
    public function processSale(int $sessionId, array $cartItems, array $payments): Sale;

    /**
     * Close an open POS session and produce the end-of-shift reconciliation.
     *
     * @param int   $sessionId
     * @param Money $closingFloat  Cash physically counted at session close.
     *
     * @return SessionSummary  {
     *   session_id: int,
     *   cashier_id: int,
     *   opened_at: DateTimeString,
     *   closed_at: DateTimeString,
     *   opening_float: Money,
     *   closing_float: Money,
     *   total_sales: Money,
     *   total_cash_expected: Money,  // opening_float + cash sales
     *   variance: Money,             // closing_float - total_cash_expected
     *   variance_type: string,       // 'SURPLUS' | 'SHORTAGE' | 'BALANCED'
     *   sales_by_payment_method: array,
     *   sale_count: int,
     * }
     *
     * @throws SessionNotFoundException       If sessionId does not exist.
     * @throws InvalidSessionStatusException  If session is already closed.
     *
     * Business rules:
     *   - Variance posted to GL: DR/CR POS Variance Account.
     *   - Session status set to CLOSED; closing_float and closed_at recorded.
     *   - SessionSummary report available for printing immediately.
     */
    public function closeSession(int $sessionId, Money $closingFloat): SessionSummary;

    /**
     * Process a POS sale by a field agent.
     *
     * Agent sales draw from tbl_agent_stock_balance, not from warehouse stock (BR-001).
     *
     * @param int   $agentId
     * @param array $cartItems  [{product_id: int, quantity: float}]
     *
     * @return Sale  The completed sale DTO. No session required — agents do not
     *               manage float sessions; cash accountability is via remittance.
     *
     * @throws AgentNotFoundException         If agentId does not exist.
     * @throws InsufficientAgentStockException If agent does not hold sufficient stock.
     *
     * Business rules:
     *   - Draws stock from tbl_agent_stock_balance only.
     *   - Does NOT touch tbl_stock_balance.
     *   - GL auto-post: increases agent outstanding balance (invoice issued to agent's ledger).
     *   - Receipt printed via Bluetooth thermal printer (ESC/POS).
     *   - EFRIS submission triggered same as any POS sale.
     *   - Works fully offline via Sales Agent App (stored in Room, synced via WorkManager).
     */
    public function agentProcessSale(int $agentId, array $cartItems): Sale;
}
```
