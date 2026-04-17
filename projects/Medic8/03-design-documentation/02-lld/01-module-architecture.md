# Low-Level Design — Medic8 Phase 1

**Document ID:** DD-02-01
**Project:** Medic8
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Pending Consultant Review

---

## 1. Purpose

This document specifies the internal architecture of every Phase 1 module: service class contracts, repository interfaces, controller routing, validation rules, error handling, queue jobs, caching, and event-driven flows. It is the implementation-level companion to the High-Level Design (DD-01) and serves as the primary reference from which developers write production code.

---

## 2. Architectural Conventions

### 2.1 Layer Responsibility

Every feature follows a strict 4-layer architecture. No layer may skip a layer below it.

```
Controller → Service → Repository → Database
```

| Layer | Responsibility | May Call |
|---|---|---|
| Controller | HTTP request/response handling, input validation via Form Requests, response formatting | Service |
| Service | Business logic, orchestration, authorisation checks, event dispatching | Repository, other Services |
| Repository | Data access, tenant scoping, query construction (Eloquent/Query Builder) | Database |
| Model | Column casting, relationships, attribute accessors, scopes | — |

### 2.2 Naming Conventions

| Artifact | Pattern | Example |
|---|---|---|
| Controller | `{Entity}Controller` | `PatientController` |
| Service | `{Entity}Service` | `PatientService` |
| Repository | `{Entity}Repository` (concrete), `{Entity}RepositoryInterface` (contract) | `PatientRepository` |
| Form Request | `{Action}{Entity}Request` | `RegisterPatientRequest` |
| Job | `{Action}{Entity}Job` | `SendAppointmentReminderJob` |
| Event | `{Entity}{PastTenseAction}` | `PatientRegistered` |
| Listener | `{Action}On{Event}` | `PostBillingChargeOnDrugDispensed` |
| Policy | `{Entity}Policy` | `PatientPolicy` |

### 2.3 Directory Structure

```
app/
├── Http/
│   ├── Controllers/
│   │   ├── Api/V1/                    # Tenant-scoped API controllers
│   │   └── AdminPanel/Api/V1/         # Super Admin controllers
│   ├── Middleware/
│   │   ├── TenantMiddleware.php
│   │   ├── MfaVerifiedMiddleware.php
│   │   └── IdleTimeoutMiddleware.php
│   └── Requests/                      # Form Request validation classes
├── Services/
│   ├── Clinical/                      # CDS, Terminology, EMPI
│   ├── Billing/
│   ├── Pharmacy/
│   ├── Lab/
│   └── Infrastructure/               # FormState, Resume, SyncQueue
├── Repositories/
│   ├── Contracts/                     # Interfaces
│   └── Eloquent/                      # Concrete implementations
├── Models/
│   ├── Scopes/
│   │   └── FacilityScope.php
│   └── Traits/
│       └── BelongsToFacility.php
├── Events/
├── Listeners/
├── Jobs/
├── Policies/
└── Exceptions/
```

---

## 3. Shared Infrastructure

### 3.1 Tenant Middleware and Isolation

**Class:** `App\Http\Middleware\TenantMiddleware`

**Responsibility:** Extracts the `facility_id` from the authenticated session (`$_SESSION['medic8_facility_id']`) or JWT claim (`fid`) and binds it to the request context. Every downstream service and repository receives the tenant context without explicit parameter passing.

```php
final class TenantMiddleware
{
    public function handle(Request $request, Closure $next): Response
    {
        $facilityId = $this->resolveFacilityId($request);
        if ($facilityId === null) {
            throw new TenantNotResolvedException();
        }

        app()->instance('facility_id', $facilityId);
        $request->attributes->set('facility_id', $facilityId);

        return $next($request);
    }

    private function resolveFacilityId(Request $request): ?int
    {
        // Web session
        if ($request->hasSession() && $request->session()->has('medic8_facility_id')) {
            return (int) $request->session()->get('medic8_facility_id');
        }
        // JWT
        if ($request->user()?->currentAccessToken()) {
            return (int) $request->user()->currentAccessToken()->getAttribute('facility_id');
        }
        return null;
    }
}
```

**Base Tenant Repository:** All tenant-scoped repositories extend `BaseTenantRepository`, which prepends `WHERE facility_id = ?` to every query. Raw SQL queries that omit the tenant scope are rejected by a CI audit rule during build (BR-DATA-004).

```php
abstract class BaseTenantRepository
{
    protected int $facilityId;

    public function __construct()
    {
        $this->facilityId = app('facility_id');
    }

    protected function baseQuery(): Builder
    {
        return $this->model()
            ->newQuery()
            ->where('facility_id', $this->facilityId);
    }

    abstract protected function model(): Model;
}
```

**Eloquent Global Scope:** `FacilityScope` is applied to all models using the `BelongsToFacility` trait. This provides secondary defence against tenant data leakage (BR-DATA-004).

```php
final class FacilityScope implements Scope
{
    public function apply(Builder $builder, Model $model): void
    {
        $builder->where(
            $model->getTable() . '.facility_id',
            app('facility_id')
        );
    }
}
```

### 3.2 Event System

**Event Catalogue — Phase 1:**

| Event Class | Payload | Dispatched By |
|---|---|---|
| `PatientRegistered` | `patient_uid`, `facility_id`, `mrn` | `PatientService@register()` |
| `PatientMerged` | `source_uid`, `target_uid`, `merged_by` | `PatientService@merge()` |
| `PatientTriaged` | `patient_uid`, `visit_id`, `triage_level`, `news2_score` | `TriageService@recordVitals()` |
| `EncounterCreated` | `encounter_id`, `patient_uid`, `clinician_id` | `EncounterService@createVisit()` |
| `VitalsRecorded` | `patient_uid`, `visit_id`, `news2_score` | `TriageService@recordVitals()` |
| `DiagnosisRecorded` | `encounter_id`, `icd_code`, `patient_uid` | `EncounterService@addDiagnosis()` |
| `PrescriptionWritten` | `prescription_id`, `patient_uid`, `drug_ids[]` | `PrescriptionService@create()` |
| `InvestigationRequested` | `request_id`, `patient_uid`, `test_ids[]`, `urgency` | `InvestigationService@requestLab()` |
| `LabResultEntered` | `request_id`, `patient_uid`, `is_critical` | `LabService@enterResult()` |
| `LabCriticalValue` | `request_id`, `patient_uid`, `parameter`, `value`, `requesting_clinician_id` | `LabService@enterResult()` |
| `LabResultValidated` | `request_id`, `validated_by` | `LabService@validateResult()` |
| `DrugDispensed` | `prescription_id`, `patient_uid`, `drug_id`, `quantity`, `batch_id` | `PharmacyService@dispense()` |
| `StockLow` | `drug_id`, `facility_id`, `current_qty`, `min_level` | `StockService@deductStock()` |
| `StockExpiring` | `drug_id`, `batch_id`, `expiry_date` | `CheckExpiryJob` |
| `ChargeAdded` | `patient_uid`, `amount`, `source_module`, `source_id` | `BillingService@addCharge()` |
| `PaymentReceived` | `patient_uid`, `amount`, `payment_method`, `receipt_number` | `BillingService@collectPayment()` |
| `AppointmentBooked` | `appointment_id`, `patient_uid`, `doctor_id`, `datetime` | `AppointmentService@book()` |
| `AppointmentCancelled` | `appointment_id`, `reason` | `AppointmentService@cancel()` |
| `EmergencyAccessInvoked` | `clinician_id`, `patient_uid`, `facility_id`, `reason` | `EmergencyAccessService@requestBreakTheGlass()` |
| `AuditEntryCreated` | `user_id`, `action`, `resource_type`, `resource_id` | `AuditService@log()` |

**Listener Bindings:**

| Listener | Subscribes To | Action |
|---|---|---|
| `PostBillingChargeOnDrugDispensed` | `DrugDispensed` | Posts pharmacy charge to patient account (BR-FIN-001) |
| `PostBillingChargeOnLabResultEntered` | `LabResultEntered` | Posts lab charge to patient account (BR-FIN-001) |
| `IncrementHMISCounterOnDiagnosisRecorded` | `DiagnosisRecorded` | Increments HMIS 105 tally by age group and sex (BR-HMIS-001) |
| `EscalateCriticalValueOnLabCriticalValue` | `LabCriticalValue` | Dispatches `EscalateCriticalValueJob` with 30/60-minute delays (BR-CLIN-003) |
| `SendSMSOnEmergencyAccessInvoked` | `EmergencyAccessInvoked` | Sends patient SMS notification (BR-DATA-002) |
| `WriteAuditLogOnAnyEvent` | All events | Writes immutable audit trail entry (FR-RBAC-005) |
| `CheckDuplicateOnPatientRegistered` | `PatientRegistered` | Triggers batch EMPI scan for background duplicate detection |

**Queue Configuration:** Redis + Laravel Horizon. Every queued job serialises `facility_id` in its payload so tenant context is restored when the job executes on a worker.

```php
abstract class TenantAwareJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    protected int $facilityId;

    public function __construct()
    {
        $this->facilityId = app('facility_id');
    }

    public function handle(): void
    {
        app()->instance('facility_id', $this->facilityId);
        $this->execute();
    }

    abstract protected function execute(): void;
}
```

### 3.3 Clinical Decision Support Engine

**Class:** `App\Services\Clinical\ClinicalDecisionSupportService`

**Responsibility:** Evaluates clinical rules against patient context before prescription acceptance (BR-CLIN-004).

```php
final class ClinicalDecisionSupportService
{
    public function __construct(
        private readonly CdsRuleRepository $ruleRepo,
        private readonly CdsOverrideRepository $overrideRepo,
    ) {}

    /**
     * Check a drug against the patient's active medications and allergy profile.
     *
     * @param int $drugId         Drug being prescribed
     * @param int $patientUid     Target patient UUID
     * @param int[] $activeDrugIds Currently active medication drug IDs
     * @return CdsAlertCollection Zero or more alerts, each with tier 1-4
     */
    public function checkInteractions(
        int $drugId,
        string $patientUid,
        array $activeDrugIds
    ): CdsAlertCollection {
        $rules = $this->ruleRepo->getMatchingRules($drugId, $activeDrugIds);
        $allergyRules = $this->ruleRepo->getAllergyRules($drugId, $patientUid);

        return new CdsAlertCollection(
            array_merge($rules, $allergyRules)
        );
    }

    /**
     * Record a clinician override for a Tier 3 alert.
     * Tier 4 alerts cannot be overridden.
     */
    public function recordOverride(
        int $ruleId,
        int $clinicianId,
        string $reason
    ): CdsOverride {
        $rule = $this->ruleRepo->findOrFail($ruleId);

        if ($rule->severity === 4) {
            throw new FatalInteractionCannotBeOverriddenException();
        }

        return $this->overrideRepo->create([
            'rule_id'       => $ruleId,
            'clinician_id'  => $clinicianId,
            'reason'        => $reason,
            'overridden_at' => now(),
        ]);
    }
}
```

**Rule Store:** Database table `cds_rules` with columns: `rule_id` (PK), `category` (`drug-drug`, `drug-allergy`, `dosing`, `duplicate-therapy`), `severity` (1-4), `trigger_drug_id`, `interacting_drug_id` (nullable), `allergy_class` (nullable), `condition` (JSON), `message` (text). Not tenant-scoped — rules are shared across all facilities.

**Alert Response Tiers (BR-CLIN-004):**

| Tier | Label | UI Behaviour | Override | Logged |
|---|---|---|---|---|
| 1 | Info | Sidebar note | Not required | No |
| 2 | Warning | Amber banner | Not required | No |
| 3 | Serious | Modal blocks workflow | Clinician must enter reason (min 20 chars) | Yes — `cds_overrides` |
| 4 | Fatal | Hard stop | Cannot be overridden; pharmacist intervention required | Yes — `cds_overrides` (escalation only) |

### 3.4 Terminology Service

**Class:** `App\Services\Clinical\TerminologyService`

