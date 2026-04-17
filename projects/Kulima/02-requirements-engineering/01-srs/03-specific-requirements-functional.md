# 3 Specific Requirements — Functional

All functional requirements follow the stimulus-response pattern per IEEE Std 830-1998 Section 5.3.2. Each requirement uses "The system shall" to denote mandatory behaviour. Requirements are grouped by module and tagged with the deployment phase (1/2/3/4).

---

## 3.1 Farm and Plot Management

#### FR-FARM-001: Create Farm

**Phase:** 1

**Stimulus:** The user submits a new farm registration form with farm name, location (District, Sub-County, Parish, Village), total area (acres), and optionally GPS coordinates.
**Response:** The system shall create a new farm record under the authenticated tenant, assign a unique farm ID, associate the Uganda administrative hierarchy, store the area in acres, and convert to hectares and square metres for display.
**Pre-conditions:** The user is authenticated and the tenant's farm count has not reached the subscription tier limit.
**Post-conditions:** The farm record exists in the database; the user is redirected to the farm detail screen.
**Business Rule:** Each farm must have a unique name within the tenant. A single account can manage multiple farms within tier limits.

**Verifiability:** Create a farm named "Mbarara Estate" with District "Mbarara", area 50 acres. Verify the farm appears in the farm list, area displays as 50 acres / 20.23 hectares, and the farm ID is unique. Attempt to create a second farm with the same name — verify the system rejects it with a duplicate name error.

---

#### FR-FARM-002: Read Farm Details

**Phase:** 1

**Stimulus:** The user selects a farm from the farm list or dashboard.
**Response:** The system shall display the farm detail screen showing farm name, location hierarchy (District > Sub-County > Parish > Village), total area, number of plots, GPS coordinates (if recorded), land tenure type, creation date, and summary statistics (active crop seasons, animal count, financial balance).
**Pre-conditions:** The farm belongs to the authenticated tenant.
**Post-conditions:** No data modification occurs.

**Verifiability:** Navigate to farm "Mbarara Estate". Verify all fields (name, location, area, plot count, GPS, tenure, date, summary stats) render correctly. Verify a user from a different tenant cannot access this farm.

---

#### FR-FARM-003: Update Farm

**Phase:** 1

**Stimulus:** The user edits farm details and submits the update form.
**Response:** The system shall update the farm record with the modified fields and log the change in the audit trail with the previous values, user ID, and timestamp.
**Pre-conditions:** The user has Farm Owner or Farm Manager role for the farm.
**Post-conditions:** The farm record reflects the updated values; an audit log entry exists.

**Verifiability:** Change the farm name from "Mbarara Estate" to "Mbarara Estate Ltd". Verify the name updates, the audit log records the old name, the acting user, and the timestamp.

---

#### FR-FARM-004: Delete Farm

**Phase:** 1

**Stimulus:** The Farm Owner requests farm deletion and confirms the action via a confirmation dialog.
**Response:** The system shall soft-delete the farm and all associated plots, crop seasons, animals, financial records, tasks, and inventory records. The data shall be recoverable for 90 days.
**Pre-conditions:** The user has the Farm Owner role. A confirmation prompt is displayed and acknowledged.
**Post-conditions:** The farm and all child records are marked as deleted; they no longer appear in active views but remain in the database for 90 days.

**Verifiability:** Delete farm "Mbarara Estate Ltd". Verify it no longer appears in the farm list. Verify associated plots, crops, and animals are no longer visible. Verify a database query confirms records are soft-deleted with a deletion timestamp. Verify the data is recoverable within 90 days.

---

#### FR-FARM-005: Create Plot

**Phase:** 1

**Stimulus:** The user submits a new plot form specifying plot name, plot type (selected from 25+ system-defined types), area (acres), and parent farm.
**Response:** The system shall create a plot record linked to the specified farm. If the sum of all plot areas exceeds the farm's total area, the system shall display a warning but shall not block the operation.
**Pre-conditions:** The parent farm exists and belongs to the authenticated tenant.
**Post-conditions:** The plot record exists; the farm's plot count increments by 1.
**Business Rule:** Plot types are system-defined; farmers cannot create custom types. Plot area sum exceeding farm area triggers a warning, not a hard block.

**Verifiability:** Create a plot named "North Field" of type "Cropland" with area 10 acres under a farm with total area 50 acres. Verify the plot appears in the farm's plot list. Create additional plots totalling 55 acres — verify a warning is displayed but all plots are saved.

---

#### FR-FARM-006: Read Plot Details

**Phase:** 1

**Stimulus:** The user selects a plot from the farm's plot list.
**Response:** The system shall display the plot detail screen showing plot name, type, area, GPS polygon (if mapped), soil data (if recorded), irrigation data (if recorded), active crop seasons, and activity history.
**Pre-conditions:** The plot belongs to a farm owned by the authenticated tenant.
**Post-conditions:** No data modification occurs.

**Verifiability:** Navigate to plot "North Field". Verify all fields render correctly. Verify that active crop seasons on the plot are listed with their current status.

---

#### FR-FARM-007: Update Plot

**Phase:** 1

**Stimulus:** The user edits plot details and submits the update form.
**Response:** The system shall update the plot record and log the change in the audit trail.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The plot record reflects updated values; an audit log entry exists.

**Verifiability:** Change plot type from "Cropland" to "Orchard". Verify the type updates and the audit trail records the change.

---

#### FR-FARM-008: Delete Plot

**Phase:** 1

**Stimulus:** The user requests plot deletion and confirms via dialog.
**Response:** The system shall soft-delete the plot. If active crop seasons exist on the plot, the system shall warn the user and require explicit confirmation before proceeding.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The plot is soft-deleted; associated crop seasons are flagged for review.

**Verifiability:** Attempt to delete a plot with an active crop season — verify the warning is displayed. Confirm deletion — verify the plot is soft-deleted and the crop season is flagged.

---

#### FR-FARM-009: Record Soil Data

**Phase:** 1

**Stimulus:** The user enters soil data for a plot (soil type, pH, organic matter, texture, last test date).
**Response:** The system shall store the soil data record linked to the plot with the entry date.
**Pre-conditions:** The plot exists and belongs to the authenticated tenant's farm.
**Post-conditions:** The soil data record is persisted and displayed on the plot detail screen.

**Verifiability:** Enter soil data for plot "North Field" with pH 6.5, type "Loam". Verify the data displays on the plot detail screen with the correct date.

---

#### FR-FARM-010: Record Irrigation Data

**Phase:** 1

**Stimulus:** The user enters irrigation data for a plot (irrigation type, water source, schedule, flow rate).
**Response:** The system shall store the irrigation record linked to the plot.
**Pre-conditions:** The plot exists and belongs to the authenticated tenant's farm.
**Post-conditions:** The irrigation record is persisted and displayed on the plot detail screen.

**Verifiability:** Enter irrigation data for "North Field" with type "Drip", source "Borehole". Verify the data displays correctly on the plot detail screen.

---

#### FR-FARM-011: Record Land Tenure Type

**Phase:** 1

**Stimulus:** The user selects the land tenure type for a farm (Customary, Freehold, Leasehold, Mailo).
**Response:** The system shall store the tenure type on the farm record.
**Pre-conditions:** The farm exists and belongs to the authenticated tenant.
**Post-conditions:** The tenure type is persisted and displayed on the farm detail screen.

**Verifiability:** Set tenure type to "Mailo" for a farm. Verify it displays correctly on the farm detail screen.

---

#### FR-FARM-012: Uganda Administrative Hierarchy Selection

**Phase:** 1

**Stimulus:** The user selects the farm location by navigating the administrative hierarchy (District → Sub-County → Parish → Village).
**Response:** The system shall present cascading dropdown menus pre-loaded with Uganda's administrative hierarchy. Each selection filters the next level. The selected hierarchy is stored with the farm record.
**Pre-conditions:** The administrative hierarchy reference data is loaded in the system (or pre-loaded on the mobile device for offline use).
**Post-conditions:** The farm record stores the full hierarchy (district_id, subcounty_id, parish_id, village_id).

**Verifiability:** Select District "Mbarara", verify Sub-County options load for Mbarara only. Select Sub-County, verify Parish options filter accordingly. Complete the full hierarchy and verify all 4 levels are stored with the farm.

---

#### FR-FARM-013: Farm Switcher

**Phase:** 1

**Stimulus:** The user taps the farm switcher control (available on all screens).
**Response:** The system shall display a list of all farms belonging to the authenticated tenant. Upon selection, the system shall switch the active farm context and reload the current screen with data from the selected farm.
**Pre-conditions:** The tenant has 2 or more farms.
**Post-conditions:** The active farm context is updated; all data displayed reflects the selected farm.

**Verifiability:** Create 2 farms. Verify the farm switcher lists both. Select the second farm — verify all dashboard data, plots, and records reflect the second farm.

---

#### FR-FARM-014: Multiple Farms per Account

**Phase:** 1

**Stimulus:** The user attempts to create a new farm when they already have one or more farms.
**Response:** The system shall check the tenant's subscription tier farm limit. If the limit is not reached, the system shall allow farm creation. If the limit is reached, the system shall display a clear upgrade prompt with tier comparison.
**Pre-conditions:** The user is authenticated.
**Post-conditions:** Either a new farm is created or an upgrade prompt is displayed.
**Business Rule:** Tier limits enforced at API level before any write operation. Exceeding a limit returns a clear upgrade prompt, never silently truncates data.

**Verifiability:** On a "Seedling" (free) tier limited to 1 farm, create 1 farm successfully. Attempt to create a second — verify the upgrade prompt appears and no farm is created.

---

#### FR-FARM-015: GPS Polygon Farm Boundary Mapping

**Phase:** 2

**Stimulus:** The user initiates boundary mapping by either walking the perimeter with the GPS module active or drawing on satellite imagery in the map view.
**Response:** The system shall record GPS coordinates as a GeoJSON polygon with accuracy within 5 metres. The polygon is stored in a MySQL JSON column with spatial indexing. The calculated area from the polygon is displayed alongside the manually entered area.
**Pre-conditions:** The device has GPS capability and location permissions are granted. Google Maps SDK or OpenStreetMap tiles are available.
**Post-conditions:** The GeoJSON polygon is stored with the farm record. The farm overview map displays the boundary.

**Verifiability:** Walk a known boundary of a 2-acre plot. Verify the captured polygon area is within $\pm 5\%$ of 2 acres. Verify the GeoJSON is valid and renders on the map.

---

## 3.2 Crop Management

#### FR-CROP-001: Browse Crop Library

**Phase:** 1

**Stimulus:** The user opens the crop library screen or searches for a crop by name.
**Response:** The system shall display a searchable list of 200+ pre-loaded crops with scientific name, common English name, and local names (Luganda, Swahili, Kinyarwanda). Each crop entry shows the crop category (cereal, legume, root/tuber, fruit, vegetable, cash crop, fodder).
**Pre-conditions:** The crop library reference data is loaded (pre-loaded on mobile for offline use).
**Post-conditions:** No data modification occurs.

**Verifiability:** Search for "coffee". Verify that both Arabica and Robusta appear with their scientific names, local names, and category "Cash Crop". Verify the search works offline.

---

#### FR-CROP-002: Select Crop Variety

**Phase:** 1

**Stimulus:** The user selects a crop from the library and views available varieties/cultivars.
**Response:** The system shall display the varieties for the selected crop, each showing: variety name, maturity period (days), expected yield per acre, recommended planting season, and key characteristics.
**Pre-conditions:** The crop exists in the crop library.
**Post-conditions:** No data modification occurs.

**Verifiability:** Select "Coffee (Arabica)". Verify varieties are listed (e.g., SL14, SL28, KP423) with maturity periods and expected yields. Verify these values match the pre-loaded reference data.

---

#### FR-CROP-003: Create Season Plan

**Phase:** 1

**Stimulus:** The user creates a new crop season by selecting a plot, crop variety, planting date, expected harvest date, target area, and target yield.
**Response:** The system shall create a crop season record linking the plot, crop variety, and date range. The system shall calculate the expected yield based on the variety's benchmark yield per acre multiplied by the target area.
**Pre-conditions:** The plot exists and belongs to the tenant's farm. The crop variety exists in the library.
**Post-conditions:** The crop season record exists with status "Planned". The season appears on the farm calendar and plot detail screen.
**Business Rule:** A crop season is linked to exactly one plot and one crop variety. Multiple seasons can run simultaneously on different plots.

**Verifiability:** Create a season for "Maize (Longe 10H)" on "North Field" (10 acres), planned planting 1 March. Verify the expected yield calculates as $10 \times 3.5 = 35$ bags (assuming 3.5 bags/acre benchmark). Verify the season appears on the calendar with status "Planned".

---

#### FR-CROP-004: Record Planting

**Phase:** 1

**Stimulus:** The user records that planting has occurred for a crop season, entering actual planting date, seed quantity used, planting method, and spacing.
**Response:** The system shall update the crop season status from "Planned" to "Planted" and store the planting details. If input tracking is enabled, the seed quantity shall be recorded as an input usage.
**Pre-conditions:** A crop season exists with status "Planned".
**Post-conditions:** The crop season status is "Planted"; planting details are stored; seed input usage is recorded.

**Verifiability:** Record planting for the maize season with date 5 March, 25kg seed, spacing 75cm x 30cm. Verify the season status changes to "Planted" and the planting details display correctly.

---

#### FR-CROP-005: Record Crop Activity

**Phase:** 1

**Stimulus:** The user records a crop activity by selecting the crop season, activity type (from 20+ system-defined types: weeding, spraying, fertilising, pruning, thinning, irrigating, mulching, scouting, pest control, disease control, soil amendment, transplanting, staking, trellising, harvesting, drying, sorting, grading, packing, transporting), activity date, labour hours, and notes.
**Response:** The system shall create an activity record linked to the crop season with all entered details.
**Pre-conditions:** A crop season exists with status "Planted" or "Active".
**Post-conditions:** The activity record is stored; the crop season's activity timeline is updated.

**Verifiability:** Record a "Spraying" activity on 20 March with 3 labour hours. Verify the activity appears in the season timeline with correct date, type, and hours.

---

#### FR-CROP-006: Track Inputs per Activity

**Phase:** 1

**Stimulus:** While recording a crop activity, the user adds one or more inputs (e.g., pesticide name, quantity, unit, cost).
**Response:** The system shall store each input usage record linked to the activity. If inventory management is enabled (Phase 2+), the system shall automatically deduct the used quantity from the input inventory.
**Pre-conditions:** The activity record is being created or already exists.
**Post-conditions:** Input usage records are stored; inventory is deducted if applicable.
**Business Rule:** Input usage recorded during activities automatically deducts from input inventory.

**Verifiability:** Record a spraying activity with input "Ridomil Gold" (2kg, UGX 40,000). Verify the input appears linked to the activity. In Phase 2+, verify the input inventory decreases by 2kg.

---

#### FR-CROP-007: Record Crop Health Event with Photo

**Phase:** 1

