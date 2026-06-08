# Domain: Productivity (Knowledge Management & Desktop Productivity)

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | Data protection authorities (EU EDPB / national DPAs under GDPR; jurisdictional Data Protection Acts) — engaged *only* when an optional cloud feature transmits user content or metadata off-device; accessibility regulators where digital-accessibility law applies. |
| **Key Standards** | GDPR + jurisdictional Data Protection Acts (opt-in cloud AI only), WCAG 2.2 Level AA, ISO/IEC 25010:2023 (software product quality model), ISO/IEC 27001-aligned local security hygiene, EN 301 549 / Section 508 (accessibility conformance, conceptual). |
| **Risk Level** | Medium — the app holds the *user's own* documents, notes, and research, not third-party or institutional records; the central trust surface is privacy of any optional AI feature, not regulated PII custody. |
| **Audit Requirement** | No mandatory third-party certification baseline. A privacy self-assessment (Data Protection Impact Assessment screening) is required before shipping any feature that sends user content off-device. Accessibility conformance against WCAG 2.2 AA is a release gate. |
| **Data Classification** | User-Owned Content (documents, PDFs, notes — the user's own intellectual property), Catalogue Metadata (titles, authors, tags, annotations), Provider Secrets (API keys for optional cloud providers), AI History & Embeddings (derived from user content), Local Telemetry (opt-in, device-local by default). |

The defining property of this domain is **local-first by default**. The application stores the user's own corpus on the user's own device, holds no regulated third-party PII baseline, and treats every off-device transmission as an explicit, consented, reversible exception. Privacy is therefore a *design surface*, not a *custody obligation*: the engineering work is to make the boundary between on-device and off-device legible, opt-in, and auditable for the user.

## Personas

- **Individual knowledge worker** — manages a personal corpus of documents and notes; wants retrieval and structure without exporting data to a vendor cloud.
- **Researcher** — works across a large reference library (papers, PDFs, extracted citations); needs full-text search, metadata enrichment, and reproducible organisation.
- **Collector / archivist** — curates and preserves a long-lived library; values format portability, durable metadata, and non-destructive operations above convenience features.
- **Privacy-sensitive user** — will not enable any off-device feature without a precise statement of what payload leaves the device; may run entirely offline or with a local model only.

## Core Capability Areas

- Library cataloguing and organisation (the catalogue of record over the user's files).
- Document reading and annotation (PDF and other document surfaces).
- Metadata enrichment (manual, rule-based, or provider-assisted).
- Search and indexing (full-text and semantic retrieval over the local corpus).
- Optional AI assistance (privacy-tiered, from offline through opt-in content-aware).

## Default Feature Modules

- Library Catalogue (the embedded catalogue of record; import, organise, tag, deduplicate)
- PDF Reader (render, annotate, extract text, isolate untrusted document input)
- Metadata Enrichment (manual edit, rule-based normalisation, optional provider lookup, write-back)
- AI Advisor (privacy-tiered assistant: offline, metadata-only, content-aware opt-in, local-model)
- Search & Indexing (full-text index, optional embeddings, ranked retrieval over the corpus)

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements injected into new productivity projects at scaffold time.

Key injected areas:

- **NFR:** Local-first availability and offline operation for all core reading/organising/searching; cold-start and catalogue-load latency budgets validated against a real corpus; P95 search latency; non-blocking background jobs; crash-free session target; WCAG 2.2 AA keyboard and screen-reader operability; data portability with no proprietary lock-in; reversible transactional destructive operations; privacy-tier payload transparency with preview before any off-device send; signed builds with idempotent backed-up migrations; local audit trail for sensitive actions.
- **FR:** Import and catalogue user files without moving them out of user control; full-text and semantic search; non-destructive annotation; metadata write-back that preserves originals; explicit per-tier AI consent capture; deletion of AI history and embeddings; export of catalogue and annotations in open formats.
- **Interfaces:** OS credential storage (Windows Credential Manager / macOS Keychain) for provider secrets; optional cloud AI providers behind a provider gateway; optional metadata providers; optional OCR engine; embedded WebView for specialised graphics surfaces via a typed message bridge; signed auto-update channel.

## References

- [regulations.md](references/regulations.md) — privacy/compliance baseline: low burden for own-data apps; GDPR/DPA principles engaged on opt-in off-device transmission; consent per privacy tier, payload minimisation, erasure of AI history and embeddings, no training on user data without separate consent, cross-border transfer awareness, accessibility as legal expectation.
- [architecture-patterns.md](references/architecture-patterns.md) — local-first modular monolith with bounded contexts; provider-gateway abstraction; sidecar asset storage beside an embedded relational catalogue of record; resumable background-worker pipeline; privacy-tiered AI layer; embedded WebView with typed bridge; pluggable extension points.
- [security-baseline.md](references/security-baseline.md) — secrets in OS credential storage; untrusted-document isolation; library-root path validation and symlink containment; mandatory code-signing; local security-event audit log; database-at-rest and optional encryption; secure update channel.
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection.

## Feature Reference

- [library-catalogue.md](features/library-catalogue.md)
- [pdf-reader.md](features/pdf-reader.md)
- [metadata-enrichment.md](features/metadata-enrichment.md)
- [ai-advisor.md](features/ai-advisor.md)
- [search-indexing.md](features/search-indexing.md)
