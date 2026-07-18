---
name: 15-ai-rca-taxonomy-doc
description: Use when producing or updating AI root-cause taxonomy for stable failure families, tags, examples, detection links, and mitigation pointers. Use incident-postmortem for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI RCA Taxonomy Doc Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI root-cause taxonomy from approved project evidence.
- Resolve decisions about stable failure families, tags, examples, detection links, and mitigation pointers.
- Prepare a reviewable handoff for Incident reviewers and governance teams.

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
| AI Root-cause Taxonomy | Incident reviewers and governance teams | Every taxonomy node is distinct, illustrated, linked to detection and containment, and usable in a postmortem. |
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
| Evidence is complete and authority is explicit | Choose the narrowest evidence-supported primary and contributing tags and produce the full artefact. | Free-text causes that cannot reveal recurrence. |
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

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every taxonomy node is distinct, illustrated, linked to detection and containment, and usable in a postmortem.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

When a postmortem closes with a free-text root cause, the engine accumulates noise. The RCA taxonomy gives the team a shared vocabulary: every postmortem closes with one or more taxonomy tags, and the rolling Responsible-AI committee review aggregates by tag to find systemic weaknesses (e.g., 4 of the last 10 incidents were `retrieval.index-drift` — investment indicated).

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Response Runbook, Hallucination SLO, Rollout Runbook, Cost Runbook, AI Architecture, Eval Harness, Red-Team Plan, Model Card |
| **Output** | `AI_RCA_Taxonomy_Doc.md` |
| **Standards** | NIST AI RMF MAP-2; ISO/IEC 42001 Annex A.6; CAST (Causal Analysis based on Systems Theory) |

## Core Instructions

### Step 1: Six families

1. **Model** — primary or fallback foundation-model behaviour.
2. **Retrieval** — RAG index, embeddings, ranking, citations.
3. **Tool / agent** — agent tools, schemas, scopes, indirect injection.
4. **Eval** — golden sets, judge LLMs, calibration, test-set leakage.
5. **Data** — training data, ingestion, distribution shift.
6. **Infra & commercial** — gateway, routing, provider pricing, provider rate limits.

### Step 2: Enumerate nodes per family

State the canonical list per family (see `references/ai-rca-taxonomy-reference.md` for the catalogue). For each node:

- Node id (`family.node`).
- One-sentence definition.
- Example incident (synthetic or anonymised real).
- Default containment pointer (one of the six modes; per `14-ai-incident-response-runbook`).
- Pre-production detection (eval harness test, red-team test, monitoring alert).
- Durable mitigation (typical action-item class).

### Step 3: Tagging rule

Every postmortem closes with at least one tag, optionally multiple. Tags can be `primary` and `contributing`. The IC assigns; the RAI committee can re-tag during review with justification.

### Step 4: Aggregation rule

The Responsible-AI committee reviews tag frequency monthly. Investment thresholds:

- 3 or more incidents tagged the same node in a quarter -> action item escalated to road-map.
- 1 incident tagged a node with SEV1 outcome -> review the pre-production detection for that node.

### Step 5: Write the doc

`AI_RCA_Taxonomy_Doc.md` sections: 1) Families, 2) Node Catalogue, 3) Tagging Rule, 4) Aggregation & Review Cadence, 5) Cross-Refs.

## Standards

- NIST AI RMF MAP-2
- ISO/IEC 42001 Annex A.6 (incident handling and improvement)
- CAST (causal analysis based on systems theory, Leveson)
- Google SRE blameless RCA

## Resources

- `logic.prompt`, `README.md`, `references/ai-rca-taxonomy-reference.md`.
