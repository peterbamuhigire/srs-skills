# Quality Standards — Academia Pro

All targets are measurable per IEEE 982.1. No vague adjectives.

## Performance

| Metric | Target | Measurement Method |
|---|---|---|
| Page load (P95, logged-in dashboard) | ≤ 2,000 ms on 3G connection (10 Mbps simulated) | Playwright network throttle test, 50 concurrent users |
| API response time (P95, standard CRUD) | ≤ 500 ms under 200 concurrent requests | k6 load test |
| API response time (P95, report card generation — single student) | ≤ 3,000 ms | k6 load test |
| Bulk report card generation (200 students) | ≤ 120 seconds | Timed integration test |
| UNEB grade computation (500 students) | ≤ 5 seconds | PHPUnit timed test |
| Database query time (P99, any single query) | ≤ 200 ms | Laravel Telescope query log |

## Availability

| Metric | Target |
|---|---|
| Monthly uptime (all modules) | ≥ 99.5% ($\leq$ 3.65 hours downtime/month) |
| Monthly uptime during exam periods (Gradebook, Attendance, Fees) | ≥ 99.9% ($\leq$ 0.73 hours downtime/month) |
| Scheduled maintenance window | Saturdays 02:00–04:00 EAT only; not during exam periods |
| Recovery Time Objective (RTO) | ≤ 4 hours after unplanned outage |
| Recovery Point Objective (RPO) | ≤ 1 hour data loss (daily automated backups + hourly incremental) |

## Security

| Standard | Requirement |
|---|---|
| OWASP Top 10 | Zero critical or high findings in any penetration test |
| Data encryption at rest | AES-256 for all PII fields and database volumes |
| Data encryption in transit | TLS 1.3 minimum; TLS 1.2 permitted only for legacy USSD integration |
| Authentication | Multi-factor authentication (TOTP) mandatory for Super Admin and School Owner roles |
| Password policy | Minimum 10 characters, 1 uppercase, 1 number, 1 symbol; bcrypt cost factor ≥ 12 |
| Session timeout | 30 minutes inactivity for web; 7 days for mobile apps with refresh token rotation |
| Audit logging | Every create/update/delete action on student, fee, and health records logged with user_id, tenant_id, timestamp, and before/after values |
| PDPO compliance | Full specification in `_context/gap-analysis.md` HIGH-008 |

## Reliability

| Metric | Target |
|---|---|
| Fee payment idempotency | 0 duplicate receipts per 10,000 payment events (double-payment prevention — see BR-FEE-005) |
| UNEB grade computation accuracy | 100% match with manually verified UNEB sample mark sheets (sample provided by UNEB — see gap-analysis.md resource list) |
| Data backup success rate | ≥ 99.9% of scheduled backup jobs complete without error (monitored via Healthchecks.io) |

## Accessibility

| Standard | Target |
|---|---|
| WCAG 2.1 AA | Zero violations on Axe automated scan for all web portal pages |
| Keyboard navigation | All interactive elements reachable and operable without pointing device |
| Colour contrast (normal text) | Minimum 4.5:1 ratio |
| Mobile viewport | All views functional on 360 × 800 px (common Android budget phone resolution) |

## Code Quality

| Standard | Target |
|---|---|
| PHPStan level | 8 (strict) — zero errors before any PR merge |
| Test coverage (backend) | ≥ 80% line coverage; 100% on UNEB grading engine and fee calculation logic |
| Test coverage (frontend) | ≥ 70% component coverage (Vitest) |
| E2E tests | All critical user flows (admission, fee payment, mark entry, report card generation) covered by Playwright tests |
| Code style | PHP CS Fixer (PSR-12); ESLint + Prettier (TypeScript) — enforced in CI |

## Localisation

| Standard | Target |
|---|---|
| Language support | English (default); Luganda (Phase 11); French, Swahili (Phase 11 pan-Africa) |
| Currency display | UGX with comma separator (e.g., UGX 1,250,000) for Uganda; country-specific formats via locale config |
| Date format | DD/MM/YYYY for Uganda school context; ISO 8601 (YYYY-MM-DD) for all API and database values |
| Timezone | Africa/Kampala (EAT, UTC+3) default; configurable per tenant for pan-Africa expansion |
