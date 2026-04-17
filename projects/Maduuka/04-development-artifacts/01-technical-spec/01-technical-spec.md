---
title: "Maduuka -- Technical Specification"
version: "1.0"
date: "2026-04-05"
status: "Draft"
owner: "Peter Bamuhigire -- Chwezi Core Systems"
---

# Maduuka -- Technical Specification

**Project:** Maduuka
**Version:** 1.0
**Date:** 2026-04-05
**Status:** Draft
**Owner:** Peter Bamuhigire -- Chwezi Core Systems

---

## 1. System Architecture Overview

Maduuka is a multi-tenant Software as a Service (SaaS) platform structured in a four-level hierarchy:

```
Platform (Chwezi Core Systems)
  └── Tenant (Business) [franchise_id]
        ├── Branch
        │     ├── Warehouse / Stock Location
        │     └── POS Terminals / Cashier Sessions
        └── Staff
```

`franchise_id` scoping is applied to every database query. This isolation is enforced at the Object-Relational Mapper (ORM) and service layer -- not at the application controller or User Interface (UI) layer. Cross-tenant data access is architecturally impossible for application-layer queries.

Three client applications consume one shared Representational State Transfer (REST) Application Programming Interface (API):

- Android application (Phase 1, primary product)
- Web application (Phase 1, full-featured equal)
- iOS application (Phase 2)

No platform-specific endpoints exist. All three clients call the same API surface under `/api/v1/`.

**Offline-first strategy by platform:**

- Android: Room (SQLite) + WorkManager background sync
- iOS (Phase 2): Core Data + BackgroundTasks (BGAppRefreshTask)
- Web: Progressive Web App (PWA) Service Worker + Web App Manifest

---

## 2. Backend API Specification

### 2.1 Language and Runtime

- PHP 8.3+ with modern typed properties and enums
- `declare(strict_types=1)` in every file

### 2.2 Authentication

| Client | Mechanism |
|---|---|
| Android / iOS | JSON Web Token (JWT) Bearer token |
| Web | PHP session cookie + Cross-Site Request Forgery (CSRF) token |

**JWT token lifecycle:**

- Access token Time to Live (TTL): 15 minutes
- Refresh token TTL: 30 days
- Refresh endpoint: `POST /api/v1/auth/refresh`
- Logout: invalidates refresh token server-side

**Token storage by platform:**

| Platform | Storage Mechanism | Encryption |
|---|---|---|
| Android | EncryptedSharedPreferences | AES-256-GCM |
| iOS (Phase 2) | Keychain Services | AES-256 |
| Web | HttpOnly session cookie | N/A (server-side session) |

### 2.3 Role-Based Access Control

Role-Based Access Control (RBAC) is enforced at every API route via middleware. HTTP 403 is returned for any permission failure regardless of request origin. UI-layer permission checks are supplementary only and are not a security boundary.

### 2.4 Standard Error Response Format

All endpoints return errors in the following structure:

```json
{
  "success": false,
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Human-readable description",
    "field": "optional -- for validation errors"
  }
}
```

### 2.5 Standard Pagination Format

All list endpoints return paginated responses in the following structure:

```json
{
  "data": [],
  "pagination": {
    "current_page": 1,
    "per_page": 25,
    "total": 150,
    "last_page": 6,
    "next_page_url": "...",
    "prev_page_url": null
  }
}
```

Default page size: 25 records. Maximum page size: 100 records.

### 2.6 External Service Integrations

| Service | Purpose |
|---|---|
| Wasabi S3-compatible storage | Product images, receipt photos, payslip PDFs |
| Africa's Talking API | SMS and WhatsApp Business notifications |
| MTN MoMo Business API | POS push payments and bulk salary disbursements |
| Airtel Money API | POS push payments |
| Firebase Cloud Messaging (FCM) | Android push notifications |
| Apple Push Notification Service (APNs) via Firebase | iOS push notifications (Phase 2) |

### 2.7 Transport Security

TLS 1.3 is required for all data in transit. TLS 1.2 connections are rejected at the server level.

---

## 3. Database Design Principles

### 3.1 Engine and Collation

- MySQL 8.x
- Character set: `utf8mb4`
- Collation: `utf8mb4_unicode_ci`

### 3.2 Standard Column Set

