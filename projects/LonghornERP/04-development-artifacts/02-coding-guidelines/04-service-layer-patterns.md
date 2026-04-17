# Service Layer Patterns

## File Location Convention

All business logic shall reside in service classes under `src/Services/[Domain]/[ServiceName].php`. No business logic shall appear in API endpoint files, template files, or controller stubs.

Examples:
- `src/Services/Sales/InvoiceService.php`
- `src/Services/Payroll/PayslipService.php`
- `src/Services/Inventory/StockMovementService.php`

## Constructor Injection

Every service class shall declare `PDO $db` and `TenantContext $tenantContext` as constructor parameters. Additional collaborators (other services, mailers, PDF generators) shall also be injected — never instantiated inside the constructor body.

```php
<?php

declare(strict_types=1);

namespace LonghornERP\Services\Sales;

use LonghornERP\Infrastructure\TenantContext;

final class InvoiceService
{
    public function __construct(
        private readonly \PDO $db,
        private readonly TenantContext $tenantContext,
    ) {}
}
```

## Service Registration

All service classes shall be registered in `bootstrap/container.php` using PHP-DI 7.0 autowiring or explicit factory definitions. Services shall never be instantiated with `new` outside of `container.php` or test setup code.

```php
// Correct — container.php explicit definition
use LonghornERP\Services\Sales\InvoiceService;

return [
    InvoiceService::class => \DI\autowire(),
];
```

## Return Types

Service methods shall return typed arrays or dedicated Data Transfer Objects (DTOs). Raw PDO result sets (`PDOStatement` objects or untyped arrays) shall not be returned to calling code. The caller must not need to know how data was fetched.

```php
// Correct — returns typed array of DTOs
/** @return InvoiceDto[] */
public function listByStatus(string $status): array
{
    // ... query and map to InvoiceDto[]
}

// INCORRECT — returns raw statement result
public function listByStatus(string $status): \PDOStatement
{
    return $this->db->query('SELECT ...');
}
```

## HTTP Isolation

Service classes shall contain no HTTP-specific code. The following are prohibited inside any class under `src/Services/`:

- `$_GET`, `$_POST`, `$_REQUEST`, `$_FILES`, `$_COOKIE`
- `$_SESSION` (read or write)
- `header()` calls
- `echo` or `print` statements
- Direct `http_response_code()` calls

## API Endpoint Responsibility

API endpoints in `public/api/` are thin orchestrators. Each endpoint file shall follow this sequence:

1. Authenticate the request (session check or JWT verification).
2. Validate input using `respect/validation` 2.3.
3. Call the relevant service method.
4. Return the result via `ApiResponse::success($data)` or `ApiResponse::error($message, $code)`.

No database queries and no business logic shall appear directly in an API endpoint file.
