---
name: api-specification
description: Generate API specification with endpoint definitions, request/response schemas, authentication, error codes, and an OpenAPI 3.0 YAML artifact per IEEE 29148.
---

# API Specification Skill

## Overview

This skill generates comprehensive API documentation and a machine-readable OpenAPI 3.0 specification. It translates functional requirements from the SRS and architectural decisions from the HLD into a complete, implementation-ready API contract. The skill can run after 01-high-level-design completes and operates in parallel with 02-low-level-design and 04-database-design.

## When to Use

- After `01-high-level-design` has produced `HLD.md` in `../output/`, which identifies system components and integration points.
- When `SRS_Draft.md` Section 3.2 provides the functional requirements that map to API endpoints.
- When the team needs a formal API contract before backend development begins.

## Quick Reference

| Attribute     | Value                                                                 |
|---------------|-----------------------------------------------------------------------|
| **Inputs**    | `../output/SRS_Draft.md`, `../output/HLD.md`, `../project_context/tech_stack.md` |
| **Outputs**   | `../output/API_Specification.md`, `../output/openapi.yaml`           |
| **Tone**      | Technical, specification-grade, implementation-ready                  |
| **Standards** | OpenAPI 3.0, IEEE 29148-2018, RFC 7231                               |

## Input Files

| File           | Location                              | Required | Purpose                                         |
|----------------|---------------------------------------|----------|-------------------------------------------------|
| SRS_Draft.md   | `../output/SRS_Draft.md`              | Yes      | Functional requirements, security, performance  |
| HLD.md         | `../output/HLD.md`                    | Yes      | System components, integration points, data flow|
| tech_stack.md  | `../project_context/tech_stack.md`    | Yes      | Technology choices, framework conventions        |

## Output Files

| File                   | Location                              | Description                                      |
|------------------------|---------------------------------------|--------------------------------------------------|
| API_Specification.md   | `../output/API_Specification.md`      | Human-readable API reference with all sections   |
| openapi.yaml           | `../output/openapi.yaml`              | Machine-readable OpenAPI 3.0 specification       |

## Core Instructions

Follow these ten steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `SRS_Draft.md` and `HLD.md` from `../output/`, and `tech_stack.md` from `../project_context/`. Log every file path read. If any required file is missing, halt execution and report the gap.

### Step 2: Extract API Resources

Extract entities and operations from SRS Section 3.2 to identify API resources. Each entity that the system manages (e.g., User, Order, Product) becomes a resource. Each operation on that entity becomes an endpoint.

### Step 3: Map CRUD to HTTP Methods

Map CRUD operations to HTTP methods following REST conventions: Create = POST, Read = GET, Update (full) = PUT, Update (partial) = PATCH, Delete = DELETE. Use HLD component boundaries to determine resource grouping and URL namespace.

### Step 4: Define Authentication Scheme

Extract the authentication mechanism from SRS Section 3.5.3 (Security Requirements). Define the scheme as one of: JWT Bearer Token, Session Cookies, or API Key. Reference `skills/dual-auth-rbac/` if the project uses role-based access control with multiple authentication strategies.

### Step 5: Define Endpoint Details

For each endpoint, specify: path (RESTful URL), HTTP method, description, path parameters with data types, query parameters with defaults, request body schema (JSON with field types and constraints), response schema (JSON with field types), and HTTP status codes (200, 201, 400, 401, 403, 404, 422, 500).

### Step 6: Define Error Response Format

Define a standardized error response format for all endpoints. Reference `skills/api-error-handling/` for the canonical pattern:

```json
{
  "success": false,
  "error": {
    "code": "string",
    "message": "string",
    "details": []
  }
}
```

Every error status code shall return this structure.

### Step 7: Define Rate Limiting

