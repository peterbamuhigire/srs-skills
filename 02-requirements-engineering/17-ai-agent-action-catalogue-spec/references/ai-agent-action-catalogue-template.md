# Action Catalogue Spec Template

## 1. Catalogue Summary Table

| Tool | Side-effect | Reversibility | Tiers | Rate-limit class | Kill-switch | Compensating tool |
|------|-------------|----------------|-------|--------------------|--------------|---------------------|
| `email.thread.read` | read | idempotent | free, pro, ent | cheap-read | no | — |
| `email.label` | write-internal | compensable | pro, ent | internal-write | yes | `email.label.remove` |
| `email.archive` | write-internal | compensable | pro, ent | internal-write | yes | `email.unarchive` |
| `email.draft.create` | write-internal | compensable | pro, ent | internal-write | yes | `email.draft.delete` |
| `email.send` | write-external | irreversible | ent | external-write | yes | — (no compensator; human gate per call) |
| `finance.ledger.match.read` | read | idempotent | ent | cheap-read | no | — |
| `finance.ledger.entry.write` | write-internal | compensable | ent | internal-write | yes | `finance.ledger.entry.reverse` |
| `payments.refund.issue` | billing | compensable | ent | billing | yes | `payments.refund.reverse` |
| `payments.charge.execute` | billing | irreversible | ent | billing | yes | — (human gate per call) |

## 2. Reversibility Rubric

See `agent-reversibility-classification-rubric.md`.

## 3. Per-tool Entries

### `email.send`

```yaml
name: email.send
description: Send an email from the workspace owner's address. Side-effect leaves our trust boundary.
input_schema:
  type: object
  required: [thread_id, body, recipient]
  properties:
    thread_id: { type: string }
    body:      { type: string, maxLength: 8000 }
    recipient: { type: string, format: email }
output_schema:
  type: object
  properties:
    message_id: { type: string }
side_effect_class: write-external
reversibility_class: irreversible
compensating_tool: null
human_approval: required-per-call
tier_availability:
  free:       []
  pro:        []
  enterprise: [L1, L2]
rate_limit_class: external-write
kill_switch:
  global:       refuse
  per_tenant:   refuse
  refusal_msg:  "Sending is paused for your workspace. Contact your admin."
```

### `payments.refund.issue`

```yaml
name: payments.refund.issue
description: Issue a refund against a prior charge. Side-effect is compensable via reverse-refund.
input_schema:
  type: object
  required: [charge_id, amount_usd, reason_code]
  properties:
    charge_id:  { type: string }
    amount_usd: { type: number, minimum: 0.01, maximum: 10000 }
    reason_code:{ type: string, enum: [duplicate, fraud, customer-request, error] }
output_schema:
  type: object
  properties:
    refund_id: { type: string }
side_effect_class: billing
reversibility_class: compensable
compensating_tool: payments.refund.reverse
human_approval: required-per-call-above-threshold
approval_threshold:
  amount_usd: 200
tier_availability:
  enterprise: [L1, L2]
rate_limit_class: billing
kill_switch:
  global:       refuse
  per_tenant:   refuse
  refusal_msg:  "Refund automation is paused. Issue refunds manually."
```

## 4. Tier Availability Matrix

| Tool | Free | Pro | Enterprise |
|------|------|-----|------------|
| `email.thread.read` | L0 | L0..L2 | L0..L3 |
| `email.label` | — | L0..L2 | L0..L3 |
| `email.send` | — | — | L1, L2 |
| `payments.refund.issue` | — | — | L1, L2 |
| `payments.charge.execute` | — | — | L1 only (per-call HITL mandatory) |

## 5. Audit Field Schema

Every tool call emits an `agent_tool_call_event` record with:

| Field | Notes |
|-------|-------|
| `tenant_id` | required |
| `user_id` | required |
| `agent_run_id` | required |
| `plan_id` | required |
| `step_index` | required |
| `tool_name` | required |
| `input_args_redacted` | PII redacted at the dispatcher |
| `output_summary_redacted` | first 256 chars; PII redacted |
| `latency_ms` | required |
| `cost_usd` | LLM cost + external cost; rolls up to agent_run total |
| `outcome` | one of {success, refused, error, timeout, kill-switch-aborted} |
| `irreversibility_class` | snapshot at call time |
| `human_approval_event_id` | required when reversibility=irreversible or above-threshold |

Retention: minimum 13 months hot; 7 years cold for billing-class and irreversible-class events.

## 6. Rate-limit Class Table

| Class | Per-tenant | Per-agent-run | Burst |
|-------|------------|----------------|-------|
| `cheap-read` | 60/min | 100 | 20 |
| `expensive-read` | 10/min | 20 | 5 |
| `internal-write` | 30/min | 50 | 10 |
| `external-write` | 5/min | 10 | 2 |
| `billing` | 2/min | 5 | 1 |

## 7. Kill-switch Behaviour

- Global kill-switch (operator-only): refuses every tool with `kill_switch.global = refuse`. Cheap reads continue to allow status pages to render.
- Per-tenant kill-switch (admin-or-operator): refuses every tool with `kill_switch.per_tenant = refuse`.
- Refusal returns the user-visible message and terminates the agent run gracefully (no retries).

## 8. Change-control Protocol

Adding, removing, or modifying a tool entry requires:

1. PR with reviewer = back-end owner + AI Lead + Security.
2. Red-team smoke targeting the new tool category.
3. ADR in `19-ai-agent-adr-catalogue` if the change alters tier availability, reversibility class, or human-approval requirement.
4. Sign-off via `python -m engine signoff` before deploy.

## 9. Traceability to Agent FRs

| FR | Tools referenced |
|----|---------------------|
| AFR-TRG-001 | `email.thread.read`, `email.label`, `email.archive`, `email.draft.create` |
| AFR-REC-001 | `finance.ledger.match.read`, `finance.ledger.entry.write`, `finance.ledger.entry.reverse` |
| AFR-SUP-001 | `ticket.read`, `ticket.label`, `ticket.assign`, `ticket.comment.internal` |
