# Database Interaction Patterns

## Overview

This section defines the mandatory patterns governing all database access in Longhorn ERP. Every service class must conform to these patterns without exception. Deviations require written approval from the lead architect and must be documented as architecture decision records before implementation.

---

## PDO Injection

The application uses a single `PDO` singleton registered in the PHP-DI container. No service class may call `new PDO()` directly.

**Correct pattern:**

```php
final class InvoiceService
{
    public function __construct(
        private readonly PDO $pdo,
        private readonly SessionService $session,
        private readonly AuditService $audit,
    ) {}
}
```

The `PDO` instance is configured at container bootstrap time with:
- `PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION`
- `PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC`
- `PDO::ATTR_EMULATE_PREPARES => false`

`ATTR_EMULATE_PREPARES` is set to `false` to ensure that MySQL processes type information natively and to prevent SQL injection via emulated binding.

---

## Tenant Isolation Rule

Every query against an operational table must include a `tenant_id` filter. The `tenant_id` value always comes from `SessionService::getTenantId()`; it is never taken from request input, URL parameters, or any client-supplied value.

**Mandatory pattern:**

```php
$stmt = $this->pdo->prepare(
    'SELECT * FROM invoices WHERE id = :id AND tenant_id = :tenant_id'
);
$stmt->execute([
    ':id'        => $invoiceId,
    ':tenant_id' => $this->session->getTenantId(),
]);
```

`tenant_id` must be the first `WHERE` clause condition in all prepared statements. Queries that filter by `tenant_id` in a subquery or join condition without placing it first in the `WHERE` clause are non-conformant and must be refactored.

---

## Prepared Statements

All SQL is issued through PDO prepared statements. Raw string interpolation into SQL is prohibited. This applies to all query types: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `CALL` for stored procedures.

**Stored procedure call pattern:**

```php
$stmt = $this->pdo->prepare(
    'CALL sp_post_invoice_to_gl(:invoice_id, :tenant_id)'
);
$stmt->execute([
    ':invoice_id' => $invoiceId,
    ':tenant_id'  => $this->session->getTenantId(),
]);
```

The five stored procedures and their call signatures are:

| Procedure | Parameters | Called By |
|---|---|---|
| `sp_post_invoice_to_gl` | `:invoice_id`, `:tenant_id` | `InvoiceService::postInvoiceToGL()` |
| `sp_post_purchase_to_gl` | `:document_id`, `:tenant_id` | `GRNService::postGRN()`, `SupplierInvoiceService::postToGL()` |
| `sp_post_return_to_gl` | `:invoice_id`, `:tenant_id` | `InvoiceService::voidInvoice()` |
| `sp_generate_entry_number` | `:tenant_id`, `:period_id` | `AccountingService::postJournal()` |
| `sp_get_account_mapping` | `:tenant_id`, `:mapping_code` | `InvoiceService`, `BankReconciliationService` |

---

## Transaction Boundaries

Every `post*` method that writes to more than one table must wrap its writes in an explicit transaction. The transaction is committed only after all writes succeed. Any exception causes an immediate rollback.

**Mandatory pattern:**

```php
public function postGRN(int $grnId): void
{
    $this->pdo->beginTransaction();
    try {
        // 1. Post stock ledger movements
        // 2. Call stored procedure for GL
        // 3. Update GRN status
        // 4. Log to AuditService (inside the same transaction)
        $this->pdo->commit();
    } catch (\Throwable $e) {
        $this->pdo->rollBack();
        throw $e;
    }
}
```

`AuditService::log()` is called inside the `try` block, before `commit()`. This ensures the audit record is written atomically with the state change it records. If the transaction rolls back, the audit record is also discarded.

---

## Audit Log Integration

`AuditService::log()` is called inside every state-changing transaction for all `CREATE`, `UPDATE`, `DELETE`, `POST`, and `VOID` operations. The service captures the before and after state as JSON snapshots.

The `audit_logs` table is INSERT-only. The MySQL user account used by the application holds no `UPDATE` or `DELETE` privilege on `audit_logs`. This constraint is enforced at the database permission level, not solely at the application level.

---

## View Usage

Read-heavy reporting queries use database views rather than raw table aggregations in PHP. The authoritative view list is:

| View | Used By |
|---|---|
| `v_current_stock` | `ItemService::getStockBalance()` |
| `v_low_stock_items` | `ItemService::getLowStockItems()` |
| `v_trial_balance` | `AccountingService::getTrialBalance()` |
| `v_customer_aging` | `CustomerService::getAgingReport()` |
| `v_supplier_aging` | `SupplierService::getAgingReport()` |
| `v_vat_return` | `TaxService::generateVATReturn()` |
| `v_bsc_scorecard` | `StrategyService::generateScorecardReport()` |

Views are read-only from the application layer. No `INSERT`, `UPDATE`, or `DELETE` is issued against a view.

---

## Branch Isolation

Where the business domain requires branch-level data segregation (stock balances, POS sessions, GRNs), queries include both `tenant_id` and `branch_id` filters. The `branch_id` value always comes from `SessionService::getBranchId()`. Reports that aggregate across branches require explicit superadmin or cross-branch permission (`CROSS_BRANCH_REPORT`).

---

## Connection Lifecycle

The PDO singleton is created once per request by `ContainerFactory::build()`. Connection pooling is not implemented at the PHP layer; connection reuse relies on MySQL's `wait_timeout` and the web server's persistent process model. Long-running CLI processes (e.g., payroll batch runs, depreciation jobs) must call `PDO::setAttribute(PDO::ATTR_PERSISTENT, false)` to prevent stale connections.
