# Feature: Metadata Enrichment

## Purpose and Scope

Improve the accuracy and completeness of catalogue metadata from three sources — the filename, the file's embedded metadata, and text extracted from its first pages — and, where the user permits, from external metadata providers. The metadata-enrichment module never blindly overwrites user-entered values: every proposed change is reviewable, confidence-scored, and field-attributed to its source. Optional write-back into the source file is gated behind a backup-write-verify-restore protocol so the user's originals are never put at risk for a metadata edit.

Scope is the *derivation and merge* of metadata. It does not own the catalogue schema (the library-catalogue module does); it proposes values into that schema under an explicit merge policy.

## Core Entities

- **Identifier Candidate** — a detected identifier (for example ISBN or DOI) with its source {filename, embedded, extracted-text} and a confidence score.
- **Provider** — an external metadata source behind a uniform provider interface. Attributes: name, capability (which fields it can supply), rate limit, auth requirement, enabled flag.
- **Enrichment Proposal** — a set of field-level suggested values for one Item, each value carrying its source provider, confidence score, and the existing value it would change.
- **Field Provenance** — a per-field record of where the current value came from {user, filename, embedded, extracted, provider:name} and when.
- **Write-Back Operation** — a record of an optional change written into the source file: pre-image backup reference, before/after diff, verify-opens result, and restore path.
- **Metadata Quality Score** — a per-Item completeness-and-confidence measure over the catalogued fields.

## Identifier Detection

Identifier detection runs in three passes, each contributing Identifier Candidates with a confidence score:

1. **Filename** — pattern-match the filename and path for embedded identifiers.
2. **Embedded metadata** — read the file's own metadata block (document properties, XMP, or equivalent).
3. **Extracted first pages** — scan the first pages' extracted text for identifier patterns.

Multiple candidates are ranked by confidence; a candidate is never promoted to an authoritative lookup key without crossing a configured confidence threshold.

## Merge Policy

The merge policy is the trust-critical rule of this module:

- **User edits win.** A field the user has set is never silently overwritten; a provider value that conflicts is offered as a reviewable suggestion, not applied.
- **Confidence-scored suggestions.** Each proposed value carries a confidence score and its source; the user reviews and accepts, edits, or rejects per field.
- **Field-level provenance.** Every stored value records its source and timestamp so the user can see why a field holds its current value and revert it.
- **No blind overwrite.** Batch enrichment proposes changes for review; it does not auto-commit conflicting values over user or higher-provenance data without confirmation.

## Provider Interface and Batch Enrichment

External lookups go through a uniform provider interface so no enrichment caller is coupled to one vendor. Any provider call is an off-device transmission and therefore subject to the privacy-tier preview and confirmation (NFR-PROD-011): the user sees the exact identifier or query being sent and the destination before it leaves the device. Batch enrichment respects each provider's declared rate limit, retries transient failures with backoff, runs on a background worker, and produces one reviewable Enrichment Proposal set for the user to confirm.

## Optional Write-Back

Write-back into the source file is opt-in and never required for cataloguing. When the user chooses it, the operation runs under a strict protocol so an original is never corrupted for a metadata edit:

1. Capture a verified pre-image backup of the source file.
2. Write the metadata change to the file.
3. Re-open the written file to verify it still parses and renders (*verify-opens*).
4. Record a before/after diff and the restore path.
5. On any verification failure, restore the pre-image automatically.

This mirrors NFR-PROD-010's backup-write-verify-restore guarantee applied to user files rather than the catalogue.

## Edge Cases Worth Specifying

- **Conflicting provider results** — two providers return different values for the same field; both are surfaced as competing suggestions with sources and confidence; neither auto-wins.
- **No match found** — lookup returns nothing; the Item is left unchanged, the attempt is recorded, and the user is told no match was found rather than shown a fabricated value.
- **Ambiguous identifiers** — a detected identifier maps to multiple works; the user is asked to disambiguate before any field is populated.
- **Write-back failure** — the written file fails verify-opens; the pre-image is restored automatically and the failure is recorded; the catalogue value is unaffected.
- **Offline operation** — with no network, identifier detection from filename, embedded metadata, and extracted text still runs; only external provider lookup is unavailable, and that path degrades to a recorded, retryable pending state rather than an error (NFR-PROD-001).

