---
name: 09-ai-agent-user-disclosure-pack
description: Use when preparing user-facing disclosures for an AI agent's capabilities, limits, data use, autonomy, approvals, escalation, and incident contact. Use responsible-ai-addendum for internal governance and DPA language for contractual processing terms.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Agent User Disclosure Pack Skill

<!-- dual-compat-start -->

## Use When

- Use when preparing user-facing disclosures for an AI agent's capabilities, limits, data use, autonomy, approvals, escalation, and incident contact. Use responsible-ai-addendum for internal governance and DPA language for contractual processing terms.

## Do Not Use When

- Do not use for internal-only agents with no end-user exposure.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Rollout_Runbook.md, Responsible_AI_Declaration.md, Trust Center doc pack. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| An agent can act or process data in a way the disclosure omits | Block publication and correct the disclosure | Misleading consent and unsafe use |
| A capability varies by tier, role, or autonomy level | State the boundary explicitly | Users overestimating agent authority |

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
| AI Agent User Disclosure Pack | Customer, support, success, sales, or implementation owner | Every agent feature shall have a does / does-not / authority / override / undo / contestation block in plain language. Copy shall be reviewable by a layperson and shall not use marketing language. Regional disclosures shall meet EU AI Act Art. 13 and local DPA requirements. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent User Disclosure Pack evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every agent feature shall have a does / does-not / authority / override / undo / contestation block in plain language. Copy shall be reviewable by a layperson and shall not use marketing language. Regional disclosures shall meet EU AI Act Art. 13 and local DPA requirements.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent User Disclosure Pack from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if an agent can act or process data in a way the disclosure omits, block publication and correct the disclosure. Record the evidence and result in the validation record; this avoids misleading consent and unsafe use.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Core Instructions

### Step 1: Per-feature does and does not

For each agent feature, write a paragraph with two bullets:

- What the agent does. Plain language. One sentence.
- What the agent does not do. Plain language. One sentence.

### Step 2: Authority statement

Per feature, state in plain language:

- Whose authority the agent acts under (the workspace, the user).
- Which actions the agent is allowed to take.
- Which actions it is not allowed to take.
- Any per-call human approval required.

### Step 3: Override and undo copy

For each agent feature:

- How to disable the feature (admin path).
- How to undo a specific action (per-action path).
- How to cancel a run in progress.
- What is not reversible (the explicit, plain-language list).

### Step 4: 'Agent worked on your behalf' notification

Design pattern for the notification that surfaces when an agent acted:

- When it shows (after every agent action with a user-visible side-effect).
- Where it shows (inbox, banner, dedicated audit drawer).
- What it shows (action verb + target + timestamp + agent name + revert button if applicable + 'how this worked' link).
- How the user dismisses it (acknowledge; do not auto-dismiss).

### Step 5: Contestation path

Per feature:

- How a user reports a wrong action (form, email, in-product flag).
- Expected response time.
- What evidence is gathered (audit log excerpt for that user / run).
- Escalation path to a human reviewer.

### Step 6: Regional disclosures

- EEA: prominent EU AI Act Art. 13 transparency notice; opt-in default for L2+; reference to the responsible-AI declaration.
- UK ICO: AI accountability statement reference.
- US: state-specific disclosures where applicable (CO AI Act 2026; NYC bias audits for employment-related agents).
- Africa: per local DPA (Uganda DPPA, Ghana DPA, Nigeria NDPR).

### Step 7: Write the pack

`AI_Agent_User_Disclosure_Pack.md` sections: 1) Per-feature Disclosure Blocks, 2) Notification Design, 3) Contestation Path, 4) Regional Disclosures, 5) Copy String Tables (per locale), 6) Review Cadence.

## Standards

- EU AI Act Art. 13 (transparency)
- ICO AI auditing guidance
- WCAG 2.2 AA (copy and contrast)
- Plain Language Act / GOV.UK content style
- Anthropic / OpenAI agent-disclosure patterns

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-user-disclosure-pack-template.md`.
