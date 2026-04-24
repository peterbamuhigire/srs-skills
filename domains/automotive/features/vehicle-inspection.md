# Feature: Vehicle Inspection

## Purpose

Provide a digital multi-point inspection that is evidence-based, customer-visible, and drives the estimate line items.

## Core Entities

- **Inspection Template** — tenant-authored, service-type-specific (general workshop, tyre centre, body shop, quick-fit, EV). Template has sections and checkpoints. Checkpoints declare: label, measurement unit (pass/fail, percentage, mm, psi, Nm, °C), threshold rules that map values to a traffic-light severity (green/amber/red), and whether photo evidence is required.
- **Inspection Report** — one per job card. Carries completed checkpoints, photos, DTC list, technician notes, mileage at inspection, inspection-started-at, inspection-completed-at, technician identity.
- **Recommendation** — derived from amber/red checkpoints. Each recommendation has a suggested service code, labour estimate, parts estimate, customer-friendly description, and evidence reference (photo IDs, measurement, DTC code).

## Key Workflows

1. **Template selection.** On inspection start, the technician or service advisor selects the template that matches the service type.
2. **Checkpoint execution.** The technician walks the list on the mobile app. Measurement inputs are first-class (not freetext). Amber/red findings require a photo.
3. **DTC capture.** Manual at MVP; OBD-II adapter stub reserved (see architecture-patterns.md — OBD-II Integration Envelope).
4. **Recommendation generation.** Red findings become recommended services at the top of the estimate; amber findings become "monitor at next visit." Green findings are reassurance items displayed to the customer.
5. **Customer visibility.** The Customer App shows the inspection with traffic-light summary, photos, technician notes, and the option to approve or decline each recommendation independently.

## Evidence Standards

See NFR-AUTO-009. Photos are SHA-256 hashed at upload, tied to the inspection report, and immutable.

## Interfaces

- Workshop operations: inspection completion transitions the job to "estimated."
- Customer App: inspection report is rendered to the customer with plain-language explanation per finding.
- Parts: recommended parts hit the reservation flow once the customer approves a line.
- AI add-on (future): a vision model may pre-classify tyre tread depth, brake pad wear, and visible corrosion from photos; technicians always retain final judgement.

## Non-Functional Expectations

Inherit NFR-AUTO-001, NFR-AUTO-002, NFR-AUTO-009.

## Edge Cases

- Inspection paused mid-way — state persists; resume from the last saved checkpoint.
- Customer declines a red recommendation — the decline is logged with timestamp and customer identity; the garage's dispute protection relies on this record.
- Re-inspection on warranty-return — a new inspection report links back to the original and highlights the deltas.