Extract performance constraints from SRS Section 3.3 (Performance Requirements). Define rate limits per endpoint tier: public endpoints, authenticated endpoints, and administrative endpoints. Specify the rate limit headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`.

### Step 8: Define Pagination

Define pagination strategy for all list endpoints: cursor-based or offset-based depending on data characteristics. Include standard parameters `page`, `per_page` and response envelope `total`, `data[]`. Reference `skills/api-pagination/` if available.

### Step 9: Generate API_Specification.md

Write the human-readable specification to `../output/API_Specification.md` with all sections defined in the Output Format below.

### Step 10: Generate openapi.yaml

Generate a valid OpenAPI 3.0 document at `../output/openapi.yaml`. The document shall include: `openapi: "3.0.3"`, `info` block, `servers` block, `paths` with all endpoints, `components/schemas` with all request/response models, and `components/securitySchemes` with the authentication definition.

## Output Format

The generated `API_Specification.md` shall follow this template structure:

```
# API Specification: [Project Name]

## Document Header
## 1. API Overview
### 1.1 Base URL and Versioning
### 1.2 Content Types
### 1.3 Common Headers
## 2. Authentication and Authorization
### 2.1 Authentication Scheme
### 2.2 Authorization Model
### 2.3 Token Lifecycle
## 3. Endpoint Reference
### 3.x [Resource Name]
#### 3.x.1 [METHOD] /api/v1/resource
## 4. Request and Response Schemas
### 4.1 Common Models
### 4.2 Resource-Specific Models
## 5. Error Response Format
### 5.1 Standard Error Envelope
### 5.2 Error Code Registry
## 6. Rate Limiting
## 7. Pagination
## 8. Versioning Strategy
## 9. CORS and Security Headers
## 10. Traceability Matrix
```

Section 10 (Traceability Matrix) shall map each endpoint to its originating SRS requirement ID and the HLD component that owns it.

## Common Pitfalls

1. **Missing error codes**: Every endpoint shall document all possible HTTP status codes, not just the success case.
2. **Unprotected routes**: Every non-public endpoint shall specify its authentication and authorization requirements.
3. **Inconsistent naming**: Use consistent casing (snake_case or camelCase) and pluralization across all endpoints and schema fields.
4. **No pagination on list endpoints**: Every endpoint that returns a collection shall include pagination parameters and metadata.
5. **Missing request validation**: Document required fields, data types, and constraints for every request body.

## Verification Checklist

- [ ] All required input files were read and logged.
- [ ] Every entity in SRS Section 3.2 maps to at least one API resource with CRUD endpoints.
- [ ] Every endpoint specifies authentication requirements, request/response schemas, and all applicable status codes.
- [ ] The error response format is consistent across all endpoints.
- [ ] List endpoints include pagination parameters and response metadata.
- [ ] The `openapi.yaml` file is valid OpenAPI 3.0 and contains all endpoints defined in `API_Specification.md`.

## Integration

| Direction  | Skill                                        | Relationship                                       |
|------------|----------------------------------------------|----------------------------------------------------|
| Upstream   | `03-design-documentation/01-high-level-design` | Consumes HLD.md for component boundaries          |
| Upstream   | `02-requirements-engineering`                | Consumes SRS_Draft.md for functional requirements  |
| Downstream | Phase 04 (Development)                       | API contract drives backend implementation         |
| Downstream | Phase 05 (Testing)                           | Endpoint definitions drive API test cases          |
| Reference  | `skills/api-error-handling/`                 | Canonical error response patterns                  |
| Reference  | `skills/api-pagination/`                     | Pagination strategy patterns                       |
| Reference  | `skills/dual-auth-rbac/`                     | Authentication and RBAC patterns                   |

## Standards

- **OpenAPI 3.0**: The OpenAPI Specification defines a standard, language-agnostic interface to HTTP APIs. Governs the structure of `openapi.yaml`.
- **IEEE 29148-2018**: Systems and software engineering -- Life cycle processes -- Requirements engineering. Ensures traceability from requirements to API endpoints.
- **RFC 7231**: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content. Defines HTTP method semantics and status code meanings.

## Resources

- `logic.prompt` -- executable prompt for automated API specification generation.
- `README.md` -- quick-start guide for this skill.
