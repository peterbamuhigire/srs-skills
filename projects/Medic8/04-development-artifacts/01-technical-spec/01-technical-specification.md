# Technical Specification -- Medic8 Healthcare Management System

**Document ID:** DA-01-01
**Project:** Medic8
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft -- Pending Consultant Review

---

## 1. Development Environment Setup

### 1.1 Backend Runtime

| Component | Version | Purpose |
|---|---|---|
| PHP | 8.2+ | Application runtime (strict typing enabled) |
| Composer | 2.x | Dependency management, PSR-4 autoloading |
| MySQL | 8.x | Primary data store (InnoDB, strict mode, utf8mb4) |
| Redis | 7.x | Cache driver, queue driver, session driver |
| Node.js | 18+ | Frontend asset compilation (Vite) |
| Laravel Horizon | Latest stable | Queue monitoring dashboard |

### 1.2 Required PHP Extensions

Every developer environment and every deployment target must have all of the following extensions enabled. The application bootstrapper checks for these at startup and fails fast if any are missing.

- `pdo_mysql` -- MySQL database driver
- `mbstring` -- Multi-byte string handling (patient names in non-Latin scripts)
- `openssl` -- TLS, JWT signing, AES-256-GCM encryption of Protected Health Information (PHI)
- `xml` -- CDA R2 discharge summaries, HL7 v2 message parsing
- `curl` -- HTTP client for DHIS2 API, Africa's Talking SMS, MTN MoMo API, FHIR R4
- `gd` -- Patient photo processing, barcode/QR generation for specimen labels
- `intl` -- ICU locale-aware formatting (dates, numbers, currency for UGX, KES, INR, AUD)
- `sodium` -- Modern cryptography primitives (Argon2id password hashing)
- `bcmath` -- Arbitrary-precision arithmetic for billing calculations (no floating-point rounding)
- `zip` -- HMIS report export, bulk CSV/Excel import packaging
- `redis` -- PHP Redis extension for cache, queue, and session drivers

### 1.3 MySQL Configuration

The following `my.cnf` settings are mandatory for all environments:

```ini
[mysqld]
sql_mode            = STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
default_storage_engine = InnoDB
character_set_server   = utf8mb4
collation_server       = utf8mb4_unicode_ci
innodb_strict_mode     = ON
innodb_file_per_table  = ON
max_connections        = 200
innodb_buffer_pool_size = 1G
```

**Rationale:** Strict mode prevents silent data truncation on clinical fields. `utf8mb4` supports the full Unicode range required for patient names across Uganda, Kenya, India, and Australia. InnoDB provides row-level locking for concurrent clinical workflows.

### 1.4 Local Development Options

**Option A -- WAMP/LAMP stack:**

1. Install WAMP (Windows) or LAMP (Linux) with PHP 8.2+, MySQL 8.x
2. Install Redis via WSL (Windows) or package manager (Linux)
3. Install Composer 2.x globally
4. Install Node.js 18+ via nvm
5. Clone the repository, run `composer install`, `npm install`
6. Copy `.env.example` to `.env`, configure database and Redis credentials
7. Run `php artisan key:generate`, `php artisan migrate --seed`
8. Start Horizon: `php artisan horizon`
9. Compile assets: `npm run dev`

**Option B -- Docker (docker-compose):**

The repository includes a `docker-compose.yml` with services for `app` (PHP-FPM 8.2), `mysql` (8.x), `redis` (7.x), `horizon` (queue worker), and `node` (asset compiler). Run `docker-compose up -d` to start all services.

### 1.5 IDE Configuration

**PHPStorm (recommended):**

- Enable PSR-12 code style under Settings > Editor > Code Style > PHP
- Install Laravel Idea plugin for route, config, and view autocompletion
- Enable PHPStan integration at level 8
- Configure Xdebug for step debugging (port 9003)

**VS Code (alternative):**

