---
name: 24-ai-agent-attestation-preparation-spec
description: Use when planning evidence collection, remediation, rehearsals, and audit-day execution for an AI-agent SOC 2 Type II, ISO 27001 surveillance, or HIPAA review. Use control packs to define controls and evidence-pack-spec to define evidence handling.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Agent Attestation Preparation Spec Skill

<!-- dual-compat-start -->

## Use When

- Use when planning evidence collection, remediation, rehearsals, and audit-day execution for an AI-agent SOC 2 Type II, ISO 27001 surveillance, or HIPAA review. Use control packs to define controls and evidence-pack-spec to define evidence handling.

## Do Not Use When

- Do not use as a substitute for the SOC 2 control pack or the evidence pack spec — this skill orchestrates them in time. Do not use this for SOC 2 Type I (point-in-time); the timeline structure assumes a Type II window.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_SOC2_Control_Pack.md, AI_Agent_ISO27001_Control_Pack.md, AI_Agent_HIPAA_Control_Pack.md, AI_Agent_Compliance_Policy_Pack.md, AI_Agent_Evidence_Pack_Spec.md, AI_Agent_Compliance_Runbook.md, prior-year audit findings (if any), engagement letter from auditor. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A required source, owner, obligation, or acceptance condition is missing | Stop the affected claim and record the gap | Unsupported governance artefact |
| Evidence satisfies the declared acceptance condition | Record the decision and hand off to the named consumer | Ambiguous approval or release |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Agent Attestation Preparation Spec | Accountable reviewer, control owner, auditor, or release authority | The timeline shall name every milestone with a date and an owner. The pre-gathering schedule shall list every evidence artefact with collector ownership and target date. The readiness checklist shall be 50-100 points covering policy, controls, evidence, training, drills. The on-the-day playbook shall name the demoer, the click path, and the artefact per question. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent Attestation Preparation Spec evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- The timeline shall name every milestone with a date and an owner. The pre-gathering schedule shall list every evidence artefact with collector ownership and target date. The readiness checklist shall be 50-100 points covering policy, controls, evidence, training, drills. The on-the-day playbook shall name the demoer, the click path, and the artefact per question.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent Attestation Preparation Spec from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a required source, owner, obligation, or acceptance condition is missing, stop the affected claim and record the gap. Record the evidence and result in the validation record; this avoids unsupported governance artefact.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

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
