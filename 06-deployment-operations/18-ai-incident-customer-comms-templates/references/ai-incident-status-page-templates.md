# AI Incident Status Page Templates

Status page entries are short, factual, time-stamped, and updated until resolution. One template per AI failure class. All entries must use UTC timestamps and tag the affected feature(s).

---

## Hallucination spike

**Initial entry**
> `[HH:MM UTC]` — Investigating: `[feature]` may be returning answers with reduced citation accuracy for some customers. We have placed the feature into supervised mode while we investigate.

**Mitigation entry**
> `[HH:MM UTC]` — Mitigation in place: we have rolled back the most recent prompt update and re-enabled grounding. We are running our eval suite before lifting supervised mode.

**Resolution entry**
> `[HH:MM UTC]` — Resolved. Eval suite has confirmed restoration of grounded-answer rate above our service-level objective. A detailed postmortem will follow within `[N]` business days.

---

## Prompt drift / model regression

**Initial entry**
> `[HH:MM UTC]` — Investigating: `[feature]` is producing responses that differ in tone or accuracy from expected behaviour. The underlying model release has been rolled back and we are validating.

**Resolution entry**
> `[HH:MM UTC]` — Resolved. The prior model and prompt configuration have been pinned. The eval suite has confirmed return to baseline behaviour. Postmortem in `[N]` business days.

---

## Prompt injection / jailbreak

**Initial entry — be vague intentionally**
> `[HH:MM UTC]` — Investigating: an input-handling issue was identified in `[feature]`. As a precaution we have enabled stricter input filtering and restricted high-risk tools.

(Do not detail the attack vector publicly. Detail goes only into the trust-portal incident page and the regulator notification.)

**Resolution entry**
> `[HH:MM UTC]` — Resolved. Additional input-handling controls have been deployed and validated against our red-team test suite.

---

## Tool / agent action incident

**Initial entry**
> `[HH:MM UTC]` — Investigating: agent-initiated actions in `[feature]` have been paused while we investigate a behaviour anomaly. Pending actions are queued for human review.

**Mitigation entry**
> `[HH:MM UTC]` — Mitigation: irreversible-action gating has been tightened. Actions are running in supervised mode (each action approved by a human before execution).

**Resolution entry**
> `[HH:MM UTC]` — Resolved. Eval and red-team suites have been re-run and the agent has returned to autonomous operation under tightened action policy. Affected customers have been notified directly.

---

## Cost runaway

**Initial entry** (only if a customer-facing throttle was triggered)
> `[HH:MM UTC]` — Some customers may be seeing rate-limited responses from `[feature]`. We have engaged a precautionary cost ceiling while we investigate higher-than-expected token usage.

**Resolution entry**
> `[HH:MM UTC]` — Resolved. Standard limits restored. No customer was charged for the affected period.

---

## Retrieval drift / index issue

**Initial entry**
> `[HH:MM UTC]` — Investigating: `[feature]` is returning citations that may be stale or incomplete. We have pinned the retrieval index to the previous known-good snapshot.

**Resolution entry**
> `[HH:MM UTC]` — Resolved. The retrieval index has been rebuilt and validated. Affected answers issued during the window are re-runnable on request.

---

## Foundation-model provider outage

**Initial entry**
> `[HH:MM UTC]` — Investigating: an upstream model provider is experiencing degraded service. `[feature]` has automatically failed over to our secondary provider. You may notice differences in response style during the failover.

**Resolution entry**
> `[HH:MM UTC]` — Resolved. The primary provider has restored service and `[feature]` has returned to its standard model. There was no data exposure during failover.

---

## Eval-drift detected (proactive — no customer impact yet)

**Initial entry**
> `[HH:MM UTC]` — Maintenance: we have detected a drift in our internal evaluation scores for `[feature]` and are deploying a precautionary mitigation. No customer impact has been observed. Updates will follow if any customer-visible action is required.

---

## Tone, length, and time

- Entries ≤ 350 characters wherever possible.
- Update every 30 min for SEV-1 (during initial window), every 2 h afterwards.
- Use UTC. Mention the local timezone (e.g. Africa/Nairobi) only on a duplicate per-region status page.
- Always say "investigating" before "identified" and "mitigated" before "resolved".
- Never use the words: catastrophic, exposed, leaked, compromised, hack, hacker, breach (unless the legal team has authorised a breach notification).
