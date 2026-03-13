# Healthcare: Default Non-Functional Requirements

These requirements are auto-injected into new healthcare project scaffolds.
All blocks are tagged `[DOMAIN-DEFAULT: healthcare]` for consultant review.

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-001: PHI Audit Trail
The system shall maintain a complete, tamper-proof audit log of all create,
read, update, and delete operations on Protected Health Information (PHI) in
compliance with HIPAA Security Rule 45 CFR §164.312(b).

**Verifiability:** Execute a read operation on a patient record; verify that an
immutable log entry is created containing: user_id, timestamp, action, resource_id,
and outcome. Attempt to modify the log entry; the system shall reject the modification.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-002: Data Encryption at Rest
The system shall encrypt all PHI stored in the database using AES-256-GCM.
Unencrypted PHI shall not exist on any persistent storage medium.

**Verifiability:** Inspect raw database storage; PHI fields must be unreadable
without the encryption key. Key management must follow NIST SP 800-57.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-003: Data Encryption in Transit
All transmission of PHI shall use TLS 1.2 or higher. TLS 1.0 and 1.1 shall
be disabled on all endpoints.

**Verifiability:** Run `nmap --script ssl-enum-ciphers` against all endpoints;
verify TLS 1.0/1.1 returns no supported ciphers.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-004: Session Timeout
The system shall automatically terminate inactive clinical user sessions after
15 minutes of inactivity, requiring re-authentication to resume.

**Verifiability:** Authenticate as a clinical user; remain idle for 15 minutes;
attempt any action — the system shall redirect to the login screen.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-005: Multi-Factor Authentication
The system shall require Multi-Factor Authentication (MFA) for all users with
access to PHI, in compliance with HIPAA Security Rule 45 CFR §164.312(d).

**Verifiability:** Attempt login with valid credentials only; the system shall
not grant access without a valid second factor.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-006: Availability for Clinical Systems
The system shall maintain 99.9% uptime availability ($\leq 8.76$ hours downtime
per year) for all clinical-facing modules, measured monthly.

**Verifiability:** Monitor uptime over 30 days; calculated as:
$Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-007: Data Retention
The system shall retain patient records and associated audit logs for a minimum
of 6 years from the date of creation or last access, in compliance with HIPAA
45 CFR §164.530(j).

**Verifiability:** Attempt to delete a PHI record less than 6 years old; the
system shall reject the deletion and return an appropriate error.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-008: Breach Notification Capability
The system shall provide tooling to identify and report all PHI records affected
by a security breach within 60 days, in compliance with HIPAA Breach Notification
Rule 45 CFR §164.412.

**Verifiability:** Given a simulated breach event (compromised user account),
the system shall produce a report of all PHI accessed by that account within
the breach window, within 4 hours of query execution.
<!-- [END DOMAIN-DEFAULT] -->
