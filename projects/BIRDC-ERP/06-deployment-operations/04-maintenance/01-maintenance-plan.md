---
title: "BIRDC ERP — Maintenance and Support Plan"
subtitle: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
---

# BIRDC ERP Maintenance and Support Plan

**Document:** Maintenance and Support Plan
**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com)
**Client:** PIBID / BIRDC, Nyaruzinga hill, Bushenyi District, Western Uganda
**Date:** 2026-04-05
**Version:** 1.0
**Deployment Model:** Single-tenant, on-premise at BIRDC Nyaruzinga, Bushenyi, Uganda

---

## 1. Purpose and Scope

This plan governs the post-go-live maintenance of the BIRDC ERP system from Phase 7 completion through the initial 12-month warranty period and beyond. It defines the following areas of ongoing system stewardship:

- Routine preventive and security maintenance activities
- Incident response service level agreements (SLAs)
- Update and patching procedures for application, OS, and third-party dependencies
- Performance monitoring thresholds and alert escalation
- Database housekeeping and retention schedule enforcement
- Regulatory configuration update procedures (Uganda Revenue Authority, PPDA, NSSF)
- Android application maintenance
- 12-month warranty terms and post-warranty engagement
- Long-term sustainability and escalation matrix

This plan applies to all 17 ERP modules and the 6 Android applications delivered under Phases 1–7. It takes effect from the date of the Phase 7 go-live sign-off, as evidenced by **MAC-BIRDC-M-007**.

---

## 2. Maintenance Categories

| Category | Description | Frequency | Owner |
|---|---|---|---|
| Preventive | Scheduled activities that prevent failures before they occur | Per schedule in Section 3 | BIRDC IT + Peter Bamuhigire |
| Corrective | Bug fixes and defect resolution after go-live | On occurrence | Peter Bamuhigire |
| Adaptive | Regulatory updates: PAYE bands, PPDA thresholds, NSSF rates, EFRIS API versions | On regulatory change | Peter Bamuhigire |
| Perfective | Performance optimisation, usability improvements | Quarterly review | Peter Bamuhigire (billable post-warranty) |
| Security | OS, PHP, MySQL, and dependency vulnerability patches | Monthly minimum | BIRDC IT + Peter Bamuhigire |

---

## 3. Routine Maintenance Schedule

| Task | Frequency | Owner | Procedure Ref |
|---|---|---|---|
| MySQL full backup verification (restore test) | Monthly — first Monday of month | BIRDC IT | MNT-003 (Runbook) |
| MySQL slow query log review | Weekly | BIRDC IT | MNT-002 |
| PHP/MySQL security patch assessment | Monthly | Peter Bamuhigire | MNT-003 |
| OS security updates (Ubuntu 22.04 LTS) | Monthly | BIRDC IT | MNT-004 |
| EFRIS queue review and reconciliation | Weekly | Finance Director | MNT-005 (Runbook) |
| SSL/TLS certificate renewal | 90 days before expiry | BIRDC IT | Auto-alert from system |
| Audit trail archive (export records > 2 years old to cold storage) | Annual | IT Administrator | MNT-006 |
| User access review (inactive accounts, role appropriateness) | Quarterly | IT Administrator + DPO | MNT-007 |
| Android APK update review | Per release | Peter Bamuhigire | MNT-008 |
| Payroll element configuration review (PAYE bands, NSSF rates, LST tiers) | Annual — at new Uganda tax year (1 July) | Peter Bamuhigire + Finance Director | MNT-009 |
| PPDA threshold configuration review | Annual / on PPDA directive | Peter Bamuhigire + Administration Officer | MNT-010 |
| Database index rebuild and ANALYZE | Quarterly | BIRDC IT | MNT-011 |
| Retention schedule review — personal data expiry alerts | Quarterly | DPO | MNT-012 (DPPA) |
| PDPO registration renewal (if required by regulations) | Annual | DPO | MNT-013 |

---

## 4. Incident Response SLAs

Response times are measured from receipt of an incident report submitted to the BIRDC IT contact channel (WhatsApp or email). Peter Bamuhigire provides first response within the stated time during business hours: 07:00–20:00 EAT, Monday–Saturday. Outside these hours, P1 incidents only.

| Severity | Definition | Examples | Response Time | Resolution Target |
|---|---|---|---|---|
| P1 — Critical | System unavailable or data integrity at risk | Server down; EFRIS API broken blocking all invoicing; GL hash chain violation (**INC-008**); database corruption | 2 hours | 8 hours |
| P2 — High | Core business function degraded | POS not printing receipts; payroll calculation error; agent app sync failing; PPDA block not releasing | 4 hours | 24 hours |
| P3 — Medium | Non-critical function impaired | Report formatting error; slow query on 1 report; minor UI bug | 8 hours | 5 business days |
| P4 — Low | Cosmetic or minor enhancement | Label text incorrect; colour issue; column sort order | Next scheduled release | 30 days |

### SLA Clock

