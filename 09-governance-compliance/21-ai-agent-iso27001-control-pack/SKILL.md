---
name: "ai-agent-iso27001-control-pack"
description: "Generate the AI Agent ISO/IEC 27001:2022 Control Pack: Annex A control matrix (A.5 Organisational, A.6 People, A.7 Physical, A.8 Technological) extended with agent-specific treatments; per-control treatment statement, applicability decision, evidence required, audit procedure, sampling, and the certification-body walkthrough script. Mapped to ISO/IEC 42001 where the AI overlay applies."
metadata:
  use_when: "Use whenever a SaaS operates one or more agent features at L1+ and intends to certify or maintain ISO/IEC 27001 certification, or holds an ISO/IEC 42001 AI management system certification. Mandatory before the ISMS surveillance audit, and refreshed annually or after any material change to the planner, action catalogue, supervisor, kill-switch SLA, or sub-processor list."
  do_not_use_when: "Do not use as the sole framework if SOC 2 is also required — produce both control packs side by side. Do not use the 2013 control numbering; the 2022 edition (93 controls in 4 themes) is the operating reference."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_Runbook.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_Responsible_AI_Addendum.md, AI_Agent_ADR_Catalogue.md, AI_Agent_Compliance_Policy_Pack.md, AI_Agent_Evidence_Pack_Spec.md, parent ISMS Statement of Applicability."
  workflow: "Confirm applicability per control; declare the agent-specific treatment; declare the evidence and source; declare the audit procedure; declare sampling and frequency; produce the Statement of Applicability delta; write the control pack."
  quality_standards: "Every applicable Annex A control shall have an agent-specific treatment statement, an evidence row, an audit procedure, and a sampling note. The Statement of Applicability shall name every control as applicable, applicable-with-justification, or not-applicable-with-justification. ISO/IEC 42001 overlay controls shall be cited for every AI control."
  anti_patterns: "Do not declare 'not applicable' for A.5.30 ICT readiness, A.5.34 privacy, A.8.16 monitoring, A.8.28 secure coding when an agent ships — these are all in-scope for agents. Do not omit A.5.7 threat intelligence — agentic CVE-style advisories are part of threat intel. Do not skip A.8.34 protection of test data when red-team sets contain real customer data."
  outputs: "AI_Agent_ISO27001_Control_Pack.md, Statement_of_Applicability_Agent_Delta.md, and per-control entries in `iso27001-controls/<id>.md`."
  references: "Use references/ai-agent-iso27001-control-matrix-template.md."
---

# AI Agent ISO/IEC 27001 Control Pack Skill

## Overview

ISO 27001:2022 reorganised the Annex A controls into 4 themes: A.5 Organisational (37 controls), A.6 People (8), A.7 Physical (14), A.8 Technological (34). For an agentic SaaS, many controls require agent-specific treatments that the parent ISMS does not articulate. ISO/IEC 42001:2023 sits alongside as the AI management system standard; this pack cites 42001 clauses where the AI overlay applies but the operating reference for evidence and audit is 27001:2022.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Agent PRD, Action Catalogue, Agent Architecture, Agent SLO, Agent Runbook, Agent Eval, Agent Red-Team, Responsible-AI Addendum, ADR Catalogue, Policy Pack, Evidence Pack Spec, parent ISMS SoA |
| **Output** | `AI_Agent_ISO27001_Control_Pack.md` + `iso27001-controls/*.md` + `Statement_of_Applicability_Agent_Delta.md` |
| **Standards** | ISO/IEC 27001:2022; ISO/IEC 27002:2022; ISO/IEC 42001:2023 |

## Core Instructions

### Step 1: Statement of Applicability delta

For every Annex A control, declare:

- Applicability: applicable / not-applicable / applicable-with-justification.
- Reasoning that explicitly mentions the agent surface (planner, dispatcher, supervisor, memory, audit log, kill-switch).
- Cross-link to the parent ISMS SoA row.

### Step 2: Per-control agent treatment

Default treatments for the most agent-relevant controls:

| Control | Agent treatment |
|---------|------------------|
| A.5.1 Policies | Agent action governance policy in policy pack |
| A.5.7 Threat intelligence | Agentic CVE-style advisories monitored; new red-team scenarios added within 7 days |
| A.5.9 Inventory of information and assets | Agent service principals and action catalogue inventoried |
| A.5.12 Classification of information | Tool output classified; redaction in audit log |
| A.5.15 Access control | Agent service-principal least privilege; per-tenant scope at dispatcher |
| A.5.19 Information security in supplier relationships | Model provider supplier-risk; training-exclusion evidence; sub-processor notice |
| A.5.23 Information security for cloud services | Model gateway, vector store, orchestrator cloud-service controls |
| A.5.25 Assessment of security events | Agent-incident playbooks |
| A.5.27 Learning from incidents | Postmortems include agent-specific RCA taxonomy |
| A.5.30 ICT readiness for business continuity | Kill-switch, force-pause, replay-a-run drills |
| A.5.34 Privacy and PII protection | DPIA addendum; agent memory erasure |
| A.6.3 Awareness, education, and training | Agent on-call training; agent disclosure training |
| A.6.7 Remote working | Agent operators must use approved kill-switch console only |
| A.7.4 Physical security monitoring | Inherited from parent unless dedicated agent infra |
| A.8.1 User end-point devices | Inherited |
| A.8.2 Privileged access rights | Two-person rule for global kill-switch |
| A.8.3 Information access restriction | Per-tenant scope enforcement |
| A.8.5 Secure authentication | Agent service-principal credential rotation |
| A.8.7 Protection against malware | Tool-result sanitisers for indirect prompt injection |
| A.8.9 Configuration management | Planner template, supervisor prompt, action catalogue under change control |
| A.8.10 Information deletion | Memory erasure policy verification |
| A.8.12 Data leakage prevention | Cross-tenant tool-routing prevention; tenant data exfil red-team |
| A.8.15 Logging | Action audit log retention by event class |
| A.8.16 Monitoring activities | Agent SLI burn-rate alerts |
| A.8.20 Network security | Egress with rate-limit class; provider compromise playbook |
| A.8.22 Segregation of networks | Tenant boundary at dispatcher and at every external tool |
| A.8.24 Use of cryptography | Hash-chain audit log; signed approval events |
| A.8.25 Secure development lifecycle | Eval gate + red-team smoke gate + ADR + sign-off |
| A.8.27 Secure system architecture | Agent architecture spec; reversibility rubric |
| A.8.28 Secure coding | Tool-input validation per schema |
| A.8.29 Security testing | Red-team CI smoke + weekly full set |
| A.8.31 Separation of development, test, and production environments | Replay environment isolation; red-team set isolation |
| A.8.32 Change management | Planner / catalogue / supervisor changes through CAB + ADR + red-team smoke |
| A.8.34 Protection of information systems during audit testing | Red-team sets do not contain real customer data; eval set governance |

### Step 3: ISO/IEC 42001 overlay

Cross-link the AI management system clauses for every AI control:

- Clause 4 Context / 5 Leadership / 6 Planning / 7 Support / 8 Operation / 9 Performance / 10 Improvement.
- Annex A of 42001 mapped to specific 27001 controls where they reinforce.

### Step 4: Evidence and audit procedure

For each control: evidence artefact, source system, capture method, frequency, retention, sampling, audit procedure (the certification body's procedure: inquiry, inspection, observation, reperformance).

### Step 5: Internal audit programme entries

Add agent-specific internal audit entries to the ISMS internal audit plan:

- Agent action audit-log integrity review quarterly.
- Agent kill-switch drill review quarterly.
- Agent change-management sample review semi-annually.
- Agent supplier (model provider) review annually.

### Step 6: Management review inputs

The agent ISMS slice contributes the following to management review:

- Agent SLO performance vs targets.
- Agent incident summary by severity.
- Agent red-team findings and remediation status.
- Agent control test results.
- Agent supplier risk changes.

### Step 7: Write the pack

`AI_Agent_ISO27001_Control_Pack.md` sections: 1) SoA Delta, 2) Per-control Treatments, 3) ISO/IEC 42001 Overlay, 4) Evidence and Audit Procedure, 5) Internal Audit Programme Additions, 6) Management Review Inputs, 7) Cross-Refs, 8) Sign-off Ledger.

## Standards

- ISO/IEC 27001:2022 (ISMS requirements)
- ISO/IEC 27002:2022 (control guidance)
- ISO/IEC 27007 (auditing guidelines)
- ISO/IEC 42001:2023 (AI management system)
- ISO/IEC 23894 (AI risk management)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-iso27001-control-matrix-template.md`.
