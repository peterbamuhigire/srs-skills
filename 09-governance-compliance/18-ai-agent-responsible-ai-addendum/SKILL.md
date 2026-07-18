---
name: 18-ai-agent-responsible-ai-addendum
description: Use when extending a responsible-AI declaration with agent autonomy, action approval, supervision, kill switch, memory, auditability, and red-team controls. Use user-disclosure-pack for customer language and compliance-policy-pack for signed policies.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Agent Responsible-AI Addendum Skill

<!-- dual-compat-start -->

## Use When

- Use when extending a responsible-AI declaration with agent autonomy, action approval, supervision, kill switch, memory, auditability, and red-team controls. Use user-disclosure-pack for customer language and compliance-policy-pack for signed policies.

## Do Not Use When

- Do not use for AI features that do not call tools or act on the user's behalf. Cover those under the parent Responsible AI Declaration.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_User_Disclosure_Pack.md, Responsible_AI_Declaration.md, AI_Act_Regulatory_Compliance_Doc.md. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| AI Agent Responsible-AI Addendum | Accountable reviewer, control owner, auditor, or release authority | Every irreversible-action class shall have a named human-final-decision principle. Every agent feature shall have a contestability path. Audit-log retention shall meet or exceed regulatory minima. Every paragraph in the public declaration that mentions agents shall trace back to an internal evidence row in the addendum. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent Responsible-AI Addendum evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every irreversible-action class shall have a named human-final-decision principle. Every agent feature shall have a contestability path. Audit-log retention shall meet or exceed regulatory minima. Every paragraph in the public declaration that mentions agents shall trace back to an internal evidence row in the addendum.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent Responsible-AI Addendum from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

## Core Instructions

### Step 1: Action accountability per feature

For each agent feature, declare:

- The accountable role for an agent action (typically the workspace admin who enabled the feature).
- The responsible party for the agent's design and operation (us).
- The named human approver role for any irreversible-action call.
- The audit retention path that supports each accountability claim.

### Step 2: Audit-log retention by event class

| Event class | Hot | Cold | Justification |
|--------------|-----|------|----------------|
| Tool call (read) | 90 d | 13 months | operational debugging |
| Tool call (write-internal) | 13 months | 3 years | tenant audit + dispute resolution |
| Tool call (write-external, billing, irreversible) | 13 months | 7 years | regulatory + dispute |
| Plan + approval events | 13 months | 7 years | regulatory + dispute |
| Kill-switch events | 13 months | 7 years | safety audit |
| Human-approval events | 13 months | 7 years | regulatory |

Retention shall meet or exceed regulatory minima per region (EU, UK, US sectoral, African DPAs).

### Step 3: Contestability mechanism

State the user-facing contestation path; the internal review SLA; the evidence assembly procedure; the escalation path; the postmortem trigger for confirmed wrong actions.

### Step 4: Human-final-decision principle

For every tool class with `reversibility_class=irreversible`, state in plain language:

- The named human role that takes the final decision.
- The moment in the flow the decision is taken.
- The information shown at that moment.
- The bypass policy (no bypass; documented exceptions only with ADR and waiver).

This is the operationalisation of EU AI Act Art. 14 for the product.

### Step 5: Bias and harm reviews

For every agent feature whose actions affect protected-class outcomes (hiring, lending, housing, healthcare, education), declare:

- The bias review cadence.
- The reviewers (named individuals; include external reviewers where regulation requires).
- The metrics tracked.
- The remediation path.

### Step 6: Cross-link the public declaration

The public Responsible AI Declaration carries plain-language paragraphs. The internal addendum is the evidence trail. Every public paragraph that mentions agents shall trace to an internal evidence row.

### Step 7: Write both documents

- `AI_Agent_Responsible_AI_Addendum.md` (internal) — the evidence trail.
- `Responsible_AI_Declaration_Agent_Section.md` (public) — the plain-language paragraphs to slot into the parent declaration.

Sections (internal): 1) Action Accountability per Feature, 2) Audit-Log Retention, 3) Contestability Mechanism, 4) Human-Final-Decision Principle, 5) Bias and Harm Reviews, 6) Public-Declaration Cross-link Table, 7) Review Cadence.

## Standards

- EU AI Act Art. 13 (transparency), Art. 14 (human oversight)
- NIST AI RMF GOVERN-3
- ISO/IEC 42001 Clause 7.4 (communication)
- Google AI Principles
- Anthropic AUP / RSP

## Compliance evidence cross-link

The addendum is a primary evidence artefact for the following control rows:

- SOC 2 CC1.1, CC2.3 — public Responsible-AI Declaration and tenant-admin disclosure.
- SOC 2 CC5.1, PI1.4 — irreversibility gates and approval-event evidence.
- ISO/IEC 27001:2022 A.5.1, A.5.34 — policy authority and PII protection.
- HIPAA §164.308(a)(4) and §164.312(d) — approval-event evidence (where PHI in scope).
- EU AI Act Art. 13 (transparency) and Art. 14 (human oversight).
- NIST AI RMF GOVERN-3.

Each Addendum section maps to one or more rows in `09-governance-compliance/25-ai-agent-evidence-pack-spec/references/ai-agent-evidence-frequency-table.md` (rows 25, 26, 39, 40). The Addendum is signed annually as part of the Compliance Policy Pack (`09-governance-compliance/23-ai-agent-compliance-policy-pack`).

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-responsible-ai-addendum-template.md`.
