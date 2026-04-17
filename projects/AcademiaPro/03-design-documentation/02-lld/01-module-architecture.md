# Low-Level Design — Academia Pro Phase 1

**Document ID:** DD-02-01
**Project:** Academia Pro
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Pending Consultant Review

---

## 1. Purpose

This document specifies the internal architecture of every Phase 1 module: service class contracts, repository interfaces, controller routing, validation rules, error handling, queue jobs, caching, and event-driven flows. It is the implementation-level companion to the High-Level Design (DD-01) and OpenAPI 3.1 Specification (DD-03).

---

## 2. Architectural Conventions

### 2.1 Layer Responsibility

Every feature follows a strict 4-layer architecture. No layer may skip a layer below it.

```
Controller → Service → Repository → Database
```

| Layer | Responsibility | May Call |
|---|---|---|
| Controller | HTTP request/response handling, input validation, response formatting | Service |
| Service | Business logic, orchestration, authorisation checks, event dispatching | Repository, other Services |
| Repository | Data access, tenant scoping, query construction | Database (Eloquent/Query Builder) |
| Model | Column casting, relationships, attribute accessors | — |

### 2.2 Naming Conventions

| Artifact | Pattern | Example |
|---|---|---|
| Controller | `{Entity}Controller` | `StudentController` |
| Service | `{Entity}Service` | `StudentService` |
| Repository | `{Entity}Repository` (concrete), `{Entity}RepositoryInterface` (contract) | `StudentRepository` |
| Form Request | `{Action}{Entity}Request` | `AdmitStudentRequest` |
| Job | `{Action}{Entity}Job` | `SendFeeReminderJob` |
| Event | `{Entity}{Action}Event` | `StudentAdmittedEvent` |
| Listener | `{Action}On{Event}` | `CreateAuditLogOnStudentAdmitted` |
| Policy | `{Entity}Policy` | `StudentPolicy` |

### 2.3 Directory Structure

```
app/
├── Http/
│   ├── Controllers/
│   │   ├── Api/V1/                    # Tenant-scoped API controllers
│   │   └── AdminPanel/Api/V1/         # Super Admin controllers
│   ├── Middleware/
│   └── Requests/                      # Form Request validation classes
├── Services/                          # Business logic
├── Repositories/
│   ├── Contracts/                     # Interfaces
│   └── Eloquent/                      # Concrete implementations
├── Models/
├── Events/
├── Listeners/
├── Jobs/
├── Policies/
└── Exceptions/
```

---

## 3. Module Specifications

### 3.1 Authentication Module

**Files:**
- `AuthController` — login, refresh, logout, me
- `AuthService` — credential validation, token generation, session management
- `TokenRepository` — Sanctum token CRUD

**Login Flow (FR-AUTH-002):**
1. `AuthController@login` receives `LoginRequest` (validates username, password, device_id).
2. `AuthService@authenticate()`:
   - Queries `users` by username.
   - Checks `failed_login_attempts >= 5` → throws `AccountLockedException` (HTTP 403).
   - Verifies password with `Hash::check()` (Argon2id).
   - Resets `failed_login_attempts` to 0 on success.
   - Loads user's `tenant_id` and `role` from `user_roles`.
   - Creates Sanctum token with abilities: `['tenant_id' => $tenantId, 'user_id' => $user->id, 'role' => $role]`.
   - Creates refresh token in `api_refresh_tokens` table (30-day TTL).
3. Returns `TokenPair` (access_token, refresh_token, expires_in, token_type).

**Failed Login:**
- Increments `failed_login_attempts` on the user record.
- At 5 failures, sets `locked_until = now() + 30 minutes`.
- Returns `INVALID_CREDENTIALS` (HTTP 401) or `ACCOUNT_LOCKED` (HTTP 403).

**Token Refresh (FR-AUTH-003):**
1. `AuthController@refresh` receives `RefreshTokenRequest`.
2. `AuthService@refreshToken()`:
   - Looks up `api_refresh_tokens` by token hash.
   - Validates: not expired, not revoked.
   - Revokes the submitted refresh token immediately (rotation).
   - Issues new access token + new refresh token.
   - If the submitted token was already revoked (replay attack), revokes ALL tokens for that user/device and returns `TOKEN_REVOKED` (HTTP 401).

