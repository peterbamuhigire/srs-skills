---
name: "ai-data-and-knowledge-base-spec"
description: "Generate the AI Data and Knowledge-Base Spec: the canonical record of what data feeds AI features, per-tenant vs shared scope, ingestion SLA, freshness, retention, lineage, training-data exclusion, and the cross-tenant leak controls for embeddings and conversation logs."
metadata:
  use_when: "Use when one or more AI features are powered by retrieval, fine-tuning, or any dataset that feeds the model. Mandatory for RAG features."
  do_not_use_when: "Do not use for a single LLM-call feature that takes only the user's own request as input."
  required_inputs: "AI_Feature_PRD_Spec.md, Multi_Tenancy_Architecture_Spec.md, Data_Isolation_Evidence_Pack.md (if exists), DPA, sub-processor list."
  workflow: "Inventory knowledge sources, declare per-source scope (shared vs per-tenant), set ingestion SLA and freshness, declare retention and lineage, declare training-data exclusion clauses, declare embedding and conversation-log isolation rules, write the AI_Data_And_Knowledge_Base_Spec.md."
  quality_standards: "Every knowledge source shall have an owner, classification, ingestion mode, freshness target, retention rule, and training-data exclusion verdict. Every shared store shall have a documented cross-tenant control."
  anti_patterns: "Do not put per-tenant content into a shared embedding index without an explicit isolation strategy. Do not omit retention. Do not assume the model provider will not retain logs by default."
  outputs: "AI_Data_And_Knowledge_Base_Spec.md."
  references: "Use references/ai-data-and-knowledge-base-spec-template.md."
---

# AI Data and Knowledge-Base Spec Skill

## Overview

The data-and-knowledge artefact that retrieval-augmented and fine-tuned features absolutely need but the generic Database Design skill does not produce. Captures lineage, retention, freshness, and the cross-tenant control story.

## Core Instructions

### Step 1: Knowledge source inventory

For every source feeding an AI feature: name, type (document store / data warehouse / external API / customer-uploaded), owner, classification (public / internal / confidential / PII / SPI), volumes, refresh cadence.

### Step 2: Per-source scope

For each source state whether it is shared across tenants (e.g. a public-document corpus) or per-tenant. Shared sources MUST also state the licence / copyright / opt-out posture.

### Step 3: Ingestion pipeline

For each source: ingestion mode (push / pull / event), schedule, transformation, chunking strategy (size, overlap), embedding model, vector store, index segmentation rule (per-tenant index, namespace, metadata filter).

### Step 4: SLA and freshness

| Source | Ingestion SLA | Freshness | Stale-data behaviour |
|--------|----------------|-----------|------------------------|
| Customer document upload | < 5 min from upload to retrievable | < 5 min | feature shows "indexing in progress" |
| CRM sync | hourly | < 1 h | retrieval can be slightly stale |
| Public corpus | weekly | weekly snapshot | n/a |

### Step 5: Retention and lineage

Each source has a retention rule (regulatory + product). Conversation logs (prompt + response) have their own retention. State the lineage record: which model + prompt + index version produced each output. Lineage is queryable for audit.

### Step 6: Training-data exclusion

For each source state whether the data may be used to train the model provider's general models, our fine-tunes, our embedding model. Show evidence: contract clause, gateway endpoint flag, opt-out documentation.

### Step 7: Cross-tenant controls for embeddings and logs

- Per-tenant vector index or namespace + metadata filter; never rely on metadata-only filtering for SPI.
- Per-tenant conversation log with tenant-scoped query path.
- Re-ranker and retrieval prompts include tenant-id as a guarded claim.
- Encryption at rest with per-tenant key for Enterprise tier where contracted.

### Step 8: Write the spec

`AI_Data_And_Knowledge_Base_Spec.md` sections: 1) Source Inventory, 2) Per-Source Scope, 3) Ingestion Pipelines, 4) SLA & Freshness, 5) Retention & Lineage, 6) Training-Data Exclusion, 7) Cross-Tenant Controls, 8) Traceability to AI FRs.

## Standards

- ISO/IEC 42001
- NIST AI RMF MAP-2 (data characteristics)
- GDPR Art. 25 (data minimisation, purpose limitation)
- OWASP LLM06 (sensitive information disclosure)
