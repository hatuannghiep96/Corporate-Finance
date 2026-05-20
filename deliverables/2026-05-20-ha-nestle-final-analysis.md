# Nestlé S.A. (NESN) — Financial Ratio Analysis FY2025

**Author:** Ha Tuan Nghiep
**Date:** 2026-05-20
**Course:** BUS-629 International Corporate Finance — VEMBA 33
**Company:** Nestlé S.A. (NESN, SIX Swiss Exchange)
**Data source:** Consolidated Financial Statements FY2025 (IFRS, CHF millions)

> **Editorial note:** This document is the evaluated and annotated final analysis. The raw LLM output (`deliverables/2026-05-20-ha-nestle-llm-raw.md`) was reviewed against the Stage 3 workbook and the manual verification table (`analysis/validation/2026-05-20-ha-nestle-stage5-verification.md`). Two rounding corrections were applied: Du Pont ROE (22.1% → 22.2%) and Current Ratio (0.79x reported; precise value 0.786x). All ratio formulas and arithmetic were independently verified. Strategic recommendations reflect my own judgment, informed by direct operational experience managing the coffee product line at Nestlé Vietnam (June 2022–August 2023).

---

## Executive Summary

Nestlé S.A. enters FY2025 in a paradox familiar to large-cap FMCG companies: strong headline profitability masking structural pressure beneath. Net sales of CHF 89,490M and net income of CHF 9,033M produced an ROC (average capitalization) of 12.4% — comfortably above the 9.0% WACC and confirming value creation. EVA of CHF 2,456M is positive but thin relative to the company's scale. The performance premium, however, is almost entirely leverage-driven: Du Pont decomposition reveals an operating profit margin of 11.6% and asset turnover of 0.64x yielding a standalone ROA of 7.47% — below the cost of capital. It is the 3.85x leverage factor that amplifies ROE to 22.2%.

This leverage is sustainable near-term given Nestlé's investment-grade rating and CHF 15.9B operating cash flow. But at net debt/EBITDA of 2.90x — the top of management's own 2–3x target — the buffer is thin. Three structural vulnerabilities require active management: margin erosion (trading operating profit margin fell 180bps from 16.0% to 14.2%), asset base inefficiency (CHF 44.3B intangibles diluting asset turnover to 0.64x), and capital allocation discipline following completion of the buyback program. Five recommendations follow from the ratio evidence.

---

## Ratio Results

### Performance

| Ratio | Formula | Value | Interpretation |
|---|---|---|---|
| Market Value Added (MVA) | `market_capitalization − currentYear_equity` | CHF 152,280M | Substantial brand and distribution value not on balance sheet |
| Market-to-Book | `market_capitalization / currentYear_equity` | 5.61x | Premium justified only if ROC sustainably exceeds WACC |
| Economic Value Added (EVA) | `currentYear_after_tax_operating_income − (cost_capital × startYear_total_capitalization)` | CHF 2,456M | Positive but thin; vulnerable to margin deterioration |

### Profitability

| Ratio | Formula | Value | Interpretation |
|---|---|---|---|
| ROA (start-year assets) | `currentYear_after_tax_operating_income / startYear_total_assets` | 7.5% | Below WACC on start-year basis |
| ROC (start-year cap) | `currentYear_after_tax_operating_income / startYear_total_capitalization` | 11.8% | Above WACC; value-creating |
| ROE (start-year equity) | `INC_net / startYear_equity` | 24.6% | Leverage-amplified |
| ROA (avg assets) | `currentYear_after_tax_operating_income / avg_total_assets` | 7.8% | Primary ROA metric; below WACC |
| ROC (avg cap) | `currentYear_after_tax_operating_income / avg_total_capitalization` | 12.4% | Primary ROC metric; 340bps above WACC |
| ROE (avg equity) | `INC_net / avg_equity` | 25.9% | Primary ROE metric |

### Efficiency

