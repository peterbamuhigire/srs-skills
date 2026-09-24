# AI Evaluation Set, Graduation Gate and Failure Behaviour Requirements

Parent skill: [AI feature PRD spec](../SKILL.md). Load at Step 2 (per-FR
clauses) and Step 7 (eval acceptance gates). The seven AI clauses already name
thresholds such as "factuality >= 0.92 on golden-200". This reference specifies
what makes that number trustworthy: how the evaluation set is built and
governed, when a prototype may become a production requirement, what the
product does when the model fails, and which business rules must never be left
for a model to infer.

Neighbours: data sourcing and knowledge-base content belong to
`15-ai-data-and-knowledge-base-spec`; agent actions to
`16-ai-agent-feature-prd-spec` and `17-ai-agent-action-catalogue-spec`; the
evaluation harness implementation belongs to engineering. User-facing
override, explanation, reliance and handoff requirements (HAI-nnn) live in
[human-AI collaboration requirements](human-ai-collaboration-requirements.md);
Section 5 below supplies the system-side failure classes those HAI
requirements depend on, and the per-language slices in Section 4 satisfy its
per-language evaluation oracle.

## 1. Non-AI baseline and required uplift

Before any AI-FR is accepted, record:

| Field | Content |
|---|---|
| Current method | How the task is done today, including rules, templates or manual work |
| Optimised non-AI option | The best deterministic improvement available (validation rules, templates, search, a form redesign) and its measured or estimated result |
| Baseline metric | Same unit as the AI metric, measured on the same case set |
| Required uplift | The minimum improvement over the optimised non-AI option that justifies the AI's cost and risk, agreed with the sponsor before evaluation runs |

Rule: an AI-FR whose evaluated result does not beat the optimised non-AI option
by the required uplift is withdrawn or returned to discovery. The uplift is set
before results are seen; moving it afterwards is recorded as a sponsor decision.

## 2. Rules the model must not be left to infer

AI components handle common patterns well and domain specifics badly. Any rule
below is written as a deterministic requirement enforced outside the model
(validation, policy layer, tool contract), and the model's output is checked
against it:

- Money and tax rules: rates, rounding, thresholds, approval limits, statutory
  deductions (for Uganda: VAT, withholding tax, PAYE, NSSF) as configured data.
- Eligibility and authorisation: who may see, approve, or trigger what.
- Identity and verification steps required by law or policy.
- Integration contracts: identifiers, formats and idempotency with named
  external systems.
- Irreversible actions: always behind explicit human confirmation.

Acceptance: for each rule, a test in which the model output violates the rule
and the system rejects, corrects, or escalates it.

## 3. Prototype graduation gate

A prototype is disposable. It becomes the basis for production requirements
only when all of the following are recorded:

| Signal | Measurable condition (set per project) |
|---|---|
| Stable requirements | No new must-have need emerged in the last K user sessions |
| Value signal | Repeat or unprompted use by the target segment, not novelty praise (evidence rung E3 or higher in the PRD risk register) |
| Predictable behaviour | Failure rate on the evaluation set at or below a stated ceiling, and failures fall into catalogued classes |
| Defined success | Each AI-FR has a metric, threshold and case set agreed with the owner |

If failures on realistic inputs are still frequent or unclassified, the work is
prompt, data and design iteration, not production engineering. Keep it in
discovery.

### Handoff pack (mandatory inputs to this skill)

1. Reference prototype, with the model, version and configuration it used.
2. Evaluation set: representative inputs with expected outputs or grading
   rubric (Section 4).
3. Failure-mode catalogue: each known failure with example input, frequency on
   the evaluation set, and user impact.
4. Instruction and retrieval strategy: the prompts, retrieval settings, and
   tool definitions that produced the best results, versioned.
5. Known limits: input size, languages, formats and volumes beyond which
   quality was not measured.

Missing items are `[CONTEXT-GAP]`; the affected AI-FR stays `[DRAFT]`.

## 4. Evaluation set requirements

Treat the evaluation set as a controlled requirements artefact with its own
identifier, version and owner.

| Property | Requirement | Verification |
|---|---|---|
| Slices | Cases are grouped into named slices: common, boundary, adversarial, should-abstain, and each material user segment, language or channel | Slice manifest with counts |
| Per-slice thresholds | Every slice has its own pass threshold; an aggregate score may not hide a failing slice | Report shows per-slice results |
| Size rationale | Each slice's size is justified by the decision it supports and the precision needed; a small starter set (tens of cases) is acceptable for early gating only if labelled as such | Rationale recorded against each slice |
| Provenance | Every case records source (production sample, synthetic, expert-written), date, and consent or lawful basis for any personal data | Case metadata audit |
| Expected output form | Each case declares its oracle type: exact match, structured-field match, reference with tolerance, or rubric | Oracle type field on every case |
| Labelling protocol | Rubric cases are labelled by at least two qualified reviewers independently; disagreement is adjudicated and the agreement rate is recorded | Agreement report; adjudication log |
| Model-as-judge | A judge model may grade only after its grades agree with adjudicated human grades at or above a stated rate on a calibration subset; the judge's model and version are pinned | Calibration report |
| Separation | Cases used to tune prompts or retrieval are held apart from the acceptance split; acceptance-split cases are never shown to the tuning loop | Split manifest; access log |
| Regression growth | Every production failure that reaches a user and is confirmed becomes a new case within a stated period | Case IDs linked to incident IDs |
| Re-run triggers | Full re-run on any change to model, model version, prompt, retrieval index schema, tool contract, or guardrail policy | Release checklist entry |

