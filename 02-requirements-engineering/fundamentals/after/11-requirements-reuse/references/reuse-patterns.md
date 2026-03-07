# Requirements Reuse Patterns Reference

**Purpose:** Define the taxonomy of requirements reuse patterns with decision criteria for selecting the appropriate pattern.

**Standards:** IEEE 29148-2018, Laplante Ch.9

---

## Reuse Pattern Taxonomy

Four reuse patterns are defined, ranging from lowest to highest adaptation effort.

---

## Pattern 1: Verbatim Reuse

### Definition

Copy the requirement exactly as written from the library into the target project. No modifications are permitted. The requirement text, acceptance criteria, and constraints are used as-is.

### When to Use

- Regulatory or compliance requirements mandated by law (GDPR, HIPAA, PCI DSS, SOX).
- Industry standards that apply uniformly (encryption algorithms, protocol versions).
- Organizational policies that apply to all products (password policies, audit logging).

### Advantages

- Zero adaptation effort.
- Guaranteed compliance consistency across products.
- Pre-validated acceptance criteria can be reused directly.

### Risks

- Assumption that the requirement applies without context modification. Always verify applicability.
- Regulatory updates may invalidate verbatim copies. Track regulation version in the library entry.

### Example

```markdown
[LIB-SEC-001] The system shall encrypt all data at rest using AES-256
encryption as specified by NIST SP 800-175B.

Type: Verbatim
Domain: Security
Regulation: HIPAA 164.312(a)(2)(iv), PCI DSS Requirement 3.4
Applicability: All systems storing sensitive data
```

### Decision Criteria

| Criterion | Threshold |
|-----------|-----------|
| Requirement is regulation-mandated | Yes -> Verbatim |
| Requirement text is organization-wide policy | Yes -> Verbatim |
| Requirement references specific standard version | Yes -> Verbatim |
| Any project-specific values need insertion | No -> Verbatim; Yes -> Parameterized |

---

## Pattern 2: Parameterized Reuse

### Definition

Use a requirement template with clearly defined variables (parameters) that are filled in with project-specific values. The structure and intent remain constant; only the variable values change.

### When to Use

- Cross-cutting concerns where behavior is standard but thresholds vary (session timeout, retry counts, pagination sizes).
- Domain patterns where the workflow is identical but entities differ (CRUD operations, search functionality).
- Performance requirements where targets vary by system context.

### Template Syntax

Parameters are enclosed in curly braces with descriptive names:

```
{PARAMETER_NAME} -- Description (type, default, constraints)
```

### Advantages

- Low adaptation effort (fill in variables).
- Consistent structure ensures IEEE 830 quality properties are preserved.
- Parameters make variation explicit and auditable.

### Risks

- Over-parameterization (more than 5 parameters) makes templates harder to use than writing from scratch.
- Default values may be blindly accepted without project-specific evaluation.

### Example

```markdown
[LIB-AUTH-002] The system shall lock the user account after
{MAX_ATTEMPTS} consecutive failed login attempts for {LOCKOUT_DURATION}.
After the lockout period, the system shall {UNLOCK_ACTION}.

Type: Parameterized
Domain: Authentication
Parameters:
  - MAX_ATTEMPTS: integer, default=5, range=[3,10]
  - LOCKOUT_DURATION: duration, default=15 minutes, range=[5 min, 24 hours]
  - UNLOCK_ACTION: enum [auto-unlock, require admin unlock, require MFA],
    default=auto-unlock
```

### Instantiation Example

```markdown
[REQ-AUTH-002] The system shall lock the user account after 3 consecutive
failed login attempts for 30 minutes. After the lockout period, the system
shall require MFA verification to unlock.

Derived from: LIB-AUTH-002
Parameters applied: MAX_ATTEMPTS=3, LOCKOUT_DURATION=30 minutes,
UNLOCK_ACTION=require MFA
```

### Decision Criteria

| Criterion | Threshold |
|-----------|-----------|
| Requirement structure is reusable but values differ | Yes -> Parameterized |
| Number of variable values | 1-5 -> Parameterized; 6+ -> consider Pattern |
| Parameter values have clear types and constraints | Yes -> Parameterized |
| Template can be instantiated without domain expertise | Yes -> Parameterized |

---

## Pattern 3: Compositional Reuse

### Definition

Combine multiple library requirements (building blocks) to construct a composite requirement or feature. Each building block is a self-contained requirement that can be assembled with others.

### When to Use

- Complex features that decompose into standard sub-requirements (e.g., a checkout flow combines cart management, payment processing, order confirmation, and notification).
- Feature sets where the combination varies by product but the individual components are standard.
- When a product includes a subset of a larger feature library.

### Advantages

