# Introduction to the Transportation and Fleet Operations Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Transportation and Fleet Operations module of Longhorn ERP. It specifies how shipment demand, route planning, dispatch, execution visibility, fleet assignment, proof of delivery, freight audit, and transport analytics shall be managed as first-class operating workflows rather than as side effects of sales delivery or asset maintenance records.

## 1.2 Scope

The Transportation and Fleet Operations module is an optional add-on for organisations that move goods using internal vehicles, third-party carriers, or hybrid transport models. It covers shipment-order creation, route and load planning, dispatch, carrier or fleet allocation, ETA and milestone tracking, exception handling, mobile proof capture, trip closure, freight audit, cost settlement, and transport analytics.

The module integrates with:

- **Sales** - outbound delivery demand, delivery-note linkage, and customer proof of delivery
- **Procurement** - inbound shipment visibility and supplier delivery planning
- **Inventory and Advanced Inventory** - warehouse staging, transfer demand, loading, receipt confirmation, and stock movement control
- **Assets** - vehicle identity, maintenance availability status, and capital-asset reference data
- **HR & Payroll** - driver identity and optional labour-cost linkage
- **Accounting** - freight accruals, carrier payables, transport cost allocation, and route profitability analysis
- **Mobile API** - mobile dispatch, proof capture, and driver-side status updates

## 1.3 Definitions, Acronyms, and Abbreviations

The following terms are used throughout this document per IEEE Std 610.12-1990 definitions unless otherwise noted.

| Term | Definition |
|---|---|
| TMS | Transportation Management System - the discipline and system of record for transportation planning, execution, and control |
| Shipment Order | The transport-demand object created from a sales order, purchase order, transfer order, or manual transport request |
| Load | The planned grouping of 1 or more shipment orders onto a single trip, vehicle, or carrier movement |
| Stop | A planned pickup, delivery, or checkpoint event within a route |
| ETA | Estimated Time of Arrival |
| POD | Proof of Delivery - evidence that a shipment or stop was completed and received |
| Freight Audit | The validation of actual carrier or trip charges against planned or contracted transport cost |
| Exception Queue | A prioritised worklist of transport execution issues requiring planner or dispatcher action |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| SRS | Software Requirements Specification |
| P95 | 95th percentile response time under measured load |

## 1.4 Applicable Standards

The requirements in this document are grounded in the following standards.

- IEEE Std 830-1998 - Recommended Practice for Software Requirements Specifications
- IEEE Std 1233-1998 - Guide for Developing System Requirements Specifications
- IEEE Std 610.12-1990 - Standard Glossary of Software Engineering Terminology
- ISO 9001 - process control, traceability, and corrective-action discipline

## 1.5 Overview of This Document

Section 2 specifies the core functional requirements for shipment planning, route design, dispatch, live visibility, proof capture, freight audit, and fleet operations control. Section 3 defines non-functional requirements governing performance, availability, offline behaviour, and auditability. Section 4 presents the Traceability Matrix mapping each functional requirement to the business goals defined below.

## 1.6 Business Goals

The following business goals govern requirement priority and traceability throughout this SRS.

- **BG-TMS-001:** Reduce transport cost through better load planning, route control, and freight validation.
- **BG-TMS-002:** Improve service reliability through dispatch discipline, ETA visibility, and exception ownership.
- **BG-TMS-003:** Increase fleet utilisation and operational control for organisations running internal vehicles.
- **BG-TMS-004:** Create a traceable transport record from shipment planning through proof of delivery and settlement.
- **BG-TMS-005:** Give management transport analytics that connect physical movement to financial outcomes.

## 1.7 Assumptions and Dependencies

- The tenant has activated the Transportation and Fleet Operations module under a subscription plan that permits add-on modules.
- Sales, Procurement, Inventory, and Advanced Inventory remain the source modules for shipment demand and stock events.
- Assets remains the system of record for vehicle capital ownership and maintenance history, while Transportation owns dispatch and route operations.
- Mobile API services are available for field-side status capture and proof collection.
- GPS or telematics integration may be enabled later; the module shall operate without it in its baseline form.
