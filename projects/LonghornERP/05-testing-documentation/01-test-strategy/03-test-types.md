# Test Types

Each test type addresses a distinct quality dimension. For every type, this section specifies the purpose, tools, execution frequency, and deterministic pass criterion.

## 3.1 Functional Testing

| Attribute | Detail |
|---|---|
| **Purpose** | Verify that every FR-*-* requirement produces the specified output when the specified input or trigger condition occurs. |
| **Tools** | PHPUnit 11.2 (automated); manual test scripts (browser workflows) |
| **Frequency** | Every pull request; all automated cases run in the CI pipeline before merge |
| **Pass Criterion** | 100% of test cases pass; every FR-*-* requirement has at least 1 corresponding test case with a deterministic assertion |

Functional test IDs follow the pattern `FT-<Module>-<Sequence>` (e.g., `FT-GL-001`) and are traceable to the SRS requirement ID in the test management artefact store.

---

## 3.2 Security Testing

| Attribute | Detail |
|---|---|
| **Purpose** | Verify that the system resists the attack vectors most relevant to a multi-tenant financial SaaS. |
| **Tools** | OWASP Top 10 manual checklist; PHPUnit integration tests for tenant isolation; prepared statement audit via PHPStan custom rule; manual penetration test scripts |
| **Frequency** | Before every release candidate; tenant isolation tests on every PR (see Level 2) |
| **Pass Criterion** | Zero High or Critical security findings open at release; tenant isolation penetration test returns no cross-tenant data |

### 3.2.1 Security Test Coverage Requirements

The following attack vectors must have documented test results before any release is approved:

1. **Tenant Data Leakage (GAP-004):** Execute authenticated requests as Tenant A attempting to read, write, and delete records belonging to Tenant B across all 16 modules. Each attempt must return HTTP 403 or an empty result set — never Tenant B's data.
2. **SQL Injection:** PHPStan static analysis must confirm that every database query uses prepared statements (PDO or Eloquent query builder). No raw string interpolation in SQL expressions. Zero findings required.
3. **CSRF Token Validation:** Every state-changing web form submission (POST, PUT, DELETE) must include a valid CSRF token. Requests with a missing or invalid CSRF token must return HTTP 419. Test case executes a form submission with a deliberately invalid token and asserts HTTP 419.
4. **JWT Security (Mobile API):** Test cases must verify: (a) expired JWT returns HTTP 401; (b) revoked JWT returns HTTP 401 even before natural expiry; (c) JWT signed with a wrong secret returns HTTP 401; (d) JWT refresh token accepted only once (single-use rotation).
5. **Brute-Force Lockout:** After 5 consecutive failed login attempts from the same IP within 10 minutes, the account is locked for 15 minutes. Test case asserts that attempt 6 returns HTTP 429 and that the lockout clears after 15 minutes.
6. **OWASP Top 10 Checklist:** A documented walkthrough of all 10 categories is completed and signed off by the tech lead before each major release.

---

## 3.3 Performance Testing

| Attribute | Detail |
|---|---|
| **Purpose** | Verify that NFR performance targets are met under the specified concurrent load profile. |
| **Tools** | Apache JMeter or k6 (project team chooses one tool and standardises before the first performance test cycle) |
| **Frequency** | Before every release candidate; re-run on any commit that touches a query used in a critical path |
| **Pass Criterion** | All 6 NFR performance targets below are met simultaneously under the 100-concurrent-user load profile |

### 3.3.1 NFR Performance Targets

| NFR ID | Target | Load Profile |
|---|---|---|
| NFR-PERF-001 | Web page load ≤ 2 s at P95 | 100 concurrent users, standard browse pattern |
| NFR-PERF-002 | Payroll run ≤ 30 s for 500 employees | Single payroll run job, staging data |
| NFR-PERF-003 | Mobile API response ≤ 500 ms at P95 | 100 concurrent mobile API requests |
| NFR-ASSET-001 | Depreciation run ≤ 30 s for 5,000 assets | Single depreciation batch job, staging data |
| NFR-COOP-001 | Cooperative bulk payment ≤ 60 s for 1,000 farmers | Single bulk payment dispatch job |
| NFR-AVAIL-001 | System uptime ≥ 99.5% | Measured over rolling 30-day window via external uptime monitor |

### 3.3.2 Performance Test Data Requirements

