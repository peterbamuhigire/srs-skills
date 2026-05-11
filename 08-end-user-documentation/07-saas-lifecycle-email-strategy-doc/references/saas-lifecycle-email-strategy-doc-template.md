# SaaS Lifecycle Email Strategy Doc — Template

## 1. Lifecycle map

| Stage | Audience | Goal | Key metric |
|-------|----------|------|-----------|
| Pre-trial / Acquisition | leads not yet signed up | get signup | signup rate |
| Trial / Onboarding | signed up, not yet activated | reach aha-moment | activation rate |
| Activation | activated, < 30 days | habit formation | day-30 retention |
| Adoption / Retention | activated, 30-365d | expand depth & breadth | feature adoption |
| Expansion / Upsell | green health + signal | seat / tier upgrade | expansion ARR |
| At-risk / Dunning | health red OR payment failed | recover | save rate |
| Churned / Win-back | post-churn 30-180d | reactivate | reactivation rate |

## 2. RFM segmentation

| Segment | Recency | Frequency | Monetary | Eligible campaigns |
|---------|---------|-----------|----------|--------------------|
| Power | < 7d | > 5/wk | high | expansion |
| Active | < 30d | > 1/wk | mid | adoption |
| Drifting | 30-60d | < 1/wk | any | re-engage |
| Cold | > 60d | 0 | any | win-back |
| New | < 7d | – | – | onboarding |

## 3. Campaign catalogue (one row per campaign)

| Stage | Campaign | Audience | Channel | Trigger / schedule | Goal | Stop-date | Post-send action | A/B test |
|-------|----------|----------|---------|--------------------|------|-----------|------------------|----------|
| Onboarding | Welcome | signed up | email | T+0 | open + click | one-shot | move to D1 segment | subject |
| Onboarding | D1 no profile | not profile-complete D1 | email + in-app | T+24h | profile completion | T+7d | exit on completion | CTA |
| Onboarding | Aha story | not aha by D5 | email | T+5d | aha event | T+14d | exit on aha | offer vs story |
| Adoption | Feature spotlight | active 30-90d | email | weekly | feature adoption | rolling | tag | subject |
| Expansion | Seat upsell | seat-cap 80% | email + in-app | event | seat add | T+14d | exit on conversion | offer |
| Dunning | Payment failure | failed today | email | T+0/+3/+7 | recovery | T+14d | exit on payment | tone |
| Win-back | 30d post-churn | churned 30d | email | T+30d | reactivation | T+90d | exit on signup | offer |

## 4. Pre-send QA checklist

- [ ] Segmentation: target list reviewed; sample inspected.
- [ ] Sender name and email pass spam check.
- [ ] Subject line scored; no weird characters.
- [ ] Preview text shows expected words.
- [ ] Personalization variables populate.
- [ ] Copy free of errors; offer appropriate; codes work.
- [ ] Links functional; tracking present.
- [ ] Unsubscribe present (one click).
- [ ] Postal address in footer.
- [ ] Template tested across Gmail, Outlook, Apple Mail, dark mode, mobile.
- [ ] Goal tracking confirmed in analytics.
- [ ] Sign-off: <name>, <date>.

## 5. Measurement

| Level | Metric |
|-------|--------|
| Campaign | sent, delivered, opens, clicks, goal completions, replies, unsubscribes |
| Program | cohort activation lift, day-30 retention lift, expansion ARR attributable, dunning recovery rate |
| Health | spam-complaint rate ≤ 0.1%, bounce ≤ 2%, deliverability ≥ 98% |

## 6. Transactional vs lifecycle vs behavioral

| Type | Examples | Rules |
|------|----------|-------|
| Transactional | receipts, password resets, suspension notices | must deliver; separate sub-domain; not opt-out |
| Lifecycle (stage-based) | onboarding, retention, win-back | opt-out honoured |
| Behavioral (trigger-based) | seat-add upsell, milestone celebrations | opt-out honoured; cap 3/wk |

Frequency caps: max 3 lifecycle emails per week per active subscriber. Suppress lifecycle when transactional was sent in the last 24h (where overlap likely).

## 7. Compliance

- Consent capture at signup with lawful basis (Performance of Contract for transactional; Legitimate Interest with opt-out for lifecycle; Consent for marketing).
- Unsubscribe one-click; preferences page for granularity.
- Address footer.
- ESP listed as sub-processor in DPA Annex III.

## 8. Tooling & SoT

- ESP: <name>.
- Lifecycle tool: <Customer.io / Iterable / Braze>.
- BI: <warehouse>.
- SoT for subscription: <CRM>; for content: <repo>.

## 9. Review cadence

- Weekly: send results.
- Monthly: experiment cycle (one new variant per stage).
- Quarterly: strategy revision.
