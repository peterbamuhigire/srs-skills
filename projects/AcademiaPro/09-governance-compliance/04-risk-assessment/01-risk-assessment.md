# Risk Assessment — Academia Pro

## 1 Document Information

| Property | Value |
|---|---|
| **Project** | Academia Pro — Multi-Tenant SaaS School Management Platform |
| **Owner** | Peter, Chwezi Core Systems |
| **Standards** | ISO 31000:2018 (Risk Management), IEEE 1012-2016 (V&V) |
| **Version** | 1.0 |
| **Date** | 2026-04-03 |
| **Status** | Draft — Pending Consultant Review |

---

## 2 Risk Assessment Methodology

### 2.1 ISO 31000 Framework

This assessment follows the ISO 31000:2018 risk management process: establish context, identify risks, analyse risks, evaluate risks, and treat risks. The scope is the full Academia Pro product lifecycle from Phase 1 development through Phase 12 (Pan-Africa expansion), with emphasis on Phase 1 through Phase 4 where the highest concentration of foundational technical risk exists.

Risk identification draws from the following sources:

- `_context/gap-analysis.md` — 8 HIGH-priority and 12 MEDIUM-priority gaps
- `_context/business_rules.md` — 30+ binding business rules
- `_context/vision.md` — 5 strategic goals and success criteria
- `_context/domain.md` — Uganda regulatory environment (PDPO 2019, UNEB, EMIS, BoU)

### 2.2 Probability Scale

| Level | Label | Description | Frequency |
|---|---|---|---|
| 1 | Rare | Event requires exceptional circumstances | < 1 occurrence per 5 years |
| 2 | Unlikely | Event could occur but is not expected | 1 occurrence per 2–5 years |
| 3 | Possible | Event could occur at some point | 1 occurrence per 1–2 years |
| 4 | Likely | Event will probably occur in most circumstances | 1–3 occurrences per year |
| 5 | Almost Certain | Event is expected to occur regularly | > 3 occurrences per year |

### 2.3 Impact Scale

| Level | Label | Financial | Operational | Compliance | Reputational |
|---|---|---|---|---|---|
| 1 | Negligible | < UGX 1M | < 1 hr downtime | Advisory notice | No public awareness |
| 2 | Minor | UGX 1M–10M | 1–4 hr downtime | Minor non-conformity | Limited user complaints |
| 3 | Moderate | UGX 10M–50M | 4–24 hr downtime | Formal warning | Social media complaints |
| 4 | Major | UGX 50M–200M | 1–7 day disruption | Enforcement action | Press coverage |
| 5 | Catastrophic | > UGX 200M | > 7 day outage | Licence revocation or lawsuit | Mass school churn |

### 2.4 Risk Scoring Matrix

$$RiskScore = Probability \times Impact$$

|  | **Impact 1** | **Impact 2** | **Impact 3** | **Impact 4** | **Impact 5** |
|---|---|---|---|---|---|
| **Prob 5** | 5 | 10 | 15 | 20 | 25 |
| **Prob 4** | 4 | 8 | 12 | 16 | 20 |
| **Prob 3** | 3 | 6 | 9 | 12 | 15 |
| **Prob 2** | 2 | 4 | 6 | 8 | 10 |
| **Prob 1** | 1 | 2 | 3 | 4 | 5 |

### 2.5 Risk Tolerance Thresholds

| Risk Level | Score Range | Response Requirement |
|---|---|---|
| Low | 1–4 | Accept or monitor; no immediate action required |
| Medium | 5–9 | Mitigate; assign owner and implement controls before Phase 2 |
| High | 10–15 | Mitigate urgently; controls must be in place before the risk materialises |
| Critical | 16–25 | Avoid or transfer; escalate to project owner immediately; block deployment until resolved |

---

## 3 Risk Identification

### 3.1 Technical Risks

