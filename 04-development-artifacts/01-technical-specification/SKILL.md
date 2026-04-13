---
name: "technical-specification"
description: "Generate a detailed technical specification bridging LLD to implementation with module contracts, data formats, and integration specifications per IEEE 1016 and IEEE 830."
metadata:
  use_when: "Use when the task matches technical specification skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Technical Specification Skill

## Overview

This is the first skill in Phase 04 (Development Artifacts). It transforms the Low-Level Design module decomposition and SRS requirements into an implementation-ready technical specification that defines module contracts, data format schemas, integration specifications, configuration parameters, and dependency matrices. The output serves as the primary reference for developers translating design into code and conforms to IEEE 1016-2009 and IEEE 830-1998.

## When to Use

- After Phase 03 completes and `LLD.md` exists in `../output/` with module decomposition and class diagrams.
- When `SRS_Draft.md` is present in `../output/` for requirement traceability.
- When `tech_stack.md` is present in `../project_context/` for technology-specific implementation details.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../output/LLD.md`, `../output/SRS_Draft.md`, `../project_context/tech_stack.md` |
| **Output**  | `../output/Technical_Specification.md` |
| **Tone**    | Implementation-precise, contract-driven, developer-facing |
| **Standard** | IEEE 1016-2009, IEEE 830-1998 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| LLD.md | `../output/LLD.md` | Yes | Module decomposition, class diagrams, algorithms to formalize as contracts |
| SRS_Draft.md | `../output/SRS_Draft.md` | Yes | Functional requirements for traceability and interface constraints |
| tech_stack.md | `../project_context/tech_stack.md` | Yes | Technology choices, runtime versions, framework-specific implementation details |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Technical_Specification.md | `../output/Technical_Specification.md` | Complete technical specification with module contracts, data formats, and integration specs |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `LLD.md` and `SRS_Draft.md` from `../output/` and `tech_stack.md` from `../project_context/`. Log the absolute path of each file read. If any required file is missing, halt execution and report the gap.

### Step 2: Extract Module Contracts from LLD

For each module defined in LLD.md, extract and formalize the contract:
- **Module Name**: exact identifier from the LLD class diagram
- **Public Interface**: method signatures with typed parameters and return types
- **Preconditions**: input constraints that must hold before invocation
- **Postconditions**: guaranteed state after successful execution
- **Exceptions**: error conditions and corresponding exception types

### Step 3: Define Data Format Specifications

For each data entity exchanged between modules or exposed via APIs, define:
- JSON schema with field names, types, required/optional flags, and constraints
- Database column types with precision (e.g., `DECIMAL(19,4)` for monetary values)
- Enumeration values with definitions for every status or category field

### Step 4: Define Integration Specifications

For each integration point identified in LLD and SRS Section 3.1, define the API contract:
- Endpoint path, HTTP method, and content type
- Request schema with typed parameters and validation rules
- Response schema with status codes and payload structure
- Authentication requirements and rate limits

### Step 5: Define Configuration Parameters

Document every configurable parameter the system requires:
- Parameter name, data type, default value, and valid range
- Environment variable mapping (e.g., `DB_HOST` maps to database connection host)
- Configuration file format and location

### Step 6: Define Dependency Matrix

Produce a module-to-module dependency matrix:
- Source module, target module, dependency type (compile-time, runtime, optional)
- Circular dependency detection: flag any bidirectional dependencies as design issues

### Step 7: Generate Implementation Notes

For each module, provide implementation guidance:
- Recommended design patterns from LLD (e.g., Repository, Strategy, Observer)
- Performance considerations derived from SRS non-functional requirements
- Security considerations derived from SRS Section 3.5

### Step 8: Write Output with Traceability

Write the completed document to `../output/Technical_Specification.md`. Include a traceability table mapping every module contract to its LLD module and originating SRS requirement IDs. Log the total count of module contracts, data schemas, and integration specifications.

## Output Format

The generated `Technical_Specification.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Introduction and Scope, 2. Module Contracts, 3. Data Format Specifications, 4. Integration Specifications, 5. Configuration Parameters, 6. Dependency Matrix, 7. Implementation Notes, 8. Traceability Matrix, Appendix A: Glossary.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Module contracts without preconditions | Every public method shall state input constraints explicitly |
| JSON schemas missing required/optional flags | Every field shall declare whether it is required or optional |
| Integration specs without error responses | Every API contract shall document error status codes and payloads |
| Configuration parameters without defaults | Every parameter shall have a documented default value or be flagged as mandatory |

## Verification Checklist

- [ ] `Technical_Specification.md` exists in `../output/` with all eight sections populated.
- [ ] Every LLD module has a corresponding contract with public interface, preconditions, and postconditions.
- [ ] Data format specifications include JSON schemas with typed fields and constraints.
- [ ] Integration specifications document request/response schemas with status codes.
- [ ] Configuration parameters list default values and valid ranges.
- [ ] Dependency matrix flags any circular dependencies.
- [ ] Traceability table maps every module contract to LLD modules and SRS requirement IDs.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 03 (02-low-level-design) | Consumes `LLD.md` module decomposition and class diagrams |
| Upstream | Phase 02 (Requirements Engineering) | Consumes `SRS_Draft.md` for requirement traceability |
| Downstream | 02-coding-guidelines | Informs coding patterns based on module contracts |
| Downstream | Phase 05 (Testing) | Feeds module contracts and integration specs for test derivation |

## Standards

- **IEEE 1016-2009** -- Software Design Descriptions. Governs module contract structure and design viewpoints.
- **IEEE 830-1998** -- Recommended Practice for Software Requirements Specifications. Ensures requirement traceability in the specification.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step technical specification generation logic.
- `README.md` -- Quick-start guide for this skill.
