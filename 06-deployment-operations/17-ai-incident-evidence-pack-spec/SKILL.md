---
name: 17-ai-incident-evidence-pack-spec
description: Use when producing or updating AI incident evidence-pack specification for capture, chain of custody, retention, redaction, reproducibility, and handover. Use incident-response-runbook for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Incident Evidence Pack Spec Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI incident evidence-pack specification from approved project evidence.
- Resolve decisions about capture, chain of custody, retention, redaction, reproducibility, and handover.
- Prepare a reviewable handoff for Incident, legal, security, and audit teams.

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
| AI Incident Evidence-pack Specification | Incident, legal, security, and audit teams | Every evidence item has a source, capture method, integrity check, access policy, retention rule, and handover format. |
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
| Evidence is complete and authority is explicit | Choose evidence scope from severity, affected data, and legal obligations and produce the full artefact. | Missing or over-collected incident evidence. |
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

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every evidence item has a source, capture method, integrity check, access policy, retention rule, and handover format.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

An AI incident produces a unique evidence surface: the prompt, the model version, the tool calls, the retrieval set, and the eval output at the moment of failure must be preserved together. Without that bundle, the postmortem cannot reach a defensible root cause and the regulator handover cannot be assembled within the EU AI Act Art. 73 or GDPR Art. 33 windows.

This skill produces the spec. The software-dev engine pass owns the implementation (evidence-bundle exporter, reproduce-script generator, price-table snapshotter); this spec is the contract.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Severity Matrix, Response Runbook, AI Architecture, Hallucination SLO, Cost Runbook, Model Card, AI Act doc, Tenancy Spec |
| **Output** | `AI_Incident_Evidence_Pack_Spec.md` |
| **Standards** | EU AI Act Art. 12 (logs); Art. 20 (corrective actions); GDPR Art. 30 (records); ISO/IEC 42001 Clause 9.1 |

## Core Instructions

### Step 1: Evidence items

The pack carries at minimum the following items per incident:

1. **Trace bundle** — every model call, tool call, and gateway decision affected by the incident; full request/response with prompt id, model id, tool id, tenant id; time-bounded.
2. **Prompt + model + tool versions at T** — snapshot of the prompt registry, model gateway routing config, agent tool registry at the incident start time.
3. **Retrieval set** — for RAG incidents, the documents retrieved per affected request; index id and snapshot id.
4. **Eval output at T** — the most recent eval run before the incident; the run that gated the latest release; calibration-set scores.
5. **Customer-affected list** — tenant ids, user ids (subject to data-protection scope), affected request count, autonomous-action count per tenant.
6. **Action audit log** — for agent-action incidents: every tool call that succeeded, every record mutated, every recipient contacted.
7. **Reproduce script** — a deterministic script that re-runs the failing request against the pinned configuration and reproduces the failure (best-effort for non-deterministic models; expected to surface the regression).
8. **Model-price-table snapshot** — provider price list at T (for cost-runaway incidents and for postmortem cost calculation).
9. **Containment-action log** — every containment mode invoked, time, operator id, verification outcome.
10. **Customer comms artefacts** — outgoing emails, status-page snapshots, tenant-notifications.

### Step 2: Chain-of-custody

- Each item is captured to immutable storage (write-once-read-many, or content-addressed with append-only audit log).
- Capture is automatic on incident declaration; the IC may extend the time window during the incident.
- Each capture event names: source system, time window, capture operator (or job id), hash of the captured artefact, storage location.
- Modifying a captured item is impossible by design; redaction creates a derived artefact with a back-link.

### Step 3: Retention per severity

| Severity | Retention | Justification |
|----------|-----------|---------------|
| SEV1 | 7 years | EU AI Act Art. 12 + audit timeline; potential litigation |
| SEV2 | 3 years | postmortem cycle + audit timeline |
| SEV3 | 1 year | learning + trend analysis |
| SEV4 | 90 d | minor noise window |

Override per tenant DPA if longer is contractually required. Adhere to "right to erasure" exceptions (GDPR Art. 17(3)(b), Art. 17(3)(e)) for incident records.

### Step 4: Redaction policy

For external handover (regulator or affected-tenant):

- Other tenants' data redacted by default.
- User-identifying fields redacted unless required by the receiving authority.
- Provider-confidential information (model architecture details under NDA) redacted.
- Redaction log appended to the pack; redacted-vs-unredacted is auditable.

### Step 5: Regulator-handover packaging

For Art. 73 / Art. 33 / state-level / African regulators:

- The pack is exported as a sealed bundle (signed zip or equivalent).
- Index manifest names every artefact, its hash, its capture provenance, and any redactions.
- Cross-reference to the regulator-notification template (`09-governance-compliance/18-ai-regulator-incident-notification-doc`).
- DPO/legal sign-off recorded in the manifest before handover.

### Step 6: Access policy

- Read access in normal operation: AI lead, SRE on-call, security, DPO, legal, exec sponsor — by role.
- Read access for customer-distribution: redacted view only.
- Read access for regulator handover: time-bound, logged, named recipient.

### Step 7: Write the spec

`AI_Incident_Evidence_Pack_Spec.md` sections: 1) Evidence Items, 2) Chain-of-Custody, 3) Retention, 4) Redaction Policy, 5) Regulator-Handover Packaging, 6) Access Policy, 7) Capture Tooling (cross-link to software-dev pass), 8) Cross-Refs.

## Standards

- EU Reg 2024/1689 Art. 12 (record-keeping), Art. 20 (corrective actions)
- EU Reg 2016/679 Art. 30 (records of processing)
- ISO/IEC 42001 Clause 9.1 (monitoring)
- NIST AI RMF MEASURE-3 (record of decisions)

## Relationship to the compliance evidence pack

The incident evidence pack is a **superset** of the compliance evidence pack for the affected control rows during the incident window:

- Trace bundle, action audit log, reproduce script, and price-table snapshot all feed back into the SOC 2 PI1.4, ISO A.8.15/A.8.24, and HIPAA §164.312(b)/(c) evidence rows for the audit window.
- The incident pack chain-of-custody and redaction rules apply unchanged when those artefacts are referenced by the compliance pack.
- The compliance pack manifest cross-references each incident pack by `incident_id` and inherits its hash.

See `09-governance-compliance/25-ai-agent-evidence-pack-spec` for the steady-state pack and the auditor portal contract; this spec governs the per-incident superset.

## Resources

- `logic.prompt`, `README.md`, `references/ai-incident-evidence-pack-spec-template.md`.
