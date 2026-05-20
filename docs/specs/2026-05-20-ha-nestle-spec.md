---
template: spec
purpose: "Technical specification for Nestlé S.A. accounting ratios analysis — defines scope, inputs, formulas, validation, and analysis requirements precisely enough that any competent executor (human or LLM) can produce correct output"
audience: instructor
fields_required: [title, author, date, version, company, scope, model_architecture, data_inputs, derived_inputs, formulas, validation, analysis_requirements, output_format, references]
naming_convention: "YYYY-MM-DD-{slug}.md"
courses: [BUS-629]
---

# Nestlé S.A. — Accounting Ratios Analysis: Technical Specification

**Author:** Ha Tuan Nghiep
**Date:** 2026-05-20
**Version:** 1.0
**Company:** Nestlé S.A., NESN, SIX Swiss Exchange

---

## 1. Scope & Objective

This specification defines the complete ratio analysis for Nestlé S.A. (NESN) using audited consolidated IFRS financial statements for FY2025 (year ended December 31, 2025) as the current year and FY2024 (year ended December 31, 2024) as the prior year. All figures are in CHF millions unless otherwise noted. Reporting standard: IFRS as adopted by the IASB. Reporting currency: Swiss Francs (CHF).

The analytical objective is to compute the full suite of performance, profitability, efficiency, leverage, liquidity, and Du Pont ratios specified in the Stage 1 template, assess Nestlé's financial position and trajectory across FY2024–FY2025, and produce 3–5 actionable strategic recommendations grounded in the ratio evidence.

Intended audience: BUS-629 course instructor (Adam Stauffer), with secondary audience of a senior analyst reviewing the work for portfolio inclusion.

---

## Part A — Model Specification

### 2. Model Architecture

The workbook (`2026-05-20-ha-nestle-financials.xlsx`) contains six tabs in the following order:

| Tab | Type | Purpose |
|-----|------|---------|
| Cover | Instructions | Color key, named-range convention guide, course metadata |
| Balance Sheet | Input | FY2025 (current) and FY2024 (prior) balance sheet data |
| Income Statement | Input | FY2025 income statement data |
| Cash Flow Statement | Input | FY2025 cash flow data |
| Ratios | Input + Output | Four analyst assumptions at top; all ratios auto-compute below |
| Notes | Input | Company metadata, source URL, reporting standard, currency, FYE |

**Color coding conventions:**
- Yellow background = data inputs (hardcoded values from audited statements)
- Light blue background + blue text = analyst assumptions (share price, shares outstanding, WACC, tax rate)
- Green text = formulas and cross-sheet references — do not overwrite
- Gray background = ratio outputs — computed automatically, do not overwrite

**Input/output separation:** All hardcoded values live in Balance Sheet, Income Statement, Cash Flow, and the top section of Ratios. The Ratios tab output section is entirely formula-driven from named ranges. No manual entry in the output section.

**Units:** All monetary figures in CHF millions. Percentages formatted to one decimal. Multiples formatted to two decimals with "x" suffix.

---

### 3. Data Inputs

All values sourced from Nestlé S.A. Consolidated Financial Statements 2025 (IFRS, CHF millions). FY2024 figures are the prior-year comparatives published in the same document.

**Balance Sheet — FY2025 (Current Year)**