**Responsibility:** Provides a single gateway to ICD-10, ICD-11, SNOMED CT, LOINC, RxNorm, and ATC code systems. All terminology lookups pass through this service to ensure consistent caching and mapping.

```php
final class TerminologyService
{
    public function __construct(
        private readonly TerminologyRepository $repo,
        private readonly CacheManager $cache,
    ) {}

    /**
     * Search a code system by term.
     * Returns up to 25 results within 200 ms at P95.
     *
     * @param string $system  One of: icd10, icd11, snomed, loinc, rxnorm, atc
     * @param string $query   Search term (min 2 chars)
     * @return TerminologyResult[]
     */
    public function searchByTerm(string $system, string $query): array
    {
        $cacheKey = "term:{$system}:" . md5($query);

        return $this->cache->remember($cacheKey, 3600, function () use ($system, $query) {
            return $this->repo->search($system, $query, limit: 25);
        });
    }

    /**
     * Retrieve a single code by exact code value.
     */
    public function getByCode(string $system, string $code): ?TerminologyResult
    {
        $cacheKey = "code:{$system}:{$code}";

        return $this->cache->remember($cacheKey, 86400, function () use ($system, $code) {
            return $this->repo->findByCode($system, $code);
        });
    }

    /**
     * Map a code from one system to another (e.g., ICD-10 to SNOMED CT).
     * Returns null if no mapping exists.
     */
    public function mapCode(string $fromSystem, string $toSystem, string $code): ?string
    {
        return $this->repo->findMapping($fromSystem, $toSystem, $code);
    }
}
```

**Caching:** Redis cache per code system. ICD-10/ICD-11 search results cached with 1-hour TTL. Exact code lookups cached with 24-hour TTL. Cache is warmed on deployment for the 500 most-used ICD-10 codes in Uganda (malaria B50, HIV B20-B24, pneumonia J18, diarrhoea A09, etc.).

### 3.5 Enterprise Master Patient Index Service

**Class:** `App\Services\Clinical\EMPIService`

**Responsibility:** Probabilistic patient matching across the global patient pool. Used at registration (FR-REG-001) and during nightly batch duplicate scans (FR-REG-009).

```php
final class EMPIService
{
    private const THRESHOLD_DUPLICATE_WARNING = 80;
    private const THRESHOLD_AUTO_LINK         = 95;
    private const THRESHOLD_ADVISORY          = 60;

    public function __construct(
        private readonly GlobalPatientRepository $globalRepo,
    ) {}

    /**
     * Find potential duplicates using probabilistic matching.
     *
     * @return EMPICandidate[] Each with patient_uid and confidence score (0-100)
     */
    public function matchPatient(
        string $firstName,
        string $lastName,
        ?string $dob,
        ?string $nin,
        ?string $phone
    ): array {
        $candidates = $this->globalRepo->getCandidates($firstName, $lastName, $dob);

        return array_map(
            fn (GlobalPatient $candidate) => new EMPICandidate(
                patientUid: $candidate->patient_uid,
                confidence: $this->calculateScore($candidate, $firstName, $lastName, $dob, $nin, $phone),
            ),
            $candidates
        );
    }

    /**
     * Weighted scoring algorithm (BR-PID-001):
     *   Name (Soundex + Metaphone):  30%
     *   DOB (exact match):           25%
     *   NIN (exact match):           25%
     *   Phone (exact match):         20%
     *
     * Soundex and Metaphone are adapted for African naming patterns:
     * compound surnames, clan names, and spelling variations.
     */
    private function calculateScore(
        GlobalPatient $candidate,
        string $firstName,
        string $lastName,
        ?string $dob,
        ?string $nin,
        ?string $phone
    ): float {
        $score = 0.0;

        // Name matching — 30% weight
        $nameScore = $this->fuzzyNameScore($candidate, $firstName, $lastName);
        $score += $nameScore * 30;

        // DOB — 25% weight
        if ($dob !== null && $candidate->date_of_birth === $dob) {
            $score += 25;
        }

        // NIN — 25% weight
        if ($nin !== null && $candidate->nin === $nin) {
            $score += 25;
        }

        // Phone — 20% weight
        if ($phone !== null && $candidate->contact_phone === $phone) {
            $score += 20;
        }

        return round($score, 1);
    }

    private function fuzzyNameScore(
        GlobalPatient $candidate,
        string $firstName,
        string $lastName
    ): float {
        $firstSoundex  = soundex($firstName) === soundex($candidate->first_name) ? 0.5 : 0.0;
        $firstMeta     = metaphone($firstName) === metaphone($candidate->first_name) ? 0.5 : 0.0;
        $lastSoundex   = soundex($lastName) === soundex($candidate->last_name) ? 0.5 : 0.0;
        $lastMeta      = metaphone($lastName) === metaphone($candidate->last_name) ? 0.5 : 0.0;

        return ($firstSoundex + $firstMeta + $lastSoundex + $lastMeta) / 2.0;
    }
}
```

**Thresholds (BR-PID-002):**

| Score Range | Action |
|---|---|
| > 95% | Auto-link to existing global record |
| > 80% | Mandatory duplicate warning — registrar must confirm "New Patient" or select existing |
| 60-80% | Advisory notification to Records Officer |
| < 60% | No alert |

### 3.6 HL7 Gateway Service

**Class:** `App\Services\Lab\HL7GatewayService`

**Responsibility:** Handles bidirectional HL7 v2.x messaging between Medic8 and laboratory analysers (Cobas, Mindray, Sysmex). Translates ORM (Order Request) and ORU (Observation Result Unsolicited) messages.

```php
final class HL7GatewayService
{
    public function __construct(
        private readonly LabRequestRepository $labRepo,
        private readonly HL7Parser $parser,
        private readonly HL7Builder $builder,
    ) {}

    /**
     * Process an inbound ORU message from an analyser.
     * Parses the message, matches to a lab request by LAN, and auto-populates results.
     */
    public function processInboundORU(string $rawMessage): HL7ProcessingResult
    {
        $parsed = $this->parser->parseORU($rawMessage);
        $labRequest = $this->labRepo->findByAccessionNumber($parsed->accessionNumber);

        if ($labRequest === null) {
            return HL7ProcessingResult::unmatchedResult($parsed);
        }

        foreach ($parsed->observations as $obs) {
            $this->labRepo->upsertResult(
                requestId:   $labRequest->id,
                parameterId: $obs->parameterId,
                value:       $obs->value,
                unit:        $obs->unit,
                flag:        $obs->abnormalFlag,
                source:      'analyser',
            );
        }

        return HL7ProcessingResult::matched($labRequest->id);
    }

    /**
     * Generate an outbound ORM message for a new lab request.
     * Sent to bidirectional analysers to place the order on the analyser worklist.
     */
    public function buildOutboundORM(int $labRequestId): string
    {
        $request = $this->labRepo->findOrFail($labRequestId);
        return $this->builder->buildORM($request);
    }
}
```

---

## 4. Phase 1 Module Specifications

### 4.1 Patient Module

**Files:**
- `PatientController` — register, lookup, merge, profile, identifiers, guardians
- `PatientService` — registration logic, global identity matching, merge/unmerge
- `TriageService` — vital signs recording, NEWS2 calculation, triage queue
- `PatientRepository` — tenant-scoped patient queries
- `GlobalPatientRepository` — cross-tenant global identity queries (not tenant-scoped)
- `RegisterPatientRequest`, `UpdatePatientRequest`, `MergePatientRequest` — validation
- `PatientPolicy` — merge restricted to Records Officer / Facility Admin

#### 4.1.1 PatientService

```php
final class PatientService
{
    public function __construct(
        private readonly PatientRepository $patientRepo,
        private readonly GlobalPatientRepository $globalRepo,
        private readonly EMPIService $empi,
        private readonly MRNGeneratorService $mrnGenerator,
        private readonly AuditService $audit,
    ) {}

    /**
     * Register a new patient (FR-REG-001).
     *
     * @throws DuplicateDetectedException  Confidence > 80%, user must resolve (BR-PID-002)
     * @throws ContactRequiredException    Neither phone nor address provided (BR-DATA-006)
     */
    public function register(RegisterPatientRequest $request): Patient
    {
        // Step 1: EMPI duplicate check (FR-REG-009)
        $candidates = $this->empi->matchPatient(
            firstName: $request->first_name,
            lastName:  $request->last_name,
            dob:       $request->date_of_birth,
            nin:       $request->nin,
            phone:     $request->contact_phone,
        );

        $highConfidence = array_filter(
            $candidates,
            fn (EMPICandidate $c) => $c->confidence > EMPIService::THRESHOLD_DUPLICATE_WARNING
        );

        if (count($highConfidence) > 0 && !$request->confirmed_new_patient) {
            throw new DuplicateDetectedException($highConfidence);
        }

        // Step 2: Create global patient record (BR-DATA-001)
        $globalPatient = $this->globalRepo->create([
            'patient_uid'   => Str::uuid()->toString(),
            'first_name'    => $request->first_name,
            'last_name'     => $request->last_name,
            'date_of_birth' => $request->date_of_birth,
            'sex'           => $request->sex,
            'nin'           => $request->nin,
            'contact_phone' => $request->contact_phone,
        ]);

        // Step 3: Create facility patient record (tenant-scoped)
        $mrn = $this->mrnGenerator->generate();
        $patient = $this->patientRepo->create([
            'patient_uid'      => $globalPatient->patient_uid,
            'mrn'              => $mrn,
            'category'         => $this->resolveCategory($request->date_of_birth),
            'status'           => 'active',
            'blood_group'      => $request->blood_group,
            'photo_path'       => $request->photo_path,
            'nationality'      => $request->nationality ?? 'UG',
        ]);

        // Step 4: Store identifiers (FR-REG-005)
        $this->storeIdentifiers($globalPatient->patient_uid, $request);

        // Step 5: Store allergies and chronic conditions
        $this->storeAllergies($patient, $request->allergies ?? []);
        $this->storeChronicConditions($patient, $request->chronic_conditions ?? []);

        event(new PatientRegistered(
            patientUid: $globalPatient->patient_uid,
            facilityId: app('facility_id'),
            mrn:        $mrn,
        ));

        return $patient;
    }

    /**
     * Search for patients within the caller's facility (FR-REG-003).
     * Searches: first_name, last_name, mrn, contact_phone, nin.
     * Returns up to 25 results within 300 ms at P95.
     */
    public function lookup(string $query): Collection
    {
        return $this->patientRepo->searchFuzzy($query, limit: 25);
    }

    /**
     * Merge two patient records (FR-REG-008, BR-PID-003).
     * Transfers all clinical and billing data from source to target.
     * Reversible within 30 days.
     *
     * @throws UnauthorizedException Only Records Officer or Facility Admin
     */
    public function merge(string $sourceUid, string $targetUid, int $performedBy): MergeResult
    {
        $transferCounts = $this->patientRepo->transferAllRecords($sourceUid, $targetUid);
        $this->globalRepo->markAsMerged($sourceUid, $targetUid);

        $this->audit->log(
            action:       'PATIENT_MERGE',
            resourceType: 'patient',
            resourceId:   $targetUid,
            metadata:     ['source_uid' => $sourceUid, 'counts' => $transferCounts],
        );

        event(new PatientMerged(
            sourceUid: $sourceUid,
            targetUid: $targetUid,
            mergedBy:  $performedBy,
        ));

        return new MergeResult($targetUid, $transferCounts);
    }

    /**
     * Reverse a patient merge within the 30-day window (BR-PID-003).
     *
     * @throws UnmergeWindowExpiredException  Merge older than 30 days
     */
    public function unmerge(string $sourceUid, string $targetUid): void
    {
        $mergeRecord = $this->patientRepo->findMergeRecord($sourceUid, $targetUid);

        if ($mergeRecord->merged_at->diffInDays(now()) > 30) {
            throw new UnmergeWindowExpiredException();
        }

        $this->patientRepo->reverseTransfer($sourceUid, $targetUid);
        $this->globalRepo->unmarkMerge($sourceUid);
    }

    /**
     * Assign or update patient category (FR-REG-004).
     * Categories: adult, paediatric, staff, vip, indigent, refugee.
     */
    public function updateCategory(string $patientUid, string $category): void
    {
        $this->patientRepo->updateCategory($patientUid, $category);

        $this->audit->log(
            action:       'CATEGORY_CHANGED',
            resourceType: 'patient',
            resourceId:   $patientUid,
            metadata:     ['new_category' => $category],
        );
    }

    private function resolveCategory(?string $dob): string
    {
        if ($dob === null) {
            return 'adult';
        }
        $age = Carbon::parse($dob)->age;
        return $age < 12 ? 'paediatric' : 'adult';
    }
}
```

