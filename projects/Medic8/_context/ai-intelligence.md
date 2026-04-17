# AI Intelligence Module — Medic8 Context

## Module Positioning

The AI Intelligence module (Module 32) is a tenant-toggleable add-on. It is completely decoupled from the clinical subscription tier. Any facility on any clinical tier (Starter, Growth, Pro, Enterprise) can activate the AI Intelligence module independently.

Billing model: facilities choose either a *credit pack* (token-denominated; AI features pause when credits are exhausted) or a *flat monthly fee* (fixed add-on; unlimited use within defined capacity limits).

Individual capabilities within the module can be toggled independently per tenant from the admin panel. A facility may activate AI ICD Coding Assist and AI Claim Scrubbing while leaving AI Clinical Documentation and AI Differential Diagnosis disabled.

Tier coupling: none. The AI Intelligence module does not require Pro or Enterprise tier. It is a separate billing line.

## Capability 1 — AI Clinical Documentation

The system shall draft SOAP notes, discharge summaries, and referral letters from structured encounter data (ICD-10 diagnoses, vital signs, medications, procedures, and lab results) using the configured AI provider.

Key behaviours:

- The AI draft is surfaced to the clinician in a side-by-side view: the draft on the right, the structured encounter data on the left.
- The clinician reviews the draft and may edit any section before approving.
- The clinician must click **Approve Draft** to save the AI-generated text to the patient record.
- The system shall never auto-save AI-generated text to the patient record without explicit clinician approval.
- If the clinician closes the draft without approving, the draft is discarded and no text is written.
- An audit log entry is created for every draft generated, approved, edited, or discarded, recording the clinician ID, timestamp, token count, and AI provider used.

Supported output types:

- SOAP note (Subjective, Objective, Assessment, Plan)
- Discharge summary
- Referral letter

## Capability 2 — AI ICD Coding Assist

The system shall read the free-text clinical note entered by the clinician and suggest the top 3–5 ICD-10 or ICD-11 codes with a confidence score for each suggestion.

Key behaviours:

- Code suggestions are displayed as a selectable list alongside the diagnosis field during OPD consultation and at discharge.
- The clinician selects one or more suggested codes, or dismisses all suggestions and types a manual search query.
- Acceptance is recorded for model feedback tracking. Acceptance rate is reported in the admin panel.
- Suggestions are advisory only. The clinician may override any suggestion.
- The capability reduces the need for a dedicated medical coder at facilities with fewer than 100 OPD visits per day.

## Capability 3 — AI Differential Diagnosis

At the point of care, the system shall surface a ranked differential diagnosis list derived from the patient's presenting symptoms, recorded vitals, and recent lab results (within the past 7 days).

Key behaviours:

- The differential list is displayed as a collapsible panel in the OPD consultation screen, below the presenting complaint field.
- Each entry shows: the condition name, its ICD-11 code, the top 3 contributing factors from the patient data, and a ranked position (1 = most likely).
- The clinician may dismiss individual suggestions. Dismissed suggestions are removed from the current consultation view.
- The list is presented as a *clinical prompt*, not a decision. The label above the list reads: "AI Differential — for clinician review only. Not a diagnosis."
- No differential suggestion is written to the patient record unless the clinician selects it as an active diagnosis.
- The system shall never present a differential list without disclosing its AI origin on the same screen.

## Capability 4 — AI Patient Plain-Language Summary

The system shall translate the clinical discharge note into a plain-language summary in the patient's preferred locale (`en`, `fr`, or `sw`) for display in the patient portal app.

Key behaviours:

- The summary is generated after the clinician approves the discharge summary.
- Reading level is calibrated per locale: `sw` summaries target a lower Flesch–Kincaid reading level than `fr` or `en` equivalents.
- The summary is displayed in the patient portal under the discharge record. It does not replace the clinical discharge note in the clinical record.
- The patient may share the summary via the patient portal's share function. The clinician-approved discharge note is never shared directly from the clinical record without explicit facility-level consent configuration.
- If the patient's preferred locale is not set, the summary is generated in `en` by default.

## Capability 5 — AI Claim Scrubbing

