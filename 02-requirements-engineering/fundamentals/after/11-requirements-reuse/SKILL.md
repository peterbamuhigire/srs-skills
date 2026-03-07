---
name: requirements-reuse
description: Identify reusable requirements patterns and build a requirements library for product line engineering per IEEE 29148 and Laplante Ch.9. OPTIONAL skill.
---

# Requirements Reuse Skill Guidance

## Overview

This skill is OPTIONAL and intended for organizations building multiple related products or maintaining a portfolio of applications. It scans existing requirements artifacts, identifies candidates for reuse, classifies them by reuse type, and generates a requirements library catalog. The library accelerates future projects by providing vetted, parameterized requirements templates.

## When to Use This Skill

- After requirements have been baselined and validated for at least one project.
- When an organization is starting a second or subsequent product that shares domain characteristics.
- During product line engineering to establish commonality and variability models.
- When regulatory requirements (GDPR, HIPAA, SOX) recur across multiple systems.

## Quick Reference

- **Inputs:** All artifacts in `../output/`, `../project_context/vision.md`
- **Outputs:** `../output/requirements_library.md`
- **Tone:** Cataloging, systematic, pattern-oriented

## Input Files

| File | Source | Required? |
|------|--------|-----------|
| All `*.md` artifacts | `../output/` | Yes |
| `vision.md` | `../project_context/` | Yes |
| `requirements_baseline.md` | `../output/` | Recommended |
| `traceability_matrix.md` | `../output/` | Recommended |

## Output Files

| File | Contents | Destination |
|------|----------|-------------|
| `requirements_library.md` | Reusable requirements catalog with classification and adaptation guidelines | `../output/` |

## Core Instructions

### Step 1: Read All Artifacts

Read every file in `../output/` and `../project_context/vision.md`. Log each file path read. Build a consolidated list of all requirements with their full definitions, acceptance criteria, and trace links.

### Step 2: Identify Reuse Candidates

Scan all requirements for patterns that indicate reuse potential. Candidates fall into three categories:

#### Cross-Cutting Concerns

Requirements that appear in virtually every software system:

| Domain | Examples |
|--------|----------|
| Authentication | User registration, login, password reset, session management, MFA |
| Authorization | Role-based access control, permission matrices, privilege escalation prevention |
| Logging | Audit trails, event logging, log retention policies, log format standards |
| Error Handling | Error codes, user-facing error messages, retry logic, graceful degradation |
| Data Validation | Input sanitization, format validation, boundary checks, encoding rules |
| Notification | Email dispatch, SMS alerts, in-app notifications, notification preferences |

#### Domain Patterns

Requirements specific to a business domain but recurring across products in that domain:

| Domain | Examples |
|--------|----------|
| E-Commerce | Shopping cart, checkout flow, payment processing, order tracking, returns |
| Healthcare | Patient registration, appointment scheduling, prescription management, HIPAA consent |
| Finance | Account management, transaction processing, regulatory reporting, fraud detection |
| Education | Course enrollment, grade management, attendance tracking, learning management |

#### Regulatory and Compliance

Requirements mandated by law or regulation that apply to any system within scope:

| Regulation | Requirements |
|------------|-------------|
| GDPR | Consent management, right to erasure, data portability, privacy impact assessment |
| HIPAA | Business Associate Agreement, PHI encryption, access logging, breach notification |
| SOX | Financial controls, audit trails, segregation of duties, data retention |
| PCI DSS | Cardholder data protection, network segmentation, vulnerability management |
| WCAG 2.1 | Perceivable, operable, understandable, robust accessibility requirements |

### Step 3: Classify Reuse Type

For each candidate requirement, classify the reuse type:

| Reuse Type | Definition | When to Use |
|------------|-----------|-------------|
| Verbatim | Copy the requirement as-is into the new project | Regulatory mandates, universal standards |
| Parameterized | Use a template with variables to fill in | Domain patterns with project-specific values |
| Pattern | Adapt the structure and intent but rewrite specifics | Cross-cutting concerns with varying implementations |

#### Verbatim Reuse Example

```
[LIB-SEC-001] The system shall encrypt all data at rest using AES-256.
Type: Verbatim | Domain: Security | Regulation: HIPAA, PCI DSS
```

#### Parameterized Reuse Example

```
[LIB-AUTH-001] The system shall lock the user account after
{MAX_ATTEMPTS} consecutive failed login attempts for {LOCKOUT_DURATION}.
Type: Parameterized | Domain: Authentication
Parameters: MAX_ATTEMPTS (integer, default: 5), LOCKOUT_DURATION (minutes, default: 15)
```

#### Pattern Reuse Example

```
[LIB-NOTIFY-001] The system shall deliver {NOTIFICATION_TYPE} notifications
to {RECIPIENT_ROLE} within {DELIVERY_SLA} of {TRIGGER_EVENT}.
Type: Pattern | Domain: Notification
Structure: Trigger -> Channel -> Recipient -> SLA
```

### Step 4: Generate Library Catalog

For each reusable requirement, create a catalog entry:

| Field | Description |
|-------|-------------|
| Library ID | LIB-[DOMAIN]-[NNN] |
| Category | Cross-cutting, Domain, or Regulatory |
| Domain | Authentication, Security, E-Commerce, etc. |
| Reuse Type | Verbatim, Parameterized, or Pattern |
| Description | The requirement text or template |
| Parameters | Variables that must be filled (parameterized/pattern only) |
| Defaults | Default values for parameters |
| Constraints | Conditions under which this requirement applies |
| Source Projects | Projects where this requirement has been used |
| Usage Count | Number of times reused across projects |
| Last Used | Date of most recent reuse |
| Validation Status | Verified, Unverified, or Deprecated |
| Standards | Applicable IEEE/ISO/regulatory standards |

