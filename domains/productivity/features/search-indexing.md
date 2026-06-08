# Feature: Search & Indexing

## Purpose and Scope

Retrieve items from the local corpus across three layers — instant metadata lookup, full-text search over extracted and OCR text, and semantic search over embeddings — and blend them into a single ranked, explainable result. The search-indexing module owns the indexes derived from the corpus and the index manager that keeps them consistent with the user's files. Search runs locally; results are correct with no network present (NFR-PROD-001), and the index never claims its inputs are clean when they are not.

Scope is *retrieval and the indexes behind it*. It consumes extracted/OCR text from the reader and metadata from the catalogue; it does not own those source records, only the derived index entries.

## Core Entities

- **Metadata Index** — an in-memory or lightweight on-disk structure over catalogue fields (title, author, tags, status, rating) for instant lookup.
- **Full-Text Index** — an inverted index over extracted and OCR document text supporting BM25-style ranked term queries (for example an embedded full-text search engine).
- **Embedding Index** — locally stored vectors enabling semantic similarity search.
- **Index Entry** — per-Item derivation state: extraction status, extraction-quality flag, OCR status, last-indexed content hash, embedding status.
- **Search Result** — a ranked hit carrying the Item, score, matched layer(s), and a match explanation.
- **Index Manager State** — aggregate progress and health: items indexed, pending OCR, failed extraction, embedding coverage, storage used.

## Layered Search

1. **Instant metadata search.** Matches against catalogue fields with sub-perceptible latency; available before any heavy index finishes building.
2. **Full-text search.** Ranked term matching over extracted and OCR text using a BM25-style relevance model; returns within the search latency budget (NFR-PROD-004).
3. **Semantic search.** Embedding-based similarity for conceptual queries where exact terms are absent; returns within the semantic latency budget (NFR-PROD-004).

## Hybrid Ranking and Explanation

The default ranked result blends signals rather than relying on any single one:

- Exact and near-exact term matches (full-text).
- Semantic similarity (embeddings).
- Recency, item status, and user rating as modifiers.

Each Search Result carries a **match explanation** stating which layer(s) and signals produced the hit (for example "title term match + semantic similarity"), so the user can judge relevance. Hits derived from OCR text are labelled as OCR-derived, since OCR text carries higher error risk than born-digital extraction.

## Index Manager

The index manager is a user-facing surface, not a hidden background process only:

- Shows indexing progress, storage used by each index, items pending OCR, and items with failed extraction.
- Exposes a **rebuild-from-source** command that discards derived indexes and re-derives them from the user's files, used after corruption or a major upgrade.
- Flags extraction quality per Item so callers do not treat extracted text as clean.

## Index Consistency

The index tracks the content hash it was built from. When the catalogue reports an Item changed (new hash) or missing, the affected Index Entry is invalidated and re-derived or removed on the next indexing pass, so search never serves results from content that no longer exists. Re-indexing runs on a background worker and never blocks the UI (NFR-PROD-005).

## Edge Cases Worth Specifying

- **Index drift from content** — a changed or deleted source file invalidates its Index Entry; the next pass re-derives or removes it so stale hits are not served.
- **Index corruption / repair** — a corrupt index is detected on open, quarantined, and rebuildable from source via the index manager; search degrades to the layers that remain healthy meanwhile.
- **Huge indexes** — corpora of tens of thousands of documents: indexing is incremental and resumable; storage use is reported; the search latency budget holds at the stated corpus size (NFR-PROD-004).
- **Extraction-quality flags** — extracted text is never assumed clean; low-quality extractions are flagged so ranking and the UI can signal lower confidence.
- **OCR-derived hits** — results from OCR text are clearly labelled as such, since OCR introduces character errors that affect match precision.
- **Pending derivation** — an Item not yet fully indexed is still findable by metadata search and is shown as partially indexed rather than silently absent from results.

## Representative Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| **FR-SEARCH-001** | The system shall return instant metadata search results against catalogue fields before any full-text or embedding index has finished building. | MVP | Given an indexing pass in progress, when the user searches a title term, then matching items are returned from the metadata index with no wait for full-text completion. |
| **FR-SEARCH-002** | The system shall return ranked full-text results over extracted and OCR text using a BM25-style relevance model within the search latency budget. | MVP | Given a 50,000-document index, when a multi-term query runs, then ranked results return within 500 ms at P95 (NFR-PROD-004). |
| **FR-SEARCH-003** | When semantic search is enabled, the system shall return embedding-similarity results within the semantic latency budget against the reference corpus. | V1 | Given the embedding index over the reference corpus, when a conceptual query runs, then results return within 1.5 seconds at P95 (NFR-PROD-004). |
| **FR-SEARCH-004** | The system shall produce a default ranked result that blends exact term matches, semantic similarity, recency, status, and rating. | V1 | Given a query with both an exact-term and a semantic match, when results return, then ranking reflects all blended signals, not term matching alone. |
| **FR-SEARCH-005** | Each search result shall carry a match explanation naming the layer(s) and signals that produced the hit. | V1 | Given a hybrid result, when a hit is inspected, then it states which layers (for example term + semantic) and modifiers produced it. |
| **FR-SEARCH-006** | The system shall label results derived from OCR text as OCR-derived. | V1 | Given a hit whose match is in OCR text, when it is displayed, then it is marked as OCR-derived. |
| **FR-SEARCH-007** | The index manager shall display indexing progress, per-index storage use, items pending OCR, and items with failed extraction. | MVP | Given an indexing session, when the index manager is opened, then progress, storage use, pending-OCR count, and failed-extraction count are shown. |
| **FR-SEARCH-008** | The index manager shall provide a rebuild-from-source command that discards derived indexes and re-derives them from the user's files. | V1 | Given a rebuild request, when it runs, then prior derived indexes are discarded and rebuilt from source, and search returns consistent results afterward. |
| **FR-SEARCH-009** | When a source Item's content hash changes or it becomes missing, the system shall invalidate its index entry and re-derive or remove it on the next pass. | MVP | Given an edited or deleted source file, when the next indexing pass runs, then no stale hit referencing the prior content is returned. |
| **FR-SEARCH-010** | When index corruption is detected, the system shall quarantine the affected index, degrade to the healthy layers, and offer rebuild-from-source. | V1 | Given a corrupted full-text index, when the application opens, then metadata and semantic search still function and a rebuild is offered. |
| **FR-SEARCH-011** | The system shall flag per-Item extraction quality so callers do not treat extracted text as clean. | V1 | Given an Item with a low-quality extraction, when its index entry is read, then an extraction-quality flag is present and visible to ranking and the UI. |
| **FR-SEARCH-012** | An Item not yet fully indexed shall remain findable by metadata search and shall be shown as partially indexed. | V1 | Given an Item pending full-text derivation, when the user searches its title, then it is returned and marked partially indexed. |

## Data and Entities Owned

This module owns the Metadata Index, Full-Text Index, Embedding Index, per-Item Index Entry state, and Index Manager State. It consumes extracted/OCR text from the pdf-reader module and metadata from the library-catalogue module, and it serves ranked results to the AI advisor's local-degradation path.

## Applicable NFR Defaults

Inherit NFR-PROD-001 (local search with no network), NFR-PROD-003 (catalogue/result rendering budget), NFR-PROD-004 (full-text and semantic search latency budgets), NFR-PROD-005 (non-blocking background indexing, OCR, and embedding generation), NFR-PROD-009 (export remains possible independent of derived indexes), NFR-PROD-014 (embedding erasure coordinated with the AI advisor).
