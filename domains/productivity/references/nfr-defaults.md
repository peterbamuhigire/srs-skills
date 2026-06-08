# Productivity — Non-Functional Requirement Defaults

Each block below is injected into the scaffolded SRS under `<!-- [DOMAIN-DEFAULT: productivity] -->` markers. Consultants review, edit, or delete per product context before the SRS is built.

These defaults assume a **local-first desktop application** that holds the user's own corpus on the user's own device. Latency budgets are stated as *engineering budgets to validate against a representative corpus*, not as universal guarantees; the verification method for each is named so the threshold can be tested rather than asserted.

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-001: Local-First Core Availability
The application SHALL perform all core operations — open the library, browse the catalogue, read a document, annotate, and execute full-text search — with no network connection present and no degradation of result correctness. Verification: an automated test suite SHALL run the full core-operation set with the network interface disabled and SHALL pass with identical results to the connected run.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-002: Cold-Start Latency Budget
The application SHALL reach an interactive state (main window rendered, catalogue list responsive to input) within 3 seconds at P95 on the defined reference hardware, measured against a representative corpus of at least 5,000 catalogue items. Verification: an instrumented startup benchmark SHALL run against the reference corpus on the reference machine in CI and fail the build if the P95 budget is exceeded.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-003: Catalogue-Load Latency Budget
The application SHALL render the first screen of catalogue results within 1 second at P95 and SHALL render or scroll any subsequent page within 200 ms at P95, measured against a representative corpus of at least 50,000 catalogue items. Verification: a scripted scroll-and-render benchmark over the reference corpus reports P95 timings; values are recorded against the budget at each release.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-004: Search Latency Budget
The application SHALL return ranked full-text search results within 500 ms at P95 for a single-term or multi-term query against an index built from a representative corpus of at least 50,000 documents. Semantic (embedding) search, where enabled, SHALL return within 1.5 seconds at P95 against the same corpus. Verification: a query-replay benchmark over a fixed query set against the reference index reports P95 latency per search mode.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-005: UI Responsiveness and Non-Blocking Background Work
The application SHALL not block the user-interface thread for longer than 100 ms during any user-initiated interaction. All long-running work — import, indexing, OCR, metadata enrichment, embedding generation, and provider calls — SHALL execute on background workers and SHALL not freeze, modal-lock, or hang the foreground while running. Verification: UI-thread frame timing is sampled during a scripted import-and-index session; any main-thread stall exceeding 100 ms is logged as a defect.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-006: Crash-Free Session Target
The application SHALL achieve a crash-free session rate of at least 99.5% across opted-in telemetry over any rolling 30-day window. Any reproducible crash that causes loss of unsaved annotation or catalogue state is a release blocker regardless of the aggregate rate. Verification: opt-in crash telemetry computes the crash-free session rate; the figure is reviewed at each release and against the blocker rule.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-007: Keyboard Operability (WCAG 2.2 AA)
Every interactive control SHALL be reachable and operable using the keyboard alone, with a visible focus indicator meeting the WCAG 2.2 *Focus Appearance* and *Focus Not Obscured* criteria, and SHALL present no keyboard trap. Verification: a keyboard-only walkthrough of every primary workflow plus an automated accessibility check (axe-core or equivalent) runs at each release; any blocked control fails the gate.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-008: Screen-Reader Operability (WCAG 2.2 AA)
All non-decorative UI elements SHALL expose an accessible name, role, and state to the platform accessibility API (UI Automation on Windows, NSAccessibility on macOS), and dynamic state changes SHALL be announced. Text and meaningful UI SHALL meet the WCAG 2.2 AA contrast ratios (4.5:1 for normal text, 3:1 for large text and UI components). Verification: a screen-reader pass over each primary workflow plus an automated contrast audit runs at each release.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-009: Data Portability and No Proprietary Lock-In
The user's source files SHALL remain in their original, openly readable formats on disk under the user's control; the application SHALL NOT rewrite source files into a proprietary container as a precondition of use. The user SHALL be able to export the full catalogue, all annotations, and all metadata to documented open formats (for example JSON and CSV, with annotations in a documented sidecar format) such that the export is sufficient to reconstruct the organisation in another tool. Verification: a round-trip test exports the catalogue and re-imports it into a clean instance, confirming no loss of metadata or annotation linkage.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-010: Reversible, Transactional Destructive Operations
Any destructive operation — delete, bulk move, bulk re-tag, metadata overwrite, or merge — SHALL execute under a backup-write-verify-restore protocol: the prior state is captured, the change is written transactionally, the write is verified, and a single-action undo or restore is available for the operation. A partial failure SHALL leave the catalogue in its pre-operation state. Verification: a fault-injection test interrupts each destructive operation mid-write and confirms the catalogue restores to the exact pre-operation state.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-011: Privacy-Tier Transparency and Payload Preview
Before any operation transmits user content or metadata off-device, the application SHALL display the active privacy tier and a preview of the exact payload to be sent (content, field set, and destination provider) and SHALL require explicit confirmation. The default tier SHALL be the most restrictive (offline / no off-device transmission). Verification: an integration test asserts that no off-device request is issued by any AI or enrichment path without a recorded prior confirmation referencing the previewed payload.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-012: Update Safety — Signed Builds and Reversible Migrations
Every published build SHALL be code-signed and SHALL be verified against its signature before installation; an unsigned or tamper-detected update SHALL be refused. Every catalogue-schema migration SHALL be idempotent, SHALL snapshot the catalogue before applying, and SHALL be reversible to the pre-migration snapshot if post-migration verification fails. Verification: the update pipeline rejects a deliberately corrupted artifact in test, and a migration-failure injection confirms automatic restore to the pre-migration snapshot.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-013: Local Audit Trail for Sensitive Actions
The application SHALL append a local, tamper-evident audit record for each sensitive action: provider-credential add/change/remove, AI-mode (privacy-tier) change, off-device transmission, metadata write-back to source files, bulk destructive operation, and export. Each record SHALL carry the action, timestamp, affected scope, and active privacy tier. The audit log SHALL be viewable and exportable by the user and SHALL NOT be silently truncated. Verification: each listed action is performed in test and the corresponding audit record is asserted present with the required fields.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: productivity] Source: domains/productivity/references/nfr-defaults.md -->
#### NFR-PROD-014: AI History and Embedding Erasure
The user SHALL be able to delete AI query history and all embeddings derived from a given document or from the entire corpus, and the deletion SHALL remove both the stored vectors and any cached provider responses for that scope within the same operation. Where embeddings were generated by an off-device provider, the application SHALL surface the provider's deletion mechanism or guidance. Verification: a test generates embeddings and AI history for a document, invokes scoped erasure, and asserts no residual vectors or cached responses remain for that scope.
<!-- [END DOMAIN-DEFAULT] -->
