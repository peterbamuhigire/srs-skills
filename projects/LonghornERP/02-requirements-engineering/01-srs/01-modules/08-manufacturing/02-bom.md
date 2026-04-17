# Bill of Materials

## 2.1 BOM Structure

**FR-MFG-001** — When a user creates a BOM, the system shall assign a unique BOM ID in the format `BOM-NNN`, capture the finished goods item code, BOM version number (starting at 1.0), effective start date, and optional effective end date; multiple BOM versions may exist for the same item but only one version may be active for a given date.

**FR-MFG-002** — Each BOM line shall record: component item code, component description, quantity per unit of finished good, unit of measure (UOM), wastage percentage (default 0%), and whether the component is a phantom item (sub-assembly that is not separately stocked).

**FR-MFG-003** — When a wastage percentage is defined on a BOM line, the system shall compute the gross required quantity as: $GrossQty = NetQty \div (1 - WastageRate)$ and shall issue the gross quantity from stock, recording the net consumed and wastage quantities separately.

**FR-MFG-004** — The system shall support multi-level BOMs with a maximum nesting depth of 5 levels; the system shall detect and reject circular BOM references (a component that directly or indirectly references the finished good itself).

## 2.2 Uganda Agro-Processing BOM Templates

**FR-MFG-005** — The system shall provide pre-configured BOM starter templates for the following Uganda agro-processing sectors: sugar (sugarcane → raw sugar → refined sugar), edible oil (sunflower seed → crude oil → refined oil), wheat flour milling (wheat grain → semolina → flour), dairy (raw milk → pasteurised milk / yoghurt / ghee), and commercial brewing (maize/sorghum → wort → beer).

**FR-MFG-006** — Uganda agro-processing BOM templates shall include sector-specific fields: intake batch (linked to farmer intake records for cooperative tenants), milling ratio (input/output kg ratio per processing run), and moisture correction factor.

## 2.3 BOM Cost Roll-Up

**FR-MFG-007** — The system shall calculate the standard cost of a finished good by rolling up all BOM component costs: $StandardCost = \sum_{i=1}^{n} (ComponentCost_i \times GrossQty_i)$; the roll-up shall traverse all BOM levels and shall use the current weighted average cost of each component.

**FR-MFG-008** — The system shall provide a BOM cost explosion report showing every component across all BOM levels, its quantity per finished unit, its current unit cost, and its contribution to the total standard cost.
