## 6. Non-Functional Requirements

All NFRs in this section apply to the Multi-Tenancy engine, Tenant Lifecycle service, Module Activation subsystem, and Subscription Billing service. Performance thresholds are defined at the 95th percentile (P95) under normal load unless otherwise stated.

---

**NFR-PLAT-001:** The system shall provision a new Tenant and make it operational within 10 minutes of super admin confirmation. Operational is defined as: Tenant record created, Core Modules activated, COA seeded, Head Office branch created, and primary admin user able to complete a successful login. Measurement window: from provisioning form submission to first successful authentication by the Tenant admin.

*Verifiability:* Provision 10 new Tenants consecutively during a load test. Record the elapsed time from form submission to first successful login for each. Confirm all 10 complete within 600 seconds.

---

**NFR-PLAT-002:** The system shall enforce Tenant data isolation such that no database query, API response, or report output returns data belonging to any Tenant other than the authenticated Tenant. A cross-tenant data leak of any kind is classified as a Critical severity defect and triggers immediate incident response under the security incident protocol.

The isolation mechanism is `tenant_id` column enforcement on every data table, applied at the ORM query layer, never accepted from client-supplied request parameters. See GAP-004 for the mandatory independent security review prior to first Tenant onboarding.

*Verifiability:* Execute a test suite that attempts 50 cross-tenant data access scenarios (direct API calls, manipulated JWT claims, forged request parameters). Confirm zero cross-tenant records are returned in any response. The test suite must be run after any change to the Tenant Context service.

---

**NFR-PLAT-003:** The system shall support ≥ 500 concurrent active Tenants on a single deployment instance without the P95 API response time degrading below the thresholds stated in the system-wide performance NFR (NFR-PERF-001). Concurrent active is defined as Tenants with at least 1 authenticated user session within the preceding 5-minute window.

*Verifiability:* Load test with 500 simulated concurrent Tenants, each with 5 active sessions. Measure P95 response times for the 10 most-called API endpoints. Confirm no endpoint exceeds its NFR-PERF-001 threshold.

---

**NFR-PLAT-004:** The system shall complete Add-On Module activation — including database record creation, navigation cache invalidation, and permission enforcement — within 60 seconds of super admin confirmation.

*Verifiability:* Activate 5 Add-On Modules on 10 test Tenants simultaneously (50 concurrent activations). Confirm all 50 activations complete within 60 seconds, measured from super admin confirmation to confirmed module accessibility by the Tenant admin.

---

**NFR-PLAT-005:** The system shall complete each Tenant lifecycle state transition — including access flag updates, notification dispatch, and Audit Log write — within 60 seconds of the triggering event (payment confirmation or scheduler execution).

*Verifiability:* Trigger all 8 permitted state transitions for 10 test Tenants concurrently (80 transitions). Confirm all transitions complete within 60 seconds each.

---

**NFR-PLAT-006:** The system shall retain all billing records (invoices, payments, credits, plan history) for a minimum of 7 years from the date of creation, consistent with the Audit Log retention policy, to support financial audit and tax compliance obligations.

*Verifiability:* Confirm no automated deletion job targets the `invoices`, `payments`, `billing_credits`, or `plan_history` tables within the 7-year retention window. Review the data retention configuration document.

---

**NFR-PLAT-007:** The system shall deliver billing notification emails (invoice generation, overdue notice, suspension warning, payment confirmation) within 5 minutes of the triggering event, measured from event occurrence to confirmed email dispatch by the mail service.

*Verifiability:* Trigger each of the 5 notification event types for a test Tenant. Record the timestamp of the triggering event and the timestamp of the email dispatch log entry. Confirm all 5 deliveries occur within 300 seconds.

---

**NFR-PLAT-008:** The system shall not expose tenant subscription plan details, billing amounts, or payment method data in any client-facing API response beyond the authenticated Tenant's own billing screens. Cross-tenant billing data access by any non-super-admin user shall return HTTP 403.

*Verifiability:* Authenticate as a Tenant admin of Tenant A. Attempt to call the billing API for Tenant B using Tenant A's JWT. Confirm HTTP 403 and confirm no Tenant B data is disclosed in the response body or headers.
