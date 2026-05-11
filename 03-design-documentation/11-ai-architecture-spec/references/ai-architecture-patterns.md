# AI Architecture Patterns Reference

## Pattern: Direct LLM call

```
[user] -> [feature service] -> [model gateway] -> [provider] -> response
```

Use when: input is self-contained; no external grounding required. Typical: summarisation, translation, classification of short user text.

## Pattern: RAG (Retrieval-Augmented Generation)

```
[user] -> [feature service]
              | -> [retriever] -> [vector store, tenant-scoped]
              | -> [reranker]
              | -> [prompt build]
              | -> [model gateway] -> [provider]
              | -> [citation post-processor]
         -> response with citations
```

Use when: grounding required in tenant data or curated corpus. Defines the citation contract: every fact in the answer cites a chunk.

## Pattern: Agent (planner + tools)

```
[user] -> [planner] -> approved-actions catalogue
              | for each step:
              |   -> [model gateway] decides tool call
              |   -> [executor] sandbox runs tool
              |   -> [observer] writes to audit log
              | -> [model gateway] final answer
         -> response + audit trail
```

Use when: multi-step task with side effects. Mandatory: approved-actions catalogue is the closed list; per-step human approval for any irreversible action.

## Pattern: Fine-tune

```
[training pipeline] -> [eval suite] -> [model artefact in registry]
[runtime] -> [gateway] -> tag-pinned model
```

Use when: narrow repetitive task, cost reduction is the driver, base model behaviour is consistently wrong on the task. Mandatory: training-data lineage record + eval pass before promotion.

## Pattern: Classical ML

```
[input] -> [feature store] -> [model artefact] -> prediction
[monitoring] -> drift detection -> retrain trigger
```

Use when: structured prediction, low-latency, explainability required, ample labelled data exists.

## Decision rubric

1. If you can express the task as deterministic code, do that instead.
2. If you can solve it with one LLM call and no external data, choose Direct LLM.
3. If grounding is the failure mode, choose RAG.
4. If the task requires side effects through external systems, choose Agent.
5. Only choose Fine-tune after a documented cost or accuracy gap that prompting alone cannot close.
6. Classical ML wins for structured prediction, low latency, and tight explainability.
