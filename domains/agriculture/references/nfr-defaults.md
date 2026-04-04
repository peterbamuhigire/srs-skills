# Agriculture: Default Non-Functional Requirements

These requirements are auto-injected into new agriculture project scaffolds.
All blocks are tagged `[DOMAIN-DEFAULT: agriculture]` for consultant review.

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-001: Offline Operation Capability
The system shall support full offline operation for core farm management functions
including crop activity logging, expense recording, and livestock health event
capture. All data created offline shall persist in the local database and
synchronise with the server within 30 seconds of connectivity restoration.

**Verifiability:** Disable network connectivity on the device; create a crop
activity record, log an expense, and record a livestock health event. Verify all
3 records persist in the local database. Re-enable connectivity; verify all 3
records appear on the server within 30 seconds.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-002: Farm Boundary Data Encryption
The system shall encrypt all GPS farm boundary data stored as GeoJSON using
AES-256 encryption at rest. Unencrypted farm boundary coordinates shall not
exist on any persistent storage medium.

**Verifiability:** Inspect the raw database storage for a farm boundary record;
the GeoJSON field must be unreadable without the decryption key. Verify key
management follows NIST SP 800-57 guidelines.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-003: Financial Transaction Audit Trail
The system shall produce an immutable audit log entry for every income, expense,
and payment operation. The audit log shall be append-only; modification and
deletion of log entries shall be rejected by the system.

**Verifiability:** Create a financial transaction (income or expense); verify
that an audit log entry is created containing: user_id, timestamp, action,
amount, and tenant_id. Attempt to modify or delete the log entry; the system
shall reject the operation with an appropriate error.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-004: API Response Time
The system shall maintain a P95 response time of ≤ 500 ms for all CRUD
operations under a load of 1,000 concurrent authenticated users.

**Verifiability:** Execute a load test simulating 1,000 concurrent users
performing standard CRUD operations (create farm record, read dashboard,
update crop activity, delete draft). Measure P95 response time; it shall
not exceed 500 ms.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-005: Mobile App Cold Start
The mobile application shall complete cold start and reach an interactive state
within 3 seconds on a device with 2 GB RAM.

**Verifiability:** Force-stop the application on a Tecno Spark device with 2 GB
RAM. Launch the application and measure time from tap to interactive (first
screen fully rendered and responsive to input). The measured time shall not
exceed 3 seconds.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-006: Multi-Lingual Support
All user-facing text in the system shall be translatable via the translation
table. The active display language shall be switchable per user without
requiring an application restart.

**Verifiability:** Navigate to language settings; switch the display language
from English to Luganda (or another supported locale). Verify that all UI
labels, menu items, and system messages update immediately without restarting
the application.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-007: Data Sync Conflict Resolution
When the same record is modified on two devices while both are offline, the
system shall resolve the conflict using a last-write-wins strategy based on
device-local timestamps and shall log the conflict for farmer review.

**Verifiability:** Modify the same record on two devices while both are offline.
Reconnect both devices. Verify that the version with the latest timestamp is
the active version. Verify that the conflict log contains both versions with
their respective timestamps and device identifiers.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-008: Low Bandwidth Adaptation
The application shall detect connection quality and switch to a text-only,
compressed-response mode when available bandwidth falls below 256 kbps.

**Verifiability:** Throttle the device connection to 128 kbps. Verify that
the application suppresses image loading, uses compressed API responses,
and remains functionally usable. Restore full bandwidth; verify the
application returns to normal rendering mode.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-009: Tenant Data Isolation
No tenant shall be able to access, query, or infer data belonging to another
tenant. Tenant isolation shall be enforced at the API layer on every request.

**Verifiability:** Authenticate as Tenant A. Attempt an API call using a
resource ID belonging to Tenant B. The system shall return HTTP 403 Forbidden
or HTTP 404 Not Found. Repeat for all resource endpoints; no cross-tenant
data leakage shall occur.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: agriculture] Source: domains/agriculture/references/nfr-defaults.md -->
#### NFR-AG-010: Photo Compression Before Upload
All photo attachments captured within the application shall be compressed
client-side to a maximum file size of 512 KB before upload.

**Verifiability:** Capture or select a 5 MB photo within the application.
Verify that the transmitted upload payload does not exceed 512 KB. Verify
that the compressed image retains sufficient resolution and clarity for
pest and disease identification by visual inspection.
<!-- [END DOMAIN-DEFAULT] -->
