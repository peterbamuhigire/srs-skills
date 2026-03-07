# Advanced API Patterns Reference

**Source:** API Design Patterns (JJ Geewax, Manning 2021)
**Standards:** OpenAPI 3.0, RFC 7231, IEEE 29148-2018

---

## Resource-Oriented Design

### Resource Hierarchy

Structure APIs around resources organized in a hierarchy of collections, resources, and sub-collections:

```
/collections/{resource_id}/sub-collections/{sub_resource_id}
```

**Example:**
```
/organizations/{org_id}/projects/{project_id}/tasks/{task_id}
```

**Rules:**
- Collections use **plural nouns** (e.g., `/users`, `/orders`, `/products`).
- Resource identifiers appear as path parameters (e.g., `/users/{user_id}`).
- Nesting depth shall not exceed 3 levels. Beyond 3 levels, promote the sub-resource to a top-level collection with a filter parameter.

### Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Collection names | Plural nouns, kebab-case | `/line-items`, `/order-statuses` |
| Resource identifiers | Opaque strings or UUIDs | `/users/a1b2c3d4` |
| Query parameters | snake_case or camelCase (pick one, stay consistent) | `?sort_by=created_at` |
| Request/response fields | snake_case (recommended by Google API guidelines) | `{ "first_name": "Ada" }` |

### Resource Relationships

Express relationships through sub-collections when a strong parent-child ownership exists. Use reference fields (foreign keys) when the relationship is a loose association.

## Standard Methods Beyond CRUD

| Method | HTTP | URL Pattern | Description |
|--------|------|-------------|-------------|
| **List** | GET | `/resources` | Return a paginated collection; support filtering, sorting, and field selection |
| **Get** | GET | `/resources/{id}` | Return a single resource by identifier |
| **Create** | POST | `/resources` | Create a new resource; return 201 + Location header |
| **Update (full)** | PUT | `/resources/{id}` | Replace the entire resource; client sends all fields |
| **Update (partial)** | PATCH | `/resources/{id}` | Update specific fields; client sends only changed fields with a field mask |
| **Delete (soft)** | DELETE | `/resources/{id}` | Mark as deleted (set `deleted_at`); resource remains queryable via `?include_deleted=true` |
| **Delete (hard)** | DELETE | `/resources/{id}` | Permanently remove the resource; return 204 No Content |

**Soft vs hard delete decision:** Use soft delete when audit trails, undo functionality, or referential integrity require retaining the record. Use hard delete for ephemeral data (sessions, temp files) or when GDPR/data-retention mandates permanent removal.

## Custom Methods

When an operation does not map cleanly to CRUD, use a custom method with the `:action` suffix:

```
POST /resources/{id}:action
```

**Examples:**
| Endpoint | Purpose |
|----------|---------|
| `POST /orders/{id}:cancel` | Cancel an order (state transition) |
| `POST /documents/{id}:translate` | Trigger translation of a document |
| `POST /users/{id}:deactivate` | Deactivate a user account |
| `POST /reports:generate` | Trigger report generation (collection-level action) |

**When to use custom methods:**
- State transitions (approve, reject, cancel, archive, publish)
- Actions with side effects that go beyond data modification (send email, trigger export)
- Operations on a collection rather than a single resource

**When NOT to use custom methods:**
- Simple CRUD (use standard methods)
- Filtering or searching (use GET with query parameters)

## Singleton Sub-Resources

A singleton sub-resource exists exactly once per parent and has no collection. It is accessed directly without an identifier:

```
GET    /users/{id}/settings        -- retrieve settings
PUT    /users/{id}/settings        -- replace settings
PATCH  /users/{id}/settings        -- partially update settings
```

**Examples:**
| Singleton | Parent | Rationale |
|-----------|--------|-----------|
| `/users/{id}/settings` | User | Each user has exactly one settings object |
| `/orders/{id}/invoice` | Order | Each order produces exactly one invoice |
| `/products/{id}/inventory` | Product | One inventory record per product per warehouse |

Singleton sub-resources do not support List or Create operations.

## Cross-References

Reference resources across collections without embedding the full object. Return a reference field containing the resource identifier:

```json
{
  "id": "order_123",
  "customer": "user_456",
  "items": ["product_789", "product_012"]
}
```

Provide a `?expand=customer` query parameter to inline the referenced resource when the client needs it, avoiding N+1 round-trips.

## Association Resources

Model many-to-many (M:M) relationships as first-class resources:

```
POST   /group-memberships          -- create membership
GET    /group-memberships?group_id=g1  -- list members of group g1
GET    /group-memberships?user_id=u1   -- list groups for user u1
DELETE /group-memberships/{id}      -- remove membership
```

**Schema:**
```json
{
  "id": "mem_001",
  "group_id": "g1",
  "user_id": "u1",
  "role": "admin",
  "joined_at": "2025-01-15T10:00:00Z"
}
```

Association resources allow adding metadata to the relationship (role, permissions, timestamps) without polluting either parent resource.

## Field Masks

Specify which fields to return (GET) or update (PATCH) to reduce payload size and avoid unintended overwrites.

### Read Field Masks (Partial Response)

```
GET /users/123?fields=id,name,email
```

The server returns only the requested fields. Nested fields use dot notation:

```
GET /orders/456?fields=id,customer.name,items.product_id,items.quantity
```

### Write Field Masks (Partial Update)

Include a `field_mask` or `update_mask` in the PATCH request to specify which fields the server should update:

```json
PATCH /users/123
{
  "update_mask": ["display_name", "email"],
  "display_name": "Ada Lovelace",
  "email": "ada@example.com"
}
```

Fields not listed in the mask remain unchanged, even if present in the request body. This prevents accidental overwrites.

### Implementation Options

| Option | Mechanism | Trade-off |
|--------|-----------|-----------|
| `fields` query parameter | Client lists desired fields in the URL | Simple; limited by URL length |
| `FieldMask` header | Client sends field list in a custom header | Cleaner URLs; less visible |
| `field_mask` body field | Included in PATCH request body | Explicit; couples mask to payload |

## Partial Responses

For large resources, reduce payload size by returning only the fields the client needs:

1. **Default fields:** Return a curated set of commonly used fields when no `fields` parameter is provided.
2. **Full fields:** Return all fields when `fields=*` is specified.
3. **Nested selection:** Support dot-notation for nested objects (e.g., `fields=id,address.city`).

Document the default field set for each resource in the API specification.

---

**Cross-references:**
- `references/long-running-operations.md` -- LRO pattern for async custom methods
- `references/batch-operations.md` -- Batch endpoints for bulk operations
- `SKILL.md` Step 5 (Endpoint Details) -- Apply these patterns when defining endpoint specifications