Localised slices matter. A Ugandan customer-support assistant needs slices for
English, Luganda and code-switched messages, for mobile-money reference
formats, and for low-bandwidth truncated inputs; a single English aggregate
would pass while the most common real traffic fails.

## 5. Failure and fallback behaviour

Every AI-FR carries a degradation table. Each row is a testable requirement.

| Failure class | Detection | User-visible behaviour | System behaviour | Logged event |
|---|---|---|---|---|
| Timeout beyond budget | Timer | Task continues without AI; clear message and manual path | Cancel call; no partial write | `ai_timeout` with feature, model, latency |
| Provider unavailable | Error or health check | Same as timeout; status notice if prolonged | Circuit opens after N failures; retries with backoff | `ai_provider_down` |
| Low confidence or insufficient evidence | Abstain rule | States it cannot answer and offers the next step (search, human, form) | No answer rendered as fact | `ai_abstain` with reason |
| Policy block | Safety layer | Neutral refusal with route to help | Output discarded | `ai_policy_block` with rule ID |
| Malformed output | Schema validation | Retry once invisibly, then manual path | Invalid output never persisted | `ai_schema_fail` |
| Cost ceiling reached | Budget meter | Feature paused with explanation to the admin; user sees manual path | Metering stops further calls for the period | `ai_budget_exhausted` with tenant |

Acceptance for each row: a fault-injection test producing the failure and
asserting the user-visible behaviour, the absence of corrupted data, and the
logged event.

## 6. AI non-functional requirements beyond the seven clauses

- **Cost per successful task**, not only per call: include retries, retrieval,
  judge calls and human review time. Example: "Cost per accepted loan-summary
  shall not exceed UGX 150 at P90 over a 30-day window."
- **Interactive latency** split into time to first visible output and time to
  completion, each at P50 and P95, measured from the user's action on the
  target network profile (state the profile, for example a 3G-class mobile
  connection).
- **Version pinning:** the production model and version are named; a provider
  deprecation notice triggers re-evaluation before the retirement date.
- **Human review load:** where outputs are reviewed, the expected review rate
  and the reviewer time per item are requirements, because they drive staffing
  and unit cost.

## 7. Acceptance criteria examples

- AI-FR-SUP-003: On evaluation set `EVS-SUP v1.4`, acceptance split, the
  assistant shall resolve at least 85% of common-slice cases and at least 75%
  of code-switched-slice cases correctly per rubric R-SUP-2, and shall abstain
  on at least 95% of should-abstain cases.
- AI-FR-SUP-003-NFR: P95 time to first visible output shall be at most 1.5 s
  and P95 completion at most 6 s on the reference mobile profile.
- AI-FR-SUP-003-FB: When the provider returns no response within 6 s, the user
  shall see the manual ticket form pre-filled with their message within 1 s,
  and no AI text shall be stored.

## 8. Premium versus generic output

| Generic output | Premium output |
|---|---|
| "The model shall be accurate" | Versioned case set, slice thresholds, oracle types and labeller agreement |
| One aggregate score | Per-slice results with the weakest slice named |
| "Graceful fallback" | Failure-class table with user-visible behaviour and a fault-injection test per row |
| Model infers VAT or loan limits | Rules enforced outside the model; violation tests prove rejection |
| Demo success taken as readiness | Graduation gate with recorded evidence |

## Evidence and currentness

Checked 2026-09-24 against primary sources:

- EU AI Act application dates as amended by Regulation (EU) 2026/1744 (Digital
  Omnibus on AI, published in the Official Journal 24 July 2026, in force 27
  July 2026): high-risk obligations for Annex III systems apply from 2 December
  2027 and for Annex I product-embedded systems from 2 August 2028; Article 50
  transparency obligations apply from August 2026. Sources: European Commission,
  "AI Act" policy page (digital-strategy.ec.europa.eu); EUR-Lex, Regulation
  (EU) 2026/1744. Article-level detail of the amended Article 14 and any
  Article 50 transitional arrangements: `NOT_ASSESSED`; confirm in
  `09-governance-compliance/15-ai-act-and-regulatory-compliance-doc`.
- ISO/IEC 42001:2023 (AI management system), edition 1, remains the current
  published edition per iso.org; amendment status beyond that: `NOT_ASSESSED`.
- NIST AI RMF 1.0 (NIST AI 100-1) is under revision per nist.gov; cite version
  and access date when relying on it.
- The procedure itself is `NO_TIME_SENSITIVE_CLAIMS`; all thresholds shown are
  illustrative.

Sources: Khan, A. (2026, early release) *AI Product Management*; Marchiotto, A.
(2025) *Adopting AI for Business Transformation*; engine synthesis with the
parent skill's seven-clause contract and
`ai-system-human-control-contract.md`.
