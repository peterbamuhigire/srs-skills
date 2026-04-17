# Security Architecture — Academia Pro

**Document ID:** DD-01-02
**Project:** Academia Pro
**Author:** Chwezi Core Systems
**Date:** 2026-04-03
**Version:** 1.0
**Status:** Draft — Pending Consultant Review
**Gap Resolved:** HIGH-001

---

## 1. Purpose

This document specifies the multi-tenancy security architecture for Academia Pro. It defines, at implementation level, how `tenant_id` isolation is enforced at every application layer so that no tenant can access another tenant's data under any circumstances (BR-MT-001).

A developer must be able to implement all components described herein without additional clarification.

---

## 2. Scope

This document covers:

1. JWT authentication middleware — token validation and `tenant_id` binding
2. Repository base class — mandatory `tenant_id` scoping on every query
3. Eloquent global scope — secondary model-level defence
4. Raw query audit — CI/CD rule preventing unscoped raw queries
5. Queue job isolation — `tenant_id` serialisation and re-binding
6. Event listener isolation — same pattern as queue jobs
7. API response sanitisation — stripping internal fields from outbound JSON
8. Super Admin bypass — audited cross-tenant read access for Chwezi support staff

---

## 3. Authentication Layer (Laravel Sanctum + JWT Claims)

### 3.1 Token Structure

Academia Pro uses Laravel Sanctum's API token system. Each token is issued with an associated
`tenant_id` stored in the `personal_access_tokens.abilities` JSON column (repurposed as claims).

**Token payload claims (stored in `abilities` JSON):**

```json
{
  "tenant_id": 42,
  "user_id": 1007,
  "role": "bursar",
  "iat": 1712150400,
  "exp": 1712236800
}
```

`tenant_id` is always an integer. Null or absent `tenant_id` is only valid for Super Admin tokens
(Chwezi staff), which carry `"tenant_id": null` and a `"role": "super_admin"` claim.

### 3.2 `AuthenticateTenant` Middleware

**File:** `app/Http/Middleware/AuthenticateTenant.php`

**Responsibility:** Validate the token, extract `tenant_id`, and bind it to the request context.
Every authenticated API route must pass through this middleware.

**Logic:**

```
1. Extract Bearer token from Authorization header.
2. Look up token hash in personal_access_tokens.
3. If not found or expired → 401 Unauthorized.
4. Decode the abilities JSON column.
5. If abilities.tenant_id is null AND abilities.role != 'super_admin' → 403 Forbidden.
6. Bind to request context:
   request->attributes->set('tenant_id', abilities.tenant_id)
   request->attributes->set('acting_user_id', abilities.user_id)
   request->attributes->set('acting_role', abilities.role)
7. Bind to service container:
   app()->instance('tenant_id', abilities.tenant_id)
8. Pass to next middleware.
```

**Route registration** (`routes/api.php`):

```php
Route::middleware(['auth:sanctum', AuthenticateTenant::class])->group(function () {
    // All authenticated API routes live here
});
```

---

## 4. Repository Layer — Mandatory Tenant Scoping

### 4.1 `TenantAwareRepository` Base Class

**File:** `app/Repositories/TenantAwareRepository.php`

Every repository for a tenant-scoped entity extends `TenantAwareRepository`. The base class
resolves `tenant_id` from the service container on instantiation and appends it to every
query builder chain.

**Base class contract:**

```php
abstract class TenantAwareRepository
{
    protected int $tenantId;

    public function __construct()
    {
        $tenantId = app('tenant_id');

        if ($tenantId === null) {
            throw new \LogicException(
                'TenantAwareRepository instantiated without a bound tenant_id. ' .
                'Ensure AuthenticateTenant middleware ran before this repository is resolved.'
            );
        }

        $this->tenantId = (int) $tenantId;
    }

    /**
     * Apply tenant scope to any query builder instance.
     * Call this at the start of every query method.
     */
    protected function scopedQuery(string $table): \Illuminate\Database\Query\Builder
    {
        return DB::table($table)->where('tenant_id', $this->tenantId);
    }

    /**
     * Apply tenant scope to an Eloquent builder.
     */
    protected function scopedModel(\Illuminate\Database\Eloquent\Builder $query):
        \Illuminate\Database\Eloquent\Builder
    {
        return $query->where('tenant_id', $this->tenantId);
    }
}
```

