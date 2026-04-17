# 7 Success Metrics and Key Performance Indicators

This section defines the measurable KPIs that govern Medic8's progress across business growth, clinical safety, operational performance, user adoption, AI Intelligence performance, and internationalisation quality. Each KPI specifies a baseline, target, measurement method, and timeline. KPIs are evaluated at phase gates per the Water-Scrum-Fall methodology (see Section 8 Constraints and Assumptions).

All targets are binding unless marked `[ASPIRATIONAL]`. Unknown baselines are flagged with `[BASELINE-TBD]` and must be established during Phase 1 pilot data collection.

## 7.1 Business KPIs

| KPI | Category | Baseline | Target | Measurement Method | Timeline |
|---|---|---|---|---|---|
| Monthly Recurring Revenue (MRR) | Revenue | UGX 0 | UGX 1.5M (Phase 1), UGX 15M (Phase 2), UGX 40M (Phase 3), UGX 100M (Phase 4) | Subscription billing system aggregate | Phase 1: Month 6; Phase 2: Month 12; Phase 3: Month 18; Phase 4: Month 24 |
| Number of paying facilities | Growth | 0 | 10 (Phase 1), 50 (Phase 2), 100 (Phase 3), 200+ (Phase 4) | Active subscription count in tenant registry | Per phase gate |
| Customer Acquisition Cost (CAC) | Efficiency | `[BASELINE-TBD]` | < UGX 500,000 per facility (Phase 1); decreasing 20% per phase | Total sales and marketing spend / new paying facilities acquired in period | Quarterly from Phase 1 |
| Monthly churn rate | Retention | `[BASELINE-TBD]` | < 5% (Phase 1), < 3% (Phase 2+) | Facilities that cancelled or downgraded / total active facilities at start of month | Monthly from first paying customer |
| Facility onboarding time | Efficiency | `[BASELINE-TBD]` | 2-4 hours from account creation to first patient registration | Timestamp delta: account creation to first `Patient` record saved | Phase 1 pilot onboarding |
| Net Promoter Score (NPS) | Satisfaction | `[BASELINE-TBD]` | ≥ 40 (Phase 1), ≥ 50 (Phase 2+) | In-app survey at 90-day post-onboarding check-in (0-10 scale) | Quarterly from Phase 1 |
| Average Revenue Per Facility (ARPF) | Revenue | UGX 150,000 (Starter tier) | UGX 300,000 (blended average by Phase 2) | MRR / total paying facilities | Monthly |
| Cash billing reconciliation rate | Revenue integrity | `[BASELINE-TBD]` | ≥ 95% | System-recorded billing total vs bank deposit reconciliation | Phase 1 gate criterion |
| Lifetime Value (LTV) to CAC ratio | Unit economics | `[BASELINE-TBD]` | ≥ 3:1 by Phase 2 | (ARPF × average facility lifespan in months) / CAC | Quarterly from Phase 2 |

## 7.2 Clinical Safety KPIs

| KPI | Category | Baseline | Target | Measurement Method | Timeline |
|---|---|---|---|---|---|
| Medication error rate (with Medic8) | Patient safety | `[BASELINE-TBD]` — measure pre-Medic8 rate during pilot intake | 50% reduction vs pre-Medic8 baseline within 6 months of adoption | Incident reports filed in Medic8 incident reporting module vs pre-Medic8 paper-based error logs | Phase 1 Month 3 (baseline), Phase 1 Month 9 (comparison) |
| CDS alert override rate | Alert effectiveness | Industry benchmark: 90%+ override rate (literature) | < 30% for Serious/Fatal tier alerts; < 60% for Warning tier | Override events / total alerts fired, segmented by tier (Info, Warning, Serious, Fatal) | Monthly from Phase 1 CDS activation |
| Critical value notification acknowledgment time | Lab safety | `[BASELINE-TBD]` | < 30 minutes from result entry to clinician acknowledgment | Timestamp delta: lab technician marks result as critical to clinician acknowledgment action in system | Phase 1 (basic lab module) |
| Adverse drug event (ADE) rate | Patient safety | `[BASELINE-TBD]` — establish from pilot facility incident data | Decreasing trend quarter-over-quarter | ADE incident reports per 1,000 medication orders | Quarterly from Phase 1 |
| Patient identification error rate (duplicate records) | Data integrity | `[BASELINE-TBD]` | < 1% duplicate rate in EMPI | EMPI probabilistic matching: flagged potential duplicates / total patient registrations | Monthly from Phase 1 |
| Drug interaction alert accuracy (true positive rate) | Alert quality | `[BASELINE-TBD]` — dependent on licensed drug interaction database (gap HIGH-001) | ≥ 95% true positive rate for Serious/Fatal interactions | Clinical pharmacist review of a random 5% sample of alerts fired monthly | Quarterly from Phase 1 |
| Allergy-prescription conflict detection rate | Patient safety | `[BASELINE-TBD]` | 100% of known allergies checked against every prescription | Automated: system confirms allergy check executed before prescription save | Phase 1 (prescribing module) |
| Paediatric dosing error prevention rate | Patient safety | `[BASELINE-TBD]` | 100% of weight-based prescriptions validated against mg/kg formula with adult ceiling cap | Automated: system rejects prescriptions exceeding calculated dose range | Phase 1 (prescribing module) |
| Zero patient safety incidents in pilot | Phase 1 gate | 0 | 0 incidents attributable to system error | Incident investigation report with root cause analysis | Phase 1 gate criterion |