#### 4.1.2 TriageService

```php
final class TriageService
{
    public function __construct(
        private readonly VitalsRepository $vitalsRepo,
        private readonly NEWS2Calculator $news2,
        private readonly TriageQueueRepository $queueRepo,
    ) {}

    /**
     * Record triage vital signs (FR-OPD-001).
     * Calculates BMI, NEWS2, and Z-scores (for children under 5).
     * Assigns triage level based on NEWS2 score.
     *
     * @throws MuacRequiredException  Patient under 12 and MUAC not provided
     */
    public function recordVitals(string $patientUid, int $visitId, array $vitals): VitalsRecord
    {
        $patient = app(PatientRepository::class)->findByUid($patientUid);

        // MUAC required for patients under 12
        if ($patient->age < 12 && empty($vitals['muac'])) {
            throw new MuacRequiredException();
        }

        // Auto-calculate BMI
        $vitals['bmi'] = round($vitals['weight'] / (($vitals['height'] / 100) ** 2), 1);

        // NEWS2 score calculation (BR-CLIN-007)
        $news2Score = $this->news2->calculate(
            respiratoryRate: $vitals['respiratory_rate'],
            spo2:            $vitals['spo2'],
            systolicBp:      $vitals['systolic_bp'],
            pulse:           $vitals['pulse'],
            temperature:     $vitals['temperature'],
            consciousness:   $vitals['consciousness'] ?? 'alert',
        );

        $vitals['news2_score'] = $news2Score;
        $vitals['triage_level'] = $this->news2->suggestTriageLevel($news2Score);

        // Z-scores for children under 5 (WHO growth standards)
        if ($patient->age < 5) {
            $vitals['z_scores'] = $this->calculateZScores($patient, $vitals);
        }

        $record = $this->vitalsRepo->create($patientUid, $visitId, $vitals);

        // Add patient to triage queue sorted by priority (BR-CLIN-001)
        $this->queueRepo->enqueue($patientUid, $visitId, $vitals['triage_level']);

        event(new VitalsRecorded(
            patientUid: $patientUid,
            visitId:    $visitId,
            news2Score: $news2Score,
        ));

        // NEWS2 >= 7: immediate clinical review required
        if ($news2Score >= 7) {
            event(new PatientTriaged(
                patientUid:  $patientUid,
                visitId:     $visitId,
                triageLevel: 'emergency',
                news2Score:  $news2Score,
            ));
        }

        return $record;
    }
}
```

#### 4.1.3 PatientRepository Interface

```php
interface PatientRepositoryInterface
{
    public function create(array $data): Patient;
    public function findByUid(string $patientUid): ?Patient;
    public function searchFuzzy(string $query, int $limit = 25): Collection;
    public function getDuplicateCandidates(string $firstName, string $lastName, ?string $dob): Collection;
    public function updateCategory(string $patientUid, string $category): void;
    public function transferAllRecords(string $sourceUid, string $targetUid): array;
    public function reverseTransfer(string $sourceUid, string $targetUid): void;
    public function findMergeRecord(string $sourceUid, string $targetUid): PatientMerge;
}
```

#### 4.1.4 Validation Rules

**`RegisterPatientRequest`:**

```php
public function rules(): array
{
    return [
        'first_name'      => ['required', 'string', 'max:100'],
        'last_name'       => ['required', 'string', 'max:100'],
        'sex'             => ['required', Rule::in(['male', 'female'])],
        'date_of_birth'   => ['required_without:estimated_age', 'date', 'before:today'],
        'estimated_age'   => ['required_without:date_of_birth', 'integer', 'min:0', 'max:150'],
        'contact_phone'   => ['required_without:physical_address', 'regex:/^\+[1-9]\d{6,14}$/'],
        'physical_address'=> ['required_without:contact_phone', 'string', 'max:500'],
        'nin'             => ['nullable', 'string', 'max:20'],
        'blood_group'     => ['nullable', Rule::in(['A+','A-','B+','B-','AB+','AB-','O+','O-'])],
        'allergies'       => ['nullable', 'array'],
        'allergies.*.name'=> ['required_with:allergies', 'string'],
        'allergies.*.severity' => ['required_with:allergies', Rule::in(['mild','moderate','severe','anaphylaxis'])],
        'chronic_conditions'   => ['nullable', 'array'],
        'chronic_conditions.*' => ['string', 'regex:/^[A-Z]\d{2}(\.\d{1,2})?$/'], // ICD-10 format
    ];
}
```

---

### 4.2 OPD Module

**Files:**
- `EncounterController` — SOAP consultation, visit lifecycle
- `PrescriptionController` — prescription CRUD, drug search
- `InvestigationController` — lab/radiology order entry
- `EncounterService` — visit creation, SOAP recording, diagnosis, disposition
- `PrescriptionService` — prescription creation, drug interaction check, Five Rights
- `InvestigationService` — lab and radiology order dispatching
- `PaediatricDosingService` — weight-based dose calculation (BR-CLIN-006)
- `EncounterRepository`, `PrescriptionRepository`, `InvestigationRepository`
- `CreatePrescriptionRequest`, `RecordDiagnosisRequest` — validation

#### 4.2.1 EncounterService

```php
final class EncounterService
{
    public function __construct(
        private readonly EncounterRepository $encounterRepo,
        private readonly TerminologyService $terminology,
        private readonly BillingService $billing,
        private readonly AuditService $audit,
    ) {}

    /**
     * Create a new OPD visit (FR-OPD-003).
     * Posts a consultation fee to the patient's billing account (BR-FIN-001).
     */
    public function createVisit(string $patientUid, int $clinicianId): Encounter
    {
        $encounter = $this->encounterRepo->create([
            'patient_uid'   => $patientUid,
            'clinician_id'  => $clinicianId,
            'department'    => 'OPD',
            'status'        => 'in_progress',
            'started_at'    => now(),
        ]);

        $this->billing->addCharge(
            patientUid:   $patientUid,
            sourceModule: 'OPD',
            sourceId:     $encounter->id,
            serviceCode:  'CONSULTATION',
        );

        event(new EncounterCreated(
            encounterId: $encounter->id,
            patientUid:  $patientUid,
            clinicianId: $clinicianId,
        ));

        return $encounter;
    }

    /**
     * Record SOAP notes (FR-OPD-003).
     * Subjective, Objective, Assessment, and Plan are stored as JSON fields.
     */
    public function recordSOAP(int $encounterId, array $soapData): Encounter
    {
        return $this->encounterRepo->updateSOAP($encounterId, [
            'subjective' => $soapData['subjective'] ?? null,
            'objective'  => $soapData['objective'] ?? null,
            'plan_notes' => $soapData['plan_notes'] ?? null,
        ]);
    }

    /**
     * Add an ICD-10/ICD-11 coded diagnosis (FR-OPD-004).
     * Free-text-only diagnosis entry is not permitted (BR-DATA-006).
     *
     * @throws IcdCodeRequiredException  No ICD code provided
     */
    public function addDiagnosis(
        int $encounterId,
        string $icdCode,
        string $clinicalDescription,
        bool $isPrimary = false
    ): Diagnosis {
        // Validate ICD code exists in terminology service
        $term = $this->terminology->getByCode('icd10', $icdCode);
        if ($term === null) {
            $term = $this->terminology->getByCode('icd11', $icdCode);
        }
        if ($term === null) {
            throw new InvalidIcdCodeException($icdCode);
        }

        $diagnosis = $this->encounterRepo->addDiagnosis($encounterId, [
            'icd_code'             => $icdCode,
            'icd_system'           => $term->system,
            'clinical_description' => $clinicalDescription,
            'is_primary'           => $isPrimary,
        ]);

        event(new DiagnosisRecorded(
            encounterId: $encounterId,
            icdCode:     $icdCode,
            patientUid:  $this->encounterRepo->findOrFail($encounterId)->patient_uid,
        ));

        return $diagnosis;
    }

    /**
     * End visit with disposition (FR-OPD-013).
     * Dispositions: discharged, admitted, referred, left_without_being_seen.
     */
    public function endVisit(int $encounterId, string $disposition): Encounter
    {
        $encounter = $this->encounterRepo->findOrFail($encounterId);

        if ($disposition === 'referred') {
            $hasReferral = $this->encounterRepo->hasReferral($encounterId);
            if (!$hasReferral) {
                throw new ReferralRequiredException();
            }
        }

        $this->encounterRepo->update($encounterId, [
            'status'      => 'completed',
            'disposition' => $disposition,
            'ended_at'    => now(),
        ]);

        // Remove from all active queues
        app(TriageQueueRepository::class)->dequeue($encounter->patient_uid);

        return $this->encounterRepo->findOrFail($encounterId);
    }
}
```

#### 4.2.2 PrescriptionService

```php
final class PrescriptionService
{
    public function __construct(
        private readonly PrescriptionRepository $rxRepo,
        private readonly ClinicalDecisionSupportService $cds,
        private readonly PaediatricDosingService $paedDosing,
        private readonly StockService $stockService,
        private readonly FormularyRepository $formularyRepo,
        private readonly BillingService $billing,
    ) {}

    /**
     * Create a prescription (FR-OPD-006).
     * Executes Five Rights validation (BR-CLIN-008), drug interaction check (BR-CLIN-004),
     * paediatric dose safeguards (BR-CLIN-006), and stock-aware warning (BR-RX-002).
     *
     * @param PrescriptionItem[] $items Array of drug/dose/frequency/duration/route
     * @throws FiveRightsViolationException  Any of the Five Rights fails
     * @throws FatalInteractionException     Tier 4 interaction detected
     * @throws WeightRequiredException       Paediatric patient without weight on file
     */
    public function create(
        int $encounterId,
        string $patientUid,
        int $clinicianId,
        array $items
    ): Prescription {
        $patient = app(PatientRepository::class)->findByUid($patientUid);

        foreach ($items as $item) {
            // Right Drug: must be in active formulary
            $drug = $this->formularyRepo->findActiveOrFail($item->drugId);

            // Right Route: route must be valid for the drug
            if (!in_array($item->route, $drug->valid_routes, true)) {
                throw new FiveRightsViolationException('INVALID_ROUTE', $drug->generic_name, $item->route);
            }

            // Right Dose: within therapeutic range
            if ($item->dose > $drug->max_dose) {
                throw new FiveRightsViolationException('DOSE_EXCEEDS_MAXIMUM', $drug->generic_name, $item->dose);
            }

            // Paediatric safeguards (BR-CLIN-006)
            if ($patient->category === 'paediatric' || $patient->age < 12) {
                $this->paedDosing->validate($patient, $drug, $item->dose);
            }

            // Drug interaction check (BR-CLIN-004)
            $activeDrugIds = $this->rxRepo->getActiveDrugIds($patientUid);
            $alerts = $this->cds->checkInteractions($item->drugId, $patientUid, $activeDrugIds);

            if ($alerts->hasBlockingAlert()) {
                throw new FatalInteractionException($alerts->getBlockingAlerts());
            }

            // Stock-aware warning (BR-RX-002)
            $stock = $this->stockService->getCurrentStock($item->drugId);
            $item->stockWarning = $stock < $item->quantity
                ? new StockWarning($stock, $this->formularyRepo->getAlternatives($item->drugId))
                : null;
        }

        $prescription = $this->rxRepo->create([
            'encounter_id'  => $encounterId,
            'patient_uid'   => $patientUid,
            'clinician_id'  => $clinicianId,
            'status'        => 'pending',
            'prescribed_at' => now(),
        ]);

        foreach ($items as $item) {
            $this->rxRepo->addItem($prescription->id, [
                'drug_id'    => $item->drugId,
                'dose'       => $item->dose,
                'dose_unit'  => $item->doseUnit,
                'frequency'  => $item->frequency,
                'duration'   => $item->duration,
                'route'      => $item->route,
                'quantity'   => $item->quantity,
                'instructions' => $item->instructions,
            ]);

            // Auto-billing (BR-FIN-001)
            $this->billing->addCharge(
                patientUid:   $patientUid,
                sourceModule: 'PHARMACY',
                sourceId:     $prescription->id,
                serviceCode:  'DRUG',
                drugId:       $item->drugId,
                quantity:     $item->quantity,
            );
        }

        event(new PrescriptionWritten(
            prescriptionId: $prescription->id,
            patientUid:     $patientUid,
            drugIds:        array_map(fn ($i) => $i->drugId, $items),
        ));

        return $prescription;
    }
}
```

