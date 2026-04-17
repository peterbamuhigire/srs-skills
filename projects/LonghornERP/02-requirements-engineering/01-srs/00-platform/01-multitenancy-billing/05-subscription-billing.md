## 5. Subscription Billing

### 5.1 Subscription Plans Reference

All prices are denominated in Ugandan Shillings (UGX). Annual billing charges 10 months and grants 12 months of access (2 months free). The following plans are available:

| Plan | UGX/month | Max Users | Max Branches | Add-Ons Included |
|---|---|---|---|---|
| Starter | 250,000 | 5 | 2 | None |
| Small Business | 500,000 | 15 | 5 | Any 2 |
| Professional | 1,000,000 | 30 | 10 | Any 5 |
| Business | 1,750,000 | 60 | 20 | All |
| Enterprise | 2,500,000 | Unlimited | Unlimited | All + priority support |

Pricing is org-wide; no per-user fee applies.

---

### 5.2 Plan Assignment and Upgrades

**FR-PLAT-040:** The system shall assign a subscription plan to a Tenant when a super admin selects a plan during provisioning or updates it via the billing management screen. The assigned plan shall determine: the monthly billing amount, the maximum active user count, the maximum branch count, and which Add-On Modules are included without additional charge.

*Verifiability:* Assign the Professional plan to a Tenant. Confirm the Tenant record stores the correct plan code, monthly amount (UGX 1,000,000), user limit (30), and branch limit (10).

---

**FR-PLAT-041:** The system shall enforce the user limit associated with the Tenant's active subscription plan. When a Tenant admin attempts to create a user account that would cause the active user count to exceed the plan limit, the system shall reject the action with a plan-limit-exceeded error and display the current plan's user limit and upgrade options.

*Verifiability:* Place a Tenant on the Starter plan (5-user limit) with 5 active users. Attempt to create a 6th user. Confirm HTTP 422 with `PLAN_USER_LIMIT_EXCEEDED` and the upgrade CTA.

---

**FR-PLAT-042:** The system shall enforce the branch limit associated with the Tenant's active subscription plan. When a Tenant admin attempts to create a branch that would exceed the plan limit, the system shall reject the action and display upgrade options.

*Verifiability:* Place a Tenant on the Starter plan (2-branch limit) with 2 branches. Attempt to create a 3rd branch. Confirm HTTP 422 with `PLAN_BRANCH_LIMIT_EXCEEDED`.

---

**FR-PLAT-043:** The system shall apply a plan upgrade immediately upon super admin confirmation. All additional module activations and limit increases granted by the new plan shall take effect within 60 seconds of the plan change being recorded.

*Verifiability:* Upgrade a Tenant from Starter to Professional. Confirm the user limit changes to 30, the branch limit to 10, and the 5 included Add-On slots become activatable within 60 seconds.

---

**FR-PLAT-044:** The system shall apply a plan downgrade at the end of the current billing cycle, not immediately. The Tenant shall retain access to the higher plan's features until the cycle end date.

*Verifiability:* Downgrade a Tenant from Business to Professional with 14 days remaining in the billing cycle. Confirm all Business-tier features remain accessible for those 14 days. Confirm the plan record updates to Professional at the cycle end date.

---

### 5.3 Billing Cycle Management

**FR-PLAT-045:** The system shall support two billing cycle modes for each Tenant: monthly (billed every 30 days) and annual (billed once per year, covering 12 months of access at a price equal to 10 months).

*Verifiability:* Configure a Tenant with annual billing at the Professional plan (UGX 1,000,000/month). Confirm the annual invoice amount is UGX 10,000,000. Confirm the access expiry date is 365 days from the invoice date.

---

**FR-PLAT-046:** The system shall generate a billing invoice for a Tenant 7 days before the next billing cycle start date. The invoice shall itemise: the base plan charge, any a-la-carte Add-On charges, and any outstanding balance carried forward from prior cycles.

*Verifiability:* Set a Tenant's next billing date to 7 days from today. Run the billing scheduler. Confirm an invoice record is created with the correct line items and total. Confirm the billing contact receives an email with the invoice attached.

---

**FR-PLAT-047:** The system shall carry forward any unpaid balance from a previous invoice to the next invoice as a separate line item labelled "Arrears".

*Verifiability:* Leave a Tenant with UGX 500,000 unpaid from the prior cycle. Generate the next invoice. Confirm a line item "Arrears: UGX 500,000" is present and the total reflects the combined amount.

---

### 5.4 Payment Recording

**FR-PLAT-048:** The system shall record a payment against a Tenant's outstanding invoice when a super admin submits a payment record containing: payment date, amount, currency, payment method, and reference number. The system shall mark the invoice as settled when the cumulative payments equal or exceed the invoice total.

*Verifiability:* Create an invoice for UGX 1,000,000. Record a partial payment of UGX 600,000. Confirm the invoice status is `PARTIAL`. Record a second payment of UGX 400,000. Confirm the invoice status changes to `SETTLED`.

---

**FR-PLAT-049:** The system shall support the following payment methods for recording: credit/debit card, bank transfer, MTN MoMo Business, and M-Pesa Daraja. Each payment record shall store the payment method code and the external reference returned by the payment gateway or bank.

`[CONTEXT-GAP: GAP-011]` — MTN MoMo Business bulk payment API specification is not yet available. This requirement's automated settlement confirmation behaviour depends on GAP-011 resolution.
`[CONTEXT-GAP: GAP-012]` — M-Pesa Daraja B2C API specification is not yet available.