**Logout (FR-AUTH-004):**
1. Revokes all refresh tokens for the authenticated `device_id`.
2. Deletes the current Sanctum access token.

---

### 3.2 Student Information Module

**Files:**
- `StudentController` — CRUD, lookup, transfer, retention lock
- `StudentService` — admission logic, global identity matching, transfer workflow
- `StudentRepository` — tenant-scoped student queries
- `GlobalStudentRepository` — cross-tenant global identity queries (not tenant-scoped)
- `AdmitStudentRequest`, `UpdateStudentRequest` — validation

**Admission Flow (FR-SIS-001):**
1. `StudentController@store` receives `AdmitStudentRequest`.
2. `StudentService@admitStudent()`:
   - If NIN or LIN is provided, calls `GlobalStudentRepository@findByIdentifier()`.
   - If a global match exists:
     - Checks `school_enrollments` for an active enrollment at another school (BR-STU-004). If found → throws `StudentAlreadyEnrolledException` (HTTP 409).
     - Uses the existing `student_uid`.
   - If no global match:
     - Creates a new `global_students` record with UUID.
     - Creates `student_identifiers` records for NIN/LIN.
   - Creates a `school_enrollments` record linked to the global `student_uid`.
   - Generates `local_admission_number` if not provided (format: `{YEAR}/{SEQ}`).
   - Dispatches `StudentAdmittedEvent`.
3. Returns the full `Student` resource.

**Transfer Out (FR-SIS-004):**
1. `StudentService@transferOut()`:
   - Validates the student has `status = active`.
   - Sets `school_enrollments.status = transferred`.
   - Sets `school_enrollments.transfer_date` and `transfer_reason`.
   - Creates a `school_departures` record with `reason = transferred_platform` or `transferred_external`.
   - Dispatches `StudentTransferredEvent`.
   - This action is immutable — no reversal endpoint exists.

**Retention Lock (FR-SIS-005):**
1. `StudentService@setRetentionLock()`:
   - Sets `school_enrollments.retention_locked = true` and `retention_lock_reason`.
   - A retention-locked student is excluded from the Promotion Wizard's default bulk-promote action.
   - Only the Head Teacher may resolve the lock.

---

### 3.3 Academics Module

**Files:**
- `AcademicYearController`, `ClassController`, `SubjectController`, `TimetableController`
- `AcademicYearService` — year lifecycle, promotion wizard orchestration
- `PromotionWizardService` — bulk promotion, repeat, departure processing
- `AcademicYearRepository`, `ClassRepository`, `SubjectRepository`, `TimetableRepository`

**Academic Year Lifecycle (FR-ACA-001):**
- State machine: `draft → active → closed`.
- `draft → active` transition requires `promotion_wizard_complete = true` (BR-PROM-001).
- Only one year may be `active` at a time per tenant.
- Closing a year triggers the `AcademicYearClosedEvent`, which schedules the `LockHistoricalRecordsJob` (BR-PROM-005) with a 30-day delay.

**Promotion Wizard (BR-PROM-001 – BR-PROM-007):**
1. `PromotionWizardService@getClassStatuses()` — returns all classes with their promotion status (pending/promoted/departed/skipped).
2. `PromotionWizardService@submitDecisions()`:
   - Accepts an array of `{student_enrollment_id, action, departure_reason}`.
   - For `action = promote`: creates a new `school_enrollments` record in the destination class for the new year.
   - For `action = repeat`: creates a new `school_enrollments` record in the **same** class for the new year (BR-PROM-004).
   - For `action = depart`: creates a `school_departures` record with the specified reason code (BR-DEPART-001).
   - Creates a `promotion_events` audit record (BR-PROM-006).
   - Marks the class as resolved.
3. When all classes are resolved, sets `promotion_wizard_complete = true` on the academic year.

**Timetable (FR-ACA-004):**
- `TimetableRepository@upsertForClass()` — deletes existing entries for the class/year and inserts new entries in a single transaction.
- Validates no time-slot overlaps for the same teacher across classes.

---

### 3.4 Fees Module

**Files:**
- `FeeStructureController`, `PaymentController`, `RefundController`, `FeeReportController`
- `FeeService` — payment recording, duplicate detection, balance calculation
- `RefundService` — initiation/approval workflow
- `FeeReminderService` — SMS dispatch logic
- `FeeStructureRepository`, `PaymentRepository`, `RefundRepository`
- `RecordPaymentRequest`, `InitiateRefundRequest` — validation
- `SendFeeReminderJob` — queued SMS dispatch

