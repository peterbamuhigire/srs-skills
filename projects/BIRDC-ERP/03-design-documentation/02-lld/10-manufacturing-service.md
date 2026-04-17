# 10. ManufacturingService

**Namespace:** `App\Services\Manufacturing\ManufacturingService`
**Dependencies:** `ProductionOrderRepository`, `RecipeRepository`, `InventoryService`, `QCService`, `GLService`, `AuditLogService`
**Test coverage required:** ≥ 80%

## 10.1 Method Signatures

```php
final class ManufacturingService
{
    /**
     * Create a new production order from a recipe (Bill of Materials).
     *
     * @param int   $recipeId   The tbl_manufacturing_recipes.id to use.
     * @param float $quantity   Target output quantity in the recipe's output UOM.
     *
     * @return ProductionOrder  The created production order DTO in PLANNED status.
     *
     * @throws RecipeNotFoundException        If recipeId does not exist.
     * @throws InsufficientMaterialsException If warehouse stock is insufficient for the
     *                                        required inputs at the planned quantity.
     *                                        $exception->getShortfalls() lists each deficit.
     *
     * Business rules:
     *   - Required material quantities scaled from recipe: required_qty = recipe_qty_per_unit × $quantity.
     *   - Circular economy recipes included: peel → biogas (calorific value output),
     *     waste water → bio-slurry (kg output). All by-products are planned as expected outputs.
     *   - Production order includes job card with step-by-step instructions and worker assignment slots.
     *   - Mass balance parameters recorded: expected_input_kg = sum of all raw material inputs;
     *     expected_output_kg = primary outputs + by-product outputs + estimated scrap (configurable % per recipe).
     */
    public function createProductionOrder(int $recipeId, float $quantity): ProductionOrder;

    /**
     * Reserve raw materials for a production order (WIP accounting).
     *
     * @param int $orderId  The production order ID.
     *
     * @return void
     *
     * @throws ProductionOrderNotFoundException  If orderId does not exist.
     * @throws InvalidStatusException            If order is not in PLANNED status.
     * @throws InsufficientMaterialsException    If stock has changed since createProductionOrder().
     *
     * Business rules:
     *   - Calls InventoryService::recordMovement('PRODUCTION_INPUT', ...) for each raw material line.
     *   - GL auto-post: DR WIP / CR Raw Material Inventory (for each material line).
     *   - FEFO batch selection applied to all reserved materials (BR-007).
     *   - Order status advances from PLANNED to IN_PROGRESS.
     *   - Materials are physically deducted from warehouse stock at this point.
     */
    public function reserveMaterials(int $orderId): void;

    /**
     * Record the completion of a production order and submit to QC.
     *
     * @param int   $orderId
     * @param array $outputs  [
     *   {output_type: 'PRIMARY'|'BY_PRODUCT'|'SCRAP', product_id: int, quantity_kg: float},
     *   ...
     * ]
     *
     * @return CompletionRecord {
     *   order_id: int,
     *   completed_at: DateTimeString,
     *   outputs: array,
     *   mass_balance_status: 'WITHIN_TOLERANCE' | 'VARIANCE_DETECTED',
     *   variance_pct: float,
     *   qc_batch_ids: int[],   // Batch IDs created in tbl_inventory_batches with QC_PENDING status
     * }
     *
     * @throws ProductionOrderNotFoundException  If orderId does not exist.
     * @throws InvalidStatusException            If order is not in IN_PROGRESS status.
     * @throws MassBalanceViolationException     If verifyMassBalance() returns a variance
     *                                           outside the configured tolerance and the
     *                                           Production Supervisor has not acknowledged it.
     *
     * Business rules:
     *   - Calls verifyMassBalance() before any stock or GL updates.
     *   - If mass balance variance > configured tolerance (default ±2%): order CANNOT be closed
     *     without Production Supervisor acknowledgement (BR-008).
     *   - Finished goods batch created in tbl_inventory_batches with status QC_PENDING.
     *   - Stock transfer to saleable inventory is BLOCKED until QCService::releaseToInventory()
     *     is called (BR-004).
     *   - GL auto-post on completion: DR Finished Goods (QC_PENDING) / CR WIP.
     *   - Calls sp_close_production_order stored procedure for atomic close.
     */
    public function recordCompletion(int $orderId, array $outputs): CompletionRecord;

    /**
     * Verify the mass balance for a production order.
     *
     * @param int $orderId
     *
     * @return MassBalanceResult {
     *   order_id: int,
     *   total_input_kg: float,
     *   primary_output_kg: float,
     *   byproduct_output_kg: float,
     *   scrap_kg: float,
     *   total_output_kg: float,       // primary + by-product + scrap
     *   variance_kg: float,           // total_input_kg - total_output_kg
     *   variance_pct: float,          // |variance_kg / total_input_kg| × 100
     *   tolerance_pct: float,         // configured per recipe (default 2.0)
     *   within_tolerance: bool,
     * }
     *
     * Business rules:
     *   - Equation: $\text{Total Input (kg)} = \text{Primary Output (kg)} + \text{By-product Output (kg)} + \text{Scrap/Waste (kg)}$ (BR-008).
     *   - Tolerance is configurable per recipe in tbl_manufacturing_recipes.mass_balance_tolerance_pct.
     *   - If within_tolerance = false: generates a mass balance variance report (mPDF)
     *     for review by the Production Supervisor before order can be closed.
     */
    public function verifyMassBalance(int $orderId): MassBalanceResult;

    /**
     * Calculate the total production cost for a completed production order.
     *
     * @param int $orderId
     *
     * @return Money  Total production cost in UGX.
     *
     * Business rules:
     *   - Cost components:
     *       Raw materials: FIFO cost of batches reserved at reserveMaterials() time.
     *       Direct labour: worker hours × wage rate (from job card attendance records).
     *       Absorbed overhead: overhead rate per kg of output (configurable per cost centre).
     *   - Unit cost = total_production_cost / total_primary_output_kg.
     *   - Stored against the finished goods batch for COGS calculations downstream.
     */
    public function calculateProductionCost(int $orderId): Money;
}
```
