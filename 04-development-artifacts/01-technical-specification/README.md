# 01-Technical-Specification Skill

## Objective

This skill produces a technical specification that bridges Low-Level Design modules to implementation-ready contracts with typed interfaces, data format schemas, and integration specifications. It serves as the primary developer reference for translating design into code per IEEE 1016-2009 and IEEE 830-1998.

## Execution Steps

1. Verify `../output/LLD.md`, `../output/SRS_Draft.md`, and `../project_context/tech_stack.md` exist. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill extracts module contracts, defines data formats and integration specs, and writes `../output/Technical_Specification.md`.
3. Review the traceability matrix to confirm every module contract maps to an LLD module and at least one SRS requirement ID.
4. Proceed to `02-coding-guidelines` and `03-dev-environment-setup` which can run in parallel once this skill completes.

## Quality Reminder

Every module contract shall define preconditions, postconditions, and exception types. Every JSON schema shall declare required and optional fields with type constraints. Every integration specification shall document both success and error response payloads. Flag specification gaps rather than fabricating implementation details.

## Standards

- IEEE 1016-2009 (Software Design Descriptions)
- IEEE 830-1998 (Software Requirements Specifications)
