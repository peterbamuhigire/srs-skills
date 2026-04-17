## 8. Data-Lite Mode

This section specifies the data-lite mode capability. Mobile clients operating in low-bandwidth environments — common in rural Uganda and across much of sub-Saharan Africa — may request reduced-payload responses to minimise data transfer costs and improve perceived latency on 2G/3G connections.

### 8.1 Data-Lite Mode Activation

**FR-MAPI-090:** The system shall support a data-lite mode for all Mobile API responses, activated by the presence of the request header `X-Data-Lite: true`. When data-lite mode is active, the system shall omit non-essential fields from response payloads, reducing the response size by ≥ 40% compared to the full response for the same endpoint.

The definition of "non-essential" fields per endpoint shall be maintained in a server-side field exclusion registry (configurable JSON per endpoint). Non-essential fields include but are not limited to: audit metadata (`created_by_name`, `updated_by_name`), descriptive long-text fields not required for list views, base64-encoded attachments, and computed display fields redundant with primitive fields.

- Test oracle: Call any list endpoint without `X-Data-Lite: true`; record the response size in bytes. Call the same endpoint with `X-Data-Lite: true`; assert the second response is ≥ 40% smaller than the first. Assert all fields required to render the primary list view are present in the data-lite response.

### 8.2 Data-Lite Mode Behaviour Constraints

**FR-MAPI-091:** The system shall not omit fields that are required for the mobile client to perform its primary function (record creation, approval, sync) in data-lite mode. The field exclusion registry shall classify every field as `essential` or `non-essential`; only `non-essential` fields are removed.

- Test oracle: Call a list endpoint in data-lite mode; attempt to open a record detail view using the fields returned; assert no required identifier or status field is missing.

**FR-MAPI-092:** The system shall include the response header `X-Data-Lite: applied` on any response generated in data-lite mode, allowing the mobile client to confirm the mode was recognised and applied.

- Test oracle: Submit a request with `X-Data-Lite: true`; assert the response includes `X-Data-Lite: applied`; submit the same request without the header; assert the header is absent from the response.

**FR-MAPI-093:** The system shall apply data-lite mode at the serialisation layer, after all business logic, authorisation, and tenant isolation checks are complete. Data-lite mode shall not affect the completeness of audit log entries, which shall always record the full payload regardless of the request mode.

- Test oracle: Submit a data-lite create request; assert the audit log entry contains the full field set, not the reduced payload.
