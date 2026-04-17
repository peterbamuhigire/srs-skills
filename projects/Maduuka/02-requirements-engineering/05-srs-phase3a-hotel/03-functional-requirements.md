# 3. Functional Requirements

All functional requirements follow the IEEE 830 stimulus-response pattern: "When [stimulus], the system shall [response]." Each requirement carries a unique identifier in the series FR-HTL-001 through FR-HTL-112.

---

## 3.1 Property Setup (FR-HTL-001 to FR-HTL-015)

**FR-HTL-001** — When a Business Owner creates a new property, the system shall record: property name, physical address, star rating (1–5 stars or unrated), total room count, standard check-in time, and standard check-out time.

**FR-HTL-002** — When a Business Owner saves a property profile, the system shall validate that property name is non-empty and standard check-in time is earlier than standard check-out time; the system shall reject the record and display a field-level error if either condition is not met.

**FR-HTL-003** — When a Business Owner creates a room type, the system shall record: room type name, capacity (maximum guests), floor assignment (optional), description, nightly rate (UGX), hourly rate (UGX), and a configurable amenities list (free-text tags).

**FR-HTL-004** — When a Business Owner edits a room type's default rate, the system shall apply the new rate to all future check-ins of that room type; existing open folios shall retain the rate that was active at check-in.

**FR-HTL-005** — When a Business Owner creates an individual room record, the system shall record: room number (unique per property), room type (foreign key to room type), floor, initial status (default: Available), and optional notes.

**FR-HTL-006** — When a Business Owner attempts to save an individual room with a room number that already exists for the same property, the system shall reject the record and display the error: "Room number [X] already exists for this property."

**FR-HTL-007** — When a Business Owner edits an individual room's room type, the system shall update the room's future billing defaults; any open folio for that room shall retain its originally assigned room type rates.

**FR-HTL-008** — When a Business Owner creates a seasonal pricing rule, the system shall record: a label (e.g., "High Season 2026"), a start date, an end date, a price override (nightly rate and/or hourly rate), and the room type(s) to which the rule applies.

**FR-HTL-009** — When a guest check-in date falls within an active seasonal pricing rule for the assigned room type, the system shall apply the seasonal rate to the folio instead of the room type default rate; the rate source (seasonal rule name) shall be displayed on the folio.

**FR-HTL-010** — When two seasonal pricing rules overlap for the same room type and date range, the system shall apply the rule with the later creation date and shall display a warning to the Business Owner on the seasonal pricing management screen.

**FR-HTL-011** — When a Business Owner creates a conference room, the system shall record it as a distinct room type with: a conference-specific flag, hourly rate (UGX), seated capacity, and AV equipment list (free-text, multi-item).

**FR-HTL-012** — When a Business Owner deactivates a room type, the system shall prevent new reservations from being assigned to that type but shall not affect open reservations or folios referencing it.

**FR-HTL-013** — When a Business Owner deactivates an individual room, the system shall set its status to Out of Order and prevent new reservations from being assigned to it.

**FR-HTL-014** — When a Business Owner views the property setup screen, the system shall display a summary count of rooms by status (Available, Occupied, Reserved, Cleaning, Maintenance, Out of Order).

**FR-HTL-015** — When a Business Owner exports the room type list, the system shall generate a CSV file containing all room type fields including current default rates.

---

## 3.2 Room Status Board (FR-HTL-016 to FR-HTL-025)

**FR-HTL-016** — When a staff member opens the room status board, the system shall render a grid view of all rooms for the selected property, each cell displaying: room number, room type name, current status, and (if occupied) the guest name and expected checkout date.

**FR-HTL-017** — When the status of any room changes (by any user on any connected client), the system shall propagate the updated status to all connected clients displaying the room status board within 2 seconds. *This requirement applies to properties with up to 200 rooms under normal load.*

**FR-HTL-018** — When the room status board is rendered, the system shall colour-code each room cell using the following scheme: Available — green; Occupied — red; Reserved — amber; Cleaning — blue; Maintenance — orange; Out of Order — grey.

