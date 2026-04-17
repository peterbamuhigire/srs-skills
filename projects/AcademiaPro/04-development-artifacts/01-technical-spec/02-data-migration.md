# Data Migration Specification — Academia Pro Phase 1

**Document ID:** TS-01-02
**Project:** Academia Pro
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Pending Consultant Review
**Gap Resolved:** HIGH-007

---

## 1. Purpose

This specification defines the data import pathway for schools migrating to Academia Pro from spreadsheets (Excel or Google Sheets) or paper-based records. It covers the student roster import wizard available to the Accounts Bursar and School Owner roles during initial school onboarding.

No historical attendance records, historical examination marks, or prior-school fee payment histories are imported. These categories are either impractical to standardise or are superseded by the platform's own data collection from onboarding forward.

---

## 2. Scope

### 2.1 What Is Imported

| Data Category | Included | Notes |
|---|---|---|
| Student personal details (name, DOB, gender) | Yes | Mapped to `global_students` and `school_enrollments` |
| Uganda NIN / LIN identifiers | Yes | Mapped to `student_identifiers` |
| Class assignment | Yes | Must match an existing class in the tenant |
| Local admission number | Yes | School's own numbering |
| Admission date | Yes | Date student first enrolled at this school |
| Guardian name, phone, relationship | Yes | Mapped to `school_enrollments` |
| Current enrollment status | Yes | active / inactive only (no transfers at import time) |

### 2.2 What Is Not Imported

| Data Category | Excluded | Reason |
|---|---|---|
| Historical attendance records | No | Unstandardised formats; platform collects fresh from onboarding |
| Historical examination marks | No | Too varied across curriculum types and school formats |
| Prior-school fee payment history | No | BR-HIST-003: prior school balances do not follow the student |
| Staff / HR records | No | Out of scope for Phase 1 |
| Class schedules (historical) | No | Timetable is configured fresh per academic year |
| Documents and attachments | No | No file import in Phase 1 |

---

## 3. Supported Import Formats

| Format | Extension | Notes |
|---|---|---|
| Microsoft Excel | `.xlsx` | Primary format. Must use the official Academia Pro Student Import Template. |
| Comma-Separated Values | `.csv` | Accepted for schools without Excel access. UTF-8 encoding required. |

JSON and XML import are not supported in Phase 1.

---

## 4. Student Import Template

The template is downloadable from the import wizard. Schools must use the canonical column headers below. Column order in the file does not matter — the importer maps by header name.

### 4.1 Column Definitions

| Column Header | Data Type | Required | Validation Rules |
|---|---|---|---|
| `first_name` | String | Yes | 1–100 characters |
| `last_name` | String | Yes | 1–100 characters |
| `middle_name` | String | No | ≤ 100 characters |
| `date_of_birth` | Date | Yes | Format `YYYY-MM-DD`. Must be a past date. Student must be ≤ 25 years old. |
| `gender` | Enum | Yes | `male` or `female` (case-insensitive) |
| `class_name` | String | Yes | Must exactly match the `name` field of an existing class for this tenant. Case-insensitive. |
| `admission_date` | Date | Yes | Format `YYYY-MM-DD`. Must be ≤ today. |
| `local_admission_number` | String | No | ≤ 50 characters. Auto-generated if blank. Must be unique within the tenant if provided. |
| `nin` | String | No | 14 characters maximum. Alphanumeric. Applied only to students aged 16+. |
| `lin` | String | No | 14 characters maximum. Alphanumeric. |
| `guardian_name` | String | No | ≤ 150 characters |
| `guardian_phone` | String | No | E.164 format (e.g., `+256701234567`). Validated if present. |
| `guardian_relationship` | Enum | No | `father`, `mother`, `guardian`, `other` (case-insensitive) |
| `status` | Enum | No | `active` or `inactive`. Defaults to `active` if blank. |

### 4.2 Row Limits

The importer accepts up to **2,000 rows per file**. Schools with more than 2,000 students must split the import into multiple files by class group. This limit prevents timeout in the synchronous validation phase and ensures the async processing job completes within the platform's 5-minute job timeout.

---

## 5. Import Workflow

The import wizard consists of 4 steps presented in the web UI.

### Step 1 — File Upload

The bursar or school owner navigates to **Settings → Data Import → Student Import** and uploads the completed template file. The wizard accepts `.xlsx` and `.csv` files up to 10 MB. Files exceeding 10 MB are rejected immediately with an error message.

### Step 2 — Synchronous Validation

Upon upload, the system performs column-header detection and row-level validation synchronously before queuing the import job. Validation checks for:

1. Required columns present.
2. No extra unrecognised columns (warning, not error — unknown columns are ignored).
3. `class_name` values match existing tenant classes.
4. Date formats are valid.
5. `nin` and `lin` values pass format checks.
6. `guardian_phone` values pass E.164 format check.
7. `local_admission_number` values are unique within the file and within the tenant.

If any of checks 1–7 fail, the wizard halts and presents a validation error summary. The file is not queued. The user corrects the file and re-uploads.

### Step 3 — Async Import Job

Once validation passes, the file is handed to a Laravel queued job (`ImportStudentsJob`) that processes rows in batches of 100. For each row the job:

1. Checks `global_students` by NIN or LIN (if provided). If a match is found, the existing `student_uid` is reused (BR-STU-001). If no match, a new `global_students` record is created with a new UUID.
2. Checks that the student does not already have an active enrollment at another school (BR-STU-004). If a conflict exists, the row is skipped and logged as a conflict error.
3. Creates a `school_enrollments` record linked to the `student_uid`.
4. Creates a `student_identifiers` record for NIN and/or LIN if provided.

