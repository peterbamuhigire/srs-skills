# Software Product Line Requirements Reference

**Purpose:** Guide commonality/variability analysis, feature modeling, variation point identification, and the distinction between platform and product requirements for Software Product Line (SPL) engineering.

**Standards:** IEEE 29148-2018, Laplante Ch.9

---

## What Is Software Product Line Engineering?

A Software Product Line (SPL) is a set of software-intensive systems that share a common, managed set of features satisfying the specific needs of a particular market segment or mission. SPL requirements engineering identifies which requirements are common to all products and which vary between products.

---

## Commonality/Variability Analysis

### Commonality

Common requirements are features, behaviors, or constraints shared by **every product** in the product line. They form the platform core.

**Identification Criteria:**
- The requirement appears in every existing product.
- The requirement is mandated by regulation or organizational policy for all products.
- Removing the requirement would invalidate the product line's core value proposition.

**Examples:**
- User authentication (all products require login).
- Audit logging (all products must log actions for compliance).
- Data encryption at rest (all products handle sensitive data).

### Variability

Variable requirements are features, behaviors, or constraints that **differ between products** in the product line. They represent the points where products diverge.

**Identification Criteria:**
- The requirement applies to some products but not others.
- The requirement's parameters differ between products (e.g., different SLA targets).
- The requirement's implementation varies by product context (e.g., different payment gateways).

**Examples:**
- Payment processing (Product A uses Stripe; Product B uses PayPal; Product C has no payments).
- Reporting (Product A needs financial reports; Product B needs inventory reports).
- Multi-language support (Product A is English-only; Product B supports 5 languages).

### Analysis Template

| Requirement | Product A | Product B | Product C | Classification |
|-------------|-----------|-----------|-----------|----------------|
| User authentication | Yes | Yes | Yes | Common |
| Audit logging | Yes | Yes | Yes | Common |
| Payment processing | Stripe | PayPal | N/A | Variable |
| Multi-language | No | Yes (5 langs) | Yes (3 langs) | Variable |
| Mobile app | Yes | No | Yes | Optional |

---

## Feature Models

A feature model is a hierarchical representation of all features in a product line, showing which features are mandatory, optional, or alternative.

### Feature Types

| Type | Symbol | Definition |
|------|--------|-----------|
| Mandatory | Filled circle | Feature must be included in every product |
| Optional | Empty circle | Feature may or may not be included |
| Alternative (XOR) | Arc with line | Exactly one feature from the group must be selected |
| Or (inclusive) | Filled arc | At least one feature from the group must be selected |

### Feature Model Template

```
Root Feature: [Product Line Name]
│
├── [Mandatory] Core Authentication
│   ├── [Mandatory] Login
│   ├── [Mandatory] Password Management
│   └── [Optional] Multi-Factor Authentication
│
├── [Mandatory] Data Management
│   ├── [Mandatory] CRUD Operations
│   ├── [Optional] Bulk Import/Export
│   └── [Alternative] Storage Backend
│       ├── MySQL
│       ├── PostgreSQL
│       └── SQLite
│
├── [Optional] Payment Processing
│   └── [Or] Payment Gateway
│       ├── Stripe
│       ├── PayPal
│       └── Square
│
├── [Optional] Reporting
│   ├── [Mandatory] Dashboard
│   └── [Optional] Export to PDF/CSV
│
└── [Optional] Internationalization
    ├── [Mandatory] Language Selection
    └── [Optional] RTL Support
```

### Feature Model Constraints

Cross-tree constraints express dependencies and exclusions between features:

| Constraint Type | Syntax | Meaning |
|----------------|--------|---------|
| Requires | A requires B | If A is selected, B must also be selected |
| Excludes | A excludes B | If A is selected, B must not be selected |
| Recommends | A recommends B | If A is selected, B should be selected (soft constraint) |

