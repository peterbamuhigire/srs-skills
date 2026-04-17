# 9. FarmerService

**Namespace:** `App\Services\Farmers\FarmerService`
**Dependencies:** `FarmerRepository`, `CooperativeRepository`, `ContributionRepository`, `GLService`, `MobileMoneyService`, `NotificationService`, `AuditLogService`
**Test coverage required:** ≥ 80%

## 9.1 Method Signatures

```php
final class FarmerService
{
    /**
     * Register a new farmer in the BIRDC cooperative network.
     *
     * @param array $data {
     *   name: string,
     *   nin: string,              // Uganda National Identification Number (required)
     *   phone: string,            // Mobile number for SMS payment notifications
     *   mobile_money_number: string,
     *   mobile_money_provider: string,  // 'MTN' | 'AIRTEL'
     *   cooperative_id: int,
     *   photo_path: string|null,  // Server path to uploaded photo
     *   gps_latitude: float|null,
     *   gps_longitude: float|null,
     *   farms: [{size_acres: float, banana_variety: string, gps_polygon: string|null}],
     * }
     *
     * @return Farmer  The created farmer DTO.
     *
     * @throws DuplicateNINException       If a farmer with this NIN is already registered.
     * @throws CooperativeNotFoundException If cooperative_id does not exist.
     *
     * Business rules:
     *   - NIN must be unique across all farmers (tbl_farmers UNIQUE constraint on nin).
     *   - [CONTEXT-GAP: GAP-004] — Uganda Data Protection and Privacy Act 2019 legal review
     *     of farmer personal data (NIN, GPS, photo, mobile money) must be completed before
     *     go-live. See gap-analysis.md.
     *   - Farmer registration works offline in the Farmer Delivery App (queued in Room,
     *     synced via FarmerCatalogueSyncWorker).
     *   - Farmer ID (auto-incremented) is assigned on server sync, not on device.
     */
    public function registerFarmer(array $data): Farmer;

    /**
     * Record an individual farmer's contribution within a cooperative batch.
     *
     * This is Stage 3 of the 5-stage cooperative procurement workflow (BR-011).
     *
     * @param int    $batchId    tbl_procurement_cooperative_receipts.id
     * @param int    $farmerId
     * @param float  $weight     Weight in kilograms delivered by this farmer.
     * @param string $grade      Quality grade: 'A' | 'B' | 'C'
     *
     * @return Contribution {
     *   contribution_id: int,
     *   batch_id: int,
     *   farmer_id: int,
     *   weight_kg: float,
     *   grade: string,
     *   unit_price: Money,        // Derived from tbl_procurement_price_tiers[grade]
     *   gross_payable: Money,     // weight_kg × unit_price
     *   deductions: Money,        // Loan repayments + cooperative levies
     *   net_payable: Money,       // gross_payable - deductions
     * }
     *
     * @throws BatchNotFoundException  If batchId does not exist.
     * @throws FarmerNotFoundException If farmerId does not exist.
     * @throws InvalidGradeException   If grade is not 'A', 'B', or 'C'.
     *
     * Business rules:
     *   - Batch cannot progress to Stage 4 (stock receipt) until ALL delivered
     *     weight in the batch is attributed to individual farmers (BR-011).
     *   - Unit price per grade is drawn from tbl_procurement_price_tiers (configurable — DC-002).
     *   - Deductions: loan repayment instalments from tbl_farmer_loans + cooperative levy from
     *     tbl_cooperative_levy_rates.
     */
    public function recordContribution(
        int $batchId,
        int $farmerId,
        float $weight,
        string $grade
    ): Contribution;

    /**
     * Generate a farmer payment schedule for a period.
     *
     * @param DateString $periodStart
     * @param DateString $periodEnd
     *
     * @return PaymentSchedule[]  One PaymentSchedule per farmer with net_payable > 0.
     *   Each: {farmer_id, farmer_name, mobile_money_number, provider, net_payable: Money}
     *
     * @throws EmptyPeriodException  If no contributions exist in the specified period.
     *
     * Business rules:
     *   - Only contributions with batch status POSTED_TO_GL are included.
     *   - Minimum payment threshold: UGX 5,000 (configurable). Farmers below threshold
     *     are carried forward to the next payment period.
     */
    public function generateFarmerPaymentSchedule(
        string $periodStart,
        string $periodEnd
    ): array;

    /**
     * Execute bulk mobile money payment to farmers.
     *
     * @param PaymentSchedule[] $schedule  Output of generateFarmerPaymentSchedule().
     *
     * @return PaymentResult {
     *   total_farmers: int,
     *   total_amount: Money,
     *   successful: int,
     *   failed: int,
     *   failures: [{farmer_id, farmer_name, reason: string}],
     *   transaction_batch_id: string,  // MoMo batch reference
     * }
     *
     * @throws EmptyScheduleException  If schedule is empty.
     *
     * Business rules:
     *   - Routes each payment to MTN MoMo or Airtel Money based on mobile number prefix.
     *   - [CONTEXT-GAP: GAP-002] — MTN MoMo sandbox credentials required for testing.
     *   - [CONTEXT-GAP: GAP-003] — Airtel Money sandbox credentials required for testing.
     *   - GL auto-post on each successful disbursement: DR Cooperative Payable / CR Bank.
     *   - SMS confirmation sent to farmer on successful payment via NotificationService.
     *   - Failed payments are logged with reason and flagged for Finance Director review.
     *   - Requires Finance Manager approval before execution (SoD — separate approval step).
     */
    public function bulkMobileMoneyPayment(array $schedule): PaymentResult;
}
```
