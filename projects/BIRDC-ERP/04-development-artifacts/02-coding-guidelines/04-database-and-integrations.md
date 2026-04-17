# 4. Database Access Rules

## 4.1 All Queries Through the Repository Layer

The layered architecture enforces a single rule: **only Repository classes contain SQL queries**.

| Layer | SQL Permitted | Reason |
|---|---|---|
| Controller | No | Controllers handle HTTP only — they call services |
| Service | No | Services contain business logic — they call repositories |
| Repository (interface) | No | Interfaces define the contract |
| Repository (implementation) | Yes | This is the only permitted location for SQL |

Any SQL found in a Controller or Service class is rejected at code review.

## 4.2 Transaction Management

All operations that modify multiple rows across multiple tables must be wrapped in a database transaction. The transaction is managed in the Service layer (not the Repository layer), because only the Service knows the full scope of the operation.

```php
public function confirmInvoice(int $invoiceId): Invoice
{
    $this->pdo->beginTransaction();
    try {
        $invoice = $this->invoiceRepository->findById($invoiceId);
        $invoice->confirm();
        $this->invoiceRepository->save($invoice);
        $this->glPostingService->postInvoice($invoice);  // multiple GL inserts
        $this->pdo->commit();
        return $invoice;
    } catch (\Throwable $e) {
        $this->pdo->rollBack();
        throw $e;
    }
}
```

Stored procedures that manage their own transactions (e.g., `sp_apply_remittance_to_invoices`) are called from a repository method. The service does not wrap a stored procedure call in an additional transaction.

## 4.3 Stored Procedure Calling Convention

```php
// Calling sp_apply_remittance_to_invoices from RemittanceRepository
public function allocateToInvoices(int $remittanceId): array
{
    $stmt = $this->pdo->prepare("CALL sp_apply_remittance_to_invoices(:remittance_id, @allocations)");
    $stmt->execute([':remittance_id' => $remittanceId]);
    $result = $this->pdo->query("SELECT @allocations")->fetchColumn();
    return json_decode($result, true);
}
```

All stored procedure input parameters use the `:param_name` PDO named placeholder syntax. Output parameters use MySQL `@variable` syntax and are fetched in a subsequent `SELECT`.

---

# 5. EFRIS Integration Guidelines

## 5.1 Always Asynchronous

EFRIS submissions are always non-blocking. The user-facing transaction (invoice confirmation, POS sale) completes immediately. The EFRIS submission is enqueued and processed asynchronously.

**Flow:**

1. Invoice is confirmed → status set to `pending_efris` → record saved.
2. The `tr_invoices_after_status_change` database trigger inserts a row into `tbl_efris_queue`.
3. A background job (cron every 30 seconds, or on-demand trigger) processes the queue: calls the URA EFRIS API for each queued item.
4. On success: stores `fdn` (Fiscal Document Number) and `qr_code` on the invoice → status set to `issued`.
5. On failure: increments `retry_count`. After 3 failures: Finance Manager is alerted via email; status set to `efris_failed`.

## 5.2 Never Block the User Transaction on EFRIS Failure

If the EFRIS API is unreachable, slow, or returns an error:

- The invoice or POS receipt is **posted to the system** with status `pending_efris`.
- The cashier or sales manager is **not shown an error** — they see the transaction as complete.
- The EFRIS failure is visible only to the Finance Manager (EFRIS queue dashboard, alert email).
- URA allows a grace period for failed EFRIS submissions — the retry queue handles eventual consistency.

```php
// PROHIBITED — blocking EFRIS call
public function confirmInvoice(int $invoiceId): Invoice
{
    // ...
    $fdn = $this->efrisAdapter->submitSync($invoice); // BLOCKS the request
    $invoice->setFdn($fdn);
    // ...
}

// REQUIRED — async EFRIS enqueue
public function confirmInvoice(int $invoiceId): Invoice
{
    // ...
    $this->efrisQueue->enqueue($invoice->getId()); // non-blocking
    // ...
}
```

## 5.3 Always Queue on Failure

The EFRIS retry queue must handle the following failure modes without data loss:

- Network timeout (URA API unreachable).
- URA API returns a 5xx error.
- URA API returns a validation error (4xx) — these are logged separately as they require manual correction (e.g., incorrect TIN).

The `tbl_efris_queue` table columns:

| Column | Type | Description |
|---|---|---|
| `id` | INT UNSIGNED | Primary key |
| `invoice_id` | INT UNSIGNED | FK to `tbl_invoices.id` |
| `document_type` | ENUM | `invoice`, `credit_note`, `pos_receipt` |
| `payload` | JSON | The full EFRIS submission payload (stored at enqueue time) |
| `status` | ENUM | `pending`, `submitted`, `failed`, `manual_review` |
| `retry_count` | TINYINT | Number of submission attempts |
| `last_error` | TEXT | Last API error message |
| `created_at` | DATETIME | When enqueued |
| `submitted_at` | DATETIME or NULL | When successfully submitted |

