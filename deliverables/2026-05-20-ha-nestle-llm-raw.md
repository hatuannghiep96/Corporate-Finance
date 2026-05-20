# Nestlé S.A. (NESN) — Financial Ratio Analysis FY2025

**Author:** Ha Tuan Nghiep
**Date:** 2026-05-20
**Version:** 1.0 — Raw LLM Output (unedited)
**Spec source:** `docs/specs/2026-05-20-ha-nestle-spec.md`

---

## Executive Summary

Nestlé S.A. (NESN) enters FY2025 as the world's largest food and beverage company by revenue, but the ratio evidence reveals a company under meaningful financial pressure on three dimensions: contracting margins, elevated leverage, and a shrinking asset base. Net sales of CHF 89,490M delivered a net income of CHF 9,033M, but the template's operating profit margin of 11.6% sits well below Nestlé's own reported trading operating profit margin of 14.2% — the gap attributable to the template's after-tax treatment. ROC of 12.4% (avg) clears the 9.0% WACC hurdle, confirming Nestlé is creating economic value, but the margin between ROIC and WACC has narrowed. Leverage at 3.85x (assets/equity) amplifies a moderate asset turnover of 0.64x into an ROE of 24.8% — impressive on the surface but structurally dependent on debt that is already at the top of management's 2–3x net debt/EBITDA target range. Liquidity ratios below 1.0x are structurally expected and are backstopped by CHF 15.9B in operating cash flow. Five strategic recommendations follow from the ratio evidence, centered on leverage reduction, margin recovery, and asset portfolio rationalization.

---

## Ratio Results

### Performance

| Ratio | Formula | Computed Value | Interpretation |
|---|---|---|---|
| Market Value Added (MVA) | `market_capitalization − currentYear_equity` | CHF 152,230M | Market values Nestlé at CHF 152.2B above book equity — significant premium |
| Market-to-Book | `market_capitalization / currentYear_equity` | 5.61x | Premium of 5.61x over book; justified only if ROC sustainably exceeds WACC |
| Economic Value Added (EVA) | `currentYear_after_tax_operating_income − (cost_capital × startYear_total_capitalization)` | CHF 2,696M | EVA > 0 confirms value creation; spread over WACC is positive but thin |

*Calculations:*
- `market_capitalization` = 72.06 × 2,572 = CHF 185,338M
- `currentYear_equity` = CHF 33,058M
- MVA = 185,338 − 33,058 = **CHF 152,280M**
- Market-to-Book = 185,338 / 33,058 = **5.61x**
- `startYear_total_capitalization` = 51,697 + 36,693 = CHF 88,390M
- EVA = 10,411 − (0.09 × 88,390) = 10,411 − 7,955 = **CHF 2,456M**

---

### Profitability

| Ratio | Formula | Computed Value | Interpretation |
|---|---|---|---|
| ROA (start-year assets) | `currentYear_after_tax_operating_income / startYear_total_assets` | 7.5% | Below WACC of 9.0% on start-year basis |
| ROC (start-year cap) | `currentYear_after_tax_operating_income / startYear_total_capitalization` | 11.8% | Above WACC; value-creating on start-year basis |
| ROE (start-year equity) | `INC_net / startYear_equity` | 24.6% | Strong; leverage-amplified |
| ROA (avg assets) | `currentYear_after_tax_operating_income / avg_total_assets` | 7.8% | Slightly above start-year; below WACC |
| ROC (avg cap) | `currentYear_after_tax_operating_income / avg_total_capitalization` | 12.4% | Primary ROC metric; comfortably above WACC |
| ROE (avg equity) | `INC_net / avg_equity` | 25.9% | Primary ROE metric; leverage-amplified |

*Calculations:*
- `currentYear_after_tax_operating_income` = 9,033 + (1 − 0.246) × 1,826 = 9,033 + 1,378 = **CHF 10,411M**
- `startYear_total_assets` = CHF 139,264M
- `avg_total_assets` = (139,264 + 127,151) / 2 = CHF 133,208M
- `startYear_total_capitalization` = CHF 88,390M
- `avg_total_capitalization` = (88,390 + 79,304) / 2 = CHF 83,847M
- `startYear_equity` = CHF 36,693M
- `avg_equity` = (36,693 + 33,058) / 2 = CHF 34,876M
- ROA (start) = 10,411 / 139,264 = **7.5%**
- ROC (start) = 10,411 / 88,390 = **11.8%**
- ROE (start) = 9,033 / 36,693 = **24.6%**
- ROA (avg) = 10,411 / 133,208 = **7.8%**
- ROC (avg) = 10,411 / 83,847 = **12.4%**
- ROE (avg) = 9,033 / 34,876 = **25.9%**