**Stimulus:** The user records a crop health event by selecting the crop season, health event type (pest sighting, disease symptom, nutrient deficiency, weed pressure, weather damage), severity (Low, Medium, High, Critical), affected area percentage, and optionally attaching a photo.
**Response:** The system shall store the health event with all details. Photos shall be compressed to a maximum of 512KB before storage. The event appears on the crop season health timeline.
**Pre-conditions:** A crop season exists.
**Post-conditions:** The health event record and photo (if provided) are stored.

**Verifiability:** Record a "Pest Sighting" event with severity "High", affected area 30%, and attach a photo. Verify the event displays in the health timeline. Verify the stored photo is $\leq$ 512KB.

---

#### FR-CROP-008: AI Pest/Disease Identification from Photo

**Phase:** 3

**Stimulus:** The user uploads a photo of a crop health issue and requests AI identification.
**Response:** The system shall send the photo to the Claude Vision API with the crop type and region context. The system shall display the AI's identification (pest/disease name, confidence level, recommended treatment) within 10 seconds. If confidence is below 70%, the system shall recommend consulting an extension officer.
**Pre-conditions:** The device has internet connectivity. The tenant's AI query count has not reached the subscription tier limit.
**Post-conditions:** The AI identification result is stored with the health event record.
**Business Rule:** Extension officer escalation on low confidence.

**Verifiability:** Upload a photo of Fall Armyworm damage on maize. Verify the API returns an identification within 10 seconds. Verify the result includes pest name, confidence percentage, and treatment recommendation. Test with an ambiguous photo — verify the extension officer referral message appears when confidence is below 70%.

---

#### FR-CROP-009: Record Harvest

**Phase:** 1

**Stimulus:** The user records a harvest event by entering the crop season, harvest date, quantity harvested (kg/bags/tonnes), quality grade (A/B/C), and storage destination.
**Response:** The system shall store the harvest record and update the crop season status to "Harvested". The system shall calculate the actual yield per acre as $\text{Yield} = \frac{\text{Quantity Harvested}}{\text{Plot Area (acres)}}$.
**Pre-conditions:** A crop season exists with status "Planted" or "Active".
**Post-conditions:** The harvest record is stored; the crop season status is "Harvested"; yield per acre is calculated and stored.
**Business Rule:** Harvest records must specify a storage destination.

**Verifiability:** Record a harvest of 30 bags of maize from 10 acres. Verify the yield calculates as $\frac{30}{10} = 3.0$ bags/acre. Verify the season status changes to "Harvested". Verify the storage destination is recorded.

---

#### FR-CROP-010: Yield Analysis

**Phase:** 1

**Stimulus:** The user views the yield analysis report for a completed crop season.
**Response:** The system shall display actual yield per acre compared to the variety's expected yield per acre, calculated as a percentage: $\text{Achievement} = \frac{\text{Actual Yield}}{\text{Expected Yield}} \times 100\%$. The system shall display a historical trend of yields for the same crop variety across seasons.
**Pre-conditions:** At least one harvest record exists for the crop season.
**Post-conditions:** No data modification occurs.

**Verifiability:** For a maize season with actual yield 3.0 bags/acre and expected yield 3.5 bags/acre, verify the achievement displays as $\frac{3.0}{3.5} \times 100 = 85.7\%$. Verify historical data from previous seasons is charted.

---

#### FR-CROP-011: Crop Rotation Planner

**Phase:** 1

**Stimulus:** The user opens the crop rotation view for a plot.
**Response:** The system shall display the history of crops grown on the plot across all seasons in chronological order. The system shall flag consecutive same-crop plantings with a rotation advisory.
**Pre-conditions:** The plot has at least one completed crop season.
**Post-conditions:** No data modification occurs.

**Verifiability:** View rotation history for a plot that grew maize for 3 consecutive seasons. Verify a rotation advisory warning is displayed. Verify the chronological crop history renders correctly.

---

#### FR-CROP-012: Season Calendar View

**Phase:** 1

**Stimulus:** The user opens the season calendar.
**Response:** The system shall display a calendar view showing all crop seasons across all plots on the active farm, colour-coded by crop type, with planting and expected harvest dates visible. Uganda's two growing seasons (Season A: March-June, Season B: August-November) shall be overlaid as reference bands.
**Pre-conditions:** At least one crop season exists on the active farm.
**Post-conditions:** No data modification occurs.

**Verifiability:** Create seasons on 3 different plots. Open the calendar — verify all 3 appear with correct date ranges. Verify Season A and Season B reference bands display.

---

#### FR-CROP-013: Uganda Crop Calendar

**Phase:** 1

**Stimulus:** The user views the MAAIF crop calendar for a specific crop.
**Response:** The system shall display the recommended planting, maintenance, and harvest windows for the selected crop based on Uganda's agro-ecological zones and the farm's district.
**Pre-conditions:** The crop exists in the library with MAAIF calendar data.
**Post-conditions:** No data modification occurs.

**Verifiability:** View the crop calendar for coffee in Kasese District. Verify the planting and harvest windows match MAAIF recommendations for the western Uganda agro-ecological zone.

---

#### FR-CROP-014: Common Pest/Disease Alerts

**Phase:** 1

**Stimulus:** The user creates a crop season for a crop that has pre-configured regional pest/disease alerts (e.g., Fall Armyworm for maize, Cassava Mosaic for cassava, BXW for banana, Coffee Wilt for coffee).
**Response:** The system shall display region-specific pest/disease watch notices on the crop season detail screen. If the crop health monitoring detects a matching symptom, the system shall cross-reference the alert database.
**Pre-conditions:** The crop has pre-configured pest/disease alerts in the reference data.
**Post-conditions:** Alert notices are displayed on the crop season screen.

**Verifiability:** Create a maize season. Verify that "Fall Armyworm Watch" notice appears on the season detail screen. Create a banana season — verify "BXW Watch" appears.

---

#### FR-CROP-015: Intercropping Support

**Phase:** 1

**Stimulus:** The user creates multiple crop seasons on the same plot with overlapping date ranges.
**Response:** The system shall allow multiple simultaneous crop seasons on a single plot (e.g., maize + beans intercrop). Each season is tracked independently with its own activities, inputs, and harvest records.
**Pre-conditions:** The plot exists.
**Post-conditions:** Multiple crop seasons exist on the same plot with overlapping dates.
**Business Rule:** Multiple crop seasons can run simultaneously on different plots — this extends to the same plot for intercropping.

**Verifiability:** Create a maize season and a bean season on the same plot with overlapping dates. Verify both appear in the plot's season list. Record activities independently for each — verify they remain separate.

---

#### FR-CROP-016: Activity Type Library

**Phase:** 1

**Stimulus:** The user opens the activity type selection when recording a crop activity.
**Response:** The system shall display a list of 20+ system-defined activity types: Land Preparation, Ploughing, Harrowing, Ridging, Planting, Transplanting, Weeding, Thinning, Pruning, Spraying, Fertilising, Top Dressing, Irrigating, Mulching, Staking, Trellising, Scouting, Pest Control, Disease Control, Harvesting, Drying, Sorting, Grading, Packing, Transporting.
**Pre-conditions:** A crop season exists.
**Post-conditions:** No data modification occurs.

**Verifiability:** Open the activity type selector. Verify at least 20 activity types are listed. Verify each has a name and icon.

---

#### FR-CROP-017: Crop Season Status Transitions

**Phase:** 1

**Stimulus:** The user performs actions that trigger status changes on a crop season.
**Response:** The system shall enforce the following status transitions: Planned → Planted → Active → Harvested → Completed. The transition from Planted to Active occurs automatically when the first activity is recorded. The transition to Harvested occurs when a harvest record is created. The transition to Completed is manual.
**Pre-conditions:** The crop season exists.
**Post-conditions:** The status updates according to the defined transition rules.

**Verifiability:** Create a season (status: Planned). Record planting (status: Planted). Record a weeding activity (status: Active). Record a harvest (status: Harvested). Mark complete (status: Completed). Verify each transition occurs correctly and that skipping states (e.g., Planned → Harvested) is blocked.

---

#### FR-CROP-018: Enterprise Type Tagging

**Phase:** 1

**Stimulus:** The user creates a crop season.
**Response:** The system shall automatically tag the crop season with an enterprise type based on the crop (e.g., "Maize Enterprise", "Coffee Enterprise") for financial profitability analysis.
**Pre-conditions:** The crop exists in the library with an enterprise type mapping.
**Post-conditions:** The enterprise type is stored with the crop season.

**Verifiability:** Create a coffee crop season. Verify the enterprise type "Coffee Enterprise" is automatically assigned. Verify this enterprise type is available for filtering in financial reports.

---

#### FR-CROP-019: Crop Season Summary Dashboard

**Phase:** 1

**Stimulus:** The user views the crop season summary.
**Response:** The system shall display a summary card for the season showing: crop name, plot name, planting date, days since planting, total activities recorded, total input cost, total labour hours, harvest quantity (if harvested), and yield analysis.
**Pre-conditions:** A crop season exists.
**Post-conditions:** No data modification occurs.

**Verifiability:** View a season with 5 activities, UGX 200,000 in inputs, 15 labour hours. Verify all values display correctly on the summary card.

---

#### FR-CROP-020: Matooke Enterprise Tracking

**Phase:** 1

**Stimulus:** The user creates a crop season for matooke (banana) with a specific variety (Mbwazirume, Nakitembe, Nfuuka).
**Response:** The system shall track matooke-specific metrics: number of stools, bunch weight per harvest cycle, ratoon management, sucker selection records, and the perennial nature of the crop (no end date on the season).
**Pre-conditions:** The crop variety is a matooke/banana variety.
**Post-conditions:** Matooke-specific tracking fields are enabled on the crop season.

**Verifiability:** Create a matooke season with variety "Mbwazirume". Verify the season has no end date (perennial). Verify fields for stool count, bunch weight, and sucker selection are available.

---

## 3.3 Livestock Management

#### FR-LIVE-001: Species and Breed Library

**Phase:** 1

**Stimulus:** The user opens the species/breed selection when registering an animal.
**Response:** The system shall display a list of supported species (cattle, goats, sheep, pigs, chickens, ducks, turkeys, rabbits, donkeys, horses, bees, fish) with breeds per species and breed-specific benchmarks (expected milk yield, growth rate, egg production, gestation period).
**Pre-conditions:** The species and breed reference data is pre-loaded.
**Post-conditions:** No data modification occurs.

**Verifiability:** Browse cattle breeds. Verify "Ankole Longhorn" and "Holstein Friesian" appear with different milk yield benchmarks. Verify offline access to the breed library.

---

#### FR-LIVE-002: Register Individual Animal

**Phase:** 1

**Stimulus:** The user registers a new animal by entering species, breed, tag/ID (ear tag, RFID, or name), sex, date of birth (or estimated age), colour/markings, acquisition method (born on farm, purchased, donated), acquisition date, and acquisition cost.
**Response:** The system shall create an individual animal record with status "Active" and assign it to the active farm. For species requiring individual tracking (cattle, goats, sheep, pigs, donkeys, horses), each animal shall have a unique tag within the tenant.
**Pre-conditions:** The tenant's animal count has not reached the subscription tier limit.
**Post-conditions:** The animal record exists with status "Active".
**Business Rule:** Individual tracking is mandatory for cattle, goats, sheep, pigs, donkeys, horses. Flock-level management is permitted for poultry and rabbits.

**Verifiability:** Register a cow with tag "AK-001", breed "Ankole Longhorn", sex "Female", DOB 15 January 2023. Verify the animal appears in the livestock list with all entered details. Attempt to register another animal with tag "AK-001" — verify duplication is rejected.

---

#### FR-LIVE-003: Animal Status Management

**Phase:** 1

**Stimulus:** The user changes an animal's status.
**Response:** The system shall enforce the following status transitions: Active → Sold, Active → Deceased, Active → Slaughtered, Active → Lost, Active → Quarantine, Active → Transferred. The system shall require a reason and date for each transition. Status "Sold" requires sale price and buyer information. Status "Deceased" requires cause of death.
**Pre-conditions:** The animal exists with status "Active" (or "Quarantine" transitioning back to "Active").
**Post-conditions:** The animal status is updated; the transition is logged in the audit trail.
**Business Rule:** Status transitions follow defined paths.

**Verifiability:** Change animal "AK-001" status from Active to Sold with price UGX 2,500,000 and buyer "John". Verify the status updates, sale details are stored, and the animal no longer appears in the active herd count.

---

#### FR-LIVE-004: Pedigree Tracking

**Phase:** 1

**Stimulus:** The user records sire and dam for an animal.
**Response:** The system shall link the animal to its sire and dam records within the same tenant. The system shall display a pedigree tree (up to 3 generations) on the animal detail screen.
**Pre-conditions:** The sire and dam animals exist within the same tenant.
**Post-conditions:** The pedigree links are stored; the pedigree tree is displayable.
**Business Rule:** Pedigree links must reference animals within the same tenant.

**Verifiability:** Register a calf with sire "AK-005" and dam "AK-001". Verify the pedigree tree shows the parents. Register a grandchild — verify 3-generation display.

---

#### FR-LIVE-005: Weight Tracking

**Phase:** 1

**Stimulus:** The user records a weight measurement for an animal (weight in kg, date, measurement method).
**Response:** The system shall store the weight record and display a growth chart showing weight over time. The system shall calculate Average Daily Gain (ADG) as $\text{ADG} = \frac{W_2 - W_1}{D_2 - D_1}$ where $W$ is weight and $D$ is date.
**Pre-conditions:** The animal exists.
**Post-conditions:** The weight record is stored; the growth chart and ADG update.

**Verifiability:** Record weights of 150kg on 1 January and 180kg on 1 April (90 days). Verify ADG calculates as $\frac{180 - 150}{90} = 0.33$ kg/day. Verify the growth chart plots both points.

---

#### FR-LIVE-006: Vaccination Record

**Phase:** 1

**Stimulus:** The user records a vaccination event for an animal or group of animals by selecting vaccination type, vaccine name, batch number, date administered, next due date, and administering officer.
**Response:** The system shall store the vaccination record and schedule a reminder notification for the next due date.
**Pre-conditions:** The animal(s) exist with status "Active".
**Post-conditions:** The vaccination record is stored; a reminder is scheduled for the next due date.
**Business Rule:** Vaccination and treatment records must include the next due date where applicable.

**Verifiability:** Record an FMD vaccination for animal "AK-001" on 1 March with next due date 1 September. Verify the record displays in the health history. Verify a reminder notification is generated for 1 September.

---

#### FR-LIVE-007: Treatment Record

**Phase:** 1

**Stimulus:** The user records a treatment event for an animal (diagnosis, treatment type, medicine name, dosage, route, duration, cost, vet name, next follow-up date).
**Response:** The system shall store the treatment record and schedule a follow-up reminder if a next date is provided.
**Pre-conditions:** The animal exists.
**Post-conditions:** The treatment record is stored; a follow-up reminder is scheduled if applicable.

**Verifiability:** Record treatment for East Coast Fever: diagnosis "ECF", medicine "Buparvaquone", dosage "2.5mg/kg", cost UGX 45,000, follow-up 7 March. Verify all details display in the health history. Verify a reminder is set for 7 March.

---

#### FR-LIVE-008: Deworming Record

**Phase:** 1

**Stimulus:** The user records a deworming event for an animal or group (dewormer name, dosage, date, next due date).
**Response:** The system shall store the deworming record and schedule a reminder for the next due date.
**Pre-conditions:** The animal(s) exist with status "Active".
**Post-conditions:** The deworming record is stored; a reminder is scheduled.

**Verifiability:** Record deworming with "Albendazole" on 1 March, next due 1 June. Verify the record and reminder are created.

---

#### FR-LIVE-009: Reproduction — Mating Record

**Phase:** 1

**Stimulus:** The user records a mating event (female animal, male animal or AI sire, mating date, mating method: natural/AI).
**Response:** The system shall store the mating record and calculate the expected calving/kidding/farrowing date based on species-specific gestation period.
**Pre-conditions:** The female animal exists with status "Active".
**Post-conditions:** The mating record is stored; the expected birth date is calculated and a reminder is scheduled.

**Verifiability:** Record mating for cow "AK-001" on 1 March. Verify the expected calving date calculates as approximately 5 December (283 days gestation for cattle). Verify a reminder is scheduled.

---

#### FR-LIVE-010: Reproduction — Pregnancy Check

**Phase:** 1

**Stimulus:** The user records a pregnancy check result (positive/negative/inconclusive, check date, method, checked by).
**Response:** The system shall update the mating record with the pregnancy check result. If positive, the system shall maintain the expected birth date. If negative, the system shall clear the expected birth date and flag the animal for re-breeding.
**Pre-conditions:** A mating record exists for the animal.
**Post-conditions:** The pregnancy check result is recorded; expected birth date is maintained or cleared.

**Verifiability:** Record a positive pregnancy check for "AK-001" on 15 April. Verify the expected calving date remains. Record a negative check for another animal — verify the expected birth date is cleared.

---

#### FR-LIVE-011: Reproduction — Birth Record

**Phase:** 1

**Stimulus:** The user records a birth event (mother, date, number of offspring, sex of each, birth weight, birth type: normal/assisted/caesarean, sire if known).
**Response:** The system shall create new animal records for each offspring with pedigree links to the dam and sire. The system shall update the dam's reproduction history.
**Pre-conditions:** The dam exists with an active pregnancy record.
**Post-conditions:** New animal records are created for offspring; pedigree links are established; the dam's reproduction history is updated.

**Verifiability:** Record a birth for "AK-001": 1 female calf, birth weight 28kg. Verify a new animal record is created with dam "AK-001" and the correct sire. Verify the dam's birth count increments.

---

#### FR-LIVE-012: Milk Production Record

**Phase:** 1

**Stimulus:** The user records milk production for a cow (date, session: morning/evening/midday, quantity in litres).
**Response:** The system shall store the milk record and update the daily/weekly/monthly production totals. The system shall compare actual production against breed-specific benchmarks.
**Pre-conditions:** The animal is female and belongs to a dairy species.
**Post-conditions:** The milk record is stored; production summaries update.
**Business Rule:** Milk production records require session identification (morning/evening/midday).

**Verifiability:** Record morning milk for "AK-001": 5 litres on 1 March. Record evening milk: 4 litres. Verify daily total displays as 9 litres. Verify the Ankole Longhorn benchmark comparison is shown.

---

#### FR-LIVE-013: Egg Production Record

**Phase:** 1

**Stimulus:** The user records egg collection for a poultry flock (date, quantity, grade, breakage count).
**Response:** The system shall store the egg record at the flock level and calculate the laying rate as $\text{Laying Rate} = \frac{\text{Eggs Collected}}{\text{Active Hens}} \times 100\%$.
**Pre-conditions:** A poultry flock exists with a recorded hen count.
**Post-conditions:** The egg record is stored; the laying rate is calculated.

**Verifiability:** Record 25 eggs from a flock of 30 hens. Verify the laying rate calculates as $\frac{25}{30} \times 100 = 83.3\%$.

---

#### FR-LIVE-014: Honey Production Record

**Phase:** 1

**Stimulus:** The user records a honey harvest from a beehive (date, quantity in kg, quality grade, hive ID).
**Response:** The system shall store the honey harvest record linked to the specific hive/apiary plot.
**Pre-conditions:** A bee enterprise exists on the farm with at least one hive registered.
**Post-conditions:** The honey harvest record is stored.

**Verifiability:** Record 12kg of honey from Hive H-003 on 15 May. Verify the record displays in the apiary production history with the correct hive reference.

---

#### FR-LIVE-015: Feeding Record

**Phase:** 1

**Stimulus:** The user records a feeding event for an animal or group (feed type, quantity, cost, date).
**Response:** The system shall store the feeding record. If inventory management is active, the system shall deduct the feed quantity from feed stock.
**Pre-conditions:** The animal or group exists.
**Post-conditions:** The feeding record is stored; feed inventory is updated if applicable.

**Verifiability:** Record feeding of 5kg dairy meal to "AK-001" on 1 March, cost UGX 10,000. Verify the record displays in the animal's feeding history.

---

#### FR-LIVE-016: Movement Log

**Phase:** 1

**Stimulus:** The user records a movement event for an animal (from location, to location, date, reason, movement permit number if applicable).
**Response:** The system shall store the movement record and update the animal's current location.
**Pre-conditions:** The animal exists with status "Active".
**Post-conditions:** The movement record is stored; the animal's location is updated.

**Verifiability:** Record movement of "AK-001" from "Farm A - Paddock 1" to "Farm A - Paddock 3" on 1 March. Verify the animal's current location updates to "Paddock 3".

---

#### FR-LIVE-017: Sale Record

**Phase:** 1

**Stimulus:** The user records a sale event for an animal (sale date, sale price, buyer name, buyer contact, payment method).
**Response:** The system shall change the animal's status to "Sold", store the sale details, and create a corresponding income record in the financial module tagged to the livestock enterprise.
**Pre-conditions:** The animal exists with status "Active".
**Post-conditions:** The animal status is "Sold"; a financial income record is created.
**Business Rule:** Status "Sold" requires sale price and buyer information.

**Verifiability:** Record sale of "AK-001" for UGX 2,500,000 to "John Okello" via MoMo on 15 March. Verify the animal status is "Sold". Verify a UGX 2,500,000 income record appears in financial records tagged to "Cattle Enterprise".

---

#### FR-LIVE-018: Mortality Record

**Phase:** 1

**Stimulus:** The user records a mortality event (animal, date, cause of death, disposal method, financial loss estimate).
**Response:** The system shall change the animal's status to "Deceased" and store the mortality details.
**Pre-conditions:** The animal exists with status "Active" or "Quarantine".
**Post-conditions:** The animal status is "Deceased"; mortality details are stored.

**Verifiability:** Record death of "AK-002" on 10 March, cause "East Coast Fever", disposal "Buried". Verify the animal status is "Deceased" and the cause of death displays in the animal record.

---

#### FR-LIVE-019: Herd Summary Dashboard

**Phase:** 1

**Stimulus:** The user opens the livestock dashboard for the active farm.
**Response:** The system shall display a summary including: total animals by species, total by status (active, sold, deceased), sex ratio, age distribution, upcoming vaccinations, upcoming dewormings, recent health events, production totals (daily milk, weekly eggs), and recent births.
**Pre-conditions:** At least one animal exists on the active farm.
**Post-conditions:** No data modification occurs.

**Verifiability:** On a farm with 20 cattle (15 active, 3 sold, 2 deceased), 30 chickens (flock), verify all counts display correctly. Verify upcoming vaccination reminders show within the next 30 days.

---

#### FR-LIVE-020: Flock Management

**Phase:** 1

**Stimulus:** The user manages poultry or rabbits at the flock level, recording flock size adjustments (additions, removals, mortalities) rather than individual animals.
**Response:** The system shall maintain a flock-level record with current size, tracking additions (purchases, hatches), removals (sales, culling), and mortalities with running totals.
**Pre-conditions:** The species is poultry or rabbits (flock-eligible).
**Post-conditions:** The flock size is updated; the adjustment is logged.
**Business Rule:** Flock-level management (not individual) is permitted for poultry and rabbits.

**Verifiability:** Create a chicken flock of 100 birds. Record a purchase of 50 chicks and a mortality of 3. Verify the flock size updates to 147. Verify the adjustment history shows all 3 events.

---

## 3.4 Financial Records

#### FR-FIN-001: Record Income

**Phase:** 1

**Stimulus:** The user records farm income by entering date, amount (UGX), source category (crop sales, livestock sales, milk sales, egg sales, other), description, payment method (cash, MoMo, Airtel Money, bank transfer, cheque), and optionally linking to a farm and enterprise type.
**Response:** The system shall create an income record linked to the farm and enterprise type. The system shall store the mobile money transaction ID if payment method is MoMo or Airtel Money.
**Pre-conditions:** The user is authenticated and has Farm Owner or Farm Manager role.
**Post-conditions:** The income record is stored.
**Business Rule:** Every income record must be linked to a farm and optionally to an enterprise type.

**Verifiability:** Record income of UGX 500,000 from "Crop Sales" (maize) via MoMo with transaction ID "TXN123456". Verify the record appears in financial records with all details.

---

#### FR-FIN-002: Record Expense

**Phase:** 1

**Stimulus:** The user records a farm expense by entering date, amount (UGX), category (inputs, labour, transport, equipment, veterinary, feed, fuel, rent, utilities, other), description, payment method, and optionally linking to a specific activity.
**Response:** The system shall create an expense record linked to the farm, enterprise type, and optionally to a specific crop or livestock activity.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The expense record is stored.

**Verifiability:** Record expense of UGX 80,000 for "Inputs" (fertiliser) on 5 March. Verify the record appears in financial records with the correct category and date.

---

#### FR-FIN-003: Link Expense to Activity

**Phase:** 1

**Stimulus:** While recording an expense, the user selects an existing crop or livestock activity to link to.
**Response:** The system shall create a link between the expense record and the activity, enabling per-activity cost analysis.
**Pre-conditions:** The activity record exists.
**Post-conditions:** The expense is linked to the activity; activity cost totals update.

**Verifiability:** Link a UGX 40,000 expense to a "Spraying" activity. Verify the activity's total cost includes this expense. Verify the enterprise profitability report includes this cost.

---

#### FR-FIN-004: Budget Planning

**Phase:** 1

**Stimulus:** The user creates a budget for a season or year by entering budget lines (category, planned amount) for each enterprise or the whole farm.
**Response:** The system shall store the budget records with the specified period and categories.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The budget record is stored and available for comparison with actuals.

**Verifiability:** Create a Season A 2026 budget with 5 line items totalling UGX 3,000,000. Verify each line item and the total display correctly.

---

#### FR-FIN-005: Budget vs Actuals

**Phase:** 1

**Stimulus:** The user views the budget comparison report for a period.
**Response:** The system shall display each budget category with the planned amount, actual amount, and variance: $\text{Variance} = \text{Actual} - \text{Planned}$. Positive variance (overspend) shall be highlighted in red; negative variance (underspend) in green.
**Pre-conditions:** A budget exists and actual income/expense records exist for the same period.
**Post-conditions:** No data modification occurs.

**Verifiability:** With a "Inputs" budget of UGX 500,000 and actual expenses of UGX 620,000, verify the variance displays as +UGX 120,000 highlighted in red.

---

#### FR-FIN-006: Enterprise Profitability

**Phase:** 1

**Stimulus:** The user views the enterprise profitability report for a specified period.
**Response:** The system shall calculate profitability per enterprise type as $\text{Profit} = \text{Income} - \text{Expenses}$ for the period. The report shall list each enterprise with total income, total expenses, and net profit/loss.
**Pre-conditions:** Income and expense records exist with enterprise type tags.
**Post-conditions:** No data modification occurs.
**Business Rule:** Enterprise profitability is calculated by summing income minus expenses per enterprise type per period.

**Verifiability:** With maize income UGX 2,000,000 and maize expenses UGX 1,200,000, verify the maize enterprise profit displays as UGX 800,000.

---

#### FR-FIN-007: Cash Flow Summary

**Phase:** 1

**Stimulus:** The user views the cash flow summary for a specified period (monthly/quarterly/annual).
**Response:** The system shall display a bar chart showing total income and total expenses per period, with net cash flow. The chart shall allow period drill-down.
**Pre-conditions:** Income and expense records exist for the specified period.
**Post-conditions:** No data modification occurs.

**Verifiability:** View monthly cash flow for January-June. Verify each month shows income and expense bars. Verify the net cash flow line matches $\text{Income} - \text{Expenses}$ for each month.

---

#### FR-FIN-008: Market Price Recording

**Phase:** 1

**Stimulus:** The user records a market price observation (crop/product, market name, price per unit, unit, date).
**Response:** The system shall store the price record and display it in the price history timeline for the product.
**Pre-conditions:** The user is authenticated.
**Post-conditions:** The price record is stored.
**Business Rule:** Market prices are recorded per crop per market per date; the system does not fetch prices automatically in Phase 1.

**Verifiability:** Record maize price at Kalerwe Market: UGX 2,500/kg on 1 March. Verify the record appears in the price history for maize.

---

#### FR-FIN-009: Loan Tracking

**Phase:** 1

**Stimulus:** The user records a loan (lender: SACCO/MFI/bank/mobile money, principal amount, interest rate, term, start date, repayment schedule).
**Response:** The system shall store the loan record and calculate the outstanding balance. The user can manually record repayments against the loan.
**Pre-conditions:** The user has Farm Owner role.
**Post-conditions:** The loan record is stored with calculated outstanding balance.
**Business Rule:** Loans must track outstanding balance; the system does not auto-deduct repayments.

**Verifiability:** Record a SACCO loan of UGX 5,000,000 at 2% monthly interest. Record a repayment of UGX 500,000. Verify the outstanding balance updates to UGX 4,500,000 (plus accrued interest per the loan terms).

---

#### FR-FIN-010: Receipt Photo Upload

**Phase:** 1

**Stimulus:** The user attaches a photo of a receipt to an income or expense record.
**Response:** The system shall compress the photo to a maximum of 512KB and store it linked to the financial record.
**Pre-conditions:** The financial record exists.
**Post-conditions:** The receipt photo is stored and viewable from the financial record detail screen.

**Verifiability:** Upload a receipt photo to an expense record. Verify the photo displays when viewing the expense detail. Verify the stored photo is $\leq$ 512KB.

---

#### FR-FIN-011: Export PDF/Excel

**Phase:** 1

**Stimulus:** The user requests a financial report export in PDF or Excel format.
**Response:** The system shall generate a formatted report (income statement, expense report, cash flow, or enterprise profitability) and download it in the requested format.
**Pre-conditions:** Financial records exist for the selected period.
**Post-conditions:** The file is generated and available for download.

**Verifiability:** Export a 6-month income statement as PDF. Verify the PDF contains all income and expense line items, totals, and date range. Verify it opens correctly in a PDF reader.

---

#### FR-FIN-012: Invoice Generation

**Phase:** 1

**Stimulus:** The user creates an invoice by entering buyer details, line items (product, quantity, unit price), payment terms, and due date.
**Response:** The system shall generate a formatted invoice with a unique invoice number and store it linked to the farm.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The invoice is stored and available for PDF export.

**Verifiability:** Generate an invoice for 100 bags of maize at UGX 250,000/bag to "ABC Trading Ltd". Verify the invoice total is UGX 25,000,000, the invoice number is unique, and the PDF renders correctly.

---

#### FR-FIN-013: Bank Loan Credibility Report

**Phase:** 1

**Stimulus:** The user requests a bank loan credibility report.
**Response:** The system shall aggregate the past 12 months of income, expenses, asset records (livestock, equipment), and production history into a standardised report format suitable for bank loan applications.
**Pre-conditions:** At least 6 months of financial records exist.
**Post-conditions:** The report is generated and available for PDF export.
**Business Rule:** Bank loan credibility report aggregates 12 months of income, expenses, and asset records into a standardised format.

**Verifiability:** Generate a loan credibility report for a farm with 12 months of records. Verify the report includes monthly income and expense summaries, asset inventory, production history, and net worth calculation.

---

#### FR-FIN-014: Mobile Money Payment Tracking

**Phase:** 1

**Stimulus:** The user records a mobile money payment (incoming or outgoing) by entering the provider (MTN MoMo or Airtel Money), transaction ID, phone number, amount, and date.
**Response:** The system shall store the mobile money reference with the corresponding income or expense record.
**Pre-conditions:** The user is authenticated.
**Post-conditions:** The MoMo/Airtel transaction reference is stored.
**Business Rule:** Mobile money transaction IDs are recorded but not validated against mobile money APIs.

**Verifiability:** Record a MoMo payment received: TXN ID "MPC123456", UGX 500,000. Verify the transaction ID displays with the income record and is searchable.

---

#### FR-FIN-015: Multi-Currency Support

**Phase:** 1

**Stimulus:** The user selects a non-UGX currency for a financial record.
**Response:** The system shall store the financial record in the selected currency (UGX, KES, TZS, RWF, NGN, GHS, ZMW) and display the UGX equivalent using a configurable exchange rate.
**Pre-conditions:** The user is authenticated.
**Post-conditions:** The record stores both the original currency amount and the UGX equivalent.

**Verifiability:** Record income of KES 50,000 with exchange rate 28 UGX/KES. Verify the system stores KES 50,000 and displays UGX equivalent as $50{,}000 \times 28 = 1{,}400{,}000$ UGX.

---

## 3.5 Inventory Management

#### FR-INV-001: Input Inventory Registration

**Phase:** 2

**Stimulus:** The user registers an input item in inventory (input type: seed, fertiliser, pesticide, herbicide, feed, medicine; name, unit of measurement, minimum stock level).
**Response:** The system shall create an inventory item record with initial stock of zero.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The inventory item exists with stock quantity 0.

**Verifiability:** Register "Ridomil Gold" (pesticide, kg, minimum stock 5kg). Verify the item appears in inventory with stock 0 and minimum level 5kg.

---

#### FR-INV-002: Stock Receipt

**Phase:** 2

**Stimulus:** The user records a stock receipt (inventory item, quantity received, supplier, batch number, expiry date, unit cost, receipt date).
**Response:** The system shall increment the item's stock quantity by the received amount and store the receipt record with supplier and batch details.
**Pre-conditions:** The inventory item exists.
**Post-conditions:** The stock quantity increases; the receipt record is stored.

**Verifiability:** Receive 10kg of "Ridomil Gold" from "Balton Uganda", batch "RG-2026-003", expiry 1 March 2027, cost UGX 20,000/kg. Verify stock updates to 10kg and receipt details are stored.

---

#### FR-INV-003: Usage Deduction from Activity

**Phase:** 2

**Stimulus:** A crop or livestock activity is recorded with input usage referencing an inventory item.
**Response:** The system shall deduct the used quantity from the inventory item's stock. If the deduction would result in negative stock, the system shall display a warning but shall allow the record.
**Pre-conditions:** The inventory item exists; an activity is being recorded.
**Post-conditions:** The stock quantity decreases; the usage record links the activity to the inventory item.
**Business Rule:** Stock cannot go below zero — if a usage record would cause negative stock, the system warns but allows the record.

**Verifiability:** Use 3kg of "Ridomil Gold" in a spraying activity. Verify stock decreases from 10kg to 7kg. Use 8kg more — verify a warning appears but the record is saved. Verify stock displays as -1kg.

---

#### FR-INV-004: Low Stock Alert

**Phase:** 2

**Stimulus:** An inventory item's stock quantity falls below its configured minimum stock level.
**Response:** The system shall generate a low stock alert notification (in-app, push, and optionally SMS) identifying the item and current stock level.
**Pre-conditions:** The item has a configured minimum stock level.
**Post-conditions:** A notification is generated and delivered.
**Business Rule:** Low stock alerts fire when current stock falls below the item's minimum stock level.

**Verifiability:** Set minimum stock for "Ridomil Gold" to 5kg. Record usage reducing stock to 4kg. Verify a low stock alert is generated within 30 seconds.

---

#### FR-INV-005: Expiry Alert

**Phase:** 2

**Stimulus:** An inventory item's expiry date approaches (90, 60, or 30 days before expiry).
**Response:** The system shall generate an expiry alert notification at each threshold (90, 60, 30 days).
**Pre-conditions:** The item has a recorded expiry date.
**Post-conditions:** Notifications are generated at each threshold.
**Business Rule:** Expiry alerts fire at 30, 60, and 90 days before expiry date.

**Verifiability:** Register an item with expiry date 90 days from today. Verify an alert fires today (90-day threshold). Advance to 60 days before expiry — verify a second alert. Advance to 30 days — verify a third alert.

---

#### FR-INV-006: Equipment Inventory

**Phase:** 2

**Stimulus:** The user registers farm equipment (name, type, serial number, purchase date, purchase price, condition, assigned farm/plot).
**Response:** The system shall create an equipment record with the specified details.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The equipment record is stored.

**Verifiability:** Register a "Knapsack Sprayer" with serial "KS-001", purchased 1 January 2026, price UGX 150,000. Verify the equipment appears in the equipment list.

---

#### FR-INV-007: Maintenance Scheduling

**Phase:** 2

**Stimulus:** The user configures a maintenance schedule for an equipment item (maintenance type, frequency: daily/weekly/monthly/custom, next due date).
**Response:** The system shall store the maintenance schedule and generate reminder notifications when maintenance is due.
**Pre-conditions:** The equipment item exists.
**Post-conditions:** The maintenance schedule is stored; reminders are configured.
**Business Rule:** Equipment maintenance reminders follow the maintenance schedule configured per equipment item.

**Verifiability:** Schedule monthly maintenance for "Knapsack Sprayer" starting 1 February. Verify a reminder is generated on 1 February. Verify the next reminder is scheduled for 1 March.

---

#### FR-INV-008: Produce Inventory

**Phase:** 2

**Stimulus:** The user views or updates produce inventory by storage location (store, warehouse, drying rack, cold room).
**Response:** The system shall display produce quantities per storage location, updated from harvest records and sales/dispatches. The system shall track produce quality changes over time.
**Pre-conditions:** Harvest records exist with storage destinations.
**Post-conditions:** Produce inventory reflects current quantities per location.

**Verifiability:** Record a harvest of 30 bags to "Main Store" and a sale of 10 bags from "Main Store". Verify the produce inventory for "Main Store" shows 20 bags.

---

#### FR-INV-009: Storage Location Management

**Phase:** 2

**Stimulus:** The user creates a storage location (name, type, capacity, current conditions: temperature/humidity if applicable).
**Response:** The system shall create a storage location record linked to the farm.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The storage location exists and is available for harvest record and produce inventory operations.

**Verifiability:** Create storage location "Cold Room A" with capacity 500kg. Verify it appears in the storage location list and is selectable when recording harvests.

---

#### FR-INV-010: Post-Harvest Loss Tracking

**Phase:** 2

**Stimulus:** The user records a post-harvest loss event (produce, quantity lost, loss cause: pest damage/moisture/theft/spoilage, date, storage location).
**Response:** The system shall deduct the lost quantity from produce inventory and store the loss record for analysis.
**Pre-conditions:** Produce inventory exists at the specified storage location.
**Post-conditions:** Produce inventory decreases; the loss record is stored.

**Verifiability:** Record a loss of 5 bags of maize due to "Weevil damage" at "Main Store". Verify the inventory decreases by 5 bags and the loss record appears in the loss history.

---

## 3.6 Task and Worker Management

#### FR-TASK-001: Create Task

**Phase:** 1

**Stimulus:** The user creates a task by entering task name, description, linked plot/enterprise, assigned worker(s), due date, estimated hours, and priority (Low/Medium/High/Urgent).
**Response:** The system shall create a task record with status "To Do" and send a notification to assigned worker(s).
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The task record exists with status "To Do"; assigned workers are notified.

**Verifiability:** Create task "Spray North Field" assigned to worker "Ocan David" due 15 March, 3 estimated hours, priority "High". Verify the task appears in the task list and Ocan receives a push notification.

---

#### FR-TASK-002: View Task List

**Phase:** 1

**Stimulus:** The user opens the task list screen.
**Response:** The system shall display tasks filterable by status (To Do, In Progress, Done), priority, worker, and date range. Tasks shall be sortable by due date, priority, and creation date.
**Pre-conditions:** At least one task exists.
**Post-conditions:** No data modification occurs.

**Verifiability:** With 10 tasks in mixed statuses, filter by "To Do". Verify only tasks with status "To Do" display. Sort by priority — verify "Urgent" tasks appear first.

---

#### FR-TASK-003: Assign Task to Workers

**Phase:** 1

**Stimulus:** The user assigns one or more workers to an existing task.
**Response:** The system shall update the task's assignee list and send a notification to each newly assigned worker.
**Pre-conditions:** The task exists; the workers are registered under the same tenant.
**Post-conditions:** The task assignees are updated; notifications are sent.
**Business Rule:** Tasks can be assigned to one or more workers.

**Verifiability:** Assign 2 workers to a task. Verify both appear as assignees. Verify both receive notifications.

---

#### FR-TASK-004: Complete Task by Worker

**Phase:** 1

**Stimulus:** An assigned worker marks a task as complete on their mobile app by entering actual hours worked and optional notes.
**Response:** The system shall update the task status to "Done", record the actual hours, and log the completion timestamp.
**Pre-conditions:** The user is an assigned worker or has Farm Manager/Owner role.
**Post-conditions:** The task status is "Done"; actual hours are recorded.
**Business Rule:** Only the assigned worker or a Farm Manager/Owner can mark a task complete.

**Verifiability:** Worker "Ocan David" marks task "Spray North Field" complete with 3.5 actual hours. Verify the task status changes to "Done", hours are recorded, and completion timestamp is stored. Verify a different unassigned worker cannot mark the task complete.

---

#### FR-TASK-005: Daily Work Log

**Phase:** 1

**Stimulus:** The user views the daily work log for a specific date.
**Response:** The system shall display all tasks completed on the selected date, grouped by worker, showing task name, hours worked, and associated enterprise.
**Pre-conditions:** Tasks with completion dates exist.
**Post-conditions:** No data modification occurs.

**Verifiability:** View work log for 15 March. Verify all tasks completed on that date appear grouped by worker with hours.

---

#### FR-TASK-006: Worker Profile Management

**Phase:** 1

**Stimulus:** The user creates or edits a worker profile (name, phone number, daily/hourly rate, NIN, employment type: casual/permanent, bank/mobile money details).
**Response:** The system shall store the worker profile record.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The worker profile is stored.

**Verifiability:** Create worker "Ocan David" with phone "0770123456", daily rate UGX 15,000, NIN "CM01234567890", type "Casual", MoMo number "0770123456". Verify all details display on the worker profile screen.

---

#### FR-TASK-007: Payroll Calculation

**Phase:** 1

**Stimulus:** The user generates payroll for a specified period.
**Response:** The system shall calculate each worker's pay based on hours worked and rate. For casual workers: $\text{Pay} = \text{Hours} \times \text{Hourly Rate}$ (or $\text{Days} \times \text{Daily Rate}$). For permanent staff: the system shall calculate gross pay and apply NSSF (10% employee, 5% employer) and PAYE deductions where applicable.
**Pre-conditions:** Workers have completed tasks with recorded hours during the period.
**Post-conditions:** The payroll summary is generated.
**Business Rule:** NSSF and PAYE deductions apply only to workers marked as "permanent staff".

**Verifiability:** Generate payroll for Ocan David (casual, 20 days at UGX 15,000/day). Verify gross pay = UGX 300,000 with no NSSF/PAYE. Generate payroll for a permanent worker at UGX 600,000/month — verify NSSF employee contribution of UGX 60,000 and appropriate PAYE deduction.

---

#### FR-TASK-008: Calendar View

**Phase:** 1

**Stimulus:** The user opens the task calendar.
**Response:** The system shall display tasks on a monthly/weekly/daily calendar, colour-coded by status (To Do: blue, In Progress: orange, Done: green). Overdue tasks shall be highlighted in red.
**Pre-conditions:** At least one task exists.
**Post-conditions:** No data modification occurs.

**Verifiability:** Create tasks with different due dates and statuses. Verify they appear on the correct calendar dates with the specified colour coding. Verify an overdue task is highlighted in red.

---

#### FR-TASK-009: Recurring Tasks

**Phase:** 1

**Stimulus:** The user creates a recurring task by specifying the recurrence pattern (daily, weekly, biweekly, monthly, custom days).
**Response:** The system shall auto-generate new task instances according to the recurrence pattern. Each generated instance is independent and can be completed or modified individually.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** Recurring task instances are generated per the schedule.
**Business Rule:** Recurring tasks auto-generate new task instances according to their schedule.

**Verifiability:** Create a recurring task "Morning Milking" daily at 6am. Verify a new task instance is generated each day. Complete Monday's instance — verify Tuesday's remains as "To Do".

---

#### FR-TASK-010: Kanban Board

**Phase:** 1

**Stimulus:** The user opens the Kanban view.
**Response:** The system shall display tasks in 3 columns: "To Do", "In Progress", "Done". Tasks can be dragged between columns to update their status. Each task card shows name, assignee, due date, and priority.
**Pre-conditions:** At least one task exists.
**Post-conditions:** Dragging a task to a new column updates its status.

**Verifiability:** View the Kanban board with tasks in all 3 columns. Drag a task from "To Do" to "In Progress". Verify the task status updates to "In Progress".

---

#### FR-TASK-011: Mobile Money Worker Payment

**Phase:** 1