---

# 6. Testing Requirements

## 6.1 PHPUnit for All Service Classes

Every public method in every Service class must have a corresponding PHPUnit test. Repository implementations are tested with integration tests against a test database.

**Test class naming:**

- Service test: `InvoiceServiceTest` in `tests/Application/Finance/InvoiceServiceTest.php`
- Repository integration test: `MySqlInvoiceRepositoryTest` in `tests/Infrastructure/Persistence/MySqlInvoiceRepositoryTest.php`

**Test method naming convention:**

```
test_[method_name]_[scenario]_[expected_outcome]
```

Examples:

- `test_confirmInvoice_whenInvoiceIsDraft_postsGlEntriesAndEnqueuesEfris()`
- `test_verifyRemittance_whenCreatorIsVerifier_throwsSegregationException()`
- `test_runPayroll_withStandardEmployee_calculatesCorrectPaye()`
- `test_closeProductionOrder_whenMassBalanceExceedsTolerance_throwsException()`

## 6.2 80% Minimum Coverage for Financial Services

The CI pipeline enforces an 80% line coverage gate on the following namespaces:

| Namespace | Coverage Requirement | Rationale |
|---|---|---|
| `BirdcErp\Application\Finance` | ≥ 80% | GL posting, journal entries, hash chain |
| `BirdcErp\Application\Sales` | ≥ 80% | Invoice lifecycle, EFRIS, sequential numbering |
| `BirdcErp\Application\Payroll` | ≥ 80% | PAYE, NSSF, LST calculations — regulatory compliance |
| `BirdcErp\Application\AgentDistribution` | ≥ 80% | Commission (BR-015), FIFO allocation (BR-002) |

Coverage below 80% in any of these namespaces blocks the PR merge. Coverage reports are generated by PHPUnit and stored as CI artefacts for review.

## 6.3 Test Data and Fixtures

- Tests never use production data.
- Fixtures for test data are in `tests/fixtures/`. Fixture files are JSON or PHP arrays — not SQL dumps.
- Tests that require a database use an in-memory SQLite database or a dedicated test MySQL schema (`birdc_erp_test`) that is reset before each test run.
- Never commit database credentials for the test schema to version control — use environment variables: `DB_TEST_NAME`, `DB_TEST_USER`, `DB_TEST_PASS`.

---

# 7. Code Review Standards

## 7.1 Reviewer Checklist

The reviewer checks every PR against this checklist before approving:

**Correctness:**

- [ ] The code does what the PR description claims.
- [ ] Business rules referenced in the PR template are correctly enforced.
- [ ] Edge cases described in the PR are handled (null inputs, zero amounts, empty collections).

**Security (per Section 3.3 PR template):**

- [ ] No raw SQL — 100% PDO prepared statements.
- [ ] All HTML output escaped.
- [ ] CSRF token present on new state-changing forms.
- [ ] RBAC check at the API endpoint level (not just UI).
- [ ] Audit log entry added for financial transactions.
- [ ] No credentials in code.
- [ ] No hardcoded business rules (DC-002 compliance).

**Code Quality:**

- [ ] `declare(strict_types=1)` on every new PHP file.
- [ ] PHPDoc on all public methods.
- [ ] No SQL in Controllers or Services.
- [ ] No `!!` (non-null assertion) in Kotlin without a justifying comment.
- [ ] Log statements use structured context arrays (not string concatenation).

**Tests:**

- [ ] New public service methods have corresponding PHPUnit tests.
- [ ] Coverage gate will pass (reviewer estimates based on changed lines).

## 7.2 Approval Requirements

| Change Type | Required Approvals |
|---|---|
| Standard feature PR | 1 approval (any senior developer) |
| Payroll calculation changes | 1 developer approval + Finance Director written sign-off |
| GL posting logic changes | 1 developer approval + Finance Director written sign-off |
| Commission calculation changes | 1 developer approval + Sales Manager acknowledgement |
| Security-related changes | 1 developer approval + project consultant review |
| Schema migrations (new tables or columns) | 1 developer approval + IT Administrator awareness |

Finance Director and Sales Manager sign-offs are recorded as PR comments (not GitHub approvals). The phrase "Approved — [Name], [Date]" in a comment from the relevant stakeholder is sufficient.

## 7.3 What Reviewers Do Not Do

- Reviewers do not rewrite code in comments — they raise the concern and let the author fix it.
- Reviewers do not approve PRs they have not read in full.
- Reviewers do not approve their own PRs (GitHub branch protection enforces this).
- Reviewers do not merge PRs until all required sign-offs are collected and CI passes.
