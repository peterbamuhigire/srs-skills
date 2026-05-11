---
name: "ai-agent-compliance-runbook"
description: "Generate the AI Agent Compliance Runbook: the operational runbook for continuous compliance — drill schedule, evidence-collection schedule, control-test schedule, audit-window operations, on-the-day auditor playbook activation, gap-remediation cadence. Operates the artefacts produced by the SOC 2 / ISO / HIPAA control packs, policy pack, evidence pack spec, and attestation preparation spec."
metadata:
  use_when: "Use whenever a SaaS operates one or more agent features at L1+ in production and must demonstrate continuous compliance across SOC 2 Type II, ISO 27001, HIPAA. Mandatory before the audit window opens and active continuously thereafter."
  do_not_use_when: "Do not use as a substitute for the parent SaaS runbook or for the agent operations runbook; this is the compliance-operations runbook layered on top. Do not use for one-off audits without ongoing compliance posture; use the attestation preparation spec alone in that case."
  required_inputs: "AI_Agent_SOC2_Control_Pack.md, AI_Agent_ISO27001_Control_Pack.md, AI_Agent_HIPAA_Control_Pack.md, AI_Agent_Compliance_Policy_Pack.md, AI_Agent_Evidence_Pack_Spec.md, AI_Agent_Attestation_Preparation_Spec.md, AI_Agent_Runbook.md, AI_Incident_Response_Runbook.md."
  workflow: "Build the drill schedule; build the evidence-collection schedule; build the control-test schedule; build the audit-window operating procedure; build the on-the-day playbook activation procedure; build the gap-remediation cadence; write the runbook."
  quality_standards: "Every drill, every evidence collection, every control test shall have an owner, a cadence, a calendar invite, and a completion verification step. Audit-window operations shall be documented including daily integrity reports, weekly evidence sweeps, mid-window gap check. Gap remediation SLA shall match the attestation preparation spec."
  anti_patterns: "Do not let drills slip without a documented exception. Do not run evidence collection only when the audit is imminent — continuous collection is the operating standard. Do not split ownership of drills between roles without naming the lead. Do not skip the closure-preparation checklist."
  outputs: "AI_Agent_Compliance_Runbook.md."
  references: "Use references/ai-agent-compliance-runbook-template.md."
---

# AI Agent Compliance Runbook Skill

## Overview

The compliance runbook converts the control packs, policy pack, evidence pack spec, and attestation prep spec into a calendar-driven operating procedure: who does what, when, with what artefact. It is the daily / weekly / monthly / quarterly / annual heartbeat that keeps compliance posture continuous.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | SOC 2 / ISO / HIPAA control packs, Policy Pack, Evidence Pack Spec, Attestation Prep Spec, Agent Runbook, AI Incident Response Runbook |
| **Output** | `AI_Agent_Compliance_Runbook.md` |
| **Standards** | AICPA AT-C 205; ISO/IEC 27001 Clauses 9.1 and 9.2; ISO/IEC 17021; HIPAA §164.308(a)(8) |

## Core Instructions

### Step 1: Drill schedule

| Drill | Cadence | Owner | Verification |
|-------|---------|-------|--------------|
| Global kill-switch (staging) | quarterly | SRE Lead | Drill report; audit-log entry; propagation ≤ 5 s |
| Per-tenant kill-switch (staging) | quarterly | SRE Lead | Drill report |
| Per-feature kill-switch (staging) | quarterly | AI Lead | Drill report |
| Global kill-switch (production) | annual + on-event | SRE Lead | Drill report; tenant notification |
| Replay-a-run | quarterly | AI Lead | Drill report |
| Force-pause + force-resume | quarterly | SRE Lead | Drill report |
| Agent-task quarantine | annual | AI Lead | Drill report; tenant-admin notification |
| Evidence-pack assembly dry run | quarterly | Compliance Manager | Pack signed zip; manifest hash |
| BAA / DPA execution dry run | annual | DPO | Counter-signed addendum produced |
| Auditor portal access dry run | quarterly | Compliance Manager | Access granted to named test recipient; access revoked on day +1 |

