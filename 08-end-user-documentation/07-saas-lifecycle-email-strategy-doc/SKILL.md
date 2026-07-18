---
name: 07-saas-lifecycle-email-strategy-doc
description: Use when defining consent-aware SaaS acquisition, activation, adoption, retention, expansion, risk, and win-back email campaigns with triggers, suppression, QA, and measurement. Use onboarding-journey-spec for in-product activation.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Lifecycle Email Strategy Doc Skill

<!-- dual-compat-start -->

## Use When

- Use when defining consent-aware SaaS acquisition, activation, adoption, retention, expansion, risk, and win-back email campaigns with triggers, suppression, QA, and measurement. Use onboarding-journey-spec for in-product activation.

## Do Not Use When

- Do not use if no email program exists.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: Onboarding_Journey_Spec.md, Pricing_And_Packaging_Spec.md, Customer_Success_Playbook.md, ESP / lifecycle tool access, target ICP. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| SaaS Lifecycle Email Strategy Doc | Customer, support, success, sales, or implementation owner | Every campaign has the 9 required elements (audience, channel, template, content, stop-date, goal, schedule, post-send action, A/B test). Every send has a pre-send QA. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| SaaS Lifecycle Email Strategy Doc evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every campaign has the 9 required elements (audience, channel, template, content, stop-date, goal, schedule, post-send action, A/B test). Every send has a pre-send QA.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing SaaS Lifecycle Email Strategy Doc from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

Sourced from Garbugli's *SaaS Email Marketing Playbook*. Produces the strategy doc that turns email from ad-hoc sends into an instrumented lifecycle program.

## Core Instructions

### Step 1: Lifecycle map

Stages: Pre-trial / Acquisition → Trial / Onboarding → Activation → Adoption / Retention → Expansion / Upsell → At-risk / Dunning → Churned / Win-back. Document audience definition per stage.

### Step 2: RFM segmentation

Segment subscribers by Recency, Frequency, Monetary. Define how segments map to which campaign categories.

### Step 3: Campaign catalogue

For each stage produce campaigns. Each campaign has the 9 elements:

1. Audience
2. Channel (email / in-app / push / SMS)
3. Template (mobile-friendly + design tested across major inboxes)
4. Content (subject, preview, body, links, CTA)
5. Stop-date (no infinite campaigns)
6. Goal (one CTA per email; quantified)
7. Schedule (trigger or cron)
8. Post-send action (move segment, tag, exit)
9. A/B test (when volume permits)

### Step 4: Pre-send QA checklist

For every send, before going live:

- Segmentation: who is it sent to? Random sample reviewed.
- Sender name / address: passes spam filters.
- Subject line: scored with subject-line tool, no weird characters.
- Preview text: expected words appear in major inbox previews.
- Personalization: variables populate.
- Copy: offer appropriate; error-free; discount codes work.
- Links: functional; tracking parameters present.
- Privacy: unsubscribe link; full address; consent honored.
- Template: tested across Gmail, Outlook, Apple Mail, dark-mode, mobile.
- Goal: clear way to track performance.

### Step 5: Measurement

Per campaign metrics: send volume, opens, clicks, goal-completion, replies, delivery rate. Per program metrics: cohort activation lift, retention lift, expansion lift, dunning recovery rate.

### Step 6: Transactional vs lifecycle vs behavioral

State which sends are transactional (legal-required, must deliver, separate domain or sub-domain), lifecycle (stage-based), behavioral (trigger-based on user action). State throttling rules and frequency caps.

### Step 7: Compliance

GDPR / CCPA / CAN-SPAM compliance: consent capture, lawful basis, unsubscribe within one click, address footer, separate sub-processor.

### Step 8: Write the doc

`Lifecycle_Email_Strategy_Doc.md` with sections: 1) Lifecycle Map, 2) RFM Segmentation, 3) Campaign Catalogue per Stage, 4) Pre-send QA Checklist, 5) Measurement, 6) Transactional vs Lifecycle vs Behavioral, 7) Frequency Caps, 8) Compliance, 9) Tooling & Source-of-truth, 10) Review cadence.

## Standards

- Garbugli (2017) *SaaS Email Marketing Playbook*.
- CAN-SPAM Act, GDPR Art.6/7, CCPA.

## Resources

- `logic.prompt`, `README.md`, `references/saas-lifecycle-email-strategy-doc-template.md`.
