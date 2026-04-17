# Non-Functional Requirements for the AI Intelligence Module

## 4.1 Overview

Non-functional requirements (NFRs) define the quality and constraint envelope within which all functional behaviour specified in Section 3 must operate. Each NFR is assigned a unique identifier in the `NFR-AI-NNN` series and is stated with a specific, measurable metric per IEEE 982.1.

## 4.2 Performance

**NFR-AI-001:** All AI forecast jobs (FR-AI-001, FR-AI-003) shall complete within the time windows specified in their respective FRs. Jobs running beyond their window shall log a `job_timeout` event and notify the system administrator.

**NFR-AI-002:** Real-time AI responses (FR-AI-004 risk scoring, FR-AI-001 dashboard query) shall meet the response time thresholds specified in their respective FRs under normal load (≤ 100 concurrent users per tenant).

## 4.3 Accuracy

**NFR-AI-003:** The demand forecast (FR-AI-003) shall achieve a Mean Absolute Error (MAE) of ≤ 20% against actual weekly demand, measured monthly across all tenants with ≥ 180 days of history. Monthly accuracy reports shall be generated and reviewed by the Chwezi engineering team.

## 4.4 Data Privacy and Isolation

**NFR-AI-004:** All AI computation for FR-AI-001, FR-AI-002, FR-AI-003, and FR-AI-004 shall execute entirely within the tenant's data boundary. No tenant data shall be transmitted to external services for these features.

**NFR-AI-005:** For FR-AI-005 (narrative generation), financial summary data — aggregated amounts and variance percentages only, not individual transaction records — shall be transmitted to the Claude API. Transmission shall occur over TLS 1.3. Raw transaction data shall not leave the tenant boundary.

## 4.5 Graceful Degradation

**NFR-AI-006:** If an AI feature's scheduled job fails or the Claude API is unavailable, the core ERP modules shall continue to operate without interruption. The AI feature shall display a "Feature temporarily unavailable" message. Failed jobs shall be retried once after a 30-minute delay before logging a permanent failure.

## 4.6 Data Minimums

**NFR-AI-007:** Features requiring historical data shall display an "Insufficient history — [X] days of data required, [Y] days available" message rather than generating unreliable forecasts when the minimum data threshold has not been met.