**Stimulus:** The user initiates a mobile money payment to a worker from the payroll screen.
**Response:** The system shall send a payment request to the MTN MoMo or Airtel Money API for the calculated amount to the worker's registered mobile money number. The system shall store the transaction ID and payment status (pending, completed, failed).
**Pre-conditions:** The worker has a registered mobile money number. The payroll has been calculated.
**Post-conditions:** A payment request is initiated; the transaction record is stored.

**Verifiability:** Initiate a UGX 300,000 payment to Ocan David via MoMo. Verify the API request is sent with the correct amount and phone number. Verify the transaction ID is stored upon completion.

---

#### FR-TASK-012: Task Progress Tracking

**Phase:** 1

**Stimulus:** A worker updates a task to "In Progress" on their mobile app.
**Response:** The system shall update the task status to "In Progress" and record the start timestamp.
**Pre-conditions:** The task is assigned to the worker and has status "To Do".
**Post-conditions:** The task status is "In Progress"; the start time is recorded.

**Verifiability:** Worker opens task "Spray North Field" and taps "Start". Verify status changes to "In Progress" and the start time is logged.

---

## 3.7 Weather and Advisory

#### FR-WX-001: Retrieve Weather Forecast

**Phase:** 1

**Stimulus:** The user opens the weather screen for a farm, or the system performs a scheduled forecast retrieval.
**Response:** The system shall query the Open-Meteo API using the farm's GPS coordinates and display the forecast. Free tier: 3-day forecast. Paid tiers: 8-day forecast. Forecast shall include temperature (min/max), precipitation probability, wind speed, humidity, and UV index.
**Pre-conditions:** The farm has GPS coordinates recorded. Internet connectivity is available.
**Post-conditions:** The forecast data is cached locally for offline access.

**Verifiability:** Open weather for a farm with GPS coordinates in Mbarara. Verify a 3-day forecast displays with all required fields. Verify the data is available offline after initial retrieval.

---

#### FR-WX-002: Real-Time Weather Display

**Phase:** 1

**Stimulus:** The user views the farm dashboard or weather screen.
**Response:** The system shall display the current weather conditions (temperature, humidity, wind speed, precipitation, UV index) for the farm's GPS location, updated at the most recent sync.
**Pre-conditions:** The farm has GPS coordinates. Weather data has been retrieved.
**Post-conditions:** No data modification occurs.

**Verifiability:** Verify real-time weather displays on the dashboard for a farm in Kasese. Verify the values update when the user refreshes.

---

#### FR-WX-003: Weather Alert Notification

**Phase:** 1

**Stimulus:** The Open-Meteo API returns a severe weather event (heavy rainfall > 50mm, wind speed > 60km/h, temperature < 5°C, heatwave > 35°C) for the farm's location.
**Response:** The system shall generate an alert notification via push (FCM), SMS (Africa's Talking), and in-app notification with the alert type, severity, and recommended actions.
**Pre-conditions:** The farm has GPS coordinates and notification preferences configured.
**Post-conditions:** Notifications are delivered through configured channels.

**Verifiability:** Simulate an API response with rainfall > 50mm. Verify a push notification and SMS are sent to the farm owner within 5 minutes. Verify the alert appears in the in-app notification centre.

---

#### FR-WX-004: Seasonal Forecast

**Phase:** 1

**Stimulus:** The user requests the seasonal forecast view.
**Response:** The system shall display the rainfall and temperature outlook for the current and upcoming season, based on the farm's agro-ecological zone. El Nino/La Nina status shall be indicated where data is available.
**Pre-conditions:** Seasonal forecast data is available.
**Post-conditions:** No data modification occurs.

**Verifiability:** View seasonal forecast for a farm in western Uganda. Verify the outlook for Season A (March-June) and Season B (August-November) is displayed.

---

#### FR-WX-005: Historical Weather Data

**Phase:** 1

**Stimulus:** The user requests historical weather data for a specified date range.
**Response:** The system shall display historical temperature, rainfall, and humidity data in chart format for the farm's location.
**Pre-conditions:** Historical weather data is available from the API or local cache.
**Post-conditions:** No data modification occurs.

**Verifiability:** Request historical weather for January-June 2025 for a farm. Verify temperature and rainfall charts render with daily or weekly data points.

---

#### FR-WX-006: Climate-Smart Advisory

**Phase:** 1

**Stimulus:** The system detects a weather condition relevant to the farm's current crop activities (e.g., rain expected during a planned spray day, dry spell approaching during critical growth stage).
**Response:** The system shall generate an advisory notification with actionable guidance (e.g., "Rain expected tomorrow — delay spraying by 2 days", "Dry spell forecast — irrigate maize in vegetative stage").
**Pre-conditions:** Active crop seasons exist. Weather forecast data is current.
**Post-conditions:** Advisory notifications are generated.

**Verifiability:** Create a crop season with a planned spray activity for tomorrow. Set forecast to show rain tomorrow. Verify the system generates a "Delay spraying" advisory.

---

#### FR-WX-007: Frost Alert for Highland Farms

**Phase:** 1

**Stimulus:** The weather forecast predicts temperatures below 5°C for a farm located above 1,500m elevation.
**Response:** The system shall generate a frost alert notification with recommended protective actions for the farm's active crops.
**Pre-conditions:** The farm's elevation is above 1,500m. Temperature forecast is below 5°C.
**Post-conditions:** Frost alert notifications are delivered.

**Verifiability:** Simulate a forecast of 3°C for a farm at 2,000m elevation in Kabale. Verify a frost alert is generated with crop protection recommendations.

---

#### FR-WX-008: Irrigation Scheduling Recommendation

**Phase:** 1

**Stimulus:** The user requests an irrigation recommendation for a crop season.
**Response:** The system shall calculate irrigation need based on the crop's water requirement, current soil moisture (if sensor data is available), recent rainfall, and forecast rainfall. The recommendation shall specify litres per acre per day.
**Pre-conditions:** An active crop season exists. Rainfall data is available.
**Post-conditions:** The recommendation is displayed on the crop season screen.

**Verifiability:** View irrigation recommendation for a tomato crop in dry season with 0mm rainfall in the past 7 days. Verify the system recommends a specific water quantity based on tomato water requirements.

---

## 3.8 Authentication and Tenancy

#### FR-AUTH-001: User Registration

**Phase:** 1

**Stimulus:** A new user submits the registration form with name, phone number, email (optional), password, and selected language.
**Response:** The system shall create a new user account and a new tenant (farm account) with the "Seedling" (free) tier. The system shall send a verification SMS to the provided phone number.
**Pre-conditions:** The phone number is not already registered.
**Post-conditions:** The user account and tenant are created; a verification SMS is sent.

**Verifiability:** Register with phone "0771234567" and password "Kulima2026!". Verify the account is created, the tenant has "Seedling" tier, and an SMS verification is sent.

---

#### FR-AUTH-002: Login (Dual Authentication)

**Phase:** 1

**Stimulus:** The user submits login credentials (phone number or email + password).
**Response:** For web: the system shall create an authenticated session (cookie-based). For mobile/API: the system shall issue a JWT access token (24-hour expiry) and a refresh token. The system shall enforce session timeout after 30 minutes of inactivity.
**Pre-conditions:** The user account exists and is verified.
**Post-conditions:** An authenticated session or JWT token pair is issued.

**Verifiability:** Login via web — verify a session cookie is set. Login via API — verify a JWT token is returned with 24-hour expiry. Remain inactive for 31 minutes — verify the session expires.

---

#### FR-AUTH-003: Role-Based Access Control

**Phase:** 1

**Stimulus:** An authenticated user attempts to access a resource or perform an action.
**Response:** The system shall evaluate the user's role (Farm Owner, Farm Manager, Worker, Director, Cooperative Admin, Field Agent, Buyer) against the resource's permission requirements. Access shall be granted or denied based on the RBAC policy.
**Pre-conditions:** The user is authenticated.
**Post-conditions:** The action is allowed or denied with appropriate error message.

**Verifiability:** Assign role "Worker" to a user. Attempt to delete a farm — verify access is denied with "Insufficient permissions" message. Attempt to mark a task complete — verify access is granted.

---

#### FR-AUTH-004: Tenant Data Isolation

**Phase:** 1

**Stimulus:** An authenticated user queries data via any API endpoint.
**Response:** The system shall automatically scope all database queries to the authenticated user's tenant ID. No data from other tenants shall be returned or accessible.
**Pre-conditions:** The user is authenticated with a valid tenant association.
**Post-conditions:** Only data belonging to the user's tenant is returned.
**Business Rule:** Each tenant operates in complete data isolation. A tenant's data is never visible to another tenant.

**Verifiability:** Create 2 tenants each with farms. Login as Tenant A — verify only Tenant A's farms are visible. Attempt to access Tenant B's farm by manipulating the API request URL/ID — verify a 403 Forbidden or 404 Not Found response.

---

#### FR-AUTH-005: Subscription Tier Enforcement

**Phase:** 1

**Stimulus:** An authenticated user attempts a write operation that would exceed a subscription tier limit (farm count, plot count, animal count, user count, AI query count).
**Response:** The system shall check the tier limit at the API level before processing the write. If the limit is reached, the system shall return a clear upgrade prompt identifying the limit reached and available upgrade options.
**Pre-conditions:** The user is authenticated; a subscription tier is associated with the tenant.
**Post-conditions:** The write operation succeeds (within limit) or is blocked with an upgrade prompt (at limit).
**Business Rule:** Tier limits enforced at API level before any write operation. Exceeding a limit returns a clear upgrade prompt, never silently truncates data.

**Verifiability:** On a "Seedling" tier limited to 1 farm, create 1 farm successfully. Attempt to create a second — verify the response contains a clear upgrade prompt with tier comparison.

---

#### FR-AUTH-006: Mobile Money Subscription Payment

**Phase:** 1

**Stimulus:** The user initiates a subscription payment from within the app, selecting MTN MoMo or Airtel Money.
**Response:** The system shall send a payment request to the selected mobile money API for the tier price. Upon successful payment, the system shall upgrade the tenant's tier and extend the subscription period.
**Pre-conditions:** The user has Farm Owner role. The mobile money API is available.
**Post-conditions:** The subscription is activated/renewed; the payment record is stored.
**Business Rule:** Annual discount: pay 10 months, receive 12 months of service.

**Verifiability:** Initiate a monthly subscription payment of UGX 40,000 via MoMo. Verify the payment request is sent. Simulate successful payment — verify the tier is upgraded and the subscription end date is set to 30 days from now. Initiate an annual payment — verify the charge is for 10 months ($10 \times 40{,}000 = 400{,}000$ UGX) and the subscription extends for 12 months.

---

#### FR-AUTH-007: Farm Switcher (Multi-Farm Context)

**Phase:** 1

**Stimulus:** The user opens the farm switcher control.
**Response:** The system shall display all farms the user has access to (owned or shared with them via RBAC) and allow switching the active farm context.
**Pre-conditions:** The user has access to 2 or more farms.
**Post-conditions:** The active farm context changes; all displayed data refreshes for the selected farm.

**Verifiability:** A user with access to 3 farms opens the farm switcher. Verify all 3 farms are listed. Select farm 2 — verify all data (dashboard, plots, animals, financials) reflects farm 2.

---

#### FR-AUTH-008: Language Selection

**Phase:** 1

**Stimulus:** The user changes the app language from the settings screen.
**Response:** The system shall immediately switch all UI text to the selected language without requiring an app restart. Available languages: English, Luganda, Swahili (Phase 1); French, Portuguese, Kinyarwanda (Phase 2).
**Pre-conditions:** The language pack is available (pre-loaded on mobile).
**Post-conditions:** All UI elements display in the selected language.

**Verifiability:** Switch language from English to Luganda. Verify all navigation labels, button text, and form labels display in Luganda. Verify no app restart is required. Switch back to English — verify the change is instant.

---

## 3.9 Offline and Sync

#### FR-SYNC-001: Local Data Storage

**Phase:** 1

**Stimulus:** The user performs any CRUD operation on the mobile app while offline.
**Response:** The system shall execute the operation against the local database (Room on Android, SwiftData on iOS) with zero degradation compared to online operation. All core functions (farms, plots, crops, livestock, finances, tasks) shall work identically offline.
**Pre-conditions:** The app is installed with pre-loaded reference data.
**Post-conditions:** Data is persisted locally.
**Business Rule:** All write operations succeed locally regardless of connectivity.

**Verifiability:** Enable airplane mode. Create a farm, add a plot, record an activity, log an expense. Verify all operations complete successfully. Verify the data is accessible immediately after creation.

---

#### FR-SYNC-002: Queue-Based Write Sync

**Phase:** 1

**Stimulus:** The mobile app detects internet connectivity after a period of offline operation.
**Response:** The system shall process the local write queue in priority order: financial transactions → activities → animals → reference data. Each queued record shall be sent to the server API. Successfully synced records shall be marked as synced.
**Pre-conditions:** The write queue contains unsynced records. Internet connectivity is detected.
**Post-conditions:** Queued records are synced to the server; sync status is updated.
**Business Rule:** Sync queue processes in priority order: financial transactions → activities → animals → reference data.

**Verifiability:** Create 5 records offline (2 expenses, 1 activity, 1 animal, 1 plot update). Enable connectivity. Verify the 2 expenses sync first, then the activity, then the animal. Verify all records appear on the web dashboard within 30 seconds.

---

#### FR-SYNC-003: Background Sync

**Phase:** 1

**Stimulus:** The app is running in the background and detects connectivity.
**Response:** The system shall perform background sync using WorkManager (Android) or BGTaskScheduler (iOS), syncing queued records without user intervention.
**Pre-conditions:** The app has background execution permissions.
**Post-conditions:** Queued records are synced.

**Verifiability:** Create records offline, then close the app but do not force-stop. Enable WiFi. Verify records sync in the background within 30 seconds. Verify no user interaction is required.

---

#### FR-SYNC-004: Conflict Resolution

**Phase:** 1

**Stimulus:** During sync, the server detects that a record has been modified both locally and on the server since the last sync.
**Response:** The system shall apply last-write-wins by timestamp. Both versions (local and server) shall be preserved in a conflict log for the farmer to review.
**Pre-conditions:** A sync conflict exists (same record modified on 2 devices).
**Post-conditions:** The latest version wins; both versions are logged.
**Business Rule:** Conflict resolution: last-write-wins by timestamp; conflicts logged for farmer review.

**Verifiability:** Modify the same expense record on 2 devices while both are offline. Sync both. Verify the version with the later timestamp is retained. Verify a conflict log entry exists showing both versions.

---

#### FR-SYNC-005: Attachment Sync

**Phase:** 1

**Stimulus:** Photos or receipt images are queued for sync.
**Response:** The system shall sync attachments separately from data records, only on WiFi or strong 3G/4G connections. Each photo shall be compressed to a maximum of 512KB before upload.
**Pre-conditions:** Attachments are queued for sync. The connection quality meets the threshold.
**Post-conditions:** Attachments are uploaded; references are updated.
**Business Rule:** Photos and attachments sync separately, only on WiFi or strong 3G/4G.

**Verifiability:** Queue 3 photos for sync on 2G. Verify they do not sync. Switch to WiFi — verify all 3 photos sync. Verify each uploaded photo is $\leq$ 512KB.

---

#### FR-SYNC-006: Low Bandwidth Mode

**Phase:** 1

**Stimulus:** The system detects a 2G connection or connection speed below 100kbps.
**Response:** The system shall switch to low bandwidth mode: suppress image sync, reduce sync payload size, and prioritise text data sync.
**Pre-conditions:** The connection quality is below the 3G threshold.
**Post-conditions:** Sync behaviour adapts to low bandwidth constraints.

**Verifiability:** Simulate a 2G connection. Verify photos do not sync. Verify text data (expenses, activities) syncs successfully. Verify sync payload is $\leq$ 1MB per batch.

---

#### FR-SYNC-007: Sync Priority Order

**Phase:** 1

**Stimulus:** Multiple record types are queued for sync.
**Response:** The system shall sync in the defined priority order: 1) Financial transactions, 2) Activities, 3) Animal records, 4) Reference data updates. Within each category, older records sync first (FIFO).
**Pre-conditions:** Multiple unsynced record types exist in the queue.
**Post-conditions:** Records sync in priority order.

