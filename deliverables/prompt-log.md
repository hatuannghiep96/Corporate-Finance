# Prompt Log — BUS-629 Corporate Finance

This file tracks all AI prompts used in producing
deliverables for this project, as required by Stage 4.

## Stage 2 — Company Selection Memo
**Tool:** Claude (claude.ai)
**Date:** 2026-05-16
**Purpose:** Draft company selection memo for Nestlé S.A.
**Prompt:** "Draft a Stage 2 company selection memo for
Nestlé S.A. (NESN, SIX). I am a former Nestlé Vietnam
Supply Chain Management Trainee. Use real 2024 financial
data. Include 3 falsifiable hypotheses in I expect X
because Y form. Audience is a managing director."
**Edits made:** Verified all figures against Nestlé 2024
full-year results press release. Confirmed data accuracy.

## Stage 3 — Financial Model Population (2026-05-20)

**Session goal:** Populate performance ratios workbook with Nestlé FY2025 and FY2024 audited financials.

**Prompts used:**
1. Claude (chat) read Nestlé xlsx source files and mapped all line items to template named ranges
2. Claude (chat) populated all tabs: Balance Sheet (both years), Income Statement (FY2025), Cash Flow (FY2025), Notes/Cover, Ratios assumptions
3. Claude Code committed and pushed populated workbook to models/builds/

**Verification:** Balance sheet balanced both years (127,151 = 127,151 and 139,264 = 139,264). Zero formula errors. Net income CHF 9,033M, sales CHF 89,490M, operating cash flow CHF 15,904M — all tie to audited source.

## Stage 4 — Technical Specification HIL Iteration (2026-05-20)

**Round 1 gaps identified after reviewing the first draft:**

1. `currentYear_cash_marketable_securities` was used in the Cash Ratio formula (Section 5) but never defined in Section 4 (Derived Inputs). A Stage 5 LLM would not know its source or value.

2. `RATIO_leverage` appeared in the Du Pont table without a formula definition. The Stage 5 LLM could not compute it.

3. `INC_ebit` and `INC_taxable_income` were listed as "(computed)" in Section 3 Data Inputs with no formula — making them inputs, not derived values. Moved formulas to Section 4.

4. The 11.6% operating profit margin benchmark in Section 7 appeared without a formula or source — a Stage 5 LLM could not verify or reproduce it.

**Fixes applied:** Added all four missing definitions to Sections 4, 5, and 7. The spec is now fully self-contained — every named range referenced in a formula has an explicit definition and numeric value.
