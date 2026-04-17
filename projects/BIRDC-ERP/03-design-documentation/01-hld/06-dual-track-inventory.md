# 6. Dual-Track Inventory Design

## 6.1 Design Principle

Business Rule BR-001 mandates that warehouse stock and agent field stock are permanently separate ledgers. Cross-contamination between the two ledgers is architecturally impossible — enforced at the database schema level, the API layer, and the reporting layer.

## 6.2 Two-Table Architecture

| Aspect | Warehouse Track | Agent Track |
|---|---|---|
| Primary table | `tbl_stock_balance` | `tbl_agent_stock_balance` |
| Movement table | `tbl_inventory_movements` | `tbl_agent_stock_movements` |
| Location granularity | Warehouse location (unlimited locations) | Agent ID (one virtual store per agent) |
| Updated by | Stock receipts, transfers, sales (F-002 factory gate/showroom POS), adjustments, production output | Agent stock issuances, agent POS sales, agent stock returns |
| Float limit enforcement | Not applicable | `trg_agent_float_check` (BR-006): blocks issuance if value would exceed agent's configured float limit |
| FEFO enforcement | Yes — `InventoryService::enforceFefo()` | Yes — same logic applied to agent batch allocation |
| Reports | Warehouse stock on hand, stock movement history, stock valuation | Agent stock on hand, agent stock movement, agent outstanding balance |

## 6.3 Issuance Flow (Warehouse → Agent)

The only authorised path for inventory to move from the warehouse track to the agent track is via an explicit agent stock issuance transaction:

1. Store Manager initiates agent stock issuance in `InventoryService::processAgentIssuance()`.
2. Service checks agent float limit (BR-006): $\text{CurrentAgentStockValue} + \text{IssuanceValue} \leq \text{FloatLimit}$. Blocks if exceeded.
3. Service calls `enforceFefo()` to select the correct batches.
4. A `tbl_inventory_movements` record is created (type: `AGENT_ISSUANCE`, quantity negative, source location = warehouse).
5. A `tbl_agent_stock_movements` record is created (type: `ISSUANCE`, quantity positive, agent ID set).
6. `tbl_stock_balance` is decremented.
7. `tbl_agent_stock_balance` is incremented.
8. GL auto-post: DR Agent Receivable (Inventory) / CR Warehouse Inventory (the monetary value moves to agent-held inventory as a receivable until the agent remits cash).

## 6.4 API Endpoints Enforcing Separation

| Endpoint | Enforcement |
|---|---|
| `POST /api/inventory/transfer` | `location_type` parameter validation rejects `AGENT` as a destination — transfers are warehouse-to-warehouse only |
| `POST /api/agent/issuance` | Dedicated endpoint; always writes to agent track; never touches `tbl_stock_balance` directly |
| `POST /api/pos/agent-sale` | Reads from `tbl_agent_stock_balance` only; zero access to `tbl_stock_balance` |
| `POST /api/pos/sale` (factory gate) | Reads from `tbl_stock_balance` only; zero access to `tbl_agent_stock_balance` |
| `GET /api/reports/stock-on-hand` | `track` parameter: `warehouse`, `agent`, or `consolidated`. Response is always labelled with the track. |

## 6.5 Reporting

| Report | Source | Label |
|---|---|---|
| Warehouse Stock on Hand | `vw_stock_on_hand` (draws from `tbl_stock_balance`) | "Warehouse Inventory" |
| Agent Stock on Hand | `vw_agent_stock_on_hand` (draws from `tbl_agent_stock_balance`) | "Agent-Held Inventory" |
| Total Company Stock (consolidated) | UNION of both views | Both sections labelled separately; grand total is sum of both |

No consolidated report presents a combined stock figure without a clear breakdown showing the warehouse component and the agent-held component separately.
