---
name: 20-ai-agent-compliance-runbook
description: Use when producing or updating AI-agent compliance operations runbook for control testing, evidence collection, drills, audit-window operations, and remediation. Use agent-runbook for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Agent Compliance Runbook Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI-agent compliance operations runbook from approved project evidence.
- Resolve decisions about control testing, evidence collection, drills, audit-window operations, and remediation.
- Prepare a reviewable handoff for Compliance, control owners, and auditors.

## Do Not Use When

- The task is primarily owned by agent-runbook; route there and use this skill only for its named output.
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
| AI-agent Compliance Operations Runbook | Compliance, control owners, and auditors | Every control activity has an owner, cadence, evidence object, exception path, and closure verification. |
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
| Evidence is complete and authority is explicit | Choose cadence from control requirement and evidence freshness and produce the full artefact. | Audit-time evidence scrambles or untested controls. |
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
- Mixing the neighbouring agent-runbook concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every control activity has an owner, cadence, evidence object, exception path, and closure verification.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

The compliance runbook converts the control packs, policy pack, evidence pack spec, and attestation prep spec into a calendar-driven operating procedure: who does what, when, with what artefact. It is the daily / weekly / monthly / quarterly / annual heartbeat that keeps compliance posture continuous.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | SOC 2 / ISO / HIPAA control packs, Policy Pack, Evidence Pack Spec, Attestation Prep Spec, Agent Runbook, AI Incident Response Runbook |
| **Output** | `AI_Agent_Compliance_Runbook.md` |
| **Standards** | AICPA AT-C 205; ISO/IEC 27001 Clauses 9.1 and 9.2; ISO/IEC 17021; HIPAA §164.308(a)(8) |

## Core Instructions

### Step 1: Drill schedule

| Drill | Cadence | Owner | Verification |
|-------|---------|-------|--------------|
| Global kill-switch (staging) | quarterly | SRE Lead | Drill report; audit-log entry; propagation ≤ 5 s |
| Per-tenant kill-switch (staging) | quarterly | SRE Lead | Drill report |
| Per-feature kill-switch (staging) | quarterly | AI Lead | Drill report |
| Global kill-switch (production) | annual + on-event | SRE Lead | Drill report; tenant notification |
| Replay-a-run | quarterly | AI Lead | Drill report |
| Force-pause + force-resume | quarterly | SRE Lead | Drill report |
| Agent-task quarantine | annual | AI Lead | Drill report; tenant-admin notification |
| Evidence-pack assembly dry run | quarterly | Compliance Manager | Pack signed zip; manifest hash |
| BAA / DPA execution dry run | annual | DPO | Counter-signed addendum produced |
| Auditor portal access dry run | quarterly | Compliance Manager | Access granted to named test recipient; access revoked on day +1 |

### Step 2: Evidence-collection schedule

For every evidence artefact in the evidence frequency table, document:

- Calendar invite (recurring) with owner.
- Verification step (artefact present in pack at declared frequency).
- Escalation if missed (SEV2 if missed cadence × 2; SEV1 if missed × 3).

### Step 3: Control-test schedule

| Test | Cadence | Owner |
|------|---------|-------|
| Access review for agent service principals | quarterly | Security |
| Tool allow-list reperformance | quarterly | AI Lead |
| Hash-chain integrity verification | daily (automated) + weekly review | Security |
| Approval-event sample review (25 events) | monthly | AI Lead |
| Daily-review ticket sample review (25 tickets) | monthly | AI Lead |
| PR sample review (25 PRs) | quarterly | CTO |
| Sub-processor list review | quarterly | DPO |
| BAA / DPA addendum currency review | quarterly | DPO |
| Disclosure currency review (public + in-product) | quarterly | AI Lead |
| Bias review (protected-class features) | quarterly | DPO + AI Lead |

### Step 4: Audit-window operating procedure

Once the audit window opens (per the attestation preparation spec):

- **Daily** — hash-chain integrity report reviewed; anomaly tickets triaged.
- **Weekly** — evidence sweep (every evidence artefact captured for the week); manifest hash recorded.
- **Monthly** — SLO report assembled; daily-review tickets sampled; approval events sampled.
- **Quarterly** — drills executed; access reviews; sub-processor review; BAA/DPA review; bias review; auditor portal dry run.
- **Mid-window (T-3)** — gap check; remediation actions for any control with < 95% evidence completeness.
- **T-1** — closure preparation; auditor portal access prepared; on-the-day playbook printed.
- **T+1** — auditor fieldwork begins; playbook activated.

### Step 5: On-the-day playbook activation

When the auditor walks in (or joins the video call):

1. Compliance Manager confirms auditor identity; activates portal access for named recipient; logs activation.
2. Demoer roster confirmed; back-up demoers on standby.
3. Walkthrough order set with auditor.
4. Each walkthrough follows the auditor on-the-day playbook (`24-ai-agent-attestation-preparation-spec/references/ai-agent-auditor-on-the-day-playbook.md`).
5. Action items recorded as they arise; closure target before auditor leaves where possible.
6. End of day: portal access reduced to read-only; debrief held.

### Step 6: Gap-remediation cadence

| Severity | Definition | SLA | Owner |
|----------|------------|-----|-------|
| SEV1 | Mandatory control without evidence; control failed during the window | 7 days | AI Lead + CTO |
| SEV2 | Evidence incomplete; sampling not yet attainable | 30 days | AI Lead |
| SEV3 | Documentation polish; cross-link missing | 90 days | Compliance Manager |

### Step 7: Roles

| Role | Responsibility |
|------|-----------------|
| AI Lead | Compliance posture for agent features; evidence custodian; demoer for governance and approval walkthroughs |
| CTO | Change management sample; system architecture walkthrough |
| CISO | Kill-switch drill owner; security control walkthroughs |
| DPO | Privacy controls; DSAR; BAA/DPA addenda; sub-processor reviews; bias review co-owner |
| Compliance Manager | Audit-window orchestration; auditor portal; sign-off ledger; pack assembly |
| SRE Lead | Drill execution; observability evidence; orchestrator availability evidence |

### Step 8: Write the runbook

`AI_Agent_Compliance_Runbook.md` sections: 1) Drill Schedule, 2) Evidence-Collection Schedule, 3) Control-Test Schedule, 4) Audit-Window Operating Procedure, 5) On-the-Day Playbook Activation, 6) Gap-Remediation Cadence, 7) Roles, 8) Calendar Index, 9) Cross-Refs, 10) Sign-off.

## Standards

- AICPA AT-C Section 205
- ISO/IEC 27001 Clauses 9.1, 9.2
- ISO/IEC 17021-1
- HIPAA §164.308(a)(8)
- Google SRE (drill discipline)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-compliance-runbook-template.md`.
