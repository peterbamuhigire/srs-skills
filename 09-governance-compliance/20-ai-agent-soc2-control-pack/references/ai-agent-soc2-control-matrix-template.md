# AI Agent SOC 2 Control Matrix Template

Worked example: agentic-CX SaaS (an inbox-triage + draft-reply + send-with-approval agent for B2B customer success teams). Adapt by replacing `{tenant placeholder}` values.

## How to read this template

- One row per applicable TSC criterion.
- "Parent control" = the parent SaaS SOC 2 row already in place; do not duplicate.
- "Agent-specific extension" = the new requirement, evidence, and test that the auditor needs in addition.
- Every "Evidence" cell names the artefact, the source system, and the cadence.
- Every "Test" cell names inquiry / inspection / observation / reperformance.

## Section CC1 — Control Environment

### CC1.1 — Integrity and ethical values

| Field | Value |
|-------|-------|
| Parent control | Code of conduct signed by all employees on hire and annually |
| Agent-specific extension | Agent action governance policy signed by AI lead, CTO, CEO, DPO; reviewed annually; published in the policy pack |
| Owner | AI Lead |
| Evidence | `policy_pack/agent-action-governance-policy.pdf` (signed); `sign-off-ledger/agent-governance-policy-YYYY.csv` |
| Source system | document management; sign-off ledger |
| Capture method | manual sign + ledger entry |
| Frequency | annual |
| Retention | 7 years |
| Sampling | full population (one document per year in the window) |
| Auditor test | inquiry of AI lead; inspect signed policy; inspect ledger entry; trace sign-off date against policy version date |

### CC1.4 — Commitment to competence

| Agent-specific extension | Agent-incident on-call training completed by every on-call engineer; AI lead competence reviewed annually |
| Evidence | `training/agent-oncall-completion-Qn.csv`; AI lead annual competence review |
| Frequency | quarterly training; annual competence review |
| Auditor test | inspect completion records; inquire on-call engineer about kill-switch console click path |

## Section CC2 — Communication and Information

### CC2.2 — Internal communication

| Agent-specific extension | Quarterly agent governance review communicated to engineering, security, legal; audit-log integrity report shared monthly |
| Evidence | meeting minutes; integrity report email log |
| Frequency | quarterly meeting; monthly integrity report |
| Auditor test | inspect minutes; observe integrity report distribution |

### CC2.3 — External communication

| Agent-specific extension | Responsible-AI Declaration public; tenant-admin disclosure shown on agent enablement; user-facing "performed by an agent" notification in product |
| Evidence | public Responsible-AI Declaration URL; product screenshot of disclosure modal; tenant-admin email template |
| Frequency | on-publish; on-enablement event |
| Auditor test | inspect public page; observe in-product flow; inspect tenant-admin email send log |

## Section CC3 — Risk Assessment

### CC3.2 — Risk identification

| Agent-specific extension | Per-feature agent risk register row; reversibility classification rubric applied to every tool in the catalogue |
| Evidence | `risk-register/agent-features.csv`; `action-catalogue/<tool>.yaml` reversibility_class field |
| Frequency | continuous (catalogue) + quarterly review |
| Auditor test | inspect risk register; sample 5 tools and verify reversibility class is justified |

## Section CC4 — Monitoring Activities

### CC4.1 — Ongoing monitoring

| Agent-specific extension | Agent SLI burn-rate alerts active for: task success, intervention rate, irreversible-action-incident rate, agent-task availability, agent-cost-per-run, cross-tenant tool-routing attempts; daily review of irreversible-action audit log by on-call operator |
| Evidence | alert configuration export; daily-review ticket log; monthly SLO report |
| Source system | observability platform; ticket system |
| Capture method | automated configuration export (software-dev pass collector); ticket-system export |
| Frequency | continuous + daily review + monthly report |
| Sampling | 25 daily-review tickets stratified across the window |
| Auditor test | inspect alert configuration; observe daily-review workflow; inspect 25 daily-review tickets; inquire on-call operator on escalation criteria |

## Section CC5 — Control Activities

### CC5.1 — Selection and development of controls

| Agent-specific extension | Approval-event control for every irreversible action; kill-switch control with two-person rule for global; supervision policy declared per feature |
| Evidence | approval-event audit log; kill-switch ADR; supervision policy section in policy pack |
| Frequency | continuous (events) + annual policy refresh |
| Sampling | 25 approval events; full population of kill-switch drills (quarterly) |
| Auditor test | inquire AI lead; inspect supervision policy; reperform an approval event in non-production and verify audit log row including signature |

