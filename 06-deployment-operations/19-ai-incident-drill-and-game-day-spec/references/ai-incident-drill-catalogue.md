# AI Incident Drill & Game-Day Catalogue

Pre-defined drill scenarios used to validate the AI incident response runbook end-to-end. Cadence: **quarterly minimum** for SEV-1 drills; **monthly** for tabletop walkthroughs.

Each drill specifies: scenario, injection method, target detection signal, target detection time, target mitigation time, target customer-comms time, success criteria, failure modes that block sign-off.

---

## Drill 1 — Hallucination spike

**Scenario.** Faithfulness eval score on a major feature drops from 0.92 baseline to 0.71 over a 4-hour window after a prompt update is promoted.

**Injection method.** Stage on a non-prod tenant by deploying a degraded prompt and replaying production-shaped traffic against it; or in prod by intentionally promoting a known-degraded prompt to 1% of canary traffic with full eval gates configured to detect.

**Target detection signal.** Hallucination-rate burn-rate alert fires within `≤ 15 min` of the burn threshold being crossed.

**Target detection time.** ≤ 15 min from threshold cross.
**Target mitigation time.** ≤ 30 min (prompt rollback + eval re-run).
**Target customer-comms time.** SEV-2 status page entry within 45 min.

**Success criteria.**
- On-call detects within 15 min.
- Rollback executed cleanly via documented kill-switch path.
- Eval re-run passes prior to status-page resolution entry.
- Postmortem authored within 5 business days.

**Failure modes that block sign-off.** Alert fires but no on-call response within 30 min; rollback procedure ambiguous; eval re-run not in CI; status page entry uses forbidden language.

---

## Drill 2 — Prompt injection via tool output

**Scenario.** A malicious payload is embedded in a third-party tool response (e.g. a CRM record body) that the agent retrieves. The payload attempts to escalate the agent's action scope.

**Injection method.** Plant a record in a sandbox tool with a known payload. Trigger the agent loop. Validate the input-filter blocks; validate that even if it passes, the action gate rejects the escalated action.

**Target detection signal.** Action-gate refusal logged + red-team monitor alert.

**Target detection time.** Detection at the action gate (synchronous, must be ≤ 1 s).
**Target mitigation time.** N/A — the gate must block in real time.
**Target follow-up time.** Postmortem in 5 business days; red-team test added.

**Success criteria.**
- Input filter or action gate refuses the escalated request.
- Refusal is logged with full trace.
- Red-team CI test is added to permanent suite within 5 business days.
- Affected tenant is notified of a near-miss with no customer impact.

**Failure modes.** Action executed; refusal logged but no alert; no test added.

---

## Drill 3 — Cost runaway

**Scenario.** A single tenant's agent enters a long loop and consumes 50x normal tokens in 1 hour.

**Injection method.** Stage in a sandbox tenant by giving the agent a task it cannot solve and letting it retry without step budget. (Verify that production has step + token + wallclock + cost budgets enforced.)

**Target detection signal.** Cost anomaly alert per tenant fires within `≤ 10 min` of normal-baseline breach.

**Target detection time.** ≤ 10 min.
**Target mitigation time.** ≤ 5 min (automated throttle / kill-switch).
**Target customer-comms time.** SEV-3 follow-up to affected tenant within 1 business day.

**Success criteria.** Hard ceiling triggers automatically; tenant is not charged for the runaway; explanation issued.

**Failure modes.** Hard ceiling missing; no per-tenant cost alert; customer charged.

---

## Drill 4 — Foundation-model provider outage

**Scenario.** Primary LLM provider returns 503 for ≥ 5 min for the affected region.

**Injection method.** In staging, configure provider adapter to return 503 for `[provider, region]`. In prod, run a controlled chaos test against a single canary slice.

**Target detection signal.** Provider error-rate alert; automatic failover engages.

**Target detection time.** Failover engages within 30 s of sustained error rate.
**Target mitigation time.** Customer-facing latency restored within 1 min of failover.
**Target customer-comms time.** Status-page entry within 15 min noting failover.

