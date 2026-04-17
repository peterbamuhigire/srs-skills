# Strategic Framework and BSC Perspective Configuration

## 2.1 Overview

The strategic framework defines the foundational elements of a tenant's strategy: the organisation's mission statement, vision statement, and strategic themes. These elements form the top tier of the strategic hierarchy above which BSC perspectives, objectives, KPIs, and initiatives are structured. Each tenant's strategic framework is fully isolated; no cross-tenant data is accessible.

## 2.2 Mission, Vision, and Strategic Theme Configuration

**FR-BSC-001:** The system shall allow a user holding the `strategy.admin` role to create or update the tenant's mission statement and vision statement, each stored as a free-text field with a maximum length of 1,000 characters; the system shall display the current mission and vision at the top of the scorecard dashboard.

**FR-BSC-002:** The system shall allow a `strategy.admin` user to create a strategic theme by supplying a theme name (free text, max 120 characters), a description (free text, max 500 characters), and a display colour (hex code); the system shall enforce uniqueness of theme names within the tenant.

**FR-BSC-003:** The system shall allow a `strategy.admin` user to edit the name, description, and colour of an existing strategic theme, and shall reject deletion of any theme that has at least 1 active strategic objective linked to it, returning a validation error listing the count of linked objectives.

**FR-BSC-004:** The system shall display the configured strategic themes as labelled, colour-coded groupings on the scorecard dashboard, allowing executive users to filter the scorecard view by strategic theme.

## 2.3 BSC Perspective Setup

**FR-BSC-005:** The system shall pre-populate every new BSC-enabled tenant with 4 default perspectives — Financial, Customer, Internal Process, and Learning & Growth — each assigned a default display order (1 through 4 respectively) when the BSC module is first activated for a tenant.

**FR-BSC-006:** The system shall allow a `strategy.admin` user to rename any default perspective, change its display order, and toggle its visibility; the system shall not allow deletion of a perspective that has at least 1 active strategic objective linked to it.

**FR-BSC-007:** The system shall allow a `strategy.admin` user to create a custom perspective by supplying a perspective name (free text, max 80 characters), description (free text, max 300 characters), and display order (positive integer); the system shall support a maximum of 8 active perspectives per tenant at any one time.

**FR-BSC-008:** When a tenant activates OKR mode (see Section 7.1), the system shall hide the BSC perspective layer from the scorecard dashboard and substitute the OKR hierarchy (Objective → Key Result) without deleting the underlying perspective configuration data, so that switching back to BSC mode restores all perspectives and their linked objectives intact.

## 2.4 Framework Mode Selection

**FR-BSC-009:** The system shall allow a `strategy.admin` user to set the tenant's active strategic framework to one of three modes: BSC, OKR, or Hybrid; in Hybrid mode, the system shall display both BSC perspectives and OKR hierarchies in separate tabs on the scorecard dashboard.

**FR-BSC-010:** The system shall record a timestamped audit log entry — capturing `user_id`, `action`, `from_mode`, `to_mode`, and `timestamp` — on every change to the tenant's active framework mode.
