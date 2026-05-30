# Productivity — Architecture Patterns

These patterns are generic and reusable across local-first knowledge-management and desktop-productivity products. They assume a single-user application that owns a corpus of the user's files on the user's device, with optional, privacy-tiered off-device features layered on top of a fully functional offline core.

## Local-First Modular Monolith

The recommended baseline is a **single deployable desktop application** decomposed internally into bounded contexts, not a distributed system. A modular monolith keeps the offline core simple and avoids network coupling for operations that must work with no connection, while clean module boundaries preserve the option to extract a context later.

Suggested bounded contexts:

- **Catalogue** — the catalogue of record over the user's files: items, collections, tags, relationships. Owns identity and organisation.
- **Ingestion** — import, deduplication, text extraction, and handoff to indexing. Owns the import pipeline.
- **Reader** — document rendering, annotation, and text/selection extraction. Owns the reading surface.
- **Search-index** — full-text index and optional embedding index; ranked retrieval. Owns retrieval.
- **AI advisor** — privacy-tiered assistance over catalogue and content. Owns AI orchestration.
- **Settings / security** — preferences, privacy tiers, credential management, audit trail. Owns the security and consent state.
- **Packaging** — update channel, migrations, build integrity. Owns lifecycle.

Each context exposes an internal interface; cross-context calls go through those interfaces rather than reaching into another context's storage. The catalogue is the single source of truth for organisation; other contexts hold derived state (indexes, embeddings) that can be rebuilt from the catalogue and source files.

## Provider-Gateway Abstraction

No UI or feature-module code may call an external AI or metadata provider directly. All off-device calls route through a single **provider gateway** that:

- Resolves credentials from OS credential storage (never from settings or the database).
- Enforces the active privacy tier and refuses any call the tier does not permit.
- Applies payload minimisation and emits the payload preview for confirmation before sending.
- Writes the off-device audit entry.
- Normalises provider responses to an internal shape so providers are interchangeable.

This yields one enforceable network egress chokepoint and lets metadata providers, OCR engines, and AI providers be swapped without touching feature code.

## Sidecar Asset Storage Beside an Embedded Catalogue of Record

The **catalogue of record** is an embedded relational store (for example SQLite) holding items, metadata, tags, annotations, AI history, and embeddings references. Large or binary derived assets — extracted text blobs, generated thumbnails, OCR layers, annotation overlays — are stored as **sidecar files** in an application-managed asset directory, referenced by the catalogue rather than embedded as large blobs in the database.

Invariants:

- Source files remain the user's files in their original location and format; the catalogue references them and is never the only copy (see NFR-PROD-009).
- Derived assets and indexes are rebuildable: deleting them and re-running ingestion reconstructs them from source files and the catalogue.
- The relational catalogue is the authority for organisation; sidecar assets are cache-like and disposable.

## Background-Worker Pipeline (Resumable, Per-Item Failure Isolation)

Import, text extraction, OCR, metadata enrichment, and embedding generation run on a **background-worker pipeline** off the UI thread (see NFR-PROD-005). The pipeline:

- Processes items as independent units so one malformed or oversized item fails in isolation without aborting the batch.
- Is **resumable**: progress is checkpointed per item, so an interrupted import or re-index resumes from the last completed item rather than restarting.
- Records per-item status (pending, processing, done, failed-with-reason) the user can inspect and retry.
- Enforces time and memory bounds per item, consistent with the untrusted-document controls in `security-baseline.md`.

## Privacy-Tiered AI Layer

AI features are organised as explicit tiers, with the most restrictive as default. The active tier governs what the provider gateway will permit.

| Tier | Off-device payload | Use |
|---|---|---|
| Offline | None | No AI, or AI features disabled. The full core remains functional. |
| Metadata-only | Catalogue metadata fields only (titles, authors, tags) | Lookup and normalisation that need bibliographic fields, not document content. |
| Content-aware (opt-in) | Selected document content | Summarisation, question-answering, semantic indexing over content the user explicitly consents to send. |
| Local-model | None (inference on-device) | Content-aware capability with no off-device transmission, where an on-device model is available. |

Tier changes are recorded in the audit trail, and the gateway re-evaluates permitted payloads whenever the tier changes.

## Embedded WebView for Specialised Graphics Surfaces

Where a feature needs a rich rendering surface that the native UI toolkit serves poorly — for example a PDF canvas, an annotation overlay, or a graph/visualisation view — an **embedded WebView** MAY host that surface. The integration MUST use a **typed message bridge** between the native shell and the WebView, with a defined message schema in both directions, rather than ad-hoc string passing. The WebView surface is treated as a rendering boundary for untrusted document content (see `security-baseline.md`): active content disabled by default, no uncontrolled external resource fetches, and no direct access to credentials or the catalogue except through bridge messages the native side authorises.

## Pluggable Extension Points

The architecture defines stable extension points so capabilities can be added without modifying core modules:

- **Metadata providers** — implement a common lookup/normalisation interface behind the provider gateway.
- **Exporters** — implement a common export interface producing documented open formats (see NFR-PROD-009).
- **OCR engines** — implement a common text-extraction interface, runnable on the background-worker pipeline.
- **AI providers** — implement a common chat/embedding interface behind the provider gateway, governed by the active privacy tier.

Each extension point is a contract; implementations are interchangeable and discovered through configuration, never hard-wired into feature modules. This keeps the offline core independent of any specific external service and lets a product ship with local defaults and add providers later.