### Step 5: Define Adaptation Guidelines

Document the process for reusing requirements from the library in new projects:

1. **Search:** Query the library by domain, category, or keyword.
2. **Evaluate:** Assess applicability to the target project context.
3. **Adapt:** For parameterized and pattern types, fill in project-specific values.
4. **Validate:** Verify the adapted requirement against the target project's vision and constraints.
5. **Register:** Add the new usage to the library's usage tracking.
6. **Trace:** Establish trace links from the reused requirement to target project business goals.

### Step 6: Commonality and Variability Analysis

For product line engineering, perform commonality/variability analysis:

- **Common Requirements:** Requirements shared by all products in the product line (mandatory inclusion).
- **Variable Requirements:** Requirements that differ between products (variation points).
- **Optional Requirements:** Requirements included only in specific product variants.

Document variation points with:

| Field | Description |
|-------|-------------|
| Variation Point ID | VP-[NNN] |
| Description | What varies across products |
| Variants | List of possible options |
| Binding Time | Design-time, build-time, or runtime |
| Default Variant | The variant used when no explicit choice is made |

### Step 7: Generate Output

Write `../output/requirements_library.md` following the output format below.

## Output Format

### requirements_library.md

```markdown
# Requirements Library: [Project Name]

**Generated:** [Date]
**Standards:** IEEE 29148-2018, Laplante Ch.9

---

## Library Summary

| Metric | Value |
|--------|-------|
| Total Library Entries | N |
| Cross-Cutting Concerns | N |
| Domain Patterns | N |
| Regulatory Requirements | N |
| Verbatim Reuse | N |
| Parameterized Reuse | N |
| Pattern Reuse | N |

---

## Library Catalog

### Cross-Cutting Concerns

| Library ID | Domain | Reuse Type | Description | Parameters |
|------------|--------|-----------|-------------|------------|
| LIB-AUTH-001 | Authentication | Parameterized | Account lockout | MAX_ATTEMPTS, LOCKOUT_DURATION |

### Domain Patterns

| Library ID | Domain | Reuse Type | Description | Parameters |
|------------|--------|-----------|-------------|------------|
| LIB-ECOM-001 | E-Commerce | Pattern | Checkout flow | PAYMENT_METHODS, TAX_RULES |

### Regulatory Requirements

| Library ID | Regulation | Reuse Type | Description | Applicability |
|------------|-----------|-----------|-------------|---------------|
| LIB-GDPR-001 | GDPR | Verbatim | Consent management | All EU-facing systems |

---

## Adaptation Guidelines

[Step-by-step process for reusing library entries]

---

## Commonality/Variability Analysis

| VP ID | Description | Variants | Binding Time |
|-------|-------------|----------|-------------|
| VP-001 | Payment processing | Stripe, PayPal, Square | Build-time |

---

## Usage Tracking

| Library ID | Source Project | Target Project | Date Reused | Adaptation Notes |
|------------|---------------|----------------|-------------|-----------------|
| LIB-AUTH-001 | Project A | Project B | [Date] | MAX_ATTEMPTS=3 |
```

## Common Pitfalls

- **Premature generalization:** Do not extract a pattern from a single instance. A requirement is a reuse candidate only after it has appeared in at least one project and has clear cross-project applicability.
- **Over-parameterization:** Too many parameters make a template harder to use than writing from scratch. Limit parameterized templates to 5 or fewer variables.
- **Stale library entries:** Requirements that reference obsolete technologies or superseded regulations shall be marked Deprecated and excluded from new project reuse.
- **Ignoring context:** A requirement that works in one domain may be harmful in another. Always validate adapted requirements against the target project's specific constraints.
- **Copy without trace:** Reused requirements must still be traced to the target project's business goals. Reuse does not exempt a requirement from traceability obligations.

## Verification Checklist

- [ ] All cross-cutting concerns in output artifacts have been evaluated for reuse potential.
- [ ] Each library entry has a unique LIB-[DOMAIN]-[NNN] identifier.
- [ ] Reuse type is classified as Verbatim, Parameterized, or Pattern.
- [ ] Parameterized templates include parameter definitions with defaults.
- [ ] Adaptation guidelines define the search-evaluate-adapt-validate-register-trace workflow.
- [ ] Variation points are documented for product line requirements.
- [ ] No library entry references undefined or subjective terms.

## Integration

- **Upstream:** `08-requirements-management`, `09-traceability-engineering`, `10-requirements-metrics`
- **Downstream:** Future project initialization skills, product line engineering
- **Optional:** This skill is not required for single-product organizations

## Standards

- **IEEE Std 29148-2018:** Requirements reuse and product line provisions.
- **Laplante Ch.9:** Software product line engineering and requirements reuse.
- **Wiegers Practice 20:** Requirements process improvement and institutionalization.
- **IEEE Std 610.12-1990:** Terminology definitions.

## Resources

- `references/reuse-patterns.md`: Requirements reuse pattern taxonomy and decision criteria.
- `references/product-line-requirements.md`: SPL commonality/variability analysis guide.

---
**Last Updated:** 2026-03-07
**Skill Version:** 1.0.0
