---
title: "User Stories -- Dashboard and Settings (F-009, F-010)"
project: "Maduuka"
module: "Dashboard / Settings"
version: "1.0"
date: "2026-04-05"
---

# User Stories: Dashboard and Settings (F-009, F-010)

These stories express the dashboard and settings functional requirements from the perspective of two roles: Business Owner (Robert) and Platform Admin (Chwezi Core Systems).

---

## Dashboard and Business Health (F-009)

**US-DASH-001:** As a business owner, I want to check the dashboard on my morning commute so that I know yesterday's closing position before I arrive at the office.

**Acceptance Criteria:**

- Given the business owner opens the dashboard on the Android app, when the screen loads, then the system displays four KPI cards: Today's Revenue, Transaction Count, Outstanding Credit, and Cash Position, with the last sync timestamp.
- Given the app has no internet connection, then the dashboard displays cached KPI values from the last successful sync with the timestamp clearly marked.

**FR Reference:** FR-DASH-001

**Priority:** Must Have

---

**US-DASH-002:** As a business owner, I want to compare today's revenue to yesterday's so that I can quickly gauge whether today is performing above or below the prior day.

**Acceptance Criteria:**

- Given the business owner views the revenue comparison cards, when the dashboard loads, then the system displays today's revenue vs yesterday's revenue and this week's revenue vs last week's revenue.
- Given the comparison is displayed, then an up or down directional indicator and a percentage change figure are shown alongside each comparison.

**FR Reference:** FR-DASH-002

**Priority:** Must Have

---

**US-DASH-003:** As a business owner, I want to switch between branches on the dashboard so that I can view each branch's performance without logging in and out of separate accounts.

**Acceptance Criteria:**

- Given the business owner taps the branch switcher on the dashboard, when a branch is selected, then all KPI cards and the recent transactions list update to reflect the selected branch's data within 2 seconds.
- Given the business has only one branch, then the branch switcher is not displayed.

**FR Reference:** FR-DASH-006

**Priority:** Must Have

---

**US-DASH-004:** As a business owner, I want to see pending approvals on the dashboard so that I can action expense, leave, and stock adjustment requests without navigating to each module.

**Acceptance Criteria:**

- Given there are pending items requiring the current user's action, when the dashboard loads, then the system displays a pending approvals count badge and lists each pending item with a direct action link.
- Given there are no pending items, then the pending approvals section is not displayed.

**FR Reference:** FR-DASH-005

**Priority:** Must Have

---

**US-DASH-005:** As a business owner, I want the web dashboard to refresh automatically every 2 minutes so that I see up-to-date figures without manually reloading the page.

**Acceptance Criteria:**

- Given the business owner has the web dashboard open with an active internet connection, when 2 minutes elapse, then all KPI values refresh without a page reload.
- Given the dashboard is in a browser tab that is not in focus, then the auto-refresh continues in the background.

**FR Reference:** FR-DASH-003

**Priority:** Should Have

---

**US-DASH-006:** As a business owner, I want to see low-stock alerts on the dashboard so that I can initiate reorders before products run out.

**Acceptance Criteria:**

- Given any product is below its reorder level, when the dashboard loads, then the count of low-stock products is displayed as a badge.
- Given the business owner expands the low-stock panel, then the system lists each affected product with its current quantity and reorder level.

**FR Reference:** FR-DASH-004

**Priority:** Must Have

---

## Settings and Configuration (F-010)

**US-SET-001:** As a business owner, I want to set up two-factor authentication on my account so that no one can access the system using my credentials alone.

**Acceptance Criteria:**

- Given the business owner enables 2FA in settings, when 2FA is activated, then the system requires TOTP code entry (Google Authenticator compatible) on every login from an unrecognised device.
- Given the TOTP secret is stored, then it is stored server-side encrypted and never transmitted after initial setup.
- Given the business owner loses access to their authenticator app, then a recovery process is available.

**FR Reference:** FR-SET-011

**Priority:** Must Have

---

**US-SET-002:** As a platform admin, I want to provision a new tenant account so that a new business can begin using Maduuka immediately after subscribing.

**Acceptance Criteria:**

- Given a new subscription is confirmed, when the platform admin provisions the tenant, then the tenant's isolated data environment is created and the business owner receives login credentials.
- Given the tenant is provisioned, then the platform admin can view the tenant in the management console with subscription status, usage metrics, and last active date.

**FR Reference:** FR-SET-007 (subscription management context)

**Priority:** Must Have

---

**US-SET-003:** As a platform admin, I want to manage a tenant's subscription plan so that I can upgrade, downgrade, or cancel a subscription in response to a business request.

**Acceptance Criteria:**

- Given the platform admin selects a tenant and a new plan, when the plan change is confirmed, then the tenant's access limits (users, branches, products, storage) are updated immediately.
- Given a subscription is cancelled, then the tenant retains read-only access to their data until the end of the billing period.

**FR Reference:** FR-SET-007

**Priority:** Must Have

---

**US-SET-004:** As a business owner, I want to view all connected devices and revoke access for any device I do not recognise so that I can prevent unauthorised access if a device is lost or compromised.

**Acceptance Criteria:**

- Given the business owner opens the connected devices list, when the list loads, then it shows all devices with active sessions, including device name, last active date, and IP address.
- Given the business owner revokes a device, then the device's refresh token is immediately invalidated and the device is logged out on its next API request.

**FR Reference:** FR-SET-012

**Priority:** Must Have
