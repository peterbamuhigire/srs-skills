# Maduuka -- High-Level Design

**Version:** 1.0
**Date:** 2026-04-05
**Owner:** Peter Bamuhigire -- Chwezi Core Systems
**Scope:** Phase 1 -- Android + Web, all 10 core modules

---

## 1. System Context

Maduuka is a multi-tenant SaaS platform accessed by three client types:

- **Android application** (primary product) -- Kotlin/Jetpack Compose, offline-first
- **Web application** (full-featured equal) -- PHP 8.3+, Bootstrap 5/Tabler, PWA
- **iOS application** (Phase 2) -- Swift/SwiftUI, identical feature parity

All three clients communicate exclusively with the **Maduuka REST API**. No client-to-client communication occurs. The REST API is the single source of truth for all persistent state.

External systems connected to the REST API:

- MTN MoMo Business API (Uganda) -- POS push payments and bulk salary payments
- Airtel Money API (Uganda) -- POS push payments
- Africa's Talking -- SMS and WhatsApp Business API (receipts, notifications, magic links)
- Firebase Cloud Messaging -- Android push notifications
- Apple Push Notification Service (Phase 2) -- iOS push notifications
- Wasabi S3-compatible storage -- product images, receipt photos, payslip PDFs
- MySQL 8.x database -- all persistent data
- URA EFRIS API (Phase 3) -- fiscal invoicing compliance

---

## 2. Tenant Hierarchy

```
Platform (Chwezi Core Systems)
  └── Business (Tenant) [franchise_id]
        ├── Branch A
        │     ├── Warehouse / Stock Location
        │     └── POS Terminals / Cashier Sessions
        ├── Branch B
        │     └── Warehouse / Stock Location
        └── Staff (cross-branch or branch-assigned)
```

Every database table that contains tenant-specific data includes a non-nullable `franchise_id` foreign key. Every API query executed by the application layer includes `WHERE franchise_id = :currentTenantId`. Cross-tenant data access is architecturally impossible for application-layer queries.

Support access (Platform Admin) goes through a logged, audited impersonation mechanism. Every support session is recorded with: admin user, target tenant, start timestamp, end timestamp, and actions taken.

---

## 3. Component Architecture

### 3.1 Android Application

```
Presentation Layer (Jetpack Compose UI)
      |
ViewModel (StateFlow, LiveData)
      |
Domain Layer (Use Cases -- pure Kotlin, no Android imports)
      |
Data Layer
  ├── Remote: Retrofit + OkHttp (REST API, JWT, certificate pinning)
  └── Local: Room DAO (SQLite, offline-first cache)
      |
WorkManager (background sync -- queues pending_sync records)
```

**Key Android components:**

- `CameraX + ML Kit` -- barcode scanning in POS
- `BiometricPrompt` -- re-authentication on app resume
- `EncryptedSharedPreferences` (AES-256-GCM) -- JWT token storage
- `OkHttp CertificatePinner` -- API certificate pinning
- `Firebase Cloud Messaging` -- push notifications
- `Room` -- offline-first local database (products, customers, pending_sync transactions)

### 3.2 Web Application

```
Browser (Bootstrap 5 / Tabler UI)
      |
PHP 8.3+ Controllers (MVC or equivalent)
      |
Service Layer (business logic)
      |
Database Layer (MySQL 8.x via PDO/Eloquent)
```

**Key web components:**

- Session + CSRF authentication
- Service Worker + Web App Manifest (PWA, offline asset caching)
- ApexCharts (dashboard charts and report visualisations)
- Leaflet.js (customer location map)
- Browser print dialog (receipt printing to USB thermal printer)
- KDS auto-refresh (polling every 10 seconds or WebSocket)

### 3.3 REST API

Single API consumed by Android, Web (Phase 1), and iOS (Phase 2). Authentication method determined by request headers:

- `Authorization: Bearer <jwt>` -- mobile clients
- Session cookie + `X-CSRF-Token` header -- web client

All endpoints versioned under `/api/v1/`. All responses follow: `{ success: bool, data: {}, errors: [] }`.

---

## 4. Multi-Tenant Data Isolation Model

### 4.1 Token Structure (Mobile)

Every mobile JWT payload includes:

```json
{
  "sub": "<user_id>",
  "franchise_id": "<tenant_id>",
  "branch_id": "<branch_id_or_null>",
  "roles": ["cashier"],
  "exp": <unix_timestamp>
}
```

The `franchise_id` in the token is set at login and cannot be changed by the client. Every API request validates the token and injects `franchise_id` into the query context at the service layer. No endpoint accepts a `franchise_id` parameter from the client.

### 4.2 Database Scoping Pattern

Every tenant-scoped table:

```sql
CREATE TABLE products (
  id            BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  franchise_id  BIGINT UNSIGNED NOT NULL,
  name          VARCHAR(255) NOT NULL,
  -- other columns
  FOREIGN KEY (franchise_id) REFERENCES businesses(id)
);
```

Every application-layer query:

```sql
SELECT * FROM products
WHERE franchise_id = :currentFranchiseId
  AND id = :productId;
```

