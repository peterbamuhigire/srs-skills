# Feature: AI Advisor

## Purpose and Scope

Provide an optional assistant that helps the user navigate and reason over *their own* collection — recommending items, generating reading plans, and explaining its suggestions — without making AI a precondition of any core feature. The ai-advisor module is the domain's central trust surface: privacy and explainability are its primary engineering concerns, not afterthoughts. Every off-device transmission is opt-in, previewed, and reversible; the assistant degrades to local behaviour rather than blocking the application when a provider is unavailable or unconfigured.

Scope is *assistance over the local corpus*. The advisor does not own the catalogue, the index, or embeddings storage as a schema authority; it composes their outputs into recommendations and explanations under a privacy-tiered gateway.

## Provider-Neutral Gateway

No UI code calls an AI provider directly. All model interaction passes through a single AI gateway that:

- Exposes a provider-neutral request/response contract so providers are swappable without touching feature code.
- Enforces the active privacy tier before any request is constructed.
- Constructs the payload, applies the prompt budget, and routes to the selected provider (cloud or local model).
- Records local query history and surfaces cost/usage.

Because every provider call funnels through the gateway, the payload-preview and consent guarantees are enforced in one place rather than per call site.

## Privacy Tiers

The advisor operates in explicit, user-selectable tiers, defaulting to the most restrictive:

- **Offline** *(default)* — no off-device transmission; the advisor uses only local search and local data.
- **Metadata-only** — only catalogue metadata (titles, authors, tags) may be sent off-device, never document content.
- **Content-aware (opt-in)** — document content may be sent off-device after explicit per-operation consent and payload preview.
- **Local-model** — inference runs on a local model on the user's device; no content or metadata leaves the device.

The active tier is always visible. Changing tier is an audited action (NFR-PROD-013). A more permissive tier is never entered without explicit user action.

## Recommendation and Explanation

- **Intent-driven recommendation.** The user states an intent (a topic, a question, a goal); the advisor recommends items from the user's own collection, each with an explanation of *why* it was suggested and a confidence indicator.
- **Reading-plan generation.** The advisor sequences a subset of the collection into an ordered plan addressing the stated intent, with the rationale for the ordering shown.
- **Explainability is mandatory.** Every recommendation surfaces the signals behind it (matching terms, semantic similarity, tags, status) so the user can judge it rather than trust it blindly.

## Payload Preview and Consent

Before any off-device send, the advisor shows the exact payload — content or field set, and destination provider — and requires confirmation (NFR-PROD-011). Consent is captured per privacy tier, is revocable, and on revocation the advisor immediately ceases off-device sends and reverts to a local tier. Local query history is retained on-device and is fully deletable and disablable by the user.

## Local Embeddings

Embeddings, where used, may be generated and stored locally with no cloud upload; the user controls whether embeddings exist and can delete them per document or for the whole corpus (NFR-PROD-014). When a more permissive tier would generate embeddings off-device, that is disclosed in the payload preview before it occurs.

## Cost and Usage Visibility

For any tier that calls a paid provider, the advisor shows usage and estimated cost so the user is never billed by surprise; an unconfigured provider simply disables that tier rather than erroring.

## Edge Cases Worth Specifying

- **Provider failure** — a failed or timed-out provider call degrades to local search and local recommendation; it never blocks the application or loses the user's query (NFR-PROD-001, NFR-PROD-006).
- **No API key configured** — tiers requiring a cloud provider are disabled with a clear setup notice; offline and local-model tiers remain fully usable.
- **User revokes consent** — off-device sends stop immediately; the advisor reverts to the most restrictive viable tier and records the revocation.
- **Large collections exceeding a prompt budget** — the advisor selects and ranks a within-budget subset (for example by relevance and recency), discloses that the input was truncated, and never silently sends an over-budget or partial-without-notice payload.
- **Stale embeddings** — when underlying content changes, affected embeddings are marked stale and re-generated locally on next use rather than serving outdated similarity.

