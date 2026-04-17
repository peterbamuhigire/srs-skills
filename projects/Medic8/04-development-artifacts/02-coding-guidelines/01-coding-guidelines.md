# Coding Guidelines -- Medic8 Healthcare Management System

**Document ID:** DA-02-01
**Project:** Medic8
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft -- Pending Consultant Review

---

## 1. PHP Coding Standards

### 1.1 Language Configuration

Every PHP file in the application starts with:

```php
<?php

declare(strict_types=1);
```

No exceptions. Test files, configuration files, and migration files all include the strict types declaration.

### 1.2 PSR-12 Compliance

All code follows PSR-12 Extended Coding Style. PHP CS Fixer enforces this in CI with the following non-default rules:

- `ordered_imports` -- imports sorted alphabetically
- `no_unused_imports` -- unused imports removed
- `trailing_comma_in_multiline` -- trailing commas in multiline arrays, arguments, and parameters
- `single_quote` -- single quotes for strings that do not contain interpolation

### 1.3 Naming Conventions

| Artifact | Convention | Example |
|---|---|---|
| Class | PascalCase, singular noun | `Patient`, `Encounter`, `Prescription` |
| Interface | PascalCase with `Interface` suffix | `PatientRepositoryInterface` |
| Method | camelCase, verb-first | `getPatient()`, `createEncounter()`, `dispenseFor()` |
| Variable | camelCase, descriptive | `$patientId`, `$facilityId`, `$prescriptionItems` |
| Constant | UPPER_SNAKE_CASE | `MAX_LOGIN_ATTEMPTS`, `CDS_TIER_FATAL` |
| Enum | PascalCase class, PascalCase cases | `TiagePriority::Emergency` |
| Config key | snake_case, dot-separated namespace | `medic8.cds.alert_timeout` |
| Database column | snake_case | `facility_id`, `date_of_birth`, `created_at` |
| Route parameter | camelCase | `/patients/{patientId}/encounters/{encounterId}` |

### 1.4 Type Hints

- All method parameters must have type hints
- All method return types must be declared
- Use union types (`string|int`) sparingly; prefer specific types
- Use `?Type` for nullable parameters; never pass `null` as a default for non-nullable parameters
- Use PHP 8.2 `true`, `false`, and `null` standalone types where semantically appropriate
- Array type hints must specify the element type in PHPDoc: `@param array<int, Patient> $patients`

### 1.5 Constructor Promotion

Use constructor promotion for dependency injection and value objects:

```php
final class PatientService
{
    public function __construct(
        private readonly PatientRepositoryInterface $patientRepository,
        private readonly EMPIService $empiService,
        private readonly AuditService $auditService,
    ) {}
}
```

### 1.6 Enums

Use PHP 8.1+ backed enums for all domain value sets:

```php
enum TriagePriority: string
{
    case Emergency = 'emergency';
    case Urgent = 'urgent';
    case SemiUrgent = 'semi_urgent';
    case NonUrgent = 'non_urgent';
}

enum CDSAlertTier: int
{
    case Info = 1;
    case Warning = 2;
    case Serious = 3;
    case Fatal = 4;
}
```

Store the backed value in the database. Cast to the enum in the Eloquent model.

---

## 2. Laravel Conventions

### 2.1 Controllers

Controllers are resource controllers with a maximum of 5 public methods:

| Method | HTTP Verb | Route | Purpose |
|---|---|---|---|
| `index` | GET | `/api/v1/patients` | List (paginated) |
| `store` | POST | `/api/v1/patients` | Create |
| `show` | GET | `/api/v1/patients/{id}` | Read single |
| `update` | PUT/PATCH | `/api/v1/patients/{id}` | Update |
| `destroy` | DELETE | `/api/v1/patients/{id}` | Delete |

If a resource requires additional actions (e.g., `merge`, `transfer`, `discharge`), create a dedicated single-action controller:

```php
final class MergePatientController extends Controller
{
    public function __invoke(MergePatientRequest $request, int $patientId): JsonResponse
    {
        $result = $this->patientService->merge($patientId, $request->validated());
        return response()->json([
            'success' => true,
            'data' => new PatientResource($result),
            'message' => 'Patient records merged successfully',
            'errors' => [],
        ]);
    }
}
```

### 2.2 Form Requests

One Form Request per endpoint, named `{Action}{Resource}Request`:

| Endpoint | Form Request |
|---|---|
| `POST /patients` | `RegisterPatientRequest` |
| `PUT /patients/{id}` | `UpdatePatientRequest` |
| `POST /encounters/{id}/prescriptions` | `CreatePrescriptionRequest` |
| `POST /lab-results/{id}/validate` | `ValidateLabResultRequest` |