---

### Efficiency

| Ratio | Formula | Computed Value | Interpretation |
|---|---|---|---|
| Asset Turnover | `INC_sales / startYear_total_assets` | 0.64x | Moderate; heavy intangible asset base dilutes turnover |
| Receivables Turnover | `INC_sales / startYear_receivables` | 7.95x | Healthy; consistent with large FMCG volumes |
| Avg Collection Period | `startYear_receivables / currentYear_daily_sales_average` | 45.9 days | At the upper edge of FMCG norm (30–45 days); large retail customers extend terms |
| Inventory Turnover | `INC_cost_goods_sold / startYear_inventory` | 3.67x | Stable; slight improvement signals working capital discipline |
| Days in Inventory | `startYear_inventory / currentYear_cost_goods_sold_daily` | 99.4 days | High but typical for global FMCG with long supply chains |
| Profit Margin | `INC_net / INC_sales` | 10.1% | Solid net margin for FMCG at scale |
| Operating Profit Margin | `currentYear_after_tax_operating_income / INC_sales` | 11.6% | Below Nestlé's reported 14.2% trading margin — template uses after-tax operating income |

*Calculations:*
- Asset Turnover = 89,490 / 139,264 = **0.64x**
- `startYear_receivables` = CHF 11,251M
- Receivables Turnover = 89,490 / 11,251 = **7.95x**
- `currentYear_daily_sales_average` = 89,490 / 365 = CHF 245.2M/day
- Avg Collection Period = 11,251 / 245.2 = **45.9 days**
- `startYear_inventory` = CHF 13,260M
- Inventory Turnover = 48,694 / 13,260 = **3.67x**
- `currentYear_cost_goods_sold_daily` = 48,694 / 365 = CHF 133.4M/day
- Days in Inventory = 13,260 / 133.4 = **99.4 days**
- Profit Margin = 9,033 / 89,490 = **10.1%**
- Operating Profit Margin = 10,411 / 89,490 = **11.6%**

---

### Leverage

| Ratio | Formula | Computed Value | Interpretation |
|---|---|---|---|
| Debt Ratio | `currentYear_liabilities_total / currentYear_assets_total` | 74.0% | Highly leveraged; normal for investment-grade FMCG |
| Times Interest Earned (TIE) | `INC_ebit / INC_interest_expense` | 5.67x | Comfortable; above 5x threshold |
| Debt Burden | `INC_net / INC_taxable_income` | 0.774x | Tax and financing costs consume ~22.6% of taxable income |

*Calculations:*
- Debt Ratio = 94,093 / 127,151 = **74.0%**
- TIE = 10,361 / 1,826 = **5.67x**
- Debt Burden = 9,033 / 11,673 = **0.774x**

---

### Liquidity

| Ratio | Formula | Computed Value | Interpretation |
|---|---|---|---|
| Current Ratio | `currentYear_assets_current / currentYear_liabilities_current` | 0.79x | Below 1.0x — structurally expected; backstopped by CHF 15.9B operating CF |
| Quick Ratio | `(currentYear_assets_current − BAL_inventories_curr) / currentYear_liabilities_current` | 0.47x | Inventory exclusion reveals reliance on receivables collection |
| Cash Ratio | `currentYear_cash_marketable_securities / currentYear_liabilities_current` | 0.15x | Conservative measure; operational cash generation is the real liquidity source |

*Calculations:*
- Current Ratio = 31,969 / 40,694 = **0.79x**
- Quick Ratio = (31,969 − 12,813) / 40,694 = 19,156 / 40,694 = **0.47x**
- Cash Ratio = 6,230 / 40,694 = **0.15x**

---

### Du Pont Decomposition

| Component | Formula | Value |
|---|---|---|
| Operating Profit Margin | `currentYear_after_tax_operating_income / INC_sales` | 11.6% |
| Asset Turnover | `INC_sales / startYear_total_assets` | 0.64x |
| Leverage | `BAL_assets_total_curr / BAL_equity_shareholders_curr` | 3.85x |
| Debt Burden | `INC_net / INC_taxable_income` | 0.774x |
| **Du Pont ROA** | Margin × Turnover | **7.4%** |
| **Du Pont ROE** | Margin × Turnover × Leverage × Debt Burden | **22.1%** |

