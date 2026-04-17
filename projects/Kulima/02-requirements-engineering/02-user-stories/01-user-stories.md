# User Stories — Kulima Farm Management Information System

**Project:** Kulima
**Version:** 1.0
**Date:** 2026-04-04
**Methodology:** Hybrid (Water-Scrum-Fall)

---

## Phase 1 — MVP (Core Modules)

---

## EP-FARM: Farm and Plot Management

### US-FARM-001: Register a New Farm

**As a** smallholder farmer (Nakato Grace), **I want to** register my farm with its name, location (district, sub-county, parish, village), total area in acres, and land tenure type, **so that** I have a digital record of my farm that replaces my paper notebook.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer is logged in and on the farm registration screen, **when** she enters farm name, selects District > Sub-County > Parish > Village from cascading dropdowns, enters total area in acres, and selects land tenure type (customary, freehold, leasehold, or mailo), **then** the system saves the farm and displays it on the farm list screen.
2. **Given** the farmer has already registered a farm named "Nakato Farm", **when** she attempts to register another farm with the same name, **then** the system displays an error: "A farm with this name already exists in your account."
3. **Given** the farmer is offline, **when** she completes the farm registration form and taps Save, **then** the farm is saved to the local database and queued for sync when connectivity is restored.

---

### US-FARM-002: Add Plots to a Farm

**As a** commercial farmer (Mugisha Robert), **I want to** subdivide my farm into named plots with plot type, area, and optional soil and irrigation data, **so that** I can track activities and costs at the plot level.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has a registered farm, **when** he creates a new plot by entering plot name, selecting plot type from the 25+ system-defined types (cropland, pasture, greenhouse, poultry house, fish pond, apiary, etc.), and entering area in acres, **then** the plot is saved and appears under the farm's plot list.
2. **Given** the farm total area is 200 acres and existing plots sum to 195 acres, **when** the farmer creates a new plot of 10 acres (exceeding the farm total), **then** the system displays a warning "Plot area sum (205 acres) exceeds farm total area (200 acres)" but allows the save.
3. **Given** the farmer is on the plot detail screen, **when** he optionally records soil type and irrigation method, **then** the data is saved and displayed on the plot detail screen.

---

### US-FARM-003: View Farm Overview Dashboard

**As a** commercial farmer (Mugisha Robert), **I want to** see a dashboard summarising all my plots, active crop seasons, livestock counts, and recent financial totals, **so that** I can assess my farm's status at a glance from Kampala.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has at least one farm with plots, crops, and livestock, **when** he opens the farm overview dashboard, **then** the system displays: total farm area, number of plots, active crop seasons count, total livestock count, and current month income vs expenses.
2. **Given** the farmer manages 2 farms, **when** he selects a specific farm from the farm switcher, **then** the dashboard refreshes to show data for the selected farm only.

---

### US-FARM-004: Manage Multiple Farms

**As a** commercial farmer (Mugisha Robert), **I want to** register and switch between multiple farms under my account, **so that** I can manage my coffee estate in Kasese and cattle ranch in Mbarara from a single login.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer's subscription tier permits multiple farms, **when** he registers a second farm, **then** both farms appear in the farm list and he can switch between them.
2. **Given** the farmer has reached his tier's farm limit, **when** he attempts to register an additional farm, **then** the system displays a clear upgrade prompt indicating the current tier limit and the next tier that supports more farms.
3. **Given** the farmer switches from Farm A to Farm B, **when** the switch completes, **then** all screens (plots, crops, livestock, finances) reflect Farm B data with zero cross-contamination from Farm A.

---

### US-FARM-005: View Farm in Hectares or Square Metres

**As a** smallholder farmer (Nakato Grace), **I want to** see my farm and plot areas converted to hectares or square metres, **so that** I can compare with official land records that use metric units.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has registered a farm of 3 acres, **when** she toggles the area unit to hectares, **then** the system displays 1.21 hectares (calculated as 3 x 0.4047).
2. **Given** the farmer views her plot list, **when** she selects square metres as the display unit, **then** all plot areas display in square metres with the conversion applied consistently.

---

## EP-CROP: Crop Management

### US-CROP-001: Plan a Crop Season

**As a** smallholder farmer (Nakato Grace), **I want to** create a crop season by selecting a plot, crop, variety, planned planting date, and expected harvest date, **so that** I can plan my growing season and track it digitally.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has at least one plot, **when** she creates a crop season by selecting the plot, choosing a crop and variety from the pre-loaded library, and entering planned planting and harvest dates, **then** the system saves the season and displays it on the crop seasons list with status "Planned."
2. **Given** the crop variety "Matooke (Mbwazirume)" has a maturity period of 12 months, **when** the farmer enters a planting date of 2026-03-15 and a harvest date of 2026-08-15 (5 months), **then** the system displays a warning: "Harvest date is earlier than the variety's typical maturity period of 12 months."
3. **Given** it is February and Uganda Season A begins in March, **when** the farmer opens the crop season planner, **then** the system displays a prompt: "Season A (March-June) is approaching. Plan your crops now."

---

### US-CROP-002: Record Planting Activity

**As a** smallholder farmer (Nakato Grace), **I want to** record the actual planting date, seed quantity used, and planting method for a crop season, **so that** I have an accurate record of when and how I planted.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** a crop season exists with status "Planned", **when** the farmer records the actual planting date, seed quantity (with unit), and planting method (direct sowing, transplanting, etc.), **then** the season status changes to "Planted" and the planting record is saved.
2. **Given** the farmer records planting while offline, **when** she returns to connectivity, **then** the planting record syncs to the server without data loss.

---

### US-CROP-003: Log Crop Activities

**As a** commercial farmer (Mugisha Robert), **I want to** log activities such as weeding, spraying, fertilising, and irrigating against a crop season with date, inputs used, labour hours, and cost, **so that** I can track input costs per acre for my coffee estate.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** a crop season has status "Planted", **when** the farmer logs an activity by selecting activity type (from 20+ types), entering date, worker(s), hours, inputs used (name, quantity, unit, cost), and optional notes, **then** the activity is saved and appears in the crop season's activity timeline.
2. **Given** the farmer logs a spraying activity with 2 litres of pesticide at UGX 25,000/litre, **when** the activity is saved, **then** the system records the total input cost as UGX 50,000 and adds it to the season's cumulative cost.
3. **Given** the farmer uploads a photo of crop health during the activity, **when** the photo is attached, **then** the photo is stored locally (compressed) and queued for sync.

---

### US-CROP-004: Record Harvest

**As a** smallholder farmer (Nakato Grace), **I want to** record the harvest quantity, quality grade, and storage destination for a crop season, **so that** I can track actual yield and compare it against expectations.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** a crop season has status "Planted" and at least one activity logged, **when** the farmer records harvest date, quantity (with unit — kg, bags, bunches), quality grade, and storage destination, **then** the season status changes to "Harvested" and the harvest record is saved.
2. **Given** the variety "Arabica Coffee (SL28)" has an expected yield of 800 kg/acre and the plot is 10 acres, **when** the farmer records a harvest of 6,500 kg, **then** the system displays yield analysis: "Actual: 650 kg/acre | Expected: 800 kg/acre | Variance: -18.75%."

---

### US-CROP-005: Browse Crop Library