**Payment Recording (FR-FEE-002):**
1. `FeeService@recordPayment()`:
   - Checks for duplicate: queries `payments` where `tenant_id`, `student_enrollment_id`, `amount_ugx`, and `created_at > now() - 5 minutes` match. If found → throws `DuplicatePaymentException` (HTTP 409, code `DUPLICATE_PAYMENT`).
   - Creates `payments` record.
   - Generates sequential receipt number: `RCT-{YEAR}-{SEQ:05d}` where SEQ is per-tenant auto-increment.
   - Creates `payment_receipts` record (immutable — BR-FEE-004).
   - Dispatches `PaymentRecordedEvent`.

**Fee Reminder Schedule (BR-FEE-006):**
- `SendFeeReminderJob` is scheduled by `FeeReminderScheduler` (registered in `Console\Kernel`).
- Runs at D-7, D-1, and D+7 relative to each term's `start_date`.
- Queries all students with `outstanding_balance > 0` and a valid `guardian_phone`.
- Sends SMS via Africa's Talking API.
- Schools may disable D-1 and D+7 via tenant settings; D-7 cannot be disabled.

**Refund Workflow (FR-FEE-005, BR-FEE-007):**
1. Bursar calls `RefundService@initiate()` → creates refund with `status = pending_approval`.
2. School Owner calls `RefundService@approve()` → sets `status = approved`, records `approved_by_user_id` and `approved_at`.
3. Authorisation enforced by `RefundPolicy`: only `school_owner` or `director` role may call `approve`.

---

### 3.5 Attendance Module

**Files:**
- `AttendanceController`
- `AttendanceService` — submission, amendment rules, absence alert logic
- `AttendanceRepository`
- `SubmitAttendanceRequest` — validation
- `SendAbsenceAlertJob` — queued SMS for 3 consecutive absences

**Submission (FR-ATT-001):**
1. `AttendanceService@submitForClass()`:
   - Validates all `student_enrollment_id` values belong to the specified class.
   - Upserts `attendance_records` for the class/date.
   - After save, checks each student for 3 consecutive `absent` records (BR-ATT-002).
   - For each student exceeding the threshold, dispatches `SendAbsenceAlertJob`.

**Amendment Rules (FR-ATT-003, BR-ATT-003):**
1. `AttendanceService@amendRecord()`:
   - If `record.date >= now() - 48 hours`: any class teacher for that class may amend.
   - If `record.date < now() - 48 hours`: only `head_teacher` or above may amend.
   - Creates an amendment audit trail: `original_status`, `new_status`, `amended_by_user_id`, `amendment_reason`, `amended_at`.

---

### 3.6 Examinations Module

**Files:**
- `ExamController`, `MarkController`, `GradingController`
- `ExamService` — exam lifecycle, lock/unlock logic
- `MarkService` — mark submission, validation against maximum
- `GradingService` — grade computation per curriculum type
- `UnebExportService` — UNEB file generation
- `ExamRepository`, `MarkRepository`
- `SubmitMarksRequest` — validation (BR-UNEB-005: score ≤ maximum_mark)

**Mark Submission (FR-EXM-002):**
1. `MarkService@submitMarks()`:
   - Checks exam status: if `locked` and no active unlock window → throws `ExamLockedException` (HTTP 409).
   - Validates each score against `exam_subjects.maximum_mark` (BR-UNEB-005). Out-of-range scores → HTTP 422 with per-field error.
   - For Thematic curriculum: validates score is one of `HC`, `C`, `NYC` (BR-UNEB-004).
   - Upserts `exam_marks` records.
   - Dispatches `MarksSubmittedEvent`.

**Grading Engine (FR-EXM-004 – FR-EXM-007):**
- `GradingService` uses a Strategy pattern. The strategy is selected by `class.curriculum_type`:

| Curriculum Type | Strategy Class | Grade Scale |
|---|---|---|
| `thematic` | `ThematicGradingStrategy` | HC / C / NYC (BR-UNEB-004) |
| `primary` | `PrimaryGradingStrategy` | Percentage + class rank |
| `o_level` | `OLevelGradingStrategy` | D1–F9, division I–IV (BR-UNEB-002) |
| `a_level` | `ALevelGradingStrategy` | A–F principal, O subsidiary, points (BR-UNEB-003) |

