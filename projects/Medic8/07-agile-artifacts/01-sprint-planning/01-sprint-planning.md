# Sprint Planning: Medic8 Phase 1 MVP

**Document ID:** Medic8-SP-001
**Version:** 1.0
**Date:** 2026-04-03
**Methodology:** Hybrid (Water-Scrum-Fall)
**Phase:** 1 — Foundation MVP
**Development Window:** 16 weeks (8 sprints) plus Sprint Zero (1 week) and Post-Sprint hardening (2 weeks)
**Total Calendar Duration:** 19 weeks
**Team Size:** 1 (solo developer)
**Standards:** IEEE 29148-2018, Scrum Guide 2020
**Product Scope:** 32 modules (Phase 1 core modules plus Module 32: AI Intelligence)

---

## 1 Sprint Cadence

**Sprint Duration:** 2 weeks (10 working days)

**Ceremonies:**

1. **Sprint Planning** — Monday AM, Week 1 of sprint. Duration: 2 hours. Select stories from the prioritised backlog, confirm acceptance criteria, identify technical dependencies, and commit to the sprint goal.
2. **Daily Journal** — Daily, 15 minutes. Solo developer replacement for the Daily Standup. Record: what was completed yesterday, what is planned today, and any blockers. Written in `projects/Medic8/_context/sprint-journal.md`.
3. **Sprint Review** — Friday PM, Week 2 of sprint. Duration: 1 hour. Demonstrate completed stories against acceptance criteria on the staging environment. Record demo outcomes and stakeholder feedback.
4. **Sprint Retrospective** — Friday PM, Week 2 of sprint (immediately after Sprint Review). Duration: 30 minutes. Document: what went well, what did not, and one actionable improvement for the next sprint.

**Velocity:**

- Initial estimate: 40 story points per sprint (solo developer baseline)
- Adjust after Sprint 2 based on actual throughput from Sprints 1 and 2
- Velocity range assumption: 35-50 points per sprint depending on story complexity and technical debt

**Estimation Scale:** Modified Fibonacci (1, 2, 3, 5, 8, 13). Any story exceeding 13 points requires decomposition before sprint commitment.

---

## 2 Sprint Zero: Pre-Development Foundation (1 Week)

**Duration:** 1 week (5 working days), preceding Sprint 1
**Sprint Goal:** Establish the development environment, toolchain, and foundational technical decisions so that Sprint 1 begins with zero infrastructure blockers.

| # | Task | Days | Deliverable |
|---|---|---|---|
| SZ-01 | Development environment setup: PHP 8.3, Laravel 11, Composer, Node.js, MySQL 8, Redis, Docker Compose | 1 | `docker-compose.yml`, `.env.example`, verified local stack |
| SZ-02 | Database schema design review: platform tables, auth tables, tenant isolation (`facility_id` pattern per BR-DATA-004) | 1 | ERD v1.0, migration stubs for auth, tenants, and global_patients |
| SZ-03 | CI/CD pipeline setup: GitHub Actions, PHPStan level 8, PHP CS Fixer (PSR-12), PHPUnit, tenant-scope CI audit rule (BR-DATA-004) | 0.5 | `.github/workflows/ci.yml`, passing pipeline on empty project |
| SZ-04 | Coding standards alignment: PSR-12, strict types declaration, Conventional Commits, branch naming convention, PR template | 0.5 | `CONTRIBUTING.md`, `.php-cs-fixer.dist.php`, commit-msg hook |
| SZ-05 | Test framework setup: PHPUnit 11, Pest PHP, feature test base class with tenant context, factory stubs | 0.5 | Base test classes, `phpunit.xml`, passing empty test suite |
| SZ-06 | Drug interaction database licensing: evaluate and licence a drug interaction dataset (DrugBank, Medi-Span, or First Databank) | 0.5 | Licensing decision documented, dataset access confirmed |
| SZ-07 | PDPA legal review initiation: engage legal counsel for Uganda Personal Data Protection Act 2019 compliance assessment | 0.5 | Legal engagement letter sent, review timeline documented |
| SZ-08 | Tabler UI template integration: install Tabler Bootstrap 5 admin template, configure Laravel Blade layout | 0.5 | Base layout with sidebar, header, and authentication views |

