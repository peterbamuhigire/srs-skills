# AI-Feature Tier Guidance (addendum to pricing & packaging spec)

When pricing tiers expose AI features, the spec must additionally capture:

## 1. AI tier placement principles

- AI summarisation often becomes table-stakes; expose on Starter or above.
- AI assistants / copilots usually live on Professional and above.
- AI analysts / agents and per-tenant high-cost AI typically live on Business / Enterprise.
- Free tier AI access (if any) is rate-limited; cost loss is a CAC budget line, not a margin loss.

## 2. AI usage-based dimensions

Augment the value-metric chapter with AI-usage dimensions where relevant:

- AI summaries per workspace per month.
- AI composer drafts per user per day.
- AI analyst queries per workspace per day.
- AI agent runs per workspace per day.
- Tokens included in tier; overage rate per 1M tokens.

## 3. Per-tier cost-to-serve

For each tier, document the expected cost-to-serve of AI features:

| Tier | Included AI features | Modelled cost / workspace / month | Gross margin floor |
|------|------------------------|--------------------------------------|-----------------------|
| Free | AI Summary (limited) | $X | -- (CAC bucket) |
| Starter | AI Summary (full) | $X | >= 75% |
| Pro | + AI Composer | $X | >= 70% |
| Business | + AI Analyst | $X | >= 65% |
| Enterprise | + AI Agent + dedicated CSM | $X | >= 60% |

## 4. Overage and throttle

- Soft warn at 80% of included.
- Hard throttle at 100% of included (cheaper-model route).
- Pay-as-you-go overage at the published per-1M-token rate, billed monthly.
- Per-tenant daily ceilings prevent runaway (see AI Cost Runbook).

## 5. Pricing-change protocol for AI tiers

- Provider price changes cascade to our tiers with quarterly review.
- 90-day notice on AI overage rate change.
- Grandfather existing AI commitments on contract terms.

## 6. Cross-links

- Cost Runbook: `06-deployment-operations/12-ai-cost-runbook/`
- Billing & Metering Spec (AI events): `02-requirements-engineering/13-saas-billing-and-metering-spec/`
- Feature Strategy Doc: `01-strategic-vision/13-ai-feature-strategy-doc/`