**As a** smallholder farmer (Nakato Grace), **I want to** browse the pre-loaded crop library with local names in Luganda, **so that** I can find the crop I grow even if I do not know the English name.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer's language is set to Luganda, **when** she opens the crop library, **then** crop names display in Luganda alongside the English name (e.g., "Matooke / Cooking Banana").
2. **Given** the farmer searches for "mmwanyi", **when** the search executes, **then** "Coffee (Emmwanyi)" appears in the results because the search matches across all language variants.
3. **Given** the crop library contains 200+ crops, **when** the farmer filters by category (cereals, legumes, fruits, vegetables, cash crops), **then** only crops in the selected category display.

---

### US-CROP-006: Track Crop Rotation

**As a** commercial farmer (Mugisha Robert), **I want to** view the crop history for each plot across seasons, **so that** I can plan crop rotation and avoid planting the same crop consecutively.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** a plot has had 3 crop seasons recorded over 2 years, **when** the farmer views the plot's crop history, **then** the system displays a chronological list of all seasons on that plot showing crop name, variety, planting date, harvest date, and yield.
2. **Given** the farmer is planning a new season on a plot that grew beans in the previous season, **when** she selects beans again, **then** the system displays a notice: "Beans were grown on this plot in the previous season. Consider rotating to a different crop family."

---

## EP-LIVE: Livestock Management

### US-LIVE-001: Register an Individual Animal

**As a** smallholder farmer (Nakato Grace), **I want to** register each of my 5 Ankole cattle with tag number, name, sex, date of birth, breed, and sire/dam, **so that** I have a digital record of every animal.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer is on the livestock registration screen, **when** she enters tag number, animal name, selects species (cattle), breed (Ankole Longhorn), sex (female), date of birth, and optionally selects sire and dam from existing animals, **then** the animal is saved and appears in the herd list.
2. **Given** the farmer enters a tag number that already exists in her herd, **when** she attempts to save, **then** the system displays an error: "An animal with tag number [X] already exists on this farm."
3. **Given** the farmer is offline, **when** she registers a new animal, **then** the record is saved locally and synced when connectivity is restored.

---

### US-LIVE-002: Record Health Event

**As a** smallholder farmer (Nakato Grace), **I want to** record vaccination, treatment, and deworming events for my cattle with the next due date, **so that** I never miss a vaccination and lose another calf to East Coast Fever.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer selects an animal, **when** she records a health event by selecting type (vaccination, treatment, deworming, dipping), entering date, product used, dosage, administering person, and next due date, **then** the event is saved and the next due date appears on the animal's timeline.
2. **Given** a vaccination has a next due date of 2026-05-15, **when** the current date is 2026-05-08 (7 days before), **then** the system sends a push notification and SMS reminder: "Vaccination due for [Animal Name] on 15 May 2026."
3. **Given** the farmer views the animal detail screen, **when** she checks the health history tab, **then** all health events display in reverse chronological order with type, date, product, and next due date.

---

### US-LIVE-003: Log Production Records

**As a** smallholder farmer (Nakato Grace), **I want to** record daily milk yield per cow (morning and evening sessions) and daily egg collection, **so that** I can track production trends and understand profitability.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer selects a dairy cow, **when** she records milk production by entering date, session (morning/evening), and quantity in litres, **then** the production record is saved and the daily total updates.
2. **Given** the farmer manages a flock of 30 chickens, **when** she records egg collection by entering date and total eggs collected, **then** the flock production record is saved (flock-level, not individual).
3. **Given** the farmer views the production dashboard for a cow over the past 30 days, **when** the data loads, **then** a bar chart displays daily milk yield with the monthly average calculated and displayed.

---

### US-LIVE-004: Record Reproductive Events

**As a** smallholder farmer (Nakato Grace), **I want to** record mating, pregnancy checks, births, and weaning for my cattle, **so that** I can manage breeding and know when calves are expected.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer selects a female cow, **when** she records a mating event with date, bull/sire (selected from herd), and mating method (natural/AI), **then** the system saves the event and calculates an expected calving date (approximately 283 days for cattle).
2. **Given** a cow has a recorded mating event, **when** the farmer records a pregnancy confirmation, **then** the expected calving date is confirmed and a reminder is set for 2 weeks before the due date.
3. **Given** a cow gives birth, **when** the farmer records a birth event with calf sex, weight, and name, **then** a new animal record is automatically created with dam and sire pedigree links populated.

---

### US-LIVE-005: Manage Flocks

**As a** smallholder farmer (Nakato Grace), **I want to** manage my 30 kienyeji chickens as a flock rather than individually, **so that** I can track total flock size, mortality, and production without registering each bird.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer creates a new flock, **when** she enters flock name, species (chicken), breed (kienyeji), initial count (30), and housing (poultry house plot), **then** the flock is saved with current count set to 30.
2. **Given** the flock has 30 birds, **when** the farmer records a mortality event of 2 birds with cause (disease), **then** the flock count decreases to 28 and the mortality event is logged.
3. **Given** the flock has 28 birds, **when** the farmer records a sale of 5 birds with sale price and buyer, **then** the flock count decreases to 23 and the sale is recorded in financial records.

---

### US-LIVE-006: View Herd Summary Dashboard

**As a** commercial farmer (Mugisha Robert), **I want to** see a summary dashboard showing total animals by species and status, upcoming vaccinations, recent health events, and production trends, **so that** I can monitor my cattle ranch from Kampala.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has registered animals across cattle and goats, **when** he opens the herd summary dashboard, **then** the system displays: total count per species, count by status (active, sold, deceased), upcoming vaccinations in the next 14 days, and last 7 days of milk production totals.
2. **Given** a cow's status is "Active", **when** the farmer records a sale for that cow, **then** the cow's status transitions to "Sold" and the herd count decreases by 1.

---

## EP-FIN: Financial Records

### US-FIN-001: Record Farm Income

**As a** smallholder farmer (Nakato Grace), **I want to** record income from selling matooke, milk, and eggs with date, amount, buyer, and enterprise type, **so that** I know how much money each enterprise brings in.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer is on the income entry screen, **when** she enters date, amount (UGX), description, selects enterprise type (matooke, dairy, poultry), and optionally enters buyer name and mobile money transaction ID, **then** the income record is saved and linked to the active farm.
2. **Given** the farmer records income of UGX 150,000 for matooke sales, **when** the record saves, **then** the farm's total income for the current month updates to include this amount.

---

### US-FIN-002: Record Farm Expense

**As a** commercial farmer (Mugisha Robert), **I want to** record expenses for inputs, labour, transport, and equipment with receipt photo upload, **so that** I can track costs accurately for my bank loan reports.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer is on the expense entry screen, **when** he enters date, amount (UGX), category (inputs, labour, transport, veterinary, equipment, utilities, other), description, optional receipt photo, and links the expense to a farm activity, **then** the expense is saved.
2. **Given** the farmer uploads a receipt photo, **when** the photo is attached, **then** it is compressed to under 512 KB and stored locally, queued for sync on WiFi or strong connectivity.
3. **Given** the farmer has recorded expenses for the coffee estate, **when** he views expenses filtered by enterprise "Coffee", **then** only expenses linked to coffee activities display with a running total.

---

### US-FIN-003: View Profitability per Enterprise

**As a** smallholder farmer (Nakato Grace), **I want to** see profit or loss per enterprise (matooke, dairy, poultry) for a selected period, **so that** I can decide which enterprises to expand and which to reduce.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has recorded income and expenses linked to enterprise types, **when** she selects a period (this month, this season, this year), **then** the system displays a table: Enterprise | Total Income | Total Expenses | Profit/Loss.
2. **Given** the matooke enterprise earned UGX 500,000 and incurred UGX 350,000 in expenses for Season A, **when** the farmer views the profitability report, **then** the system shows Profit: UGX 150,000 for matooke.

