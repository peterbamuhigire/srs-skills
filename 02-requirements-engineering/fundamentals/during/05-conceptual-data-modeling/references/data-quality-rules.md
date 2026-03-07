# Data Quality Rules Reference Guide

**Purpose:** Define six data quality dimensions with measurement criteria and map them to business rules at the conceptual modeling level.

**Standards:** IEEE 29148-2018, Book 2 Ch.6-7

---

## 1. Six Data Quality Dimensions

### 1.1 Completeness

**Definition:** All required data fields have values; no mandatory information is missing.

**Measurement Criterion:**

$CompletenessRate = \frac{PopulatedRequiredFields}{TotalRequiredFields} \times 100$

**Business Rule Mapping:**
- Every entity attribute marked as "Required" in the conceptual model SHALL have a completeness rule
- Minimum acceptable completeness rate SHALL be defined per entity (typical threshold: 98%)

**Example:**
- Entity: Customer
- Rule: "Customer Name and Email Address shall be populated for every customer record."
- Threshold: 100% for name, 98% for email (some legacy records may lack email)

### 1.2 Consistency

**Definition:** The same data is represented in the same way across all contexts where it appears.

**Measurement Criterion:**

$ConsistencyRate = \frac{ConsistentRecords}{TotalCrossReferencedRecords} \times 100$

**Business Rule Mapping:**
- When the same entity attribute appears in multiple features or subsystems, a consistency rule SHALL enforce identical representation
- Format standards (date formats, currency notation, unit systems) SHALL be declared per attribute

**Example:**
- Entity: Order
- Rule: "Order status values shall use the same enumeration (Draft, Submitted, Approved, Shipped, Delivered, Cancelled) across all subsystems."
- Threshold: 100% (no inconsistent status values)

### 1.3 Conformity

**Definition:** Data values adhere to defined formats, patterns, and domain constraints.

**Measurement Criterion:**

$ConformityRate = \frac{ConformingValues}{TotalValues} \times 100$

**Business Rule Mapping:**
- Every attribute with a defined format (email, phone, postal code, currency) SHALL have a conformity rule
- Conformity rules SHALL specify the validation pattern or reference standard

**Example:**
- Entity: Customer
- Attribute: Email Address
- Rule: "Email address shall conform to RFC 5322 format."
- Threshold: 100% (reject non-conforming values at input)

### 1.4 Accuracy

**Definition:** Data correctly represents the real-world entity or event it describes.

**Measurement Criterion:**

$AccuracyRate = \frac{VerifiedAccurateRecords}{TotalSampledRecords} \times 100$

**Business Rule Mapping:**
- Accuracy is typically verified through sampling or stakeholder confirmation
- Critical entities (financial, regulatory) SHALL have accuracy verification procedures defined

**Example:**
- Entity: Product
- Attribute: Base Price
- Rule: "Product base price shall match the current supplier price list, verified quarterly."
- Threshold: 99.5% (0.5% tolerance for pricing lag)

### 1.5 Timeliness

**Definition:** Data is current and updated within an acceptable latency window.

**Measurement Criterion:**

$TimelinessCompliance = \frac{RecordsUpdatedWithinThreshold}{TotalRecords} \times 100$

**Business Rule Mapping:**
- Every entity with time-sensitive attributes SHALL define a maximum acceptable data age
- Real-time, near-real-time, and batch update categories SHALL be documented

**Example:**
- Entity: Inventory
- Attribute: Stock Quantity
- Rule: "Stock quantity shall reflect actual warehouse count within a 15-minute latency."
- Threshold: 95% of updates within 15 minutes

### 1.6 Uniqueness

**Definition:** No duplicate entity instances exist within the system; each real-world entity is represented exactly once.

**Measurement Criterion:**

$DuplicateRate = \frac{DuplicateRecords}{TotalRecords} \times 100$

Target: $DuplicateRate < 1\%$

**Business Rule Mapping:**
- Every entity SHALL define a natural key or business key that uniquely identifies instances
- Deduplication rules SHALL specify matching criteria (exact match, fuzzy match, phonetic match)

**Example:**
- Entity: Customer
- Business Key: Email Address
- Rule: "No two customer records shall share the same email address. Duplicates shall be detected and merged."
- Threshold: 0% duplicates (enforce at creation time)

---

## 2. Data Quality Profile Template

For each entity in the conceptual model, produce a quality profile:

| Entity    | Dimension    | Rule Description                              | Threshold | Verification Method        |
|-----------|--------------|-----------------------------------------------|-----------|----------------------------|
| Customer  | Completeness | Name and email required                       | 100%      | Null check on insert       |
| Customer  | Uniqueness   | Email must be unique                          | 0% dupes  | Unique constraint          |
| Customer  | Conformity   | Email conforms to RFC 5322                    | 100%      | Regex validation           |
| Order     | Consistency  | Status uses defined enumeration               | 100%      | Enum constraint            |
| Order     | Timeliness   | Status updated within 5 minutes of event      | 98%       | Timestamp comparison       |
| Product   | Accuracy     | Price matches supplier list                   | 99.5%     | Quarterly audit            |
| Inventory | Timeliness   | Stock count within 15-minute latency          | 95%       | Update timestamp monitoring|

---

## 3. Quality Rule Priority

Not all quality dimensions are equally important for every entity. Apply the following priority framework:

| Entity Type        | Critical Dimensions                    | Important Dimensions         | Monitored Dimensions    |
|--------------------|----------------------------------------|------------------------------|-------------------------|
| Financial entities | Accuracy, Completeness, Consistency    | Timeliness, Conformity       | Uniqueness              |
| Master data        | Uniqueness, Completeness, Consistency  | Accuracy, Conformity         | Timeliness              |
| Transactional      | Timeliness, Completeness, Accuracy     | Consistency, Conformity      | Uniqueness              |
| Reference data     | Accuracy, Consistency, Completeness    | Conformity                   | Timeliness, Uniqueness  |

---

## 4. Business Rule-to-Quality Dimension Mapping Process

1. Read each business rule from `business_rules.md`
2. Identify which data quality dimension the rule enforces
3. Map the rule to the specific entity and attribute it governs
4. Define the acceptance threshold
5. Specify the verification method (automated validation, manual audit, sampling)

**Example Mapping:**

| Business Rule | Quality Dimension | Entity.Attribute        | Threshold |
|---------------|-------------------|-------------------------|-----------|
| BR-001        | Completeness      | Customer.name           | 100%      |
| BR-002        | Conformity        | Customer.email          | 100%      |
| BR-005        | Accuracy          | Product.base_price      | 99.5%     |
| BR-010        | Timeliness        | Inventory.stock_quantity | 95%       |

---

## 5. Data Quality Checklist

- [ ] Every entity has at least one quality dimension defined
- [ ] Every required attribute has a completeness rule
- [ ] Every entity has a uniqueness key defined
- [ ] Format-constrained attributes have conformity rules
- [ ] Time-sensitive attributes have timeliness thresholds
- [ ] Quality thresholds are numeric and measurable (not subjective)
- [ ] Verification methods are specified for every rule
- [ ] Business rules from `business_rules.md` are mapped to quality dimensions

---

**Last Updated:** 2026-03-07
