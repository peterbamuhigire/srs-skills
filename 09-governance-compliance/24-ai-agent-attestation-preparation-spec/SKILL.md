---
name: "ai-agent-attestation-preparation-spec"
description: "Generate the AI Agent Attestation Preparation Spec: end-to-end preparation for SOC 2 Type II window, ISO/IEC 27001 surveillance audit, and HIPAA periodic review. Defines the 12-month timeline, the evidence pre-gathering schedule, the auditor-readiness checklist, the gap-remediation cadence, and the on-the-day auditor playbook for agent-specific control areas."
metadata:
  use_when: "Use 12 months before a SOC 2 Type II report window opens, 6 months before an ISO surveillance audit, or 90 days before a HIPAA covered-entity periodic review. Refreshed each cycle."
  do_not_use_when: "Do not use as a substitute for the SOC 2 control pack or the evidence pack spec — this skill orchestrates them in time. Do not use this for SOC 2 Type I (point-in-time); the timeline structure assumes a Type II window."
  required_inputs: "AI_Agent_SOC2_Control_Pack.md, AI_Agent_ISO27001_Control_Pack.md, AI_Agent_HIPAA_Control_Pack.md, AI_Agent_Compliance_Policy_Pack.md, AI_Agent_Evidence_Pack_Spec.md, AI_Agent_Compliance_Runbook.md, prior-year audit findings (if any), engagement letter from auditor."
  workflow: "Build the 12-month timeline; build the evidence pre-gathering schedule; build the auditor-readiness checklist; declare the gap-remediation cadence; produce the on-the-day playbook; record sign-off."
  quality_standards: "The timeline shall name every milestone with a date and an owner. The pre-gathering schedule shall list every evidence artefact with collector ownership and target date. The readiness checklist shall be 50-100 points covering policy, controls, evidence, training, drills. The on-the-day playbook shall name the demoer, the click path, and the artefact per question."
  anti_patterns: "Do not start preparation < 6 months before the window for SOC 2 Type II. Do not let policy review slip into the audit window. Do not omit drill rehearsal of the auditor walkthroughs. Do not skip prior-year finding follow-up."
  outputs: "AI_Agent_Attestation_Preparation_Spec.md, AI_Agent_Compliance_Readiness_Checklist.md, AI_Agent_Auditor_On_The_Day_Playbook.md."
  references: "Use references/ai-agent-compliance-readiness-checklist.md and references/ai-agent-auditor-on-the-day-playbook.md."
---

# AI Agent Attestation Preparation Spec Skill

## Overview

Attestation preparation is the orchestration layer over the control packs, policy pack, and evidence pack: it places every artefact on a 12-month timeline, drives a gap-remediation cadence, and produces the on-the-day playbook the team executes when the auditor walks in.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | SOC 2 / ISO / HIPAA control packs, Policy Pack, Evidence Pack Spec, Compliance Runbook, prior-year findings, auditor engagement letter |
| **Output** | `AI_Agent_Attestation_Preparation_Spec.md` + Readiness Checklist + Auditor On-The-Day Playbook |
| **Standards** | AICPA AT-C 205 (SOC 2); ISO/IEC 27001 Clause 9.2 (internal audit) and ISO/IEC 17021 (certification body process); HIPAA §164.308(a)(8) (evaluation) |

## Core Instructions

### Step 1: 12-month timeline for SOC 2 Type II

| Month | Milestones |
|-------|------------|
| T-12 | Engagement letter signed; window dates set; auditor scope confirmed; prior-year findings reviewed |
| T-11 | Policy pack refreshed; signatures collected |
| T-10 | Control pack refreshed; SoA delta merged into parent ISMS SoA |
| T-9 | Evidence-collector configuration verified (cross-engine handoff to software-dev pass) |
| T-8 | Kill-switch drill in staging; report produced |
| T-7 | Internal audit (sample 25 events per control class); findings remediated |
| T-6 | Pre-window dry run with internal audit team; gap analysis |
| T-5 | Window opens; daily integrity reports begin; weekly evidence sweeps |
| T-3 | Mid-window gap check; remediation if any control has < 95% evidence completeness |
| T-1 | Closure preparation; auditor portal access prepared |
| T-0 | Window closes |
| T+1 | Fieldwork begins; on-the-day playbook activated |
| T+2 | Auditor walkthroughs; reperformance |
| T+3 | Auditor draft report; management response drafted |
| T+4 | Final report; corrective action plan; next cycle planning |

### Step 2: 6-month timeline for ISO 27001 surveillance

Compressed; focus on changes since last certification audit and on the agent-specific controls.

### Step 3: 90-day timeline for HIPAA covered-entity periodic review

| Day | Milestones |
|-----|------------|
| -90 | Covered-entity notice received; scope confirmed |
| -75 | PHI flow inventory refreshed; admin-only constraint verified per feature |
| -60 | BAA addenda current; provider BAA status confirmed |
| -45 | Audit-log integrity report produced |
| -30 | Daily-review ticket sample assembled; minimum-necessary review completed |
| -14 | Dry run with covered entity's security officer |
| 0 | Review meeting |
| +14 | Corrective action plan delivered if required |

### Step 4: Evidence pre-gathering schedule

For each evidence artefact in the evidence pack spec, declare:

- Target completion date relative to T-0.
- Collector owner (cross-link software-dev pass).
- Format expected.
- Sampling completion gate (25 events stratified, or full population).

### Step 5: Auditor-readiness checklist (50-100 points)

Adapt `references/ai-agent-compliance-readiness-checklist.md`. Cover: policy currency, control coverage, evidence completeness, training currency, drill recency, prior-year remediation, sub-processor list current, BAA current, public Responsible-AI Declaration current, in-product disclosures live, auditor portal prepared.

### Step 6: Gap-remediation cadence

| Severity | Definition | SLA |
|----------|------------|-----|
| SEV1 gap | Mandatory control without evidence | 7 days |
| SEV2 gap | Evidence incomplete or sampling not yet attainable | 30 days |
| SEV3 gap | Documentation polish; cross-link missing | 90 days |

### Step 7: On-the-day auditor playbook

For each likely auditor question type, prepare the demoer role, the click path, the artefact handed over, the response language. Adapt `references/ai-agent-auditor-on-the-day-playbook.md`.

### Step 8: Write the spec

`AI_Agent_Attestation_Preparation_Spec.md` sections: 1) Scope and engagement, 2) Timeline (per framework), 3) Evidence pre-gathering schedule, 4) Readiness checklist (reference), 5) Gap-remediation cadence, 6) On-the-day playbook (reference), 7) Prior-year findings status, 8) Cross-Refs, 9) Sign-off.

## Standards

- AICPA AT-C Section 205 (attestation engagements)
- AICPA SOC 2 reporting framework
- ISO/IEC 17021-1 (certification body requirements)
- ISO/IEC 27001 Clause 9.2 (internal audit)
- HIPAA §164.308(a)(8) (evaluation)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-compliance-readiness-checklist.md`, `references/ai-agent-auditor-on-the-day-playbook.md`.