### 4.3 Platform Admin Impersonation

Platform Admin access to tenant data uses a separate impersonation token issued for a specific session:

```json
{
  "sub": "<admin_user_id>",
  "impersonating_franchise_id": "<target_tenant_id>",
  "reason": "<support_ticket_ref>",
  "exp": <unix_timestamp_30min>
}
```

All read and write operations during an impersonation session are recorded in `support_audit_log` with admin_user_id, action, table, record_id, and timestamp.

---

## 5. Offline-First Data Flow (Android)

```
User action (e.g., POS sale)
        |
Write to Room (local SQLite)
status = 'pending_sync' (if offline) or 'synced' (if online)
        |
If online:
  POST to REST API immediately
  On success: update Room record status to 'synced'
  On failure: leave as 'pending_sync', WorkManager retries
        |
If offline:
  Record stays in Room as 'pending_sync'
  WorkManager (periodic + connectivity constraint) retries
  On connectivity restoration: uploads all pending_sync records in FIFO order
  Marks each as 'synced' on API confirmation
```

**Offline data cached in Room:**

- Products (full catalogue with prices, stock levels as of last sync)
- Customers (profiles and current balances)
- Payment methods and accounts
- Tax rates and receipt configuration
- All pending_sync transactions

**Background sync:** WorkManager job with `NetworkType.CONNECTED` constraint runs every 15 minutes when the app is in the background.

---

## 6. Authentication and Session Model

### 6.1 Mobile (Android / iOS Phase 2)

```
POST /api/v1/auth/login
  { phone, password }
  --> { access_token (15 min TTL), refresh_token (30 day TTL) }

API request:
  Authorization: Bearer <access_token>

Token refresh (automatic, background):
  POST /api/v1/auth/refresh
  { refresh_token }
  --> { new_access_token }

Logout:
  POST /api/v1/auth/logout
  --> invalidates refresh_token server-side
```

Access tokens are stored in AES-256-GCM EncryptedSharedPreferences. Refresh tokens are stored in the same. Neither is stored in plain SharedPreferences, files, or logcat.

### 6.2 Web

```
POST /auth/login (form submit)
  { email_or_phone, password, _csrf_token }
  --> Set-Cookie: session_id=<httponly; secure; samesite=strict>

Every state-changing request:
  POST/PUT/PATCH/DELETE includes X-CSRF-Token header
  Server validates CSRF token against session

Session expiry: 8 hours of inactivity
```

---

## 7. RBAC Model

Permissions are assigned to roles. Users are assigned to roles. Role assignment is per-tenant.

**Core roles and key permissions (Phase 1):**

| Role | POS | Inventory | Customers | Finance | Reports | HR | Settings |
|---|---|---|---|---|---|---|---|
| Business Owner | Full | Full | Full | Full | Full | Full | Full |
| Branch Manager | Full | Full | Full | Read | Read | Approve | Branch only |
| Cashier | POS only | Read (stock check) | Read (credit check) | None | None | None | None |
| Stock Manager | None | Full | None | None | Inventory only | None | None |
| Accountant | None | Read | Read + payments | Full | Full | Read (no salaries) | None |
| HR Manager | None | None | None | None | HR only | Full | None |

Permission enforcement: every API endpoint calls a `can(permission, resource)` middleware. HTTP 403 is returned for any permission failure, regardless of request origin.

---

## 8. Module Dependency Map

```
Settings (F-010)
    |--- configures --> All modules
    
Dashboard (F-009)
    |--- reads from --> POS, Inventory, Customers, Finance, HR

POS (F-001)
    |--- writes to --> Inventory (stock levels)
    |--- writes to --> Customers (credit balances)
    |--- writes to --> Financial Accounts (payment account balances)
    |--- writes to --> Audit Log

Inventory (F-002)
    |--- reads from --> Suppliers (purchase orders)
    |--- writes to --> Financial Accounts (stock valuation)

Suppliers (F-004)
    |--- writes to --> Inventory (goods receipt)
    |--- writes to --> Financial Accounts (supplier payments)

HR/Payroll (F-008)
    |--- writes to --> Financial Accounts (payroll disbursements)
    |--- reads from --> Settings (tax bands, NSSF rates)

Expenses (F-005)
    |--- writes to --> Financial Accounts (expense disbursements)

Reports (F-007)
    |--- reads from --> POS, Inventory, Customers, Finance, HR
```

---

## 9. Security Architecture Summary

| Layer | Mechanism |
|---|---|
| Transport | TLS 1.3 (TLS 1.2 rejected) |
| Authentication | JWT (mobile), Session+CSRF (web) |
| Authorisation | RBAC at every API endpoint |
| Mobile token storage | AES-256-GCM EncryptedSharedPreferences |
| Certificate pinning | OkHttp CertificatePinner (Android) |
| Biometric re-auth | BiometricPrompt (Android) on app resume |
| Password hashing | bcrypt cost factor >= 12 |
| Audit trail | Append-only audit_log table |
| Tenant isolation | franchise_id on every table, injected at service layer |
| Root/jailbreak detection | At app launch (Android) |
