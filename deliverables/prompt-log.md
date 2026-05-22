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

---

## Stage 5 — LLM Analysis, Evaluation, and Repo Polish (2026-05-20)

**Tool:** Claude (claude.ai) for analysis generation and document drafting; Claude Code (terminal) for all file commits
**Model:** Claude Sonnet 4.6
**Purpose:** Execute Stage 4 spec through LLM, verify output, produce final analysis, spec retrospective, and complete repo polish.

---

### Session 1 — PR feedback response

**Prompt (claude.ai):**
```
The instructor opened PR #1 "Stage 4 instructor review" on my repo.
The feedback file is at docs/feedback/stage4-review-2026-05-19.md.
Read it and tell me exactly what needs to be done — what to respond,
what to change, and in what order.
```

**Actions taken:**
- Posted response comment on PR thread acknowledging all feedback points
- Accepted structural suggestion: standalone Named Range Conventions §4
- Merged PR with descriptive merge commit message referencing the suggestion
- Added §4 Named Range Conventions (7-row prefix glossary + 5 convention rules) to spec in follow-up commit `a579882`

---

### Session 2 — Raw LLM output generation

**Prompt (claude.ai — spec only, no additional context):**
```
[Full contents of docs/specs/2026-05-20-ha-nestle-spec.md pasted verbatim]
```

No additional context was provided. The spec was required to stand alone per Stage 5 instructions. The complete unedited response was saved as `deliverables/2026-05-20-ha-nestle-llm-raw.md`.

**Output summary:** All 25+ ratios computed with full arithmetic. Two issues identified for correction:
1. Du Pont ROE stated as 22.1% — correct value is 22.2% (intermediate rounding compounded across four multiplications)
2. Current Ratio stated as 0.79x — precise value is 0.786x (rounding convention difference, not an error)

---

### Session 3 — Manual verification table

**Prompt (claude.ai):**
```
Build a manual verification table for Stage 5. Select 7 ratios spanning
all categories — prioritize ratios involving averages, start-year values,
or multi-step calculations where LLM errors are most likely. Show full
arithmetic for each. Compare to the LLM's stated values. Flag any discrepancies
with an explanation.
```

**Ratios selected and outcome:**

