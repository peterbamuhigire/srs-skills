# SaaS Growth Experiment — Template

## 1. Hypothesis

If <change>, then <metric> will <direction> by <magnitude>, because <mechanism>.

## 2. Metrics

| Type | Metric | Source | Target |
|------|--------|--------|--------|
| Primary | | | |
| Guardrail 1 | | | must not regress > |
| Guardrail 2 | | | |
| Leading indicator | | | |

## 3. Segment & sample size

- Segment definition:
- Baseline: <%>
- MDE: <%>
- Power: 80%, Significance: 95%
- Sample size per arm: <N>
- Estimated duration: <weeks>

## 4. Stop rule

- Max duration: <weeks>
- Early-stop on guardrail breach: yes / no, threshold <%>
- Pre-registered analysis date: <YYYY-MM-DD>

## 5. Decision rule

- Ship if: primary +X% with p < 0.05 AND no guardrail regresses by > Y%.
- Reject if: primary -X% OR guardrail regresses > Y%.
- Iterate if: inconclusive.

## 6. Instrumentation

- Variant assignment: `hash(user_id || experiment_id) % 100`.
- Events emitted: `experiment.assigned`, primary metric event, guardrails.
- A/B platform: <name>.
- Tenant scoping: <user-level | tenant-level>.

## 7. Risks & ethics

- Reversibility:
- Customer impact:
- Pricing-test caveats (if applicable):
- User notification:

## 8. Timeline

| Date | Milestone |
|------|-----------|
| | Design review |
| | Launch |
| | Mid-experiment check |
| | Pre-registered analysis |
| | Decision |

## 9. Post-mortem (fill after)

- Result summary:
- Did we learn what we hypothesised?
- Action taken:
- Surprising findings:
- Process notes:
