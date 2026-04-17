---
project: Maduuka
document: UX Specification — Validation Checklist
version: 1.0
date: 2026-04-05
author: Peter Bamuhigire · Chwezi Core Systems
status: Draft
---

# UX Validation Checklist

## Design Covenant Validation Criteria

The following criteria are testable against every screen in the Maduuka UX specification. Each item is a pass/fail gate. Screens failing any criterion must be redesigned before the feature is accepted into build.

---

### DC-001: Mobile-First, Web-Equal

- [ ] Verify that every feature accessible on the Web application has a corresponding screen or flow on the Android application. Document any deliberate asymmetry (e.g., Custom Report Builder is Web-only by design) in a DC-001 Asymmetry Register.
- [ ] Confirm that every Android screen renders correctly on a 360 dp width viewport without horizontal scroll, clipped text, or overlapping elements.
- [ ] Confirm that every Web screen renders correctly at 1280 px, 992 px, and 768 px viewport widths without broken layouts or hidden primary actions.
- [ ] Ensure that the Android bottom tab bar provides access to the same top-level destinations as the Web sidebar, with no destination present on one platform but absent from the other (except documented exceptions).
- [ ] Verify that data created on Android (e.g., a sale, a stock movement) is visible on Web after sync, and vice versa.

---

### DC-002: Zero Mandatory Training

- [ ] Confirm that a first-time user who can use WhatsApp can complete a cash sale end-to-end (product selection → payment → receipt) in under 3 minutes without reading any documentation. Validate via observed usability test with a representative Agnes persona.
- [ ] Verify that every form field displays either a descriptive label above the field or a placeholder inside the field that explains the expected input in plain language. No field may have only a field name as its label (e.g., "Amount" alone without "Enter the expense amount in [currency]").
- [ ] Confirm that every error message describes both what went wrong and what the user must do to fix it. Error messages containing only a code (e.g., "Error 422") or a generic phrase ("Something went wrong") are a fail.
- [ ] Verify that the primary action on every screen (the action the user should take next to complete their task) is visually the most prominent element — largest, highest contrast, brand-colour fill. No screen may have two equal-prominence actions without clear visual differentiation.
- [ ] Confirm that no screen or feature requires knowledge of accounting terminology (e.g., "debit," "credit note," "GL posting") to complete a primary workflow. Accounting terms may appear in Grace (Accountant) screens but must not appear in Agnes (Cashier) screens.

---

### DC-003: Offline-First, Always

- [ ] Confirm that Agnes can complete a full cash sale — from product search to receipt print — with no internet connection. Test by disabling network access on a physical device and completing a sale.
- [ ] Verify that the offline indicator banner is visible on every screen when the device has no connectivity, and that it disappears automatically when connectivity is restored without requiring a user action.
- [ ] Confirm that stock levels, the product catalogue, and the active cart are readable and usable from local cache when offline. The data shown must be accompanied by a last-sync timestamp so the user knows the data currency.
- [ ] Verify that all offline-queued operations (sales, stock movements, expenses) sync in chronological order without duplicates upon connectivity restoration. Test with 10 offline sales followed by reconnection.
- [ ] Confirm that no critical action (POS sale, stock lookup, basic report view) shows an error or is blocked due to network unavailability.

---

### DC-004: Works on Cheapest Phone

- [ ] Verify that all screens render without frame drops below 60 fps on a reference device: 2 GB RAM Android running Android 10, 360 dp screen, Snapdragon 430-class CPU. Use Android GPU Profiler to confirm.
- [ ] Confirm that the product grid in the POS module renders 30 products without visible jank or list stutter on the reference device (use `LazyColumn` with `key` parameters to minimise recomposition).
- [ ] Verify that no screen requires more than 2 GB RAM to operate — confirm via Android Memory Profiler that peak heap usage for any screen stays below 150 MB.
- [ ] Confirm that animations (product add confirmation, tab transitions) are implemented with `AnimationSpec` that skips if `reduceMotion` is enabled or if the frame rate drops below 50 fps. No animation shall cause a visible freeze.
- [ ] Verify that all images in the product grid use appropriate resolution for the display density. Product thumbnails shall be ≤ 200 KB on disk (WebP format, loaded lazily via Coil).

