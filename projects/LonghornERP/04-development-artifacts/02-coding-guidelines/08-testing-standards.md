# Testing Standards

## Test File Location and Naming

All PHPUnit test files shall reside under `tests/[Domain]/[ServiceName]Test.php`. The directory structure shall mirror `src/Services/`.

Examples:
- `tests/Sales/InvoiceServiceTest.php`
- `tests/Payroll/PayslipServiceTest.php`
- `tests/Inventory/StockMovementServiceTest.php`

## Class and Method Naming

Test classes shall extend `PHPUnit\Framework\TestCase` and follow the naming convention `[ServiceName]Test`.

Test methods shall follow the convention `test[MethodName][Scenario]`. The scenario segment shall describe the test condition in plain English, not the expected output.

```php
// Correct method names
public function testCreateInvoiceWithValidData(): void {}
public function testCreateInvoiceThrowsOnNegativeAmount(): void {}
public function testListInvoicesReturnsEmptyArrayForNewTenant(): void {}

// INCORRECT — scenario is too vague
public function testCreate(): void {}
public function test1(): void {}
```

## Coverage Requirement

Every service class shall achieve a minimum of 80% line coverage as measured by PHPUnit with Xdebug. Coverage reports shall be generated during CI runs. A pull request that reduces a service class below 80% line coverage shall be blocked from merging.

## Tenant Isolation Assertion

Every service test shall include at least 1 negative test case that verifies tenant isolation. This test shall:

1. Create or seed data under `tenant_id` A.
2. Execute the method under test using a different `tenant_id` B.
3. Assert that no data from tenant A is returned or affected.

```php
public function testListInvoicesDoesNotReturnOtherTenantData(): void
{
    // Seed data for tenant 1
    $this->seedInvoice(tenantId: 1, reference: 'INV-001');

    // Query as tenant 2
    $tenantContext = $this->createTenantContext(tenantId: 2);
    $service = new InvoiceService($this->db, $tenantContext);

    $results = $service->listByStatus('draft');

    $this->assertEmpty($results, 'Tenant 2 must not receive Tenant 1 invoices.');
}
```

## Static Analysis Gate

Developers shall run `vendor/bin/phpstan analyse` at level 8 before every commit. Zero PHPStan errors are required. Commits that introduce PHPStan errors shall be rejected by the CI pipeline.

## Code Style Gate

Developers shall run `vendor/bin/php-cs-fixer fix` before every commit to apply PSR-12 formatting automatically. The CI pipeline shall run `php-cs-fixer check --dry-run` and fail the build if any unformatted file is detected.

## Pre-Commit Checklist Summary

Before creating a commit, every developer shall verify all of the following:

1. `vendor/bin/phpstan analyse` completes with zero errors.
2. `vendor/bin/php-cs-fixer fix` has been run and all changes are staged.
3. `vendor/bin/phpunit` passes with no failures or errors.
4. New service methods have corresponding tests in `tests/[Domain]/`.
5. Line coverage for affected service classes is ≥ 80%.
