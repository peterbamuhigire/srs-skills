---
name: "ai-architecture-spec"
description: "Generate the AI Architecture Specification: RAG vs fine-tune vs agent decisions, model gateway, vector store, eval harness, observability, security boundaries, and the SaaS-specific multi-tenant AI plane that the generic HLD does not capture."
metadata:
  use_when: "Use when one or more AI features ship in a SaaS product. Required alongside or after the generic HLD."
  do_not_use_when: "Do not use for projects with no AI features."
  required_inputs: "HLD.md, Multi_Tenancy_Architecture_Spec.md, AI_Feature_PRD_Spec.md, AI_Data_And_Knowledge_Base_Spec.md, tech_stack.md."
  workflow: "Read inputs, declare the AI plane decomposition, map each feature to a pattern (RAG / agent / fine-tune / direct call), spec the model gateway, vector store, eval harness, observability, security boundaries, emit ADR seeds, write the AI_Architecture_Spec.md."
  quality_standards: "Every AI feature shall map to a pattern with explicit drivers. The model gateway shall be the sole egress for model calls. Every cross-tenant boundary shall name its enforcement mechanism."
  anti_patterns: "Do not let individual services call model providers directly. Do not store conversation logs in the same store as customer documents without isolation. Do not omit the eval harness from the architecture."
  outputs: "AI_Architecture_Spec.md plus ADR seeds in adr-seeds/."
  references: "Use references/ai-architecture-spec-template.md and references/ai-architecture-patterns.md."
---

# AI Architecture Spec Skill

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