- **RISK-T01:** Tenant isolation breach — a query or API response leaks data belonging to Tenant A to Tenant B due to a missing `tenant_id` filter in a Repository method or raw SQL query.
- **RISK-T02:** UNEB grading engine inaccuracy — the automated grade computation for PLE, UCE, or UACE produces a result that differs from the official UNEB manual computation for 1 or more candidates.
- **RISK-T03:** Database performance degradation at scale — query response time exceeds the 500 ms P95 threshold when the system serves 500 concurrent tenants with 200,000+ student records.
- **RISK-T04:** Offline sync conflict — a teacher submits attendance or marks offline, and a conflicting record was entered online by the head teacher during the same period, resulting in data loss or incorrect records.
- **RISK-T05:** Payment double-processing — the same fee payment is recorded twice (via manual entry race condition or SchoolPay webhook replay), inflating the school's revenue and generating a duplicate receipt.
- **RISK-T06:** Meilisearch index sync lag — search results for recently enrolled students or updated fee records are stale for more than 30 seconds, causing bursars to record payments against outdated balances.

### 3.2 Operational Risks

- **RISK-O01:** Solo developer bus factor — Peter is the sole developer, architect, and system administrator. Illness, unavailability, or departure for more than 2 weeks halts all development, support, and incident response.
- **RISK-O02:** Single-VPS infrastructure failure — the production environment runs on a single AWS VPS. Hardware failure, region outage, or misconfigured deployment causes total service unavailability exceeding the 4-hour RTO.
- **RISK-O03:** SchoolPay API downtime — SchoolPay's payment gateway becomes unavailable during peak fee collection periods (Term 1 opening week), blocking all electronic fee payments for an indeterminate period.
- **RISK-O04:** Africa's Talking SMS delivery failure — SMS notifications (fee reminders, attendance alerts, OTPs) fail to deliver due to Africa's Talking API downtime or telco gateway congestion, with delivery rates dropping below 90%.
- **RISK-O05:** AWS region unavailability — the chosen AWS region (af-south-1, Cape Town) experiences an outage lasting more than 4 hours, exceeding the RTO target.

### 3.3 Compliance Risks

- **RISK-C01:** PDPO 2019 violation — Chwezi Core Systems processes personal data of minors (students under 18) without completing Data Controller registration with the Personal Data Protection Office, or fails to execute Data Processing Agreements with subscribing schools.
- **RISK-C02:** UNEB registration export format non-compliance — the UNEB export function produces output that does not match the official UNEB registration file format, causing rejection by UNEB's system. *Note: core registration fields (name, date of birth, gender, NIN/LIN, nationality, district, school centre number) are now documented from the MoES EMIS Secondary School Manual. The exact UNEB electronic registration file format still requires direct UNEB ICT department liaison to confirm column order, encoding, and submission protocol.*
- **RISK-C03:** EMIS export rejection — the MoES EMIS export function generates data that fails validation against the MoES EMIS data dictionary, causing schools to miss statutory reporting deadlines. *Note: a complete EMIS data dictionary has been created from 5 official MoES documents (2023 Learner Registration Form, 2024 Staff Registration Form, International Learner Form, Primary School Manual, Secondary School Manual). This significantly reduces the probability of field-level validation failures.*
- **RISK-C04:** BoU Payment Systems Operator licence delay — direct mobile money integration (MTN MoMo, Airtel Money) in Phase 3 requires a BoU PSO licence. Licence approval delay exceeds 6 months, blocking the Phase 3 payment module.

### 3.4 Project Risks

- **RISK-P01:** Scope creep across 12 phases — feature requests from pilot schools or market pressure cause Phase 1 scope to expand beyond the 49 specified functional requirements, delaying launch by more than 3 months.
- **RISK-P02:** School adoption slower than target — fewer than 50 schools subscribe within the first 12 months (10% of the 500-school, 24-month target), creating a revenue gap that threatens operational sustainability.
- **RISK-P03:** Competing products — an established competitor (e.g., QuickSchools, Zeraki, or a well-funded local entrant) launches a Uganda-localised product with UNEB grading and MoMo integration before Academia Pro reaches Phase 8.
- **RISK-P04:** Funding and revenue gap — subscription revenue from early adopters is insufficient to cover AWS hosting, SchoolPay transaction fees, Africa's Talking SMS costs, and Peter's living expenses during the 12-month pre-revenue period.
- **RISK-P05:** Pilot school data quality — the first pilot school provides incomplete or inconsistent student data during migration (Excel import), causing data integrity errors that undermine confidence in the platform.