**FR-HTL-019** — When a staff member performs a check-in, the system shall automatically transition the assigned room's status from Available (or Reserved) to Occupied.

**FR-HTL-020** — When a staff member processes a checkout, the system shall automatically transition the room's status from Occupied to Cleaning.

**FR-HTL-021** — When a Housekeeping Staff member marks a room as clean, the system shall transition the room's status from Cleaning to Available.

**FR-HTL-022** — When any staff member flags a room for maintenance, the system shall transition the room's status to Maintenance from Available or Cleaning only; the system shall prevent a maintenance flag on a room with status Occupied or Reserved and shall display the error: "Room [X] is currently [status] and cannot be flagged for maintenance."

**FR-HTL-023** — When a Business Owner sets a room to Out of Order, the system shall transition the room's status to Out of Order from any current status and shall prevent any new reservation or check-in assignment to that room until the status is cleared.

**FR-HTL-024** — When a Housekeeping Staff member opens the housekeeping dashboard, the system shall display a list of all rooms with status Cleaning, showing: room number, floor, room type, time since checkout, and assigned housekeeper (if any).

**FR-HTL-025** — When a Business Owner or Front Desk Staff assigns a housekeeper to a room task, the system shall record the assignment and notify the assigned Housekeeping Staff member via in-app notification.

---

## 3.3 Reservations (FR-HTL-026 to FR-HTL-045)

**FR-HTL-026** — When a staff member initiates a new reservation, the system shall require: room type, requested check-in date, requested check-out date, guest full name, guest phone number, ID type (National ID / Passport / Driving Permit), ID number, billing mode (Nightly or Hourly), booking source (`walk-in` or `phone`; [CONTEXT-GAP: GAP-007 — channel manager source values deferred to Phase 4]), and deposit amount (may be zero).

**FR-HTL-027** — When a reservation is submitted, the system shall query the room inventory for rooms of the requested type that have status Available for the entire requested date range and shall return the count of available rooms before allowing room assignment.

**FR-HTL-028** — When the availability check (FR-HTL-027) returns zero available rooms for the requested room type and dates, the system shall block reservation creation and display: "No rooms of type [X] are available from [date] to [date]."

**FR-HTL-029** — When a staff member assigns a specific room to a reservation, the system shall enforce BR-015: if the room is already assigned to any active reservation or open check-in with any overlapping date range, the system shall block the assignment and display: "Room [X] is already reserved from [date] to [date]."

**FR-HTL-030** — When BR-015 enforcement (FR-HTL-029) is implemented, the double-booking check shall be executed as a database-level constraint (unique partial index on room_id, overlapping date range, active status) in addition to the UI validation layer.

**FR-HTL-031** — When a reservation is saved, the system shall assign a unique reservation reference number and record a creation timestamp and the staff member who created it.

**FR-HTL-032** — When a reservation is saved and the guest phone number is provided, the system shall send an SMS confirmation to the guest via Africa's Talking containing: reservation reference number, property name, room type, check-in date, and check-out date.

**FR-HTL-033** — When the Africa's Talking SMS gateway returns an error, the system shall record the failed SMS in a retry queue and shall not block reservation creation.

**FR-HTL-034** — When a staff member opens the reservation calendar view, the system shall render a month or week view (user-selectable) showing all active reservations per room as coloured bars spanning the reserved date range, displaying guest name and reservation reference on each bar.

**FR-HTL-035** — When a staff member modifies a reservation's dates or room type, the system shall re-execute the availability check (FR-HTL-027) and the double-booking check (FR-HTL-029) against the new values before saving.

**FR-HTL-036** — When a staff member modifies a reservation's deposit amount, the system shall record the change in the audit log (BR-003) with the previous value, new value, staff member, and timestamp.

**FR-HTL-037** — When a staff member cancels a reservation, the system shall require a cancellation reason (free-text, mandatory), record the refund policy applied (configurable: full refund / partial refund / no refund), and update the room's availability to remove the reservation block.

**FR-HTL-038** — When a reservation is cancelled, the system shall record the deposit handling action (refunded / forfeited / partially refunded) and the amount; this record is appended to the audit log (BR-003).

