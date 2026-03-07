# Goal-Oriented Requirements Engineering Reference Guide

**Purpose:** Decompose business goals into requirements using KAOS and i* frameworks with AND/OR goal trees.

**Standards:** IEEE 29148-2018 Section 6.2, Laplante Ch.5

---

## 1. Goal-Oriented RE Overview

Goal-Oriented Requirements Engineering (GORE) starts from high-level business objectives and systematically decomposes them into implementable requirements. Unlike feature-driven approaches, GORE ensures every requirement traces to a justified business purpose and exposes goal conflicts early.

### When to Apply GORE

- Business goals in `vision.md` are complex or hierarchical
- Multiple stakeholders have competing objectives
- The team needs to justify why each requirement exists
- Regulatory or compliance goals must be formally decomposed

---

## 2. KAOS Framework

KAOS (Knowledge Acquisition in autOmated Specification) uses four modeling concepts:

### 2.1 Core Concepts

| Concept    | Definition                                                    | Notation       |
|------------|---------------------------------------------------------------|----------------|
| Goal       | A prescriptive statement of intent the system shall satisfy   | Parallelogram  |
| Agent      | An active entity (human or system) responsible for a goal     | Hexagon        |
| Object     | A passive entity acted upon by agents                         | Rectangle      |
| Operation  | A transformation an agent performs on objects to achieve goals | Oval           |

### 2.2 Goal Decomposition

Goals are decomposed using AND/OR refinement:

- **AND-refinement:** All sub-goals must be satisfied to satisfy the parent goal
- **OR-refinement:** At least one sub-goal must be satisfied to satisfy the parent goal

**Example:**

```
Goal: Ensure Order Fulfillment (AND)
  |
  +-- Sub-Goal 1: Validate Order Contents (AND)
  |     +-- Check inventory availability
  |     +-- Verify pricing accuracy
  |
  +-- Sub-Goal 2: Process Payment (OR)
  |     +-- Process credit card payment
  |     +-- Process bank transfer
  |
  +-- Sub-Goal 3: Ship Order
        +-- Generate shipping label
        +-- Notify customer of shipment
```

### 2.3 Goal Types

| Type           | Definition                                            | Example                                    |
|----------------|-------------------------------------------------------|--------------------------------------------|
| Achieve        | A state that must eventually be reached               | "Order shall be shipped within 48 hours"   |
| Maintain       | A condition that must hold continuously               | "System shall remain available 99.9%"      |
| Avoid          | A state that must never occur                         | "Customer data shall never be exposed"     |
| Optimize       | A measurable value that should be maximized/minimized | "Minimize order processing time"           |

### 2.4 Agent Assignment

Each leaf-level goal SHALL be assigned to exactly one agent:

| Goal                        | Agent Type     | Agent Name        |
|-----------------------------|----------------|-------------------|
| Validate inventory          | System         | InventoryService  |
| Approve refund              | Human          | StoreManager      |
| Process credit card         | External System| PaymentGateway    |

---

## 3. i* (Intentional) Modeling

The i* framework models stakeholder intentions and dependencies.

### 3.1 Core Concepts

| Concept       | Definition                                              | Notation       |
|---------------|---------------------------------------------------------|----------------|
| Actor         | An entity with intentional properties (goals, beliefs)  | Circle         |
| Goal          | A state of affairs the actor wants to achieve           | Rounded rect   |
| Softgoal      | A goal without a clear-cut satisfaction criterion       | Cloud shape    |
| Task          | A specific way of doing something                       | Hexagon        |
| Resource      | A physical or informational entity                      | Rectangle      |
| Dependency    | A relationship where one actor depends on another       | Arrow with "D" |

### 3.2 Strategic Dependency Model

Maps dependencies between actors:

```
Customer --[goal: receive order]--> System
System --[resource: payment confirmation]--> PaymentGateway
System --[task: ship order]--> WarehouseStaff
Manager --[softgoal: customer satisfaction]--> System
```

