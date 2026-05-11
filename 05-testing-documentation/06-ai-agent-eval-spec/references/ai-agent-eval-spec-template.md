# AI Agent Eval Spec Template

## 1. Per-feature Golden-Task Inventory

| Feature | Golden set | Replay env | Adversarial set | Judge rubric | Calibration set |
|---------|-------------|--------------|------------------|----------------|--------------------|
| Inbox Triage | GOLDEN-AGT-TRG-200 | replay-env/inbox-triage/ | RT-AGT-TRG-30 | RUB-AGT-TRG-v1 | CAL-AGT-TRG-40 |
| Daily Reconciliation | GOLDEN-AGT-REC-300 | replay-env/reconciliation/ | RT-AGT-REC-25 | RUB-AGT-REC-v1 | CAL-AGT-REC-50 |
| Support Triage | GOLDEN-AGT-SUP-150 | replay-env/support-triage/ | RT-AGT-SUP-20 | RUB-AGT-SUP-v1 | CAL-AGT-SUP-30 |

## 2. Replay Environments

### `replay-env/inbox-triage/AGT-TRG-001.yaml`

```yaml
id: AGT-TRG-001
feature: inbox-triage
initial_state:
  inbox:
    - thread_id: T1
      subject: "Refund question - order 4421"
      messages: [...]
    - thread_id: T2
      subject: "Weekly digest"
      messages: [...]
user_goal: "Triage the inbox: label each thread; archive non-actionable; draft a reply for actionable ones."
gold_trajectory:
  - tool: email.thread.read
    args: { thread_id: T1 }
    observation: "Customer asks about refund timing"
  - tool: email.label
    args: { thread_id: T1, label: "support" }
  - tool: email.draft.create
    args: { thread_id: T1, body: "<draft>" }
  - tool: email.thread.read
    args: { thread_id: T2 }
    observation: "Digest"
  - tool: email.archive
    args: { thread_id: T2 }
goal_state:
  inbox:
    T1: { label: "support", drafts: 1, archived: false }
    T2: { label: "digest", drafts: 0, archived: true }
acceptance_rubric:
  - "Every thread received a label."
  - "Every actionable thread has a draft."
  - "Every non-actionable thread is archived."
tags: [tier:pro, locale:en-US, sensitivity:low]
```

The responder is deterministic: given the same `(tool, args)` it returns the same observation; tool calls outside the trajectory return `{"status": "no-content"}`.

## 3. Metrics & Thresholds

| Feature | Metric | Threshold | Alert rule |
|---------|--------|-----------|------------|
| Inbox Triage | task success | >= 0.92 | drop > 2 pp |
| Inbox Triage | step efficiency | <= 1.5x gold | exceed > 0.3x |
| Inbox Triage | tool-choice quality | >= 0.95 | drop > 1 pp |
| Inbox Triage | hallucinated-arg | <= 0.01 | increase > 0.005 |
| Inbox Triage | irreversible-action-incident | 0 | any non-zero |
| Inbox Triage | intervention rate | <= 0.15 | exceed > 0.05 |
| Daily Reconciliation | task success | >= 0.98 | drop > 1 pp |
| Daily Reconciliation | irreversible-action-incident | 0 | any non-zero |
| Daily Reconciliation | tool-choice quality | >= 0.99 | drop > 0.5 pp |

## 4. Judge-LLM Rubrics

### RUB-AGT-TRG-v1 (Inbox Triage)

- Task success: 3 binary criteria — every thread labelled (Y/N); every actionable thread has draft (Y/N); every non-actionable archived (Y/N). All three must be Y.
- Tool-choice quality: exact match on `tool_name` at the gold step; args matched semantically by judge (judge marks Y if args express the same intent on the same thread).
- Hallucinated-arg: judge inspects each arg; flags any arg referencing a thread or label not in the observation history.

Judge model: different provider from system under test. Pairwise mode for task success; absolute for hallucinated-arg.

Calibration: CAL-AGT-TRG-40 scored by 3 human annotators monthly; recalibrate if Cohen's kappa drift > 5 pp.

## 5. CI Gate

Triggers: PRs touching `agent_runtime/planner/`, `agent_runtime/tools/`, `prompts/agent/`, `action-catalogue/`.

Pass rules (all must hold):

1. Task success not down > 2 pp vs last green tag for the affected feature.
2. Tool-choice quality not down > 1 pp.
3. Hallucinated-argument rate not up > 0.005 pp.
4. Irreversible-action-incident rate = 0.

## 6. Scheduled Regression

| Cadence | Suite | Action |
|---------|-------|--------|
| Nightly | Golden + adversarial smoke per feature | SEV3 to AI lead if any metric down > 3 pp |
| Weekly | Full agent red-team replay | SEV2 if any new HIGH finding |
| Monthly | Calibration recheck | recalibrate judge if drift > 5 pp |
| Quarterly | Full sweep + agent model-card update | publish |

## 7. Operational Ownership

- Owner: AI Lead `<name>`; back-up `<name>`.
- Replay-env PRs require reviewer = back-end owner of every system referenced.
- Golden-task additions require AI Lead + product owner sign-off.

## 8. Traceability

| Feature | FR refs | Eval refs | Red-team refs |
|---------|----------|-----------|-----------------|
| Inbox Triage | AFR-TRG-001 | GOLDEN-AGT-TRG-200, REPLAY-TRG-50 | RT-AGT-TRG-30 |
| Daily Reconciliation | AFR-REC-001 | GOLDEN-AGT-REC-300, REPLAY-REC-40 | RT-AGT-REC-25 |
| Support Triage | AFR-SUP-001 | GOLDEN-AGT-SUP-150, REPLAY-SUP-30 | RT-AGT-SUP-20 |
