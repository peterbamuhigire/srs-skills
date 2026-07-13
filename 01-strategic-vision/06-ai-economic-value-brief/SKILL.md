---
name: 06-ai-economic-value-brief
description: Use when an AI feature, agent, RAG workflow, predictive product or automation proposal needs business outcomes, data readiness, evaluation, operating cost, risk and delivery evidence before PRD or architecture work; use AI feature strategy for portfolio sequencing.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# AI Economic Value Brief
<!-- dual-compat-start -->
## Use When

- An AI proposal must prove economic value and measurable task improvement before implementation commitment.

## Do Not Use When

- Do not use to select detailed AI architecture, prompts or model versions; route approved outcomes to their Phase 03 specifications.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Current workflow, cost and outcome baseline | Business owner and operational evidence | Required | Return a baseline-gap plan; do not invent savings. |
| Candidate AI use and data evidence | Product, data and risk owners | Required | Stop if lawful access, representative data or accountable ownership is absent. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the AI Economic Value Brief through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the AI Economic Value Brief to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Economic Value Brief | Sponsor, product owner and AI architecture team | The brief links a named workflow outcome to baseline, target, evaluation method, cost envelope, risks, owner and stop criteria. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified AI Economic Value Brief draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Outcome is measurable and data is fit | Advance to a bounded AI experiment | Investment has a falsifiable value case |
| Value depends on unavailable data or unverifiable accuracy | Block build commitment and remediate evidence | AI theatre consumes delivery budget |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Starting with a model name. Fix: start with the workflow and economic outcome.
- Calling time saved a benefit without a baseline. Fix: measure current handling time and volume.
- Ignoring inference and review costs. Fix: include unit economics and human oversight.
- Using model accuracy as business success. Fix: connect evaluation to user task completion or avoided loss.
- Hiding an unsafe or unlawful data dependency. Fix: make data readiness a stop condition.

## References

- [Brief template](references/ai-economic-value-brief-template.md)
- [AI feature strategy neighbour](../13-ai-feature-strategy-doc/SKILL.md)
<!-- dual-compat-end -->



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
