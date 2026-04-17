# Go-Live Readiness Checklist — Academia Pro

Every tenant go-live and every platform release passes the checklist below. No go-live without every item ticked.

## Platform Release Checklist

- [x] All phase-gate `python -m engine validate` checks PASS.
- [x] Signed audit report committed to `09-governance-compliance/audit-report.md`.
- [x] Risk register up-to-date; no Sev-1 risks unmitigated.
- [x] Security scan (OWASP ZAP + Snyk) passes.
- [x] WCAG 2.1 AA axe-core passes with 0 critical.
- [x] Penetration test report on file (annual cadence).
- [x] DPIA signed off for any AI features in scope.
- [x] Test completion report signed off.
- [x] Rollback drill executed within last 30 days.
- [x] On-call rota confirmed for the go-live week.
- [x] Stakeholder comms sent at least 48 hours before the change window.
- [x] All ADRs reviewed; no expired waivers.

## Per-Tenant (School) Go-Live Checklist

- [x] Tenant record created in `tenants` table with every mandatory metadata field.
- [x] RBAC roles assigned to the first wave of users.
- [x] DPPA consent acknowledged in writing by school admin.
- [x] Data migration dry-run successful (see `04-development/01-technical-spec/02-data-migration.md`).
- [x] Initial fee structures seeded.
- [x] Initial academic calendar seeded.
- [x] MTN MoMo / Airtel / SchoolPay integration tested with a real UGX 1,000 transaction.
- [x] UNEB candidate file export dry-run (secondary schools only).
- [x] Training session delivered to school administrators.
- [x] 1-week hypercare on-call schedule published.
- [x] Tenant onboarding packet handed over (user manual, quick-start, escalation contacts).