### 3.3 Strategic Rationale Model

Details the internal reasoning of each actor:

```
Actor: OrderManagementSystem
  Goal: Process Order
    Task: Validate Order (AND)
      Resource: Product Catalog
      Resource: Inventory Database
    Task: Calculate Total
      Softgoal: Accuracy [++]
      Softgoal: Performance [+]
    Task: Submit Payment
      Dependency: PaymentGateway
```

---

## 4. AND/OR Goal Decomposition Trees

### 4.1 Construction Process

1. **Identify Root Goal:** Extract the top-level business goal from `vision.md`
2. **Decompose:** Ask "What sub-goals must be achieved?" (AND) or "What alternative sub-goals could achieve this?" (OR)
3. **Refine:** Continue decomposing until each leaf goal is specific enough to be a requirement
4. **Assign Agents:** Map each leaf goal to a responsible agent
5. **Validate:** Ensure the tree is complete (no missing branches) and consistent (no contradictions)

### 4.2 Textual Tree Format

```
[AND] G-001: Manage Customer Orders
  |
  +-- [AND] G-001.1: Accept New Orders
  |     +-- [LEAF] G-001.1.1: Validate order data -> FR-010
  |     +-- [LEAF] G-001.1.2: Check inventory -> FR-011
  |     +-- [LEAF] G-001.1.3: Calculate pricing -> FR-012
  |
  +-- [OR] G-001.2: Process Payment
  |     +-- [LEAF] G-001.2.1: Credit card -> FR-020
  |     +-- [LEAF] G-001.2.2: Bank transfer -> FR-021
  |
  +-- [AND] G-001.3: Fulfill Order
        +-- [LEAF] G-001.3.1: Generate packing slip -> FR-030
        +-- [LEAF] G-001.3.2: Update inventory -> FR-031
        +-- [LEAF] G-001.3.3: Send shipping notification -> FR-032
```

### 4.3 Goal Conflict Detection

Goal conflicts arise when satisfying one goal impedes another:

| Conflict Type     | Description                                             | Resolution            |
|-------------------|---------------------------------------------------------|-----------------------|
| Resource Conflict | Two goals compete for the same limited resource         | Prioritize or sequence|
| Logic Conflict    | Achieving goal A makes goal B impossible                | Stakeholder arbitration|
| Temporal Conflict | Two goals have incompatible timing requirements         | Schedule negotiation  |

**Detection Process:**
1. For each pair of sibling goals under the same parent, ask: "Does achieving one make the other harder?"
2. For goals assigned to the same agent, check for resource contention
3. Document conflicts with the conflicting goal identifiers and recommended resolution

---

## 5. GORE-to-Requirements Mapping

| Goal Tree Element        | Maps To                  | IEEE 29148 Reference     |
|--------------------------|--------------------------|--------------------------|
| Root Goal                | Business Objective       | Section 6.2.1            |
| AND-decomposed sub-goal  | Feature or capability    | Section 6.2.2            |
| OR-decomposed sub-goal   | Alternative requirement  | Section 6.2.2            |
| Leaf Goal                | Functional Requirement   | Section 6.5              |
| Softgoal                 | Non-Functional Requirement | Section 6.5.3          |
| Agent Assignment         | Responsibility Matrix    | Section 6.4              |

---

## 6. Goal Modeling Checklist

- [ ] Root goals extracted from `vision.md` business objectives
- [ ] Every goal decomposed until leaf goals are requirement-level
- [ ] AND/OR decomposition type explicitly marked at every branch
- [ ] Every leaf goal assigned to exactly one agent
- [ ] Goal conflicts detected and documented with resolution strategies
- [ ] Leaf goals mapped to functional or non-functional requirement identifiers
- [ ] Goal tree validated for completeness (no missing branches)

---

**Last Updated:** 2026-03-07
