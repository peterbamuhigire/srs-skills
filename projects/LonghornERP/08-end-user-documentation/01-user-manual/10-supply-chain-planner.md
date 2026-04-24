# Supply Chain Planner Guide

**Role:** Supply Chain Planner

**Accessible modules:** Supply Chain Planning, Inventory, Procurement (read context), Manufacturing (read context where active)

---

## Creating a Demand Plan

1. In the sidebar, click **Supply Chain Planning**, then click **Demand Plans**.
2. Click **New Demand Plan**.
3. Select the **Planning Horizon**.
4. Select the **Item Scope**, **Location Scope**, and optional **Channel** filters.
5. Click **Generate Baseline**.
6. Review the baseline values and the exception list.
7. Save the version.

---

## Applying an Override

1. Open the demand plan version.
2. Click the line you want to adjust.
3. Enter the **Override Quantity**.
4. Select a **Reason Code**.
5. Enter a short note explaining the business reason.
6. Set the **Override Expiry Date** if required.
7. Click **Save Override**.

---

## Running a Supply Plan

1. Open **Supply Chain Planning > Supply Plans**.
2. Click **New Supply Plan**.
3. Select the approved **Demand Plan Version**.
4. Select the **Planning Horizon** and the relevant supply locations.
5. Click **Run Plan**.
6. Review shortages, late supply, and policy exceptions in the exception workbench.

---

## Comparing a Scenario

1. Open **Supply Chain Planning > Scenarios**.
2. Click **Create Scenario From Plan**.
3. Select the released or working plan you want to clone.
4. Rename the scenario clearly, for example **Supplier Delay - 2 Weeks**.
5. Make the planning adjustments required for the scenario.
6. Click **Compare to Current Plan**.
7. Review the service, inventory, shortage, and financial impact summary before presenting the scenario for decision.

---

## Releasing an Approved Plan

1. Open the approved supply plan.
2. Confirm that all required exceptions are resolved or escalated.
3. Click **Release Recommendations**.
4. Review the confirmation dialog showing the number of planned purchase, production, or transfer recommendations to be published.
5. Click **Confirm Release**.
6. Verify that the plan status changes to **Released** and that the downstream recommendation log shows exactly 1 successful publication event.
