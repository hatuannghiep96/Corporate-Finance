# Prompt Log — BUS-629 International Corporate Finance

**Student:** Ha Tuan Nghiep
**Course:** BUS-629 International Corporate Finance — VEMBA 33, Shidler College of Business, University of Hawaiʻi at Mānoa
**Repo:** https://github.com/hatuannghiep96/Corporate-Finance
**Purpose:** Required log of all AI-assisted sessions used in producing project deliverables. Each entry records the tool, model, prompt, output evaluation, and edits made.

---

## Stage 0 — Repository Setup (2026-05-16)

**Tool:** Claude Code (terminal)
**Model:** Claude Sonnet 4.6
**Purpose:** Scaffold repo structure, write professional bio and resume, configure .gitignore, and establish commit conventions.

**Prompts used:**
1. "Create a professional GitHub repo structure for a corporate finance MBA project. Folders needed: analysis/, data/, deliverables/, docs/, models/ — all lowercase. Add a README.md to each folder describing what belongs there."
2. "Write a 190-word professional bio for README.md. Background: Operations Manager at a family-owned Vietnamese manufacturer, former Nestlé Vietnam export-import role, RMIT Bachelor with Distinction, 4 peer-reviewed publications, MBA at Shidler UH Mānoa."
3. "Review my last 18 commit messages and identify which ones are too vague. Rewrite each weak message to follow the format: VERB + file/area + why."

**Edits made:** The initial bio draft was 240 words — trimmed to 190. Commit message rewrites required two rounds: Claude's first pass on three messages still used "Update" as the verb without enough context, so I specified the exact file and reason for each and re-ran.

---

## Stage 1 — Excel Performance Ratios Template (2026-05-16)

**Tool:** Claude (claude.ai)
**Model:** Claude Sonnet 4.6
**Purpose:** Review the instructor-provided performance ratios template and confirm placement in repo at `models/templates/`.

**Prompts used:**
1. "Read this Excel template. Summarize the tab structure, named-range conventions, and what data inputs are required at Stage 3."
2. "Confirm the color coding conventions match the Stage 1 brief. Flag any named ranges that appear in ratio formulas but are not defined as inputs."

**Edits made:** Template placed unmodified at `models/templates/performance-ratios-template.xlsx` per instructor instructions. The audit at Stage 4 later caught two named ranges that were under-defined — logged in the Stage 4 HIL entry.

---

## Stage 2 — Company Selection Memo (2026-05-16, revised 2026-05-20)

**Tool:** Claude (claude.ai)
**Model:** Claude Sonnet 4.6
**Purpose:** Draft a company selection memo for Nestlé S.A. meeting the Stage 2 rubric: executive summary, background, method, 3 directional hypotheses, data collection plan, limitations, references.

**Round 1 prompt:**
```
Draft a Stage 2 company selection memo for Nestlé S.A. (NESN, SIX Swiss Exchange).
Context: I am a former Nestlé Vietnam Supply Chain Management Trainee (June 2022–August 2023).
Requirements:
- IFRS reporting, CHF currency, December 31 fiscal year end
- Three directional hypotheses in "I expect X because Y" form, each grounded in a specific financial metric
- Audience: MBA course instructor reviewing for analytical rigor
- Include data collection plan and source documentation
- Target: 400–600 words prose
```

**Evaluation of Round 1 output:** Draft came in at 1,039 words — nearly double the target. Several sections repeated the same points in different phrasing. The fiscal years referenced (FY2023/FY2024) needed to be updated to FY2024/FY2025 after confirming Nestlé had published FY2025 statements. The trading operating profit margin was cited as "near 17%" — incorrect; actual FY2024 figure was 16.0%, falling to 14.2% in FY2025.

**Round 2 prompt:**
```
Trim this memo to under 600 words. Remove repetitive sections — a senior analyst memo is short.
Also fix: (1) update all fiscal year references from FY2023/FY2024 to FY2024/FY2025,
(2) correct the trading operating profit margin — it was 16.0% in FY2024 not 17%,
(3) the buyback figure of CHF 4.5B refers to FY2024 — label it as such since FY2025 buybacks
were only CHF 213M (program completed).
```

**Final edits made:** Output trimmed to ~550 words. All three factual corrections applied. Two additional line edits made manually: added "(FY2023 to FY2024)" to the net debt hypothesis for clarity, and updated the references list to remove the half-year press release not cited in the body.

---

## Stage 3 — Financial Model Population (2026-05-20)

**Tool:** Claude (claude.ai) for data mapping; Claude Code (terminal) for file commits
**Model:** Claude Sonnet 4.6
**Purpose:** Populate the performance ratios workbook with Nestlé FY2025 (current) and FY2024 (prior) audited IFRS financials across all three statement tabs.

