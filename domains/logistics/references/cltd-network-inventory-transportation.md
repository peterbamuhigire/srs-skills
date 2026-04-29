# CLTD Network, Inventory, and Transportation Requirements

Use this reference when generating requirements for logistics, distribution, wholesale, import/export, fleet, ERP, WMS, TMS, agriculture aggregation, manufacturing dispatch, and branch replenishment projects.

## Requirement Themes

- Logistics network design must identify suppliers, ports, borders, plants, warehouses, cross-docks, branches, customer zones, trade lanes, carriers, and reverse-logistics flows.
- Service-level commitments must be tested against total logistics cost: transportation, warehouse handling, storage, safety stock, delivery frequency, customs clearance, returns, and administration.
- Inventory requirements must distinguish cycle stock, safety stock, WIP, finished goods, packaging, spares, consigned stock, quarantined stock, returns, and in-transit stock where applicable.
- Transportation requirements must cover mode selection, carrier/fleet assignment, dispatch, route planning, tracking, expediting, consolidation, proof of delivery, claims, and returns.
- International logistics requirements must include Incoterms, customs broker role, commercial invoice, packing list, BOL/waybill, customs declaration, duties, clearance status, and transfer of cost/risk.
- Logistics outsourcing requirements must distinguish carrier, freight forwarder, 3PL, 4PL, and lead-logistics-provider responsibilities, SLAs, integrations, and escalation paths.

## Functional Requirement Prompts

- Can users map and maintain network nodes, lanes, lead times, transport modes, carriers, cost basis, and service-level targets?
- Can inventory policy be configured by SKU, ABC class, location, supplier, lead time, MOQ, review method, and safety-stock service level?
- Does replenishment consider on-hand, reserved, backordered, scheduled receipt, in-transit, quarantined, damaged, and expired quantities?
- Can the system create, track, and reconcile shipments for customer orders, supplier inbound, branch transfers, returns, and reverse logistics?
- Can users generate and retain shipment documents, labels, proof of delivery, freight bills, customs documents, and claims evidence?
- Can dispatchers select carrier or fleet options based on service level, lane, capacity, cost, compliance, tracking capability, and performance history?
- Are delays, damage, shortages, refused delivery, lost goods, vehicle breakdown, customs hold, and route disruption handled as explicit exception workflows?
- Can management compare own fleet, hired carrier, courier, freight forwarder, 3PL, 4PL, and lead-logistics-provider options without changing the core order lifecycle?

## Non-Functional Requirement Prompts

- Shipment and stock events must be auditable, timestamped, actor-attributed, and immutable or correction-based.
- Tracking and inventory availability must update within the business's promised operational latency.
- The system must preserve service and cost history for carrier scorecards, claims, network redesign, and cost-to-serve analysis.
- Offline or degraded-mode workflows must be considered for warehouses, depots, drivers, and border/field locations with weak connectivity.
- Access control must separate sales, warehouse, dispatch, procurement, finance, customs/compliance, and carrier/LSP users.

## Metrics to Require

- Fill rate, stockout rate, backorder rate, and backorder age
- Inventory turnover, inventory days, safety-stock coverage, slow stock, obsolete stock, and carrying cost
- Dock-to-stock time, pick accuracy, inventory accuracy, and order fulfilment cycle time
- On-time pickup, on-time delivery, OTIF, route adherence, and exception closure time
- Transport cost per order, unit, km, tonne-km, or sales value
- Load utilisation, empty running, fleet utilisation, idle time, maintenance downtime, and backhaul contribution
- Freight claims, damage rate, loss rate, claims recovery, documentation error rate, customs clearance lead time, and carrier/LSP scorecard

## ERP Design Notes for Longhorn and BIRDC-Style Systems

- Treat fulfilment as a cross-module workflow spanning sales, inventory, warehouse, dispatch, finance, customer service, procurement, and reporting.
- For agriculture or factory ERP, model inbound aggregation, batch/lot traceability, quarantine, processing release, finished-goods staging, export dispatch, claims, and returns.
- For Uganda-first ERP, keep support for local tax/accounting controls separate from logistics documents so EFRIS or finance postings do not replace BOL, waybill, POD, or customs evidence.
- Do not hide stockout, backorder, or shipment exceptions inside comments; expose them as workflow states with owners, SLA clocks, escalation, and financial impact.
