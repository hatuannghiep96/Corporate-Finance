#!/usr/bin/env python3
"""
ratio_harness.py — Automated conformance checker for ratio analysis
====================================================================
Direction 1: reads the Stage 3 workbook, recomputes all ratios from
named ranges per the spec, extracts LLM-stated values from the final
analysis markdown, and reports PASS/FAIL per ratio.

Usage (run from repo root):
    python analysis/ratio_harness.py

Requirements:
    pip install openpyxl --break-system-packages

Author: Ha Tuan Nghiep
Date:   2026-05-22
Repo:   https://github.com/hatuannghiep96/Corporate-Finance
"""

import re
import sys
from pathlib import Path

try:
    import openpyxl
except ImportError:
    print("ERROR: openpyxl not installed.")
    print("Run:   pip install openpyxl --break-system-packages")
    sys.exit(1)

# ── CONFIGURATION ─────────────────────────────────────────────────────────────

REPO_ROOT     = Path(__file__).parent.parent          # two levels up from analysis/
WORKBOOK_PATH = REPO_ROOT / "models" / "builds" / "2026-05-20-ha-nestle-financials.xlsx"
ANALYSIS_PATH = REPO_ROOT / "deliverables" / "2026-05-20-ha-nestle-final-analysis.md"

# Tolerances for PASS/FAIL
PCT_TOLERANCE  = 0.15   # percentage points
MULT_TOLERANCE = 0.02   # multiples
DAYS_TOLERANCE = 0.50   # days
CHF_TOLERANCE  = 50     # CHF millions

# Analyst assumptions (from inputs yaml — not stored in workbook cells)
SHARE_PRICE        = 72.06
SHARES_OUTSTANDING = 2572.0   # millions
COST_CAPITAL       = 0.09
TAX_RATE           = 0.246

# ── STEP 1: LOAD WORKBOOK ─────────────────────────────────────────────────────