*Calculations:*
- Du Pont ROA = 11.6% × 0.64 = **7.4%**
- Leverage = 127,151 / 33,058 = **3.85x**
- Du Pont ROE = 11.6% × 0.64 × 3.85 × 0.774 = **22.1%**

---

## Du Pont Decomposition Analysis

**Primary driver: Leverage (3.85x).** Nestlé's operating profit margin of 11.6% and asset turnover of 0.64x yield a Du Pont ROA of 7.4% — below the WACC of 9.0% on a standalone basis. It is the leverage factor of 3.85x, amplified by a debt burden of 0.774x, that elevates Du Pont ROE to 22.1%.

**Time-mismatch disclosure:** The Du Pont ROE of 22.1% differs from the direct ROE of 25.9% (avg equity basis) because leverage uses current-year assets (127,151) while asset turnover uses prior-year assets (139,264). This time-mismatch is intentional and consistent with the spec's §6 Rule 4 — the two measures are not directly comparable.

**Du Pont ROA vs direct ROA:** Du Pont ROA (7.4%) is close to but slightly below direct ROA on avg assets (7.8%). The small divergence (0.4%) is attributable to the time-mismatch between start-year assets in the turnover formula vs. average assets in direct ROA. Within acceptable rounding tolerance.

**Sustainability assessment:** The leverage factor of 3.85x is high but not unusual for an investment-grade FMCG company with predictable cash flows. However, at net debt/EBITDA of 2.90x (management definition, FY2024) — the top of management's stated 2–3x target range — there is limited headroom for further leverage. A meaningful deterioration in EBITDA (e.g., further volume decline, commodity cost spike) would push the ratio above the target ceiling and potentially trigger a rating review.

---

## Category Analysis

**Performance.** Nestlé's MVA of CHF 152.3B confirms that equity markets assign substantial intangible value to the brand portfolio, pricing power, and global distribution network that do not appear on the balance sheet. The market-to-book of 5.61x is high by absolute standards but consistent with a company whose book equity has been compressed by CHF 7.8B in annual dividends and historical buybacks. EVA of CHF 2,456M is positive — Nestlé is creating value above its cost of capital — but the spread is thin relative to the company's scale. A 1% decline in after-tax operating income would reduce EVA by ~CHF 1,160M, approximately halving it.

**Profitability.** ROC (avg) of 12.4% exceeds the 9.0% WACC, confirming value creation. This compares to management's reported ROIC of 14.1% (FY2024) — the gap reflects definitional differences: management's ROIC uses invested capital (net debt + equity), while the template's ROC uses total capitalization (long-term debt + equity) on an average basis. The direction is consistent; the absolute values differ by approximately 1.7 percentage points. Both measures confirm the company is earning above its cost of capital, though the spread is narrowing.

**Efficiency.** Asset turnover of 0.64x is modest for an FMCG company of this scale; the CHF 44.3B goodwill and intangibles position (35% of total assets) structurally dilutes turnover. The average collection period of 45.9 days sits at the upper edge of the 30–45 day FMCG norm — a reflection of Nestlé's exposure to large retail counterparties (Walmart, Carrefour, Tesco) that negotiate extended payment terms. Days in inventory of 99.4 days is high in absolute terms but consistent with the complexity of a 188-country supply chain managing temperature-controlled and shelf-stable product categories simultaneously. The operating profit margin of 11.6% (template) vs 14.2% (management reported) gap is a definition difference: the template's after-tax operating income denominator is lower than management's pre-tax trading operating profit.

**Leverage.** The debt ratio of 74.0% confirms Nestlé as a highly leveraged company — appropriate for an investment-grade issuer with predictable cash flows and strong pricing power. TIE of 5.67x is comfortable; interest is covered 5.7 times by EBIT, well above the 3x threshold below which concern is warranted. The debt burden of 0.774x means that 22.6% of taxable income is consumed by taxes and net financing costs before reaching net income. Cross-referencing management's net debt/EBITDA of 2.90x: this is at the top of the stated 2–3x target range, limiting the capacity for further debt-financed M&A or buybacks in the near term.

**Liquidity.** The current ratio of 0.79x and quick ratio of 0.47x are below 1.0x — a structural feature of Nestlé's business model, not a distress signal. The company operates with negative net working capital of (CHF 8,725M) because its large trade payables (CHF 20,023M) substantially exceed its current receivables and inventories combined. This is a competitive advantage: Nestlé effectively borrows from its supplier base at zero cost. The cash ratio of 0.15x confirms that on-hand liquidity is modest; however, CHF 15.9B in annual operating cash flow provides an order-of-magnitude larger liquidity buffer than any balance-sheet measure captures.

