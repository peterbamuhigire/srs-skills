---
name: 16-ai-incident-postmortem-template
description: Use when producing or updating AI incident postmortem for source-attributed timeline, impact, taxonomy-based causes, actions, and publication decision. Use incident-response-runbook for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Incident Postmortem Template Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI incident postmortem from approved project evidence.
- Resolve decisions about source-attributed timeline, impact, taxonomy-based causes, actions, and publication decision.
- Prepare a reviewable handoff for Service owners, governance, and customers as approved.

## Do Not Use When

- The task is primarily owned by incident-response-runbook; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, and relevant architecture | Project owner and upstream phase skills | Required | Stop at a gap register; do not invent scope, thresholds, integrations, or owners. |
| Existing artefact, implementation, configuration, and evidence named below | Repository, delivery team, or service owner | Required when updating or assessing | Mark inaccessible items `not assessed`; do not treat them as passed. |
| Target audience, environment, risk tolerance, and authority | Requester and accountable owner | Required | Produce a read-only outline with explicit assumptions; do not mutate project or production state. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Incident Postmortem | Service owners, governance, and customers as approved | The postmortem is blameless, evidence-linked, names residual risk, and assigns each corrective action an owner and due date. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Assessment and planning default to read-only. Create or edit the named project document only when the request explicitly authorises it. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose conclusions only from preserved incident evidence and produce the full artefact. | Blame, hindsight narratives, or unsupported causes. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring incident-response-runbook concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when the postmortem is blameless, evidence-linked, names residual risk, and assigns each corrective action an owner and due date.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
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
