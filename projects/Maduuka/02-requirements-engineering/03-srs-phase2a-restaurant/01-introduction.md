---
title: "SRS Phase 2a — Restaurant/Bar Add-on Module (F-011)"
subtitle: "Section 1: Introduction"
project: Maduuka
version: "0.1-draft"
date: 2026-04-05
---

# Section 1: Introduction

## 1.1 Purpose

This document is the Software Requirements Specification (SRS) for the Restaurant/Bar add-on module (F-011) of the Maduuka platform. It defines all functional requirements, non-functional requirements, and constraints governing the behaviour of F-011 in a manner that is correct, unambiguous, complete, and verifiable per IEEE Std 830-1998.

This SRS supplements — and does not replace — the Phase 1 SRS. Readers of this document must be familiar with the Phase 1 SRS before interpreting requirements herein. All Phase 1 functional requirements remain in force for tenants who activate F-011.

## 1.2 Scope

The Restaurant/Bar add-on module extends the Maduuka core Point of Sale (F-001) and Inventory (F-002) modules to support table-service food and beverage (F&B) operations. The module addresses:

- Table layout management and real-time occupancy tracking
- Kitchen Order Ticket (KOT) creation, routing, and display
- Bar tab management across a session
- Bill-of-materials (BOM) driven stock deduction from raw material inventory
- F&B-specific billing: service charge, cover charge, split billing
- Server performance and kitchen throughput reporting
- Web-only floor plan designer

This module does not cover hotel room charge posting — that integration is Phase 3 scope (F-013). EFRIS fiscal integration for F&B items is subject to [CONTEXT-GAP: GAP-010 — confirm Uganda VAT treatment of restaurant/bar items before EFRIS integration is specified].

F-011 is an optional add-on at UGX 30,000 per month. It is available to any Maduuka tenant with active Phase 1 core modules.

## 1.3 Relationship to Phase 1 SRS

The Phase 1 SRS governs requirements **FR-POS-001** through **FR-SET-012**. This document governs requirements **FR-RES-001** through **FR-RES-085**. Where a requirement in this document references a Phase 1 capability (e.g., payment processing, stock deduction), the Phase 1 requirement identifier is cited. In cases of conflict between this document and the Phase 1 SRS, this document takes precedence for F-011 behaviour only.

## 1.4 Applicable Standards

| Standard | Title | Application |
| --- | --- | --- |
| IEEE Std 830-1998 | Recommended Practice for Software Requirements Specifications | Overall SRS structure and quality criteria |
| IEEE Std 1233-1998 | Guide for Developing System Requirements Specifications | Stimulus-response requirement format |
| IEEE Std 610.12-1990 | Standard Glossary of Software Engineering Terminology | Terminology definitions |
| ASTM E1340-96 | Standard Guide for Rapid Evaporation | Estimation and sizing guidance |

## 1.5 Definitions

**Bill of Materials (BOM):** A structured list that maps a finished menu item (e.g., "Chicken Stew") to the raw material stock-keeping units (SKUs) and quantities consumed in producing one unit of that item. On KOT send, the system uses the BOM to auto-deduct raw material inventory.

**Bar Tab:** A running account opened for a customer at the bar that accumulates drink rounds across a session before final settlement. A bar tab may be linked to a named customer, a table, or a reference label.

**Cover:** One diner occupying a seat. Cover count is used for cover charge calculation and performance reporting.

**Cover Charge:** A fixed monetary amount charged per cover (per diner), configurable by the business owner. Cover charge is added to the bill before payment.

**Floor Plan:** A visual representation of the restaurant's physical layout showing tables, sections, and seating areas. The floor plan is defined in the web-based floor plan designer and rendered as the table status board.

**Kitchen Display System (KDS):** A browser-based display screen installed in the kitchen or bar that shows open KOTs in real time, colour-coded by elapsed time. The KDS auto-refreshes without manual reload.

**Kitchen Order Ticket (KOT):** A record sent to the kitchen (or bar) containing the table number, server name, ordered items with modifiers and special instructions, and a timestamp. A KOT is the unit of work for kitchen staff.

**Service Charge:** A configurable percentage applied to the net food and beverage subtotal before tax. It is distinct from a tip and is a business-defined charge, not a gratuity.

**Station:** A designated preparation area within the kitchen or bar (e.g., grill, cold section, fryer). Each station may have its own KDS view showing only tickets relevant to that station.

**Table Status:** The current operational state of a table. Valid states are: *Available*, *Occupied*, *Reserved*, and *Cleaning*.
