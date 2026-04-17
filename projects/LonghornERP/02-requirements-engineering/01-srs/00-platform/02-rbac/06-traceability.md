## 6. Requirements Traceability Matrix

The following table maps every functional requirement in this SRS to the originating business goal in the Product Requirements Document (PRD) and to the designated test case identifier.

| Requirement ID | Requirement Summary | PRD Business Goal | Test Case ID |
|---|---|---|---|
| **FR-RBAC-001** | Create user with name, email, role, branch, initial password | BG-PLT-01: Secure multi-tenant user administration | TC-RBAC-001 |
| **FR-RBAC-002** | Enforce email uniqueness within tenant on user creation | BG-PLT-01: Secure multi-tenant user administration | TC-RBAC-002 |
| **FR-RBAC-003** | Enforce password policy on initial password at creation | BG-PLT-02: NIST SP 800-63B-compliant password governance | TC-RBAC-003 |
| **FR-RBAC-004** | Flag new account as pending and send activation email | BG-PLT-01: Secure multi-tenant user administration | TC-RBAC-004 |
| **FR-RBAC-005** | Activate account via time-limited token | BG-PLT-01: Secure multi-tenant user administration | TC-RBAC-005 |
| **FR-RBAC-006** | Deactivate account and terminate all sessions immediately | BG-PLT-03: Zero-latency session revocation | TC-RBAC-006 |
| **FR-RBAC-007** | Reactivate deactivated account | BG-PLT-01: Secure multi-tenant user administration | TC-RBAC-007 |
| **FR-RBAC-008** | Self-service password reset via email token | BG-PLT-02: NIST SP 800-63B-compliant password governance | TC-RBAC-008 |
| **FR-RBAC-008a** | Complete self-service reset and invalidate existing sessions | BG-PLT-02: NIST SP 800-63B-compliant password governance | TC-RBAC-008A |
| **FR-RBAC-008b** | Admin-initiated password reset | BG-PLT-01: Secure multi-tenant user administration | TC-RBAC-008B |
| **FR-RBAC-009** | Enforce configurable password policy (length, complexity, expiry, history) | BG-PLT-02: NIST SP 800-63B-compliant password governance | TC-RBAC-009 |
| **FR-RBAC-010** | Force password change on expiry at next login | BG-PLT-02: NIST SP 800-63B-compliant password governance | TC-RBAC-010 |
| **FR-RBAC-011** | Enforce configurable max concurrent sessions | BG-PLT-03: Zero-latency session revocation | TC-RBAC-011 |
| **FR-RBAC-012** | Terminate idle session after configurable timeout | BG-PLT-03: Zero-latency session revocation | TC-RBAC-012 |
| **FR-RBAC-013** | Reset idle timeout counter on each authenticated request | BG-PLT-03: Zero-latency session revocation | TC-RBAC-013 |
| **FR-RBAC-014** | Admin-triggered forced logout invalidates all sessions | BG-PLT-03: Zero-latency session revocation | TC-RBAC-014 |
| **FR-RBAC-015** | Display "Session terminated by administrator" on post-logout request | BG-PLT-03: Zero-latency session revocation | TC-RBAC-015 |
| **FR-RBAC-016** | Lock account after N consecutive failed login attempts | BG-PLT-04: Brute-force attack prevention | TC-RBAC-016 |
| **FR-RBAC-017** | Prevent login to locked account until auto-unlock or admin unlock | BG-PLT-04: Brute-force attack prevention | TC-RBAC-017 |
| **FR-RBAC-018** | Reset failed attempt counter on successful login | BG-PLT-04: Brute-force attack prevention | TC-RBAC-018 |
| **FR-RBAC-019** | Log every failed login attempt in Audit Log | BG-PLT-05: Complete and immutable audit trail | TC-RBAC-019 |
| **FR-RBAC-020** | Email notification on account lockout to user and admin | BG-PLT-04: Brute-force attack prevention | TC-RBAC-020 |
| **FR-RBAC-030** | Create role with name, description, and initial permission set | BG-PLT-06: Granular RBAC with least-privilege enforcement | TC-RBAC-030 |
| **FR-RBAC-031** | Enforce role name uniqueness within tenant | BG-PLT-06: Granular RBAC with least-privilege enforcement | TC-RBAC-031 |
| **FR-RBAC-032** | Clone existing role with independent permission copy | BG-PLT-06: Granular RBAC with least-privilege enforcement | TC-RBAC-032 |
| **FR-RBAC-033** | Assign role to user and apply permissions immediately | BG-PLT-06: Granular RBAC with least-privilege enforcement | TC-RBAC-033 |
| **FR-RBAC-034** | Support exactly 1 active role per user; invalidate cache on reassignment | BG-PLT-06: Granular RBAC with least-privilege enforcement | TC-RBAC-034 |
| **FR-RBAC-035** | Enforce function × action permission matrix (view/create/edit/approve/delete) | BG-PLT-06: Granular RBAC with least-privilege enforcement | TC-RBAC-035 |
| **FR-RBAC-036** | Return HTTP 403 and "Access Denied" for unauthorised function/action | BG-PLT-06: Granular RBAC with least-privilege enforcement | TC-RBAC-036 |
| **FR-RBAC-037** | Hide non-permitted UI elements; do not merely disable | BG-PLT-06: Granular RBAC with least-privilege enforcement | TC-RBAC-037 |
| **FR-RBAC-038** | Restrict data access to user's assigned branches | BG-PLT-07: Branch-level data segmentation | TC-RBAC-038 |
| **FR-RBAC-039** | Allow admin to update branch assignments; apply within cache window | BG-PLT-07: Branch-level data segmentation | TC-RBAC-039 |
| **FR-RBAC-040** | Exempt "All Branches" flag holders from branch restriction | BG-PLT-07: Branch-level data segmentation | TC-RBAC-040 |
| **FR-RBAC-041** | Enforce per-user per-transaction-type approval limits (UGX) | BG-PLT-08: Configurable financial approval authority | TC-RBAC-041 |
| **FR-RBAC-042** | Allow admin to set, update, or remove approval limits | BG-PLT-08: Configurable financial approval authority | TC-RBAC-042 |
| **FR-RBAC-043** | Audit log entry for every approval limit change | BG-PLT-05: Complete and immutable audit trail | TC-RBAC-043 |
| **FR-RBAC-044** | Deny access to functions in non-activated modules | BG-PLT-09: Module access gating per subscription | TC-RBAC-044 |
| **FR-RBAC-045** | Re-evaluate module gates in real time on subscription change | BG-PLT-09: Module access gating per subscription | TC-RBAC-045 |
| **FR-RBAC-046** | Super admin initiates impersonation session for any tenant user | BG-PLT-10: Audited super admin impersonation for support | TC-RBAC-046 |
| **FR-RBAC-047** | Log all impersonation session actions with impersonation flag | BG-PLT-05: Complete and immutable audit trail | TC-RBAC-047 |
| **FR-RBAC-048** | Display persistent impersonation banner with End Impersonation control | BG-PLT-10: Audited super admin impersonation for support | TC-RBAC-048 |
| **FR-RBAC-049** | Auto-terminate impersonation session after 30 minutes | BG-PLT-10: Audited super admin impersonation for support | TC-RBAC-049 |
| **FR-RBAC-050** | Restrict privileged operations within impersonation session | BG-PLT-10: Audited super admin impersonation for support | TC-RBAC-050 |
| **FR-RBAC-060** | Generate TOTP shared secret and QR code on 2FA enrollment initiation | BG-PLT-11: MFA enforcement per NIST SP 800-63B AAL2 | TC-RBAC-060 |
| **FR-RBAC-061** | Complete 2FA enrollment on valid TOTP code submission | BG-PLT-11: MFA enforcement per NIST SP 800-63B AAL2 | TC-RBAC-061 |
| **FR-RBAC-062** | Generate 10 single-use backup codes on 2FA enrollment | BG-PLT-11: MFA enforcement per NIST SP 800-63B AAL2 | TC-RBAC-062 |
| **FR-RBAC-063** | Mark backup code as used; block re-use | BG-PLT-11: MFA enforcement per NIST SP 800-63B AAL2 | TC-RBAC-063 |
| **FR-RBAC-064** | Require TOTP or backup code on every login when 2FA is enabled | BG-PLT-11: MFA enforcement per NIST SP 800-63B AAL2 | TC-RBAC-064 |
| **FR-RBAC-065** | Admin can mandate 2FA enrollment for specific roles | BG-PLT-11: MFA enforcement per NIST SP 800-63B AAL2 | TC-RBAC-065 |
| **FR-RBAC-066** | Admin or user can disable 2FA per tenant policy | BG-PLT-11: MFA enforcement per NIST SP 800-63B AAL2 | TC-RBAC-066 |
| **FR-RBAC-067** | Receive biometric authentication events from Zkteco devices | BG-PLT-12: Biometric time-attendance and optional session auth | TC-RBAC-067 |
| **FR-RBAC-068** | Record attendance and optionally create session on valid Zkteco event | BG-PLT-12: Biometric time-attendance and optional session auth | TC-RBAC-068 |
| **FR-RBAC-069** | Reject and audit-log invalid or unregistered Zkteco events | BG-PLT-12: Biometric time-attendance and optional session auth | TC-RBAC-069 |
| **FR-RBAC-070** | Admin configures per-user biometric session creation policy | BG-PLT-12: Biometric time-attendance and optional session auth | TC-RBAC-070 |
| **FR-RBAC-071** | Authenticate USSD session by caller mobile number match | BG-PLT-13: USSD access for low-bandwidth warehouse workers | TC-RBAC-071 |
| **FR-RBAC-072** | USSD stock lookup by item code returns name and quantity | BG-PLT-13: USSD access for low-bandwidth warehouse workers | TC-RBAC-072 |
| **FR-RBAC-073** | USSD GRN confirmation updates GRN status and audit log | BG-PLT-13: USSD access for low-bandwidth warehouse workers | TC-RBAC-073 |
| **FR-RBAC-074** | Terminate USSD session for unregistered or unauthorised caller | BG-PLT-13: USSD access for low-bandwidth warehouse workers | TC-RBAC-074 |
| **FR-RBAC-075** | Terminate USSD session on timeout or gateway close; discard partial state | BG-PLT-13: USSD access for low-bandwidth warehouse workers | TC-RBAC-075 |