The job uses **skip-and-report mode**: rows that fail processing are recorded in the import error log and skipped. The job continues processing remaining rows. This prevents a single bad row from blocking the entire import.

### Step 4 — Import Report

When the job completes, the wizard displays the import summary:

- Total rows in file
- Rows imported successfully
- Rows skipped (with downloadable error CSV)
- Rows with warnings (e.g., NIN/LIN matched a student with an active enrollment elsewhere)

The error CSV uses the same column headers as the import template, with an additional `error_reason` column. The bursar can correct the skipped rows and re-import.

---

## 6. Validation Error Reference

| Error Code | Trigger Condition | User Action |
|---|---|---|
| `MISSING_REQUIRED_COLUMN` | A required column header is absent from the file. | Add the missing column to the file. |
| `INVALID_DATE_FORMAT` | A date cell is not in `YYYY-MM-DD` format. | Correct the date values. Excel date serial numbers are auto-converted. |
| `CLASS_NOT_FOUND` | `class_name` does not match any active class for the tenant. | Create the class first via Academics Setup, or correct the spelling. |
| `DUPLICATE_ADMISSION_NUMBER` | `local_admission_number` appears more than once in the file or already exists in the tenant. | Remove the duplicate or leave the field blank for auto-generation. |
| `INVALID_PHONE_FORMAT` | `guardian_phone` is not valid E.164 format. | Correct the phone number or leave blank. |
| `ALREADY_ENROLLED_ELSEWHERE` | A student matched via NIN/LIN already has an active enrollment at another school (BR-STU-004). | Contact the other school to transfer the student out before importing. |
| `INVALID_GENDER` | `gender` is not `male` or `female`. | Correct the value. |
| `INVALID_STATUS` | `status` is not `active` or `inactive`. | Correct the value or leave blank (defaults to `active`). |
| `ROW_LIMIT_EXCEEDED` | File contains more than 2,000 data rows. | Split the file into multiple smaller files. |
| `FILE_TOO_LARGE` | File exceeds 10 MB. | Reduce file size or split into multiple files. |

---

## 7. NIN / LIN Cross-School Matching

The importer applies the global identity lookup defined in BR-STU-001 and BR-STU-002:

1. If `nin` is provided: query `student_identifiers` where `identifier_type = NIN` and `value = <nin>`. If a match is found, link the existing `student_uid`.
2. If `nin` is absent but `lin` is provided: query by `identifier_type = LIN`.
3. If both are absent: no cross-school lookup is performed. A new `global_students` record is created. The student can be linked to an existing global identity later via manual NIN/LIN assignment.

If a NIN/LIN match is found but the matched student has `global_students.status = deceased`, the row is skipped with error `STUDENT_DECEASED`.

---

## 8. Fee History Handling

Historical fee payments from prior years or prior schools are not imported. The reason is threefold:

1. BR-HIST-003: outstanding balances at prior schools do not follow the student.
2. Prior school fee records do not conform to the Academia Pro fee structure schema (class × term × line item).
3. Importing unverified historical payments could corrupt reconciliation reports.

Schools wishing to document prior-period payments may record them manually via the Fees → Record Payment screen, using the `note` field to indicate the historical period.

---

## 9. Audit and Logging

Every import job creates an `import_jobs` record with:

- `tenant_id`
- `initiated_by_user_id`
- `file_name`
- `row_count`
- `success_count`
- `skip_count`
- `status` (queued / processing / complete / failed)
- `started_at`
- `completed_at`

Every row-level outcome (success or skip) is recorded in `import_job_rows` for audit purposes. The import event is written to `audit_logs` with `action = STUDENT_IMPORT_COMPLETED`.

---

## 10. Implementation Notes for Development

### 10.1 Job Configuration

```php
// app/Jobs/ImportStudentsJob.php
class ImportStudentsJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $timeout = 300; // 5 minutes
    public int $tries   = 1;   // No retries — idempotency is per-job, not per-row

    protected int $tenantId;
    protected string $importFilePath;
    protected int $importJobId;

    public function __construct(int $tenantId, string $importFilePath, int $importJobId)
    {
        $this->tenantId      = $tenantId;
        $this->importFilePath = $importFilePath;
        $this->importJobId   = $importJobId;
    }
}
```

### 10.2 Batch Processing

Process rows in batches of 100 using `LazyCollection` to avoid loading the entire file into memory:

```php
// Pseudo-code — actual implementation uses PhpSpreadsheet or league/csv
foreach ($rows->chunk(100) as $batch) {
    foreach ($batch as $rowIndex => $row) {
        $this->processRow($rowIndex, $row);
    }
    // Flush import_job_rows insert for this batch
}
```

### 10.3 Excel Date Handling

Excel stores dates as integer serial numbers (days since 1900-01-01). PhpSpreadsheet automatically converts these to `DateTime` objects when reading `.xlsx` files. The importer must call `\PhpOffice\PhpSpreadsheet\Shared\Date::excelToDateTimeObject()` for cells detected as numeric in date columns. CSV files always receive string values and are parsed with `Carbon::createFromFormat('Y-m-d', $value)`.

### 10.4 Atomic Global Student Creation

When creating a new `global_students` record, use a database transaction with a `SELECT ... FOR UPDATE` lock on the `student_identifiers` table by NIN/LIN to prevent duplicate UUID creation under concurrent imports:

```php
DB::transaction(function () use ($nin, $lin) {
    $existing = DB::table('student_identifiers')
        ->where('identifier_type', 'NIN')
        ->where('value', $nin)
        ->lockForUpdate()
        ->first();

    if ($existing) {
        return $existing->student_uid;
    }
    // Create new global_students record
});
```