Before an insurance claim is submitted to the insurer, the system shall predict the rejection probability for each line item using a model trained on the facility's historical claim-rejection data.

Key behaviours:

- The claim scrubbing panel is displayed in the Insurance module at the claim review step, before the **Submit Claim** action.
- Each line item is flagged: green (rejection probability < 10%), amber (10–30%), or red (> 30%).
- Red-flagged line items display the top 2 reasons historically associated with rejection for that insurer and procedure code combination.
- The billing clerk may correct flagged fields before submission.
- Claim scrubbing does not block submission. The clerk may submit a red-flagged claim with a documented override reason.
- Scrubbing accuracy improves over time as the facility's historical rejection dataset grows. The admin panel displays the model's current accuracy metric and the date of last model refresh.

## Capability 6 — AI Outbreak Early Warning

The system shall monitor the facility's OPD and IPD diagnosis data and detect anomalous clustering of diagnosis codes before the Integrated Disease Surveillance and Response (IDSR) national threshold is crossed.

Key behaviours:

- The detection model runs daily as a background job.
- An anomaly is defined as: the 7-day rolling count of a diagnosis code exceeds 2 standard deviations above the facility's 90-day baseline for that diagnosis code and calendar month.
- When an anomaly is detected, the system generates an alert to the Facility Admin and the Medical Officer on duty: "AI Outbreak Alert: [Disease Name] — [N] cases in the past 7 days, [X]% above baseline. Review IDSR threshold."
- Alerts include: the disease code and name, the 7-day case count, the 90-day baseline average, the percentage deviation, and a link to the affected patient list (accessible to authorised clinical staff only).
- The alert does not constitute a mandatory IDSR report. The Medical Officer must assess the alert and initiate IDSR reporting if the national threshold is met.
- False positive rate is tracked in the admin panel over a rolling 90-day period. Target: false positive rate ≤ 15%.

## Provider Adapter Architecture

A single internal `AIProviderInterface` is implemented by four concrete adapter classes. Per-tenant configuration selects the active provider. Switching providers requires no code change — only a tenant configuration update in the admin panel.

```
AIProviderInterface
  ├── OpenAIAdapter       (GPT-4o, GPT-4o-mini)
  ├── AnthropicAdapter    (Claude Sonnet, Claude Haiku)
  ├── DeepSeekAdapter     (DeepSeek-V3, DeepSeek-R1)
  └── GeminiAdapter       (Gemini 1.5 Pro, Gemini 1.5 Flash)
```

All adapters expose the same three methods:

- `complete(prompt: string, options: CompletionOptions): CompletionResponse` — single-turn text generation
- `chat(messages: Message[], options: ChatOptions): ChatResponse` — multi-turn conversation
- `embed(text: string): EmbeddingVector` — text embedding for semantic search and similarity

## Per-Tenant Configuration

Each tenant's AI configuration is stored in the `tenant_ai_config` table with the following fields:

| Field | Description |
|-------|-------------|
| `primary_provider` | Active adapter: `openai`, `anthropic`, `deepseek`, `gemini` |
| `primary_api_key` | API key for the primary provider; encrypted at rest using AES-256-GCM |
| `failover_provider` | Fallback adapter if the primary times out |
| `failover_api_key` | API key for the failover provider; encrypted at rest |
| `capability_flags` | JSON object: per-capability toggle (`clinical_docs`, `icd_coding`, `differential`, `plain_language`, `claim_scrub`, `outbreak_alert`) |
| `billing_model` | `credit_pack` or `flat_fee` |
| `credit_balance` | Current token credit balance (credit pack model only) |

The AI Administrator role configures these fields from the facility admin panel. No other role may access or modify AI provider credentials.

## Failover Behaviour

If the primary AI provider returns an error or does not respond within 10 seconds:

1. The system automatically retries the request using the configured failover provider.
2. If the failover provider also fails within 10 seconds, the AI capability returns a graceful degradation response: the capability UI is disabled with the message "AI service temporarily unavailable. Please complete this step manually."
3. Clinical workflows are never blocked by an AI provider failure. All AI capabilities are additive — the underlying clinical workflow (prescription, discharge, claim submission) proceeds without AI assistance when the provider is unavailable.
4. All failover events are logged with timestamp, primary provider error, and failover outcome.