---

### DC-005: Currency-Neutral

- [ ] Search every string resource file (Android `strings.xml`) and every PHP view template for hardcoded occurrences of "UGX," "Shs," or "Uganda Shilling." Zero occurrences are required. Any found occurrence is a fail.
- [ ] Confirm that changing the currency in Settings → Business Profile updates the currency symbol in the POS charge button, receipt preview, KPI cards, and all report totals within 1 navigation action (no app restart required).
- [ ] Verify that the currency symbol position (prefix or suffix) respects the configuration. Some currencies (e.g., USD) use prefix symbols; others (e.g., some African currencies) use suffix notation. The system shall support both.
- [ ] Confirm that currency amounts are formatted with the configured decimal separator and thousands separator. Example: 1,000,000.00 (English) vs 1.000.000,00 (some European locales). Test with at least 2 different locale configurations.

---

### DC-006: Compliance Built In

- [ ] Verify that every receipt — printed (80mm), PDF (A4), and digital (WhatsApp/SMS) — contains a visible EFRIS fiscal indicator area. When EFRIS is not active, the indicator shall display a placeholder (e.g., a greyed box labelled "EFRIS — Not Active") rather than being absent.
- [ ] Confirm that the Receipt Customisation screen (ST-02) includes the EFRIS fiscal indicator position setting (Top / Bottom), and that the setting is visible even when EFRIS is not activated.
- [ ] Verify that the business TIN field in the Business Profile (ST-01) is present and that the receipt includes the TIN when populated.
- [ ] Confirm that the tax rate configuration screen (ST-03) supports Uganda VAT rates (Standard 18%, Zero-Rated 0%, Exempt) as default categories, without these being the only categories (custom rates must also be addable).
- [ ] Verify that the EFRIS status indicator in the Web footer is visible on all Web screens, and that it correctly shows "EFRIS Ready" (grey placeholder) vs "EFRIS Active" (green) based on the system's EFRIS activation state.

---

## Heuristic Review Checklist

The following checklist applies Nielsen's 10 Usability Heuristics to Maduuka's specific context. Each item is evaluated per screen during design review.

---

### H-01: Visibility of System Status

- [ ] Ensure that after every user action (save, submit, void, approve), a feedback signal is visible within 200 ms — either a loading indicator, a success state, or an error. No action may complete silently.
- [ ] Verify that the POS Session status (open/closed, session owner, opening float) is visible from the POS Main Screen without requiring navigation. A session status badge in the POS top bar satisfies this requirement.
- [ ] Confirm that the sync status of offline-queued transactions is visible to Agnes without requiring her to navigate to a settings or status screen. A sync queue count shown on the offline banner satisfies this.

---

### H-02: Match Between System and the Real World

- [ ] Verify that terminology used in Agnes (Cashier) screens matches the language a Ugandan shopkeeper would use. "Sale" not "transaction." "Receipt" not "fiscal document." "Customer owes" not "outstanding receivable."
- [ ] Confirm that icons used without text labels are universally recognisable to the target user base (Ugandan SMB, WhatsApp-familiar). Conduct a 5-second icon recognition test with 3 representative users. Any icon with less than 80% correct identification must be replaced with a labelled button.
- [ ] Ensure that the receipt format mirrors a physical 80mm thermal receipt that Ugandan shopkeepers are familiar with — same structure (header, items list, totals, footer) rather than an unfamiliar digital format.

---

### H-03: User Control and Freedom

- [ ] Verify that every form screen (product entry, customer entry, staff profile) provides a clearly visible Cancel or Back option that discards changes without saving — reachable with a single tap.
- [ ] Confirm that the "Hold Sale" function allows Agnes to immediately revert to a clean cart for a new customer without losing the held cart. Held carts must be resumable at any point within the session.
- [ ] Ensure that any approved item (payroll, stock adjustment) has a documented reversal path. The reversal path does not need to be in the same screen, but it must exist and be accessible to authorised users.

---

### H-04: Consistency and Standards

