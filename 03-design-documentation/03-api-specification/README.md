# 03-API-Specification Skill

## Objective

This skill produces a comprehensive API specification and a machine-readable OpenAPI 3.0 YAML artifact. It translates SRS functional requirements and HLD architectural decisions into a complete, implementation-ready API contract that development and testing teams consume directly.

## Execution Steps

1. Verify `../output/SRS_Draft.md`, `../output/HLD.md`, and `../project_context/tech_stack.md` exist. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill extracts API resources from SRS Section 3.2, maps operations to REST endpoints, defines authentication, error handling, rate limiting, and pagination.
3. Review the generated `../output/API_Specification.md` to confirm all SRS entities have corresponding endpoints with complete request/response schemas and status codes.
4. Validate that `../output/openapi.yaml` is a structurally valid OpenAPI 3.0 document containing every endpoint defined in the specification.

## Quality Reminder

Every endpoint shall specify authentication requirements, all applicable HTTP status codes, and request/response schemas. Every list endpoint shall include pagination. The traceability matrix shall map every endpoint back to its SRS requirement and HLD component. The `openapi.yaml` shall be valid OpenAPI 3.0 and match the human-readable specification exactly.

## Standards

- OpenAPI 3.0 (API Specification Format)
- IEEE 29148-2018 (Requirements Engineering)
- RFC 7231 (HTTP Semantics and Content)
