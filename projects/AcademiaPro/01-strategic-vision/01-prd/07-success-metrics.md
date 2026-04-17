# Product Requirements Document — Academia Pro

## Success Metrics

All metrics below are measurable per IEEE 982.1. Vague qualitative targets have been replaced with specific thresholds, measurement methods, and review cadences. Metrics are grouped by the phase at which they first become measurable.

---

### Business and Commercial Metrics

| Metric | Target | Measurement Method | Review Cadence |
|---|---|---|---|
| Uganda school acquisition (24 months post Phase 1 launch) | ≥ 500 active paying schools | Chwezi CRM / tenant record count | Monthly |
| Pan-Africa country expansion (36 months post Phase 1 launch) | ≥ 3 countries live with ≥ 10 paying schools each | Tenant country profile records | Quarterly |
| Monthly Recurring Revenue (MRR) growth rate | ≥ 15% MoM for first 12 months post Phase 9 launch | Billing system export | Monthly |
| School churn rate (annual) | ≤ 5% of active paying schools per year | Cancelled subscriptions / active school count | Quarterly |
| Net Promoter Score (NPS) — school administrators | ≥ 50 | In-app NPS survey, minimum 100 responses | Per term |
| Support ticket resolution time (P90) | ≤ 24 hours for critical issues; ≤ 72 hours for standard | Helpdesk system ticket log | Monthly |

---

### Phase Gate Criteria

**Phase 1 Gate**

- All 7 standard modules pass 100% automated test suite (PHPUnit/Pest backend; Vitest frontend).
- At least 1 pilot school is live and using the system for a complete term (fee collection + attendance + mark entry + report card generation).
- SchoolPay integration passes live transaction reconciliation test: 0 unreconciled payments after a 7-day live run.
- UNEB grading engine produces correct results for a manually verified sample set of 50 PLE students, 50 UCE students, and 50 UACE students.

**Phase 4 Gate**

- 100% automated test suite pass across all Phase 1 and Phase 2 modules before Phase 5 begins.
- PHPStan level 8: zero errors in CI pipeline.
- Test coverage: ≥ 80% line coverage (backend); 100% on UNEB grading engine and fee calculation logic.

**Phase 8 Gate**

- Zero OWASP Top 10 critical or high findings in third-party penetration test report.
- UNEB grading engine validated against UNEB-provided sample mark sheets for PLE, UCE, and UACE cohorts.
- MoES EMIS export validated by a MoES field officer for format compliance.
- SchoolPay merchant integration certified by SchoolPay operations team.
- Android app approved and live on Google Play Store.

**Phase 11 Gate (Pan-Africa)**

- Kenya NEMIS integration functional: student data export passes NEMIS format validation.
- M-Pesa Daraja API tested with live transactions: 0 failed payments in a 100-transaction test run.
- At least 10 Kenya schools active on the platform.

---

### System Performance Metrics

| Metric | Target | Measurement Method |
|---|---|---|
| Page load time (P95, logged-in dashboard, simulated 3G) | ≤ 2,000 ms | Playwright network throttle test, 50 concurrent users |
| API response time (P95, standard CRUD) | ≤ 500 ms | k6 load test, 200 concurrent requests |
| API response time (P95, single report card generation) | ≤ 3,000 ms | k6 load test |
| Bulk report card generation (200 students) | ≤ 120 seconds | Timed integration test |
| UNEB grade computation (500 students) | ≤ 5 seconds | PHPUnit timed test |
| Database query time (P99, any single query) | ≤ 200 ms | Laravel Telescope query log |
| Monthly uptime (all modules) | ≥ 99.5% (≤ 3.65 hours downtime/month) | UptimeRobot / Healthchecks.io |
| Monthly uptime — exam period modules (Gradebook, Attendance, Fees) | ≥ 99.9% (≤ 0.73 hours downtime/month) | UptimeRobot with exam-period alert profile |
| Recovery Time Objective (RTO) | ≤ 4 hours after unplanned outage | Incident log |
| Recovery Point Objective (RPO) | ≤ 1 hour data loss | Backup success log; hourly incremental backup verification |

---

### Data Integrity Metrics

| Metric | Target | Measurement Method |
|---|---|---|
| Fee payment duplicate receipts | 0 per 10,000 payment events | Fee payments audit query on `external_reference` uniqueness |
| UNEB grade computation accuracy | 100% match with UNEB sample mark sheets | Automated comparison test against UNEB-provided answer key |
| Backup success rate | ≥ 99.9% of scheduled backup jobs complete without error | Healthchecks.io job monitoring |
| SchoolPay reconciliation completeness | ≥ 99.5% of SchoolPay transactions matched within 24 hours | Daily reconciliation report: unmatched count / total transactions |

---

### User Adoption Metrics

| Metric | Target | Measurement Method | Phase |
|---|---|---|---|
| Attendance entry via app or web (vs. paper only) | ≥ 80% of class teachers submitting digitally within 90 days of onboarding | Attendance records with `source=digital` / total records | Phase 1 |
| Report card generation time per class (head teacher workflow) | ≤ 15 minutes for a class of 40 students | Measured from bulk-generate trigger to last PDF confirmed | Phase 1 |
| Fee reconciliation time per week (bursar workflow) | ≤ 30 minutes/week, compared to baseline of ≥ 3 hours/week (manual Excel) | Bursar time-in-module session log | Phase 1 |
| Parent app weekly active users (WAU) | ≥ 60% of registered parents active within 7 days of report card release | App analytics (Firebase) | Phase 5 |
| Teacher app attendance submission rate | ≥ 90% of classes recording digital attendance by end of first full term | Attendance records completeness report | Phase 6 |

---

### Security Metrics

| Metric | Target | Measurement Method |
|---|---|---|
| OWASP Top 10 critical/high findings | 0 in any penetration test | Third-party pentest report (Phase 8) |
| Cross-tenant data leak incidents | 0 | Tenant isolation audit; automated test suite (tenant boundary tests) |
| PDPO breach notifications | 0 reportable breaches | Incident log |
| MFA adoption for Super Admin and School Owner/Director roles | 100% | MFA status check query on qualifying role accounts |

---

### Quality Code Metrics

| Metric | Target | Measurement Method |
|---|---|---|
| PHPStan level | 8 (strict), 0 errors | CI pipeline (GitHub Actions) |
| Backend test coverage | ≥ 80% line; 100% on UNEB engine and fee logic | Pest coverage report in CI |
| Frontend component coverage | ≥ 70% | Vitest coverage report |
| E2E critical flows passing | 100% (admission, fee payment, mark entry, report card generation) | Playwright CI suite |
| Code style violations | 0 at merge | PHP CS Fixer + ESLint + Prettier in CI pre-merge gate |
