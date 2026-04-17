# Multi-Location Warehousing

## 2.1 Warehouse and Location Setup

**FR-ADVINV-001** — The system shall support a three-level location hierarchy within each branch: Warehouse → Zone → Bin (e.g., "Main Warehouse → Aisle A → Bin A1-001"); each level shall be independently configurable by name, code, and type (storage, staging, quarantine, dispatch).

**FR-ADVINV-002** — The system shall allow each item to be assigned a default storage location; when a GRN is posted for that item, the system shall suggest the default location automatically but shall permit the user to override it.

**FR-ADVINV-003** — The system shall maintain a bin-level stock balance for every item: when stock is received into a bin, transferred out of a bin, or consumed from a bin, the system shall update the bin-level balance in the same transaction as the branch-level stock movement (`FR-INV-*`).

## 2.2 Putaway and Pick from Bin

**FR-ADVINV-004** — When a GRN is confirmed and the item has a bin assigned, the system shall generate a putaway task listing the item, quantity, source location (receiving dock), and destination bin; the putaway task shall be assignable to a warehouse operative.

**FR-ADVINV-005** — When a delivery note or production issue requires stock from a specific bin, the system shall generate a pick task identifying the source bin, item, and quantity; if FEFO is enabled for the item, the system shall apply FEFO bin selection per Section 5.

**FR-ADVINV-006** — The system shall support the transfer of stock between bins within the same branch without creating a stock adjustment; a bin transfer shall update the source bin and destination bin balances while keeping the branch total unchanged.

## 2.3 Bin Occupancy and Capacity

**FR-ADVINV-007** — When a bin is configured with a maximum capacity (units or weight), the system shall warn the user if a putaway task would exceed that capacity and shall require supervisor confirmation to proceed.

**FR-ADVINV-008** — The system shall provide a warehouse map view showing each zone and bin with current occupancy percentage and the items currently stored; this view shall refresh in real time during active putaway and pick operations.