| Ratio | Result |
|---|---|
| ROC (avg capitalization) | ✅ Exact match (12.4%) |
| EVA | ✅ Exact match (CHF 2,456M) |
| Du Pont ROE | ⚠️ Rounding difference (22.2% vs LLM's 22.1%) |
| Avg Collection Period | ✅ Exact match (45.9 days) — LLM correctly used start-year receivables |
| Times Interest Earned | ✅ Exact match (5.67x) |
| Current Ratio | ⚠️ Rounding difference (0.786x vs LLM's 0.79x) |
| ROE (avg equity) | ✅ Exact match (25.9%) |

Zero material errors. Both discrepancies are rounding artifacts documented with full arithmetic.

---

### Session 4 — Final analysis with insider context

**Round 1 prompt (claude.ai):**
```
Draft the evaluated final analysis from the raw LLM output. Apply the
two rounding corrections. Add annotations where corrections were made.
Follow the output format in spec §11: Executive Summary, Ratio Results,
Du Pont, Category Analysis, Strategic Recommendations, Limitations.
Target: 1,200–1,800 words excluding tables.
```

**HIL iteration — insider context addition:**

After reviewing the Round 1 draft, I provided direct operational context from my time at Nestlé Vietnam to replace generic FMCG commentary:

- **Replenishment system:** Nestlé's proprietary demand-sensing system connects directly with supplier ERP systems and issues daily recommended purchase orders ("Đơn Hàng Đề Nghị"). The system runs through three commitment stages — fully flexible, ±5 unit adjustment, locked — progressively capturing real demand and eliminating bullwhip effect across the supply chain. Safety stock maintained at 15–21 days depending on product type.
- **Supplier payment terms:** 90-day payment terms applied uniformly across the supply base as a global parent company policy — the structural source of Nestlé's negative NWC position.
- **Product line context:** Coffee product line management, including cross-border export-import projects between Vietnam and Japan.

**Round 2 prompt (claude.ai):**
```
Rewrite the Efficiency and Liquidity category analysis paragraphs using
the operational details I just provided. Weave the replenishment system
explanation (three commitment stages, Đơn Hàng Đề Nghị, 15–21 day safety
stock, bullwhip effect) into the inventory discussion. Add the 90-day
supplier payment terms to the liquidity section as the structural source
of negative NWC. Keep prose within 1,200–1,800 words excluding tables.
```

**Final result:** 1,703 words prose (excluding tables). Two corrections annotated inline. Recommendation 4 reframed from generic "supply chain finance" to expanding the replenishment platform globally with a specific inventory days target (99.4 → 92–94 days).

---

### Session 5 — Spec retrospective

**Prompt (claude.ai):**
```
Complete the spec retrospective template for my Stage 4 spec. Use the
verification table and final analysis as evidence. Be honest — the grade
rewards specificity over self-congratulation. Identify the three most
consequential gaps with exact fix language. Rate effectiveness 1–5 with
evidence-tied justification.
```

**Key findings:**
- **Gap 1 (Du Pont precision):** Spec did not instruct executor to carry full decimal precision through Du Pont intermediate steps. Fix: add four-decimal-place precision instruction to Section 6.
- **Gap 2 (recommendation quantitative targets):** Spec required "actionable" recommendations but not numeric targets. Two recommendations required editorial additions. Fix: add mandatory quantitative target requirement to Section 9.
- **Gap 3 (EVA capital base disambiguation):** Spec listed three capitalization figures in proximity without explaining why start-year is the correct EVA convention. LLM got it right but could have substituted average (~CHF 569M EVA difference). Fix: add convention note to EVA row in Section 6.

**Effectiveness rating:** 4/5 — spec produced zero material arithmetic errors but required editorial intervention on Du Pont rounding and recommendation specificity.

---

## Stage 5 — Repo Polish & AI Tooling Memo (2026-05-20)

**Tool:** Claude (claude.ai)
**Model:** Claude Sonnet 4.6
**Purpose:** Complete Stage 5 repo polish checklist and write optional AI tooling experiment memo.

**Actions taken:**
1. Full repo audit identified 3 remaining issues: missing `docs/feedback/README.md`, stale `docs/README.md` structure table, and `BIO.md`/`RESUME.md` casing. All fixed in commit `de1c4e5`.
2. Final analysis updated with two missing required sections: "LLM Evaluation & Annotations" and "Executive Justification" — committed in `2949b12`.
3. Root `README.md` rewritten as a professional portfolio landing page with 6-stage project status table, repo tree, and analyst bio — committed in `2949b12`.
4. GitHub repo description set manually: "BUS-629 Corporate Finance portfolio — Nestlé S.A. ratio analysis (IFRS, FY2025) | MBA, Shidler UH Mānoa"

**AI tooling memo prompt:**
```
I want to write a 100–300 word reflection memo on AI-assisted financial
analysis for my portfolio repo. Ask me 5 questions first so the memo
reflects my actual experience, not a generic template.
```

**Key reflections captured:**
- Tan Hung Firm (family SME) currently runs on experience with no formal data structure — the workflow from this project is directly applicable at SME scale
- The biggest surprise: Claude Code's accessibility for someone with zero GitHub or coding background
- Core insight: AI accelerates the analysis layer but cannot run without structured data — the prerequisite for Tan Hung is building records, not buying tools
- Would use the spec-driven workflow on real SME financial analysis: gross margin by product line, inventory turnover, distributor receivables days

---

## Portfolio Extensions — Direction 4: Parameterized Spec Template (2026-05-22)

**Tool:** Claude (claude.ai)
**Model:** Claude Sonnet 4.6
**Purpose:** Refactor the Nestlé-specific Stage 4 spec into a reusable parameterized template that any analyst can run for a different company by swapping one inputs file.

**Prompt:**
```
Read the instructor's Direction 4 advice carefully. Refactor
docs/specs/2026-05-20-ha-nestle-spec.md into two files:
1. docs/templates/spec-template.md — company-agnostic structure
   with {{PLACEHOLDER}} syntax for all company-specific values
2. docs/specs/2026-05-20-ha-nestle-inputs.yaml — all Nestle-specific
   data values, analyst assumptions, and business context fields

Apply the Gap 1 fix (Du Pont precision instruction) and Gap 2 fix
(mandatory quantitative targets) from the retrospective while
rewriting. Make it Unilever-runnable by swapping only the inputs file.
```

**Design decisions made:**
- `{{PLACEHOLDER}}` syntax chosen over Jinja2 for readability — any analyst can understand it without coding knowledge
- YAML format for inputs — machine-readable by Python (feeds directly into Direction 1 harness) and human-readable for manual editing
- Gap 1 fix applied to Section 6: "Compute each component to at least four decimal places before multiplying. Round only the final output."
- Gap 2 fix applied to Section 10: mandatory quantitative target required in every recommendation
- "How to use" section added at bottom — self-documenting for future analysts
- "Notes for next analyst" comments added in yaml — explains exactly what to change for Unilever

**Output:** 552 lines total across two files — commit `0a02255`

**Next steps identified:**
- Run for Unilever as validation that the template is truly company-agnostic
- Add §12 Sensitivity Specification to the template (Direction 3 extension)
- Link the Python harness (Direction 1) to the template as the conformance artifact

---

## Portfolio Extensions — Direction 1: Python Ratio Conformance Harness (2026-05-22)

**Tool:** Claude (claude.ai) for script design; Claude Code for execution
**Model:** Claude Sonnet 4.6
**Purpose:** Build a 430-line Python script that automatically reads the Stage 3 workbook, recomputes all 23 ratios from spec formulas, extracts LLM-stated values from the final analysis markdown, and reports PASS/FAIL per ratio with tolerances.

**Design prompt:**
```
Build a Python conformance harness for the Nestle ratio analysis.
It must:
1. Load models/builds/2026-05-20-ha-nestle-financials.xlsx via openpyxl
2. Read named ranges from Balance Sheet, Income Statement, Cash Flow tabs
3. Recompute all 23 ratios from spec Section 6 formulas at full precision
4. Extract LLM-stated values from deliverables/2026-05-20-ha-nestle-final-analysis.md via regex
5. Compare computed vs LLM values with tolerances:
   - Percentages: ±0.15 percentage points
   - Multiples: ±0.02x
   - Days: ±0.5 days
   - CHF values: ±50M
6. Report PASS/FAIL per ratio in a clean table
7. Run the Du Pont rounding gap analysis automatically
   (Gap 1 from retrospective: full precision vs early-rounded path)
8. Validate balance sheet balance
```

**Execution result:**
```
Ratios checked:   23
PASS:             23
FAIL:              0
Pass rate:       100.0%
```

**Notable diagnostics caught automatically:**
- EVA: computed CHF 2,454.70M vs LLM-stated CHF 2,456M — CHF 1.3M difference, within tolerance ✓
- Du Pont ROE: full precision 22.2483% vs early-rounded 22.1228% — 0.1255% gap confirmed and quantified automatically — exactly the Gap 1 issue documented in the spec retrospective
- Balance sheet: Assets − (Liabilities + Equity) = 0 ✓

**Significance:** The harness independently confirmed what the manual verification table showed — zero material errors in the LLM output. The Du Pont rounding gap detection is the Gap 1 retrospective insight now running as code. Commit `[see latest]`.

**Next steps identified:**
- Add Monte Carlo sensitivity loop over cost_capital (7–11%) — produces EVA tornado chart (Direction 3 extension, ~20 additional lines)
- Verify EVA crosses zero at WACC ≈ 11.8% automatically
- Update WORKBOOK_PATH and ANALYSIS_PATH to run for Unilever once inputs yaml is complete

---

## Recommended next sessions (not yet executed)

**Priority 1 — Operational context annex:**
Extract Nestlé Vietnam insider knowledge into `analysis/operational-context.md` — replenishment system architecture, 90-day supplier terms, three commitment stages, bullwhip effect elimination. Currently buried in Stage 5 prompt log. As a standalone artifact it becomes reusable context for future LLM runs and a portfolio piece the instructor specifically called out.

**Priority 2 — Direction 1 extension (Monte Carlo):**
Add §12 Sensitivity Specification to spec-template.md. Extend ratio_harness.py with a 5,000-trial Monte Carlo over cost_capital (7–11%, triangular) and tax_rate (22–28%, uniform). Report EVA at 10th/50th/90th percentile. Verify EVA-crosses-zero WACC programmatically (~11.8% based on arithmetic: EVA = 0 when WACC = atoi / startYear_cap = 10,411 / 88,390 = 11.78%).

**Priority 3 — Direction 4 validation (Unilever run):**
Download Unilever FY2024 + FY2025 IFRS financials. Create `2026-05-22-ha-unilever-inputs.yaml` by duplicating the Nestlé file and replacing all values. Run spec-template.md end-to-end. Write a one-page comparison memo: where do Nestlé and Unilever converge/diverge on ratios, and what does the gap reveal about FMCG capital allocation strategy?

---

## Portfolio Extensions — Direction 3: Monte Carlo EVA Sensitivity (2026-05-22)

**Tool:** Claude (claude.ai) for script design; Claude Code for execution
**Model:** Claude Sonnet 4.6
**Purpose:** Extend the ratio harness with a 5,000-trial Monte Carlo simulation over the two analyst assumptions that most affect EVA, per spec Section 12 requirements. Also add §12 Sensitivity Specification to spec-template.md so any future LLM run knows to produce this output.

**Design rationale:**
The instructor noted in the Stage 4 feedback that Gap 3 (EVA capital base ambiguity) revealed an insight: "EVA = 0 when WACC = atoi / startYear_cap = 10,411 / 88,390 = 11.78%." This is arithmetic that should run automatically, not be computed once and forgotten. The Monte Carlo extension makes that computation repeatable, generalizable, and self-documenting.

**Prompt (claude.ai):**
```
Extend ratio_harness.py with a Step 5 Monte Carlo sensitivity function.
Requirements per spec Section 12:
- Draw cost_capital from triangular distribution (low=7%, mode=9%, high=11%)
- Draw tax_rate from uniform distribution (low=22%, high=28%)
- Run 5,000 trials, recompute EVA each trial using numpy
- Report EVA at 10th, 50th, 90th percentile
- Report P(EVA > 0)
- Compute break-even WACC analytically: atoi / startYear_cap
- Produce text tornado chart showing WACC vs tax rate dominance
- Add --sensitivity flag to argparse so base harness runs unchanged
Also add Section 12 Sensitivity Specification to spec-template.md
with the exact output requirements as a structured table.
```

**Monte Carlo results (5,000 trials, seed=42):**

| Output | Value |
|---|---|
| EVA 10th percentile (pessimistic) | CHF 1,479M |
| EVA 50th percentile (median) | CHF 2,450M |
| EVA 90th percentile (optimistic) | CHF 3,451M |
| P(EVA > 0) | **100.0%** |
| Break-even WACC | **11.78%** (278bps headroom above base 9.0%) |
| WACC dominance over tax rate | **32×** (±CHF 1,768M vs ±CHF 55M) |

**Key insight:** WACC is the dominant driver of EVA uncertainty by a factor of 32. Tax rate optimization is essentially irrelevant to Nestlé's value creation thesis — WACC management is everything. Nestlé's value-creation thesis is robust across 100% of simulated scenarios.

**Spec impact:** §12 added to spec-template.md — any future company run using the template will automatically include this sensitivity analysis. The harness catches break-even WACC automatically for any company whose inputs yaml is loaded.

---

## Portfolio Extensions — Direction 3 + Operational Context Annex (2026-05-22)

**Tool:** Claude (claude.ai)
**Model:** Claude Sonnet 4.6
**Purpose:** Extract Nestlé Vietnam insider knowledge into a standalone reusable artifact, per instructor's specific suggestion in Stage 4 feedback: "pulled out, it becomes a reusable annex that future Stage 5 runs can re-inject as context — and it's a portfolio piece in its own right."

**Prompt:**
```
Write analysis/operational-context.md — a standalone reusable annex
extracting my Nestlé Vietnam operational experience. Structure:
1. How to use this file (injection instructions for future LLM runs)
2. The replenishment system — three stages, Đơn Hàng Đề Nghị,
   safety stock 15-21 days, bullwhip effect elimination
3. Supplier payment terms — 90-day global policy, financial consequence
   at group level, interaction with retail collection terms
4. Cross-border export-import operations (Vietnam-Japan, coffee line)
5. Supplier Innovation Workshop 2023 context
6. Implications for ratio interpretation (specific ratio categories)
7. What this context cannot tell you (honest limitations)
```

**Design decision:** Section 7 (limitations) is the most important section analytically. Writing what your insider knowledge cannot tell you — subsidiary vs. group, 14-month tenure vs. current policy, coffee line vs. other categories — is what distinguishes a credible analytical voice from unqualified generalization. This section makes the rest of the document more credible, not less.

**Output:** 1,438 words across 7 sections — commit `c66277d`

---

## Portfolio Extensions — Direction 4 Validation: Unilever Peer Comparison (2026-05-22)

**Tool:** Claude (claude.ai) for data extraction and script design; Claude Code for execution
**Model:** Claude Sonnet 4.6
**Purpose:** Validate that spec-template.md is truly company-agnostic by running it for Unilever PLC (ULVR) — a direct FMCG peer to Nestlé — using only a swapped inputs yaml file. This is the core Direction 4 test: does the template require zero changes between companies?

**Data extraction prompt:**
```
Read the Unilever Annual Report and Accounts 2025 (PDF uploaded).
Extract all financial statement data needed to populate the spec-template
named ranges for FY2025 (current) and FY2024 (prior):
- Consolidated balance sheet (page 131)
- Consolidated income statement (page 128)
- Consolidated cash flow statement (page 132)
- Notes for D&A, inventories, finance costs, tax charge
Report currency (EUR millions), any restatements, and important
structural notes (Ice Cream demerger, continuing ops basis).
```

**Key extraction decisions made:**
1. **Continuing operations only:** Unilever demerged Ice Cream in 2025 (gain €3,373M). All income statement figures use continuing operations (€5,682M net profit to parent) to ensure comparability with Nestlé's uninterrupted operations.
2. **FY2024 restated:** Unilever restated FY2024 comparatives to exclude Ice Cream throughout. Used restated figures for prior-year named ranges.
3. **Share price verification:** ULVR ADR closing price December 31, 2025 = USD 65.40 (verified from Yahoo Finance historical data). Converted at EUR/USD 1.04 = EUR 62.88. Post 888:1000 stock split (December 9, 2025) already reflected.
4. **Shares outstanding:** Back-calculated from EPS disclosure — total net profit to shareholders EUR 9,469M / Basic EPS EUR 4.33 = 2,186M shares.
5. **Tax rate:** Effective rate from continuing operations — 2,481 / 8,693 = 28.5%.

**Peer comparison script prompt:**
```
Write analysis/peer_comparison.py that:
1. Reads both nestle-inputs.yaml and unilever-inputs.yaml via pyyaml
2. Computes all ratios for both companies using identical formulas
3. Prints a side-by-side comparison table across all 6 ratio categories
4. Adds analyst commentary section identifying the 6 most analytically
   interesting divergences with directional conclusions
5. Ends with a Direction 4 template validation verdict
Currency note: Nestlé in CHF, Unilever in EUR — ratios are comparable;
absolute monetary values are not directly comparable.
```

**Results — Nestlé vs Unilever FY2025:**

| Category | Key finding |
|---|---|
| Profitability | Unilever leads across every metric — ROC avg 14.9% vs 12.4%, ROE avg 32.0% vs 25.9% |
| Value creation | Unilever EVA spread 5.9pp vs Nestlé 3.4pp above WACC; break-even WACC headroom 5.2pp vs 2.8pp |
| Efficiency | Asset turnover virtually identical (0.64x vs 0.63x); inventory gap is the standout — Unilever 70.5 days vs Nestlé 99.4 days (Nestlé's replenishment system visible in data) |
| Leverage | Almost identical — both 74-75% debt ratio, both 0.79x current ratio |
| Interest coverage | Unilever TIE 8.83x materially stronger than Nestlé 5.67x |
| Template | Direction 4 confirmed ✅ — spec-template.md ran identically; only inputs yaml changed |

**Most analytically interesting finding:** Nestlé's 99.4-day inventory vs Unilever's 70.5-day inventory reveals the trade-off in Nestlé's replenishment system. The 3-stage commitment model with 15-21 day safety stock is operationally disciplined but maintains higher buffers than Unilever's leaner model. Whether this reflects the complexity of Nestlé's 188-country footprint and temperature-controlled categories, or an opportunity to tighten further, is a legitimate analytical question for Stage 5-equivalent work.

**Direction 4 validation verdict:** Template is fully company-agnostic. The named-range conventions (Section 3), formula definitions (Section 6), validation rules (Section 7), and Du Pont decomposition (Section 9) required zero changes between Nestlé and Unilever. Only the inputs yaml changed. To run for a third company: duplicate the yaml, replace all values, run peer_comparison.py.
