# Feature: Library Catalogue

## Purpose and Scope

Maintain the catalogue of record over a user-designated content root on the user's own device. The library-catalogue module discovers files, assigns each a stable identity, tracks availability without losing user-entered metadata, and presents the corpus through browsable, sortable, filterable views. It is the spine to which the PDF reader, metadata enrichment, AI advisor, and search modules attach: every other module addresses items by the identity this module owns.

Scope is the *organisation* of the corpus, not its *content*. The catalogue records where an item lives, what it is, and how the user has classified it. The catalogue never moves source files out of the user's control and never rewrites them as a precondition of cataloguing.

## Core Entities

- **Library Root** — a user-selected directory tree the application is authorised to scan. Attributes: absolute path, include rules, exclude globs, scan policy, last full-scan timestamp.
- **Item** — one catalogued file. Attributes: stable item identity (relative path within root plus content hash), display title, author(s), format, byte size, content hash (SHA-256 or equivalent), `added_at`, `last_seen_at`, `availability` enum {present, missing, moved-candidate, excluded}, user metadata fields, tags.
- **Collection / Shelf** — a named virtual grouping. A *static collection* holds an explicit member list; a *smart collection* holds a saved filter expression evaluated on read. An item belongs to zero or more collections.
- **Tag** — a flat or hierarchical label applied to items; tags are user-owned and never auto-deleted by a rescan.
- **Scan Run** — an append-only record of each discovery pass: started/finished timestamps, items added, items re-identified, items marked missing, errors.

## Item Identity

Identity is the load-bearing design decision of this module. Each item is keyed on two signals so that neither rename nor edit alone destroys continuity:

- **Relative path** within the library root locates the file.
- **Content hash** confirms the bytes.

A file whose path changed but whose hash is unchanged is a *moved* file, re-bound to the existing item with its metadata intact. A file whose path is unchanged but whose hash changed is an *edited-in-place* item, re-hashed with metadata retained. A file present at neither the prior path nor any new path with a matching hash is marked `missing` — its catalogue row and all user metadata are retained, not deleted.

## Key Workflows

1. **Initial scan.** The user selects a library root; the application enumerates eligible files honouring exclude globs, hashes each, and creates Item rows. Scanning runs on a background worker and never blocks the UI (NFR-PROD-005).
2. **Incremental rescan.** A subsequent scan compares the filesystem against the catalogue using modification time and size as a fast pre-filter, hashing only changed or new files. Unchanged items are touched with a new `last_seen_at` and skipped.
3. **Browse and filter.** The user views the corpus in list, grid/cover, or detail view; sorts by any indexed field; and filters by tag, collection, availability, format, or saved smart-collection expression.
4. **Inspect.** Selecting an item opens the item inspector showing all metadata fields, provenance, collection memberships, file path, and availability state.
5. **Bulk edit.** The user selects multiple items and applies a tag, collection membership, or field value to all in one transactional, reversible operation (NFR-PROD-010).

## Views and Browsing

The catalogue supports at least three views over the same item set: a dense **list view** for scanning many rows, a **cover / grid view** for visual recognition, and a **detail view** pairing a single item's metadata with a preview. Sort and filter state is shared across views so switching view does not reset the user's place. First-screen render and subsequent paging meet the catalogue-load budget (NFR-PROD-003).

## Edge Cases Worth Specifying

- **Renamed or moved file** — re-bound to the existing item by matching content hash; metadata and collection membership carry over; no user data is lost.
- **Duplicate files** — two paths with identical content hash are surfaced as a duplicate set; the user chooses a primary; the catalogue records both locations without forcing a delete.
- **Removed file** — marked `missing`, not deleted; the row, tags, annotations linkage, and metadata persist so that restoring the file (or pointing at a new location) re-binds the original item.
- **Very large libraries** — tens of thousands of items: scanning is incremental and resumable; browse paging and virtualised rendering hold to the catalogue-load budget; a full re-hash is never required for an unchanged corpus.
- **Excluded folders** — paths matching an exclude glob are skipped at scan time and reported under the `excluded` availability state so the user can audit what was left out.
- **Path moved outside the root** — a file moved out of the library root is treated as `missing` rather than silently dropped, with its identity preserved for re-binding if it returns.