---

### US-FIN-004: Set Season or Annual Budget

**As a** commercial farmer (Mugisha Robert), **I want to** set a budget per enterprise per season with line items for inputs, labour, and operations, **so that** I can compare planned vs actual spending.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer selects an enterprise and period, **when** he enters budget line items (category, planned amount) for that enterprise, **then** the budget is saved and the total planned amount displays.
2. **Given** a coffee estate budget of UGX 15,000,000 for Season A with UGX 8,000,000 of expenses recorded so far, **when** the farmer views the budget vs actuals report, **then** the system displays: Budgeted: UGX 15,000,000 | Actual: UGX 8,000,000 | Remaining: UGX 7,000,000 | 53% utilised.

---

### US-FIN-005: Generate Bank Loan Report

**As a** commercial farmer (Mugisha Robert), **I want to** generate a standardised financial report covering 12 months of income, expenses, and assets, **so that** I can present it to Centenary Bank when applying for a loan facility expansion.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has at least 12 months of financial records, **when** he selects "Generate Bank Loan Report" and chooses the 12-month period, **then** the system generates a PDF report containing: farm profile, total income, total expenses, net profit, asset register (animals, equipment), loan history, and cash flow summary.
2. **Given** the farmer has fewer than 12 months of data, **when** he attempts to generate the report, **then** the system displays a warning: "Only [X] months of data available. Banks typically require 12 months. Generate anyway?" and proceeds if confirmed.

---

### US-FIN-006: Track Loans

**As a** smallholder farmer (Nakato Grace), **I want to** record loans from SACCOs and MFIs with principal, interest rate, and repayment schedule, **so that** I can track my outstanding balance.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer is on the loan tracking screen, **when** she enters lender name, loan type (SACCO, MFI, mobile money loan), principal amount, interest rate, disbursement date, and expected repayment schedule, **then** the loan is saved with an outstanding balance equal to the principal plus calculated interest.
2. **Given** the farmer records a repayment of UGX 200,000 against a loan with outstanding balance UGX 1,000,000, **when** the repayment saves, **then** the outstanding balance updates to UGX 800,000 (the system does not auto-deduct; manual recording is required per business rules).

---

## EP-TASK: Task and Worker Management

### US-TASK-001: Create and Assign a Task

**As a** commercial farmer (Mugisha Robert), **I want to** create a task with description, plot assignment, due date, estimated hours, and assign it to one or more workers, **so that** my workers know exactly what to do each day.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer is on the task creation screen, **when** he enters task title, description, selects plot, selects activity type, sets due date, estimated hours, and assigns worker(s), **then** the task is saved with status "To Do" and the assigned worker(s) receive a push notification.
2. **Given** the farmer creates a recurring task (weekly weeding), **when** the recurrence is set to "Every Monday", **then** the system auto-generates a new task instance each Monday with the same details.

---

### US-TASK-002: Worker Views and Completes Task

**As a** farm worker (Ocan David), **I want to** see my assigned tasks for today with clear descriptions, and mark each task complete when finished, **so that** my hours are accurately recorded and I receive my daily pay.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** Ocan is logged in on his phone, **when** he opens the app, **then** he sees a list of tasks assigned to him for today with task title, plot, activity type, and estimated hours.
2. **Given** Ocan has completed a spraying task, **when** he taps "Mark Complete" and enters actual hours worked, **then** the task status changes to "Done", actual hours are logged, and the farm manager is notified.
3. **Given** Ocan is offline, **when** he marks a task complete, **then** the completion is saved locally and syncs when connectivity returns.

---

### US-TASK-003: Log Daily Work Hours

**As a** farm worker (Ocan David), **I want to** see a summary of my logged hours for the current week, **so that** I can verify my hours match what the supervisor has recorded.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** Ocan has completed tasks throughout the week, **when** he views "My Work Log", **then** the system displays: date, task, hours worked, and weekly total hours.
2. **Given** Ocan worked 8 hours on Monday and 6 hours on Tuesday, **when** he views the weekly total, **then** the system shows 14 hours with the daily breakdown.

---

### US-TASK-004: Calculate Payroll

**As a** commercial farmer (Mugisha Robert), **I want to** calculate payroll for all workers based on logged hours and their configured rates, **so that** I can pay workers accurately via mobile money.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** worker Ocan David has a daily rate of UGX 15,000 and logged 6 days in the pay period, **when** Mugisha generates the payroll report, **then** the system calculates: Ocan David | 6 days | UGX 90,000.
2. **Given** a permanent staff member has NSSF and PAYE deductions configured, **when** the payroll is generated, **then** the system calculates gross pay, NSSF deduction (5% employee, 10% employer), PAYE (if applicable), and net pay.
3. **Given** the payroll is finalised, **when** Mugisha exports it, **then** the system generates a PDF/Excel payroll report showing each worker's name, hours, rate, gross pay, deductions, and net pay.

---

### US-TASK-005: View Task Calendar

**As a** commercial farmer (Mugisha Robert), **I want to** see all farm tasks on a calendar view, **so that** I can plan work distribution across the week and identify scheduling conflicts.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** multiple tasks exist for the current week, **when** the farmer opens the calendar view, **then** tasks display on their due dates with colour-coding by status (To Do = blue, In Progress = amber, Done = green).
2. **Given** two tasks are assigned to the same worker on the same day with combined estimated hours exceeding 8, **when** the farmer views the calendar, **then** the system highlights the over-allocation with a warning indicator.

---

## EP-WX: Weather and Advisory

### US-WX-001: View Weather Forecast

**As a** smallholder farmer (Nakato Grace), **I want to** see a 3-day weather forecast specific to my farm's GPS location, **so that** I can decide when to plant, spray, or harvest.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer's farm has a GPS location recorded, **when** she opens the weather screen, **then** the system displays a 3-day forecast showing temperature (high/low), precipitation probability, wind speed, and humidity for each day.
2. **Given** the farmer is on the free tier, **when** she views the forecast, **then** only 3 days display with a prompt: "Upgrade to see 8-day forecast."

---

### US-WX-002: Receive Weather Alerts

**As a** smallholder farmer (Nakato Grace), **I want to** receive SMS and push notification alerts when extreme weather is forecast for my farm's location, **so that** I can protect my crops and animals.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the weather API forecasts heavy rainfall (>50mm) for the farmer's location, **when** the alert is triggered, **then** the farmer receives a push notification and SMS: "Heavy rainfall expected at [Farm Name] tomorrow. Secure livestock and drainage."
2. **Given** the farmer has weather alerts enabled, **when** a hailstorm warning is issued, **then** the alert is delivered within 30 minutes of the weather service publishing the warning.

---

### US-WX-003: View Historical Weather Data

**As a** commercial farmer (Mugisha Robert), **I want to** view historical rainfall and temperature data for my farm's location over past seasons, **so that** I can correlate weather patterns with crop yield.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** historical weather data is available for the farm location, **when** the farmer selects a past season (e.g., Season A 2025), **then** the system displays monthly rainfall totals and average temperatures in a table and chart.
2. **Given** the farmer views historical data alongside yield records, **when** both datasets are displayed, **then** the farmer can visually compare rainfall patterns with harvest quantities for the same period.

---

## EP-AUTH: Authentication and User Management

### US-AUTH-001: Register an Account

