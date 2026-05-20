---
template: spec-retrospective
purpose: "Structured self-evaluation of the Stage 4 technical specification after seeing how the LLM executed it at Stage 5"
author: Ha Tuan Nghiep
date: 2026-05-20
company: Nestlé S.A. (NESN)
spec_file: docs/specs/2026-05-20-ha-nestle-spec.md
stage5_output: deliverables/2026-05-20-ha-nestle-llm-raw.md
courses: [BUS-629]
---

# Stage 4 Spec — Retrospective

**Author:** Ha Tuan Nghiep
**Date:** 2026-05-20
**Company:** Nestlé S.A. (NESN, SIX Swiss Exchange)
**Spec being evaluated:** `docs/specs/2026-05-20-ha-nestle-spec.md`
**Stage 5 LLM output:** `deliverables/2026-05-20-ha-nestle-llm-raw.md`
**Verification table:** `analysis/validation/2026-05-20-ha-nestle-stage5-verification.md`

---

## 1. Section-by-section verdict

| Spec section | Verdict | Symptom in Stage 5 output |
|---|---|---|
| Part A.1 — Scope & Objective | Clear | LLM correctly identified FY2025 as current year, FY2024 as prior year, IFRS, CHF millions throughout. No scope drift observed. |
| Part A.2 — Model Architecture | Clear | LLM correctly described the six-tab workbook structure and color-coding conventions without prompting. |
| Part A.3 — Data Inputs | Clear | All 314 named-range references resolved correctly. LLM used `startYear_receivables` (11,251) rather than current-year receivables for the collection period — the correct spec-consistent choice. |
| Part A.4 — Named Range Conventions | Clear | All prefixes (`BAL_*`, `INC_*`, `CASH_*`, `RATIO_*`, `startYear_*`, `currentYear_*`, `avg_*`) applied consistently throughout the output. Added in response to Stage 4 PR feedback from `adamwstauffer`; the addition demonstrably improved LLM precision. |
| Part A.5 — Derived Inputs | Clear | All derived inputs computed correctly: `currentYear_after_tax_operating_income` = 10,411, `avg_total_capitalization` = 83,847, `avg_equity` = 34,876. No hallucinated values detected. |
| Part A.6 — Ratio Definitions & Formulas | Vague | Du Pont ROE computed as 22.1% instead of 22.2% due to intermediate rounding. Spec did not instruct the executor to carry full decimal precision through multi-step Du Pont multiplications. See Gap 1. |
| Part A.7 — Validation Rules | Clear | LLM explicitly noted the Du Pont ROE time-mismatch (§6 Rule 4) and the structural-negative-NWC note (§6 Rule 6) in the analysis — both pre-empted false-positive flags that would otherwise have appeared. |
| Part B.8 — Analysis Requirements | Clear | All five ratio categories analyzed with benchmarks. Management KPI cross-references (ROIC 14.1%, net debt/EBITDA 2.90x) cited correctly in context. |
| Part B.9 — Du Pont Decomposition | Clear | Primary driver (leverage 3.85x) correctly identified. Time-mismatch disclosed. Du Pont ROA vs direct ROA compared (7.4% vs 7.8%). Sustainability assessed against net debt/EBITDA target range. |
| Part B.10 — Strategic Recommendation Requirements | Vague | All five recommendations followed the "Ratio X → Y → action → risk" template. However, the spec did not specify a minimum quantitative threshold for recommendations — two of the five lacked specific numeric targets (e.g., "20–30% capex increase" was present, but "CHF 3–5B debt reduction target" was absent from the LLM draft and had to be added in the final analysis). See Gap 2. |
| Part B.11 — Output Format | Clear | Document structure matched the spec exactly: Executive Summary, Ratio Results, Du Pont, Category Analysis, Strategic Recommendations, Limitations — in the correct order. Word count within the 1,200–1,800 target. |

---

## 2. Top three gaps with evidence

### Gap 1: Du Pont intermediate rounding instruction missing

- **Where it surfaced:** The raw LLM output (`deliverables/2026-05-20-ha-nestle-llm-raw.md`, Du Pont Decomposition section) states Du Pont ROE as 22.1%. The correct unrounded value is 22.26% → 22.2%. The LLM rounded each intermediate component before multiplying (11.6% × 0.64 × 3.85 × 0.774), compounding error across four multiplications. Confirmed in the verification table (R3).
- **Spec cause:** Section 6 (Ratio Definitions & Formulas) listed the Du Pont formula components with example rounded values in the table (e.g., "11.6%", "0.64x") without explicitly instructing the executor to preserve full decimal precision through intermediate steps and only round at the final output.
- **Fix (exact language):** Add the following sentence to the Du Pont table in Section 6: *"Compute each component to at least four decimal places before multiplying. Round only the final Du Pont ROA and Du Pont ROE outputs to one decimal place. Rounding intermediate components before multiplication will compound error across the four-step product."*

---

### Gap 2: Strategic recommendations lacked mandatory quantitative targets