| Ratio | Formula | Value | Interpretation |
|---|---|---|---|
| Asset Turnover | `INC_sales / startYear_total_assets` | 0.64x | Intangible-heavy balance sheet structurally dilutes turnover |
| Receivables Turnover | `INC_sales / startYear_receivables` | 7.95x | Healthy for FMCG at scale |
| Avg Collection Period | `startYear_receivables / currentYear_daily_sales_average` | 45.9 days | Upper edge of FMCG norm; large retail counterparty terms |
| Inventory Turnover | `INC_cost_goods_sold / startYear_inventory` | 3.67x | Stable; automated replenishment system maintains discipline |
| Days in Inventory | `startYear_inventory / currentYear_cost_goods_sold_daily` | 99.4 days | High in absolute terms; normal for 188-country supply chain |
| Profit Margin | `INC_net / INC_sales` | 10.1% | Solid net margin at FMCG scale |
| Operating Profit Margin | `currentYear_after_tax_operating_income / INC_sales` | 11.6% | Template figure; see Limitations for definition note |

### Leverage

| Ratio | Formula | Value | Interpretation |
|---|---|---|---|
| Debt Ratio | `currentYear_liabilities_total / currentYear_assets_total` | 74.0% | Highly leveraged; appropriate for investment-grade FMCG |
| Times Interest Earned | `INC_ebit / INC_interest_expense` | 5.67x | Comfortable; well above 3x floor |
| Debt Burden | `INC_net / INC_taxable_income` | 0.774x | 22.6% of taxable income consumed before reaching net income |

### Liquidity

| Ratio | Formula | Value | Interpretation |
|---|---|---|---|
| Current Ratio | `currentYear_assets_current / currentYear_liabilities_current` | 0.786x | Below 1.0x — structural, not distress; cash-flow-driven liquidity |
| Quick Ratio | `(currentYear_assets_current − BAL_inventories_curr) / currentYear_liabilities_current` | 0.470x | Inventory exclusion reveals reliance on receivables cycle |
| Cash Ratio | `currentYear_cash_marketable_securities / currentYear_liabilities_current` | 0.153x | CHF 15.9B operating CF is the real liquidity buffer |

> **Correction note (Current Ratio):** The raw LLM output reported 0.79x. Precise value is 31,969 / 40,694 = 0.786x. Both are within spec rounding conventions; 0.786x is reported here for transparency.

---

## Du Pont Decomposition

| Component | Formula | Value |
|---|---|---|
| Operating Profit Margin | `currentYear_after_tax_operating_income / INC_sales` | 11.637% |
| Asset Turnover | `INC_sales / startYear_total_assets` | 0.6426x |
| Leverage | `BAL_assets_total_curr / BAL_equity_shareholders_curr` | 3.846x |
| Debt Burden | `INC_net / INC_taxable_income` | 0.7739x |
| **Du Pont ROA** | Margin × Turnover | **7.47%** |
| **Du Pont ROE** | Margin × Turnover × Leverage × Burden | **22.2%** |

> **Correction note (Du Pont ROE):** Raw LLM output stated 22.1%. Correct unrounded value is 22.26% → 22.2%. The LLM rounded each intermediate component before multiplying, compounding error across four steps. Carrying full precision gives 22.2%. This is a spec gap documented in the retrospective.

**Primary driver: Leverage (3.85x).** Margin (11.6%) and turnover (0.64x) yield a Du Pont ROA of 7.47% — below WACC on a standalone basis. The 3.85x leverage factor, modulated by a 0.774x debt burden, is what elevates Du Pont ROE to 22.2%. Without leverage, Nestlé does not clear its cost of capital at the asset level.

**Time-mismatch:** Du Pont ROE (22.2%) differs from direct ROE (25.9%) because leverage uses current-year assets (127,151) while turnover uses prior-year assets (139,264). Per spec §6 Rule 4, this is intentional and the two figures are not directly comparable.

---

## Category Analysis

