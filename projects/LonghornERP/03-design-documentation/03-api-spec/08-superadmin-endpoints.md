# Super Admin Panel Endpoints

All endpoints in this section are restricted to super-admin sessions. A super-admin session is issued only to Chwezi Core Systems platform administrators via a separate admin login interface. Super-admin endpoints are not accessible to tenant users under any permission configuration.

The base path `/api/superadmin/` is unversioned. All requests must carry a valid super-admin session cookie.

---

## GET /api/superadmin/tenants

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/superadmin/tenants` |
| **Auth Required** | Yes — super-admin session |
| **Description** | Returns a paginated list of all tenants provisioned on the platform, including their subscription status, module activations, and billing state. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `status` | string | No | `active`, `suspended`, `trial`, `cancelled`. |
| `search` | string | No | Partial match on tenant name, tenant code, or contact email. |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "b1c2d3e4-0000-0000-0000-111122223333",
        "name": "Acme Distributors Ltd",
        "tenant_code": "ACME-UG",
        "contact_email": "admin@acme.co.ug",
        "contact_phone": "+256700000001",
        "country": "UG",
        "status": "active",
        "plan": "enterprise",
        "monthly_fee_ugx": 2500000.00,
        "active_modules": ["accounting", "inventory", "sales", "hr", "pos"],
        "user_count": 14,
        "subscription_expires_at": "2026-12-31T23:59:59Z",
        "created_at": "2024-11-01T00:00:00Z"
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 38, "total_pages": 2 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED` (no super-admin session), 403 `FORBIDDEN`.

---

