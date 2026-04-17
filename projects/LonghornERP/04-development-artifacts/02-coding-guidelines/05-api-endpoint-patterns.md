# REST API Endpoint Conventions

## File Location

Web API endpoint files shall reside at `public/api/[domain]/[action].php`. Mobile API endpoint files shall reside at `public/api/mobile/v1/[domain]/[action].php`. No API logic shall be placed in subdirectories deeper than these paths without a documented reason in `_context/`.

Examples:
- `public/api/sales/save-invoice.php`
- `public/api/inventory/adjust-stock.php`
- `public/api/mobile/v1/sales/get-invoice.php`

## Authentication

Every endpoint shall verify authentication as its first executable action, before reading any input or calling any service.

- Web endpoints shall check the session (`LONGHORN_ERP_SESSION`) and reject unauthenticated requests with HTTP 401.
- Mobile endpoints shall include `_mobile_auth.php` to verify the JWT Bearer token. Claims extracted from the JWT (`tenant_id`, `user_id`, `role`, enabled modules) shall populate `TenantContext` for the request lifetime.

```php
<?php

declare(strict_types=1);

// Web endpoint authentication check
require_once __DIR__ . '/../../_session_check.php';

// Mobile endpoint authentication check
require_once __DIR__ . '/../_mobile_auth.php';
// $jwtClaims is now available with tenant_id, user_id, role
```

## Input Validation

All user-supplied input shall be validated using `respect/validation` 2.3 before being passed to any service method. Validation failures shall return HTTP 400 with a structured error response.

```php
use Respect\Validation\Validator as v;

$body = json_decode(file_get_contents('php://input'), true) ?? [];

try {
    v::key('customer_id', v::intVal()->positive())
     ->key('amount', v::floatVal()->positive())
     ->assert($body);
} catch (\Respect\Validation\Exceptions\ValidationException $e) {
    http_response_code(400);
    echo ApiResponse::error($e->getMessage(), 400);
    exit;
}
```

## Standardised Response Format

All endpoints shall return responses exclusively via `ApiResponse::success($data)` or `ApiResponse::error($message, $code)`. Raw `echo json_encode(...)` calls are prohibited in endpoint files.

```php
// Success
http_response_code(201);
echo ApiResponse::success(['invoice_id' => $newId]);

// Error
http_response_code(404);
echo ApiResponse::error('Invoice not found', 404);
```

## HTTP Status Code Usage

Endpoints shall return the following status codes according to the outcome:

| Code | Condition |
|---|---|
| 200 | Successful read or update |
| 201 | Successful resource creation |
| 400 | Validation failure or malformed request |
| 401 | Missing or invalid authentication |
| 403 | Authenticated but lacks required permission or module access |
| 404 | Resource not found within the tenant's scope |
| 500 | Unhandled server error |

## Error Response Safety

Stack traces, exception messages containing file paths, and raw PHP error output shall never appear in API responses. All unhandled exceptions shall be caught at the endpoint level, logged server-side, and returned as a generic HTTP 500 message.

```php
try {
    $result = $invoiceService->create($tenantId, $body);
    echo ApiResponse::success($result);
} catch (\Throwable $e) {
    error_log($e->getMessage() . ' in ' . $e->getFile() . ':' . $e->getLine());
    http_response_code(500);
    echo ApiResponse::error('An internal error occurred. Please contact support.', 500);
}
```

## Mobile API JWT Verification

All files under `public/api/mobile/v1/` shall include `_mobile_auth.php` as the first `require_once` statement. This file validates the `Authorization: Bearer <token>` header using `firebase/php-jwt` 7.0, populates `TenantContext`, and terminates the request with HTTP 401 if the token is absent, expired, or invalid.
