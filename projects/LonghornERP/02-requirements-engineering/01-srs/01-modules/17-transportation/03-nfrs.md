# Non-Functional Requirements for the Transportation and Fleet Operations Module

## 3.1 Overview

Non-functional requirements (NFRs) define the quality and operating envelope within which all transport behaviour specified in Section 2 must operate. Each NFR is assigned a unique identifier in the `NFR-TMS-NNN` series and is stated with a specific, measurable metric.

## 3.2 Performance

**NFR-TMS-001:** Shipment-planning workbench queries, dispatch-dashboard refreshes, and transport analytics views shall meet the response-time thresholds stated in their respective functional requirements under normal load of up to 100 concurrent transportation users per tenant.

## 3.3 Availability and Continuity

**NFR-TMS-002:** Failure of telematics or location-ping ingestion shall not block manual trip progression, proof capture, or trip closure. The module shall continue to operate in manual mode with a visible warning that live location updates are unavailable.

## 3.4 Mobile and Offline Operation

**NFR-TMS-003:** Mobile proof capture and milestone updates shall support store-and-forward behaviour when connectivity is unavailable. Offline-captured events shall sync automatically within 60 seconds of connectivity restoration and shall preserve original event timestamps.

## 3.5 Auditability

**NFR-TMS-004:** Every transport-plan release, dispatch event, proof-capture action, trip-close action, settlement approval, and exception-owner reassignment shall generate an immutable Audit Log entry within 1 second of transaction commit.

## 3.6 Operational Safety Controls

**NFR-TMS-005:** The system shall prevent dispatch of internal vehicles whose maintenance or compliance availability state is `blocked`. Blocked-state evaluation shall include at minimum maintenance hold, expired insurance, and inactive vehicle status.

## 3.7 Graceful Degradation

**NFR-TMS-006:** If route-ETA calculations, telematics ingestion, or notification delivery are temporarily unavailable, the core shipment, dispatch, proof, and settlement workflows shall remain usable. The unavailable subsystem shall surface a clear warning state without corrupting transport records.
