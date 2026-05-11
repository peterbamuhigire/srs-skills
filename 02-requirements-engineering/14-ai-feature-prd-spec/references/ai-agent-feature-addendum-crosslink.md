# Agent-Feature Addendum Cross-Link

When an AI feature in the AI Feature PRD Spec is classified as agentic by the AI Agent Strategy Doc, the PRD MUST also produce the **AI Agent Feature PRD Spec** addendum.

## Trigger

A feature is agentic if it passes three of four gates in `01-strategic-vision/14-ai-agent-strategy-doc`:

1. Multi-step with branching that cannot be enumerated at design time.
2. Tool use beyond a single retrieval call (write or external).
3. Outcome-shaped success criterion.
4. Variable step count by input.

## Downstream artefacts

Once a feature is agentic, the AI Feature PRD Spec's seven AI clauses are joined by seven additional agent clauses captured in `02-requirements-engineering/16-ai-agent-feature-prd-spec`:

- Task scope boundary
- Autonomy level (L0..L4)
- Action-catalogue reference
- Intervention triggers
- Budget caps (max-step, max-cost, max-wallclock)
- Abstain criteria
- Irreversible-action gate

## Acceptance gate alignment

The eval-harness acceptance gate is augmented for agentic features by the agent eval rig (`05-testing-documentation/06-ai-agent-eval-spec`) — golden-task replay, tool-choice quality, hallucinated-argument rate, irreversible-action-incident rate, intervention rate.

## Skill invocation order

For an agentic feature:

1. `ai-feature-strategy-doc` → declares the feature.
2. `ai-agent-strategy-doc` → confirms agent classification, autonomy, tier.
3. `ai-feature-prd-spec` → seven AI clauses on the feature.
4. `ai-agent-feature-prd-spec` → seven agent clauses on the feature.
5. `ai-agent-action-catalogue-spec` → tool surface.
6. `ai-agent-architecture-spec` → runtime.
7. `ai-agent-eval-spec` + `ai-agent-red-team-test-plan` → tests.
8. `ai-agent-slo-doc` + `ai-agent-runbook` + `ai-agent-rollout-runbook` → operations.
9. `ai-agent-user-disclosure-pack` → user-facing copy.
10. `ai-agent-responsible-ai-addendum` + `ai-agent-adr-catalogue` → governance.
