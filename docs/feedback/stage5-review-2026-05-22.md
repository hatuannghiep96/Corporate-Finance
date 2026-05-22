# Stage 5 review — 2026-05-22

Reviewing `deliverables/2026-05-20-ha-nestle-final-analysis.md`, `deliverables/2026-05-20-ha-nestle-spec-retrospective.md`, and the supporting verification + retrospective artifacts.

Nghiep — the analysis content here is among the strongest in the cohort. The Vietnam Nestlé operational background, especially the replenishment-system section (three commitment stages, the "Đơn Hàng Đề Nghị" daily ordering loop, 90-day supplier terms as a structural NWC advantage), turns this from a textbook ratio analysis into something a senior analyst at a buy-side firm would read top to bottom. That's the rarest thing in a Stage 5 deliverable, and it can't be auto-generated — it had to come from you. Most of the notes below are about the *packaging* of the analysis (auto-scanner-visible signals the rubric measures), not the analysis itself. Take the packaging notes seriously — under the revision-sweep policy they're low-effort fixes that retroactively improve the Stage 5 score — but read them as adjacent to, not corrections of, content that's already strong.

---

## What the auto-scan picks up

| Artifact | Status |
|---|---|
| Raw LLM output | ✓ `deliverables/2026-05-20-ha-nestle-llm-raw.md` |
| Manual verification table | ✓ `analysis/validation/2026-05-20-ha-nestle-stage5-verification.md` (11 rows, Match? column present) |
| Final analysis | ✓ 2,982 words, 117 ratio citations |
| Spec retrospective | ✓ 1,672 words, 4/5 template signals detected |
| Prompt log | ✓ `deliverables/prompt-log.md` |
| Stage 2 feedback response memo | — not detected |

The auto-scanner flagged three packaging issues that pulled the rubric score below where the content quality sits. Each is addressable in well under an hour.

### Packaging fix 1 — Recommendations not detected by the scanner

The grading scanner counted **0 strategic recommendations** in your final analysis — but you have five, with clear ratio anchors and quantitative targets. The scanner is regex-based and looking for a specific pattern; your formatting (`**1. Accelerate debt reduction...**` as a bold inline header followed by the prose) doesn't match the pattern it watches for.

**The simplest fix is to add explicit subheadings.** Change:

```markdown
**1. Accelerate debt reduction while the buyback program is dormant.**
`RATIO_debt_ratio` at 74.0% and net debt/EBITDA at 2.90x leave limited headroom...
```

to:

```markdown
### Recommendation 1 — Accelerate debt reduction while the buyback program is dormant

**Ratio anchor:** `RATIO_debt_ratio` at 74.0%; net debt/EBITDA at 2.90x.
**Action:** Target CHF 3–5B gross debt repayment in FY2026 → net debt/EBITDA of 2.40–2.50x by year-end.
**Risk:** Reduces flexibility for opportunistic bolt-on acquisitions.
```

The content is identical; the structural cues (`###` heading, labeled "Ratio anchor / Action / Risk" lines) make the recommendations machine-detectable while also reading more naturally as a board-deck-style memo. Apply the same change to recommendations 2–5 and you'll go from 0 detected to 5 detected.

### Packaging fix 2 — Missing "Company & Data Summary" section header

Your document opens with a clean metadata block (Author / Date / Course / Company / Data source) followed by an editorial note, then jumps to the Executive Summary. The rubric template lists a literal section called **"Company & Data Summary"** between the metadata and the Executive Summary. The content the rubric is looking for is already in your metadata block — what's missing is the explicit named section.

Add this between the metadata block and the Executive Summary:

```markdown
## Company & Data Summary

**Company:** Nestlé S.A. (NESN, SIX Swiss Exchange).
**Reporting:** Consolidated Financial Statements FY2025 (IFRS, CHF millions).
**Fiscal year:** FY2025 (current) vs. FY2024 (prior).
**Data sources:** Nestlé FY2025 Annual Report, ratios computed
from the Stage 3 workbook at `models/builds/2026-05-20-ha-nestle-financials.xlsx`
(named ranges: `BAL_*`, `INC_*`, `CASH_*`, `RATIO_*`).
**Analyst assumptions:** `share_price` = CHF 72.06 (Dec 31, 2025);
`shares_outstanding` = 2,587M (basic, FY2025);
`cost_capital` = 9.00% (BUS-629 class default); `tax_rate` = 21%.
```

This costs you 15 lines and converts a rubric-blind section to a rubric-visible one.

### Packaging fix 3 — Stage 2 feedback response memo