**Exit Criteria:**

- [ ] Local development environment boots in under 60 seconds
- [ ] CI pipeline runs and passes on an empty commit
- [ ] PHPStan level 8 and PHP CS Fixer are enforced in CI
- [ ] Tenant-scoped query audit rule is active in CI
- [ ] ERD v1.0 reviewed and approved
- [ ] Drug interaction data source confirmed

---

## 3 Phase 1 Sprint Plan

### Sprint 1: Foundation and Authentication (Weeks 1-2)

**Sprint Goal:** Deliver a secure, multi-tenant authentication system with tenant provisioning so that the first facility can log in and access a role-scoped dashboard.

**Capacity:** 38 story points

| Story ID | Story Title | Points | Priority | Dependencies |
|---|---|---|---|---|
| US-AUTH-001 | Web Login | 5 | Critical | SZ-08 (Tabler layout) |
| US-AUTH-002 | Mobile JWT Login | 5 | Critical | -- |
| US-AUTH-003 | Token Refresh | 3 | Critical | US-AUTH-002 |
| US-AUTH-004 | Logout | 2 | Critical | US-AUTH-001, US-AUTH-002 |
| US-AUTH-005 | Session Timeout (15 min) | 3 | Critical | US-AUTH-001 |
| US-AUTH-006 | MFA for Admin Roles | 5 | High | US-AUTH-001 |
| FR-TNT-001 | Tenant Provisioning | 5 | Critical | SZ-02 (schema) |
| FR-TNT-002 | Tenant Activation/Deactivation | 3 | Critical | FR-TNT-001 |
| FR-TNT-003 | Tenant Configuration (modules, locale, currency) | 3 | High | FR-TNT-001 |
| FR-TNT-004 | Tenant Data Isolation Enforcement | 4 | Critical | FR-TNT-001, BR-DATA-004 |

**Technical Tasks (not story-pointed):**

- Database migrations: `users`, `tenants`, `facilities`, `roles`, `permissions`, `personal_access_tokens`, `global_patients` (schema only)
- Eloquent global scope for `facility_id` enforcement (BR-DATA-004)
- Repository base class with mandatory tenant filter
- API envelope response format
- Exception handler with typed exceptions
- Staging environment deployment

**Key Risks:**

- MFA TOTP library selection and testing may take longer than estimated
- Tenant isolation pattern must be validated thoroughly; a defect here propagates to every subsequent sprint

---

### Sprint 2: Patient Registration (Weeks 3-4)

**Sprint Goal:** Enable a receptionist to register new patients, look up returning patients, and manage patient identity with duplicate detection, so that the patient master index is ready for clinical workflows.

**Capacity:** 46 story points

| Story ID | Story Title | Points | Priority | Dependencies |
|---|---|---|---|---|
| US-REG-001 | Register New Patient (demographics, photo) | 5 | Critical | Sprint 1 (auth, tenant) |
| US-REG-002 | Auto-Generate Unique MRN | 3 | Critical | US-REG-001 |
| US-REG-003 | Look Up Returning Patient | 5 | Critical | US-REG-001 |
| US-REG-004 | Assign Patient Category | 3 | High | US-REG-001 |
| US-REG-005 | Add Multiple Identifiers | 3 | High | US-REG-001, BR-PID-004 |
| US-REG-006 | Link Guardian for Paediatric Patient | 3 | High | US-REG-001, BR-CLIN-006 |
| US-REG-007 | Record Allergies and Chronic Conditions | 5 | Critical | US-REG-001 |
| US-REG-008 | Merge Duplicate Patient Records | 5 | High | US-REG-001, BR-PID-003 |
| US-REG-009 | EMPI Probabilistic Matching | 8 | High | US-REG-001, BR-PID-001 |
| US-REG-010 | Triage Queue Assignment | 3 | Critical | US-REG-001, BR-CLIN-001 |