**As a** new farmer, **I want to** register an account using my phone number and a password, **so that** I can start using Kulima to manage my farm.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** a person opens the Kulima app for the first time, **when** they enter their phone number, create a password (minimum 8 characters), and enter their name, **then** the system sends an OTP via SMS for verification.
2. **Given** the person receives the OTP, **when** they enter the correct OTP within 5 minutes, **then** the account is created and the farmer is directed to the farm registration screen.
3. **Given** the phone number is already registered, **when** the person attempts to register, **then** the system displays: "This phone number is already registered. Please log in."

---

### US-AUTH-002: Login

**As a** registered farmer (Nakato Grace), **I want to** log in with my phone number and password, **so that** I can access my farm data securely.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer enters a valid phone number and correct password, **when** she taps Login, **then** the system authenticates her and displays the farm overview dashboard.
2. **Given** the farmer enters an incorrect password 5 times, **when** the 5th attempt fails, **then** the system locks the account for 15 minutes and displays: "Too many failed attempts. Try again after 15 minutes."

---

### US-AUTH-003: Manage User Roles

**As a** commercial farmer (Mugisha Robert), **I want to** invite users to my farm with specific roles (Farm Manager or Worker), **so that** each user has appropriate access to farm data and functions.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** Mugisha is a Farm Owner, **when** he invites a user by phone number and assigns the role "Farm Manager", **then** the invited user receives an SMS invitation and, upon acceptance, can access the farm with manager-level permissions (all CRUD operations except role management and subscription changes).
2. **Given** Mugisha assigns a user the role "Worker", **when** the worker logs in, **then** they can only view assigned tasks, mark tasks complete, and log hours — they cannot access financial records, animal registrations, or farm settings.

---

### US-AUTH-004: Subscription Payment via Mobile Money

**As a** smallholder farmer (Nakato Grace), **I want to** pay my monthly subscription using MTN Mobile Money from within the app, **so that** I do not need a bank account or credit card.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer's free tier is expiring or she wants to upgrade, **when** she selects a subscription plan and chooses MTN MoMo as payment method, **then** the system initiates a mobile money payment request to her registered phone number.
2. **Given** the mobile money payment is confirmed, **when** the transaction completes, **then** the subscription is activated immediately and a receipt is sent via SMS.
3. **Given** the farmer selects annual payment, **when** she pays for 10 months, **then** the system activates 12 months of service (annual discount per business rules).

---

## EP-SYNC: Offline and Sync

### US-SYNC-001: Work Offline

**As a** smallholder farmer (Nakato Grace), **I want to** use all core app functions (register animals, record activities, log income/expenses) without internet, **so that** I can record data at night by paraffin lamp when there is no signal.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer's phone has no internet connectivity, **when** she records a milk production entry, **then** the record saves to the local Room database and appears in the app immediately.
2. **Given** the farmer is offline, **when** she browses the crop library, **then** all 200+ crops display from the pre-loaded reference data without requiring a network request.

---

### US-SYNC-002: Background Sync on Connectivity

**As a** smallholder farmer (Nakato Grace), **I want to** have my offline records automatically sync to the server when my phone connects to the internet, **so that** I do not have to manually upload data.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has 15 offline records queued, **when** her phone connects to WiFi or 3G/4G, **then** the sync queue processes automatically in priority order: financial transactions first, then activities, then animals, then reference data.
2. **Given** a sync is in progress, **when** the farmer continues using the app, **then** the sync runs in the background without blocking the UI.

---

### US-SYNC-003: Resolve Sync Conflicts

**As a** commercial farmer (Mugisha Robert), **I want to** be notified if my offline edits conflict with changes made by my farm manager on another device, **so that** I can review and resolve the conflict.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** Mugisha edited an animal's weight offline while his manager edited the same animal's weight on the web, **when** Mugisha's phone syncs, **then** the system applies last-write-wins by timestamp and logs the conflict in a "Sync Conflicts" list.
2. **Given** a conflict is logged, **when** Mugisha views the conflict list, **then** each entry shows: record type, field, his value, server value, timestamp of each, and which value was kept.

---

### US-SYNC-004: Compressed Photo Sync

**As a** smallholder farmer (Nakato Grace), **I want to** have my crop and receipt photos sync only when on WiFi or strong connectivity to avoid draining my mobile data, **so that** I am not charged unexpected data costs.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer has 5 photos queued for sync, **when** her phone connects to WiFi, **then** photos sync in the background after all text data has synced.
2. **Given** the phone detects weak 2G/Edge connectivity, **when** a photo sync is pending, **then** the system defers the photo sync until a stronger connection is detected.

---

## EP-LANG: Multi-lingual

### US-LANG-001: Switch App Language

**As a** smallholder farmer (Nakato Grace), **I want to** switch the app language to Luganda, **so that** I can understand all menus, labels, and instructions in my mother tongue.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the farmer is on the settings screen, **when** she selects Luganda from the language options (English, Luganda, Swahili), **then** all app interface text (menus, buttons, labels, messages) switches to Luganda immediately.
2. **Given** the language is set to Luganda, **when** the farmer navigates to the crop management screen, **then** crop names display in Luganda with English shown in parentheses.

---

### US-LANG-002: View Crop and Livestock Names in Local Language

**As a** smallholder farmer (Nakato Grace), **I want to** see crop and livestock breed names in Luganda, **so that** I can identify the correct crop or breed without needing to know the English name.

**Phase:** 1

**Acceptance Criteria:**

1. **Given** the language is set to Luganda, **when** the farmer browses livestock breeds, **then** "Ankole Longhorn" displays as "Ente z'Ankole (Ankole Longhorn)."
2. **Given** the language is set to Swahili, **when** the farmer browses the crop library, **then** crops display in Swahili: "Mahindi (Maize)", "Kahawa (Coffee)."

---

## Phase 2 — Growth

---

## EP-MAP: GPS Mapping

### US-MAP-001: Draw Farm Boundary by Walking Perimeter

**As a** cooperative programme manager (Apio Sarah), **I want to** send field agents to walk the perimeter of a member farmer's land while the app records GPS coordinates, **so that** I can map all 320 member farms with accurate boundaries.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the field agent is at the farm and has GPS enabled, **when** they tap "Start Walking Boundary" and walk the perimeter, **then** the app records GPS coordinates at regular intervals and draws the polygon on the map in real time.
2. **Given** the agent completes the perimeter walk (returns to the start point), **when** they tap "Finish", **then** the system closes the polygon, calculates the area in acres, and saves the GeoJSON geometry to the farm record.
3. **Given** the GPS accuracy is below 10 metres, **when** the agent attempts to start the boundary walk, **then** the system displays a warning: "GPS accuracy is low ([X]m). Move to an open area for better accuracy."

---

### US-MAP-002: Draw Plot Boundaries on Satellite Imagery

**As a** commercial farmer (Mugisha Robert), **I want to** draw my plot boundaries on a satellite map by tapping corners, **so that** I can subdivide my farm digitally without physically walking each plot.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the farmer is viewing his farm on the satellite map, **when** he taps on the map to place corner points of a plot, **then** the system draws the polygon connecting the points and calculates the area.
2. **Given** the farmer has drawn the polygon, **when** he saves with a plot name and type, **then** the plot boundary is stored as GeoJSON and linked to the farm's plot record.

---

### US-MAP-003: View Farm Map with Colour-Coded Plots

**As a** commercial farmer (Mugisha Robert), **I want to** view a satellite map of my farm showing all plots colour-coded by crop status, **so that** I can see at a glance which plots are planted, harvested, or fallow.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the farmer has GPS boundaries for his farm and 10 plots, **when** he opens the farm map, **then** each plot displays as a colour-coded polygon: green = active crop, amber = approaching harvest, grey = fallow, brown = livestock.
2. **Given** the farmer taps on a plot polygon, **when** the popup displays, **then** it shows: plot name, plot type, current crop (if any), and area.