- **Where it surfaced:** In the raw LLM output, Recommendation 1 (leverage reduction) stated "accelerate debt repayment" without specifying a target amount or ratio level. Recommendation 3 (intangible rationalization) said "reduce the intangible asset base" without specifying a percentage or timeline. Both required editorial additions in the final analysis (CHF 3–5B debt repayment target; 10–15% intangible reduction over FY2026–FY2028).
- **Spec cause:** Section 9 (Strategic Recommendations) required each recommendation to "propose a concrete, actionable response" and "identify the primary risk" but did not require a quantitative target (a specific CHF amount, percentage, ratio level, or timeline). The LLM interpreted "actionable" as directional rather than numeric.
- **Fix (exact language):** Add to Section 9: *"Each recommendation must include at least one quantitative target anchored to a specific ratio value or CHF amount — for example, 'reduce net debt/EBITDA from 2.90x to 2.40x by year-end FY2026' or 'increase pet care capex by CHF 500M in FY2026.' Directional statements without a numeric anchor do not satisfy this requirement."*

---

### Gap 3: EVA capital base not explicitly disambiguated

- **Where it surfaced:** The LLM correctly used `startYear_total_capitalization` (88,390) as the EVA capital base — which matches the spec formula. However, the spec listed three different capitalization figures in close proximity: `startYear_total_capitalization`, `currentYear_total_capitalization`, and `avg_total_capitalization`. A less capable LLM or a human analyst following the spec cold might have substituted the average (83,847) or current-year figure (79,304), producing EVA of 3,025M or 3,274M respectively — differences of CHF 569M and CHF 818M.
- **Spec cause:** Section 5 (Derived Inputs) defined the EVA formula as `currentYear_after_tax_operating_income − (cost_capital × startYear_total_capitalization)` but did not include a parenthetical note explaining *why* the start-year capital base is used (EVA convention: capital employed at the start of the period, before the year's returns are generated).
- **Fix (exact language):** Add to the EVA row in Section 6: *"Note: EVA uses `startYear_total_capitalization` as the capital base — not the average or current-year figure. Convention: capital is measured at the start of the period over which returns are generated. Using average or current-year capital would overstate EVA if capital was reduced during the year (as it was in FY2025, when total capitalization fell from 88,390 to 79,304)."*

---

## 3. Revisions

If re-running with a revised spec, the three changes I would make:

1. **Add Du Pont precision instruction** (four decimal places through intermediate steps, round only at final output) — addresses Gap 1. This is a one-sentence addition to Section 6 with zero ambiguity.
2. **Require quantitative targets in recommendations** (specific CHF amount, ratio level, or percentage, not just direction) — addresses Gap 2. This would have produced stronger LLM recommendations without editorial intervention.
3. **Add EVA capital base disambiguation note** (explain why start-year is the correct convention, and flag the ~CHF 600–800M sensitivity to the choice) — addresses Gap 3. This would protect against a silent substitution error in a less capable executor.

---

## 4. Effectiveness rating

**My rating: 4**

**Justification:**

The spec produced arithmetically reliable output across all 25+ ratios with zero material errors — confirmed by the manual verification table (5 exact matches, 2 rounding-only differences, 0 material errors). The structural validation rules (§6) performed exactly as designed: the negative NWC false-positive was pre-empted, the Du Pont time-mismatch was disclosed correctly in the LLM output without prompting, and all six ratio categories were covered with correct named-range references throughout.

The rating falls short of 5 on two grounds. First, the Du Pont ROE rounding gap (22.1% vs 22.2%) required a manual correction — a one-sentence precision instruction in Section 6 would have prevented it. Second, two of the five strategic recommendations required editorial additions of quantitative targets before they met the standard I expected of a final analysis. Both gaps are traceable to specific spec omissions, not to LLM capability failure — which is exactly the discipline this retrospective is designed to surface.

I would hand this spec to a junior analyst with confidence that the ratio arithmetic would be correct. I would not hand it to them without reviewing the Du Pont component calculations and the recommendation specificity — hence a 4, not a 5.

---

## 5. Forward link

In the next spec I write — for any company or domain — I will include a dedicated "Computation Precision" subsection in Part A specifying rounding conventions at the intermediate step level, not just at the final output, because multi-step formulas are where rounding error compounds silently and escapes detection until the verification stage.

---

## 6. Retrospective process feedback

**What filling this out surfaced that a free-form write-up would not have:**

The section-by-section verdict table forced me to read the LLM output against the spec section by section, rather than reading it as a continuous document. This revealed Gap 3 (EVA capital base ambiguity) — which I would not have noticed in a free-form review because the LLM happened to get the answer right. The table structure forces you to ask "could a different executor have gotten this wrong?" rather than just "did this executor get it right?" That is a meaningfully different question and produces more useful spec improvement insights.

**One structural change I would make to this template:**

Add a "Near-miss" column to the Section 1 verdict table — a cell for cases where the LLM got the right answer but the spec was ambiguous enough that a wrong answer was plausible. Gap 3 (EVA capital base) is exactly this case: verdict is "Clear" because the output was correct, but the spec had a latent ambiguity that a near-miss column would have forced me to document. Currently, a "Clear" verdict and a "Clear-but-lucky" verdict look identical in the table — and the distinction matters for improving the spec.
