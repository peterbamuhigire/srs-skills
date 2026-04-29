# 5. InventoryService

**Namespace:** `App\Services\Inventory\InventoryService`
**Dependencies:** `InventoryRepository`, `AgentRepository`, `BatchRepository`, `GLService`, `AuditLogService`
**Test coverage required:** ≥ 80%

## 5.1 Method Signatures

```php
final class InventoryService
{
    /**
     * Record a stock movement (receipt, transfer, adjustment, issuance, sale, production).
     *
     * @param string $type          Movement type constant:
     *                              'RECEIPT' | 'TRANSFER' | 'ADJUSTMENT' | 'AGENT_ISSUANCE' |
     *                              'SALE' | 'PRODUCTION_INPUT' | 'PRODUCTION_OUTPUT' |
     *                              'AGENT_RETURN' | 'WRITE_OFF'
     * @param array  $items         [{product_id, batch_id, quantity, unit_cost: Money|null}]
     * @param int|null $fromLocation  Source location ID (null for receipts)
     * @param int|null $toLocation    Destination location ID (null for sales/write-offs)
     *
     * @return Movement  The recorded movement DTO.
     *
     * @throws InsufficientStockException  If type is a reduction and quantity exceeds on-hand.
     * @throws LocationNotFoundException   If fromLocation or toLocation does not exist.
     * @throws FEFOViolationException      If a specific batch_id was provided that violates
     *                                     FEFO order (BR-007).
     *
     * Business rules:
     *   - For AGENT_ISSUANCE type: delegates to processAgentIssuance() for float limit check.
     *   - FEFO enforced when batch_id is null — auto-selected via enforceFefo().
     *   - tbl_stock_balance updated atomically with the movement record.
     *   - GL auto-post generated for ADJUSTMENT, WRITE_OFF, AGENT_ISSUANCE, PRODUCTION_INPUT,
     *     PRODUCTION_OUTPUT types (not for TRANSFER — no GL impact on warehouse transfers).
     */
    public function recordMovement(
        string $type,
        array $items,
        ?int $fromLocation,
        ?int $toLocation
    ): Movement;

    /**
     * Enforce First Expiry First Out (FEFO) batch allocation for a product and quantity.
     *
     * @param int   $productId
     * @param float $quantity   Total quantity required.
     *
     * @return BatchAllocation[]  Array of batch allocations summing to $quantity,
     *                            ordered by earliest expiry_date first.
     *
     * @throws InsufficientStockException  If total available stock is less than $quantity.
     * @throws NoExpiryDataException       If called for a product not tracked by expiry
     *                                     (non-food products may not have expiry dates).
     *
     * Business rules:
     *   - Selects batches in ascending expiry_date order (earliest first — BR-007).
     *   - Partial batch allocation is allowed when a batch has less than remaining quantity.
     *   - Only batches with QC status 'APPROVED' and quantity > 0 are eligible.
     *   - Generates expiry alert events for batches within the 30/60/90-day threshold windows.
     */
    public function enforceFefo(int $productId, float $quantity): array;

    /**
     * Initiate a physical stock count for a warehouse location.
     *
     * Freezes stock movements for the location during the count period.
     *
     * @param int $locationId  The warehouse location to count.
     *
     * @return StockCount  {count_id, location_id, initiated_by, initiated_at, status: 'FROZEN'}
     *
     * @throws ActiveCountExistsException  If a count is already in progress for this location.
     * @throws PermissionException         If user does not hold STORE_MANAGER role.
     *
     * Business rules:
     *   - Sets location status to FROZEN in tbl_warehouse_locations.
     *   - New movements to/from the frozen location are blocked until count is approved.
     *   - Generates count sheets (printable via mPDF) with expected quantities.
     */
    public function initiateStockCount(int $locationId): StockCount;

    /**
     * Process an agent stock issuance from the warehouse to an agent.
     *
     * Enforces the agent float limit (BR-006) and updates both inventory tracks atomically.
     *
     * @param int   $agentId
     * @param array $items   [{product_id: int, quantity: float}]
     *
     * @return void
     *
     * @throws AgentNotFoundException       If agentId does not exist.
     * @throws FloatLimitExceededException  If the issuance would cause the agent's stock
     *                                      value to exceed their configured float limit (BR-006).
     *                                      $exception->getRemainingCapacity() returns available UGX.
     * @throws InsufficientStockException   If warehouse has insufficient stock.
     *
     * Business rules:
     *   - Float limit check: (current agent stock value + issuance value) ≤ agent.float_limit.
     *     Enforced both here and by trg_agent_float_check trigger (defence in depth).
     *   - FEFO batch selection applied for all issued items.
     *   - Decrements tbl_stock_balance; increments tbl_agent_stock_balance.
     *   - GL auto-post: DR Agent Receivable (Inventory) / CR Warehouse Inventory.
     *   - Requires Store Manager role (creator) + Store Manager approval (SoD via L7 if
     *     a second supervisor must approve large issuances — configurable threshold).
     */
    public function processAgentIssuance(int $agentId, array $items): void;

    /**
     * Recommend a putaway bin for received or produced stock.
     *
     * @param array $receiptLine {stock_item_id, batch_id, quantity, location_id, qc_status}
     *
     * @return PutawayRecommendation {
     *   recommended_bin_id: int,
     *   candidate_bins: [{bin_id, score, capacity_remaining, reason}],
     *   override_required: bool
     * }
     *
     * Business rules:
     *   - Respects cold-store, QC, capacity, FEFO/FIFO rotation, and staging policies.
     *   - Overrides require reason code and Store Manager role.
     */
    public function recommendPutaway(array $receiptLine): PutawayRecommendation;

    /**
     * Generate pick tasks and pick-path sequence for a source document.
     *
     * @param string $sourceType
     * @param int    $sourceId
     *
     * @return PickWave {wave_id, tasks: [{task_id, item_id, batch_id, bin_id, quantity, sequence_no}]}
     *
     * Business rules:
     *   - Applies FEFO and excludes rejected, on-hold, and expired batches.
     *   - Moves picked stock to a named staging location until dispatch or issue confirmation.
     */
    public function generatePickWave(string $sourceType, int $sourceId): PickWave;
}
```
