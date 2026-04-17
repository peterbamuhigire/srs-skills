## 3. Roles and Permissions Requirements

### 3.1 Role Creation

**FR-RBAC-030:** The system shall create a new role when an administrator submits a role creation form containing a unique role name, a description, and an initial permission set drawn from the function × action matrix; the role shall be immediately available for assignment to users within that tenant.

**FR-RBAC-031:** The system shall enforce role name uniqueness within the tenant when a role is created or renamed; if the submitted name already exists, the system shall reject the request and return a validation error identifying the duplicate name.

### 3.2 Role Cloning

**FR-RBAC-032:** The system shall create a new role as an exact copy of an existing role's permission set when an administrator triggers the clone action on a source role and supplies a unique name for the new role; the cloned role shall be editable independently of the source role.

### 3.3 Role Assignment

**FR-RBAC-033:** The system shall assign a role to a user and apply the corresponding permission set immediately when an administrator selects a role from the available roles list and confirms the assignment on the user record.

**FR-RBAC-034:** The system shall support assignment of exactly 1 active role per user at any time; reassigning a role shall replace the previous role and invalidate the user's cached permission set within the time window specified in **NFR-RBAC-005**.

### 3.4 Function × Action Permission Matrix

**FR-RBAC-035:** The system shall enforce a permission matrix in which every system function is mapped to the following discrete actions: view, create, edit, approve, and delete; a role may grant any combination of these actions per function.

**FR-RBAC-036:** The system shall deny access and return an HTTP 403 response with a user-facing "Access Denied" message when an authenticated user requests a function or action for which their current role does not hold a granted permission.

**FR-RBAC-037:** The system shall present only the navigation items, buttons, and form actions that correspond to permissions granted to the current user's role when rendering any page, hiding non-permitted UI elements rather than disabling them.

### 3.5 Branch Restriction

**FR-RBAC-038:** The system shall restrict all data queries, reports, and transaction creation for a user to the branches explicitly assigned to that user when the user performs any data access operation; the system shall not return records belonging to branches outside the user's assignment.

**FR-RBAC-039:** The system shall allow an administrator to assign one or more branches to a user or reassign branches at any time; the updated branch restriction shall take effect within the time window specified in **NFR-RBAC-005** for subsequent requests.

**FR-RBAC-040:** The system shall exempt users whose role carries a "All Branches" flag from the per-user branch restriction, granting them access to data across all branches of the tenant.

### 3.6 Approval Limits

**FR-RBAC-041:** The system shall enforce a configurable per-user approval limit (in UGX) for each transaction type (e.g., purchase order approval, payment voucher approval, credit note approval) when a user attempts to approve a transaction; if the transaction amount exceeds the user's configured limit for that type, the system shall reject the approval and display the applicable limit.

**FR-RBAC-042:** The system shall allow a tenant administrator to set, update, or remove approval limits for individual users per transaction type; a null or absent limit shall be interpreted as no approval authority for that transaction type.

**FR-RBAC-043:** The system shall record every approval limit configuration change in the Audit Log, capturing the old limit value, the new limit value, the transaction type, the user whose limit was changed, the administrator who made the change, and the timestamp.

### 3.7 Module Access Gating

**FR-RBAC-044:** The system shall prevent a user from accessing any function belonging to a module that the tenant has not activated in their subscription when the user attempts to navigate to or call an API endpoint for that function; the system shall return an informative message indicating that the module is not active on the tenant's subscription.

**FR-RBAC-045:** The system shall re-evaluate module access gates in real time when a tenant's activated module list changes; affected users' sessions shall reflect the updated module access within the time window specified in **NFR-RBAC-005**.

### 3.8 Super Admin Impersonation

**FR-RBAC-046:** The system shall allow a super administrator to initiate an impersonation session for any tenant user when the super admin selects the "Impersonate" action on the target user record in the Super Admin Panel; the impersonation session shall open in the tenant workspace with the target user's effective permissions.

**FR-RBAC-047:** The system shall record every action taken during an impersonation session in the Audit Log with `impersonation_flag = TRUE`, the `impersonator_id` of the super admin, and the `impersonated_user_id`, in addition to all standard audit fields, when any state-changing action is performed.

**FR-RBAC-048:** The system shall display a persistent, visually distinct banner within the impersonation session informing the operator which user is being impersonated and providing a one-click "End Impersonation" control.

**FR-RBAC-049:** The system shall automatically terminate an impersonation session when the session duration reaches 30 minutes from the time impersonation was initiated; the operator shall be redirected to the Super Admin Panel and a session expiry notification shall be displayed.

**FR-RBAC-050:** The system shall prevent a super admin acting under impersonation from performing the following privileged operations on the impersonated tenant: deleting tenant data, modifying subscription plan, accessing other tenant data, or escalating the impersonated user's own permissions.
