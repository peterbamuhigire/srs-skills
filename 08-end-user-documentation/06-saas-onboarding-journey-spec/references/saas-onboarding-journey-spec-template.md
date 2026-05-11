# SaaS Onboarding Journey Spec — Template

## 1. Aha-moment

- Aha-moment event: `<event name>`
- Definition: "<one sentence>"
- Activation rate definition: % of signups reaching this event within `<N>` days.
- Current baseline: <%>
- Target: ≥ 30%

## 2. Activation milestones

| # | Milestone | Event | Target window | Rationale |
|---|-----------|-------|---------------|-----------|
| 1 | Sign-up complete | `user.signed_up` | T0 | |
| 2 | Profile / org set | `tenant.profile_completed` | T+5m | |
| 3 | First action | `<product-specific>` | T+1d | |
| 4 | Aha moment | `<aha event>` | T+7d | |
| 5 | Team / integration | `team.invited` or `integration.connected` | T+14d | |
| 6 | Habit formed | `user.returned_3_times_in_7d` | T+21d | |

## 3. Channel orchestration

| Stage | In-app | Email | Push | SMS | CSM (Gold/Ent) |
|-------|--------|-------|------|-----|----------------|
| Sign-up | welcome modal | welcome email | – | – | – |
| 24h no profile | tooltip | reminder | – | – | – |
| Day 3 no first action | guided tour | activation tip | – | – | – |
| Day 7 no aha | template / offer | aha-story email | – | – | call (Gold+) |
| Day 14 no team | invite prompt | team-onboarding playbook | – | – | – |

Cap: 3 touches per day per user.

## 4. Drop-off interventions

| Drop-off step | Intervention | Owner |
|---------------|--------------|-------|
| | | |

## 5. KPI thresholds

| KPI | Target | Owner |
|-----|--------|-------|
| Sign-up → activation | ≥ 30% | Product + Growth |
| Time-to-aha P50 | ≤ 5 d | Product |
| Day-30 retention (activated cohort) | ≥ 60% | Product + CS |
| Email open (onboarding) | ≥ 40% | Lifecycle |
| In-app nudge CTR | ≥ 25% | Growth |

## 6. Segmented paths

| Segment | Tier | Onboarding shape |
|---------|------|------------------|
| Freelance / Indie | Free/Indie | fully self-serve, in-app + email |
| SMB | Pro/Studio | product-led + CSM cameos |
| Mid-market | Studio | CSM-led with product-led extension |
| Enterprise | Enterprise | TAM + CSM, kickoff workshop, multi-week plan |

## 7. Event catalogue (emit + tenant context)

| Event | Schema | Required fields | Tenant context |
|-------|--------|-----------------|----------------|
| user.signed_up | timestamp, user_id, source | yes | tenant_id |
| tenant.profile_completed | timestamp, tenant_id | yes | tenant_id |
| <product-specific> | | | tenant_id, tier |

## 8. Review cadence

- Weekly: funnel review with Product + Growth.
- Monthly: iteration cycle (one experiment per stage).
- Quarterly: spec revision.