## Representative Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| **FR-META-001** | When enrichment runs for an Item, the system shall detect identifier candidates from filename, embedded metadata, and extracted first pages, each with a source and confidence score. | MVP | Given a file with an ISBN in its filename, when detection runs, then an Identifier Candidate is recorded with source `filename` and a confidence score. |
| **FR-META-002** | When a provider returns a value that conflicts with a user-entered field, the system shall present it as a reviewable suggestion and shall not overwrite the user value. | MVP | Given a user-set title and a different provider title, when enrichment completes, then the stored title remains the user value and the provider value appears as a pending suggestion. |
| **FR-META-003** | When the user accepts, edits, or rejects a proposed field value, the system shall record the resulting value's provenance with source and timestamp. | MVP | Given an accepted provider value, when it is applied, then Field Provenance for that field reads the provider name and the apply timestamp. |
| **FR-META-004** | Before any provider lookup, the system shall preview the exact identifier or query and destination provider and shall require confirmation. | MVP | Given an enrichment request, when a provider call would occur, then the payload preview is shown and no request is sent without a recorded confirmation (NFR-PROD-011). |
| **FR-META-005** | When batch enrichment runs, the system shall respect each provider's declared rate limit, retry transient failures with backoff, and run on a background worker. | V1 | Given a 1,000-Item batch against a provider with a stated rate limit, when the batch runs, then request pacing stays within the limit and the UI thread shows no stall exceeding 100 ms. |
| **FR-META-006** | When the user enables write-back for an Item, the system shall back up the source, write the change, verify the file re-opens, record a before/after diff, and restore the backup on any verification failure. | V1 | Given a write-back that produces an unparseable file, when verify-opens fails, then the pre-image is restored and the original opens unchanged. |
| **FR-META-007** | When two providers return conflicting values for one field, the system shall surface both with their sources and confidence and shall not auto-select either. | V1 | Given provider A and provider B returning different authors, when the proposal is shown, then both author values appear with their source and confidence and neither is applied automatically. |
| **FR-META-008** | When a lookup returns no match, the system shall leave the Item unchanged, record the attempt, and inform the user that no match was found. | MVP | Given an identifier with no provider record, when lookup completes, then no field changes and a no-match outcome is recorded. |
| **FR-META-009** | When a detected identifier is ambiguous, the system shall prompt the user to disambiguate before populating any field. | V2 | Given an identifier resolving to 2 works, when enrichment proceeds, then the user is asked to choose before any field is set. |
| **FR-META-010** | When the network is unavailable, the system shall still run filename, embedded, and extracted-text detection and shall mark provider lookups as pending and retryable. | V1 | Given no network, when enrichment runs, then local detection completes and provider lookups are queued as pending rather than failing the operation. |
| **FR-META-011** | The system shall compute and display a metadata quality score per Item reflecting field completeness and value confidence. | V2 | Given an Item with half its tracked fields populated from high-confidence sources, when the inspector opens, then a quality score is shown for that Item. |

## Data and Entities Owned

This module owns Identifier Candidate, Provider configuration, Enrichment Proposal, Field Provenance, Write-Back Operation, and Metadata Quality Score records. It writes accepted values into catalogue fields owned by the library-catalogue module and consumes extracted text produced by the pdf-reader module.

## Applicable NFR Defaults

Inherit NFR-PROD-001 (offline-capable local detection), NFR-PROD-005 (non-blocking batch enrichment), NFR-PROD-009 (export of metadata and provenance in open formats), NFR-PROD-010 (reversible write-back and metadata changes), NFR-PROD-011 (privacy-tier preview before provider lookups), NFR-PROD-013 (audit trail for metadata write-back to source files).
