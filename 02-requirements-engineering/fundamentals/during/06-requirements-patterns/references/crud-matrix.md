# CRUD Matrix Reference Guide

**Purpose:** Map data access permissions across entities and roles using CRUD matrices with gap analysis and RBAC integration.

**Standards:** IEEE 830-1998, IEEE 29148-2018, Wiegers Practice 12

---

## 1. CRUD Matrix Fundamentals

### 1.1 CRUD Operations

| Operation | Symbol | Definition                                             |
|-----------|--------|--------------------------------------------------------|
| Create    | C      | The role can create new instances of the entity        |
| Read      | R      | The role can view existing instances of the entity     |
| Update    | U      | The role can modify existing instances of the entity   |
| Delete    | D      | The role can remove instances of the entity            |

### 1.2 Matrix Structure

Rows represent entities (data objects). Columns represent roles (actors). Cell values indicate which CRUD operations the role may perform on the entity.

| Entity / Role  | Admin | Manager | Staff | Guest |
|----------------|-------|---------|-------|-------|
| Customer       | CRUD  | CRU     | R     | -     |
| Order          | CRUD  | CRUD    | CRU   | -     |
| Product        | CRUD  | CRU     | R     | R     |
| Report         | CRUD  | CR      | R     | -     |
| AuditLog       | R     | R       | -     | -     |

### 1.3 Notation Conventions

| Symbol | Meaning                                    |
|--------|--------------------------------------------|
| C      | Create only                                |
| R      | Read only                                  |
| U      | Update only                                |
| D      | Delete only                                |
| CR     | Create and Read                            |
| CRU    | Create, Read, and Update                   |
| CRUD   | Full access (Create, Read, Update, Delete) |
| -      | No access                                  |

---

## 2. Matrix Construction Process

### Step 1: List Entities

Extract all data entities from:
- The conceptual data model (`projects/<ProjectName>/<phase>/<document>/conceptual_data_model.md`)
- Feature descriptions (`projects/<ProjectName>/_context/features.md`)
- Business rules (`projects/<ProjectName>/_context/business_rules.md`)

Include every entity that stores persistent data.

### Step 2: List Roles

Extract all user roles from:
- Stakeholder documentation
- Feature descriptions (role references in user stories)
- Access control requirements

Include system roles (e.g., SystemScheduler, IntegrationService) that perform automated data operations.

### Step 3: Map Permissions

For each (Role, Entity) pair:
1. Review which features require the role to interact with the entity
2. Determine the minimum set of CRUD operations needed
3. Apply the principle of least privilege: grant only the operations the role needs

### Step 4: Validate With Business Rules

Cross-reference every cell against `business_rules.md`:
- BR-005: "Only managers shall approve refunds" -> Manager needs U on Refund; Staff does not
- BR-010: "Audit logs shall be immutable" -> No role gets U or D on AuditLog

### Step 5: Document Justification

For each non-obvious permission assignment, record the justification:

| Role    | Entity   | Permission | Justification                                |
|---------|----------|------------|----------------------------------------------|
| Staff   | Order    | CRU        | Staff create orders and update status; deletion requires manager approval (BR-020) |
| Guest   | Product  | R          | Guest users can browse the product catalog (Feature F-003) |

---

## 3. Gap Analysis

### 3.1 Entity-Level Gaps

Check every entity for the following gaps:

| Gap Type     | Condition                                  | Tag             | Risk                                   |
|--------------|--------------------------------------------|-----------------|-----------------------------------------|
| No Create    | No role has C permission for the entity    | `[NO-CREATE]`   | Entity can never be instantiated       |
| No Read      | No role has R permission for the entity    | `[NO-READ]`     | Entity data is inaccessible (orphan)   |
| No Update    | No role has U permission for the entity    | `[NO-UPDATE]`   | Entity data is immutable (intentional?)|
| No Delete    | No role has D permission for the entity    | `[NO-DELETE]`   | Entity records accumulate indefinitely |

