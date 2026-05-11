# Agent Action Reversibility Classification Rubric

## Purpose

Force every tool in the action catalogue into exactly one reversibility class. Different classes attract different gates at the FR layer and different rate-limit and kill-switch treatments at the dispatcher.

## The three classes

### `idempotent`

**Definition** — calling the tool again with the same arguments produces the same observable result; the tool has no side-effect outside our trust boundary or has a side-effect that is invisible (a metrics counter, a cache write).

**Examples** — `email.thread.read`, `crm.contact.lookup`, `search.execute`, any pure GET.

**Treatment** — admissible at any autonomy level. No human approval required.

### `compensable`

**Definition** — the tool has a side-effect inside our system that can be cleanly reversed by another named tool in the catalogue. The reversal is **mechanical** — it does not require external escalation, customer notification, or accounting adjustments outside the system.

**Compensability test** — answer "yes" to all four:

1. Is there a named compensating tool in the catalogue (`compensating_tool: <name>`)?
2. Does the compensator restore the system to the state before the original call, observationally?
3. Can the compensator run within minutes, not days?
4. Does the compensator require no human action other than agent or operator initiation?

A "no" on any question downgrades the tool to `irreversible`.

**Examples** — `email.draft.create` (compensated by `email.draft.delete`), `finance.ledger.entry.write` (compensated by `finance.ledger.entry.reverse`), `email.label` (compensated by `email.label.remove`).

**Edge case — refunds** — `payments.refund.issue` is classified `compensable` only if a true `payments.refund.reverse` exists at the payment-provider level and is exposed as a catalogue tool. If the payment provider does not support refund-reversal, the refund tool is `irreversible`.

**Treatment** — admissible at L1+ with the per-FR HITL placement; threshold-gated where the side-effect has financial or reputational magnitude.

### `irreversible`

**Definition** — the tool has a side-effect that cannot be reversed by a catalogue tool. Reversal, if possible at all, requires customer notification, external party action, accounting adjustment, or apology.

**Examples** — `email.send` (the email is gone), `payments.charge.execute` (charging a card cannot be unilaterally undone; the corresponding refund creates a *new* transaction with its own customer-visible side-effects), `file.delete-permanent`, `slack.post-public`, `social.publish`.

**Treatment** —

1. Admissible only at L1 (per-call human approval) or as part of an L2 plan whose plan-approval explicitly covers every irreversible step.
2. Never admissible at L3 or higher without a written waiver and an ADR.
3. Every call emits an `irreversibility_class=irreversible` audit event with the `human_approval_event_id`.
4. Kill-switch always refuses irreversible tools when triggered.

## Edge cases

### "It's reversible if I email the customer"

That is **not** mechanical reversal. The tool is `irreversible`.

### "We have an undo button"

If the undo button is a catalogue tool that the agent can call and that meets the compensability test, the original tool is `compensable`. If the undo is a manual operator action, the original is `irreversible`.

### "It's only irreversible above $X"

Treat the tool as `compensable` with a `threshold_above_which_irreversible: X` field. The dispatcher promotes the class at runtime when the input crosses the threshold.

### "The first call is idempotent but the second is destructive"

The tool is misdesigned. Split it into two catalogue entries with distinct schemas.

## Anti-patterns

- Tools claimed `compensable` with no named compensator. Reject in PR.
- Tools claimed `idempotent` that emit external network traffic with state effects (e.g. webhook POST). Reclassify.
- Tools claimed `irreversible` admitted at L3 without ADR. Reject.

## Cross-references

- `02-requirements-engineering/17-ai-agent-action-catalogue-spec` — uses this rubric.
- `02-requirements-engineering/16-ai-agent-feature-prd-spec` — irreversible-action gate at the FR layer.
- `05-testing-documentation/07-ai-agent-red-team-test-plan` — action-escalation scenarios target this rubric.
- `09-governance-compliance/19-ai-agent-adr-catalogue` — Reversibility-gating policy is an explicit ADR slot.