**Technical Tasks:**

- Patient profile UI (Tabler): demographics, photo, identifiers, allergies, guardian panel
- EMPI matching algorithm: Soundex + Metaphone adapted for African naming patterns (BR-PID-001)
- Auto-save implementation for registration forms (BR-DATA-005)
- Image compression pipeline for patient photos (max 512 KB)
- `global_patients` table population and cross-tenant identity layer

**Key Risks:**

- EMPI algorithm (8 points) is the most complex story in the sprint; accuracy testing against African naming patterns requires a representative test dataset
- Sprint is at 46 points, 6 above baseline velocity; monitor daily and defer US-REG-008 (merge) if velocity target is missed

---

### Sprint 3: OPD Core (Weeks 5-6)

**Sprint Goal:** Deliver the outpatient clinical consultation workflow from queue to diagnosis, so that a doctor can see patients, record SOAP notes, enter diagnoses, and request investigations.

**Capacity:** 42 story points

| Story ID | Story Title | Points | Priority | Dependencies |
|---|---|---|---|---|
| US-OPD-001 | Doctor's Queue with Triage Priority | 5 | Critical | US-REG-010 (triage queue) |
| US-OPD-002 | Triage: Vital Signs Entry | 5 | Critical | US-REG-010 |
| US-OPD-003 | Clinical Consultation: SOAP Notes | 5 | Critical | US-OPD-001 |
| US-OPD-004 | Diagnosis Entry with ICD-10 Search | 5 | Critical | US-OPD-003, BR-DATA-006 |
| US-OPD-005 | Investigation Requests (Lab, Radiology) | 5 | Critical | US-OPD-003 |
| US-OPD-006 | Clinical Notes History | 3 | High | US-OPD-003 |
| US-OPD-007 | NEWS2 Early Warning Score | 5 | High | US-OPD-002, BR-CLIN-007 |
| US-OPD-008 | Single-Page OPD Summary UI | 5 | High | US-OPD-003, US-OPD-004, US-OPD-005 |
| US-OPD-009 | Auto-Save for Clinical Forms | 4 | Critical | BR-DATA-005 |

**Technical Tasks:**

- ICD-10 code database import and searchable index (typeahead, min 3 characters)
- Real-time queue updates (polling or WebSocket)
- NEWS2 score calculation engine with Sub-Saharan Africa baseline adjustments (BR-CLIN-007)
- Clinical data audit trail logging (immutable append-only)
- HMIS 105 Section 1 auto-tally hooks (BR-HMIS-001)

**Key Risks:**

- ICD-10 dataset is large (approximately 70,000 codes); search performance must meet the 1-second response target
- NEWS2 population-adjusted thresholds require clinical validation; flag as `[CONTEXT-GAP]` if no validated African thresholds are available

---

### Sprint 4: OPD Prescribing and Clinical Decision Support (Weeks 7-8)

**Sprint Goal:** Deliver safe prescribing with drug interaction checking, paediatric dosing safeguards, and Five Rights CPOE enforcement, so that medication safety is embedded from the first prescription.

**Capacity:** 35 story points

| Story ID | Story Title | Points | Priority | Dependencies |
|---|---|---|---|---|
| US-RX-001 | Prescription Writing (generic + brand) | 5 | Critical | US-OPD-003 |
| US-RX-002 | Stock-Aware Prescribing | 3 | High | US-RX-001, BR-RX-002 |
| US-RX-003 | Drug Interaction Checking (4-Tier Alerts) | 8 | Critical | US-RX-001, BR-CLIN-004, SZ-06 (drug DB) |
| US-RX-004 | Five Rights CPOE Enforcement | 5 | Critical | US-RX-001, BR-CLIN-008 |
| US-RX-005 | Paediatric Weight-Based Dosing | 5 | Critical | US-RX-001, BR-CLIN-006 |
| US-RX-006 | Tall Man Lettering for LASA Drugs | 3 | High | US-RX-001, BR-RX-003 |
| US-RX-007 | NEWS2 Alert Integration in Prescribing | 3 | High | US-OPD-007, US-RX-001 |
| US-RX-008 | Prescribing Authority Enforcement | 3 | Critical | US-RX-001, BR-CLIN-002 |

