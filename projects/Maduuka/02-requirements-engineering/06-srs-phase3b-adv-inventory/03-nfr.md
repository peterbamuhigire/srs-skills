---
title: "SRS Phase 3b -- Advanced Inventory: Non-Functional Requirements"
project: "Maduuka"
version: "1.0"
date: "2026-04-05"
status: "Draft"
---

# Section 3: Non-Functional Requirements -- Advanced Inventory (F-014)

All performance thresholds below apply under normal load, defined as: up to 500 concurrent active users per tenant, standard cloud infrastructure (minimum 4 vCPU, 8 GB RAM application tier), and a relational database with indexes maintained per the Maduuka database maintenance schedule.

---

## 3.1 Performance

**NFR-AINV-P-001:** The cross-warehouse availability query (FR-AINV-006) shall return the aggregate available stock and per-warehouse breakdown within 500 ms at P95 for tenants with up to 50 active warehouses and product catalogues of up to 10,000 SKUs.

**NFR-AINV-P-002:** The serial number search query (FR-AINV-018) shall return the matching serial number record and its complete movement history within 300 ms at P95.

**NFR-AINV-P-003:** The batch recall notification list (FR-AINV-028) shall be generated and presented to the user within 5 seconds for recall events affecting up to 10,000 sale transactions linked to the recalled batch.

**NFR-AINV-P-004:** The demand forecast calculation (FR-AINV-059, FR-AINV-061) for the full product catalogue shall complete within 10 seconds at P95 for catalogues of up to 10,000 SKUs. Pre-calculated cache values shall be refreshed at least once per hour automatically.

**NFR-AINV-P-005:** The production order material requirement calculation (FR-AINV-048) shall complete and display the full raw material requirement list within 2 seconds at P95 for BOMs with up to 50 raw material lines.

**NFR-AINV-P-006:** Compliance audit reports (FR-AINV-068, FR-AINV-069, FR-AINV-071) shall complete rendering within 15 seconds at P95 for periods of up to 12 months and movement records of up to 500,000 rows.

---

## 3.2 Data Integrity

**NFR-AINV-DI-001:** All stock movement records created by F-014 operations (production consumption, production output, landed cost allocation updates, transfer-in, transfer-out, transfer-cancel) shall be immutable once committed. No update or delete operation shall be permitted on a committed movement record at the database layer.

**NFR-AINV-DI-002:** Landed cost allocation records (FR-AINV-038) shall be stored as append-only records. Corrections shall create new adjustment records referencing the original allocation, preserving the full audit trail.

**NFR-AINV-DI-003:** BOM versioning (FR-AINV-045) shall ensure that completed production orders retain a permanent reference to the BOM version used at the time of the order. Deletion of a BOM version that is referenced by a production order shall be prevented.

---

## 3.3 Scalability

**NFR-AINV-SC-001:** The multi-warehouse data model shall support up to 200 active warehouses per tenant without architectural changes, with the cross-warehouse availability query remaining within the NFR-AINV-P-001 threshold up to 50 warehouses. Performance degradation beyond 50 warehouses is permitted provided it degrades linearly (not exponentially).

**NFR-AINV-SC-002:** The serial number registry shall support up to 1,000,000 serial number records per tenant. Search performance (FR-AINV-018) shall remain within the 300 ms threshold at this volume.

---

## 3.4 Availability

**NFR-AINV-AV-001:** F-014 advanced inventory features shall share the Maduuka platform availability SLA of 99.5% uptime per calendar month, excluding scheduled maintenance windows communicated at least 48 hours in advance.

---

## 3.5 Audit and Compliance

**NFR-AINV-AC-001:** Every F-014 action that modifies stock, costs, or production records shall write an audit log entry containing: tenant ID, user ID, action type, affected record IDs, before-value (where applicable), after-value, and UTC timestamp. Audit logs shall be retained for a minimum of 7 years to support tax and regulatory audit requirements applicable in Uganda.
