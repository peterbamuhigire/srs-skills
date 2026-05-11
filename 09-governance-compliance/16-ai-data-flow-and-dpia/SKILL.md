---
name: "ai-data-flow-and-dpia"
description: "Generate the AI Data-Flow Diagram and AI-specific DPIA addendum: where customer data flows when AI features run, every model provider as a processor, sub-processor notice, consent capture, training-data exclusion evidence, cross-border transfer mechanism, and the AI-specific risk register that augments the base DPIA."
metadata:
  use_when: "Use for any SaaS shipping AI features that process personal data. Mandatory before EU launch or any regulated-region launch."
  do_not_use_when: "Do not use for AI features that demonstrably process no personal data."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Data_And_Knowledge_Base_Spec.md, DPA, sub-processor list, Multi_Tenancy_Architecture_Spec.md, base DPIA (if exists)."
  workflow: "Inventory data flows, draw the AI data-flow diagram with model providers as processors, write the AI DPIA addendum, declare consent capture, declare training-data exclusion evidence, declare cross-border transfer mechanism, write the AI-specific risk register, write the document."
  quality_standards: "Every data flow shall name source, sink, classification, transfer mechanism, training-exclusion verdict, retention. Every processor shall have a contract reference."
  anti_patterns: "Do not omit retrieval and embedding flows. Do not treat conversation logs as ephemeral if they persist. Do not claim provider-side training exclusion without contract evidence."
  outputs: "AI_Data_Flow_And_DPIA.md plus data-flow diagram source."
  references: "Use references/ai-dpia-addendum-template.md and references/ai-data-flow-diagram-conventions.md."
---

# AI Data-Flow and DPIA Skill

## Core Instructions

### Step 1: Inventory data flows

For each AI feature trace every data flow:

- User -> our service.
- Our service -> retrieval store.
- Our service -> model gateway.
- Model gateway -> model provider.
- Model provider -> response back through gateway.
- Gateway -> conversation log.
- Gateway -> billing-event store.
- Eval pipeline -> judge-LLM provider.
- Red-team -> separate set.

For each flow capture: source, sink, data classes, classification, transfer mechanism (TLS + signed claim), training-exclusion verdict, retention.

### Step 2: Data-flow diagram

Draw the diagram per `references/ai-data-flow-diagram-conventions.md`. Tenant boundary, organisation boundary, jurisdiction boundary, processor boundary. Use distinct symbols for personal data, sensitive personal data, and aggregate / anonymised.

### Step 3: AI DPIA addendum

Augment the base DPIA (if exists) or write standalone. Sections:

- Nature, scope, context, purpose of the AI processing.
- Lawful basis (per GDPR Art. 6 + Art. 9 where applicable).
- Necessity and proportionality assessment.
- Risks to data subjects (with AI-specific risks: opacity, hallucination, automated decisions, retraining drift, prompt-injection leak).
- Measures to address risks (eval harness, red-team, abstain rule, human-in-the-loop, isolation, encryption).
- Residual risk.
- Consultation if residual risk remains high (Art. 36).

### Step 4: Consent capture

For features requiring consent (regulated regions, generative features, high-risk), state where and how consent is captured, the lawful-basis fallback, and the revocation flow.

### Step 5: Training-data exclusion evidence

Per provider: contract clause reference, technical endpoint flag, audit cadence, audit date.

### Step 6: Cross-border transfer mechanism

EU -> US: Adequacy Decision (DPF) or SCCs + transfer impact assessment + supplementary measures. Kenya: data-residency commitment + DPA s.49. Nigeria: NDP Act 2023 Schedule. South Africa: POPIA s.72.

### Step 7: AI-specific risk register

Augment the base risk register:

- Hallucination affecting data subjects (incorrect data attributed to a person).
- Prompt-injection leading to disclosure.
- Cross-tenant retrieval leak.
- Model provider sub-processor change without sufficient notice.
- Training-data exclusion lapse (provider changes terms).
- Conversation log surfacing PII unintentionally.

### Step 8: Write the doc

`AI_Data_Flow_And_DPIA.md` sections: 1) Data Flow Inventory, 2) Data-Flow Diagram, 3) AI DPIA (full Art. 35 form), 4) Consent Capture, 5) Training-Data Exclusion Evidence, 6) Cross-Border Transfer Mechanism, 7) AI-Specific Risk Register, 8) Sign-off Ledger.

## Standards

- GDPR Art. 35 + Art. 36
- EU AI Act Art. 27 (fundamental-rights impact assessment)
- Kenya DPA 2019 s.31
- Nigeria NDP Act 2023 Art. 28
- South Africa POPIA s.71-72