## Representative Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| **FR-CAT-001** | When the user selects a library root, the system shall enumerate eligible files, compute a content hash for each, and create one Item per file on a background worker. | MVP | Given a root of N eligible files, when the scan completes, then N Item rows exist, each with a non-empty relative path and content hash, and the UI thread shows no stall exceeding 100 ms. |
| **FR-CAT-002** | When the user triggers a rescan, the system shall hash only files whose modification time or size changed since `last_seen_at` and shall leave unchanged items untouched except for `last_seen_at`. | MVP | Given a corpus with 1 changed file among 10,000, when rescan runs, then exactly 1 file is re-hashed and the other 9,999 retain their prior hash and metadata. |
| **FR-CAT-003** | When a catalogued file is found at a new path with an unchanged content hash, the system shall re-bind it to the existing Item and preserve all user metadata, tags, and collection membership. | MVP | Given an item in 2 collections with 3 tags, when its file is moved within the root and a rescan runs, then the same Item row references the new path and retains the 2 collections and 3 tags. |
| **FR-CAT-004** | When a catalogued file is no longer present at its path and no hash match is found, the system shall mark the Item `missing` and shall retain its row and all user metadata. | MVP | Given a deleted source file, when rescan runs, then the Item availability is `missing` and a subsequent inspector view shows all prior metadata intact. |
| **FR-CAT-005** | When two Items share an identical content hash, the system shall present them as a duplicate set and shall let the user designate a primary without deleting either file. | V1 | Given 2 identical files in the root, when the duplicate view is opened, then both appear in one set and selecting a primary leaves both files on disk. |
| **FR-CAT-006** | When the user defines a smart collection from a filter expression, the system shall evaluate membership on read so that newly imported matching items appear without manual re-add. | V1 | Given a smart collection filtered on tag `x`, when an item is tagged `x`, then it appears in that collection on next view without an explicit add. |
| **FR-CAT-007** | When the user applies a bulk edit to a selection, the system shall apply it transactionally with a single-action undo and shall leave the catalogue unchanged on partial failure. | V1 | Given a 500-item selection, when a bulk tag is applied and interrupted mid-write, then either all 500 carry the tag or none do, and one undo reverts the applied change. |
| **FR-CAT-008** | When the user adds an exclude glob to a library root, the system shall skip matching paths on the next scan and shall report them under the `excluded` state. | V1 | Given an exclude glob `**/drafts/**`, when scan runs, then no file under any `drafts` directory becomes a `present` Item and the excluded count is reported. |
| **FR-CAT-009** | When the user opens the item inspector, the system shall display every metadata field, its provenance, file path, availability, and collection memberships for the selected item. | MVP | Given a selected item, when the inspector opens, then all populated fields, the source path, and availability state are shown. |
| **FR-CAT-010** | When a corpus of at least 50,000 items is loaded, the system shall render the first screen of catalogue results within the catalogue-load budget and shall page subsequent results within budget. | V1 | Given a 50,000-item corpus on reference hardware, when the catalogue opens, then first-screen render is within 1 second at P95 and paging within 200 ms at P95 (NFR-PROD-003). |

## Data and Entities Owned

This module owns Library Root, Item, Collection/Shelf, Tag, and Scan Run records, and the item-identity binding (relative path + content hash). Other modules reference Items by identity but do not own the identity mapping.

## Applicable NFR Defaults

Inherit NFR-PROD-001 (local-first availability), NFR-PROD-002 (cold-start), NFR-PROD-003 (catalogue-load latency), NFR-PROD-005 (non-blocking background scan), NFR-PROD-009 (data portability and export of catalogue), NFR-PROD-010 (reversible destructive and bulk operations), NFR-PROD-013 (local audit trail for bulk destructive operations).
