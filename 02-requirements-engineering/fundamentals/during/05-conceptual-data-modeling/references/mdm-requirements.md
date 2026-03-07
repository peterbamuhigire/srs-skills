# Master Data Management Requirements Reference Guide

**Purpose:** Define MDM requirements including golden record identification, entity resolution, data stewardship, and cross-system integration at the conceptual level.

**Standards:** IEEE 29148-2018, Book 2 Ch.7

---

## 1. MDM Overview

Master Data Management governs the creation, maintenance, and use of core business entities that are shared across multiple subsystems or organizational boundaries. MDM ensures a single, authoritative version of each master entity exists (the "golden record").

### When MDM Requirements Apply

- Multiple features reference the same core entity (e.g., Customer, Product, Employee)
- Data originates from or is consumed by more than one system
- Business rules require consistent entity definitions across domains
- Regulatory requirements mandate data lineage or provenance tracking

---

## 2. Golden Record Identification

### 2.1 Definition

A golden record is the single, authoritative representation of a master entity. It is the version of truth that all systems reference.

### 2.2 Identification Process

1. **Inventory Master Entities:** List all entities referenced by more than one feature or subsystem
2. **Identify Source Systems:** For each master entity, document where records originate
3. **Determine Survivorship Rules:** Define which source system's value wins when conflicts exist

**Master Entity Inventory Template:**

| Entity    | Referenced By Features       | Source Systems         | Golden Record Owner |
|-----------|------------------------------|------------------------|---------------------|
| Customer  | Sales, Support, Billing      | CRM, E-commerce, ERP   | CRM                 |
| Product   | Sales, Inventory, Purchasing | PIM, E-commerce, ERP   | PIM                 |
| Employee  | HR, Payroll, Access Control  | HRIS, Payroll System   | HRIS                |

### 2.3 Survivorship Rules

When the same attribute has different values across source systems, survivorship rules determine which value becomes the golden record:

| Strategy        | Rule                                                     | Best For                    |
|-----------------|----------------------------------------------------------|-----------------------------|
| Source Priority  | Designated source system always wins                     | Clear system-of-record      |
| Most Recent     | Most recently updated value wins                         | Fast-changing attributes    |
| Most Complete   | Value with the most populated fields wins                | Legacy migration scenarios  |
| Most Frequent   | Value appearing in the most sources wins                 | No clear authority          |
| Manual Override | Data steward makes the final decision                    | Conflict resolution         |

---

## 3. Entity Resolution Rules

Entity resolution determines whether two records from different sources represent the same real-world entity.

### 3.1 Matching Criteria

| Match Type     | Definition                                            | Example                           |
|----------------|-------------------------------------------------------|-----------------------------------|
| Exact Match    | All key fields are identical                          | Email = email, Name = name        |
| Fuzzy Match    | Key fields are similar within a defined tolerance     | "Jon Smith" ~ "John Smith"        |
| Phonetic Match | Key fields sound similar (Soundex, Metaphone)         | "Smith" ~ "Smyth"                 |
| Composite Match| Multiple fields combined reach a confidence threshold | Name + Address + Phone >= 85%     |

### 3.2 Match Confidence Scoring

$MatchConfidence = \sum_{i=1}^{n} w_i \times similarity(field_i^A, field_i^B)$

Where:
- $w_i$ is the weight assigned to field $i$
- $similarity()$ returns a value between 0 and 1

**Confidence Thresholds:**

| Confidence     | Action                                                  |
|----------------|---------------------------------------------------------|
| >= 95%         | Auto-merge records                                       |
| 75% - 94%      | Flag for data steward review                            |
| < 75%          | Treat as separate entities                               |

### 3.3 Resolution Process

1. **Match:** Compare incoming record against existing golden records
2. **Score:** Calculate match confidence using weighted field comparison
3. **Decide:** Auto-merge, flag for review, or create new record based on thresholds
4. **Merge:** If merging, apply survivorship rules to resolve attribute conflicts
5. **Audit:** Log the merge decision with source records and rationale

---

## 4. Data Stewardship Roles

### 4.1 Role Definitions

| Role               | Responsibility                                              | Typical Assignment       |
|--------------------|-------------------------------------------------------------|--------------------------|
| Data Owner         | Accountable for the quality and policy of a data domain     | Business unit leader     |
| Data Steward       | Operationally responsible for data quality and resolution   | Domain subject matter expert |
| Data Custodian     | Technically responsible for storage, access, and security   | IT/DBA team              |
| Data Consumer      | Uses data; reports quality issues                           | End users, analysts      |

### 4.2 Stewardship Assignment Template

| Entity    | Data Owner            | Data Steward         | Data Custodian      |
|-----------|-----------------------|----------------------|---------------------|
| Customer  | VP Sales              | CRM Administrator   | Database Team       |
| Product   | VP Merchandising      | Product Manager     | Database Team       |
| Employee  | VP Human Resources    | HR Operations Lead  | IT Security Team    |

### 4.3 Stewardship Responsibilities

The data steward for each master entity SHALL:
- Review and resolve flagged entity matches (75-94% confidence)
- Approve or reject survivorship rule overrides
- Monitor data quality metrics and report deviations
- Maintain the entity's golden record definition
- Escalate unresolvable conflicts to the data owner

---

## 5. Cross-System Integration Requirements

### 5.1 Integration Pattern Selection

| Pattern              | When to Use                                       | Latency       |
|----------------------|---------------------------------------------------|---------------|
| Real-time sync       | Changes must propagate immediately                | Milliseconds  |
| Event-driven         | Systems react to entity change events             | Seconds       |
| Batch synchronization| Periodic bulk updates are acceptable              | Hours         |
| Request-response     | Consumer queries master on demand                 | Milliseconds  |

### 5.2 Integration Requirements Template

For each master entity shared across systems, document:

| Field                  | Content                                               |
|------------------------|-------------------------------------------------------|
| Entity                 | The master entity name                                |
| Source System           | System of record (golden record source)              |
| Consumer Systems        | Systems that consume this entity's data              |
| Integration Pattern     | Real-time sync, event-driven, batch, or request-response |
| Sync Frequency          | How often data is synchronized                       |
| Conflict Resolution     | How conflicts between systems are resolved           |
| Data Format             | Canonical format for entity exchange                 |
| Error Handling          | What happens when sync fails                         |

### 5.3 Canonical Data Model

When multiple systems exchange master data, define a canonical (system-neutral) representation of each entity. The conceptual data model serves as the foundation for this canonical model.

**Canonical Model Requirements:**
- Entity names SHALL match the conceptual model glossary
- Attributes SHALL be a superset of all system-specific attributes
- Mappings from each source system to the canonical model SHALL be documented
- The canonical model SHALL be versioned and change-controlled

---

## 6. MDM Requirements Checklist

- [ ] Master entities identified (referenced by 2+ features or systems)
- [ ] Source systems documented for each master entity
- [ ] Golden record owner designated for each master entity
- [ ] Survivorship rules defined for attribute conflict resolution
- [ ] Entity resolution matching criteria defined with confidence thresholds
- [ ] Data stewardship roles assigned (owner, steward, custodian)
- [ ] Cross-system integration pattern selected per entity
- [ ] Canonical data model aligned with the conceptual ER model
- [ ] Error handling and conflict resolution procedures documented

---

**Last Updated:** 2026-03-07