---

## EP-INV: Inventory Management

### US-INV-001: Track Input Stock

**As a** commercial farmer (Mugisha Robert), **I want to** maintain an inventory of farming inputs (seeds, fertilisers, pesticides, animal feed, veterinary medicine) with current stock levels, **so that** I know what I have on hand before purchasing more.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the farmer is on the inventory screen, **when** he adds an input item with name, category, unit of measure, current quantity, minimum stock level, and storage location, **then** the item is saved and appears in the inventory list.
2. **Given** an input item has current stock of 5 kg and minimum stock level of 10 kg, **when** the inventory is viewed, **then** the item displays a "Low Stock" warning badge.

---

### US-INV-002: Auto-Deduct Stock on Activity Logging

**As a** commercial farmer (Mugisha Robert), **I want to** have input quantities automatically deducted from inventory when I log a crop or livestock activity, **so that** stock levels stay accurate without manual adjustment.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the farmer logs a spraying activity using 2 litres of pesticide, **when** the activity is saved, **then** the pesticide inventory decreases by 2 litres automatically.
2. **Given** the farmer logs an activity using 5 kg of fertiliser but only 3 kg remain in stock, **when** the activity is saved, **then** the system displays a warning: "Stock will go negative. Current stock: 3 kg. Usage: 5 kg." but allows the record (per business rules, stock can go negative).

---

### US-INV-003: Receive Expiry Alerts

**As a** commercial farmer (Mugisha Robert), **I want to** receive alerts when inputs approach their expiry date, **so that** I can use them before they expire and avoid waste.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** a pesticide batch has an expiry date of 2026-09-15, **when** the current date is 2026-07-17 (60 days before expiry), **then** the system sends a push notification: "[Pesticide Name] expires on 15 September 2026. Use or dispose before expiry."
2. **Given** expiry alerts are configured, **when** the system checks daily, **then** alerts fire at 90, 60, and 30 days before each item's expiry date.

---

### US-INV-004: Manage Equipment and Tools

**As a** commercial farmer (Mugisha Robert), **I want to** maintain an equipment register with maintenance schedules and fuel logs, **so that** I can track equipment costs and prevent breakdowns.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the farmer registers a tractor, **when** he enters name, type, purchase date, purchase cost, and maintenance schedule (every 200 hours or every 3 months), **then** the equipment is saved and the next maintenance date is calculated.
2. **Given** a tractor's maintenance is due in 7 days, **when** the system checks the schedule, **then** the farmer receives a reminder: "Tractor maintenance due on [date]."

---

## EP-TRACE: Supply Chain Traceability

### US-TRACE-001: Create Harvest Batch

**As a** cooperative programme manager (Apio Sarah), **I want to** create a harvest batch from a collection centre delivery, linking it to the origin farm(s), plot(s), and quality grade, **so that** the batch is traceable from farm to buyer.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** coffee has been delivered to a collection centre, **when** Apio creates a batch by selecting origin farmer(s), plot(s), harvest record(s), entering weight, and assigning quality grade, **then** the batch is saved with a unique batch ID and linked to the origin data.
2. **Given** the batch is created, **when** it is viewed, **then** the origin trail (farmer name, farm GPS polygon, plot, crop, harvest date, inputs used) is visible.

---

### US-TRACE-002: Generate QR Code for Batch

**As a** cooperative programme manager (Apio Sarah), **I want to** generate a QR code for each harvest batch, **so that** buyers can scan it to verify origin and compliance.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** a batch has been created with complete origin data, **when** Apio selects "Generate QR Code", **then** the system generates a QR code that links to the buyer portal page for that batch.
2. **Given** the QR code is generated, **when** it is printed on the shipment label and scanned by Van der Berg Hans, **then** his browser opens the Kulima buyer portal showing: farm GPS polygon, crop type, harvest date, input history, certifications, and deforestation check result.

---

### US-TRACE-003: Export GeoJSON for EUDR Compliance

**As a** European coffee buyer (Van der Berg Hans), **I want to** download the GeoJSON polygon data for the farms in my supply chain, **so that** my compliance team can verify deforestation-free sourcing for EUDR.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** Van der Berg is viewing a batch on the buyer portal, **when** he clicks "Download GeoJSON", **then** the system exports the farm GPS polygon(s) as a GeoJSON file.
2. **Given** the GeoJSON is exported, **when** compared against the December 2020 Global Forest Watch baseline, **then** the deforestation check result (pass/fail) is included in the export metadata.

---

### US-TRACE-004: Manage Certifications

**As a** cooperative programme manager (Apio Sarah), **I want to** record and track certifications (organic, RainForest Alliance, UTZ, GlobalGAP, FairTrade) for member farmers, **so that** I can include valid certifications in traceability data and receive renewal reminders.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** Apio selects a member farmer, **when** she records a certification by entering type, issuing body, certificate number, issue date, and expiry date, **then** the certification is saved and linked to the farmer's profile.
2. **Given** a certification expires in 60 days, **when** the system runs its daily check, **then** Apio receives a notification: "[Farmer Name]'s [Certification] expires on [date]. Initiate renewal."

---

## EP-MKT: Marketplace

### US-MKT-001: Post Produce Listing

**As a** smallholder farmer (Nakato Grace), **I want to** list my surplus matooke for sale with quantity, price, and location, **so that** buyers in my area can find and purchase my produce.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the farmer is on the marketplace screen, **when** she creates a listing by selecting produce type, entering quantity, price per unit, optional photo, and confirming her location, **then** the listing is published and visible to other users searching the marketplace.
2. **Given** the listing is published, **when** a buyer taps "Contact Seller", **then** the system opens a WhatsApp direct link to the farmer's registered phone number.

---

### US-MKT-002: View Market Prices

**As a** smallholder farmer (Nakato Grace), **I want to** view current market prices for my crops in nearby markets, **so that** I can decide where and when to sell for the best price.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** market prices have been recorded for matooke in Mbarara, Kampala, and Masaka markets, **when** the farmer selects "Matooke" on the market prices screen, **then** the system displays a table: Market | Price per Bunch | Date Updated.
2. **Given** the farmer sets a price alert for "Matooke above UGX 15,000/bunch in Kampala", **when** the recorded price reaches UGX 16,000, **then** the farmer receives a push notification: "Matooke price in Kampala is now UGX 16,000/bunch."

---

### US-MKT-003: Find Agro-Dealers and Vets

**As a** smallholder farmer (Nakato Grace), **I want to** search for nearby agro-dealers and veterinary officers, **so that** I can buy inputs and get animal health services.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the farmer is on the directory screen, **when** she selects "Agro-Dealers" and enters her district, **then** a list of agro-dealers in the district displays with name, location, phone number, and products/services.
2. **Given** the farmer selects a veterinary officer from the directory, **when** she taps "Call", **then** the phone's dialler opens with the vet's number pre-filled.

---

## EP-COOP: Cooperative Management

### US-COOP-001: Register Member Farmers

**As a** cooperative programme manager (Apio Sarah), **I want to** register member farmers under the cooperative with their name, phone number, NIN, and farm details, **so that** I can manage all 320 members digitally.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** Apio is logged in as cooperative admin, **when** she registers a member farmer by entering name, phone, NIN, farm name, and estimated farm size, **then** the member is added to the cooperative's member list and a user account is created with a default password sent via SMS.
2. **Given** the member farmer is registered, **when** the member logs in, **then** they can see their own farm data but cannot see other members' data (tenant isolation within the cooperative franchise).