- [ ] Verify that all primary action buttons across the application use the same visual style: brand-colour fill, white text, 56 dp height, 8 dp corner radius (Android) / 6 px (Web).
- [ ] Confirm that status badge colour semantics are consistent across all modules. Green = complete/positive, Amber = pending/warning, Red = error/critical. No module uses these colours for different meanings.
- [ ] Verify that the "Confirm" button in destructive confirmation dialogs always uses the red fill (#D32F2F) and is always on the right side of the dialog. The Cancel button is always on the left side (or top on stacked layouts).

---

### H-05: Error Prevention

- [ ] Confirm that the Credit Sale screen enforces the credit limit check (BR-002) before the "Approve Credit Sale" button becomes active — the user cannot submit a sale that would exceed the limit without an explicit manager PIN override.
- [ ] Verify that the Payroll Run screen prevents approval if any staff member in the run has a warning flag (missing NIN, incomplete salary structure). The approve button must be disabled until warnings are resolved or explicitly acknowledged.
- [ ] Ensure that the "Close POS Session" action requires entering the counted cash float before the confirm button activates, preventing accidental session closure without reconciliation.

---

### H-06: Recognition Over Recall

- [ ] Verify that the POS product grid is browsable by category without requiring the user to remember any product name or code. Agnes must be able to find a product by visual scanning of the category-filtered grid without typing.
- [ ] Confirm that the Payment Screen shows the full sale total prominently throughout the payment flow so Agnes never has to navigate back to check how much to collect.
- [ ] Ensure that the Payroll Run screen shows each staff member's previous month's net pay alongside the current computation so Amara can spot anomalies by comparison without opening a separate report.

---

### H-07: Flexibility and Efficiency of Use

- [ ] Verify that Grace (Accountant) can complete the bank reconciliation workflow for up to 200 transactions using only a keyboard on the Web application (Tab to navigate, Enter to confirm matches, arrow keys to select).
- [ ] Confirm that the POS search field supports partial name search, exact barcode scan, and SKU prefix search — three different lookup strategies that different users prefer.
- [ ] Ensure that scheduled reports (Screen R-04) eliminate the need for Grace to manually run the same report daily. Test: configure a daily sales summary report and confirm delivery at the scheduled time.

---

### H-08: Aesthetic and Minimalist Design

- [ ] Verify that no screen presents more than 7 primary data points or action buttons at the same time without a visual grouping mechanism (card, section header, or tab). Count data points and actions per screen during design review.
- [ ] Confirm that the Dashboard KPI cards on Android display exactly 4 KPIs in the first visible area (Today's Revenue, Transaction Count, Outstanding Credit, Cash Position). Additional metrics require scroll or tap-through. No KPI is hidden behind a settings screen.
- [ ] Ensure that confirmation dialogs contain no more than: a title, one sentence of consequence, a Cancel button, and a Confirm button. No additional instructional text, help links, or secondary options in the dialog.

---

### H-09: Help Users Recognise, Diagnose, and Recover from Errors

- [ ] Verify that every API error response results in a user-facing message that identifies the problem in plain language, not an HTTP status code or internal error code alone.
- [ ] Confirm that MoMo payment failure states (Screen 6) show the specific failure reason (declined, timed out, insufficient funds, network error) with a specific next step for each — not a generic "Payment failed" message.
- [ ] Ensure that the Three-Way Matching Review screen (S-04) identifies each discrepancy by line item and shows the delta value, not just a flag that "discrepancies exist." The user must be able to identify and resolve each discrepancy from a single screen.

---

### H-10: Help and Documentation

- [ ] Confirm that the POS module has a visible help icon (question mark, 24 dp) in the top bar that opens an in-app quick reference for keyboard shortcuts (Web) and barcode scanning tips (Android). This satisfies the zero-training requirement while providing a safety net.
- [ ] Verify that all error messages containing a technical constraint (e.g., "Barcode must be 8 or 13 digits") include the constraint value so the user knows the correct input — not just that their input was wrong.
- [ ] Ensure that the 2FA Setup flow (ST-06) includes a "Need help?" link on the QR code and verification steps, linking to a WhatsApp support contact or in-app FAQ — because 2FA is the highest-risk setup action for a non-technical user.
