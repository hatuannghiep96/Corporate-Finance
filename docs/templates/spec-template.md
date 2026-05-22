---
template: spec-parameterized
version: "2.0"
purpose: "Reusable technical specification for IFRS accounting ratio analysis — parameterized for any publicly listed company. Swap the inputs file to run for a different company. All named-range conventions, formula definitions, validation rules, and Du Pont decomposition are company-agnostic."
author: Ha Tuan Nghiep
created: 2026-05-22
based_on: docs/specs/2026-05-20-ha-nestle-spec.md
usage: "Pair with a {company}-inputs.yaml file. Replace every {{PLACEHOLDER}} with the value from the inputs file before feeding to an LLM."
courses: [BUS-629]
---

# {{COMPANY_FULL}} — Accounting Ratios Analysis: Technical Specification

**Author:** {{ANALYST_NAME}}
**Date:** {{ANALYSIS_DATE}}
**Version:** {{VERSION}}
**Company:** {{COMPANY_FULL}}, {{TICKER}}, {{EXCHANGE}}

---

## 1. Scope & Objective

This specification defines the complete ratio analysis for {{COMPANY_FULL}} ({{TICKER}}) using audited {{REPORTING_STANDARD}} financial statements for {{FY_CURRENT}} (year ended {{FYE_CURRENT}}) as the current year and {{FY_PRIOR}} (year ended {{FYE_PRIOR}}) as the prior year. All figures are in {{CURRENCY}} {{UNIT}} unless otherwise noted. Reporting standard: {{REPORTING_STANDARD}}. Reporting currency: {{CURRENCY_FULL}}.

The analytical objective is to compute the full suite of performance, profitability, efficiency, leverage, liquidity, and Du Pont ratios specified in the Stage 1 template, assess {{COMPANY_SHORT}}'s financial position and trajectory across {{FY_PRIOR}}–{{FY_CURRENT}}, and produce 3–5 actionable strategic recommendations grounded in the ratio evidence.

Intended audience: {{AUDIENCE_PRIMARY}}, with secondary audience of {{AUDIENCE_SECONDARY}}.

---

## Part A — Model Specification

### 2. Model Architecture

The workbook (`{{WORKBOOK_FILENAME}}`) contains six tabs in the following order:

| Tab | Type | Purpose |
|-----|------|---------|
| Cover | Instructions | Color key, named-range convention guide, course metadata |
| Balance Sheet | Input | {{FY_CURRENT}} (current) and {{FY_PRIOR}} (prior) balance sheet data |
| Income Statement | Input | {{FY_CURRENT}} income statement data |
| Cash Flow Statement | Input | {{FY_CURRENT}} cash flow data |
| Ratios | Input + Output | Four analyst assumptions at top; all ratios auto-compute below |
| Notes | Input | Company metadata, source URL, reporting standard, currency, FYE |

**Color coding conventions:**
- Yellow background = data inputs (hardcoded values from audited statements)
- Light blue background + blue text = analyst assumptions (share price, shares outstanding, WACC, tax rate)
- Green text = formulas and cross-sheet references — do not overwrite
- Gray background = ratio outputs — computed automatically, do not overwrite

**Input/output separation:** All hardcoded values live in Balance Sheet, Income Statement, Cash Flow, and the top section of Ratios. The Ratios tab output section is entirely formula-driven from named ranges. No manual entry in the output section.

**Units:** All monetary figures in {{CURRENCY}} {{UNIT}}. Percentages formatted to one decimal. Multiples formatted to two decimals with "x" suffix.

---

### 3. Named Range Conventions

All named ranges in the workbook follow a strict prefix convention. Any executor (human or LLM) must reference these prefixes exactly — no abbreviations, no case changes.

| Prefix | Scope | Example |
|--------|-------|---------|
| `BAL_` | Balance sheet line items | `BAL_assets_total_curr` |
| `INC_` | Income statement line items | `INC_sales`, `INC_net` |
| `CASH_` | Cash flow statement line items | `CASH_operating`, `CASH_capex` |
| `RATIO_` | Computed ratio outputs | `RATIO_roe`, `RATIO_leverage` |
| `startYear_*` | Prior-year ({{FY_PRIOR}}) balance sheet values used as period-start denominators | `startYear_equity`, `startYear_total_assets` |
| `currentYear_*` | Current-year ({{FY_CURRENT}}) derived values computed from balance sheet inputs | `currentYear_equity`, `currentYear_working_capital_net` |
| `avg_*` | Simple average of start-year and current-year values | `avg_equity`, `avg_total_assets` |

**Convention rules:**
- All names are lowercase with underscores — no camelCase, no hyphens
- Suffix `_curr` = {{FY_CURRENT}} current year balance sheet input
- Suffix `_prior` = {{FY_PRIOR}} prior year balance sheet input
- Suffix `_curr` is dropped for income statement and cash flow items (single year only)
- Never hardcode a value where a named range exists — always reference the range

---

### 4. Data Inputs

> **Executor instruction:** All values in this section come from `{{INPUTS_FILE}}`. Do not invent or estimate any value. If a line item is not available in the source financial statements, enter 0 and note the omission in the Limitations section of the analysis.

**Balance Sheet — {{FY_CURRENT}} (Current Year)**

| Named Range | Line Item | Value ({{CURRENCY}} {{UNIT}}) |
|-------------|-----------|--------------|
| `BAL_cash_marketable_securities_curr` | Cash + Short-term investments | {{BAL_cash_marketable_securities_curr}} |
| `BAL_receivables_curr` | Trade and other receivables | {{BAL_receivables_curr}} |
| `BAL_inventories_curr` | Inventories | {{BAL_inventories_curr}} |
| `BAL_assets_other_current_curr` | Other current assets | {{BAL_assets_other_current_curr}} |
| `BAL_assets_current_curr` | Total current assets | {{BAL_assets_current_curr}} |
| `BAL_ppe_curr` | Property, plant and equipment (net) | {{BAL_ppe_curr}} |
| `BAL_intangibles_curr` | Goodwill + Intangible assets | {{BAL_intangibles_curr}} |
| `BAL_assets_other_curr` | Other non-current assets | {{BAL_assets_other_curr}} |
| `BAL_assets_total_curr` | Total assets | {{BAL_assets_total_curr}} |
| `BAL_debt_current_curr` | Current financial debt | {{BAL_debt_current_curr}} |
| `BAL_payables_curr` | Trade and other payables | {{BAL_payables_curr}} |
| `BAL_liabilities_other_current_curr` | Other current liabilities | {{BAL_liabilities_other_current_curr}} |
| `BAL_liabilities_current_curr` | Total current liabilities | {{BAL_liabilities_current_curr}} |
| `BAL_debt_long_term_curr` | Non-current financial debt | {{BAL_debt_long_term_curr}} |
| `BAL_liabilities_other_long_term_curr` | Other non-current liabilities | {{BAL_liabilities_other_long_term_curr}} |
| `BAL_liabilities_total_curr` | Total liabilities | {{BAL_liabilities_total_curr}} |
| `BAL_equity_common_curr` | Share capital + Treasury shares | {{BAL_equity_common_curr}} |
| `BAL_equity_retained_curr` | Retained earnings + Reserves + NCI | {{BAL_equity_retained_curr}} |
| `BAL_equity_shareholders_curr` | Total equity | {{BAL_equity_shareholders_curr}} |

**Balance Sheet — {{FY_PRIOR}} (Prior Year)**

