# AI Incident Customer Notification Templates

Per-severity, per-tenant notification language. Use the matching template for the declared severity. Plug in only the bracketed `[...]` values. Never invent technical detail that hasn't been confirmed by the incident commander.

---

## SEV-1 — broad customer impact, immediate notification (≤ 60 min)

**Subject:** Service incident affecting your `[product-or-feature]` — [DATE T+0]

> Hi `[Customer Name]` team,
>
> At `[HH:MM UTC]` today we detected an issue affecting `[feature]` for some `[Product]` customers including your tenant. Specifically: `[one-line factual symptom — e.g. "the assistant began returning answers without citations" or "agent actions are paused"]`.
>
> Current status: `[Investigating / Mitigated / Resolved]`. We have `[concrete mitigation taken — e.g. "rolled back the model release", "engaged read-only mode for affected feature", "paused agent actions and queued pending tasks for human review"]`.
>
> Your impact window: `[HH:MM]` to `[HH:MM]` (UTC). Affected scope on your tenant: `[users / workflows / records]`. No `[customer data / model training data / payment data]` was exposed.
>
> What we are doing next: `[next concrete step + ETA]`. We will send the next update by `[HH:MM]`.
>
> Status page: `[link]`. If you have urgent questions, reply to this email or reach your CSM at `[contact]`.
>
> `[Name]`, `[Title]`, on behalf of `[Company]`

---

## SEV-2 — partial / degraded impact

**Subject:** Degraded `[feature]` performance — your tenant may be affected

> Hi `[Customer Name]` team,
>
> Between `[HH:MM]` and `[HH:MM]` UTC, `[feature]` was operating in a degraded state. Symptom: `[factual symptom]`. Root cause has been identified as `[high-level class — e.g. "a regression in model behaviour following a routine update", "a retrieval index drift"]` and the mitigation is `[mitigation]`. The feature is now `[Restored / Restored with fallback model / Running in supervised mode]`.
>
> Your tenant: `[users / workflows]` likely affected. We have logged the trace IDs for your records (available on request).
>
> A detailed postmortem will be published within `[5 / 10]` business days at `[link]`.
>
> `[Name]`, `[Title]`

---

## SEV-3 — localized / single-tenant impact

**Subject:** A small `[feature]` issue we want you to know about

> Hi `[Customer Name]`,
>
> Earlier today we identified that `[feature]` returned `[unexpected output / refused valid requests / produced an ungrounded answer]` for a small number of requests on your tenant between `[HH:MM]` and `[HH:MM]` UTC.
>
> This was caused by `[brief factual class]`. We have `[action — e.g. "pinned the previous prompt version for your tenant", "added the failing case to our regression suite"]`. No further customer action is required.
>
> If you would like the affected trace IDs or a 1:1 walkthrough, reply to this email.
>
> `[Name]`, `[Title]`

---

## SEV-4 — informational / near-miss

For high-trust customers and regulated buyers. Often delivered in the next monthly trust report rather than a same-day email. Templates omitted; copy SEV-3 with the lead "We want to flag a near-miss that did not affect production."

---

## Per-tenant customisation rules

1. **Always identify the actual impact window for that tenant**, not the global window. Most multi-tenant AI incidents affect only a slice.
2. **Always state what data exposure did NOT occur**, in plain language. For AI incidents the customer's first fear is "did the model leak my data into someone else's response or into training" — answer it pre-emptively.
3. **Never name a model provider unless legally required.** Use "an underlying model component."
4. **Never name a competing customer.** Use "a small number of tenants."
5. **Never speculate on root cause before it is confirmed.** Use "the issue is under active investigation" until you have a confirmed RCA class from the taxonomy doc.
6. **Escalate to the customer's designated security/compliance contact** in parallel for SEV-1 and SEV-2 in regulated industries (financial services, insurance, healthcare, public sector).

## Escalation matrix

| Severity | First notification (target) | Second update | Final / RCA |
|---|---|---|---|
| SEV-1 | ≤ 60 min | every 2 h until mitigated | within 5 business days |
| SEV-2 | ≤ 4 h | every 8 h | within 10 business days |
| SEV-3 | within 1 business day | n/a | with monthly trust report |
| SEV-4 | with monthly trust report | n/a | with monthly trust report |

## Channels (in order of priority)

1. Designated tenant primary contact + designated security contact (email).
2. In-product banner (if affected user is currently using the feature).
3. Status page entry tagged to feature.
4. CSM follow-up call for SEV-1 within 24 h.
5. Trust portal incident page update for SEV-1 and SEV-2.

## Anti-patterns

- Sending a generic all-customer email when only 4 tenants were affected.
- Burying the impact window inside marketing language.
- "Out of an abundance of caution we have…" — overused, drains trust.
- Claiming resolution before the eval-gated re-promotion completes.
- Naming the foundation-model provider, the failing prompt version, or internal staff in customer-facing comms.
