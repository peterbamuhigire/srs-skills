# Test Objectives and Scope

## 1.1 Test Objectives

The test strategy for Longhorn ERP is grounded in IEEE 1012-2016 Verification and Validation (V&V) requirements. The objectives of the test programme are:

1. Verify that every Software Requirements Specification (SRS) functional requirement (FR-*-*) is implemented correctly and completely before any release is approved.
2. Validate that non-functional requirements (NFRs) — including performance, availability, and security targets — are met under representative load conditions.
3. Detect tenant data leakage between logical tenants before any code reaches the staging environment.
4. Confirm that all financial calculations (general ledger postings, payroll computation, asset depreciation, cooperative bulk payments) produce arithmetically correct results under both normal and boundary conditions.
5. Ensure that every Critical and High defect discovered during testing has a corresponding automated regression test added before the defect is marked Closed.
6. Maintain PHPStan level 8 zero-error compliance and PHP CS Fixer zero-violation compliance on every commit throughout the development lifecycle.

## 1.2 Scope

### 1.2.1 In Scope

The following system components are within scope for all test levels:

- All 16 Longhorn ERP functional modules: General Ledger, Accounts Payable, Accounts Receivable, Fixed Assets, Payroll, Inventory, Procurement, Sales, HR, Cooperative Management, Project Accounting, Budgeting, Tax (URA EFRIS integration logic), Reporting, User Management, and Tenant Administration.
- 4 platform services: Authentication (session/JWT), RBAC engine, Audit Log, and Multi-Tenant Isolation layer.
- Web interface: PHP 8.3 / Bootstrap 5.3 / jQuery 3.7 rendered in supported browsers.
- Mobile interfaces: Android (Kotlin/Jetpack Compose, API 29+) and iOS (Swift/SwiftUI, iOS 16+).
- REST API endpoints consumed by the mobile clients.
- Database schema integrity: row-level `tenant_id` isolation on all tables in MySQL 9.1.

### 1.2.2 Out of Scope

The following components are excluded from this test strategy. Defects originating in these components are logged as external dependencies and escalated to the relevant third party.

- URA EFRIS server infrastructure and EFRIS API availability.
- MTN MoMo, Airtel Money, and Stanbic bank network availability and settlement logic residing on the payment provider side.
- Physical weighbridge hardware at cooperative intake points.
- Cloud hosting infrastructure (OS-level, network-level, and hardware failures).

## 1.3 Test Entry Criteria

Testing at each level may not begin until all of the following conditions are satisfied:

1. The feature branch has passed PHPStan level 8 with zero errors.
2. PHP CS Fixer reports zero violations on the branch.
3. A test environment matching the specification in Section 4 is provisioned and accessible.
4. All SRS functional requirements targeted by the test cycle carry status "Approved."
5. Test data fixtures and seed scripts for the relevant module are committed to the repository under `database/seeders/testing/`.
6. The defect tracking system is configured with the severity and SLA definitions in Section 5.

## 1.4 Test Exit Criteria

A release is approved for promotion to the next environment only when all of the following conditions are satisfied:

1. 100% of planned test cases have been executed.
2. Zero Critical defects remain in Open or In Progress status.
3. Zero High defects remain in Open or In Progress status.
4. All Medium defects have an accepted workaround documented in the defect tracker, or are deferred to the next sprint with product owner approval.
5. PHPStan level 8 reports zero errors on the release branch.
6. Code coverage for the release branch is ≥ 80% line coverage per service class (unit test suite).
7. All NFR performance benchmarks defined in Section 1.5 have been met on the staging environment under the specified load profile.
8. The UAT sign-off document is signed by the product owner.

## 1.5 Defect Severity Classification

| Severity | Definition | Examples |
|---|---|---|
| **Critical** | Data loss, security breach, tenant data leakage, or financial calculation error. System unusable or produces incorrect monetary output. | Cross-tenant GL query returns another tenant's records; payroll computation produces wrong net pay; session token accepted after explicit logout. |
| **High** | Feature broken, user workflow blocked, or financial output incorrect in a non-critical path. No acceptable workaround exists. | Invoice cannot be saved; depreciation run errors mid-batch; mobile JWT not refreshed, causing forced logout on valid session. |
| **Medium** | Degraded performance that does not breach an NFR threshold, or a minor behavioural deviation with an acceptable workaround. | Report export takes 8 s instead of the expected 2 s under low load; a filter field resets unexpectedly but data is not lost. |
| **Low** | Cosmetic issue, typo, or documentation discrepancy. No functional or data impact. | Label capitalisation inconsistent; tooltip text contains a grammatical error. |

All security defects — regardless of functional impact — are treated as Critical in the defect lifecycle (see Section 5.4).

## 1.6 Definition of Done for a Test Phase

A test phase is complete when:

1. All Critical and High defects are resolved and verified via retest.
2. All Medium defects either have an accepted workaround or are formally deferred with product owner approval.
3. PHPStan level 8 reports zero errors on the branch under test.
4. Every Critical and High defect fix is accompanied by a new automated test case that would have caught the defect before introduction.
5. Test execution results and defect closure evidence are archived in the project's test management artefact store.