The SLA clock starts when Peter Bamuhigire acknowledges receipt of the incident report. The clock pauses if Peter Bamuhigire is waiting for information from the BIRDC side (credentials, screenshots, confirmation of steps performed). The clock resumes when BIRDC responds.

---

## 5. Regulatory Update Protocol (Adaptive Maintenance)

When Uganda Revenue Authority (URA), PPDA, or NSSF issues updates that affect system configuration, the following procedure applies.

1. Finance Director or Administration Officer notifies Peter Bamuhigire, providing the official gazette or formal regulatory circular. Do not initiate changes based on media reports.
2. Peter Bamuhigire assesses the impact: payroll configuration (PAYE bands, NSSF rates, LST tiers), PPDA procurement thresholds, EFRIS API version, or tax band tables.
3. **Configuration-level changes** (data updates only — no code change): applied within 1 business day. Finance Director confirms correctness by running a test payroll or test procurement transaction in staging.
4. **Code-level changes** (e.g., EFRIS API version change requiring new request/response schema): treated as a Standard change per the Change Management Procedure (**04-change-management**). Estimate, test, and deploy per that procedure.
5. Finance Director signs a written confirmation (WhatsApp or email) that the regulatory update has been verified before the configuration goes live in production.

---

## 6. Performance Monitoring

The following performance thresholds are derived from `_context/metrics.md` and the Design Covenants. BIRDC IT reviews the system administration dashboard daily. Breaches trigger the escalation actions noted below.

| Metric | Threshold | Alert Trigger |
|---|---|---|
| POS transaction time (search to receipt) | ≤ 90 seconds | > 120 seconds → P2 incident |
| Product search response | ≤ 500 ms at P95 | > 1,000 ms at P95 → investigate slow query log |
| Report generation (up to 12 months) | ≤ 10 seconds | > 20 seconds → P3 incident |
| Trial balance generation | ≤ 5 seconds | > 10 seconds → P3 incident |
| System uptime (06:00–22:00 EAT) | ≥ 99% | < 99% in any calendar month → P2 review |
| Concurrent web users (peak) | 50 without degradation | > 40 active sessions → notify Peter Bamuhigire |

**Monitoring tools:** MySQL slow query log (threshold: 1 second), PHP error log, system administration dashboard displaying CPU, RAM, disk usage, MySQL connections, EFRIS queue depth, and active sessions.

**Infrastructure alert thresholds:**

- Disk usage > 80% of total volume → notify BIRDC IT and Peter Bamuhigire immediately.
- MySQL active connections > 40 → investigate for long-running queries.
- Application error log entries > 10 per hour → classify as P2 incident and investigate.

---

## 7. Database Housekeeping

All housekeeping operations are performed during the defined maintenance window: **Sunday 02:00–04:00 EAT**, unless otherwise noted. The IT Administrator notifies Peter Bamuhigire before executing any archive or purge operation the first time.

| Task | Schedule | Query Pattern |
|---|---|---|
| Archive GL entries > 7 years old to `tbl_gl_archive` | Annual — after confirming 7-year retention satisfied | `INSERT INTO tbl_gl_archive SELECT * FROM tbl_journals WHERE posting_date < DATE_SUB(NOW(), INTERVAL 7 YEAR);` |
| Purge EFRIS queue succeeded records > 90 days | Monthly | `DELETE FROM tbl_efris_queue WHERE status = 'success' AND submitted_at < NOW() - INTERVAL 90 DAY;` |
| Purge audit log entries > 7 years | Annual — with DPO approval; export to cold storage first | Export to compressed CSV on BIRDC offline server before DELETE |
| `OPTIMIZE TABLE` on high-write tables | Quarterly | Tables: `tbl_journals`, `tbl_stock_movements`, `tbl_audit_log` — during maintenance window |
| Review and rebuild indexes per query execution plans | Quarterly | `EXPLAIN` on top 10 slow queries from slow query log; rebuild indexes as needed |

### Personal Data Retention (Uganda Data Protection and Privacy Act 2019)

The DPO reviews personal data expiry alerts quarterly (MNT-012). Farmer records, employee records, and agent records containing NIN, GPS coordinates, mobile money numbers, and photos are subject to defined retention periods. No personal data is deleted without DPO written sign-off. Archive files are stored on BIRDC's local infrastructure — not on any external service (Design Covenant DC-006).

---

## 8. Backup and Recovery SLA

Per the deployment guide, the following backup regime is in place:

- **Daily full backup:** `mysqldump` with `--single-transaction` flag, written to `/backups/birdc-erp/`, compressed with `gzip`.
- **Weekly offsite copy:** IT Administrator copies the weekly backup to a USB drive stored in the Finance Director's safe.
- **Monthly restore test:** MNT-003 (Runbook) — performed on the first Monday of each month.

| Recovery Objective | Target | Notes |
|---|---|---|
| Recovery Time Objective (RTO) | 4 hours | Full database restore from most recent backup, verified by MNT-003 |
| Recovery Point Objective (RPO) | 24 hours | Daily backup cycle — maximum 24 hours of transactions at risk |

