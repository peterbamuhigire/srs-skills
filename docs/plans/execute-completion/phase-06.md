# Phase 6: AI-Differentiated Product Layer

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Deepen the AI ecosystem from conceptual coverage to production-grade RAG
implementation — the final gap in a 28-skill AI library that is otherwise expert-grade.

**Architecture:** 28 AI skills are already built. The only gap is production RAG depth:
naive → advanced → modular RAG progression, RAGAS evaluation, multi-tenant isolation,
and cost management patterns. This single enhancement closes the last AI gap.

**Skills library path:** `C:\Users\Peter\.claude\skills\`

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Build production RAG systems beyond naive retrieval — query transformation, compression, self-RAG
- Evaluate RAG quality using RAGAS metrics (faithfulness, answer relevance, context precision)
- Isolate tenant embeddings in multi-tenant RAG architectures to prevent data leakage
- Manage RAG costs: embedding API spend, retrieval latency, LLM context token budgets
- Diagnose RAG failure modes: empty retrieval, hallucination despite context, staleness
- Apply hybrid search (vector + BM25) for better retrieval in diverse document collections
- Use HyDE (Hypothetical Document Embeddings) for improved query-to-document matching
- Stream AI responses into every platform: web (Next.js), iOS (SwiftUI), Android (Compose)
- Gate AI features by subscription tier using module gating and per-tenant token quotas
- Build AI features that justify 1.5–3× premium pricing over non-AI equivalents

---

## Current Strengths — AI Ecosystem (28 Skills — Expert Grade)

### LLM Integration Foundation
- `ai-llm-integration` — Direct API: streaming, tool use, prompt caching, multi-provider routing
- `ai-prompt-engineering` — Templates, Chain-of-Thought, prompt versioning, defensive prompting
- `ai-agents-tools` — ReAct loop, tool definitions, multi-agent orchestration, handoffs
- `openai-agents-sdk` — OpenAI Agents SDK: agent types, handoffs, guardrails, tracing
- `deepseek-integration` — DeepSeek V3/R1: cost-efficient coding, local deployment (Ollama)

### RAG & Knowledge Layer
- `ai-rag-patterns` — RAG architecture, chunking, retrieval, pgvector, Pinecone — **ENHANCE THIS PHASE**
- `ai-web-apps` — AI-powered web app patterns: streaming UI, tool call rendering, progressive disclosure

### Product Intelligence
- `ai-opportunity-canvas` — Discover which AI features to build; business case template
- `ai-feature-spec` — Design one AI feature end-to-end: input/output, latency SLA, cost model
- `ai-analytics-saas` — NL2SQL, embedding-based clustering, anomaly detection inside SaaS
- `ai-analytics-dashboards` — KPI cards, AI Insights panel, role-based dashboard views
- `ai-analytics-strategy` — AI analytics roadmap: quick wins, medium-term, platform
- `ai-predictive-analytics` — LLM-based predictions without ML infrastructure
- `ai-nlp-analytics` — Sentiment analysis, entity extraction, classification, multi-language

### Architecture & Cost
- `ai-architecture-patterns` — Module gate, budget guard, provider abstraction, fallback chain
- `ai-app-architecture` — AI-powered SaaS stack: app layer, AI layer, data layer
- `ai-cost-modeling` — Token economics, per-user/tenant cost modelling, margin calculation
- `ai-metering-billing` — Token ledger schema, metering middleware, invoice line items
- `ai-saas-billing` — Module gating (off by default), quota management, tier enforcement

### Safety, Quality & Evaluation
- `ai-security` — Prompt injection prevention, PII scrubbing, DPPA compliance for AI
- `llm-security` — OWASP LLM Top 10, trust boundaries, indirect injection via documents
- `ai-error-handling` — 5-layer validation stack: format → range → consistency → logic → semantic
- `ai-error-prevention` — Verify-first pattern, TDD for AI output, golden test sets
- `ai-evaluation` — Evaluation framework: golden sets, AI-as-judge, drift detection, A/B

### UX & Slop Prevention
- `ai-ux-patterns` — Streaming UI, progressive disclosure, confidence indicators, override UI
- `ai-slop-prevention` — Detecting and preventing AI slop: specificity rules, review gates
- `ai-integration-section` — Grant proposal AI section generator (consulting-specific)

### Orchestration
- `custom-sub-agents` — Custom agent patterns: specialised agents, routing, result aggregation

---

## Build Tasks

### Task 1: Enhance `ai-rag-patterns` with production implementation depth

**File to modify:** `C:\Users\Peter\.claude\skills\ai-rag-patterns\SKILL.md`

**Read first:**
- *AI Engineering* — Chip Huyen (O'Reilly 2025), RAG chapter (most important)
- *Hands-On Large Language Models* — Alammar & Grootendorst, embedding chapters
- RAGAS documentation — `docs.ragas.io`
- LangChain RAG guide — `python.langchain.com/docs/use_cases/question_answering`
- Anthropic Cookbook — `github.com/anthropics/anthropic-cookbook` (contextual retrieval section)

**New sections to add to the existing SKILL.md:**

The existing skill covers basic RAG architecture. Add a new `## Production RAG Implementation`
section containing:

1. **RAG Maturity Model** — Naive RAG → Advanced RAG → Modular RAG: what changes at each level
2. **Query Transformation Techniques:**
   - HyDE (Hypothetical Document Embeddings): generate a hypothetical answer, embed it, retrieve against it
   - Multi-query expansion: LLM generates 3 query variants, retrieve for each, merge results
   - Step-back prompting: rephrase specific questions as general principles before retrieving
3. **Contextual Compression** — LLM summarises retrieved chunks to reduce context window cost
4. **Self-RAG** — LLM decides whether to retrieve at all; critiques its own retrieval quality
5. **Hybrid Search** — Vector similarity + BM25 keyword: combine scores with Reciprocal Rank Fusion
6. **Re-ranking** — Cross-encoder re-ranks top-K results before injecting into LLM prompt
7. **Chunking Strategies:**
   - Fixed-size (512 tokens): simple, consistent; struggles with sentence breaks
   - Semantic chunking: split on sentence boundaries; better context preservation
   - Hierarchical: parent chunk for context, child chunk for retrieval (ParentDocumentRetriever)
8. **RAGAS Evaluation Framework:**
   - Faithfulness: does the answer follow from the context?
   - Answer relevance: does the answer address the question?
   - Context precision: are retrieved chunks relevant?
   - Context recall: were all relevant chunks retrieved?
9. **Multi-Tenant RAG** — Metadata filtering by `tenant_id`, vector namespace isolation (Pinecone), row-level security in pgvector
10. **Embedding Pipeline** — text-embedding-3-small ($0.02/1M tokens), batch embedding, upsert patterns
11. **Cost Management:**
    - Embedding cost: token count estimation per document corpus
    - Retrieval latency: top-K tuning (K=3 vs K=10 trade-off)
    - LLM context cost: compression vs full-chunk injection decision tree
12. **Failure Mode Playbook:**
    - Empty retrieval → fallback to general LLM response with caveat
    - Irrelevant retrieval → hybrid search or query expansion
    - Hallucination despite context → RAGAS faithfulness < 0.7 triggers human review flag
    - Stale embeddings → re-embedding schedule triggered by document update timestamp

**Step 1:** Read all five source materials above.
**Step 2:** Open `ai-rag-patterns/SKILL.md` and append the new `## Production RAG Implementation` section.
**Step 3:** Ensure the file stays under 500 lines after the addition. If it exceeds 500 lines,
   split into `ai-rag-patterns/SKILL.md` (architecture) and `ai-rag-patterns/references/production-rag.md`.
**Step 4:** Every technique must have a Python/TypeScript pseudo-code snippet.
**Step 5:** Commit: `feat(skills): enhance ai-rag-patterns with production RAG implementation depth`

---

## Phase Completion Checklist

- [ ] `ai-rag-patterns` has the new `## Production RAG Implementation` section added
- [ ] All 12 sub-topics in the new section are present
- [ ] Every technique has at least one code snippet
- [ ] File does not exceed 500 lines (split if necessary)
- [ ] RAGAS evaluation framework is fully documented with metrics and thresholds
- [ ] Multi-tenant RAG section includes concrete `metadata.filter` or namespace patterns
- [ ] Cost management decision tree is actionable with specific dollar figures
- [ ] Git commit made: `feat(skills): complete phase-6 — AI-differentiated product layer`

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *AI Engineering* | Chip Huyen | O'Reilly | ~$60 | **The most important book for this phase.** RAG, evaluation, vector databases, production AI systems — the single best treatment of the entire AI engineering discipline. |
| 2 | *Hands-On Large Language Models* | Jay Alammar & Maarten Grootendorst | O'Reilly | ~$60 | Visual, accessible — embeddings, attention, RAG explained with diagrams. Excellent companion to Huyen. |
| 3 | *Building LLM Apps* | Valentina Alto | Packt | ~$40 | End-to-end LLM application implementation with LangChain — chunking, retrieval, agents, evaluation. |
| 4 | *AI-Powered Search* | Trey Grainger | Manning | ~$55 | Hybrid search (vector + keyword): BM25, Reciprocal Rank Fusion, re-ranking. Directly feeds hybrid search section. |

### Free Resources

- RAGAS documentation — `docs.ragas.io` — RAG evaluation framework: faithfulness, relevance, precision metrics
- Anthropic Cookbook — `github.com/anthropics/anthropic-cookbook` — contextual retrieval, caching patterns
- LangChain RAG guide — `python.langchain.com/docs/use_cases/question_answering` — practical retrieval code
- LlamaIndex documentation — `docs.llamaindex.ai` — ParentDocumentRetriever, HyDE, query expansion
- Pinecone documentation — `docs.pinecone.io` — metadata filtering, namespace isolation, hybrid search
- Qdrant documentation — `qdrant.tech/documentation` — self-hosted vector DB; payload filtering
- pgvector README — `github.com/pgvector/pgvector` — HNSW index setup, distance operators, performance

---

*Next phase: [Phase 7 — Quality Engineering & Test Automation](phase-07.md)*
