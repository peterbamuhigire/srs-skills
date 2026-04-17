## 2. User Lifecycle Requirements

### 2.1 User Creation

**FR-RBAC-001:** The system shall create a new user account when an administrator submits a user creation form containing a full name, unique email address, assigned role, branch assignment(s), and an initial temporary password.

**FR-RBAC-002:** The system shall enforce email uniqueness within the tenant when a new user is created; if the submitted email already exists for that tenant, the system shall reject the request and return a validation error identifying the duplicate field.

**FR-RBAC-003:** The system shall enforce the configured password policy (see FR-RBAC-009) against the initial temporary password when a user account is created; if the policy is violated, the system shall reject the creation request and display the specific policy rule(s) that were not met.

**FR-RBAC-004:** The system shall flag a newly created user account as *pending activation* and shall send a welcome email containing a time-limited activation token to the user's registered email address when account creation completes.

### 2.2 Account Activation and Deactivation

**FR-RBAC-005:** The system shall activate a user account and mark it as *active* when the user clicks the activation link containing a valid, unexpired activation token; the token shall expire 48 hours after issuance.

**FR-RBAC-006:** The system shall deactivate a user account immediately when an administrator sets the account status to *inactive*; the system shall terminate all active sessions for that user within the time window specified in **NFR-RBAC-001** and prevent any new login attempts.

**FR-RBAC-007:** The system shall reactivate a previously deactivated user account and restore session access when an administrator sets the account status back to *active*.

### 2.3 Password Reset

**FR-RBAC-008:** The system shall initiate a self-service password reset when a user submits their registered email address on the password reset request screen; the system shall send a password reset email containing a single-use token valid for 30 minutes to that address.

**FR-RBAC-008a:** The system shall complete a self-service password reset and update the stored password hash when the user submits a new password paired with a valid, unexpired reset token; the system shall invalidate all existing sessions for the user upon completion.

**FR-RBAC-008b:** The system shall permit an administrator to trigger an admin-initiated password reset for any user within their tenant when the administrator selects the "Reset Password" action on the user record; the system shall send a reset email to the user's registered address and mark the account as requiring password change on next login.

### 2.4 Password Policy Enforcement

**FR-RBAC-009:** The system shall enforce the following password policy rules when a user sets or changes a password; each rule shall be independently configurable by a tenant administrator:

- Minimum length: configurable integer, default 8 characters.
- Complexity: configurable flags for requiring at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character.
- Maximum age: configurable integer (days); a value of 0 disables expiry.
- Password history depth: configurable integer; the system shall reject any new password that matches any of the last N stored password hashes.

**FR-RBAC-010:** The system shall prompt a user to change their password when their password age reaches the configured maximum age at next login, and shall prevent access to the application until the password change is completed.

### 2.5 Concurrent Session Control

**FR-RBAC-011:** The system shall enforce a configurable maximum number of concurrent active sessions per user (default: 1 for web, 2 for mobile) when a new login attempt occurs; if the limit is already reached, the system shall either reject the new login with an informative error or terminate the oldest session, depending on the tenant's configured policy.

### 2.6 Session Timeout

**FR-RBAC-012:** The system shall terminate an authenticated web session and redirect the user to the login screen when the session has been idle for a duration equal to the configured idle timeout (default: 30 minutes, configurable per tenant from 5 to 480 minutes).

**FR-RBAC-013:** The system shall reset the idle timeout counter when a user performs any authenticated HTTP request, ensuring only genuine inactivity triggers session expiry.

### 2.7 Forced Logout

**FR-RBAC-014:** The system shall invalidate all active web and mobile sessions for a specific user when an administrator triggers a "Force Logout" action on that user's account; all sessions shall be invalidated within the time window specified in **NFR-RBAC-001**.

**FR-RBAC-015:** The system shall display a "Session terminated by administrator" message to the affected user when they attempt any subsequent request after a forced logout event.

### 2.8 Account Lockout

**FR-RBAC-016:** The system shall lock a user account when the number of consecutive failed login attempts reaches the configured lockout threshold (default: 5 attempts, configurable per tenant from 3 to 10).

**FR-RBAC-017:** The system shall prevent any login attempt for a locked account until either: (a) the configured auto-unlock duration expires (configurable, default: 30 minutes); or (b) an administrator manually unlocks the account.

**FR-RBAC-018:** The system shall reset the failed login attempt counter to 0 when a successful login occurs for that user.

**FR-RBAC-019:** The system shall record every failed login attempt in the Audit Log, capturing the timestamp, the user identifier submitted, the IP address, and the current failed attempt count, when a login failure occurs.

**FR-RBAC-020:** The system shall send an email notification to the user and to the tenant administrator when an account is locked due to excessive failed login attempts, including the timestamp and IP address of the triggering event.
