# Introduction to the Longhorn ERP API

## Purpose and Scope

This document specifies the REST API surface for Longhorn ERP, a multi-tenant SaaS Enterprise Resource Planning platform developed by Chwezi Core Systems. It covers all HTTP endpoints exposed to the web panel, the mobile client (API v1), and the super-admin console. The audience is backend engineers, mobile developers, integration partners, and QA engineers who need a deterministic contract for building against or testing these interfaces.

The API underpins every functional module of Longhorn ERP: Accounting, Inventory, Sales, Procurement, Human Resources, Payroll, Point of Sale, and platform administration. All endpoints described here are prospective; this document governs the target design state, not the current implementation state.

## API Design Principles

Longhorn ERP's API is built on six non-negotiable design principles.

- **REST semantics:** Every resource is identified by a URL noun. HTTP verbs carry the operation intent: `GET` reads, `POST` creates, `PUT` fully replaces, `PATCH` partially updates, `DELETE` removes.
- **JSON-only payload:** All request and response bodies are `application/json`. The API does not accept or emit XML, form-urlencoded data, or multipart bodies except where file upload is explicitly documented.
- **Standard response envelope:** Every response, success or failure, is wrapped in the envelope described in Section 1.4. Clients always inspect `success` before reading `data`.
- **Tenant isolation by token:** The `tenant_id` is never accepted as a client-supplied parameter in the request body or URL. It is derived exclusively from the authenticated session (web) or the JWT claims (mobile). This eliminates an entire class of horizontal privilege-escalation attacks.
- **Consistent versioning:** Mobile API endpoints carry the `/api/v1/` prefix. The web panel API uses unversioned paths under `/api/`. Super-admin endpoints use `/api/superadmin/`. Breaking changes to the mobile API will be released under `/api/v2/` with a documented deprecation window.
- **TLS-only transport:** The server refuses all plain HTTP connections with a `301 Moved Permanently` redirect to the HTTPS equivalent. No sensitive data ever traverses an unencrypted channel.

## Authentication Overview

Longhorn ERP uses two authentication mechanisms, each scoped to its client type.

**Session authentication (web panel):** The web panel authenticates via `POST /api/auth/login`. On success the server issues an `HttpOnly`, `Secure`, `SameSite=Strict` session cookie. All subsequent web panel requests carry this cookie. The session is destroyed server-side on logout or after a configurable idle timeout.

**JWT Bearer authentication (mobile API v1):** The mobile client authenticates via `POST /api/v1/auth/login`. On success the server returns a short-lived *access token* and a longer-lived *refresh token*. The client presents the access token in the `Authorization: Bearer <token>` header on every subsequent request. When the access token expires the client calls `POST /api/v1/auth/refresh` to obtain a new pair; the old refresh token is immediately invalidated (rotation). Refresh tokens are stored server-side and can be revoked individually or globally per user.

JWT claims embedded in every access token:

```json
{
  "tenant_id": "uuid",
  "user_id": "uuid",
  "branch_id": "uuid",
  "role_id": "uuid",
  "modules": ["accounting", "inventory", "sales"],
  "exp": 1775000000,
  "iat": 1774996400
}
```

## Standard Response Envelope

All API responses use the following envelope structure.

**Success response:**

```json
{
  "success": true,
  "data": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "Example Resource"
  },
  "error": null
}
```

**Error response:**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The field 'email' must be a valid email address.",
    "details": [
      { "field": "email", "issue": "invalid_format" }
    ]
  }
}
```

**Paginated list response:**

```json
{
  "success": true,
  "data": {
    "items": [],
    "pagination": {
      "page": 1,
      "per_page": 25,
      "total": 142,
      "total_pages": 6
    }
  },
  "error": null
}
```

All list endpoints accept `?page=<n>&per_page=<n>` query parameters. The default page size is 25; the maximum is 100.

## Standard HTTP Error Codes

| HTTP Status | Error Code | Meaning |
|---|---|---|
| 400 | `BAD_REQUEST` | Malformed JSON or missing required fields. |
| 401 | `UNAUTHORIZED` | No valid session cookie or Bearer token present. |
| 403 | `FORBIDDEN` | Authenticated user lacks the required role or module permission. |
| 404 | `NOT_FOUND` | The requested resource does not exist within the tenant's scope. |
| 409 | `CONFLICT` | The operation conflicts with the current resource state (e.g., duplicate reference number, already-posted journal). |
| 422 | `UNPROCESSABLE_ENTITY` | Request is structurally valid but fails business rule validation (e.g., unbalanced journal entry, negative stock). |
| 429 | `RATE_LIMIT_EXCEEDED` | The caller has exceeded the rate limit: 60 requests/minute per user token (mobile); 200 requests/minute per session (web). |
| 500 | `INTERNAL_SERVER_ERROR` | An unexpected server-side error occurred. The `error.message` field contains a reference ID for log correlation. |

## API Versioning Strategy

| Client | Base Path | Versioning Mechanism |
|---|---|---|
| Web panel | `/api/` | Unversioned; breaking changes use feature flags and migration notices. |
| Mobile API | `/api/v1/` | URL-prefix versioned; new incompatible versions increment to `/api/v2/`. |
| Super-admin | `/api/superadmin/` | Unversioned; access is restricted to super-admin sessions. |

The `v1` prefix is a stability contract: no breaking changes will be introduced to `/api/v1/` endpoints after GA. Additive changes (new optional fields, new endpoints) are backward-compatible and may be added without a version increment. Deprecation of an endpoint follows a 90-day notice period communicated via the `Deprecation` and `Sunset` response headers.
