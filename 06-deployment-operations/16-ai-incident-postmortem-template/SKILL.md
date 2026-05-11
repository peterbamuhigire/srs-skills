---
name: "ai-incident-postmortem-template"
description: "Generate the blameless AI Incident Postmortem template: timeline, RCA classification (against the AI RCA taxonomy), contributing factors, per-tenant impact, regulator-impact assessment, action items by class (improve eval, change gate, add red-team test, etc.), public publication policy."
metadata:
  use_when: "Use after every AI incident at SEV2 or above. Use optionally at SEV3 if the failure class is novel or the taxonomy tag is new."
  do_not_use_when: "Do not use as a substitute for the SaaS postmortem on a pure availability incident with no AI dimension."
  required_inputs: "AI_Incident_Severity_Matrix.md, AI_Incident_Response_Runbook.md, AI_RCA_Taxonomy_Doc.md, AI_Incident_Evidence_Pack_Spec.md, incident timeline, AI_Hallucination_SLO_Doc.md (for budget burn), pricing & packaging spec (for service-credit calc)."
  workflow: "Confirm severity and tag against the taxonomy, write timeline from scribe notes, write per-tenant impact from the evidence pack, write regulator-impact assessment, write action items keyed to RCA tag, decide publication posture, write the postmortem."
  quality_standards: "Every postmortem shall be blameless. Every postmortem shall close with one or more RCA taxonomy tags. Every action item shall have an owner, due date, and class (improve eval, change gate, add red-team test, change containment, etc.). Every SEV1 postmortem shall include a regulator-impact assessment regardless of whether reporting was triggered."
  anti_patterns: "Do not name individuals as causes. Do not close a postmortem without a taxonomy tag. Do not omit the regulator-impact assessment on SEV1 even if no reporting was triggered."
  outputs: "AI_Postmortem_<incident_id>.md per incident."
  references: "Use references/ai-incident-postmortem-template.md."
---

# AI Incident Postmortem Template Skill

## Overview

The blameless postmortem template for AI incidents. Extends the SaaS postmortem with RCA-taxonomy tagging, per-tenant AI-impact reporting, regulator-impact assessment, AI-specific action-item classes (improve eval, change gate, add red-team test, change containment, change provider posture, update model card), and a public-publication policy.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Severity Matrix, Response Runbook, RCA Taxonomy, Evidence Pack, timeline, Hallucination SLO, pricing |
| **Output** | `AI_Postmortem_<incident_id>.md` per incident |
| **Standards** | Google SRE blameless postmortem; ISO/IEC 42001 Clause 10; NIST AI RMF MANAGE-4 |

## Core Instructions

### Step 1: Header and metadata

Incident ID, dates, severity (final), tenant scope, autonomy level, AI failure class, RCA taxonomy tags (primary + contributing), author, status (draft / under review / published / closed).

### Step 2: Summary and impact

One paragraph summary. Impact section names: tenants affected (count + named for Enterprise), duration, error-budget burn per affected SLO, financial impact estimate (service credits + churn risk + provider cost), support load (tickets, peak concurrent), reputational impact (press, social).

### Step 3: Timeline

UTC. Source-attributed (alert id, dashboard, customer ticket, scribe note). Reconstructed from the evidence pack, not from memory.

### Step 4: Root-cause analysis

5-whys with the taxonomy tag attached to each level. Identify primary tag and contributing tags. Cross-link the evidence pack entries.

### Step 5: Per-tenant impact

Table per tenant: tenant id (anonymised for Free/Pro; named for Enterprise), severity-experienced, requests affected, outputs flagged, autonomous actions taken (if any), reconciliation required, comms sent, service credit owed.

### Step 6: Regulator-impact assessment

For every SEV1, regardless of whether reporting was triggered:

- EU AI Act Art. 73 limbs evaluated; verdict per limb; window applicable; notification status.
- GDPR Art. 33 evaluated; verdict; notification status; clock start time.
- US state-level applicable (NYC AEDT, CO SB24-205, CA ADMT) evaluated.
- African regulators applicable (Kenya ODPC, Nigeria NDPC, POPIA) evaluated.
- DPO sign-off on the assessment.

### Step 7: Action items by class

Action-item classes (each carries owner, due date, severity):

- **Improve eval** — add a test or extend coverage to catch this class pre-production.
- **Change gate** — strengthen a promotion gate in the rollout runbook.
- **Add red-team test** — add a red-team probe to the plan.
- **Change containment** — strengthen one of the six containment modes or add a new mode.
- **Change provider posture** — pin model version, add fallback, multi-provider, change rate-limit contract.
- **Update model card** — disclose the failure mode and the change.
- **Update runbook** — patch the per-failure-class procedure if the playbook proved wrong.
- **Update training material** — add to drill catalogue, update game-day exercises.

### Step 8: Publication policy

For each postmortem decide:

- **Internal-only** (default for SEV3, SEV4).
- **Customer-distributed** (SEV1 and SEV2 affecting tenants) — sent to affected tenants via the comms template.
- **Public** — published to trust-center / blog. Required when Art. 73 reporting occurred or when the incident was widely visible. Redaction policy named.

### Step 9: Closure

Postmortem closes when all SEV-high action items are done. Postmortem closure is independent of incident closure.

### Step 10: Write the doc

`AI_Postmortem_<incident_id>.md` per the template in `references/`.

## Standards

- Google SRE blameless postmortem
- ISO/IEC 42001 Clause 10 (improvement)
- NIST AI RMF MANAGE-4 (response and recovery)
- EU Reg 2024/1689 Art. 73 (reporting)
- EU Reg 2016/679 Art. 33 (breach reporting)

## Resources

- `logic.prompt`, `README.md`, `references/ai-incident-postmortem-template.md`.