| Named Range | Line Item | Value (CHF M) |
|-------------|-----------|--------------|
| `BAL_cash_marketable_securities_curr` | Cash + Short-term investments | 6,230 |
| `BAL_receivables_curr` | Trade and other receivables | 10,561 |
| `BAL_inventories_curr` | Inventories | 12,813 |
| `BAL_assets_other_current_curr` | Other current assets | 2,365 |
| `BAL_assets_current_curr` | Total current assets | 31,969 |
| `BAL_ppe_curr` | Property, plant and equipment (net) | 32,549 |
| `BAL_intangibles_curr` | Goodwill + Intangible assets | 44,309 |
| `BAL_assets_other_curr` | Other non-current assets | 18,324 |
| `BAL_assets_total_curr` | Total assets | 127,151 |
| `BAL_debt_current_curr` | Current financial debt | 11,606 |
| `BAL_payables_curr` | Trade and other payables | 20,023 |
| `BAL_liabilities_other_current_curr` | Other current liabilities | 9,065 |
| `BAL_liabilities_current_curr` | Total current liabilities | 40,694 |
| `BAL_debt_long_term_curr` | Non-current financial debt | 46,246 |
| `BAL_liabilities_other_long_term_curr` | Other non-current liabilities | 7,153 |
| `BAL_liabilities_total_curr` | Total liabilities | 94,093 |
| `BAL_equity_common_curr` | Share capital + Treasury shares | (130) |
| `BAL_equity_retained_curr` | Retained earnings + Reserves + NCI | 33,188 |
| `BAL_equity_shareholders_curr` | Total equity | 33,058 |

**Balance Sheet — FY2024 (Prior Year)**

| Named Range | Line Item | Value (CHF M) |
|-------------|-----------|--------------|
| `BAL_cash_marketable_securities_prior` | Cash + Short-term investments | 7,871 |
| `BAL_receivables_prior` | Trade and other receivables | 11,251 |
| `BAL_inventories_prior` | Inventories | 13,260 |
| `BAL_assets_other_current_prior` | Other current assets | 2,806 |
| `BAL_assets_current_prior` | Total current assets | 35,188 |
| `BAL_ppe_prior` | Property, plant and equipment (net) | 33,706 |
| `BAL_intangibles_prior` | Goodwill + Intangible assets | 49,840 |
| `BAL_assets_other_prior` | Other non-current assets | 20,530 |
| `BAL_assets_total_prior` | Total assets | 139,264 |
| `BAL_debt_current_prior` | Current financial debt | 11,863 |
| `BAL_payables_prior` | Trade and other payables | 21,807 |
| `BAL_liabilities_other_current_prior` | Other current liabilities | 9,193 |
| `BAL_liabilities_current_prior` | Total current liabilities | 42,863 |
| `BAL_debt_long_term_prior` | Non-current financial debt | 51,697 |
| `BAL_liabilities_other_long_term_prior` | Other non-current liabilities | 8,011 |
| `BAL_liabilities_total_prior` | Total liabilities | 102,571 |
| `BAL_equity_shareholders_prior` | Total equity | 36,693 |

**Income Statement — FY2025**

| Named Range | Line Item | Value (CHF M) |
|-------------|-----------|--------------|
| `INC_sales` | Net sales | 89,490 |
| `INC_cost_goods_sold` | Cost of goods sold | 48,694 |
| `INC_sga` | Distribution + Marketing + R&D | 26,802 |
| `INC_depreciation` | Depreciation and amortization | 3,633 |
| `INC_ebit` | EBIT (computed) | 10,361 |
| `INC_other_income` | Other income (net, incl. associates) | 3,138 |
| `INC_interest_expense` | Financial expense | 1,826 |
| `INC_taxable_income` | Taxable income (computed) | 11,673 |
| `INC_taxes` | Taxes | 2,640 |
| `INC_net` | Net income (to parent shareholders) | 9,033 |
| `INC_dividends` | Dividends paid to parent shareholders | 7,849 |

**Cash Flow Statement — FY2025**

| Named Range | Line Item | Value (CHF M) |
|-------------|-----------|--------------|
| `CASH_operating` | Operating cash flow | 15,904 |
| `CASH_capex` | Capital expenditure | (4,527) |
| `CASH_investing` | Investing cash flow | (4,367) |
| `CASH_financing` | Financing cash flow | (12,500) |
| `CASH_net` | Net change in cash | (963) |
| `CASH_depreciation` | Depreciation (from CF reconciliation) | 3,633 |

**Analyst Assumptions (Ratios tab)**

| Named Range | Item | Value |
|-------------|------|-------|
| `yearCurrent` | Current fiscal year | 2025 |
| `share_price` | NESN closing price Dec 31, 2025 (CHF) | 72.06 |
| `shares_outstanding` | Diluted weighted avg shares (M) | 2,572 |
| `cost_capital` | Cost of capital (WACC) | 9.0% |
| `tax_rate` | Effective tax rate FY2025 | 24.6% |