| Named Range | Line Item | Value ({{CURRENCY}} {{UNIT}}) |
|-------------|-----------|--------------|
| `BAL_cash_marketable_securities_prior` | Cash + Short-term investments | {{BAL_cash_marketable_securities_prior}} |
| `BAL_receivables_prior` | Trade and other receivables | {{BAL_receivables_prior}} |
| `BAL_inventories_prior` | Inventories | {{BAL_inventories_prior}} |
| `BAL_assets_other_current_prior` | Other current assets | {{BAL_assets_other_current_prior}} |
| `BAL_assets_current_prior` | Total current assets | {{BAL_assets_current_prior}} |
| `BAL_ppe_prior` | Property, plant and equipment (net) | {{BAL_ppe_prior}} |
| `BAL_intangibles_prior` | Goodwill + Intangible assets | {{BAL_intangibles_prior}} |
| `BAL_assets_other_prior` | Other non-current assets | {{BAL_assets_other_prior}} |
| `BAL_assets_total_prior` | Total assets | {{BAL_assets_total_prior}} |
| `BAL_debt_current_prior` | Current financial debt | {{BAL_debt_current_prior}} |
| `BAL_payables_prior` | Trade and other payables | {{BAL_payables_prior}} |
| `BAL_liabilities_other_current_prior` | Other current liabilities | {{BAL_liabilities_other_current_prior}} |
| `BAL_liabilities_current_prior` | Total current liabilities | {{BAL_liabilities_current_prior}} |
| `BAL_debt_long_term_prior` | Non-current financial debt | {{BAL_debt_long_term_prior}} |
| `BAL_liabilities_other_long_term_prior` | Other non-current liabilities | {{BAL_liabilities_other_long_term_prior}} |
| `BAL_liabilities_total_prior` | Total liabilities | {{BAL_liabilities_total_prior}} |
| `BAL_equity_shareholders_prior` | Total equity | {{BAL_equity_shareholders_prior}} |

**Income Statement — {{FY_CURRENT}}**

| Named Range | Line Item | Value ({{CURRENCY}} {{UNIT}}) |
|-------------|-----------|--------------|
| `INC_sales` | Net sales | {{INC_sales}} |
| `INC_cost_goods_sold` | Cost of goods sold | {{INC_cost_goods_sold}} |
| `INC_sga` | SG&A + Operating expenses | {{INC_sga}} |
| `INC_depreciation` | Depreciation and amortization | {{INC_depreciation}} |
| `INC_ebit` | EBIT (computed: `INC_sales − INC_cost_goods_sold − INC_sga − INC_depreciation`) | {{INC_ebit}} |
| `INC_other_income` | Other income (net, incl. associates) | {{INC_other_income}} |
| `INC_interest_expense` | Financial expense | {{INC_interest_expense}} |
| `INC_taxable_income` | Taxable income (computed: `INC_ebit + INC_other_income − INC_interest_expense`) | {{INC_taxable_income}} |
| `INC_taxes` | Taxes | {{INC_taxes}} |
| `INC_net` | Net income (to parent shareholders) | {{INC_net}} |
| `INC_dividends` | Dividends paid to parent shareholders | {{INC_dividends}} |

**Cash Flow Statement — {{FY_CURRENT}}**

| Named Range | Line Item | Value ({{CURRENCY}} {{UNIT}}) |
|-------------|-----------|--------------|
| `CASH_operating` | Operating cash flow | {{CASH_operating}} |
| `CASH_capex` | Capital expenditure | {{CASH_capex}} |
| `CASH_investing` | Investing cash flow | {{CASH_investing}} |
| `CASH_financing` | Financing cash flow | {{CASH_financing}} |
| `CASH_net` | Net change in cash | {{CASH_net}} |
| `CASH_depreciation` | Depreciation (from CF reconciliation) | {{CASH_depreciation}} |

**Analyst Assumptions**

| Named Range | Item | Value |
|-------------|------|-------|
| `yearCurrent` | Current fiscal year | {{yearCurrent}} |
| `share_price` | Closing share price at {{FYE_CURRENT}} ({{CURRENCY}}) | {{share_price}} |
| `shares_outstanding` | Diluted weighted avg shares ({{UNIT}}) | {{shares_outstanding}} |
| `cost_capital` | Cost of capital (WACC) | {{cost_capital}} |
| `tax_rate` | Effective tax rate {{FY_CURRENT}} | {{tax_rate}} |

---

### 5. Derived Inputs

All derived inputs are computed in the Ratios tab from named ranges. The executor must not hardcode these values.