*Verifiability:* Record one payment via each of the 4 supported methods. Confirm each record stores the correct method code and reference.

---

**FR-PLAT-050:** The system shall update the Tenant's lifecycle status from Overdue to Active within 60 seconds of a payment that brings the outstanding balance to zero and the current invoice to Settled status.

*Verifiability:* Place a Tenant in Overdue status with a single unpaid invoice. Record a payment that fully settles the invoice. Confirm status transitions to `ACTIVE` within 60 seconds.

---

### 5.5 Annual Billing Incentive

**FR-PLAT-051:** The system shall calculate the annual billing amount for any plan as $AnnualAmount = MonthlyRate \times 10$, granting the Tenant 12 months of access upon payment. The system shall display the effective monthly rate and the saving relative to 12 monthly payments when presenting the annual billing option.

*Verifiability:* For the Business plan at UGX 1,750,000/month, confirm the annual invoice total is UGX 17,500,000, the access period is 365 days, and the displayed saving is UGX 3,500,000 (2 months free).

---

### 5.6 A-La-Carte Add-On Billing

**FR-PLAT-052:** The system shall allow a super admin to attach one or more a-la-carte Add-On subscriptions to a Tenant whose plan permits a-la-carte purchases (Small Business and Professional plans only). The Starter plan shall not permit a-la-carte Add-On activation; a plan upgrade error shall be returned.

*Verifiability:* Attempt to add an a-la-carte module to a Starter Tenant. Confirm HTTP 422 with `PLAN_DOES_NOT_SUPPORT_ADDONS`. Add an a-la-carte module to a Small Business Tenant. Confirm activation succeeds and the module charge appears on the next invoice.

---

**FR-PLAT-053:** The system shall add the a-la-carte module charge to the Tenant's monthly invoice as a separate line item per module, using the published UGX pricing from the subscription plan catalogue.

*Verifiability:* Attach HR_PAYROLL (UGX 150,000) and ADV_INVENTORY (UGX 150,000) a-la-carte to a Small Business Tenant. Confirm the next invoice contains 2 separate line items totalling UGX 300,000, in addition to the base plan charge of UGX 500,000.

---

**FR-PLAT-054:** The system shall calculate the cumulative a-la-carte monthly add-on total for a Tenant at every billing cycle. When the cumulative total reaches ≥ 95% of the next subscription tier's monthly price, the system shall display a plan upgrade recommendation to the super admin before generating the invoice, showing the cost difference and the additional entitlements of the higher plan.

The threshold condition is: $AddOnTotal \geq NextTierMonthlyPrice \times 0.95$

*Verifiability:* Configure a Professional Tenant (UGX 1,000,000/month) with a-la-carte Add-Ons totalling UGX 1,662,500 (≥ 95% of Business tier UGX 1,750,000). Trigger the billing cycle. Confirm the super admin dashboard displays the upgrade recommendation before the invoice is finalised.

---

**FR-PLAT-055:** The system shall automatically add the POS module charge as UGX 100,000 per registered POS terminal per month, not as a flat module charge, when POS is activated as an a-la-carte Add-On.

*Verifiability:* Activate POS a-la-carte for a Tenant with 3 registered terminals. Confirm the next invoice line item for POS reads UGX 300,000 (3 × UGX 100,000).

---

**FR-PLAT-056:** The system shall record every billing event — invoice generation, payment receipt, plan change, add-on activation, add-on deactivation — to the Audit Log with Tenant ID, event type, amount, actor, and timestamp.

*Verifiability:* Execute each billing event type for a test Tenant. Confirm 1 Audit Log entry per event with all required fields.

---

**FR-PLAT-057:** The system shall prevent any billing data (invoice amounts, payment records, plan details) from being modified after the invoice is marked as Settled. Any attempt to edit a settled invoice via the API shall return HTTP 422 with `INVOICE_LOCKED`.

*Verifiability:* Settle a test invoice. Attempt a PATCH request to modify the invoice total. Confirm HTTP 422 with `INVOICE_LOCKED`.

---

**FR-PLAT-058:** The system shall generate invoice documents in PDF format containing: Chwezi Core Systems company details, Tenant organisation name, invoice number, invoice date, due date, line items with descriptions and amounts, subtotal, any applicable taxes, and total due in UGX.

`[CONTEXT-GAP: GAP-015]` — White-labelling policy is undecided. If white-labelling is approved for Enterprise Tenants, the company details on the invoice cover must be configurable per Tenant.

*Verifiability:* Generate an invoice for a test Tenant. Download the PDF. Confirm all required fields are present and the totals are arithmetically correct.

---

**FR-PLAT-059:** The system shall send the generated invoice PDF to the Tenant's registered billing contact email address on the invoice generation date.

*Verifiability:* Generate an invoice. Confirm an email with the PDF attachment is received at the billing contact address within 5 minutes of invoice generation.

---

**FR-PLAT-060:** The system shall allow a super admin to issue a billing credit to a Tenant (e.g., for disputed charges or service outage compensation). The credit shall appear as a negative line item on the next invoice and reduce the total due accordingly. Credits shall be recorded in the Audit Log with the authorising super admin identity and reason.

*Verifiability:* Issue a UGX 50,000 credit to a Tenant. Generate the next invoice. Confirm a line item "Credit: UGX -50,000" is present and the invoice total is reduced accordingly. Confirm the Audit Log contains the credit record with the super admin identity and reason text.