def load_workbook_data(path):
    """Read all input values from the Stage 3 workbook."""
    print(f"\n{'='*62}")
    print("STEP 1 — Loading Stage 3 workbook")
    print(f"{'='*62}")

    if not path.exists():
        print(f"ERROR: Workbook not found at:\n  {path}")
        print("\nMake sure you are running this script from the repo root,")
        print("or that models/builds/2026-05-20-ha-nestle-financials.xlsx exists.")
        sys.exit(1)

    wb = openpyxl.load_workbook(path, data_only=True)
    print(f"✓ Loaded: {path.name}")
    print(f"  Sheets: {wb.sheetnames}")

    d = {}
    bs    = wb["Balance Sheet"]
    istat = wb["Income Statement"]
    cf    = wb["Cash Flow Statement"]

    # ── Balance Sheet ──
    # Template layout confirmed:
    # Row 7  = Cash / Debt current
    # Row 8  = Receivables / Payables
    # Row 9  = Inventories / Other CL
    # Row 10 = Other CA / Total CL
    # Row 11 = Total CA
    # Row 12 = Long-term debt (liabilities side)
    # Row 14 = PP&E
    # Row 16 = Net tangible fixed assets
    # Row 19 = Intangibles / Retained earnings
    # Row 20 = Other assets / Total equity
    # Row 23 = Total assets / Total L+E
    # Columns: C = FY current, D = FY prior, G = current liabilities/equity, H = prior

    d["BAL_cash_marketable_securities_curr"]  = bs["C7"].value  or 0
    d["BAL_receivables_curr"]                 = bs["C8"].value  or 0
    d["BAL_inventories_curr"]                 = bs["C9"].value  or 0
    d["BAL_assets_other_current_curr"]        = bs["C10"].value or 0
    d["BAL_assets_current_curr"]              = bs["C11"].value or 0
    d["BAL_ppe_curr"]                         = bs["C14"].value or 0
    d["BAL_intangibles_curr"]                 = bs["C19"].value or 0
    d["BAL_assets_other_curr"]                = bs["C20"].value or 0
    d["BAL_assets_total_curr"]                = bs["C23"].value or 0

    d["BAL_debt_current_curr"]                = bs["G7"].value  or 0
    d["BAL_payables_curr"]                    = bs["G8"].value  or 0
    d["BAL_liabilities_other_current_curr"]   = bs["G9"].value  or 0
    d["BAL_liabilities_current_curr"]         = bs["G10"].value or 0
    d["BAL_debt_long_term_curr"]              = bs["G12"].value or 0
    d["BAL_liabilities_total_curr"]           = bs["G15"].value or 0
    d["BAL_equity_shareholders_curr"]         = bs["G20"].value or 0

    d["BAL_cash_marketable_securities_prior"] = bs["D7"].value  or 0
    d["BAL_receivables_prior"]                = bs["D8"].value  or 0
    d["BAL_inventories_prior"]                = bs["D9"].value  or 0
    d["BAL_assets_current_prior"]             = bs["D11"].value or 0
    d["BAL_assets_total_prior"]               = bs["D23"].value or 0
    d["BAL_debt_long_term_prior"]             = bs["H12"].value or 0
    d["BAL_liabilities_total_prior"]          = bs["H15"].value or 0
    d["BAL_equity_shareholders_prior"]        = bs["H20"].value or 0

    # ── Income Statement ──
    # Row 6=Sales, 7=COGS, 8=SGA, 9=D&A, 10=EBIT(formula),
    # 11=Other income, 12=Interest, 13=Taxable(formula),
    # 14=Taxes, 15=Net income(formula), 18=Dividends
    d["INC_sales"]            = istat["C6"].value  or 0
    d["INC_cost_goods_sold"]  = istat["C7"].value  or 0
    d["INC_sga"]              = istat["C8"].value  or 0
    d["INC_depreciation"]     = istat["C9"].value  or 0
    d["INC_other_income"]     = istat["C11"].value or 0
    d["INC_interest_expense"] = istat["C12"].value or 0
    d["INC_taxes"]            = istat["C14"].value or 0
    d["INC_net"]              = istat["C15"].value or 0
    d["INC_dividends"]        = istat["C18"].value or 0

    # Computed IS items (recompute rather than trust formula cells)
    d["INC_ebit"]         = (d["INC_sales"] - d["INC_cost_goods_sold"]
                             - d["INC_sga"] - d["INC_depreciation"])
    d["INC_taxable_income"] = (d["INC_ebit"] + d["INC_other_income"]
                               - d["INC_interest_expense"])

    # ── Cash Flow ──
    # Row 16=Operating CF, 19=Capex, 22=Investing, 30=Financing, 32=Net change
    d["CASH_operating"]    = cf["C16"].value or 0
    d["CASH_capex"]        = cf["C19"].value or 0
    d["CASH_investing"]    = cf["C22"].value or 0
    d["CASH_financing"]    = cf["C30"].value or 0
    d["CASH_net"]          = cf["C32"].value or 0
    d["CASH_depreciation"] = cf["C8"].value  or 0

    print(f"\n  Key values read from workbook:")
    print(f"    INC_sales:                    {d['INC_sales']:>10,.0f}  CHF M")
    print(f"    INC_net:                      {d['INC_net']:>10,.0f}  CHF M")
    print(f"    BAL_assets_total_curr:        {d['BAL_assets_total_curr']:>10,.0f}  CHF M")
    print(f"    BAL_assets_total_prior:       {d['BAL_assets_total_prior']:>10,.0f}  CHF M")
    print(f"    BAL_equity_shareholders_curr: {d['BAL_equity_shareholders_curr']:>10,.0f}  CHF M")
    print(f"    CASH_operating:               {d['CASH_operating']:>10,.0f}  CHF M")

    # Sanity check
    if d["INC_sales"] == 0:
        print("\n  ⚠ WARNING: INC_sales = 0. The workbook may be the empty template,")
        print("    not the populated Stage 3 file. Verify the path and re-run.")

    return d

# ── STEP 2: RECOMPUTE ALL RATIOS ──────────────────────────────────────────────