---

## Strategic Recommendations

**1. Prioritize debt reduction over buybacks in FY2026.**
`RATIO_debt_ratio` at 74.0% and management's net debt/EBITDA at 2.90x (top of the 2–3x target range) indicate limited deleveraging headroom. With the buyback program completed (CHF 213M in FY2025 vs CHF 4.7B in FY2024), the CHF 15.9B operating cash flow creates a one-time window to accelerate debt repayment. Recommendation: allocate at least CHF 3–5B of FY2026 free cash flow to gross debt reduction, targeting net debt/EBITDA of 2.50x by year-end. Primary risk: reduces financial flexibility for opportunistic M&A if a portfolio rationalization target emerges.

**2. Accelerate the "Fuel for Growth" cost reduction program to restore operating margin.**
`RATIO_operating_profit_margin` (template) declined from an implied ~12.5% (FY2024) to 11.6% (FY2025), and Nestlé's own reported trading operating profit margin fell from 16.0% to 14.2%. The CHF 2.5B "Fuel for Growth" program's savings are not yet visible in the margin trajectory. Recommendation: establish a quarterly margin recovery milestone — targeting return to 15%+ trading operating profit margin by FY2027 — and tie executive compensation to margin improvement, not just organic growth. Primary risk: aggressive cost cuts could impair brand investment, accelerating volume share loss in emerging markets.

**3. Rationalize the intangible asset portfolio to improve asset turnover.**
Asset turnover of 0.64x (`RATIO_asset_turnover`) is diluted by CHF 44.3B in goodwill and intangibles (35% of total assets). Several of these assets relate to brands and geographies with below-average organic growth. Recommendation: conduct a structured portfolio review of brands generating below-group organic growth rates; divest or license non-core brands to reduce the intangible asset base by 10–15% over three years. Primary risk: divested brands may recover under new ownership, and transaction costs reduce near-term cash flow.

**4. Extend supplier payment terms to protect negative NWC advantage.**
`currentYear_working_capital_net` of (CHF 8,725M) reflects Nestlé's structural advantage in supplier financing — the company effectively operates with zero-cost working capital funding from its supplier base. This advantage is at risk if supplier consolidation reduces Nestlé's relative bargaining power. Recommendation: implement a supply chain finance program that extends payment terms for large suppliers while offering early payment at a discount, protecting the negative NWC position. Primary risk: reputational risk if payment term extensions are perceived as predatory to smaller suppliers in emerging markets.

**5. Redeploy free cash flow into high-ROIC growth categories.**
ROC (avg) of 12.4% exceeds WACC of 9.0% by 340 basis points, but the spread is narrowing. Capital allocation into categories with above-group ROIC (pet care, coffee, medical nutrition) would sustain the spread. Recommendation: increase capex allocation to pet care and medical nutrition by 20–30% in FY2026–FY2027, funded by divestiture proceeds from non-core brands (Recommendation 3). Primary risk: execution risk in scaling medical nutrition, which has longer regulatory lead times than mainstream FMCG.

---

## Limitations

- **Template vs. management definition gap:** The template's `RATIO_operating_profit_margin` (11.6%) uses after-tax operating income as the numerator; Nestlé's reported trading operating profit margin (14.2%) uses pre-tax trading operating profit. Neither is wrong — they measure different things. Comparisons between the two require explicit disclosure.
- **ROIC definition mismatch:** Template ROC (12.4%) and management ROIC (14.1% FY2024) differ because of denominator scope (total capitalization vs. invested capital) and period (FY2025 vs. FY2024). The directional conclusion (ROIC > WACC) holds in both definitions.
- **CHF appreciation distortion:** CHF strengthened significantly versus USD and EUR in FY2024, reducing reported sales by approximately 7.5%. Year-on-year comparisons of revenue-based ratios (asset turnover, receivables turnover) are affected. Organic growth figures (not used in ratio formulas) are the cleaner measure of underlying performance.
- **Consolidated group vs. segment:** All ratios are computed at the consolidated group level aggregating 188 countries. Segment-level performance (Zone AOA, Zone AMS, Zone EMENA) may differ materially from group averages and is not captured in the template.
- **Share price point-in-time:** The `share_price` assumption (CHF 72.06, December 31, 2025) is a point-in-time value. MVA and market-to-book ratios are sensitive to equity market conditions and should not be interpreted as intrinsic value measures.
