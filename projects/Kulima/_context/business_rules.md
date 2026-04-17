# Business Rules

## Multi-Tenancy and Isolation
- Each tenant (farmer account, farm business, or cooperative) operates in complete data isolation
- A tenant's data is never visible to another tenant
- Cooperative tenants operate as franchises — the cooperative admin sees aggregated member data; individual members see only their own farm data

## Subscription and Tier Enforcement
- Tier limits (farms, plots, users, animals, AI queries) enforced at API level before any write operation
- Exceeding a tier limit returns a clear upgrade prompt, never silently truncates data
- Free tier (Seedling) data is never deleted due to inactivity — permanent retention
- Add-on modules (IoT, cameras, GPS, traceability, cooperative, marketplace) are boolean feature flags per tenant
- Annual subscription discount: pay 10 months, receive 12 months of service

## Farm and Plot Rules
- A single account can manage multiple farms (within tier limits)
- Each farm must have a unique name within the tenant
- Each plot must belong to exactly one farm
- Plot area sum should not exceed farm total area (warning, not hard block — GPS boundaries may differ from official records)
- Plot types are system-defined (25+ types); farmers cannot create custom plot types
- Farm GPS boundary is optional in Phase 1 (manual area entry), required for traceability and EUDR in Phase 2+

## Crop Rules
- A crop season is linked to exactly one plot and one crop variety
- Multiple crop seasons can run simultaneously on different plots
- Uganda has two growing seasons: Season A (March-June) and Season B (August-November) — system pre-populates seasonal prompts
- Crop activities must reference a valid crop season
- Input usage recorded during activities automatically deducts from input inventory
- Harvest records must specify a storage destination
- Yield analysis compares actual harvest quantity against the variety's expected yield per acre

## Livestock Rules
- Every animal must belong to a species and optionally a breed
- Individual animal tracking is mandatory for cattle, goats, sheep, pigs, donkeys, horses
- Flock-level management (not individual) is permitted for poultry and rabbits
- Pedigree links (sire/dam) must reference animals within the same tenant
- An animal's status transitions follow defined paths: Active → Sold/Deceased/Slaughtered/Lost/Quarantine/Transferred
- Vaccination and treatment records must include the next due date where applicable
- Milk production records require session identification (morning/evening/midday)

## Financial Rules
- Every income and expense record must be linked to a farm and optionally to an enterprise type
- Enterprise profitability is calculated by summing income minus expenses per enterprise type per period
- Mobile money payment references (MoMo/Airtel transaction IDs) should be recorded but are not validated against mobile money APIs
- Loans must track outstanding balance; the system does not auto-deduct repayments
- Market prices are recorded per crop per market per date — the system does not fetch prices automatically in Phase 1
- Bank loan credibility report aggregates 12 months of income, expenses, and asset records into a standardised format

## Cooperative / Franchise Rules
- A cooperative operates as a single franchise tenant
- Member farmers are registered under the cooperative tenant with their own user accounts and farm data
- Collection centre deliveries are recorded with weight, quality grade, and date
- Member payments are calculated as: quantity delivered x grade-specific price per unit
- Bulk mobile money disbursement sends individual payments to each member's registered mobile money number
- The cooperative admin can view aggregated member data but cannot edit individual member farm records
- Member farmers can operate independently (own sales, own expenses) within the cooperative umbrella

## Inventory Rules
- Input stock cannot go below zero — if a usage record would cause negative stock, the system warns but allows the record (farmer may have received inputs informally)
- Expiry alerts fire at 30, 60, and 90 days before expiry date
- Low stock alerts fire when current stock falls below the item's minimum stock level
- Equipment maintenance reminders follow the maintenance schedule configured per equipment item

## Task and Worker Rules
- Tasks can be assigned to one or more workers
- Only the assigned worker or a Farm Manager/Owner can mark a task complete
- Recurring tasks auto-generate new task instances according to their schedule
- Worker daily wage is calculated as: hours worked x hourly rate (or flat daily rate)
- NSSF and PAYE deductions apply only to workers marked as "permanent staff"

## Offline and Sync Rules
- All write operations succeed locally regardless of connectivity
- Sync queue processes in priority order: financial transactions → activities → animals → reference data
- Conflict resolution: last-write-wins by timestamp; conflicts logged for farmer review
- Photos and attachments sync separately, only on WiFi or strong 3G/4G
- A device that has been offline for more than 90 days triggers a full sync on reconnection

## Traceability Rules (Phase 2+)
- A batch must reference at least one plot and one harvest record
- Chain of custody stages must be recorded in chronological order
- QR codes are generated per batch and are immutable once created
- EUDR DDS export includes only: farm GPS polygon, crop type, harvest date, deforestation check result
- Deforestation check compares farm polygon against the December 2020 baseline from Global Forest Watch
- Certification expiry triggers renewal reminder alerts at 90, 60, and 30 days before expiry

## IoT Rules (Phase 3+)
- IoT devices must be assigned to a specific animal before data is displayed
- Jaguza data polling occurs every 10 minutes; webhook alerts are processed in real time
- IoT alert severity levels: Info, Warning, Critical
- Critical alerts (disease early warning, geofence breach) trigger immediate SMS + push notification

## Camera Rules (Phase 3+)
- Camera streams are proxied (RTSP → HLS) — Kulima does not store video
- Motion alert zones must be configured per camera; full-frame alerts are disabled by default to reduce false positives
- Camera access can be shared via time-limited links (configurable: 1 hour, 24 hours, 7 days)

## GPS Tracking Rules (Phase 3+)
- Geofence breach alerts must fire within 2 minutes of the GPS position exiting the boundary
- SMS alert delivery is mandatory (works without smartphone); push and WhatsApp are supplementary
- Historical GPS data retained for 90 days; older data archived or deleted per tenant preference