**Technical Tasks:**

- Drug formulary database schema and seed data (generic names, brands, strengths, routes, frequencies)
- CDS engine: rule evaluation pipeline for drug interactions, dosing limits, allergy cross-checks
- LASA drug list management interface for pharmacy lead
- Prescription audit trail (Tier 3 and Tier 4 override logging per BR-CLIN-004)
- CDS unit tests: positive, negative, boundary, and override scenarios (100% coverage required for CDS)

**Key Risks:**

- Drug interaction checking (8 points) is the highest-risk story in Phase 1; the CDS engine must fire correctly for all 4 tiers and must never silently suppress a Fatal alert
- Drug interaction database quality directly determines CDS accuracy; verify coverage of the Uganda Essential Medicines List

---

### Sprint 5: Laboratory (Weeks 9-10)

**Sprint Goal:** Deliver the laboratory workflow from sample collection to result validation, so that lab technicians can process requests, enter results with reference ranges, and trigger critical value alerts.

**Capacity:** 48 story points

| Story ID | Story Title | Points | Priority | Dependencies |
|---|---|---|---|---|
| US-LAB-001 | Lab Request from Clinical Screen | 5 | Critical | US-OPD-005 |
| US-LAB-002 | Sample Collection with Barcode Generation | 5 | Critical | US-LAB-001 |
| US-LAB-003 | Specimen Tracking Workflow | 5 | High | US-LAB-002 |
| US-LAB-004 | Result Entry with Reference Ranges and Auto-Flag | 5 | Critical | US-LAB-001 |
| US-LAB-005 | Critical Value Alerts with Escalation Cascade | 8 | Critical | US-LAB-004, BR-CLIN-003 |
| US-LAB-006 | Result Validation by Supervisor | 3 | High | US-LAB-004 |
| US-LAB-007 | QC Records | 3 | High | US-LAB-004 |
| US-LAB-008 | HL7 v2 Gateway (Analyser Interface) | 8 | High | US-LAB-004 |
| US-LAB-009 | LOINC Test Definitions | 3 | High | US-LAB-001 |
| US-LAB-010 | Lab Dashboard and Turnaround Time Tracking | 3 | High | US-LAB-003 |

**Technical Tasks:**

- Barcode generation library integration (Code 128 for specimen labels)
- HL7 v2 message parser for analyser integration (Cobas, Mindray, Sysmex)
- LOINC test code database import
- Critical value threshold configuration per test per facility
- Escalation cascade timer service (30 min to doctor, 60 min to ward sister, then Facility Admin per BR-CLIN-003)
- HMIS 105 Section 2 auto-tally hooks (BR-HMIS-001)

**Key Risks:**

- Sprint is at 48 points, 8 above baseline velocity; HL7 v2 gateway (8 points) and critical value alerts (8 points) are both high-complexity stories
- If velocity is tracking below target at mid-sprint, defer US-LAB-008 (HL7 gateway) to Sprint 8 and reduce to 40 points
- HL7 v2 analyser integration requires access to test equipment or a simulator; confirm availability before sprint commitment

---

### Sprint 6: Pharmacy and Dispensing (Weeks 11-12)

**Sprint Goal:** Deliver the pharmacy dispensing workflow with stock management, so that pharmacists can dispense prescriptions, manage inventory, and track controlled substances.

**Capacity:** 49 story points

