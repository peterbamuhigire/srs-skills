# Service Layer Architecture

## 4.1 Principle

All business logic resides in the service layer. No page handler, API endpoint, or middleware layer shall contain domain logic directly. This separation ensures that business rules are testable in isolation (via PHPUnit 11.2), reusable across web and mobile entry points, and auditable as distinct units during code review.

## 4.2 Service Directory Structure

Services are organised by domain under `src/Services/`:

```
src/
└── Services/
    ├── Accounting/
    │   ├── GeneralLedgerService.php
    │   ├── AccountsPayableService.php
    │   └── ...
    ├── Inventory/
    │   ├── StockService.php
    │   └── ...
    ├── Sales/
    │   ├── InvoiceService.php
    │   └── ...
    ├── Procurement/
    │   └── ...
    ├── HR/
    │   └── ...
    ├── Manufacturing/
    │   └── ...
    ├── PLM/
    │   └── ...
    ├── Transportation/
    │   └── ...
    ├── Cooperative/
    │   └── ...
    ├── Auth/
    │   └── ...
    └── Platform/
        ├── TenantContext.php
        ├── ModuleGate.php
        └── ...
```

Each domain directory maps directly to the corresponding module code. Services within a domain directory may call other services within the same domain. Cross-domain calls (e.g., `InvoiceService` calling `GeneralLedgerService` to post a receivable) are explicitly modelled as inter-service dependencies registered in the container.

For the industrial operating model, the service layer shall preserve these ownership boundaries:

- `PLM` owns engineering items, revisions, changes, document control, and downstream release publication.
- `Manufacturing` owns routings, production execution, work-centre operations, genealogy, quality execution, and costing.
- `Transportation` owns shipment planning, dispatch, trip execution, proof capture, transport exceptions, and freight settlement.
- `Assets` may expose vehicle-reference data to `Transportation`, but it does not own trip state or dispatch logic.

## 4.3 Dependency Injection Container

All services are registered in `bootstrap/container.php` using PHP-DI 7.0. The container is the single authorised mechanism for resolving service instances. Direct `new ServiceClass()` instantiation outside the container is prohibited.

Registration follows the constructor injection pattern:

```php
// bootstrap/container.php (illustrative - prospective)
$container->set(InvoiceService::class, function (Container $c) {
    return new InvoiceService(
        $c->get(TenantContext::class),
        $c->get(GeneralLedgerService::class),
        $c->get(PDO::class)
    );
});
```

Services are injected into:

1. API endpoint files under `public/api/[domain]/endpoint.php` - resolved from the container at the top of each file.
2. Page handler files under `public/[domain]/page.php` - resolved from the container at the top of each file.

## 4.4 TenantContext Injection into Services

Every service that accesses operational data shall receive `TenantContext` as the first constructor parameter. The service uses `$this->tenantContext->getTenantId()` as the value for the `tenant_id` clause on every SQL query. No service shall accept a `tenant_id` parameter from a caller - the tenant identity is always derived from the injected context.

```php
// Illustrative service constructor (prospective)
class InvoiceService
{
    public function __construct(
        private readonly TenantContext $tenantContext,
        private readonly GeneralLedgerService $gl,
        private readonly PDO $pdo
    ) {}
}
```

## 4.5 ApiResponse Standard

All REST API endpoints shall return responses using the `ApiResponse` class. The class enforces the standardised JSON envelope defined in Section 9:

```
{ "success": bool, "data": {}, "error": {} }
```

`ApiResponse` provides the following static factory methods:

- `ApiResponse::success(mixed $data, int $httpCode = 200)` - returns a success envelope.
- `ApiResponse::error(string $message, string $code, int $httpCode)` - returns an error envelope.

No endpoint shall write raw `echo json_encode(...)` output. All output is routed through `ApiResponse`.

## 4.6 JavaScript Architecture

Each page that requires client-side behaviour shall have exactly 1 dedicated JavaScript file at `public/js/[page-name].js`. Inline `<script>` blocks in PHP page files are prohibited.

JavaScript files shall reference API endpoints using relative paths (e.g., `./api/invoices/create.php`). Absolute URL construction in JavaScript is prohibited, as it breaks multi-path deployments.

All AJAX calls made from page JavaScript shall include the `X-CSRF-Token` header populated from the session token injected into the page by the PHP renderer.

## 4.7 Database Access Standards

All database access shall use PHP Data Objects (PDO) with prepared statements. Raw SQL string concatenation is prohibited. This applies to all service classes, stored procedure calls, and any direct PDO usage in API endpoints.

```php
// Required pattern (prospective):
$stmt = $this->pdo->prepare(
    'SELECT * FROM invoices WHERE tenant_id = ? AND id = ?'
);
$stmt->execute([$this->tenantContext->getTenantId(), $invoiceId]);
```

Stored procedures in MySQL 9.1 are used for complex multi-step operations (General Ledger posting, sequential document numbering, account mapping). Stored procedure calls shall also use PDO prepared statement syntax (`CALL procedure_name(?, ?)`) and shall never interpolate values into the call string.