Form Requests handle:

- Validation rules (including custom rules like `ICD10Code`, `NINFormat`, `UgandaPhoneNumber`)
- Authorisation via the `authorize()` method (delegates to Policy)
- Input sanitisation via `prepareForValidation()` (e.g., normalise phone numbers to +256 format)

### 2.3 API Resources

Use Laravel API Resources to transform model data into API responses. Never return Eloquent models directly from controllers.

```php
final class PatientResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'mrn' => $this->mrn,
            'first_name' => $this->first_name,
            'last_name' => $this->last_name,
            'sex' => $this->sex,
            'date_of_birth' => $this->date_of_birth->toDateString(),
            'age' => $this->date_of_birth->age,
            'blood_group' => $this->blood_group,
            'phone' => $this->phone,
            'registered_at' => $this->created_at->toIso8601String(),
        ];
    }
}
```

Note: `facility_id` is never included in API responses. Patient NIN and other PHI fields are omitted from list responses and included only in detail responses with appropriate ABAC checks.

### 2.4 Policies

Every model that supports authorisation has a Policy class. Policies are the single source of truth for access control:

```php
final class PatientPolicy
{
    public function view(User $user, Patient $patient): bool
    {
        return $user->facility_id === $patient->facility_id
            && $user->hasPermission('patients.view');
    }

    public function viewSensitive(User $user, Patient $patient): bool
    {
        return $this->view($user, $patient)
            && $user->hasAttribute('sensitive_record_access');
    }
}
```

Sensitive record access (HIV, mental health, reproductive health, substance abuse) uses Attribute-Based Access Control (ABAC) layered on top of RBAC (BR-DATA-001, HIGH-005).

### 2.5 Observers

Observers are used only for cross-cutting concerns that apply uniformly to a model lifecycle. Permitted uses:

- **AuditObserver:** logs create, update, delete events to the audit trail
- **CacheInvalidationObserver:** clears relevant cache keys on model changes

Observers must not contain business logic. If a model change triggers a business action (e.g., dispensing a drug triggers a billing charge), use an Event/Listener pair instead.

### 2.6 Events and Listeners

Domain events are dispatched by services for significant state changes:

```php
// In PharmacyService::dispense()
event(new DrugDispensed($prescription, $dispenseRecord, $facilityId));
```

Listeners handle cross-module side effects:

| Event | Listener | Effect |
|---|---|---|
| `DrugDispensed` | `PostBillingChargeOnDrugDispensed` | Creates billing charge (BR-FIN-001) |
| `DrugDispensed` | `DeductStockOnDrugDispensed` | Reduces pharmacy stock |
| `DrugDispensed` | `LogNarcoticOnDrugDispensed` | Adds narcotic register entry if controlled substance (BR-RX-001) |
| `LabResultValidated` | `CheckCriticalValueOnLabResult` | Triggers escalation if panic threshold exceeded (BR-CLIN-003) |
| `PatientRegistered` | `RunEMPIMatchOnPatientRegistered` | Runs duplicate detection (BR-PID-002) |
| `VitalSignsRecorded` | `CalculateNEWS2OnVitalSigns` | Computes Early Warning Score (BR-CLIN-007) |

### 2.7 Service Provider Registration

- Bind repository interfaces to concrete implementations in `AppServiceProvider`
- Register event-listener mappings in `EventServiceProvider`
- Register custom validation rules in `AppServiceProvider::boot()`
- Use contextual binding for services that vary by tenant configuration

---

## 3. Healthcare-Specific Conventions

### 3.1 Tenant Context Propagation

All clinical data methods accept the facility context implicitly via the `TenantContext` singleton bound by `TenantMiddleware`. Services do not accept `$facilityId` as a parameter on every method; instead, the repository resolves it from the bound context:

```php
final class BaseRepository
{
    protected function facilityId(): int
    {
        return app(TenantContext::class)->facilityId();
    }

    protected function scopedQuery(): Builder
    {
        return $this->model->newQuery()->where('facility_id', $this->facilityId());
    }
}
```

For operations that explicitly cross tenant boundaries (e.g., EMPI lookup, Super Admin reports), use `TenantContext::asGlobal()` with audit logging.

### 3.2 Drug Name Storage

- **Primary:** `generic_name` (WHO International Nonproprietary Name) -- always populated
- **Secondary:** `brand_name` -- nullable, populated when the facility uses brand names
- Drug selection interfaces display: `generic_name (brand_name)` e.g., "Amoxicillin (Amoxil)"
- Tall Man Lettering applied to LASA drugs in selection interfaces (BR-RX-003)

