## 4. API Versioning and Backward Compatibility

This section specifies the versioning strategy for the Mobile API. The versioning model ensures that mobile app releases on user devices — which cannot be force-upgraded — continue to function across server-side deployments.

### 4.1 Version Path Convention

**FR-MAPI-030:** The system shall expose all Mobile API endpoints under a version-prefixed URL path of the form `/api/mobile/v{N}/`, where `{N}` is a positive integer representing the major version. Examples: `/api/mobile/v1/`, `/api/mobile/v2/`.

- Test oracle: Assert that all endpoints documented in the Mobile API specification are accessible under `/api/mobile/v1/`; assert that a request to `/api/mobile/` without a version prefix returns HTTP 404.

**FR-MAPI-031:** The system shall support ≥ 2 active API versions simultaneously for a minimum deprecation window, so that clients on the previous version remain functional during migration.

- Test oracle: At any point when a new version `v{N+1}` is deployed, assert that `v{N}` endpoints respond correctly for all previously-documented requests.

### 4.2 Backward Compatibility Guarantee

**FR-MAPI-032:** The system shall not remove, rename, or change the data type of any response field in an existing versioned endpoint. Additive changes (new optional fields) are permitted without a version increment.

- Test oracle: Diff the response schema of any `v1` endpoint between two consecutive server releases; assert no fields have been removed or had their data types changed.

**FR-MAPI-033:** The system shall maintain a deprecated API version in an operational state for ≥ 90 days after the publication of its successor version before decommissioning it. The deprecation start date shall be recorded in the version discovery endpoint response.

- Test oracle: Deploy `v2`; assert `v1` continues to return correct responses for 90 days; assert the version discovery endpoint reports `v1` deprecation date = deployment date of `v2`.

### 4.3 Version Discovery Endpoint

**FR-MAPI-034:** The system shall expose a public, unauthenticated endpoint at `GET /api/mobile/versions` that returns a JSON array listing all supported API versions, their status (`active`, `deprecated`, `sunset`), and their scheduled sunset dates.

- Example response structure:

```json
{
  "versions": [
    {
      "version": "v1",
      "status": "deprecated",
      "deprecation_date": "2026-04-05",
      "sunset_date": "2026-07-04",
      "base_url": "/api/mobile/v1/"
    },
    {
      "version": "v2",
      "status": "active",
      "deprecation_date": null,
      "sunset_date": null,
      "base_url": "/api/mobile/v2/"
    }
  ]
}
```

- Test oracle: Call `GET /api/mobile/versions` without an Authorization header; assert HTTP 200 with a JSON body matching the schema above and containing at least 1 `active` version.

**FR-MAPI-035:** The system shall include a `Deprecation` response header and a `Sunset` response header on all responses from a deprecated API version, formatted per RFC 8594, to enable mobile clients to detect version transitions programmatically.

- Test oracle: Call any `v1` endpoint after `v2` is published; assert the response includes `Deprecation: <ISO-8601 date>` and `Sunset: <ISO-8601 date>` headers.