- PLE grading (P7 classes):
  - Uses `OLevelGradingStrategy` variant for PLE.
  - Aggregate = sum of grades in 4 compulsory subjects.
  - Division mapping: 4–12 = Div I, 13–23 = Div II, 24–29 = Div III, 30–34 = Div IV, 35–36 = Ungraded (BR-UNEB-001).

**Exam Lock/Unlock (FR-EXM-003, BR-CAL-003):**
- Exams auto-lock when `now() > academic_year.exam_submission_deadline`.
- `ExamService@unlockExam()`: Head Teacher grants a time-limited unlock. Sets `exam.unlock_until` to the specified datetime. The exam re-locks automatically when the window expires.
- `LockHistoricalRecordsJob` (triggered 30 days after term end — BR-PROM-005) permanently locks all exams for that year. No unlock is possible after this.

---

### 3.7 Reports Module

**Files:**
- `ReportCardController`, `SchoolPerformanceController`
- `ReportCardService` — single and bulk PDF generation
- `ReportCardPdfGenerator` — mPDF rendering
- `SchoolPerformanceService` — aggregate statistics
- `GenerateBulkReportCardsJob` — queued bulk PDF generation

**Single Report Card (FR-RPT-001):**
1. `ReportCardService@generateForStudent()`:
   - Loads grading results from `GradingService`.
   - Loads attendance summary from `AttendanceRepository`.
   - Loads teacher/head teacher comments from `report_card_comments`.
   - Renders PDF via `ReportCardPdfGenerator` (mPDF).
   - Uploads to S3: `reports/{tenant_id}/{year}/{term}/{student_uid}.pdf`.
   - Returns a pre-signed download URL (60-minute TTL).

**Bulk Generation (FR-RPT-002):**
1. `ReportCardController@bulkGenerate` creates a `report_generation_jobs` record and dispatches `GenerateBulkReportCardsJob`.
2. The job processes students in batches of 10, generating individual PDFs.
3. When all PDFs are complete, creates a ZIP archive and uploads to S3.
4. The frontend polls `GET /report-cards/bulk/{jobId}` for status.

---

### 3.8 RBAC Module

**Files:**
- `UserController`, `PermissionController`
- `UserService` — invitation, role change, deactivation
- `PermissionService` — effective permission resolution
- `UserRepository`
- `InviteUserRequest` — validation
- `SendInvitationEmailJob` — queued email dispatch

**Permission Resolution (FR-RBAC-001):**
- `PermissionService@getEffectivePermissions()`:
  - Loads the user's `role` from `user_roles` for the current `tenant_id`.
  - Joins `role_permissions` to get all permission slugs.
  - Returns a flat array of permission strings (e.g., `students.view`, `fees.record_payment`).
  - Cached in Redis for 5 minutes per user/tenant combination. Cache is invalidated on role change.

**Privilege Escalation Prevention (BR-RBAC-002):**
- `UserService@changeRole()` and `UserService@inviteUser()` both check:
  - `$callerRoleLevel >= $targetRoleLevel` → throws `PrivilegeEscalationException` (HTTP 403).
- Role levels: super_admin=5, school_owner=4, head_teacher=3, class_teacher/bursar/receptionist=2, parent/student=1.

**Session Revocation (FR-RBAC-004):**
- `UserService@revokeSessions()`:
  - Deletes all `personal_access_tokens` for the user at the current tenant.
  - Deletes all `api_refresh_tokens` for the user.
  - Dispatches `UserSessionsRevokedEvent`.

---

### 3.9 EMIS and Audit Module

**Files:**
- `EmisExportController`, `AuditLogController`
- `EmisExportService` — data aggregation and file generation
- `AuditLogService` — query and filtering
- `AuditLogRepository` — append-only queries (no update/delete methods)
- `GenerateEmisExportJob` — queued file generation

**EMIS Export (FR-EMIS-001):**
1. `EmisExportService@generate()`:
   - Aggregates: student count by class and gender, attendance summary, examination results.
   - Renders XLSX using PhpSpreadsheet.
   - Uploads to S3: `emis/{tenant_id}/{year}/EMIS_{tenant_slug}_{year}.xlsx`.
   - Creates `emis_exports` record for history tracking.
   - Returns pre-signed download URL (30-minute TTL).