### Step 2: Evidence-collection schedule

For every evidence artefact in the evidence frequency table, document:

- Calendar invite (recurring) with owner.
- Verification step (artefact present in pack at declared frequency).
- Escalation if missed (SEV2 if missed cadence × 2; SEV1 if missed × 3).

### Step 3: Control-test schedule

| Test | Cadence | Owner |
|------|---------|-------|
| Access review for agent service principals | quarterly | Security |
| Tool allow-list reperformance | quarterly | AI Lead |
| Hash-chain integrity verification | daily (automated) + weekly review | Security |
| Approval-event sample review (25 events) | monthly | AI Lead |
| Daily-review ticket sample review (25 tickets) | monthly | AI Lead |
| PR sample review (25 PRs) | quarterly | CTO |
| Sub-processor list review | quarterly | DPO |
| BAA / DPA addendum currency review | quarterly | DPO |
| Disclosure currency review (public + in-product) | quarterly | AI Lead |
| Bias review (protected-class features) | quarterly | DPO + AI Lead |

### Step 4: Audit-window operating procedure

Once the audit window opens (per the attestation preparation spec):

- **Daily** — hash-chain integrity report reviewed; anomaly tickets triaged.
- **Weekly** — evidence sweep (every evidence artefact captured for the week); manifest hash recorded.
- **Monthly** — SLO report assembled; daily-review tickets sampled; approval events sampled.
- **Quarterly** — drills executed; access reviews; sub-processor review; BAA/DPA review; bias review; auditor portal dry run.
- **Mid-window (T-3)** — gap check; remediation actions for any control with < 95% evidence completeness.
- **T-1** — closure preparation; auditor portal access prepared; on-the-day playbook printed.
- **T+1** — auditor fieldwork begins; playbook activated.

### Step 5: On-the-day playbook activation

When the auditor walks in (or joins the video call):

1. Compliance Manager confirms auditor identity; activates portal access for named recipient; logs activation.
2. Demoer roster confirmed; back-up demoers on standby.
3. Walkthrough order set with auditor.
4. Each walkthrough follows the auditor on-the-day playbook (`24-ai-agent-attestation-preparation-spec/references/ai-agent-auditor-on-the-day-playbook.md`).
5. Action items recorded as they arise; closure target before auditor leaves where possible.
6. End of day: portal access reduced to read-only; debrief held.

### Step 6: Gap-remediation cadence

| Severity | Definition | SLA | Owner |
|----------|------------|-----|-------|
| SEV1 | Mandatory control without evidence; control failed during the window | 7 days | AI Lead + CTO |
| SEV2 | Evidence incomplete; sampling not yet attainable | 30 days | AI Lead |
| SEV3 | Documentation polish; cross-link missing | 90 days | Compliance Manager |

### Step 7: Roles

| Role | Responsibility |
|------|-----------------|
| AI Lead | Compliance posture for agent features; evidence custodian; demoer for governance and approval walkthroughs |
| CTO | Change management sample; system architecture walkthrough |
| CISO | Kill-switch drill owner; security control walkthroughs |
| DPO | Privacy controls; DSAR; BAA/DPA addenda; sub-processor reviews; bias review co-owner |
| Compliance Manager | Audit-window orchestration; auditor portal; sign-off ledger; pack assembly |
| SRE Lead | Drill execution; observability evidence; orchestrator availability evidence |

### Step 8: Write the runbook

`AI_Agent_Compliance_Runbook.md` sections: 1) Drill Schedule, 2) Evidence-Collection Schedule, 3) Control-Test Schedule, 4) Audit-Window Operating Procedure, 5) On-the-Day Playbook Activation, 6) Gap-Remediation Cadence, 7) Roles, 8) Calendar Index, 9) Cross-Refs, 10) Sign-off.

## Standards

- AICPA AT-C Section 205
- ISO/IEC 27001 Clauses 9.1, 9.2
- ISO/IEC 17021-1
- HIPAA §164.308(a)(8)
- Google SRE (drill discipline)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-compliance-runbook-template.md`.