| Named Range | Formula | 
|-------------|---------|
| `market_capitalization` | `share_price × shares_outstanding` |
| `startYear_equity` | `BAL_equity_shareholders_prior` |
| `startYear_inventory` | `BAL_inventories_prior` |
| `startYear_receivables` | `BAL_receivables_prior` |
| `startYear_total_assets` | `BAL_assets_total_prior` |
| `startYear_total_capitalization` | `BAL_debt_long_term_prior + BAL_equity_shareholders_prior` |
| `currentYear_after_tax_operating_income` | `INC_net + (1 − tax_rate) × INC_interest_expense` |
| `currentYear_daily_sales_average` | `INC_sales / 365` |
| `currentYear_equity` | `BAL_equity_shareholders_curr` |
| `currentYear_assets_current` | `BAL_assets_current_curr` |
| `currentYear_liabilities_current` | `BAL_liabilities_current_curr` |
| `currentYear_working_capital_net` | `BAL_assets_current_curr − BAL_liabilities_current_curr` |
| `currentYear_debt_long_term` | `BAL_debt_long_term_curr` |
| `currentYear_assets_total` | `BAL_assets_total_curr` |
| `currentYear_total_capitalization` | `currentYear_debt_long_term + currentYear_equity` |
| `currentYear_liabilities_total` | `BAL_liabilities_total_curr` |
| `currentYear_cost_goods_sold_daily` | `INC_cost_goods_sold / 365` |
| `currentYear_cash_marketable_securities` | `BAL_cash_marketable_securities_curr` |
| `avg_equity` | `AVERAGE(startYear_equity, currentYear_equity)` |
| `avg_total_assets` | `AVERAGE(startYear_total_assets, currentYear_assets_total)` |
| `avg_total_capitalization` | `AVERAGE(startYear_total_capitalization, currentYear_total_capitalization)` |

---

### 6. Ratio Definitions & Formulas

> **Precision instruction:** Compute each ratio component to at least four decimal places before multiplying or dividing. Round only the final output to one decimal place (percentages) or two decimal places (multiples). Rounding intermediate components before the final step will compound error — this is especially critical for the Du Pont ROE four-step multiplication.

**Performance**

| Ratio | Formula (named-range notation) | Unit |
|-------|-------------------------------|------|
| Market Value Added (MVA) | `market_capitalization − currentYear_equity` | {{CURRENCY}} {{UNIT}} |
| Market-to-Book | `market_capitalization / currentYear_equity` | x |
| Economic Value Added (EVA) | `currentYear_after_tax_operating_income − (cost_capital × startYear_total_capitalization)` | {{CURRENCY}} {{UNIT}} |

> **EVA capital base note:** EVA uses `startYear_total_capitalization` as the capital base — not the average or current-year figure. Convention: capital is measured at the start of the period over which returns are generated.

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

1. **Balance Sheet balance ({{FY_CURRENT}}):** `BAL_assets_total_curr` = `BAL_liabilities_total_curr + BAL_equity_shareholders_curr` → {{BAL_assets_total_curr}} = {{BAL_liabilities_total_curr}} + {{BAL_equity_shareholders_curr}} ✓
2. **Balance Sheet balance ({{FY_PRIOR}}):** `BAL_assets_total_prior` = `BAL_liabilities_total_prior + BAL_equity_shareholders_prior` → {{BAL_assets_total_prior}} = {{BAL_liabilities_total_prior}} + {{BAL_equity_shareholders_prior}} ✓
3. **Du Pont ROA check:** Du Pont ROA must equal direct ROA within 0.5%. If they diverge beyond this, recheck `RATIO_operating_profit_margin` and `RATIO_asset_turnover` formulas.
4. **Du Pont ROE time-mismatch note:** Du Pont ROE will not exactly equal direct ROE because leverage uses current-year assets while asset turnover uses prior-year assets. This time-mismatch is intentional — note it in the analysis.
5. **Zero formula errors:** No #REF!, #DIV/0!, or #NAME? anywhere in the Ratios tab.
6. **Structural notes:** {{STRUCTURAL_NOTES}}

---

## Part B — Analysis Specification

### 8. Analysis Requirements

The executor must compute all ratios in Part A, then interpret each category as follows:

**Performance (MVA, Market-to-Book, EVA)**
- MVA: Is market value above or below book equity? By how much in {{CURRENCY}} {{UNIT}}?
- Market-to-Book: Is the premium justified by ROIC? Compare to WACC of {{cost_capital}}.
- EVA: Is {{COMPANY_SHORT}} generating economic profit above its cost of capital? A negative EVA means the company is destroying value despite accounting profit.
- Benchmark: EVA > 0 is the minimum bar for value creation.

**Profitability (ROA, ROC, ROE)**
- Compute all six profitability ratios (start-year and average-based).
- Primary focus: ROE (avg) and ROC (avg) — these are the most comparable across periods.
- Benchmark: WACC = {{cost_capital}}. ROC > WACC means the company earns above its cost of capital.
- Management KPI cross-reference: {{MANAGEMENT_ROIC_NOTE}}
- Cross-category: Link ROE to Du Pont decomposition.

**Efficiency (Asset Turnover, Receivables, Inventory)**
- Asset turnover: How efficiently does {{COMPANY_SHORT}} use its asset base to generate sales?
- Avg collection period: Compare to industry norm of {{INDUSTRY_COLLECTION_NORM}}. {{COLLECTION_PERIOD_CONTEXT}}
- Days in inventory: Compare {{FY_CURRENT}} vs {{FY_PRIOR}} (use both start-year figures).
- Operating profit margin: Compare template figure to management's reported margin of {{MANAGEMENT_OPERATING_MARGIN}} and explain the definition difference.

**Leverage (Debt Ratio, TIE, Debt Burden)**
- Debt ratio: Interpret in context of {{COMPANY_SHORT}}'s credit profile and cash flow predictability.
- Times interest earned: A ratio below 3x warrants concern; above 5x is comfortable.
- Management leverage KPI cross-reference: {{MANAGEMENT_LEVERAGE_NOTE}}

**Liquidity (Current, Quick, Cash)**
- Current ratio: Interpret in context of {{COMPANY_SHORT}}'s NWC structure and operating cash flow.
- Quick ratio: Excludes inventories. Compare to current ratio to see inventory's role.
- Cash ratio: Most conservative measure.
- {{LIQUIDITY_CONTEXT}}

---

### 9. Du Pont Decomposition

Perform the full Du Pont ROE decomposition using the four components defined in Section 6:

```
ROE = Operating Profit Margin × Asset Turnover × Leverage × Debt Burden
```

Step-by-step instructions:
1. Compute each component to four decimal places before multiplying.
2. Identify the primary driver of ROE.
3. Assess sustainability of the leverage component. {{LEVERAGE_SUSTAINABILITY_NOTE}}
4. Note the time-mismatch: Du Pont ROE uses current-year assets for leverage but prior-year assets for turnover. State this explicitly.
5. Compare Du Pont ROA to direct ROA — if they diverge by more than 0.5%, flag and recheck formulas.

---

### 10. Strategic Recommendations

Produce exactly **3–5 strategic recommendations** grounded in ratio evidence. Each recommendation must:

- Open with a `### Recommendation N — [title]` heading
- Name the specific ratio(s) that motivate it (labeled **Ratio anchor:**)
- State a concrete, quantitative action with a specific target (labeled **Action:**) — e.g., a specific {{CURRENCY}} amount, ratio level, percentage, or timeline. Directional statements without a numeric anchor do not satisfy this requirement.
- Identify the primary risk or trade-off (labeled **Risk:**)

Candidate themes based on the data:
{{RECOMMENDATION_THEMES}}

---

### 11. Output Format

**Document title:** "{{COMPANY_FULL}} ({{TICKER}}) — Financial Ratio Analysis {{FY_CURRENT}}"
**Author:** {{ANALYST_NAME}}
**Date:** [submission date]
**Tone:** Professional analyst memo — concise, evidence-driven, no filler language
**Length:** 1,200–1,800 words (excluding ratio tables)