**Performance.** MVA of CHF 152.3B prices in Nestlé's brand equity, distribution depth across 188 countries, and global pricing power — none of which appears on the balance sheet. EVA of CHF 2,456M confirms value creation above the cost of capital, but the spread is thin for a company of this scale. A 1% decline in after-tax operating income reduces EVA by roughly CHF 104M — a sensitivity the capital allocation team must stress-test against the FY2026 margin recovery trajectory, particularly if volume softness continues in developed markets.

**Profitability.** ROC (avg) of 12.4% clears the 9.0% WACC by 340 basis points. Management's reported ROIC of 14.1% (FY2024) is approximately 1.7 percentage points higher, reflecting a definitional difference: management uses invested capital (net debt + equity) while the template uses total capitalization (long-term debt + equity) on an average basis. The direction is identical — both confirm above-WACC returns — but the magnitudes differ by convention. ROA (avg) of 7.8% sitting below WACC is a structural feature of the leverage model: Nestlé's value creation happens at the capitalization level, not the total asset level.

**Efficiency.** Asset turnover of 0.64x reflects an asset base structurally weighted toward intangibles (CHF 44.3B goodwill and intangibles, 35% of total assets) and manufacturing infrastructure spread across markets with declining volumes post-pricing cycle. The collection period of 45.9 days sits at the upper edge of the 30–45 day FMCG norm, reflecting Nestlé's exposure to large retail counterparties — Walmart, Carrefour, Tesco — that negotiate extended payment terms as a condition of shelf space. On inventory, the 99.4 days figure is high in absolute terms but operationally grounded. At Nestlé Vietnam, I managed the coffee product line within a proprietary replenishment system that connected directly with supplier ERP systems — tracking inventory on hand, daily selling rates, and product type to issue daily recommended purchase orders (internally called "Đơn Hàng Đề Nghị"). The system maintained a safety stock of 15–21 days depending on product type, running through three commitment stages: a fully flexible stage, a ±5 unit adjustment stage, and a final locked stage where suppliers were required to deliver exactly as ordered. The effect, over time, was that the system captured real demand — systematically eliminating the bullwhip effect that inflates inventory buffers throughout a supply chain. A group-level inventory turnover of 3.67x and 99.4 days reflects the complexity of 188 countries and multiple temperature-controlled categories, not an absence of discipline.

**Leverage.** Debt ratio of 74.0% and TIE of 5.67x confirm Nestlé is highly but comfortably leveraged. Interest is covered 5.7 times by EBIT — well above the 3x threshold. The debt burden of 0.774x means 22.6% of taxable income is consumed before reaching net income. Cross-referencing management's net debt/EBITDA of 2.90x: this is the top of the stated 2–3x target range, with limited headroom for further debt-financed M&A or share buybacks. Refinancing legacy low-rate debt at current rates will continue to pressure the debt burden ratio in FY2026.

**Liquidity.** Current ratio of 0.786x and quick ratio of 0.470x are structurally below 1.0x — a feature of Nestlé's business model. The company operates with negative NWC of (CHF 8,725M) because trade payables of CHF 20,023M substantially exceed current receivables and inventories combined. At Nestlé Vietnam, the standard supplier payment term was 90 days — a global policy from the parent company applied uniformly across the supply base, regardless of supplier size. This meant Nestlé Vietnam was effectively financing its operations on supplier credit for three months, a structural working capital advantage that flows directly into the negative NWC position visible in the consolidated balance sheet. The cash ratio of 0.153x confirms on-hand liquidity is modest; the CHF 15.9B annual operating cash flow is the real buffer — an order of magnitude larger than any balance-sheet liquidity ratio captures.

---

## Strategic Recommendations

