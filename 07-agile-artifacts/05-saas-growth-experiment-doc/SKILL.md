---
name: "saas-growth-experiment-doc"
description: "Generate a SaaS Growth Experiment Document: hypothesis, target metric, segment, MDE, sample size, duration, stop rule, instrumentation, decision rule, post-mortem template."
metadata:
  use_when: "Use for any A/B test, multivariate test, in-app experiment, lifecycle-email experiment, or pricing experiment in a SaaS."
  do_not_use_when: "Do not use for prod hotfixes."
  required_inputs: "Onboarding_Journey_Spec.md or Lifecycle_Email_Strategy_Doc.md or Pricing_And_Packaging_Spec.md (whichever the experiment touches), product analytics, A/B platform."
  workflow: "Frame hypothesis, choose metric, choose segment, compute sample size, set guardrails, set stop rule, set decision rule, document instrumentation."
  quality_standards: "Every experiment has a single primary metric, a pre-registered stop rule, and at least one guardrail metric."
  anti_patterns: "Do not run an experiment without a stop rule. Do not pick a primary metric after seeing the data. Do not run on a segment too small to detect MDE."
  outputs: "Growth_Experiment_Doc.md."
  references: "references/saas-growth-experiment-template.md"
---

# SaaS Growth Experiment Doc Skill

## Overview

Codifies the experiment design that good growth teams operate on. Anchored in standard A/B-test rigor + Garbugli's lifecycle experiment chapters.

## Core Instructions

### Step 1: Hypothesis

`If <change>, then <metric> will <direction> by <magnitude>, because <mechanism>.`

State explicitly. Frame as falsifiable.

### Step 2: Primary metric + guardrails

- One primary metric (e.g. activation rate, week-1 retention, MRR per signup).
- 1-3 guardrail metrics that MUST NOT regress (e.g. churn, support load, page latency).
- One leading-indicator metric.

### Step 3: Segment & sample size

- Segment: who is exposed (e.g. signups in last 7 d in EU on Pro tier).
- Baseline conversion: <%>.
- Minimum Detectable Effect (MDE): <%>.
- Statistical power: 80%.
- Significance: 95%.
- Required sample size per arm: computed.
- Estimated duration: <weeks>.

### Step 4: Stop rule

- Maximum duration: <weeks>.
- Early-stop on guardrail breach: yes if guardrail regresses by > <threshold>.
- Early-stop on success: only at full sample (Bayesian / sequential rules pre-registered if used).
- Pre-registered analysis date.

### Step 5: Decision rule

- Ship if primary metric +X% with p<0.05 AND no guardrail regresses by > Y%.
- Reject if primary -X% OR any guardrail regresses by > Y%.
- Iterate if inconclusive.

### Step 6: Instrumentation

- Variant assignment: deterministic by user_id hash.
- Tenant-context: variant exposed at user level (consider tenant-scoping for multi-user SaaS).
- Events emitted: variant_assignment, primary_metric, guardrails.
- A/B platform: <name>.

### Step 7: Risks & ethics

- Reversibility: can we roll back instantly?
- Customer-impact: does any variant degrade experience for paying users?
- Pricing tests: extra care with paying tenants — usually segment to free or new-trial.
- Notification: do users need to know?

### Step 8: Post-mortem

After experiment:

- Result summary.
- Did we learn what we hypothesised?
- Action taken: ship / reject / iterate.
- Surprising findings.
- Process notes.

### Step 9: Write the doc

`Growth_Experiment_Doc.md` with sections: 1) Hypothesis, 2) Metrics (primary, guardrails, leading), 3) Segment & Sample Size, 4) Stop Rule, 5) Decision Rule, 6) Instrumentation, 7) Risks & Ethics, 8) Timeline, 9) Post-mortem (filled after).

## Standards

- IEEE 29148 (requirements engineering).
- Industry A/B-test rigour (Kohavi, Tang, Xu, *Trustworthy Online Controlled Experiments*).

## Resources

- `logic.prompt`, `README.md`, `references/saas-growth-experiment-template.md`.
