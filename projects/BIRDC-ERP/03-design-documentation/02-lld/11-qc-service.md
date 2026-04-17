# 11. QCService

**Namespace:** `App\Services\QC\QCService`
**Dependencies:** `InspectionRepository`, `BatchRepository`, `InventoryService`, `GLService`, `AuditLogService`
**Test coverage required:** ≥ 80%

## 11.1 Method Signatures

```php
final class QCService
{
    /**
     * Create a QC inspection record for a batch using a configured template.
     *
     * @param int $batchId     The tbl_inventory_batches.id of the batch to inspect.
     * @param int $templateId  The inspection template (tbl_qc_templates.id) to apply.
     *                         Templates are configurable per product category (DC-002).
     *
     * @return Inspection  The created inspection DTO in PENDING status.
     *
     * @throws BatchNotFoundException    If batchId does not exist.
     * @throws TemplateNotFoundException If templateId does not exist.
     * @throws InvalidStatusException    If batch is not in QC_PENDING status.
     *
     * Business rules:
     *   - One active inspection per batch at a time.
     *   - Template parameters may be: NUMERIC (with min/max limits), PASS_FAIL, TEXT, PHOTO.
     *   - Batch status remains QC_PENDING until inspection is completed.
     *   - For export batches: QC template must include all parameters specified by the
     *     destination market (BR-017). [CONTEXT-GAP: GAP-010] — exact export QC parameters
     *     per market are pending BIRDC QC Manager input.
     */
    public function createInspection(int $batchId, int $templateId): Inspection;

    /**
     * Record a single inspection result for a parameter within an inspection.
     *
     * @param int        $inspectionId
     * @param int        $parameterId   The tbl_qc_template_parameters.id
     * @param mixed      $value         Numeric, string, or bool depending on parameter type.
     *
     * @return void
     *
     * @throws InspectionNotFoundException  If inspectionId does not exist.
     * @throws ParameterNotFoundException   If parameterId does not belong to this inspection's template.
     * @throws InvalidValueException        If value type does not match parameter type, or
     *                                      if numeric value is outside specification limits.
     *
     * Business rules:
     *   - For NUMERIC parameters: value is validated against min_limit and max_limit.
     *     Out-of-spec values are recorded but do not throw an exception — they are flagged.
     *   - When all parameters on an inspection are recorded, inspection status automatically
     *     advances to AWAITING_DECISION.
     */
    public function recordResult(int $inspectionId, int $parameterId, mixed $value): void;

    /**
     * Generate a Certificate of Analysis for a batch.
     *
     * @param int    $batchId
     * @param string $marketType  'DOMESTIC' | 'SOUTH_KOREA' | 'EU' | 'SAUDI_ARABIA' |
     *                             'QATAR' | 'USA'
     *
     * @return CertificateOfAnalysis {
     *   coa_id: int,
     *   batch_id: int,
     *   batch_number: string,
     *   product_name: string,
     *   market_type: string,
     *   issued_at: DateTimeString,
     *   issued_by: int,
     *   parameters: [{name, result, unit, min_limit, max_limit, pass: bool}],
     *   overall_status: 'APPROVED' | 'APPROVED_FOR_DOMESTIC' | 'REJECTED',
     *   pdf_path: string,   // Path to generated mPDF CoA document
     * }
     *
     * @throws BatchNotFoundException  If batchId does not exist.
     * @throws InspectionIncompleteException If the inspection has parameters not yet recorded.
     *
     * Business rules:
     *   - An 'APPROVED_FOR_DOMESTIC' batch cannot be dispatched on an export order without
     *     generating an export-grade CoA with the specific market's parameters (BR-017).
     *   - Export-grade CoA parameters are market-specific and sourced from
     *     tbl_qc_market_requirements.
     *   - CoA PDF is generated using mPDF with BIRDC letterhead and BIRDC Director signature block.
     *   - Each CoA is uniquely numbered: COA-YYYY-NNNN.
     */
    public function generateCoA(int $batchId, string $marketType): CertificateOfAnalysis;

    /**
     * Release a QC-approved batch to saleable inventory.
     *
     * This is the gate control for BR-004: stock transfer to saleable inventory is
     * blocked until QC approval.
     *
     * @param int $batchId
     *
     * @return void
     *
     * @throws BatchNotFoundException    If batchId does not exist.
     * @throws QCGateBlockedException    If batch QC status is not 'APPROVED' or
     *                                   'APPROVED_FOR_DOMESTIC' — error message specifies
     *                                   which parameters failed (BR-004).
     * @throws PermissionException       If user does not hold QC_MANAGER role.
     *
     * Business rules:
     *   - Checks tbl_inventory_batches.qc_status = 'APPROVED' before proceeding (BR-004).
     *   - Calls InventoryService::recordMovement('PRODUCTION_OUTPUT', ...) to transfer
     *     batch from QC_PENDING location to the designated finished goods location.
     *   - GL adjustment: DR Finished Goods (Saleable) / CR Finished Goods (QC_PENDING).
     *   - After release, batch becomes available for sales allocation and FEFO picks.
     */
    public function releaseToInventory(int $batchId): void;
}
```