**RPO upgrade path:** If the Finance Director determines that a 24-hour RPO is unacceptable (e.g., following a high-volume production day), the backup regime can be upgraded to hourly incremental binary log (`binlog`) backups. This is additional scope and is billable outside the warranty terms.

---

## 9. Security Maintenance

The following monthly security checklist is completed jointly by BIRDC IT and Peter Bamuhigire. The IT Administrator leads on infrastructure items; Peter Bamuhigire leads on application items.

**Monthly Security Checklist:**

- [ ] Apply Ubuntu 22.04 LTS security patches: `sudo apt update && sudo apt upgrade`
- [ ] Check PHP/Composer for known vulnerabilities: `composer audit`
- [ ] Review failed login attempts in the audit log: > 10 failed logins for any user within 24 hours → investigate as potential brute-force attempt
- [ ] Verify CSRF token rotation is functioning on all form submissions
- [ ] Check SSL/TLS certificate validity and confirm renewal reminder is active
- [ ] Review API access log for unusual patterns: off-hours access, bulk requests, unexpected IP addresses
- [ ] Confirm backup encryption keys are current (rotate annually)
- [ ] Confirm all inactive user accounts (no login in 90 days) are deactivated in **Admin > Users**

**Annual security review:** Peter Bamuhigire conducts a full OWASP Top 10 re-assessment annually. Findings are documented and remediated before the next assessment. The first annual review is due 12 months from Phase 7 go-live.

---

## 10. Android Application Maintenance

The 6 Android applications (Sales Agent App, Warehouse App, Farmer Delivery App, Executive Dashboard App, Factory Floor App, HR Self-Service App) require the following ongoing maintenance.

| Activity | Frequency | Owner |
|---|---|---|
| Security library updates (Retrofit, Room, WorkManager, OkHttp) | Monthly — assessed via Dependabot or manual dependency check | Peter Bamuhigire |
| Google Play Store policy compliance review | Annual | Peter Bamuhigire |
| Android OS compatibility test on new major Android version | Within 30 days of new Android major release | Peter Bamuhigire |
| Firebase App Distribution build push (warranty period) | Per release | Peter Bamuhigire |
| Migration to Google Play internal track | After Phase 7 go-live — timing per BIRDC IT readiness | Peter Bamuhigire + BIRDC IT |

**Versioning:** Each APK release receives a semantic version number (`MAJOR.MINOR.PATCH`) recorded in the BIRDC IT maintenance log. The release notes are retained for 7 years as part of the audit trail.

---

## 11. 12-Month Warranty Terms

The warranty period is 12 months from the date of the Phase 7 go-live sign-off, as evidenced by **MAC-BIRDC-M-007** (signed by BIRDC Director and Finance Director).

### Included at No Additional Charge (Warranty Scope)

- P1 and P2 bug fixes within the SLAs defined in Section 4
- Annual regulatory configuration updates: PAYE tax bands, NSSF rates, LST tiers
- Security patches: OS, PHP, MySQL, Android library vulnerabilities
- EFRIS API version updates if URA changes the API within the warranty period
- Monthly routine maintenance as per Section 3 (Peter Bamuhigire's contribution)

### Excluded (Billable Even Within Warranty Period)

- New modules or features not scoped in Phases 1–7
- Third-party integration setup beyond the integrations specified in Phases 1–7
- Hardware procurement, maintenance, or replacement
- Staff retraining beyond the initial training delivered in Phase 7
- Performance upgrades requiring server hardware changes
- RPO upgrade to hourly binlog backup (see Section 8)

### Post-Warranty Continuation

Upon expiry of the 12-month warranty, maintenance and support continues under a separate annual maintenance contract. Pricing and scope are per the engagement letter to be negotiated no later than month 10 of the warranty period to avoid a support gap.

---

## 12. Escalation Matrix

| Issue Type | First Contact | Escalation | Final Authority |
|---|---|---|---|
| Application bug | Peter Bamuhigire — WhatsApp / peter@techguypeter.com | — | Peter Bamuhigire |
| Server / OS issue | BIRDC IT Administrator | Peter Bamuhigire for application-layer advice | BIRDC IT Director |
| EFRIS API issue | Peter Bamuhigire contacts URA EFRIS helpdesk (efris@ura.go.ug) | Finance Director notified | URA EFRIS team |
| MTN MoMo API issue | Peter Bamuhigire contacts MTN Business | BIRDC Finance Director notified | MTN Business team |
| Data breach (DPPA 2019) | DPO → PDPO (NITA-U) immediately — written notification required | Finance Director + BIRDC Director | PDPO / NITA-U |
| Payroll dispute | Finance Director → HR Director | Peter Bamuhigire for system verification | Finance Director |
| GL hash chain integrity failure | Peter Bamuhigire + Finance Director — phone call, not WhatsApp only | BIRDC Director | OAG Uganda (if tampering confirmed) |
| Backup restore failure | BIRDC IT → Peter Bamuhigire | Finance Director notified | Peter Bamuhigire |
