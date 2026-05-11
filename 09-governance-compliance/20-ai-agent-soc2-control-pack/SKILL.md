---
name: "ai-agent-soc2-control-pack"
description: "Generate the AI Agent SOC 2 Control Pack: TSC control matrix (Security, Availability, Confidentiality, Processing Integrity, Privacy) extended with agent-specific implementation requirements; per-control objective, agent-specific implementation, evidence required, evidence frequency, test procedure, sampling protocol, and the auditor-walkthrough script."
metadata:
  use_when: "Use whenever a SaaS operates one or more agent features at L1+ and intends to pass a SOC 2 Type I or Type II attestation. Mandatory before the SOC 2 audit window opens. Refreshed annually and after any change to the planner, action catalogue, supervisor prompt, or kill-switch SLA."
  do_not_use_when: "Do not use for L0 suggest-only AI features with no tool-call surface; the parent SaaS SOC 2 control pack is sufficient. Do not use as the sole control mapping for HIPAA or ISO; use the parallel HIPAA and ISO control packs."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_Runbook.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_Responsible_AI_Addendum.md, AI_Agent_ADR_Catalogue.md, AI_Agent_Compliance_Policy_Pack.md, AI_Agent_Evidence_Pack_Spec.md, parent SOC 2 control matrix (if exists)."
  workflow: "Walk every applicable TSC criterion; declare the agent-specific implementation requirement; declare the evidence required per criterion; declare the evidence frequency; declare the test procedure and sampling protocol; cross-link to the automated-evidence collector from the software-dev pass; write the control pack."
  quality_standards: "Every applicable TSC criterion shall have an agent-specific implementation requirement, an evidence row, an evidence-frequency value, and a test procedure. Every irreversible-action-class control shall name the human-final-decision evidence. Every monitoring criterion shall name the SLI from the agent SLO doc. Every control narrative shall be readable by an AICPA auditor in under three minutes."
  anti_patterns: "Do not write the SOC 2 control narrative as marketing prose. Do not omit the agent-specific implementation row when the parent control narrative says only 'least privilege' — the agent service principal needs its own treatment. Do not declare 'continuous' evidence cadence without naming the collector. Do not skip the irreversible-action and kill-switch test procedures."
  outputs: "AI_Agent_SOC2_Control_Pack.md and per-criterion entries in `soc2-controls/<criterion>.md`."
  references: "Use references/ai-agent-soc2-control-matrix-template.md."
---

# AI Agent SOC 2 Control Pack Skill

## Overview

The SOC 2 auditor walks the Trust Services Criteria row by row. For an agentic SaaS, the parent SaaS control narrative is insufficient because every TSC row has agent-specific implementation depth the auditor will ask about: the agent service principal's access (CC6), agent action monitoring (CC7), agent change management (CC8), agent availability SLI (A1), processing integrity of agent output (PI1), confidentiality of tool-output (C1), and privacy of agent-handled personal data (P1–P8).

This skill produces the control pack: one row per applicable TSC criterion, naming the agent-specific implementation, the evidence the auditor will accept, the frequency, the test procedure, and the auditor walkthrough script. The software-dev pass owns the **collector** that produces the evidence; this pack defines what the collector must produce and the format the auditor will read.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Agent PRD, Action Catalogue, Agent Architecture, Agent SLO, Agent Runbook, Agent Eval, Agent Red-Team, Responsible-AI Addendum, ADR Catalogue, Policy Pack, Evidence Pack Spec |
| **Output** | `AI_Agent_SOC2_Control_Pack.md` + `soc2-controls/*.md` |
| **Standards** | AICPA TSP 100 (2017, 2022 revisions); SOC 2 Type II attest engagement |

## Core Instructions

### Step 1: Confirm scope

For each TSC category, declare in-scope or out-of-scope with reasoning:

- **Security (CC1–CC9)** — always in-scope for any agent feature.
- **Availability (A1)** — in-scope if a customer-facing SLA names agent-task availability.
- **Confidentiality (C1)** — in-scope if customer-confidential data is processed by the agent (almost always).
- **Processing Integrity (PI1)** — in-scope if the agent performs transactional or financial actions (billing, ledger, contracts, regulated reporting).
- **Privacy (P1–P8)** — in-scope if the agent processes personal data; mandatory if any feature is subject to GDPR, CCPA, or an African DPA.

