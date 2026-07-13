---
name: 14-ai-incident-response-runbook
description: Use when producing or updating AI incident response runbook for detection, classification, containment, evidence preservation, recovery, and communication. Use incident-postmortem for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Incident Response Runbook Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI incident response runbook from approved project evidence.
- Resolve decisions about detection, classification, containment, evidence preservation, recovery, and communication.
- Prepare a reviewable handoff for Incident commanders and responders.

## Do Not Use When

- The task is primarily owned by incident-postmortem; route there and use this skill only for its named output.
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
| AI Incident Response Runbook | Incident commanders and responders | Each incident class has a timed containment path, authority boundary, evidence checklist, recovery test, and communication owner. |
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
- Inspection is read-only by default. Create or edit the named project document only when explicitly authorised. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose containment from severity, autonomy, and affected surface and produce the full artefact. | Continued harmful operation or destroyed evidence. |
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
- Mixing the neighbouring incident-postmortem concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when each incident class has a timed containment path, authority boundary, evidence checklist, recovery test, and communication owner.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
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
