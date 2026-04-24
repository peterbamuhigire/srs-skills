# Non-Functional Requirements - Supply Chain Planning

## 6.1 Performance

**NFR-SCP-001** - The demand-planning engine shall generate a baseline forecast for up to 50,000 item-location combinations over a 12-month horizon within <= 15 minutes under normal database load.

**NFR-SCP-002** - The supply-planning engine shall generate a feasible plan for up to 50,000 item-location combinations and 5 distribution or supply echelons within <= 20 minutes under normal database load.

**NFR-SCP-003** - Creating a planning scenario by cloning an existing approved plan version of up to 50,000 item-location combinations shall complete within <= 2 minutes.

## 6.2 Data Integrity and Operability

**NFR-SCP-004** - Planning input data replicated from execution modules shall be refreshed within <= 30 minutes of the latest committed source transaction, excluding upstream connector outages outside the platform boundary.

**NFR-SCP-005** - Releasing a plan version shall be idempotent; repeating the same release action due to retry or timeout shall not create duplicate downstream recommendation records or duplicate integration events.

**NFR-SCP-006** - Every released replenishment recommendation shall retain lineage to the originating demand-plan version, supply-plan version, and inventory-policy version for the full retention life of the record.

## 6.3 Availability and Security

**NFR-SCP-007** - The Supply Chain Planning module shall maintain 99.5% uptime measured monthly, excluding scheduled maintenance windows announced at least 24 hours in advance.

**NFR-SCP-008** - All planning endpoints, exports, and dashboards shall enforce tenant isolation and role-based access control such that no user can view or edit another tenant's plan data, scenarios, or released recommendations.