---

### 4. Named Range Conventions

All named ranges in the workbook follow a strict prefix convention. Any executor (human or LLM) must reference these prefixes exactly — no abbreviations, no case changes.

| Prefix | Scope | Example |
|--------|-------|---------|
| `BAL_` | Balance sheet line items | `BAL_assets_total_curr` |
| `INC_` | Income statement line items | `INC_sales`, `INC_net` |
| `CASH_` | Cash flow statement line items | `CASH_operating`, `CASH_capex` |
| `RATIO_` | Computed ratio outputs | `RATIO_roe`, `RATIO_leverage` |
| `startYear_*` | Prior-year (FY2024) balance sheet values used as period-start denominators | `startYear_equity`, `startYear_total_assets` |
| `currentYear_*` | Current-year (FY2025) derived values computed from balance sheet inputs | `currentYear_equity`, `currentYear_working_capital_net` |
| `avg_*` | Simple average of start-year and current-year values | `avg_equity`, `avg_total_assets` |

**Convention rules:**
- All names are lowercase with underscores — no camelCase, no hyphens
- Suffix `_curr` = FY2025 current year balance sheet input
- Suffix `_prior` = FY2024 prior year balance sheet input
- Suffix `_curr` is dropped for income statement and cash flow items (single year only)
- Never hardcode a value where a named range exists — always reference the range

---

### 5. Derived Inputs

All derived inputs are computed in the Ratios tab from named ranges. The executor must not hardcode these values.

| Named Range | Formula | Value (CHF M) |
|-------------|---------|--------------|
| `market_capitalization` | `share_price × shares_outstanding` | 185,288 |
| `startYear_equity` | `BAL_equity_shareholders_prior` | 36,693 |
| `startYear_inventory` | `BAL_inventories_prior` | 13,260 |
| `startYear_receivables` | `BAL_receivables_prior` | 11,251 |
| `startYear_total_assets` | `BAL_assets_total_prior` | 139,264 |
| `startYear_total_capitalization` | `BAL_debt_long_term_prior + BAL_equity_shareholders_prior` | 88,390 |
| `currentYear_after_tax_operating_income` | `INC_net + (1 − tax_rate) × INC_interest_expense` | 10,411 |
| `currentYear_daily_sales_average` | `INC_sales / 365` | 245.2 |
| `currentYear_equity` | `BAL_equity_shareholders_curr` | 33,058 |
| `currentYear_assets_current` | `BAL_assets_current_curr` | 31,969 |
| `currentYear_liabilities_current` | `BAL_liabilities_current_curr` | 40,694 |
| `currentYear_working_capital_net` | `BAL_assets_current_curr − BAL_liabilities_current_curr` | (8,725) |
| `currentYear_debt_long_term` | `BAL_debt_long_term_curr` | 46,246 |
| `currentYear_assets_total` | `BAL_assets_total_curr` | 127,151 |
| `currentYear_total_capitalization` | `currentYear_debt_long_term + currentYear_equity` | 79,304 |
| `currentYear_liabilities_total` | `BAL_liabilities_total_curr` | 94,093 |
| `currentYear_cost_goods_sold_daily` | `INC_cost_goods_sold / 365` | 133.4 |
| `avg_equity` | `AVERAGE(startYear_equity, currentYear_equity)` | 34,876 |
| `avg_total_assets` | `AVERAGE(startYear_total_assets, currentYear_assets_total)` | 133,208 |
| `avg_total_capitalization` | `AVERAGE(startYear_total_capitalization, currentYear_total_capitalization)` | 83,847 |
| `currentYear_cash_marketable_securities` | `BAL_cash_marketable_securities_curr` | 6,230 |
| `INC_ebit` | `INC_sales − INC_cost_goods_sold − INC_sga − INC_depreciation` | 10,361 |
| `INC_taxable_income` | `INC_ebit + INC_other_income − INC_interest_expense` | 11,673 |

