# Industrial Modules - Low-Level Design

## Overview

This section specifies the service-layer design for the industrial modules introduced into Longhorn ERP: Product Lifecycle Management (PLM) and Transportation & Fleet Operations. These services are add-on modules and must be protected by `ModuleRegistry::isActive()` checks before any controller or endpoint dispatches work into them.

---

## PLMItemService

**Namespace:** `App\Modules\PLM`

**Module guard:** `ModuleRegistry::isActive('PLM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createItem(array $data): int` | Engineering item payload containing `item_code`, `name`, `item_class`, `uom_id`, and initial revision metadata | New `plm_items.id` | Creates the engineering item header and its first draft revision inside a single transaction. |
| `createRevision(int $itemId, array $data): int` | Engineering item primary key, revision payload | New `plm_item_revisions.id` | Creates a successor draft revision for a released or superseded item. Carries forward document and BOM linkage rules where configured. |
| `getRevisionHistory(int $itemId): array` | Engineering item primary key | Ordered revision array | Returns full revision chain newest first. |

**Tables read/written:** `plm_items`, `plm_item_revisions`

---

## EngineeringChangeService

**Namespace:** `App\Modules\PLM`

**Module guard:** `ModuleRegistry::isActive('PLM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `PLMItemService`, `PLMPublicationService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `submitEcr(array $data): int` | ECR payload containing affected object, reason, impact summary, and requested effective date | New `plm_ecrs.id` | Inserts an ECR in `submitted` state after validating the target object is under PLM control. |
| `approveEcr(int $ecrId, string $roleCode, string $note): void` | ECR primary key, approver role code, note | `void` | Records role-specific approval. When both required approval tracks exist, transitions ECR to `approved`. |
| `releaseEco(int $ecoId): void` | ECO primary key | `void` | Validates release blockers, sets ECO to `released`, and delegates downstream publication to `PLMPublicationService`. |

**Tables read/written:** `plm_ecrs`, `plm_eco_approvals`, `plm_ecos`, `plm_release_log`

---

## PLMDocumentService

**Namespace:** `App\Modules\PLM`

**Module guard:** `ModuleRegistry::isActive('PLM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `FileStorageService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `attachDocument(int $revisionId, array $meta, string $tmpPath): int` | Revision primary key, metadata array, temporary upload path | New `plm_documents.id` | Stores the file, computes checksum, writes the document row, and links it to the revision. |
| `markMandatoryForClass(string $itemClass, string $documentType): void` | Item class code, document type code | `void` | Updates the mandatory-release rules for the tenant. |
| `validateReleaseReadiness(int $revisionId): array` | Revision primary key | Array of blocking issues | Returns missing document or expired compliance blockers. |

**Tables read/written:** `plm_documents`, `plm_document_rules`

---

## NPIService

**Namespace:** `App\Modules\PLM`

**Module guard:** `ModuleRegistry::isActive('PLM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createProgramme(array $data): int` | NPI payload with owner, release target, budget notes, and product family context | New `plm_npi_programmes.id` | Creates a new NPI programme in `concept` state. |
| `advanceStage(int $programmeId, string $targetStage): void` | NPI programme primary key, target stage code | `void` | Validates stage-gate checklist completion and required approvals before transition. |
| `getStageSummary(int $programmeId): array` | NPI programme primary key | Checklist and status summary | Returns stage progress, unresolved risks, and blocker counts. |

**Tables read/written:** `plm_npi_programmes`, `plm_npi_checklists`, `plm_npi_risks`

---

## PLMPublicationService

**Namespace:** `App\Modules\PLM`

**Module guard:** `ModuleRegistry::isModuleActive('PLM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `InventorySyncService`, `ManufacturingSyncService`, `ProcurementSyncService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `publishRevision(int $revisionId): int` | Revision primary key | New `plm_publication_events.id` | Creates a publication event record and dispatches sync handlers for each enabled downstream consumer. |
| `retryPublication(int $eventId): void` | Publication event primary key | `void` | Retries failed downstream deliveries using the stored publication payload. |
| `getPublicationStatus(int $revisionId): array` | Revision primary key | Per-consumer status array | Returns consumer delivery states and last-attempt metadata. |

**Tables read/written:** `plm_publication_events`, `plm_publication_targets`, `plm_release_log`

---

## ShipmentPlanningService

**Namespace:** `App\Modules\Transportation`

