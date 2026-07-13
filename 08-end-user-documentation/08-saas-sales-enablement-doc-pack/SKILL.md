---
name: 08-saas-sales-enablement-doc-pack
description: Use when producing product-specific ICP, discovery, demo, qualification, battlecard, and closing material for a sales-assisted SaaS. Use customer-success-playbook for post-sale operations and FAQ for customer self-service answers.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Sales Enablement Doc Pack Skill

<!-- dual-compat-start -->

## Use When

- Use when producing product-specific ICP, discovery, demo, qualification, battlecard, and closing material for a sales-assisted SaaS. Use customer-success-playbook for post-sale operations and FAQ for customer self-service answers.

## Do Not Use When

- Do not use for pure-self-serve products with no sales rep.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: PRD.md, Pricing_And_Packaging_Spec.md, competitive scan, target ICP, GTM Segment Profile (if available). | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A claim, segment, trigger, metric, or intervention lacks product evidence | Qualify it and request the missing source | Generic playbooks detached from product reality |
| Consent, suppression, fairness, or customer-harm guardrail fails | Stop the affected play or campaign | Dark patterns or non-compliant outreach |

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
| SaaS Sales Enablement Doc Pack | Customer, support, success, sales, or implementation owner | Every doc shall be product-specific (no generic templates pasted). Every discovery question shall be a tested formulation. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| SaaS Sales Enablement Doc Pack evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every doc shall be product-specific (no generic templates pasted). Every discovery question shall be a tested formulation.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing SaaS Sales Enablement Doc Pack from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a claim, segment, trigger, metric, or intervention lacks product evidence, qualify it and request the missing source. Record the evidence and result in the validation record; this avoids generic playbooks detached from product reality.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

Sourced from Winning by Design's *SaaS Sales Method Fundamentals* and *for Account Executives*. Produces the AE-facing doc pack that operationalises discovery, demo, and closing.

## Core Instructions

### Step 1: ICP & target persona

For each segment in scope, produce: firmographics, technographics, trigger events, buying-committee map, common objections, vocabulary.

### Step 2: Sales-methodology selection

Per product line:

| Methodology | When | ACV band | Sales cycle | Deals / mo / AE |
|-------------|------|----------|-------------|-----------------|
| Transactional | high-volume inbound | < $1k | < 30d | 10-20 |
| Solution | inbound/outbound mid | $5k | ~30d | 5-10 |
| Consultative | platform sale | $20-100k | 6-18 mo | 1-3 |
| Provocative | innovation, CEO-level | $250k+ | 6-9 mo | 1-2 |

Pick one; state the team-shape implication.

### Step 3: 8-step discovery meeting script

Per Winning by Design AE method:

1. Prepare for the meeting.
2. Open the conversation.
3. ACE the start (Acknowledge, Connect, Empathise).
4. Set the agenda.
5. Diagnose situation + pain (S + P questions).
6. Summarize the conversation.
7. Provide a 3rd-party reference.
8. Identify value via impact (I) questions.

For each step write: goal, recommended phrases, common mistakes, the standard SPI questions tailored to the ICP.

### Step 4: Demo script (two-part)

- **Part 1 — Demonstrate the product.** Show the 3-5 narrative beats that show the customer's pain being solved. Use the customer's tone words from discovery.
- **Part 2 — Integrate into the call.** Tie each demo beat back to a stated customer pain. End on impact and next step.

State the demo length budget (30 min for solution sale; 60 for consultative).

### Step 5: Competitive battlecards

One per main competitor. Sections: positioning, differentiation, where they win, where we win, traps to avoid, objection responses, proof points (named customers).

### Step 6: Closing playbook

- Trade / Commit / Go Dark signals and responses.
- MEDDIC qualification (Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion).
- Mutual action plan template.
- Procurement / legal / security review playbook (DPA, security questionnaire, MSA negotiation).

### Step 7: Value quantification worksheet

Cost / Experience / Revenue impact (Reduce / Improve / Increase). Tied to discovery findings.

### Step 8: Write the pack

`Sales_Enablement_Doc_Pack.md` indexes:

- `ICP.md`
- `Sales_Methodology.md`
- `Discovery_Meeting_Script.md`
- `Demo_Script.md`
- `Battlecards/<competitor>.md`
- `Closing_Playbook.md`
- `Value_Quantification_Worksheet.md`
- `Pricing_Cheatsheet.md` (derived from Pricing & Packaging Spec)

## Standards

- IEEE 29148 (stakeholder requirements).
- Winning by Design *SaaS Sales Method* fundamentals + AE volumes.

## Resources

- `logic.prompt`, `README.md`, `references/saas-sales-enablement-doc-pack-template.md`, `references/saas-value-quantification-worksheet.md`.
