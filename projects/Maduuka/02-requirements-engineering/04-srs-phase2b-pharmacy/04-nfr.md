---
title: "SRS Phase 2b — Pharmacy/Drug Store Add-on Module (F-012)"
subtitle: "Section 4: Non-Functional Requirements"
project: Maduuka
version: 0.1-draft
date: 2026-04-05
status: Draft — Pending Human Review
---

# Section 4: Non-Functional Requirements for the Pharmacy/Drug Store Module

Non-functional requirements (NFRs) in this section define measurable quality thresholds per IEEE 830-1998. Each NFR specifies the condition, the metric, the measurement method, and the pass/fail criterion. Vague qualifiers ("fast", "reliable", "robust") are prohibited per CLAUDE.md Principle 7.

---

## 4.1 Performance

**NFR-PHR-P-001 — Allergy Alert Display Latency**

- *Condition:* A product is added to the pharmacy dispensing cart and the patient has 1 or more allergen entries.
- *Metric:* Time from add-to-cart confirmation to allergy alert display.
- *Threshold:* ≤ 300 ms at P95 under normal operating load (defined as ≤ 50 concurrent pharmacy POS sessions per tenant cluster).
- *Measurement method:* Synthetic transaction test injecting a cart add event against a patient with 10 allergen entries; P95 latency measured over 1,000 runs.
- *Pass criterion:* P95 latency ≤ 300 ms with 0 missed alerts (every allergy match must trigger a display event).

**NFR-PHR-P-002 — Drug Reference Search Response Time**

- *Condition:* A user enters a search term of 3 or more characters in the drug reference search field.
- *Metric:* Time from search submission to first result row rendered in the UI.
- *Threshold:* ≤ 500 ms at P95 under normal operating load.
- *Measurement method:* Synthetic search test against a drug reference database of 5,000 drug records (generic + brand names) using randomised 3–8 character search terms; P95 latency measured over 500 runs.
- *Pass criterion:* P95 latency ≤ 500 ms. Result set must include all matches with Levenshtein distance ≤ 2 (per FR-PHR-048).

**NFR-PHR-P-003 — Controlled Drugs Register Write Latency**

- *Condition:* A dispensing transaction for a controlled substance is committed.
- *Metric:* Time from dispensing confirmation to controlled drugs register entry being durably written to the database.
- *Threshold:* ≤ 1 second at P99 under normal operating load.
- *Measurement method:* Transaction commit timestamp compared against register entry `created_at` timestamp in the database; P99 latency measured over 500 controlled dispensing events in a load test environment.
- *Pass criterion:* P99 latency ≤ 1 second. Zero transactions committed without a corresponding register entry (register completeness = 100%).

**NFR-PHR-P-004 — NDA Audit Log Export Generation Time**

- *Condition:* An NDA audit log export is requested for a 12-month date range.
- *Metric:* Time from export request to file being available for download (PDF and CSV both generated).
- *Threshold:* ≤ 10 seconds for a 12-month dataset containing up to 10,000 register entries.
- *Measurement method:* Export request fired against a test tenant seeded with 10,000 controlled drugs register entries spanning 12 months; wall-clock time measured from request to download-ready state.
- *Pass criterion:* Export completes in ≤ 10 seconds. Generated PDF and CSV files must contain all register entries within the requested date range with no omissions.

**NFR-PHR-P-005 — Patient Search Response Time**

- *Condition:* A user enters 2 or more characters in the patient search field.
- *Metric:* Time from search submission to result list rendered.
- *Threshold:* ≤ 500 ms at P95 (per FR-PHR-004).
- *Measurement method:* Synthetic search against a tenant with 10,000 patient records; P95 latency over 500 runs.
- *Pass criterion:* P95 latency ≤ 500 ms.

---

## 4.2 Security and Data Integrity

**NFR-PHR-S-001 — Patient PII Encryption at Rest**

- *Metric:* Patient PII fields (name, NIN, DOB, phone, allergy records, prescription data) shall be encrypted at rest using AES-256.
- *Pass criterion:* Verified by security audit confirming no PII field stored in plaintext in the database.

**NFR-PHR-S-002 — Controlled Drugs Register Immutability Assurance**

- *Metric:* The SHA-256 hash stored per register entry (FR-PHR-075) shall match a recomputed hash of the stored entry content on every audit read.
- *Pass criterion:* 0 hash mismatches detected across all register entries in the compliance audit report.

**NFR-PHR-S-003 — NDA Inspector Session Timeout**

- *Metric:* An NDA Inspector session shall auto-expire after 60 minutes of inactivity.
- *Pass criterion:* Session token invalidated within 5 seconds of the 60-minute inactivity threshold.

---

## 4.3 Reliability

**NFR-PHR-R-001 — Controlled Drugs Register Durability**

- *Metric:* The controlled drugs register must be durable — no register entry shall be lost in the event of an application server failure occurring after dispensing confirmation.
- *Threshold:* Recovery Point Objective (RPO) = 0 for controlled drugs register entries (write-ahead log or equivalent synchronous persistence required).
- *Pass criterion:* Post-failure recovery test confirms 0 register entries lost when server is killed immediately after dispensing confirmation.

**NFR-PHR-R-002 — Allergy Alert Availability**

- *Metric:* The allergy check service (FR-PHR-033) shall be available whenever the pharmacy POS is available. If the allergy check service is unavailable, the pharmacy POS shall prevent dispensing entirely rather than silently bypass the allergy check.
- *Pass criterion:* With allergy service mocked as unavailable, POS displays: "Allergy check unavailable. Dispensing is suspended until the service is restored." Zero dispensing events processed without an allergy check result.