**Usage in a concrete repository:**

```php
class StudentRepository extends TenantAwareRepository
{
    public function findById(int $id): ?array
    {
        return $this->scopedQuery('students')
            ->where('id', $id)
            ->first();
    }

    public function create(array $data): int
    {
        $data['tenant_id'] = $this->tenantId; // Always inject on write
        return DB::table('students')->insertGetId($data);
    }
}
```

### 4.2 Enforcement Rule

No repository method may call `DB::table()`, `DB::select()`, `Model::query()`, or similar
without first applying `$this->tenantId` scoping. This is enforced by the CI audit rule
described in Section 6.

### 4.3 Global Entities (No `tenant_id`)

Tables without `tenant_id` (`global_students`, `student_identifiers`) are accessed only through
dedicated read-only service methods, not through `TenantAwareRepository`. Write access is gated
at the service layer per BR-MT-002.

```php
class GlobalStudentService
{
    // Any authenticated school may read global identity fields
    public function findByNin(string $nin): ?GlobalStudent { ... }

    // Only the owning school (checked against global_students.created_by_tenant_id)
    // may update global identity fields
    public function updateIdentity(int $globalStudentId, array $data): void
    {
        $student = GlobalStudent::findOrFail($globalStudentId);

        if ($student->created_by_tenant_id !== app('tenant_id')) {
            throw new \App\Exceptions\UnauthorisedIdentityWriteException();
        }

        $student->update($data);
    }
}
```

---

## 5. Eloquent Global Scope — Secondary Defence Layer

### 5.1 `TenantScope`

**File:** `app/Models/Scopes/TenantScope.php`

All Eloquent models for tenant-scoped tables apply this global scope automatically.
It provides a secondary isolation layer on top of the repository pattern.

```php
class TenantScope implements \Illuminate\Database\Eloquent\Scope
{
    public function apply(Builder $builder, Model $model): void
    {
        $tenantId = app('tenant_id');

        if ($tenantId !== null) {
            $builder->where($model->getTable() . '.tenant_id', $tenantId);
        }
        // Super Admin has tenant_id = null — scope is intentionally skipped.
        // All Super Admin access is audited via AuditSuperAdminAccess middleware.
    }
}
```

### 5.2 `TenantModel` Base Model

**File:** `app/Models/TenantModel.php`

```php
abstract class TenantModel extends Model
{
    protected static function booted(): void
    {
        static::addGlobalScope(new TenantScope());
    }

    protected static function creating(array $attributes): array
    {
        $attributes['tenant_id'] = app('tenant_id');
        return $attributes;
    }
}
```

All tenant-scoped Eloquent models extend `TenantModel` instead of `Model`.

---

## 6. Raw Query Audit — CI/CD Enforcement

### 6.1 Rule

No `DB::statement()` or `DB::select()` call may appear in any PHP file under `app/` without
a `tenant_id` parameter binding. Violation blocks the pull request merge.

### 6.2 PHPStan Custom Rule

**File:** `tests/Architecture/TenantIsolationRule.php`

A PHPStan level 8 custom rule scans for unscoped raw query patterns and fails the build:

```php
class RawQueryTenantCheck implements \PHPStan\Rules\Rule
{
    public function getNodeType(): string
    {
        return \PhpParser\Node\Expr\StaticCall::class;
    }

    public function processNode(Node $node, Scope $scope): array
    {
        if ($this->isUnscoped($node)) {
            return [
                RuleErrorBuilder::message(
                    'Raw DB query detected without tenant_id binding. ' .
                    'Use TenantAwareRepository::scopedQuery() instead, ' .
                    'or bind $tenantId as a named parameter.'
                )->build()
            ];
        }

        return [];
    }
}
```

### 6.3 GitHub Actions Step

**File:** `.github/workflows/ci.yml` (partial):

```yaml
- name: PHPStan — Tenant Isolation Audit
  run: vendor/bin/phpstan analyse app/ --level=8 --configuration=phpstan.neon
```

