---
name: ai-economic-value-brief
description: Use when creating the strategic brief for an AI-powered system, AI feature,
  agentic workflow, analytics product, or automation initiative. Converts AI ambition
  into business outcomes, measurable requirements, data needs, risk controls, and a
  defensible delivery roadmap.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Economic Value Brief
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use When

- A project involves AI apps, AI-assisted workflows, RAG, agents, predictive analytics, automation, or AI copilots.
- Stakeholders are asking for AI but have not defined business value, evaluation criteria, data readiness, or operating ownership.
- You need inputs for PRD, SRS, business case, architecture, test strategy, governance, or proposal documents.

## Required Inputs

- Business process and users affected.
- Current baseline: time, cost, errors, revenue, conversion, service level, compliance risk, or decision quality.
- Data sources, owners, freshness, sensitivity, quality gaps, and integration constraints.
- AI action type: generate, classify, extract, search, recommend, predict, analyze, or execute.
- Risk level and required human approval points.
- Budget, timeline, maintenance owner, and success metric.

## Brief Workflow

1. **Define economic outcome**: State the metric AI should improve and why it matters.
2. **Map the workflow**: Trigger, inputs, decisions, actions, handoffs, current bottlenecks, and failure costs.
3. **Select AI pattern**: Simple LLM call, RAG, deterministic workflow, analytics/ML, agent, or fine-tune.
4. **Specify data foundation**: Required data, access rights, quality checks, retention, privacy, and tenant isolation.
5. **Set evaluation gates**: Golden cases, adversarial cases, quality thresholds, cost limits, latency targets, and rollback triggers.
6. **Plan governance**: Human approval, audit trail, explainability, security controls, incident response, and ownership.
7. **Sequence roadmap**: Prototype, pilot, production hardening, rollout, monitoring, and continuous improvement.

## Output Template

```markdown
# AI Economic Value Brief: [System/Feature]

## 1. Business Outcome
- Target metric:
- Baseline:
- Desired improvement:
- Economic value:

## 2. Users and Workflow
- Users:
- Current workflow:
- AI-assisted workflow:
- Decision/action changed:

## 3. AI Pattern
- Recommended pattern:
- Why this pattern:
- Rejected alternatives:

## 4. Data and Integration
- Data sources:
- Data quality risks:
- Privacy/security requirements:
- Required integrations:

## 5. Evaluation and Acceptance
- Golden test cases:
- Quality thresholds:
- Cost/latency thresholds:
- Safety thresholds:
- Rollback triggers:

## 6. Operations
- Human approval points:
- Monitoring:
- Owner:
- Maintenance cadence:

## 7. Roadmap
- Prototype:
- Pilot:
- Production:
- Scale:
```

## Hard Rules

- Do not approve an AI requirement that lacks a measurable outcome or evaluation method.
- Prefer deterministic workflows over agents for known, auditable processes.
- Treat prompts, model versions, retrieval indexes, and tool contracts as versioned requirements.
- Document failure modes and fallback behavior as first-class requirements.
