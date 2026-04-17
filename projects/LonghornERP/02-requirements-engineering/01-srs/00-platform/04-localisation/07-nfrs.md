## 7. Non-Functional Requirements

**NFR-LOC-001:** Adding a new country localisation profile shall require no code deployment.

- *Metric:* A super admin inserts a new profile record into `localisation_profiles`, assigns it to a test tenant, and the tenant workspace applies all profile parameters — currency display, date format, tax calculation, and COA starter — without restarting the application server. Verified by executing this procedure in the staging environment and confirming correct behaviour within 60 seconds of saving the profile assignment.
- *Standard:* IEEE 830-1998 §4.3 — Correctness and Verifiability.

**NFR-LOC-002:** A localisation profile switch for a tenant shall take effect within 30 seconds of the super admin saving the change.

- *Metric:* Measured from the HTTP 200 response to the profile save request to the first request from that tenant receiving responses formatted per the new profile. Verified by automated integration test: save profile switch at T=0; assert that the tenant's next API response at T≤30s reflects the new currency symbol, date format, and tax rate. Pass threshold: ≤ 30 seconds at P95 across 10 test iterations.
- *Standard:* IEEE 830-1998 §4.3 — Verifiability.

**NFR-LOC-003:** All localisation profile parameters shall be stored in the database, not in application configuration files or code constants.

- *Metric:* Static analysis shall find zero references to currency codes, tax rates, language codes, or date formats as hard-coded string or numeric literals outside of migration seed files. Verified by running a grep-equivalent static scan against the production codebase for a set of 20 known profile parameter values (e.g., `"UGX"`, `0.18`, `"d M Y"`) and confirming zero matches outside `database/seeders/` and `database/migrations/`. Pass threshold: 0 matches.
- *Standard:* IEEE 830-1998 §4.3 — Verifiability; Principle 3 of CLAUDE.md — configuration-driven architecture.