def compute_ratios(d):
    """Recompute every ratio from spec Section 6 formulas."""
    print(f"\n{'='*62}")
    print("STEP 2 — Recomputing ratios from spec formulas")
    print(f"{'='*62}")

    r = {}

    # Derived inputs
    r["market_cap"]              = SHARE_PRICE * SHARES_OUTSTANDING
    r["startYear_equity"]        = d["BAL_equity_shareholders_prior"]
    r["startYear_inventory"]     = d["BAL_inventories_prior"]
    r["startYear_receivables"]   = d["BAL_receivables_prior"]
    r["startYear_assets"]        = d["BAL_assets_total_prior"]
    r["startYear_cap"]           = d["BAL_debt_long_term_prior"] + d["BAL_equity_shareholders_prior"]
    r["atoi"]                    = d["INC_net"] + (1 - TAX_RATE) * d["INC_interest_expense"]
    r["daily_sales"]             = d["INC_sales"] / 365
    r["daily_cogs"]              = d["INC_cost_goods_sold"] / 365
    r["curr_equity"]             = d["BAL_equity_shareholders_curr"]
    r["curr_assets_current"]     = d["BAL_assets_current_curr"]
    r["curr_liab_current"]       = d["BAL_liabilities_current_curr"]
    r["curr_NWC"]                = d["BAL_assets_current_curr"] - d["BAL_liabilities_current_curr"]
    r["curr_lt_debt"]            = d["BAL_debt_long_term_curr"]
    r["curr_assets_total"]       = d["BAL_assets_total_curr"]
    r["curr_cap"]                = r["curr_lt_debt"] + r["curr_equity"]
    r["curr_liab_total"]         = d["BAL_liabilities_total_curr"]
    r["curr_cash"]               = d["BAL_cash_marketable_securities_curr"]
    r["avg_equity"]              = (r["startYear_equity"] + r["curr_equity"]) / 2
    r["avg_assets"]              = (r["startYear_assets"] + r["curr_assets_total"]) / 2
    r["avg_cap"]                 = (r["startYear_cap"] + r["curr_cap"]) / 2

    # Performance
    r["MVA"]            = r["market_cap"] - r["curr_equity"]
    r["Market_to_Book"] = r["market_cap"] / r["curr_equity"] if r["curr_equity"] else 0
    r["EVA"]            = r["atoi"] - (COST_CAPITAL * r["startYear_cap"])

    # Profitability
    r["ROA_start"] = r["atoi"] / r["startYear_assets"] * 100 if r["startYear_assets"] else 0
    r["ROC_start"] = r["atoi"] / r["startYear_cap"] * 100    if r["startYear_cap"] else 0
    r["ROE_start"] = d["INC_net"] / r["startYear_equity"] * 100 if r["startYear_equity"] else 0
    r["ROA_avg"]   = r["atoi"] / r["avg_assets"] * 100       if r["avg_assets"] else 0
    r["ROC_avg"]   = r["atoi"] / r["avg_cap"] * 100          if r["avg_cap"] else 0
    r["ROE_avg"]   = d["INC_net"] / r["avg_equity"] * 100    if r["avg_equity"] else 0

    # Efficiency
    r["Asset_Turnover"]   = d["INC_sales"] / r["startYear_assets"]    if r["startYear_assets"] else 0
    r["Recv_Turnover"]    = d["INC_sales"] / r["startYear_receivables"] if r["startYear_receivables"] else 0
    r["Avg_Coll_Period"]  = r["startYear_receivables"] / r["daily_sales"] if r["daily_sales"] else 0
    r["Inv_Turnover"]     = d["INC_cost_goods_sold"] / r["startYear_inventory"] if r["startYear_inventory"] else 0
    r["Days_Inventory"]   = r["startYear_inventory"] / r["daily_cogs"] if r["daily_cogs"] else 0
    r["Profit_Margin"]    = d["INC_net"] / d["INC_sales"] * 100       if d["INC_sales"] else 0
    r["Op_Profit_Margin"] = r["atoi"] / d["INC_sales"] * 100          if d["INC_sales"] else 0

    # Leverage
    r["Debt_Ratio"]   = r["curr_liab_total"] / r["curr_assets_total"] * 100 if r["curr_assets_total"] else 0
    r["TIE"]          = d["INC_ebit"] / d["INC_interest_expense"]     if d["INC_interest_expense"] else 0
    r["Debt_Burden"]  = d["INC_net"] / d["INC_taxable_income"]        if d["INC_taxable_income"] else 0

    # Liquidity
    r["Current_Ratio"] = r["curr_assets_current"] / r["curr_liab_current"] if r["curr_liab_current"] else 0
    r["Quick_Ratio"]   = (r["curr_assets_current"] - d["BAL_inventories_curr"]) / r["curr_liab_current"] if r["curr_liab_current"] else 0
    r["Cash_Ratio"]    = r["curr_cash"] / r["curr_liab_current"]       if r["curr_liab_current"] else 0

    # Du Pont — FULL PRECISION throughout (Gap 1 fix from retrospective)
    dp_m = r["atoi"] / d["INC_sales"]          if d["INC_sales"] else 0
    dp_t = d["INC_sales"] / r["startYear_assets"] if r["startYear_assets"] else 0
    dp_l = r["curr_assets_total"] / r["curr_equity"] if r["curr_equity"] else 0
    dp_b = d["INC_net"] / d["INC_taxable_income"] if d["INC_taxable_income"] else 0

    r["DP_margin"]   = dp_m
    r["DP_turnover"] = dp_t
    r["DP_leverage"] = dp_l
    r["DP_burden"]   = dp_b
    r["DuPont_ROA"]  = dp_m * dp_t * 100
    r["DuPont_ROE"]  = dp_m * dp_t * dp_l * dp_b * 100

    print(f"  ✓ All ratios computed")
    print(f"  Key diagnostics:")
    print(f"    NWC:             {r['curr_NWC']:>10,.0f}  CHF M  "
          f"{'✓ negative (expected for Nestlé)' if r['curr_NWC'] < 0 else '⚠ positive — check BS'}")
    print(f"    EVA:             {r['EVA']:>10,.0f}  CHF M  "
          f"{'✓ positive (value-creating)' if r['EVA'] > 0 else '⚠ negative (value-destroying)'}")
    print(f"    Du Pont ROE:     {r['DuPont_ROE']:>10.4f}%  (full precision)")
    print(f"    ROC (avg):       {r['ROC_avg']:>10.2f}%")

    return r

