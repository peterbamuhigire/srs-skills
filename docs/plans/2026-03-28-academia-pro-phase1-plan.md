# Academia Pro — Phase 1 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a fully functional multi-tenant SaaS school management web application covering all Starter-tier modules, plus basic scaffolds for the Super Admin, Owner, Student, and Parent portals — sufficient for the first paying school to use the system through a complete school term.

**Architecture:** PHP 8.2+ Service/Repository pattern on MySQL 8.x. Row-level multi-tenancy enforced via `tenant_id` on every table. Global student identity layer (global_students + student_identifiers + school_enrollments) with no tenant_id on identity tables. JWT for API auth; session for web portals. SchoolPay API integration as primary payment channel.

**Tech Stack:** PHP 8.2+, MySQL 8.x, Tabler UI / Bootstrap 5, Alpine.js, mPDF, Africa's Talking SMS, SchoolPay API, Anthropic Claude API (for AI stubs), JWT, bcrypt

---

### Task 1: Project Bootstrapping & Database Foundation

**Files:**
- Create: `src/bootstrap.php`
- Create: `src/Config/Database.php`
- Create: `src/Config/App.php`
- Create: `database/migrations/001_create_tenants.sql`
- Create: `database/migrations/002_create_global_identity.sql`
- Create: `database/migrations/003_create_users_roles.sql`
- Create: `database/seeds/001_seed_super_admin.sql`
- Create: `public/index.php`
- Create: `.env.example`
- Test: `tests/Unit/Config/DatabaseTest.php`

**Step 1: Write the failing test**
```php
// tests/Unit/Config/DatabaseTest.php
class DatabaseTest extends TestCase {
    public function test_connection_uses_tenant_id(): void {
        $db = new Database(getenv('DB_DSN'));
        $this->assertInstanceOf(PDO::class, $db->connection());
    }
}
```

**Step 2:** Run `composer test tests/Unit/Config/DatabaseTest.php` — expect FAIL.

**Step 3: Create migrations**

`database/migrations/001_create_tenants.sql`:
```sql
CREATE TABLE tenants (
    tenant_id     INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    school_name   VARCHAR(200) NOT NULL,
    subdomain     VARCHAR(100) NOT NULL UNIQUE,
    plan          ENUM('starter','growth','pro') DEFAULT 'starter',
    status        ENUM('active','suspended','trial') DEFAULT 'trial',
    country_code  CHAR(2) DEFAULT 'UG',
    currency      CHAR(3) DEFAULT 'UGX',
    timezone      VARCHAR(50) DEFAULT 'Africa/Kampala',
    created_at    DATETIME DEFAULT NOW(),
    updated_at    DATETIME ON UPDATE NOW()
) ENGINE=InnoDB;
```

`database/migrations/002_create_global_identity.sql`:
```sql
CREATE TABLE global_students (
    student_uid   CHAR(36) PRIMARY KEY,
    full_name     VARCHAR(150) NOT NULL,
    date_of_birth DATE,
    gender        ENUM('M','F','Other'),
    photo_url     VARCHAR(500),
    deleted_at    DATETIME,
    created_at    DATETIME DEFAULT NOW(),
    updated_at    DATETIME ON UPDATE NOW()
) ENGINE=InnoDB;

CREATE TABLE student_identifiers (
    id            BIGINT AUTO_INCREMENT PRIMARY KEY,
    student_uid   CHAR(36) NOT NULL,
    id_type       ENUM('nin','phone','email','passport','birth_cert','lin') NOT NULL,
    id_value      VARCHAR(200) NOT NULL,
    verified      TINYINT(1) DEFAULT 0,
    added_at      DATETIME DEFAULT NOW(),
    UNIQUE KEY uq_identifier (id_type, id_value),
    FOREIGN KEY (student_uid) REFERENCES global_students(student_uid)
) ENGINE=InnoDB;

CREATE TABLE school_enrollments (
    enrollment_id       CHAR(36) PRIMARY KEY,
    student_uid         CHAR(36) NOT NULL,
    tenant_id           INT UNSIGNED NOT NULL,
    local_admission_no  VARCHAR(50),
    local_name_override VARCHAR(150),
    admission_date      DATE NOT NULL,
    leaving_date        DATE,
    status              ENUM('active','left','transferred','completed','suspended') DEFAULT 'active',
    class_id            INT UNSIGNED,
    section_id          INT UNSIGNED,
    academic_session    VARCHAR(20),
    previous_school     VARCHAR(200),
    previous_class      VARCHAR(100),
    created_at          DATETIME DEFAULT NOW(),
    UNIQUE KEY uq_enrollment (student_uid, tenant_id, academic_session),
    FOREIGN KEY (student_uid) REFERENCES global_students(student_uid),
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
) ENGINE=InnoDB;
```