---

## 4 Risk Analysis Matrix

The following grid plots each risk by its assessed probability and impact. Risks in the shaded upper-right quadrant (score $\geq$ 16) are Critical.

|  | **Impact 1** | **Impact 2** | **Impact 3** | **Impact 4** | **Impact 5** |
|---|---|---|---|---|---|
| **Prob 5** |  |  | RISK-O01 |  |  |
| **Prob 4** |  |  | RISK-O04, RISK-P05 | RISK-P01, RISK-P04 | RISK-T02 |
| **Prob 3** |  | RISK-T06 | RISK-T04, RISK-O03, RISK-C04, RISK-P02 | RISK-T03, RISK-C01, RISK-P03 |  |
| **Prob 2** |  |  | RISK-O05 | RISK-T01, RISK-C02 | RISK-T05 |
| **Prob 1** |  |  |  | RISK-C03 |  |

---

## 5 Risk Register

| Risk ID | Category | Description | Prob | Impact | Score | Response | Mitigation Action | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| RISK-T01 | Technical | Tenant data leak: missing `tenant_id` filter exposes Tenant A data to Tenant B | 2 | 4 | 8 | Mitigate | Enforce `tenant_id` via Repository base class global scope + CI static analysis rule rejecting raw queries without `tenant_id` parameter (HIGH-001 spec) | Peter | Open |
| RISK-T02 | Technical | UNEB grading engine produces incorrect PLE/UCE/UACE results for $\geq$ 1 candidate | 4 | 5 | 20 | Mitigate | Validate engine against 100+ UNEB sample mark sheets (UG-NFR-001). Implement property-based tests covering all grade boundary values. Block release until 0 discrepancies confirmed | Peter | Open |
| RISK-T03 | Technical | API P95 latency exceeds 500 ms at 500-tenant scale (200,000+ student rows) | 3 | 4 | 12 | Mitigate | Add composite indexes on `(tenant_id, <lookup_column>)` for all high-frequency queries. Implement query result caching (Redis) for read-heavy endpoints. Load test at 2x target volume before Phase 8 go-live | Peter | Open |
| RISK-T04 | Technical | Offline sync conflict overwrites valid online attendance/marks entry | 3 | 3 | 9 | Mitigate | Implement last-write-wins with server timestamp comparison. Log all conflict resolutions with both values. Alert the teacher when a conflict is auto-resolved (MEDIUM-011 gap) | Peter | Open |
| RISK-T05 | Technical | Double fee payment recorded via manual entry race condition or SchoolPay webhook replay | 2 | 5 | 10 | Mitigate | Enforce `UNIQUE` constraint on `fee_payments.external_reference`. Implement 5-minute duplicate detection window (BR-FEE-005). Return original receipt on duplicate submission | Peter | Open |
| RISK-T06 | Technical | Meilisearch index lags server state by > 30 seconds, causing stale search results | 3 | 2 | 6 | Accept | Monitor index sync latency. Set Meilisearch task queue alert threshold at 30 seconds. Fallback to direct DB search if index lag exceeds 60 seconds | Peter | Open |
| RISK-O01 | Operational | Solo developer incapacitated for > 2 weeks — all development, support, and ops halted | 5 | 3 | 15 | Mitigate | Document all infrastructure credentials in encrypted vault (1Password). Write runbooks for critical ops (deployment, backup restore, incident response). Identify 1 freelance Laravel developer for emergency engagement within 48 hours | Peter | Open |
| RISK-O02 | Operational | Single-VPS failure causes total outage exceeding 4-hour RTO | 3 | 3 | 9 | Mitigate | Implement automated daily DB backups to S3 (cross-region). Test restore procedure quarterly. Prepare AMI snapshot for rapid VPS re-provisioning. Target: restore to new instance within 2 hours | Peter | Open |
| RISK-O03 | Operational | SchoolPay API unavailable during peak fee collection window (Term 1 opening) | 3 | 3 | 9 | Mitigate | Implement manual cash entry as primary fallback. Queue failed SchoolPay webhook deliveries for retry (exponential backoff, 24-hour retention). Display "Online payments temporarily unavailable" banner when health check fails | Peter | Open |
| RISK-O04 | Operational | Africa's Talking SMS delivery rate drops below 90% during peak periods | 4 | 3 | 12 | Mitigate | Implement secondary SMS provider (e.g., Yo! Payments Uganda) as automatic failover when primary delivery rate drops below 85% over a 1-hour window. Log all SMS delivery statuses for reconciliation | Peter | Open |
| RISK-O05 | Operational | AWS af-south-1 region outage exceeds 4 hours | 2 | 3 | 6 | Accept | Monitor AWS Health Dashboard. Maintain off-region S3 backup (eu-west-1). Accept residual risk — multi-region active-active is not cost-justified for Phase 1 | Peter | Open |
| RISK-C01 | Compliance | Processing student PII without PDPO Data Controller registration or school DPAs | 3 | 4 | 12 | Avoid | Complete PDPO registration before Phase 8 go-live. Draft DPA template and require school signature during onboarding. Spec complete (HIGH-008 resolved) — execution pending | Peter | Open |
| RISK-C02 | Compliance | UNEB registration export rejected due to incorrect file format | 2 | 4 | 8 | Mitigate | Core registration fields documented from EMIS Secondary Manual. Obtain exact UNEB electronic submission format (column order, encoding, protocol) via UNEB ICT liaison. Build export module only after format is confirmed. Validate output against sample file before release. *Partially resolved — field-level gap closed; submission format gap remains.* | Peter | Open |
| RISK-C03 | Compliance | EMIS export fails MoES validation, causing schools to miss statutory deadlines | 1 | 4 | 4 | Mitigate | Complete EMIS data dictionary created from 5 official MoES documents (2023 Learner Registration, 2024 Staff Registration, International Learner Form, Primary Manual, Secondary Manual). Build EMIS export validator as automated test. Test against MoES staging portal before Phase 8. *Resolved — data dictionary gap closed.* | Peter | Open |
| RISK-C04 | Compliance | BoU PSO licence approval delayed > 6 months, blocking Phase 3 direct MoMo integration | 3 | 3 | 9 | Transfer | Use SchoolPay as licensed payment intermediary for Phases 1–2. Begin BoU licence application 6 months before Phase 3 target date. Accept SchoolPay transaction fee margin until direct licence is obtained | Peter | Open |
| RISK-P01 | Project | Scope creep — pilot school requests expand Phase 1 beyond 49 FRs, delaying launch > 3 months | 4 | 4 | 16 | Mitigate | Enforce phase gate sign-off (Water-Scrum-Fall methodology). Log all feature requests to backlog; do not promote to Phase 1 scope without formal change request. Communicate Phase 1 boundary to pilot schools during onboarding | Peter | Open |
| RISK-P02 | Project | Fewer than 50 schools subscribe within 12 months of launch | 3 | 3 | 9 | Mitigate | Offer 1-term free trial for first 20 schools. Partner with Uganda Private Schools Association for referral channel. Target schools already using SchoolPay (warm leads with digital payment experience) | Peter | Open |
| RISK-P03 | Project | Competitor launches Uganda-localised school management SaaS with UNEB + MoMo before Phase 8 | 3 | 4 | 12 | Accept | Accelerate Phase 1–4 timeline. Differentiate on KUPAA micro-payment model, offline-first Android app, and depth of UNEB grading accuracy. Monitor competitor landscape quarterly | Peter | Open |
| RISK-P04 | Project | Subscription revenue insufficient to cover hosting, APIs, and operational costs during pre-revenue period | 4 | 4 | 16 | Mitigate | Model break-even point (target: 80 schools at UGX 150,000/school/term). Maintain 12-month personal runway before Phase 8 launch. Seek grant funding from Uganda Innovation Fund or Hive Colab if runway falls below 6 months | Peter | Open |
| RISK-P05 | Project | Pilot school provides incomplete or inconsistent student data during Excel migration | 4 | 3 | 12 | Mitigate | Provide structured Excel import template with validation rules (HIGH-007 spec). Implement skip-and-report error mode. Conduct data cleaning workshop with pilot school bursar before import | Peter | Open |