- Extensions: PHP Intelephense, Laravel Blade Snippets, PHP Debug, EditorConfig
- Configure `php.validate.executablePath` to PHP 8.2+ binary
- Enable format-on-save with PHP CS Fixer (PSR-12 preset)

---

## 2. Project Structure

```
medic8/
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   │   ├── Api/V1/                    # Tenant-scoped API controllers
│   │   │   └── AdminPanel/Api/V1/         # Super Admin controllers
│   │   ├── Middleware/
│   │   │   ├── TenantMiddleware.php        # Resolves facility_id from session/JWT
│   │   │   ├── MfaVerifiedMiddleware.php   # Enforces MFA for admin roles
│   │   │   └── IdleTimeoutMiddleware.php   # 15-minute session timeout
│   │   └── Requests/                      # Form Request validation classes
│   ├── Services/
│   │   ├── Clinical/                      # CDS engine, terminology, EMPI
│   │   ├── Billing/                       # Auto-billing, insurance claims
│   │   ├── Pharmacy/                      # Dispensing, stock, narcotic register
│   │   ├── Lab/                           # Specimen tracking, result validation
│   │   └── Infrastructure/               # FormState, SyncQueue, AuditService
│   ├── Repositories/
│   │   ├── Contracts/                     # Repository interfaces
│   │   └── Eloquent/                      # Concrete implementations (tenant-scoped)
│   ├── Models/
│   │   ├── Scopes/
│   │   │   └── FacilityScope.php          # Global scope: WHERE facility_id = ?
│   │   └── Traits/
│   │       └── BelongsToFacility.php      # Trait applying FacilityScope
│   ├── Events/                            # Domain events (PatientRegistered, DrugDispensed)
│   ├── Listeners/                         # Event handlers (PostBillingChargeOnDrugDispensed)
│   ├── Jobs/                              # Queue jobs (extend TenantAwareJob)
│   ├── Policies/                          # Authorization policies per model
│   ├── Rules/                             # Custom validation rules (ICD10Code, NIN)
│   ├── Exceptions/                        # Typed exceptions (TenantViolationException)
│   └── CDS/                              # Clinical Decision Support engine
│       ├── Rules/                         # CDS rule definitions (drug interactions, dosing)
│       ├── Alerts/                        # Alert severity classification (4-tier)
│       └── Engine.php                     # Rule evaluation engine
├── config/
│   ├── medic8.php                         # Application-level configuration
│   ├── tenancy.php                        # Multi-tenant configuration
│   ├── cds.php                            # CDS alert thresholds, severity levels
│   └── hmis.php                           # HMIS form version mappings
├── database/
│   ├── migrations/                        # Timestamped migrations
│   ├── seeders/                           # Default data seeders
│   └── factories/                         # Test data factories
├── routes/
│   ├── api.php                            # Tenant-scoped API routes (/api/v1/...)
│   ├── admin.php                          # Super Admin API routes
│   └── web.php                            # Web UI routes (Blade/Tabler)
├── tests/
│   ├── Unit/                              # Isolated unit tests (Services, Rules, CDS)
│   ├── Feature/                           # HTTP-level feature tests
│   └── Integration/                       # Cross-module integration tests
├── resources/
│   ├── views/                             # Blade templates (Tabler UI)
│   ├── js/                                # JavaScript (vanilla + jQuery, DataTables)
│   └── css/                               # Custom stylesheets
└── storage/
    ├── app/                               # Uploaded files (temporary)
    └── logs/                              # Application logs (no PHI)
```

### 2.1 Layer Responsibility

Every feature follows a strict 4-layer architecture. No layer may bypass the layer directly below it.

```
Controller -> Service -> Repository -> Database
```

| Layer | Responsibility | May Call |
|---|---|---|
| Controller | HTTP I/O, input validation via Form Requests, response formatting | Service only |
| Service | Business logic, orchestration, authorisation, event dispatching | Repository, other Services |
| Repository | Data access, tenant scoping, query construction | Database (Eloquent/Query Builder) |
| Model | Column casting, relationships, attribute accessors, scopes | -- |

