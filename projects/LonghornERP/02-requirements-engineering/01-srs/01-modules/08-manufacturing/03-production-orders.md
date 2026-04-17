# Production Orders

## 3.1 Production Order Creation

**FR-MFG-009** — When a user creates a production order, the system shall assign a unique identifier in the format `PRD-YYYY-NNNN`, link it to an active BOM version, capture: planned quantity, planned start date, planned completion date, and the production location (branch and warehouse zone).

**FR-MFG-010** — When a production order is created, the system shall auto-calculate the component requirements by multiplying the BOM gross quantities by the planned production quantity; the system shall display a material availability check showing available stock, reserved stock, and any shortfall for each component.

**FR-MFG-011** — When a component shortfall exists, the system shall allow the user to proceed with a partial production order covering available materials, or to raise a purchase requisition for the shortfall quantity and await stock before confirming the order.

## 3.2 Production Order Lifecycle

**FR-MFG-012** — A production order shall follow the status lifecycle: Draft → Released → In Progress → Quality Check → Completed or Rejected; the system shall enforce that each status transition is triggered by the appropriate action (e.g., raw material issue triggers "In Progress").

**FR-MFG-013** — When a production order is released, the system shall reserve the required component quantities in the Inventory module, preventing them from being allocated to other orders or sales picks.

**FR-MFG-014** — When a production order is cancelled, the system shall release all reservations, reverse any issued raw materials back to stock, and record the cancellation reason and acting user in the audit log.

## 3.3 Scheduling

**FR-MFG-015** — The system shall maintain a production schedule view showing all production orders on a calendar (day and week views), colour-coded by status; the schedule shall display machine and work-centre occupancy to assist production planners in avoiding resource conflicts.

**FR-MFG-016** — When two production orders are scheduled to use the same work centre in overlapping time windows, the system shall flag the conflict with a visual warning but shall not automatically resolve it; resolution is the planner's responsibility.