**Module guard:** `ModuleRegistry::isActive('TRANSPORTATION', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createShipmentOrder(array $data): int` | Shipment payload from Sales, Procurement, Inventory transfer, or manual request | New `shipment_orders.id` | Creates a transport-demand object with source document references and dimensional data. |
| `listUnplanned(array $filters): array` | Filter array (`branch_id`, `service_priority`, `date_from`, `date_to`) | Shipment order list | Returns all open shipment orders not yet assigned to a load or active route. |
| `assignToLoad(int $shipmentOrderId, int $loadId): void` | Shipment order primary key, load primary key | `void` | Links the shipment to a load after validating tenant, status, and planning compatibility. |

**Tables read/written:** `shipment_orders`, `transport_loads`, `transport_load_shipments`

---

## RoutePlanningService

**Namespace:** `App\Modules\Transportation`

**Module guard:** `ModuleRegistry::isActive('TRANSPORTATION', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `ShipmentPlanningService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createRoute(array $data): int` | Route payload with departure plan, assigned load, and ordered stops | New `transport_routes.id` | Creates the route header and stop rows in a single transaction. |
| `validateCapacity(int $routeId): array` | Route primary key | Capacity check result array | Computes aggregate weight, volume, and stop-count versus selected resource profile. |
| `resequenceStops(int $routeId, array $stopIds): void` | Route primary key, ordered stop identifiers | `void` | Rewrites stop sequence numbers and planned arrival ordering. |

**Tables read/written:** `transport_routes`, `transport_route_stops`, `carrier_profiles`, `vehicle_capacity_profiles`

---

## DispatchService

**Namespace:** `App\Modules\Transportation`

**Module guard:** `ModuleRegistry::isActive('TRANSPORTATION', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `VehicleAvailabilityService`, `NotificationService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `dispatchRoute(int $routeId, array $assignment): int` | Route primary key, assignment payload for internal fleet or external carrier | New `transport_trips.id` | Validates resource availability, marks route `dispatched`, creates trip record, and emits dispatch notification. |
| `cancelDispatch(int $tripId, string $reason): void` | Trip primary key, reason text | `void` | Cancels trip before departure and returns route to `planned` state if no milestone has been posted. |
| `getDispatchBoard(array $filters): array` | Branch/date/status filters | Route and trip board rows | Returns operational dispatch-board state. |

**Tables read/written:** `transport_trips`, `transport_routes`, `transport_resource_assignments`, `notification_log`

---

## TripExecutionService

**Namespace:** `App\Modules\Transportation`

**Module guard:** `ModuleRegistry::isActive('TRANSPORTATION', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `ExceptionService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `recordMilestone(int $tripId, array $event): int` | Trip primary key, milestone payload | New `transport_trip_events.id` | Writes the milestone event, recalculates ETA, and triggers exception evaluation. |
| `captureProof(int $tripId, int $stopId, array $proof): int` | Trip primary key, stop primary key, proof payload | New `transport_proofs.id` | Stores proof metadata and optional image/document path. |
| `closeTrip(int $tripId, array $closeout): void` | Trip primary key, close-out payload with actual times and costs | `void` | Validates stop completion and closes the trip. |

**Tables read/written:** `transport_trip_events`, `transport_proofs`, `transport_routes`, `transport_route_stops`, `transport_trips`

---

## ExceptionService

**Namespace:** `App\Modules\Transportation`

**Module guard:** `ModuleRegistry::isActive('TRANSPORTATION', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `NotificationService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `evaluateTripState(int $tripId): void` | Trip primary key | `void` | Computes late-stop thresholds and creates or updates transport exceptions. |
| `assignException(int $exceptionId, int $userId): void` | Exception primary key, user primary key | `void` | Changes exception ownership and logs reassignment. |
| `resolveException(int $exceptionId, string $resolutionCode, string $note): void` | Exception primary key, resolution code, note | `void` | Marks exception resolved and stores outcome context. |

**Tables read/written:** `transport_exceptions`, `notification_log`

---

## FreightSettlementService

**Namespace:** `App\Modules\Transportation`

**Module guard:** `ModuleRegistry::isActive('TRANSPORTATION', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `submitSettlement(array $data): int` | Settlement payload for carrier invoice or internal trip close-out | New `transport_settlements.id` | Creates a settlement in `submitted` or `audit_hold` state based on variance rules. |
| `approveSettlement(int $settlementId, string $note): void` | Settlement primary key, approval note | `void` | Approves a held settlement and posts payables or internal cost allocations to the GL. |
| `getLaneAnalytics(array $filters): array` | Date and lane filters | Aggregated analytics rows | Returns transport performance by lane, carrier, vehicle, and customer. |

**Tables read/written:** `transport_settlements`, `transport_settlement_lines`, `transport_lane_costs`
