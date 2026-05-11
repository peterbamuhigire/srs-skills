# AI Agent ISO/IEC 27001:2022 Control Matrix Template

Worked example: agentic-CX SaaS, EU + UK + US footprint, single ISMS scope including agent features. Adapt by replacing `{tenant placeholder}` values.

## A.5 — Organisational controls (selected agent-relevant rows)

### A.5.1 — Policies for information security

| Field | Value |
|-------|-------|
| Applicability | Applicable |
| Agent treatment | Seven agent policies bundled in the Agent Compliance Policy Pack; signed annually by AI Lead, CTO, CEO, DPO |
| ISO 42001 overlay | Clause 5.2 (policy) |
| Evidence | signed policy pack PDF; sign-off ledger |
| Frequency | annual |
| Sampling | full population (one policy pack per year) |
| Audit procedure | inquire AI Lead on policy authority; inspect signed pack and ledger |

### A.5.7 — Threat intelligence

| Applicability | Applicable |
| Agent treatment | Agentic CVE-style advisories monitored (OWASP LLM Top 10 agentic addendum, MITRE ATLAS updates, provider advisories); new red-team scenarios added within 7 days of public advisory |
| ISO 42001 overlay | Clause 6.1.2 (risk assessment) |
| Evidence | threat-intel monitoring source list; red-team scenario change log |
| Frequency | continuous |
| Audit procedure | inquire on intake process; inspect change log against advisory dates |

### A.5.9 — Inventory of information and other associated assets

| Applicability | Applicable |
| Agent treatment | Agent service principals inventoried with scopes; action catalogue treated as a controlled asset; replay environment inventoried |
| Evidence | service-principal inventory export; `action-catalogue/` directory; replay-env inventory |
| Frequency | continuous + quarterly review |
| Audit procedure | inspect inventory; reperform: add a tool to the catalogue and verify inventory update |

### A.5.12 — Classification of information

| Applicability | Applicable |
| Agent treatment | Tool output classified at retrieval-time; redaction rules in audit log per classification |
| Evidence | classification rules file; sample audit-log entry with redaction applied |
| Frequency | continuous |
| Audit procedure | inspect rules; inspect samples |

### A.5.15 — Access control

| Applicability | Applicable |
| Agent treatment | Agent service-principal least privilege; per-tenant scope at dispatcher; tool allow-list at dispatcher; global kill-switch two-person rule |
| ISO 42001 overlay | Annex A.4 (data management), A.5 (lifecycle) |
| Evidence | service-principal scope export; dispatcher allow-list snapshot |
| Frequency | continuous + quarterly review |
| Audit procedure | inspect scope; reperform out-of-scope tool call and verify refusal |

### A.5.19 — Information security in supplier relationships

| Applicability | Applicable |
| Agent treatment | Model provider supplier-risk assessed at onboarding and annually; training-data exclusion evidence retained; sub-processor change notice protocol |
| Evidence | supplier-risk assessment; training-exclusion contract clauses; sub-processor change log |
| Frequency | annual + on-change |
| Audit procedure | inspect assessment; inspect contract; sample sub-processor change records |

### A.5.23 — Information security for use of cloud services

| Applicability | Applicable |
| Agent treatment | Model gateway, orchestrator, vector store, audit-log store treated as cloud services with documented controls |
| Evidence | cloud-service inventory; per-service control statement |
| Frequency | annual |
| Audit procedure | inspect inventory and statements |

### A.5.25 — Assessment and decision on information security events

| Applicability | Applicable |
| Agent treatment | Agent-specific incident severity matrix and playbooks; declaration criteria for SEV1 (irreversible action incorrect; cross-tenant routing succeeded; mass exfil; provider compromise) |
| Evidence | severity matrix; playbooks; incident log |
| Frequency | continuous |
| Audit procedure | sample 25 events; trace classification |

### A.5.27 — Learning from information security incidents

| Applicability | Applicable |
| Agent treatment | AI RCA taxonomy applied to agent incidents; postmortem action items tracked to closure |
| Evidence | postmortems; action-item closure log |
| Frequency | per incident |
| Audit procedure | sample SEV1/SEV2 postmortems |

### A.5.30 — ICT readiness for business continuity

| Applicability | Applicable |
| Agent treatment | Kill-switch (global / per-tenant / per-feature) drills quarterly; force-pause and replay-a-run drills quarterly; agent-task quarantine drill annually |
| Evidence | drill reports; drill audit-log entries |
| Frequency | quarterly |
| Audit procedure | inspect reports; observe drill if scheduled in audit window |

### A.5.34 — Privacy and protection of personal identifiable information (PII)

| Applicability | Applicable |
| Agent treatment | DPIA addendum; memory erasure policy; sub-processor notice; cross-link to AI Data Flow doc |
| ISO 42001 overlay | Clause 6.1.4 (impact assessment) |
| Evidence | DPIA addendum; erasure event log; sub-processor notice log |
| Frequency | continuous + annual review |
| Audit procedure | inspect DPIA; sample erasure events |

## A.6 — People controls

### A.6.3 — Information security awareness, education, and training

