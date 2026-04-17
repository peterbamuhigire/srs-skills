# Accounting Module — Low-Level Design

## Overview

The Accounting module implements a double-entry general ledger. All financial postings go through stored procedures to guarantee atomicity and consistent entry-number generation. Application-layer service classes prepare the data and call the stored procedures; they never write directly to `gl_entries` or `gl_entry_lines`.

---

## AccountingService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `PeriodService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `getAccountBalance(int $accountId, ?string $asOfDate = null): float` | Chart-of-accounts primary key, optional ISO 8601 date | Net balance as float | Sums `gl_entry_lines.debit - gl_entry_lines.credit` for the account up to `$asOfDate`. Filters by `tenant_id`. |
| `postJournal(array $lines, string $memo, int $periodId): int` | Array of `['account_id', 'debit', 'credit']` entries, memo text, period primary key | New `gl_entries.id` | Validates that the sum of debits equals the sum of credits. Calls `sp_generate_entry_number` to obtain the next entry reference. Wraps the INSERT into `gl_entries` and the batch INSERT into `gl_entry_lines` in a single transaction. |
| `getTrialBalance(int $periodId): array` | Period primary key | Array of account-balance rows | Reads from `v_trial_balance` view filtered by `tenant_id` and `period_id`. |
| `closePeriod(int $periodId): void` | Period primary key | `void` | Delegates to `PeriodService::closePeriod()`. |

**Tables read:** `gl_entries`, `gl_entry_lines`, `chart_of_accounts`, `v_trial_balance`

**Tables written:** `gl_entries`, `gl_entry_lines`

**Stored procedures called:** `sp_generate_entry_number`

---

## InvoiceService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `PeriodService`, `TaxService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createInvoice(int $customerId, array $lines, int $periodId, ?string $dueDate = null): int` | Customer primary key, array of `['item_id', 'qty', 'unit_price', 'tax_code']` line entries, period primary key, optional ISO 8601 due date | New `invoices.id` | Validates the active period, calculates line totals via `TaxService::calculateVAT()`, inserts one row into `invoices` and one row per line into `invoice_lines`. Status is set to `draft`. |
| `postInvoiceToGL(int $invoiceId): void` | Invoice primary key | `void` | Calls the stored procedure `CALL sp_post_invoice_to_gl(:invoice_id, :tenant_id)`. Updates `invoices.status` to `posted`. Calls `AuditService::log()` inside the same transaction. |
| `voidInvoice(int $invoiceId, string $reason): void` | Invoice primary key, free-text void reason | `void` | Verifies no payment allocation exists. Sets `invoices.status = 'void'` and writes `void_reason` and `voided_at`. Calls `sp_post_return_to_gl(:invoice_id, :tenant_id)` to reverse the GL entries. Logs to `AuditService`. |

**Tables read/written:** `invoices`, `invoice_lines`

**Stored procedures called:** `sp_post_invoice_to_gl`, `sp_post_return_to_gl`, `sp_get_account_mapping`

---

## PaymentService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `allocatePayment(int $paymentId, int $invoiceId, float $amount): void` | Payment primary key, invoice primary key, allocation amount | `void` | Inserts a row into `payment_allocations`. Updates `invoices.amount_paid` and recalculates `invoices.balance_due`. Posts a GL clearing entry via `AccountingService::postJournal()`. Throws `AllocationException` if `$amount` exceeds the unallocated payment balance. |
| `reversePayment(int $paymentId, string $reason): void` | Payment primary key, free-text reason | `void` | Removes all allocation rows for the payment. Reverses the original GL entry by calling `AccountingService::postJournal()` with negated amounts. Sets `payments.status = 'reversed'`. |

**Tables read/written:** `payments`, `payment_allocations`, `invoices`

---

## BankReconciliationService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `importStatement(int $bankAccountId, string $csvPath): int` | Bank account primary key, absolute path to the uploaded CSV file | Count of rows imported | Parses the CSV, inserts each row into `bank_statement_lines` with `status = 'unmatched'`. Skips duplicate rows identified by `(bank_account_id, transaction_date, reference, amount)`. |
| `matchTransaction(int $statementLineId, int $glEntryLineId): void` | Bank statement line primary key, GL entry line primary key | `void` | Sets `bank_statement_lines.status = 'matched'` and `bank_statement_lines.gl_entry_line_id = :glEntryLineId`. Marks the GL entry line as reconciled. |
| `postUnmatched(int $bankAccountId, int $periodId): void` | Bank account primary key, period primary key | `void` | Iterates `bank_statement_lines WHERE status = 'unmatched'` for the account. For each row, determines the GL account via `sp_get_account_mapping` and posts a journal via `AccountingService::postJournal()`. |

**Tables read/written:** `bank_statement_lines`, `gl_entry_lines`, `bank_accounts`

---

## TaxService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `calculateVAT(float $netAmount, string $taxCode): array` | Net taxable amount, tax code key (e.g., `VAT18`, `EXEMPT`) | `['net' => float, 'tax' => float, 'gross' => float]` | Looks up the rate in `tax_codes` by `code` and `tenant_id`. Applies the rate: $tax = netAmount \times rate$. |
| `calculateWHT(float $grossAmount, string $whtCode): array` | Gross payment amount, WHT code key | `['gross' => float, 'wht' => float, 'net_payable' => float]` | Looks up the WHT rate in `wht_codes`. Calculates $wht = grossAmount \times rate$. |
| `generateVATReturn(int $periodId): array` | Period primary key | Array of VAT return summary rows | Aggregates `invoice_lines.tax_amount` and `supplier_invoice_lines.tax_amount` grouped by `tax_code` for the period. Reads from `v_vat_return`. |

**Tables read:** `tax_codes`, `wht_codes`, `invoice_lines`, `supplier_invoice_lines`, `v_vat_return`

---

## BudgetService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `setBudget(int $accountId, int $periodId, float $amount): void` | Chart-of-accounts primary key, period primary key, budgeted amount | `void` | Upserts a row in `account_budgets` for `(tenant_id, account_id, period_id)`. Logs to `AuditService`. |
| `getBudgetVariance(int $accountId, int $periodId): array` | Chart-of-accounts primary key, period primary key | `['budget' => float, 'actual' => float, 'variance' => float, 'variance_pct' => float]` | Reads `account_budgets.amount` and calls `AccountingService::getAccountBalance()`. $variance = budget - actual$, $variance\_pct = (variance / budget) \times 100$. |

**Tables read/written:** `account_budgets`

---

## PeriodService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `openPeriod(int $year, int $month): int` | Fiscal year (four-digit integer), month (1–12) | New `accounting_periods.id` | Inserts a row into `accounting_periods` with `status = 'open'`. Throws `PeriodConflictException` if a period for the same year-month already exists for the tenant. |
| `closePeriod(int $periodId): void` | Period primary key | `void` | Verifies no unposted documents reference the period. Sets `accounting_periods.status = 'closed'` and writes `closed_at = NOW()`. Logs to `AuditService`. |
| `getActivePeriod(): array` | None | Period row as associative array | Returns the single row in `accounting_periods` where `tenant_id = :tenant_id AND status = 'open'`. Throws `NoPeriodOpenException` if no open period exists. |

**Tables read/written:** `accounting_periods`