---

### US-COOP-002: Manage Collection Centre Operations

**As a** cooperative programme manager (Apio Sarah), **I want to** record deliveries at collection centres with weight, quality grade, and delivering farmer, **so that** I can calculate accurate payments for each member.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** a farmer delivers coffee to the collection centre, **when** Apio records the delivery by selecting the farmer, entering weight (kg), assigning quality grade (Grade A/B/C), and date, **then** the delivery record is saved and linked to the farmer's account.
2. **Given** 50 farmers have delivered during harvest season, **when** Apio views the collection summary, **then** the system displays: total weight collected, weight by grade, delivery count, and breakdown per farmer.

---

### US-COOP-003: Calculate Member Payments

**As a** cooperative programme manager (Apio Sarah), **I want to** calculate payments per member based on quantity delivered multiplied by grade-specific price, **so that** members are paid fairly and transparently.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** Grade A price is UGX 5,000/kg and farmer Okello delivered 200 kg Grade A, **when** Apio generates the payment schedule, **then** Okello's payment is calculated as 200 x 5,000 = UGX 1,000,000.
2. **Given** the payment schedule is generated for all members, **when** Apio reviews it, **then** the system displays each member's name, total kg by grade, calculated payment, and registered mobile money number.

---

### US-COOP-004: Bulk Mobile Money Disbursement

**As a** cooperative programme manager (Apio Sarah), **I want to** disburse payments to all members via bulk mobile money transfer (MTN MoMo or Airtel Money), **so that** payments that used to take 3 days by hand are completed in one action.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the payment schedule is approved, **when** Apio taps "Disburse Payments", **then** the system sends individual mobile money payment requests to each member's registered number via the bulk payment API.
2. **Given** the disbursement is in progress, **when** a payment fails (e.g., invalid number), **then** the system marks that payment as "Failed" with the reason and continues processing remaining payments.
3. **Given** all payments are processed, **when** Apio views the disbursement report, **then** the system displays: total disbursed, total failed, and status per member with transaction IDs for successful payments.

---

### US-COOP-005: Distribute Inputs to Members

**As a** cooperative programme manager (Apio Sarah), **I want to** record distribution of subsidised inputs (seedlings, organic fertiliser) to specific member farmers, **so that** I can verify who received what and report to the funding NGO.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** the cooperative has received a shipment of 10,000 coffee seedlings, **when** Apio records distribution to member Akello (500 seedlings) on date, **then** the distribution record saves and deducts 500 from the cooperative's seedling stock.
2. **Given** distributions are recorded for all members, **when** Apio generates the distribution report, **then** the system displays each member's name, items received, quantity, date, and acknowledgement status.

---

## EP-ACCT: Advanced Accounting

### US-ACCT-001: Switch to Advanced Accounting Mode

**As a** commercial farmer (Mugisha Robert), **I want to** switch from Simple Mode ("Money in, Money out") to Advanced Mode (double-entry accounting), **so that** my accountant can manage formal books with a chart of accounts, journal entries, and financial statements.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** Mugisha is on the financial settings screen, **when** he toggles "Advanced Accounting Mode" on, **then** the system activates the chart of accounts, journal entry screen, and financial statement reports, while preserving all existing Simple Mode records as imported transactions.
2. **Given** Advanced Mode is active, **when** the accountant creates a journal entry with debit and credit accounts and amounts, **then** the system validates that total debits equal total credits before saving.

---

### US-ACCT-002: Generate Financial Statements

**As a** commercial farmer (Mugisha Robert), **I want to** generate an income statement, balance sheet, and trial balance for a selected period, **so that** I can present professional financial reports to Centenary Bank and investors.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** journal entries have been recorded for Q1 2026, **when** Mugisha selects "Income Statement" for Q1 2026, **then** the system generates: Revenue, Cost of Goods Sold, Gross Profit, Operating Expenses, and Net Profit.
2. **Given** the balance sheet is generated, **when** the report is viewed, **then** Assets = Liabilities + Equity (the fundamental accounting equation must balance).
3. **Given** any report is generated, **when** Mugisha taps "Export PDF", **then** the report downloads as a formatted PDF suitable for bank presentation.

---

### US-ACCT-003: View Trial Balance

**As a** commercial farmer (Mugisha Robert), **I want to** generate a trial balance showing all account balances, **so that** my accountant can verify that the books are balanced before preparing financial statements.

**Phase:** 2

**Acceptance Criteria:**

1. **Given** journal entries exist for the selected period, **when** the accountant generates the trial balance, **then** the system lists every account with its debit or credit balance.
2. **Given** the trial balance is generated, **when** total debits do not equal total credits, **then** the system flags the imbalance with the variance amount.

---

## Phase 3 — IoT and Surveillance

---

## EP-IOT: IoT Integration

### US-IOT-001: Connect Jaguza Account

**As a** commercial farmer (Mugisha Robert), **I want to** connect my Jaguza account to Kulima via OAuth, **so that** ear tag sensor data for my cattle appears in my Kulima dashboard without using the Jaguza app separately.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha is on the IoT settings screen, **when** he taps "Connect Jaguza" and completes the OAuth flow with his Jaguza credentials, **then** the system links his Jaguza account and begins polling device data every 10 minutes.
2. **Given** the connection is established, **when** Mugisha views his connected devices, **then** each Jaguza ear tag displays: device ID, assigned animal, battery status, and last data timestamp.

---

### US-IOT-002: View Animal Sensor Data

**As a** commercial farmer (Mugisha Robert), **I want to** view sensor data (temperature, activity level, fertility index) for a specific animal on its detail screen, **so that** I can monitor animal health remotely.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** a Jaguza ear tag is assigned to cow "Nakasero", **when** Mugisha opens Nakasero's detail screen and selects the "Sensors" tab, **then** the system displays: current temperature, activity graph (last 24 hours), and fertility index.
2. **Given** sensor data is polled every 10 minutes, **when** the latest data arrives, **then** the sensor tab updates without requiring a manual refresh.

---

### US-IOT-003: Receive Heat Detection Alert

**As a** commercial farmer (Mugisha Robert), **I want to** receive an alert when a cow's fertility index indicates she is in heat, **so that** I can arrange mating or AI service at the optimal time.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** a Jaguza ear tag detects elevated activity and fertility index above the heat threshold for cow "Nakasero", **when** the webhook alert fires, **then** Mugisha receives an immediate push notification and SMS: "Heat detected: Nakasero. Optimal breeding window: next 12-18 hours."
2. **Given** the alert is received, **when** Mugisha views the animal's detail screen, **then** the heat event is logged in the reproductive timeline with timestamp and sensor readings.

---

### US-IOT-004: Receive Disease Early Warning

**As a** commercial farmer (Mugisha Robert), **I want to** receive an early warning when sensor data indicates a potential disease (elevated temperature, reduced activity), **so that** I can call a vet before the condition worsens.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** a cow's temperature reading exceeds 39.5 degrees C for 2 consecutive readings, **when** the system evaluates the data, **then** a Critical alert is generated: "Possible fever detected for [Animal Name]. Temperature: [X] degrees C. Contact your vet."
2. **Given** the alert severity is Critical, **when** it is triggered, **then** SMS + push notification are sent immediately (within 2 minutes of data receipt).

---

### US-IOT-005: View Herd Health Dashboard