## POST /api/superadmin/tenants

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/superadmin/tenants` |
| **Auth Required** | Yes — super-admin session |
| **Description** | Provisions a new tenant on the platform. Creates the tenant record, initialises the tenant's database schema partition, seeds default Chart of Accounts and configuration, and activates the specified modules. The first admin user is created and a welcome email with a password-reset link is dispatched. |

**Request Body:**

```json
{
  "name": "Pearl Foods Uganda Ltd",
  "tenant_code": "PFUG",
  "contact_email": "admin@pearlfoodsug.com",
  "contact_phone": "+256772000002",
  "country": "UG",
  "currency": "UGX",
  "plan": "professional",
  "monthly_fee_ugx": 1500000.00,
  "subscription_starts_at": "2026-04-06",
  "subscription_expires_at": "2027-04-05",
  "modules": ["accounting", "inventory", "sales", "procurement"],
  "admin_user": {
    "full_name": "Pearl Admin",
    "email": "admin@pearlfoodsug.com"
  }
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Tenant company name. |
| `tenant_code` | string | Yes | Unique alphanumeric code used in mobile login. Max 10 characters; uppercase, no spaces. |
| `contact_email` | string | Yes | Primary billing and communication email. |
| `country` | string | Yes | ISO 3166-1 alpha-2 country code. |
| `currency` | string | Yes | ISO 4217 currency code (e.g., `UGX`, `KES`). |
| `plan` | string | Yes | `starter`, `professional`, `enterprise`. |
| `monthly_fee_ugx` | number | Yes | Agreed monthly subscription fee in UGX. |
| `modules` | array | Yes | Module codes to activate at provisioning. |
| `admin_user` | object | Yes | First admin user credentials. A password-reset email is sent to `admin_user.email`. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "new-tenant-uuid",
    "name": "Pearl Foods Uganda Ltd",
    "tenant_code": "PFUG",
    "status": "active",
    "admin_user_id": "new-user-uuid",
    "provisioned_at": "2026-04-06T00:00:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing required fields or invalid module code. |
| 409 | `CONFLICT` | `tenant_code` or `contact_email` already exists. |
| 422 | `UNPROCESSABLE_ENTITY` | `subscription_starts_at` is after `subscription_expires_at`. |

---

## PUT /api/superadmin/tenants/{id}/suspend

| Field | Value |
|---|---|
| **Method** | PUT |
| **Path** | `/api/superadmin/tenants/{id}/suspend` |
| **Auth Required** | Yes — super-admin session |
| **Description** | Suspends an active tenant. All user sessions for the tenant are immediately invalidated and all issued JWT tokens are revoked. Users attempting to log in receive a `403 FORBIDDEN` with a suspension message. Tenant data is preserved and the suspension is fully reversible. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Tenant identifier. |

**Request Body:**

```json
{
  "reason": "Non-payment — subscription overdue by 30 days.",
  "notify_admin": true
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `reason` | string | Yes | Internal reason for suspension, stored in audit log. |
| `notify_admin` | boolean | No | If `true`, send suspension notice to tenant's `contact_email`. Default: `true`. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "id": "b1c2d3e4-0000-0000-0000-111122223333",
    "status": "suspended",
    "sessions_revoked": 8,
    "suspended_at": "2026-04-05T12:00:00Z",
    "suspended_by": "superadmin-uuid-001"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT` (tenant is already suspended or cancelled).

---

## PUT /api/superadmin/tenants/{id}/reactivate

| Field | Value |
|---|---|
| **Method** | PUT |
| **Path** | `/api/superadmin/tenants/{id}/reactivate` |
| **Auth Required** | Yes — super-admin session |
| **Description** | Reactivates a suspended tenant. Users can log in again immediately after reactivation. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Tenant identifier. |

**Request Body:**

```json
{
  "reason": "Payment received — subscription renewed.",
  "new_expiry_date": "2027-04-05",
  "notify_admin": true
}
```

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "id": "b1c2d3e4-0000-0000-0000-111122223333",
    "status": "active",
    "subscription_expires_at": "2027-04-05T23:59:59Z",
    "reactivated_at": "2026-04-05T13:00:00Z",
    "reactivated_by": "superadmin-uuid-001"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT` (tenant is already active).

---

## POST /api/superadmin/tenants/{id}/modules

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/superadmin/tenants/{id}/modules` |
| **Auth Required** | Yes — super-admin session |
| **Description** | Activates a module for the specified tenant. The module is immediately available to tenant users with the appropriate role permissions. The tenant's subscription fee is updated if the module carries an additional cost. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Tenant identifier. |

**Request Body:**

```json
{
  "module_code": "payroll",
  "effective_date": "2026-04-06"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `module_code` | string | Yes | Valid module code: `accounting`, `inventory`, `sales`, `procurement`, `hr`, `payroll`, `pos`, `fixed_assets`. |
| `effective_date` | string (ISO 8601) | Yes | Date from which the module is active. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "tenant_id": "b1c2d3e4-0000-0000-0000-111122223333",
    "module_code": "payroll",
    "status": "active",
    "effective_date": "2026-04-06",
    "activated_at": "2026-04-05T14:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND` (tenant not found), 409 `CONFLICT` (module already active for tenant), 422 `UNPROCESSABLE_ENTITY` (invalid `module_code`).

---

## DELETE /api/superadmin/tenants/{id}/modules/{module_code}

| Field | Value |
|---|---|
| **Method** | DELETE |
| **Path** | `/api/superadmin/tenants/{id}/modules/{module_code}` |
| **Auth Required** | Yes — super-admin session |
| **Description** | Deactivates a module for the specified tenant. Users lose access to the module immediately. Existing data within the module is retained and is accessible if the module is reactivated. The `accounting` module cannot be deactivated; it is required by all other modules. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Tenant identifier. |
| `module_code` | string | Module code to deactivate. |

**Request Body:**

```json
{
  "reason": "Customer downgrade — removed payroll add-on."
}
```

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "tenant_id": "b1c2d3e4-0000-0000-0000-111122223333",
    "module_code": "payroll",
    "status": "inactive",
    "deactivated_at": "2026-04-05T15:00:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 404 | `NOT_FOUND` | Tenant or module activation not found. |
| 422 | `UNPROCESSABLE_ENTITY` | Attempting to deactivate the `accounting` module. |

---

## GET /api/superadmin/billing/subscriptions

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/superadmin/billing/subscriptions` |
| **Auth Required** | Yes — super-admin session |
| **Description** | Returns a paginated list of all active tenant subscriptions including billing amounts, expiry dates, and renewal status. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `status` | string | No | `active`, `expired`, `expiring_soon` (within 30 days). |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "sub-uuid-0001",
        "tenant_id": "b1c2d3e4-0000-0000-0000-111122223333",
        "tenant_name": "Acme Distributors Ltd",
        "plan": "enterprise",
        "monthly_fee_ugx": 2500000.00,
        "subscription_starts_at": "2024-11-01T00:00:00Z",
        "subscription_expires_at": "2026-12-31T23:59:59Z",
        "days_until_expiry": 270,
        "auto_renew": true,
        "status": "active"
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 38, "total_pages": 2 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`.

---

## POST /api/superadmin/billing/subscriptions/{id}/renew

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/superadmin/billing/subscriptions/{id}/renew` |
| **Auth Required** | Yes — super-admin session |
| **Description** | Renews a tenant subscription. The new expiry date is calculated from the later of the current expiry date or today's date, extended by the specified number of months. A renewal record is created for billing audit purposes. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Subscription identifier. |

**Request Body:**

```json
{
  "renewal_months": 12,
  "amount_paid_ugx": 30000000.00,
  "payment_reference": "TXN-RENEWAL-2026-0001",
  "payment_date": "2026-04-05",
  "notes": "Annual renewal — full payment received."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `renewal_months` | integer | Yes | Number of months to extend the subscription. Must be between 1 and 24. |
| `amount_paid_ugx` | number | Yes | Amount received for this renewal period in UGX. |
| `payment_reference` | string | Yes | Bank or payment reference for audit trail. |
| `payment_date` | string (ISO 8601) | Yes | Date payment was received. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "subscription_id": "sub-uuid-0001",
    "tenant_name": "Acme Distributors Ltd",
    "previous_expiry": "2026-12-31T23:59:59Z",
    "new_expiry": "2027-12-31T23:59:59Z",
    "renewal_months": 12,
    "amount_paid_ugx": 30000000.00,
    "renewed_at": "2026-04-05T16:00:00Z",
    "renewed_by": "superadmin-uuid-001"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing required fields or `renewal_months` outside valid range. |
| 404 | `NOT_FOUND` | Subscription not found. |
| 409 | `CONFLICT` | Tenant is suspended; reactivate before renewing. |
