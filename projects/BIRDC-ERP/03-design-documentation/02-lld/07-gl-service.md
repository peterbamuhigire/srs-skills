# 7. GLService

**Namespace:** `App\Services\GL\GLService`
**Dependencies:** `JournalRepository`, `AccountRepository`, `HashChainRepository`, `AuditLogService`
**Test coverage required:** 100% (financial-critical)

## 7.1 Method Signatures

```php
final class GLService
{
    /**
     * Post a balanced journal entry to the General Ledger.
     *
     * This method is the single entry point for all GL postings in the system.
     * All 17 modules call GLService::postJournal() — no module writes directly
     * to tbl_gl_journals or tbl_gl_journal_lines.
     *
     * @param array $entries {
     *   reference_type: string,    // 'INVOICE' | 'PAYMENT' | 'PAYROLL' | 'PRODUCTION' | ...
     *   reference_id: int,         // The ID of the originating transaction
     *   narration: string,         // Human-readable description
     *   period_id: int,            // tbl_accounting_periods.id
     *   lines: [
     *     {
     *       account_id: int,
     *       debit: Money,          // 0 if credit line
     *       credit: Money,         // 0 if debit line
     *       segment_code: string|null,   // Parliamentary vote segment (PIBID)
     *       cost_centre: string|null,
     *       narration: string|null,
     *     }
     *   ]
     * }
     *
     * @return Journal  The posted journal DTO with journal_id, je_number, and posted_at.
     *
     * @throws UnbalancedJournalException   If sum(debit) ≠ sum(credit) across all lines.
     * @throws AccountNotFoundException     If any account_id does not exist.
     * @throws ClosedPeriodException        If the target accounting period is closed.
     * @throws BrokenHashChainException     If the account's hash chain status is CHAIN_BROKEN —
     *                                      no new entries permitted until integrity is restored.
     *
     * Business rules:
     *   - Validates sum(debit) = sum(credit) before any DB write.
     *   - Calls sp_post_gl_journal stored procedure which:
     *       1. Assigns sequential JE number (JE-YYYY-NNNN) via trg_je_number_seq.
     *       2. Inserts tbl_gl_journals and tbl_gl_journal_lines.
     *       3. Computes and stores entry_hash for each line (BR-013).
     *       4. Checks and updates budget vote expenditure (triggers trg_budget_vote_alert).
     *   - Status: journals are posted immediately (no draft → post lifecycle for auto-posts).
     *   - Manual journal entries (by Accounts Assistant) go through draft → approved → posted,
     *     with SoD check at approval (BR-003).
     */
    public function postJournal(array $entries): Journal;

    /**
     * Generate the trial balance as of a given date.
     *
     * @param DateString $asOfDate  The balance date (all entries on or before this date).
     * @param int|null   $modeFilter  null = both modes; 0 = BIRDC commercial; 1 = PIBID parliamentary.
     *
     * @return TrialBalance {
     *   as_of_date: DateString,
     *   accounts: [{
     *     account_code: string,
     *     account_name: string,
     *     account_type: string,
     *     debit_total: Money,
     *     credit_total: Money,
     *     net_balance: Money,
     *   }],
     *   total_debits: Money,
     *   total_credits: Money,
     *   is_balanced: bool,    // total_debits = total_credits
     * }
     *
     * Business rules:
     *   - Uses vw_trial_balance view with date and mode filters.
     *   - Living report: no period-close required.
     *   - is_balanced = false is an anomaly; Finance Director is alerted.
     */
    public function getTrialBalance(string $asOfDate, ?int $modeFilter = null): TrialBalance;

    /**
     * Generate and store the cryptographic hash for a journal line.
     *
     * Called internally by sp_post_gl_journal. Exposed as a public method
     * for use in data migration and integrity re-seeding under Finance Director authority.
     *
     * @param int $journalLineId  The ID of the journal line to hash.
     *
     * @return string  The SHA-256 hash string (64 hex characters).
     *
     * Business rules:
     *   - Hash inputs: prev_hash | journal_id | account_id | debit | credit | posted_at (BR-013).
     *   - For genesis entries (first line on an account), prev_hash = SHA256("BIRDC-ERP-GENESIS|{account_id}").
     *   - The computed hash is stored in tbl_gl_journal_lines.entry_hash.
     */
    public function generateHashChain(int $journalLineId): string;

    /**
     * Verify the hash chain integrity for a GL account.
     *
     * @param int $accountId  The GL account to verify.
     *
     * @return IntegrityReport {
     *   account_id: int,
     *   account_code: string,
     *   lines_checked: int,
     *   broken_at: int|null,           // journal_line_id where chain breaks; null if intact
     *   broken_journal_id: int|null,   // journal_id of broken entry
     *   broken_at_timestamp: DateTimeString|null,
     *   status: 'INTACT' | 'CHAIN_BROKEN',
     * }
     *
     * @throws AccountNotFoundException  If accountId does not exist.
     *
     * Business rules:
     *   - Traverses all journal lines for the account in chronological order.
     *   - Recomputes each hash and compares to stored entry_hash.
     *   - First mismatch is recorded; traversal continues to count total broken lines.
     *   - If status = 'CHAIN_BROKEN': sets tbl_coa_accounts.integrity_status = 'CHAIN_BROKEN';
     *     sends CRITICAL alert to Finance Director, IT Administrator, and Director (BR-013).
     *   - Result logged to AuditLogService.
     */
    public function verifyHashChainIntegrity(int $accountId): IntegrityReport;
}
```
