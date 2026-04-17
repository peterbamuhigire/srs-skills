# 1. PHP 8.3+ Standards

## 1.1 Language Version and Strict Typing

The BIRDC ERP backend runs on PHP 8.3 or higher. Every PHP file in the codebase must begin with:

```php
<?php
declare(strict_types=1);
```

`strict_types=1` is mandatory on every file without exception. It is not optional for "simple" files. Pull requests that include files missing this declaration are rejected at the linter stage (PHPStan level 8 enforces this).

PHP 8.x features that are actively used in this project:

- Named arguments for constructor injection clarity.
- Match expressions instead of switch for value mapping.
- Nullsafe operator (`?->`) for optional chain traversal.
- Readonly properties for Value Objects and DTOs.
- Enum types for status fields (invoice status, batch quality status, production order status).
- Union types and intersection types where appropriate.

## 1.2 PSR-4 Autoloading and Namespace Conventions

All classes follow PSR-4 autoloading. The `composer.json` autoload section maps:

```json
{
  "autoload": {
    "psr-4": {
      "BirdcErp\\": "src/"
    }
  }
}
```

### Namespace Hierarchy

```
BirdcErp\
  ├── Domain\                  — Domain entities, Value Objects, Enums
  │   ├── Finance\
  │   ├── Sales\
  │   ├── Inventory\
  │   ├── Production\
  │   ├── HumanResources\
  │   └── ...
  ├── Application\             — Use cases / application services
  │   ├── Finance\
  │   ├── Sales\
  │   └── ...
  ├── Infrastructure\          — Repositories, external service adapters
  │   ├── Persistence\         — Repository implementations
  │   ├── Efris\               — URA EFRIS API adapter
  │   ├── MobileMoney\         — MTN MoMo / Airtel Money adapters
  │   └── Biometric\           — ZKTeco adapter
  └── Http\                    — Controllers, Middleware, Request/Response
      ├── Controllers\
      ├── Middleware\
      └── Api\
```

### Naming Conventions

| Construct | Convention | Example |
|---|---|---|
| Class | `PascalCase` | `InvoiceService` |
| Interface | `PascalCase` + `Interface` suffix | `InvoiceRepositoryInterface` |
| Abstract class | `PascalCase` + `Abstract` suffix | `AbstractPaymentProcessor` |
| Method | `camelCase` | `calculateCommission()` |
| Property | `camelCase` | `$agentCashBalance` |
| Constant | `UPPER_SNAKE_CASE` | `MAX_FLOAT_LIMIT` |
| Enum case | `PascalCase` | `InvoiceStatus::PendingEfris` |

## 1.3 PSR-12 Code Style

All PHP code must conform to PSR-12. Key rules enforced by PHP_CodeSniffer in CI:

- 4-space indentation (no tabs).
- Opening brace for classes and methods on the same line as the declaration.
- One blank line between method definitions within a class.
- Opening parenthesis of a function call on the same line as the function name.
- All `use` statements at the top of the file, grouped: PHP built-ins, then external packages, then project namespaces.
- Maximum line length: 120 characters.
- Visibility (`public`, `protected`, `private`) declared on all properties and methods.

## 1.4 PHP-DI Dependency Injection Container

The project uses PHP-DI as the dependency injection container. All services, repositories, and controllers are wired through the container.

### Container Configuration

The container is configured in `config/container.php`. All bindings must be explicit — no auto-wiring in production configuration. Example binding:

```php
use BirdcErp\Application\Finance\InvoiceService;
use BirdcErp\Infrastructure\Persistence\MySqlInvoiceRepository;
use BirdcErp\Domain\Finance\InvoiceRepositoryInterface;

return [
    InvoiceRepositoryInterface::class => DI\autowire(MySqlInvoiceRepository::class),
    InvoiceService::class => DI\autowire(InvoiceService::class),
];
```

### Constructor Injection Rule