**Required sections in order:**
1. **Company & Data Summary** — company, reporting standard, fiscal years, data sources, analyst assumptions
2. **Executive Summary** (150–200 words)
3. **Ratio Results** — one table per category
4. **Du Pont Decomposition** — dedicated section with decomposition table
5. **Category Analysis** — one paragraph per ratio category (6 paragraphs)
6. **Strategic Recommendations** — 3–5 using ### Recommendation N format
7. **LLM Evaluation & Annotations** — what the LLM got right, where it deviated, spec gaps vs LLM limitations
8. **Executive Justification** — analyst's own strategic thesis, not the LLM's
9. **Limitations** — 3–5 bullet points

**Formatting rules:**
- All monetary figures in {{CURRENCY}} {{UNIT}} unless stated otherwise
- Percentages to one decimal place
- Multiples to two decimal places with "x"
- Named ranges in backtick code style
- No unsupported claims — every assertion tied to a specific ratio value

---

## How to use this template

To run this analysis for a different company:

1. Create a new inputs file: `YYYY-MM-DD-{lastname}-{company-slug}-inputs.yaml`
2. Fill every field in the inputs file from the company's audited financial statements
3. Replace every `{{PLACEHOLDER}}` in this template with the corresponding value from the inputs file
4. Feed the completed spec to your LLM of choice with no additional context
5. Save the unedited LLM response as `llm-raw.md`
6. Verify ≥5 ratios manually and produce the final analysis

The named-range conventions (Section 3), formula definitions (Section 6), validation rules (Section 7), and Du Pont decomposition (Section 9) require no changes between companies. Only the inputs file and the company-specific context fields change.

---

## 12. Sensitivity Specification

> **Purpose:** Point-estimate specs produce point-estimate analyses. This section extends the analysis to quantify uncertainty in the two analyst assumptions that most affect EVA and profitability ratios. The executor must produce a sensitivity appendix alongside the main ratio results.

### Inputs to stress-test

| Input | Named range | Point estimate | Range | Distribution |
|---|---|---|---|---|
| Cost of capital (WACC) | `cost_capital` | {{cost_capital}} | 7.0% – 11.0% | Triangular, mode = {{cost_capital}} |
| Effective tax rate | `tax_rate` | {{tax_rate}} | 22.0% – 28.0% | Uniform |

### Required outputs

**Output 1 — EVA sensitivity table:**
Recompute EVA at five WACC points holding tax rate at point estimate:

| WACC | EVA ({{CURRENCY}} {{UNIT}}) | vs base case |
|---|---|---|
| 7.0% | [compute] | [delta] |
| 8.0% | [compute] | [delta] |
| {{cost_capital}} (base) | [compute] | — |
| 10.0% | [compute] | [delta] |
| 11.0% | [compute] | [delta] |

**Output 2 — EVA break-even WACC:**
Find the WACC at which EVA = 0. Formula:
```
EVA = 0  when  cost_capital = currentYear_after_tax_operating_income / startYear_total_capitalization
```
State this value explicitly. If EVA is positive at the base case WACC, the break-even WACC is the maximum the company can sustain before destroying value.

**Output 3 — Monte Carlo simulation (5,000 trials):**
- Draw `cost_capital` from triangular distribution (low=7%, mode={{cost_capital}}, high=11%)
- Draw `tax_rate` from uniform distribution (low=22%, high=28%)
- Recompute `currentYear_after_tax_operating_income` and EVA each trial
- Report: EVA at 10th, 50th, 90th percentile
- Report: probability that EVA > 0

**Output 4 — Tornado chart (text format):**
Show which input drives more EVA variance:
```
EVA sensitivity (holding other input at base case)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cost_capital  [━━━━━━━━━━━━━━━━━━━━━━━] ±{{range}}M
tax_rate      [━━━━━━━━━━━] ±{{range}}M
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Output 5 — One narrative paragraph:**
State which input dominates EVA uncertainty, what the break-even WACC implies for the company's value-creation thesis, and whether the 10th percentile EVA is still positive (i.e., whether value creation is robust to pessimistic assumptions).

### Conformance note
The ratio harness (`analysis/ratio_harness.py`) verifies the base-case EVA computation. The Monte Carlo extension in the harness independently validates the break-even WACC and percentile outputs.
