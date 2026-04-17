# Attendance

## 4.1 Attendance Capture

**FR-HR-019** — The system shall record daily attendance for each active employee with the following statuses: Present, Absent (Approved Leave), Absent (Unapproved), Public Holiday, or Rest Day.

**FR-HR-020** — The system shall support attendance capture via: (a) biometric device integration (time and attendance API — `[CONTEXT-GAP: GAP-009 — biometric device brand and API specification]`), (b) mobile clock-in/clock-out with GPS coordinate capture, and (c) manual entry by an HR administrator with a mandatory justification.

**FR-HR-021** — When an employee clocks in via the mobile application, the system shall record the GPS coordinates and compare them to the tenant's configured work location geofence (radius configurable, default 200 m); if the clock-in location falls outside the geofence, the system shall flag the record for supervisor review but shall not prevent the clock-in.

## 4.2 Shift Management

**FR-HR-022** — The system shall support configurable shift patterns, each defining: shift name, start time, end time, break duration (minutes), grace period for late arrival (minutes), and whether the shift qualifies for an overtime supplement.

**FR-HR-023** — When an employee works beyond the scheduled shift end time, the system shall compute overtime hours as: $OvertimeHours = ActualClockOut - ShiftEnd - BreakDuration$ and flag the record for approval by the line manager before payroll inclusion.

## 4.3 Attendance Reports

**FR-HR-024** — The system shall generate a monthly attendance summary per employee showing total present days, late arrivals, early departures, approved leave days, unapproved absent days, and overtime hours; this report shall be a prerequisite input to the payroll run.

**FR-HR-025** — The system shall generate a late-arrivals and absenteeism report per department, sortable by frequency, to support HR disciplinary workflows.
