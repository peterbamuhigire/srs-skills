# Non-Functional Requirements for the Product Lifecycle Management Module

## 3.1 Overview

Non-functional requirements (NFRs) define the quality and control envelope within which all PLM behaviour specified in Section 2 must operate. Each NFR is assigned a unique identifier in the `NFR-PLM-NNN` series and is stated with a specific, measurable metric.

## 3.2 Performance

**NFR-PLM-001:** Revision-history retrieval, BOM-effectivity resolution, and NPI dashboard queries shall meet the response-time thresholds stated in their respective functional requirements under normal load of up to 50 concurrent PLM users per tenant.

## 3.3 Integrity and Concurrency

**NFR-PLM-002:** The module shall enforce optimistic or equivalent concurrency control so that 2 users cannot silently overwrite the same draft engineering object revision. A conflicting save attempt shall be rejected with a deterministic "record changed by another user" message.

## 3.4 Auditability

**NFR-PLM-003:** All state transitions involving revision status, ECR/ECO approval, release, supersession, effectivity change, and downstream publication shall generate immutable Audit Log entries within 1 second of transaction commit.

## 3.5 Access Control and Segregation of Duties

**NFR-PLM-004:** Release approval permissions shall be separable from authoring permissions. A tenant shall be able to configure roles such that the user who authors a change cannot be the only approver of that same change.

## 3.6 File Security and Retention

**NFR-PLM-005:** Controlled document files shall be stored with checksum verification and version retention. The system shall reject any uploaded file whose computed checksum differs from the stored checksum after write confirmation, and shall preserve all released document revisions for a minimum of 7 years unless a longer retention period is configured by the tenant.

## 3.7 Graceful Downstream Isolation

**NFR-PLM-006:** Failure of downstream publication to Inventory, Procurement, or Manufacturing shall not corrupt the released engineering record. The release shall remain traceable as released-but-not-published until publication succeeds or is administratively resolved.