### Step 2: Agent-specific control extensions

Walk every applicable criterion and declare the agent-specific implementation. Default treatment:

| TSC | Agent-specific extension |
|-----|---------------------------|
| CC1 Control Environment | Agent governance owner named; policy pack signed; ADR catalogue current |
| CC2 Communication | Agent disclosures (user, tenant admin); Responsible-AI public paragraph |
| CC3 Risk Assessment | Agent-feature risk register row per feature; reversibility classification rubric applied |
| CC4 Monitoring | Agent SLI burn-rate alerts active; intervention rate trended; quarterly audit-log review |
| CC5 Control Activities | Approval-event control; kill-switch control; supervision-policy control |
| CC6 Logical Access | Agent service-principal access reviewed quarterly; per-tenant scope verified; tool allow-list enforced |
| CC7 System Operations | Agent-incident playbooks; anomaly detection on irreversible-action rate, intervention rate, cost-per-run, cross-tenant tool routing |
| CC8 Change Management | Planner / catalogue / supervisor / kill-switch changes through CAB; red-team smoke required; ADR required |
| CC9 Risk Mitigation | Agent insurance / vendor risk; provider sub-processor change protocol |
| A1 Availability | Agent-task availability SLI; capacity for peak agent runs; failover for orchestrator |
| C1 Confidentiality | Tool-output isolation; cross-tenant routing prevention; memory tier confidentiality; redaction in audit log |
| PI1 Processing Integrity | Action audit log integrity (hash-chain); reproduce-script evidence; eval coverage |
| P1–P8 Privacy | DPIA addendum; consent capture for agent processing; right-to-erasure on agent memory; sub-processor notice for model provider |

### Step 3: Declare evidence per criterion

For each criterion, declare:

- **Evidence artefact name** (e.g., `agent_access_review_Qn.csv`).
- **Source system** (e.g., IAM provider, agent orchestrator, audit log).
- **Capture method** (automated collector, scheduled job, sign-off ledger).
- **Frequency** (continuous, daily, weekly, monthly, quarterly, annual, on-event).
- **Retention** (per evidence-pack spec).
- **Sampling protocol** (full population, statistical sample with stated confidence, judgemental sample with stated size).

Refer to `references/ai-agent-soc2-control-matrix-template.md` for the canonical evidence table.

### Step 4: Declare the test procedure per criterion

For each criterion, declare the auditor's test:

- **Inquiry** (question the auditor will ask, and the role who answers).
- **Inspection** (artefact the auditor will inspect, and the system of record).
- **Observation** (walkthrough the auditor will observe — e.g., kill-switch drill).
- **Reperformance** (action the auditor will reperform — e.g., approve an irreversible action, then verify the audit-log row).

### Step 5: Declare the sampling protocol

| Population | Default sample |
|-------------|----------------|
| Approval events (irreversible actions) | 25 events stratified across features, or full population if < 25 |
| Kill-switch drills | full population (typically quarterly = 4) |
| Action-catalogue change PRs | 25 PRs stratified across features, or full population |
| Access reviews | 1 review per quarter, full population of agent service principals |
| Memory-erasure requests | full population |
| Red-team CRITICAL findings | full population; HIGH/MEDIUM by sample |
| Eval gate failures | full population during the audit window |
| Incident postmortems (SEV1/SEV2) | full population |

### Step 6: Auditor walkthrough script

Write a 1-page walkthrough script per major area: agent governance, action audit log, kill-switch drill, approval-event flow, evidence-pack assembly. Each script names the demoer role, the system, the click path, and the artefact the auditor will leave with.

### Step 7: Write the pack

`AI_Agent_SOC2_Control_Pack.md` sections: 1) Scope, 2) Agent-Specific Control Extensions, 3) Evidence Inventory, 4) Test Procedures, 5) Sampling Protocols, 6) Auditor Walkthrough Scripts, 7) Cross-Refs (to policy pack, evidence pack spec, runbook), 8) Sign-off Ledger.

## Standards

- AICPA TSP 100 (Trust Services Criteria)
- AICPA AT-C Section 205 (Attest Engagements)
- ISO/IEC 42001 Clause 9 (cross-link)
- NIST AI RMF MEASURE / MANAGE (cross-link)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-soc2-control-matrix-template.md`.