**FR-HTL-039** — When a staff member creates a group booking, the system shall link 2 or more individual room reservations under a single group reference number, recording: group name, lead guest name, lead guest phone, and total room count.

**FR-HTL-040** — When a group booking is created, the system shall apply FR-HTL-029 (BR-015) independently to each room in the group; if any room fails the double-booking check, the system shall block the entire group booking and list all conflicting rooms.

**FR-HTL-041** — When a staff member searches reservations, the system shall support search by: reservation reference number, guest name (partial match), guest phone number, check-in date range, and room number.

**FR-HTL-042** — When a staff member views a reservation detail, the system shall display the full reservation record including: booking source, billing mode, assigned room (if confirmed), deposit paid, and all modification history.

**FR-HTL-043** — When a reservation's check-in date passes without a check-in event, the system shall mark the reservation status as "No-Show" and release the room to Available status; a Business Owner or Front Desk Staff member may manually override the no-show designation.

**FR-HTL-044** — When a staff member sets a reservation to No-Show, the system shall record the deposit handling action per the property's configured no-show policy.

**FR-HTL-045** — When a staff member exports the reservation list for a date range, the system shall generate a CSV file including: reservation reference, guest name, room number, room type, check-in date, check-out date, billing mode, booking source, deposit, and reservation status.

---

## 3.4 Check-In (FR-HTL-046 to FR-HTL-060)

**FR-HTL-046** — When a staff member initiates check-in against an existing reservation, the system shall pre-populate the check-in form with: guest name, phone, ID type/number, room type, reserved dates, billing mode, and deposit amount from the reservation record.

**FR-HTL-047** — When a staff member initiates a walk-in check-in (no prior reservation), the system shall present the same check-in form without pre-population and execute the availability check (FR-HTL-027) and double-booking check (FR-HTL-029) before confirming room assignment.

**FR-HTL-048** — When a staff member completes the check-in form, the system shall require: guest full name, guest phone, ID type, ID number, room assignment, billing mode confirmation, and payment of or waiver of deposit; the system shall block check-in submission if any mandatory field is absent.

**FR-HTL-049** — When a staff member attaches a guest ID document (scan or photo), the system shall store the image against the guest folio record in the tenant's cloud storage and record the filename, upload timestamp, and uploading staff member in the audit log (BR-003).

**FR-HTL-050** — When the check-in form displays the billing mode selection (BR-016), the system shall present the selection as a prominent, labelled control (Nightly / Hourly) and require explicit staff confirmation before saving; the confirmed billing mode shall be displayed on all subsequent folio screens.

**FR-HTL-051** — When billing mode Hourly is selected at check-in, the system shall record the check-in timestamp to the nearest minute and display it on the folio header.

**FR-HTL-052** — When billing mode Nightly is selected at check-in, the system shall record the check-in date and the expected check-out date; the nightly charge is calculated on checkout from the number of nights (FR-HTL-063).

**FR-HTL-053** — When a staff member attempts to check in a guest to a room that has status Cleaning, the system shall display a warning: "Room [X] has not been marked clean. Proceed?" and require a manager-level approval to override.

**FR-HTL-054** — When a manager approves an early check-in override (FR-HTL-053), the system shall record the approving manager's user ID, the override reason, and the timestamp in the audit log (BR-003).

**FR-HTL-055** — When a deposit is collected at check-in, the system shall record: deposit amount (UGX), payment method (from the F-006 payment account list), and posting timestamp; the deposit shall appear on the folio as a credit entry.

**FR-HTL-056** — When a deposit is waived at check-in, the system shall record the waiver with a mandatory reason code and the staff member's user ID.

**FR-HTL-057** — When check-in is confirmed, the system shall generate a room key record containing: room number, guest name, check-in timestamp, and expected checkout date/time; this record is printable as a key card slip (A6 PDF or thermal receipt format).

**FR-HTL-058** — When check-in is confirmed, the system shall transition the room status to Occupied (FR-HTL-019) and create an open folio for the stay.

**FR-HTL-059** — When a group check-in is processed (linked to a group booking), the system shall allow individual rooms within the group to be checked in sequentially or simultaneously; each room generates its own folio linked to the group reference.

