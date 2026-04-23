# LonghornERP Enterprise Asset Management Enhancement Roadmap

## Purpose

This document translates the source book `C:\Users\Peter\Downloads\ERP Playbook\Enterprise Asset Management System Playbook.epub` into concrete enhancement decisions for LonghornERP.

The goal is to evolve LonghornERP's `ASSETS` module from strong fixed-asset accounting with basic maintenance support into a more complete enterprise asset management capability.

## Executive Decision

LonghornERP should keep `ASSETS` as the tenant-facing module, but deepen it into an EAM-grade bounded context.

The playbook makes one point very clearly: enterprise asset management is not just depreciation or maintenance reminders. It is the governed system for how physical assets are identified, prioritized, maintained, analyzed, and improved across their operating lives.

Critical implication for LonghornERP:

- do not split finance-facing asset records away from operational asset stewardship in a way that destroys traceability
- do not overload `ASSETS` with functions owned by `TRANSPORTATION`, `MANUFACTURING`, `PROCUREMENT`, or `ACCOUNTING`
- do deepen `ASSETS` so that it owns the physical-asset work-management and reliability chain

## Critical Findings from the Playbook

### 1. EAM is broader than work orders

The EAM playbook frames EAM around 5 connected domains:

- asset registry and hierarchy
- work management
- preventive and condition-based maintenance
- maintenance materials support
- reliability, performance, and compliance visibility

Critical implication for LonghornERP:

- maintenance schedules and service logs are useful, but they are not enough
- asset hierarchy, criticality, planning quality, materials readiness, and closeout quality all need explicit documentation

### 2. Reliability depends on closure quality and usable history

The playbook emphasizes:

- failure coding
- repeat-failure analysis
- PM compliance
- backlog discipline
- root-cause feedback loops

Critical implication for LonghornERP:

- vague maintenance history is not enough
- work requests, work orders, closeout, and failure evidence need stronger structure

### 3. EAM needs clean boundaries with ERP, inventory, and operations

The playbook treats EAM as tightly integrated to finance, procurement, MRO inventory, and operational systems, but not as a substitute for those systems.

Critical implication for LonghornERP:

- `ASSETS` should request, plan, and consume MRO work context
- `INVENTORY` should remain the stock and reservation authority
- `PROCUREMENT` should remain the purchasing authority
- `ACCOUNTING` and finance operations remain the financial book of record

## Current LonghornERP Position

## Strengths already present

LonghornERP already has strong asset-accounting foundations:

- asset register
- depreciation
- revaluation and disposal
- transfers and custodianship
- insurance tracking
- physical verification
- book-versus-tax depreciation
- vehicle capital-asset history
- basic maintenance scheduling and work-order tracking

## Critical gaps

### Gap A: Asset hierarchy and criticality are too light

Current documentation does not yet provide enough depth for:

- functional locations
- parent-child asset structures
- criticality ranking
- consequence-based prioritization

### Gap B: Work management is not yet EAM-grade

Current documentation needs stronger modeling for:

- work request intake and screening
- planning and scheduling
- planned versus unplanned work discipline
- shutdown or turnaround packaging
- richer closeout standards and failure coding

### Gap C: Reliability and condition workflows are too thin

Current documentation needs stronger support for:

- repeat-failure visibility
- bad-actor tracking
- condition-based triggers
- maintenance KPI dashboards
- reliability improvement workflow

### Gap D: MRO materials integration is too implicit

The EAM playbook expects stronger linkage between maintenance work and materials availability than LonghornERP currently documents.

Critical implication:

- work orders should be able to reserve, stage, and consume MRO parts through Inventory and Procurement boundaries without blurring ownership

## Recommended Module Boundary

`ASSETS` should own:

- physical asset registry and hierarchy
- asset criticality and lifecycle state
- work requests, work orders, PM, inspections, and closeout
- reliability evidence, condition exceptions, and maintenance KPIs
- shutdown and turnaround maintenance packaging
- asset-side maintenance history for vehicles and non-vehicle equipment

It should not own:

- live fleet dispatch or trip execution, which remain under `TRANSPORTATION`
- enterprise purchasing and supplier contracting, which remain under `PROCUREMENT`
- warehouse stock ledger authority, which remains under `INVENTORY`
- core financial-book governance, which remains under `ACCOUNTING` and finance operations

## Required EAM Uplifts

LonghornERP should explicitly add or strengthen:

- functional locations and asset hierarchy
- asset criticality and risk-based prioritization
- work request screening and planning packs
- weekly scheduling and backlog-aging controls
- failure coding and repeat-failure analysis
- condition-event ingestion and condition-based maintenance triggers
- maintenance KPI dashboards
- MRO reservations and staging integration points

## Recommended Delivery Steps

1. Upgrade module and architecture wording so `ASSETS` is positioned as enterprise asset management, not only fixed-asset accounting.
2. Extend the Asset Management SRS for hierarchy, work management, reliability, and condition workflows.
3. Extend design documentation for operational asset services, endpoints, and tables.
4. Add test and user documentation for work request, work order, scheduling, and condition-alert workflows.

## Output Standard

A stronger LonghornERP asset capability must support:

- auditable fixed-asset accounting
- disciplined enterprise maintenance workflows
- stronger uptime and maintenance reliability
- better MRO coordination with inventory and procurement
- clearer evidence for compliance, shutdown planning, and repair-versus-replace decisions