---

## 6 Risk Response Strategies for High and Critical Risks

### 6.1 RISK-T02 (Critical, Score 20) — UNEB Grading Engine Inaccuracy

**Strategy:** Mitigate through exhaustive validation.

1. Obtain official UNEB grading rules documentation for PLE, UCE, and UACE from UNEB or MoES.
2. Build a test suite of $\geq$ 100 candidate mark sheets per curriculum level, including all boundary cases (exact division cut-off scores, subjects with missing marks, candidates with fewer than the required subject count).
3. Implement property-based tests asserting: $\forall c \in Candidates: gradeEngine(c) = manualComputation(c)$.
4. Execute the test suite as a CI gate — any discrepancy blocks the build.
5. Engage a secondary verifier (e.g., a head teacher with UNEB marking experience) to manually verify 20 edge-case results.

### 6.2 RISK-P01 (Critical, Score 16) — Scope Creep

**Strategy:** Mitigate through governance.

1. Freeze Phase 1 scope at the 49 functional requirements documented in the SRS.
2. All feature requests from pilot schools are logged in a Phase 2+ backlog with a formal change request form.
3. Phase gate review (per Water-Scrum-Fall methodology) must confirm that no un-approved requirements entered the sprint.
4. Peter reviews the backlog monthly and promotes items only during phase planning.

