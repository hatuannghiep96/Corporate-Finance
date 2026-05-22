# Stage 4 review — 2026-05-22

Reviewing `docs/specs/2026-05-20-ha-nestle-spec.md`, `deliverables/prompt-log.md`, and `deliverables/2026-05-20-ha-nestle-spec-retrospective.md`.

Nghiep — this is one of the strongest Stage 4 submissions in the cohort. The Part A / Part B structural split, the §4 prefix glossary you added in response to the earlier PR (with seven prefix scopes including `startYear_*`, `currentYear_*`, and `avg_*` separately), the explicit Du Pont ROE time-mismatch caveat in §7 Rule 4, and the structural-negative-NWC note in Rule 6 — these are the kinds of judgment calls that turn a checklist into an actual specification. The retrospective is genuinely unusual: very few MBA students will write a section-by-section verdict table with named-range counts and then quantify a Gap-3 sensitivity at "CHF 569M EVA difference." The notes below are not "you need to fix this" — they're four directions you could take *next*, picked because they extend something you've already done well rather than papering over something missing. Take any one of them seriously and you're doing real AI-quant work, not student work.

---

## What the auto-scan confirms

| Signal | Value | Read |
|---|---|---|
| Section coverage | 11/11 | Complete, with explicit Part A / Part B split |
| Spec length | ~2,491 words | At the top of the 1,500–2,500 target band |
| Named-range hits | 314 | Cohort-leading density — every formula and data input anchored to a named range |
| Ratio categories in §6 | 6/6 (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont) | All categories from the master template covered |
| Validation rules | 7 | Includes the Du Pont ROE time-mismatch caveat and structural-NWC business-context note |
| Prompt log | ~1,400 words | Documents two-round revision discipline across Stages 2, 3, and 4 with gaps named explicitly |
| Spec retrospective | Present | Effectiveness rated 4/5 with three gap fixes written in exact insertion language |

There is no Stage 4 rubric item where this spec falls short. The rest of this file is forward-looking.

---

## Four directions you could take next

These are ordered by how much new skill they exercise, not by priority — pick whichever interests you. None of them affects your Stage 4 score; this is intellectual extension work that the cohort's strongest students should be doing if they want their portfolios to actually demonstrate AI-quant capability rather than just "I followed the rubric."

### 1. Turn your spec into an eval harness (the "specification as benchmark" move)

You've already done the hardest part of this conceptually — your Stage 5 manual verification table picks seven ratios spanning all categories and grades the LLM's output to four-decimal precision (ROC, EVA, Du Pont ROE, Avg Collection Period, TIE, Current Ratio, ROE). You found two rounding-driven discrepancies and explained both. That table is, in spirit, an evaluation harness — written for a human grader.

The natural follow-up: **make it a program.**

**Concrete next step.** Take your manual verification table and rewrite it as a 30–50-line Python script that:
- Reads your Stage 5 analysis Markdown file (`deliverables/2026-05-20-ha-nestle-final-analysis.md`).
- Extracts each ratio value the LLM reported (regex against the Ratio Results tables is enough).
- Recomputes the expected value from your Stage 3 workbook by pulling the named ranges referenced in §6 (e.g., `INC_net / startYear_equity` for ROE-start-year) via `openpyxl`.
- Reports a pass/fail per validation rule from §7, including Rule 3's Du Pont ROA = direct ROA tolerance check.

You'd be the first student in the cohort to ship a spec with a programmatic conformance check attached. The artifact takes a few hours and demonstrates something most MBA finance courses don't even ask for: that you can specify a thing precisely enough to grade an AI's execution of it. Given that your retrospective already quantifies Gap 1 as "intermediate rounding compounded across four multiplications, 22.1% vs. 22.2%," you have the exact failure mode the harness should catch — and you have the fix language for it pre-written.

### 2. Run the spec through three LLMs and write the diff

Right now your Stage 5 evaluates a single LLM's output (Claude Sonnet 4.6) against your spec. The more interesting question — and the one that's harder to get a clean answer to — is: **how much does the model matter when the spec is good enough?**

