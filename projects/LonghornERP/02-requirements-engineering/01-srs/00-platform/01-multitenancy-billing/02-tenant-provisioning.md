## 2. Tenant Provisioning

This section specifies functional requirements for creating and initialising a new Tenant record. All provisioning actions are performed by a super admin (a platform-level operator, not a Tenant user). The super admin role resides outside the Tenant data boundary and has no access to Tenant business data.

---

**FR-PLAT-001:** The system shall create a new Tenant record when a super admin submits a valid provisioning form containing: organisation name, primary contact name, primary contact email, country, and subscription plan.

*Verifiability:* Submit a provisioning form with all required fields populated. The system returns HTTP 201 and the Tenant record is readable from the admin panel within 10 seconds.

---

**FR-PLAT-002:** The system shall assign a unique, URL-safe slug to each Tenant at creation time. The slug shall be derived from the organisation name, lowercased, with spaces replaced by hyphens and special characters stripped. If the derived slug already exists, the system shall append a numeric suffix (e.g., `acme-ltd-2`) until uniqueness is achieved.

*Verifiability:* Provision 2 tenants with identical organisation names. Confirm the second tenant receives a suffix-differentiated slug. Confirm the slug appears in all tenant-scoped URLs.

---

**FR-PLAT-003:** The system shall set the initial Tenant lifecycle status to *Trial* when a new Tenant is provisioned, regardless of the subscription plan selected.

*Verifiability:* Provision a new Tenant. Query the `tenants` table and confirm `status = 'TRIAL'`. Confirm the trial expiry timestamp is set to `provisioning_date + 30 days`.

---

**FR-PLAT-004:** The system shall create a default *System Administrator* role with full permissions across all active modules when a Tenant is provisioned, and shall assign that role to the primary contact user account created during provisioning.

*Verifiability:* Log in as the primary contact user on a freshly provisioned Tenant. Confirm the user can access all core module functions without a permission error.

---

**FR-PLAT-005:** The system shall apply the Tenant's selected Localisation Profile at creation time, setting: default currency, language locale, tax configuration, statutory deduction rules, Chart of Accounts (COA) starter template, address format, invoice legal text, and mobile money gateway routing.

*Verifiability:* Provision a Tenant with the Uganda localisation profile. Confirm the COA starter contains URA-compliant account codes, the currency is UGX, and the mobile money gateway is set to MTN MoMo Uganda. Provision a second Tenant with the Kenya profile. Confirm the currency is KES and the gateway is M-Pesa Daraja.

---

**FR-PLAT-006:** The system shall automatically activate all 6 Core Modules — ACCOUNTING, INVENTORY, SALES, PROCUREMENT, USER_MGMT, and AUDIT — for every new Tenant immediately upon provisioning, without requiring any super admin action beyond submitting the provisioning form.

*Verifiability:* Provision a new Tenant. Query `tenant_modules` for that Tenant and confirm all 6 Core Module records exist with `status = 'ACTIVE'`.

---

**FR-PLAT-007:** The system shall create a default *Head Office* branch for the Tenant at provisioning time, designated as the primary branch.

*Verifiability:* Provision a new Tenant. Confirm a branch record named "Head Office" exists, is marked as the primary branch, and is visible in the branch management screen.

---

**FR-PLAT-008:** The system shall seed the Tenant's Chart of Accounts from the COA starter template associated with the Tenant's Localisation Profile at provisioning time.

*Verifiability:* Provision a Tenant with the Uganda localisation profile. Navigate to the COA screen. Confirm all accounts from the Uganda COA starter template are present with correct account codes, names, and account types.

---

**FR-PLAT-009:** The system shall send a provisioning confirmation email to the primary contact address upon successful Tenant creation. The email shall contain the Tenant's login URL (incorporating the unique slug), the primary contact's temporary password, and a link to the Longhorn ERP onboarding guide.

*Verifiability:* Provision a new Tenant. Confirm an email is received at the primary contact address within 5 minutes containing the slug-based login URL and a temporary password. Confirm the temporary password authenticates successfully on first use and the system prompts for a password change.

---

**FR-PLAT-010:** The system shall record the provisioning timestamp, provisioning super admin identity, and selected subscription plan in the Tenant record at creation time. This record shall be immutable after creation.

*Verifiability:* Provision a Tenant. Attempt to update the provisioning timestamp via the API. The system shall return HTTP 403. Confirm the Audit Log records the provisioning event with the correct super admin identity.
