---
name: 14-ai-responsible-ai-declaration
description: Use when documenting an AI feature's intended use, limits, human oversight, evaluation, data, safety, fairness, transparency, and accountability. Use ai-data-flow-and-dpia for privacy risk and responsible-ai-addendum for agent-specific controls.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Responsible AI Declaration Skill

<!-- dual-compat-start -->

## Use When

- Use when documenting an AI feature's intended use, limits, human oversight, evaluation, data, safety, fairness, transparency, and accountability. Use ai-data-flow-and-dpia for privacy risk and responsible-ai-addendum for agent-specific controls.

## Do Not Use When

- Do not use for internal-only AI tools or research demonstrations.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Feature_PRD_Spec.md, AI_Model_Card.md (per feature), AI_Architecture_Spec.md, AI_Act_Regulatory_Compliance_Doc.md, DPA, sub-processor list, Trust Center doc pack. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| Responsible AI Declaration | Accountable reviewer, control owner, auditor, or release authority | Every AI feature shall have a does/does-not statement, an HITL statement, a data-use statement, a regulatory tier, and a model-provider declaration. Statements shall be reviewable by a layperson. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Responsible AI Declaration evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every AI feature shall have a does/does-not statement, an HITL statement, a data-use statement, a regulatory tier, and a model-provider declaration. Statements shall be reviewable by a layperson.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Responsible AI Declaration from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

The buyer-, regulator-, and user-facing statement of how the product uses AI. Anchored in Google AI Principles, Anthropic AUP/RSP, and the disclosure obligations of EU AI Act Art. 13.

## Core Instructions

### Step 1: Public summary

One paragraph: where AI appears in the product, what it does at a high level, what humans control.

### Step 2: Per-feature does / does not

For each AI feature publish:

- What the AI does (in plain language).
- What the AI does not do (limits, prohibited uses).
- What humans control (approval, contest, override).

### Step 3: Human oversight and contestability

State how a user can:

- Tell that AI produced an output.
- Regenerate, edit, or reject.
- Flag perceived inaccuracy.
- Escalate to a human reviewer.
- Request human-only handling where available.

### Step 4: Data use and training

Plain-language summary of:

- What customer data is sent to model providers.
- Whether that data is used to train provider general models (no).
- Whether it is used to train our fine-tunes (state policy).
- Retention of prompts and responses.
- Tenant isolation summary.

### Step 5: Model providers and sub-processors

List the model providers in use, the data passed to each, the contract terms (no-training, residency), and cross-link the sub-processor list.

### Step 6: Per-feature regulatory tier

For each feature declare the EU AI Act tier (prohibited / high-risk / limited-risk / minimal-risk), the US sectoral applicability, and the African DPA applicability where in scope.

### Step 7: Incident disclosure approach

State how AI-quality incidents (mass hallucinations, bias incidents, jailbreak disclosures, cross-tenant leaks) are disclosed. Tie to the SaaS incident-response runbook.

### Step 8: Review cadence

Quarterly review by the AI Lead + DPO + Security + Legal. Publish version history.

### Step 9: Write the two documents

- `Responsible_AI_Declaration.md` (public) -- plain language, no internal jargon.
- `Responsible_AI_Declaration_Internal.md` (internal) -- the evidence trail that backs every public statement.

## Standards

- EU AI Act Art. 13 (transparency)
- Google AI Principles
- Anthropic AUP / RSP
- ISO/IEC 42001 Clause 7.4 (communication)
- NIST AI RMF GOVERN