## Section CC6 — Logical and Physical Access

### CC6.1 — Logical access — accounts and credentials

| Parent control | Workforce account provisioning, MFA, periodic review |
| Agent-specific extension | Agent service-principal identity is named, scoped, and credentialed per tenant; least-privilege per tool; service-principal access reviewed quarterly; tool allow-list enforced at dispatcher |
| Evidence | `access-review/agent-service-principals-Qn.csv`; dispatcher allow-list snapshot |
| Frequency | quarterly review; continuous allow-list snapshot |
| Sampling | full population of agent service principals |
| Auditor test | inspect quarterly review; reperform a refused tool call (call a tool not in the allow-list) and verify dispatcher refusal in audit log |

### CC6.3 — Logical access — system boundary

| Agent-specific extension | Per-tenant scope enforced at dispatcher and at every external tool; cross-tenant tool routing prevented and tested (red-team scenario RT-AGT-CRT-001) |
| Evidence | red-team test result for cross-tenant routing; dispatcher tenant-scope unit-test report |
| Frequency | continuous (test) + weekly red-team replay |
| Auditor test | inspect red-team replay log; inspect test code review approval |

### CC6.6 — Logical access — external connections

| Agent-specific extension | External tool calls go through a named egress with rate-limit class; provider compromise has a documented kill-switch playbook |
| Evidence | dispatcher egress configuration; runbook section on provider compromise |
| Frequency | continuous |
| Auditor test | inspect egress configuration; inquire on-call on provider-compromise procedure |

### CC6.7 — Logical access — data in transit

| Agent-specific extension | Tool calls TLS 1.2+ enforced; signed claim on tenant identity passed to provider where applicable |
| Evidence | TLS configuration export; signed-claim sample |
| Frequency | continuous |
| Auditor test | inspect configuration; inspect sample |

## Section CC7 — System Operations

### CC7.2 — Anomaly detection

| Agent-specific extension | Anomalies surfaced for: irreversible-action rate, intervention rate, cost-per-run, cross-tenant tool-routing attempts, agent-vs-supervisor token mismatches |
| Evidence | anomaly detection rule export; anomaly ticket log |
| Frequency | continuous |
| Sampling | 25 anomaly tickets in the window |
| Auditor test | inspect rules; sample tickets; observe on-call response in drill |

### CC7.3 — Incident detection

| Agent-specific extension | Agent-incident playbooks for: mass irreversible-action incident, cross-tenant tool-routing attempt, indirect prompt injection succeeded, budget runaway, agent unresponsive, tool provider compromise, disclosure of agent action |
| Evidence | runbook; incident postmortems for the window |
| Frequency | continuous + incident-based |
| Sampling | full population of SEV1/SEV2 in window |
| Auditor test | inspect playbooks; inspect postmortems |

### CC7.4 — Incident response

| Agent-specific extension | Kill-switch drill quarterly (global, per-tenant, per-feature); replay-a-run drill quarterly; agent-task quarantine procedure exercised in drill |
| Evidence | drill report quarterly; kill-switch drill audit-log entry |
| Frequency | quarterly |
| Sampling | full population (4 drills per year) |
| Auditor test | inspect drill report; observe a drill if one is scheduled in the audit window |

## Section CC8 — Change Management

### CC8.1 — Change management for system components

| Agent-specific extension | Changes to planner template, action catalogue, supervisor prompt, memory policy, or kill-switch SLA require: PR + ADR + red-team smoke + eval gate pass + AI lead sign-off + Security sign-off |
| Evidence | PR list filtered to those paths; ADR list; red-team smoke results; eval gate results |
| Frequency | continuous |
| Sampling | 25 PRs across the window stratified by component |
| Auditor test | sample PRs; verify ADR, smoke result, eval gate result, sign-off; reperform an agent-component PR in non-production and verify gates fired |

## Section CC9 — Risk Mitigation

### CC9.1 — Identification of risks

| Agent-specific extension | Provider sub-processor change protocol; agent insurance reviewed annually |
| Evidence | sub-processor change records; insurance certificate |
| Frequency | on-event; annual |
| Auditor test | inspect records and certificate |

