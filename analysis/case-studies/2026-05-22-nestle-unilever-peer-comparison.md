---
purpose: "FMCG peer comparison — Nestlé S.A. vs Unilever PLC FY2025, computed by peer_comparison.py from audited IFRS inputs"
author: Ha Tuan Nghiep
date: 2026-05-22
source_script: analysis/peer_comparison.py
inputs:
  - docs/specs/2026-05-20-ha-nestle-inputs.yaml
  - docs/specs/2026-05-22-ha-unilever-inputs.yaml
---

================================================================
  FMCG Peer Comparison — Direction 4 Validation
  Ha Tuan Nghiep — BUS-629 Corporate Finance
  github.com/hatuannghiep96/Corporate-Finance
================================================================

  Loading inputs files...
  ✓ Nestlé:   Nestlé S.A. (FY2025)
  ✓ Unilever: Unilever PLC (FY2025)

  Computing ratios...
  ✓ All ratios computed for both companies

================================================================
  FMCG PEER COMPARISON — FY2025
  Nestlé S.A. (NESN)                Unilever PLC (ULVR)
  IFRS · CHF millions               IFRS · EUR millions
================================================================

  SCALE
  ────────────────────────────────────────────────────────────────
  Revenue                             CHF 89,490M     EUR 50,503M
  Total assets                       CHF 127,151M     EUR 70,471M
  Market capitalization              CHF 185,338M    EUR 137,456M
  Net income (to parent)               CHF 9,033M      EUR 5,682M
  Net working capital                 CHF -8,725M     EUR -4,596M

  PERFORMANCE
  ────────────────────────────────────────────────────────────────
  MVA                                CHF 152,280M    EUR 121,926M
  Market-to-Book                            5.61x           8.85x
  EVA                                  CHF 2,455M      EUR 2,358M
  EVA as % of capital                        2.8%            5.2%
  Break-even WACC                           11.8%           14.2%

  PROFITABILITY
  ────────────────────────────────────────────────────────────────
  ROA (start-year assets)                    7.5%            8.0%
  ROC (start-year cap)                      11.8%           14.2%
  ROE (start-year equity)                   24.6%           28.4%
  ROA (avg assets)                           7.8%            8.5%
  ROC (avg cap)                             12.4%           14.9%
  ROE (avg equity)                          25.9%           32.0%
  Gross margin                              45.6%           46.9%
  Operating profit margin                   11.6%           12.7%
  Net profit margin                         10.1%           11.3%

  EFFICIENCY
  ────────────────────────────────────────────────────────────────
  Asset turnover                            0.64x           0.63x
  Receivables turnover                      7.95x           8.40x
  Avg collection period                 45.9 days       43.4 days
  Inventory turnover                        3.67x           5.18x
  Days in inventory                     99.4 days       70.5 days
  NWC as % of revenue                       -9.7%           -9.1%

  LEVERAGE
  ────────────────────────────────────────────────────────────────
  Debt ratio                                74.0%           75.0%
  Times interest earned                     5.67x           8.83x
  Debt burden                               0.77x           0.65x

  LIQUIDITY
  ────────────────────────────────────────────────────────────────
  Current ratio                             0.79x           0.79x
  Quick ratio                               0.47x           0.60x
  Cash ratio                                0.15x           0.23x

  DU PONT DECOMPOSITION
  ────────────────────────────────────────────────────────────────
  Operating profit margin                   11.6%           12.7%
  Asset turnover                            0.64x           0.63x
  Leverage (assets/equity)                  3.85x           4.54x
  Debt burden                               0.77x           0.65x
  Du Pont ROA                                7.5%            8.0%
  Du Pont ROE                               22.2%           23.9%

================================================================

================================================================
  ANALYST COMMENTARY — KEY DIVERGENCES
================================================================

  1. VALUE CREATION SPREAD (ROC avg - WACC of 9.0%)
     Nestlé:   12.4% - 9.0% = +3.4bps above WACC
     Unilever: 14.9% - 9.0% = +5.9bps vs WACC
     → Unilever has the wider value-creation spread

  2. ECONOMIC VALUE ADDED
     Nestlé:   CHF 2,455M (2.8% of capital base)
     Unilever: EUR 2,358M (5.2% of capital base)
     → Note: currencies differ; EVA % of capital is the comparable metric

  3. WACC HEADROOM (break-even WACC where EVA = 0)
     Nestlé:   11.78% — headroom: 3bps
     Unilever: 14.23% — headroom: 5bps
     → Unilever is more resilient to rising cost of capital

  4. NEGATIVE NWC AS % OF REVENUE (supplier financing advantage)
     Nestlé:   -8,725 CHF M (-9.7% of revenue)
     Unilever: -4,596 EUR M (-9.1% of revenue)
     → Nestlé extracts more supplier financing relative to revenue

  5. DU PONT PRIMARY DRIVER
     Nestlé:   leverage 3.85x | margin 11.6% | turnover 0.64x
     Unilever: leverage 4.54x | margin 12.7% | turnover 0.63x
     → Nestlé ROE primarily driven by: leverage
     → Unilever ROE primarily driven by: leverage

  6. INVENTORY EFFICIENCY
     Nestlé:   99.4 days (3.67x turnover)
     Unilever: 70.5 days (5.18x turnover)
     → Unilever holds fewer days of inventory
     → Nestlé's replenishment system (15-21 day safety stock, 3-stage
        commitment, ERP integration) visible in this comparison

================================================================
  TEMPLATE VALIDATION RESULT
================================================================
  ✓ spec-template.md ran successfully for both companies
  ✓ Only the inputs yaml changed between runs
  ✓ All named-range conventions applied consistently
  ✓ Direction 4 objective achieved: template is company-agnostic
================================================================

