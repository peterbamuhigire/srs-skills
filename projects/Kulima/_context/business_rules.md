# Business Rules

## Multi-Tenancy and Isolation
- Each tenant (farmer account, farm business, or cooperative) operates in complete data isolation.
- A tenant's data is never visible to another tenant.
- Cooperative tenants operate as franchises: the cooperative admin sees aggregate and governed member data; members see only their own farm data.

## Subscription and Tier Enforcement
- Tier limits (farms, plots, users, animals, AI queries, storage, and premium modules) are enforced at API level before any write operation.
- Exceeding a tier limit returns a clear upgrade prompt and never silently truncates data.
- Free-tier data is never deleted due to inactivity.
- Add-on modules (AI, IoT, cameras, GPS, traceability, cooperative, marketplace) are explicit feature flags per tenant.
- Annual subscription discount remains pay 10 months, receive 12 months of service.

## Whole-Farm Planning
- Every farm may maintain one current annual whole-farm plan plus archived historical versions.
- The whole-farm plan must define goals, enterprise mix, target area/headcount, target output, and budget assumptions for the planning period.
- Enterprise targets roll down into seasonal plans, task schedules, and performance dashboards.

## Farm and Plot Rules
- A single account can manage multiple farms within tier limits.
- Each farm must have a unique name within the tenant.
- Each plot must belong to exactly one farm.
- Plot area sum should not exceed farm total area, but the system warns rather than hard-blocks because surveyed and official sizes may differ.
- Plot types are system-defined; custom types are not allowed in Phase 1.
- Farm GPS boundary is optional in Phase 1 and required for traceability workflows in Phase 2+.

## Crop and Livestock Rules
- A crop season is linked to exactly one plot and one crop variety.
- Multiple crop seasons can run simultaneously on different plots.
- Crop and livestock activities must reference a valid enterprise context.
- Input usage recorded during activities deducts from stock records when inventory controls are enabled.
- Harvest, production, and sale records must preserve enough detail to support enterprise profitability and traceability.

## Financial and Commercial Rules
- Every income and expense record must be linked to a farm and should be linked to an enterprise, customer, supplier, or activity whenever applicable.
- Enterprise profitability is calculated as income minus direct and allocated operating expenses per enterprise per period.
- Budget variance is calculated as Actual - Planned and must be visible at whole-farm and enterprise levels.
- Customer receivables and supplier payables must remain open until fully settled or written off with approval.
- Capital purchases above a configurable approval threshold require approval before payment.
- Mobile money references may be recorded without external API validation when payment was executed outside Kulima.

## Procurement and Inventory Rules
- All purchased inputs and materials should be tied to a supplier and expense category.
- Requested quantity, received quantity, invoiced quantity, and paid quantity are tracked separately.
- Low stock alerts fire when current stock falls below the configured minimum.
- Expiry alerts fire at 90, 60, and 30 days before expiry.
- Equipment maintenance reminders follow the configured schedule for each asset.
- Dispatch of produce is blocked when required compliance gates fail, including unresolved withholding periods or missing mandatory lot data.

## Labour and SOP Rules
- Tasks can be assigned to one or more workers or crews.
- Only the assigned worker, supervisor, or manager can close a task.
- Recurring tasks auto-generate according to schedule.
- Permanent staff may have statutory deductions; casual staff default to simpler wage calculations.
- Hazardous or compliance-sensitive tasks may require an SOP checklist before completion.
- Worker training and skill records must be retained for audit and scheduling purposes.

## Offline and Sync Rules
- Core write operations succeed locally regardless of connectivity.
- Sync queue priority is financial transactions -> commercial commitments -> activities -> animals -> reference data.
- Conflict resolution defaults to last-write-wins by timestamp while preserving a conflict log for review.
- Photos and large attachments sync separately and can be deferred on weak networks.

## Traceability and Compliance Rules
- A batch must reference at least one plot and one harvest or production record.
- Chain-of-custody stages must be chronological.
- QR codes are immutable once created.
- Certification expiry triggers renewal reminders at 90, 60, and 30 days before expiry.
- Deforestation checks compare farm polygons against the December 2020 baseline.
- Dispatch-ready status requires all mandatory compliance checks to pass for the selected market or certification context.

## IoT, Camera, and GPS Rules
- IoT devices must be assigned to a specific animal or asset before data is shown in operational dashboards.
- Critical IoT and geofence alerts trigger immediate SMS and push notifications.
- Camera streams are proxied in real time; Kulima does not store video by default.
- Historical GPS data retention is configurable per tenant, with 90 days as the default active window.
