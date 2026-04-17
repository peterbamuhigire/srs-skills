# Authentication Endpoints

## Session Authentication — Web Panel

### POST /api/auth/login

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/auth/login` |
| **Auth Required** | No |
| **Description** | Authenticates a web panel user with email and password. On success, issues an `HttpOnly` session cookie. |

**Request Body:**

```json
{
  "email": "admin@acme.co.ug",
  "password": "S3cur3P@ssword"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string | Yes | Registered user email address. |
| `password` | string | Yes | Plaintext password (transmitted over TLS only). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "full_name": "Admin User",
    "email": "admin@acme.co.ug",
    "tenant_id": "b1c2d3e4-0000-0000-0000-111122223333",
    "role": "admin",
    "modules": ["accounting", "inventory", "sales", "hr"]
  },
  "error": null
}
```

The session cookie (`session_id`) is set in the `Set-Cookie` response header. The cookie attributes are `HttpOnly; Secure; SameSite=Strict; Path=/`.

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing `email` or `password` field. |
| 401 | `UNAUTHORIZED` | Invalid credentials. |
| 429 | `RATE_LIMIT_EXCEEDED` | More than 10 failed login attempts within 15 minutes from the same IP. |

---

### POST /api/auth/logout

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/auth/logout` |
| **Auth Required** | Yes (active session cookie) |
| **Description** | Destroys the current server-side session. The client must discard the session cookie. |

**Request Body:** None.

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": { "message": "Session terminated." },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 401 | `UNAUTHORIZED` | No valid session cookie present. |

---

### GET /api/auth/me

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/auth/me` |
| **Auth Required** | Yes (active session cookie) |
| **Description** | Returns the current authenticated user's profile, assigned role, and module permissions. Used by the web panel on page load to initialise the permission context. |

**Request Body:** None.

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "full_name": "Admin User",
    "email": "admin@acme.co.ug",
    "tenant_id": "b1c2d3e4-0000-0000-0000-111122223333",
    "branch_id": "aabbccdd-0000-0000-0000-ffeeddccbbaa",
    "role": {
      "id": "role-uuid",
      "name": "Finance Manager",
      "permissions": ["accounting.read", "accounting.post", "reports.read"]
    },
    "modules": ["accounting", "inventory", "sales"]
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 401 | `UNAUTHORIZED` | Session cookie is absent or expired. |

---

## JWT Authentication — Mobile API v1

### POST /api/v1/auth/login

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/auth/login` |
| **Auth Required** | No |
| **Description** | Authenticates a mobile user with email, password, and tenant code. Returns a short-lived JWT access token and a long-lived refresh token. |

**Request Body:**

```json
{
  "email": "cashier@acme.co.ug",
  "password": "S3cur3P@ssword",
  "tenant_code": "ACME-UG"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string | Yes | Registered user email address. |
| `password` | string | Yes | Plaintext password (transmitted over TLS only). |
| `tenant_code` | string | Yes | Unique alphanumeric code identifying the tenant. Used to resolve `tenant_id` server-side. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "user": {
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "full_name": "Cashier One",
      "branch_id": "aabbccdd-0000-0000-0000-ffeeddccbbaa",
      "modules": ["pos", "inventory"]
    }
  },
  "error": null
}
```

JWT access token claims:

```json
{
  "tenant_id": "b1c2d3e4-0000-0000-0000-111122223333",
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "branch_id": "aabbccdd-0000-0000-0000-ffeeddccbbaa",
  "role_id": "role-uuid",
  "modules": ["pos", "inventory"],
  "exp": 1775000000,
  "iat": 1774996400
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing required field. |
| 401 | `UNAUTHORIZED` | Invalid credentials. |
| 404 | `NOT_FOUND` | `tenant_code` does not resolve to an active tenant. |
| 403 | `FORBIDDEN` | Tenant is suspended. |
| 429 | `RATE_LIMIT_EXCEEDED` | More than 10 failed login attempts within 15 minutes. |

---

### POST /api/v1/auth/refresh

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/auth/refresh` |
| **Auth Required** | No (refresh token is the credential) |
| **Description** | Exchanges a valid refresh token for a new access token and a new refresh token. The submitted refresh token is immediately invalidated (rotation). Reuse of an invalidated refresh token triggers revocation of the entire token family and forces re-authentication. |

**Request Body:**

```json
{
  "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4..."
}
```

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "bmV3UmVmcmVzaFRva2Vu...",
    "token_type": "Bearer",
    "expires_in": 3600
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | `refresh_token` field missing. |
| 401 | `UNAUTHORIZED` | Refresh token is expired, revoked, or was already used (reuse attack detected). |

---

### POST /api/v1/auth/logout

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/auth/logout` |
| **Auth Required** | Yes (`Authorization: Bearer <access_token>`) |
| **Description** | Revokes the user's current refresh token server-side. The client must discard both the access token and the refresh token. |

**Request Body:**

```json
{
  "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4..."
}
```

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": { "message": "Token revoked." },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 401 | `UNAUTHORIZED` | Access token is absent or expired. |
| 400 | `BAD_REQUEST` | `refresh_token` field missing. |
