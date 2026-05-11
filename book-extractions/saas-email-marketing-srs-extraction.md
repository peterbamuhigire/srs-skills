# The SaaS Email Marketing Playbook — SRS-Engine Extraction

**Source:** Étienne Garbugli, *The SaaS Email Marketing Playbook: Convert Leads, Increase Customer Retention, and Close More Recurring Revenue with Email.*

**Lens:** What lifecycle-communication, onboarding-journey, retention, and email-program documents must the engine output?

## One-line takeaway

SaaS email is run as a **lifecycle program** with documented audiences, behavioural triggers, campaigns mapped to user stages (acquisition → activation → retention → expansion → reactivation → win-back), pre-send QA checklists, and post-send measurement — every stage is a doc, not an ad-hoc send.

## Distinctive documentation surface

### 1. Lifecycle email strategy doc

A map of every stage in the customer lifecycle and the email program at each stage:

- **Pre-trial / lead-nurture** — content-driven, warm-up before sendout.
- **Trial / onboarding** — activation triggers, aha-moment milestones.
- **Active subscription** — retention, feature adoption, expansion.
- **At-risk / dunning** — churn-prevention, payment-failure recovery.
- **Churned / win-back** — reactivation.

The engine should produce a **Lifecycle Email Strategy Document** with each stage, audience, trigger, channel, template, goal, and stop date.

### 2. Onboarding journey spec

Activation rate / Aha-moment is the primary KPI; the engine should produce a **SaaS Onboarding Journey Spec** mapping product activation steps to email/in-app/push channels and the metric thresholds.

### 3. Campaign-spec checklist

A campaign has 9 documented elements: audience, channel, template, content, stop-date, goal, schedule, post-send action, A/B test. The engine should produce a **Campaign Specification Template** enforcing these elements.

### 4. Pre-send QA checklist

Segmentation, sender name & address, subject line, preview text, personalization, copy, links, privacy/unsubscribe, template across major inboxes, goal tracking. The engine should produce a **Pre-Send QA Checklist** template — a real production gate.

### 5. Metrics & measurement doc

Volume, opens, clicks, goal completion, deliveries, replies. Per-campaign reporting template.

### 6. Pricing-page email tactics & expansion playbook

Defaulting to annual, value-metric upgrade nudges, dunning-recovery, "right time, right discount" rules. Each becomes a documented playbook entry.

## Documentation patterns

- Every campaign has a documented goal (not just opens/clicks).
- Pre-send QA is a real checklist with named owners.
- Segments are documented (RFM: Recency, Frequency, Monetary).
- Glossary of activation, aha-moment, ARPU, ARPPU, behavioural emails is shared across teams.

## Implications for the SDLC-Docs-Engine

1. Add Phase 01 + 08 skill **`12-saas-lifecycle-email-strategy-doc`** (treat strategic + operational spans).
2. Add Phase 02 + 08 skill **`13-saas-onboarding-journey-spec`** with activation milestones and event spec.
3. Add cross-cutting template **`saas-lifecycle-email-strategy-doc-template.md`** and **`saas-onboarding-journey-spec-template.md`**.
4. Enhance `08-end-user-documentation/01-user-manual` with a cross-link to onboarding/email content so end-user docs and in-product comms stay consistent.

## Source mapping

- Behavioural / lifecycle / transactional categorisation → Lifecycle Email Strategy structure.
- Campaign 9-element spec → Campaign Specification Template.
- Pre-send QA section → Pre-Send QA Checklist.
- Activation / Aha-Moment glossary → Onboarding Journey Spec KPIs.
- Recency-Frequency-Monetary segmentation → segment-definition pattern.
- Dunning / payment-recovery → at-risk-stage playbook.
- Expansion / upsell email tactics → expansion playbook.