---

## 3. Coding Standards

### 3.1 PHP Language Standards

- **PSR-12** coding style enforced by PHP CS Fixer in CI
- Every file starts with `declare(strict_types=1);`
- Type hints on all method parameters and return types -- no untyped methods
- Use `final` on classes that are not designed for extension
- Use `readonly` properties where the value is set once at construction
- No `mixed` type hints except when interfacing with third-party libraries
- Maximum method length: 30 lines (excluding PHPDoc). Extract to private methods or services if exceeded
- Maximum class length: 300 lines. Split into collaborators if exceeded

### 3.2 Business Logic Placement

- **Controllers:** Thin. Accept request, call service, return response. No `if/else` business logic
- **Services:** All business logic lives here. Services are stateless, injected via constructor DI
- **Repositories:** Data access only. No business decisions. Tenant scope enforced at this layer
- **Models:** No business logic. Only Eloquent concerns: relationships, casts, scopes, accessors

### 3.3 Documentation

- PHPDoc on all public methods with `@param`, `@return`, and `@throws` annotations
- Inline comments only for non-obvious clinical logic (e.g., NEWS2 score calculation, paediatric dose ceiling)
- No comments that restate the code -- every comment must explain *why*, not *what*

### 3.4 Static Analysis

- PHPStan at level 8 with zero baseline errors
- Larastan for Laravel-specific analysis
- CI fails on any new PHPStan error

---

## 4. Database Migration Standards

### 4.1 Naming Convention

Migrations follow the Laravel timestamped convention:

```
YYYY_MM_DD_HHMMSS_create_<table>_table.php    # New table
YYYY_MM_DD_HHMMSS_add_<column>_to_<table>.php  # Add column
YYYY_MM_DD_HHMMSS_modify_<column>_on_<table>.php  # Modify column
```

### 4.2 Mandatory Columns for Tenant-Scoped Tables

Every table that stores facility-specific data must include:

```php
$table->id();
$table->foreignId('facility_id')->constrained()->index();
$table->timestamps();  // created_at, updated_at
```

The `facility_id` column is always indexed. The foreign key constraint references `facilities.id`.

### 4.3 Soft Deletes

Soft deletes (`$table->softDeletes()`) are required on the following tables only:

- `patients` -- patient records must never be physically deleted (BR-DATA-001, 10-year retention)
- `encounters` -- clinical encounter history is legally required
- `prescriptions` -- prescribing audit trail
- `medication_dispenses` -- dispensing audit trail
- `lab_results` -- clinical results are medico-legal records
- `audit_logs` -- tamper-proof audit trail (PDPA 2019 Section 24)
- `narcotic_register_entries` -- controlled substance accountability

All other tables use hard deletes.

### 4.4 Data Type Standards

| Data Type | Column Type | Rationale |
|---|---|---|
| Money (UGX, KES) | `$table->bigInteger('amount')` | Store in smallest currency unit; no float rounding |
| Patient age | Never stored | Calculate from `date_of_birth` at query time |
| Dates | `$table->date()` or `$table->dateTime()` | Always UTC in database |
| ICD codes | `$table->string('icd_code', 10)` + `$table->tinyInteger('icd_version')` | Store code and version (10 or 11) |
| Drug names | `$table->string('generic_name')` + `$table->string('brand_name')->nullable()` | Generic is primary |
| Lab values | `$table->decimal('value', 10, 4)` + `$table->string('unit', 20)` | Always store with unit |
| Vital signs | Metric units only | Celsius, mmHg, kg, cm |
| PHI fields | `$table->text('encrypted_value')` | Encrypted with AES-256-GCM via `encrypt()` |
| Boolean flags | `$table->boolean()` | Never use tinyint(1) with ambiguous values |
| Enums | `$table->string('status', 30)` | Use PHP enums in model, string in DB for portability |

