# Definition of Done: Medic8

**Document ID:** Medic8-DoD-001
**Version:** 1.0
**Date:** 2026-04-03
**Methodology:** Hybrid (Water-Scrum-Fall)
**Standards:** Scrum Guide 2020, IEEE 29148-2018, PDPA 2019

The Definition of Done (DoD) is the shared quality contract for the Medic8 development team. No story, sprint, or release is considered complete until every applicable item is satisfied. Items marked as conditional apply only when the stated condition is true.

---

## 1 Story Level Definition of Done

Every user story must meet all of the following criteria before it is accepted into the sprint increment.

### 1.1 Code Quality

- [ ] Code written following PSR-12 coding standard with `declare(strict_types=1)` in every PHP file
- [ ] No PHP CS Fixer violations (enforced by CI pipeline)
- [ ] No PHPStan level 8 errors (enforced by CI pipeline)
- [ ] Error handling uses typed exceptions; no generic `\Exception` throws
- [ ] No `dd()`, `dump()`, `var_dump()`, or `print_r()` statements in committed code
- [ ] Committed to a feature branch with a Conventional Commit message (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`)

### 1.2 Testing

- [ ] Unit tests written and passing with minimum 80% line coverage for service classes
- [ ] 100% line coverage for Clinical Decision Support (CDS) classes (drug interactions, dosing calculations, NEWS2, Five Rights)
- [ ] Integration test written for every API endpoint (request/response, validation, auth, tenant isolation)
- [ ] All existing tests continue to pass (no regressions)
- [ ] Test names describe the behaviour under test, not the method name

### 1.3 Multi-Tenant Isolation

- [ ] Tenant isolation verified: every database query that touches tenant-scoped data includes `facility_id` filtering (BR-DATA-004)
- [ ] Eloquent global scope applied to all tenant-scoped models
- [ ] No raw SQL queries without tenant scope (CI audit rule passes)
- [ ] Cross-tenant data leakage test written and passing (attempt to read Facility B data from Facility A context returns empty)

### 1.4 API and Data Standards

- [ ] API response follows the envelope format: `{ "success": bool, "data": {}, "message": string, "errors": [] }`
- [ ] Form Request validation implemented for all input endpoints; no inline validation in controllers
- [ ] Request validation messages are user-facing and specific (not framework defaults)
- [ ] Database migrations are reversible (`down()` method implemented)

### 1.5 Clinical Data Integrity

- [ ] Audit trail logging implemented for all create, update, and delete operations on clinical data (PDPA 2019 Section 24)
- [ ] Audit log entries include: user ID, facility ID, action, table, record ID, old values, new values, IP address, and timestamp
- [ ] Auto-save implemented for clinical forms (BR-DATA-005): form state persisted on every interaction, recoverable after power loss or browser crash
- [ ] No Protected Health Information (PHI) in log output (`storage/logs/*.log`): patient names, NINs, diagnoses, and prescriptions are never logged

### 1.6 Review and Documentation

- [ ] Peer review completed; for solo developer: self-review checklist completed against this DoD before merge
- [ ] Inline code comments explain "why," not "what," for non-obvious logic
- [ ] API endpoint documented in the API specification (route, method, request body, response, auth requirement)

---

## 2 Clinical Safety Definition of Done

These criteria apply in addition to the Story Level DoD for any story that touches clinical workflows, prescribing, CDS rules, or patient safety logic.

### 2.1 Clinical Decision Support

- [ ] CDS rules tested with 4 scenario types: positive (alert fires correctly), negative (alert does not fire when it should not), boundary (values at exact threshold), and override (clinician override is logged and auditable)
- [ ] Drug interaction alerts fire at the correct severity tier (Info, Warning, Serious, Fatal) per BR-CLIN-004
- [ ] Tier 4 (Fatal) drug interaction alerts cannot be overridden by the prescriber; pharmacist intervention is required and enforced
- [ ] All Tier 3 and Tier 4 overrides are logged with clinician ID, timestamp, and documented reason

### 2.2 Dosing and Scoring

- [ ] Paediatric weight-based dosing calculation verified against manual calculation for at least 3 representative drugs and 3 weight ranges (BR-CLIN-006)
- [ ] Adult ceiling dose cap applied and verified for paediatric patients
- [ ] Decimal error detection (dose exceeding 10x expected) verified with test cases
- [ ] NEWS2 Early Warning Score calculation verified against the Royal College of Physicians scoring reference (BR-CLIN-007)
- [ ] NEWS2 escalation thresholds (0-4, 5-6, 7+) trigger the correct clinical response

### 2.3 Critical Values and Escalation

- [ ] Critical value escalation cascade tested: 30-minute notification to requesting doctor, 60-minute escalation to ward sister, then Facility Admin (BR-CLIN-003)
- [ ] All escalation steps are timestamped in the audit trail
- [ ] Acknowledgement mechanism tested: notification is dismissed only when the responsible clinician acknowledges

### 2.4 Offline and Resilience

- [ ] Offline mode tested for the clinical workflow (registration, OPD, prescribing, dispensing, lab result entry)
- [ ] Offline queue verified: data entered offline is queued and synced on connectivity restoration
- [ ] Conflict resolution for clinical fields preserves both versions for clinician review (BR-DATA-003)
- [ ] Auto-save recovery verified after simulated power loss

### 2.5 Five Rights

- [ ] Five Rights CPOE enforcement verified: right patient, right drug, right dose, right route, right time (BR-CLIN-008)
- [ ] Failure of any individual right blocks prescription submission with a specific error message identifying the failed check
- [ ] Prescribing authority enforcement verified: nurses cannot prescribe, clinical officers are scope-restricted (BR-CLIN-002)

---

## 3 Sprint Level Definition of Done

Every sprint must meet all of the following criteria before the increment is considered releasable.

- [ ] All stories committed to the sprint meet the Story Level DoD (Section 1)
- [ ] All clinical stories meet the Clinical Safety DoD (Section 2) in addition to the Story Level DoD
- [ ] Sprint demo completed: all stories demonstrated on the staging environment against their acceptance criteria
- [ ] Staging environment deployed with the sprint increment and smoke-tested (login, navigate to each new module, perform one end-to-end transaction)
- [ ] No Critical severity bugs open at sprint close
- [ ] No High severity bugs open at sprint close (or explicitly deferred to next sprint with documented justification and stakeholder acknowledgement)
- [ ] Sprint retrospective completed and at least 1 actionable improvement documented for the next sprint
- [ ] `DOCUMENTATION-STATUS.md` updated to reflect newly completed modules and any outstanding documentation gaps
- [ ] Sprint velocity recorded for capacity planning

---

## 4 Release Level Definition of Done

Phase 1 MVP is considered release-ready only when all of the following criteria are met. This checklist is evaluated at the end of Post-Sprint 8 (UAT period).

### 4.1 Quality Gates

- [ ] All 8 Sprint Level DoDs met (Sprints 1-8)
- [ ] Full regression test suite passing: unit, integration, and end-to-end tests
- [ ] Zero Critical or High severity bugs open
- [ ] Test coverage meets minimums: 80% for services, 100% for CDS classes

### 4.2 Performance

- [ ] P95 API response time under 500 ms under normal load (50 concurrent users per facility)
- [ ] Page load time under 2 seconds on a 1 Mbps connection
- [ ] Cloud uptime target validated: infrastructure supports 99.9% availability
- [ ] Database query performance verified: no N+1 queries, no full table scans on tables exceeding 10,000 rows

### 4.3 Security

- [ ] Security scan clean: `composer audit` reports zero known vulnerabilities
- [ ] OWASP Top 10 checklist reviewed: SQL injection, XSS, CSRF, broken auth, security misconfiguration, sensitive data exposure
- [ ] Encryption at rest (AES-256-GCM) verified for all patient health data
- [ ] Encryption in transit (TLS 1.2+) verified on all endpoints; TLS 1.0/1.1 disabled
- [ ] Session timeout (15 minutes) verified for clinical users
- [ ] MFA enforced for Super Admin, Facility Admin, Accountant, and Auditor roles
- [ ] HTTP security headers configured: `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`, `Content-Security-Policy`
- [ ] Rate limiting configured for authentication and API endpoints

### 4.4 Clinical Safety

- [ ] HMIS 105 auto-tally accuracy validated against manual tally for at least 1 month of synthetic data (BR-HMIS-001)
- [ ] Drug interaction database coverage verified against the Uganda Essential Medicines List
- [ ] Clinical safety sign-off obtained from a clinical advisor (doctor or clinical officer)
- [ ] All `[V&V-FAIL]` tags resolved or documented with accepted risk and sign-off

### 4.5 User Acceptance

- [ ] UAT completed with 3 pilot facilities (1 private clinic, 1 mission hospital, 1 HC IV)
- [ ] UAT sign-off obtained from each pilot facility's Facility Admin
- [ ] Cash billing reconciliation rate at 95% or above during UAT period (Phase 1 success criterion)
- [ ] End-to-end patient journey completed successfully at each pilot facility: registration, triage, consultation, investigation, prescribing, dispensing, billing, and receipt

### 4.6 Operations

- [ ] Data migration scripts tested (if migrating from a legacy system): test with a copy of production data, verify record counts and data integrity
- [ ] Rollback procedure documented and tested: confirm the system can revert to the previous release within 30 minutes
- [ ] Deployment guide reviewed: step-by-step production deployment procedure documented
- [ ] Backup and restore procedure tested: database backup, restore to a clean environment, verify data integrity
- [ ] Monitoring and alerting configured: uptime monitoring, error rate alerting, disk space alerting
- [ ] Incident response procedure documented: who to contact, escalation path, communication template

---

## 5 Applicability Matrix

| DoD Level | Applies To | Gating Action |
|---|---|---|
| Story Level (Section 1) | Every user story | Story cannot be marked "Done" in the sprint |
| Clinical Safety (Section 2) | Stories tagged with clinical workflow, CDS, prescribing, or patient safety | Story cannot be marked "Done"; clinical safety is non-negotiable |
| Sprint Level (Section 3) | Every sprint increment | Increment cannot be deployed to staging as "releasable" |
| Release Level (Section 4) | Phase 1 MVP release | System cannot proceed to production go-live |

---

## 6 Escalation Procedure

When a DoD item cannot be met:

1. Document the specific item that is not met and the reason
2. Assess the impact: is patient safety affected? Is data integrity at risk? Is regulatory compliance compromised?
3. If patient safety, data integrity, or regulatory compliance is affected: the item is non-negotiable and must be resolved before proceeding
4. If the item is a quality or convenience concern with no safety or compliance impact: escalate to the project owner (Peter) for a documented accept/defer decision
5. All deferred DoD items are tracked as technical debt in the backlog with a target sprint for resolution