**1. Accelerate debt reduction while the buyback program is dormant.**
`RATIO_debt_ratio` at 74.0% and net debt/EBITDA at 2.90x leave limited headroom. With buybacks complete (CHF 213M in FY2025 vs CHF 4.7B in FY2024), CHF 15.9B operating cash flow creates a window to delever. Recommendation: target CHF 3–5B of gross debt repayment in FY2026, aiming for net debt/EBITDA of 2.40–2.50x by year-end. Primary risk: reduces flexibility for opportunistic bolt-on acquisitions in high-growth categories if targets emerge.

**2. Establish quarterly margin milestones tied to "Fuel for Growth."**
Trading operating profit margin fell 180bps from 16.0% (FY2024) to 14.2% (FY2025). The CHF 2.5B "Fuel for Growth" savings are not yet visible in results. Recommendation: implement quarterly board-level margin milestone reporting — target 15.0% by FY2026 and 16.0% by FY2027 — and tie short-term incentive compensation to margin recovery, not organic growth volume alone. Primary risk: cost-focused cuts risk under-investing in brand-building, accelerating private label share gains in Europe and North America.

**3. Rationalize the intangible portfolio to improve asset turnover.**
`RATIO_asset_turnover` of 0.64x is diluted by CHF 44.3B in goodwill and intangibles (35% of total assets). Recommendation: divest or license brands generating below-group organic growth for three consecutive years, targeting a 10–15% reduction in the intangible asset base over FY2026–FY2028. Proceeds fund Recommendation 1. Primary risk: divested brands may recover under new ownership; transitional service agreements create 12–24 months of operational drag.

**4. Expand the replenishment system globally to protect NWC and reduce inventory days.**
`currentYear_working_capital_net` of (CHF 8,725M) reflects the 90-day supplier payment terms and automated replenishment discipline I observed directly at Nestlé Vietnam. The multi-stage commitment model — flexible, ±5 adjustment, locked — captures real demand over time and eliminates bullwhip-driven safety stock inflation. Recommendation: accelerate global rollout of the replenishment platform to markets still running manual ordering, targeting a 5–7 day reduction in days-in-inventory (from 99.4 to ~92–94 days) over three years. Primary risk: ERP integration with local suppliers in emerging markets requires significant IT investment and change management.

**5. Redeploy incremental capex into above-WACC growth categories.**
ROC (avg) of 12.4% exceeds WACC by 340bps, but the spread is narrowing. Recommendation: increase capex allocation to pet care, medical nutrition, and premium coffee by 20–30% in FY2026–FY2027, funded by divestiture proceeds from Recommendation 3. Deprioritize capex in water and mainstream confectionery where pricing power is structurally weaker. Primary risk: medical nutrition has longer regulatory lead times and higher working capital intensity, requiring patient capital with a 3–5 year payback horizon.

---

## Limitations

- **Operating margin definition gap:** Template `RATIO_operating_profit_margin` (11.6%) uses after-tax operating income; Nestlé's reported trading operating profit margin (14.2%) uses pre-tax trading operating profit. The 260bps gap is definitional, not an error. Both confirm margin pressure directionally.
- **ROIC definition mismatch:** Template ROC (12.4%, avg capitalization) vs. management ROIC (14.1%, FY2024, invested capital) differ by ~1.7 percentage points due to denominator scope and period. Both confirm ROIC exceeds WACC.
- **CHF appreciation distortion:** CHF strengthened significantly vs. USD and EUR in FY2024, reducing reported sales by ~7.5%. Revenue-based ratios (asset turnover, collection period) are affected. Organic growth figures are the cleaner measure of underlying performance.
- **Consolidated group level only:** All ratios aggregate 188 countries. Zone AOA (Asia, Oceania, Africa) — which includes Vietnam — may differ materially from group averages and is not separately captured.
- **Share price point-in-time:** `share_price` of CHF 72.06 (December 31, 2025) drives MVA and market-to-book. These are equity-market-sensitive and should not be interpreted as intrinsic value measures.

---

## LLM Evaluation & Annotations

**What the LLM executed correctly:**

