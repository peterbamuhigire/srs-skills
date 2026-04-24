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

---

## CloseOrchestrationService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `PeriodService`, `FinanceApprovalService`, `NotificationService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `startCloseRun(int $periodId, string $scope = 'entity', ?int $groupId = null, ?string $templateCode = null): int` | Period primary key, scope (`entity` or `group`), optional reporting-group primary key, optional close-template code | New `finance_close_runs.id` | Creates a close run in `status = 'in_progress'`. Copies task definitions from `finance_close_templates` and `finance_close_template_tasks` into run-level task rows so the run remains immutable even if the template changes later. Rejects duplicate active runs for the same `(tenant_id, period_id, scope, group_id)` combination. |
| `getCloseDashboard(int $closeRunId): array` | Close run primary key | Array of run, task, dependency, and exception metrics | Returns the run header plus task progress, overdue items, unresolved control exceptions, pending approvals, and entity certification state. Reads only the authenticated tenant's run data. |
| `completeCloseTask(int $taskId, array $evidence = [], ?string $note = null): void` | Close task primary key, evidence manifest array, optional completion note | `void` | Verifies all predecessor tasks in `finance_close_task_dependencies` are completed. Writes evidence references to `finance_task_evidence`, marks the task `completed`, and, where the task requires sign-off, creates an approval request via `FinanceApprovalService::submitForApproval()`. |
| `reopenClosedPeriod(int $periodId, string $reason): int` | Period primary key, controller justification | New `finance_approvals.id` | Creates a controlled reopen request instead of directly mutating the period. Once approved, the service sets `accounting_periods.status = 'reopened_pending_adjustments'`, records the reason, and publishes a notification to reporting owners. |
| `finalizeCloseRun(int $closeRunId): void` | Close run primary key | `void` | Verifies all mandatory tasks are completed, all blocking exceptions are resolved, and all required close certifications are approved. Writes `finance_close_runs.status = 'closed'`, stamps `closed_at`, and delegates ledger locking to `PeriodService::closePeriod()`. |

**Tables read/written:** `finance_close_runs`, `finance_close_templates`, `finance_close_template_tasks`, `finance_close_tasks`, `finance_close_task_dependencies`, `finance_task_evidence`, `finance_control_exceptions`, `finance_approvals`, `accounting_periods`

---

## RecurringJournalService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`, `FinanceApprovalService`, `PeriodService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createTemplate(string $code, string $description, string $cadence, array $lines, array $rules = []): int` | Unique template code, description, cadence (`monthly`, `quarterly`, `event_driven`), journal template lines, optional rule payload | New `recurring_journal_templates.id` | Creates a reusable journal template and its line definitions. Each line stores either a fixed amount, a formula, or a source query reference, plus default dimensions and reversal policy. |
| `generateRun(int $templateId, int $periodId, string $runDate, array $parameters = []): int` | Template primary key, period primary key, ISO 8601 run date, optional runtime parameters | New `recurring_journal_runs.id` | Materializes a point-in-time journal snapshot from the template into `recurring_journal_runs` and `recurring_journal_run_lines`. Prevents duplicate runs for the same `(template_id, period_id)` unless the prior run was cancelled. |
| `submitRunForApproval(int $runId): int` | Recurring-run primary key | New `finance_approvals.id` | Applies the configured approval policy for the template. High-value or policy-sensitive runs move to `pending_approval`; low-risk runs can auto-approve where policy allows. |
| `postApprovedRun(int $runId): int` | Recurring-run primary key | New `gl_entries.id` | Re-validates the target period, then posts the frozen run lines through `AccountingService::postJournal()`. Stores the generated `gl_entry_id` on the run and, where configured, creates an automatic reversal entry for the next open period. |
| `suspendTemplate(int $templateId, string $reason): void` | Template primary key, free-text reason | `void` | Sets the template `status = 'suspended'`, prevents future generation, and logs the change to preserve audit traceability around disabled automation. |

**Tables read/written:** `recurring_journal_templates`, `recurring_journal_template_lines`, `recurring_journal_runs`, `recurring_journal_run_lines`, `finance_approvals`, `gl_entries`, `gl_entry_lines`

---