`phpstan.neon` includes the `TenantIsolationRule` under the `rules:` key.

---

## 7. Queue Job Isolation

### 7.1 `TenantAwareJob` Base Class

**File:** `app/Jobs/TenantAwareJob.php`

Every queued job that performs tenant-scoped work must extend `TenantAwareJob`.
The base class serialises `tenant_id` into the job payload and re-binds it in the
service container before `handle()` is called.

```php
abstract class TenantAwareJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    protected int $tenantId;

    public function __construct()
    {
        // Capture current tenant context at dispatch time
        $this->tenantId = (int) app('tenant_id');

        if ($this->tenantId === 0) {
            throw new \LogicException('Job dispatched without a bound tenant_id.');
        }
    }

    /**
     * Re-bind tenant context before the worker executes handle().
     * Called automatically by Laravel's job pipeline.
     */
    public function middleware(): array
    {
        return [new RebindTenantContextMiddleware($this->tenantId)];
    }
}
```

**File:** `app/Jobs/Middleware/RebindTenantContextMiddleware.php`

```php
class RebindTenantContextMiddleware
{
    public function __construct(private readonly int $tenantId) {}

    public function handle(mixed $job, callable $next): void
    {
        app()->instance('tenant_id', $this->tenantId);
        $next($job);
    }
}
```

### 7.2 Example — Fee Reminder Job

```php
class SendFeeReminderJob extends TenantAwareJob
{
    public function __construct(
        private readonly int $studentId,
        private readonly string $reminderType,
    ) {
        parent::__construct(); // captures tenant_id
    }

    public function handle(FeeReminderService $service): void
    {
        // tenant_id is already bound in container by middleware
        $service->sendReminder($this->studentId, $this->reminderType);
    }
}
```

---

## 8. Event Listener Isolation

### 8.1 Rule

Any event listener that triggers database reads or writes must resolve `tenant_id` from the
event payload (not from the service container), because listeners may be queued and executed
in a different request context.

### 8.2 `TenantAwareEvent` Base Class

**File:** `app/Events/TenantAwareEvent.php`

```php
abstract class TenantAwareEvent
{
    public readonly int $tenantId;

    public function __construct()
    {
        $this->tenantId = (int) app('tenant_id');
    }
}
```

**Example event:**

```php
class StudentEnrolledEvent extends TenantAwareEvent
{
    public function __construct(
        public readonly int $studentId,
        public readonly string $className,
    ) {
        parent::__construct(); // stores tenant_id on the event
    }
}
```

**Example listener:**

```php
class SendEnrolmentConfirmationListener
{
    public function handle(StudentEnrolledEvent $event): void
    {
        app()->instance('tenant_id', $event->tenantId); // re-bind before any DB access
        // ... proceed with tenant-scoped database work
    }
}
```

---

## 9. API Response Sanitisation

### 9.1 `StripInternalFieldsMiddleware`

**File:** `app/Http/Middleware/StripInternalFieldsMiddleware.php`

**Responsibility:** Remove implementation-internal keys from all outbound JSON responses.
These keys are never exposed to API consumers.

**Fields stripped from all response bodies (recursive, any nesting depth):**

- `tenant_id`
- `created_by_tenant_id`
- `franchise_id` (legacy alias used in some base patterns)
- `deleted_at` (unless the requesting role is Super Admin)

```php
class StripInternalFieldsMiddleware
{
    private const STRIP_KEYS = ['tenant_id', 'created_by_tenant_id', 'franchise_id'];

    public function handle(Request $request, Closure $next): Response
    {
        $response = $next($request);

        if ($response instanceof JsonResponse) {
            $data = $response->getData(true);
            $cleaned = $this->stripKeys($data);
            $response->setData($cleaned);
        }

        return $response;
    }

    private function stripKeys(array $data): array
    {
        foreach ($data as $key => &$value) {
            if (in_array($key, self::STRIP_KEYS, true)) {
                unset($data[$key]);
            } elseif (is_array($value)) {
                $value = $this->stripKeys($value);
            }
        }
        return $data;
    }
}
```

Register in `app/Http/Kernel.php` under the `api` middleware group, after `AuthenticateTenant`.

---