**Concrete next step.** Take your finalized Stage 4 spec, feed it to Claude (Opus), ChatGPT (GPT-4 or GPT-5), and Gemini Pro with the same wrapper prompt (literally: *"Read this spec and produce the analysis it requests. No other context."*). Save all three outputs. Then write a one-page comparison:

- **Convergence:** Which ratio values do all three models compute identically? (These are the parts of your spec where the named-range formula notation is unambiguous — likely most of §6.)
- **Divergence:** Where do they differ — in computed values (Du Pont ROE rounding behavior is a likely candidate), in narrative judgment (interpretation of negative NWC), in hypothesis verdicts? Where one model gives a different Du Pont ROE than the other two, *why*? (Almost always: the ambiguous parts of your spec — which then become your retrospective's Gap 1 fix in production.)
- **One-paragraph thesis:** What does the divergence pattern tell you about which parts of finance work are now commodity-AI tasks vs. which still need a human (or a domain expert like your Nestlé Vietnam operational context — which no LLM has)?

This is the genre of work being published in industry blogs (Anthropic, OpenAI, McKinsey AI practice) right now. A solid one-page version of it from a finance MBA student is a portfolio piece, not coursework.

### 3. Sensitivity & Monte Carlo on the assumptions

Your spec uses two hardcoded analyst assumptions: `cost_capital = 9.0%` (class default) and `tax_rate = 24.6%` (Nestlé's FY2025 effective). Both are point estimates. EVA depends on `cost_capital` directly; `currentYear_after_tax_operating_income` depends on `tax_rate` through the after-tax operating income formula, which then propagates into ROA, ROC, EVA, and Du Pont operating margin.

A point-estimate spec produces a point-estimate analysis. A spec that **builds uncertainty in** produces an analysis that distinguishes "Nestlé's EVA is CHF 2,456M" from "Nestlé's EVA is CHF 2.5B ± CHF 1.8B at 80% confidence, with the bulk of the uncertainty coming from WACC, not operating performance." Your Gap-3 sensitivity language ("CHF 569M EVA difference if you swap startYear for avg capital") shows you already have the instinct for this.

**Concrete next step.** Add a §12 ("Sensitivity Specification") to your spec that defines:

```markdown
### 12. Sensitivity Specification

The Stage 5 analysis must include a one-page sensitivity appendix
covering the two analyst-assumption inputs:

| Input | Point estimate | Range to test | Distribution shape |
|---|---|---|---|
| cost_capital | 9.0% | 7.0% – 11.0% | Triangular, mode at 9.0% |
| tax_rate | 24.6% | 22.0% – 28.0% | Uniform |

Required outputs:
- One tornado chart showing which input moves EVA the most.
- A 5,000-trial Monte Carlo histogram of EVA with the 10th/50th/90th
  percentile values reported.
- One narrative paragraph: at what value of cost_capital does
  EVA cross zero? (Currently EVA = 2,456M at 9.0%; with
  startYear_total_capitalization of 88,390, EVA hits zero at
  WACC ≈ 11.8%.)
```

The Stage 5 LLM can produce this if your spec asks for it. The deliverable becomes a meaningfully better-than-textbook analysis — one that names what you don't know as well as what you do. Bonus: it would naturally combine with Direction 1 (the eval harness can score whether the Monte Carlo percentiles fall in the right range), and the EVA-crosses-zero point estimate above falls out of arithmetic you've already done.

### 4. Spec-driven generalization — make the spec Unilever-runnable

Your spec is Nestlé-specific in several places, but the structure is not. The §1 scope, §2 architecture, §4 prefix glossary, §5–§7 formula tables and validation rules, §8 ratio interpretation framework, §9 Du Pont decomposition, and §10–§11 output spec are all **company-agnostic**. The Nestlé-specific anchors are concentrated in: §3 (CHF data values for both years), §7 Rule 6 ("structurally normal for Nestlé"), §8's references to the ROIC 14.1% management KPI, the 2.90x net debt/EBITDA target, the "Fuel for Growth" CHF 2.5B program, the 90-day supplier payment terms, and the FMCG-specific collection-period benchmark of 30–45 days. The deeper observation: a well-written spec should be a parameterized template, and the company-specific values should be an appendix you swap out.

**Concrete next step.** Refactor the spec into two files:

- `spec-template.md` — the structure, with `{{COMPANY}}`, `{{TICKER}}`, `{{EXCHANGE}}`, `{{REPORTING_STANDARD}}`, `{{CURRENCY}}`, and `{{FYE}}` placeholders. §7 business-context rules become a `{{STRUCTURAL_NOTES}}` block; §8 management-KPI cross-references become a `{{MANAGEMENT_KPIS}}` block.
- `2026-05-20-ha-nestle-inputs.yaml` (or `.md`) — the Nestlé-specific data values for §3 (both years), the assumption set in §3 analyst-assumptions, the structural notes (negative-NWC-is-normal, 90-day supplier terms), and the management KPIs (ROIC 14.1%, net debt/EBITDA 2.90x, Fuel for Growth CHF 2.5B).

Then write a 1-paragraph note: *"To run this spec for Unilever (or any FMCG peer), replace the inputs file and re-run Stage 5. The named-range conventions, formula definitions, validation rules, and Du Pont decomposition are unchanged. The structural notes block in §7 and the management-KPI block in §8 are the only spec sections that require company-specific authoring."*

You will have shipped a **reusable analytical artifact** rather than a one-off deliverable. That's the difference between an MBA project and something you'd put on a senior analyst's GitHub. If the BUS-629 master template ever gets revised to support multi-company portfolio analysis, the parameterized version of your spec is the contribution that gets cited.

---

## A small honest reaction to the prompt log

Your prompt log is the most disciplined in the cohort, and it does something most logs don't: it shows **two-round revision behavior** with the specific gaps named between rounds. The Stage 4 Round 1 → Round 2 entry — where you caught that `currentYear_cash_marketable_securities` was referenced in §5 but never defined in §4, that `RATIO_leverage` had no formula in the Du Pont table, that `INC_ebit` and `INC_taxable_income` were ambiguously placed between §3 and §4, and that the 11.6% margin had no arithmetic source — is exactly the kind of self-audit that turns an LLM session into engineering. The Stage 3 entry catching the IFRS associates-income classification (CHF 1,143M after-tax, not pre-tax, recovering net income from CHF 8,111M to CHF 9,033M) is the kind of domain catch a non-finance LLM would miss without your insider context.

The single way the log could be sharper for portfolio purposes: when you describe the HIL iteration in Stage 5 Session 4 (the replenishment-system, three-commitment-stage, 90-day-supplier-terms context you added from your Nestlé Vietnam tenure), you could pull that into a separate `analysis/operational-context.md` artifact that lives independently of the prompt log. Right now that knowledge is buried in a Stage 5 Round 2 prompt; pulled out, it becomes a reusable annex that future Stage 5 runs (or a Direction-2 cross-LLM run) can re-inject as context — and it's a portfolio piece in its own right, since "I worked at Nestlé Vietnam and here is how their replenishment system actually works" is something no public dataset will ever contain.

---

## Looking ahead to Stage 5

Your Stage 5 deliverable is already in the repo and is unusually complete: raw LLM output preserved separately, manual verification table with seven ratios spanning all categories, final analysis with 1,703 words of prose (within target band) plus the two annotated rounding corrections, spec retrospective with effectiveness 4/5 and three gap fixes written in exact insertion language, AI tooling memo, and full repo polish. There is no Stage 5 cleanup work to schedule. Use that bandwidth on one of the four directions above instead. If you do, drop a note in your prompt log or under `analysis/explorations/` so the work is visible; if you don't, your Stage 5 is already in clean shape and you'll have lost nothing.

The post-deadline revision-sweep window is open if you want to add any of the above to the spec retroactively — bumps to Stage 4 are possible, though they're not the point. The point is whether one of these directions sounds interesting enough to spend a Saturday morning on. If yes, that's a much better use of the next two weeks than incremental polish on what's already a strong artifact. Directions 1 and 3 compose naturally (the harness can grade the Monte Carlo); Direction 4 composes with both (a parameterized spec is easier to cross-LLM test). Pick the one that sounds like the most fun.

---

*This review is feedback-only — no scores included.* Score numbers live in the internal grade report and the instructor's email; this file is intended as colleague-level input on your work, not as a graded artifact.