### 4.5 Indexing Standards

- Every `facility_id` column is indexed (composite indexes preferred for high-traffic queries)
- Every foreign key column is indexed
- Composite index on `(facility_id, created_at)` for tables frequently queried by date range
- Composite index on `(facility_id, patient_id)` for clinical tables
- Full-text index on `patients.first_name`, `patients.last_name` for patient search
- No index on columns with fewer than 3 distinct values (e.g., boolean flags) unless part of a composite

---

## 5. API Design Standards

### 5.1 URL Structure

All tenant-scoped API endpoints follow the pattern:

```
GET    /api/v1/{resource}          # List (paginated)
POST   /api/v1/{resource}          # Create
GET    /api/v1/{resource}/{id}     # Read
PUT    /api/v1/{resource}/{id}     # Update (full)
PATCH  /api/v1/{resource}/{id}     # Update (partial)
DELETE /api/v1/{resource}/{id}     # Delete
```

Nested resources for direct relationships:

```
GET    /api/v1/patients/{patientId}/encounters
POST   /api/v1/encounters/{encounterId}/prescriptions
GET    /api/v1/encounters/{encounterId}/lab-requests
```

### 5.2 Response Envelope

Every API response uses a consistent envelope:

```json
{
  "success": true,
  "data": {},
  "message": "Patient registered successfully",
  "errors": []
}
```

Error response:

```json
{
  "success": false,
  "data": null,
  "message": "Validation failed",
  "errors": {
    "date_of_birth": ["The date of birth field is required."],
    "icd_code": ["The selected ICD code is invalid."]
  }
}
```

### 5.3 Pagination

Paginated list endpoints accept `?page=1&per_page=25` (default: page 1, 25 per page, maximum: 100 per page).

Response includes a `meta` object:

```json
{
  "success": true,
  "data": [],
  "meta": {
    "total": 1420,
    "per_page": 25,
    "current_page": 3,
    "last_page": 57,
    "from": 51,
    "to": 75
  },
  "message": ""
}
```

### 5.4 Healthcare-Specific HTTP Status Codes

In addition to standard HTTP status codes, Medic8 uses custom codes for healthcare-specific conditions:

| Code | Meaning | Example |
|---|---|---|
| 200 | Success | Standard success response |
| 201 | Created | Patient registered, encounter created |
| 400 | Bad Request | Malformed request body |
| 401 | Unauthorised | Invalid or expired token |
| 403 | Forbidden | Insufficient RBAC/ABAC permissions |
| 404 | Not Found | Resource does not exist in this tenant |
| 409 | Conflict | Duplicate patient (EMPI match > 80%) |
| 422 | Validation Error | Form validation failure |
| 460 | CDS Alert Fired | Clinical Decision Support alert requires acknowledgement |
| 461 | Prescribing Violation | Five Rights check failed (BR-CLIN-008) |
| 462 | Tenant Isolation Violation | Request attempted cross-tenant data access |
| 463 | Consent Required | Patient consent not on file for requested data category |
| 429 | Rate Limited | API rate limit exceeded |
| 500 | Server Error | Unhandled exception |

### 5.5 Filtering and Sorting

List endpoints support query parameters for filtering and sorting:

```
GET /api/v1/patients?search=Nakamya&gender=female&sort=-created_at
GET /api/v1/lab-results?status=critical&from_date=2026-01-01&to_date=2026-03-31
```

- Prefix `-` for descending sort
- Date ranges use `from_date` and `to_date` parameters
- Search is case-insensitive and uses full-text search where available

---

## 6. Security Implementation Standards

### 6.1 Authentication

**Web UI (Session-based):**

- Laravel session authentication with CSRF protection on all POST/PUT/PATCH/DELETE routes
- Session timeout: 15 minutes of inactivity (configurable per facility)
- MFA required for: Super Admin, Facility Admin, Accountant, Auditor roles
- MFA method: TOTP (Google Authenticator, Authy) or SMS OTP via Africa's Talking