#### 4.2.3 PaediatricDosingService

```php
final class PaediatricDosingService
{
    /**
     * Validate paediatric dose against weight-based calculation (BR-CLIN-006).
     *
     * @throws WeightRequiredException       No weight recorded within 24 hours
     * @throws DecimalErrorSuspectedException Dose exceeds 10x expected
     * @throws DoseExceedsAdultCeilingException
     */
    public function validate(Patient $patient, Drug $drug, float $prescribedDose): void
    {
        $weight = app(VitalsRepository::class)->getLatestWeight($patient->patient_uid, hoursAgo: 24);

        if ($weight === null) {
            throw new WeightRequiredException();
        }

        $calculatedDose = $weight * $drug->mg_per_kg;

        // Adult ceiling cap
        if ($calculatedDose > $drug->max_dose) {
            $calculatedDose = $drug->max_dose;
        }

        // 10x decimal error detection
        if ($prescribedDose > $calculatedDose * 10) {
            throw new DecimalErrorSuspectedException(
                prescribed: $prescribedDose,
                expected:   $calculatedDose,
                weight:     $weight,
            );
        }
    }

    /**
     * Calculate the recommended paediatric dose (FR-PHR-014).
     * Returns the calculated dose with the adult ceiling applied.
     */
    public function calculateDose(float $weightKg, Drug $drug): PaediatricDoseResult
    {
        $rawDose = $weightKg * $drug->mg_per_kg;
        $cappedDose = min($rawDose, $drug->max_dose);

        return new PaediatricDoseResult(
            calculatedDose: round($rawDose, 2),
            cappedDose:     round($cappedDose, 2),
            ceilingApplied: $rawDose > $drug->max_dose,
            weightUsed:     $weightKg,
        );
    }
}
```

#### 4.2.4 InvestigationService

```php
final class InvestigationService
{
    public function __construct(
        private readonly InvestigationRepository $investigationRepo,
        private readonly BillingService $billing,
        private readonly NotificationService $notifications,
    ) {}

    /**
     * Request a lab or radiology investigation (FR-OPD-005).
     * Posts a billing charge per test and notifies the lab/radiology team.
     * Emergency requests jump to queue top (BR-CLIN-001).
     */
    public function requestLab(
        int $encounterId,
        string $patientUid,
        int $clinicianId,
        array $tests
    ): Collection {
        $requests = collect();

        foreach ($tests as $test) {
            $labRequest = $this->investigationRepo->create([
                'encounter_id'        => $encounterId,
                'patient_uid'         => $patientUid,
                'clinician_id'        => $clinicianId,
                'test_id'             => $test['test_id'],
                'specimen_type'       => $test['specimen_type'] ?? null,
                'clinical_indication' => $test['clinical_indication'] ?? null,
                'urgency'             => $test['urgency'] ?? 'routine',
                'status'              => 'requested',
                'accession_number'    => $this->generateAccessionNumber(),
                'requested_at'        => now(),
            ]);

            $this->billing->addCharge(
                patientUid:   $patientUid,
                sourceModule: 'LAB',
                sourceId:     $labRequest->id,
                serviceCode:  'LAB_TEST',
                testId:       $test['test_id'],
            );

            $this->notifications->sendToRole('lab_technician', [
                'type'    => 'lab_request',
                'message' => "New {$test['urgency']} lab request for MRN {$labRequest->patient->mrn}",
                'urgency' => $test['urgency'],
            ]);

            $requests->push($labRequest);
        }

        event(new InvestigationRequested(
            requestId:  $requests->first()->id,
            patientUid: $patientUid,
            testIds:    array_column($tests, 'test_id'),
            urgency:    $tests[0]['urgency'] ?? 'routine',
        ));

        return $requests;
    }

    private function generateAccessionNumber(): string
    {
        $year = now()->format('Y');
        $seq = $this->investigationRepo->getNextSequence();
        return sprintf('LAB-%s-%05d', $year, $seq);
    }
}
```

---

### 4.3 Laboratory Module

**Files:**
- `LabController` — request queue, sample collection, result entry, validation
- `LabService` — specimen lifecycle, result entry, critical value escalation
- `QualityControlService` — QC recording, Westgard rule evaluation, Levey-Jennings
- `HL7GatewayService` — analyser interface (see Section 3.6)
- `LabRepository` — tenant-scoped lab queries
- `EnterLabResultRequest`, `ValidateResultRequest` — validation
- `EscalateCriticalValueJob` — delayed escalation at 30/60-minute intervals

#### 4.3.1 LabService

```php
final class LabService
{
    public function __construct(
        private readonly LabRepository $labRepo,
        private readonly QualityControlService $qcService,
        private readonly NotificationService $notifications,
        private readonly AuditService $audit,
    ) {}

    /**
     * Record sample collection (FR-LAB-002).
     * Generates barcode/QR label data for 25x50mm lab label stock.
     */
    public function collectSample(
        int $requestId,
        int $technicianId,
        string $specimenType
    ): SampleCollectionResult {
        $request = $this->labRepo->findOrFail($requestId);

        $this->labRepo->update($requestId, [
            'status'           => 'collected',
            'collected_by'     => $technicianId,
            'collected_at'     => now(),
            'specimen_type'    => $specimenType,
        ]);

        $labelData = new LabLabel(
            patientName:    $request->patient->full_name,
            mrn:            $request->patient->mrn,
            accessionNumber: $request->accession_number,
            testName:       $request->test->test_name,
            collectedAt:    now(),
            specimenType:   $specimenType,
        );

        return new SampleCollectionResult($request, $labelData);
    }

    /**
     * Enter lab result (FR-LAB-004).
     * Auto-flags abnormal values (H/L/HH/LL).
     * Triggers critical value alert for HH/LL (FR-LAB-005, BR-CLIN-003).
     *
     * @throws QcOutOfControlException  Assay is flagged out-of-control by Westgard rules
     */
    public function enterResult(
        int $requestId,
        int $technicianId,
        array $results
    ): LabResult {
        $request = $this->labRepo->findOrFail($requestId);

        // Check QC status — block if out of control (FR-LAB-007)
        if ($this->qcService->isOutOfControl($request->test_id)) {
            throw new QcOutOfControlException($request->test->test_name);
        }

        $isCritical = false;

        foreach ($results as $result) {
            $parameter = $this->labRepo->getParameter($request->test_id, $result['parameter_id']);
            $flag = $this->evaluateFlag($result['value'], $parameter, $request->patient);

            $this->labRepo->upsertResult(
                requestId:   $requestId,
                parameterId: $result['parameter_id'],
                value:       $result['value'],
                unit:        $result['unit'],
                flag:        $flag,
                source:      'manual',
                enteredBy:   $technicianId,
            );

            if (in_array($flag, ['HH', 'LL'], true)) {
                $isCritical = true;

                event(new LabCriticalValue(
                    requestId:             $requestId,
                    patientUid:            $request->patient_uid,
                    parameter:             $parameter->name,
                    value:                 $result['value'],
                    requestingClinicianId: $request->clinician_id,
                ));

                // Timed escalation cascade (BR-CLIN-003)
                EscalateCriticalValueJob::dispatch($requestId, 'ward_sister')
                    ->delay(now()->addMinutes(30));
                EscalateCriticalValueJob::dispatch($requestId, 'facility_admin')
                    ->delay(now()->addMinutes(60));
            }
        }

        $this->labRepo->update($requestId, [
            'status'     => 'result_ready_pending_validation',
            'entered_by' => $technicianId,
            'entered_at' => now(),
        ]);

        event(new LabResultEntered(
            requestId:  $requestId,
            patientUid: $request->patient_uid,
            isCritical: $isCritical,
        ));

        return $this->labRepo->getResult($requestId);
    }

    /**
     * Validate a lab result (FR-LAB-006).
     * Two-step validation: technician enters, supervisor approves/rejects.
     * Only validated results are visible to clinicians.
     */
    public function validateResult(
        int $requestId,
        int $supervisorId,
        bool $approved,
        ?string $rejectionReason = null
    ): void {
        if ($approved) {
            $this->labRepo->update($requestId, [
                'status'        => 'validated',
                'validated_by'  => $supervisorId,
                'validated_at'  => now(),
            ]);

            // Notify requesting clinician
            $request = $this->labRepo->findOrFail($requestId);
            $this->notifications->sendToUser($request->clinician_id, [
                'type'    => 'lab_result_ready',
                'message' => "Lab results ready for {$request->patient->full_name}: {$request->test->test_name}",
            ]);
        } else {
            $this->labRepo->update($requestId, [
                'status'           => 'rejected',
                'rejection_reason' => $rejectionReason,
                'rejected_by'     => $supervisorId,
                'rejected_at'     => now(),
            ]);
        }
    }

    /**
     * Evaluate abnormal flag for a result value against age/sex-specific reference ranges.
     */
    private function evaluateFlag(
        float $value,
        TestParameter $parameter,
        Patient $patient
    ): ?string {
        $range = $parameter->getReferenceRange($patient->age, $patient->sex);

        if ($value >= $range->critical_high) return 'HH';
        if ($value <= $range->critical_low)  return 'LL';
        if ($value > $range->high)           return 'H';
        if ($value < $range->low)            return 'L';

        return null;
    }
}
```

#### 4.3.2 QualityControlService