Every tenant-scoped table includes the following columns:

| Column | Type | Constraint |
|---|---|---|
| `id` | BIGINT UNSIGNED | AUTO_INCREMENT PRIMARY KEY |
| `franchise_id` | BIGINT UNSIGNED | NOT NULL, FOREIGN KEY |
| `created_at` | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP |
| `updated_at` | TIMESTAMP | NOT NULL ON UPDATE CURRENT_TIMESTAMP |
| `created_by` | BIGINT UNSIGNED | NOT NULL (user_id) |
| `updated_by` | BIGINT UNSIGNED | NOT NULL (user_id) |

### 3.3 Soft Deletes

The following tables use soft deletes via a `deleted_at TIMESTAMP NULL` column rather than hard DELETE operations:

- `customers`
- `suppliers`
- `products`
- `employees`

### 3.4 EFRIS Placeholder Columns

The following nullable columns are added to relevant tables in Phase 1 to avoid a schema migration when the EFRIS module is activated in Phase 3:

- `efris_fdn` -- Fiscal Document Number
- `efris_qr_code` -- QR code string for the fiscal receipt
- `efris_status` -- Sync status with Uganda Revenue Authority (URA) EFRIS API

All three columns are `NULL` by default in Phase 1 and Phase 2.

### 3.5 Referential Integrity

Foreign key constraints are enforced at the database level for all relationships. Application-layer checks alone are not sufficient.

### 3.6 Index Strategy

All high-frequency queries use a composite index on `(franchise_id, <query_column>)`. Single-column indexes on `franchise_id` alone are not created; the composite pattern is mandatory.

### 3.7 Audit Log Table

The `audit_log` table is append-only. The application database user has INSERT permission only on this table -- no UPDATE or DELETE is granted. Audit entries record: `actor_id`, `franchise_id`, `action`, `table_name`, `record_id`, `old_value` (JSON), `new_value` (JSON), `ip_address`, `device_id`, and `created_at`.

---

## 4. Android Technical Specification

### 4.1 Language and Architecture

- Kotlin, targeting Android API 21+ (Android 5.0 Lollipop minimum)
- Jetpack Compose for all UI
- MVVM + Clean Architecture with three layers:
  1. Presentation (Compose UI + ViewModel)
  2. Domain (Use Cases -- pure Kotlin, no Android framework imports)
  3. Data (Room DAO + Retrofit/OkHttp)

### 4.2 Local Database (Offline-First)

Room (SQLite) caches the following data sets locally:

- Full product catalogue with prices and stock levels (as of last sync)
- Customer profiles and current balances
- Payment methods and accounts
- Tax rates and receipt configuration
- `pending_sync_queue` -- all transactions awaiting upload

### 4.3 Dependency Injection

Hilt manages all dependency injection throughout the application.

### 4.4 Background Sync

WorkManager executes a background sync job every 15 minutes with a `NetworkType.CONNECTED` constraint. All `pending_sync` records are uploaded in First In, First Out (FIFO) order. Each record is marked `synced` only after the API returns a success response.

### 4.5 Barcode Scanning

CameraX + ML Kit supports the following symbologies:

- EAN-13
- EAN-8
- Code-128
- Code-39
- QR Code

External USB/Bluetooth scanners operating in Human Interface Device (HID) keyboard profile are also supported.

### 4.6 Security Components

| Component | Implementation |
|---|---|
| Certificate pinning | OkHttp CertificatePinner on all API calls |
| Biometric re-authentication | BiometricPrompt on app resume after 5 minutes of inactivity |
| Token storage | EncryptedSharedPreferences (AES-256-GCM) |
| Root detection | Executed at app launch; session is blocked if root is detected |

### 4.7 Push Notifications

Firebase Cloud Messaging delivers push notifications for sale confirmations, low-stock alerts, and payroll events.

### 4.8 PDF Generation

Receipts and payslip PDFs are generated locally on-device using a PDF rendering library, without requiring an internet connection.

---

## 5. iOS Technical Specification (Phase 2)

### 5.1 Language and Architecture

- Swift 5.9+, targeting iOS 16 minimum
- SwiftUI for all UI
- MVVM + Clean Architecture (Presentation / Domain / Data)

### 5.2 Local Database (Offline-First)