# ── STEP 3: EXTRACT LLM VALUES FROM MARKDOWN ──────────────────────────────────

def extract_llm_values(path):
    """Extract ratio values from final analysis markdown using regex."""
    print(f"\n{'='*62}")
    print("STEP 3 — Extracting LLM-stated values from final analysis")
    print(f"{'='*62}")

    if not path.exists():
        print(f"ERROR: Analysis file not found at:\n  {path}")
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    llm  = {}

    # Each pattern searches the markdown ratio tables
    patterns = {
        "MVA":            r"Market Value Added[^\n]*\|\s*CHF\s*([\d,]+)M",
        "Market_to_Book": r"Market-to-Book[^\n]*\|\s*([\d.]+)x\s*\|",
        "EVA":            r"Economic Value Added[^\n]*\|\s*CHF\s*([\d,]+)M",
        "ROA_start":      r"ROA \(start-year assets\)[^\n]*\|\s*([\d.]+)%",
        "ROC_start":      r"ROC \(start-year cap\)[^\n]*\|\s*([\d.]+)%",
        "ROE_start":      r"ROE \(start-year equity\)[^\n]*\|\s*([\d.]+)%",
        "ROA_avg":        r"ROA \(avg assets\)[^\n]*\|\s*([\d.]+)%",
        "ROC_avg":        r"ROC \(avg cap\)[^\n]*\|\s*([\d.]+)%",
        "ROE_avg":        r"ROE \(avg equity\)[^\n]*\|\s*([\d.]+)%",
        "Asset_Turnover": r"Asset Turnover[^\n]*\|\s*([\d.]+)x\s*\|",
        "Avg_Coll_Period":r"Avg Collection Period[^\n]*\|\s*([\d.]+) days",
        "Inv_Turnover":   r"Inventory Turnover[^\n]*\|\s*([\d.]+)x\s*\|",
        "Days_Inventory": r"Days in Inventory[^\n]*\|\s*([\d.]+) days",
        "Profit_Margin":  r"Profit Margin[^\n]*\|\s*([\d.]+)%",
        "Op_Profit_Margin":r"Operating Profit Margin[^\n]*\|\s*([\d.]+)%",
        "Debt_Ratio":     r"Debt Ratio[^\n]*\|\s*([\d.]+)%",
        "TIE":            r"Times Interest Earned[^\n]*\|\s*([\d.]+)x",
        "Debt_Burden":    r"Debt Burden[^\n]*\|\s*([\d.]+)x",
        "Current_Ratio":  r"Current Ratio[^\n]*\|\s*([\d.]+)x",
        "Quick_Ratio":    r"Quick Ratio[^\n]*\|\s*([\d.]+)x",
        "Cash_Ratio":     r"Cash Ratio[^\n]*\|\s*([\d.]+)x",
        "DuPont_ROA":     r"\*\*Du Pont ROA\*\*[^\n]*\|\s*\*\*([\d.]+)%\*\*",
        "DuPont_ROE":     r"\*\*Du Pont ROE\*\*[^\n]*\|\s*\*\*([\d.]+)%\*\*",
    }

    for name, pattern in patterns.items():
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            llm[name] = float(m.group(1).replace(",", ""))
        else:
            llm[name] = None

    found   = sum(1 for v in llm.values() if v is not None)
    missing = sum(1 for v in llm.values() if v is None)
    print(f"  ✓ Extracted {found}/{len(patterns)} ratio values")
    if missing:
        missing_names = [k for k, v in llm.items() if v is None]
        print(f"  ⚠ Not found ({missing}): {', '.join(missing_names)}")

    return llm