- The staging database must contain ≥ 500 employee records in the payroll module before the payroll performance test executes.
- The staging database must contain ≥ 5,000 active asset records before the depreciation performance test executes.
- The staging cooperative module must contain ≥ 1,000 registered farmer records before the bulk payment test executes.

---

## 3.4 Static Analysis

| Attribute | Detail |
|---|---|
| **Purpose** | Detect type errors, undefined variables, unreachable code, and unsafe patterns before runtime. |
| **Tools** | PHPStan 1.11, level 8 (maximum strictness) |
| **Frequency** | Every commit (pre-push hook and CI pipeline) |
| **Pass Criterion** | Zero errors reported by PHPStan at level 8 on the branch under test |

PHPStan configuration is maintained in `phpstan.neon` at the project root. The baseline file (`phpstan-baseline.neon`) must remain empty — no errors are grandfathered. Any suppression of a PHPStan error via `@phpstan-ignore` requires a comment justifying the suppression and approval from the tech lead in the PR review.

---

## 3.5 Code Style Compliance

| Attribute | Detail |
|---|---|
| **Purpose** | Enforce consistent formatting so that code review effort focuses on logic rather than style. |
| **Tools** | PHP CS Fixer 3.64 |
| **Frequency** | Every commit (pre-push hook) |
| **Pass Criterion** | Zero violations reported by PHP CS Fixer in `--dry-run` mode |

PHP CS Fixer configuration is maintained in `.php-cs-fixer.php` at the project root. The ruleset must not be modified without a change record in the project changelog.

---

## 3.6 Regression Testing

| Attribute | Detail |
|---|---|
| **Purpose** | Confirm that previously passing functionality has not been broken by new changes. |
| **Tools** | Full PHPUnit 11.2 test suite (unit + integration) |
| **Frequency** | Before every release candidate build; after every Critical or High defect fix |
| **Pass Criterion** | 100% of the full PHPUnit suite passes on the release branch |

The regression suite is the complete set of unit and integration tests accumulated over the project lifecycle. No test case may be deleted without the tech lead's approval and a documented justification.

---

## 3.7 Mobile Testing

| Attribute | Detail |
|---|---|
| **Purpose** | Verify functional correctness, offline-sync behaviour, and platform-specific rendering on Android and iOS. |
| **Tools** | Android Emulator (API 29+) and physical Android device; iOS Simulator (iOS 16+) and physical iPhone |
| **Frequency** | Before every mobile release build |
| **Pass Criterion** | All mobile test scripts pass on both emulator/simulator and at least 1 physical device per platform; offline sync test passes |

### 3.7.1 Mandatory Mobile Test Scenarios

1. **Offline Mode:** Disconnect the test device from the network mid-session after loading a data form. Complete form entry and submit. Reconnect. Assert that the record is synchronised to the server within 30 seconds of reconnection and that no data is lost.
2. **JWT Refresh Flow:** Allow the access token to expire while the app is in the foreground. Assert that the app silently refreshes the token without requiring the user to re-authenticate, and that the in-progress user action completes successfully.
3. **Platform Rendering:** Execute the full mobile smoke test script on an Android device (API 29) and an iOS device (iOS 16) to verify that all screens render without layout overflow, truncation, or missing elements.

---

## 3.8 Accessibility Testing

| Attribute | Detail |
|---|---|
| **Purpose** | Verify conformance to WCAG 2.1 Level AA on the web interface. |
| **Tools** | axe browser extension (automated scan); manual keyboard-navigation test |
| **Frequency** | Selected screens audited before each major release |
| **Pass Criterion** | Zero axe-reported violations at WCAG 2.1 AA level on audited screens; all interactive elements reachable via keyboard Tab sequence |

Screens prioritised for accessibility audit: login, dashboard, invoice entry form, payroll run initiation, and the cooperative intake form.

---

## 3.9 Usability Testing

| Attribute | Detail |
|---|---|
| **Purpose** | Validate NFR-USAB-001: a first-time user can complete a primary task without assistance. |
| **Tools** | Moderated task-observation sessions; screen recording |
| **Frequency** | Before the first pilot tenant onboarding and before each major UX change release |
| **Pass Criterion** | ≥ 4 of 5 representative users, with no prior Longhorn ERP training, complete their first assigned task in ≤ 10 minutes without assistance from the development or product team |

Representative users are recruited from the target tenant profile (accounting clerks or farm cooperative managers with standard computer literacy). Sessions are recorded with participant consent and findings are logged as usability defects or enhancement requests in the defect tracker.
