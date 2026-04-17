# 8. ProcurementService

**Namespace:** `App\Services\Procurement\ProcurementService`
**Dependencies:** `PurchaseRequestRepository`, `LPORepository`, `GRNRepository`, `VendorRepository`, `InventoryService`, `GLService`, `AuditLogService`
**Test coverage required:** ≥ 80%

## 8.1 Method Signatures

```php
final class ProcurementService
{
    /**
     * Create a new Purchase Request.
     *
     * @param array $data {
     *   requested_by: int,          // user_id of the requesting staff member
     *   department_id: int,
     *   items: [{description: string, quantity: float, estimated_unit_cost: Money, uom: string}],
     *   justification: string,
     *   required_by: DateString,
     *   budget_vote_id: int|null,   // PIBID parliamentary vote (if applicable)
     *   cost_centre: string,
     * }
     *
     * @return PurchaseRequest  The created PR DTO in PENDING_APPROVAL status.
     *
     * @throws BudgetVoteNotFoundException  If budget_vote_id does not exist.
     * @throws BudgetExceededException      If estimated value would breach 100% of vote allocation
     *                                      and no Director override is attached (BR-014).
     *
     * Business rules:
     *   - PPDA category is automatically classified based on estimated total value
     *     using the thresholds in tbl_ppda_thresholds (configurable — DC-002, BR-005).
     *     [CONTEXT-GAP: GAP-007] — exact UGX thresholds pending BIRDC confirmation.
     *   - PPDA category determines the required approval chain (BR-005).
     */
    public function createPR(array $data): PurchaseRequest;

    /**
     * Approve a Purchase Request, advancing it toward LPO/RFQ.
     *
     * @param int $prId        The PR to approve.
     * @param int $approverId  The user approving the PR.
     *
     * @return void
     *
     * @throws PRNotFoundException            If prId does not exist.
     * @throws InvalidStatusException         If PR is not in PENDING_APPROVAL status.
     * @throws SegregationOfDutiesException   If approverId = pr.requested_by (BR-003).
     * @throws InsufficientAuthorityException If approverId's role does not match the
     *                                        required PPDA approval level (BR-005).
     *
     * Business rules:
     *   - PPDA level check: verifies approverId holds the role required for the PR's
     *     PPDA category (Micro → Department Head; Small → Finance Manager; Large → Director; BR-005).
     *   - On approval: PR status set to APPROVED; approverId and approved_at recorded.
     *   - Budget commitment recorded against the relevant vote / cost centre.
     */
    public function approvePR(int $prId, int $approverId): void;

    /**
     * Convert an approved Purchase Request to a Local Purchase Order (LPO).
     *
     * @param int $prId  The approved PR to convert.
     *
     * @return LPO  The created LPO DTO in ISSUED status, formatted for Uganda standard LPO.
     *
     * @throws PRNotFoundException    If prId does not exist.
     * @throws InvalidStatusException If PR is not in APPROVED status.
     *
     * Business rules:
     *   - LPO number assigned sequentially: LPO-YYYY-NNNN.
     *   - LPO includes: vendor details, items, quantities, agreed unit prices, delivery date,
     *     payment terms, PPDA reference, and required PPDA documentation checklist.
     *   - PDF generated via mPDF in Uganda standard LPO format.
     */
    public function convertToLPO(int $prId): LPO;

    /**
     * Record a Goods Receipt Note (GRN) against an LPO.
     *
     * @param int   $lpoId
     * @param array $items  [{lpo_line_id: int, quantity_received: float, batch_number: string|null,
     *                        manufacturing_date: DateString|null, expiry_date: DateString|null}]
     *
     * @return GRN  The recorded GRN DTO.
     *
     * @throws LPONotFoundException         If lpoId does not exist.
     * @throws InvalidStatusException       If LPO is not in ISSUED or PARTIALLY_RECEIVED status.
     * @throws QuantityExceedsLPOException  If received quantity exceeds LPO quantity for any line.
     *
     * Business rules:
     *   - Creates tbl_inventory_batches records for each received lot.
     *   - Calls InventoryService::recordMovement('RECEIPT', ...) to update stock levels.
     *   - GL auto-post: DR Raw Material Inventory / CR Accounts Payable.
     *   - GRN is required before vendor invoice can be matched (BR-012).
     */
    public function recordGRN(int $lpoId, array $items): GRN;

    /**
     * Perform three-way matching: LPO vs. GRN vs. vendor invoice.
     *
     * @param int $lpoId
     * @param int $grnId
     * @param int $invoiceId  The vendor invoice (tbl_ap_vendor_invoices.id).
     *
     * @return MatchResult {
     *   matched: bool,
     *   price_variance_pct: float,      // (invoice_unit_price - lpo_unit_price) / lpo_unit_price × 100
     *   quantity_variance_pct: float,   // (invoice_quantity - grn_quantity) / grn_quantity × 100
     *   flags: string[],               // ['PRICE_VARIANCE_EXCEEDS_5PCT', 'QTY_VARIANCE_EXCEEDS_2PCT']
     *   requires_finance_review: bool,
     * }
     *
     * @throws DocumentNotFoundException  If any of the three IDs do not exist.
     *
     * Business rules:
     *   - Price variance > 5%: sets requires_finance_review = true; payment blocked (BR-012).
     *   - Quantity variance > 2%: sets requires_finance_review = true; payment blocked (BR-012).
     *   - Matched invoices proceed to payment scheduling without Finance Manager intervention.
     *   - Farmer payments bypass three-way matching — use individual contribution records instead (BR-012).
     */
    public function threeWayMatch(int $lpoId, int $grnId, int $invoiceId): MatchResult;
}
```
