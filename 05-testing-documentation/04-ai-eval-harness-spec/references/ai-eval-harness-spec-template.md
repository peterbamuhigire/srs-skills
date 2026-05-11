# AI Eval Harness Spec Template

## 1. Per-feature Suite Inventory

| Feature | Golden set | Adversarial set | Judge rubric | Calibration set |
|---------|------------|-------------------|----------------|--------------------|
| AI Summary | EVAL-SUM-200 | RT-SUM-50 | RUB-SUM-v1 | CAL-SUM-50 |
| AI Composer | EVAL-COMP-150 | RT-COMP-60 | RUB-COMP-v1 | CAL-COMP-40 |
| AI Analyst | EVAL-ANL-300 | RT-ANL-80 | RUB-ANL-v1 | CAL-ANL-60 |
| AI Agent | EVAL-AGT-100 | RT-AGT-50 | RUB-AGT-v1 | CAL-AGT-30 |

## 2. Golden Set Construction

### EVAL-SUM-200

- Provenance: 120 from production traffic snapshots (anonymised, opt-in), 60 from design-partner samples, 20 expert-authored edge cases.
- Labellers: <names>; QA review by AI lead.
- Class balance: short / medium / long; technical / non-technical; 5 locales.
- Per-example schema:

```yaml
- id: SUM-001
  input:
    thread: |
      ...
  expected:
    rubric: "summary captures the action item, the date, and the owner"
  category: action-item
  locale: en-US
  sensitivity: low
```

Repeat for every golden set.

## 3. Metrics and Thresholds

| Feature | Metric | Threshold | Alert rule |
|---------|--------|-----------|------------|
| AI Summary | pass rate | >= 92% | drop > 3 pp |
| AI Summary | factuality | >= 0.95 | drop > 2 pp |
| AI Summary | toxicity violations | 0 | any non-zero |
| AI Composer | pass rate | >= 90% | drop > 3 pp |
| AI Composer | tone match | >= 0.85 | drop > 3 pp |
| AI Composer | citation rate | >= 0.90 | drop > 3 pp |
| AI Composer | toxicity violations | 0 | any non-zero |
| AI Analyst | numeric correctness | >= 0.97 | drop > 1 pp |
| AI Analyst | citation accuracy | >= 0.95 | drop > 2 pp |
| AI Analyst | toxicity violations | 0 | any non-zero |
| AI Agent | tool-arg correctness | >= 0.98 | drop > 1 pp |
| AI Agent | unapproved action rate | 0 | any non-zero |

## 4. Judge-LLM Patterns

- Judge model: distinct provider from the system under test (e.g. judge is OpenAI when system is Anthropic, and vice versa).
- Rubric form: 3-5 short discrete criteria per feature, each scored {0, 1}; aggregate by rubric weights.
- Pairwise judging used for tone, style, and helpfulness; absolute judging for factuality and citation correctness.
- Calibration: judge re-runs on the CAL-* sets monthly; if judge agreement with human labels drops by > 5 pp, recalibrate or replace the rubric.
- Judge prompt and rubric versioned in the prompt registry.

## 5. CI Gate

Rules (all must pass):

1. Golden pass rate for the affected feature shall not regress by more than 2 percentage points relative to the last green tag.
2. Safety / toxicity violation count = 0.
3. Citation rate (RAG features) shall not regress by more than 3 pp.
4. Latency P95 in the eval harness simulator shall remain within +20% of last green tag.

The gate runs on every PR that touches: prompts/, models/, retrieval-config/, post-processors/, eval-sets/.

## 6. Scheduled Regression

| Cadence | Suite | Action on drop |
|---------|-------|------------------|
| Nightly | Golden, per feature | SEV3 to AI lead if > 3 pp drop |
| Weekly | Red-team, per feature | SEV2 if any new high finding |
| Monthly | Calibration | recalibrate judge if drift > 5 pp |
| Quarterly | Full sweep (golden + red-team + cal) | publish updated model card |

## 7. A/B Prompt Eval

Procedure for evaluating a proposed prompt change:

1. Pin the existing prompt tag and the candidate prompt tag.
2. Run both on the golden set + a recent 200-example production-snapshot set.
3. Side-by-side judge run for tone / helpfulness metrics; absolute scoring for factuality / citation.
4. Win criterion: candidate >= existing on the primary metric (per feature) AND no regression on the safety metric AND latency P95 within +10%.
5. If win, promote candidate to staging; bake 24 h; promote to prod.

## 8. Operational Ownership

- AI Lead: <name> -- owner of suite versions, judge versions, CI gate.
- Back-up: <name>.
- Eval-set changes: PR with sign-off from AI Lead + the relevant feature owner.
- Judge model swaps: ADR + recalibration on the CAL set before merge.

## 9. Traceability

| Eval ID | AI FR | Model Card | Red-team ID |
|---------|-------|-------------|--------------|
| EVAL-SUM-200 | AI-FR-001 | MC-SUM-v1 | RT-SUM-50 |
| EVAL-COMP-150 | AI-FR-002 | MC-COMP-v1 | RT-COMP-60 |
| EVAL-ANL-300 | AI-FR-003 | MC-ANL-v1 | RT-ANL-80 |
| EVAL-AGT-100 | AI-FR-004 | MC-AGT-v1 | RT-AGT-50 |