**Step 4:** Run `php database/migrate.php` — expect all tables created.

**Step 5: Commit**
```bash
git add database/ src/Config/ public/ .env.example
git commit -m "feat: bootstrap project with tenants and global identity schema"
```

---

### Task 2: Authentication, RBAC & Multi-Tenancy Middleware

**Files:**
- Create: `src/Auth/JwtService.php`
- Create: `src/Auth/SessionAuth.php`
- Create: `src/Middleware/TenantMiddleware.php`
- Create: `src/Middleware/AuthMiddleware.php`
- Create: `database/migrations/004_create_auth_tables.sql`
- Test: `tests/Unit/Auth/JwtServiceTest.php`
- Test: `tests/Unit/Middleware/TenantMiddlewareTest.php`

**Step 1: Write failing tests**
```php
// tests/Unit/Auth/JwtServiceTest.php
public function test_token_includes_tenant_id(): void {
    $jwt = new JwtService('secret');
    $token = $jwt->generate(['user_id' => 1, 'tenant_id' => 5, 'role' => 'admin']);
    $payload = $jwt->verify($token);
    $this->assertEquals(5, $payload['tenant_id']);
}

public function test_tenant_middleware_blocks_cross_tenant_access(): void {
    $middleware = new TenantMiddleware();
    $request = new Request(['tenant_id' => 1]);
    $token_payload = ['tenant_id' => 2];
    $this->expectException(UnauthorizedException::class);
    $middleware->handle($request, $token_payload);
}
```

**Step 2:** Run tests — expect FAIL.

**Step 3: Auth tables migration**
```sql
-- database/migrations/004_create_auth_tables.sql
CREATE TABLE roles (
    role_id     INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tenant_id   INT UNSIGNED NOT NULL,  -- 0 = platform-wide role
    role_name   VARCHAR(100) NOT NULL,
    is_system   TINYINT(1) DEFAULT 0,
    INDEX idx_tenant (tenant_id)
) ENGINE=InnoDB;

CREATE TABLE users (
    user_id       INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tenant_id     INT UNSIGNED NOT NULL,
    role_id       INT UNSIGNED NOT NULL,
    full_name     VARCHAR(150) NOT NULL,
    email         VARCHAR(200) UNIQUE,
    phone         VARCHAR(20),
    password_hash VARCHAR(255) NOT NULL,
    status        ENUM('active','inactive','suspended') DEFAULT 'active',
    last_login    DATETIME,
    created_at    DATETIME DEFAULT NOW(),
    INDEX idx_tenant_role (tenant_id, role_id),
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
) ENGINE=InnoDB;

CREATE TABLE permissions (
    permission_id   INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    role_id         INT UNSIGNED NOT NULL,
    module          VARCHAR(100) NOT NULL,
    action          ENUM('view','create','edit','delete','approve','export') NOT NULL,
    UNIQUE KEY uq_role_perm (role_id, module, action),
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
) ENGINE=InnoDB;
```

**Step 4:** Implement TenantMiddleware — enforce that every query WHERE clause includes `tenant_id = :tenant_id`. The service layer repository base class must inject tenant_id automatically.

**Step 5: Commit**
```bash
git add src/Auth/ src/Middleware/ database/migrations/004_create_auth_tables.sql
git commit -m "feat: JWT auth, RBAC, and tenant isolation middleware"
```

---

### Task 3: Student Information Module

**Files:**
- Create: `database/migrations/005_create_student_tables.sql`
- Create: `src/Modules/Students/StudentRepository.php`
- Create: `src/Modules/Students/StudentService.php`
- Create: `src/Modules/Students/StudentController.php`
- Create: `resources/views/students/index.blade.php`
- Create: `resources/views/students/admission-form.blade.php`
- Test: `tests/Integration/Students/StudentServiceTest.php`

