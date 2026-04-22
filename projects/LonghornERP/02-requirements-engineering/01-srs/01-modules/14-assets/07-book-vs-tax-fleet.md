# Book vs. Tax Depreciation, Deferred Tax, and Vehicle Fleet Management

## 7.1 Overview

Uganda's Income Tax Act (Third Schedule) specifies depreciation rates for tax purposes that differ from the IFRS-compliant rates used for book reporting. This section specifies requirements for maintaining dual depreciation schedules per asset, computing the resulting deferred tax liability, and managing the Vehicle Fleet sub-ledger — which adds mileage, fuel, and service record tracking to standard asset management.

Within Longhorn ERP, the Vehicle Fleet sub-ledger in Asset Management exists to preserve vehicle capital-asset records, depreciation, maintenance history, insurance and regulatory compliance history, and other auditable ownership data. The Transportation module is the source of truth for dispatch, trips, routes, driver movement control, consignment movement, and live fleet operations. Where operational events are reflected here, they are retained only as supporting records for asset stewardship, maintenance planning, compliance evidence, and financial auditability.

## 7.2 Book vs. Tax Depreciation

### 7.2.1 Background

Book depreciation is computed per IAS 16 using the method and rate configured on the asset class (straight-line or reducing balance). Tax depreciation is computed using URA-prescribed rates from the Income Tax Act Third Schedule, which define maximum allowable depreciation per asset class. The *tax base* of an asset after each period is its cost less cumulative tax depreciation; the *carrying amount* is its NBV per the books. Where the carrying amount exceeds the tax base, a deferred tax liability arises.

### 7.2.2 Deferred Tax Liability Formula

$$DTL = (TaxBase - CarryingAmount) \times TaxRate$$

where *TaxBase* is the asset's cost less cumulative tax depreciation, *CarryingAmount* is the NBV per book records, and *TaxRate* is the applicable corporate income tax rate (30% for Uganda as at the effective date of this SRS; configurable per tenant localisation profile).

Note: when *CarryingAmount > TaxBase*, the formula yields a negative value indicating a *Deferred Tax Liability*. When *TaxBase > CarryingAmount*, the difference is a *Deferred Tax Asset* (outside the scope of this module — [CONTEXT-GAP: deferred tax asset recognition policy]).

**FR-ASSET-058:** When an asset category is configured, the system shall provide a separate field for the *URA Tax Depreciation Rate* (percentage per annum) distinct from the book depreciation rate; this field is mandatory if the tenant's localisation profile has the Uganda tax jurisdiction enabled.

**FR-ASSET-059:** When the monthly depreciation run is executed, the system shall compute both the book depreciation charge (per FR-ASSET-013 or FR-ASSET-014) and the tax depreciation charge (using the URA rate and the reducing balance method as mandated by the Uganda Income Tax Act) for every active asset with a URA tax rate configured, and store both computed amounts separately on the depreciation run line record.

**FR-ASSET-060:** When the monthly depreciation run is posted, the system shall compute the cumulative deferred tax liability for each affected asset as:

$$DTL = (TaxBase - CarryingAmount) \times TaxRate$$

and post a GL journal for the period-end deferred tax movement: debit or credit the Deferred Tax Liability account and credit or debit the Income Tax Expense account for the change in DTL since the prior period, within the same atomic transaction as the book depreciation journal.

**FR-ASSET-061:** When an authorised user requests the Book vs. Tax Depreciation Report for a selected period, the system shall return a table with one row per asset showing: asset number, asset description, category, book NBV at period start, book depreciation charge, book NBV at period end, tax base at period start, tax depreciation charge, tax base at period end, temporary difference, tax rate, and DTL/DTA balance — exportable to Excel and PDF within ≤ 15 seconds at P95 for up to 5,000 assets.

**FR-ASSET-062:** When the URA tax depreciation rate for a category is updated, the system shall apply the new rate prospectively from the next depreciation run; historical tax depreciation records shall not be recalculated.

## 7.3 Vehicle Fleet Management

The requirements in this subsection apply to the asset-history and maintenance/compliance view of fleet vehicles. They do not transfer ownership of dispatching or live operational fleet control into Asset Management. If the Transportation module records operational trips, routes, telematics, or dispatch events, Asset Management may consume the resulting odometer, fuel, utilisation, or compliance evidence through integration while Transportation remains the authoritative operational system.

**FR-ASSET-063:** When an asset category is flagged as *Vehicle Fleet*, the system shall activate additional fleet data fields on the asset master record: vehicle registration number, make, model, year of manufacture, engine capacity (cc), fuel type (Petrol, Diesel, Electric, Hybrid), odometer reading at acquisition (km), and assigned driver.

**FR-ASSET-064:** When an authorised user records a mileage log entry for a fleet vehicle, the system shall require: trip date, starting odometer reading (km), ending odometer reading (km, > starting), trip purpose (free text, ≤ 200 characters), and driver identity; the system shall compute trip distance as *ending odometer − starting odometer* and update the vehicle's cumulative mileage on the asset record.

**FR-ASSET-065:** When an authorised user records a fuel log entry for a fleet vehicle, the system shall require: date, fuel quantity (litres, > 0), fuel cost per litre, total fuel cost, odometer reading at refuel, fuel station name, and driver identity; the system shall compute and store fuel consumption efficiency as *litres per 100 km* using the odometer reading change since the prior refuel entry.

**FR-ASSET-066:** When an authorised user records a vehicle service record, the system shall require: service date, service type (Routine Service, Oil Change, Tyre Replacement, Major Overhaul, or custom), odometer reading at service, service provider name, service cost, and a notes field (≤ 500 characters); the service record shall be linked to the asset's maintenance history log defined in Section 5.5.

**FR-ASSET-067:** When a fleet vehicle has a scheduled service interval configured (either by odometer distance in km or by calendar period), the system shall trigger a work order and in-app notification to the fleet manager when the vehicle's current odometer reading is within 500 km of the next service threshold, or when the calendar interval is within 7 days of the due date — whichever condition is met first.

**FR-ASSET-068:** When an authorised user requests the Fleet Utilisation Report for a selected date range, the system shall return a per-vehicle summary showing: total km travelled, total fuel consumed (litres), average fuel efficiency (L/100 km), total fuel cost, number of trips, number of services, total service cost, and current odometer reading; the report shall be exportable to Excel and PDF within ≤ 10 seconds at P95 for up to 500 vehicles.
