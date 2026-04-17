# 1. PHP Coding Standards

## 1.1 Strict Types and File Header

Every PHP file must open with exactly:

```php
<?php
declare(strict_types=1);
```

No blank line between `<?php` and `declare`. No other content before `declare`. This is checked by PHPStan level 8 in CI.

## 1.2 PSR-12 Style Examples

### Class Definition

```php
<?php
declare(strict_types=1);

namespace BirdcErp\Application\AgentDistribution;

use BirdcErp\Domain\AgentDistribution\AgentRepositoryInterface;
use BirdcErp\Domain\AgentDistribution\RemittanceRepositoryInterface;
use BirdcErp\Domain\AgentDistribution\Remittance;
use BirdcErp\Domain\Finance\GlPostingServiceInterface;

final class RemittanceService
{
    public function __construct(
        private readonly AgentRepositoryInterface $agentRepository,
        private readonly RemittanceRepositoryInterface $remittanceRepository,
        private readonly GlPostingServiceInterface $glPostingService,
    ) {}

    public function verifyRemittance(int $remittanceId, int $verifiedByUserId): Remittance
    {
        $remittance = $this->remittanceRepository->findById($remittanceId);

        if ($remittance->getCreatedBy() === $verifiedByUserId) {
            throw new \BirdcErp\Domain\AgentDistribution\SegregationOfDutiesException(
                'The person who created a remittance cannot verify it (BR-003).'
            );
        }

        $remittance->verify($verifiedByUserId);
        $this->glPostingService->postRemittance($remittance);

        return $this->remittanceRepository->save($remittance);
    }
}
```

**Key style rules visible in this example:**

- `final` on all concrete service and repository classes unless inheritance is explicitly required.
- Trailing comma after the last constructor parameter.
- One blank line between the constructor and the first method.
- Method body starts immediately after the opening brace — no blank line at the start.
- `throw` statements use the fully qualified class name only when the `use` statement is not present.

### PHPDoc Blocks

PHPDoc blocks are required on all public methods. Private methods require a docblock only if the method's purpose is not obvious from the name and parameter names alone.

```php
/**
 * Applies a verified remittance to the agent's outstanding invoices in FIFO order.
 *
 * Enforces BR-002 (FIFO allocation) via stored procedure sp_apply_remittance_to_invoices.
 * Commission accrues on cleared invoices per BR-015.
 *
 * @param  int   $remittanceId  The verified remittance to allocate.
 * @return array<int, float>    Map of invoice_id => amount_cleared.
 * @throws RemittanceAlreadyAllocatedException If the remittance has already been allocated.
 */
public function allocateRemittance(int $remittanceId): array
{
    // ...
}
```

**PHPDoc requirements:**

- `@param` for every parameter with type and description.
- `@return` with type and description of the return value.
- `@throws` for every exception the method can throw.
- No `@author` or `@date` tags — git blame provides this information.
- No redundant docblocks (`/** Gets the name. */` above `getName()` adds no value — omit it).

## 1.3 Service Layer Pattern

Services contain all business logic. Rules:

- Services never extend a base class (use constructor injection, not inheritance).
- Services never instantiate their dependencies with `new` — all dependencies are injected.
- Services never access `$_REQUEST`, `$_POST`, `$_GET`, or any superglobal — those are handled in Controllers.
- Services never render HTML or return HTTP responses.
- One service class per bounded context feature (e.g., `InvoiceService`, not a single `SalesService` that handles invoices, credit notes, customers, and pricing).

## 1.4 Repository Layer Pattern

Repositories abstract all database access. Rules:

- The interface is in the Domain layer; the implementation is in the Infrastructure layer.
- Repository methods return Domain objects, not raw arrays or `stdClass` instances.
- No business logic in repositories — a repository finds and persists; it does not calculate.
- No raw SQL in controllers or services — queries belong in repositories only.
- Repository methods that could return 0 results return a typed array or `null`; they never return `false`.

### Repository Method Naming

| Action | Method Name Pattern | Example |
|---|---|---|
| Find one by primary key | `findById(int $id)` | `$invoiceRepository->findById(1234)` |
| Find one by other criteria | `findBy[Criteria](...)` | `findByInvoiceNumber(string $number)` |
| Find multiple | `findAll[Criteria](...)` | `findAllByStatus(InvoiceStatus $status)` |
| Persist (insert or update) | `save(Entity $entity)` | `$invoiceRepository->save($invoice)` |
| Delete (soft) | `softDelete(int $id, int $deletedBy)` | N/A for financial tables |
| Custom query | descriptive verb + noun | `getAgentCashBalance(int $agentId)` |

## 1.5 Exception Handling

**Rule:** Never use `@` error suppression. Never catch a `Throwable` and swallow it silently.

```php
// PROHIBITED — swallowed exception
try {
    $this->efrisAdapter->submit($invoice);
} catch (\Exception $e) {
    // do nothing
}

// REQUIRED — log and handle or rethrow
try {
    $this->efrisAdapter->submit($invoice);
} catch (EfrisApiException $e) {
    $this->logger->error('EFRIS submission failed', [
        'invoice_id' => $invoice->getId(),
        'error' => $e->getMessage(),
    ]);
    $this->efrisRetryQueue->enqueue($invoice->getId());
    // Do NOT re-throw — EFRIS failure must never block the user transaction (DC-005)
}
```

**Exception hierarchy rules:**

- Catch the most specific exception type possible.
- Only catch `\Exception` or `\Throwable` at the top-level error handler.
- Business rule violations throw domain exceptions (never `\RuntimeException` or `\InvalidArgumentException` for business logic).

## 1.6 Logging Standards

Use dependency-injected `LoggerInterface` (PSR-3). Never use `error_log()`, `var_dump()`, or `print_r()` in production code.

```php
// PROHIBITED
error_log("Invoice confirmed: " . $invoiceId);

// REQUIRED
$this->logger->info('Invoice confirmed', [
    'invoice_id' => $invoiceId,
    'invoice_number' => $invoice->getNumber(),
    'user_id' => $userId,
]);
```

Log levels used in this project:

| Level | When to use |
|---|---|
| `debug` | Development-only diagnostic information. Never in production-facing paths. |
| `info` | Normal business events: invoice confirmed, payroll run completed, remittance verified. |
| `warning` | Unexpected but recoverable states: EFRIS queued after first attempt fails, sync conflict detected. |
| `error` | Failures requiring attention: EFRIS failed after 3 retries, hash chain integrity failure, sync job exhausted retries. |
| `critical` | System-level failures: database connection lost, application exception handler triggered. |
