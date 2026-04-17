# 6. AgentService

**Namespace:** `App\Services\Agents\AgentService`
**Dependencies:** `AgentRepository`, `RemittanceRepository`, `InvoiceRepository`, `GLService`, `DatabaseConnection`, `NotificationService`, `AuditLogService`
**Test coverage required:** ≥ 80%

## 6.1 Method Signatures

```php
final class AgentService
{
    /**
     * Apply a cash remittance received from an agent to their outstanding invoices (FIFO).
     *
     * Delegates to stored procedure sp_apply_remittance_to_invoices for atomic allocation.
     *
     * @param int   $agentId
     * @param Money $amount   The amount of cash received from the agent.
     *
     * @return RemittanceResult {
     *   remittance_id: int,
     *   agent_id: int,
     *   amount_received: Money,
     *   allocations: [{invoice_id, invoice_number, amount_allocated: Money, invoice_cleared: bool}],
     *   remaining_balance: Money,  // amount not yet allocated (agent still owes)
     *   status: 'PENDING_VERIFICATION',
     * }
     *
     * @throws AgentNotFoundException  If agentId does not exist.
     * @throws ZeroAmountException     If $amount ≤ 0.
     *
     * Business rules:
     *   - Remittance is recorded with status PENDING_VERIFICATION — no GL post yet.
     *   - Calls sp_apply_remittance_to_invoices which performs FIFO allocation in a
     *     single database transaction (BR-002): oldest invoice cleared first.
     *   - Partial allocation allowed: if amount < oldest invoice balance, the invoice
     *     is partially cleared; remaining invoice balance is preserved.
     *   - Commission does NOT accrue at this point — only on verification (BR-015).
     *   - Remittance creator is recorded; the verifier must be a different user (BR-003).
     */
    public function applyRemittance(int $agentId, Money $amount): RemittanceResult;

    /**
     * Verify a pending remittance (supervisor confirmation of cash receipt).
     *
     * Triggers GL posting and commission accrual.
     *
     * @param int $remittanceId  The remittance to verify.
     * @param int $verifierId    The supervisor performing the verification.
     *
     * @return void
     *
     * @throws RemittanceNotFoundException    If remittanceId does not exist.
     * @throws InvalidStatusException         If remittance is not in PENDING_VERIFICATION status.
     * @throws SegregationOfDutiesException   If verifierId = remittance.created_by (BR-003).
     *
     * Business rules:
     *   - SoD check: verifierId ≠ remittance.created_by (BR-003). Enforced at L7 by
     *     RBACService::hasPermission() before this method is called, and also as a
     *     guard at the top of this method (defence in depth).
     *   - GL auto-post on verification: DR Cash / CR Agent Receivable.
     *   - Status updated to VERIFIED with verifier ID and timestamp.
     *   - Commission accrued: calculateCommission() called for the cleared invoices.
     *   - SMS notification sent to agent: "UGX X,XXX,XXX remittance verified. Commission: UGX Y."
     */
    public function verifyRemittance(int $remittanceId, int $verifierId): void;

    /**
     * Calculate agent commission for a period based on verified remittances only.
     *
     * @param int        $agentId
     * @param DateString $periodStart  Start date (inclusive)
     * @param DateString $periodEnd    End date (inclusive)
     *
     * @return CommissionStatement {
     *   agent_id: int,
     *   agent_name: string,
     *   period_start: DateString,
     *   period_end: DateString,
     *   verified_remittances: [{remittance_id, verified_at, amount: Money}],
     *   cleared_invoices: [{invoice_id, invoice_number, invoice_value: Money}],
     *   commission_rate_pct: float,
     *   gross_commission: Money,
     *   deductions: [{description: string, amount: Money}],
     *   net_commission: Money,
     * }
     *
     * @throws AgentNotFoundException  If agentId does not exist.
     *
     * Business rules:
     *   - Commission accrues only on invoices cleared by VERIFIED remittances (BR-015).
     *   - Commission is calculated as: gross_commission = sum(cleared_invoice_value) × rate.
     *   - Commission rate is configured per agent in tbl_agents.commission_rate_pct.
     *   - Deductions (e.g., advances, penalties) are drawn from tbl_agent_deductions.
     *   - The CommissionStatement is the basis for the GL entry:
     *     DR Commission Expense / CR Commission Payable.
     */
    public function calculateCommission(int $agentId, string $periodStart, string $periodEnd): CommissionStatement;
}
```