## ConsolidationService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `FinanceApprovalService`, `FxService`, `PeriodService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createConsolidationRun(int $groupId, int $periodId, string $basis = 'management', ?int $rateSetId = null): int` | Reporting-group primary key, period primary key, basis (`management` or `statutory`), optional FX-rate-set primary key | New `consolidation_runs.id` | Opens a group-level consolidation run and snapshots the participating entities, ownership percentages, reporting currency, and FX rate set for the run. |
| `loadEntityBalances(int $runId): void` | Consolidation-run primary key | `void` | Loads entity trial balances from the ERP ledger into `consolidation_balances`. If an entity closes outside the ERP, this method accepts a certified import package and stores the source document hash for auditability. |
| `postConsolidationAdjustment(int $runId, array $lines, string $category): int` | Consolidation-run primary key, elimination or top-side adjustment lines, category (`intercompany_elimination`, `ownership`, `reclass`, `topside`) | New `consolidation_adjustments.id` | Creates a consolidation-only adjustment that does not post back to entity ledgers. The service validates balancing, dimensions, and category-specific policy rules before saving the adjustment header and lines. |
| `certifyEntitySubmission(int $runId, int $entityId, array $checklist): int` | Consolidation-run primary key, entity primary key, certification checklist payload | New `finance_control_certifications.id` | Records entity-controller certification that trial balances, intercompany positions, and local close controls are complete. Missing checklist items create control exceptions instead of silent warnings. |
| `finalizeConsolidationRun(int $runId): void` | Consolidation-run primary key | `void` | Verifies all required entities are certified, intercompany mismatches are within policy threshold, and all adjustment approvals are complete. Locks the run for reporting and publishes the final consolidated dataset. |

**Tables read/written:** `consolidation_runs`, `consolidation_run_entities`, `consolidation_balances`, `consolidation_adjustments`, `consolidation_adjustment_lines`, `consolidation_fx_rate_sets`, `intercompany_matches`, `finance_control_certifications`, `finance_control_exceptions`, `finance_approvals`

---

## FinanceApprovalService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `NotificationService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `submitForApproval(string $documentType, int $documentId, string $policyCode, array $context = []): int` | Source document type, source document primary key, approval-policy code, optional route context | New `finance_approvals.id` | Resolves the approval path from `finance_approval_policy_rules`, creates the approval header and step rows, and places the document in a blocked state until the route is completed or rejected. |
| `recordDecision(int $approvalId, string $decision, ?string $comment = null): void` | Approval primary key, decision (`approved`, `rejected`, `changes_requested`), optional narrative | `void` | Updates the current step, advances to the next approver when required, and writes a full audit event. Terminal decisions release or reject the source document atomically. |
| `getPendingApprovals(array $filters = []): array` | Optional filters such as approver, module, document type, SLA status | Array of approval queue rows | Returns the authenticated user's pending finance approvals together with SLA age, escalation state, and source-document references. |
| `escalateOverdueApprovals(): int` | None | Count of approvals escalated | Finds approval steps past SLA, notifies the configured escalation role, and records the escalation event for audit and reporting. |

**Tables read/written:** `finance_approvals`, `finance_approval_steps`, `finance_approval_policy_rules`, `finance_approval_escalations`

---

## FinanceControlService

**Namespace:** `App\Modules\Accounting`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `FinanceApprovalService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `evaluateControlGate(string $controlCode, array $context): array` | Control-rule code, transaction or workflow context payload | `['passed' => bool, 'severity' => string, 'messages' => array]` | Executes configurable finance-control rules before journal posting, period close, consolidation finalization, or master-data changes. Supports hard-stop, warning, and evidence-required outcomes. |
| `certifyControlChecklist(string $workflowType, int $workflowId, array $items): int` | Workflow type (`close_run`, `bank_reconciliation`, `consolidation_run`, `journal_batch`), workflow primary key, checklist rows | New `finance_control_certifications.id` | Persists the checklist, sign-off status, and attachments for key finance workflows. Incomplete or failed checklist items automatically create exceptions in `finance_control_exceptions`. |
| `registerException(string $controlCode, string $documentType, int $documentId, string $severity, string $details): int` | Control code, source document type, source document primary key, severity, detail text | New `finance_control_exceptions.id` | Creates a tracked control exception with owner, due date, and remediation status. Exceptions can block posting or close based on the configured severity. |
| `resolveException(int $exceptionId, string $resolutionNote): void` | Exception primary key, remediation narrative | `void` | Closes the exception, records the remediation evidence, and writes an immutable audit event so finance can demonstrate how the issue was cleared. |

**Tables read/written:** `finance_control_rules`, `finance_control_checklists`, `finance_control_certifications`, `finance_control_exceptions`, `finance_approvals`

---

## Cross-Service Execution Rules

- `AccountingService::postJournal()` must call `FinanceControlService::evaluateControlGate()` before final posting for journal categories configured as controlled or approval-bound.
- Manual journals, recurring-journal runs, reopen-period requests, and consolidation adjustments above configured thresholds must route through `FinanceApprovalService` and remain non-posting until final approval.
- `CloseOrchestrationService` owns the run state, task state, and certification state for period close; it does not replace ledger posting logic already implemented in `AccountingService` and `PeriodService`.
- `ConsolidationService` writes only consolidation-layer balances and adjustments. Entity ledgers remain authoritative for legal-book postings; group-only eliminations and top-side entries remain off-ledger at the entity level.