### 3.2 Role-Level Gaps

Check every role for the following gaps:

| Gap Type        | Condition                                  | Risk                                   |
|-----------------|--------------------------------------------|-----------------------------------------|
| No Permissions  | Role has "-" for every entity              | Role has no purpose in the system       |
| Full Access     | Role has CRUD for every entity             | Overprivileged; violates least privilege|

### 3.3 Gap Resolution

For each gap found:
1. Determine if the gap is intentional (e.g., AuditLog has No Delete by design)
2. If intentional, document the rationale
3. If unintentional, recommend the missing permission and the business rule that supports it
4. Flag unresolved gaps with the appropriate tag

---

## 4. Permission Granularity

### 4.1 Field-Level Permissions

When roles need access to different fields within the same entity, extend the CRUD matrix with field-level detail:

| Entity.Field           | Manager | Staff |
|------------------------|---------|-------|
| Order.order_date       | R       | R     |
| Order.status           | RU      | R     |
| Order.total_amount     | R       | R     |
| Order.internal_notes   | CRU     | -     |

### 4.2 Record-Level Permissions (Row-Level Security)

When roles should only access records they own or are responsible for:

| Role    | Entity   | Scope                              | Permission |
|---------|----------|------------------------------------|------------|
| Staff   | Order    | Own orders only (created_by = self)| CRU        |
| Manager | Order    | Department orders                  | CRUD       |
| Admin   | Order    | All orders                         | CRUD       |

Document scope constraints alongside the CRUD matrix.

---

## 5. RBAC Integration

### 5.1 Role Hierarchy

When roles inherit permissions from parent roles, document the hierarchy:

```
Admin
  |-- Manager
  |     |-- Staff
  |-- Auditor (read-only across all entities)
Guest (minimal access, no hierarchy)
```

**Inheritance Rule:** A child role inherits all permissions of its parent unless explicitly overridden. Overrides SHALL be documented.

### 5.2 Permission Inheritance Matrix

| Entity   | Guest | Staff       | Manager           | Admin               |
|----------|-------|-------------|-------------------|----------------------|
| Customer | -     | R           | R + CU (inherited + own) | R + CU + D (inherited + own) |
| Order    | -     | CRU (own)   | CRU (own) + CRUD (dept) | CRUD (all)         |

### 5.3 Separation of Duties

Document any permissions that SHALL NOT be combined in a single role:

| Constraint                                    | Roles Affected         | Business Rule |
|-----------------------------------------------|------------------------|---------------|
| Creator shall not approve own request         | Staff, Manager         | BR-025        |
| Auditor shall not modify audited records      | Auditor                | BR-030        |

---

## 6. CRUD Matrix to Requirements Mapping

Each cell in the CRUD matrix SHALL produce one or more formal requirements:

**Template for permission grant:**
```
[CRUD-001, R3C2] The system shall allow users with the "Manager" role
to Create, Read, and Update Customer records.
```

**Template for permission denial:**
```
[CRUD-001, R3C2-D] The system shall prevent users with the "Manager" role
from Deleting Customer records.
```

**Template for scope constraint:**
```
[CRUD-001, R2C3-SCOPE] The system shall restrict users with the "Staff" role
to Read and Update only Order records where created_by equals the current user.
```

---

## 7. CRUD Matrix Checklist

- [ ] All persistent entities from the data model are listed as rows
- [ ] All user and system roles are listed as columns
- [ ] Every cell has an explicit permission assignment (including "-" for no access)
- [ ] Permissions justified against business rules or feature descriptions
- [ ] Gap analysis completed: No-Create, No-Read, No-Update, No-Delete checked
- [ ] Overprivileged roles identified and justified or remediated
- [ ] Role hierarchy and inheritance documented (if applicable)
- [ ] Separation of duties constraints documented
- [ ] Field-level and record-level permissions documented where needed
- [ ] Each cell mapped to a formal "shall" requirement

---

**Last Updated:** 2026-03-07
