# AI Incident Communication Language Patterns

Responsible-disclosure language for AI incidents. The wrong word costs trust; the right word de-escalates and protects without misleading.

## Core principles

1. **Factual before reassuring.** State what happened first; state what we did second; reassure last, and only with evidence.
2. **Pre-empt the AI-specific fear.** For every AI incident the customer wonders "did my data get into someone else's response or into a model's training?" Answer this proactively even when the answer is no.
3. **Concrete numbers, narrow scopes.** "12 tenants, between 14:02 and 14:48 UTC" beats "some customers, earlier today."
4. **Single source of truth.** Status page → trust portal → customer emails all reflect the same facts. Discrepancies destroy trust.
5. **Speak only to confirmed facts.** Use "investigating" until RCA class is confirmed.

## What to say / what NOT to say

| Situation | Say | Don't say |
|---|---|---|
| Model returned ungrounded answer | "the feature returned an answer without the source citation we require" | "the model hallucinated", "the AI lied", "the model lost its mind" |
| Model regression after release | "a model update was rolled back after our evaluation suite flagged a regression" | "the new model was broken", "the upgrade was a disaster" |
| Prompt injection succeeded | "an input-handling issue was identified" | "we were jailbroken", "the model was tricked", "attacker bypassed safety" |
| Agent took unexpected action | "agent actions are paused while we investigate a behaviour anomaly" | "the agent went rogue", "the AI acted on its own", "we lost control" |
| Cost runaway | "higher-than-expected token usage was detected and bounded" | "the model ran away with itself", "we got hit with an unexpected bill" |
| Cross-tenant data concern (confirmed safe) | "no customer data crossed between tenants; isolation controls held" | "we don't think anything leaked", "we are still investigating whether data was exposed" — when you actually have evidence isolation held |
| Cross-tenant data concern (under investigation) | "we are running cross-tenant isolation verification; preliminary checks indicate no exposure" | "no data was exposed" (until verified) |
| Vendor outage caused incident | "an upstream provider experienced degraded service; our system failed over as designed" | name the vendor publicly, blame the vendor |
| Eval drift caught proactively | "our internal evaluation system detected and prompted a precautionary rollback" | "we caught a problem before it hurt anyone" — sounds boastful |

## The mandatory AI-incident answer line

Every customer-facing comm for SEV-1 and SEV-2 must include one of:

- **Confirmed safe:** "We have verified that no customer data crossed between tenants and no customer data has been used to update or train any model."
- **Verifying:** "We are running our isolation verification suite and will confirm the result by `[time]`."
- **Confirmed impact:** "We have identified that `[scope]` was affected; affected customers have been contacted directly with details and next steps."

This line is non-negotiable for SEV-1 and SEV-2 AI incidents. It addresses the question the customer is silently asking.

## Tense and voice

- Use past tense for closed facts ("the issue was detected"), present continuous for ongoing work ("we are validating"), future for commitments ("we will publish a postmortem within `[N]` business days").
- Use active voice when "we" did something good ("we rolled back"). Use passive only when the actor is genuinely unknown or unhelpful to name.

## Length

- SEV-1 initial: ≤ 4 sentences.
- SEV-1 update: ≤ 6 sentences.
- SEV-1 resolution: ≤ 8 sentences + link to postmortem.
- Postmortem: as long as needed, but written for a non-engineer reader.

## Forbidden language list

- "We sincerely apologise for any inconvenience." (Use only with concrete remediation alongside.)
- "Out of an abundance of caution…" (Overused; drains credibility.)
- "We take security very seriously." (Empty.)
- "The AI made a mistake." (Anthropomorphic; misleading about responsibility.)
- "Black box." (Implies we don't understand our own system.)
- Any phrasing that suggests the AI has agency over what happened. The system is operated by humans and the company is accountable.

## Multilingual adaptations (Africa context)

For tenants in francophone, lusophone, anglophone, Swahili-speaking markets, provide translated SEV-1 entries in the customer's primary language within 2 hours of the initial notification. The translation must be reviewed by a native speaker, never machine-translated for SEV-1.

## Regulator language vs customer language

Regulator notifications (EU AI Act Art. 73, GDPR Art. 33, ODPC, NDPR, POPIA) demand more technical detail than customer comms. See the regulator notification template. The two must be factually consistent; the regulator version is a superset of the customer version, never a contradicting set.
