# Accounting Module Test Cases

This section covers the General Ledger (GL), invoice lifecycle, VAT calculation, multi-currency posting, and period close. All monetary assertions use integer arithmetic in UGX (no floating-point comparisons).

## Journal Entry

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-ACCT-001 | `JournalEntryTest` | `test_balanced_journal_posts_successfully` | Post a balanced journal: debit = credit = UGX 100,000 | Debit line UGX 100,000 (DR Expense); credit line UGX 100,000 (CR Bank); valid period | Journal status = `POSTED`; GL debit account balance increases by 100,000 UGX; GL credit account balance increases by 100,000 UGX (integer match) |
| TC-ACCT-002 | `JournalEntryTest` | `test_imbalanced_journal_returns_422` | Post a journal where debit ≠ credit | Debit UGX 100,000; credit UGX 95,000 | HTTP 422; `error_code` = `JOURNAL_IMBALANCED`; no GL rows written |
| TC-ACCT-003 | `JournalEntryTest` | `test_journal_to_locked_period_returns_422` | Post a journal to a period with status = `LOCKED` | Valid balanced journal; `period_id` pointing to a locked period | HTTP 422; `error_code` = `PERIOD_LOCKED`; no GL rows written |

## Invoice Lifecycle

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-ACCT-004 | `InvoiceLifecycleTest` | `test_create_invoice_status_is_draft` | Create a new invoice | Valid invoice payload (customer, lines, date) | Invoice record persisted; `status` = `DRAFT`; no GL entries created |
| TC-ACCT-005 | `InvoiceLifecycleTest` | `test_post_invoice_creates_gl_entries` | Post a draft invoice via `sp_post_invoice_to_gl` | Valid posted invoice with at least 1 revenue line and 18% VAT | GL entries created: AR account debited, Revenue account credited, VAT Output account credited; all amounts in UGX integer arithmetic |
| TC-ACCT-006 | `InvoiceLifecycleTest` | `test_void_posted_invoice_creates_reversal_entries` | Void a posted invoice | `invoice_id` of a posted invoice; authorised session with `invoices.void` | Reversal GL entries posted (signs flipped); original invoice `status` = `VOID`; net GL impact = 0 |

## VAT Calculation

All VAT amounts are calculated using integer arithmetic. The formula is: $VAT = LineAmount \times Rate$ where both operands are integers in UGX.

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-ACCT-007 | `VatCalculationTest` | `test_standard_rate_vat_calculated_correctly` | Invoice line UGX 1,000,000 at 18% VAT | `line_amount` = 1000000; `vat_rate` = 18 | `vat_amount` = 180000 (integer); `line_total` = 1180000 (integer); no floating-point intermediate values |
| TC-ACCT-008 | `VatCalculationTest` | `test_zero_rated_line_produces_zero_vat` | Invoice line with `vat_rate` = 0 (zero-rated supply) | `line_amount` = 500000; `vat_rate` = 0 | `vat_amount` = 0; `line_total` = 500000; invoice status proceeds normally |

## Multi-Currency Posting

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-ACCT-009 | `MultiCurrencyTest` | `test_usd_invoice_posts_gl_in_ugx_and_tracks_usd_balance` | USD invoice converted to UGX at spot rate | `currency` = `USD`; `fx_rate` = 3750; `usd_amount` = 100 (i.e. USD 100) | GL posted in UGX: 100 × 3750 = 375,000 UGX (integer); USD sub-ledger balance tracks USD 100 separately |

## Period Close

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-ACCT-010 | `PeriodCloseTest` | `test_close_period_blocks_subsequent_journal_posts` | Close a period, then attempt to post a journal to it | Step 1: close `period_id`; Step 2: post balanced journal to same `period_id` | After Step 1: period `status` = `CLOSED`; after Step 2: HTTP 422; `error_code` = `PERIOD_LOCKED` |
