# 2. Commodity Configuration Requirements

## 2.1 Overview

This section specifies requirements for configuring the commodities, grade classifications, price schedules, and seasonal parameters that govern all downstream intake and payment operations. Commodity configuration is performed by an authorised administrator and serves as the master reference data for the module.

## 2.2 Commodity Type Management

**FR-COOP-001** — When an administrator submits a new commodity record with a unique name, commodity category (e.g., Tea, Coffee, Sugarcane, Matooke), and unit of measure, the system shall create the commodity record and make it available for selection in intake, grade, and price configurations.

*Acceptance criterion:* A commodity named "Arabica Coffee" with unit "KG" is retrievable in the commodity list within 1 second of submission.

**FR-COOP-002** — When an administrator attempts to save a commodity record with a name that already exists within the same tenant, the system shall reject the submission and display the message: "A commodity with this name already exists."

*Acceptance criterion:* Duplicate name submission returns HTTP 409 and the error message; no duplicate record is created.

**FR-COOP-003** — When an administrator deactivates a commodity, the system shall prevent new intake records from referencing that commodity while preserving all historical intake and payment records that reference it.

*Acceptance criterion:* A deactivated commodity does not appear in the intake commodity selector; existing intake records remain intact and queryable.

## 2.3 Grade Configuration

**FR-COOP-004** — When an administrator opens a commodity record and adds a grade entry with a grade code, grade description, and active status, the system shall persist the grade and associate it with the parent commodity.

*Acceptance criterion:* For commodity "Robusta Coffee", grades "Grade A", "Grade B", and "Broken" are each saved and listed under that commodity in the grade management screen.

**FR-COOP-005** — When an administrator deactivates a grade, the system shall exclude that grade from the intake grade selector for new entries and flag any open intake batches that reference the deactivated grade with the warning: "Grade [code] is inactive — review intake batch [batch ID]."

*Acceptance criterion:* Deactivating "Broken" removes it from the intake form grade dropdown and triggers the warning for any open batches containing it.

**FR-COOP-006** — When an administrator assigns a price to a grade for a specified season, the system shall store the grade-price record linked to the season, commodity, and grade, and apply this price as the default unit price during intake recording.

*Acceptance criterion:* Grade "Grade A" for "Tea" in season "2025 Long Rains" has price UGX 450/kg; a new intake entry auto-populates 450 as the unit price when Grade A Tea is selected.

## 2.4 Price-Per-Grade Management

**FR-COOP-007** — When an administrator sets a floor price for a commodity-grade-season combination, the system shall reject any manual price entry during intake that is below the floor price and display: "Entered price UGX [amount] is below the floor price of UGX [floor]."

*Acceptance criterion:* Floor price UGX 400/kg; a manual entry of UGX 380/kg is rejected with the specified message.

**FR-COOP-008** — When an administrator updates a grade price mid-season, the system shall apply the new price only to intake entries created after the effective date and retain the old price on entries created before that date.

*Acceptance criterion:* Intake entry dated 2025-03-01 retains UGX 450/kg; entry dated 2025-03-15 (after price change to UGX 470/kg on 2025-03-10) shows UGX 470/kg.

**FR-COOP-009** — When an administrator configures a premium percentage for a grade, the system shall calculate the effective price as:

$EffectivePrice = BaseGradePrice \times (1 + PremiumRate)$

and store the effective price on the intake entry.

*Acceptance criterion:* Base price UGX 450, premium 10% → effective price UGX 495.00 stored on the intake record.

## 2.5 Seasonal Configuration

**FR-COOP-010** — When an administrator creates a season record with a name, start date, end date, and linked commodity, the system shall activate the season on the start date, accept intake entries throughout the season window, and automatically close intake on the end date at 23:59 server time.

*Acceptance criterion:* Season "2025 Long Rains Tea" with end date 2025-06-30 accepts intake on 2025-06-30 at 23:58 and rejects intake attempted on 2025-07-01 with: "Season is closed."

[CONTEXT-GAP: Maximum number of overlapping active seasons per commodity per tenant — confirm whether a commodity can have concurrent seasons (e.g., two harvests per year).]
