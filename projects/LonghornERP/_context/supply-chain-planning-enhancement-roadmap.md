# LonghornERP Supply Chain Planning Enhancement Roadmap

## Purpose

This document translates the source book `C:\Users\Peter\Downloads\ERP Playbook\The Supply Chain Planning System Playbook.epub` into concrete enhancement decisions for LonghornERP.

The goal is to ensure LonghornERP handles supply chain planning as a real planning discipline, not as a loose collection of reorder rules buried inside execution modules.

## Executive Decision

LonghornERP should add a dedicated `SUPPLY_CHAIN_PLANNING` add-on module.

The playbook is clear that planning and execution are adjacent but different:

- ERP records and controls execution transactions
- planning systems create governed forward-looking plans
- the organization needs one accountable demand view, one feasible supply view, one inventory-policy layer, and one escalation rhythm

Critical implication for LonghornERP:

- `INVENTORY`, `PROCUREMENT`, `ADV_INVENTORY`, `MANUFACTURING`, and `TRANSPORTATION` should remain execution and control modules
- `SUPPLY_CHAIN_PLANNING` should become the bounded context for demand planning, supply planning, inventory optimization, S&OP/IBP, and scenario management

## Critical Findings from the Playbook

### 1. Planning is not execution

The SCP playbook distinguishes planning from ERP transactions. Planning owns:

- demand forecasting and consensus demand
- supply and replenishment planning
- inventory policy and service-level logic
- capacity and constraint visibility
- scenario analysis
- S&OP / IBP cadence and executive trade-off governance

Critical implication for LonghornERP:

- reorder alerts and stock reports are useful, but they are not a planning system
- planning outputs must be reviewed, approved, and released into execution modules without blurring ownership

### 2. Governance of overrides matters as much as the forecast

The playbook repeatedly emphasizes:

- baseline versus override distinction
- ownership of changes
- bias measurement
- decision rights and escalation thresholds
- financial translation of the plan

Critical implication for LonghornERP:

- forecast override discipline and scenario governance are first-class requirements
- a planning module without accountability will just produce better spreadsheets

### 3. S&OP / IBP is a management system, not a meeting title

The playbook treats S&OP / IBP as the cross-functional mechanism linking sales, operations, supply chain, and finance.

Critical implication for LonghornERP:

- LonghornERP should model review cycles, decision gates, locked plans, and executive exceptions
- financial impact of supply plans must be visible inside the planning layer

## Current LonghornERP Position

## Strengths already present

LonghornERP already has a strong execution foundation:

- Inventory and Advanced Inventory for stock control, movements, FEFO, and warehousing
- Procurement for sourcing, RFQ, PO, GRN, invoice matching, and supplier controls
- Manufacturing for production planning and execution foundations
- Transportation for movement, dispatch, and freight operations
- Accounting for financial posting and visibility

## Critical gaps

### Gap A: No dedicated planning bounded context

Current documentation does not yet define a first-class module for:

- demand planning
- supply and replenishment planning
- inventory policy optimization
- constraint-driven planning exceptions
- formal S&OP / IBP cycle governance

### Gap B: No planner workbench

LonghornERP can control inventory transactions, but it does not yet define enough for:

- baseline forecast generation
- governed overrides
- scenario comparison
- released plan versions
- financial roll-up of planning choices

### Gap C: Supply chain decisions are not yet tied into one calendar

Execution modules operate on events and transactions, but the planning playbook expects:

- one planning cadence
- one approved plan version
- one exception path
- one executive review mechanism for trade-offs

## Recommended Module Boundary

`SUPPLY_CHAIN_PLANNING` should own:

- demand planning and forecast governance
- supply and replenishment planning
- inventory policy and service-level segmentation
- S&OP / IBP cycle orchestration
- scenario planning and exception management
- financial translation of forward-looking plans

It should not own:

- purchase orders, receipts, stock movements, or shipment execution
- production-order execution
- direct warehouse task execution
- accounting book-of-record postings

Those remain owned by:

- `PROCUREMENT`
- `INVENTORY`
- `ADV_INVENTORY`
- `MANUFACTURING`
- `TRANSPORTATION`
- `ACCOUNTING`

## Required SCP Uplifts

LonghornERP should explicitly add:

- a consensus demand model with baseline and override governance
- a feasible supply-planning model using lead times, sourcing rules, and capacity signals
- inventory policy optimization by service class and item-location segment
- a scenario sandbox for what-if analysis
- S&OP / IBP review-cycle workflows and release locks
- financial roll-up of supply plans into revenue, margin, and inventory implications

## Recommended Delivery Steps

1. Add `SUPPLY_CHAIN_PLANNING` to the module inventory and architecture set as a new add-on module.
2. Author an SRS for planning capabilities rather than trying to hide them inside inventory or procurement.
3. Extend architecture, API, and database design documentation for planning runs, scenarios, and executive review cycles.
4. Add test and user documentation for planner workflows, released-plan controls, and scenario analysis.

## Output Standard

A stronger LonghornERP supply chain capability must support:

- one accountable demand view
- one feasible supply view
- inventory policy linked to service and working capital
- scenario-based decision support
- explicit executive trade-off governance
- clean release of approved plans into ERP execution modules
