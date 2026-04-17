# Database Access Patterns

## Driver Requirement

All database access shall use PDO exclusively. Raw MySQLi calls are prohibited. The PDO connection is obtained via the PHP-DI container as `$this->db`; it shall never be instantiated directly inside a class.

```php
// Correct — injected via constructor
public function __construct(
    private readonly \PDO $db,
    private readonly TenantContext $tenantContext,
) {}

// INCORRECT — direct instantiation
$this->db = new \PDO('mysql:host=localhost;dbname=longhorn', $user, $pass);
```

## Connection Source

The PDO instance shall be registered in `bootstrap/container.php` and injected by PHP-DI 7.0 autowiring. Service classes shall never reference global variables or static factories to obtain the connection.

## Standard Query Pattern

Developers shall follow this pattern for all data retrieval:

```php
$tenantId = $this->tenantContext->getTenantId();
$stmt = $this->db->prepare(
    'SELECT id, reference, total
     FROM invoices
     WHERE tenant_id = ?
       AND status = ?
     ORDER BY created_at DESC'
);
$stmt->execute([$tenantId, $status]);
$rows = $stmt->fetchAll(\PDO::FETCH_ASSOC);
```

## Tenant ID Placement in WHERE Clauses

`tenant_id` shall always appear as the first condition in every WHERE clause on operational tables. This placement leverages the composite index `(tenant_id, ...)` present on every operational table and makes isolation intent explicit to reviewers.

```php
// Correct — tenant_id first
'WHERE tenant_id = ? AND id = ?'

// Incorrect — tenant_id not first
'WHERE id = ? AND tenant_id = ?'
```

## Transactions

Multi-statement operations that must succeed or fail atomically shall use PDO transactions. Developers shall always catch exceptions and roll back on failure.

```php
$this->db->beginTransaction();
try {
    $this->db->prepare('INSERT INTO journal_entries ...')
             ->execute([...]);
    $this->db->prepare('UPDATE account_balances ...')
             ->execute([...]);
    $this->db->commit();
} catch (\Throwable $e) {
    $this->db->rollBack();
    throw $e;
}
```

## Date Storage

Dates shall be stored in MySQL `DATE` columns using the format `Y-m-d` (e.g., `2026-04-05`). Datetime values shall use `DATETIME` columns in `Y-m-d H:i:s` format. Timestamps in epoch format are acceptable only for audit log `created_at` columns where indexed range scans are required.

## Numeric Storage

Numeric values shall be stored without thousand separators. Decimal columns shall carry the exact precision required by the business rule (e.g., `DECIMAL(15,2)` for currency). The application layer applies `number_format()` only at display time.

```php
// Correct — store raw value
$amount = 1500000.00;

// INCORRECT — storing formatted string
$amount = '1,500,000.00';
```

## Output Formatting

All numeric values retrieved from the database shall be formatted for display using `number_format()`. All string values displayed in HTML shall be wrapped in `htmlspecialchars($value, ENT_QUOTES, 'UTF-8')` before rendering.

```php
// Correct
echo htmlspecialchars(number_format((float) $row['total'], 2), ENT_QUOTES, 'UTF-8');
```
