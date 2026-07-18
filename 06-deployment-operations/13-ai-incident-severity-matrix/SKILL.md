---
name: 13-ai-incident-severity-matrix
description: Use when producing or updating AI incident severity matrix for severity criteria, impact dimensions, escalation, containment, notification, and downgrade rules. Use incident-response-runbook for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Incident Severity Matrix Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI incident severity matrix from approved project evidence.
- Resolve decisions about severity criteria, impact dimensions, escalation, containment, notification, and downgrade rules.
- Prepare a reviewable handoff for Incident commanders and responders.

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
| AI Incident Severity Matrix | Incident commanders and responders | A responder can assign severity from observable impact and trigger the matching containment and notification obligations. |
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
| Evidence is complete and authority is explicit | Choose the highest severity supported by observed impact and produce the full artefact. | Under-classification that delays containment. |
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

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when a responder can assign severity from observable impact and trigger the matching containment and notification obligations.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
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