**API/Mobile (JWT-based):**

- Laravel Sanctum with JWT tokens
- Access token lifetime: 60 minutes
- Refresh token rotation: new refresh token issued on every refresh; old token invalidated
- JWT claims include `fid` (facility_id) for tenant resolution
- Refresh tokens stored server-side with device fingerprint for revocation

### 6.2 Encryption

- **PHI at rest:** `encrypt()` helper using AES-256-GCM for: patient NIN, HIV status, mental health notes, substance abuse records, reproductive health records
- **Transport:** TLS 1.2+ on all endpoints; TLS 1.0 and 1.1 disabled at the load balancer
- **Database encryption key:** stored in environment variable `APP_KEY`, rotated annually with key versioning
- **File uploads:** encrypted at rest on S3 using AWS SSE-S3

### 6.3 Audit Trail

Every CRUD operation on patient data generates an audit log entry via `AuditService::log()`:

```php
AuditService::log(
    action: AuditAction::CREATE,
    entity: 'patients',
    entityId: $patient->id,
    facilityId: $facilityId,
    userId: $userId,
    before: null,
    after: $patient->toArray(),
    ipAddress: $request->ip(),
    userAgent: $request->userAgent()
);
```

Audit logs are append-only. No update or delete operations are permitted on the `audit_logs` table. The table uses soft deletes as a secondary safeguard but the application never calls `delete()` on audit records.

### 6.4 Tenant Isolation

- Every tenant-scoped query passes through `BaseRepository`, which injects `WHERE facility_id = ?`
- The `FacilityScope` global scope on Eloquent models provides a secondary defence layer
- Direct use of `DB::table()` or `DB::raw()` is prohibited in application code -- all queries pass through repositories
- CI includes a static analysis rule that scans for `DB::table(`, `DB::raw(`, and `DB::statement(` in `app/` and fails the build if found outside `database/migrations/`

### 6.5 Input Validation

- All input is validated through Laravel Form Requests before reaching the controller
- File uploads: validated for MIME type (whitelist), maximum size (10 MB for documents, 50 MB for DICOM images), and scanned for malware using ClamAV
- SQL injection prevention: all queries use parameterised bindings; no string interpolation in queries
- XSS prevention: all output escaped via Blade `{{ }}` syntax; `{!! !!}` prohibited except for explicitly sanitised HTML (FHIR narrative)

---

## 7. Testing Standards

### 7.1 Test Framework

- **PHPUnit** for all PHP tests (unit, feature, integration)
- **Pest PHP** as optional wrapper for expressive test syntax
- Test database: SQLite in-memory for unit tests (speed), MySQL for integration tests (parity with production)

### 7.2 Coverage Requirements

| Layer | Minimum Coverage | Rationale |
|---|---|---|
| Services | 80% | Core business logic |
| CDS rules | 100% | Patient safety -- every rule must have positive and negative test cases |
| Repositories | 60% | Data access with tenant scoping |
| Controllers | Feature tests cover these | No unit tests on controllers; feature tests verify HTTP behaviour |
| Form Requests | 80% | Validation rules for clinical data entry |

### 7.3 Test Naming

All test methods follow the pattern:

```php
public function test_it_registers_a_new_patient_with_valid_demographics(): void
```

The name describes the behaviour under test, not the implementation.

### 7.4 Test Data Generation

- Laravel Factories for all models: `PatientFactory`, `EncounterFactory`, `PrescriptionFactory`
- Factories produce realistic clinical data (valid ICD-10 codes, plausible vital sign ranges, Uganda-format phone numbers)
- Sensitive data in factories uses obviously fake values: `NIN: CM0000000000000`, `Phone: +256700000001`

### 7.5 Tenant-Aware Test Helpers

Tests that require tenant context use the helper:

