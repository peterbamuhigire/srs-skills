---
name: "saas-onboarding-journey-spec"
description: "Generate a SaaS Onboarding Journey Specification: define the aha-moment, activation milestones, channel-orchestrated nudges (in-app / email / push), KPI thresholds, drop-off interventions, segmented onboarding paths per ICP and tier."
metadata:
  use_when: "Use whenever a SaaS has a self-serve or sales-led onboarding flow."
  do_not_use_when: "Do not use when there is no signup flow."
  required_inputs: "PRD.md, Pricing_And_Packaging_Spec.md, user-research notes, product-analytics access (events catalogue)."
  workflow: "Define aha-moment, define activation milestones, define channel orchestration, define drop-off interventions, set KPI thresholds, write the spec."
  quality_standards: "Aha-moment is a single named event. Every milestone has a target completion window and a measurement source. Every nudge has a channel and a trigger."
  anti_patterns: "Do not list everything as a milestone. Do not omit drop-off interventions. Do not stack >3 nudges per day."
  outputs: "Onboarding_Journey_Spec.md."
  references: "references/saas-onboarding-journey-spec-template.md"
---

# SaaS Onboarding Journey Spec Skill

## Overview

Sourced from Garbugli (lifecycle email) and Walling (activation as escape-velocity threshold). Produces the explicit onboarding-journey doc many SaaS lack.

## Core Instructions

### Step 1: Define the aha-moment

A single named product event where the user first perceives value. State it precisely (e.g. "first invoice sent", "first deal closed in pipeline", "first dashboard published"). Activation rate = % of signups reaching this event within N days.

### Step 2: Define activation milestones

| # | Milestone | Event name | Target window | Why it matters |
|---|-----------|------------|---------------|----------------|
| 1 | Sign-up complete | `user.signed_up` | T0 | enter funnel |
| 2 | Profile complete | `user.profile_completed` | T+5 min | reduces friction |
| 3 | First action | `<product-specific>` | T+1 day | hands-on engagement |
| 4 | Aha moment | `<aha event>` | T+7 day | core activation |
| 5 | Team invited / integration | `team.invited` or `integration.connected` | T+14 day | stickiness |
| 6 | Habit formed | `user.returned_3_times` in 7 d | T+21 day | retention indicator |

### Step 3: Channel orchestration

For each milestone, define the nudge program if the milestone hasn't fired:

| Stage | In-app | Email | Push | SMS | CSM (Gold/Ent) |
|-------|--------|-------|------|-----|----------------|
| Sign-up | welcome modal | welcome email | – | – | – |
| 24h no profile | tooltip | reminder | – | – | – |
| Day 3 no first action | guided tour | activation tip | – | – | – |
| Day 7 no aha | targeted offer / on-screen template | aha-moment story | – | – | call (Gold) |
| Day 14 no team | invite prompt | team-onboarding playbook | – | – | – |

Max 3 touches per day per user.

### Step 4: Drop-off interventions

For each commonly-dropped step, design an intervention (in-product flow, CSM call, integration concierge, refund-trial-extend offer).

### Step 5: KPI thresholds

| Metric | Target | Owner |
|--------|--------|-------|
| Sign-up → activation | ≥ 30% | Product + Growth |
| Time-to-aha P50 | ≤ 5 days | Product |
| Day-30 retention of activated cohort | ≥ 60% | Product + CS |
| Email open rate (onboarding) | ≥ 40% | Lifecycle |
| In-app nudge click-through | ≥ 25% | Growth |

### Step 6: Segmented paths

Per ICP and per tier. Enterprise has CSM-led onboarding overlay; SMB is product-led; freelance is fully self-serve. Document the differences.

### Step 7: Write the spec

`Onboarding_Journey_Spec.md` with sections: 1) Aha-Moment, 2) Activation Milestones, 3) Channel Orchestration, 4) Drop-off Interventions, 5) KPI Thresholds, 6) Segmented Paths, 7) Event Catalogue (events emitted at each milestone), 8) Review cadence.

## Standards

- ISO 26514 (user documentation).
- IEEE 29148 (stakeholder requirements).
- Garbugli (SaaS Email Marketing Playbook).

## Resources

- `logic.prompt`, `README.md`, `references/saas-onboarding-journey-spec-template.md`.