### 6.3 RISK-P04 (Critical, Score 16) — Funding Gap

**Strategy:** Mitigate through financial planning.

1. Calculate monthly operational cost: AWS VPS ($\approx$ USD 50), domain and SSL ($\approx$ USD 20), Africa's Talking SMS ($\approx$ USD 30 at low volume), SchoolPay integration fee ($\approx$ USD 0 — per-transaction model).
2. Target break-even: 80 schools $\times$ UGX 150,000/term $\times$ 3 terms = UGX 36,000,000/year ($\approx$ USD 9,700).
3. Maintain personal financial runway of $\geq$ 12 months before launch.
4. Apply to Uganda Innovation Fund, Hive Colab accelerator, or UNCDF fintech grant as supplementary funding.

### 6.4 RISK-O01 (High, Score 15) — Solo Developer Bus Factor

**Strategy:** Mitigate through documentation and contingency planning.

1. Store all infrastructure credentials and API keys in 1Password with emergency access configured for a trusted contact.
2. Write deployment runbooks covering: production deploy, database backup/restore, incident escalation, DNS failover.
3. Identify 1–2 freelance Laravel/React developers in the Kampala tech community who can provide emergency support within 48 hours under a pre-negotiated retainer or on-call agreement.
4. Maintain a `docs/ops/` directory with architecture diagrams and environment configuration so a replacement developer can orient within 1 day.

### 6.5 RISK-T03 (High, Score 12) — Database Performance at Scale

**Strategy:** Mitigate through indexing, caching, and load testing.

1. Add composite indexes: `(tenant_id, student_uid)`, `(tenant_id, class_id, term_id)`, `(tenant_id, created_at)` on all high-frequency tables.
2. Implement Redis caching for read-heavy endpoints (student list, fee balance, attendance summary) with 5-minute TTL.
3. Conduct load tests using k6 at 2x target volume (1,000 concurrent tenants, 400,000 student records) before Phase 8 go-live.
4. Establish a performance regression CI gate: any endpoint exceeding 500 ms P95 on the test dataset fails the build.

### 6.6 RISK-C01 (High, Score 12) — PDPO Non-Compliance

**Strategy:** Avoid through proactive registration.

1. Submit Data Controller registration to the Uganda Personal Data Protection Office before Phase 8 go-live.
2. Publish a privacy notice on the Academia Pro website meeting PDPO Section 12 minimum content requirements (per `09-governance-compliance/03-compliance/01-pdpo-compliance.md`).
3. Require each subscribing school to sign the Data Processing Agreement during onboarding — no school is activated without a signed DPA.
4. Implement technical controls: TLS 1.3 in transit, AES-256 at rest, RBAC enforcement, and audit logging for all PII access.

### 6.7 RISK-C02 (Medium, Score 8) and RISK-C03 (Low, Score 4) — UNEB/EMIS Format Non-Compliance