**FR-HTL-060** — When check-in is confirmed, the system shall record the staff member who processed the check-in and timestamp in the folio header for audit purposes (BR-003).

---

## 3.5 Room Folios and Charge Posting (FR-HTL-061 to FR-HTL-075)

**FR-HTL-061** — When a folio is created at check-in, the system shall display a running account showing: all charge line items (description, quantity, unit rate, amount), all credit entries (deposits, payments), and a running balance (total charges minus total credits).

**FR-HTL-062** — When a folio is viewed by Front Desk Staff or a Business Owner, the system shall display the current running balance in real time, reflecting all charges posted since check-in.

**FR-HTL-063** — When a guest checks out under Nightly billing mode, the system shall calculate the accommodation charge as:

$$Charge_{nightly} = Nights \times NightlyRate$$

where *Nights* is the count of calendar nights from check-in date to check-out date, and *NightlyRate* is the rate active at check-in (seasonal override applied per FR-HTL-009).

**FR-HTL-064** — When a guest checks out under Hourly billing mode, the system shall calculate the accommodation charge as:

$$Charge_{hourly} = \lceil HoursOccupied \rceil \times HourlyRate$$

where *HoursOccupied* is the duration in decimal hours from check-in timestamp (FR-HTL-051) to checkout timestamp (recorded to the nearest minute), and *HourlyRate* is the rate active at check-in. The ceiling function rounds up any fractional hour to the next whole hour.

**FR-HTL-065** — When FR-HTL-064 is executed, the system shall display the intermediate calculation (check-in time, checkout time, raw duration in hours and minutes, rounded hours, rate, total) on the checkout confirmation screen so the staff member can verify the computation before finalising.

**FR-HTL-066** — When any staff member posts an additional charge to an occupied room's folio, the system shall record: charge description, category (F&B / Laundry / Conference / Minibar / Other), amount (UGX), posting timestamp, and posting staff member.

**FR-HTL-067** — When F-011 (Restaurant/Bar) is active and a table order is settled by "Post to Room," the system shall post the itemised bill total to the specified room's folio as a single F&B charge line item, referencing the originating order number.

**FR-HTL-068** — When a laundry charge is posted to a folio, the system shall record: item description, quantity, unit price, and total amount.

**FR-HTL-069** — When a conference room hire charge is posted to a folio, the system shall reference the conference booking record (FR-HTL-098) and display the conference room name, date, duration, and computed charge on the folio line item.

**FR-HTL-070** — When a Business Owner or Front Desk Staff member views a folio, the system shall display all line items in chronological order of posting, with the most recent at the bottom.

**FR-HTL-071** — When a manager applies a folio discount, the system shall record: discount amount (UGX) or percentage, reason code (mandatory, free-text), manager user ID, and timestamp; the discount appears as a negative line item on the folio.

**FR-HTL-072** — When a manager removes a charge from a folio, the system shall not delete the original charge record; instead, the system shall post a reversal entry of equal and opposite value, recording the reason code, manager user ID, and timestamp (BR-003).

**FR-HTL-073** — When a folio contains a reversal entry (FR-HTL-072), the original charge and the reversal shall both remain visible on the folio with their respective timestamps, with the reversal clearly labelled "Reversal of [original charge description]."

**FR-HTL-074** — When a staff member views the folio during an active stay, the system shall display the projected accommodation charge (using the current billing mode formula) based on the current time, clearly labelled as "Estimated — subject to change at checkout."

**FR-HTL-075** — When a Business Owner exports a folio to PDF, the system shall generate an itemised document showing: property name and address, guest name, room number, check-in date/time, checkout date/time, all folio line items, total charges, total credits, and net amount due.

---

## 3.6 Check-Out (FR-HTL-076 to FR-HTL-088)

**FR-HTL-076** — When a staff member initiates check-out for an occupied room, the system shall display the complete folio (FR-HTL-061), the calculated accommodation charge (FR-HTL-063 or FR-HTL-064 depending on billing mode), all posted additional charges, total credits (deposits), and the net amount due.