**Audit Trail (FR-AUD-001):**
- `AuditLogRepository` has no `update()` or `delete()` methods — append-only by design.
- `AuditLog::record()` is a static factory method called from Services and Event Listeners:
  ```php
  AuditLog::record([
      'tenant_id'     => app('tenant_id'),
      'action'        => 'STUDENT_ADMITTED',
      'resource_type' => 'student',
      'resource_id'   => $student->id,
      'user_id'       => app('acting_user_id'),
      'before'        => null,
      'after'         => $student->toArray(),
      'meta'          => ['nin_matched' => true],
      'ip_address'    => request()->ip(),
  ]);
  ```
- The `audit_logs` table has no `ON DELETE CASCADE` foreign keys — records survive even if the referenced resource is soft-deleted.

---

## 4. Error Handling Contract

### 4.1 Exception-to-HTTP Mapping

All custom exceptions extend a base `ApiException` class that carries `$code`, `$httpStatus`, and `$message`.

| Exception Class | HTTP Status | Error Code | Trigger |
|---|---|---|---|
| `ValidationException` (Laravel) | 422 | `VALIDATION_ERROR` | Form Request validation failure |
| `ModelNotFoundException` | 404 | `NOT_FOUND` | Route model binding failure |
| `AuthenticationException` | 401 | `UNAUTHENTICATED` | Missing or invalid token |
| `AccountLockedException` | 403 | `ACCOUNT_LOCKED` | 5 failed login attempts |
| `TokenExpiredException` | 401 | `TOKEN_EXPIRED` | Access token past TTL |
| `TokenRevokedException` | 401 | `TOKEN_REVOKED` | Refresh token replayed |
| `TenantSuspendedException` | 403 | `TENANT_SUSPENDED` | Tenant status = suspended |
| `PrivilegeEscalationException` | 403 | `PRIVILEGE_ESCALATION` | Role assignment above caller |
| `StudentAlreadyEnrolledException` | 409 | `STUDENT_ALREADY_ENROLLED` | Active enrollment at another school |
| `DuplicatePaymentException` | 409 | `DUPLICATE_PAYMENT` | Same payment within 5-minute window |
| `ExamLockedException` | 409 | `EXAM_LOCKED` | Mark entry on locked exam |
| `AmendmentWindowExpiredException` | 409 | `AMENDMENT_WINDOW_EXPIRED` | Attendance amendment past 48 hours by non-HT |
| `PromotionWizardIncompleteException` | 409 | `PROMOTION_WIZARD_INCOMPLETE` | Activating year without completed wizard |
| `MarksNotFinalisedException` | 409 | `MARKS_NOT_FINALISED` | Report/export with incomplete marks |

### 4.2 Exception Handler

`app/Exceptions/Handler.php` renders all `ApiException` subclasses using the standard envelope:

```php
public function render($request, Throwable $e)
{
    if ($e instanceof ApiException) {
        return response()->json([
            'success' => false,
            'error'   => [
                'code'    => $e->getErrorCode(),
                'message' => $e->getMessage(),
                'details' => $e->getDetails(),
            ],
        ], $e->getHttpStatus());
    }
    // ... default Laravel handling for non-API exceptions
}
```

---

## 5. Caching Strategy

| Cache Key Pattern | TTL | Invalidation Trigger |
|---|---|---|
| `permissions:{user_id}:{tenant_id}` | 5 min | Role change, session revocation |
| `fee_structure:{class_id}:{year_id}:{term}` | 1 hour | Fee structure update |
| `class_list:{tenant_id}:{year_id}` | 10 min | Class create/update/delete |
| `academic_year:active:{tenant_id}` | 30 min | Year status change |
| `student_count:{class_id}` | 5 min | Student admission, transfer, departure |

All cache keys are prefixed with `tenant:{tenant_id}:` to prevent cross-tenant cache leakage.

Cache driver: Redis 7. Cache store configuration in `config/cache.php` with `prefix` set to the application name.

---

## 6. Queue Jobs

