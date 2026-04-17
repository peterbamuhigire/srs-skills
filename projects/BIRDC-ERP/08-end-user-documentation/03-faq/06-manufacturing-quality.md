# Topic 6: Manufacturing and Quality

---

**Q30. Why can't I transfer finished products to the saleable store?**

Finished goods from a production order are locked until the Quality Control module approves the batch. This is a system rule (BR-004) that cannot be bypassed. The **Transfer to Saleable Inventory** button on a production order remains inactive until:

- The QC Manager or lab technician has completed all inspection steps for the batch, and
- The inspection result is set to **Approved**, and
- A Certificate of Analysis has been issued.

Once these three conditions are met, the transfer button becomes active automatically. If you believe the QC inspection is complete but the button is still inactive, ask the QC Manager to confirm the inspection status and whether the Certificate of Analysis has been issued.

---

**Q31. What is the mass balance and what happens if it fails?**

The mass balance is a check that accounts for every kilogramme of raw matooke that enters the factory. The rule is:

> Total Input (kg) = Primary Product Output (kg) + By-product Output (kg) + Scrap/Waste (kg)

By-products include banana peels sent to the biogas digester and waste water processed into bio-slurry fertiliser. When Moses records production completion, the system calculates this equation automatically. If the result does not balance within the allowed tolerance of ±2%, the production order cannot be closed. The Production Supervisor reviews the entered quantities for data entry errors and corrects them. If the figures are accurate but the balance still fails, the Production Supervisor flags the order for management review. A mass balance variance report is generated automatically and sent to the Production Manager.

---

**Q32. Can I approve my own inspection results?**

No. The system enforces segregation of duties (BR-003) across all approval workflows, including QC. The person who records the inspection results cannot be the same person who approves the batch. In practice, a lab technician records the results and the QC Manager approves. If the QC Manager is also the one recording results (for example, in a small team), a second QC-authorised user must do the final approval. The system checks the user identity at the API level — you cannot bypass this by constructing a manual request.

---

**Q33. How do I generate a Certificate of Analysis for an export order?**

Export CoAs require market-specific parameters. See Section 6.3 of the User Manual for the full step-by-step procedure. In summary:

1. Complete the inspection and set the batch to **Approved**.
2. Open the batch record and click **Issue Certificate of Analysis**.
3. Select **Export** as the type.
4. Select the destination market (South Korea, Saudi Arabia, Qatar, Italy, or United States).
5. The system loads the template for that market, which includes all parameters required by that country's food import authority.
6. Confirm all parameters show passing results.
7. Issue and sign the certificate.

*A batch approved only for domestic use cannot be sent on an export order. The export CoA must be generated before the dispatch is processed.*
