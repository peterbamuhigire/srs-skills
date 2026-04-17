---
project: Academia Pro
document: Coding Guidelines
version: "1.0"
date: 2026-04-03
standard: IEEE 730
---

# Coding Guidelines for Academia Pro

## 1 Naming Conventions

### 1.1 PHP Files and Classes

All PHP source files use PascalCase and match the class name they contain. Append a layer suffix that declares the file's architectural role.

- Compliant: `StudentFeeRepository.php`, `AttendanceService.php`, `EnrollmentController.php`
- Non-compliant: `student_fee_repo.php`, `attendanceservice.php`, `Enrollment.php` (missing suffix)

### 1.2 React / TypeScript Files and Components

React component files use PascalCase. Utility, hook, and store files use camelCase. All files end in `.tsx` (JSX) or `.ts` (pure logic).

- Compliant: `FeePaymentForm.tsx`, `useAttendance.ts`, `studentStore.ts`
- Non-compliant: `fee-payment-form.tsx`, `UseAttendance.ts`, `StudentStore.ts` (store files are camelCase)

### 1.3 Kotlin / Swift Files

Kotlin and Swift files use PascalCase matching the primary class or struct name.

- Compliant: `StudentRepository.kt`, `AttendanceViewModel.swift`
- Non-compliant: `student_repository.kt`, `attendance-view-model.swift`

### 1.4 Functions and Methods

PHP methods use camelCase with a verb-first name. TypeScript functions follow the same rule. Kotlin and Swift follow platform convention (camelCase).

- Compliant: `calculateAggregate()`, `getStudentsByTenant()`, `syncAttendanceRecords()`
- Non-compliant: `aggregate()` (no verb), `StudentsByTenant()` (PascalCase method), `calc_agg()` (abbreviation)

### 1.5 Variables

All languages use camelCase for local variables. Names must be descriptive; single-letter variables are permitted only in loop counters and lambda parameters.

- Compliant: `$outstandingBalance`, `const termStartDate`, `val enrollmentCount`
- Non-compliant: `$ob`, `const tsd`, `val ec`

### 1.6 Database Columns

MySQL columns use `snake_case`. Foreign keys follow the pattern `{referenced_table_singular}_id`. Timestamps use `created_at`, `updated_at`, `deleted_at`. Boolean flags use the `is_` prefix.

- Compliant: `tenant_id`, `student_uid`, `is_active`, `fee_amount`, `created_at`
- Non-compliant: `tenantId`, `StudentUID`, `active`, `feeAmt`, `createdAt`

### 1.7 Constants and Enums

PHP and TypeScript constants use `UPPER_SNAKE_CASE`. Group related constants in a dedicated class or object.

- Compliant: `MAX_LOGIN_ATTEMPTS = 5`, `UNEB_PLE_DIVISION_I_MAX = 4`
- Non-compliant: `maxLoginAttempts`, `PLE_Div1_Max`

### 1.8 Session Variables

All Laravel session keys must use the `academia_pro_` prefix to avoid collisions with third-party packages.

- Compliant: `academia_pro_tenant_id`, `academia_pro_current_term`
- Non-compliant: `tenant_id`, `current_term`

## 2 Code Structure

### 2.1 Backend Directory Layout (Laravel)

```
app/
  Http/
    Controllers/        # Thin controllers — delegate to Services
    Middleware/          # Tenant scoping, auth, rate limiting
    Requests/           # Form Request validation classes
  Services/             # Business logic layer
  Repositories/
    Contracts/          # Repository interfaces
    Eloquent/           # Eloquent implementations of interfaces
  DTOs/                 # Data Transfer Objects (immutable)
  Exceptions/           # Custom exception hierarchy
  Models/               # Eloquent models (data access only)
  Enums/                # PHP 8.1+ backed enums
  Events/               # Domain events
  Listeners/            # Event listeners
  Jobs/                 # Queued jobs (Horizon)
  Policies/             # Authorization policies
database/
  migrations/           # Timestamped migration files
  seeders/              # Development seed data
routes/
  api.php               # API routes (Sanctum-protected)
  web.php               # Web routes (session-protected)
tests/
  Unit/                 # Unit tests (no DB, no HTTP)
  Feature/              # Feature tests (HTTP + DB)
```

### 2.2 Frontend Directory Layout (React / TypeScript)

```
src/
  components/           # Reusable UI components
  pages/                # Route-level page components
  hooks/                # Custom React hooks
  stores/               # Zustand stores
  services/             # API client functions (Axios)
  types/                # TypeScript interfaces and type aliases
  utils/                # Pure utility functions
  lib/                  # Third-party configuration (shadcn/ui)
```

### 2.3 Module Boundaries