| Job Class | Queue | Timeout | Retries | Trigger |
|---|---|---|---|---|
| `SendFeeReminderJob` | `notifications` | 120s | 3 | Scheduled (D-7, D-1, D+7) or manual |
| `SendAbsenceAlertJob` | `notifications` | 30s | 3 | 3 consecutive absences detected |
| `SendInvitationEmailJob` | `notifications` | 30s | 3 | User invitation created |
| `GenerateBulkReportCardsJob` | `reports` | 300s | 1 | Bulk report card request |
| `GenerateEmisExportJob` | `reports` | 300s | 1 | EMIS export request |
| `ImportStudentsJob` | `imports` | 300s | 1 | Student data import wizard |
| `LockHistoricalRecordsJob` | `maintenance` | 600s | 1 | Scheduled 30 days after term end |
| `PurgeExpiredDataJob` | `maintenance` | 600s | 1 | Nightly scheduled job |

All jobs extend `TenantAwareJob` (defined in the Security Architecture document) to ensure `tenant_id` is serialised and re-bound on execution.

---

## 7. Event-Listener Map

| Event | Listeners | Purpose |
|---|---|---|
| `StudentAdmittedEvent` | `CreateAuditLogOnStudentAdmitted` | Write audit log |
| `StudentTransferredEvent` | `CreateAuditLogOnStudentTransferred` | Write audit log |
| `PaymentRecordedEvent` | `CreateAuditLogOnPaymentRecorded`, `UpdateStudentFeeBalance` | Audit + balance update |
| `RefundApprovedEvent` | `CreateAuditLogOnRefundApproved`, `UpdateStudentFeeBalance` | Audit + balance update |
| `MarksSubmittedEvent` | `CreateAuditLogOnMarksSubmitted` | Write audit log |
| `ExamUnlockedEvent` | `CreateAuditLogOnExamUnlocked` | Write audit log |
| `UserRoleChangedEvent` | `CreateAuditLogOnRoleChanged`, `InvalidatePermissionCache` | Audit + cache bust |
| `UserSessionsRevokedEvent` | `CreateAuditLogOnSessionsRevoked` | Write audit log |
| `AcademicYearClosedEvent` | `ScheduleHistoricalRecordLock` | Schedule 30-day lock job |
| `PromotionDecisionsRecordedEvent` | `CreatePromotionAuditRecord` | Write promotion_events |

---

## AI Service Module Architecture

This section specifies the internal class design for the AI Module add-on. All AI classes live in the `app/AI/` namespace. No class outside this namespace may call an external LLM API directly.

### AI Service Layer Stack

```
AIController
    → AIGate::check(tenantId, featureSlug)
    → BudgetGuard::check(tenantId)
    → PIIScrubber::scrub(text, tenantId)
    → AIInputSanitiser::sanitise(text)
    → AIMeteredClient::complete(prompt, model, featureSlug)
        → AIProvider::complete(messages, model)   ← external API call
        → AIUsageRepository::record(usage)
        → AIAuditRepository::record(audit)
    → AIOutputValidator::validate(json, schema)
    → AIResponseRepository::store(result)
```

### AIMeteredClient

**File:** `app/AI/AIMeteredClient.php`

The single entry point for all LLM API calls. Enforces gate, budget, PII scrubbing, metering, and audit logging in one pipeline. No other class may call an AI provider directly.

```php
class AIMeteredClient
{
    public function __construct(
        private readonly AIGate $gate,
        private readonly BudgetGuard $budget,
        private readonly PIIScrubber $scrubber,
        private readonly AIInputSanitiser $sanitiser,
        private readonly AIProvider $provider,
        private readonly AIUsageRepository $usage,
        private readonly AIAuditRepository $audit,
    ) {}

    public function complete(
        string $prompt,
        string $model,
        string $featureSlug,
        int $tenantId,
        ?int $userId = null,
    ): AIResponse {
        $this->gate->check($tenantId, $featureSlug);
        $this->budget->check($tenantId);

        $cleanPrompt = $this->scrubber->scrub(
            $this->sanitiser->sanitise($prompt),
            $tenantId
        );

        $startMs = now()->valueOf();
        $response = $this->provider->complete($cleanPrompt, $model);
        $latencyMs = now()->valueOf() - $startMs;

        $this->usage->record(new AIUsageRecord(
            tenantId: $tenantId,
            userId: $userId,
            featureSlug: $featureSlug,
            model: $model,
            inputTokens: $response->inputTokens,
            outputTokens: $response->outputTokens,
            costUsd: $response->costUsd,
            costUgx: $this->convertToUgx($response->costUsd),
            billingPeriod: now()->format('Y-m'),
            latencyMs: $latencyMs,
        ));

        $this->audit->record(new AIAuditRecord(
            tenantId: $tenantId,
            userId: $userId,
            featureSlug: $featureSlug,
            model: $model,
            promptHash: hash('sha256', $cleanPrompt),
            responseHash: hash('sha256', $response->content),
            piiScrubbed: true,
            outcome: 'success',
        ));

        return $response;
    }
}
```