**Key schema:**
```sql
CREATE TABLE students (
    id                  BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    enrollment_id       CHAR(36) NOT NULL,
    tenant_id           INT UNSIGNED NOT NULL,
    -- 40+ admission fields
    first_name          VARCHAR(100) NOT NULL,
    last_name           VARCHAR(100) NOT NULL,
    date_of_birth       DATE,
    gender              ENUM('M','F'),
    nationality         ENUM('Ugandan','Foreign','Refugee') DEFAULT 'Ugandan',
    nin                 VARCHAR(20),   -- National ID Number
    lin                 VARCHAR(20),   -- Learner ID Number (EMIS)
    district_of_birth   VARCHAR(100),
    district_of_residence VARCHAR(100),
    sub_county          VARCHAR(100),
    category            ENUM('day','boarder','special_needs') DEFAULT 'day',
    house               VARCHAR(100),
    orphan_status       ENUM('both_parents','single_parent','orphan'),
    previous_school     VARCHAR(200),
    previous_class      VARCHAR(100),
    -- Guardian info
    guardian_name       VARCHAR(150),
    guardian_phone      VARCHAR(20),
    guardian_email      VARCHAR(200),
    guardian_relation   VARCHAR(50),
    guardian_nin        VARCHAR(20),
    -- Status
    status              ENUM('active','inactive','left','graduated') DEFAULT 'active',
    disable_reason      VARCHAR(500),
    admission_date      DATE,
    leaving_date        DATE,
    created_at          DATETIME DEFAULT NOW(),
    INDEX idx_tenant (tenant_id),
    INDEX idx_enrollment (enrollment_id),
    FOREIGN KEY (enrollment_id) REFERENCES school_enrollments(enrollment_id),
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
) ENGINE=InnoDB;
```

**Critical rule:** Every StudentRepository method MUST include `AND tenant_id = :tenant_id` in every WHERE clause. The base Repository class enforces this via a protected `$tenantId` property set at construction time from the JWT payload.

**Test:**
```php
public function test_student_belongs_to_correct_tenant(): void {
    $service = new StudentService($this->db, tenantId: 1);
    $student = $service->findById(studentId: 999);
    // student 999 belongs to tenant 2 — must throw
    $this->assertNull($student);
}
```

**Step 5: Commit**
```bash
git commit -m "feat: student information module with 40-field admission form and tenant isolation"
```

---

### Task 4: Academics Setup Module

**Files:**
- Create: `database/migrations/006_create_academics_tables.sql`
- Create: `src/Modules/Academics/` (AcademicSessionRepository, ClassRepository, SubjectRepository, TimetableRepository, their Services and Controllers)
- Test: `tests/Integration/Academics/`

**Key tables:** academic_sessions, classes (Baby Class → S6), sections, subjects, subject_groups, class_sections, timetable_slots, teacher_assignments

Pre-seed Uganda class list: Baby Class, Middle Class, Top Class, P1–P7, S1–S4 (UCE), S5–S6 (UACE), plus secondary school technical classes.

Pre-seed Uganda subject list per curriculum level (Thematic P1–P3, Activity-Based P4–P7, Lower Secondary S1–S4, O-Level, A-Level).

**Step 5: Commit**
```bash
git commit -m "feat: academics setup with Uganda pre-configured classes, subjects, and timetable builder"
```

---

### Task 5: Examinations & UNEB Grading Module

**Files:**
- Create: `database/migrations/007_create_examinations_tables.sql`
- Create: `src/Modules/Examinations/` (ExamRepository, MarksRepository, GradingEngineService, ReportCardService, UnebGradingService)
- Create: `src/Modules/Examinations/GradingSchemes/UgandaPleGrading.php`
- Create: `src/Modules/Examinations/GradingSchemes/UgandaUceGrading.php`
- Create: `src/Modules/Examinations/GradingSchemes/UgandaUaceGrading.php`
- Create: `src/Modules/Examinations/GradingSchemes/ThematicGrading.php`
- Test: `tests/Unit/Examinations/GradingEngineTest.php`

**Critical grading tests:**
```php
public function test_ple_aggregate_calculation(): void {
    // P7: 4 subjects, grade 1-4 per subject, aggregate 4-16
    $grading = new UgandaPleGrading();
    $result = $grading->calculate(['English'=>1,'Mathematics'=>2,'Science'=>3,'SST'=>4]);
    $this->assertEquals(10, $result['aggregate']);
    $this->assertEquals('Division 2', $result['division']);
}

public function test_uce_division_classification(): void {
    // O-Level: best 8 subjects, D1=1 to F9=9 points, Division I ≤ 32 points
    $grading = new UgandaUceGrading();
    $subjects = ['Maths'=>1,'English'=>2,'Physics'=>3,'Chemistry'=>3,'Biology'=>4,'History'=>5,'Geography'=>5,'CRE'=>6];
    $result = $grading->calculate($subjects);
    $this->assertEquals('Division I', $result['division']);
}
```

**Report card features:** 5 built-in templates (Nursery, Primary, O-Level, A-Level old/new). Assessment column configuration (weights, max marks). Teacher initials per subject. Promotion settings per class. Configurable grade bands with comment templates. CSV marks import. OCR marks upload (Claude vision API stub — implement fully in Phase 4).

**Step 5: Commit**
```bash
git commit -m "feat: examinations module with UNEB PLE/UCE/UACE grading and report cards"
```

---

### Task 6: Attendance Module

**Files:**
- Create: `database/migrations/008_create_attendance_tables.sql`
- Create: `src/Modules/Attendance/` (AttendanceRepository, AttendanceService, AttendanceController, SmsAlertService stub)
- Test: `tests/Integration/Attendance/AttendanceServiceTest.php`

**Key features:** Mark by class in one screen (present/absent/late/half-day/holiday). Staff attendance separate. SMS alert to parent on absent (Africa's Talking integration — test with sandbox in Phase 1). Term-aware summaries. Gender breakdown for EMIS.

**Step 5: Commit**
```bash
git commit -m "feat: attendance module with parent SMS alerts and term-aware reporting"
```

---

### Task 7: Fees Collection + SchoolPay Integration

**Files:**
- Create: `database/migrations/009_create_fees_tables.sql`
- Create: `src/Modules/Fees/` (FeesTypeRepository, FeesGroupRepository, FeesAssignmentService, FeesCollectionService, FeeReceiptService, MicroPaymentService)
- Create: `src/Integrations/SchoolPay/SchoolPayClient.php`
- Create: `src/Integrations/SchoolPay/SchoolPayWebhookHandler.php`
- Test: `tests/Integration/Fees/FeesCollectionServiceTest.php`
- Test: `tests/Unit/Integrations/SchoolPayClientTest.php`

**SchoolPay integration:**
```php
class SchoolPayClient {
    // Verify student payment code
    public function verifyStudentCode(string $studentCode): array {}
    // Get payment status for a student
    public function getPaymentStatus(string $studentCode, string $term): array {}
    // Register webhook to receive payment notifications
    public function registerWebhook(string $callbackUrl): bool {}
    // Handle incoming payment notification from SchoolPay
    public function handleWebhook(array $payload): PaymentRecord {}
}
```

**Micro-payment rules (KUPAA-derived):**
- No minimum payment floor — UGX 1,000 is valid
- Pre-term payments allocated to upcoming term automatically
- Part-payment receipt generated immediately via SMS
- Running balance visible to parent at all times
- "Do not send home for fees" flag — prevents absent-fees marking

**Test:**
```php
public function test_no_minimum_payment_floor(): void {
    $service = new FeesCollectionService($this->db, tenantId: 1);
    $payment = $service->recordPayment(enrollmentId: 'uuid', amount: 1000, mode: 'cash');
    $this->assertEquals(1000, $payment->amount);
    $this->assertEquals('paid', $payment->status);
}
```

**Step 5: Commit**
```bash
git commit -m "feat: fees collection with SchoolPay integration and KUPAA micro-payment model"
```

---

### Task 8: Front Office, Notice Board, Homework, Download Centre, Calendar, Certificates

**Files:** One migration + service/controller/view set per module.

**Front office:** enquiry log, visitor book, phone log, postal dispatch/receive.
**Notice board:** post with target audience (All/Class/Section/Role), visible across portals, email/SMS send, log.
**Homework:** teacher assigns (file attachment), student submits, teacher evaluates, reports.
**Download centre:** upload file/video, share by class/section/student/all, content types including past UNEB papers.
**Calendar:** annual events, Uganda public holidays pre-loaded, personal to-do, event category colours.
**Certificates & ID cards:** student ID card template (photo, name, class, logo, barcode), certificate templates, TC/leaving certificate, bulk print by class, PDF export.

**Step 5: Commit per module:**
```bash
git commit -m "feat: front office, notice board, homework, download centre, calendar, certificates modules"
```

---

### Task 9: Reports & Analytics Module

**Files:**
- Create: `src/Modules/Reports/ReportBuilder.php`
- Create: `src/Modules/Reports/ReportExporter.php` (PDF via mPDF + Excel/CSV)
- Create: individual report classes for each report type

**Reports to implement:**
- Student: enrollment by class/section/gender/category
- Fees: daily/weekly/monthly/termly totals, per-student statement, outstanding balances
- Attendance: daily, monthly, termly rates; gender breakdown
- Exam: rank report, result summary, mark analysis
- Staff: attendance, payroll summary
- EMIS: enrollment return format (stub — full in Phase 4)

All reports: PDF export + Excel/CSV export.

**Step 5: Commit**
```bash
git commit -m "feat: reports module with PDF and Excel export for all core report types"
```

---

### Task 10: Portal Scaffolds (Super Admin, Owner, Student, Parent)

**Files:**
- Create: `resources/views/portals/super-admin/` (dashboard, school-list, school-detail, billing-overview)
- Create: `resources/views/portals/owner/` (dashboard, school-switcher, enrollment-overview, fees-overview)
- Create: `resources/views/portals/student/` (dashboard, profile, timetable, homework-list, results, fees-balance)
- Create: `resources/views/portals/parent/` (dashboard, child-selector, fees-balance, payment-initiate, attendance-summary, notices)
- Create: `src/Http/Controllers/Portal/` (SuperAdminController, OwnerController, StudentController, ParentController)

**Super admin portal:** List all schools with status/plan/student count. Create new school (tenant). View billing overview. View platform stats (total schools, total students, SMS credits).

**Owner portal:** View own school(s) list. Switch between schools. See enrollment count and fees collection rate per school. Basic approval notification placeholder.

**Student portal:** Personal profile. Current timetable. Homework list (due/submitted/evaluated). Exam results by term. Fee balance with payment history via SchoolPay.

**Parent portal:** Select child (supports multiple children). View fees balance + outstanding. Initiate SchoolPay payment (redirect to SchoolPay payment page or USSD instructions). View attendance summary. View notices. View child's timetable and homework.

**Step 5: Commit**
```bash
git commit -m "feat: super admin, owner, student, and parent portal scaffolds"
```

---

### Task 11: Phase 1 Test Suite Completion

**Files:**
- Create: `tests/E2E/AdmissionFlow/StudentAdmissionTest.php`
- Create: `tests/E2E/FeesFlow/FeePaymentFlowTest.php`
- Create: `tests/E2E/ExamFlow/ResultPublicationTest.php`
- Create: `tests/Security/TenantIsolationTest.php`
- Create: `tests/Security/SqlInjectionTest.php`
- Create: `tests/Performance/LoadTest.php` (using Apache Bench or k6)

**Critical security tests:**
```php
// tests/Security/TenantIsolationTest.php
public function test_tenant_a_cannot_read_tenant_b_students(): void {
    $service = new StudentService($this->db, tenantId: 1);
    // Student 9999 belongs to tenant 2
    $result = $service->findById(9999);
    $this->assertNull($result, 'Cross-tenant data leak detected');
}

public function test_all_queries_include_tenant_id(): void {
    // Enable MySQL query log, run service methods, verify every SELECT has tenant_id in WHERE
    $queries = $this->captureQueries(fn() => $this->studentService->getAll());
    foreach ($queries as $query) {
        $this->assertStringContainsString('tenant_id', $query);
    }
}
```

**Step 5: Commit**
```bash
git commit -m "test: complete Phase 1 test suite — unit, integration, E2E, security"
```

---

### Task 12: Phase 1 Completion Gate

**Checklist before marking Phase 1 complete:**
- [ ] All migrations run cleanly on fresh database
- [ ] All 9 built-in roles log in and see correct scoped views
- [ ] Student admission form saves all 40+ fields
- [ ] UNEB PLE, UCE, and UACE grading calculations pass test suite
- [ ] Fees collect and SchoolPay webhook processes payment to student record
- [ ] Attendance marks and SMS alert sends via Africa's Talking sandbox
- [ ] Report cards generate as PDF with correct Uganda templates
- [ ] All 4 portal scaffolds render without errors
- [ ] Tenant isolation test: zero cross-tenant data leaks
- [ ] SQL injection test: all inputs sanitized
- [ ] P95 response time ≤ 500ms on standard endpoints

**Final commit:**
```bash
git commit -m "feat: Phase 1 complete — full Starter tier web app with 4 portal scaffolds"
```

---

## Execution Options

**Plan complete and saved. Two execution options:**

**1. Subagent-Driven (this session)** — Dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** — Open new session with executing-plans, batch execution with checkpoints

Which approach?