- Controllers must not contain business logic; they validate input via Form Requests and delegate to a Service.
- Services must not call Eloquent directly; they call Repository interfaces.
- Repository implementations enforce `tenant_id` scoping on every query.
- React components must not call Axios directly; they call functions in `services/`.

### 2.4 File and Function Length Limits

- PHP class file: 400 lines maximum. Exceeding this signals the class has too many responsibilities.
- PHP method: 30 lines maximum. Extract helper methods for longer logic.
- TypeScript component file: 300 lines maximum. Extract sub-components or custom hooks.
- TypeScript function: 25 lines maximum.

### 2.5 Import Ordering

PHP `use` statements: (1) PHP core classes, (2) Laravel framework classes, (3) third-party packages, (4) application classes. Separate each group with a blank line.

TypeScript imports: (1) React and framework imports, (2) third-party libraries, (3) application modules (`@/`), (4) relative imports. Enforce via ESLint `import/order` rule.

## 3 Design Patterns to Use

### 3.1 Repository Pattern

Every database query passes through a Repository interface. The Eloquent implementation prepends `->where('tenant_id', $tenantId)` before every query. No Eloquent calls outside Repository classes.

### 3.2 Service Layer Pattern

Business logic resides in Service classes. A Service receives Repository interfaces via constructor injection, performs domain operations, and returns DTOs.

### 3.3 Data Transfer Objects

Use immutable PHP `readonly` classes to transfer data between layers. DTOs replace associative arrays in Service return values.

```php
// Compliant
final readonly class StudentFeeDTO {
    public function __construct(
        public int $studentId,
        public int $amountOwed,
        public int $amountPaid,
    ) {}
}

// Non-compliant: returning an associative array from a Service
return ['student_id' => $id, 'owed' => $amount];
```

### 3.4 Form Requests

All input validation lives in Laravel Form Request classes. Controllers never call `$request->validate()` inline.

### 3.5 Zustand Stores (Frontend)

Each bounded context (fees, attendance, students) owns a single Zustand store. Stores hold server-cache state only when React Query is insufficient (e.g., offline PWA state).

### 3.6 MVVM + Repository (Mobile)

Android ViewModels expose `StateFlow`; iOS ViewModels expose `@Published` properties. Both delegate data access to Repository interfaces backed by Room (Android) or SwiftData (iOS) for offline-first behaviour.

## 4 Anti-Patterns to Avoid

### 4.1 God Classes

A class exceeding 400 lines or handling more than one bounded context.

- Alternative: Split into focused Service classes scoped to a single domain aggregate.

### 4.2 N+1 Queries

Looping through a collection and issuing a query per item.

- Alternative: Use eager loading (`with()`) in Repository methods or batch queries.

### 4.3 Eloquent in Controllers or Services

Calling `Model::where()` outside a Repository class bypasses tenant isolation.

- Alternative: Inject the Repository interface and call its scoped methods.

### 4.4 Magic Numbers

Embedding raw numeric values in business logic without explanation.

- Alternative: Define named constants in an Enum or constants class. Example: `UNEBGrading::PLE_DIVISION_I_MAX` instead of `4`.

### 4.5 Hardcoded Credentials or Secrets

Embedding API keys, passwords, or tokens in source code.

- Alternative: Store in `.env` and access via `config()` helper. Never commit `.env`.

### 4.6 Direct DOM Manipulation in React

Using `document.getElementById()` or `document.querySelector()` inside React components.

- Alternative: Use `useRef` hooks and React's declarative rendering model.

### 4.7 Catching Generic Exceptions Silently

Writing `catch (Exception $e) {}` with no logging or re-throw.

- Alternative: Catch the narrowest exception type and log it. Re-throw if unrecoverable.

### 4.8 String Concatenation for SQL

Building SQL with `.` or `+` operators and user input.

- Alternative: Use parameterized queries or Eloquent's query builder exclusively.

## 5 Error Handling

### 5.1 Exception Hierarchy

```
App\Exceptions\
  AcademiaProException          # Base (extends RuntimeException)
  ├── TenantMismatchException   # Tenant isolation violation
  ├── BusinessRuleException     # Domain rule violation (e.g., grading)
  ├── PaymentGatewayException   # SchoolPay / MoMo failures
  ├── ExternalApiException      # EMIS, FCM, SMS gateway errors
  └── ValidationException       # Input validation (Laravel default)
```

All custom exceptions extend `AcademiaProException`. Controllers catch specific types and map them to HTTP status codes. The global exception handler logs uncaught exceptions and returns a JSON error envelope.

### 5.2 Try-Catch Scope

