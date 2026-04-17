## 3. Tenant Lifecycle

### 3.1 State Model

A Tenant exists in exactly one of the following states at any point in time:

| State | Meaning |
|---|---|
| Trial | Tenant is within the 30-day free trial period. Full access to all provisioned modules. |
| Active | Subscription is current and all payments are up to date. Full access. |
| Overdue | A billing cycle has passed without payment. Access is restricted. |
| Suspended | The grace period has elapsed without payment. Minimum read-only access only. |
| Archived | Tenant has been inactive beyond the extended suspension period. All access revoked; data retained. |

The permitted state transitions are:

- Trial → Active (first payment received)
- Trial → Overdue (trial period expires without conversion)
- Active → Overdue (billing cycle passes without payment)
- Overdue → Active (outstanding payment received within grace period)
- Overdue → Suspended (grace period elapses without payment)
- Suspended → Active (full outstanding balance paid)
- Suspended → Archived (extended suspension period elapses without payment)
- Archived → Active (super admin manual reactivation on full balance settlement — requires super admin action)

No other transitions are permitted by the system.

---

### 3.2 State Transition Requirements

**FR-PLAT-011:** The system shall transition a Tenant from Trial to Active when a payment record for the first billing cycle is confirmed as settled. The transition shall complete within 60 seconds of payment confirmation.

*Verifiability:* Record a first payment for a Trial Tenant. Confirm `tenant.status` changes to `ACTIVE` within 60 seconds. Confirm Audit Log records the transition with timestamp and triggering payment ID.

---

**FR-PLAT-012:** The system shall transition a Tenant from Trial to Overdue when the trial expiry date is reached and no payment has been received. The transition shall be executed by an automated scheduled process running at 00:05 UTC daily.

*Verifiability:* Set a test Tenant's trial expiry to the previous day with no payment recorded. Run the lifecycle scheduler. Confirm `tenant.status` changes to `OVERDUE` and the Tenant's users receive an overdue notification.

---

**FR-PLAT-013:** The system shall transition a Tenant from Active to Overdue when a billing cycle end date passes without a payment recorded against the due invoice. The transition shall be executed by the automated lifecycle scheduler within 24 hours of the billing cycle end date.

*Verifiability:* Advance a test Active Tenant's billing cycle end date to yesterday with no payment. Run the scheduler. Confirm status transitions to `OVERDUE` and an overdue invoice notification is sent to the billing contact.

---

**FR-PLAT-014:** The system shall grant a 7-day grace period to an Overdue Tenant, during which full system access is retained and the billing contact receives a payment reminder notification every 48 hours.

*Verifiability:* Transition a Tenant to Overdue. Confirm all users retain full access. Confirm reminder notifications are sent on day 1, day 3, and day 5. Confirm no Suspended transition occurs before day 7 elapses.

---

**FR-PLAT-015:** The system shall transition a Tenant from Overdue to Suspended when the 7-day grace period elapses without receipt of the outstanding payment.

*Verifiability:* Set a test Tenant to Overdue with the overdue date 8 days in the past and no payment recorded. Run the scheduler. Confirm status transitions to `SUSPENDED`.

---

**FR-PLAT-016:** The system shall transition a Tenant from Overdue to Active when the outstanding balance is paid in full before the grace period expires. The transition shall complete within 60 seconds of payment confirmation.

*Verifiability:* Set a Tenant to Overdue within the 7-day grace window. Record a payment covering the full outstanding balance. Confirm status transitions to `ACTIVE` within 60 seconds.

---

**FR-PLAT-017:** The system shall restrict a Suspended Tenant's user access to read-only retrieval of financial data for export purposes only. All create, edit, approve, and delete operations shall return HTTP 403 with a message directing the user to the billing contact.

*Verifiability:* Suspend a test Tenant. Log in as a Tenant user. Attempt to create a sales order. Confirm HTTP 403. Confirm the user can open and export an existing financial report.

---

**FR-PLAT-018:** The system shall transition a Suspended Tenant from Suspended to Active when the full outstanding balance (all unpaid invoices) is recorded as paid. The transition shall restore full access within 60 seconds of payment confirmation.

*Verifiability:* Suspend a test Tenant with 2 unpaid invoices. Record payment for invoice 1 only. Confirm status remains `SUSPENDED`. Record payment for invoice 2. Confirm status transitions to `ACTIVE` within 60 seconds and full access is restored.

---

**FR-PLAT-019:** The system shall transition a Suspended Tenant to Archived when 90 consecutive days elapse without receipt of the outstanding balance.

*Verifiability:* Set a test Tenant to Suspended with the suspension date 91 days in the past and no payment. Run the scheduler. Confirm status transitions to `ARCHIVED`.

---

**FR-PLAT-020:** The system shall revoke all user access to an Archived Tenant. All login attempts by users of an Archived Tenant shall return an account-archived error message with a contact email for data retrieval requests.

*Verifiability:* Archive a test Tenant. Attempt login as any Tenant user. Confirm authentication is rejected with the account-archived message and the support contact email.

---

**FR-PLAT-021:** The system shall retain all data for an Archived Tenant for a minimum of 7 years from the archival date, consistent with the Audit Log retention policy, to support legal and tax obligations.

*Verifiability:* Archive a test Tenant. Confirm data records remain queryable by the super admin after archival. Confirm no automated deletion occurs during the 7-year retention window.

---

**FR-PLAT-022:** The system shall allow a super admin to manually reactivate an Archived Tenant to Active status upon confirmation that all outstanding balances have been settled. The reactivation shall restore all user access and module activations as they existed at the time of archival.

*Verifiability:* Archive a Tenant. Record settlement of all outstanding invoices. Execute super admin reactivation. Confirm status returns to `ACTIVE`, all previously active modules are restored, and Tenant users can authenticate successfully.

---

**FR-PLAT-023:** The system shall log every Tenant state transition — trigger event, previous state, new state, timestamp, and actor (scheduler or super admin identity) — to the Audit Log as an immutable record.

*Verifiability:* Trigger each of the 8 permitted transitions for a test Tenant. Confirm the Audit Log contains a record for each transition with all required fields populated.
