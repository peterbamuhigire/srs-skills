# Actor Classification and Identification Guide

## Purpose

This reference provides techniques for identifying, classifying, and organizing actors in a use case model. Correct actor identification ensures complete system boundary definition and prevents orphan requirements.

## Reference Standards

- UML 2.5.1 Section 18.1 -- Use Case Actors
- IEEE 29148-2018 -- Stakeholder identification for behavioral requirements
- Dennis, Wixom, Tegarden -- "Systems Analysis and Design with UML" (actor analysis)

## Actor Definition

An actor represents a role that a user or external system plays when interacting with the system under design. An actor is not a specific person -- it is a role. One person may fulfill multiple actor roles, and one actor role may be filled by multiple people.

## Actor Types

### Primary Actor

The actor who initiates the use case to achieve a goal. The system exists to serve the primary actor's needs.

| Characteristic | Description |
|---------------|-------------|
| **Relationship** | Directly triggers use case execution |
| **Goal** | Has a specific, measurable goal the system shall fulfill |
| **Diagram Position** | Left side of the use case diagram |
| **Example** | Customer placing an order, Employee submitting a timesheet |

### Supporting (Secondary) Actor

The actor that provides a service to the system during use case execution. The system calls upon the supporting actor to complete a task.

| Characteristic | Description |
|---------------|-------------|
| **Relationship** | Responds to system requests; does not initiate use cases |
| **Goal** | Fulfills a supporting function (authentication, payment processing, notification) |
| **Diagram Position** | Right side of the use case diagram |
| **Example** | Payment Gateway, Email Service, Identity Provider |

### Offstage Actor

The actor who has an interest in the use case outcome but does not directly interact with the system during execution.

| Characteristic | Description |
|---------------|-------------|
| **Relationship** | Stakeholder with constraints or interests; no direct interaction |
| **Goal** | Ensures compliance, receives reports, or sets business rules |
| **Diagram Position** | Noted in use case description but typically not on the diagram |
| **Example** | Regulatory Body, Auditor, Company Board |

## Human Actors vs System Actors

| Attribute | Human Actor | System Actor |
|-----------|-------------|-------------|
| **Representation** | Stick figure in UML | Stick figure with `<<system>>` stereotype |
| **Interaction** | Through user interfaces | Through APIs, protocols, or message queues |
| **Reliability** | May make errors; alternative flows needed | Deterministic; exception flows for failures |
| **Authentication** | Credentials, biometrics, tokens | API keys, certificates, OAuth tokens |
| **Example** | Customer, Administrator | Payment Gateway, Notification Service, LDAP Server |

## Actor Identification Techniques

### Technique 1: Stakeholder List Review

1. Read `stakeholder_register.md` (or `stakeholders.md`).
2. For each stakeholder, determine whether they interact directly with the system.
3. If yes, the stakeholder is a candidate actor. Determine the type (primary or supporting).
4. If no direct interaction, evaluate whether the stakeholder has constraints or interests. If yes, classify as offstage.

### Technique 2: Role Analysis

1. Extract all "As a [role]" clauses from user stories in `features.md`.
2. Deduplicate roles. Two different user story roles that perform the same system interactions shall merge into one actor.
3. Roles that only appear in acceptance criteria (not as initiators) are supporting actors.

### Technique 3: System Boundary Analysis

1. Draw the system boundary (what is inside vs outside the system).
2. Identify all external entities that send data into or receive data from the system.
3. Each external entity is a candidate actor.
4. External systems (APIs, databases, services) are system actors.

### Technique 4: Event Analysis

1. List all external events the system shall respond to.
2. For each event, identify who or what generates the event.
3. The event generator is a candidate actor.

## Actor Generalization (Inheritance)

### When to Use

Apply actor generalization when two or more actors share a common set of use cases but each also has unique use cases.

### Structure

```
        [General Actor]
           /       \
  [Specific A]   [Specific B]
```

- The general actor defines shared behaviors.
- Specific actors inherit all use cases from the general actor and add their own.

### Example

```
           User
          /    \
    Customer   Administrator
```

- **User** participates in: View Profile, Update Password.
- **Customer** inherits from User and adds: Place Order, Track Shipment.
- **Administrator** inherits from User and adds: Manage Users, Generate Reports.

### Rules

1. The generalization shall reduce duplication in the use case diagram.
2. Do not create a general actor unless at least two specific actors share at least two use cases.
3. The general actor may be abstract (no direct instances) or concrete.
4. Generalization depth shall not exceed two levels.

## Actor vs Persona

| Aspect | Actor | Persona |
|--------|-------|---------|
| **Purpose** | Models a role in system interactions | Models a fictional representative user |
| **Scope** | System behavior and boundaries | User experience and motivation |
| **Detail** | Role name, type, interactions | Name, demographics, goals, frustrations |
| **Usage** | Use case diagrams and descriptions | UX design, stakeholder communication |
| **Standard** | UML 2.5.1 | Not standardized |

**Rule:** Actors and personas are complementary. The skill shall identify actors for the use case model. Personas may inform actor discovery but shall not replace actors in the model.

## Actor Catalog Template

The skill shall produce an actor catalog in this format:

| Actor | Type | Human/System | Description | Generalization | Use Cases |
|-------|------|-------------|-------------|----------------|-----------|
| Customer | Primary | Human | End user who purchases products | Inherits from User | UC-001, UC-002, UC-005 |
| Administrator | Primary | Human | Internal user who manages system configuration | Inherits from User | UC-010, UC-011 |
| Payment Gateway | Supporting | System | External service that processes payments | None | UC-002 |
| Regulatory Body | Offstage | Human | Government agency requiring compliance reports | None | Referenced in UC-015 |

## Validation Rules

1. Every actor shall participate in at least one use case. Flag orphan actors with `[V&V-FAIL: Actor "[Name]" has no associated use case]`.
2. Every use case shall have exactly one primary actor. Flag violations with `[V&V-FAIL: UC-[NNN] has [count] primary actors]`.
3. Actor names shall be singular nouns or noun phrases (e.g., "Customer" not "Customers").
4. No two actors shall have the same name unless they are the same actor.
5. Supporting actors shall have at least one system-initiated interaction (the system calls them, not the reverse).

## Common Mistakes

| Mistake | Correction |
|---------|------------|
| Listing a specific person as an actor | Use the role name, not the person's name |
| Creating an actor for every stakeholder | Only stakeholders who interact with the system are primary/supporting actors |
| Confusing actors with user interface components | "Login Screen" is not an actor; the user who logs in is the actor |
| Missing system actors | Review all external integrations, APIs, and services |
| Flat actor list without generalization | Look for shared use cases and apply inheritance |
| Using plural names | Actor names shall be singular: "Customer" not "Customers" |
