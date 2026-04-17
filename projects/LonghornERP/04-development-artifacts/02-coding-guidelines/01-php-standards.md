# PHP 8.3 Coding Standards

## Strict Types Declaration

All PHP files shall include `declare(strict_types=1);` as the first statement after the opening `<?php` tag. No exceptions are permitted. Files missing this declaration shall be rejected by code review.

```php
<?php

declare(strict_types=1);
```

## Autoloading and Namespace Conventions

Developers shall follow PSR-4 autoloading. The fully qualified class name shall mirror the file system path relative to `src/`.

- Namespace root: `LonghornERP\`
- Class `LonghornERP\Services\Sales\InvoiceService` shall reside at `src/Services/Sales/InvoiceService.php`.
- One class per file — no exceptions.

## Code Style (PSR-12)

All PHP source files shall conform to PSR-12. Compliance is enforced automatically by PHP CS Fixer 3.64. Developers shall run `vendor/bin/php-cs-fixer fix` before every commit. A CI check shall fail any pull request that introduces PSR-12 violations.

## Static Analysis (PHPStan Level 8)

All code shall pass PHPStan static analysis at level 8 with zero errors. Developers shall run `vendor/bin/phpstan analyse` before every commit. Baseline suppressions are prohibited — every error must be resolved in code.

## Type Declarations

Type declarations are mandatory on all function parameters and return types. The `mixed` type is prohibited unless the function explicitly handles multiple unrelated types and a comment documents each accepted type.

```php
// Correct
public function findById(int $id, int $tenantId): ?Invoice
{
    // ...
}

// Incorrect — missing parameter and return types
public function findById($id, $tenantId)
{
    // ...
}
```

## Named Arguments

Developers shall use named arguments on any function call that passes 3 or more parameters, or on any call where the argument order is non-obvious.

```php
// Correct
$this->mailer->send(
    to: $recipient,
    subject: $subject,
    body: $body,
    attachments: $attachments,
);

// Acceptable for 2 parameters with obvious order
$this->db->prepare($sql);
```

## Match Expressions Over Switch Statements

Developers shall use `match` expressions in place of `switch` statements wherever the value being tested maps to a scalar result. `match` performs strict comparison and eliminates fall-through bugs.

```php
// Correct
$label = match($status) {
    'draft'    => 'Draft',
    'approved' => 'Approved',
    'paid'     => 'Paid',
    default    => throw new \InvalidArgumentException("Unknown status: {$status}"),
};

// Incorrect — switch permits fall-through and loose comparison
switch ($status) {
    case 'draft':
        $label = 'Draft';
        break;
    // ...
}
```

## Null Coalescing Operator

Developers shall use the null coalescing operator (`??`) in place of ternary expressions that test `isset()` or nullable values.

```php
// Correct
$name = $input['name'] ?? 'Unknown';

// Incorrect
$name = isset($input['name']) ? $input['name'] : 'Unknown';
```