**Strategy:** Mitigate through specification acquisition and validation.

1. **RISK-C03 (EMIS) — substantially resolved.** A complete EMIS data dictionary has been compiled from 5 official MoES documents (2023 Learner Registration Form, 2024 Staff Registration Form, International Learner Form, Primary School Manual, Secondary School Manual). Build EMIS export validators against this dictionary. Test against MoES staging portal before Phase 8.
2. **RISK-C02 (UNEB) — partially resolved.** Core UNEB registration fields (name, DOB, gender, NIN/LIN, nationality, district, centre number) are documented from the EMIS Secondary Manual. The exact UNEB electronic submission format (column order, file encoding, upload protocol) still requires direct UNEB ICT department liaison. Do not build the UNEB export module until the submission format is confirmed.
3. Build automated validators that compare export output against the official schema before each release.

### 6.8 RISK-P03 (High, Score 12) — Competitor Threat

**Strategy:** Accept with acceleration.

1. Monitor the Uganda EdTech market quarterly (track QuickSchools Uganda, Zeraki, ESIS, SchoolApp).
2. Prioritise the 3 differentiators that competitors lack: KUPAA micro-payment model (no minimum payment), offline-first Android app for rural schools, and 100% UNEB grading accuracy.
3. Accelerate Phase 1–4 delivery to reduce time-to-market risk.

---

## 7 Residual Risk Assessment

After mitigation actions are implemented, the following residual risk scores apply:

| Risk ID | Initial Score | Residual Prob | Residual Impact | Residual Score | Residual Level |
|---|---|---|---|---|---|
| RISK-T01 | 8 | 1 | 4 | 4 | Low |
| RISK-T02 | 20 | 2 | 5 | 10 | High |
| RISK-T03 | 12 | 2 | 3 | 6 | Medium |
| RISK-T04 | 9 | 2 | 2 | 4 | Low |
| RISK-T05 | 10 | 1 | 5 | 5 | Medium |
| RISK-T06 | 6 | 3 | 1 | 3 | Low |
| RISK-O01 | 15 | 5 | 2 | 10 | High |
| RISK-O02 | 9 | 2 | 2 | 4 | Low |
| RISK-O03 | 9 | 3 | 2 | 6 | Medium |
| RISK-O04 | 12 | 2 | 2 | 4 | Low |
| RISK-O05 | 6 | 2 | 3 | 6 | Medium |
| RISK-C01 | 12 | 1 | 4 | 4 | Low |
| RISK-C02 | 8 | 1 | 4 | 4 | Low |
| RISK-C03 | 4 | 1 | 3 | 3 | Low |
| RISK-C04 | 9 | 3 | 2 | 6 | Medium |
| RISK-P01 | 16 | 2 | 4 | 8 | Medium |
| RISK-P02 | 9 | 3 | 3 | 9 | Medium |
| RISK-P03 | 12 | 3 | 4 | 12 | High |
| RISK-P04 | 16 | 3 | 3 | 9 | Medium |
| RISK-P05 | 12 | 2 | 2 | 4 | Low |

**Residual risk summary:** After mitigation, 3 risks remain High (RISK-T02, RISK-O01, RISK-P03). RISK-T02 remains High because UNEB grading accuracy is a zero-tolerance requirement and the test dataset has not yet been obtained. RISK-O01 remains High because the solo developer constraint is structural and cannot be fully mitigated without hiring. RISK-P03 remains High because competitor behaviour is outside project control. RISK-C02 and RISK-C03 have been reduced to Low following the creation of a complete EMIS data dictionary from 5 official MoES documents; RISK-C03 residual impact is also reduced to 3 (Moderate) because field-level validation failures are now preventable.

---

## 8 Risk Monitoring Plan

### 8.1 Review Cadence

| Activity | Frequency | Responsible |
|---|---|---|
| Risk register review | Monthly during active development; quarterly post-launch | Peter |
| Residual risk re-assessment | At each phase gate (Water-Scrum-Fall methodology) | Peter |
| Critical risk status check | Weekly during Phase 1–4 development | Peter |
| Post-incident risk update | Within 48 hours of any production incident | Peter |

