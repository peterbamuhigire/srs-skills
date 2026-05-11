# AI Hallucination SLO Template

## 1. AI SLI Inventory

| SLI | Definition | Source | Sample |
|-----|-----------|--------|--------|
| Factuality | % responses where judge-LLM confirms all claims supported | judge-LLM on production-sample | 1% of traffic, nightly |
| Citation accuracy | % cited spans matching source (tolerance 50 chars) | post-processor + judge | every cited response, daily aggregation |
| Abstention precision | abstains that should have abstained / total abstains | judge + monthly human spot-check | 100% of abstains audited |
| Abstention recall | abstains on should-abstain inputs / total should-abstain | judge on production-sample | 1% of traffic |
| Safety violation rate | content-filter trips per million calls | filter telemetry | every event |
| Latency P95 | per parent SLO doc | APM | every request |
| Cost / call | per cost runbook | gateway meter | every request |

## 2. Measurement Procedure

- Factuality: replay 1% of production requests through judge-LLM nightly. Persist scores; alert on rolling-7-day drop > 3 pp.
- Citation: post-processor records every citation; daily job validates citation against source.
- Abstention: every abstain payload labelled by structured abstain_reason; nightly judge audit; monthly human spot-check of 50 abstains.
- Safety violation: content-filter emits an event per trip. Each event alarms.

## 3. Per-Feature SLO Targets

### AI Summary

| Tier | Factuality | Abstention precision | Safety violations |
|------|-----------|-----------------------|--------------------|
| Free | >= 0.90 | >= 0.75 | 0 |
| Pro | >= 0.93 | >= 0.80 | 0 |
| Enterprise | >= 0.95 | >= 0.85 | 0 |

### AI Composer

| Tier | Factuality | Citation accuracy | Abstention precision | Safety violations |
|------|-----------|--------------------|-----------------------|--------------------|
| Pro | >= 0.92 | >= 0.90 | >= 0.80 | 0 |
| Enterprise | >= 0.95 | >= 0.93 | >= 0.85 | 0 |

### AI Analyst

| Tier | Numeric correctness | Citation accuracy | Abstention precision | Safety violations |
|------|----------------------|--------------------|-----------------------|--------------------|
| Business | >= 0.95 | >= 0.93 | >= 0.80 | 0 |
| Enterprise | >= 0.97 | >= 0.95 | >= 0.85 | 0 |

### AI Agent

| Tier | Tool-arg correctness | Unauthorised actions | Safety violations |
|------|------------------------|------------------------|--------------------|
| Enterprise | >= 0.98 | 0 | 0 |

## 4. Error Budgets (30-day)

Budget(calls) = (1 - SLO_factuality) × calls_in_period.

Examples:

- AI Summary Enterprise, factuality 0.95, 10M calls/mo: budget = 500,000 acceptable not-fully-supported responses.
- AI Analyst Enterprise, numeric 0.97, 1M calls/mo: budget = 30,000.

## 5. Burn-Rate Alerts

| Alert | Burn rate | Window | Threshold | Severity |
|-------|-----------|--------|-----------|----------|
| Fast burn | 14× | 1 h | 2% of monthly budget | SEV2 |
| Medium burn | 6× | 6 h | 5% | SEV3 |
| Slow burn | 1× | 3 d | 10% | SEV4 |
| Citation drop | -- | 24 h | drop > 5 pp | SEV2 + auto-rollback |
| Safety trip | -- | event | any | SEV1 |

## 6. Freeze and Rollback Rules

- Error budget exhausted (30-d): freeze prompt and model changes; eval bumps require executive approval.
- Citation accuracy drop > 5 pp in 24 h: auto-rollback to last green prompt tag.
- Factuality drop > 5 pp in 24 h: SEV2; manual rollback decision within 1 h.
- Safety violation: pause feature; SEV1; postmortem; provider escalation if upstream.

## 7. Customer-Facing AI Commitments

| Tier | Public commitment | Internal SLO backing it |
|------|---------------------|---------------------------|
| Free | best-effort AI features; no SLA | -- |
| Pro | "AI features evaluated on a published golden set; flagged outputs reviewed within 5 BD" | factuality SLO + flag-button + review SLA |
| Business | as Pro + "monthly AI-quality summary" | factuality + citation SLOs |
| Enterprise | as Business + per-deployment model card + quarterly review meeting | full SLI set + dedicated CSM |

Perceived-hallucination report flow:

1. User clicks "Report inaccurate" on output.
2. Output, prompt, retrieval-set, and model+tag captured.
3. Ticket auto-created; assigned to AI quality queue.
4. Review within 5 BD (Pro), 3 BD (Business), 1 BD (Enterprise).
5. Confirmed hallucinations feed the eval-set + the model card limitations.

## 8. Review Cadence

- Monthly: AI SLI review (AI lead + SRE + customer success).
- Quarterly: per-tier commitment review; model card refresh.
- After every model bump: re-baseline SLOs.
