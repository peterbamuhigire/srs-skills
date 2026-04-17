# 3. Functional Requirements

## 3.1 F-015: Research & Development

### 3.1.1 Banana Cultivar Library

**FR-RES-001**
When the Research Coordinator opens the cultivar library and creates a new cultivar record, the system shall store: cultivar name, variety code (unique, system-assigned format `VAR-NNNN`), Musa taxonomy classification (genome group, subgroup), regional suitability (configurable region list), disease resistance notes, typical maturation period (days), and source reference (publication or institution). The variety code must be unique across the entire cultivar library; a duplicate code submission shall be rejected with a field-level validation error.

**FR-RES-002**
When the Research Coordinator adds processing characteristics to a cultivar record, the system shall store: processing yield (kg flour per 100 kg fresh matooke input), dry matter content (%), starch content (%), quality score (numeric 1–10, configurable scale), moisture content (%), and any additional configurable numeric or text parameters. These values shall serve as the reference benchmark against which field trial results are compared.

**FR-RES-003**
When the Research Coordinator searches the cultivar library by cultivar name, variety code, regional suitability, or quality score range, the system shall return all matching records within 2 seconds, displayed in a sortable DataTable.

**FR-RES-004**
When the Research Coordinator cross-references a cultivar record with the Farmer Management module (F-010), the system shall display the list of registered BIRDC cooperative farmers who grow that cultivar, the total farm area (hectares) under that cultivar, and the total matooke deliveries of that cultivar in the last 12 months, without requiring a separate query.

**FR-RES-005**
When the Research Coordinator requests a cultivar distribution report, the system shall generate a report showing all cultivars in the BIRDC farmer network, the number of farmers growing each, total hectares, and average delivery volume per season, exportable to PDF and Excel within 10 seconds.

### 3.1.2 Field Trial Management

**FR-RES-006**
When the Research Coordinator creates a new field trial record, the system shall store: trial ID (format: `TRL-YYYY-NNNN`), trial name, trial objective, start date, planned end date, plot location (text description and GPS coordinates), cultivar variety code (linked to cultivar library), trial type (Fertiliser Trial / Irrigation Trial / Pruning Trial / Pest Control Trial / Other — configurable), and the name of the responsible researcher.

**FR-RES-007**
When a field trial is active, the Research Coordinator shall be able to record intervention events for that trial specifying: intervention date, intervention type (from the configurable trial type list), intervention description, input materials used (type, quantity, unit), and the researcher who applied the intervention. Multiple interventions per trial shall be supported.

**FR-RES-008**
When a harvest event is recorded for a field trial plot, the system shall store: harvest date, plot identifier within the trial, fresh weight harvested (kg), number of bunches, average bunch weight (kg), quality grade assigned, processing yield measured (kg flour per 100 kg input), and any field observations. Multiple harvests per trial over its duration shall be supported.

**FR-RES-009**
When the Research Coordinator requests a yield comparison report across trial treatments, the system shall compute and display: average processing yield per treatment group, standard deviation, percentage variance from the cultivar library benchmark, and a ranked list of treatments by average yield, within 5 seconds.

**FR-RES-010**
When a field trial is closed by the Research Coordinator, the system shall require the entry of a trial conclusion summary (free text, minimum 50 characters) and a recommendation status (Recommended for Scale-Up / Not Recommended / Requires Further Trial). The conclusion shall be stored permanently and linked to the trial record.

**FR-RES-011**
When the Research Coordinator requests a field trial status dashboard, the system shall display all active and recently closed trials in a summary table showing: trial ID, cultivar, location, start date, days elapsed, number of harvest events recorded, and current status (Planning / Active / Harvest Phase / Closed), updated in real time.

### 3.1.3 Product Development Register

**FR-RES-012**
When the Research Coordinator creates a new product development entry, the system shall store: product idea ID (format: `PD-NNNN`), product name, product description, originator (linked to employee record), date originated, product category (from a configurable list: Flour / Snack / Beverage / Fertiliser / By-product / Other), target market, and initial status (Idea Submitted).

**FR-RES-013**
When a product idea progresses to the pilot batch stage, the Research Coordinator shall be able to link one or more production order references from F-011 (Manufacturing) as pilot batch records, storing the pilot batch date, batch size, recipe version used, and actual yield achieved. The product idea status shall advance to "Pilot Batch in Progress".

**FR-RES-014**
When a sensory evaluation is conducted for a pilot batch, the Research Coordinator shall record: evaluation date, evaluator names, evaluation parameters (appearance, aroma, texture, taste, overall acceptability — each scored 1–9 on a configurable hedonic scale), overall mean score, and any evaluator comments. Multiple evaluations per pilot batch shall be supported.

**FR-RES-015**
When market testing results are available, the Research Coordinator shall record: market test date, test location, number of test participants, acceptance rate (%), key consumer feedback (text), and go/no-go recommendation. The product idea status shall advance to "Market Testing Complete".

**FR-RES-016**
When the Research Coordinator requests a product development pipeline report, the system shall display all active product ideas grouped by status stage (Idea / Pilot / Market Testing / Approved for Launch / Discontinued), with elapsed days in current stage, responsible researcher, and next planned action, exportable to PDF within 5 seconds.

### 3.1.4 Technology Transfer and IP Records

**FR-RES-017**
When the Research Coordinator records an external research partnership, the system shall store: partner organisation name, partner type (University / Government Research Institute / NGO / Private Company), partnership agreement reference number, effective date, expiry date, scope of collaboration (text), and the BIRDC research staff member responsible for the partnership.

**FR-RES-018**
When the Research Coordinator records a licensing agreement, the system shall store: licensee name, licensed technology or variety, agreement date, royalty terms (if applicable), exclusivity scope, territory, and expiry date. The system shall automatically send a renewal reminder to the Research Coordinator and Finance Director 90 days before the agreement expiry date.

**FR-RES-019**
When the Research Coordinator records an intellectual property item, the system shall store: IP title, IP type (Patent Application / Registered Variety / Trade Secret / Copyright / Other), registration number if applicable, filing date, registration date, territory, and the names of all inventors or authors. Attached documentation (PDF or image) shall be uploadable with a file size limit of 25 MB per file.

**FR-RES-020**
When the Research Coordinator records an academic publication, the system shall store: publication title, authors, journal or conference name, publication date, DOI or URL reference, and the BIRDC research project it relates to. Publications shall be searchable and filterable by author, year, and project.

### 3.1.5 R&D Expenditure Tracking

**FR-RES-021**
When the Research Coordinator or Finance Manager records an R&D expenditure, the system shall store: expenditure ID, date, description, amount (UGX), supplier or payee, related field trial ID or product development ID, and the GL cost centre "Research". The system shall post the expenditure to the GL as DR Research Expense — [Sub-category] / CR Accounts Payable or CR Cash, without requiring a separate manual journal entry.

**FR-RES-022**
When the Finance Director requests an R&D expenditure report by trial, product, or period, the system shall aggregate all expenditure records by the requested dimension and display total spend with a comparison to any configured R&D budget for that cost centre, within 5 seconds. The report shall be exportable to PDF and Excel.

**FR-RES-023**
When the Research Coordinator or Finance Director requests a full R&D project cost summary, the system shall display all expenditure categories (personnel, materials, external services, equipment, travel) per trial or product development initiative, with subtotals per category and a grand total, satisfying the Finance Director's need for parliamentary reporting on R&D investment.