```php
$this->actingAsFacility($facility)
     ->actingAs($user)
     ->postJson('/api/v1/patients', $payload)
     ->assertStatus(201);
```

`actingAsFacility()` sets the facility context in the request, ensuring repository-level tenant scoping is exercised during tests.

### 7.6 CDS Test Requirements

Every CDS rule must have:

1. A positive test: input triggers the expected alert at the correct severity tier
2. A negative test: input within safe range produces no alert
3. A boundary test: input at the exact threshold value
4. An override test: Tier 3 alert is overridable with reason; Tier 4 alert is not overridable

---

## 8. Git Workflow

### 8.1 Branch Naming

| Branch Type | Pattern | Example |
|---|---|---|
| Feature | `feature/<module>-<description>` | `feature/pharmacy-narcotic-register` |
| Bug fix | `fix/<issue-number>-<description>` | `fix/142-duplicate-billing-charge` |
| Hotfix | `hotfix/<description>` | `hotfix/critical-value-escalation` |
| Release | `release/<version>` | `release/1.2.0` |

### 8.2 Commit Messages

Conventional Commits format:

```
feat(pharmacy): add narcotic register with running balance
fix(billing): prevent duplicate charge on partial dispense
refactor(auth): extract MFA verification to middleware
test(cds): add boundary tests for paediatric dose ceiling
docs(api): document insurance claim endpoints
chore(ci): add PHPStan level 8 to pipeline
```

### 8.3 Pull Request Requirements

- All changes to `main` require a pull request with at least 1 reviewer
- PR description must include: what changed, why, how to test
- CI must pass: lint (PHP CS Fixer), static analysis (PHPStan level 8), all tests, security scan
- No force-pushes to `main`

### 8.4 CI Pipeline

The CI pipeline runs on every push and PR:

1. **Lint:** PHP CS Fixer (PSR-12), ESLint for JavaScript
2. **Static Analysis:** PHPStan level 8 with Larastan
3. **Unit Tests:** PHPUnit with SQLite in-memory
4. **Integration Tests:** PHPUnit with MySQL 8.x service container
5. **Security Scan:** `composer audit` for known vulnerabilities, CI rule for `DB::raw()` usage
6. **Coverage Report:** uploaded to coverage tracking service; PR blocked if coverage drops below threshold

---

## 9. Data Migration from Legacy Systems

### 9.1 Supported Migration Sources

Medic8 provides an import wizard for facilities transitioning from:

1. **Paper-based records** -- manual data entry with validation assistance
2. **ClinicMaster** -- CSV export with field mapping
3. **OpenMRS** -- database export with concept dictionary mapping

### 9.2 Import Templates

CSV/Excel import templates are provided per module:

| Module | Template Fields | Validation Rules |
|---|---|---|
| Patients | first_name, last_name, sex, date_of_birth, phone, nin, address | DOB format: YYYY-MM-DD; sex: M/F; phone: +256 format |
| Staff | name, role, licence_number, licence_expiry, department | Role must match Medic8 role list |
| Pharmacy inventory | generic_name, brand_name, quantity, unit_cost, expiry_date, batch_number | Expiry must be future date |
| Lab test catalogue | test_name, sample_type, reference_range_low, reference_range_high, unit | Numeric ranges required |
| Price list | service_name, category, price, insurance_price | Price in UGX smallest unit |

### 9.3 Import Validation

- **Mode:** Skip-and-report. Invalid rows are skipped and logged to an error report. Valid rows are imported. The facility reviews the error report and corrects source data for re-import
- **Duplicate detection:** EMPI matching runs during patient import. Rows matching an existing patient above 80% confidence are flagged for manual review, not auto-imported
- **Dry run:** Every import supports a dry-run mode that validates all rows and produces the error report without writing to the database

### 9.4 ClinicMaster Field Mapping