## 10. Super Admin Cross-Tenant Bypass

### 10.1 `withoutTenantScope()` Method

Super Admin users (Chwezi support staff) may read any tenant's data for support purposes.
This bypass is:

- Available only to users with `role = 'super_admin'` in their token claims.
- Restricted to read operations only (no writes across tenant boundaries).
- Logged unconditionally per BR-MT-003.

**File:** `app/Repositories/TenantAwareRepository.php` (addition):

```php
/**
 * Return a query builder for the given table WITHOUT tenant scope.
 * For Super Admin use only. Throws if called by a non-Super Admin.
 * All calls are logged to audit_logs.
 */
protected function withoutTenantScope(string $table, string $reason): \Illuminate\Database\Query\Builder
{
    if (app('acting_role') !== 'super_admin') {
        throw new \App\Exceptions\UnauthorisedCrossTenantAccessException(
            'withoutTenantScope() may only be called by super_admin role.'
        );
    }

    AuditLog::record([
        'event'          => 'super_admin_cross_tenant_read',
        'actor_user_id'  => app('acting_user_id'),
        'target_table'   => $table,
        'reason'         => $reason,
        'occurred_at'    => now(),
    ]);

    return DB::table($table);
}
```

### 10.2 Super Admin Read-Only Enforcement

Super Admin API routes are registered under a separate middleware group that:

1. Validates the `super_admin` role claim.
2. Injects `tenant_id = null` into the container (bypasses `TenantScope` in Eloquent).
3. Applies `AuditSuperAdminAccess` middleware that logs every request with `actor_id`,
   `target_tenant_id` (from query parameter or route param), `endpoint`, and `timestamp`.
4. Rejects any `POST`, `PUT`, `PATCH`, or `DELETE` method to tenant-scoped endpoints
   — Super Admins read only.

**Route group:**

```php
Route::middleware(['auth:sanctum', AuthenticateTenant::class, 'role:super_admin',
    AuditSuperAdminAccess::class, EnforceReadOnly::class])
    ->prefix('admin')
    ->group(function () {
        Route::get('/tenants/{tenantId}/students', [SuperAdminStudentController::class, 'index']);
        // ... other Super Admin read endpoints
    });
```

---

## 11. Security Architecture Checklist

Use this checklist at code review for every Pull Request touching authentication or data access.

- [ ] All new API routes use the `AuthenticateTenant` middleware group.
- [ ] All new repositories extend `TenantAwareRepository`.
- [ ] All new Eloquent models for tenant-scoped tables extend `TenantModel`.
- [ ] All new jobs that touch DB extend `TenantAwareJob`.
- [ ] All new events that carry data extend `TenantAwareEvent`.
- [ ] No `DB::statement()` or `DB::select()` without `tenant_id` parameter.
- [ ] `withoutTenantScope()` is not called outside Super Admin controllers.
- [ ] PHPStan level 8 passes with zero errors before merge.
- [ ] Response does not include `tenant_id` field (verified with integration test).

---

## 12. Threat Model Summary

| Threat | Mitigation |
|--------|-----------|
| Tenant A reads Tenant B's student records | `tenant_id` scoping at Repository + Eloquent scope layers |
| Token replay after session expiry | Sanctum token expiry enforced; idle timeout FR-AUTH-005 |
| Horizontal privilege escalation (role bypass) | RBAC gate on every route; `AuthenticateTenant` resolves role from token, not request body |
| Super Admin data exfiltration | Read-only enforcement + immutable audit log for every cross-tenant access |
| Raw SQL injection bypassing tenant scope | PHPStan CI rule blocks unscoped raw queries before merge |
| Tenant ID tampering in request body | `tenant_id` sourced exclusively from validated token — never from request body or query string |
| Queue job cross-tenant leakage | `TenantAwareJob` serialises and re-binds `tenant_id` on every job execution |

---

## 13. Cross-References

