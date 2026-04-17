# Test Levels

Longhorn ERP testing is organised into 4 levels that mirror the V-model stages defined in IEEE 1012-2016. Each level specifies the tool, owner, trigger event, and deterministic pass criterion.

## 2.1 Level 1 — Unit Tests

| Attribute | Detail |
|---|---|
| **Tool** | PHPUnit 11.2 |
| **Owner** | Developer (author of the changed service class) |
| **Trigger** | Pre-push git hook; blocks push on failure |
| **Environment** | Local development; no live database |

### 2.1.1 Scope

- Individual service class methods tested in isolation.
- All external dependencies — MySQL database, EFRIS API, MoMo API, file system — are replaced with PHPUnit mocks or stubs.
- Test files reside in `tests/Unit/` and mirror the `app/Services/` directory structure.

### 2.1.2 Key Coverage Requirements

- Line coverage ≥ 80% per service class, measured by the PHPUnit code coverage driver (Xdebug or PCOV).
- All boundary conditions for financial calculations must have explicit test cases: zero-value inputs, negative inputs, maximum integer values, and currency rounding to 2 decimal places.
- Each RBAC permission check in a service method must have a test case for both an authorised and an unauthorised caller.

### 2.1.3 Pass Criterion

- 100% of unit test cases pass (zero failures, zero errors).
- Aggregate line coverage for the changed service class is ≥ 80%.

### 2.1.4 Failure Action

The pre-push hook exits non-zero, blocking the push. The developer resolves all failures before re-attempting the push. No exceptions are granted for bypassing the hook.

---

## 2.2 Level 2 — Integration Tests

| Attribute | Detail |
|---|---|
| **Tool** | PHPUnit 11.2 |
| **Owner** | Developer; reviewed by tech lead on PR |
| **Trigger** | Every pull request merge into `develop` or `main` |
| **Environment** | CI pipeline; dedicated MySQL 9.1 test schema, reset per test class via transactions or schema rebuild |

### 2.2.1 Scope

- Service layer interacting with a real MySQL test database; no mocks for the database layer.
- HTTP controllers tested end-to-end within the PHP process (no external HTTP call).
- External APIs (EFRIS, MoMo) remain mocked at the HTTP adapter level.

### 2.2.2 Mandatory Scenario Coverage

Every integration test suite must include the following scenarios before a PR is approved:

1. **GL Double-Entry Integrity:** After every financial transaction (invoice post, payment, journal entry, depreciation run), execute `SELECT SUM(debit_amount) - SUM(credit_amount) FROM gl_entries WHERE transaction_id = :id` and assert the result equals 0.00.
2. **Tenant Isolation:** For every query that filters by `tenant_id`, execute an equivalent query substituting a second test tenant's ID and assert the result set is empty. This test must exist for GL entries, payroll records, inventory stock, and asset registers.
3. **Audit Log Completeness:** Every state-changing operation (create, update, delete, approve, reverse) must produce exactly 1 audit log record containing the actor's `user_id`, the affected `table_name`, the `record_id`, and a `before`/`after` JSON snapshot.

### 2.2.3 Pass Criterion

- 100% of integration test cases pass (zero failures, zero errors).
- No cross-tenant data leakage detected in any tenant isolation scenario — a single leakage failure is a Critical defect and blocks the PR merge.

---

## 2.3 Level 3 — System / End-to-End Tests

| Attribute | Detail |
|---|---|
| **Tool** | PHPUnit 11.2 HTTP client (API flows); manual test scripts (browser flows) |
| **Owner** | QA lead |
| **Trigger** | Pre-release candidate build on staging environment |
| **Environment** | Staging (see Section 4) |

### 2.3.1 Scope

- Full workflow execution via HTTP from an external client perspective.
- Browser flows are executed manually against the staging environment using documented test scripts.
- API flows are executed by the PHPUnit HTTP client suite in `tests/System/`.

### 2.3.2 Minimum Workflow Coverage

At minimum, one happy-path system test must exist and pass for each of the following workflows before any release candidate is approved:

| Workflow | Key Assertions |
|---|---|
| Invoice lifecycle | Draft → Approved → Posted → Payment matched; GL balance = 0 after posting |
| Payroll run (500 employees) | Run completes in ≤ 30 s; net pay per employee matches manual calculation for 3 sampled records |
| Cooperative intake and bulk payment | Intake recorded, grading applied, bulk payment dispatched to 1,000 farmers in ≤ 60 s |
| Asset registration and depreciation run | Asset created, depreciation run completes in ≤ 30 s for 5,000 assets, NBV decrements correctly |
| Mobile API authentication | JWT issued, request authenticated, JWT expired, refresh accepted, revoked token rejected with HTTP 401 |
| Tenant onboarding | New tenant created; isolated schema partition verified; admin user created with correct RBAC role |

### 2.3.3 Pass Criterion

- 100% of system test scripts pass with no assertion failures.
- All NFR performance targets in Section 1.5 are met under the load profile specified in the performance test plan.

---

## 2.4 Level 4 — User Acceptance Testing (UAT)

| Attribute | Detail |
|---|---|
| **Tool** | Manual execution against acceptance criteria from SRS |
| **Owner** | Product owner; executed by product owner + selected pilot tenants |
| **Trigger** | System test level has passed (Level 3 exit criteria met) |
| **Environment** | Staging server with production-equivalent data volume (anonymised clone) |

### 2.4.1 Scope

- Real-user testing of complete business workflows by users unfamiliar with the implementation details.
- Acceptance criteria sourced directly from the approved SRS functional requirements.
- Usability benchmark: NFR-USAB-001 — a representative user with no prior Longhorn ERP training completes a first assigned task in ≤ 10 minutes.

### 2.4.2 UAT Execution Protocol

1. The QA lead provides the product owner with a UAT test pack containing one test case per SRS acceptance criterion.
2. Pilot tenants execute test cases on the staging environment using their own accounts.
3. All defects discovered during UAT are logged in the defect tracker with severity assigned by the QA lead.
4. No development team member guides or assists pilot tenants during task execution — assistance invalidates the usability benchmark.

### 2.4.3 Pass Criterion

- All acceptance criteria documented in the SRS are met as demonstrated by signed-off UAT test cases.
- Zero Critical defects open at UAT sign-off.
- Zero High defects open at UAT sign-off.
- NFR-USAB-001 benchmark met: ≥ 4 of 5 representative users complete their first assigned task in ≤ 10 minutes without assistance.
