# Feature: PDF Reader

## Purpose and Scope

Render documents from the catalogue, navigate them, and let the user mark them up without altering the source file. The pdf-reader module is where the user spends reading time, so its correctness budget centres on faithful rendering, durable annotation, and resumable position. Annotations and reading state are persisted *in the application*, keyed to the catalogued Item, so the source file on disk is never rewritten as a precondition of reading or marking up.

Scope covers paginated document surfaces (PDF as the primary format, with the same patterns applying to other paginated formats). The module treats every opened document as untrusted input and isolates rendering accordingly per the security baseline.

## Core Entities

- **Reading Session** — per-Item state: last page, last scroll offset, last zoom/fit mode, last layout mode. Resumed on reopen.
- **Navigation History** — a per-session stack of visited locations supporting back/forward across jumps (internal links, search hits, bookmarks).
- **Bookmark** — a user-named pointer to a page or location within an Item.
- **Annotation** — a highlight, note, ink, or shape anchored to a document location. Attributes: type, page index, geometry (rectangles or path), anchor signature, colour, body text, `created_at`, `layer_id`.
- **Annotation Layer** *(advanced)* — a named, toggleable group of annotations over one Item, so distinct passes (for example a first read versus an editorial review) can be shown or hidden independently.
- **Citation Capture** — a structured reference extracted from a selection: quoted text, page, and item identity, suitable for export to a metadata or reference record.

## Rendering and Navigation

- **Open and render.** The reader opens the source from its catalogued path and renders the current page on a background worker so the UI thread is never blocked (NFR-PROD-005).
- **Resume.** On reopen, the reader restores the Reading Session — page, offset, zoom, and layout — without the user re-locating their position.
- **Page navigation and history.** The user moves by page, jumps to a page number, follows internal links, and steps back/forward through Navigation History.
- **Zoom and fit.** Discrete zoom plus fit-width, fit-page, and fit-height modes.
- **Layout.** Single-page, two-page spread, and continuous scroll layouts, switchable without losing position.
- **Calm reading mode.** A full-screen mode that hides chrome, with night and sepia rendering modes meeting the WCAG 2.2 AA contrast criteria for any retained UI text (NFR-PROD-008).

## In-Document Search

The reader searches extracted text within the open document and highlights matches in place, stepping match-to-match through Navigation History. Where a document is image-only, in-document search returns no hits until OCR text exists for it; the reader states this explicitly rather than silently returning empty results.

## Annotation Model

Highlights, notes, ink, and shapes are stored against the Item, never written into the source PDF by default. Each annotation carries both an explicit page-and-geometry anchor and an anchor signature (for example a snippet of the underlying text) so that re-extraction or minor re-pagination can re-locate it. When geometry can no longer be resolved confidently, the annotation is retained and flagged as *stale* rather than discarded.

Annotation layers let the user group annotations into independently toggleable passes over the same document.

## Specialised and Untrusted Input

- **Password-protected documents** are unlocked through the operating-system credential flow; the application stores no document password in plaintext and routes any retained secret to OS credential storage.
- **OCR** of image-only documents runs as an *optional background job* that produces a text layer for search and selection; it never blocks reading and never modifies the source file.
- Every opened document is treated as untrusted; rendering is isolated so a malformed file cannot compromise the host process.

## Edge Cases Worth Specifying

- **Scanned / image-only documents** — no extractable text until OCR completes; search and selection are disabled with an explicit notice, then enabled against the OCR text layer.
- **Very large documents** — 1,000+ pages: pages render on demand; the reader does not pre-render or hold the whole document in memory; navigation to an arbitrary page meets the UI-responsiveness budget.
- **Rotated pages** — page rotation metadata is honoured in rendering and in text-selection geometry.
- **Broken or corrupt files** — a file that cannot be parsed yields a clear error and leaves the catalogue Item intact and re-openable; the reader does not crash the session (NFR-PROD-006).
- **Reading-order issues in extracted text** — multi-column or table layouts may extract out of reading order; selection and copy reflect the extracted order, and the limitation is surfaced rather than presented as authoritative.
- **Stale annotation geometry after re-extraction** — annotations whose anchors no longer resolve are retained and flagged stale, never silently deleted.

