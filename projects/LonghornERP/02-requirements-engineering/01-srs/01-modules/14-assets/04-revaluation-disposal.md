# Revaluation and Disposal — Upward/Downward Revaluation, Sale, Write-Off, and GL Postings

## 4.1 Overview

Asset revaluation adjusts the carrying amount of an asset to its fair value, as permitted by IAS 16 using the revaluation model. Disposal records the removal of an asset from the register — either by sale or write-off — and recognises the resulting gain or loss in the Profit and Loss account.

## 4.2 Asset Revaluation

### 4.2.1 Upward Revaluation

When an asset's fair value exceeds its current NBV, the increase is credited to the Revaluation Reserve equity account, per IAS 16 §39. If the same asset has a prior revaluation decrease recognised in Profit and Loss, the current upward revaluation is first recognised in Profit and Loss to the extent it reverses that prior decrease; any remaining surplus is then credited to Revaluation Reserve.

**FR-ASSET-025:** When an authorised user submits an upward revaluation for an asset, the system shall compute the revaluation surplus as *FairValue − NBV*, post a GL journal crediting the Revaluation Reserve account and debiting the Asset Cost account for the surplus, update the asset's carrying amount to the new fair value, reset the accumulated depreciation to zero on the asset record, recalculate the depreciation schedule from the new carrying amount over the remaining useful life, and return HTTP 200 with the updated NBV within ≤ 3 seconds at P95.

**FR-ASSET-026:** When the asset subject to upward revaluation has a previously posted downward revaluation recognised in Profit and Loss, the system shall first credit the Profit and Loss account up to the amount of the prior loss and credit any residual surplus to the Revaluation Reserve, producing separate GL lines for each portion within the same atomic journal.

### 4.2.2 Downward Revaluation

**FR-ASSET-027:** When an authorised user submits a downward revaluation for an asset, the system shall compute the decrease as *NBV − FairValue*, post a GL journal debiting the Profit and Loss (Impairment Loss or Revaluation Decrease) account and crediting the Accumulated Depreciation or Asset Cost account as appropriate, update the asset's carrying amount to the new fair value, and recalculate the depreciation schedule from the new carrying amount over the remaining useful life.

**FR-ASSET-028:** When the asset subject to downward revaluation has a Revaluation Reserve balance from a prior upward revaluation, the system shall first debit the Revaluation Reserve up to the available balance before debiting any remainder to Profit and Loss, producing separate GL lines for each portion within the same atomic journal.

**FR-ASSET-029:** When any revaluation (upward or downward) is submitted without a supporting revaluation basis note (text field, ≥ 10 characters), the system shall reject the submission with HTTP 422 and the message "Revaluation basis is required."

## 4.3 Asset Disposal

### 4.3.1 Gain and Loss Formula

The gain or loss on disposal is:

$$Gain = DisposalProceeds - NBV$$

A positive result is a gain; a negative result is a loss. When the asset is written off with no proceeds, $DisposalProceeds = 0$ and the entire NBV is recognised as a loss.

**FR-ASSET-030:** When an authorised user initiates a disposal by sale, the system shall require: disposal date, disposal proceeds (numeric, ≥ 0), disposal method (*Sale*), counterparty name, and a supporting reference (invoice or receipt number).

**FR-ASSET-031:** When an authorised user initiates a write-off disposal, the system shall require: disposal date, write-off reason (free text, ≥ 10 characters), and disposal method (*Write-Off*); proceeds shall default to 0 and the full NBV shall be posted as a loss.

**FR-ASSET-032:** When a disposal is confirmed, the system shall compute NBV at the disposal date (NBV = Acquisition Cost − Total Accumulated Depreciation posted through the last completed period), compute $Gain = DisposalProceeds - NBV$, and post a GL journal within a single atomic transaction with the following structure:

- Debit: Proceeds receivable or cash account (for sales disposals), amount = disposal proceeds.
- Debit: Accumulated Depreciation account (to clear accumulated depreciation balance).
- Credit: Asset Cost account (to derecognise asset at cost).
- Debit or Credit: Disposal Gain/Loss account — debit if loss ($Gain < 0$), credit if gain ($Gain > 0$), amount = $|Gain|$.

**FR-ASSET-033:** When a disposal journal is posted, the system shall set the asset status to *Disposed*, record the disposal date, disposal method, proceeds, and gain/loss amount on the asset master record, and prevent all further depreciation runs from including the disposed asset.

**FR-ASSET-034:** When a disposal is posted and the asset has a Revaluation Reserve balance, the system shall transfer the entire remaining Revaluation Reserve balance for that asset to Retained Earnings via a separate GL journal line within the same disposal transaction, per IAS 16 §41.

**FR-ASSET-035:** When an authorised user attempts to reverse a posted disposal, the system shall require: reversal reason (free text, ≥ 10 characters) and approval from a user with the `assets.reverse_disposal` permission; upon approval the system shall post an equal and opposite reversal journal, restore the asset status to *Active*, and write a full audit log entry within the same transaction.
