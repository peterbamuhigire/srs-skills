# SaaS Customer Success Playbook — Template

## 1. Customer Health Score

| Signal | Weight | Source | Formula |
|--------|--------|--------|---------|
| Usage depth (% of features adopted) | 25% | telemetry | |
| Usage breadth (unique features in 30d) | 15% | telemetry | |
| Engagement frequency (active days / 30) | 15% | telemetry | |
| Support sentiment (avg CSAT 90d) | 10% | support | |
| NPS (latest) | 10% | survey | |
| Contract age (months since signing) | 10% | CRM | |
| Expansion signal (seat or usage growth) | 15% | billing | |

Score: 0-100; refresh weekly.

Bands and actions:

| Band | Score | Action |
|------|-------|--------|
| Green | 75-100 | expansion play eligible |
| Yellow | 50-74 | weekly check-in, identify blocker |
| Red | < 50 | escalation, save plan within 14 d |

## 2. Segmentation

Tier × Stage matrix. Each cell named with a CSM coverage model:

| | Onboarding | Adoption | Renewal | At-risk |
|---|------------|----------|---------|---------|
| Bronze | digital-only | digital-only | auto-renewal | low-touch |
| Silver | pooled CSM | pooled CSM | scheduled call | targeted save |
| Gold | named CSM | named CSM | QBR | exec touch |
| Enterprise | named CSM + TAM | named CSM + TAM | exec QBR + steering | exec-sponsor save |

## 3. Per-stage plays (template applied per cell)

```
### Play: <name>
- Trigger:
- Owner:
- Action(s):
- Channel(s):
- Frequency:
- Success measurement:
- Escalation rule:
```

### Required plays

| Play | Trigger | Owner | Channel |
|------|---------|-------|---------|
| Onboarding kickoff | D0 after activation | CSM | in-app + email + call (Gold+) |
| First-value milestone | D7 if milestone not reached | CSM | email + in-app |
| 30-day health review | D30 | CSM | call |
| At-risk intervention | health → Red | CS Lead | call within 48h |
| Renewal forecast T-90 | T-90 to renewal | CSM + RevOps | internal review |
| Renewal forecast T-60 | T-60 | CSM + sales | customer call |
| Renewal forecast T-30 | T-30 | CSM + sales | exec confirm |
| Renewal-at-risk save | renewal forecast Red | CS Lead + exec sponsor | save plan |
| Expansion / upsell | Green + signal | CSM + AE | call |
| Dunning recovery | payment failure (D+0 to D+14) | RevOps + CSM | email + call |
| Churned-recoverable | post-churn 30-90d | CSM + Marketing | targeted re-engagement |

## 4. QBR template

```
# Quarterly Business Review — <Customer>

1. Business objectives (customer's, not ours)
2. Usage & adoption summary (chart: depth, breadth, frequency)
3. Value delivered this quarter (named outcomes)
4. Support summary (tickets, resolution, sentiment)
5. Expansion opportunities (named)
6. Risks identified (named)
7. Roadmap relevant to customer (asks, commitments)
8. Action items (owner, date)
```

## 5. Dunning recovery

Aligns with Billing & Metering Spec Section 6. CSM tasks:

| Day | Action | Channel |
|-----|--------|---------|
| D+0 | system reminder | email |
| D+3 | personal email from CSM | email |
| D+7 | phone call attempt + in-app banner | call + in-app |
| D+10 | escalation to CS Lead | exec email |
| D+14 | suspension imminent notice | call + email |
| D+30 | save plan or offboarding plan | exec |

## 6. Escalation matrix

| Trigger | Escalates to | Within |
|---------|--------------|--------|
| Health → Red, Gold/Enterprise | CS Lead | 24 h |
| Renewal-at-risk, ≥ $50k ACV | CRO | 5 BD |
| Exec contact change | CSM owner + AE | 48 h |
| Integration partner change | TAM | 5 BD |
| Security/compliance complaint | CISO + CS Lead | immediate |

## 7. Tooling

- CRM (CS module or Gainsight/ChurnZero).
- BI dashboards (health score, retention cohorts).
- Source-of-truth: CRM for relationship state; billing for revenue truth; telemetry for usage.

## 8. Cadence

- Weekly: CS team health-score review.
- Monthly: business review (retention, expansion, churn).
- Quarterly: playbook revision.
