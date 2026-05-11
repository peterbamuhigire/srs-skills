# AI-Feature PRD Addendum (for any AI-powered FR)

Use this addendum when an FR's output is produced or modified by an LLM, vision model, embedding-based retrieval, agent, or fine-tune. Append the seven AI clauses to the FR's body. The full AI-Feature PRD Spec lives at `02-requirements-engineering/14-ai-feature-prd-spec/`.

## The seven mandatory clauses per AI FR

| # | Clause | Form |
|---|--------|------|
| 1 | Hallucination tolerance | factuality threshold + abstain rule |
| 2 | Latency budget | P95 ms target + timeout + fallback |
| 3 | Cost ceiling | per-call USD cap + per-tenant daily cap |
| 4 | Abstain criteria | quantitative rule + behaviour |
| 5 | Citation policy | when required + rendering rule |
| 6 | Consent / opt-in | default state per region + admin override |
| 7 | Training-data exclusion | provider-config evidence + audit cadence |

## Template block to paste under each AI FR

```markdown
### AI clauses for FR-XXX

- Hallucination tolerance: factuality >= 0.XX on EVAL-XXX; abstain below threshold.
- Latency budget: P95 <= XXXX ms; timeout XXXX ms; fallback <fallback>.
- Cost ceiling: <= $0.XX per call; per-tenant daily ceiling $XX (configurable on tier upgrade).
- Abstain criteria: <quantitative rule>; abstain payload per system-message spec.
- Citation policy: every factual claim cites a source span (RAG features); rendered as <link form>.
- Consent / opt-in: default <state> per region; EEA off by default for high-risk; admin override.
- Training-data exclusion: provider configured with no-training endpoint; quarterly audit; contract clause <ref>.

Acceptance: eval harness golden set EVAL-XXX pass >= XX% + red-team set RT-XXX pass >= XX% + hallucination SLO met for the rollout-defined bake duration.
```

## Cross-links

- Full spec: `02-requirements-engineering/14-ai-feature-prd-spec/`
- Eval harness: `05-testing-documentation/04-ai-eval-harness-spec/`
- Red team: `05-testing-documentation/05-ai-red-team-test-plan/`
- Hallucination SLO: `06-deployment-operations/10-ai-hallucination-slo-doc/`
- Responsible AI Declaration: `09-governance-compliance/14-ai-responsible-ai-declaration/`