### 3.3 ICD Code Storage

Every diagnosis stores both the code and the version:

```php
$table->string('icd_code', 10);       // e.g., "J18.9"
$table->tinyInteger('icd_version');    // 10 or 11
$table->string('clinical_description'); // e.g., "Pneumonia, unspecified organism"
```

Free-text diagnosis entry is not permitted (BR-DATA-006). The UI provides a searchable ICD-10/ICD-11 lookup with auto-complete.

### 3.4 Laboratory Value Storage

Lab results always store the numeric value, unit, and reference range:

```php
$table->decimal('value', 10, 4);
$table->string('unit', 20);           // e.g., "mmol/L", "g/dL", "cells/uL"
$table->decimal('reference_low', 10, 4)->nullable();
$table->decimal('reference_high', 10, 4)->nullable();
$table->string('flag', 10)->nullable(); // "H", "L", "HH" (critical high), "LL" (critical low)
```

### 3.5 Vital Sign Standards

All vital signs are stored in metric units. Conversion happens at input if the source provides non-metric values.

| Vital Sign | Unit | Column Type | Typical Range |
|---|---|---|---|
| Temperature | Celsius | `decimal(4,1)` | 35.0 -- 42.0 |
| Blood pressure (systolic) | mmHg | `smallInteger` | 60 -- 250 |
| Blood pressure (diastolic) | mmHg | `smallInteger` | 30 -- 150 |
| Pulse | bpm | `smallInteger` | 30 -- 220 |
| SpO2 | % | `tinyInteger` | 50 -- 100 |
| Weight | kg | `decimal(5,2)` | 0.50 -- 300.00 |
| Height | cm | `decimal(5,1)` | 20.0 -- 250.0 |
| BMI | kg/m2 | calculated, not stored | -- |
| MUAC | cm | `decimal(4,1)` | 5.0 -- 40.0 |
| Respiratory rate | breaths/min | `tinyInteger` | 5 -- 60 |

BMI is calculated from weight and height at query time, never stored.

### 3.6 Date and Time Handling

- **Database:** All timestamps stored in UTC
- **Display:** Converted to the facility's configured timezone (`facilities.timezone` column)
- **Patient-facing:** Dates displayed in the facility's locale format (e.g., DD/MM/YYYY for Uganda)
- **API responses:** ISO 8601 format (`2026-04-03T14:30:00Z`)

### 3.7 Money and Currency

- **Storage:** Always in the smallest currency unit as a `bigInteger`
  - UGX: store as integer (1 UGX = 1 unit, no decimals)
  - KES: store as cents (100 cents = 1 KES)
  - USD: store as cents (100 cents = 1 USD)
- **Display:** Format using `NumberFormatter` with the facility's currency locale
- **Arithmetic:** Use `bcmath` functions for all calculations; never use floating-point arithmetic on money values
- **Rounding:** Round to the nearest whole unit after all calculations are complete, not during intermediate steps

### 3.8 Patient Age

Patient age is never stored as a database field. Always calculate from `date_of_birth`:

```php
// In Patient model
public function getAgeAttribute(): int
{
    return $this->date_of_birth->age;
}

public function getAgeInMonthsAttribute(): int
{
    return $this->date_of_birth->diffInMonths(now());
}
```

For patients where only an estimated age is known at registration, calculate and store an estimated `date_of_birth` (1 January of the estimated birth year).

---

## 4. Error Handling

### 4.1 Typed Exceptions

Every domain-specific error has a typed exception class:

| Exception | HTTP Code | When Thrown |
|---|---|---|
| `PatientNotFoundException` | 404 | Patient ID does not exist in this facility |
| `EncounterNotFoundException` | 404 | Encounter ID does not exist |
| `CDSAlertException` | 460 | CDS rule fired an alert requiring acknowledgement |
| `PrescribingViolationException` | 461 | Five Rights check failed |
| `TenantViolationException` | 462 | Cross-tenant data access attempted |
| `ConsentRequiredException` | 463 | Sensitive data access without patient consent |
| `DuplicatePatientException` | 409 | EMPI match exceeds 80% confidence |
| `InsufficientStockException` | 422 | Pharmacy stock insufficient for dispensing |
| `CriticalValueException` | -- | Lab result exceeds panic threshold (internal, triggers escalation) |
| `DischargeIncompleteException` | 422 | Discharge attempted without required documentation (BR-CLIN-009) |

### 4.2 Exception Hierarchy

