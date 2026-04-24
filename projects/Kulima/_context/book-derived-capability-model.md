# Book-Derived Capability Model

## Purpose

This note captures the management capabilities Kulima should emphasise after reviewing three source books provided for the project:

1. `Agribusiness Management`
2. `The Organic Farmer's Business Handbook: A Complete Guide to Managing Finances, Crops, and Staff - and Making a Profit`
3. `Whole Farm Management`

The books were used for synthesis only. This document paraphrases the management themes and converts them into product requirements for Kulima.

## Core Insight

The books agree on a simple point: a farm management system becomes useful when it helps the farm plan, execute, control, analyse, and improve the business of farming. A system that only records field activities, weather, or hardware data is incomplete.

## Capability Themes Pulled from the Books

### 1. Whole-farm planning
- Farms need an explicit annual and seasonal operating plan.
- Planning must cover natural resources, infrastructure, labour, finances, and enterprise choices.
- The software should connect strategy to field execution and measurement.

### 2. Profit-centre management
- Farmers need enterprise budgets, crop/livestock journals, and gross margin visibility.
- The product should show which enterprises make money and which absorb cash.
- Records must support decisions, not just archive history.

### 3. Commercial controls
- Purchases, categories, approvals, suppliers, and paper flows are major leakage points.
- Kulima should track requested, ordered, received, invoiced, and paid states for commercial purchases.
- Management needs clear receivables, payables, and working-capital visibility.

### 4. Labour and management discipline
- Labour is a major farm cost and must be planned, assigned, tracked, and evaluated.
- Commercial farms need SOPs, training records, role clarity, and performance visibility.
- Task systems should support crews, not only individuals.

### 5. Post-harvest and market execution
- Useful farm software must continue past production into storage, packing, dispatch, contracts, and customer delivery.
- Price, market channel, and timing decisions are management decisions, not separate bookkeeping tasks.

### 6. Financial analysis and investment decisions
- Budgeting, cash flow, ratio-style analysis, and capital investment evaluation are foundational management tools.
- Kulima should support scenario planning and investment appraisal for commercial farms.

### 7. Risk, compliance, and stewardship
- Farms manage biological, financial, regulatory, and market risk at the same time.
- Compliance and traceability must be integrated into operations, not bolted on at dispatch time.

## Capability Changes Recommended for Kulima

### Elevate into the management core
- Whole-farm planning workspace
- Enterprise budgets and monthly budget vs actuals
- Procurement and supplier controls
- Labour planning, SOPs, and training records
- Customer, contract, and collections visibility

### Treat as commercial growth capabilities
- Lot-level inventory and packhouse controls
- Dispatch compliance gates
- Scenario planning and capital investment evaluation
- Benchmarking across farms and enterprises

### Keep as add-ons after the core is trusted
- AI advisor
- IoT data
- GPS animal tracking
- Camera surveillance

## Kulima Design Principle from the Synthesis

Kulima should behave like a farm operating system:

`plan -> assign -> execute -> record -> control -> sell -> analyse -> improve`

If a feature does not improve one of those steps for a real farm manager, it should not displace higher-priority management capabilities.
