# Ogma Library — SRS Engagement Design

- **Date:** 2026-05-30
- **Product owner:** Chwezi Core Systems / Peter Bamuhigire
- **Input specification:** `Ogma_Library_Application_Design_Report_v1.0_2026-05-30.docx` (v1.0 Application Design Report, marked *Confidential — Internal Use Only*)
- **Status:** Approved (brainstorm gate passed 2026-05-30)

## 1. What Ogma Library Is

Ogma Library is a **local-first, premium desktop application** that turns a collection of PDF files into a managed, searchable, beautiful personal library. The product thesis from the design report:

> Ogma Library gives readers private, durable, beautiful command over their PDF collections.

It is not "a PDF viewer with AI." It is a private, immersive library operating system for personal knowledge, where scanning, metadata repair, 3D browsing, reading progress, annotations, full-text search, AI recommendations, and portable ownership reinforce one another.

**Technical shape (from the report, with the engine's runtime correction):**

- Runtime: **.NET 10 LTS** (active to 2028-11-14); the original spec's .NET 8 ends support 2026-11-10 and is a fallback only behind a documented blocker.
- Shell: **Avalonia** modular monolith desktop app.
- Catalogue: **SQLite** as source of truth + sidecar asset folder (covers, thumbnails, spines, OCR, extracted text, embeddings, backups).
- Reader: **PDFium** render pipeline, **PdfPig** text extraction, **PDFsharp** metadata write-back (isolated, backup + diff + verify).
- 3D bookshelf: **WebView-hosted Three.js** scene with a C#↔JavaScript message bridge.
- AI: provider-neutral **AI gateway** with privacy tiers (offline, metadata-only, content-aware opt-in, local-only via Ollama).
- Search: hybrid — metadata + **SQLite FTS5** full-text + embedding semantic search.
- Packaging: **Velopack** (direct) / **MSIX** (Store/enterprise) / signed-notarized macOS.

## 2. Engagement Decisions (brainstorm outcome)

| Decision | Choice | Rationale |
|---|---|---|
| Engagement goal | **Full document suite** | Vision/PRD → SRS → architecture → design → test → governance, plus Agile delivery artifacts. |
| Methodology | **Hybrid (Water-Scrum-Fall)** | Formal up-front Waterfall SRS sign-off gate, then Agile delivery of the report's 8 build phases. Matches the signed-design-then-iterate shape. |
| Hybrid confirmation | **Yes — formal requirements sign-off before development** | Report defines release gates and a signed design baseline; Water-Scrum-Fall pattern noted in `_context/vision.md`. |
| Domain | **New `productivity` domain pack** | No existing vertical (health/finance/etc.) fits a horizontal knowledge-management desktop tool. Reusable for future Chwezi desktop products. |
| Team size | **3–5 people** | Cross-functional across the 8 build phases. |
| Owner | **Chwezi Core Systems / Peter Bamuhigire** | Never attribute to Byoosi. |

## 3. The `productivity` Domain Pack

New `domains/productivity/` modelled on the existing pack format (e.g. `automotive/`):

- `INDEX.md` — profile: knowledge-management / desktop-productivity, **risk level Medium**, key standards: GDPR / jurisdictional DPA (opt-in cloud AI), **WCAG 2.2 AA**, **ISO/IEC 25010** quality model.
- `references/nfr-defaults.md` — `[DOMAIN-DEFAULT]` blocks: local-first availability, P95 latency budgets, WCAG 2.2 AA, crash-free sessions, data portability, offline operation.
- `references/regulations.md` — GDPR/DPA for opt-in cloud AI payloads, data-subject controls, AI transparency (payload preview), no-regulated-PII baseline.
- `references/security-baseline.md` — OS credential storage for keys, untrusted-PDF isolation, path validation against library root, signed updates, local audit trail.
- `references/architecture-patterns.md` — local-first modular monolith, provider-gateway abstraction, sidecar asset storage, background-worker pipeline, privacy-tiered AI.
- `features/` — `library-catalogue.md`, `pdf-reader.md`, `metadata-enrichment.md`, `ai-advisor.md`, `search-indexing.md`.
- Registered in `domains/INDEX.md`.

## 4. Project Workspace

Scaffolded via `python -m engine new-project Ogma-Library --methodology hybrid --domain productivity` (no golden-path example exists for productivity, so `_context/` is hand-seeded from the report).

```
projects/Ogma-Library/              (LOCAL ONLY — gitignored, never pushed)
  _context/   vision, stakeholders, features, glossary, methodology(hybrid), domain(productivity)
  _registry/  controls.yaml, baseline-trace.yaml, identifiers.yaml, glossary.yaml
  01-strategic-vision/        Vision/PRD, premium product positioning
  02-requirements/            formal IEEE SRS (FR groups LIB/CAT/META/READ/SEARCH/AI + NFRs)
  03-architecture/            module boundaries, bounded contexts, data model, PDF/3D/AI pipelines
  04-design/                  UX blueprint, reader, command palette
  05-test-quality/            golden corpus, test layers, release gates
  07-agile-delivery/          epics/stories mapped to build Phases 0–7
  09-governance-compliance/   ADRs (.NET 10, WebView, PDF renderer), privacy center, DPIA-lite
  export/  export-docs.ps1  export-docs.sh
```

## 5. Cross-Cutting Rules Honored

- **Hybrid gate:** after the Phase 02 Waterfall SRS is signed off and before any Phase 07 Agile artifact, invoke `hybrid-synchronization`; the kernel blocks Phase 07 until `python -m engine validate Ogma-Library` passes the hybrid gate.
- **Premium default:** premium quality expressed as measurable NFRs (latency, crash-free, accessibility, trust/privacy), not marketing prose; invoke `01-strategic-vision/07-premium-product-positioning` before PRD/SRS finalisation.
- **Grounding:** every requirement traces to the design report or `_context/`; gaps flagged `[CONTEXT-GAP]`, never invented.
- **Privacy/security as requirements:** privacy modes, payload preview, OS credential storage, untrusted-PDF isolation, local audit trail become verifiable requirements.
- **No finance trigger:** Ogma has no money/stock/tax/payroll flows, so the finance-accounting doctrine does not apply.

## 6. Git Policy

This repo is **public** (skills engine published free on GitHub). Client project workspaces are **local-only and never tracked**. The `productivity` domain pack and this design doc are public-repo safe and committed; `projects/Ogma-Library/` is gitignored. (On 2026-05-30, 22 straggler project files were untracked to restore this policy.)

## 7. Build Order

1. Design doc (this file) + `productivity` domain pack → commit (public).
2. Scaffold `projects/Ogma-Library/`; seed `_context/` from the report; `engine sync`.
3. Generate the document suite phase-by-phase with sub-agents (Inspect/Modify per PRIME), build `.docx`, run export script — all local.