---

### 6. Ratio Definitions & Formulas

All ratios auto-compute in the Ratios tab output section. The executor must verify each formula references the correct named range and produces a number (no #REF!, #DIV/0!, or #NAME? errors).

**Performance**

| Ratio | Formula (named-range notation) | Unit |
|-------|-------------------------------|------|
| Market Value Added (MVA) | `market_capitalization − currentYear_equity` | CHF M |
| Market-to-Book | `market_capitalization / currentYear_equity` | x |
| Economic Value Added (EVA) | `currentYear_after_tax_operating_income − (cost_capital × startYear_total_capitalization)` | CHF M |

**Profitability**

| Ratio | Formula | Unit |
|-------|---------|------|
| ROA (start-year assets) | `currentYear_after_tax_operating_income / startYear_total_assets` | % |
| ROC (start-year cap) | `currentYear_after_tax_operating_income / startYear_total_capitalization` | % |
| ROE (start-year equity) | `INC_net / startYear_equity` | % |
| ROA (avg assets) | `currentYear_after_tax_operating_income / avg_total_assets` | % |
| ROC (avg cap) | `currentYear_after_tax_operating_income / avg_total_capitalization` | % |
| ROE (avg equity) | `INC_net / avg_equity` | % |

**Efficiency**

| Ratio | Formula | Unit |
|-------|---------|------|
| Asset Turnover | `INC_sales / startYear_total_assets` | x |
| Receivables Turnover | `INC_sales / startYear_receivables` | x |
| Avg Collection Period | `startYear_receivables / currentYear_daily_sales_average` | days |
| Inventory Turnover | `INC_cost_goods_sold / startYear_inventory` | x |
| Days in Inventory | `startYear_inventory / currentYear_cost_goods_sold_daily` | days |
| Profit Margin | `INC_net / INC_sales` | % |
| Operating Profit Margin | `currentYear_after_tax_operating_income / INC_sales` | % |

**Leverage**

| Ratio | Formula | Unit |
|-------|---------|------|
| Debt Ratio | `currentYear_liabilities_total / currentYear_assets_total` | % |
| Times Interest Earned | `INC_ebit / INC_interest_expense` | x |
| Debt Burden | `INC_net / INC_taxable_income` | x |

**Liquidity**

| Ratio | Formula | Unit |
|-------|---------|------|
| Current Ratio | `currentYear_assets_current / currentYear_liabilities_current` | x |
| Quick Ratio | `(currentYear_assets_current − BAL_inventories_curr) / currentYear_liabilities_current` | x |
| Cash Ratio | `currentYear_cash_marketable_securities / currentYear_liabilities_current` | x |

**Du Pont Decomposition**

| Component | Formula | Named Range |
|-----------|---------|-------------|
| Operating profit margin | `currentYear_after_tax_operating_income / INC_sales` | `RATIO_operating_profit_margin` |
| Asset turnover | `INC_sales / startYear_total_assets` | `RATIO_asset_turnover` |
| Leverage | `BAL_assets_total_curr / BAL_equity_shareholders_curr` | `RATIO_leverage` |
| Debt burden | `INC_net / INC_taxable_income` | `RATIO_debt_burden` |
| Du Pont ROA | `RATIO_operating_profit_margin × RATIO_asset_turnover` | % |
| Du Pont ROE | `RATIO_operating_profit_margin × RATIO_asset_turnover × RATIO_leverage × RATIO_debt_burden` | % |

---

### 7. Validation Rules

The executor must verify all of the following before proceeding to analysis:

1. **Balance Sheet balance (FY2025):** `BAL_assets_total_curr` = `BAL_liabilities_total_curr + BAL_equity_shareholders_curr` → 127,151 = 94,093 + 33,058 ✓
2. **Balance Sheet balance (FY2024):** `BAL_assets_total_prior` = `BAL_liabilities_total_prior + BAL_equity_shareholders_prior` → 139,264 = 102,571 + 36,693 ✓
3. **Du Pont ROA check:** Du Pont ROA must equal direct ROA (within rounding). If they diverge, recheck `RATIO_operating_profit_margin` and `RATIO_asset_turnover` formulas.
4. **Du Pont ROE time-mismatch note:** Du Pont ROE will not exactly equal direct ROE because leverage uses current-year assets while asset turnover uses prior-year assets. This time-mismatch is intentional — note it in the analysis.
5. **Zero formula errors:** No #REF!, #DIV/0!, or #NAME? anywhere in the Ratios tab. A #DIV/0! on a ratio means a denominator named range is empty.
6. **Net working capital is negative:** `currentYear_working_capital_net` = (8,725) CHF M. This is structurally normal for Nestlé — the company operates with negative NWC due to large trade payables from its supplier terms. Do not treat as an error.

---

## Part B — Analysis Specification

### 8. Analysis Requirements

The executor must compute all ratios in Part A, then interpret each category as follows:

**Performance (MVA, Market-to-Book, EVA)**
- MVA: Is market value above or below book equity? By how much in CHF M?
- Market-to-Book: Is the premium justified by ROIC? Compare to WACC of 9.0%.
- EVA: Is Nestlé generating economic profit above its cost of capital? EVA = after-tax operating income − (WACC × capital employed). A negative EVA means the company is destroying value despite accounting profit.
- Benchmark: EVA > 0 is the minimum bar for value creation.

**Profitability (ROA, ROC, ROE)**
- Compute all six profitability ratios (start-year and average-based).
- Primary focus: ROE (avg) and ROC (avg) — these are the most comparable across periods.
- Benchmark: WACC = 9.0%. ROC > WACC means the company earns above its cost of capital.
- Note: Nestlé's ROIC (management definition) was 14.1% in FY2024 — compare template ROC to this figure and explain any difference in definition.
- Cross-category: Link ROE to Du Pont decomposition (Section 8).

**Efficiency (Asset Turnover, Receivables, Inventory)**
- Asset turnover: How efficiently does Nestlé use its asset base to generate sales?
- Avg collection period: Compare to FMCG industry norm (~30–45 days). Nestlé's large retailer relationships typically extend payment terms.
- Days in inventory: Compare FY2025 vs FY2024 (use both start-year figures). A decrease supports Hypothesis 3 (working capital improvement).
- Operating profit margin: Compare the template operating profit margin (`currentYear_after_tax_operating_income / INC_sales` = 10,411 / 89,490 = 11.6%) to Nestlé's reported trading operating profit margin of 14.2% (FY2025) and explain the difference (template uses after-tax operating income; management uses trading operating profit before tax).

**Leverage (Debt Ratio, TIE, Debt Burden)**
- Debt ratio: At 74.0% (94,093 / 127,151), Nestlé is highly leveraged. Interpret in context of investment-grade rating and predictable cash flows.
- Times interest earned: EBIT / interest expense. A ratio below 3x warrants concern; above 5x is comfortable.
- Management's net debt/EBITDA of 2.90x (FY2024) should be cross-referenced. Note that management's definition nets cash from gross debt — the template's debt ratio uses total liabilities.

**Liquidity (Current, Quick, Cash)**
- Current ratio below 1.0x: Expected for Nestlé given negative NWC structure. Interpret in context of CHF 15.9B operating cash flow — liquidity is cash-flow driven, not balance-sheet driven.
- Quick ratio: Excludes inventories. Compare to current ratio to see inventory's role.
- Cash ratio: Most conservative measure. Nestlé's CHF 6.2B cash + investments supports this.

---

### 9. Du Pont Decomposition

Perform the full Du Pont ROE decomposition using the four components defined in Section 6:

```
ROE = Operating Profit Margin × Asset Turnover × Leverage × Debt Burden
```

Step-by-step instructions for the executor:
1. Compute each component separately and present in a table.
2. Identify the **primary driver** of ROE: which component contributes most? For Nestlé, the hypothesis is that leverage is the amplifying factor compensating for moderate asset turnover.
3. Assess **sustainability**: Is the leverage component (assets/equity = ~3.8x) at a level management can maintain? Cross-reference net debt/EBITDA 2.90x and management's stated 2–3x target range.
4. Note the **time-mismatch**: Du Pont ROE uses current-year assets for leverage but prior-year assets for turnover. State this explicitly in the analysis.
5. Compare Du Pont ROA to direct ROA — they should match (within rounding). If they diverge by more than 0.5%, flag and recheck formulas.

---

### 10. Strategic Recommendations

Produce exactly **3–5 strategic recommendations** grounded in ratio evidence. Each recommendation must:

- Name the specific ratio(s) that motivate it
- State the observed value and the concern or opportunity it reveals
- Propose a concrete, actionable response (not "improve margins" — specify how)
- Identify the primary risk or trade-off of the recommendation

Suggested framing for each recommendation:
> "Ratio X shows Y. This indicates Z. Recommendation: [specific action]. Primary risk: [trade-off]."

Candidate themes based on the data (executor may substitute with ratio-evidenced alternatives):
1. **Leverage reduction** — Net debt/EBITDA 2.90x at top of target range; FY2025 operating CF of CHF 15.9B creates opportunity to accelerate debt repayment vs. buybacks.
2. **Margin recovery** — Trading operating margin fell from 16.0% (FY2024) to 14.2% (FY2025); the "Fuel for Growth" program's CHF 2.5B cost reduction should be evaluated for progress.
3. **Asset efficiency** — Goodwill + intangibles = CHF 44.3B (35% of total assets); portfolio rationalization could improve asset turnover.
4. **Working capital discipline** — Negative NWC of (CHF 8.7B) reflects strong supplier terms; maintaining or extending this advantage protects operating cash flow.
5. **Capital allocation** — FY2025 buybacks dropped to CHF 213M from CHF 4.7B in FY2024 (program completed); evaluate optimal use of free cash flow — dividend growth vs. debt reduction vs. M&A.

---

### 11. Output Format

The Stage 5 analysis deliverable must follow this exact structure:

**Document title:** "Nestlé S.A. (NESN) — Financial Ratio Analysis FY2025"
**Author:** Ha Tuan Nghiep
**Date:** [submission date]
**Tone:** Professional analyst memo — concise, evidence-driven, no filler language
**Length:** 1,200–1,800 words (excluding ratio tables)
**Audience:** BUS-629 instructor; secondary audience is a portfolio analyst

**Required sections in order:**

1. **Executive Summary** (150–200 words) — Key findings across all ratio categories; 2–3 sentence strategic conclusion.
2. **Ratio Results** — Present all computed ratios organized by category (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont). Use a table for each category. Include the formula, computed value, and one-line interpretation for each ratio.
3. **Du Pont Decomposition** — Dedicated section. Show the decomposition table, identify the primary driver, and assess sustainability.
4. **Category Analysis** — One paragraph per ratio category (6 paragraphs total). Each paragraph: what the ratios show, what it means for Nestlé specifically, cross-reference to another category where relevant.
5. **Strategic Recommendations** — 3–5 numbered recommendations in the format specified in Section 10.
6. **Limitations** — 3–5 bullet points noting data limitations, definition differences (template vs. management KPIs), and currency effects.

**Formatting rules:**
- All monetary figures in CHF millions unless stated otherwise
- Percentages to one decimal place (e.g., 24.6%)
- Multiples to two decimal places with "x" (e.g., 2.90x)
- Named ranges in backtick code style when referenced (e.g., `INC_sales`)
- No unsupported claims — every assertion tied to a specific ratio value

---

## References

- Nestlé S.A. Consolidated Financial Statements 2025. nestle.com/investors/publications
- Nestlé S.A. Consolidated Financial Statements 2024. nestle.com/investors/publications
- Nestlé S.A. Full-Year Results 2024 Press Release (February 13, 2025). nestle.com/media/pressreleases/allpressreleases/full-year-results-2024
- Stage 1 template: `models/templates/performance-ratios-template.xlsx`
- Stage 3 populated workbook: `models/builds/2026-05-20-ha-nestle-financials.xlsx`