### 8.2 Trigger Conditions

The following events require immediate risk register update and re-assessment:

- Any production incident affecting $\geq$ 10 tenants or lasting $\geq$ 1 hour
- A UNEB grading discrepancy reported by any school
- A PDPO Office inquiry or complaint notification
- SchoolPay API deprecation notice or contract change
- A competitor product launch announcement with Uganda localisation
- Subscription count falling $\geq$ 30% below the quarterly target
- Peter's unavailability exceeding 5 consecutive business days

### 8.3 Escalation Protocol

1. **Low risks (1–4):** Logged and monitored. No escalation required.
2. **Medium risks (5–9):** Peter assigns a mitigation action with a target completion date. Review at next monthly cycle.
3. **High risks (10–15):** Peter implements mitigation within 2 weeks. If mitigation is blocked, escalate to advisory contact (freelance developer or mentor).
4. **Critical risks (16–25):** Halt affected phase. Do not proceed past the current phase gate until the risk is reduced to High or below.

---

## 9 Risk Summary and Recommendations

### 9.1 Summary

This assessment identifies 20 risks across 4 categories:

| Category | Count | Critical | High | Medium | Low |
|---|---|---|---|---|---|
| Technical | 6 | 1 | 1 | 2 | 2 |
| Operational | 5 | 0 | 1 | 2 | 2 |
| Compliance | 4 | 0 | 1 | 2 | 1 |
| Project | 5 | 2 | 1 | 1 | 1 |
| **Total** | **20** | **3** | **4** | **7** | **6** |

The 3 Critical risks (score $\geq$ 16) are:

1. **RISK-T02** (Score 20) — UNEB grading inaccuracy. *Existential risk.* A single publicly reported grading error destroys school trust in the platform.
2. **RISK-P01** (Score 16) — Scope creep. Structural risk inherent to a 12-phase solo project.
3. **RISK-P04** (Score 16) — Funding gap. Revenue timing risk during the pre-launch period.

### 9.2 Recommendations

1. **Obtain UNEB sample mark sheets immediately.** RISK-T02 cannot be mitigated until test data is available. This is the single highest-priority external dependency. Initiate formal request to UNEB ICT department this week.
2. **Validate EMIS export against the compiled data dictionary.** RISK-C03 context gap is closed — the complete EMIS data dictionary has been created from 5 official MoES documents. Build automated EMIS export validators and test against MoES staging portal before Phase 8.
3. **Complete PDPO registration before any school processes live student data.** RISK-C01 is avoidable — the mitigation is administrative, not technical.
4. **Build financial runway model.** RISK-P04 requires a concrete month-by-month cash flow projection. Model 3 scenarios: pessimistic (20 schools in Year 1), baseline (80 schools), optimistic (150 schools).
5. **Write ops runbooks before Phase 8 go-live.** RISK-O01 is structural but its impact is reducible. Runbooks, credential vaults, and a named emergency contact are non-negotiable before production launch.
6. **Enforce phase gate discipline.** The Water-Scrum-Fall methodology already provides the governance mechanism for RISK-P01. The risk is that Peter relaxes the gate under time pressure. Treat phase gate sign-off as a binding commitment.

---

## 10 Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-04-03 | Peter (Chwezi Core Systems) | Initial risk assessment — 20 risks identified across 4 categories |
| 1.1 | 2026-04-03 | Peter (Chwezi Core Systems) | EMIS context gaps closed — RISK-C02 reduced to Medium (score 8), RISK-C03 reduced to Low (score 4) following creation of complete EMIS data dictionary from 5 MoES documents |


---

## AI Module Risk Register

The following risks are introduced by the AI Module add-on. They supplement the existing risk register and follow the same scoring methodology: Probability (1–5) × Impact (1–5) = Risk Score.