**Verifiability:** Queue 1 financial record, 1 activity, and 1 animal record simultaneously. Monitor sync order. Verify the financial record syncs first, then the activity, then the animal.

---

#### FR-SYNC-008: Offline Reference Data

**Phase:** 1

**Stimulus:** The app is installed or a reference data update is available.
**Response:** The system shall pre-load all reference data (crop library, disease library, species/breeds, Uganda administrative hierarchy, activity types) to the local database during initial setup. Reference data updates shall sync when connectivity is available.
**Pre-conditions:** The app is being installed or an update is available.
**Post-conditions:** All reference data is available locally for offline use.

**Verifiability:** Install the app on a new device with WiFi. Verify the crop library (200+ crops), disease library, species list, and administrative hierarchy are available. Enable airplane mode — verify the crop library search still functions.

---

## 3.10 Supply Chain Traceability

#### FR-TRACE-001: Create Batch

**Phase:** 2

**Stimulus:** The user creates a traceability batch by selecting harvest record(s), origin plot(s), crop type, quality grade, quantity, and batch date.
**Response:** The system shall create a batch record with a unique batch ID, linking to the source plot(s) and harvest records.
**Pre-conditions:** Harvest records exist. The farm has GPS polygon boundaries mapped (required for EUDR compliance).
**Post-conditions:** The batch record is created with traceability links to origin data.
**Business Rule:** A batch must reference at least one plot and one harvest record.

**Verifiability:** Create a batch from 2 harvest records on 2 plots. Verify the batch ID is unique, both plots are linked, and the total quantity matches the sum of the harvest records.

---

#### FR-TRACE-002: Chain of Custody Recording

**Phase:** 2

**Stimulus:** The user records a chain of custody stage (e.g., Farm → Collection Centre → Processor → Exporter) by entering stage type, location, date, handler, and notes.
**Response:** The system shall append the custody stage to the batch's chain in chronological order.
**Pre-conditions:** The batch exists.
**Post-conditions:** The custody stage is recorded; the chain displays in chronological order.
**Business Rule:** Chain of custody stages must be recorded in chronological order.

**Verifiability:** Record 3 custody stages for a batch: Farm (1 March), Collection Centre (5 March), Exporter (15 March). Verify they display in chronological order. Attempt to add a stage dated 2 March after the 5 March stage — verify the system warns about chronological order.

---

#### FR-TRACE-003: QR Code Generation

**Phase:** 2

**Stimulus:** The user requests a QR code for a batch.
**Response:** The system shall generate a QR code that encodes a URL to the batch's buyer portal view. The QR code shall be downloadable as PNG and printable.
**Pre-conditions:** The batch exists.
**Post-conditions:** The QR code is generated and stored with the batch. The QR code is immutable once created.
**Business Rule:** QR codes are generated per batch and are immutable once created.

**Verifiability:** Generate a QR code for batch "B-2026-001". Scan the QR code — verify it opens the buyer portal showing batch origin, chain of custody, and certifications.

---

#### FR-TRACE-004: GeoJSON Polygon Export

**Phase:** 2

**Stimulus:** The user exports the farm/plot boundary as GeoJSON for EUDR compliance.
**Response:** The system shall export the GPS polygon data for all plots linked to the batch as a valid GeoJSON file.
**Pre-conditions:** The linked plots have GPS polygon boundaries mapped.
**Post-conditions:** A GeoJSON file is generated and downloadable.

**Verifiability:** Export GeoJSON for a batch linked to 2 plots. Verify the file is valid GeoJSON containing 2 polygon features. Verify the coordinates match the stored farm boundary data.

---

#### FR-TRACE-005: Farmer Profile for Buyers

**Phase:** 2

**Stimulus:** A buyer accesses the batch's buyer portal and views the farmer profile.
**Response:** The system shall display the farmer's name, farm name, location (District, Sub-County), farm photos, certifications, and a description of their farming practices. Sensitive data (exact GPS, financial records, contact details) shall not be displayed.
**Pre-conditions:** The batch has a QR code generated. The farmer has opted into the buyer profile.
**Post-conditions:** No data modification occurs.

**Verifiability:** Scan a batch QR code. Verify the farmer profile displays name, farm name, District, and certifications. Verify no phone numbers, GPS coordinates, or financial data are visible.

---

#### FR-TRACE-006: Input Traceability

**Phase:** 2

**Stimulus:** The buyer portal displays the input history for a batch.
**Response:** The system shall list all inputs (fertilisers, pesticides) used during the crop season(s) linked to the batch, showing input name, quantity, and application date.
**Pre-conditions:** Input usage records exist for the crop season(s) linked to the batch.
**Post-conditions:** No data modification occurs.

**Verifiability:** View a batch that used 3 different inputs during the crop season. Verify all 3 inputs display with names, quantities, and dates.

---

#### FR-TRACE-007: Certification Tracking

**Phase:** 2

**Stimulus:** The user records a certification for the farm (certification type: Organic, RainForest Alliance, UTZ, GlobalGAP, FairTrade; issuing body, certificate number, issue date, expiry date).
**Response:** The system shall store the certification record and schedule renewal reminder alerts at 90, 60, and 30 days before expiry.
**Pre-conditions:** The user has Farm Owner or Farm Manager role.
**Post-conditions:** The certification record is stored; renewal reminders are scheduled.
**Business Rule:** Certification expiry triggers renewal reminder alerts at 90, 60, and 30 days before expiry.

**Verifiability:** Record an "Organic" certification expiring 31 December 2026. Verify reminders are scheduled for 2 October (90 days), 1 November (60 days), and 1 December (30 days).

---

#### FR-TRACE-008: Deforestation Check

**Phase:** 2

**Stimulus:** The user requests a deforestation verification for a farm or plot.
**Response:** The system shall compare the farm's GPS polygon against the Global Forest Watch December 2020 baseline dataset. The result (deforestation-free: yes/no, check date) shall be stored with the farm record.
**Pre-conditions:** The farm has GPS polygon boundaries. Global Forest Watch data is accessible.
**Post-conditions:** The deforestation check result is stored.
**Business Rule:** Deforestation check compares farm polygon against the December 2020 baseline from Global Forest Watch.

**Verifiability:** Run a deforestation check for a farm polygon. Verify the result (yes/no) is stored with the check date. Verify the result appears on the batch traceability view.

---

#### FR-TRACE-009: EUDR DDS Generation

**Phase:** 2

**Stimulus:** The user requests generation of an EUDR Due Diligence Statement for a batch.
**Response:** The system shall generate a DDS document containing: farm GPS polygon, crop type, harvest date, deforestation check result, input history, and certification status.
**Pre-conditions:** The batch exists with GPS polygon, deforestation check, and harvest records.
**Post-conditions:** The DDS document is generated as a downloadable PDF.
**Business Rule:** EUDR DDS export includes only: farm GPS polygon, crop type, harvest date, deforestation check result.

**Verifiability:** Generate a DDS for a coffee batch. Verify the PDF contains the GPS polygon map, crop type "Coffee (Arabica)", harvest date, and deforestation check result "Deforestation-free: Yes". Verify the document structure matches EUDR requirements.

---

#### FR-TRACE-010: Buyer Portal (Read-Only)

**Phase:** 2

**Stimulus:** An unauthenticated user scans a batch QR code or navigates to the buyer portal URL.
**Response:** The system shall display a read-only view showing: batch ID, crop type, origin (District, Sub-County), harvest date, quality grade, chain of custody stages, farmer profile, input history, certifications, deforestation check result, and GPS polygon map.
**Pre-conditions:** The batch exists and has a QR code generated.
**Post-conditions:** No data modification occurs. No authentication required.

**Verifiability:** Scan a batch QR code without logging in. Verify all traceability data displays. Verify no edit or delete actions are available. Verify no sensitive farmer data (phone, exact GPS, financials) is exposed.

---

## 3.11 Marketplace

#### FR-MKT-001: Create Produce Listing

**Phase:** 2

**Stimulus:** The user creates a marketplace listing for produce (crop type, variety, quantity available, price per unit, unit, quality grade, location, photos, harvest date, availability period).
**Response:** The system shall create a listing visible to buyers in the marketplace search.
**Pre-conditions:** The user has Farm Owner role.
**Post-conditions:** The listing is active and searchable.

**Verifiability:** Create a listing for 100 bags of maize at UGX 250,000/bag in Mbarara. Verify the listing appears in marketplace search results when searching for "maize" in "Mbarara".

---

#### FR-MKT-002: Create Livestock Listing

**Phase:** 2

**Stimulus:** The user creates a marketplace listing for a live animal (species, breed, sex, age, weight, price, health status, photos, location).
**Response:** The system shall create a listing visible in the marketplace livestock section.
**Pre-conditions:** The user has Farm Owner role.
**Post-conditions:** The listing is active and searchable.

**Verifiability:** List a "Holstein Friesian" cow, 4 years old, 450kg, UGX 4,500,000 in Mbarara. Verify the listing appears when searching for cattle in Mbarara.

---

#### FR-MKT-003: Buyer Search

**Phase:** 2

**Stimulus:** A buyer searches the marketplace by crop type, livestock species, location (District), price range, or quantity.
**Response:** The system shall return matching listings sorted by relevance, with distance from the buyer's location if GPS is available.
**Pre-conditions:** Active listings exist.
**Post-conditions:** No data modification occurs.

**Verifiability:** Search for "coffee" in "Kasese" with price range UGX 5,000-8,000/kg. Verify only matching listings appear. Verify results are sorted by relevance.

---

#### FR-MKT-004: Market Price Database

**Phase:** 2

**Stimulus:** The user views the market price database.
**Response:** The system shall display current and historical prices for major crops across Uganda's markets, with trend charts.
**Pre-conditions:** Market price records exist.
**Post-conditions:** No data modification occurs.

**Verifiability:** View market prices for maize. Verify prices are displayed per market (Kalerwe, Nakasero, Busia) with trend charts showing price movement over the last 90 days.

---

#### FR-MKT-005: Price Alert

**Phase:** 2

**Stimulus:** The user configures a price alert for a crop (crop type, target price, market, direction: above/below).
**Response:** The system shall monitor recorded prices and send a notification when the target threshold is reached.
**Pre-conditions:** The user has configured a price alert.
**Post-conditions:** The alert is stored and monitored.

**Verifiability:** Set alert "Notify when maize price at Kalerwe exceeds UGX 3,000/kg". Record a price of UGX 3,200/kg. Verify a notification is generated.

---

#### FR-MKT-006: Directory Listings

**Phase:** 2

**Stimulus:** The user browses the agro-dealer directory, vet directory, or extension officer directory.
**Response:** The system shall display directory listings filterable by location (District), speciality, and service type.
**Pre-conditions:** Directory listings exist.
**Post-conditions:** No data modification occurs.

**Verifiability:** Browse the agro-dealer directory filtered by "Mbarara". Verify agro-dealers in Mbarara are listed with name, contact, and services.

---

#### FR-MKT-007: Order Management

**Phase:** 2

**Stimulus:** A buyer expresses interest in a listing and the seller accepts.
**Response:** The system shall create an order record tracking the listing, buyer, seller, agreed quantity, agreed price, and order status (Pending, Confirmed, Completed, Cancelled). Communication between buyer and seller shall be facilitated via WhatsApp direct link.
**Pre-conditions:** An active listing exists; a buyer has expressed interest.
**Post-conditions:** The order record is created; WhatsApp link is provided.

**Verifiability:** Create an order for 50 bags of maize from a listing. Verify the order appears with status "Pending" for both buyer and seller. Verify a WhatsApp link is generated with the correct phone number.

---

#### FR-MKT-008: Verified Reviews

**Phase:** 2

**Stimulus:** A buyer submits a review for a completed order (rating 1-5 stars, comment).
**Response:** The system shall store the review linked to the seller and order. Only buyers with completed orders can submit reviews.
**Pre-conditions:** The order status is "Completed".
**Post-conditions:** The review is stored and displayed on the seller's profile.

**Verifiability:** Complete an order and submit a 4-star review. Verify the review displays on the seller's marketplace profile. Attempt to submit a review without a completed order — verify the system rejects it.

---

## 3.12 Cooperative Management

#### FR-COOP-001: Member Farmer Registration

**Phase:** 2

**Stimulus:** The cooperative admin registers a new member farmer by entering farmer name, phone number, NIN, farm location, and assigning a member ID.
**Response:** The system shall create a member farmer record under the cooperative tenant with their own user account and farm data.
**Pre-conditions:** The cooperative tenant has not reached its member limit.
**Post-conditions:** The member farmer account is created under the cooperative umbrella.
**Business Rule:** A cooperative operates as a single franchise tenant. Member farmers are registered under the cooperative tenant.

**Verifiability:** Register member "Nakato Grace" with phone "0777123456", member ID "ACO-001". Verify the member appears in the cooperative member list. Verify Nakato can log in and see her own farm data.

---

#### FR-COOP-002: Member Farm Mapping

**Phase:** 2

**Stimulus:** A field agent maps a member farmer's farm boundary using the mobile app GPS.
**Response:** The system shall capture the GPS polygon boundary and store it as GeoJSON linked to the member's farm record.
**Pre-conditions:** The field agent has GPS-enabled device and is assigned to the member.
**Post-conditions:** The GPS polygon is stored with the member's farm.

**Verifiability:** Walk the perimeter of a member's 2-acre farm. Verify the polygon is captured and displays on the cooperative's farm map. Verify the calculated area is within $\pm 5\%$ of 2 acres.

---

#### FR-COOP-003: Input Distribution Tracking

**Phase:** 2

**Stimulus:** The cooperative admin records input distribution to members (input type, quantity per member, distribution date, batch number).
**Response:** The system shall create distribution records per member and update the cooperative's input stock.
**Pre-conditions:** The cooperative has input stock. Members are registered.
**Post-conditions:** Distribution records are created; cooperative stock decreases.

