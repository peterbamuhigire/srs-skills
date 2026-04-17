# Commission Rule Engine

## 4.1 Overview

The commission rule engine allows each tenant to configure the method and rates used to calculate agent commissions without developer intervention. Three rule types are supported: flat rate, tiered, and product-specific. Rules are versioned and effective-dated so that historical commission runs always use the rule set that was active at the time of the run.

## 4.2 Rule Lifecycle Management

**FR-AGENT-021** — When an authorised user creates a commission rule via the **Commission Rules** configuration screen, the system shall require the following fields: **Rule Name**, **Rule Type** (`FlatRate`, `Tiered`, or `ProductSpecific`), **Effective From Date**, and at least one rate definition. The system shall reject the form if a rule of the same type with an overlapping effective date range already exists for the same scope (tenant-wide or agent-specific), returning error `RULE_OVERLAP`.

**Test oracle:** Creating a second flat-rate rule effective 2026-04-01 when one already covers 2026-03-01 to present returns `RULE_OVERLAP`.

---

**FR-AGENT-022** — When an authorised user saves a commission rule, the system shall assign it a unique **Rule ID** in the format `CR-{YYYYMMDD}-{NNN}` and set its status to `Active`. The rule shall become available for selection in commission run configuration immediately upon saving.

**Test oracle:** After saving, the rule appears in the commission run rule selection list with its **Rule ID** and status `Active`.

---

**FR-AGENT-023** — When an authorised user deactivates a commission rule with status `Active`, the system shall set its **Effective To Date** to the current date, change its status to `Inactive`, and prevent it from being applied to any new commission run. Existing commission runs that reference the rule shall retain their computed values.

**Test oracle:** After deactivation, new commission run creation does not list the deactivated rule; existing run records continue to display the deactivated rule's name and computed values.

## 4.3 Flat Rate Rules

**FR-AGENT-024** — When the rule type is `FlatRate`, the system shall apply a single percentage rate to the total attributed sales amount for the agent within the commission period. The commission amount shall be computed as:

$$Commission_{Flat} = AttributedSales \times Rate_{Flat}$$

where $Rate_{Flat}$ is expressed as a decimal (e.g., 0.05 for 5%).

**Test oracle:** An agent with attributed sales of UGX 4,000,000 and a flat rate of 5% (0.05) yields a computed commission of exactly UGX 200,000.

## 4.4 Tiered Rate Rules

**FR-AGENT-025** — When the rule type is `Tiered`, the system shall allow the authorised user to define up to 10 tiers, each with a **Threshold From** (inclusive), **Threshold To** (exclusive, or "unlimited" for the final tier), and **Rate**. The system shall apply the rate corresponding to the tier that contains the agent's total attributed sales for the period.

**Test oracle:** Three tiers — UGX 0–1,000,000 at 3%, UGX 1,000,000–3,000,000 at 5%, UGX 3,000,000+ at 7% — applied to attributed sales of UGX 3,500,000 yields a commission of UGX 245,000 (UGX 3,500,000 × 0.07).

---

**FR-AGENT-026** — When configuring a tiered rule, the system shall validate that tier threshold ranges are contiguous (no gaps and no overlaps) and that each rate value is greater than 0% and less than or equal to 100%. The system shall reject the form and display the specific validation error if either condition is violated.

**Test oracle:** Defining tiers with a gap (e.g., UGX 0–500,000 and UGX 600,000+) returns error `TIER_GAP_DETECTED` identifying the gap range.

---

**FR-AGENT-027** — When the tenant configuration flag `TierCalculationMethod` is set to `Cumulative`, the system shall calculate commission by applying each tier's rate only to the sales amount that falls within that tier's range (marginal method), not to the total. The commission shall be computed as:

$$Commission_{Cumulative} = \sum_{i=1}^{n} \min(Sales, T_i^{max}) - T_i^{min}) \times Rate_i$$

where $T_i^{min}$ and $T_i^{max}$ are the lower and upper bounds of tier $i$ and computation stops when remaining sales are exhausted.

**Test oracle:** Three tiers — UGX 0–1,000,000 at 3%, UGX 1,000,000–3,000,000 at 5%, UGX 3,000,000+ at 7% — applied to UGX 3,500,000 under `Cumulative` method yields: (1,000,000 × 0.03) + (2,000,000 × 0.05) + (500,000 × 0.07) = 30,000 + 100,000 + 35,000 = UGX 165,000.

## 4.5 Product-Specific Rules

**FR-AGENT-028** — When the rule type is `ProductSpecific`, the system shall allow the authorised user to assign a distinct rate (flat or tiered) to each product or product category. Attribution records for each product shall be multiplied by their respective rate, and the total commission shall be the sum of all product-level amounts:

$$Commission_{ProductSpecific} = \sum_{p=1}^{m} AttributedSales_p \times Rate_p$$

**Test oracle:** An agent with product A sales of UGX 1,000,000 at 4% and product B sales of UGX 2,000,000 at 6% yields total commission of (40,000 + 120,000) = UGX 160,000.

---

**FR-AGENT-029** — When a `ProductSpecific` rule is applied and an attributed invoice contains a product with no defined rate in the rule, the system shall log a warning `RATE_NOT_DEFINED_FOR_PRODUCT` for that line item, exclude it from the commission calculation for the run, and include the warning in the commission run exception report.

**Test oracle:** A commission run with one product missing a rate produces a run exception report that names the product and shows its attributed amount as excluded from the commission total.

## 4.6 Agent-Level Rule Override

**FR-AGENT-030** — When an authorised user assigns an agent-specific commission rule override via the **Agent Commission Override** panel, the system shall apply the override rule in place of the tenant-wide rule for that agent during commission runs. The override record shall store **Agent ID**, **Rule ID**, **Effective From Date**, and **Effective To Date** (nullable). The override history shall be fully preserved and auditable.

**Test oracle:** An agent with an active override rule receives commission calculated using the override rule; other agents in the same run receive the tenant-wide rule. The run summary differentiates overridden agents with a flag `Override Applied`.
