# 4. Non-Functional Requirements

## 4.1 Performance

**NFR-HTL-001 — Room status board propagation latency:** When any room status change is committed, the updated status shall appear on all connected room status board clients within 2 seconds, measured at P95 under normal load (up to 200 rooms, up to 20 concurrent connected clients per property).

**NFR-HTL-002 — Availability check response time:** When a staff member queries room availability (FR-HTL-027), the system shall return results within 500 ms at P95 for properties with up to 500 rooms, measured from the moment the query is submitted to the moment results are rendered in the UI.

**NFR-HTL-003 — Folio load time:** When a staff member opens a guest folio, the complete folio including all charge line items shall render within 1 second at P95 for folios with up to 200 line items.

**NFR-HTL-004 — PDF invoice generation:** When a staff member requests a folio PDF export, the document shall be available for download within 5 seconds at P95 for folios with up to 200 line items.

## 4.2 Reliability and Data Integrity

**NFR-HTL-005 — Double-booking prevention (BR-015) — database-level enforcement:** The double-booking prevention constraint (FR-HTL-029, FR-HTL-030) shall be implemented as a database-level unique partial index (or equivalent database constraint) on the room assignment table, scoped to overlapping active date ranges. UI-layer validation alone is insufficient; the database constraint is the authoritative enforcement point and must reject conflicting inserts even if two concurrent requests bypass the UI simultaneously.

**NFR-HTL-006 — Hourly charge calculation precision:** The ceiling function applied in FR-HTL-064 shall operate on duration computed from timestamps stored to the nearest minute. The rounding behaviour shall be verified with the following test oracle: a check-in at 14:00 and a checkout at 16:01 shall produce a rounded duration of 3 hours (not 2), yielding $Charge = 3 \times HourlyRate$. A checkout at 16:00 (exactly 2 hours) shall produce 2 hours with no ceiling applied.

**NFR-HTL-007 — Folio immutability after checkout:** Once a folio is closed at checkout (FR-HTL-084), no charge, credit, or modification may alter the original posted entries. All corrections shall be supplementary records (BR-003). The system shall enforce this at the API layer, not only in the UI.

**NFR-HTL-008 — Audit trail completeness:** All create, edit, cancel, and delete events on reservations, folios, room status changes, and corporate account transactions shall be recorded in the append-only audit log (BR-003). The audit log entry shall include: entity type, entity ID, action, previous value, new value, user ID, and timestamp (UTC).

## 4.3 Security and Access Control

**NFR-HTL-009 — Tenant data isolation:** All F-013 database queries shall be scoped to the authenticated tenant's `franchise_id` (BR-001). No query path shall permit cross-tenant data access.

**NFR-HTL-010 — Guest ID document storage:** Guest ID document images shall be stored in tenant-scoped cloud storage with access restricted to authenticated users of the same tenant. Direct public URLs to ID images shall not be generated. Access shall be via short-lived signed URLs (maximum validity: 15 minutes). This requirement supports compliance with Uganda Data Protection and Privacy Act 2019 (GAP-002).

**NFR-HTL-011 — Role-based access control:** The following operations are restricted by role:

- Setting a room to Out of Order: Business Owner only.
- Approving early check-in override (FR-HTL-053): Manager or Business Owner.
- Applying folio discounts (FR-HTL-071): Manager or Business Owner.
- Posting folio charge reversals (FR-HTL-072): Manager or Business Owner.
- Approving corporate direct billing above credit limit (FR-HTL-091): Business Owner only.
- Viewing occupancy analytics (Section 3.9): Business Owner and Accountant only.

## 4.4 Usability

**NFR-HTL-012 — Billing mode prominence:** The billing mode selection control at check-in (FR-HTL-050) shall be rendered as a top-level UI element, not embedded in a collapsed section or secondary screen. The selected billing mode shall be permanently visible on the folio header throughout the stay.

**NFR-HTL-013 — Status board mobile readability:** On Android and iOS screen widths from 360 dp to 428 dp, the room status board shall display a minimum of 3 rooms per row in grid view; each cell shall display room number and status colour without truncation.

## 4.5 Scalability

**NFR-HTL-014 — Maximum tested property size:** Phase 3 is tested and supported for properties with up to 200 individual rooms. Properties exceeding 200 rooms may be onboarded but are not covered by Phase 3 performance guarantees; this threshold shall be documented in the subscription terms.
