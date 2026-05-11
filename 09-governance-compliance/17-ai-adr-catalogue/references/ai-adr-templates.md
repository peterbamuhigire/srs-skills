# AI ADR Templates (seed ADRs)

Each ADR follows:

```
# ADR-AI-NNNN: <Decision title>

Status: { proposed | accepted | superseded by ADR-AI-MMMM | deprecated }
Date: YYYY-MM-DD
Owners: <AI Lead, Architect, DPO if applicable>

## Context
<why we are deciding this; constraints>

## Decision
<the choice>

## Consequences
<positive, negative, neutral>

## Alternatives Considered
- Option A: <why rejected>
- Option B: <why rejected>

## Evidence
- <pointers to eval, red-team, model card, contract clause, audit dates>

## Sign-off
- AI Lead: <name, date>
- Architect: <name, date>
- DPO (if applicable): <name, date>
```

## Seed: ADR-AI-001 -- Model Gateway as Sole Egress

- Decision: All model-provider traffic egresses through the Model Gateway. Direct provider calls from feature services are prohibited.
- Drivers: tenant-claim enforcement; cost metering; content filter; fallback routing; audit log; egress allow-list.
- Alternatives: per-service direct call (rejected: no central enforcement of tenant claim, cost, filter); CDN-level allow-list only (rejected: no application-level audit).

## Seed: ADR-AI-002 -- Primary Model for AI Summary

- Decision: <Provider X model Y@vZ> as primary; <Provider X model A@vZ> as cheaper-comparable.
- Drivers: factuality, latency, cost ceiling.
- Alternatives: open-weights self-host (rejected: ops burden today); other hosted provider (rejected on eval delta).
- Evidence: eval EVAL-SUM-200 comparison table; cost runbook table.

## Seed: ADR-AI-003 -- RAG (not fine-tune) for AI Composer

- Decision: AI Composer uses RAG over the customer's own thread plus a tone-prompt; fine-tune is deferred 12 months.
- Drivers: training-data governance, time-to-market, eval portability.
- Alternatives: fine-tune now (rejected: governance + cost); direct LLM only (rejected: no grounding).

## Seed: ADR-AI-004 -- Vector Store: pgvector per-tenant table

- Decision: pgvector with per-tenant table partitioning.
- Drivers: tenant isolation primacy; existing operational competence with Postgres; query latency acceptable at scale envelope.
- Alternatives: dedicated vector DB (rejected: ops surface area today); shared namespace with metadata filter (rejected: metadata-only isolation insufficient for SPI).

## Seed: ADR-AI-005 -- Eval CI Gate at 2pp Regression Threshold

- Decision: PR is blocked if golden-set pass rate regresses > 2 percentage points relative to last green tag.
- Alternatives: 1 pp (rejected: noisy); 5 pp (rejected: lets real regressions through).
- Evidence: 90-d eval variance analysis.

## Seed: ADR-AI-006 -- Abstain Policy

- Decision: Features abstain when judge-LLM confidence < 0.6 or retrieval-set < 2 chunks (RAG features). Abstain payload uses the standard schema.
- Alternatives: no abstain (rejected: invites hallucination); abstain by user opt-in only (rejected: defeats default safety).

## Seed: ADR-AI-007 -- Content Filter Chain

- Decision: Order is: PII detector (input) -> jailbreak detector -> policy classifier -> model call -> PII detector (output) -> policy classifier (output).
- Alternatives: post-only (rejected: loses input safety); pre-only (rejected: loses output safety).

## Seed: ADR-AI-008 -- Prompt Registry Change Protocol

- Decision: PR with diff + regression eval + red-team smoke + AI Lead and feature-owner sign-off; tag bump on merge; staged deploy dev -> staging -> prod with 24 h bake.
- Alternatives: bypass via override (rejected: removes the safety property).

## Seed: ADR-AI-009 -- Conversation Log Retention

- Decision: 90 d hot, 13 mo cold, then delete; per-tenant partition; PII redaction at write.
- Alternatives: indefinite retention (rejected: violates minimisation); 7 d (rejected: insufficient for troubleshooting and audit).

## Seed: ADR-AI-010 -- Training-Data Exclusion Policy

- Decision: All provider contracts shall include a no-training clause for customer content; gateway uses the no-training endpoint where available; quarterly audit of compliance.
- Alternatives: allow training with opt-in (rejected: governance complexity exceeds value today).

## Seed: ADR-AI-011 -- Cross-Tenant Retrieval Prohibition

- Decision: Gateway returns 403 on any retrieval payload whose tenant claim does not match the caller's tenant.
- Alternatives: prompt-level guard only (rejected: prompt-injection bypass risk).

## Seed: ADR-AI-012 -- Judge-LLM Selection

- Decision: Judge model is from a different vendor than the system under test; pinned by version; recalibrated monthly against CAL-* sets.
- Alternatives: same-vendor judge (rejected: self-bias); human-only grading (rejected: doesn't scale to CI).

## Seed: ADR-AI-013 -- Cost Ceiling and Throttle Policy

- Decision: Per-feature per-tenant daily and monthly ceilings; cheaper-comparable model at 130%; hard throttle at 150%; pause at 200%.
- Alternatives: provider-side cap only (rejected: cannot enforce per-tenant).

## Seed: ADR-AI-014 -- Rollback Trigger Set

- Decision: Auto-rollback on citation accuracy drop > 5 pp 24h; manual rollback on factuality drop > 5 pp 24h; pause on safety violation.
- Alternatives: manual-only (rejected: time-to-rollback too long).

## Seed: ADR-AI-015 -- Retraining / Re-evaluation Trigger

- Decision: Re-run full eval + red-team on every provider model version bump and every major prompt change before promotion to prod.
- Alternatives: quarterly only (rejected: provider bumps can ship between cycles).

## Seed: ADR-AI-016 -- Embedding Model Choice

- Decision: <embedding model X@vY>; pinned by version; re-embed on version change for affected indexes only.
- Alternatives: rotate per provider release (rejected: re-embedding cost prohibitive).

## Seed: ADR-AI-017 -- Fallback Model Routing

- Decision: Fallback to <model B> when (a) primary unavailable > 60 s, (b) latency P95 > 200% target, (c) per-tenant cost > 130%. Agent feature has no fallback model (pause instead).
- Alternatives: degrade to abstain only (rejected: poor UX).