The Stage 5 rubric has a 5-point line for "Stage 2 feedback incorporation" that looks for a response memo at `docs/decisions/{date}-{lastname}-stage4-feedback-response.md` (or similar). You committed three Stage 2 memo updates after the instructor PR landed, which is the work — but without a small writeup that *names* the changes, the auto-scanner can't tie commits to feedback.

A 250–400-word response memo would close the gap. Suggested structure:

```markdown
# Response to Stage 2 instructor feedback

**Feedback received:** [link to PR or one-sentence summary of the
main suggestion]

**Changes made:**
1. [Specific edit] — see commit [hash], file [path]
2. [Specific edit] — see commit [hash]
3. [Specific edit] — see commit [hash]

**What I'd do differently next time:**
[2–3 sentences on the methodological lesson, not the specific edit]
```

If the original instructor feedback recommended something you chose *not* to adopt, name that too — explaining your reasoning is more valuable to a reviewer than silent acceptance. Save to `docs/decisions/2026-05-22-ha-stage2-feedback-response.md` and commit.

---

## Three things worth specifically calling out as strong

These aren't generic compliments — they're things I want to name explicitly because they're hard to do well and you did them.

**1. The replenishment-system section is the highest-signal analytical paragraph in the cohort's Stage 5 work.** Specifically the part where you write: *"The system maintained a safety stock of 15–21 days depending on product type, running through three commitment stages: a fully flexible stage, a ±5 unit adjustment stage, and a final locked stage where suppliers were required to deliver exactly as ordered."* That's not financial commentary, that's *industry intelligence* — the kind of thing buy-side analysts would pay for, sourced from someone who can actually distinguish a bullwhip-effect cause from a procurement-software vendor's marketing claims. The bridge from this operational paragraph to "a group-level inventory turnover of 3.67x and 99.4 days reflects the complexity of 188 countries and multiple temperature-controlled categories, not an absence of discipline" is the move the rubric is asking for and most submissions don't make. Yours does.

**2. The retrospective's "Near-miss" column proposal is a structural template improvement, not just spec feedback.** From Part F: *"Add a 'Near-miss' column to the Section 1 verdict table — a cell for cases where the LLM got the right answer but the spec was ambiguous enough that a wrong answer was plausible."* This is the kind of meta-engineering observation the assignment is designed to elicit and almost no submissions get to. Whether or not the template ever changes, the thinking behind that proposal — "a 'Clear' verdict and a 'Clear-but-lucky' verdict look identical and the distinction matters" — is the disposition of someone who's going to be useful in any AI-quant role they take.

**3. The two correction notes (Du Pont ROE 22.1% → 22.2%; Current Ratio 0.79x → 0.786x) handled with explicit gap-attribution to the spec, not blame on the LLM.** Most students either silently corrected or attributed errors to "AI got it wrong." Your retrospective Gap 1 says: *"This is a spec gap documented in the retrospective"* and proposes the exact fix language. That's the disposition the course is trying to teach — the spec is the artifact you control, the LLM is the executor.

---

## One direction worth taking next (optional, post-grade)

If you want one piece of additional work that builds on the analysis you've already done — not as a fix for Stage 5, but as a portfolio-building extension — write a **case study** at `analysis/case-studies/2026-05-22-replenishment-as-cash-flow-engine.md` that turns Section "Efficiency" of your final analysis into a standalone 2-page piece. Take the replenishment-system paragraph, the 90-day supplier terms paragraph, and the negative NWC arithmetic, and lift them into a self-contained narrative aimed at a reader who hasn't seen the rest of the analysis. Frame: *"How operational discipline becomes a balance-sheet feature."*

Why this matters as a portfolio piece: someone looking at your GitHub will not read the full Stage 5 analysis cold. They'll skim. A standalone case study that demonstrates you can read both an income statement *and* a procurement system is the artifact that gets shared in a LinkedIn post or an internal mobility application. It would take 2–3 hours to extract from work you've already done, and it would be the single most distinctive document in your portfolio at the end of this course.

---

## Looking forward

The Stage 5 deadline is the formal endpoint, but the post-deadline revision sweep is open. The three packaging fixes above — recommendation subheadings, the "Company & Data Summary" header, and the Stage 2 response memo — are mechanical edits to existing files, no new analysis required. Submitting them before the sweep is a low-effort, score-positive move. The case study is genuinely optional and lives on your timeline.

The content of what you submitted is already at the level the course is trying to reach. The packaging fixes are about making the rubric scanner see what's already there.

---

*This review is feedback-only — no scores included.* Score numbers live in the internal grade report and the instructor's email; this file is intended as colleague-level input on your work, not as a graded artifact.
