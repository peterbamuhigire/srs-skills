# Productivity — Security Baseline

The threat model for a local-first desktop productivity application differs from that of a multi-tenant cloud service. There is no tenant-isolation boundary and no server-side attacker surface at the core, because the corpus lives on the user's machine. The dominant risks are: leakage of provider secrets, malicious or malformed imported documents, path-traversal against the configured library, supply-chain tampering of the installed binary, and silent off-device exfiltration of user content. The controls below address those risks.

## Secrets and Credential Storage

| Control | Requirement |
|---|---|
| Provider secrets at rest | API keys, tokens, and provider credentials MUST be stored in OS-native credential storage (Windows Credential Manager / DPAPI, macOS Keychain, Linux Secret Service / kwallet). They MUST NEVER be written to plaintext settings files, the application database, log files, or crash reports. |
| Redaction | Secrets MUST be redacted from all logs, error reports, telemetry, and the audit trail. A correlation ID, not the key, identifies a provider call. |
| Scope | Each secret is bound to the provider it authenticates and is retrievable only by the application process; it is never embedded in exported catalogues or backups. |
| Rotation and removal | Removing a provider MUST delete its secret from OS credential storage in the same action and record a credential-removal entry in the local audit trail. |

## Untrusted Document Handling

Imported documents — especially PDFs — are untrusted input. PDF parsers and renderers are a well-known exploit surface (embedded JavaScript, malformed object streams, font and image decoder bugs).

| Control | Requirement |
|---|---|
| Treat as untrusted | All imported document content MUST be treated as untrusted input regardless of source. |
| Rendering isolation | Document rendering and OCR SHOULD execute within a worker boundary (separate process or sandboxed worker) isolated from the catalogue and credential store, so a parser exploit cannot reach secrets or the catalogue of record. |
| Active content | Embedded JavaScript and auto-executing actions in documents MUST be disabled by default; external resource fetches initiated by document content MUST be blocked unless the user explicitly enables them. |
| Resource bounds | Render and OCR workers MUST enforce time and memory bounds so a malformed document degrades to a per-item failure rather than hanging or crashing the application. |

## File-Path and Library-Root Validation

| Control | Requirement |
|---|---|
| Root containment | Every file operation MUST validate the resolved, canonicalised path against the configured library root. A path that resolves outside the root is refused. |
| Symlink containment | The application MUST NOT follow symbolic links that resolve outside the library root without explicit per-action user consent, preventing a planted symlink from redirecting reads or writes outside the intended scope. |
| Write-back safety | Metadata write-back to source files MUST target only files within the validated root, MUST preserve the original (see NFR-PROD-010), and MUST record a write-back entry in the audit trail. |
| Traversal defence | Catalogue import MUST reject or quarantine entries whose names attempt directory traversal (for example `..` segments) rather than acting on the traversed path. |

## Application Integrity and Updates

| Control | Requirement |
|---|---|
| Code-signing | All public builds MUST be code-signed (Authenticode on Windows, Developer ID / notarization on macOS). The signature MUST be verified before an update is installed; an unsigned or tamper-detected artifact MUST be refused (see NFR-PROD-012). |
| Secure update channel | Update metadata and artifacts MUST be fetched over an authenticated, integrity-checked channel; the update descriptor MUST be signature-verified independently of transport. |
| Migration safety | Schema migrations MUST snapshot before applying and restore on verification failure, so a tampered or faulty update cannot corrupt the catalogue irreversibly. |

## Data at Rest

| Control | Requirement |
|---|---|
| Catalogue database | The embedded catalogue database (titles, tags, annotations, AI history, embeddings) MUST support optional encryption at rest, with the key held in OS credential storage rather than alongside the database. |
| Default posture | Where the platform provides full-disk encryption the application MAY rely on it for source files, but the catalogue database encryption option MUST be available for users who require defence against offline access to the device. |
| Backups | Backups produced by destructive-operation protection MUST inherit the same at-rest protection as the catalogue and MUST NOT contain provider secrets. |

## Off-Device Transmission Controls

| Control | Requirement |
|---|---|
| Default deny | No user content or metadata leaves the device unless the active privacy tier permits it and the user has confirmed the previewed payload (see NFR-PROD-011). |
| Single egress path | All off-device calls MUST route through the provider gateway (see `architecture-patterns.md`); no UI or feature module may open its own network connection to a provider, ensuring one enforceable egress chokepoint. |
| Audit | Every off-device transmission MUST produce a local audit entry naming the provider, purpose, payload scope, and active tier. |

## Local Security-Event Audit Log

A local, tamper-evident audit log (see NFR-PROD-013) MUST record at minimum:

- Provider-credential add, change, and removal.
- AI-mode / privacy-tier changes.
- Off-device transmissions.
- Metadata write-back to source files.
- Bulk destructive operations.
- Exports of catalogue, annotations, or audit log itself.

Each entry carries action, timestamp, affected scope, and active privacy tier. The log is user-viewable and user-exportable and MUST NOT be silently truncated; rotation, if any, MUST be append-only with retained integrity markers.