```php
final class QualityControlService
{
    public function __construct(
        private readonly QcRepository $qcRepo,
    ) {}

    /**
     * Record a daily QC result and evaluate Westgard rules (FR-LAB-007).
     * Returns violation details if any rule is triggered.
     */
    public function recordQcResult(
        int $testId,
        int $technicianId,
        string $level,
        float $value
    ): QcEvaluation {
        $this->qcRepo->store($testId, $level, $value, $technicianId);

        $stats = $this->qcRepo->getStatistics($testId, $level);
        $recentValues = $this->qcRepo->getRecentValues($testId, $level, count: 10);

        $violations = $this->evaluateWestgardRules($value, $recentValues, $stats);

        if (count($violations) > 0) {
            $this->qcRepo->flagOutOfControl($testId, $violations);
        }

        return new QcEvaluation(
            testId:     $testId,
            value:      $value,
            mean:       $stats->mean,
            sd:         $stats->sd,
            violations: $violations,
        );
    }

    /**
     * Check whether an assay is currently out of control.
     * Out-of-control assays block patient result entry.
     */
    public function isOutOfControl(int $testId): bool
    {
        return $this->qcRepo->hasUnresolvedFlag($testId);
    }

    /**
     * Westgard rules: 1-2s (warning), 1-3s (reject), 2-2s, R-4s, 4-1s, 10x.
     */
    private function evaluateWestgardRules(
        float $current,
        array $recent,
        QcStatistics $stats
    ): array {
        $violations = [];
        $zScore = ($current - $stats->mean) / $stats->sd;

        // 1-3s: single result > 3 SD from mean
        if (abs($zScore) > 3) {
            $violations[] = '1-3s';
        }
        // 1-2s: single result > 2 SD (warning)
        elseif (abs($zScore) > 2) {
            $violations[] = '1-2s';
        }

        // 2-2s: two consecutive results > 2 SD on the same side
        if (count($recent) >= 1) {
            $prevZ = ($recent[0] - $stats->mean) / $stats->sd;
            if (abs($zScore) > 2 && abs($prevZ) > 2 && ($zScore * $prevZ > 0)) {
                $violations[] = '2-2s';
            }

            // R-4s: range between two consecutive results > 4 SD
            if (abs($zScore - $prevZ) > 4) {
                $violations[] = 'R-4s';
            }
        }

        // 4-1s: four consecutive results > 1 SD on the same side
        if (count($recent) >= 3) {
            $allSameSide = true;
            $sign = $zScore > 0 ? 1 : -1;
            foreach (array_slice($recent, 0, 3) as $prev) {
                $prevZ = ($prev - $stats->mean) / $stats->sd;
                if (abs($prevZ) <= 1 || ($prevZ > 0 ? 1 : -1) !== $sign) {
                    $allSameSide = false;
                    break;
                }
            }
            if ($allSameSide && abs($zScore) > 1) {
                $violations[] = '4-1s';
            }
        }

        // 10x: ten consecutive results on the same side of the mean
        if (count($recent) >= 9) {
            $sign = $zScore > 0 ? 1 : -1;
            $allSameSide = true;
            foreach (array_slice($recent, 0, 9) as $prev) {
                if (($prev - $stats->mean > 0 ? 1 : -1) !== $sign) {
                    $allSameSide = false;
                    break;
                }
            }
            if ($allSameSide) {
                $violations[] = '10x';
            }
        }

        return $violations;
    }
}
```

#### 4.3.3 LabRepository Interface

```php
interface LabRepositoryInterface
{
    public function create(array $data): LabRequest;
    public function findOrFail(int $requestId): LabRequest;
    public function findByAccessionNumber(string $accessionNumber): ?LabRequest;
    public function update(int $requestId, array $data): void;
    public function upsertResult(int $requestId, int $parameterId, $value, string $unit, ?string $flag, string $source, ?int $enteredBy = null): void;
    public function getResult(int $requestId): LabResult;
    public function getParameter(int $testId, int $parameterId): TestParameter;
    public function getPendingRequests(?string $urgency = null): Collection;
    public function getResultsForPatient(string $patientUid): Collection;
    public function getNextSequence(): int;
}
```

---

### 4.4 Pharmacy Module

**Files:**
- `PharmacyController` — prescription queue, dispensing, partial dispensing
- `StockController` — GRN, transfer, adjustment, return, expiry tracking
- `FormularyController` — drug formulary CRUD
- `NarcoticController` — controlled drug register
- `PharmacyService` — dispensing workflow, generic substitution
- `StockService` — stock movements (GRN, transfer, adjust), FIFO deduction, expiry check
- `NarcoticService` — controlled substance register, discrepancy detection
- `TallManService` — LASA drug name decoration
- `FormularyRepository`, `StockRepository`, `NarcoticRepository`, `PharmacyRepository`
- `DispenseDrugRequest`, `ReceiveGRNRequest`, `TransferStockRequest` — validation
- `CheckExpiryJob` — daily scheduled job for 90-day expiry flagging

#### 4.4.1 PharmacyService

```php
final class PharmacyService
{
    public function __construct(
        private readonly PharmacyRepository $pharmacyRepo,
        private readonly StockService $stockService,
        private readonly NarcoticService $narcoticService,
        private readonly TallManService $tallMan,
        private readonly NotificationService $notifications,
    ) {}

    /**
     * Get the pharmacy dispensing queue (FR-PHR-001).
     * Sorted by urgency (emergency > urgent > routine) then by prescription time.
     */
    public function getQueue(): Collection
    {
        return $this->pharmacyRepo->getPendingPrescriptions();
    }

    /**
     * Dispense a prescription (FR-PHR-002).
     * Deducts stock using FIFO, records batch and expiry, generates label data.
     *
     * @throws BatchExpiredException     Oldest batch is expired
     * @throws InsufficientStockException Use partialDispense() for partial fulfilment
     */
    public function dispense(
        int $prescriptionId,
        int $pharmacistId,
        array $itemDispensings
    ): DispenseResult {
        $prescription = $this->pharmacyRepo->findOrFail($prescriptionId);
        $labels = [];

        foreach ($itemDispensings as $itemId => $dispensingData) {
            $item = $this->pharmacyRepo->findItem($itemId);

            // FIFO stock deduction (nearest expiry first)
            $batchDeductions = $this->stockService->deductFIFO(
                drugId:   $item->drug_id,
                quantity: $dispensingData['quantity'],
            );

            $this->pharmacyRepo->recordDispensing($itemId, [
                'dispensed_quantity' => $dispensingData['quantity'],
                'pharmacist_id'     => $pharmacistId,
                'dispensed_at'      => now(),
                'batch_deductions'  => $batchDeductions,
            ]);

            // Narcotic register entry if controlled substance (BR-RX-001)
            if ($item->drug->is_controlled) {
                $this->narcoticService->recordDispensing(
                    drugId:       $item->drug_id,
                    quantity:     $dispensingData['quantity'],
                    patientUid:   $prescription->patient_uid,
                    prescriberId: $prescription->clinician_id,
                    pharmacistId: $pharmacistId,
                    witness:      $dispensingData['witness_name'] ?? null,
                );
            }

            // Generate dispensing label (FR-PHR-004)
            $labels[] = new DispensingLabel(
                patientName:   $prescription->patient->full_name,
                drugName:      $item->drug->generic_name,
                dose:          $item->dose . ' ' . $item->dose_unit,
                frequency:     $item->frequency,
                duration:      $item->duration . ' days',
                route:         $item->route,
                quantity:      $dispensingData['quantity'],
                instructions:  $item->instructions ?? 'Take as directed',
                facilityName:  app('facility_name'),
                dispensedAt:   now(),
                pharmacist:    $pharmacistId,
            );

            event(new DrugDispensed(
                prescriptionId: $prescriptionId,
                patientUid:     $prescription->patient_uid,
                drugId:         $item->drug_id,
                quantity:       $dispensingData['quantity'],
                batchId:        $batchDeductions[0]['batch_id'],
            ));
        }

        $this->pharmacyRepo->updateStatus($prescriptionId, 'dispensed');

        return new DispenseResult($prescription, $labels);
    }

    /**
     * Partial dispensing when stock is insufficient (FR-PHR-005).
     * Records dispensed quantity and creates a pending balance record.
     */
    public function partialDispense(
        int $prescriptionItemId,
        int $pharmacistId,
        int $dispensedQuantity
    ): PartialDispenseResult {
        $item = $this->pharmacyRepo->findItem($prescriptionItemId);
        $pendingBalance = $item->quantity - $dispensedQuantity;

        $batchDeductions = $this->stockService->deductFIFO(
            drugId:   $item->drug_id,
            quantity: $dispensedQuantity,
        );

        $this->pharmacyRepo->recordPartialDispensing($prescriptionItemId, [
            'dispensed_quantity' => $dispensedQuantity,
            'pending_balance'   => $pendingBalance,
            'pharmacist_id'     => $pharmacistId,
            'dispensed_at'      => now(),
            'batch_deductions'  => $batchDeductions,
        ]);

        // Notify prescribing clinician
        $this->notifications->sendToUser($item->prescription->clinician_id, [
            'type'    => 'partial_dispense',
            'message' => "Partial dispensing: {$dispensedQuantity}/{$item->quantity} {$item->drug->generic_name} for {$item->prescription->patient->full_name}. Balance: {$pendingBalance}.",
        ]);

        return new PartialDispenseResult(
            dispensed:      $dispensedQuantity,
            pendingBalance: $pendingBalance,
            drugName:       $item->drug->generic_name,
        );
    }

    /**
     * Substitute a branded drug with a generic equivalent (FR-PHR-003, BR-CLIN-002).
     * Notifies the prescribing doctor of the substitution.
     */
    public function substituteGeneric(
        int $prescriptionItemId,
        int $genericDrugId,
        int $pharmacistId,
        string $reason
    ): void {
        $item = $this->pharmacyRepo->findItem($prescriptionItemId);

        $this->pharmacyRepo->recordSubstitution($prescriptionItemId, [
            'original_drug_id'   => $item->drug_id,
            'substituted_drug_id'=> $genericDrugId,
            'pharmacist_id'      => $pharmacistId,
            'reason'             => $reason,
            'substituted_at'     => now(),
        ]);

        $genericDrug = $this->pharmacyRepo->findDrug($genericDrugId);

        $this->notifications->sendToUser($item->prescription->clinician_id, [
            'type'    => 'drug_substitution',
            'message' => "Prescription for {$item->drug->generic_name} substituted with {$genericDrug->generic_name} for {$item->prescription->patient->full_name} by pharmacist. Reason: {$reason}.",
        ]);
    }
}
```

#### 4.4.2 StockService

```php
final class StockService
{
    public function __construct(
        private readonly StockRepository $stockRepo,
        private readonly NotificationService $notifications,
    ) {}

    /**
     * Receive stock via Goods Received Note (FR-PHR-007).
     */
    public function receiveGRN(array $data): GoodsReceivedNote
    {
        $grn = $this->stockRepo->createGRN([
            'supplier'       => $data['supplier'],
            'invoice_number' => $data['invoice_number'],
            'received_by'    => $data['received_by'],
            'received_at'    => now(),
        ]);

        foreach ($data['items'] as $item) {
            $this->stockRepo->addBatch([
                'grn_id'       => $grn->id,
                'drug_id'      => $item['drug_id'],
                'batch_number' => $item['batch_number'],
                'expiry_date'  => $item['expiry_date'],
                'quantity'     => $item['quantity'],
                'unit_cost'    => $item['unit_cost'],
            ]);
        }

        return $grn;
    }

    /**
     * Transfer stock between stores (FR-PHR-007).
     * Source store decreases, destination store increases.
     * Receiving store must acknowledge receipt.
     */
    public function transferStock(
        int $drugId,
        int $sourceStoreId,
        int $destinationStoreId,
        int $quantity,
        int $transferredBy
    ): StockTransfer {
        $transfer = $this->stockRepo->createTransfer([
            'drug_id'              => $drugId,
            'source_store_id'      => $sourceStoreId,
            'destination_store_id' => $destinationStoreId,
            'quantity'             => $quantity,
            'transferred_by'      => $transferredBy,
            'status'               => 'pending_receipt',
            'transferred_at'      => now(),
        ]);

        $this->stockRepo->deductFromStore($sourceStoreId, $drugId, $quantity);

        return $transfer;
    }

    /**
     * Adjust stock with documented reason (FR-PHR-007).
     * Adjustments exceeding a configurable threshold require approval.
     */
    public function adjustStock(
        int $drugId,
        int $quantityDelta,
        string $reason,
        int $adjustedBy
    ): StockAdjustment {
        return $this->stockRepo->createAdjustment([
            'drug_id'        => $drugId,
            'quantity_delta'  => $quantityDelta,
            'reason'         => $reason,
            'adjusted_by'    => $adjustedBy,
            'adjusted_at'    => now(),
        ]);
    }

    /**
     * FIFO stock deduction (FR-PHR-002).
     * Deducts from the batch with the nearest expiry date first.
     *
     * @throws BatchExpiredException       Oldest available batch is expired
     * @throws InsufficientStockException  Total stock < requested quantity
     * @return array Batch deductions [{batch_id, quantity_deducted, batch_number, expiry_date}]
     */
    public function deductFIFO(int $drugId, int $quantity): array
    {
        $batches = $this->stockRepo->getActiveBatchesByExpiry($drugId);
        $remaining = $quantity;
        $deductions = [];

        foreach ($batches as $batch) {
            if ($batch->expiry_date < now()) {
                throw new BatchExpiredException($batch->batch_number, $batch->expiry_date);
            }

            $deductQty = min($remaining, $batch->quantity_on_hand);
            $this->stockRepo->deductBatch($batch->id, $deductQty);

            $deductions[] = [
                'batch_id'          => $batch->id,
                'quantity_deducted' => $deductQty,
                'batch_number'      => $batch->batch_number,
                'expiry_date'       => $batch->expiry_date,
            ];

            $remaining -= $deductQty;
            if ($remaining <= 0) break;
        }

        if ($remaining > 0) {
            throw new InsufficientStockException($drugId, $quantity, $quantity - $remaining);
        }

        // Check minimum stock level (FR-PHR-009)
        $currentStock = $this->stockRepo->getTotalStock($drugId);
        $minLevel = $this->stockRepo->getMinimumLevel($drugId);
        if ($minLevel !== null && $currentStock < $minLevel) {
            event(new StockLow(
                drugId:     $drugId,
                facilityId: app('facility_id'),
                currentQty: $currentStock,
                minLevel:   $minLevel,
            ));
        }

        return $deductions;
    }

    /**
     * Get current stock level for a drug across all stores (BR-RX-002).
     */
    public function getCurrentStock(int $drugId): int
    {
        return $this->stockRepo->getTotalStock($drugId);
    }
}
```

