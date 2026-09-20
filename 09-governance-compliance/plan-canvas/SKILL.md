---
name: plan-canvas
description: Use when an SRS, HLD/LLD, ADR, acceptance-criteria set, or any other governance artefact needs a human reviewer to point at the exact clause they mean and deliver an Approve / Request-changes verdict, instead of typing prose feedback like "change the third requirement in section 4.2". Use formal-review-gates for the gate's entry/exit criteria and sign-off-ledger to record the resulting verdict as an approval event.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
  origin: "Adapted from ECC's plan-canvas skill (C:\\Users\\Peter\\Downloads\\ECC-main\\skills\\plan-canvas\\SKILL.md), reframed for SRS-artefact review gates rather than implementation plans."
---

# Plan Canvas for SRS Review

A browser-based **annotate-and-approve** review loop for this engine's written
artefacts — SRS sections, HLD/LLD documents, ADRs, acceptance-criteria
catalogues, baseline deltas — used in place of prose feedback typed into a
chat window. The reviewer opens the artefact locally, **annotates the exact
clause or requirement they mean**, chats inline if needed, and delivers an
**Approve / Request changes** verdict. The agent blocks on one call that
returns the feedback as structured JSON.

This is the same mechanism ECC ships for plan review (`ecc-plan-canvas`),
reframed here for a governance artefact instead of an implementation plan.
Read the ECC original in full before wiring this up —
`skills/plan-canvas/SKILL.md` and `docs/design/plan-canvas.md` in the ECC
checkout — because the engineering lessons below are load-bearing, not
decorative.

## Why this engine needs it specifically

Every phase of this engine ends in a document a human must review and sign
off: an SRS baseline, a CCB decision, a waiver, a sign-off-ledger entry. Right
now that review happens as prose typed back at the agent — "change the third
requirement in section 4.2" — which is ambiguous (which of several "third"
requirements?), expensive to disambiguate, and leaves no anchored record of
what was actually pointed at. A canvas verdict is a **signature event**: it
can be recorded directly into `09-sign-off-ledger` with the anchor (which
clause), the verdict, and the reviewer identity, rather than reconstructed
from a chat transcript after the fact.

## Dependency and current status