**Example Constraints:**
- Payment Processing requires Core Authentication (cannot process payments without user identity).
- SQLite excludes Bulk Import/Export (SQLite cannot handle concurrent bulk operations).
- Internationalization recommends Reporting Export (reports should be generated in the user's language).

---

## Variation Points

A variation point is a specific location in the product line architecture where a decision must be made to select among variants.

### Variation Point Template

| Field | Description |
|-------|-------------|
| VP ID | VP-[NNN] |
| Name | Descriptive name of the variation point |
| Description | What decision must be made |
| Variants | List of available options |
| Default | The option used when no explicit selection is made |
| Binding Time | When the decision is resolved (see below) |
| Rationale | Why this is a variation point rather than a common feature |
| Constraints | Dependencies on or exclusions with other VPs |

### Example

| Field | Value |
|-------|-------|
| VP ID | VP-001 |
| Name | Payment Gateway Selection |
| Description | Which payment processing service to integrate |
| Variants | Stripe, PayPal, Square |
| Default | Stripe |
| Binding Time | Build-time |
| Rationale | Different markets prefer different payment providers |
| Constraints | Requires VP-003 (Currency Configuration) |

---

## Binding Times

The binding time determines when a variation point decision is resolved.

| Binding Time | When | How | Example |
|-------------|------|-----|---------|
| Specification-time | During requirements phase | Feature selection in requirements document | Choose which modules to include |
| Design-time | During architecture/design phase | Interface and pattern selection | Choose design pattern for extensibility |
| Build-time | During compilation/packaging | Build configuration, feature flags | Compile with Stripe vs. PayPal SDK |
| Deployment-time | During installation/configuration | Configuration files, environment variables | Set database connection string |
| Runtime | During system execution | User preferences, dynamic loading | User selects language preference |

### Binding Time Decision Criteria

| Criterion | Recommended Binding Time |
|-----------|------------------------|
| Decision affects architecture | Specification-time or Design-time |
| Decision affects dependencies | Build-time |
| Decision is environment-specific | Deployment-time |
| Decision is user-specific | Runtime |
| Decision is irreversible once made | Specification-time |
| Decision must be changeable without rebuild | Deployment-time or Runtime |

---

## Platform vs. Product Requirements

### Platform Requirements

Platform requirements define the shared infrastructure, services, and constraints that apply to all products in the product line.

| Characteristic | Description |
|---------------|-------------|
| Scope | All products |
| Ownership | Platform team |
| Change frequency | Low (changes affect all products) |
| Testing | Platform-level integration tests |
| Examples | Authentication service, logging framework, data access layer, API gateway |

### Product Requirements

Product requirements define features, behaviors, and constraints specific to a single product or a subset of products.

| Characteristic | Description |
|---------------|-------------|
| Scope | Single product or product subset |
| Ownership | Product team |
| Change frequency | Higher (changes affect only the target product) |
| Testing | Product-level acceptance tests |
| Examples | Industry-specific reports, custom workflows, specialized integrations |

### Classification Template

| Req ID | Requirement | Platform? | Products | Variation Point |
|--------|-------------|-----------|----------|----------------|
| PLT-001 | User authentication via OAuth 2.0 | Yes | All | N/A (common) |
| PLT-002 | Audit log retention for 7 years | Yes | All | N/A (common) |
| PRD-001 | Generate financial compliance report | No | Product A only | N/A |
| PRD-002 | Process payments via {GATEWAY} | No | Products A, C | VP-001 |

---

## SPL Requirements Process

### Step 1: Domain Analysis

Analyze the target market segment to identify the scope of the product line:
- What products exist or are planned?
- What features do they share?
- Where do they differ?

### Step 2: Feature Modeling

Build the feature model showing mandatory, optional, and alternative features with cross-tree constraints.

### Step 3: Commonality/Variability Classification

Classify each requirement as common, variable, or optional using the analysis template.

### Step 4: Variation Point Identification

For each variable requirement, define the variation point with its variants, binding time, and constraints.

### Step 5: Platform/Product Separation

Assign each requirement to the platform (shared) or a specific product. Platform requirements are developed and maintained by the platform team.

### Step 6: Product Derivation

For a new product, derive its requirements by:
1. Including all mandatory (common) requirements.
2. Selecting options at each variation point.
3. Adding product-specific requirements.
4. Validating that feature model constraints are satisfied.

---

## Quality Criteria for SPL Requirements

- [ ] Every requirement is classified as common, variable, or optional.
- [ ] Every variable requirement has a defined variation point.
- [ ] Every variation point has a specified binding time.
- [ ] Feature model constraints (requires/excludes) are documented.
- [ ] Platform requirements are separated from product requirements.
- [ ] No product-specific logic exists in platform requirements.
- [ ] Product derivation satisfies all feature model constraints.

---

## References

- **IEEE Std 29148-2018:** Product line requirements provisions.
- **Laplante Ch.9:** Software product line engineering.
- **Pohl, Bockle, van der Linden (2005):** Software Product Line Engineering -- Foundations, Principles, and Techniques.
- **Clements and Northrop (2001):** Software Product Lines -- Practices and Patterns.
- **Kang et al. (1990):** Feature-Oriented Domain Analysis (FODA).

---
**Last Updated:** 2026-03-07
