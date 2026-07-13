---
name: 11-ai-architecture-spec
description: Use when approved AI features need architecture decisions for direct calls, RAG, fine-tuning or agents, plus model gateway, knowledge stores, evaluation, observability and tenant security; use HLD for the whole system and agent architecture for tool-using runtimes.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# AI Architecture Spec Skill
<!-- dual-compat-start -->
## Use When

- One or more production AI features have approved value, data and evaluation requirements.

## Do Not Use When

- Do not use for projects without AI or to select a provider/model without current verification and measurable criteria.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Approved AI feature requirements and HLD | PRD/SRS and Phase 03 architecture | Required | Stop if feature acceptance or data ownership is unresolved. |
| Data, evaluation, security, latency and cost constraints | AI, data, security and finance owners | Required | Return architecture options and verification gaps when current provider facts are unavailable. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the AI Architecture Specification and ADR seeds through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the AI Architecture Specification and ADR seeds to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Architecture Specification and ADR seeds | AI, data, service, security, test and operations teams | Each feature maps to a justified pattern; gateway, data boundary, evaluation, fallback, observability, cost and tenancy controls have testable contracts. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified AI Architecture Specification and ADR seeds draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Need is grounded retrieval over governed sources | Choose RAG with citation/evaluation path | Fine-tuning does not mask knowledge freshness |
| Task needs bounded tool planning | Route to agent architecture | Agent controls are not omitted |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Letting each service call providers directly. Fix: route through the governed model gateway.
- Choosing RAG because AI is required. Fix: compare direct call, retrieval, fine-tune and non-AI alternatives.
- Sharing embeddings across tenants without policy. Fix: enforce namespace and retrieval filters.
- Treating offline eval as sufficient. Fix: add production monitoring and feedback controls.
- Pinning a model name forever. Fix: specify capability criteria, version evidence and replacement tests.

## References

- [Architecture patterns](references/ai-architecture-patterns.md)
- [Architecture template](references/ai-architecture-spec-template.md)
- [Agent runtime cross-link](references/ai-agent-runtime-crosslink.md)
<!-- dual-compat-end -->




## Overview

The AI-distinctive architecture artefact. Sits alongside the multi-tenancy spec and the generic HLD. Captures the model gateway, vector store, eval harness, prompt registry, observability bus, and the multi-tenant AI security boundaries.

## Core Instructions

### Step 1: Read context

Read HLD, multi-tenancy spec, AI feature PRD spec, AI data spec. Identify in-scope AI features, models, patterns, and the tenant boundaries.

### Step 2: Declare the AI plane

The AI plane is a sub-set of the application plane plus a small set of dedicated control-plane services:

- **Model Gateway** (control plane) — single egress for model-provider calls; carries auth, tenant-id propagation, per-tenant rate limit, cost meter, request/response log, content-filter, fallback routing.
- **Prompt Registry** (control plane) — versioned prompts, change-control, regression-test attachment.
- **Vector Store** (application plane, per-tenant or namespaced) — embedding-backed retrieval.
- **Eval Harness Runner** (control plane) — runs eval suites against new prompt/model versions in CI.
- **Observability Bus** — token use, latency, fallback rate, abstention, citation rate, judge-LLM score, cost per tenant.

Diagram with Mermaid; place every AI service.

### Step 3: Map each AI feature to a pattern

For each AI feature select the pattern:

| Pattern | When | Components |
|---------|------|-------------|
| Direct LLM call | input is self-contained, no external data | gateway + prompt + model |
| RAG | grounding in customer data | gateway + retrieval + reranker + prompt + model + citation post-processor |
| Agent | multi-step, tool-using, planned | gateway + planner + tool catalogue + executor + audit log + per-step approval UI |
| Fine-tune | repetitive narrow task, cost reduction | training pipeline + model artefact + eval suite + rollback artefact |
| Classical ML | structured prediction | feature store + model artefact + monitoring |

State the verdict per feature with rejected alternatives.

### Step 4: Specify the Model Gateway

The gateway is the sole egress to model providers. Capture:

- Supported providers and models (primary + fallback per feature).
- Authentication and credential rotation.
- Tenant-id propagation as a guarded claim.
- Per-tenant and per-feature rate limit and cost ceiling.
- Request/response log retention.
- Content-filter chain (input and output).
- Fallback routing rule (model-down, cost-overrun, latency-overrun, content-filter-trip).
- Idempotency keys for retries.

### Step 5: Specify the Vector Store

For each retrieval index: store technology, partitioning model (per-tenant index / namespace / metadata-filter), embedding model + version, dimensions, ANN parameters, freshness, encryption posture, key management.

### Step 6: Specify the Prompt Registry

Versioned, tagged, changes proposed via PR with regression eval attached. State the registry source-of-truth, deploy pipeline, rollback procedure.

### Step 7: Specify the Eval Harness in architecture terms

The eval harness is a first-class production system, not a notebook. State: dataset store, judge-LLM, CI gate hook, scheduled regression, alerting on score drop.

### Step 8: Specify observability

AI-specific signals: tokens in/out per request, model latency per provider, fallback rate, abstention rate, citation rate, judge-LLM score, cost per tenant per feature, content-filter trips, red-team alerts.

### Step 9: Specify security boundaries

- Prompt injection surface (untrusted text in retrieved docs, in user input, in tool outputs).
- Sandboxing of tool execution.
- Egress allow-list at the gateway.
- Secrets handling: never in prompts; tool-side fetch via tenant-id claim.
- Cross-tenant retrieval prohibition enforced at the gateway.

### Step 10: Emit ADR seeds

ADR seeds: model choice per feature, RAG-vs-fine-tune, vector store choice, eval threshold, abstain policy, content filter, fallback policy.

### Step 11: Write the spec

`AI_Architecture_Spec.md` sections: 1) AI Plane Diagram, 2) Feature-to-Pattern Map, 3) Model Gateway, 4) Vector Store, 5) Prompt Registry, 6) Eval Harness, 7) Observability, 8) Security Boundaries, 9) ADR Seed Index, 10) Traceability.

## Standards

- AWS Well-Architected ML/AI Lens
- OWASP LLM Top 10
- NIST AI RMF MAP / MEASURE
- ISO/IEC 42001