| Applicability | Applicable |
| Agent treatment | Agent on-call training; agent disclosure training for product, sales, support |
| Evidence | training completion records |
| Frequency | quarterly + on-hire |
| Audit procedure | inspect records |

## A.7 — Physical controls

Inherited from parent ISMS unless dedicated agent infrastructure exists. Declare inheritance in the SoA delta; do not duplicate.

## A.8 — Technological controls (selected agent-relevant rows)

### A.8.2 — Privileged access rights

| Applicability | Applicable |
| Agent treatment | Global kill-switch invocation requires two-person rule; kill-switch console privileged role; audit log of every privileged invocation |
| Evidence | privileged role membership; kill-switch invocation log |
| Frequency | continuous + quarterly review |
| Audit procedure | inspect membership; observe drill |

### A.8.7 — Protection against malware

| Applicability | Applicable |
| Agent treatment | Tool-result sanitisers for indirect prompt injection; CI red-team smoke on tool-output poisoning |
| Evidence | sanitiser configuration; red-team smoke results |
| Frequency | continuous |
| Audit procedure | inspect configuration and results |

### A.8.9 — Configuration management

| Applicability | Applicable |
| Agent treatment | Planner template, supervisor prompt, action catalogue, memory policy under version control; change via PR + ADR + red-team smoke |
| Evidence | repo history; PR list; ADRs |
| Frequency | continuous |
| Audit procedure | sample 25 PRs; trace gates |

### A.8.10 — Information deletion

| Applicability | Applicable |
| Agent treatment | Agent memory erasure policy; certificate of erasure produced per request |
| Evidence | erasure policy; erasure event log; certificate sample |
| Frequency | continuous |
| Audit procedure | sample erasure requests |

### A.8.12 — Data leakage prevention

| Applicability | Applicable |
| Agent treatment | Cross-tenant tool-routing prevented and tested; tenant data exfil red-team category |
| Evidence | red-team scenario results; dispatcher tenant-scope test results |
| Frequency | continuous + weekly red-team replay |
| Audit procedure | inspect results |

### A.8.15 — Logging

| Applicability | Applicable |
| Agent treatment | Action audit log retention by event class (per Responsible-AI Addendum); hash-chain integrity |
| ISO 42001 overlay | Annex A.6.2 (operational data) |
| Evidence | retention configuration; integrity report |
| Frequency | continuous + daily integrity check |
| Audit procedure | inspect configuration; reperform integrity check |

### A.8.16 — Monitoring activities

| Applicability | Applicable |
| Agent treatment | Agent SLI burn-rate alerts; daily irreversible-action audit-log review |
| ISO 42001 overlay | Clause 9.1 |
| Evidence | alert configuration; daily-review ticket log |
| Frequency | continuous |
| Audit procedure | inspect configuration; sample tickets |

### A.8.22 — Segregation of networks

| Applicability | Applicable |
| Agent treatment | Tenant boundary at dispatcher and at every external tool; egress restriction by feature |
| Evidence | network configuration; tenant-scope test results |
| Frequency | continuous |
| Audit procedure | inspect configuration |

### A.8.24 — Use of cryptography

| Applicability | Applicable |
| Agent treatment | Hash-chain audit log; signed approval events; TLS 1.2+ enforced for tool calls |
| Evidence | cryptography standards document; configuration export |
| Frequency | continuous |
| Audit procedure | inspect standards and configuration |

### A.8.25 — Secure development lifecycle

| Applicability | Applicable |
| Agent treatment | Eval gate + red-team smoke + ADR + sign-off on every planner / catalogue / supervisor / memory change |
| ISO 42001 overlay | Clause 8 (operation) |
| Evidence | CI configuration; gate results |
| Frequency | continuous |
| Audit procedure | inspect CI; sample PR gates |

### A.8.28 — Secure coding

| Applicability | Applicable |
| Agent treatment | Tool-input schema validation; tool-output sanitisation; refusal of out-of-schema tool calls |
| Evidence | schemas; dispatcher refusal log sample |
| Frequency | continuous |
| Audit procedure | inspect schemas; observe refusal |

### A.8.29 — Security testing in development and acceptance

| Applicability | Applicable |
| Agent treatment | Agent red-team CI smoke on every relevant PR; weekly full replay; quarterly external red-team |
| ISO 42001 overlay | Clause 8.3 |
| Evidence | CI configuration; weekly run reports; quarterly external report |
| Frequency | continuous + weekly + quarterly |
| Audit procedure | inspect configuration; sample reports |

### A.8.32 — Change management

| Applicability | Applicable |
| Agent treatment | CAB review for planner / catalogue / supervisor / memory / kill-switch changes; ADR required |
| Evidence | CAB minutes; ADR list |
| Frequency | continuous |
| Audit procedure | sample 25 changes |

### A.8.34 — Protection of information systems during audit testing

| Applicability | Applicable |
| Agent treatment | Red-team and eval sets do not contain real customer data; synthetic-data generation policy |
| Evidence | data-generation policy; red-team set provenance |
| Frequency | continuous |
| Audit procedure | inspect policy; sample red-team set |

## Sign-off

| Role | Name | Date |
|------|------|------|
| AI Lead | | |
| CISO | | |
| ISMS Manager | | |
| Certification Body Lead Auditor | | |