## Representative Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| **FR-READ-001** | When the user opens a catalogued document, the system shall render it from its source path on a background worker without rewriting the source file. | MVP | Given an Item, when it is opened, then the first page renders, the source file byte content is unchanged, and the UI thread shows no stall exceeding 100 ms. |
| **FR-READ-002** | When the user reopens a previously read document, the system shall restore the last page, scroll offset, zoom, and layout from the Reading Session. | MVP | Given a document last left on page 42 at fit-width, when it is reopened, then it displays page 42 at fit-width. |
| **FR-READ-003** | When the user creates a highlight, note, ink, or shape, the system shall persist it against the Item without modifying the source file. | MVP | Given a highlight on page 5, when the reader is closed and reopened, then the highlight reappears on page 5 and the source file content is unchanged. |
| **FR-READ-004** | When the user searches text within an open document, the system shall highlight each match and allow stepping forward and backward through matches. | MVP | Given a term present 7 times, when the user searches it, then 7 matches are indicated and next/previous step through them in order. |
| **FR-READ-005** | When a document is image-only and has no OCR text, the system shall disable in-document search and selection and shall state that OCR is required. | V1 | Given an image-only document with no OCR layer, when the user invokes search, then a notice states OCR is required and no false-empty result is returned. |
| **FR-READ-006** | When the user starts OCR for an image-only document, the system shall run it as a background job and shall enable search and selection against the resulting text layer on completion. | V1 | Given an image-only document, when OCR completes, then search returns hits against the OCR text and the source file is unmodified. |
| **FR-READ-007** | When the user opens a password-protected document, the system shall request unlock through the OS credential flow and shall not store the password in plaintext. | V1 | Given an encrypted document, when the user supplies the password via the OS flow, then it opens and no plaintext password is found in application storage. |
| **FR-READ-008** | When the user enters calm reading mode, the system shall hide application chrome and offer night and sepia rendering meeting AA contrast for retained text. | V1 | Given any document, when calm mode and night mode are active, then chrome is hidden and retained text meets the 4.5:1 contrast ratio. |
| **FR-READ-009** | When re-extraction or re-pagination invalidates an annotation's geometry, the system shall retain the annotation and flag it stale rather than delete it. | V1 | Given an annotation whose anchor no longer resolves, when the document is reopened after re-extraction, then the annotation is present and marked stale. |
| **FR-READ-010** | When the user captures a citation from a selection, the system shall record the quoted text, page, and Item identity in a structured form available for export. | V2 | Given a selected passage on page 9, when the user captures a citation, then a structured record holds the quote, page 9, and the Item identity. |
| **FR-READ-011** | When the user groups annotations into layers, the system shall let each layer be shown or hidden independently over the same document. | V2 | Given 2 annotation layers on one document, when one layer is hidden, then only the other layer's annotations are visible. |

## Data and Entities Owned

This module owns Reading Session, Navigation History, Bookmark, Annotation, Annotation Layer, and Citation Capture records. It references Items by the identity owned by the library-catalogue module and consumes OCR text produced by an optional OCR job. Extracted and OCR text it produces is consumed by the search-indexing module.

## Applicable NFR Defaults

Inherit NFR-PROD-001 (offline reading and annotation), NFR-PROD-005 (non-blocking rendering, OCR, and background work), NFR-PROD-006 (crash-free sessions; no loss of unsaved annotation state), NFR-PROD-008 (screen-reader operability and contrast for reading modes), NFR-PROD-009 (annotation export in a documented open sidecar format), NFR-PROD-010 (reversible deletion of annotations).