- **BR-MT-001** — Repository-level `tenant_id` enforcement rule
- **BR-MT-002** — Global identity table access rule
- **BR-MT-003** — Super Admin cross-tenant read logging rule
- **FR-AUTH-001 – FR-AUTH-006** — Authentication functional requirements (SRS Section 4)
- **FR-RBAC-001 – FR-RBAC-005** — RBAC functional requirements (SRS Section 4)
- **NFR-SEC** — Security non-functional requirements (SRS Section 6)
- `skills/multi-tenant-saas-architecture` — Multi-tenancy architectural patterns
- `skills/dual-auth-rbac` — Dual authentication and RBAC implementation patterns
- `skills/php-security` — PHP security baseline


---

## 14. AI Security Architecture

This section extends the security architecture to cover the AI Module add-on. All controls described below apply only when a tenant has an active `tenant_ai_modules` record. The AI Service is the sole component permitted to call external LLM APIs; no other service or controller may make direct external AI API calls.

---

### 14.1 AI Gate Enforcement

**File:** `app/AI/AIGate.php`

Before any AI API call, the gate checks two conditions in sequence:

1. `tenant_ai_modules.status = 'active'` for the requesting tenant.
2. `tenant_ai_features.is_enabled = 1` for the requested `feature_slug`.

If either check fails, the gate throws `AIModuleInactiveException`, which is caught by the controller and returns HTTP 402 `AI_MODULE_INACTIVE`. The gate never throws an uncaught exception — failure is always a clean HTTP response.

```php
class AIGate
{
    public static function check(int $tenantId, string $featureSlug): void
    {
        $module = Cache::remember("ai_module_{$tenantId}", 300, fn() =>
            DB::table('tenant_ai_modules')
              ->where('tenant_id', $tenantId)
              ->where('status', 'active')
              ->first()
        );

        if (!$module) {
            throw new AIModuleInactiveException('AI module not active for this tenant.');
        }

        $feature = Cache::remember("ai_feature_{$tenantId}_{$featureSlug}", 300, fn() =>
            DB::table('tenant_ai_features')
              ->where('tenant_id', $tenantId)
              ->where('feature_slug', $featureSlug)
              ->where('is_enabled', 1)
              ->first()
        );

        if (!$feature) {
            throw new AIModuleInactiveException("AI feature '{$featureSlug}' is not enabled.");
        }
    }
}
```

Gate results are cached in Redis with TTL = 300 seconds (5 minutes). Cache is invalidated immediately when `tenant_ai_modules.status` or `tenant_ai_features.is_enabled` changes.

---

### 14.2 PII Scrubbing Pipeline

**File:** `app/AI/PIIScrubber.php`

Every prompt string passes through `PIIScrubber::scrub()` before dispatch to the external AI API. The scrubber removes Uganda-specific PII patterns and names matched against the tenant's guardian and user records.

```php
class PIIScrubber
{
    private const PATTERNS = [
        '/\bCM\d{9}[A-Z]\d{2}\b/'       => '[NIN-REDACTED]',     // Uganda NIN
        '/\b(?:\+256|0)[7][0-9]{8}\b/'   => '[PHONE-REDACTED]',  // Uganda mobile
        '/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/' => '[EMAIL-REDACTED]',
    ];

    public function scrub(string $text, int $tenantId): string
    {
        // Pattern-based scrub
        $text = preg_replace(
            array_keys(self::PATTERNS),
            array_values(self::PATTERNS),
            $text
        );

        // Name-based scrub: replace names from guardian and user tables
        $names = $this->getTenantNames($tenantId);
        foreach ($names as $name) {
            if (strlen($name) > 2) {
                $text = str_ireplace($name, '[NAME-REDACTED]', $text);
            }
        }

        return $text;
    }

    private function getTenantNames(int $tenantId): array
    {
        return Cache::remember("pii_names_{$tenantId}", 3600, fn() =>
            DB::table('guardians')
              ->where('tenant_id', $tenantId)
              ->pluck('full_name')
              ->merge(
                  DB::table('users')
                    ->where('tenant_id', $tenantId)
                    ->pluck('full_name')
              )
              ->unique()
              ->toArray()
        );
    }
}
```

**Enforcement rule:** Any AI feature that processes text containing guardian, student, or staff names must call `PIIScrubber::scrub()` before constructing the prompt. Bypassing the scrubber is a `[DPPA-FAIL: no consent mechanism]` violation.

---

### 14.3 Prompt Injection Defence