## Section A1 — Availability

### A1.1 — Capacity

| Agent-specific extension | Capacity planning for peak concurrent agent runs by feature and tier; orchestrator failover documented |
| Evidence | capacity plan; load test report; orchestrator failover ADR |
| Frequency | annual + before major launches |
| Auditor test | inspect plan and report |

### A1.2 — System availability

| Agent-specific extension | Agent-task availability SLI per feature per tier; error budget tracked; customer commitments per tier |
| Evidence | SLO report; error-budget burn report |
| Frequency | monthly |
| Auditor test | inspect SLO report; trace customer commitment to contract |

### A1.3 — Recovery

| Agent-specific extension | Replay-a-run drill quarterly; force-pause and force-resume drill quarterly |
| Evidence | drill reports |
| Frequency | quarterly |
| Auditor test | inspect drill reports |

## Section C1 — Confidentiality

### C1.1 — Confidential information classification

| Agent-specific extension | Tool output classified by sensitivity; redaction in audit log per redaction policy |
| Evidence | redaction policy; redaction test output |
| Frequency | continuous |
| Auditor test | inspect redaction policy; inspect a sample audit-log entry verifying redaction |

### C1.2 — Confidential information disposal

| Agent-specific extension | Agent memory erasure policy; certificate of erasure produced on request |
| Evidence | erasure policy; erasure-event log; certificate sample |
| Frequency | continuous |
| Sampling | full population of erasure requests in window |
| Auditor test | inspect policy; sample erasure events |

## Section PI1 — Processing Integrity

### PI1.1 — Processing inputs

| Agent-specific extension | Tool input validation per action-catalogue schema; refusal of out-of-schema tool calls by dispatcher |
| Evidence | schema files; dispatcher refusal log sample |
| Frequency | continuous |
| Auditor test | inspect schemas; observe dispatcher refusal |

### PI1.2 — Processing accuracy

| Agent-specific extension | Eval task success threshold per tier; hallucinated-argument rate threshold; CI gate on every planner / catalogue PR |
| Evidence | eval gate reports; CI gate config |
| Frequency | continuous + nightly |
| Auditor test | inspect CI config; inspect 25 PR eval results |

### PI1.3 — Processing completeness

| Agent-specific extension | Every agent run reaches a terminal state within wallclock budget or is force-paused with operator notification |
| Evidence | run-state report; force-pause event log |
| Frequency | continuous |
| Auditor test | inspect report |

### PI1.4 — Processing — irreversible actions

| Agent-specific extension | Approval-event control on every irreversible-class tool call; signed approval record; hash-chain audit log |
| Evidence | approval-event log; hash-chain integrity report (from software-dev pass) |
| Frequency | continuous; daily integrity check |
| Sampling | 25 approval events; full population of integrity checks |
| Auditor test | sample approval events; verify signature, role, time, plan id; verify integrity report has no gaps |

### PI1.5 — Processing — output completeness

| Agent-specific extension | Reproduce script available for every incident; trace bundle preserved |
| Evidence | incident evidence pack; reproduce-script presence |
| Frequency | per incident |
| Auditor test | sample incident evidence packs |

## Section P — Privacy (P1 through P8)

| Criterion | Agent-specific extension |
|-----------|---------------------------|
| P1 Notice | Tenant-admin and user-facing agent disclosure; cross-link to Responsible-AI Declaration |
| P2 Choice and consent | Consent capture for agent processing where required; revocation flow tested |
| P3 Collection | DPIA addendum identifies every personal-data flow caused by an agent run |
| P4 Use, retention, disposal | Agent memory tiers documented; retention per tier; erasure verifiable |
| P5 Access | DSAR includes agent action history and agent memory |
| P6 Disclosure to third parties | Model provider as sub-processor; provider sub-processor change protocol |
| P7 Quality | Eval and red-team coverage; bias review for protected-class outcomes |
| P8 Monitoring and enforcement | Privacy incident playbook; DPO notification path; regulator notification template cross-link |

For each P criterion: evidence = the DPIA addendum, the consent UI screenshot, the DSAR fulfilment log, the sub-processor notice log, the bias review report, the privacy incident postmortems. Frequency declared per row in the evidence-pack spec.

## Sign-off

| Role | Name | Date |
|------|------|------|
| AI Lead | | |
| CISO | | |
| DPO | | |
| External Auditor | | |
