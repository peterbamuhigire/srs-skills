# Clinic API

- `POST /patients` returns 201 on successful enrolment; payload validated per FR-001.
- `GET /appointments` returns 200 with available slots per FR-002.
- `POST /notes` returns 201 for clinical notes per FR-003.
- `POST /prescriptions` returns 201 per FR-004.
- `POST /invoices` returns 201 per FR-005 and FR-012.
- `POST /dsar` returns 202 per FR-008.

Latency target NFR-001 applies; throughput target NFR-007 applies.
