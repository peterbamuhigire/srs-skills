---
title: "Software Requirements Specification: Hotel/Accommodation Module (F-013)"
subtitle: "Maduuka SaaS Platform — Phase 3a"
version: "0.1-draft"
date: "2026-04-05"
status: "Draft — Pending Human Review"
---

# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Hotel/Accommodation add-on module (F-013) of the Maduuka SaaS platform. This document provides a binding reference for design, development, and acceptance testing of F-013. It is written to conform to IEEE Std 830-1998 and IEEE Std 1233-1998.

The intended readers are: the Maduuka development team, business owner (Peter Bamuhigire), and any acceptance-testing stakeholders.

## 1.2 Scope

F-013 is an optional add-on module available to Maduuka subscribers at +UGX 50,000/month. It extends the Phase 1 core platform with full property management capabilities covering: hotels, lodges, guesthouses, serviced apartments, Airbnb operators, conference centres, and bush/safari camps.

F-013 is not a standalone system. It requires all Phase 1 core modules (F-001 through F-010) to be active. Integration with the Phase 2 Restaurant/Bar module (F-011) enables posting of food and beverage charges directly to a guest folio; this integration is recommended but not mandatory for F-013 activation.

This SRS covers Phase 3a scope only. Channel manager integration (Booking.com, Airbnb OTA feeds) is explicitly deferred to Phase 4 per GAP-007; however, the data model includes a `booking_source` field from the outset to accommodate that future integration without a schema migration.

## 1.3 Relationship to Existing SRS Documents

This document is a companion to:

- *SRS Maduuka Phase 1* — defines the core platform, multi-tenancy, POS, inventory, customer management, payments, HR/payroll, and settings.
- *SRS Maduuka Phase 2a — Restaurant/Bar (F-011)* — defines table management, kitchen order tickets, bar tabs, and F&B billing. F-013 references F-011 for charge-posting integration.
- *SRS Maduuka Phase 2b — Pharmacy (F-012)* — independent of F-013.

Requirements in this document supplement, and do not replace, requirements in the Phase 1 SRS. Where a Phase 1 business rule is referenced (e.g., BR-010 multi-payment, BR-003 audit trail), the Phase 1 definition governs.

## 1.4 Definitions

The following terms are used throughout this document. All IEEE Std 610.12-1990 definitions apply where no specific definition is given below.

- *Average Daily Rate (ADR)* — A hotel performance metric calculated as: Room Revenue ÷ Rooms Sold. Expressed in UGX per occupied room per night.
- *booking_source* — A database field on the reservation record identifying the channel through which the reservation was created (e.g., walk-in, phone, future: Booking.com, Airbnb). Mandatory from Phase 3; values from external channel managers populated in Phase 4.
- *channel manager* — A third-party software layer (e.g., SiteMinder, Little Hotelier) that synchronises room availability and rates across multiple Online Travel Agencies (OTAs) and the property's own system. Integration deferred to Phase 4 (GAP-007).
- *folio* — The running account maintained for a single guest stay, recording all charges (accommodation, F&B, laundry, conference) and payments from check-in to check-out. Equivalent to a guest bill or guest ledger account.
- *OTA (Online Travel Agency)* — A third-party booking platform (e.g., Booking.com, Airbnb, Expedia) through which guests may discover and reserve accommodation.
- *PMS (Property Management System)* — The category of software used to manage hotel reservations, check-in/check-out, room assignments, and guest billing. F-013 constitutes the PMS capability within Maduuka.
- *RevPAR (Revenue Per Available Room)* — A hotel performance metric calculated as: Total Room Revenue ÷ Available Room Nights. Expressed in UGX. Indicates revenue efficiency across the entire room inventory regardless of occupancy.
- *room status* — The current operational state of an individual room. Valid states are: Available, Occupied, Reserved, Cleaning, Maintenance, Out of Order.
- *room type* — A classification grouping individual rooms that share the same physical configuration, capacity, and default rate (e.g., Standard Single, Deluxe Double, Conference Suite).
- *Software Requirements Specification (SRS)* — A document that completely describes all of the functions of a proposed system and the constraints under which it must operate (IEEE Std 830-1998).

## 1.5 Uganda Market Context

Uganda's accommodation market operates two dominant billing models that coexist within the same market segment:

- *Nightly billing* — Standard overnight hotels charge a fixed rate per night, with check-in and check-out at defined standard times. Late checkout may incur an additional charge.
- *Hourly billing* — Guesthouses, lodges, and short-stay facilities charge by the hour, tracking the exact check-in timestamp and rounding the occupied duration up to the next whole hour at checkout.

A single property may serve both overnight and short-stay guests, making dual billing mode (BR-016) a first-class requirement rather than an optional feature. F-013 implements both modes with billing mode selection at check-in and an immutable lock after checkout is processed.

## 1.6 Overview of This Document

Section 2 describes the overall system context, user classes, platform constraints, and deferred integrations. Section 3 specifies all functional requirements (FR-HTL-001 through FR-HTL-112). Section 4 specifies non-functional requirements. Section 5 describes design and operational constraints.