All Medic8 exceptions extend a common base:

```php
abstract class Medic8Exception extends \RuntimeException
{
    public function __construct(
        string $message,
        public readonly int $facilityId,
        public readonly ?string $context = null,
        int $code = 0,
        ?\Throwable $previous = null,
    ) {
        parent::__construct($message, $code, $previous);
    }
}
```

The `facilityId` is always attached for audit and debugging purposes.

### 4.3 Exception Handling Rules

- Never catch generic `\Exception` or `\Throwable` in service classes -- let exceptions propagate to the global exception handler
- The global exception handler (`app/Exceptions/Handler.php`) maps typed exceptions to HTTP response codes and the standard envelope format
- Log all exceptions with facility context: `Log::error($e->getMessage(), ['facility_id' => $e->facilityId, 'context' => $e->context])`
- For CDS exceptions: log the alert details (drug names, interaction severity, patient weight) for clinical audit
- Never expose internal exception messages to API consumers in production; return the `message` from the typed exception only

### 4.4 Retry and Circuit Breaker

External service calls (Africa's Talking SMS, MTN MoMo, DHIS2, FHIR) use retry logic:

- Retry up to 3 times with exponential backoff (1s, 2s, 4s)
- After 3 failures, log the error and queue the operation for manual retry
- Circuit breaker: if an external service fails 10 consecutive times within 5 minutes, stop calling it for 30 minutes and alert the Facility Admin

---

## 5. Security Conventions

### 5.1 PHI Logging Prohibition

The following fields must never appear in application logs, error messages, or exception context:

- Patient name (first_name, last_name)
- National Identification Number (NIN)
- Phone number
- Diagnoses (ICD codes or clinical descriptions)
- HIV status
- Mental health notes
- Prescriptions and medication lists

Log the `patient_id` (integer) instead. A developer or support engineer can look up the patient by ID through the application with appropriate ABAC permissions.

```php
// WRONG -- logs PHI
Log::info("Registered patient {$patient->first_name} {$patient->last_name}, NIN: {$patient->nin}");

// CORRECT -- logs reference only
Log::info("Patient registered", ['patient_id' => $patient->id, 'facility_id' => $facilityId]);
```

### 5.2 Tenant Isolation in Code

- Never use `DB::table()` in application code outside of `database/migrations/`
- Never use `DB::raw()` or `DB::statement()` without explicit tenant scope
- Never use `Model::withoutGlobalScopes()` in production code -- only in tests or admin tooling with audit
- Always access data through the repository layer, which enforces `WHERE facility_id = ?`

```php
// WRONG -- bypasses tenant scope
$patients = DB::table('patients')->where('last_name', 'Nakamya')->get();

// WRONG -- removes tenant safety
$patients = Patient::withoutGlobalScopes()->where('last_name', 'Nakamya')->get();

// CORRECT -- repository enforces tenant scope
$patients = $this->patientRepository->searchByLastName('Nakamya');
```

### 5.3 API Response Security

- Never expose `facility_id` in API responses -- clients do not need to know their tenant ID
- Never expose database IDs for cross-resource references in public-facing APIs; use UUIDs for patient-facing endpoints (patient portal, mobile app)
- Never return full stack traces in production error responses
- Strip `X-Powered-By` and `Server` headers at the web server level

### 5.4 File Upload Security

All file uploads (clinical documents, medical images, patient photos) are validated:

1. **MIME type whitelist:** `image/jpeg`, `image/png`, `application/pdf`, `application/dicom` (configurable per upload context)
2. **Maximum size:** 10 MB for documents, 50 MB for DICOM images, 2 MB for patient photos
3. **Malware scan:** ClamAV scan before storing to S3
4. **Storage:** uploaded to S3 with a randomised key (`{facilityId}/{uuid}.{ext}`); never stored in the public web root
5. **Access:** served through a signed URL with 15-minute expiry, not through a public URL

### 5.5 SQL Injection Prevention

- All queries use parameterised bindings via Eloquent or Query Builder
- String interpolation in SQL is prohibited
- CI scans `app/` for patterns: `DB::raw(".*\$`, `->whereRaw(".*\$`, `DB::statement(".*\$` and fails on matches

### 5.6 XSS Prevention

- All Blade output uses `{{ }}` (escaped). The `{!! !!}` syntax is prohibited except for:
  - FHIR narrative HTML (sanitised through HTMLPurifier before rendering)
  - Rich-text clinical notes (sanitised through HTMLPurifier with a medical whitelist: `<p>`, `<br>`, `<strong>`, `<em>`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<tr>`, `<td>`, `<th>`)
- JavaScript: no `innerHTML` assignments; use `textContent` for dynamic text insertion
- API responses: JSON-encoded (inherently XSS-safe when consumed by JavaScript)

---

## 6. Queue and Job Conventions

### 6.1 TenantAwareJob Base Class

All queued jobs extend `TenantAwareJob`, which serialises and restores the `facility_id` context:

```php
abstract class TenantAwareJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public function __construct(
        public readonly int $facilityId,
    ) {}

    public function handle(): void
    {
        app(TenantContext::class)->set($this->facilityId);
        $this->execute();
    }

    abstract protected function execute(): void;
}
```

### 6.2 Queue Names

| Queue | Purpose | Workers |
|---|---|---|
| `default` | Standard async operations | 2 |
| `clinical` | CDS alerts, critical value escalation | 4 (higher priority) |
| `billing` | Auto-billing, insurance claim generation | 2 |
| `reporting` | HMIS report generation, DHIS2 push | 1 |
| `notifications` | SMS, email, WebSocket push | 2 |
| `imports` | Legacy data migration imports | 1 |

### 6.3 Job Failure Handling

- Failed jobs are logged to the `failed_jobs` table with full payload and exception
- Critical jobs (CDS alerts, critical lab values) retry immediately up to 3 times
- Non-critical jobs (SMS, report generation) retry with exponential backoff
- Failed notification jobs are surfaced on the Facility Admin dashboard

---

## 7. Caching Conventions

### 7.1 Cache Key Naming

Cache keys follow the pattern: `{facilityId}:{entity}:{identifier}`:

```php
// Patient cache
"42:patient:1205"

// Facility-wide cache
"42:price_list:current"
"42:formulary:active"

// Global cache (no facility prefix)
"global:icd10:index"
"global:drug_interactions:version"
```

### 7.2 Cache TTL Standards

| Data Type | TTL | Rationale |
|---|---|---|
| Patient demographics | 5 minutes | Changes infrequently; stale data acceptable briefly |
| Price list | 1 hour | Changes require admin action |
| Drug formulary | 1 hour | Changes require pharmacy lead action |
| ICD-10 code index | 24 hours | Static reference data |
| Drug interaction database | 24 hours | Updated on deployment |
| HMIS form mappings | 24 hours | Static configuration |
| Active session data | 15 minutes | Matches session timeout |

### 7.3 Cache Invalidation

- Model observers invalidate cache keys on create, update, and delete
- Price list and formulary changes broadcast a cache-clear event to all Horizon workers
- Never rely on TTL alone for clinical data; always invalidate on write

---

## 8. Logging Standards

### 8.1 Log Levels

| Level | Use | Example |
|---|---|---|
| `emergency` | System unusable | Database connection lost |
| `critical` | Critical clinical event | CDS Tier 4 alert fired, critical lab value |
| `error` | Runtime error | External API failure, unhandled exception |
| `warning` | Abnormal but handled | MTN MoMo timeout (retrying), stock below minimum |
| `info` | Significant business event | Patient registered, drug dispensed, HMIS report generated |
| `debug` | Development diagnostics | Query execution time, cache hit/miss (disabled in production) |

### 8.2 Structured Logging

All log entries include structured context:

```php
Log::info('Drug dispensed', [
    'facility_id' => $facilityId,
    'patient_id' => $patient->id,
    'prescription_id' => $prescription->id,
    'drug_id' => $drug->id,
    'quantity' => $quantity,
    'dispenser_id' => $user->id,
]);
```

Never log PHI (Section 5.1). Never log raw SQL queries in production. Never log request/response bodies that contain clinical data.

---

## 9. Code Review Checklist

Every pull request is reviewed against the following checklist:

1. **Tenant isolation:** Does every query go through the repository layer? Is `facility_id` scoped?
2. **Type safety:** Are all parameters and return types declared? Is `strict_types` present?
3. **PHI exposure:** Does the code log, expose in API responses, or display any PHI inappropriately?
4. **Business logic placement:** Is logic in the service layer, not in controllers or models?
5. **Error handling:** Are domain-specific exceptions used? Is `\Exception` caught generically?
6. **Test coverage:** Are services tested? Are CDS rules tested at 100%? Are boundary cases covered?
7. **Naming:** Do class, method, and variable names follow the conventions in Section 1.3?
8. **Security:** Are file uploads validated? Are queries parameterised? Is output escaped?
9. **Events:** Are state changes on clinical data emitting domain events?
10. **Documentation:** Do public methods have PHPDoc? Are non-obvious algorithms commented?
