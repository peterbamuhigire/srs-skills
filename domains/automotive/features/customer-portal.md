# Feature: Customer Portal / Customer App

## Purpose

Deliver a consumer-fintech-grade customer experience across booking, live status, digital approval, payment, and long-term service history. This is the surface that differentiates the platform from competitors whose "customer portal" is a basic web page.

## Surfaces

- Android (native, Jetpack Compose)
- iOS (native, SwiftUI)
- Web self-service portal (secondary; feature-complete for text content; video/push parity deferred to mobile)

## Core Entities

- **Customer** — individual or fleet. Has `tenant_id`, `customer_type`, contact block, preferred notification channels, saved payment instruments (tokens).
- **Vehicle** — owned or managed by a customer; multiple vehicles per customer; a vehicle may transfer to a new customer with an audit record.
- **Booking Request** — pre-job appointment entity.
- **Service History Record** — one per closed job card, snapshot for customer visibility.

## Key Workflows

1. **Onboard** — sign-up with phone or email; OTP verify; link first vehicle by VIN or plate.
2. **Book** — select branch, service, preferred time window; system offers available slots; one-tap confirm.
3. **Live status** — push notifications on each customer-visible transition; in-app timeline view per job.
4. **Digital approval** — receive inspection findings with photos, plain-language explanations, per-line approve/decline.
5. **Pay** — one-tap pay via saved card (Stripe tokens) or mobile money push; invoice PDF delivered.
6. **History** — scroll vehicle service history; export a service record PDF.
7. **Reminders** — scheduled maintenance reminders, licence/insurance renewal reminders (where data source available), within NFR-AUTO-012 quiet windows.

## Trust-as-a-Design-Value Patterns

- Plain-language explanations on every inspection recommendation.
- Photo evidence prominent, not hidden behind a tab.
- Price transparency — labour and parts always itemised.
- No notification fatigue — per NFR-AUTO-012, reminders respect quiet hours and cadence limits.

## Multi-Tenant Customer Identity

A single customer human may be a customer of multiple tenants (multiple garages). The recommended pattern is account-per-tenant with an optional "link accounts" experience at the user's choice; cross-tenant data never leaks without explicit linking consent.

## White-Label Strategy

Single multi-tenant app by default; per-tenant build for Enterprise-plan tenants that insist. See architecture-patterns.md — "White-Label Customer App Strategy."

## Interfaces

- Workshop operations — live status.
- Inspection — report rendering with approval.
- Invoicing and payment — view and pay.
- Marketing — controlled push and email cadence.

## Non-Functional Expectations

Inherit NFR-AUTO-011, NFR-AUTO-012, and general UX parity requirements with leading consumer fintech apps.

## Edge Cases

- Customer declines all recommendations — job continues on original scope only; system emits a "declined" summary note to the garage.
- Payment fails mid-checkout — invoice stays unpaid with a retry affordance; no duplicate charges.
- Vehicle transfer between owners — requires both parties to confirm via in-app flow; service history remains with the vehicle, not the previous owner, subject to data-protection rules.
- Fleet manager persona — sees consolidated view across many vehicles, approves on behalf of drivers, receives consolidated monthly statements.
