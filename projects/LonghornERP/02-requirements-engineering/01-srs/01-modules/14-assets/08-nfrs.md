# Non-Functional Requirements for the Asset Management Module

## 8.1 Overview

Non-functional requirements (NFRs) define the quality and constraint envelope within which all functional behaviour specified in Sections 2 through 7 must operate. Each NFR carries a unique identifier in the `NFR-ASSET-NNN` series and states a specific, measurable metric per IEEE 982.1. No NFR uses vague qualifiers such as "fast," "reliable," or "robust" without a defined threshold.

## 8.2 Performance

**NFR-ASSET-001:** The system shall complete a monthly depreciation run for up to 5,000 active assets — computing both book and tax depreciation and posting all resulting GL journals — within ≤ 30 seconds, measured end-to-end from the user's run initiation request to the confirmation screen display, under a concurrent load of 20 active tenant sessions.

**NFR-ASSET-002:** The system shall return the asset list view (paginated, 50 records per page) for a tenant with up to 20,000 asset records within ≤ 2 seconds at P95 under a load of 50 concurrent sessions.

**NFR-ASSET-003:** The system shall compute and display an individual asset's depreciation schedule (full useful-life projection) within ≤ 1 second at P95 after the user opens the depreciation schedule screen.

**NFR-ASSET-004:** The system shall generate the Book vs. Tax Depreciation Report for up to 5,000 assets within ≤ 15 seconds at P95.

**NFR-ASSET-005:** The system shall render a batch asset QR label PDF for up to 200 assets within ≤ 10 seconds at P95.

## 8.3 Data Integrity

**NFR-ASSET-006:** Every GL journal posted by the Asset Management module — whether for depreciation, revaluation, disposal, transfer, or deferred tax — shall be posted within a single atomic database transaction; if any line fails, the entire transaction shall be rolled back with no partial postings.

**NFR-ASSET-007:** The system shall prevent any direct `UPDATE` or `DELETE` operation on posted depreciation journal records, disposal records, and revaluation records at both the application layer (role check) and the database layer (trigger or row-level security policy).

**NFR-ASSET-008:** The system shall maintain referential integrity between the `asset_depreciation_runs` table and the `assets` table; deletion of an asset record with associated depreciation run entries shall be rejected by a database-level foreign key constraint.

**NFR-ASSET-009:** The system shall ensure that the sum of all depreciation charges posted for an asset from acquisition through disposal never exceeds *Cost − ResidualValue*; the depreciation run shall enforce this ceiling per FR-ASSET-015 and log an anomaly alert if the ceiling is approached within 1% of the remaining depreciable amount.

## 8.4 Availability

**NFR-ASSET-010:** The Asset Management module shall be available 99.5% of each calendar month, excluding scheduled maintenance windows announced ≥ 48 hours in advance; availability is measured as the ratio of successful health-check responses to total health-check requests over the month.

**NFR-ASSET-011:** The depreciation run scheduler shall be fault-tolerant: if a scheduled run is interrupted by a server restart, the system shall detect the interrupted run on next startup and either complete or cleanly roll it back, with no partial postings left in the database.

## 8.5 Security

**NFR-ASSET-012:** All Asset Management API endpoints shall require a valid authenticated session token; unauthenticated requests shall return HTTP 401 within ≤ 200 ms.

**NFR-ASSET-013:** Role-based access control checks for asset operations (create asset, post depreciation run, approve revaluation, approve disposal, approve transfer) shall be enforced server-side on every request; client-side UI hiding of controls does not satisfy this requirement.

**NFR-ASSET-014:** All asset data served by the Asset Management API shall be transmitted over TLS 1.2 or higher; unencrypted HTTP connections to any asset endpoint shall be rejected with HTTP 301 redirect to HTTPS.

**NFR-ASSET-015:** The `tenant_id` used to scope all asset queries shall be read exclusively from the authenticated session context; any client-supplied `tenant_id` parameter in the request body or URL shall be ignored and an anomaly event shall be logged.

## 8.6 Auditability

**NFR-ASSET-016:** Every write operation on the `assets`, `asset_categories`, `asset_depreciation_runs`, `asset_revaluations`, `asset_disposals`, `asset_transfers`, `asset_insurance_policies`, `asset_maintenance_schedules`, and `asset_work_orders` tables shall produce an audit log entry within the same database transaction, capturing: table name, record ID, action (INSERT/UPDATE), changed fields with old and new values, user identity, IP address, and UTC timestamp.

**NFR-ASSET-017:** Audit log entries for the Asset Management module shall be retained for a minimum of 10 years to satisfy the statutory record-keeping requirements under the Uganda Companies Act and URA tax records obligations; entries older than 10 years may be archived to cold storage but must remain retrievable within 72 hours of an authorised retrieval request.

## 8.7 Compliance

**NFR-ASSET-018:** All depreciation computations and financial disclosures generated by the Asset Management module shall conform to IAS 16 (Property, Plant and Equipment) and IAS 12 (Income Taxes) as in force at the date of the depreciation run; if an IFRS amendment alters the computation methodology, the system's formulas and templates shall be reviewed and updated within 90 days of the amendment's effective date.

**NFR-ASSET-019:** The Physical Verification Discrepancy Report shall include a digital signature field for the Asset Manager and an approval date field to satisfy PPDA Act documentation requirements for public-sector tenants conducting statutory asset verification.