The `plan-canvas` CLI is vendored into this engine at
`scripts/plan-canvas.js` and `scripts/lib/plan-canvas/*.js` (plus
`scripts/lib/loopback-guard.js`), the same way `hooks/destructive-bash-gate.js`
was vendored — copied from ECC's checkout
(`C:\Users\Peter\Downloads\ECC-main\scripts\plan-canvas.js` and
`scripts\lib\plan-canvas\`), with no dependency on ECC's `package.json` or
plugin-root bootstrap. Invoke it as:

```bash
node scripts/plan-canvas.js open <file>
node scripts/plan-canvas.js await <file>
```

(the `ecc-plan-canvas` name used elsewhere in this document is the
conceptual/ECC-upstream name for the same tool; this engine has no shell
alias installed for it — use the `node scripts/plan-canvas.js` form above).

The two Stop/SessionStart hooks (`hooks/plan-canvas-pending.js`,
`hooks/plan-canvas-sessions.js`) are vendored and wired into
`hooks/hooks.json` alongside `destructive-bash-gate.js`.

This was verified working, not just ported: the loopback server starts,
serves `/health` and the canvas HTML, accepts feedback over its HTTP API,
and delivers it through both `await` and the Stop-hook drain path, exercised
with real HTTP requests and real subprocess calls (not mocked). 128 ported
tests pass — `node tests/plan-canvas/markdown.test.js` (64),
`tests/plan-canvas/sessions.test.js` (16), `tests/scripts/plan-canvas.test.js`
(28), `tests/plan-canvas/e2e.test.js` (9, full CLI + detached-server
workflow), `tests/hooks/plan-canvas-pending-hook.test.js` (7), and
`tests/hooks/plan-canvas-sessions-hook.test.js` (4) — adapted from ECC's own
`tests/lib/plan-canvas-markdown.test.js`, `tests/lib/plan-canvas-sessions.test.js`,
`tests/scripts/plan-canvas.test.js`, `tests/integration/plan-canvas-e2e.test.js`,
`tests/hooks/plan-canvas-pending-hook.test.js`, and
`tests/hooks/plan-canvas-sessions-hook.test.js`, with only file-path changes
(hooks live at this engine's repo-root `hooks/`, not ECC's `scripts/hooks/`)
and no logic changes.

## When to Use

- An SRS baseline, HLD/LLD document, ADR, acceptance-criteria catalogue, or
  baseline delta is ready for `05-formal-review-gates` and needs a **reviewer
  verdict**, not just a read.
- The reviewer needs to *point at* a specific requirement, clause, or table
  row rather than describe its location in prose.
- The artefact is a local `.md` file under a project's phase directory (see
  `projects/<ProjectName>/<phase>/<document>/`) or a rendered `.html`
  deliverable.

Do NOT use for: code review of diffs, running the delivered system, or remote
URLs. The canvas serves local artefact files only — the same boundary ECC
draws.

## How It Works

```bash
# 1. Open the artefact in the reviewer's browser (returns immediately)
node scripts/plan-canvas.js open projects/<ProjectName>/09-governance-compliance/05-adr/0007-use-postgres.md

# 2. Block until the reviewer responds. Run this as a background task —
#    see "Stay listening" below — and re-run if interrupted; queued
#    feedback is never lost.
node scripts/plan-canvas.js await projects/<ProjectName>/09-governance-compliance/05-adr/0007-use-postgres.md
```

### Stay listening, or the reviewer talks to an empty chair

Feedback only reaches the agent while an `await` is actually parked on the
session. If the agent's turn ends with nothing listening, the reviewer's
message sits in the queue and, from their side of the glass, sending appears
to do nothing at all.

So **run `await` as a background task** (in Claude Code, a Bash call with
`run_in_background: true`). It exits the moment feedback arrives, which keeps
the loop alive across turns instead of dying with a foreground call that the
harness eventually time-limits.

Two backstops exist, and neither is an excuse to skip the above:

- `node scripts/plan-canvas.js pending` lists feedback queued with no listener.
- A `Stop` hook (`hooks/plan-canvas-pending.js`, vendored from ECC's
  `scripts/hooks/plan-canvas-pending.js`) blocks the agent's turn from ending
  while canvas feedback is undelivered. It is wired into this engine's
  `hooks/hooks.json` alongside `destructive-bash-gate.js`. A companion
  `SessionStart` hook (`hooks/plan-canvas-sessions.js`) surfaces any review
  left open from a previous session.

`await` prints JSON when the reviewer acts:

```json
{
  "status": "feedback",
  "items": [
    { "kind": "annotation", "text": "This NFR threshold conflicts with AC-014",
      "anchor": { "selector": "table tr:nth-of-type(4)", "tag": "tr",
                  "snippet": "NFR-003: p95 latency < 200ms" } },
    { "kind": "verdict", "verdict": "request-changes" }
  ]
}
```

- `kind: "chat"` — freeform reviewer message; answer in the canvas, not the
  terminal.
- `kind: "annotation"` — feedback anchored to a specific requirement,
  clause, or row (`anchor.selector` / `anchor.snippet` show exactly what was
  pointed at). This is the direct replacement for "the third requirement in
  section 4.2".
- `kind: "verdict"` — `approve` means the artefact is CONFIRMED at this gate:
  stop polling, record the sign-off event, and hand off to the next phase.
  `request-changes` means revise the artefact (the canvas live-reloads it)
  and keep the loop going.

**Always respond in the canvas**, then keep listening:

```bash
node scripts/plan-canvas.js await <file> --reply "Reworked NFR-003 to 150ms, matching AC-014. Take a look."
```

Silence in the chat panel is indistinguishable from a broken canvas to the
reviewer — answer there, not only in the terminal summary.

**End** when review concludes: `node scripts/plan-canvas.js end <file>`.

## Mapping the verdict into this engine's governance chain

A canvas verdict is not the end of the workflow — it is one governance event
that other skills in this phase consume:

1. **`approve`** → record the event in `09-sign-off-ledger` (reviewer
   identity, artefact path, timestamp, and the artefact's baseline
   version), and update `05-formal-review-gates`' gate-status record for
   this artefact to `passed`.
2. **`request-changes`** with one or more `annotation` items → each
   annotation becomes a line item the agent must resolve before the next
   review cycle. If the artefact is already baselined, route the change
   through `07-baseline-delta` and `06-change-impact-analysis` rather than
   editing the baseline in place.
3. A `request-changes` verdict that conflicts with an already-`accepted`
   ADR or a frozen NFR threshold is itself a decision moment — capture it
   with the `05-architecture-decision-records` skill (see that skill's
   trigger-phrase detection) rather than silently overriding the baseline.

## Diagrams (Mermaid)

When the artefact under review includes a flow, sequence, state machine, or
dependency graph (traceability chains, CCB approval flow, baseline delta
propagation), author it as a fenced ` ```mermaid ` block rather than ASCII
art — the canvas renders it as a themed diagram the reviewer can point at
directly.

## Rules

- Markdown artefacts render in the canvas's built-in template (including
  Mermaid blocks); `.html` deliverables render as-is with the annotation
  layer injected.