## 7.3 Operational KPIs

| KPI | Category | Baseline | Target | Measurement Method | Timeline |
|---|---|---|---|---|---|
| System uptime | Availability | N/A (new system) | 99.9% (≤ 8.76 hours downtime/year) | Infrastructure monitoring; $Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$ | Monthly from production launch |
| API response time (P95) | Performance | N/A | < 500 ms under normal load (≤ 50 concurrent users per facility) | Application Performance Monitoring (APM) at API gateway | Continuous from Phase 1 |
| Page load time | Performance | N/A | < 2 seconds on 1 Mbps connection | Synthetic monitoring from Kampala-based test endpoint | Continuous from Phase 1 |
| Offline sync queue size | Resilience | N/A | Queue processes within 5 minutes of connectivity restoration for up to 500 queued transactions | Sync engine metrics: queue depth, oldest item age, drain time | Phase 1 (offline-first modules) |
| Offline sync recovery time | Resilience | N/A | Full queue drain within 10 minutes on 256 Kbps connection | Sync engine completion timestamp - connectivity restoration timestamp | Phase 1 |
| HMIS report auto-population accuracy | Reporting | Manual tally (baseline) | ≥ 99% match vs manual tally for HMIS 105 and HMIS 108 | Field-by-field comparison: Medic8 auto-generated report vs MoH field officer manual tally | Phase 2 (HMIS module); Phase 2 gate criterion |
| Data completeness rate | Data quality | `[BASELINE-TBD]` | ≥ 90% of encounters with ICD-10 coded diagnosis (Phase 1); ≥ 95% (Phase 2+) | Encounters with at least one ICD-10 code / total encounters | Monthly from Phase 1 |
| Backup success rate | Disaster recovery | N/A | 100% of daily automated backups completed successfully | Backup job completion log with verification checksum | Daily from production launch |
| Recovery Point Objective (RPO) | Disaster recovery | N/A | < 1 hour | Time since last successful backup at point of failure | Tested quarterly |
| Recovery Time Objective (RTO) | Disaster recovery | N/A | < 4 hours | Time from failure declaration to full service restoration | Tested quarterly |
| FHIR R4 conformance score | Interoperability | N/A | Pass ONC certification test suite for 14 resource types | ONC FHIR conformance test runner output | Phase 3 gate criterion |

## 7.4 User Adoption KPIs

| KPI | Category | Baseline | Target | Measurement Method | Timeline |
|---|---|---|---|---|---|
| Daily Active Users (DAU) per facility | Engagement | `[BASELINE-TBD]` | ≥ 80% of registered clinical staff per facility use the system daily | Unique user logins per facility per day / total registered clinical users | Monthly from Phase 1 pilot |
| Module activation rate | Breadth | N/A | ≥ 70% of available modules activated per facility within 90 days of onboarding | Activated modules / total modules available at facility tier | Quarterly |
| Feature utilisation rate per role | Depth | `[BASELINE-TBD]` | ≥ 60% of role-scoped features used at least once per week | Feature interaction events per role / total features available to that role | Monthly from Phase 1 |
| Training completion rate | Readiness | 0% | 100% of assigned users complete module-specific video training before module activation | Training module completion records per user per module | Per module activation |
| Support ticket volume per facility | Support load | `[BASELINE-TBD]` | ≤ 5 tickets per facility per month (Phase 1); ≤ 2 per month (Phase 2+) | Help desk ticket count grouped by `facility_id` | Monthly |
| Time to resolve support ticket | Support quality | `[BASELINE-TBD]` | Median resolution time ≤ 24 hours (Phase 1); ≤ 8 hours (Phase 2+) | Ticket creation timestamp to resolution timestamp | Monthly |
| 30/60/90-day retention rate | Retention | `[BASELINE-TBD]` | ≥ 90% of pilot facilities still active at 90 days | Facilities with at least 1 login in trailing 7 days at each checkpoint | Phase 1 pilot |
| Mobile app adoption rate | Platform | `[BASELINE-TBD]` | ≥ 40% of clinical staff using mobile app by Phase 2 | Mobile app unique users / total clinical users per facility | Phase 2+ |

