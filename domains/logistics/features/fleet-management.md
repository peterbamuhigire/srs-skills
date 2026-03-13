# Feature: Fleet Management

## Description
Vehicle and driver lifecycle management — vehicle registration, maintenance
scheduling, driver qualification tracking, hours-of-service (HOS) compliance,
and ELD data management.

## Standard Capabilities
- Vehicle registration and asset profile (VIN, make, model, year, license plate, GVWR)
- Preventive maintenance scheduling (mileage-based and calendar-based)
- Vehicle inspection record management (pre-trip, post-trip, DVIR)
- Driver profile management (CDL class, endorsements, medical certificate expiry)
- Driver qualification file (DQF) maintenance per 49 CFR Part 391
- Hours-of-service (HOS) monitoring with ELD data ingestion
- HOS violation detection and automatic dispatch blocking
- Driver scorecard (safety events: hard braking, speeding, harsh acceleration)
- Fleet utilization and idle time reporting
- Vehicle out-of-service tracking and return-to-service workflow

## Regulatory Hooks
- DOT FMCSA 49 CFR Part 396: vehicle inspection records required; defects must be corrected before dispatch
- DOT FMCSA 49 CFR Part 391: driver qualification files must be maintained for active drivers + 3 years post-termination
- DOT FMCSA 49 CFR Part 395: HOS logs must be retained for 6 months; ELD data must be accessible to enforcement
- FMCSA Drug and Alcohol Clearinghouse: pre-employment and annual queries required

## Linked NFRs
- LOG-NFR-001 (Real-Time Tracking — GPS data feeds fleet telematics dashboard)
- LOG-NFR-003 (System Availability — HOS monitoring must be continuously available)
- LOG-NFR-004 (Data Retention — driver qualification records and HOS logs)