**Verifiability:** Distribute 5kg of coffee seedlings each to 50 members. Verify 50 distribution records are created. Verify cooperative stock decreases by 250kg.

---

#### FR-COOP-004: Collection Centre Management

**Phase:** 2

**Stimulus:** The collection centre operator records a member's delivery (member ID, crop type, weight, quality grade, date).
**Response:** The system shall create a collection record linked to the member and calculate the payment amount as $\text{Payment} = \text{Weight} \times \text{Grade Price}$.
**Pre-conditions:** The member is registered. A collection session is active.
**Post-conditions:** The collection record is stored; the payment amount is calculated.
**Business Rule:** Collection centre deliveries are recorded with weight, quality grade, and date. Member payments are calculated as: quantity delivered x grade-specific price per unit.

**Verifiability:** Record a delivery from member "ACO-001": 500kg of coffee, Grade A at UGX 5,000/kg. Verify payment calculates as $500 \times 5{,}000 = 2{,}500{,}000$ UGX.

---

#### FR-COOP-005: Quality Grading at Collection

**Phase:** 2

**Stimulus:** The collection operator assigns a quality grade (A/B/C/Reject) to a delivered lot.
**Response:** The system shall store the grade with the collection record and apply the grade-specific price for payment calculation.
**Pre-conditions:** The lot has been weighed and recorded.
**Post-conditions:** The grade and resulting price are stored.

**Verifiability:** Grade a 500kg lot as "B" with price UGX 4,000/kg. Verify the payment updates to $500 \times 4{,}000 = 2{,}000{,}000$ UGX.

---

#### FR-COOP-006: Member Payment Calculation

**Phase:** 2

**Stimulus:** The cooperative admin generates the payment summary for a collection season.
**Response:** The system shall aggregate all collection records per member and calculate the total payment due: $\text{Total Payment}_m = \sum_{i=1}^{n} (\text{Weight}_i \times \text{Grade Price}_i)$ for each member $m$.
**Pre-conditions:** Collection records exist for the season.
**Post-conditions:** The payment summary is generated per member.

**Verifiability:** With member "ACO-001" delivering 3 lots (500kg Grade A, 300kg Grade B, 200kg Grade C), verify the total payment calculation is correct based on grade-specific prices.

---

#### FR-COOP-007: Bulk Mobile Money Disbursement

**Phase:** 2

**Stimulus:** The cooperative admin initiates bulk payment to all members for a season.
**Response:** The system shall send individual mobile money payment requests to each member's registered phone number via MTN MoMo or Airtel Money bulk payment API. Transaction IDs and statuses shall be recorded per member.
**Pre-conditions:** Payment amounts are calculated. Members have registered mobile money numbers.
**Post-conditions:** Payment requests are sent; transaction records are stored.
**Business Rule:** Bulk mobile money disbursement sends individual payments to each member's registered mobile money number.

**Verifiability:** Initiate bulk payment to 50 members. Verify 50 individual payment requests are sent. Verify transaction IDs and statuses (pending/completed/failed) are recorded for each member.

---

#### FR-COOP-008: Aggregate Supply Reports

**Phase:** 2

**Stimulus:** The cooperative admin generates aggregate supply reports.
**Response:** The system shall display reports showing: total quantity collected per crop per season, breakdown by quality grade, total payments disbursed, and member participation rate.
**Pre-conditions:** Collection records exist.
**Post-conditions:** No data modification occurs.

**Verifiability:** Generate a report for Season A 2026 coffee collection. Verify total quantity, grade breakdown, total payments, and participation rate (members who delivered / total members) display correctly.

---

#### FR-COOP-009: Compliance Monitoring

**Phase:** 2

**Stimulus:** The cooperative admin views the compliance dashboard.
**Response:** The system shall display member compliance status: GPS farm mapped (yes/no), input received (yes/no), deliveries made (yes/no), certifications valid (yes/no). Non-compliant members shall be flagged.
**Pre-conditions:** Member records exist with associated data.
**Post-conditions:** No data modification occurs.

**Verifiability:** View compliance for 50 members. Verify members without GPS maps are flagged. Verify members with expired certifications are flagged.

---

#### FR-COOP-010: Field Agent App

**Phase:** 2

**Stimulus:** A field agent logs into the simplified mobile app.
**Response:** The system shall display a task-oriented interface showing: assigned member visits, farm mapping tasks, data collection forms, and photo upload. The interface shall be simpler than the full farmer app with fewer menu options.
**Pre-conditions:** The user has the "Field Agent" role assigned by the cooperative admin.
**Post-conditions:** Field agent tasks and data are synced with the cooperative's system.

**Verifiability:** Login as a field agent. Verify only field-agent-relevant screens are visible (member visits, farm mapping, data forms). Verify the full farmer CRUD menu is not accessible.

---

## 3.13 IoT Integration (Jaguza)

#### FR-IOT-001: Jaguza OAuth Connect

**Phase:** 3

**Stimulus:** The user initiates connection to their Jaguza account from the IoT settings screen.
**Response:** The system shall redirect to the Jaguza OAuth flow. Upon successful authorisation, the system shall store the access token and refresh token securely.
**Pre-conditions:** The user has a Jaguza account with registered devices. The tenant's subscription includes the IoT add-on.
**Post-conditions:** The Jaguza OAuth token is stored; the system can access Jaguza API.

**Verifiability:** Initiate Jaguza connection. Complete OAuth flow. Verify the system stores tokens and displays "Connected" status. Verify the system can retrieve device list from Jaguza API.

---

#### FR-IOT-002: Device Management

**Phase:** 3

**Stimulus:** The user views, registers, or assigns IoT devices to animals.
**Response:** The system shall display all Jaguza devices from the connected account. The user can assign each device to a specific animal in the Kulima system. Device battery status, last data timestamp, and signal strength shall be displayed.
**Pre-conditions:** Jaguza OAuth is connected.
**Post-conditions:** Device-to-animal assignments are stored.
**Business Rule:** IoT devices must be assigned to a specific animal before data is displayed.

**Verifiability:** View Jaguza devices. Assign device "JZ-1001" to cow "AK-001". Verify the device shows as assigned. Verify battery status and last data timestamp display.

---

#### FR-IOT-003: Data Polling and Webhook

**Phase:** 3

**Stimulus:** The system performs scheduled polling (every 10 minutes) or receives a real-time webhook from Jaguza.
**Response:** The system shall store the IoT data (activity level, temperature, location, fertility index) and link it to the assigned animal. Webhook alerts (health warning, heat detection) shall trigger immediate notification processing.
**Pre-conditions:** Devices are assigned to animals. Jaguza API is accessible.
**Post-conditions:** IoT data is stored and linked to animals; alerts trigger notifications.
**Business Rule:** Jaguza data polling occurs every 10 minutes; webhook alerts are processed in real time.

**Verifiability:** Verify a scheduled poll retrieves data from Jaguza API and stores it for the assigned animal. Simulate a webhook alert — verify it is processed within 30 seconds.

---

#### FR-IOT-004: Animal Alert Dashboard

**Phase:** 3

**Stimulus:** The user opens the IoT dashboard.
**Response:** The system shall display a herd health overview with colour-coded status per animal: Green (normal), Amber (warning), Red (critical). Each animal card shall show the latest activity level, temperature, and alert status.
**Pre-conditions:** IoT data exists for assigned animals.
**Post-conditions:** No data modification occurs.
**Business Rule:** IoT alert severity levels: Info, Warning, Critical.

**Verifiability:** With 20 animals having IoT devices, verify the dashboard shows all 20 with correct colour coding. Verify a critical alert shows the animal as Red.

---

#### FR-IOT-005: Heat Detection Alert

**Phase:** 3

**Stimulus:** The Jaguza system detects elevated activity indicating estrus in a cow.
**Response:** The system shall generate a heat detection alert notification (push + SMS) identifying the animal, estimated heat start time, and recommended insemination window.
**Pre-conditions:** The animal is female and has an assigned IoT device.
**Post-conditions:** The alert is delivered; the event is logged on the animal's reproduction timeline.
**Business Rule:** Critical alerts trigger immediate SMS + push notification.

**Verifiability:** Simulate a heat detection event for cow "AK-001". Verify SMS and push notifications are sent within 2 minutes. Verify the event appears on the animal's reproduction timeline.

---

#### FR-IOT-006: Disease Early Warning

**Phase:** 3

**Stimulus:** The Jaguza system detects abnormal activity or temperature patterns indicating potential disease.
**Response:** The system shall generate a disease warning alert (push + SMS) with the animal ID, abnormal readings, and recommended action (isolate, call vet).
**Pre-conditions:** IoT data shows abnormal patterns for an animal.
**Post-conditions:** The alert is delivered; the animal's status may be recommended for quarantine.

**Verifiability:** Simulate abnormal temperature (> 40°C sustained for 2 hours) for cow "AK-002". Verify a disease warning alert is sent via SMS and push. Verify the alert recommends isolation.

---

#### FR-IOT-007: Sensor Data Integration

**Phase:** 3

**Stimulus:** Soil sensors or weather stations send data to the Kulima IoT gateway.
**Response:** The system shall receive sensor data via MQTT or HTTP webhook, store it linked to the relevant plot or farm, and display it on the plot/farm detail screen.
**Pre-conditions:** Sensors are registered and assigned to a plot or farm.
**Post-conditions:** Sensor data is stored and displayed.

**Verifiability:** Receive soil moisture data (45%) from sensor "SM-001" assigned to "North Field". Verify the value displays on the plot detail screen with the timestamp.

---

#### FR-IOT-008: Drone Imagery Integration

**Phase:** 3

**Stimulus:** The user uploads drone survey imagery and links it to a farm or plot.
**Response:** The system shall store the imagery and overlay it on the farm map. Crop health analysis from aerial imagery shall be displayable alongside NDVI data.
**Pre-conditions:** The user has drone survey results.
**Post-conditions:** Drone imagery is stored and overlaid on the farm map.

**Verifiability:** Upload a drone ortho-mosaic image for "North Field". Verify the image overlays correctly on the farm map. Verify the overlay is toggleable.

---

## 3.14 GPS Animal Tracking

#### FR-GPS-001: Tracker Registration

**Phase:** 3

**Stimulus:** The user registers a GPS tracker by entering the device IMEI, SIM card number, assigned animal, and tracker model.
**Response:** The system shall create a tracker record and begin listening for position data from the device.
**Pre-conditions:** The tenant's subscription includes the GPS tracking add-on.
**Post-conditions:** The tracker is registered and actively monitored.

**Verifiability:** Register tracker with IMEI "123456789012345", assign to bull "AK-010". Verify the tracker appears in the device list. Verify position data begins appearing within the configured polling interval.

---

#### FR-GPS-002: Live Map

**Phase:** 3

**Stimulus:** The user opens the live tracking map.
**Response:** The system shall display a map with real-time positions of all tracked animals as moving icons. Each icon shall show the animal name/tag and last position timestamp. The map shall refresh at the tracker's reporting interval.
**Pre-conditions:** GPS trackers are registered and reporting.
**Post-conditions:** No data modification occurs.

**Verifiability:** View the live map with 5 tracked animals. Verify all 5 icons appear at correct positions. Verify positions update when new data arrives.

---

#### FR-GPS-003: Geofence Creation

**Phase:** 3

**Stimulus:** The user draws a geofence polygon on the map or selects an existing farm/paddock boundary as a geofence.
**Response:** The system shall store the geofence as a GeoJSON polygon and associate it with one or more tracked animals.
**Pre-conditions:** At least one GPS tracker is registered.
**Post-conditions:** The geofence is stored and active for breach monitoring.

**Verifiability:** Draw a geofence around a 50-acre paddock. Assign it to 3 tracked animals. Verify the geofence displays on the map and is associated with the correct animals.

---

#### FR-GPS-004: Geofence Breach Alert

**Phase:** 3

**Stimulus:** A GPS tracker reports a position outside an assigned geofence boundary.
**Response:** The system shall generate a breach alert within 2 minutes of the position report. The alert shall be sent via SMS (mandatory), push notification, and WhatsApp (if configured). The alert shall include: animal name/tag, breach time, current location (GPS coordinates), and a map link.
**Pre-conditions:** A geofence is active for the tracked animal.
**Post-conditions:** Breach alerts are delivered; the breach event is logged.
**Business Rule:** Geofence breach alerts must fire within 2 minutes. SMS is mandatory; push and WhatsApp are supplementary.

**Verifiability:** Simulate a tracker position outside the geofence at 14:00. Verify an SMS alert is received by 14:02. Verify the SMS contains the animal name, breach time, and map link.

---

#### FR-GPS-005: Historical Playback

**Phase:** 3

**Stimulus:** The user selects a date range (7, 14, or 30 days) for a tracked animal's historical movement.
**Response:** The system shall display the animal's movement path on the map as an animated playback with timestamps at each position point.
**Pre-conditions:** Historical GPS data exists for the selected period.
**Post-conditions:** No data modification occurs.
**Business Rule:** Historical GPS data retained for 90 days.

**Verifiability:** Select 7-day playback for bull "AK-010". Verify the movement path renders on the map with position timestamps. Verify playback can be paused and resumed.

---

#### FR-GPS-006: Speed Tracking for Theft Detection

**Phase:** 3

**Stimulus:** A GPS tracker reports movement speed exceeding a configurable threshold (default: 20km/h for cattle).
**Response:** The system shall generate a theft/distress alert with the animal's speed, direction, and current position. The alert shall follow the same SMS + push + WhatsApp delivery as geofence breach alerts.
**Pre-conditions:** The speed threshold is configured. The tracker reports speed data.
**Post-conditions:** The speed alert is logged and delivered.

**Verifiability:** Simulate tracker speed of 30km/h for cow "AK-001". Verify a theft alert is generated within 2 minutes with speed, direction, and position.

---

#### FR-GPS-007: Vehicle Tracking

**Phase:** 3

**Stimulus:** The user registers a GPS tracker for a farm vehicle (truck, tractor, motorcycle).
**Response:** The system shall track the vehicle's position and display it on the same live map as animal trackers, with a different icon type.
**Pre-conditions:** The GPS tracking add-on is enabled.
**Post-conditions:** The vehicle tracker is registered and monitored.

**Verifiability:** Register a tracker for "Farm Truck" with IMEI "987654321098765". Verify the vehicle appears on the live map with a vehicle icon. Verify geofence and speed alerts work for vehicles.

---

#### FR-GPS-008: Theft Investigation Report

**Phase:** 3

**Stimulus:** The user generates a theft investigation report for an incident.
**Response:** The system shall generate a report containing: animal details, geofence breach time, movement path after breach, speed data, last known position, and a map with the full incident trail. The report shall be formatted for submission to Uganda Police.
**Pre-conditions:** A geofence breach or speed alert has occurred.
**Post-conditions:** The report is generated as a downloadable PDF.

**Verifiability:** Generate a theft report after a breach event. Verify the PDF contains animal details, breach timestamp, movement path, and last known position. Verify the format includes a section header suitable for police submission.

---

## 3.15 Camera Surveillance