## 7.5 AI Intelligence Success Metrics

These metrics apply to tenants that have activated the AI Intelligence module. Measurement begins at module activation, not at Phase 1 launch.

| Metric | Target | Measurement Window | Baseline |
|---|---|---|---|
| ICD coding suggestion acceptance rate | ≥ 70% of AI suggestions accepted without modification | 90 days after AI module activation | 0% (no AI coding prior to activation) |
| AI claim scrubbing rejection rate reduction | ≥ 20% reduction in first-submission rejection rate | 6 months after AI module activation | Facility-specific pre-activation rejection rate |
| AI clinical note draft acceptance rate (unedited) | ≥ 40% of drafts approved without clinician edits | 90 days after AI module activation | 0% |
| AI outbreak early warning false positive rate | ≤ 15% false positives over rolling 90-day period | Rolling 90-day window | Measured from first alert generated |

The AI Intelligence admin panel displays all 4 metrics in real time, updated daily, accessible to the AI Administrator role.

## 7.6 Internationalisation (i18n) Quality Metric

- Zero `[I18N-GAP]` tags shall remain unresolved in any production release. An `[I18N-GAP]` tag in the `release` branch build log is a release blocker.
- The CI pipeline fails the build in the `release` branch when any `[I18N-GAP]` tag is present. The gap is assigned to the translation queue with the label `i18n-gap` and resolved by a native-speaker reviewer before the build is retried.
- Measurement method: automated build log scan for `[I18N-GAP]` pattern in `release` branch.

## 7.7 Phase Gate Criteria

### Phase 1 Gate

All criteria must be satisfied before Phase 2 begins:

1. All 7 HIGH gaps resolved and documented.
2. Core clinical workflow tested end-to-end (registration → consultation → prescription → dispensing → billing → receipt).
3. Medication safety validation complete (drug interactions, allergy conflicts, paediatric dosing guards).
4. Zero patient safety incidents attributable to system error during pilot.
5. At least 3 pilot clinics live and processing real patients.
6. Cash billing reconciliation rate ≥ 95%.
7. 100% test pass rate for all Phase 1 modules.
8. Facility onboarding demonstrated within 2-4 hours.
9. French and Kiswahili string files 100% complete with zero `[I18N-GAP]` tags across all Phase 1 modules.

### Phase 2 Gate

1. Phase 1 in production with 10+ paying facilities.
2. Zero patient safety incidents reported across all Phase 1 facilities.
3. Insurance claim submission and reconciliation functional with at least 3 Uganda insurers.
4. HMIS monthly report export validated by MoH field officer (≥ 99% accuracy).
5. At least 1 government facility (HC IV) onboarded.
6. At least 1 mission hospital onboarded.
7. AI Intelligence module available and tested with at least 1 pilot facility.

### Phase 3 Gate

1. FHIR R4 conformance tested against ONC certification test suite for 14 resource types.
2. PEPFAR MER indicators (TX_CURR, TX_NEW, TX_PVLS) validated against manual calculation with < 1% variance.
3. First OpenMRS/UgandaEMR data migration completed successfully.
4. At least 1 PEPFAR-funded facility onboarded.
5. At least 1 cross-border deployment (Kenya or Tanzania) operational.

### Phase 4 Gate

1. 50+ active facilities across all tiers.
2. Director Platform validated with at least 1 multi-facility network.
3. Multi-facility patient record sharing demonstrated across at least 2 sites with sub-second lookup.
4. Insurance claims processing validated with 3+ insurers.
5. Enterprise SLA defined and tested.
6. PACS integration tested with at least 1 radiology department.
7. Consolidated Director dashboard operational.

## 7.8 KPI Review Cadence

| Review Level | Frequency | Participants | Action |
|---|---|---|---|
| Operational dashboard | Daily | Peter (solo developer/operator) | Monitor uptime, sync queue, critical alerts |
| KPI review | Monthly | Peter | Evaluate all KPI categories, identify trends, adjust priorities |
| Phase gate review | Per phase boundary | Peter + pilot facility stakeholders | Evaluate gate criteria pass/fail; decision to proceed or remediate |
| Clinical safety review | Monthly | Peter + consulting clinician (gap HIGH-004 resolution) | Review CDS override rates, incident reports, medication errors |
| AI Intelligence review | Monthly | Peter + AI Administrator at each active tenant | Review AI success metrics, false positive rates, credit consumption trends |