#### 4.4.3 NarcoticService

```php
final class NarcoticService
{
    public function __construct(
        private readonly NarcoticRepository $narcoticRepo,
        private readonly NotificationService $notifications,
    ) {}

    /**
     * Record a controlled substance dispensing event (FR-PHR-011, BR-RX-001).
     * Entry is immutable — cannot be edited or deleted.
     * Maintains a running balance per controlled substance.
     */
    public function recordDispensing(
        int $drugId,
        int $quantity,
        string $patientUid,
        int $prescriberId,
        int $pharmacistId,
        ?string $witness
    ): NarcoticRegisterEntry {
        $runningBalance = $this->narcoticRepo->getRunningBalance($drugId);
        $newBalance = $runningBalance - $quantity;

        return $this->narcoticRepo->createEntry([
            'drug_id'        => $drugId,
            'patient_uid'    => $patientUid,
            'quantity'       => $quantity,
            'prescriber_id'  => $prescriberId,
            'pharmacist_id'  => $pharmacistId,
            'witness'        => $witness,
            'running_balance'=> $newBalance,
            'recorded_at'    => now(),
        ]);
    }

    /**
     * Check for discrepancy between physical count and system balance (BR-RX-001).
     * Triggers an immediate alert to Facility Admin if mismatch detected.
     */
    public function reconcile(int $drugId, int $physicalCount, int $countedBy): NarcoticReconciliation
    {
        $systemBalance = $this->narcoticRepo->getRunningBalance($drugId);
        $discrepancy = $systemBalance - $physicalCount;

        $reconciliation = $this->narcoticRepo->createReconciliation([
            'drug_id'        => $drugId,
            'system_balance' => $systemBalance,
            'physical_count' => $physicalCount,
            'discrepancy'    => $discrepancy,
            'counted_by'     => $countedBy,
            'counted_at'     => now(),
        ]);

        if ($discrepancy !== 0) {
            $this->notifications->sendToRole('facility_admin', [
                'type'    => 'narcotic_discrepancy',
                'message' => "Narcotic discrepancy detected: {$reconciliation->drug->generic_name}. System: {$systemBalance}, Physical: {$physicalCount}, Difference: {$discrepancy}.",
                'urgency' => 'critical',
            ]);
        }

        return $reconciliation;
    }

    /**
     * Get the narcotic register for a specific drug (FR-PHR-011).
     * Returns all immutable register entries in chronological order.
     */
    public function getRegister(int $drugId): Collection
    {
        return $this->narcoticRepo->getEntriesForDrug($drugId);
    }
}
```

#### 4.4.4 TallManService

```php
final class TallManService
{
    /**
     * Decorate a drug name with Tall Man Lettering for LASA display (FR-PHR-013, BR-RX-003).
     * Differentiating letters are displayed in uppercase.
     *
     * @param string $genericName  e.g., "hydroxyzine"
     * @param string $tallManForm  e.g., "hydrOXYzine" (stored in formulary)
     * @return string The Tall Man form if LASA-flagged, otherwise the original name
     */
    public function decorate(Drug $drug): string
    {
        if (!$drug->lasa_flag || $drug->tall_man_form === null) {
            return $drug->generic_name;
        }

        return $drug->tall_man_form;
    }

    /**
     * Apply Tall Man decoration to a collection of drugs for display.
     */
    public function decorateCollection(Collection $drugs): Collection
    {
        return $drugs->map(function (Drug $drug) {
            $drug->display_name = $this->decorate($drug);
            return $drug;
        });
    }
}
```

---

### 4.5 Billing Module

**Files:**
- `BillingController` — patient account, payments, receipts, reconciliation
- `MobileMoneyController` — MoMo/Airtel Money payment initiation and callback
- `CreditController` — credit arrangement CRUD, ageing reports
- `BillingService` — charge posting, payment recording, receipt generation
- `MobileMoneyService` — MoMo/Airtel API integration, auto-reconciliation
- `CashierReconciliationService` — session reconciliation
- `MissingChargeDetectionService` — daily audit of clinical actions vs billing
- `BillingRepository`, `PaymentRepository`, `CreditRepository`
- `CollectPaymentRequest`, `InitiateMoMoRequest` — validation
- `MissingChargeDetectionJob` — daily scheduled job
- `ReconcileUnmatchedPaymentsJob` — daily unmatched payments report

#### 4.5.1 BillingService

```php
final class BillingService
{
    public function __construct(
        private readonly BillingRepository $billingRepo,
        private readonly PriceListRepository $priceListRepo,
        private readonly AuditService $audit,
    ) {}

    /**
     * Get patient account with running balance (FR-BIL-001).
     */
    public function getAccount(string $patientUid): PatientAccount
    {
        return $this->billingRepo->getAccount($patientUid);
    }

    /**
     * Post a billing charge to the patient account (FR-BIL-001, FR-BIL-004).
     * Auto-triggered by clinical actions via event listeners.
     * Applies category pricing multipliers (FR-BIL-003).
     */
    public function addCharge(
        string $patientUid,
        string $sourceModule,
        int $sourceId,
        string $serviceCode,
        ?int $drugId = null,
        ?int $testId = null,
        int $quantity = 1
    ): BillingLine {
        $patient = app(PatientRepository::class)->findByUid($patientUid);
        $priceEntry = $this->priceListRepo->findByServiceCode($serviceCode, $drugId, $testId);

        $unitPrice = $priceEntry->base_price;

        // Category pricing (FR-BIL-003)
        $multiplier = $this->priceListRepo->getCategoryMultiplier($patient->category);
        $adjustedPrice = (int) round($unitPrice * $multiplier);

        $line = $this->billingRepo->addLine([
            'patient_uid'    => $patientUid,
            'service_code'   => $serviceCode,
            'description'    => $priceEntry->service_name,
            'quantity'       => $quantity,
            'unit_price'     => $adjustedPrice,
            'total_amount'   => $adjustedPrice * $quantity,
            'source_module'  => $sourceModule,
            'source_id'      => $sourceId,
            'posted_by'      => auth()->id(),
            'posted_at'      => now(),
        ]);

        event(new ChargeAdded(
            patientUid:   $patientUid,
            amount:       $line->total_amount,
            sourceModule: $sourceModule,
            sourceId:     $sourceId,
        ));

        return $line;
    }

    /**
     * Collect a cash payment (FR-BIL-006).
     * Supports partial payments. Generates a receipt.
     */
    public function collectPayment(
        string $patientUid,
        int $amount,
        string $paymentMethod,
        int $cashierId,
        ?int $amountTendered = null
    ): PaymentResult {
        $changeDue = 0;
        if ($paymentMethod === 'cash' && $amountTendered !== null) {
            $changeDue = max(0, $amountTendered - $amount);
        }

        $payment = $this->billingRepo->recordPayment([
            'patient_uid'     => $patientUid,
            'amount'          => $amount,
            'payment_method'  => $paymentMethod,
            'cashier_id'      => $cashierId,
            'amount_tendered' => $amountTendered,
            'change_due'      => $changeDue,
            'paid_at'         => now(),
        ]);

        $receipt = $this->generateReceipt($payment);

        event(new PaymentReceived(
            patientUid:    $patientUid,
            amount:        $amount,
            paymentMethod: $paymentMethod,
            receiptNumber: $receipt->receipt_number,
        ));

        return new PaymentResult($payment, $receipt, $changeDue);
    }

    /**
     * Generate a sequential receipt (FR-BIL-005).
     * Receipt number format: RCT-{YEAR}-{SEQ:05d}, unique per facility.
     */
    public function generateReceipt(Payment $payment): Receipt
    {
        $year = now()->format('Y');
        $seq = $this->billingRepo->getNextReceiptSequence();
        $receiptNumber = sprintf('RCT-%s-%05d', $year, $seq);

        return $this->billingRepo->createReceipt([
            'receipt_number' => $receiptNumber,
            'payment_id'     => $payment->id,
            'patient_uid'    => $payment->patient_uid,
            'items'          => $this->billingRepo->getUnreceiptedLines($payment->patient_uid),
            'total_amount'   => $payment->amount,
            'payment_method' => $payment->payment_method,
            'cashier_id'     => $payment->cashier_id,
            'issued_at'      => now(),
        ]);
    }

    /**
     * Daily cashier reconciliation (FR-BIL-008, BR-FIN-004).
     * Flags discrepancies exceeding UGX 5,000 for supervisor review.
     */
    public function reconcileCashierSession(
        int $cashierId,
        int $openingFloat,
        array $collectionsByMode,
        int $bankingAmount,
        int $closingFloat
    ): ReconciliationResult {
        $expectedTotal = $this->billingRepo->getSessionTotal($cashierId);
        $reportedTotal = array_sum($collectionsByMode);
        $discrepancy = abs($expectedTotal - $reportedTotal);

        $reconciliation = $this->billingRepo->createReconciliation([
            'cashier_id'          => $cashierId,
            'opening_float'       => $openingFloat,
            'collections_by_mode' => $collectionsByMode,
            'total_collections'   => $reportedTotal,
            'banking_amount'      => $bankingAmount,
            'closing_float'       => $closingFloat,
            'expected_total'      => $expectedTotal,
            'discrepancy'         => $discrepancy,
            'flagged'             => $discrepancy > 5000,
            'session_ended_at'    => now(),
        ]);

        return new ReconciliationResult($reconciliation);
    }
}
```

#### 4.5.2 MobileMoneyService

```php
final class MobileMoneyService
{
    public function __construct(
        private readonly MobileMoneyRepository $momoRepo,
        private readonly BillingService $billing,
        private readonly HttpClient $httpClient,
    ) {}

    /**
     * Initiate a MoMo/Airtel Money payment (FR-BIL-007).
     * Sends a payment prompt to the patient's phone via the provider API.
     */
    public function initiateMoMoPayment(
        string $patientUid,
        string $phoneNumber,
        int $amount,
        string $provider
    ): MobileMoneyRequest {
        $referenceId = Str::uuid()->toString();

        $apiResponse = $this->httpClient->post(
            $this->getApiUrl($provider),
            [
                'phone'     => $phoneNumber,
                'amount'    => $amount,
                'currency'  => 'UGX',
                'reference' => $referenceId,
                'callback'  => route('api.v1.momo.callback'),
                'reason'    => 'Medical bill payment',
            ]
        );

        return $this->momoRepo->create([
            'patient_uid'  => $patientUid,
            'phone_number' => $phoneNumber,
            'amount'       => $amount,
            'provider'     => $provider,
            'reference_id' => $referenceId,
            'status'       => 'pending',
            'initiated_at' => now(),
        ]);
    }

    /**
     * Process payment callback from MoMo/Airtel API (FR-BIL-007).
     * Auto-matches to patient account. Unmatched payments go to suspense (BR-FIN-003).
     */
    public function verifyPayment(string $referenceId, string $transactionId, string $status): void
    {
        $request = $this->momoRepo->findByReference($referenceId);

        if ($request === null) {
            $this->momoRepo->createSuspenseEntry($referenceId, $transactionId, $status);
            return;
        }

        if ($status === 'successful') {
            $this->momoRepo->update($request->id, [
                'status'         => 'completed',
                'transaction_id' => $transactionId,
                'completed_at'   => now(),
            ]);

            $this->billing->collectPayment(
                patientUid:    $request->patient_uid,
                amount:        $request->amount,
                paymentMethod: $request->provider,
                cashierId:     0, // System-initiated
            );
        } else {
            $this->momoRepo->update($request->id, [
                'status'    => 'failed',
                'failed_at' => now(),
            ]);
        }
    }

    /**
     * Daily reconciliation of unmatched MoMo payments (BR-FIN-003).
     * Payments in suspense for > 48 hours are flagged for manual review.
     */
    public function reconcileUnmatched(): UnmatchedPaymentReport
    {
        return new UnmatchedPaymentReport(
            $this->momoRepo->getUnmatchedPayments()
        );
    }
}
```