| Risk ID | Risk | Category | Probability | Impact | Score | Rating | Owner | Mitigation |
|---|---|---|---|---|---|---|---|---|
| RISK-AI-01 | AI hallucination: inaccurate student risk classification causes a teacher to ignore a genuinely at-risk student | AI Quality | 3 | 4 | 12 | High | Peter | Risk list is advisory only — no automatic action taken. Teacher retains full decision authority. Monthly accuracy review by sampling 20 AI classifications against actual term outcomes. |
| RISK-AI-02 | AI prompt injection via parent feedback text manipulates the LLM to return false sentiment data | AI Security | 2 | 3 | 6 | Medium | Backend team | `AIInputSanitiser` blocks known injection patterns. All injections logged. Batch processing means a single malicious response does not dominate the overall sentiment. |
| RISK-AI-03 | External AI provider (Anthropic) outage causes batch jobs to fail; Head Teachers receive no at-risk alerts for the week | Operational | 2 | 3 | 6 | Medium | DevOps | Circuit breaker pattern: retry 3× with exponential backoff. If primary provider unavailable, failover to secondary (OpenAI). If both unavailable: batch job deferred to next day, school owner notified via in-app alert. |
| RISK-AI-04 | Token costs spike unexpectedly (e.g., E-Learning module adding 10× the expected text volume) causing a school to exhaust its AI budget in week 1 | Financial | 2 | 3 | 6 | Medium | Peter | Monthly budget ceiling enforced by `BudgetGuard`. 80% alert gives owner time to review. Budget can be increased by Super Admin without code deployment. Per-feature cost visibility in the AI usage dashboard. |
| RISK-AI-05 | PII leak: student name or guardian phone number transmitted to Anthropic API due to `PIIScrubber` failure (regex miss or name not in guardians table) | Data Privacy | 2 | 5 | 10 | High | Backend team | PIIScrubber unit tests run for every prompt builder in CI. `pii_scrubbed = 0` in `ai_audit_log` triggers automated alert. DPPA breach notification procedure applies if PII transmission confirmed. |
| RISK-AI-06 | Model bias: AI systematically gives lower risk scores to students in certain classes due to mark distribution patterns, masking genuine risk | AI Quality | 2 | 4 | 8 | High | Peter | Quarterly bias audit: compare AI risk scores against actual term failure rates, stratified by class and curriculum type. Prompt tuning to correct systematic bias. Results published in the internal model quality log. |
| RISK-AI-07 | School owner relies entirely on AI briefing and stops reviewing raw reports, leading to over-reliance on AI summaries | Operational | 3 | 3 | 9 | High | Peter | AI briefing always links to the underlying report ("View full attendance report"). UI messaging: "AI-generated summary — verify with full reports for decisions with significant consequences." |
| RISK-AI-08 | International data transfer to Anthropic found non-compliant by Uganda PDPO; regulatory action against Chwezi Core Systems | Legal / Regulatory | 2 | 5 | 10 | High | Peter | DPA executed with Anthropic before go-live. School owner written acknowledgement obtained at AI module activation. DPIA completed and reviewed. If PDPO issues adverse finding: AI module suspended within 24 hours pending legal review. |
| RISK-AI-09 | AI-generated report card comment accepted without review contains factually incorrect statement about a specific student (e.g., wrong subject named) | AI Quality | 3 | 3 | 9 | High | Backend team | Hard Gate UI: teacher must review each comment individually. Confidence indicator shown per comment. Comments with `confidence = low` flagged with "Review carefully" warning. Feedback collected (accept/reject) to track accuracy over time. |
| RISK-AI-10 | LLM API key leaked via application logs or environment variable exposure | Security | 1 | 5 | 5 | Medium | DevOps | API keys stored only in environment variables. Never logged. Rotated quarterly. Secret scanning in CI (e.g., Trufflehog) blocks PRs containing secrets. |

### AI Risk Summary

| Rating | Count | Key Risks |
|---|---|---|
| High (≥ 8) | 6 | RISK-AI-01, RISK-AI-05, RISK-AI-06, RISK-AI-07, RISK-AI-08, RISK-AI-09 |
| Medium (4–7) | 4 | RISK-AI-02, RISK-AI-03, RISK-AI-04, RISK-AI-10 |
| Low (< 4) | 0 | — |

**Acceptance decision:** RISK-AI-05 and RISK-AI-08 are the highest-priority risks and must be fully mitigated before the AI module is commercially launched. All other risks are accepted with the stated mitigations in place.
