# AI Definition of Done Addendum

For any story whose acceptance involves AI behaviour, the team's Definition of Done MUST include the AI-specific gates below in addition to the base DoD.

## AI DoD additions

- [ ] Eval harness run on the affected feature; regression <= 2 pp on the golden set; result attached to the PR.
- [ ] Red-team smoke run on the affected feature; 0 CRITICAL, 0 HIGH; result attached.
- [ ] Model card updated for the feature (or a note in the change log if pin unchanged).
- [ ] Prompt registry tag bumped if the prompt changed; PR contains the new tag.
- [ ] Cost regression check run; per-call cost within +20% of baseline; large deltas explained.
- [ ] Observability events emitted (tokens, latency, cost, abstain flag, citation count) and visible in dashboards.
- [ ] PII redaction at the log boundary verified.
- [ ] Acceptance test references the eval set ID, not exact-string assertions.
- [ ] Documentation updated: model card, responsible-AI declaration (if user-facing behaviour shifted), AI-feature PRD addendum (if requirements moved).

## When the story introduces a NEW AI feature

Additional items:

- [ ] AI Feature PRD Spec entry with the seven AI clauses.
- [ ] Model card created and signed off.
- [ ] Eval set seeded (>= 100 examples; provenance documented).
- [ ] Red-team scenarios authored across applicable categories.
- [ ] Hallucination SLO targets set per tier.
- [ ] Rollout runbook stage definition added.
- [ ] Cost runbook ceilings set.
- [ ] Disclosure copy approved by Legal + DPO.
- [ ] ADRs created for model choice, RAG-vs-fine-tune, abstain policy, rollback trigger.

## When the story bumps a provider model

Additional items:

- [ ] Full eval + red-team re-run before promotion.
- [ ] Model card re-issued.
- [ ] Hallucination SLO re-baselined.
- [ ] Customers in the relevant tier notified per the trust-center commitments.

## When the story changes a prompt

Additional items:

- [ ] PR contains the prompt diff.
- [ ] Regression eval attached.
- [ ] Red-team smoke green.
- [ ] Owner + AI Lead sign-off in the PR.
- [ ] Tag bump per the prompt registry rules.

## When the story changes an agent tool catalogue

Additional items:

- [ ] Tool input schema validated.
- [ ] Authorisation check by tenant claim.
- [ ] Side-effect class declared (read / write / irreversible).
- [ ] Per-step approval enforced for irreversible.
- [ ] Tool-result wrapper + rider in place.