| ClinicMaster Field | Medic8 Field | Transformation |
|---|---|---|
| `PatientNo` | `mrn` | Prefix with facility code |
| `Surname`, `OtherNames` | `last_name`, `first_name` | Direct mapping |
| `Sex` | `sex` | Map: Male -> M, Female -> F |
| `DateOfBirth` | `date_of_birth` | Parse DD/MM/YYYY to YYYY-MM-DD |
| `TelNo` | `phone` | Normalise to +256 format |
| `NationalID` | `nin` | Validate against NIN format (CM + 13 digits) |
| `Village`, `Parish`, `Subcounty`, `District` | `address_json` | Store as structured JSON |

### 9.5 OpenMRS Concept Dictionary Mapping

- OpenMRS concepts are mapped to Medic8 terminology codes using a mapping table maintained in `config/legacy/openmrs-concept-map.json`
- Unmapped concepts are logged for manual review
- Drug concepts are mapped to the Medic8 formulary by ATC code where available
- Diagnosis concepts are mapped to ICD-10 codes

### 9.6 Data NOT Imported

The following data categories are excluded from legacy migration:

| Excluded Data | Reason |
|---|---|
| Historical clinical notes (free-text) | Unstructured format; no reliable way to parse into Medic8 fields |
| Historical billing transactions | Reconciliation risk; facilities start with a clean financial ledger |
| User accounts and passwords | Security risk; all users register fresh with new credentials |
| Audit logs from legacy systems | Incompatible schema; legacy audit trail is archived separately |

### 9.7 Migration Checklist

1. Export data from legacy system using provided instructions
2. Run data through Medic8 import template (column mapping)
3. Execute dry-run import; review error report
4. Correct source data; re-run dry run until error rate is below 5%
5. Execute live import
6. Verify patient count, staff count, and inventory totals match source
7. Archive legacy system data per facility retention policy
8. Begin parallel operation (legacy + Medic8) for 2 weeks before full cutover

---

## 10. Environment Configuration

### 10.1 Environment Variables

All environment-specific configuration is stored in `.env` and never committed to version control.

| Variable | Purpose | Example |
|---|---|---|
| `APP_KEY` | Encryption key (AES-256) | `base64:...` |
| `DB_HOST`, `DB_DATABASE`, `DB_USERNAME`, `DB_PASSWORD` | MySQL connection | `127.0.0.1`, `medic8`, `root`, `secret` |
| `REDIS_HOST`, `REDIS_PORT` | Redis connection | `127.0.0.1`, `6379` |
| `AFRICAS_TALKING_API_KEY` | SMS gateway | `atsk_...` |
| `AFRICAS_TALKING_USERNAME` | SMS gateway account | `medic8` |
| `MTN_MOMO_API_KEY`, `MTN_MOMO_API_SECRET` | Mobile money payments | API credentials |
| `AIRTEL_MONEY_API_KEY`, `AIRTEL_MONEY_API_SECRET` | Mobile money payments | API credentials |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_BUCKET` | S3 document storage | AWS credentials |
| `DHIS2_BASE_URL`, `DHIS2_USERNAME`, `DHIS2_PASSWORD` | HMIS reporting | `https://hmis2.health.go.ug` |
| `CDS_DRUG_INTERACTION_DB` | Drug interaction database source | `drugbank` or `rxnorm` |
| `FHIR_BASE_URL` | FHIR R4 API base URL | `https://fhir.medic8.com/r4` |

### 10.2 Configuration Caching

- Run `php artisan config:cache` on every deployment
- Never use `env()` outside of `config/*.php` files -- always use `config()` helper in application code
- Configuration is cached as a single PHP array for performance

---

## 11. Deployment Standards

### 11.1 Deployment Checklist

1. Run `composer install --no-dev --optimize-autoloader`
2. Run `npm run build` for production assets
3. Run `php artisan config:cache`
4. Run `php artisan route:cache`
5. Run `php artisan view:cache`
6. Run `php artisan migrate --force`
7. Restart Horizon workers: `php artisan horizon:terminate`
8. Clear and warm application cache: `php artisan cache:clear`
9. Verify health check endpoint responds: `GET /api/health`

