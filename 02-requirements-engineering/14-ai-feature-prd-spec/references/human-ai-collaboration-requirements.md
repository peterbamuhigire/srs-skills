# Human-AI Collaboration Requirements

Parent skill: [14-ai-feature-prd-spec](../SKILL.md). Load this reference when an AI feature
recommends, drafts, ranks, classifies or acts alongside a person, and the SRS must state how the
person stays informed, in control and appropriately reliant. It extends the
[AI system and human-control contract](ai-system-human-control-contract.md) with requirement
patterns and test oracles. Interaction and visual treatment of these requirements belong to the
design engine (`skills/04-web-and-ui-design/ai-agent-ux`); this file states what must be true and
how it is verified.

## 1. Declare the collaboration mode per AI function

The mode fixes who decides, and therefore which requirements below are mandatory.

| Mode | Who decides | Mandatory requirement groups | Typical example |
|---|---|---|---|
| Assist | Human; AI offers optional help | Disclosure, dismissal, feedback | Suggested reply text |
| Augment | Human, informed by AI output | + explanation, confidence, anchoring control | Credit-risk score shown to a loan officer |
| Cooperate | Split: AI completes bounded sub-tasks, human reviews | + review queue, override, handoff | AI pre-codes invoices; accountant approves |
| Delegate | AI acts within a policy; human monitors | + preview for irreversible actions, global pause, audit, rollback | Auto-reorder of stock below threshold |

Decision rule: if the mode is not declared, raise `[CONTEXT-GAP: collaboration mode for <function>]`
and do not write the function's requirements. Moving a function to a more autonomous mode is a
change request with its own risk assessment, not a configuration tweak.

## 2. Requirement patterns with fit criteria

Rewrite each pattern with the project's actors, thresholds and identifiers. Every requirement
keeps a deterministic oracle.

**Capability disclosure**
- HAI-001: The system shall state, at the point of first use and on demand, what the AI function
  does, what data it uses, and at least two named limitations.
  Oracle: content review against the model card; first-use screen present in 100% of entry points.
- HAI-002: The system shall label AI-generated or AI-modified content wherever it is displayed,
  exported or sent. Oracle: every export and outbound-message fixture carries the label.

**Explanation**
- HAI-010: For each Augment-mode output the system shall provide a short reason naming the top
  contributing factors in domain language, with a deeper view available on request.
  Oracle: explanation present for 100% of outputs in the evaluation set; factor names come from the
  approved glossary.
- HAI-011: Explanations shall not expose other users' personal data or restricted model internals.
  Oracle: privacy test cases with seeded personal data return no leakage.
Decision rule: default to a short, partial explanation; mandate deeper detail only where users
must justify a decision to someone else (auditor, regulator, patient, customer). Long
explanations raise perceived complexity and can lower appropriate trust.

**Confidence and uncertainty**
- HAI-020: Where the model supports calibrated scores, the system shall present confidence in the
  approved categorical bands (for example High / Medium / Low) with a stated user action per band.
  Oracle: calibration report shows observed accuracy per band within the agreed tolerance on the
  held-out set.
- HAI-021: Where no calibration evidence exists, the system shall not display numeric confidence
  and shall instead show evidence, sources or alternatives. Oracle: UI inventory has no percentage
  confidence on uncalibrated outputs.
- HAI-022: Below the abstention threshold the system shall decline to answer and route to the
  fallback path. Oracle: evaluation-set items below threshold produce the fallback, not an answer.

**Control, correction and override**
- HAI-030: The user shall be able to accept, edit, reject or dismiss every AI suggestion in no more
  than one action from where it appears. Oracle: task walkthrough per surface.
- HAI-031: A human override shall take effect immediately, be recorded with actor, time, original
  AI output, final value and optional reason, and never be silently reverted by a later AI run.
  Oracle: audit-log fixture; regression test re-running the AI on overridden records.
- HAI-032: Delegate-mode functions shall provide a global pause that stops new AI actions within
  the agreed time (for example 60 seconds) without losing queued work. Oracle: operational test.
- HAI-033: Irreversible or externally visible actions shall require preview and explicit
  confirmation of the exact action, recipient and amount. Oracle: no such action executes in test
  logs without a confirmation event.

**Appropriate reliance**
- HAI-040: For Augment-mode decisions with material consequence, the system shall support a
  judge-first flow in which the user records an initial judgement before the AI recommendation is
  revealed. Oracle: configuration test; flow enabled for the listed decision types.
- HAI-041: The system shall record whether each decision agreed with the AI and whether the AI was
  later found correct, so that over-reliance (accepting wrong AI output) and under-reliance
  (rejecting correct AI output) rates can be reported per role monthly.
  Oracle: reliance report generated from logged fixtures.