### AIProvider Interface and Implementations

**File:** `app/AI/Contracts/AIProvider.php`

```php
interface AIProvider
{
    public function complete(string $prompt, string $model): AIResponse;
}
```

**Implementations:**
- `app/AI/Providers/AnthropicProvider.php` — primary provider (Claude Haiku / Sonnet via Anthropic API)
- `app/AI/Providers/OpenAIProvider.php` — secondary failover
- `app/AI/Providers/MockAIProvider.php` — for tests; returns deterministic fixture responses

Provider selection is driven by the `AI_PROVIDER` environment variable. The `AIServiceProvider` binds the correct implementation in the service container.

### BudgetGuard

**File:** `app/AI/BudgetGuard.php`

Reads `ai_usage_monthly` (pre-aggregated, cached in Redis with TTL 300 s) and compares against `tenant_ai_modules.monthly_budget_ugx`. Sends alerts when thresholds are crossed.

```php
class BudgetGuard
{
    public function check(int $tenantId): void
    {
        $monthly = Cache::remember("ai_monthly_{$tenantId}_" . now()->format('Y-m'), 300,
            fn() => DB::table('ai_usage_monthly')
                ->where('tenant_id', $tenantId)
                ->where('billing_period', now()->format('Y-m'))
                ->first()
        );

        $module = Cache::remember("ai_module_{$tenantId}", 300,
            fn() => DB::table('tenant_ai_modules')
                ->where('tenant_id', $tenantId)
                ->first()
        );

        if (!$module) return; // Gate handles missing module

        $used = $monthly?->total_cost_ugx ?? 0;
        $budget = $module->monthly_budget_ugx;
        $pct = $budget > 0 ? ($used / $budget) * 100 : 0;

        if ($pct >= 100) {
            $this->alert($tenantId, 100, $used, $budget);
            throw new AIBudgetExceededException("Monthly AI budget exhausted for tenant {$tenantId}.");
        }

        if ($pct >= $module->alert_threshold_pct) {
            $this->alert($tenantId, $module->alert_threshold_pct, $used, $budget);
        }
    }
}
```

### Batch Job Architecture

AI batch jobs (at-risk scoring, fee prediction, weekly briefing) run on scheduled queues. Each job extends `TenantAwareJob` (Section 7.1) and dispatches one API call per student batch.

**Example — AtRiskScoringJob:**

```php
class AtRiskScoringJob extends TenantAwareJob
{
    public function __construct(
        private readonly array $studentUids, // batch of 50
        private readonly string $period,
    ) {
        parent::__construct();
    }

    public function handle(AIMeteredClient $ai, NlpResultRepository $results): void
    {
        $studentData = $this->buildStudentBatch($this->studentUids);
        $prompt = AtRiskPromptBuilder::build($studentData);

        $response = $ai->complete(
            prompt: $prompt,
            model: 'claude-haiku-4-5',
            featureSlug: 'at_risk_students',
            tenantId: $this->tenantId,
        );

        $parsed = AIOutputValidator::validate($response->content, AtRiskSchema::class);

        foreach ($parsed as $item) {
            $results->upsert(new NlpResult(
                tenantId: $this->tenantId,
                sourceType: 'student_risk',
                sourceId: $item['student_uid'],
                nlpTask: 'risk_scoring',
                resultJson: $item,
                period: $this->period,
            ));
        }
    }
}
```

The Monday scheduler dispatches one `AtRiskScoringJob` per class-batch per tenant via Laravel Horizon. Horizon monitors queue depth and worker count to ensure all tenants are processed within the 06:00–07:00 EAT window (AI-NFR-004).