**Round 1 prompt (Claude chat):**
```
I am uploading four files:
1. 2026-05-20-ha-nestle-financials.xlsx — the empty Stage 1 template (working copy)
2. 2025_income-statement_nestle.xlsx — Nestlé FY2025 income statement (IFRS, CHF millions)
3. 2025_balance-sheet_nestle.xlsx — Nestlé FY2025 balance sheet (IFRS, CHF millions)
4. 2025_cash-flow-statement_nestle.xlsx — Nestlé FY2025 cash flow (IFRS, CHF millions)

Read all four files. Map every Nestlé line item to the correct named range in the template.
Then populate the workbook: Balance Sheet (FY2025 current + FY2024 prior), Income Statement (FY2025),
Cash Flow (FY2025), Notes tab, and Ratios assumptions. Return a populated workbook with zero formula errors.
```

**Evaluation of Round 1 output:** Balance sheet balanced correctly on first pass (127,151 = 127,151 both years). Net income required one correction: the initial mapping produced CHF 8,111M instead of CHF 9,033M because IFRS income from associates (CHF 1,143M) flows after taxes — Claude's first draft treated it as pre-tax. Corrected by adjusting the "other income" plug to back-calculate from the reported net profit to parent shareholders. Net cash change also required a currency retranslation adjustment of (CHF 435M) added to financing activities to reconcile to the reported (CHF 963M).

**Verification results:**
- Balance Sheet FY2025: 127,151 = 127,151 ✓
- Balance Sheet FY2024: 139,264 = 139,264 ✓
- Net income: CHF 9,033M ✓
- Operating cash flow: CHF 15,904M ✓
- Formula errors: 0 ✓

**Claude Code prompt used to commit:**
```
Stage all 6 new files in data/, commit with message
"Add Nestle FY2024 and FY2025 source financials — income statement,
balance sheet, cash flow to data folder", push to origin main.
```

---

## Stage 4 — Technical Specification (2026-05-20)

**Tool:** Claude (claude.ai)
**Model:** Claude Sonnet 4.6
**Purpose:** Draft a self-contained technical specification covering model architecture, all data inputs with values, derived inputs with formulas, ratio definitions in named-range notation, validation rules, and full analysis requirements (Part A + Part B).

**Round 1 prompt:**
```
Read the Stage 4 brief and spec template from these URLs:
- https://raw.githubusercontent.com/adamwstauffer/shidler/main/courses/BUS-629-VEMBA-International-Corporate-Finance/stage4-technical-specification.md
- https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/spec-template.md

Using the spec template structure, draft a complete technical specification for Nestlé S.A.
ratio analysis. Requirements:
- Populate every section (Part A items 1–7, Part B items 8–11)
- Use named-range notation (BAL_*, INC_*, CASH_*, RATIO_*) throughout
- Include all data values numerically from the Stage 3 workbook
- Every named range used in a formula must be explicitly defined
- Keep YAML frontmatter intact
Company: Nestlé S.A. (NESN, SIX). FY2025 current, FY2024 prior. IFRS, CHF millions.
```

**Evaluation of Round 1 output — gaps identified:**

1. **Section 4 (Derived Inputs) — missing `currentYear_cash_marketable_securities`:** The Cash Ratio formula in Section 5 referenced this named range but it was never defined in Section 4. A Stage 5 LLM with only the spec would not know its source or value (= `BAL_cash_marketable_securities_curr` = 6,230 CHF M).

2. **Section 5 Du Pont table — `RATIO_leverage` undefined:** The component appeared in the Du Pont decomposition without a formula. Correct definition: `BAL_assets_total_curr / BAL_equity_shareholders_curr`.

3. **Section 3 vs Section 4 inconsistency — computed IS items:** `INC_ebit` and `INC_taxable_income` were listed as "(computed)" in the Data Inputs table (Section 3) but their formulas were never provided in Derived Inputs (Section 4). This created ambiguity about whether they were raw inputs or derived values.

4. **Section 7 — unsourced benchmark:** The 11.6% operating profit margin figure was stated without a formula or arithmetic source. A Stage 5 LLM could not verify it. Correct source: `currentYear_after_tax_operating_income / INC_sales` = 10,411 / 89,490 = 11.6%.

**Round 2 prompt:**
```
Fix four gaps in the spec:
1. Add currentYear_cash_marketable_securities to Section 4 Derived Inputs
   (= BAL_cash_marketable_securities_curr = 6,230 CHF M)
2. Add RATIO_leverage formula to Section 5 Du Pont table
   (= BAL_assets_total_curr / BAL_equity_shareholders_curr)
3. Move INC_ebit and INC_taxable_income from Section 3 to Section 4 with explicit formulas
4. Expand the 11.6% margin reference in Section 7 to show full arithmetic
```

**Final result:** All four gaps closed. Spec is now fully self-contained — every named range referenced in a formula has an explicit definition, source, and numeric value.
