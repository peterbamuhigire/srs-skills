---
name: "ai-incident-response-runbook"
description: "Generate the AI Incident Response Runbook: timed first-five / first-thirty / first-two-hour playbook; per-failure-class procedures (hallucination spike, prompt drift, model regression, jailbreak/injection, tool-chain failure, cost runaway, agent-action incident, training-data shift, retrieval drift, eval drift); kill-switch, model-fallback, prompt-rollback, index-pinning, abstain-mode, and read-only-mode procedures."
metadata:
  use_when: "Use for any SaaS shipping AI features in production. Mandatory before GA. Mandatory before any feature with autonomy beyond advisory."
  do_not_use_when: "Do not use for AI features that ship without a kill switch, without versioned prompts, or without a model fallback ladder — fix those first."
  required_inputs: "AI_Incident_Severity_Matrix.md, AI_Hallucination_SLO_Doc.md, AI_Feature_Rollout_Runbook.md, AI_Cost_Runbook.md, AI_Feature_PRD_Spec.md, AI_Architecture_Spec.md, Multi_Tenancy_Architecture_Spec.md, Runbook.md (parent SaaS runbook)."
  workflow: "Define IC roles, define timed phases, write per-failure-class procedures, write the six containment-mode procedures (kill switch, model fallback, prompt rollback, index pinning, abstain mode, read-only mode), define handoff rules, write the runbook."
  quality_standards: "Every AI failure class shall have a per-class procedure. Every procedure shall name the command, the system, the rollback, and the verification step. The runbook shall be usable on the day of an incident by an on-call engineer with no AI specialisation."
  anti_patterns: "Do not write the runbook as prose. Do not omit the kill-switch step. Do not omit the verification step after each containment action. Do not assume the on-call engineer knows which prompt-tag is current."
  outputs: "AI_Incident_Response_Runbook.md."
  references: "Use references/ai-incident-response-runbook-template.md, ai-incident-classification-decision-tree.md."
---

# AI Incident Response Runbook Skill

## Overview

Operator-grade runbook for AI incidents. The runbook is the document the on-call engineer reaches for when the AI quality SLO burn-rate alert fires, when the cost-anomaly alert fires, when a customer reports the AI took the wrong action, or when a red-team finding escalates. It must be unambiguous, timed, and reach a containment action within the first 30 minutes for SEV1.

This skill produces that runbook. It pairs the severity matrix (`13-ai-incident-severity-matrix`) and the comms templates (`18-ai-incident-customer-comms-templates`).

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Severity Matrix, Hallucination SLO, Rollout Runbook, Cost Runbook, AI PRD, AI Architecture, Tenancy Spec, parent Runbook |
| **Output** | `AI_Incident_Response_Runbook.md` |
| **Standards** | Google SRE; Anthropic / OpenAI production playbooks; NIST SP 800-61 (adapted for AI); ISO/IEC 42001 Clause 8 |

## Core Instructions

### Step 1: Define incident-command roles

Name the roles, even for small teams (one person may hold multiple at once). For an AI incident the minimum cast is:

- Incident commander (IC).
- AI lead on-call (knows prompts, models, eval, retrieval).
- SRE on-call (knows gateway, feature flags, infrastructure).
- Comms lead (customer + status page + internal).
- Scribe (timeline writer; preserves chain-of-custody evidence).

Add for SEV1: legal/DPO on-call, security on-call (mandatory for injection-class), CSM on-call for Enterprise tenants, executive sponsor.

### Step 2: Define timed phases

| Phase | Window | Goal |
|-------|--------|------|
| Detect | continuous | alert fires, customer report, red-team escalation |
| Triage | 0-5 min (SEV1), 0-15 min (SEV2) | classify by failure class; assign IC; declare severity |
| Contain | 0-30 min (SEV1) | invoke at least one containment mode; stop the bleeding |
| Investigate | 30-120 min | reproduce; preserve evidence; identify root cause class |
| Mitigate | 1-4 h (SEV1) | apply the durable fix or hold containment until fixed |
| Resolve | when monitoring confirms 30 min healthy | declare resolved; status-page update |
| Postmortem | within 5 BD SEV1, 10 BD SEV2 | per `16-ai-incident-postmortem-template` |

### Step 3: Write per-failure-class procedures

For each AI failure class produce a one-page procedure of the form:

1. **Detection signal** — alert name, dashboard, customer-report keyword.
2. **First-five steps** — verify the signal; confirm the failure class; declare severity per the matrix.
3. **Containment** — which of the six containment modes to invoke; explicit command.
4. **Verification** — query to confirm containment is effective.
5. **Evidence to preserve** — per `17-ai-incident-evidence-pack-spec`.
6. **Investigation path** — RCA taxonomy nodes (per `15-ai-rca-taxonomy-doc`) most likely.
7. **Customer comms trigger** — which template, who sends.
8. **Regulator-notification trigger** — which clock starts (Art. 73 / Art. 33 / state-level / African).
9. **Resolution criteria** — when to call it done.

Classes to cover (one procedure each): hallucination spike, prompt drift, model regression, jailbreak/injection (direct), jailbreak/injection (indirect via retrieval or tool), tool-chain failure, cost runaway, agent-action incident, training-data shift / distribution shift, retrieval drift, eval drift.

### Step 4: Write the six containment-mode procedures

Each must be runnable by an on-call engineer who has not read the architecture doc this quarter.

- **Kill switch** — feature flag toggle that disables the AI feature for all tenants. State the flag name, the system (LaunchDarkly / Statsig / homegrown), the command, the rollback command, the verification.
- **Model fallback** — gateway route from primary model to fallback model. State the gateway config key, the values, the verification (sample call returns from fallback).
- **Prompt rollback** — revert the prompt tag to the last green tag. State the prompt-registry command, the tag-listing command, the tag-pinning command, the verification.
- **Index pinning** — pin the retrieval index to the last known-good snapshot; freeze re-indexing. State the index id, the snapshot id, the pin command.
- **Abstain mode** — switch the feature to return an abstain payload instead of attempting a generation. State the config switch and the user-facing copy that ships with abstain.
- **Read-only mode** — disable any tool that writes (sends email, updates records, modifies files); the AI can read and recommend but not act. State the tool registry and the disable command per tool.

Cross-link to the software-dev engine pass which owns the underlying code for these switches.

### Step 5: Define handoff rules

State when the AI lead on-call hands off to a different specialist (security on-call for confirmed injection; DPO for confirmed cross-tenant leakage; FinOps for confirmed cost runaway). State the shift-rotation rules for an incident running past 4 hours.

### Step 6: Define joint-incident protocol with the SaaS incident process

The AI incident may also be a SaaS incident (data corruption, identity issue, billing). State which IR process leads (SaaS for availability and data; AI for quality and autonomy; security for confidentiality / injection). One IC overall; specialised leads underneath.

### Step 7: Write the doc

`AI_Incident_Response_Runbook.md` sections: 1) Roles, 2) Timed Phases, 3) Classification Decision Tree, 4) Per-Failure-Class Procedures, 5) Containment-Mode Procedures, 6) Handoff Rules, 7) Joint-Incident Protocol, 8) Cross-Refs.

## Standards

- Google SRE incident management
- Anthropic / OpenAI production-LLM playbooks
- NIST SP 800-61 Rev. 2 (adapted)
- ISO/IEC 42001 Clause 8 (operation)
- EU Reg 2024/1689 Art. 73 (reporting trigger)

## Resources

- `logic.prompt`, `README.md`, `references/ai-incident-response-runbook-template.md`, `references/ai-incident-classification-decision-tree.md`.
