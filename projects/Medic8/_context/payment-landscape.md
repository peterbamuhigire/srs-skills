# Payment Landscape -- Medic8 Healthcare Management System

---

## Mobile Money (Primary Payment Channel)

### MTN Mobile Money (MoMo)

Uganda's dominant mobile money platform. API integration covers 3 payment flows:

- **Patient fee payment** -- patient initiates payment from their phone; system auto-reconciles to the patient account using the transaction reference
- **Cashier verification** -- patient shows payment reference at the cashier desk; cashier confirms receipt in Medic8 before services are rendered
- **Subscription payment** -- health facility pays Medic8 subscription via MoMo

### Airtel Money

Second-largest mobile money platform in Uganda. Same API integration pattern as MTN MoMo for all 3 payment flows.

### M-Pesa (Kenya/Tanzania Expansion)

Safaricom's mobile money platform. Required for Kenya and Tanzania market entry. Integration pattern mirrors MoMo/Airtel Money.

### UPI (India Market)

Unified Payments Interface for India market expansion. Real-time bank-to-bank payment.

### Australia

No mobile money integration required. Standard card and bank payment infrastructure applies.

---

## Insurance Schemes (Uganda)

### National Schemes

- **NHIS (National Health Insurance Scheme)** -- launched 2023, mandatory contributory scheme. Pre-load benefit schedule and claims format. Register with NHIS as licensed healthcare software provider.

### Private Insurers

- AAR Healthcare
- Jubilee Health Insurance
- Prudential
- Resolution Health
- AON
- ICEA
- NIC
- UAP

### Corporate Schemes

- UNICEF staff health scheme
- WFP staff health scheme
- Makerere University staff scheme
- Ministry of Health staff scheme

### Mission and NGO Schemes

- AMDA (Association of Medical Doctors of Asia)
- ICHA (International Christian Health Association)
- Church-based medical schemes (Catholic, Anglican, SDA health networks)

---

## Donor Funding

### PEPFAR (USAID)

Ring-fenced fund accounting for HIV/TB programmes. Separate commodity tracking for ARVs, test kits, and contraceptives. Expenditure reports per programme area aligned to PEPFAR MER indicators.

### Global Fund

Separate cost centres for malaria, TB, and HIV grants. Expenditure reports per grant period. Procurement tracking for grant-funded commodities.

### UNICEF

Nutrition programme funding. RUTF (Ready-to-Use Therapeutic Food) procurement and distribution tracking.

### WHO

Operational grants and HMIS system support. Expenditure reporting per grant agreement.

---

## Government Grants

### Capitation Grants

For government-aided health facilities. Record receipt of funds and report expenditure to the District Health Officer (DHO).

### PHC (Primary Health Care) Grants

Conditional grants for specific health interventions (immunisation, maternal health, malaria). Track expenditure against approved budget lines.

### NSSF/PAYE Remittance

Statutory payroll deductions per URA (Uganda Revenue Authority) and NSSF (National Social Security Fund) requirements. Medic8 HR module calculates and generates remittance schedules.

---

## Subscription Payment

Health facilities pay Medic8 subscription via:

- MTN Mobile Money
- Airtel Money
- Bank transfer
- Card payment

**Billing model:**

- Monthly or annual billing (annual subscription includes 2 months free)
- No setup fees
- No per-user charges -- unlimited users within a facility
- Pricing published in UGX on the Medic8 website