**File:** `app/AI/AIInputSanitiser.php`

User-supplied text (parent feedback, student submissions, support messages) may contain adversarial content designed to override the system prompt. The sanitiser detects and neutralises common injection patterns before the text is included in a prompt.

Injection patterns blocked:

| Pattern | Example | Action |
|---|---|---|
| Ignore instruction override | "Ignore all previous instructions" | Strip phrase |
| Role injection | "You are now a different AI" | Strip phrase |
| System prompt override | "New system prompt:" | Strip phrase |
| Delimiter injection | `---`, `###`, `<|im_end|>` | Escape to literal text |
| Jailbreak markers | "DAN mode", "developer mode" | Strip phrase |
| Excessive repetition | Same phrase repeated 20+ times | Truncate to 1 instance |

All injected content is logged to `ai_audit_log` with `outcome = 'injection_detected'` before stripping. The cleaned text proceeds to the AI; the original is never discarded (stored as hash only).

---

### 14.4 AI Audit Log (Immutable)

Every AI API call creates one row in `ai_audit_log`. This is append-only — no application route exposes UPDATE or DELETE on this table. A MySQL trigger enforces immutability at the database layer (identical to the `audit_logs` trigger — FR-AUD-001).

The prompt and response are stored as SHA-256 hashes only (`prompt_hash`, `response_hash`). Plaintext content is never persisted, satisfying DPPA 2019 requirements for data minimisation while preserving an auditable fingerprint.

The `pii_scrubbed` flag is set to 1 when `PIIScrubber::scrub()` ran before the call, and to 0 when it was bypassed. Any row with `pii_scrubbed = 0` triggers an automated alert to the system administrator.

---

### 14.5 Rate Limiting — AI Endpoints

AI endpoints are subject to two layers of rate limiting:

| Scope | Limit | Window | Response on Breach |
|---|---|---|---|
| Per user | 20 AI requests | 60 minutes | HTTP 429 `AI_RATE_LIMIT_USER` |
| Per tenant | 500 AI requests | 60 minutes | HTTP 429 `AI_RATE_LIMIT_TENANT` |

Rate limits are tracked in Redis using `INCR` with TTL-based expiry. Batch jobs (weekly at-risk scoring, fee prediction) are excluded from per-user rate limits but included in per-tenant limits with a burst allowance of 5× the standard limit during the 05:00–07:00 EAT batch window.

---

### 14.6 AI Security Checklist Extension

Add to the Section 11 checklist for all Pull Requests touching AI features:

- [ ] `AIGate::check()` is called before any AI API dispatch.
- [ ] `PIIScrubber::scrub()` is called on every user-supplied text string before it enters a prompt.
- [ ] `AIInputSanitiser::sanitise()` is called on all free-text input included in prompts.
- [ ] Every AI call writes to `ai_usage_log` and `ai_audit_log` before returning.
- [ ] `pii_scrubbed = 1` is set in `ai_audit_log` for every call where the scrubber ran.
- [ ] No student NIN, parent phone number, or email address appears in any prompt string (verified by `PIIScrubber` unit test for this feature's prompt builder).
- [ ] `BudgetGuard::check()` is called before `AIGate::check()` so budget exhaustion is detected before a gate cache miss triggers a DB read.

---

### 14.7 Threat Model Additions (AI-Specific)

| Threat | Mitigation |
|---|---|
| Prompt injection via parent feedback | `AIInputSanitiser` strips known patterns; injections are logged; cleaned text proceeds |
| PII leakage to external LLM provider | `PIIScrubber` enforced before every external call; DPPA-FAIL tag if bypassed |
| Cost exhaustion by a malicious tenant | `BudgetGuard` enforces monthly ceiling; 80% alert + 100% hard block |
| AI response poisoning (malformed JSON crashing the application) | `AIOutputValidator` validates JSON schema before any DB write; malformed responses logged as `outcome = error` |
| Token theft (LLM API key exposure) | API keys stored exclusively in environment variables; never in code, never in logs; rotated quarterly |
| Hallucinated student data written as fact | Human-in-the-loop Hard Gate on all report card comments; at-risk lists are informational only — no automated action is taken without a teacher decision |
