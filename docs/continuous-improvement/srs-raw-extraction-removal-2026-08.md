# SRS Raw-Extraction Remediation

**Date:** 2026-08-04  
**Reason:** The source-ingestion guardrail identified seven tracked files under `book-extractions/` as full-text-style book reconstructions or raw extraction material. The repository contract requires concise, provenance-aware synthesis instead.

## Action

The seven flagged raw files were removed from the SRS repository after an SHA-256 verified backup was created at:

`C:\Users\Peter\Downloads\srs-book-extractions-backup-2026-08-04`

Removed files:

- `book-extractions/hacking-saas.md`
- `book-extractions/how-to-run-a-saas-business.md`
- `book-extractions/multi-tenant-saas-architectures.md`
- `book-extractions/saas-email-marketing-playbook.md`
- `book-extractions/saas-playbook-walling.md`
- `book-extractions/saas-sales-method-account-executives.md`
- `book-extractions/saas-sales-method-fundamentals.md`

The smaller, purpose-built SRS synthesis and audit records remain in the repository. They are retained because they express concise implementation guidance rather than reconstructive source text.

## Safety and provenance

- No file was removed before the external backup was verified by hash.
- No book text was copied into a new engine file.
- Future book intake must produce a concise synthesis, source status, limitations, and implementation decision instead of a raw extraction.
- The Digital Research engine remains the route for evidence evaluation and current-source verification.

## Acceptance evidence

- Backup exists and hashes matched before removal.
- `source_ingestion_guardrail.py` must report zero findings after this change.
- SRS skill-contract, routing, and engine validators must remain green.
