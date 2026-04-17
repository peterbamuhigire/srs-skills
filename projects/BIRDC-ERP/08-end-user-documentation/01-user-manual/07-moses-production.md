# Section 7: Moses — Production Supervisor

Moses uses the Factory Floor Android App on the production floor and the Manufacturing module in the main ERP web application for planning and reporting.

---

## 7.1 Creating a Production Order

1. Log in to the ERP web application and click **Manufacturing** in the main menu.
2. Click **Production Orders**, then click **New Production Order**.
3. Select the **Product** to be manufactured (for example, Tooke Banana Flour 1 kg).
4. Enter the **Planned Quantity** to produce.
5. Select the **Recipe/Bill of Materials** version to use. The system shows all input materials and their required quantities.
6. Set the **Planned Start Date** and **Planned End Date**.
7. Assign workers using the **Assign Workers** tab.
8. Click **Create Order**. The production order status is **Planned**.
9. When you are ready to start production, click **Release Order**. Status changes to **In Progress** and materials are reserved.

---

## 7.2 Recording Production Completion and By-Products

When a production run is finished:

1. Open the production order in the Factory Floor App (or in the web application).
2. Tap **Record Completion**.
3. Enter the **Actual Output Quantity (kg)** of the primary product (for example, 480 kg of banana flour).
4. Enter the by-products:
   - **Banana Peel → Biogas:** enter the weight of peels (kg) sent to the biogas digester. The system calculates the calorific energy output (MJ) based on the configured conversion factor.
   - **Waste Water → Bio-slurry:** enter the volume of waste water (litres) processed. The system calculates the bio-slurry output (kg) based on the configured conversion factor.
5. Enter any **Scrap/Waste (kg)** that could not be converted to a product.
6. Click **Save**.

---

## 7.3 Verifying the Mass Balance

The mass balance equation is:

> Total Input (kg) = Primary Product Output (kg) + By-product Output (kg) + Scrap/Waste (kg)

The system calculates this automatically when you save your completion record.

1. After saving the completion record, tap **View Mass Balance** (or click it in the web application).
2. The screen shows each component of the equation and the calculated total.
3. If the totals balance within the allowed tolerance (±2%), the status shows **Mass Balance: OK** in green.
4. If the totals do not balance, the status shows **Mass Balance: FAIL** in red. The production order cannot be closed.
5. If the mass balance fails:
   a. Review your input and output figures for data entry errors.
   b. Correct any wrong entries and tap **Recalculate**.
   c. If the figures are correct but the balance still fails, tap **Flag for Review**. A variance report is generated and sent to your supervisor for investigation.
6. Once the mass balance is confirmed OK, click **Close Production Order**. The finished goods batch moves to the QC queue for inspection.
