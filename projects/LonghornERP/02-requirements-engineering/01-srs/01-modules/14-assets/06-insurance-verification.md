# Insurance Tracking and Physical Verification — Policy Records, Renewal Alerts, and Scan Workflow

## 6.1 Overview

Insurance tracking records the insurance coverage attached to each asset, ensuring that policies are renewed before expiry. Physical verification provides a structured scan-based workflow that confirms assets are present at their recorded locations, flags missing or misplaced assets, and generates a discrepancy report for management action.

## 6.2 Insurance Policy Tracking

**FR-ASSET-048:** When an authorised user creates an insurance record for an asset, the system shall record: asset identifier, insurer name, policy number (unique per tenant), policy type (Comprehensive, Third Party, Fire and Theft, All Risks, or custom), policy start date, policy expiry date, sum insured (numeric, > 0), annual premium, currency, and a file attachment slot for the policy document (PDF or image, ≤ 10 MB).

**FR-ASSET-049:** When an insurance record is saved and the expiry date is in the future, the system shall compute the days-to-expiry value daily via a scheduled background job and flag the record as *Expiring Soon* when days-to-expiry ≤ 30.

**FR-ASSET-050:** When an insurance record's status changes to *Expiring Soon*, the system shall send an in-app notification and an email notification to all users holding the *Asset Manager* role within the tenant, containing the asset number, asset description, policy number, insurer name, and expiry date; notification delivery shall occur within 24 hours of the daily expiry-check job run.

**FR-ASSET-051:** When an insurance record's expiry date is passed and no renewal has been recorded, the system shall set the policy status to *Expired* and flag the associated asset record with an *Insurance Expired* indicator visible on the asset detail screen and the asset list view.

**FR-ASSET-052:** When an authorised user renews an insurance policy, the system shall create a new insurance record linked to the same asset with the new policy details, set the previous record's status to *Superseded*, and clear the *Insurance Expired* flag from the asset master record if the new policy is active.

**FR-ASSET-053:** When an authorised user requests the Insurance Expiry Report, the system shall return a list of all asset insurance records with expiry date ≤ 90 days from the report date, sorted by days-to-expiry ascending, and support export to Excel (.xlsx) and PDF within ≤ 5 seconds at P95 for up to 1,000 policy records.

## 6.3 Physical Verification Workflow

**FR-ASSET-054:** When an authorised user initiates a physical verification session, the system shall create a verification session record with a unique session reference, the initiating user identity, start timestamp, scope (All Assets, By Category, By Location, or By Branch), and set the session status to *In Progress*.

**FR-ASSET-055:** When a user scans an asset QR or barcode tag during an active verification session, the system shall match the scanned code to the asset register, record the scan timestamp, scanned location (GPS coordinates if available, or manually entered location), and the scanning user, and mark the asset as *Verified* within the session.

**FR-ASSET-056:** When a scanned asset's recorded location in the asset register differs from the location entered by the user at the time of scan, the system shall mark the asset as *Location Mismatch* in the verification session and display a warning to the scanning user showing the registered location versus the scanned location.

**FR-ASSET-057:** When an authorised user closes a verification session, the system shall generate the Physical Verification Discrepancy Report listing: all assets within the session scope that were not scanned (*Missing*), all assets marked *Location Mismatch*, and all assets marked *Verified*, with counts and percentages for each category; the report shall be exportable to PDF and Excel and available within ≤ 10 seconds at P95 for a session scope of up to 5,000 assets.