Core Data (SQLite backend) caches an identical data scope to the Android implementation: products, customers, payment methods, tax rates, and `pending_sync_queue`.

### 5.3 Networking

URLSession with `async/await` and a JWT refresh interceptor. No third-party networking library is required.

### 5.4 Security Components

| Component | Implementation |
|---|---|
| Certificate pinning | URLSession delegate with public key pinning |
| Token storage | Keychain Services (AES-256) |
| Biometric re-authentication | LocalAuthentication (Face ID / Touch ID) after 5-min inactivity |

### 5.5 Background Sync

BGAppRefreshTask executes the sync job every 15 minutes, mirroring the Android WorkManager cadence.

### 5.6 Barcode Scanning

AVFoundation + Vision framework handles camera-based barcode scanning for all symbologies supported on Android.

### 5.7 Bluetooth Printing

Core Bluetooth / Raw Print protocol targets 80mm thermal printers (Epson, Xprinter, TP-Link). Compatibility with at least 3 Uganda-market printer models must be verified before Phase 2 build begins. See GAP-004 in the project gap register.

### 5.8 PDF Generation

PDFKit + Core Graphics renders receipts, invoices, and payslip PDFs locally on-device.

### 5.9 Push Notifications

APNs delivered via Firebase, consistent with the Android FCM integration.

---

## 6. Web Technical Specification

### 6.1 Language and Framework

- PHP 8.3+ with `declare(strict_types=1)`
- Bootstrap 5 + Tabler UI component library
- Alpine.js for reactive UI components (minimal usage -- no Single-Page Application (SPA) framework)

### 6.2 Charting and Mapping

| Library | Purpose |
|---|---|
| ApexCharts | All dashboard and report charts |
| Leaflet.js | Customer location map |

### 6.3 PWA Offline Support

A Service Worker and Web App Manifest enable offline asset caching and installability. Core static assets and the most recent page states are cached; write operations queue until connectivity is restored.

### 6.4 Authentication

- Session-based authentication with PHP session cookies (`HttpOnly; Secure; SameSite=Strict`)
- CSRF token on every state-changing form (`POST`, `PUT`, `PATCH`, `DELETE`)
- Session expiry: 8 hours of inactivity

### 6.5 PDF and Print

- Server-side HTML-to-PDF conversion for receipts, invoices, and report exports
- Browser print Application Programming Interface (API) for direct thermal printer output via USB

---

## 7. CI/CD Pipeline

### 7.1 Environments

| Environment | Purpose |
|---|---|
| `dev` | Feature development and daily integration |
| `staging` | Mirrors production exactly; User Acceptance Testing (UAT) is performed here |
| `production` | Live tenant-facing deployment |

### 7.2 GitHub Actions Workflow

The pipeline executes in this order for every pull request targeting `main`:

1. Lint (PHP_CodeSniffer PSR-12, ktlint, SwiftLint)
2. Static analysis (PHPStan level 8, detekt)
3. Unit tests
4. Integration tests
5. Build artefact
6. Deploy to staging (on merge to `main`)

No merge to `main` is permitted with a failing test suite.

### 7.3 Static Analysis Thresholds

| Platform | Tool | Threshold |
|---|---|---|
| PHP | PHPStan | Level 8 -- no ignored errors without documented justification |
| PHP | PHP_CodeSniffer | PSR-12 full compliance |
| Android | ktlint | Zero violations |
| Android | detekt | Configured ruleset, zero unacknowledged issues |
| iOS | SwiftLint | Configured ruleset, zero unacknowledged issues |

---

## 8. Infrastructure

### 8.1 Server

- Virtual Private Server (VPS) or cloud instance, Uganda region preferred to minimise latency for Ugandan tenants
- Nginx web server

### 8.2 SSL

- Let's Encrypt TLS certificate with automated renewal
- TLS 1.3 enforced; TLS 1.2 rejected

### 8.3 Database

- MySQL 8.x
- Daily automated database backup
- Wasabi S3 file sync for uploaded assets (product images, PDFs)

### 8.4 Log Retention

| Log Type | Retention Period |
|---|---|
| Application logs | 90 days |
| Audit trail | 7 years |

The 7-year audit trail retention supports Uganda Revenue Authority (URA) tax audit requirements and general financial record-keeping obligations.