The LLM followed the spec structure precisely — all six ratio categories computed in the correct order, all named ranges referenced explicitly, and all benchmark comparisons grounded in the spec's guidance. Three specific executions deserve credit. First, the collection period calculation correctly used `startYear_receivables` (11,251 — FY2024 balance) rather than current-year receivables (10,561 — FY2025 balance); this is the spec-consistent choice and a common LLM error that did not occur here. Second, the EVA computation correctly used `startYear_total_capitalization` (88,390) as the capital base — not the average or current-year figure — despite three capitalization figures appearing in close proximity in the spec. Third, both validation rule pre-emptions in §6 (negative NWC structural note and Du Pont ROE time-mismatch) appeared correctly in the output without prompting, which meaningfully improved the analytical quality of the leverage and liquidity sections.

**Where the LLM deviated:**

Two deviations were identified in the manual verification table, both rounding artifacts rather than formula errors. The Du Pont ROE was stated as 22.1% instead of the correct 22.2% — caused by the LLM rounding each of the four intermediate components before multiplying, compounding error across four steps. The current ratio was stated as 0.79x; the precise value is 0.786x, within spec rounding conventions. Both were corrected in this final analysis with full arithmetic shown.

**Errors caused by spec gaps vs. LLM limitations:**

Both deviations are traceable to spec gaps, not LLM capability failure. The Du Pont rounding error would have been prevented by a single sentence in Section 6 instructing the executor to carry four decimal places through intermediate Du Pont steps. The current ratio rounding is ambiguous — both 0.79x and 0.786x are valid at different decimal conventions, and the spec did not specify which to use for ratio multiples. The LLM produced no hallucinated values, no fabricated named ranges, and no invented financial figures. Given the complexity of the 25+ ratio computation task, this is a strong execution result.

**Link to spec retrospective:** Full section-by-section verdict, three gap analyses, and effectiveness rating available at `deliverables/2026-05-20-ha-nestle-spec-retrospective.md`.

---

## Executive Justification

Nestlé is a company I know from the inside — not from a Bloomberg terminal, but from the warehouse floor, the supplier negotiation table, and the demand planning system. That perspective shapes my read of these ratios in ways the LLM cannot replicate.

The numbers confirm what anyone who has worked inside a world-class FMCG operation already suspects: Nestlé's moat is not its margin, and it is not its asset base. It is the operational discipline that converts a 74% debt ratio and a 0.64x asset turnover into a 25.9% ROE and CHF 15.9B of operating cash flow year after year. The replenishment system I used daily in Vietnam — three commitment stages, real-time ERP integration, 15–21 day safety stock targets — is not a logistics tool. It is a cash flow engine. It eliminates the bullwhip effect that inflates inventory buffers throughout supply chains, and the CHF 8,725M negative NWC position in this balance sheet is its financial signature at the group level.

What concerns me — and what the LLM's recommendations captured directionally but not with enough urgency — is the margin trajectory. A 180bps decline in trading operating profit margin in a single year is not a rounding error. It is a signal that pricing power, which carried Nestlé through the post-COVID recovery, is exhausting itself faster than volume recovery is materialising. The "Fuel for Growth" program exists because management already knows this. The question is whether CHF 2.5B in cost cuts is enough to restore a 16% margin in a portfolio where the highest-growth segments (pet care, medical nutrition) are also the most capital-intensive.

My strategic thesis: Nestlé in FY2025 is a company at an inflection point between two identities — the high-dividend, high-leverage incumbent that returned CHF 7.8B to shareholders in a single year, and the focused portfolio company that needs to reinvest in above-WACC growth categories to sustain its ROC spread. The ratio evidence suggests it cannot be both simultaneously, not at 2.90x net debt/EBITDA with a contracting margin. The next two years will reveal which identity management chooses. My recommendation, grounded in the leverage and efficiency ratios above, is that the inflection should resolve toward debt reduction and portfolio rationalization — not because it is the comfortable choice, but because the arithmetic of EVA at CHF 2,456M on a CHF 89.5B revenue base leaves almost no margin for error.