**FR-HTL-077** — When the net amount due at checkout is zero (deposits equal or exceed total charges), the system shall allow checkout to proceed without collecting further payment and shall display a clear zero-balance confirmation.

**FR-HTL-078** — When the net amount due at checkout is greater than zero, the system shall require full payment settlement before completing checkout; the staff member selects one or more payment methods from the F-006 payment account list.

**FR-HTL-079** — When checkout payment is split across multiple payment methods (BR-010), the system shall record each payment component separately against its respective payment account; the sum of all components must equal the net amount due.

**FR-HTL-080** — When checkout is finalised, the system shall generate an itemised tax invoice / receipt as a PDF, containing: invoice number, property name and address, guest name, room number, billing mode, check-in and checkout timestamps, all folio line items with amounts, total charges, credits, and amount paid per payment method.

**FR-HTL-081** — When a guest requests an early checkout, the system shall recalculate the accommodation charge from the actual checkout timestamp; for Hourly billing, FR-HTL-064 applies to the shorter duration; for Nightly billing, the charge is for the actual nights occupied (not the originally reserved nights).

**FR-HTL-082** — When a guest remains past the standard checkout time configured for the property (FR-HTL-001), the system shall calculate and display a late checkout fee; the fee amount and grace period are configurable per property by the Business Owner.

**FR-HTL-083** — When a late checkout fee is applied, the system shall post it as a separate line item on the folio with the description "Late Checkout Fee" and the minutes/hours overrun.

**FR-HTL-084** — When checkout is finalised, the system shall transition the room status from Occupied to Cleaning (FR-HTL-020) and close the folio; no further charges may be posted to a closed folio.

**FR-HTL-085** — When a manager attempts to post a charge to a closed folio, the system shall block the action and display: "This folio was closed on [date/time]. Create a supplementary invoice to add charges."

**FR-HTL-086** — When checkout is finalised, the system shall record the checkout timestamp (to the nearest minute), the staff member who processed checkout, and all payment transaction references in the audit log (BR-003).

**FR-HTL-087** — When a group checkout is processed (linked group reservation), the system shall allow individual rooms to be checked out separately; a group checkout summary report shall be generated listing all rooms, individual folio totals, and the group aggregate total.

**FR-HTL-088** — When a staff member exports the checkout receipt as PDF on iOS, the system shall generate the document using PDFKit on-device; on Web, the system shall generate it server-side using an HTML-to-PDF renderer.

---

## 3.7 Corporate Accounts (FR-HTL-089 to FR-HTL-095)

**FR-HTL-089** — When a Business Owner creates a corporate account, the system shall record: company name, primary contact name and phone, credit limit (UGX), billing address, payment terms (e.g., 30 days net), and an active/inactive flag.

**FR-HTL-090** — When a guest folio is linked to a corporate account at check-in, the system shall mark the folio for direct billing; at checkout, instead of collecting payment from the guest, the system shall post the net amount due to the corporate account's running balance.

**FR-HTL-091** — When a corporate account's running balance would exceed its configured credit limit after posting a checkout folio, the system shall display a warning to the Front Desk Staff and require Business Owner approval to proceed with direct billing.

**FR-HTL-092** — When a Business Owner generates a corporate invoice, the system shall produce an itemised PDF invoice covering all folios billed to the account within a specified date range, showing: invoice number, company name and billing address, each stay (guest name, room, dates, total), subtotal, and grand total.

**FR-HTL-093** — When a payment is received against a corporate account, the system shall record: amount, payment date, payment method, reference number, and the staff member who recorded it; the corporate account balance shall decrease by the payment amount.

**FR-HTL-094** — When a Business Owner views a corporate account statement, the system shall display a chronological list of all folio postings and payments, with a running balance after each entry.

**FR-HTL-095** — When a Business Owner exports a corporate account statement, the system shall generate a CSV and PDF version covering the selected date range.

---

## 3.8 Conference Room Booking (FR-HTL-096 to FR-HTL-103)

