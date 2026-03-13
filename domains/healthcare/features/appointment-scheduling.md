# Feature: Appointment Scheduling

## Description
Management of patient appointments — scheduling, reminders, cancellations,
waitlists, and provider availability.

## Standard Capabilities
- Provider availability calendar management
- Patient appointment booking (walk-in, phone, portal)
- Automated appointment reminders (SMS, email)
- Cancellation and rescheduling workflows
- Waitlist management with automatic slot filling
- Multi-location and multi-provider scheduling
- Recurring appointment series support

## Regulatory Hooks
- HIPAA: appointment data is PHI — must be encrypted and access-logged
- Reminder communications must offer opt-out per TCPA

## Linked NFRs
- NFR-HC-001 (Audit Trail)
- NFR-HC-004 (Session Timeout)
