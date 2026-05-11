# AI-Feature PRD Addendum (paste into generic PRD)

Use this addendum to extend the generic `01-prd-generation` output for any AI-powered feature. Append the following sub-sections to the FR block.

## FR-XXX — [Feature name]

### Hallucination tolerance

- Factuality target: >= 0.XX on golden set EVAL-XXX.
- Citation accuracy target: >= 0.XX (RAG features only).
- Abstain rule when below target.

### Latency budget

- P95 target: <= XXXX ms end-to-end.
- Per-stage budget: retrieval XXX ms, model call XXX ms, post-process XXX ms.
- Timeout: XXXX ms with graceful fallback (last good response / cached / error message).

### Cost ceiling

- Per-call ceiling: <= $0.XX.
- Per-tenant daily ceiling: <= $XX (configurable).
- Throttle behaviour on ceiling breach.

### Abstain criteria

- Quantitative: confidence score < X, retrieval count < N, or judge-LLM gate fails.
- Behaviour on abstain: structured non-answer with offer to escalate to human.

### Citation policy

- Every factual claim about ingested content cites a source span (doc id + offset).
- Citation rendering rule in UI.

### Consent and opt-in

- Feature default state per region and per tier.
- Admin override path.
- End-user privacy notice text reference.

### Training-data exclusion

- Provider configuration evidence (no-training endpoint, zero-retention contract clause).
- Quarterly audit reference.

### Acceptance gate

- Eval harness pass threshold (golden set ID + percentage).
- Red-team pass threshold (adversarial set ID + percentage).
- Hallucination SLO target post-launch.