| Story ID | Story Title | Points | Priority | Dependencies |
|---|---|---|---|---|
| US-PH-001 | Prescription Queue from OPD | 3 | Critical | US-RX-001 |
| US-PH-002 | Dispensing with Stock Deduction | 5 | Critical | US-PH-001 |
| US-PH-003 | Generic Substitution with Doctor Notification | 5 | High | US-PH-002, BR-CLIN-002 |
| US-PH-004 | Dispensing Label Generation | 3 | High | US-PH-002 |
| US-PH-005 | Partial Dispensing with Pending Balance | 3 | High | US-PH-002 |
| US-PH-006 | Narcotic/Controlled Drug Register | 5 | Critical | US-PH-002, BR-RX-001 |
| US-PH-007 | Stock Management: GRN, Transfer, Adjust | 5 | Critical | -- |
| US-PH-008 | Expiry Tracking (90-Day Flag) | 3 | High | US-PH-007 |
| US-PH-009 | Minimum Stock Level Alerts | 3 | High | US-PH-007 |
| US-PH-010 | Drug Formulary Management | 5 | High | US-PH-007 |
| US-PH-011 | Medication Reconciliation | 5 | Critical | US-PH-002, BR-CLIN-005 |
| US-PH-012 | Stock Valuation (FIFO) | 4 | High | US-PH-007 |

**Technical Tasks:**

- Pharmacy dispensing UI with prescription preview, stock levels, and substitution workflow
- Stock movement ledger: GRN, transfer, adjustment with full audit trail
- Barcode scanning for drug packs during GRN
- Narcotic register with running balance and discrepancy alerting (BR-RX-001)
- Expiry date batch tracking and 90-day warning report
- Medication reconciliation form generation at care transitions (BR-CLIN-005)

**Key Risks:**

- Sprint is at 49 points, the highest in Phase 1; this reflects the breadth of pharmacy operations
- If velocity is tracking below target, defer US-PH-012 (stock valuation) and US-PH-010 (formulary management) to Sprint 8, reducing to 40 points
- Narcotic register accuracy is a regulatory requirement; testing must include physical count reconciliation scenarios

---

### Sprint 7: Billing, Payments, and Appointments (Weeks 13-14)

**Sprint Goal:** Deliver cash billing, mobile money payments, and appointment scheduling, so that the facility can collect revenue, reconcile daily cash, and manage patient appointments.

**Capacity:** 39 story points

| Story ID | Story Title | Points | Priority | Dependencies |
|---|---|---|---|---|
| US-BIL-001 | Patient Account with Real-Time Charge Accumulation | 5 | Critical | US-OPD-003, BR-FIN-001 |
| US-BIL-002 | Auto-Billing from Clinical Screens | 5 | Critical | US-BIL-001, BR-FIN-001 |
| US-BIL-003 | Configurable Price List and Category Pricing | 3 | Critical | US-BIL-001 |
| US-BIL-004 | Cash Payment and Receipt Generation | 3 | Critical | US-BIL-001 |
| US-BIL-005 | Mobile Money Integration (MTN MoMo / Airtel Money) | 5 | High | US-BIL-001, BR-FIN-003 |
| US-BIL-006 | Daily Cashier Reconciliation | 3 | High | US-BIL-004, BR-FIN-004 |
| US-BIL-007 | Missing Charge Detection | 3 | High | US-BIL-002, BR-FIN-008 |
| US-APT-001 | Appointment Booking | 5 | High | Sprint 1 (auth) |
| US-APT-002 | SMS Appointment Reminders | 3 | High | US-APT-001 |
| US-APT-003 | Queue Integration from Appointments | 4 | High | US-APT-001, US-OPD-001 |

**Technical Tasks:**

