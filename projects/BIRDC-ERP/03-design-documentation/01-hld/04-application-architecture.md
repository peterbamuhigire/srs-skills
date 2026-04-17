# 4. Application Architecture

## 4.1 Architectural Pattern

The BIRDC ERP implements a **Service/Repository pattern** with **PHP-DI** as the dependency injection container. This pattern separates business logic (Service layer) from data access logic (Repository layer), making each layer independently testable and replaceable.

All PHP files declare `strict_types=1`. The codebase conforms to PSR-4 autoloading and PSR-12 coding standards.

## 4.2 Layered Architecture

```
┌─────────────────────────────────────────────────────┐
│  Presentation Layer                                  │
│  Bootstrap 5 + Tabler UI, jQuery, Alpine.js          │
│  Twig/PHP templates; ApexCharts; DataTables          │
│  mPDF (PDF output); PhpSpreadsheet (Excel/CSV)       │
├─────────────────────────────────────────────────────┤
│  Controller Layer                                    │
│  Thin HTTP request handlers — input validation,      │
│  CSRF verification, session/JWT authentication,      │
│  permission check, delegate to Service layer         │
├─────────────────────────────────────────────────────┤
│  Service Layer                                       │
│  Business logic — GL posting, FEFO enforcement,      │
│  FIFO remittance, mass balance, payroll calculation, │
│  EFRIS submission, commission computation            │
├─────────────────────────────────────────────────────┤
│  Repository Layer                                    │
│  100% PDO prepared statements; no string query       │
│  concatenation. One repository class per domain      │
│  aggregate. Returns domain model objects.            │
├─────────────────────────────────────────────────────┤
│  Database Layer                                      │
│  MySQL 9.1 InnoDB — stored procedures, triggers,     │
│  views, foreign key constraints, comprehensive       │
│  indexing                                            │
└─────────────────────────────────────────────────────┘
```

## 4.3 Request Lifecycle (Web)

1. Browser sends HTTPS request to Nginx.
2. Nginx routes to PHP-FPM via FastCGI.
3. `public/index.php` (front controller) bootstraps the PHP-DI container, loads `.env` variables, and initiates the router.
4. Router matches the URL to a Controller class and method.
5. Controller middleware stack executes in order:
   a. CSRF token validation (on POST/PUT/DELETE)
   b. Session authentication check (redirect to login if unauthenticated)
   c. 8-layer permission check via `RBACService`
6. Controller calls one or more Service methods, passing validated input.
7. Service executes business logic, calls Repository methods, calls external services (EFRIS, mobile money) as required.
8. Repository executes PDO prepared statements against MySQL.
9. Service returns domain model object(s) to the Controller.
10. Controller passes the result to the template layer for rendering.
11. Nginx returns the HTTP response to the browser.

## 4.4 Request Lifecycle (Mobile API)

1. Android app sends HTTPS request with `Authorization: Bearer <access_token>` header.
2. Nginx routes to PHP-FPM.
3. API front controller validates JWT signature and expiry via `AuthService::validateJWT()`.
4. Permission middleware checks 8-layer RBAC for the authenticated user.
5. Controller calls Service layer (same Service classes as the web path — no duplication).
6. Response serialised as JSON using the standard error envelope format (see LLD Section 17).
7. Response returned to Android app.

## 4.5 Dependency Injection

PHP-DI resolves all class dependencies automatically using constructor injection. No service locator pattern; all dependencies are declared via constructor type hints. This enables full unit testing with mock objects for all Service and Repository classes.

```php
// Example: SalesService receives its dependencies via constructor
final class SalesService
{
    public function __construct(
        private readonly InvoiceRepository $invoices,
        private readonly GLService $gl,
        private readonly EFRISService $efris,
        private readonly InventoryRepository $inventory,
    ) {}
}
```

## 4.6 Frontend Architecture

- **Bootstrap 5 + Tabler admin template** provides the responsive grid and component library.
- **Alpine.js** handles lightweight reactive UI state (toggling panels, form field dependencies) without a full SPA framework.
- **jQuery** supports DataTables, Select2, and legacy interaction patterns.
- **ApexCharts** renders all dashboard charts (bar, line, area, donut).
- **DataTables** handles all large tabular data sets with server-side pagination (6,440+ farmers; 1,071 agents).
- **Select2** provides searchable dropdowns for farmer selection, product search, and account selection.
- **Flatpickr** handles all date and date-range inputs with consistent formatting.
- **SweetAlert2** provides all confirmation dialogs and success/error notifications.
- No frontend build pipeline is required; all libraries are served from the local server (no CDN dependency for offline resilience per DC-005).
