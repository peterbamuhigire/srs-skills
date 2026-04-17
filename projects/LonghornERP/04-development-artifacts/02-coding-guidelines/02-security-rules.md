# Mandatory Security Rules

The rules in this section are non-negotiable. Violation of any rule constitutes a defect requiring immediate remediation before the affected code is merged or deployed. Severity levels map to the project's defect classification scheme.

---

## Rule S-01 — Tenant Isolation

**Severity of violation: Critical.**

Developers shall NEVER accept `tenant_id` from request parameters, HTTP headers, or the request body. The `tenant_id` for every database query shall be obtained exclusively from `$this->tenantContext->getTenantId()`.

```php
// Correct — tenant_id sourced from TenantContext
public function listInvoices(): array
{
    $tenantId = $this->tenantContext->getTenantId();
    $stmt = $this->db->prepare(
        'SELECT * FROM invoices WHERE tenant_id = ? ORDER BY created_at DESC'
    );
    $stmt->execute([$tenantId]);
    return $stmt->fetchAll(\PDO::FETCH_ASSOC);
}

// INCORRECT — tenant_id accepted from request input (Critical defect)
public function listInvoices(): array
{
    $tenantId = $_GET['tenant_id']; // NEVER do this
    $stmt = $this->db->prepare('SELECT * FROM invoices WHERE tenant_id = ?');
    $stmt->execute([$tenantId]);
    return $stmt->fetchAll(\PDO::FETCH_ASSOC);
}
```

---

## Rule S-02 — Prepared Statements

**Severity of violation: Critical.**

Developers shall NEVER concatenate user input into SQL strings. ALL database queries shall use PDO prepared statements with positional (`?`) or named (`:param`) placeholders.

```php
// Correct — parameterised query
$stmt = $this->db->prepare(
    'SELECT * FROM customers WHERE tenant_id = ? AND email = ?'
);
$stmt->execute([$tenantId, $email]);

// INCORRECT — string concatenation (Critical defect; SQL injection risk)
$stmt = $this->db->query(
    "SELECT * FROM customers WHERE tenant_id = $tenantId AND email = '$email'"
);
```

---

## Rule S-03 — Output Escaping

**Severity of violation: High.**

All user-derived data rendered to an HTML response shall be wrapped in `htmlspecialchars($value, ENT_QUOTES, 'UTF-8')`. This rule applies to PHP template files, inline HTML strings, and any value whose origin cannot be confirmed as a trusted constant.

```php
// Correct
echo htmlspecialchars($customer['name'], ENT_QUOTES, 'UTF-8');

// INCORRECT — raw output of user data (XSS risk)
echo $customer['name'];
```

Template files shall use a helper alias where available:

```php
// Acceptable alias pattern defined in bootstrap
function e(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
}

echo e($customer['name']);
```

---

## Rule S-04 — CSRF Protection

**Severity of violation: High.**

All state-changing HTTP requests (POST, PUT, PATCH, DELETE) shall include the `X-CSRF-Token` header. Server-side endpoints shall validate this header against the session token via `CsrfTokenManager` before processing any state change.

```php
// Correct — endpoint validates CSRF token before processing
$csrfManager = new CsrfTokenManager();
if (!$csrfManager->isValid($_SERVER['HTTP_X_CSRF_TOKEN'] ?? '')) {
    http_response_code(403);
    echo ApiResponse::error('Invalid CSRF token', 403);
    exit;
}

// INCORRECT — state-changing endpoint with no CSRF check
$_POST['amount']; // processed without token validation
```

Frontend JavaScript shall inject the token on every non-GET request:

```js
// Correct
fetch('./api/sales/save-invoice.php', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrfToken,
    },
    body: JSON.stringify(payload),
});
```

---

## Rule S-05 — Module Gating

**Severity of violation: High.**

Every add-on module page shall begin with a call to `requireModuleAccess('MODULE_CODE')`. Core module pages shall apply `RequirePermission` middleware. No page that belongs to a licensable module may proceed past the first executable line without this gate.

```php
// Correct — add-on module page
<?php
declare(strict_types=1);

requireModuleAccess('PAYROLL');

// ... page logic follows

// Correct — core module page uses middleware applied in routing
// RequirePermission::check('invoices.view') is called by the router before dispatch

// INCORRECT — module page with no access gate
<?php
declare(strict_types=1);

// Page renders for any authenticated user regardless of module subscription
$invoices = $invoiceService->list();
```