**FR-HTL-096** — When a staff member creates a conference room booking, the system shall record: conference room (selected from rooms with the conference flag, FR-HTL-011), booking date, start time, end time, client name, client phone, setup type (Boardroom / Theatre / Classroom / Custom), and AV equipment required (multi-select from the room's AV equipment list).

**FR-HTL-097** — When a conference room booking is submitted, the system shall execute a double-booking check equivalent to BR-015 for the conference room's time range: if the room is already booked for any overlapping time period on the same date, the system shall block the booking and display the conflicting booking's reference and time range.

**FR-HTL-098** — When a conference room booking is confirmed, the system shall calculate the indicative charge as:

$$Charge_{conference} = HoursBooked \times ConferenceHourlyRate$$

where *HoursBooked* is the duration from start time to end time (fractional hours rounded up to the next whole hour), and *ConferenceHourlyRate* is the rate defined on the conference room type (FR-HTL-011).

**FR-HTL-099** — When a conference room booking is completed (end time passed), the system shall allow the charge to be posted to: a guest folio (if the client is a staying guest), a corporate account, or a standalone invoice for walk-in conference clients.

**FR-HTL-100** — When a staff member views the conference room calendar, the system shall display a day view and week view of all conference bookings per conference room, with booking reference, client name, setup type, and time block displayed in each slot.

**FR-HTL-101** — When a conference room booking is cancelled, the system shall record the cancellation reason, release the time slot, and note any deposit or cancellation fee handling in the audit log (BR-003).

**FR-HTL-102** — When a standalone conference invoice is generated (FR-HTL-099, non-resident client), the system shall produce a PDF invoice showing: conference room name, date, start/end time, hours billed, rate, total amount, and payment status.

**FR-HTL-103** — When a staff member exports the conference booking list for a date range, the system shall generate a CSV file including: booking reference, conference room, client name, date, start time, end time, hours booked, computed charge, and payment status.

---

## 3.9 Occupancy Analytics (FR-HTL-104 to FR-HTL-112)

**FR-HTL-104** — When a Business Owner views the occupancy analytics dashboard, the system shall display the following metrics for a user-selected date range: occupancy rate, RevPAR, ADR, and average length of stay.

**FR-HTL-105** — When computing occupancy rate for a date range, the system shall calculate:

$$OccupancyRate = \frac{RoomsSold}{AvailableRooms} \times 100\%$$

where *RoomsSold* is the count of distinct room-nights where a room was occupied, and *AvailableRooms* is the count of room-nights where a room was in Available, Occupied, or Reserved status (excluding Out of Order room-nights from the denominator).

**FR-HTL-106** — When computing RevPAR for a date range, the system shall calculate:

$$RevPAR = \frac{TotalRoomRevenue}{AvailableRoomNights}$$

where *TotalRoomRevenue* is the sum of all accommodation charge line items (excluding F&B, laundry, and conference charges) posted within the date range.

**FR-HTL-107** — When computing ADR for a date range, the system shall calculate:

$$ADR = \frac{RoomRevenue}{RoomsSold}$$

**FR-HTL-108** — When a Business Owner views the length-of-stay distribution, the system shall display a frequency histogram of checkout-minus-checkin durations, grouped as: < 3 hours, 3–8 hours, 8–24 hours (same-day), 1 night, 2 nights, 3–6 nights, 7+ nights.

**FR-HTL-109** — When a Business Owner views the booking source breakdown, the system shall display a count and percentage of reservations by `booking_source` value for the selected period; the chart shall include a "Channel (Phase 4)" placeholder category showing zero, labelled with a tooltip: "Channel manager integration available in Phase 4."

**FR-HTL-110** — When a Business Owner views occupancy analytics, the system shall allow filtering by: date range, room type, and individual room.

**FR-HTL-111** — When a Business Owner exports an occupancy analytics report, the system shall generate a CSV file containing one row per room per day, with columns: date, room number, room type, status, billing mode, revenue posted.

**FR-HTL-112** — When a Business Owner exports an occupancy analytics report as PDF, the system shall generate a formatted document including: property name, report period, the four summary metrics (FR-HTL-104), the length-of-stay histogram, the booking source chart, and the per-room-per-day data table.