**Success criteria.** Failover engages; secondary provider model maintains eval baseline; status page entry posted; no SEV-1 declared.

**Failure modes.** No failover configured; secondary model lower eval than baseline; failover engaged but stuck on secondary after provider recovers.

---

## Drill 5 — Retrieval index poison / drift

**Scenario.** A bad ingestion run replaces a critical knowledge-base segment with corrupted documents.

**Injection method.** Stage by intentionally running a corrupt ingestion batch on a sandbox KB.

**Target detection signal.** Retrieval-relevance eval drops; or citation-accuracy alert fires; or scheduled differential against last-known-good snapshot flags drift.

**Target detection time.** ≤ 2 h (most retrieval issues are caught by scheduled differential, not real-time).
**Target mitigation time.** ≤ 30 min (pin to prior snapshot).
**Target customer-comms time.** SEV-2 if customer-visible; otherwise SEV-3 with monthly trust report.

**Success criteria.** Differential detected; snapshot rollback procedure known; pinned snapshot served while rebuild runs.

**Failure modes.** No snapshot-pinning procedure; rebuild blocks serving; customer impact during rebuild.

---

## Drill 6 — Agent irreversible-action incident

**Scenario.** The agent executes an irreversible action (e.g. issues a refund, sends an email, modifies an external system) that should have been gated.

**Injection method.** In staging, configure a tool flagged irreversible but with the gate disabled; observe whether the agent loops detect the gate is missing. In prod, this drill is performed as a tabletop only — never staged live.

**Target detection signal.** Action-audit log + post-action verification.

**Target detection time.** ≤ 1 h via the post-action verification job.
**Target mitigation time.** N/A — the action is irreversible. Compensation: customer outreach, regulator notification if applicable.
**Target customer-comms time.** Direct-to-tenant within 2 h; status-page entry within 4 h.

**Success criteria.** Compensation playbook executes (customer outreach, regulator notification if needed, internal blameless review); ADR is updated to require the gate going forward; red-team test added.

**Failure modes.** No compensation playbook; no regulator-notification flow; no ADR update.

---

## Drill 7 — Cross-tenant data bleed (most serious)

**Scenario.** A prompt or retrieval bug causes tenant A's data to surface in tenant B's response.

**Injection method.** Tabletop only on production. May be staged in staging by intentionally mis-tagging a vector chunk.

**Target detection signal.** Cross-tenant isolation regression test fails; or customer report; or proactive monitor.

**Target detection time.** Continuous monitor must run.
**Target mitigation time.** ≤ 30 min full feature kill-switch.
**Target customer-comms time.** SEV-1 within 60 min to affected tenants; regulator notification within `[24 / 72]` h depending on jurisdiction.

**Success criteria.** Full feature kill; isolation regression test added; SEV-1 process executed; regulator notification flow executed.

**Failure modes.** Slow kill-switch; no isolation regression test; regulator notification flow not exercised.

---

## Tabletop walkthrough (monthly)

Each month, the on-call team walks through a single drill scenario as a paper exercise (no injection). Time-boxed to 45 min. Required participants: on-call engineer, incident commander, comms lead, customer-success lead, security lead. Output: 1-page tabletop report tracked alongside the drill catalogue.

## Quarterly live drill (production-safe)

Each quarter, run at least one **live** drill from the catalogue against a controlled prod slice. Drills 1, 3, 4, 5 are live-safe with the right staging. Drills 2, 6, 7 are tabletop only in prod.

## Drill scoring

| Pass | All success criteria met. |
| Conditional | Success criteria met but at least one finding requires action. |
| Fail | Any failure mode triggered. |

A fail blocks any non-critical AI feature promotion for the affected stack until remediated.

## Post-drill outputs

- Trace bundle from the drill.
- 1-page report: scenario, timing measured vs targets, success/conditional/fail, action items, owner, due-date.
- Updates to the AI Incident Response Runbook and to the Red-Team Test Plan as warranted.

## Annual reset

Once a year, review the catalogue end-to-end. Retire drills the system has comfortably passed three times running; add drills for new failure classes observed in the wild.
