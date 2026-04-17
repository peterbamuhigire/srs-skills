## 4. Module Activation

### 4.1 Overview

Module activation controls which feature sets are accessible to each Tenant. Core Modules are permanently active and cannot be deactivated. Add-On Modules are activated per Tenant when included in the Tenant's subscription plan or purchased as a-la-carte additions.

---

**FR-PLAT-030:** The system shall activate an Add-On Module for a Tenant when a super admin records a confirmed subscription to that module for that Tenant. Activation shall complete within 60 seconds and the module's navigation items shall be visible to all Tenant users with appropriate role permissions upon next page load.

*Verifiability:* Record an Add-On subscription for a test Tenant. Confirm the module appears in the Tenant navigation within 60 seconds. Confirm a Tenant user with a role that includes the module's permissions can access the module's main screen.

---

**FR-PLAT-031:** The system shall deactivate an Add-On Module for a Tenant when the subscription for that module lapses (i.e., the billing period ends without renewal payment). Deactivation shall complete within 24 hours of lapse. Existing data created by the deactivated module shall be retained and remain accessible to the super admin via the data export tool.

*Verifiability:* Allow an Add-On module subscription to lapse. Confirm the module is absent from Tenant navigation within 24 hours. Confirm the super admin can export the module's data via the admin panel.

---

**FR-PLAT-032:** The system shall prevent activation of an Add-On Module for a Tenant if one or more of that module's declared dependencies are not currently active for that Tenant. The system shall return a dependency error listing all unmet dependencies by module name and code.

`[CONTEXT-GAP: GAP-005]` — A formal module dependency map has not been defined. This requirement shall be fully implementable only after GAP-005 is resolved. As an interim, the following known dependencies apply:

- MANUFACTURING depends on ADV_INVENTORY.
- COOPERATIVE depends on INVENTORY.
- ADV_INVENTORY depends on INVENTORY (Core — always met).
- SALES_CRM depends on SALES (Core — always met).
- SALES_AGENTS depends on SALES (Core — always met).

*Verifiability:* Attempt to activate MANUFACTURING for a Tenant that does not have ADV_INVENTORY active. Confirm the system returns a dependency error naming ADV_INVENTORY. Activate ADV_INVENTORY first, then retry MANUFACTURING activation. Confirm activation succeeds.

---

**FR-PLAT-033:** The system shall display only the navigation items for modules that are currently active for the authenticated Tenant. Navigation items for inactive modules shall not be rendered in the UI or returned in the navigation API response.

*Verifiability:* Log in to a Tenant that has only Core Modules active. Confirm the navigation contains no Add-On module entries. Activate HR_PAYROLL for that Tenant. Reload the UI. Confirm the HR & Payroll navigation item is now present.

---

**FR-PLAT-034:** The system shall prevent a user from accessing any route, API endpoint, or data belonging to an inactive module, returning HTTP 403 with a module-not-activated error code, even if the user's role includes permissions for that module.

*Verifiability:* Assign a role with HR_PAYROLL permissions to a user on a Tenant that does not have HR_PAYROLL activated. Attempt a direct HTTP call to an HR_PAYROLL endpoint. Confirm HTTP 403 with error code `MODULE_NOT_ACTIVATED`.

---

**FR-PLAT-035:** The system shall prevent deactivation of any Core Module (ACCOUNTING, INVENTORY, SALES, PROCUREMENT, USER_MGMT, AUDIT). Any super admin request to deactivate a Core Module shall return HTTP 422 with an explanatory error.

*Verifiability:* Attempt an API call to deactivate ACCOUNTING for any Tenant. Confirm HTTP 422 and confirm the module remains active.

---

**FR-PLAT-036:** The system shall automatically activate all Add-On Modules included in a Tenant's subscription plan when that plan is assigned or upgraded. The system shall activate only the included modules without requiring individual super admin activation per module.

*Verifiability:* Assign the Business plan (Core + all Add-Ons) to a new Tenant. Confirm all 10 Add-On Module records are created with `status = 'ACTIVE'` without additional super admin actions.

---

**FR-PLAT-037:** The system shall deactivate any Add-On Module that is no longer included in a Tenant's plan when the Tenant's plan is downgraded, effective at the end of the current billing cycle. The system shall notify the billing contact of the impending module deactivations at least 7 days before the billing cycle end date.

*Verifiability:* Downgrade a Tenant from Professional (5 Add-Ons) to Starter (0 Add-Ons). Confirm a notification email lists the 5 modules to be deactivated 7 days before the cycle end. Confirm all 5 modules deactivate at the cycle end date.

---

**FR-PLAT-038:** The system shall record every module activation and deactivation event — Tenant ID, module code, action (ACTIVATED / DEACTIVATED), trigger (plan change, super admin, subscription lapse), timestamp, and actor — to the Audit Log as an immutable record.

*Verifiability:* Activate and deactivate a test module. Confirm the Audit Log contains 2 records with all required fields.