## Credit Pack Model

Under the credit pack billing model:

- Credits are denominated in tokens.
- Each capability has a published token cost estimate per operation (displayed in the admin panel).
- Token consumption is metered per request, per capability, per tenant.
- The admin panel displays the current credit balance in real time and a consumption graph for the past 30 days.
- When the credit balance reaches zero, all AI capabilities are paused automatically. Clinical features are unaffected.
- The AI Administrator receives an email and in-app notification when the credit balance falls below a configurable threshold (default: 10% of the last top-up amount).
- Credit top-ups are processed through the Medic8 billing system (same payment flow as subscription top-ups).

## Flat Fee Alternative

Under the flat fee billing model:

- A fixed monthly add-on is charged alongside the clinical subscription.
- All six AI capabilities are available without per-token metering.
- Usage is subject to a fair-use ceiling. Tenants exceeding the ceiling by more than 200% in a calendar month are notified and offered a higher-capacity flat-fee tier.
- The flat fee model is available on Pro and Enterprise tiers only.

## Token Metering

Every AI request is logged in the `ai_usage_log` table:

| Field | Description |
|-------|-------------|
| `tenant_id` | Facility identifier |
| `capability` | One of: `clinical_docs`, `icd_coding`, `differential`, `plain_language`, `claim_scrub`, `outbreak_alert` |
| `provider` | Adapter used for the request |
| `model` | Model variant used (e.g., `gpt-4o-mini`) |
| `input_tokens` | Token count for the input prompt |
| `output_tokens` | Token count for the completion |
| `total_tokens` | Sum of input and output tokens |
| `request_timestamp` | UTC timestamp of the request |
| `response_latency_ms` | Response time in milliseconds |
| `was_failover` | Boolean: whether the failover provider was used |

Token usage is reconciled against billing at the end of each billing cycle.

## Admin Panel

The AI Intelligence admin panel (accessible to the AI Administrator role) provides:

- Provider configuration: primary and failover provider selection, encrypted API key entry.
- Credit balance: current balance, top-up history, projected depletion date based on 30-day consumption average.
- Usage dashboard: token consumption by capability, by day, by model; exportable as CSV.
- Capability toggles: per-capability on/off switches per tenant.
- Model accuracy: ICD coding suggestion acceptance rate, claim scrubbing accuracy, outbreak warning false positive rate — updated daily.

## Safety Guardrails

The following guardrails are non-negotiable and cannot be disabled by any configuration:

1. AI Clinical Documentation drafts are never auto-saved. The clinician must click **Approve Draft** before any text is written to the patient record.
2. AI Differential Diagnosis suggestions are never written to the patient record unless the clinician selects the condition as an active diagnosis.
3. Every AI-generated output displayed to a clinician must be labelled with its AI origin on the same screen (e.g., "AI-generated — clinician review required").
4. AI capabilities do not block clinical workflows. If an AI service is unavailable, the clinical workflow proceeds manually.
5. No patient personally identifiable information (name, NIN, date of birth) is included in prompts sent to AI providers where it can be avoided. Encounter data is referenced by anonymised encounter ID. The AI provider receives clinical facts (diagnoses, vitals, medications) without the patient's identity fields.

## DPPA 2019 Data Privacy

Patient clinical data sent to AI providers is governed by a Data Processing Agreement (DPA) between Chwezi Core Systems and each provider. The DPA covers:

- Data processing purpose: AI-assisted clinical workflow support only.
- Data retention by the provider: zero retention beyond the request-response cycle (providers must confirm this in their API terms).
- No training on customer data: Medic8 customer data must not be used by any provider to train or fine-tune models.
- Data residency: tenants subject to Uganda PDPA 2019 must use a provider whose infrastructure is either in Uganda or in a jurisdiction with an adequacy decision. If no such provider is configured, the system displays a compliance warning in the AI admin panel.

The AI Administrator is responsible for confirming that the selected provider's DPA terms satisfy the facility's regulatory requirements before activating the module.

[CONTEXT-GAP: Data Processing Agreement template with OpenAI, Anthropic, DeepSeek, and Gemini — legal review required before Phase 3 launch]