**As a** commercial farmer (Mugisha Robert), **I want to** see a herd health dashboard showing all IoT-monitored animals colour-coded by status (green/amber/red), **so that** I can identify problem animals at a glance.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** 20 animals have Jaguza ear tags, **when** Mugisha opens the herd health dashboard, **then** each animal displays with a status indicator: green (normal), amber (attention needed — minor deviation), red (critical — disease/heat alert active).
2. **Given** 2 animals are in "red" status, **when** Mugisha taps on a red animal, **then** the system navigates to the animal's sensor detail screen showing the triggering alert.

---

## EP-GPS: GPS Animal Tracking

### US-GPS-001: Register GPS Tracker

**As a** commercial farmer (Mugisha Robert), **I want to** register a standalone GPS tracker by IMEI and assign it to a specific animal, **so that** I can track the animal's location in real time.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha has a GPS tracker device, **when** he enters the IMEI number and SIM card number and assigns it to bull "Kashari", **then** the tracker is registered and the system begins receiving location data.
2. **Given** the tracker is registered, **when** the first location ping is received, **then** the animal's position displays on the live map with a timestamp.

---

### US-GPS-002: View Live Map

**As a** commercial farmer (Mugisha Robert), **I want to** view a live map showing the current positions of all GPS-tracked animals, **so that** I can monitor their locations from Kampala.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** 5 animals have GPS trackers, **when** Mugisha opens the live tracking map, **then** each animal displays as a labelled icon at its last reported position with the timestamp of the last ping.
2. **Given** an animal moves, **when** the next position update arrives, **then** the animal's icon moves to the new position on the map without requiring a page refresh.

---

### US-GPS-003: Create Geofence and Receive Breach Alert

**As a** commercial farmer (Mugisha Robert), **I want to** draw a geofence boundary on the map and receive an alert if any tracked animal exits the boundary, **so that** I am warned of potential theft or straying cattle (a real concern in Karamoja and Teso regions).

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha is on the geofence setup screen, **when** he draws a polygon on the map defining the allowed area and names the geofence, **then** the geofence is saved and monitoring begins.
2. **Given** bull "Kashari" exits the geofence boundary, **when** the GPS position update is received outside the polygon, **then** the system sends an SMS, push notification, and WhatsApp alert within 2 minutes: "GEOFENCE BREACH: Kashari has left [Geofence Name] at [time]. Last position: [GPS coordinates]."

---

### US-GPS-004: View Historical Movement

**As a** commercial farmer (Mugisha Robert), **I want to** replay an animal's movement history over the past 7, 14, or 30 days, **so that** I can review grazing patterns or investigate when an animal went missing.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha selects animal "Kashari" and chooses "Last 7 Days", **when** the historical playback loads, **then** the system animates the animal's movement path on the map with timestamps.
2. **Given** the playback is displayed, **when** Mugisha pauses at a specific point, **then** the timestamp, speed, and GPS coordinates for that position display.

---

## EP-CAM: Camera Surveillance

### US-CAM-001: Add Camera and View Live Stream

**As a** commercial farmer (Mugisha Robert), **I want to** register my Hikvision CCTV camera and view a live video stream from within Kulima, **so that** I can monitor my farm from Kampala without switching to a separate camera app.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha is on the camera setup screen, **when** he enters the camera name, selects brand (Hikvision/Dahua/Reolink/Generic), enters RTSP URL, and taps "Test Connection", **then** the system verifies the RTSP stream is reachable and saves the camera.
2. **Given** the camera is registered, **when** Mugisha opens the camera's live view, **then** the HLS-converted video stream plays in the app with quality auto-adjusted based on current bandwidth.

---

### US-CAM-002: Multi-Camera Grid View

**As a** commercial farmer (Mugisha Robert), **I want to** view all my cameras in a grid layout, **so that** I can monitor multiple locations simultaneously.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha has 4 cameras registered, **when** he opens the multi-camera view, **then** all 4 streams display in a 2x2 grid layout.
2. **Given** the grid is displayed, **when** Mugisha taps on one camera, **then** it expands to full-screen view with PTZ controls (if the camera supports pan-tilt-zoom).

---

### US-CAM-003: Receive Motion Detection Alert

**As a** commercial farmer (Mugisha Robert), **I want to** receive an alert with a snapshot when motion is detected in a specific zone during night hours, **so that** I am warned of potential intruders or animal disturbance.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha has configured a motion detection zone on a camera and set alert scheduling to "Night only (8PM-6AM)", **when** motion is detected in the zone during night hours, **then** the system sends a push notification, SMS, and WhatsApp message with a snapshot image.
2. **Given** motion is detected during daytime (outside the alert schedule), **when** the detection occurs, **then** no alert is sent (reducing false positives from normal farm activity).

---

### US-CAM-004: Share Camera Access

**As a** commercial farmer (Mugisha Robert), **I want to** share camera access with my farm manager via a time-limited link, **so that** the manager can view live streams during specific periods without full account access.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha selects a camera, **when** he taps "Share Access" and selects duration (1 hour, 24 hours, or 7 days), **then** the system generates a unique link and sends it to the specified phone number via SMS.
2. **Given** the link expires after the configured duration, **when** the recipient tries to access the link, **then** the system displays: "This link has expired. Contact the farm owner for new access."

---

## EP-AI: AI Farm Advisor

### US-AI-001: Ask a Farming Question

**As a** smallholder farmer (Nakato Grace), **I want to** ask a farming question in Luganda and receive an answer that considers my farm's data (crops, location, season), **so that** I get personalised advice without needing to visit an extension officer.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Nakato types "Ensuku yange y'ebbitooke zikuzimu. Nkole ntya?" (My matooke plants are dying. What do I do?), **when** she submits the question, **then** the AI responds in Luganda with a diagnosis checklist referencing her recorded farm data (location: Mbarara, crop: matooke, recent weather, recent activities).
2. **Given** the AI's confidence is below 70%, **when** it responds, **then** it appends: "For further help, contact your nearest extension officer" with a link to the directory.

---

### US-AI-002: Photograph Pest or Disease for Diagnosis

**As a** smallholder farmer (Nakato Grace), **I want to** take a photo of a sick crop or animal and receive an AI diagnosis, **so that** I can act quickly before the problem spreads.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Nakato takes a photo of a maize plant with symptoms, **when** she uploads it to the AI advisor, **then** the system uses Claude Vision API to analyse the image and returns a probable diagnosis (e.g., "Fall Armyworm damage — 85% confidence") with recommended treatment steps.
2. **Given** the AI returns a diagnosis with confidence below 60%, **when** the result displays, **then** the system recommends: "Diagnosis uncertain. Please take another photo in better lighting or consult a local extension officer."

---

### US-AI-003: Receive Personalised Recommendations

**As a** commercial farmer (Mugisha Robert), **I want to** receive AI-generated recommendations based on my activity records and yield analysis, **so that** I can optimise my farming practices.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** Mugisha's coffee estate had 18% below-expected yield last season with recorded activities showing late spraying, **when** the AI advisor generates seasonal recommendations, **then** it suggests: "Spray schedule was delayed by an average of 12 days in Season A 2025. Adhering to the recommended spray calendar could improve yield by up to 15%."
2. **Given** the recommendation references specific data, **when** Mugisha views it, **then** the recommendation cites the source data (e.g., "Based on 8 spray activities logged between March-June 2025 vs recommended schedule").

---

### US-AI-004: Use AI Advisor Offline