---

### 4.6 Appointment Module

**Files:**
- `AppointmentController` — booking, cancellation, rescheduling, check-in
- `ScheduleController` — doctor availability management
- `AppointmentService` — booking logic, conflict detection, queue conversion
- `ReminderService` — SMS/WhatsApp reminder dispatch
- `AppointmentRepository`, `ScheduleRepository`
- `BookAppointmentRequest` — validation
- `SendAppointmentReminderJob` — scheduled 24h before appointment

#### 4.6.1 AppointmentService

```php
final class AppointmentService
{
    public function __construct(
        private readonly AppointmentRepository $appointmentRepo,
        private readonly ScheduleRepository $scheduleRepo,
        private readonly ReminderService $reminderService,
        private readonly SMSService $sms,
    ) {}

    /**
     * Book an appointment (FR-APT-001).
     * Checks doctor availability and suggests alternatives on conflict.
     *
     * @throws SlotUnavailableException  Includes next 3 available slots
     */
    public function book(
        string $patientUid,
        string $department,
        ?int $doctorId,
        Carbon $appointmentDate,
        string $appointmentType
    ): Appointment {
        // Check availability (FR-APT-003)
        if ($doctorId !== null) {
            $isAvailable = $this->scheduleRepo->isSlotAvailable($doctorId, $appointmentDate);

            if (!$isAvailable) {
                $alternatives = $this->scheduleRepo->getNextAvailableSlots($doctorId, $appointmentDate, count: 3);
                throw new SlotUnavailableException($alternatives);
            }
        }

        $appointment = $this->appointmentRepo->create([
            'patient_uid'      => $patientUid,
            'department'       => $department,
            'doctor_id'        => $doctorId,
            'appointment_date' => $appointmentDate,
            'appointment_type' => $appointmentType,
            'status'           => 'booked',
            'booked_at'        => now(),
        ]);

        // Send SMS confirmation
        $patient = app(PatientRepository::class)->findByUid($patientUid);
        if ($patient->contact_phone) {
            $this->sms->send($patient->contact_phone, sprintf(
                'Appointment confirmed at %s on %s. Ref: %s',
                app('facility_name'),
                $appointmentDate->format('d M Y H:i'),
                $appointment->id
            ));
        }

        // Schedule 24h SMS reminder (FR-APT-002)
        SendAppointmentReminderJob::dispatch($appointment->id)
            ->delay($appointmentDate->copy()->subHours(24));

        event(new AppointmentBooked(
            appointmentId: $appointment->id,
            patientUid:    $patientUid,
            doctorId:      $doctorId,
            datetime:      $appointmentDate,
        ));

        return $appointment;
    }

    /**
     * Cancel an appointment (FR-APT-001).
     */
    public function cancel(int $appointmentId, string $reason): void
    {
        $this->appointmentRepo->update($appointmentId, [
            'status'           => 'cancelled',
            'cancellation_reason' => $reason,
            'cancelled_at'     => now(),
        ]);

        event(new AppointmentCancelled(
            appointmentId: $appointmentId,
            reason:        $reason,
        ));
    }

    /**
     * Reschedule an appointment.
     * Cancels the old appointment and books a new one.
     */
    public function reschedule(int $appointmentId, Carbon $newDate): Appointment
    {
        $old = $this->appointmentRepo->findOrFail($appointmentId);
        $this->cancel($appointmentId, 'Rescheduled');

        return $this->book(
            patientUid:      $old->patient_uid,
            department:      $old->department,
            doctorId:        $old->doctor_id,
            appointmentDate: $newDate,
            appointmentType: $old->appointment_type,
        );
    }

    /**
     * Convert appointment to OPD queue entry on patient arrival (FR-APT-004).
     * Patient is added to triage queue with appointment time as a priority factor.
     */
    public function convertToQueue(int $appointmentId): void
    {
        $this->appointmentRepo->update($appointmentId, [
            'status'     => 'arrived',
            'arrived_at' => now(),
        ]);

        $appointment = $this->appointmentRepo->findOrFail($appointmentId);

        app(TriageQueueRepository::class)->enqueueFromAppointment(
            $appointment->patient_uid,
            $appointment->appointment_date,
        );
    }
}
```

#### 4.6.2 ReminderService

```php
final class ReminderService
{
    public function __construct(
        private readonly SMSService $sms,
        private readonly AppointmentRepository $appointmentRepo,
    ) {}

    /**
     * Send an SMS/WhatsApp reminder 24 hours before appointment (FR-APT-002).
     * Called by SendAppointmentReminderJob.
     */
    public function sendSMSReminder(int $appointmentId): void
    {
        $appointment = $this->appointmentRepo->findOrFail($appointmentId);

        if ($appointment->status !== 'booked') {
            return; // Cancelled or already arrived
        }

        $patient = app(PatientRepository::class)->findByUid($appointment->patient_uid);

        if ($patient->contact_phone === null) {
            return;
        }

        $doctorName = $appointment->doctor?->full_name ?? 'your doctor';

        $this->sms->send($patient->contact_phone, sprintf(
            'Reminder: Your appointment at %s with Dr %s is tomorrow at %s. Reply 1 to confirm, 2 to cancel.',
            app('facility_name'),
            $doctorName,
            $appointment->appointment_date->format('h:i A')
        ));
    }
}
```

---

### 4.7 RBAC Module

**Files:**
- `RoleController` — role CRUD, permission assignment
- `AuditController` — audit trail queries
- `EmergencyAccessController` — break-the-glass, cross-facility access
- `PermissionService` — RBAC + ABAC resolution
- `AuditService` — immutable audit logging, trail queries
- `EmergencyAccessService` — cross-facility record access, break-the-glass
- `RoleRepository`, `AuditRepository`, `EmergencyAccessRepository`
- `CreateRoleRequest`, `BreakTheGlassRequest` — validation

#### 4.7.1 PermissionService

```php
final class PermissionService
{
    public function __construct(
        private readonly RoleRepository $roleRepo,
    ) {}

    /**
     * Resolve all permissions for a user based on their assigned role (FR-RBAC-001).
     * Merges built-in role permissions with any custom role permissions.
     */
    public function resolvePermissions(int $userId): PermissionSet
    {
        $roles = $this->roleRepo->getRolesForUser($userId);
        $permissions = new PermissionSet();

        foreach ($roles as $role) {
            $permissions->merge($role->permissions);
        }

        return $permissions;
    }

    /**
     * Check if the user has a specific permission.
     */
    public function hasPermission(int $userId, string $permission): bool
    {
        return $this->resolvePermissions($userId)->contains($permission);
    }

    /**
     * Attribute-Based Access Control for sensitive records (FR-RBAC-003).
     * Checks whether the clinician is the treating provider or has patient consent.
     *
     * @return bool True if access is granted
     */
    public function checkABAC(
        int $userId,
        string $patientUid,
        string $recordCategory
    ): bool {
        // Check if user is the treating clinician
        $isTreatingClinician = $this->roleRepo->isTreatingClinician($userId, $patientUid);
        if ($isTreatingClinician) {
            return true;
        }

        // Check for explicit patient consent
        $hasConsent = $this->roleRepo->hasPatientConsent($userId, $patientUid, $recordCategory);
        if ($hasConsent) {
            return true;
        }

        return false;
    }
}
```

#### 4.7.2 AuditService

```php
final class AuditService
{
    public function __construct(
        private readonly AuditRepository $auditRepo,
    ) {}

    /**
     * Write an immutable audit log entry (FR-RBAC-005).
     * Entries cannot be modified or deleted by any user, including Super Admin.
     * Enforced by database trigger at the MySQL level.
     */
    public function log(
        string $action,
        string $resourceType,
        string $resourceId,
        ?array $oldValue = null,
        ?array $newValue = null,
        ?array $metadata = null
    ): void {
        $this->auditRepo->insert([
            'user_id'       => auth()->id(),
            'facility_id'   => app('facility_id'),
            'action'        => $action,
            'resource_type' => $resourceType,
            'resource_id'   => $resourceId,
            'old_value'     => $oldValue ? json_encode($oldValue) : null,
            'new_value'     => $newValue ? json_encode($newValue) : null,
            'metadata'      => $metadata ? json_encode($metadata) : null,
            'ip_address'    => request()->ip(),
            'user_agent'    => request()->userAgent(),
            'created_at'    => now(),
        ]);
    }

    /**
     * Query the audit trail with filters (FR-RBAC-005).
     * Available to Facility Admin and Auditor roles only.
     */
    public function getTrail(
        ?int $userId = null,
        ?Carbon $from = null,
        ?Carbon $to = null,
        ?string $action = null,
        ?string $resourceType = null
    ): LengthAwarePaginator {
        return $this->auditRepo->query(
            userId:       $userId,
            from:         $from,
            to:           $to,
            action:       $action,
            resourceType: $resourceType,
        );
    }

    /**
     * Detect anomalous access patterns.
     * Flags: bulk record access, after-hours access, unusual geographic origin.
     */
    public function detectAnomaly(int $userId): AnomalyReport
    {
        $recentActions = $this->auditRepo->getRecentActions($userId, hours: 1);
        $anomalies = [];

        // Bulk access: > 50 patient records viewed in 1 hour
        $viewCount = $recentActions->where('action', 'VIEW')->count();
        if ($viewCount > 50) {
            $anomalies[] = new Anomaly('BULK_ACCESS', "User viewed {$viewCount} records in 1 hour");
        }

        return new AnomalyReport($anomalies);
    }
}
```

#### 4.7.3 EmergencyAccessService

