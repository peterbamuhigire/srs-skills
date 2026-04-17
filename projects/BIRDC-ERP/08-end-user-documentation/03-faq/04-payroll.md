# Topic 4: Payroll

---

**Q20. Why can't I edit the approved payroll run?**

Once the Finance Manager approves and locks a payroll run, it is permanently immutable. This is a legal and audit control (BR-010). The approved payroll run is the authoritative record of what each employee was paid that month — it cannot be changed because it feeds directly into PAYE remittance to URA, NSSF returns, and the General Ledger. The lock record shows the approver's name and the exact time of approval. Any attempt to unlock or edit a locked payroll is blocked at the system level and flagged in the audit trail.

---

**Q21. How do I correct a payroll error from a previous month?**

You cannot modify the original payroll run. Process a correction run in the current payroll period:

1. Click **Payroll** then **Correction Run**.
2. Select the employee whose pay needs correcting.
3. Enter the difference: if the employee was underpaid by UGX 50,000, enter +50,000. If overpaid, enter -50,000.
4. Enter the reason for the correction.
5. The correction run goes through the same approval process as a regular payroll run.
6. Once approved, the correction amount is included in the employee's next payslip as a separate line item labelled "Payroll Correction — [Month]."

*PAYE and NSSF on the correction are calculated in the current period, not retroactively. For large corrections that significantly affect tax liability, seek advice from the Finance Director.*

---

**Q22. How do I update the PAYE tax bands when URA publishes new rates?**

The Finance Director updates PAYE tax bands directly in the system — no developer involvement is needed:

1. Click **Payroll** then **PAYE Tax Bands**.
2. Click **Edit Bands**.
3. Update the income brackets and corresponding tax rates to match the URA published schedule.
4. Set the **Effective From** date to the first day of the applicable period.
5. Click **Save**.

The updated bands apply automatically to all payroll runs processed on or after the effective date. Historical payroll runs are not affected.

---

**Q23. How do I add a new payroll element (for example, a new allowance)?**

The Finance Director or IT Administrator can add a new payroll element:

1. Click **Payroll** then **Payroll Elements**.
2. Click **New Element**.
3. Enter the element name (for example, "Field Allowance").
4. Select the type: **Earning** (adds to gross pay) or **Deduction** (reduces net pay).
5. Set the calculation method: fixed amount, percentage of basic salary, or formula.
6. Select the General Ledger account this element should post to (confirm the correct account with the Finance Director).
7. Click **Save**.
8. On the next payroll run, assign the new element to the relevant employees from their individual employee records.

---

**Q24. What is LST and how is it configured?**

Local Service Tax (LST) is a small annual tax levied by local governments on employees. The rate varies by local government. BIRDC staff based in Bushenyi pay at the Bushenyi rate. Staff working in Kampala pay at the Kampala rate. To update an LST rate when a local government publishes a new ordinance:

1. Click **Payroll** then **LST Rates**.
2. Find the local government in the list (Bushenyi or Kampala).
3. Click **Edit** and update the annual LST amount.
4. Set the **Effective From** date.
5. Click **Save**. The new rate applies on the next payroll run.