**As a** smallholder farmer (Nakato Grace), **I want to** access pre-loaded farming guides when I have no internet, **so that** I can find basic pest and disease information even offline.

**Phase:** 3

**Acceptance Criteria:**

1. **Given** the farmer is offline, **when** she opens the AI advisor and asks about Fall Armyworm, **then** the system retrieves and displays the pre-loaded guide for Fall Armyworm (symptoms, treatment, prevention) from the local database.
2. **Given** the farmer asks a question that requires the online AI model, **when** the system detects no connectivity, **then** it displays: "This question requires internet. Your question has been saved and will be answered when you reconnect."

---

## Phase 4 — Enterprise

---

## EP-DIR: Director Platform

### US-DIR-001: View Consolidated Farm Overview

**As a** farm director (Katumba James), **I want to** see a single dashboard summarising financial performance, livestock health, and crop status across all 3 of my farms, **so that** I can monitor my investments in 5 minutes daily without visiting each farm.

**Phase:** 4

**Acceptance Criteria:**

1. **Given** Katumba has 3 farms (dairy, poultry, vanilla) linked to his director account, **when** he opens the director dashboard, **then** the system displays: total income vs expenses across all farms (current month), total livestock count, active IoT alerts, and crop status summary per farm.
2. **Given** the dashboard is displayed, **when** Katumba taps on a specific farm, **then** the system navigates to that farm's detailed overview without requiring re-authentication.

---

### US-DIR-002: Approve Purchase Requests

**As a** farm director (Katumba James), **I want to** review and approve purchase requests above UGX 5,000,000 submitted by farm managers, **so that** I control major expenditures and prevent unauthorised spending.

**Phase:** 4

**Acceptance Criteria:**

1. **Given** a farm manager submits a purchase request for a water pump at UGX 7,500,000, **when** the request is submitted, **then** Katumba receives a push notification: "Purchase request: Water pump — UGX 7,500,000 — [Farm Name]. Approve or reject."
2. **Given** Katumba reviews the request, **when** he taps "Approve", **then** the request status changes to "Approved", the manager is notified, and the expense is pre-authorised in the financial records.
3. **Given** Katumba rejects the request, **when** he taps "Reject" and enters a reason, **then** the request status changes to "Rejected" and the manager receives the rejection with the reason.

---

### US-DIR-003: Compare Farm Performance

**As a** farm director (Katumba James), **I want to** compare financial performance (income, expenses, net profit) across my 3 farms side by side, **so that** I can identify which farm is underperforming and investigate.

**Phase:** 4

**Acceptance Criteria:**

1. **Given** Katumba selects "Compare Farms" and a period (Q1 2026), **when** the report generates, **then** the system displays a side-by-side table: Farm | Income | Expenses | Net Profit | Profit Margin (%).
2. **Given** one farm shows a significantly lower profit margin, **when** Katumba drills into that farm's expenses, **then** the system displays the expense breakdown by category, allowing him to identify inflated line items.

---

### US-DIR-004: View IoT Alerts Across Portfolio

**As a** farm director (Katumba James), **I want to** see a unified feed of IoT alerts (disease warnings, geofence breaches, camera motion alerts) from all my farms, **so that** I can respond to emergencies quickly.

**Phase:** 4

**Acceptance Criteria:**

1. **Given** alerts exist across 3 farms, **when** Katumba opens the alerts feed, **then** the system displays all alerts in reverse chronological order with farm name, alert type, severity, and timestamp.
2. **Given** a Critical alert is raised on any farm, **when** Katumba has the app open, **then** a prominent banner displays at the top of the screen with alert details and a "View" button navigating to the source.

---

## EP-INTL: Multi-Country

### US-INTL-001: Configure Country Settings

**As a** Kenyan farmer using Kulima, **I want to** set my country to Kenya so that the app uses KES currency, Kenyan administrative divisions (County > Sub-County > Ward), and Kenyan crop library, **so that** the app is relevant to my farming context.

**Phase:** 4

**Acceptance Criteria:**

1. **Given** a new user registers from Kenya, **when** they select "Kenya" as their country during onboarding, **then** the system sets: currency to KES, administrative hierarchy to County > Sub-County > Ward, and loads the Kenyan crop library extension.
2. **Given** the country is set to Kenya, **when** the farmer views the crop library, **then** Kenya-specific crops and varieties display alongside the common East African crops.

---

### US-INTL-002: Set Currency

**As a** Tanzanian farmer using Kulima, **I want to** record all financial transactions in TZS, **so that** my financial records match my actual currency.

**Phase:** 4

**Acceptance Criteria:**

1. **Given** the farmer's country is Tanzania, **when** the currency is set to TZS, **then** all financial entry screens display the TZS symbol and all reports format amounts in TZS.
2. **Given** a director manages farms across Uganda and Kenya, **when** the consolidated dashboard displays, **then** each farm's financials display in the farm's local currency with no automatic conversion (conversion is manual and noted).

---

### US-INTL-003: Set Language Defaults per Country

**As a** Rwandan farmer using Kulima, **I want to** have Kinyarwanda as the default language when I select Rwanda as my country, **so that** the app starts in my preferred language.

**Phase:** 4

**Acceptance Criteria:**

1. **Given** a new user selects Rwanda during onboarding, **when** the country is confirmed, **then** the app language defaults to Kinyarwanda (changeable in settings).
2. **Given** the language is set to Kinyarwanda, **when** the farmer browses the crop library, **then** crop names display in Kinyarwanda alongside English.

---

### US-INTL-004: Load Country-Specific Crop Library

**As a** Kenyan farmer, **I want to** see crops and varieties relevant to Kenyan agriculture alongside the common East African crops, **so that** I find the specific varieties I grow.

**Phase:** 4

**Acceptance Criteria:**

1. **Given** the farmer's country is Kenya, **when** they open the crop library, **then** Kenya-specific entries (e.g., macadamia, pyrethrum, KALRO-recommended varieties) appear in addition to the base library.
2. **Given** the farmer searches for a crop, **when** they type "macadamia", **then** the search returns results from the Kenya-specific library even if macadamia is not in the base Uganda crop library.

---

## Appendix: User Story Summary

| Epic | Phase | Story Count |
|---|---|---|
| EP-FARM: Farm and Plot Management | 1 | 5 |
| EP-CROP: Crop Management | 1 | 6 |
| EP-LIVE: Livestock Management | 1 | 6 |
| EP-FIN: Financial Records | 1 | 6 |
| EP-TASK: Task and Worker Management | 1 | 5 |
| EP-WX: Weather and Advisory | 1 | 3 |
| EP-AUTH: Authentication and User Management | 1 | 4 |
| EP-SYNC: Offline and Sync | 1 | 4 |
| EP-LANG: Multi-lingual | 1 | 2 |
| EP-MAP: GPS Mapping | 2 | 3 |
| EP-INV: Inventory Management | 2 | 4 |
| EP-TRACE: Supply Chain Traceability | 2 | 4 |
| EP-MKT: Marketplace | 2 | 3 |
| EP-COOP: Cooperative Management | 2 | 5 |
| EP-ACCT: Advanced Accounting | 2 | 3 |
| EP-IOT: IoT Integration | 3 | 5 |
| EP-GPS: GPS Animal Tracking | 3 | 4 |
| EP-CAM: Camera Surveillance | 3 | 4 |
| EP-AI: AI Farm Advisor | 3 | 4 |
| EP-DIR: Director Platform | 4 | 4 |
| EP-INTL: Multi-Country | 4 | 4 |
| **Total** | | **86** |