#### FR-CAM-001: Camera Registration

**Phase:** 3

**Stimulus:** The user registers an IP camera by entering camera name, brand (Hikvision/Dahua/Reolink/Generic), IP address or cloud account credentials, RTSP URL, assigned location (farm/plot/building), and stream resolution.
**Response:** The system shall create a camera record, test the RTSP connection, and report success or failure.
**Pre-conditions:** The tenant's subscription includes the camera add-on. The camera is on the same network or accessible via cloud API.
**Post-conditions:** The camera record is stored; connection status is verified.

**Verifiability:** Register a Hikvision camera with RTSP URL "rtsp://admin:pass@192.168.1.100:554/ch1". Verify the system tests the connection and reports success. Verify the camera appears in the camera list.

---

#### FR-CAM-002: Stream Proxy (RTSP to HLS)

**Phase:** 3

**Stimulus:** A user requests to view a camera stream.
**Response:** The system shall proxy the RTSP stream through mediamtx/ffmpeg, converting it to HLS format. The HLS stream URL shall be served to the web or mobile client. No video shall be stored on the server.
**Pre-conditions:** The camera is registered and the RTSP connection is active.
**Post-conditions:** An HLS stream is generated and served. No recording is stored.
**Business Rule:** Camera streams are proxied (RTSP → HLS); Kulima does not store video.

**Verifiability:** Open a camera's live view. Verify the HLS stream loads within 5 seconds. Verify the stream displays video at the selected quality. Verify no video files are created on the server.

---

#### FR-CAM-003: Live Camera Viewing

**Phase:** 3

**Stimulus:** The user selects a camera from the camera list.
**Response:** The system shall display the live camera feed in a full-screen or embedded player. Stream quality options (Auto/High/Medium/Low) shall be selectable.
**Pre-conditions:** The camera is online and the proxy is running.
**Post-conditions:** No data modification occurs.

**Verifiability:** View a live camera feed. Verify the video plays smoothly. Switch quality from "High" to "Low" — verify the stream adapts. Verify a "Low" (360p) mode is available for low-bandwidth connections.

---

#### FR-CAM-004: Multi-Camera Grid View

**Phase:** 3

**Stimulus:** The user opens the multi-camera view.
**Response:** The system shall display a grid of live camera feeds (2x2 or 3x3 layout) with each camera's name and status indicator.
**Pre-conditions:** Multiple cameras are registered and online.
**Post-conditions:** No data modification occurs.

**Verifiability:** With 4 cameras registered, open the grid view. Verify all 4 streams display simultaneously in a 2x2 layout. Verify each stream shows the camera name.

---

#### FR-CAM-005: PTZ Control

**Phase:** 3

**Stimulus:** The user interacts with PTZ (Pan-Tilt-Zoom) controls on a compatible camera.
**Response:** The system shall send PTZ commands to the camera via ONVIF or the camera's API. Pan and tilt shall be controllable via directional buttons or swipe gestures. Zoom shall be controllable via +/- buttons or pinch gesture.
**Pre-conditions:** The camera supports PTZ and is connected via ONVIF or compatible API.
**Post-conditions:** The camera orientation and zoom update per the user's commands.

**Verifiability:** Pan the camera left. Verify the video feed shows the view shifting left. Zoom in — verify the image enlarges.

---

#### FR-CAM-006: Motion Detection Alert

**Phase:** 3

**Stimulus:** The camera detects motion within a configured alert zone.
**Response:** The system shall generate a motion alert with a snapshot image, delivered via push notification, SMS, and WhatsApp (if configured). Zone-based detection shall be used to reduce false positives.
**Pre-conditions:** Motion alert zones are configured for the camera. Alert scheduling allows alerts at the current time.
**Post-conditions:** The motion alert and snapshot are delivered.
**Business Rule:** Motion alert zones must be configured per camera; full-frame alerts are disabled by default. Camera streams are proxied, not stored; only snapshots are saved.

**Verifiability:** Configure a motion zone at the farm gate. Simulate motion in the zone. Verify a push notification is received with a snapshot. Simulate motion outside the zone — verify no alert is generated.

---

#### FR-CAM-007: Alert Scheduling

**Phase:** 3

**Stimulus:** The user configures alert schedules for a camera (e.g., alerts only between 18:00 and 06:00).
**Response:** The system shall store the alert schedule and only generate motion alerts during the configured time windows.
**Pre-conditions:** The camera is registered.
**Post-conditions:** The alert schedule is stored and enforced.

**Verifiability:** Set alerts for 18:00-06:00 only. Trigger motion at 14:00 — verify no alert. Trigger motion at 22:00 — verify alert is sent.

---

#### FR-CAM-008: Share Camera Access

**Phase:** 3

**Stimulus:** The user shares camera access with another person by generating a time-limited share link (1 hour, 24 hours, 7 days).
**Response:** The system shall generate a unique URL that provides view-only access to the camera stream. The link shall expire after the configured duration.
**Pre-conditions:** The user has Farm Owner or Farm Manager role for the camera.
**Post-conditions:** The share link is generated; access is granted for the configured duration.
**Business Rule:** Camera access can be shared via time-limited links (1 hour, 24 hours, 7 days).

**Verifiability:** Generate a 24-hour share link. Open the link — verify the live stream is viewable without login. Wait 25 hours — verify the link returns an "Access expired" message.

---

## 3.16 AI Farm Advisor

#### FR-AI-001: Natural Language Q&A

**Phase:** 3

**Stimulus:** The user types or voice-inputs a question in natural language (e.g., "When should I spray my coffee?" or "What is the best feed for my dairy cows?").
**Response:** The system shall send the question to the Claude API with the user's farm context (active crops, livestock, location, season) and return a personalised answer in the user's selected language (English, Luganda, or Swahili) within ≤ 8,000 ms at P95 under normal load. The system shall enforce the account's configured monthly query budget and reject the query with a budget-exceeded message when the limit is reached.
**Pre-conditions:** Internet connectivity is available. The AI add-on is enabled. At least 3 farm profile fields (crop type, location, season) are populated.
**Post-conditions:** The Q&A exchange is stored in the advisor history.

**Verifiability:** Ask "When should I spray my coffee this season?" Verify the response arrives within ≤ 8,000 ms, references the user's coffee crop, and provides a specific recommendation. Verify the response is in the user's selected language. Set the monthly budget to 1 query and exhaust it — verify the next query returns a budget-exceeded message.

---

#### FR-AI-002: Photo-Based Pest/Disease Diagnosis

**Phase:** 3

**Stimulus:** The user captures or uploads a photo of an affected crop and requests a diagnosis.
**Response:** The system shall send the photo to the Claude Vision API with context (crop type, region, season) and return a diagnosis within ≤ 10,000 ms at P95 under normal load. The response shall include: identified pest/disease name, confidence percentage (0–100%), recommended treatment steps, and preventive measures. When confidence < 70%, the system shall append an extension officer consultation recommendation.
**Pre-conditions:** Internet connectivity is available. A photo ≤ 10 MB is provided. The AI add-on is enabled.
**Post-conditions:** The diagnosis result is stored with the crop health event timestamp.

**Verifiability:** Upload a clear photo of Coffee Berry Disease. Verify the response arrives within ≤ 10,000 ms, identifies CBD with ≥ 70% confidence, and recommends a fungicide treatment. Upload a blurry, ambiguous photo — verify the confidence is < 70% and the extension officer referral message is displayed.

---

#### FR-AI-003: Personalised Recommendations

**Phase:** 3

**Stimulus:** The user opens the advisor recommendations screen.
**Response:** The system shall analyse the user's farm data (activity history, yield records, weather forecasts, market prices) and generate at least 3 personalised recommendations referencing specific farm data points (e.g., "Your maize yield decreased 15% last season. Consider soil testing before Season A."). The system shall not generate recommendations when fewer than 3 farm profile fields (crop type, GPS location, season) are populated.
**Pre-conditions:** The farm has at least 1 season of activity data. At least 3 farm profile fields are populated (crop type, GPS location, and active season).
**Post-conditions:** Recommendations are displayed and stored with a timestamp.

**Verifiability:** For a farm with declining maize yields over 2 seasons, verify the system generates at least 3 recommendations including a yield improvement recommendation. Verify each recommendation cites a specific farm data point. Configure a farm with fewer than 3 profile fields — verify the system withholds recommendations and displays a profile-completion prompt.

---

#### FR-AI-004: Seasonal Planning Advisor

**Phase:** 3

**Stimulus:** The user requests a seasonal planting plan for the upcoming season.
**Response:** The system shall retrieve a 14-day weather forecast from the Open-Meteo API for the farm's GPS zone and combine it with 3 years of historical rainfall records for that zone, the farm's plot availability, and crop rotation history to generate a "Plant or Wait?" advisory. The advisory shall specify the recommended planting window (start date ± 7 days) and the crop allocation per plot for the upcoming season.
**Pre-conditions:** Farm GPS coordinates are recorded. Open-Meteo API is reachable. At least 1 prior season of crop rotation data exists.
**Post-conditions:** The suggested plan is displayed; the user can accept and auto-create crop seasons from the plan.

**Verifiability:** Request seasonal planning for a farm with 5 plots two weeks before the typical planting window. Verify the system retrieves Open-Meteo forecast data (confirm API call in network log). Verify the advisory references historical rainfall for the GPS zone and specifies a planting window with a ± 7-day range. Accept the plan — verify 5 crop seasons are auto-created with the recommended crops.

---

#### FR-AI-005: Market Timing Advice

**Phase:** 3

**Stimulus:** The user selects a crop and requests a market timing recommendation.
**Response:** The system shall analyse a minimum of 24 months of historical market price data for the selected crop at the farmer's nearest market and generate an optimal selling window recommendation. The response shall include: the recommended selling window (expressed as weeks post-harvest), the expected price range (UGX/kg or UGX/bag), and the estimated revenue uplift versus selling at harvest. When fewer than 24 months of price data are available, the system shall state the data limitation in the response.
**Pre-conditions:** Market price history of at least 12 months exists for the crop and nearest market. The AI add-on is enabled.
**Post-conditions:** The market timing advice is stored with timestamp and crop reference.

**Verifiability:** Ask for maize market timing with 24 months of Jinja market price data. Verify the response specifies a selling window (e.g., weeks 8–10 post-harvest), an expected price range, and an estimated UGX uplift. Repeat with only 10 months of data — verify the system outputs a data-limitation notice.

---

#### FR-AI-006: Offline Fallback

**Phase:** 3

**Stimulus:** The user opens the AI advisor when the device has no internet connectivity.
**Response:** The system shall display pre-loaded offline guides covering common farming topics (pest/disease identification guides with photos, crop calendars, basic veterinary care, and market preparation). The offline guide content shall be bundled in the app package at install time and shall be available without any network request. The system shall display a persistent banner informing the user that personalised AI advice and photo-based diagnosis require connectivity.
**Pre-conditions:** The app is installed (offline guide content is embedded in the app package; no separate download step is required).
**Post-conditions:** No data is created or modified. No network request is initiated.

**Verifiability:** Install the app on a device that has never had internet access. Open the AI advisor. Verify offline guides load immediately. Verify the connectivity banner is visible. Verify the photo diagnosis button is disabled with a "requires internet" tooltip. Confirm via network monitor that zero outbound requests are made during the offline session.

---

## 3.17 Director Platform

#### FR-DIR-001: Consolidated Farm View

**Phase:** 4

**Stimulus:** The director opens the director dashboard.
**Response:** The system shall display a consolidated view of all farms the director has oversight of, showing: farm name, location, total area, active crops, livestock count, financial summary (monthly income/expense/net), and overall status (green/amber/red based on configurable thresholds).
**Pre-conditions:** The user has the "Director" role with associated farm assignments.
**Post-conditions:** No data modification occurs.

**Verifiability:** A director with 3 farms views the dashboard. Verify all 3 farms are listed with correct summary metrics. Verify clicking a farm navigates to its detailed view.

---

#### FR-DIR-002: Financial Summary Across Farms

**Phase:** 4

**Stimulus:** The director opens the financial summary view.
**Response:** The system shall display a consolidated financial dashboard showing total income, total expenses, and net profit across all assigned farms for a selected period. Breakdown by farm and by enterprise type shall be available.
**Pre-conditions:** Financial records exist across assigned farms.
**Post-conditions:** No data modification occurs.

**Verifiability:** View financial summary for Q1 2027 across 3 farms. Verify total income, expenses, and net profit are correct aggregates. Drill down by farm — verify individual farm totals.

---

#### FR-DIR-003: Livestock Health Dashboard

**Phase:** 4

**Stimulus:** The director opens the livestock health dashboard.
**Response:** The system shall display aggregated IoT health alerts from all assigned farms: total animals monitored, animals with warnings/critical alerts, recent disease warnings, and heat detections.
**Pre-conditions:** IoT data exists for animals across assigned farms.
**Post-conditions:** No data modification occurs.

**Verifiability:** With IoT devices across 3 farms, verify the dashboard aggregates all alerts. Verify a critical alert on Farm 2 appears on the director's dashboard.

---

#### FR-DIR-004: Harvest Forecast

**Phase:** 4

**Stimulus:** The director views the harvest forecast.
**Response:** The system shall display expected harvest quantities per crop across all assigned farms for the current and next season, based on planted area and variety benchmarks.
**Pre-conditions:** Active crop seasons exist with planted areas and variety benchmarks.
**Post-conditions:** No data modification occurs.

**Verifiability:** With 3 farms growing maize (total 50 acres at 3.5 bags/acre benchmark), verify the forecast shows approximately 175 bags expected. Verify the forecast breaks down by farm.

---

#### FR-DIR-005: Approval Workflow

**Phase:** 4

**Stimulus:** A farm manager submits a purchase request exceeding a configurable threshold (default: UGX 5,000,000).
**Response:** The system shall route the request to the director for approval. The director can approve, reject, or request modification. The farm manager is notified of the decision.
**Pre-conditions:** The approval threshold is configured. The request exceeds the threshold.
**Post-conditions:** The request status updates to Approved/Rejected/Modification Requested; the requester is notified.

**Verifiability:** Submit a purchase request for UGX 7,000,000 as a farm manager. Verify the director receives a notification. Approve the request — verify the farm manager is notified of approval. Reject a second request — verify the rejection notification includes the reason.

---

#### FR-DIR-006: Inter-Farm Transfer

**Phase:** 4

**Stimulus:** The director initiates a transfer of equipment or animals between two farms under their oversight.
**Response:** The system shall create a transfer record, update the asset's assigned farm, and notify both farm managers. For animals, the movement is logged in the animal's movement history.
**Pre-conditions:** Both farms are assigned to the director. The asset exists on the source farm.
**Post-conditions:** The asset is moved to the destination farm; transfer and movement records are created.

**Verifiability:** Transfer tractor "T-001" from Farm A to Farm B. Verify the tractor now appears in Farm B's equipment list and no longer in Farm A's. Verify both farm managers receive notifications. Transfer animal "AK-005" — verify the movement is logged.

---