- Maximizes reuse of validated building blocks.
- Enables product differentiation through selective composition.
- Each block retains its own trace links and test cases.

### Risks

- Integration between blocks may introduce emergent requirements not captured in individual blocks.
- Dependency ordering between blocks must be documented.

### Example

```markdown
## Feature: User Checkout (Composed)

Building Blocks:
1. [LIB-ECOM-001] Shopping cart management
2. [LIB-ECOM-002] Address validation
3. [LIB-ECOM-003] Payment processing ({PAYMENT_METHODS})
4. [LIB-ECOM-004] Order confirmation notification
5. [LIB-ECOM-005] Receipt generation

Composition Rules:
- Blocks 1-5 execute in sequence.
- Block 3 requires Block 2 to complete successfully.
- Block 4 triggers asynchronously after Block 3 succeeds.
- Block 5 is optional (include only if digital receipts are in scope).

Integration Requirements (not in library):
- [REQ-ECOM-INT-001] The system shall maintain transaction atomicity
  across blocks 1-3 (rollback cart reservation if payment fails).
```

### Decision Criteria

| Criterion | Threshold |
|-----------|-----------|
| Feature decomposes into standard sub-features | Yes -> Compositional |
| Sub-features exist independently in the library | Yes -> Compositional |
| Product variants differ by which sub-features are included | Yes -> Compositional |
| Integration between sub-features requires new requirements | Document as integration requirements |

---

## Pattern 4: Generative Reuse

### Definition

Derive requirements from a higher-level model (feature model, domain model, or decision model) rather than from individual templates. The model captures variation points and binding rules; requirements are generated by traversing the model and resolving variation points.

### When to Use

- Software product line engineering with multiple products sharing a common platform.
- Systems where feature combinations are complex and numerous (automotive, IoT, enterprise platforms).
- When the number of product variants makes individual template management impractical.

### Advantages

- Scales to large product lines with many variants.
- Ensures consistency across all derived products.
- Model-level validation catches conflicts before requirement generation.

### Risks

- Requires upfront investment in model creation and tooling.
- Model complexity can obscure individual requirement intent.
- Not justified for single-product organizations.

### Example

```markdown
## Feature Model: Notification System

Root: Notification
  ├── Channel (mandatory, select 1+)
  │   ├── Email
  │   ├── SMS
  │   ├── Push Notification
  │   └── In-App
  ├── Trigger (mandatory, select 1+)
  │   ├── Event-Driven
  │   └── Scheduled
  ├── Personalization (optional)
  │   ├── Template Engine
  │   └── User Preferences
  └── Delivery Tracking (optional)
      ├── Read Receipts
      └── Retry Logic

## Generated Requirements for Product A (Email + Push, Event-Driven)

[REQ-NOTIFY-001] The system shall deliver email notifications to the
designated recipient within 5 minutes of the triggering event.
  Generated from: Channel.Email + Trigger.Event-Driven

[REQ-NOTIFY-002] The system shall deliver push notifications to the
user's registered mobile device within 30 seconds of the triggering event.
  Generated from: Channel.Push + Trigger.Event-Driven
```

### Decision Criteria

| Criterion | Threshold |
|-----------|-----------|
| Organization manages 3+ related products | Yes -> consider Generative |
| Feature combinations exceed 20 variants | Yes -> Generative preferred |
| Model creation effort is justified by reuse volume | Yes -> Generative |
| Single product with no product line plans | No -> use Parameterized or Compositional |

---

## Pattern Selection Decision Tree

```
Is the requirement regulation-mandated or policy-fixed?
  YES -> Verbatim
  NO  -> Does the requirement have 1-5 variable values?
           YES -> Parameterized
           NO  -> Does the feature decompose into standard sub-features?
                    YES -> Compositional
                    NO  -> Is there a product line with 3+ variants?
                             YES -> Generative
                             NO  -> Write a new requirement (no reuse)
```

---

## Reuse Quality Rules

1. **Trace preservation:** Reused requirements shall retain their library ID as a "derived-from" trace link.
2. **Validation obligation:** Every reused requirement shall be validated against the target project's context, even for verbatim reuse.
3. **Parameter bounds:** All parameters shall have defined types, defaults, and valid ranges.
4. **Version tracking:** Library entries shall carry version numbers. When a library entry is updated, all projects using it shall be notified.
5. **No silent modification:** If a reused requirement is modified after instantiation, the modification shall be recorded and the library entry reviewed for potential update.

---

## References

- **IEEE Std 29148-2018:** Requirements reuse provisions.
- **Laplante Ch.9:** Software product line requirements engineering.
- **Wiegers Practice 20:** Requirements process institutionalization and reuse.
- **Pohl, Bockle, van der Linden (2005):** Software Product Line Engineering.

---
**Last Updated:** 2026-03-07