All dependencies are injected through the constructor. Property injection and method injection are prohibited. A class with more than 5 constructor dependencies is a signal to decompose it.

## 1.5 Service and Repository Pattern

### Service Layer

Services contain business logic. They orchestrate repositories and enforce business rules. Services never access the database directly.

```php
<?php
declare(strict_types=1);

namespace BirdcErp\Application\Finance;

use BirdcErp\Domain\Finance\InvoiceRepositoryInterface;
use BirdcErp\Domain\Finance\Invoice;
use BirdcErp\Domain\Finance\InvoiceStatus;
use BirdcErp\Infrastructure\Efris\EfrisAdapter;

final class InvoiceService
{
    public function __construct(
        private readonly InvoiceRepositoryInterface $invoiceRepository,
        private readonly EfrisAdapter $efrisAdapter,
        private readonly GlPostingService $glPostingService,
    ) {}

    public function confirmInvoice(int $invoiceId): Invoice
    {
        $invoice = $this->invoiceRepository->findById($invoiceId);
        $invoice->confirm(); // domain logic — validates balance, assigns sequential number
        $this->glPostingService->postInvoice($invoice); // DR AR / CR Revenue + DR COGS / CR Inventory
        $this->efrisAdapter->submitAsync($invoice); // non-blocking EFRIS submission
        return $this->invoiceRepository->save($invoice);
    }
}
```

### Repository Layer

Repositories abstract all database access. The interface is defined in the Domain layer; the implementation is in the Infrastructure layer.

```php
<?php
declare(strict_types=1);

namespace BirdcErp\Domain\Finance;

interface InvoiceRepositoryInterface
{
    public function findById(int $id): Invoice;
    public function findByStatus(InvoiceStatus $status): array;
    public function save(Invoice $invoice): Invoice;
    public function nextSequentialNumber(): string; // BR-009 enforcement
}
```

Repository implementations use PDO exclusively. See Section 6 (Security Requirements) for SQL injection rules.

## 1.6 Exception Handling

All custom exceptions extend a base `BirdcErp\Domain\DomainException` class. Exception class names describe the business rule violation:

```
BirdcErp\Domain\Finance\
  InvoiceAlreadyConfirmedException
  InvoiceSequenceGapException          — BR-009
  PayrollAlreadyLockedException        — BR-010

BirdcErp\Domain\Inventory\
  AgentFloatLimitExceededException     — BR-006
  FefoViolationException               — BR-007

BirdcErp\Domain\Production\
  MassBalanceExceededException         — BR-008
  QcGateBlockedException               — BR-004
```

All unhandled exceptions are caught by a global exception handler that:

1. Logs the full stack trace to the application log.
2. Sends an email alert to the IT Administrator for `E_ERROR` level exceptions.
3. Returns the standard error envelope (Section 4) with a sanitised message — no stack traces in API responses.

## 1.7 Logging Standards

The project uses a PSR-3 compatible logger (Monolog). Log channels:

| Channel | File | Content |
|---|---|---|
| `app` | `logs/app.log` | General application events — service method calls, state transitions |
| `security` | `logs/security.log` | Authentication events, failed logins, permission denials, 2FA events |
| `financial` | `logs/financial.log` | All financial postings — JE, invoice confirm, payroll lock, remittance verify |
| `efris` | `logs/efris.log` | Every EFRIS API request and response |
| `error` | `logs/error.log` | All uncaught exceptions |

Log format (JSON structured logging):

```json
{
  "timestamp": "2026-04-05T08:23:11+03:00",
  "channel": "financial",
  "level": "info",
  "message": "Invoice confirmed",
  "context": {
    "invoice_id": 1234,
    "invoice_number": "INV-2026-0123",
    "user_id": 42,
    "ip": "192.168.1.55"
  }
}
```

Log files are rotated daily. 90-day local retention; then archived to the offsite backup. Logs are never deleted within the 7-year retention window required by DC-003.
