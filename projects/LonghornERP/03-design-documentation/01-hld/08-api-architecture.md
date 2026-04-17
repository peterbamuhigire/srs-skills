# API Architecture

## 8.1 API Surface Overview

Longhorn ERP exposes three distinct API surfaces, each with its own authentication mechanism, path prefix, and client scope:

| API Surface | Base Path | Authentication | Client |
|---|---|---|---|
| Web UI API | `/public/api/` | Session-based + CSRF token | Browser (tenant workspace pages) |
| Mobile API v1 | `/public/api/mobile/v1/` | JWT Bearer token | Android and iOS native apps |
| Super Admin API | `/public/superadmin/api/` | Super admin session | Super Admin Panel browser pages |

## 8.2 Web UI API (`/public/api/`)

### Purpose

The Web UI API serves AJAX requests from the tenant workspace browser pages. It is not a general-purpose API and is not documented for third-party consumption.

### Authentication

Session-based. Every request to `/public/api/` passes through the same `EnsureAuthenticated → EnsureTenantSelected → EnsureTenantActive → EnsureBranchSelected → RequirePermission` middleware pipeline as page requests. Requests without a valid session are rejected with HTTP 401.

### CSRF Protection

All state-changing requests (POST, PUT, DELETE, PATCH) must include the `X-CSRF-Token` header populated from the session token. Requests missing this header are rejected with HTTP 403.

### Directory Organisation

API endpoint files are organised by domain under `/public/api/`:

```
public/api/
├── accounting/
│   ├── invoices/
│   │   ├── create.php
│   │   ├── list.php
│   │   └── ...
│   └── ...
├── inventory/
├── sales/
├── procurement/
├── hr/
└── ...
```

### Response Format

All endpoints return the standardised `ApiResponse` JSON envelope. See Section 8.5.

## 8.3 Mobile API v1 (`/public/api/mobile/v1/`)

### Purpose

The Mobile API v1 is the public REST API consumed by the Longhorn ERP Android (Kotlin + Jetpack Compose) and iOS (Swift + SwiftUI) native applications. It is versioned so that breaking changes can be introduced in v2 without affecting v1 clients.

### Authentication

JWT Bearer token. The mobile client includes the token in the `Authorization: Bearer <token>` HTTP header on every request. The server validates the token signature, expiry, and revocation status on each request. The JWT claims (`tid`, `uid`, `role`, `modules`) are used to populate a `TenantContext` equivalent for mobile requests — the `tid` claim provides the `tenant_id` used for all SQL queries, not any request body parameter.

### Versioning

The `/v1/` path segment is the API version identifier. When a new API version is required, `/public/api/mobile/v2/` shall be created with the updated endpoint implementations. Both versions shall operate concurrently during a migration window.

### Rate Limiting

Per-tenant and per-user rate limiting applies (see Section 6.5). Mobile API clients receive a `Retry-After` header on HTTP 429 responses.

### CORS

Cross-Origin Resource Sharing (CORS) headers are enabled for the Mobile API path to permit requests from native app WebView components and any hybrid client contexts. Allowed origins are restricted to the Longhorn ERP app bundle identifiers.

### Offline Sync Endpoints

The Mobile API includes sync endpoints that accept a `last_modified` timestamp parameter. The server returns only records modified after that timestamp (delta sync). This supports the offline resilience requirement: the Cooperative Procurement module shall allow offline intake for up to 72 hours and sync all pending transactions within 60 seconds of connectivity restoration (NFR-MOBILE-001).

## 8.4 Super Admin API (`/public/superadmin/api/`)

### Purpose

The Super Admin API serves AJAX requests from the Super Admin Panel browser pages. It handles tenant provisioning, subscription management, billing, and platform monitoring operations.

### Authentication

Super admin session. Requests are validated against the super admin session scope. No tenant context is injected — super admin API endpoints operate outside tenant isolation boundaries.

### CSRF Protection

The same `X-CSRF-Token` header requirement applies to all state-changing Super Admin API requests.

## 8.5 Standardised Response Format

Every API endpoint, across all three surfaces, shall return responses using the `ApiResponse` class in the following JSON envelope:

```json
{
  "success": true,
  "data": {},
  "error": {}
}
```

| Field | Type | Description |
|---|---|---|
| `success` | `bool` | `true` if the operation succeeded; `false` if it failed. |
| `data` | `object` or `array` | The response payload on success; `{}` on failure. |
| `error` | `object` | Error details on failure: `{ "code": "...", "message": "..." }`; `{}` on success. |

HTTP status codes are always set correctly: 200 for success, 201 for created, 400 for validation errors, 401 for unauthenticated, 403 for unauthorised, 404 for not found (including cross-tenant attempts), 422 for business rule violations, 429 for rate limit exceeded, 500 for server errors.

## 8.6 Output Encoding

All string values in API responses shall be HTML-escaped using `htmlspecialchars()` with `ENT_QUOTES | ENT_SUBSTITUTE` before being passed to `ApiResponse`. This prevents Cross-Site Scripting (XSS) vulnerabilities in any client that renders API response values as HTML without additional escaping.

All SQL inputs are handled via PDO prepared statements (see Section 4.7). API endpoints do not construct SQL queries directly — all data operations are delegated to service layer methods.
