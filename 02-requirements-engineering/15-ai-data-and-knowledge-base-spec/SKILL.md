---
name: 15-ai-data-and-knowledge-base-spec
description: "Use when specifying AI knowledge sources, ingestion, tenant isolation, freshness, retention, lineage, and training-data exclusions; use ai-feature-prd-spec for user-facing behaviour."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# AI Data and Knowledge-Base Spec Skill

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- specifying AI knowledge sources, ingestion, tenant isolation, freshness, retention, lineage, and training-data exclusions; use ai-feature-prd-spec for user-facing behaviour.
- Use this procedure when the required source artefacts are available and `AI data and knowledge-base specification` is the next lifecycle deliverable.

## Do Not Use When

- Use `ai-feature-prd-spec` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Approved AI use cases, data inventory, tenancy model, and privacy constraints | Data owner, security owner, and product context | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `AI data and knowledge-base specification`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| AI data and knowledge-base specification | Data engineering, AI, security, and evaluation teams | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `AI data and knowledge-base specification` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A source has unknown ownership, tenant scope, or deletion behaviour | Quarantine the source until provenance and lifecycle controls are assigned. | Cross-tenant leakage or untraceable model context. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `AI data and knowledge-base specification` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `AI data and knowledge-base specification` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `ai-feature-prd-spec` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
- [Ai Data And Knowledge Base Spec Template](references/ai-data-and-knowledge-base-spec-template.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

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