- HAI-042: Acceptance targets shall be set on appropriate reliance, not on raw acceptance rate.
  Oracle: the success-metric table contains no "increase AI acceptance rate" target without an
  accuracy condition.

**Error recovery and handoff**
- HAI-050: When the AI fails, times out or abstains, the user shall be able to complete the task
  manually with any work already done preserved. Oracle: fault-injection test per function.
- HAI-051: Escalation to a human agent shall transfer the conversation, AI outputs shown, and user
  inputs so the user does not repeat information. Oracle: handoff fixture; receiving agent view
  contains the full context.
- HAI-052: Users shall be able to report a wrong or harmful output from the output itself; reports
  reach a named owner queue with a response target. Oracle: report fixture lands in queue with
  timestamp and output ID.

**Persona, sensitive disclosure and inclusion**
- HAI-060: The AI shall not claim to be human, claim feelings, or use affection or urgency to
  influence decisions. Oracle: red-team prompt set (see `05-testing-documentation/05-ai-red-team-test-plan`).
- HAI-061: When a user volunteers sensitive personal data (health, finances, identity numbers,
  family or emotional circumstances) beyond what the task needs, the system shall not retain it
  beyond the session unless the user consents, and shall say so. Oracle: retention test on seeded
  sensitive inputs.
- HAI-062: AI output shall be exposed to assistive technology with a clear start and end of the
  response and labelled copy, edit and rate controls. Oracle: screen-reader test on the supported
  platforms (WCAG 2.2 AA conformance for the containing UI).
- HAI-063: For each supported language (for example English, Luganda, Swahili) the evaluation set
  shall include native-speaker cases, and quality thresholds shall be met per language, not only
  on aggregate. Oracle: per-language evaluation report.

## 3. Decision rules

| Condition | Required response | Failure avoided |
|---|---|---|
| Output influences credit, health, employment, legal or safety decisions | Augment mode at most; HAI-010, HAI-040, HAI-041 mandatory | Automation bias and unaccountable decisions |
| Model confidence is uncalibrated | HAI-021 applies; no percentages | False precision |
| Time pressure is part of the job (tellers, triage, dispatch) | Short explanation, categorical confidence, one-action override | Explanation overload and rubber-stamping |
| EU users are in scope | Map disclosure requirements to AI Act Article 50 and confirm with counsel | Non-compliant disclosure |

## 4. Anti-patterns and corrections

- "The AI shall be transparent." Correction: name the explanation content, trigger and oracle.
- Success metric "70% of suggestions accepted." Correction: measure over- and under-reliance.
- Confidence percentage from a language model's self-report. Correction: calibrated bands or none.
- Override stored only in the UI state. Correction: HAI-031 audit record and non-reversion test.
- Friendly human persona to raise engagement. Correction: HAI-060 and a neutral assistant voice.

## 5. Worked example (original)

A Mbarara SACCO adds an AI loan-screening aid. Mode: Augment. The loan officer enters an initial
view (approve / refer / decline) before seeing the AI band (HAI-040). The band shows High / Medium /
Low repayment likelihood with the three strongest factors, such as "mobile-money inflows fell 40% in
the last 90 days" (HAI-010, HAI-020); calibration is checked quarterly on closed loans. Any
officer decision against the band requires a one-line reason (HAI-031). The monthly reliance report
flags an officer who accepts 98% of Low bands later shown to be wrong (HAI-041). Member-facing
letters never say "the AI decided" because the officer decides.

## Evidence/currentness

Access date 2026-09-24. Verified against current official guidance: Microsoft HAX Toolkit, 18
Guidelines for Human-AI Interaction (capabilities, efficient correction and dismissal, explaining
why, global controls, notifying of changes); Google PAIR People + AI Guidebook, chapters Mental
Models, Explainability + Trust (categorical, N-best and numeric confidence; partial explanations),
Feedback + Control, Errors + Graceful Failure; W3C WCAG 2.2 Recommendation (12 Dec 2024). EU AI Act:
secondary legal summaries (Gibson Dunn, Latham & Watkins, 2026) report Article 50 transparency
duties applying from 2 Aug 2026 and high-risk (Annex III) obligations deferred to 2 Dec 2027 by the
2026 Digital Omnibus; the Official Journal text was NOT_ASSESSED — confirm with counsel. Apple HIG
"Generative AI" page exists; its detailed wording was NOT_ASSESSED (page not machine-readable).

Sources: Wu & Liang (eds.) (2026) *Human-AI Interaction and Collaboration*, Cambridge University Press; Amershi et al. (2019)
Guidelines for Human-AI Interaction (CHI); Google PAIR (2021) *People + AI Guidebook*.
