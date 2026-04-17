# 14. EFRISService

**Namespace:** `App\Services\Integrations\EFRISService`
**Dependencies:** `EFRISRepository`, `InvoiceRepository`, `AuditLogService`, `NotificationService`, `HttpClient`
**Test coverage required:** ≥ 80%

## 14.1 Method Signatures

```php
final class EFRISService
{
    /**
     * Submit a fiscal document (invoice or POS receipt) to URA EFRIS.
     *
     * @param int $invoiceId  The tbl_sales_invoices.id or tbl_pos_sales.id to submit.
     *
     * @return EFRISResult {
     *   success: bool,
     *   fdn_number: string|null,       // Fiscal Document Number from URA
     *   qr_code: string|null,          // QR code data URL from URA
     *   efris_response_code: string,
     *   efris_response_message: string,
     *   submitted_at: DateTimeString,
     * }
     *
     * @throws InvoiceNotFoundException  If invoiceId does not exist.
     *
     * Business rules:
     *   - Serialises the invoice to the URA EFRIS JSON payload format.
     *   - Payload is AES-256 encrypted and Base64-encoded per EFRIS API specification.
     *     [CONTEXT-GAP: GAP-001] — URA EFRIS API sandbox credentials required.
     *   - On success: calls storeResponse() to persist FDN and QR code; invoice status
     *     updated to ISSUED.
     *   - On failure: does NOT throw — returns EFRISResult with success = false.
     *     Caller (SalesService, POSService) is responsible for queuing a retry.
     *   - All EFRIS API calls and responses are logged to tbl_efris_log regardless
     *     of success or failure.
     */
    public function submitDocument(int $invoiceId): EFRISResult;

    /**
     * Process all items in the EFRIS retry queue.
     *
     * Called every 5 minutes by a cron job.
     *
     * @return void
     *
     * Business rules:
     *   - Fetches records from tbl_efris_retry_queue where:
     *       status = 'PENDING' AND next_retry_at ≤ NOW() AND attempts < 3.
     *   - For each: calls submitDocument(); on success removes from queue; on failure
     *     increments attempts and sets next_retry_at with exponential backoff:
     *     $\text{next\_retry\_at} = \text{NOW()} + 5 \times 2^{\text{attempts}} \text{ minutes}$
     *   - After 3 failed attempts: status set to 'FAILED'; Finance Manager notified via
     *     email and SMS with invoice number and failure reason.
     *   - tbl_efris_retry_queue entries are never deleted — they are archived with final status.
     */
    public function retryFailedSubmissions(): void;

    /**
     * Persist the EFRIS response (FDN and QR code) against a submitted invoice.
     *
     * @param int    $invoiceId
     * @param string $fdnNumber   The Fiscal Document Number returned by URA EFRIS.
     * @param string $qrCode      The QR code data (URL or base64 PNG) returned by URA.
     *
     * @return void
     *
     * @throws InvoiceNotFoundException  If invoiceId does not exist.
     *
     * Business rules:
     *   - Updates tbl_sales_invoices: fdn_number, efris_qr_code, efris_status = 'SUBMITTED',
     *     efris_submitted_at.
     *   - FDN and QR code are printed on all subsequent PDF and thermal receipt outputs
     *     of this invoice (via mPDF template).
     *   - This method is idempotent: calling it a second time with the same FDN is a no-op.
     */
    public function storeResponse(int $invoiceId, string $fdnNumber, string $qrCode): void;
}
```
