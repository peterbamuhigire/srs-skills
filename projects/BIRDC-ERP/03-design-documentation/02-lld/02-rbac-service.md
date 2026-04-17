# 2. RBACService

**Namespace:** `App\Services\Auth\RBACService`
**Dependencies:** `PermissionRepository`, `UserRepository`, `AuditLogService`
**Test coverage required:** 100% (security-critical)

## 2.1 Method Signatures

```php
final class RBACService
{
    /**
     * Check whether a user has permission to perform an action on a resource.
     *
     * This is the single authorisation gate called by every controller before
     * delegating to a service. It evaluates all 8 permission layers in sequence.
     *
     * @param int    $userId    Authenticated user's ID
     * @param string $resource  Resource identifier (e.g., 'sales.invoices', 'gl.journals')
     * @param string $action    Action identifier (e.g., 'create', 'approve', 'void', 'export')
     *
     * @return bool  true if all applicable layers grant access; false otherwise.
     *
     * Business rules:
     *   - Evaluates layers L1–L8 in order; returns false on first failure.
     *   - L7 (Conditional Rules) includes BR-003 segregation of duties checks
     *     for resources that have a creator vs. approver constraint.
     *   - L8 (Object Ownership) is evaluated only when $resource carries a
     *     record-level ownership constraint (e.g., agent can only view own invoices).
     *   - Result is cached per request (not across requests) to avoid repeated DB calls.
     *   - Access denial is logged to AuditLogService at DEBUG level.
     */
    public function hasPermission(int $userId, string $resource, string $action): bool;

    /**
     * Retrieve the full permission matrix for a user.
     *
     * Used by the frontend to conditionally render UI elements (L4)
     * and by the API middleware to build the permission cache for a session.
     *
     * @param int $userId
     *
     * @return PermissionMatrix
     *   {
     *     role: string,                    // primary role name
     *     pages: string[],                 // allowed URL paths
     *     endpoints: string[],             // allowed "METHOD /path" strings
     *     elements: string[],              // allowed UI element IDs
     *     time_restrictions: array|null,   // {days: int[], start: string, end: string} or null
     *     location_restrictions: array|null, // {allowed_ips: string[]} or null
     *     conditional_rules: array         // [{resource, action, rule_type, rule_config}]
     *   }
     *
     * @throws UserNotFoundException If $userId does not exist.
     */
    public function getUserPermissions(int $userId): PermissionMatrix;
}
```

## 2.2 8-Layer Permission Evaluation Logic

```
RBACService::hasPermission($userId, $resource, $action):

  L1 — Role Check
    Fetch user's role(s) from tbl_user_roles.
    If no role grants access to $resource → return false.

  L2 — Page Check
    Resolve the current HTTP route to a page identifier.
    If user's role does not include this page in tbl_rbac_page_permissions → return false.

  L3 — API Endpoint Check
    Resolve "METHOD /path" to an endpoint identifier.
    If user's role does not include this endpoint in tbl_rbac_endpoint_permissions → return false.

  L4 — UI Element Check
    If $action maps to a specific UI element ID:
      If user's role does not include this element in tbl_rbac_element_permissions → return false.
    (Note: L4 is enforced server-side; client-side rendering is a convenience, not a security boundary.)

  L5 — Location Check
    If user's role has location restrictions in tbl_rbac_location_rules:
      If request IP is not in the allowed_ips list → return false.

  L6 — Time Check
    If user's role has time restrictions in tbl_rbac_time_rules:
      If current server time (EAT, UTC+3) is outside allowed_days / start_time / end_time → return false.

  L7 — Conditional Rules Check
    Fetch all conditional rules for ($resource, $action) from tbl_rbac_conditional_rules.
    For each rule:
      Rule type SEGREGATION_OF_DUTIES:
        Load the target record; check that record.created_by ≠ $userId.
        If creator = current user → return false (BR-003).
      Rule type BUDGET_OVERRIDE_REQUIRED:
        Check if action would exceed a budget vote; if so, require Director-level role.
      (Other rule types evaluated per configuration.)

  L8 — Object Ownership Check
    If resource has an ownership constraint (e.g., 'agent.invoices' requires agent_id match):
      Load the record; check record.owner_id = $userId (or user's agent_id).
      If mismatch → return false.

  All layers passed → return true.
```

## 2.3 RBAC Permission Matrix — Roles × Modules × Actions

The table below defines the default permission assignments. All permissions are configurable by the IT Administrator without code changes (DC-002).

| Role | F-001 Sales | F-002 POS | F-003 Inventory | F-004 Agents | F-005 GL | F-006 AR | F-007 AP | F-008 Budget | F-009 Procurement | F-010 Farmers | F-011 Manufacturing | F-012 QC | F-013 HR | F-014 Payroll | F-016 Admin | F-017 System |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DIRECTOR | Read | Read | Read | Read | Read | Read | Read | Read/Approve | Read | Read | Read | Read | Read | Read/Approve | Read | Read |
| FINANCE_DIRECTOR | CRUD/Approve | Read | Read | Read/Verify | CRUD/Post/Approve | CRUD | CRUD/Approve | CRUD | Read | Read | Read | Read | Read | CRUD/Approve/Lock | Read | Read |
| SALES_MANAGER | CRUD | Read | Read | CRUD/Approve | Read | Read | — | Read | — | — | — | — | — | — | — | — |
| ACCOUNTS_ASSISTANT | CRUD | Read | Read | Read | Create/Draft | CRUD | CRUD | Read | — | — | — | — | — | — | — | — |
| PROCUREMENT_MANAGER | Read | — | Read | — | Read | — | Read | Read | CRUD | CRUD | — | — | — | — | Read | — |
| STORE_MANAGER | Read | Read | CRUD/Approve | Read/Approve | Read | — | Read | — | Read | — | Read | — | — | — | — | — |
| PRODUCTION_MANAGER | — | — | Read | — | Read | — | — | — | Read | — | CRUD | Read | — | — | — | — |
| QC_MANAGER | — | — | Read | — | — | — | — | — | — | — | Read | CRUD/Release | — | — | — | — |
| HR_MANAGER | — | — | — | — | Read | — | — | — | — | Read | — | — | CRUD | Read | — | — |
| PAYROLL_OFFICER | — | — | — | — | Read | — | — | — | — | — | — | — | Read | CRUD | — | — |
| CASHIER | — | CRUD | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| SALES_AGENT | — | Own POS only | — | Own data only | — | — | — | — | — | — | — | — | — | — | — | — |
| IT_ADMINISTRATOR | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Full |
| RESEARCHER | — | — | — | — | Read | — | — | — | — | Read | — | Read | — | — | — | — |
| ADMIN_OFFICER | — | — | — | — | — | — | — | — | Read | — | — | — | — | — | CRUD | — |

Legend: CRUD = Create/Read/Update/Delete; — = no access; Own = scoped to user's own records only.
