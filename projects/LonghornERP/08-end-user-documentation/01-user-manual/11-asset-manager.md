# Asset Manager Guide

**Role:** Asset Manager

**Accessible modules:** Assets, Inventory (materials context), Procurement (request context)

---

## Registering a Functional Location

1. In the sidebar, click **Assets**, then click **Functional Locations**.
2. Click **New Functional Location**.
3. Enter the **Location Code** and **Location Name**.
4. Select the **Parent Location** if this is a child node.
5. Select the default **Criticality Class** if your tenant policy requires one.
6. Click **Save**.

---

## Screening a Work Request

1. Open **Assets > Work Requests**.
2. Click the request you want to review.
3. Check the reported asset, symptom, description, and any attached photo or meter evidence.
4. Review any duplicate-warning banner shown by the system.
5. Choose 1 action:
   - **Reject**
   - **Merge Into Existing Work Order**
   - **Convert to Work Order**
6. Enter the screening note and click **Submit Decision**.

---

## Planning and Scheduling a Work Order

1. Open **Assets > Work Orders** and select the work order.
2. Complete the planning fields:
   - **Tasks**
   - **Estimated Labour Hours**
   - **Required Skills**
   - **Required Materials**
   - **Permit Requirements**
   - **Target Window**
3. Click **Reserve Materials** to request inventory reservations.
4. Open **Assets > Scheduling Board**.
5. Drag the work order onto the target crew or technician row.
6. Resolve any capacity conflict shown by the system before saving the schedule.

---

## Reviewing a Condition Alert

1. Open **Assets > Condition Events**.
2. Filter for **Threshold Breached** events.
3. Review the event source, measurement value, and recommended action.
4. Choose 1 action:
   - **Monitor**
   - **Create Inspection**
   - **Create Corrective Work Order**
5. Save the decision so the event leaves the unreviewed queue.

---

## Closing a Work Order

1. Open the work order and click **Close Work Order**.
2. Enter the required closeout details:
   - **Failure Code**
   - **Cause Code**
   - **Remedy Code**
   - **Actual Labour Hours**
   - **Materials Used**
   - **Completion Notes**
3. Attach photos or completion evidence if required.
4. Click **Submit Closeout**.
5. Confirm that the work order status changes to **Completed** and that the closeout appears in the asset history timeline.
