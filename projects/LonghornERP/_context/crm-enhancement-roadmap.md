# LonghornERP CRM Enhancement Roadmap

## Purpose

This roadmap translates the `Customer Relationship Management System Playbook.epub` study into concrete LonghornERP product, requirements, and design changes so the `SALES_CRM` capability becomes a world-class CRM for African businesses.

## Core Conclusions

- CRM must be treated as both a system of record and a system of engagement for customer-facing work.
- LonghornERP should keep a clear boundary:
  - `SALES_CRM` owns customer-facing intent, workflow, routing, account context, pipeline governance, service cases, and renewal risk signals.
  - `SALES` and `ACCOUNTING` own transactional execution, fulfilment, invoicing, collections, and financial truth.
- The CRM object model must be explicit and governed:
  - accounts
  - contacts
  - leads
  - opportunities
  - cases
  - activities
- World-class CRM requires both revenue and service capability depth. Pipeline alone is not enough.

## Capability Gaps Identified In Current LonghornERP

- CRM is currently strong on leads, opportunities, activity logging, forecasting, and mobile field use.
- CRM is currently weak or absent in:
  - account hierarchy and account planning
  - segmentation and prioritisation
  - case and service workflow
  - SLA and escalation governance
  - quote-to-cash context preservation
  - approval visibility for deal, discount, term, and risk exceptions
  - renewal and retention risk visibility
  - partner and channel relationship support
  - dedicated CRM NFRs and traceability

## Target CRM Capability Model

### 1. Revenue CRM

- lead capture, routing, qualification, and conversion discipline
- opportunity governance with clear stage exit criteria
- date-bound next steps and deal inspection readiness
- forecast inspection, override governance, and pipeline hygiene
- quote-to-cash narrative continuity from opportunity to quotation/order
- account segmentation, tiering, whitespace, and account planning

### 2. Service CRM

- case intake from multiple channels
- case categorisation, priority, and ownership
- SLA policy enforcement
- escalation workflow
- resolution coding and reopen handling
- service history visibility in the account context
- feedback loop from service issues into renewal, churn, and expansion risk

### 3. Customer Lifecycle CRM

- account and contact governance
- customer health and renewal visibility
- retention-risk flags
- expansion opportunity identification
- partner/channel participation in customer coverage where relevant

## Architecture Principles

- CRM intent is not ERP execution.
- Quotes, orders, invoices, and collections remain authoritative in core ERP modules.
- CRM must surface execution context from ERP back to relationship owners:
  - quotation status
  - order status
  - invoice status
  - overdue balance / credit context
  - service backlog / escalation state
- CRM design should avoid:
  - storing financial truth inside CRM objects
  - using opportunities as project trackers
  - using cases as generic internal tickets
  - duplicating customer identity without merge and hierarchy rules

## Recommended Documentation Changes

- Upgrade PRD positioning for `SALES_CRM` from pipeline add-on to full customer revenue and service capability.
- Extend the CRM SRS with:
  - account management
  - account hierarchy
  - segmentation and account planning
  - case management
  - SLA and escalation
  - quote-to-cash handoff
  - renewal / retention risk visibility
  - CRM-specific NFRs
  - full traceability
- Extend HLD, LLD, API, and database design with:
  - CRM object boundaries
  - service-case architecture
  - account planning services
  - opportunity approval structures
  - case workflow endpoints
  - CRM/service tables

## Product Positioning Outcome

LonghornERP should position `SALES_CRM` as the operational hub for customer acquisition, deal progression, account growth, and service continuity, while preserving the ERP core as the authoritative execution and financial system.