## Representative Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| **FR-AI-001** | The system shall route every AI request through a single provider-neutral gateway; no UI component shall call a provider directly. | MVP | Given a code/dependency audit, when call sites are inspected, then every provider call originates from the gateway and no UI module imports a provider client. |
| **FR-AI-002** | The system shall allow the AI advisor to be fully disabled with no loss of function in catalogue, reader, search, or metadata features. | MVP | Given the advisor disabled, when the user browses, reads, searches, and edits metadata, then all core workflows succeed identically to the advisor-enabled state. |
| **FR-AI-003** | The system shall default to the offline privacy tier and shall not enter a more permissive tier without explicit user action. | MVP | Given a fresh install, when AI is first used, then the active tier is offline and no off-device send occurs without a tier change initiated by the user. |
| **FR-AI-004** | Before any off-device transmission, the system shall display the exact payload and destination provider and shall require confirmation. | MVP | Given a content-aware request, when a send would occur, then the payload preview is shown and no request is issued without a recorded confirmation (NFR-PROD-011). |
| **FR-AI-005** | When the user requests a recommendation from an intent, the system shall return items from the user's own collection, each with an explanation and a confidence indicator. | V1 | Given an intent query, when recommendations return, then each recommended item is from the user's corpus and shows the signals behind it and a confidence value. |
| **FR-AI-006** | When a provider call fails or times out, the system shall degrade to local search and recommendation and shall preserve the user's query. | MVP | Given an induced provider timeout, when the user submits a query, then a local result is returned, the application stays responsive, and the query text is retained. |
| **FR-AI-007** | When no provider credential is configured, the system shall disable cloud-dependent tiers with a setup notice and shall keep offline and local-model tiers available. | V1 | Given no API key, when the user opens tier settings, then cloud tiers are disabled with guidance and offline/local-model tiers remain selectable. |
| **FR-AI-008** | When the user revokes consent for a tier, the system shall immediately stop off-device sends, revert to the most restrictive viable tier, and record the revocation. | V1 | Given consent revoked mid-session, when the next request is made, then no off-device send occurs and the tier change is in the audit trail (NFR-PROD-013). |
| **FR-AI-009** | When the user deletes AI history or embeddings for a scope, the system shall remove stored vectors and cached provider responses for that scope. | V1 | Given AI history and embeddings for a document, when scoped erasure runs, then no residual vectors or cached responses remain for that scope (NFR-PROD-014). |
| **FR-AI-010** | When a collection exceeds the prompt budget, the system shall select a within-budget ranked subset, disclose the truncation, and never send an over-budget payload silently. | V1 | Given a corpus larger than the budget, when a content-aware request runs, then the preview shows the truncated subset and the disclosure, and the sent payload is within budget. |
| **FR-AI-011** | When the user requests a reading plan for an intent, the system shall produce an ordered sequence of collection items with the rationale for the ordering. | V2 | Given an intent, when a plan is requested, then an ordered list of items is returned with a stated reason for the sequence. |
| **FR-AI-012** | For any tier that calls a paid provider, the system shall display usage and estimated cost to the user. | V2 | Given a paid-provider tier, when a request completes, then usage and an estimated cost are shown for the operation. |

## Data and Entities Owned

This module owns AI gateway configuration, privacy-tier state and consent records, local query history, and (where enabled) local embeddings storage and its erasure scope. It reads catalogue metadata, search results, and document content via the other modules' interfaces but does not own those schemas.

## Applicable NFR Defaults

Inherit NFR-PROD-001 (advisor degrades to local, never blocks core), NFR-PROD-005 (provider and embedding work runs on background workers), NFR-PROD-006 (provider failure does not crash the session), NFR-PROD-011 (privacy-tier transparency and payload preview), NFR-PROD-013 (audit trail for tier changes and off-device transmission), NFR-PROD-014 (erasure of AI history and embeddings).