- Edit the artefact file to revise — the canvas live-reloads on save. Never
  re-run `open` to refresh.
- `{"status": "ended", "endedBy": "user"}` means the reviewer closed the
  review: stop polling, deliver remaining updates in chat, and do not
  reopen without the reviewer asking to resume.
- The server is loopback-only (`127.0.0.1:4517`) and exits after 30 idle
  minutes — the same safety boundary ECC ships. No project artefact leaves
  the reviewer's machine through this mechanism.
- Never treat an `approve` verdict recorded through this skill as a
  substitute for the accountable authority named in `05-formal-review-gates`'
  decision-rights table — the canvas records *who* clicked approve; it does
  not itself confer approval authority. If the reviewer is not the named
  gate authority, route the verdict to them for countersignature before
  updating the ledger.

## Anti-Patterns

- Polling with a timeout loop instead of leaving a plain `await` running.
- Ending the agent's turn with no `await` listening while a review is open.
- Reading feedback and answering only in the terminal instead of the canvas.
- Treating a `request-changes` verdict on a baselined artefact as license to
  edit the baseline directly instead of routing through `07-baseline-delta`.
- Recording an `approve` verdict in `09-sign-off-ledger` without confirming
  the reviewer is the named decision authority for that gate.

## References

- ECC original: `skills/plan-canvas/SKILL.md`, `docs/design/plan-canvas.md`,
  `scripts/plan-canvas.js`, `scripts/lib/plan-canvas/*.js`,
  `scripts/lib/loopback-guard.js`, `scripts/hooks/plan-canvas-pending.js`,
  `scripts/hooks/plan-canvas-sessions.js`
  (C:\Users\Peter\Downloads\ECC-main).
- This engine's vendored copy: `scripts/plan-canvas.js`,
  `scripts/lib/plan-canvas/*.js`, `scripts/lib/loopback-guard.js`,
  `hooks/plan-canvas-pending.js`, `hooks/plan-canvas-sessions.js`,
  `hooks/hooks.json` (wiring), `tests/plan-canvas/*.test.js`,
  `tests/scripts/plan-canvas.test.js`, `tests/hooks/plan-canvas-*-hook.test.js`.
- This engine: `05-formal-review-gates/SKILL.md` (gate criteria and decision
  rights this skill's verdicts feed), `09-sign-off-ledger/SKILL.md` (where
  `approve` verdicts are recorded), `07-baseline-delta` and
  `06-change-impact-analysis` (where post-baseline `request-changes` route).
