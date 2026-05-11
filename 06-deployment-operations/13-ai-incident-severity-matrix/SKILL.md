---
name: "ai-incident-severity-matrix"
description: "Generate the AI Incident Severity Matrix: three-dimensional severity (sev x tenant-scope x autonomy/blast-radius); per-AI-failure-class thresholds (hallucination spike, prompt drift, model regression, jailbreak/injection, tool-chain failure, cost runaway, agent-action incident, retrieval drift, eval drift); mapping to customer-SLA service credits and EU AI Act Article 73 serious-incident definitions."
metadata:
  use_when: "Use for any SaaS shipping AI features that can fail in AI-specific ways (hallucination, injection, agent action, cost runaway). Mandatory before GA. Mandatory before any high-risk EU AI Act feature reaches the EEA."
  do_not_use_when: "Do not use for non-AI features. Do not use for internal AI experiments with no customer exposure and no autonomy."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Hallucination_SLO_Doc.md, AI_Cost_Runbook.md, AI_Feature_Rollout_Runbook.md, Multi_Tenancy_Architecture_Spec.md, pricing & packaging spec, AI_Act_And_Regulatory_Compliance_Doc.md."
  workflow: "Define the three dimensions, set per-failure-class thresholds, map to service credits, map to EU AI Act Article 73 serious-incident definitions, define elevation rules, write the AI_Incident_Severity_Matrix.md doc."
  quality_standards: "Every AI failure class shall appear in the matrix. Every severity row shall include tenant-scope and autonomy/blast-radius dimensions. Every SEV1 row shall name the SLA service-credit consequence and the regulator-notification consequence."
  anti_patterns: "Do not collapse severity to a single dimension. Do not treat agent-action incidents at the same severity floor as a hallucination spike. Do not omit the autonomy dimension; an autonomous agent that took an unauthorised action is operationally different from a chatbot that said something wrong."
  outputs: "AI_Incident_Severity_Matrix.md."
  references: "Use references/ai-incident-severity-matrix-template.md."
---

# AI Incident Severity Matrix Skill

## Overview

The SaaS severity matrix is two-dimensional (severity x tenant scope). AI features add a third operational dimension: **autonomy / blast-radius** — whether the AI output was advisory (the human acts on it), assistive (the human reviews and confirms), or autonomous (the AI acted on its own). An autonomous agent that sent the wrong email to the wrong recipient is operationally a different incident from a chatbot that produced a hallucinated answer, even at identical tenant scope.

This skill produces the three-dimensional matrix and the thresholds per AI failure class.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | AI PRD, Hallucination SLO, Cost Runbook, Rollout Runbook, Tenancy Spec, AI Act doc |
| **Output** | `AI_Incident_Severity_Matrix.md` |
| **Standards** | NIST AI RMF MANAGE-2; EU AI Act Art. 73; Google SRE; ISO/IEC 42001 Clause 8.3 |

## Core Instructions

### Step 1: Declare the three dimensions

- **Severity** — SEV1 / SEV2 / SEV3 / SEV4.
- **Tenant scope** — single tenant / tenant cohort / platform-wide / cross-tenant leakage.
- **Autonomy / blast-radius** — advisory / assistive / autonomous-with-rollback / autonomous-irreversible.

Cross-tenant leakage is a fourth tenant-scope value distinct from platform-wide because it has unique GDPR and AI-Act consequences.

### Step 2: Set per-AI-failure-class thresholds

Failure classes that must be named:

1. Hallucination spike.
2. Prompt drift / prompt regression.
3. Model regression (provider-side rotation or deprecation).
4. Jailbreak / prompt injection (direct or indirect).
5. Tool-chain failure (agent tool API change, schema change, vendor outage).
6. Cost runaway (token spend per tenant).
7. Agent-action incident (autonomous action with real-world side effect).
8. Training-data shift / distribution shift.
9. Retrieval drift (index rebuild, embedding-model change, citation drift).
10. Eval drift (golden-set rot, judge-LLM drift, test-set leakage).

For each class, name the SEV1 / SEV2 / SEV3 threshold against measurable signals (factuality drop >X pp; cost >Y% of ceiling; agent-action affected >Z records; etc.).

### Step 3: Map severity to SLA service credits

Cross-link the pricing & packaging spec. Per tier (Free / Pro / Enterprise), state the service-credit consequence of a confirmed AI incident at each severity. AI quality is not in scope for credits in most cases (per the Hallucination SLO doc, factuality is not contractually committed) but availability of the AI feature and cross-tenant leakage are.

### Step 4: Map severity to EU AI Act Article 73 serious-incident definitions

Article 73 of Regulation (EU) 2024/1689 defines a serious incident for a high-risk AI system as one causing or contributing to:

- death of a person or serious harm to a person's health;
- serious and irreversible disruption of the management or operation of critical infrastructure;
- infringement of obligations under Union law intended to protect fundamental rights;
- serious harm to property or the environment.

Map AI failure classes to which Article 73 limb they could trigger, and at what severity. Wide-scale incidents and incidents involving death or serious injury have immediate-reporting obligations (2 d for wide-scale or fundamental-rights infringement; "without delay and not later than 10 d" for death / serious harm); other serious incidents within 15 d of the provider becoming aware. Cross-link to the regulator-notification skill (`09-governance-compliance/18-ai-regulator-incident-notification-doc`).

### Step 5: Define elevation and de-escalation rules

State when the severity can be elevated mid-incident (new evidence of cross-tenant leakage; confirmed autonomous action with irreversible side effect; regulator inquiry opened) and when it can be de-escalated (confirmed bounded blast radius; abstain-mode active and effective). Severity changes require incident-commander confirmation and are logged in the timeline.

### Step 6: Write the doc

`AI_Incident_Severity_Matrix.md` sections: 1) Dimensions, 2) Per-Failure-Class Thresholds, 3) Service-Credit Mapping, 4) EU AI Act Art. 73 Mapping, 5) Elevation / De-escalation Rules, 6) Cross-Refs.

## Standards

- NIST AI RMF MANAGE-2
- EU Reg 2024/1689 Art. 73 (AI Act serious-incident reporting)
- ISO/IEC 42001 Clause 8.3 (operational risk management)
- Google SRE severity classification

## Resources

- `logic.prompt`, `README.md`, `references/ai-incident-severity-matrix-template.md`.