- Wrap only the operation that can fail, not the entire method body.
- Never use empty `catch` blocks. At minimum, log the exception.
- Re-throw exceptions that the current layer cannot resolve.

### 5.3 Error Message Format

Backend JSON error responses follow this envelope:

```json
{
  "error": {
    "code": "PAYMENT_GATEWAY_TIMEOUT",
    "message": "SchoolPay did not respond within 15 seconds.",
    "trace_id": "abc-123-def"
  }
}
```

User-facing messages must not expose stack traces, SQL, or internal class names.

### 5.4 Frontend Async Error Handling

- Axios interceptors catch 401 (redirect to login) and 403 (show permission denied) globally.
- Component-level errors use React Error Boundaries for rendering failures.
- API call failures in Zustand actions set an `error` state property that the UI reads.

### 5.5 Mobile Error Handling

- Android: `Result<T>` sealed class wraps success and failure states from Repository calls. ViewModels expose error state via `StateFlow`.
- iOS: `Result<Success, Failure>` from Repository methods. ViewModels publish error state via `@Published`.

## 6 Logging

### 6.1 Log Levels

| Level | Usage Criteria |
|-------|---------------|
| DEBUG | Method entry/exit, intermediate calculation values. Disabled in production. |
| INFO | Successful business events: fee payment recorded, student enrolled, report generated. |
| WARN | Recoverable anomalies: payment retry, cache miss, deprecated API call. |
| ERROR | Failed operations requiring investigation: gateway timeout, tenant mismatch. |
| CRITICAL | System-level failures: database unreachable, queue worker crash, disk full. |

### 6.2 Structured Log Format

All backend logs use JSON format via Laravel's logging configuration:

```json
{
  "timestamp": "2026-04-03T10:15:30Z",
  "level": "ERROR",
  "tenant_id": 42,
  "user_id": 118,
  "trace_id": "abc-123-def",
  "channel": "payment",
  "message": "SchoolPay callback failed",
  "context": { "payment_ref": "SP-20260403-0071" }
}
```

### 6.3 PII Redaction Rules

The following data must never appear in logs in plaintext:

- Student NIN, LIN, or date of birth
- Parent/guardian phone numbers and email addresses
- Payment card numbers or mobile money account numbers
- Passwords, tokens, and API keys

Use the `[REDACTED]` placeholder when referencing these values in log messages. Implement a custom Laravel log processor that masks fields matching these categories.

## 7 Security Practices

### 7.1 Input Validation

- All HTTP input passes through Laravel Form Request classes with explicit validation rules.
- API endpoints validate `tenant_id` in the JWT payload against the requested resource's `tenant_id` before any data access.
- Frontend validates input at the component level for user experience; backend validation is authoritative.

### 7.2 SQL Injection Prevention

- Use Laravel's query builder or Eloquent parameterized methods exclusively.
- Raw SQL (`DB::raw()`) is permitted only when reviewed and approved, and must use parameter binding.
- PHPStan level 8 catches unsafe string interpolation in query contexts.

### 7.3 XSS Prevention

- Backend: Escape all output rendered in Blade templates using `{{ }}` (auto-escaped). Never use `{!! !!}` without explicit sanitization.
- Frontend: React escapes JSX output by default. Never use `dangerouslySetInnerHTML` without DOMPurify sanitization.

### 7.4 CSRF Protection

- Web routes include Laravel's `@csrf` token on every form submission.
- API routes (Sanctum token-authenticated) are exempt from CSRF but require a valid Bearer token on every request.

### 7.5 Tenant Isolation Enforcement

- Every tenant-scoped Repository method must include a `tenant_id` `WHERE` clause.
- Middleware validates that the authenticated user's `tenant_id` matches the resource's `tenant_id` on every request.
- Automated tests verify that a user from Tenant A cannot read, update, or delete data belonging to Tenant B.
- Database-level: no query may omit `tenant_id` from the `WHERE` clause on a tenant-scoped table. PHPStan custom rules or Repository base class enforcement is mandatory.

### 7.6 Authentication

- Web sessions: Laravel session guard with `academia_pro_` prefixed session keys. Session lifetime: 120 minutes idle timeout.
- API/Mobile: Laravel Sanctum tokens with `tenant_id` and `user_id` claims. Token expiry: 60 minutes; refresh tokens: 30 days.
- All passwords hashed with `bcrypt` (cost factor 12).

### 7.7 Sensitive Data Handling

- Store sensitive fields (NIN, LIN) encrypted at rest using Laravel's `Crypt` facade.
- PDPO 2019 compliance: provide data export and deletion endpoints for student records upon guardian request.
- Never log, cache, or store credentials in plaintext.

## 8 Code Review Checklist

Before approving any pull request, the reviewer shall verify each item:

### Naming and Structure

- [ ] File names, classes, and methods follow Section 1 naming conventions
- [ ] Session variables use the `academia_pro_` prefix
- [ ] No file exceeds its length limit (400 lines PHP, 300 lines TSX)
- [ ] No method exceeds its length limit (30 lines PHP, 25 lines TS)
- [ ] Imports follow the ordering convention in Section 2.5

### Architecture

- [ ] Controllers contain no business logic — only validation and delegation
- [ ] Services do not call Eloquent directly — only Repository interfaces
- [ ] Repository methods enforce `tenant_id` scoping on every query
- [ ] Data returned from Services uses DTOs, not associative arrays
- [ ] React components do not call Axios directly — only service functions

### Anti-Patterns

- [ ] No God classes (single responsibility verified)
- [ ] No N+1 queries (eager loading or batch queries used)
- [ ] No magic numbers (constants or enums used)
- [ ] No hardcoded credentials or secrets
- [ ] No direct DOM manipulation in React components
- [ ] No string-concatenated SQL

### Error Handling and Logging

- [ ] Exceptions extend `AcademiaProException` hierarchy
- [ ] No empty `catch` blocks
- [ ] Error responses follow the JSON envelope format
- [ ] Log statements use the correct level per Section 6.1 criteria
- [ ] No PII appears in log messages

### Security

- [ ] All input validated via Form Requests (backend) and component validation (frontend)
- [ ] SQL uses parameterized queries exclusively
- [ ] No use of `{!! !!}` without DOMPurify or explicit sanitization
- [ ] `tenant_id` validated on every tenant-scoped request
- [ ] Sensitive fields encrypted at rest

### Testing

- [ ] Backend test coverage ≥ 80%
- [ ] UNEB grading and fee calculation test coverage = 100%
- [ ] Frontend test coverage ≥ 70%
- [ ] Tenant isolation test exists for every new tenant-scoped endpoint


---

## AI Security Coding Rules

The following rules apply to all code touching the AI Module. Violations are treated as critical security findings and block PR merge.

### AI-SEC-001: Never Interpolate User Input Directly into a Prompt

**Prohibited:**
```php
$prompt = "Analyse this feedback: {$request->input('text')}";
```

**Required:**
```php
$cleaned = $this->sanitiser->sanitise($request->input('text'));
$cleaned = $this->scrubber->scrub($cleaned, $tenantId);
$prompt = "Analyse this feedback: {$cleaned}";
```

All user-supplied text must pass through `AIInputSanitiser::sanitise()` and `PIIScrubber::scrub()` before inclusion in any prompt string.

### AI-SEC-002: Always Validate AI JSON Output Before Writing to the Database

**Prohibited:**
```php
$result = json_decode($response->content, true);
DB::table('nlp_results')->insert(['result_json' => $response->content]);
```

**Required:**
```php
$result = AIOutputValidator::validate($response->content, AtRiskSchema::class);
// Throws AIOutputInvalidException if schema fails — no DB write occurs
DB::table('nlp_results')->insert(['result_json' => json_encode($result)]);
```

### AI-SEC-003: Never Log Prompt Content

Prompt strings must never appear in application logs (Laravel `Log::info()`, `Log::debug()`, etc.). Log the prompt hash only.

```php
Log::info('AI call dispatched', [
    'feature' => $featureSlug,
    'prompt_hash' => hash('sha256', $prompt), // hash only — never $prompt
    'tenant_id' => $tenantId,
]);
```

### AI-SEC-004: Always Call the Gate Before the Budget Guard

```php
// Correct order:
AIGate::check($tenantId, $featureSlug);   // 1. Is the module active and this feature enabled?
BudgetGuard::check($tenantId);             // 2. Is there budget remaining?
// ... proceed with API call
```

Reversing the order causes a database read on `ai_usage_monthly` for tenants who have not purchased the AI module — unnecessary load and a potential information leak.

### AI-SEC-005: Never Store Plaintext Prompts or Responses

Only SHA-256 hashes are written to `ai_audit_log`. This is enforced by the `AIMeteredClient` pipeline. Do not bypass the pipeline to write directly to `ai_audit_log` with plaintext content.

### AI-SEC-006: Set pii_scrubbed = 0 Only When the Scrubber Is Genuinely Bypassed — And Treat It as an Alert Condition

If a prompt builder is designed to never contain PII (e.g., aggregated briefing data), set `pii_scrubbed = 1` regardless — because no scrubbing was needed, not because it was skipped. Set `pii_scrubbed = 0` only when the scrubber was explicitly bypassed. Any row in `ai_audit_log` with `pii_scrubbed = 0` triggers an automated alert to the system administrator.
