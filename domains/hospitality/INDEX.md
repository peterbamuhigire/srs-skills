# Domain: Hospitality

## Scope

Hotels, resorts, lodges, inns, guest houses, serviced apartments, restaurants,
bars, cafes, catering businesses, meeting/event venues and mixed hospitality
properties. Use the accommodation and food-service sections separately, then
define explicit interfaces for shared guests, room charges, inventory, finance,
events and reporting.

## Default actors

Owner/GM, reservations agent, front desk, guest, housekeeping, maintenance,
restaurant manager, waiter/server, cashier, bartender, kitchen/KOT operator,
chef, procurement/receiver, storekeeper, event manager, finance officer,
auditor, system administrator and integration operator.

## Default feature families

- property/outlet setup, room and table inventory, rates, menus and policies;
- reservations, availability, groups, waitlist, check-in/out, stays and folios;
- housekeeping, maintenance, events, service requests and guest communications;
- restaurant orders, KOT/KDS, tabs, bills, payment, shifts and day close;
- recipes/BOM, yield, stock, receiving, waste, food safety and cost control;
- finance posting, tax/fiscal boundary, reconciliation, reporting and audit;
- RBAC/tenant isolation, privacy, resilience, accessibility and support.

## Routing

Load `02-requirements-engineering/hospitality-operating-model-srs/SKILL.md`,
the hotel/restaurant feature references, the finance engine when money or
inventory is involved, and the engineering engine for implementation.

## Evidence rule

Do not mark a requirement satisfied because a screen, endpoint, migration or
reference document exists. Require executable acceptance evidence for normal,
failure, concurrency, permission, tenant, reconciliation and recovery paths;
otherwise mark it `NOT_ASSESSED`.
