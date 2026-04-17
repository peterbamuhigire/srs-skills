# Section 5: System Constraints

## 5.1 Regulatory Constraints

### 5.1.1 Uganda Data Protection and Privacy Act 2019

The system shall collect only the personal data necessary for its stated functions. Customer profiles, employee records, and transaction histories constitute personal data under the Act. The system shall provide a mechanism for a business to export all their personal data as CSV on request, and to permanently delete their account and all associated personal data.

The data retention period for transaction records shall be a minimum of 7 years to comply with Uganda Revenue Authority record-keeping requirements.

### 5.1.2 NSSF Uganda Compliance

The payroll module shall calculate NSSF contributions using the following rates: employer contribution = 10% of gross salary; employee contribution = 5% of gross salary. The system shall generate the monthly NSSF employer schedule in the format required by NSSF Uganda for employer remittance.

### 5.1.3 PAYE Uganda Compliance

The payroll module shall calculate PAYE using the Uganda Income Tax Act tax bands current as of the date of the payroll run. The system shall generate the monthly PAYE return in the format required by URA. The system shall provide a configuration update mechanism to apply revised tax bands when URA publishes annual changes, without requiring a full application release.

### 5.1.4 Local Service Tax (LST) Compliance

The payroll module shall calculate LST per the tier structure of the employee's registered local government jurisdiction. LST tiers for Kampala, Jinja, Gulu, and Mbarara shall be pre-configured. The system shall allow administrators to configure additional LST tier schedules for other jurisdictions.

### 5.1.5 EFRIS Foundation (Phase 1 Obligation)

Although the EFRIS compliance module is a Phase 3 add-on, Phase 1 data models for sales, invoices, products, and customers must be designed with sufficient structure to support EFRIS submission in Phase 3 without requiring breaking schema changes to those tables.

## 5.2 Hardware Constraints

### 5.2.1 Minimum Android Device Specification

The Android application shall operate on devices meeting the following minimum specification:

- Android API level 26 (Android 8.0 Oreo) or higher.
- Minimum 2 GB RAM.
- Minimum 1 GB available internal storage for offline cache and local database.
- Camera with autofocus (required for barcode scanning).
- Bluetooth 4.0 or higher (required for thermal printer and external scanner support).

### 5.2.2 Web Browser Compatibility

The web application shall function correctly on the following browsers: Chrome 90+, Firefox 88+, Safari 14+, and Microsoft Edge 90+. The web application shall not require any browser plugin or extension to function.

## 5.3 Design Constraints

### 5.3.1 Offline-First Architecture (Hard Constraint)

The Android application shall use Room (SQLite) as an offline-first local database. All POS sales, stock movements, and expense entries shall be written to Room first, then synchronised to the server. A sale that fails to reach the server due to connectivity loss shall be queued in Room with status `pending_sync` and retried automatically by WorkManager when connectivity is restored. No sale shall be lost due to a connectivity event.

### 5.3.2 Single REST API (Hard Constraint)

The backend shall expose a single set of REST API endpoints consumed by both the Android client and the web client. No platform-specific API endpoint duplication is permitted. Authentication method (JWT vs session) is determined by the request's `Authorization` header or session cookie, not by the endpoint URL.

### 5.3.3 Franchise ID Scoping (Hard Constraint)

Every database table that stores tenant-specific data shall include a `franchise_id` column. Every database query executed by the application layer shall include a `WHERE franchise_id = :currentTenantId` clause or its ORM equivalent. No query that retrieves, modifies, or counts records across multiple `franchise_id` values shall be permitted except in the Platform Admin context.

### 5.3.4 RBAC at API Layer (Hard Constraint)

Permission checks shall be enforced at the API layer for every endpoint. A user who lacks the required permission shall receive HTTP 403 regardless of how the request was constructed. UI-layer permission hiding is acceptable for user experience but does not substitute for API-layer enforcement.

### 5.3.5 Audit Log Immutability (Hard Constraint)

The audit log table shall be append-only. No DELETE or UPDATE operation shall be permitted on audit log records by any application user, including platform administrators. Audit log access for support purposes shall use read-only queries only.

## 5.4 Software System Attributes

### 5.4.1 Portability

The backend shall be deployable on any Linux VPS with PHP 8.3+, Nginx, and MySQL 8.x, without dependency on a specific cloud provider's proprietary services. The Android application shall be distributed via Google Play Store. The web application shall be a standard HTTPS web application with no native OS dependencies.

### 5.4.2 Maintainability

The Android codebase shall follow MVVM + Clean Architecture with strict separation of Presentation, Domain, and Data layers. Business logic shall reside in Domain layer use cases, not in ViewModel or Repository classes. This separation enables unit testing of business logic without Android framework dependencies.

### 5.4.3 Extensibility

The module system shall be designed so that Phase 2 add-on modules (Restaurant/Bar, Pharmacy) can be activated per tenant without modifying the Phase 1 core module codebase. Add-on module activation shall be controlled by a feature flag in the tenant's subscription record.

### 5.4.4 Internationalisation

All user-visible strings in the Android application and web application shall be externalised to a translation resource file (`strings.xml` for Android, language JSON files for web). No string shall be hardcoded in view code. This enables addition of new languages (French, Luganda, Arabic -- Phase 4) without code changes.

### 5.4.5 Reliability

The system shall implement idempotent API endpoints for all payment and stock-modifying operations. A retry of a failed payment request using the same idempotency key shall not create a duplicate payment record. This prevents double-charging customers or double-recording stock movements when a client retries a request due to a network timeout.
