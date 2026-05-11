---
name: "saas-lifecycle-email-strategy-doc"
description: "Generate a SaaS Lifecycle Email Strategy Document: lifecycle map (acquisition → activation → adoption → retention → expansion → at-risk → win-back), campaign catalogue per stage, pre-send QA checklist, measurement plan, RFM segmentation."
metadata:
  use_when: "Use for any SaaS that operates email as a customer-comms channel — i.e. nearly every SaaS."
  do_not_use_when: "Do not use if no email program exists."
  required_inputs: "Onboarding_Journey_Spec.md, Pricing_And_Packaging_Spec.md, Customer_Success_Playbook.md, ESP / lifecycle tool access, target ICP."
  workflow: "Map lifecycle, catalogue campaigns per stage, define segmentation, define pre-send QA, define measurement, write strategy doc."
  quality_standards: "Every campaign has the 9 required elements (audience, channel, template, content, stop-date, goal, schedule, post-send action, A/B test). Every send has a pre-send QA."
  anti_patterns: "Do not send without a defined goal. Do not skip A/B test on high-volume sends. Do not send > 3 emails per week to active subs."
  outputs: "Lifecycle_Email_Strategy_Doc.md."
  references: "references/saas-lifecycle-email-strategy-doc-template.md"
---

# SaaS Lifecycle Email Strategy Doc Skill

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