### 11.2 Health Check Endpoint

`GET /api/health` returns:

```json
{
  "status": "healthy",
  "checks": {
    "database": "ok",
    "redis": "ok",
    "horizon": "running",
    "disk_space": "ok",
    "php_version": "8.2.15"
  }
}
```

Any failed check returns `"status": "unhealthy"` with HTTP 503.

---

## AI Intelligence Module — Implementation Guide

### Implementing `AIProviderInterface`

The interface contract all adapters must satisfy:

```php
interface AIProviderInterface
{
    public function complete(string $prompt, CompletionOptions $options): CompletionResponse;
    public function chat(array $messages, ChatOptions $options): ChatResponse;
    public function embed(string $text): EmbeddingVector;
}
```

Steps to add a new adapter:

1. Create a class `MyProviderAdapter` in `app/AI/Adapters/` that implements `AIProviderInterface`.
2. Implement all three methods. Throw `AIProviderException` for any non-recoverable error; throw `AIProviderTimeoutException` for timeout (caught by the failover handler).
3. Register the adapter in `config/ai.php` under the `adapters` key with the provider slug (e.g., `'myprovider' => MyProviderAdapter::class`).
4. Add the provider slug to the `primary_provider` ENUM validation rule in `TenantAIConfigRequest`.
5. No other code changes are required. The failover handler and token metering are adapter-agnostic.

### Provider Failover Implementation

`AICapabilityService` wraps every adapter call in a try-catch. Flow:

1. Call primary adapter. If `AIProviderTimeoutException` is thrown or response time exceeds 10 s, catch and log.
2. Instantiate the failover adapter from `tenant_ai_config.failover_provider`.
3. Call failover adapter. If it also fails within 10 s, throw `AIUnavailableException`.
4. Catch `AIUnavailableException` at the controller layer. Return HTTP 503 with body `{ "error": "ai_unavailable", "message": "AI service temporarily unavailable. Please complete this step manually." }`.
5. Log the failover event to `ai_usage_log` with `was_failover = true`.

### Token Metering Implementation

After every successful adapter call:

1. Extract `input_tokens` and `output_tokens` from the adapter response.
2. Call `TokenMeteringService::meter(tenantId, capability, provider, model, inputTokens, outputTokens, latencyMs)`.
3. `meter()` inserts a row into `ai_usage_log` and calls `decrementBalance()` on the `tenant_ai_config` record (credit pack model only).
4. If `credit_balance` would go negative, `decrementBalance()` throws `CreditExhaustedException`. Catch at the capability service level and return HTTP 402.

---

## i18n — Implementation Guide

### String Key Naming Convention

All localisation keys follow the pattern `module.context.label`. Keys are lowercase and underscore-delimited. Examples:

- `opd.triage.blood_pressure_label`
- `billing.payment.mobile_money_button`
- `pharmacy.alert.drug_interaction_fatal`

### Adding a New String

1. Define the string in `lang/en/<module>.php` first (English is mandatory).
2. Add the same key to `lang/fr/<module>.php` with a contextual French translation (not word-for-word).
3. Add the same key to `lang/sw/<module>.php` with a contextual Kiswahili translation.
4. If the Kiswahili or French translation is not yet available, add the key with value `null`. The build system will emit `[I18N-GAP: <key>]` and the CI pipeline will fail on the `release` branch.
5. In PHP, use `__('module.context.label')`. In Blade, use `{{ __('module.context.label') }}`.

### Running the i18n Audit

- Run `php artisan i18n:audit` to list all keys present in `lang/en/` but missing or null in `lang/fr/` or `lang/sw/`.
- The audit output maps directly to `[I18N-GAP]` tags.
- All gaps must be resolved before a module ships to production.

Build command:

```bash
php artisan i18n:audit
```