# ── STEP 4: COMPARE AND REPORT ────────────────────────────────────────────────

def compare_and_report(r, llm):
    """Print the full PASS/FAIL conformance report."""
    print(f"\n{'='*62}")
    print("STEP 4 — Conformance report")
    print(f"{'='*62}")

    checks = [
        # (display, computed_key, unit, tolerance, suffix)
        ("MVA (CHF M)",          "MVA",            "CHF",  CHF_TOLERANCE,  "CHF M"),
        ("Market-to-Book",       "Market_to_Book", "mult", MULT_TOLERANCE, "x"),
        ("EVA (CHF M)",          "EVA",            "CHF",  CHF_TOLERANCE,  "CHF M"),
        ("ROA (start)",          "ROA_start",      "pct",  PCT_TOLERANCE,  "%"),
        ("ROC (start)",          "ROC_start",      "pct",  PCT_TOLERANCE,  "%"),
        ("ROE (start)",          "ROE_start",      "pct",  PCT_TOLERANCE,  "%"),
        ("ROA (avg)",            "ROA_avg",        "pct",  PCT_TOLERANCE,  "%"),
        ("ROC (avg)",            "ROC_avg",        "pct",  PCT_TOLERANCE,  "%"),
        ("ROE (avg)",            "ROE_avg",        "pct",  PCT_TOLERANCE,  "%"),
        ("Asset Turnover",       "Asset_Turnover", "mult", MULT_TOLERANCE, "x"),
        ("Avg Collection Period","Avg_Coll_Period", "days", DAYS_TOLERANCE, "days"),
        ("Inventory Turnover",   "Inv_Turnover",   "mult", MULT_TOLERANCE, "x"),
        ("Days in Inventory",    "Days_Inventory", "days", DAYS_TOLERANCE, "days"),
        ("Profit Margin",        "Profit_Margin",  "pct",  PCT_TOLERANCE,  "%"),
        ("Op. Profit Margin",    "Op_Profit_Margin","pct", PCT_TOLERANCE,  "%"),
        ("Debt Ratio",           "Debt_Ratio",     "pct",  PCT_TOLERANCE,  "%"),
        ("TIE",                  "TIE",            "mult", MULT_TOLERANCE, "x"),
        ("Debt Burden",          "Debt_Burden",    "mult", MULT_TOLERANCE, "x"),
        ("Current Ratio",        "Current_Ratio",  "mult", MULT_TOLERANCE, "x"),
        ("Quick Ratio",          "Quick_Ratio",    "mult", MULT_TOLERANCE, "x"),
        ("Cash Ratio",           "Cash_Ratio",     "mult", MULT_TOLERANCE, "x"),
        ("Du Pont ROA",          "DuPont_ROA",     "pct",  PCT_TOLERANCE,  "%"),
        ("Du Pont ROE",          "DuPont_ROE",     "pct",  PCT_TOLERANCE,  "%"),
    ]

    passes = fails = missing = 0
    failures = []

    print(f"\n  {'Ratio':<24} {'Computed':>10} {'LLM':>10} {'|Diff|':>8}  Result")
    print(f"  {'-'*62}")

    for display, key, unit, tol, suffix in checks:
        comp = r.get(key)
        stated = llm.get(key)

        if comp is None:
            print(f"  {'?':<2} {display:<24} {'ERROR: no computed value'}")
            continue
        if stated is None:
            print(f"  {'-':<2} {display:<24} {comp:>10.2f} {'N/A':>10} {'---':>8}  MISSING")
            missing += 1
            continue

        diff   = abs(comp - stated)
        passed = diff <= tol
        mark   = "✓" if passed else "✗"
        result = "PASS" if passed else "FAIL"
        if passed:
            passes += 1
        else:
            fails += 1
            failures.append((display, comp, stated, diff, suffix))

        print(f"  {mark:<2} {display:<24} {comp:>10.2f} {stated:>10.2f} {diff:>8.3f}  {result}  {suffix}")

    # ── Du Pont rounding gap analysis ──
    print(f"\n  {'─'*62}")
    print("  Du Pont rounding gap analysis (Gap 1 from spec retrospective):")
    dp_full  = r["DuPont_ROE"]
    dp_early = (round(r["DP_margin"]*100,1)/100 *
                round(r["DP_turnover"],2) *
                round(r["DP_leverage"],2) *
                round(r["DP_burden"],3)) * 100
    gap = abs(dp_full - dp_early)
    print(f"    Full-precision Du Pont ROE:   {dp_full:.4f}%")
    print(f"    Early-rounded Du Pont ROE:    {dp_early:.4f}%")
    print(f"    Rounding gap:                 {gap:.4f}%  "
          f"{'⚠ visible gap — matches known issue' if gap > 0.05 else '✓ negligible'}")

    # ── Balance sheet validation ──
    print(f"\n  {'─'*62}")
    print("  Balance sheet validation:")
    bs_check = r["curr_assets_total"] - (r["curr_liab_total"] + r["curr_equity"])
    print(f"    FY2025 Assets - (Liabilities + Equity) = {bs_check:,.0f} CHF M  "
          f"{'✓ balanced' if abs(bs_check) < 1 else '✗ IMBALANCE — check workbook'}")

    # ── Summary ──
    total = passes + fails + missing
    print(f"\n{'='*62}")
    print("SUMMARY")
    print(f"{'='*62}")
    print(f"  Ratios checked:   {total}")
    print(f"  PASS:             {passes}")
    print(f"  FAIL:             {fails}")
    print(f"  MISSING:          {missing}  (regex did not find value in markdown)")
    if (passes + fails) > 0:
        print(f"  Pass rate:        {passes/(passes+fails)*100:.1f}%")

    if failures:
        print(f"\n  Failures requiring attention:")
        for name, comp, stated, diff, suffix in failures:
            print(f"    ✗ {name}:")
            print(f"        Computed = {comp:.4f} {suffix}")
            print(f"        LLM said = {stated:.4f} {suffix}")
            print(f"        Diff     = {diff:.4f} {suffix}  (tolerance: ±{PCT_TOLERANCE if suffix == '%' else MULT_TOLERANCE})")
    elif fails == 0:
        print(f"\n  ✓ All detected ratios conform to spec within tolerance.")
        print(f"    LLM output is arithmetically reliable.")

    print(f"\n{'='*62}")
    print("Harness complete.")
    print(f"{'='*62}\n")

# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "=" * 62)
    print("  Ratio Conformance Harness v1.0")
    print("  Ha Tuan Nghiep — BUS-629 Corporate Finance")
    print("  github.com/hatuannghiep96/Corporate-Finance")
    print("=" * 62)

    d = load_workbook_data(WORKBOOK_PATH)
    r = compute_ratios(d)
    llm = extract_llm_values(ANALYSIS_PATH)
    compare_and_report(r, llm)