- Billing engine: charge accumulation from lab, pharmacy, OPD, and procedure events
- Price list management UI with category-based pricing tiers
- Receipt generation (thermal printer and PDF)
- MTN MoMo API and Airtel Money API integration with webhook handlers
- Unmatched payment suspense account and daily report (BR-FIN-003)
- Cashier session management: open, close, reconcile (BR-FIN-004)
- SMS gateway integration (Africa's Talking API) for appointment reminders
- Appointment calendar UI with doctor availability and walk-in slot management

**Key Risks:**

- Mobile money API integration depends on MTN and Airtel developer portal access and sandbox availability; initiate API credentials request in Sprint 6
- SMS gateway requires Africa's Talking account and sender ID registration; initiate in Sprint 6

---

### Sprint 8: RBAC, Integration Testing, and Hardening (Weeks 15-16)

**Sprint Goal:** Deliver role-based access control with 18 default roles, emergency access, and a comprehensive audit trail. Complete end-to-end integration testing, performance testing, and security hardening so that the system is ready for UAT.

**Capacity:** 31 story points

| Story ID | Story Title | Points | Priority | Dependencies |
|---|---|---|---|---|
| US-RBAC-001 | 18 Default Roles with Permission Matrix | 5 | Critical | Sprint 1 (auth) |
| US-RBAC-002 | Custom Role Creation | 3 | High | US-RBAC-001 |
| US-RBAC-003 | ABAC for Sensitive Records (HIV, psychiatric) | 5 | Critical | US-RBAC-001 |
| US-RBAC-004 | Audit Trail (Immutable) | 5 | Critical | BR-DATA-004, PDPA 2019 Section 24 |
| US-RBAC-005 | Emergency Access (Break-the-Glass) | 5 | Critical | US-RBAC-001, BR-DATA-002 |
| US-RBAC-006 | Role-Scoped Dashboard | 3 | High | US-RBAC-001 |
| US-INT-001 | End-to-End Integration Test Suite | 5 | Critical | All Sprint 1-7 stories |

**Technical Tasks (non-story-pointed, Sprint 8 dedicated):**

- End-to-end integration tests: patient journey from registration through OPD, lab, pharmacy, billing, and discharge
- Performance testing: confirm P95 API response time under 500 ms with 50 concurrent users per facility
- Security hardening: `composer audit`, OWASP dependency check, HTTP security headers, rate limiting
- Bug fixes from Sprints 1-7 (reserve 20% of capacity = approximately 6 points equivalent)
- Audit trail tamper-proof implementation: append-only log table with hash chain
- ABAC policy engine for sensitive record types (HIV status, psychiatric notes)
- Break-the-glass workflow: emergency access with 2-factor patient confirmation, 24-hour expiry, SMS notification (BR-DATA-002)
- DOCUMENTATION-STATUS.md update for all Phase 1 modules

**Key Risks:**

- Integration testing may uncover cross-module defects that require fixes in earlier module code; reserve capacity for rework
- Performance testing requires a representative data set; generate synthetic data (at least 10,000 patients, 50,000 encounters) during Sprint 7

---

## 4 Post-Sprint 8: UAT and Go-Live Preparation (2 Weeks)

**Duration:** 2 weeks (Weeks 17-18)
**Purpose:** Validate the system with real users at pilot facilities before production go-live.

### Week 17: User Acceptance Testing

| # | Activity | Duration | Participants |
|---|---|---|---|
| PS-01 | Deploy to UAT environment with synthetic data | 1 day | Developer |
| PS-02 | UAT with Pilot Facility 1: private clinic (small, OPD-focused) | 2 days | Receptionist, Doctor, Pharmacist, Cashier |
| PS-03 | UAT with Pilot Facility 2: mission hospital (multi-department) | 2 days | Lab Technician, Nurse, Facility Admin |

### Week 18: Stabilisation and Go-Live

| # | Activity | Duration | Participants |
|---|---|---|---|
| PS-04 | UAT with Pilot Facility 3: HC IV (HMIS reporting focus) | 1 day | Records Officer, Facility Admin |
| PS-05 | Bug fixes from UAT findings | 2 days | Developer |
| PS-06 | Performance optimisation based on UAT load patterns | 1 day | Developer |
| PS-07 | Go-live preparation: production environment, DNS, SSL, backups, monitoring | 1 day | Developer |

**UAT Exit Criteria:**

- [ ] All Critical and High priority bugs fixed
- [ ] 3 pilot facilities have signed UAT acceptance
- [ ] End-to-end patient journey completed successfully at each facility
- [ ] Cash billing reconciliation rate at 95% or above (Phase 1 success criterion)
- [ ] P95 API response time under 500 ms confirmed under UAT load
- [ ] CDS rules validated: drug interaction alerts fire at correct severity tier
- [ ] Clinical safety sign-off from clinical advisor
- [ ] Data backup and restore procedure tested
- [ ] Rollback procedure documented and tested

---

## 5 Sprint Point Summary

| Sprint | Name | Points | Cumulative |
|---|---|---|---|
| 0 | Pre-Development Foundation | -- | -- |
| 1 | Foundation and Authentication | 38 | 38 |
| 2 | Patient Registration | 46 | 84 |
| 3 | OPD Core | 42 | 126 |
| 4 | OPD Prescribing and CDS | 35 | 161 |
| 5 | Laboratory | 48 | 209 |
| 6 | Pharmacy and Dispensing | 49 | 258 |
| 7 | Billing, Payments, and Appointments | 39 | 297 |
| 8 | RBAC, Integration, and Hardening | 31 | 328 |
| **Total** | | **328** | |

**Average velocity required:** 41 points per sprint (328 / 8 sprints)

---

## 6 Dependency Chain

The following critical path dependencies must be completed in sequence. Delays on any critical path item cascade to all downstream sprints.

```
Sprint 0: Environment + Schema + CI
    |
Sprint 1: Auth + Tenant Isolation
    |
    +---> Sprint 2: Patient Registration + EMPI
    |         |
    |         +---> Sprint 3: OPD Core (Queue, Triage, SOAP, ICD-10, Investigations)
    |                   |
    |                   +---> Sprint 4: Prescribing + CDS Engine
    |                   |         |
    |                   |         +---> Sprint 6: Pharmacy Dispensing + Stock
    |                   |
    |                   +---> Sprint 5: Laboratory (requests flow from OPD)
    |
    +---> Sprint 7: Billing (charges from OPD, Lab, Pharmacy) + Appointments
    |
    +---> Sprint 8: RBAC + Integration Testing + Hardening
```

---

## 7 Risk Register (Sprint-Level)

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Solo developer illness or unavailability (1+ week) | Medium | High | Maintain Sprint Journal for continuity; all work in version control with Conventional Commits |
| Drug interaction database licensing delay | Low | Critical | Initiate in Sprint Zero; fallback to open-source interaction dataset (reduced coverage) |
| Mobile money API sandbox unavailability | Medium | Medium | Start API credential requests in Sprint 6; fallback to manual payment entry with MoMo reference |
| Sprint 5 and 6 exceed velocity (48 and 49 points) | High | Medium | Pre-identify deferral candidates: US-LAB-008, US-PH-012, US-PH-010; move to Sprint 8 if needed |
| HL7 analyser integration requires physical equipment | Medium | Medium | Use HL7 simulator for development and testing; defer physical analyser testing to UAT |
| EMPI accuracy for African naming patterns | Medium | High | Build representative test dataset with compound surnames, clan names, and spelling variations |
| Performance target miss at 50 concurrent users | Low | High | Run load tests from Sprint 5 onward; optimise database queries and add caching incrementally |

---

## Module 32: AI Intelligence

Module 32 (AI Intelligence) is provider-agnostic and supports OpenAI, Anthropic, DeepSeek, and Gemini via a shared `AIProviderInterface`. It exposes 6 capabilities: Clinical Documentation, ICD Coding Assist, Differential Diagnosis, Patient Plain-Language Summary, Claim Scrubbing, and Outbreak Alert. Billing is either `credit_pack` or `flat_fee` per tenant configuration.

AI Intelligence stories require sandbox API keys for the target provider to be configured in `.env.testing` before sprint planning can accept those stories as ready. Stories that arrive at Sprint Planning without confirmed sandbox access cannot be committed to the sprint.

---

## 8 Definition Cross-References

- **Definition of Done:** `07-agile-artifacts/02-dod/01-definition-of-done.md`
- **Definition of Ready:** `07-agile-artifacts/03-dor/01-definition-of-ready.md`
- **User Stories:** `02-requirements-engineering/02-user-stories/01-user-stories.md`
- **Business Rules:** `_context/business_rules.md`
- **Quality Standards:** `_context/quality_standards.md`
- **Metrics and Phase Gates:** `_context/metrics.md`