```php
final class EmergencyAccessService
{
    public function __construct(
        private readonly EmergencyAccessRepository $emergencyRepo,
        private readonly GlobalPatientRepository $globalPatientRepo,
        private readonly AuditService $audit,
        private readonly SMSService $sms,
        private readonly NotificationService $notifications,
    ) {}

    /**
     * Request break-the-glass access to a restricted record (FR-RBAC-007).
     * Requires mandatory reason (min 20 chars).
     * Grants temporary read-only access. Notifies Facility Admin.
     */
    public function requestBreakTheGlass(
        int $clinicianId,
        string $patientUid,
        string $reason
    ): EmergencyAccess {
        if (strlen($reason) < 20) {
            throw new InsufficientReasonException('Reason must be at least 20 characters.');
        }

        $access = $this->emergencyRepo->create([
            'clinician_id' => $clinicianId,
            'patient_uid'  => $patientUid,
            'reason'       => $reason,
            'access_type'  => 'break_the_glass',
            'granted_at'   => now(),
            'expires_at'   => now()->addHours(24),
        ]);

        $this->audit->log(
            action:       'BREAK_THE_GLASS',
            resourceType: 'patient',
            resourceId:   $patientUid,
            metadata:     ['reason' => $reason, 'clinician_id' => $clinicianId],
        );

        $this->notifications->sendToRole('facility_admin', [
            'type'    => 'break_the_glass',
            'message' => "Break-the-glass access invoked by clinician #{$clinicianId} for patient {$patientUid}. Reason: {$reason}",
            'urgency' => 'high',
        ]);

        event(new EmergencyAccessInvoked(
            clinicianId: $clinicianId,
            patientUid:  $patientUid,
            facilityId:  app('facility_id'),
            reason:      $reason,
        ));

        return $access;
    }

    /**
     * Cross-facility emergency access with two-factor patient confirmation (FR-RBAC-006, BR-DATA-002).
     * Reveals limited clinical data: allergies, current medications, blood group,
     * HIV status (only if prior consent), and last 3 diagnoses.
     * Sends SMS notification to patient. Expires after 24 hours.
     */
    public function requestCrossFacilityAccess(
        int $clinicianId,
        string $patientName,
        string $dateOfBirth,
        string $reason
    ): CrossFacilityAccessResult {
        // Two-factor patient confirmation
        $patient = $this->globalPatientRepo->findByNameAndDob($patientName, $dateOfBirth);

        if ($patient === null) {
            throw new PatientVerificationFailedException();
        }

        $access = $this->emergencyRepo->create([
            'clinician_id' => $clinicianId,
            'patient_uid'  => $patient->patient_uid,
            'reason'       => $reason,
            'access_type'  => 'cross_facility',
            'granted_at'   => now(),
            'expires_at'   => now()->addHours(24),
        ]);

        // Retrieve limited clinical data (BR-DATA-002)
        $limitedData = $this->globalPatientRepo->getLimitedClinicalData(
            $patient->patient_uid,
            fields: ['allergies', 'current_medications', 'blood_group', 'last_3_diagnoses'],
            includeHiv: $patient->hiv_consent_given,
        );

        // SMS notification to patient
        if ($patient->contact_phone) {
            $this->sms->send($patient->contact_phone, sprintf(
                'Your medical records were accessed at %s on %s for emergency care.',
                app('facility_name'),
                now()->format('d M Y')
            ));
        }

        $this->audit->log(
            action:       'CROSS_FACILITY_ACCESS',
            resourceType: 'patient',
            resourceId:   $patient->patient_uid,
            metadata:     ['reason' => $reason, 'clinician_id' => $clinicianId],
        );

        return new CrossFacilityAccessResult($access, $limitedData);
    }

    /**
     * Validate that a clinician's emergency access has not expired.
     */
    public function validateReason(int $accessId): bool
    {
        $access = $this->emergencyRepo->findOrFail($accessId);
        return $access->expires_at->isFuture();
    }
}
```

---

## 5. Cross-Cutting Concerns

### 5.1 Auto-Save (BR-DATA-005)

**Class:** `App\Services\Infrastructure\FormStateService`

Clinical form data is auto-saved to `localStorage` on every input interaction to protect against power failure. The implementation is client-side JavaScript, with the service providing the server-side recovery endpoint.

```php
final class FormStateService
{
    /**
     * Recover auto-saved form state for a specific form and user context.
     * Called on page load to restore unsaved work after interruption.
     */
    public function recover(
        int $userId,
        string $formType,
        ?string $patientUid = null
    ): ?array {
        return Cache::get("form_state:{$userId}:{$formType}:{$patientUid}");
    }

    /**
     * Persist form state server-side (backup for localStorage).
     * Called periodically by AJAX from the client.
     */
    public function persist(
        int $userId,
        string $formType,
        ?string $patientUid,
        array $data
    ): void {
        Cache::put(
            "form_state:{$userId}:{$formType}:{$patientUid}",
            $data,
            now()->addHours(24)
        );
    }

    /**
     * Clear form state after successful submission.
     */
    public function clear(int $userId, string $formType, ?string $patientUid): void
    {
        Cache::forget("form_state:{$userId}:{$formType}:{$patientUid}");
    }
}
```

### 5.2 Task Resumption

**Class:** `App\Services\Infrastructure\ResumeService`

Bookmarks the user's current form position (active tab, scroll offset, last-focused field) so that interrupted clinical workflows can be resumed exactly where the clinician left off.

```php
final class ResumeService
{
    public function bookmark(int $userId, string $context, array $position): void
    {
        Cache::put("resume:{$userId}:{$context}", $position, now()->addHours(8));
    }

    public function getBookmark(int $userId, string $context): ?array
    {
        return Cache::get("resume:{$userId}:{$context}");
    }

    public function clearBookmark(int $userId, string $context): void
    {
        Cache::forget("resume:{$userId}:{$context}");
    }
}
```

### 5.3 Offline Queue and Sync

**Class:** `App\Services\Infrastructure\SyncQueueService`

Manages the local-to-server synchronisation queue for offline-first operation. Clinical data entered offline is queued in the Room database (Android) or Core Data (iOS) and synced when connectivity resumes. Conflict resolution follows BR-DATA-003: last-write-wins for non-clinical fields; both versions preserved for clinical fields.

```php
final class SyncQueueService
{
    public function __construct(
        private readonly SyncQueueRepository $syncRepo,
        private readonly AuditService $audit,
    ) {}

    /**
     * Process inbound sync queue from a mobile device.
     * Applies field-level merge with conflict detection (BR-DATA-003).
     *
     * @param SyncPayload[] $payloads Array of queued operations from the device
     * @return SyncResult Merged results with conflict log
     */
    public function processSyncQueue(array $payloads, string $deviceId): SyncResult
    {
        $conflicts = [];
        $applied = 0;

        foreach ($payloads as $payload) {
            $serverRecord = $this->syncRepo->findByResourceId(
                $payload->resourceType,
                $payload->resourceId,
            );

            if ($serverRecord === null) {
                // New record — apply directly
                $this->syncRepo->applyCreate($payload);
                $applied++;
                continue;
            }

            // Detect conflicts: server updated after device's last sync timestamp
            if ($serverRecord->updated_at > $payload->deviceTimestamp) {
                $fieldConflicts = $this->detectFieldConflicts($serverRecord, $payload);

                foreach ($fieldConflicts as $field => $conflict) {
                    if ($this->isClinicalField($field)) {
                        // Preserve both versions for clinician review (BR-DATA-003)
                        $conflicts[] = new SyncConflict(
                            resourceType: $payload->resourceType,
                            resourceId:   $payload->resourceId,
                            field:        $field,
                            serverValue:  $conflict['server'],
                            deviceValue:  $conflict['device'],
                        );
                    } else {
                        // Non-clinical: last-write-wins
                        $this->syncRepo->applyFieldUpdate(
                            $payload->resourceType,
                            $payload->resourceId,
                            $field,
                            $conflict['device'],
                        );
                    }
                }
            } else {
                $this->syncRepo->applyUpdate($payload);
                $applied++;
            }
        }

        return new SyncResult($applied, $conflicts);
    }

    private function isClinicalField(string $field): bool
    {
        return in_array($field, [
            'diagnosis', 'prescription', 'allergy', 'chronic_condition',
            'lab_result', 'clinical_notes', 'vital_signs',
        ], true);
    }
}
```

### 5.4 Missing Charge Detection (BR-FIN-008)

**Job:** `App\Jobs\MissingChargeDetectionJob`

Runs daily at end of business. Compares clinical encounters against billing records and flags gaps.

```php
final class MissingChargeDetectionJob extends TenantAwareJob
{
    protected function execute(): void
    {
        $missingCharges = app(MissingChargeDetectionService::class)->detect();

        if ($missingCharges->isNotEmpty()) {
            app(NotificationService::class)->sendToRole('billing_officer', [
                'type'    => 'missing_charges',
                'message' => "{$missingCharges->count()} clinical encounters found without billing charges.",
                'data'    => $missingCharges->toArray(),
            ]);
        }
    }
}
```

```php
final class MissingChargeDetectionService
{
    public function __construct(
        private readonly BillingRepository $billingRepo,
        private readonly EncounterRepository $encounterRepo,
        private readonly LabRepository $labRepo,
        private readonly PharmacyRepository $pharmacyRepo,
    ) {}

    /**
     * Detect clinical encounters with no corresponding billing charge (BR-FIN-008).
     */
    public function detect(): Collection
    {
        $today = now()->toDateString();

        $unbilledVisits = $this->encounterRepo->getCompletedWithoutCharge($today);
        $unbilledLabs = $this->labRepo->getValidatedWithoutCharge($today);
        $unbilledDispensings = $this->pharmacyRepo->getDispensedWithoutCharge($today);

        return collect()
            ->merge($unbilledVisits->map(fn ($v) => new MissingCharge('OPD_VISIT', $v)))
            ->merge($unbilledLabs->map(fn ($l) => new MissingCharge('LAB_RESULT', $l)))
            ->merge($unbilledDispensings->map(fn ($d) => new MissingCharge('DRUG_DISPENSED', $d)));
    }
}
```

---

## 6. Scheduled Jobs Summary

| Job Class | Schedule | Description |
|---|---|---|
| `CheckExpiryJob` | Daily 06:00 | Flag stock expiring within 90 days; block expired batches (FR-PHR-008) |
| `MissingChargeDetectionJob` | Daily 18:00 | Compare clinical encounters vs billing records (BR-FIN-008) |
| `ReconcileUnmatchedPaymentsJob` | Daily 20:00 | Generate unmatched MoMo payment report (BR-FIN-003) |
| `SendAppointmentReminderJob` | Per-appointment | Send SMS 24h before appointment (FR-APT-002) |
| `EscalateCriticalValueJob` | Per-event (30/60 min delay) | Escalate unacknowledged critical lab values (BR-CLIN-003) |
| `BatchDuplicateScanJob` | Nightly 02:00 | EMPI batch scan for duplicate patient records (FR-REG-009) |

---

## 7. Error Handling Conventions

All service-layer exceptions extend `App\Exceptions\Medic8Exception` and carry a structured error code.

| Exception Class | HTTP Code | Error Code | Triggered By |
|---|---|---|---|
| `DuplicateDetectedException` | 409 | `DUPLICATE_DETECTED` | EMPI confidence > 80% |
| `ContactRequiredException` | 422 | `CONTACT_REQUIRED` | No phone or address |
| `FiveRightsViolationException` | 422 | `FIVE_RIGHTS_VIOLATION` | Dose/route/drug validation |
| `FatalInteractionException` | 422 | `FATAL_INTERACTION` | Tier 4 drug interaction |
| `WeightRequiredException` | 422 | `WEIGHT_REQUIRED` | Paediatric patient, no weight |
| `DecimalErrorSuspectedException` | 422 | `DECIMAL_ERROR_SUSPECTED` | Dose > 10x expected |
| `QcOutOfControlException` | 422 | `QC_OUT_OF_CONTROL` | Assay failed Westgard rules |
| `BatchExpiredException` | 422 | `BATCH_EXPIRED` | Dispensing expired stock |
| `InsufficientStockException` | 422 | `INSUFFICIENT_STOCK` | Stock < requested quantity |
| `SlotUnavailableException` | 409 | `SLOT_UNAVAILABLE` | Doctor slot already booked |
| `UnmergeWindowExpiredException` | 422 | `UNMERGE_WINDOW_EXPIRED` | Merge older than 30 days |
| `InsufficientReasonException` | 422 | `INSUFFICIENT_REASON` | BTG reason < 20 chars |
| `PatientVerificationFailedException` | 403 | `PATIENT_VERIFICATION_FAILED` | Name/DOB mismatch |
| `TenantNotResolvedException` | 403 | `TENANT_NOT_RESOLVED` | No facility_id in context |
| `FatalInteractionCannotBeOverriddenException` | 422 | `FATAL_CANNOT_OVERRIDE` | Tier 4 override attempt |

All exceptions return a consistent JSON envelope:

```json
{
  "error": {
    "code": "FIVE_RIGHTS_VIOLATION",
    "message": "Dose exceeds maximum for Amoxicillin: 5000 mg prescribed, max 3000 mg.",
    "details": {}
  }
}
```
