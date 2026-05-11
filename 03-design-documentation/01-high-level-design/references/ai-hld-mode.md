# HLD AI Mode (addendum)

When the system under design ships AI features, the generic HLD MUST add the following viewpoints. Treat each as required HLD content; cross-link to the dedicated AI Architecture Spec at `03-design-documentation/11-ai-architecture-spec/` for full detail.

## Required additional viewpoints

1. **Model Gateway viewpoint** — sole egress for model provider calls; cost meter; content filter; fallback routing; tenant-claim enforcement.
2. **Vector Store viewpoint** — per-tenant or namespaced; embedding model + version; freshness; encryption.
3. **Prompt Registry viewpoint** — versioned, change-controlled, regression-eval-attached.
4. **Eval Harness viewpoint** — production-class system, not a notebook; CI gate + scheduled regression.
5. **Hallucination SLO viewpoint** — factuality / citation / abstention SLIs; auto-rollback triggers.
6. **AI Observability viewpoint** — tokens, latency per model, fallback rate, abstention, citation, judge-LLM score, cost per tenant per feature.
7. **AI Security Boundary viewpoint** — prompt-injection surfaces; tool-execution sandbox; egress allow-list; cross-tenant retrieval prohibition.

## HLD section header pattern when AI Mode is on

```
3.X AI Plane
  3.X.1 Feature-to-Pattern Map
  3.X.2 Model Gateway
  3.X.3 Vector Store
  3.X.4 Prompt Registry
  3.X.5 Eval Harness
  3.X.6 Hallucination SLO Surface
  3.X.7 AI Observability
  3.X.8 AI Security Boundaries
```

For each subsection, summarise the decision and link to the AI Architecture Spec for the detail. Do not duplicate the AI Architecture Spec content here.

## When to fork the doc

If the HLD becomes unwieldy with AI plane content, hold the HLD to a one-page AI summary and move the substance to the AI Architecture Spec. Cross-link both ways.
