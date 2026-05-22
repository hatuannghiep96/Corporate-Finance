---
purpose: "Response to Stage 2 instructor feedback — documents changes made, reasoning, and methodological lessons"
author: Ha Tuan Nghiep
date: 2026-05-22
courses: [BUS-629]
---

# Response to Stage 2 Instructor Feedback

**Author:** Ha Tuan Nghiep
**Date:** 2026-05-22
**Feedback received:** Stage 2 instructor PR review (PR #1, merged 2026-05-20) — see `docs/feedback/stage4-review-2026-05-19.md` for full review notes.
**Original memo:** `docs/decisions/2026-05-16-ha-nestle-selection.md`

---

## Summary of feedback received

The Stage 2 memo scored 97.11% (4.37 / 4.5). The instructor's PR feedback identified one structural suggestion: add a standalone Named Range Conventions section (§4) to the Stage 4 spec, with a prefix glossary making `BAL_*`, `INC_*`, `CASH_*`, `RATIO_*`, `startYear_*`, `currentYear_*`, and `avg_*` discoverable at a glance. The Stage 2 memo itself received no substantive corrections — the feedback was forward-looking toward Stage 4.

Prior to receiving the PR, I had already identified and self-corrected three issues in the memo during the Stage 3 to Stage 5 workflow:

---

## Changes made

**Change 1 — Fiscal year references updated (FY2023/FY2024 → FY2024/FY2025)**
- **What changed:** The original memo referenced FY2023 and FY2024 as the analytical period. After confirming Nestlé had published FY2025 consolidated statements, all fiscal year references were updated to FY2024 (prior year) and FY2025 (current year).
- **Commit:** `d9b4028` — `docs/decisions/2026-05-16-ha-nestle-selection.md`
- **Why:** The Stage 3 financial model uses FY2025 as the current year. Consistency between the company selection memo and the financial model is required for the Stage 5 rubric to read the project as a coherent whole.

**Change 2 — Buyback figure corrected (CHF 4.5B → CHF 4.7B, labelled FY2024)**
- **What changed:** The memo stated "CHF 4.5 billion in buybacks" without a year label. The correct FY2024 figure is CHF 4.7B. The label "(FY2024)" was added to make clear this refers to the prior year — FY2025 buybacks were only CHF 213M (program completed).
- **Commit:** `d8eb87e` — `docs/decisions/2026-05-16-ha-nestle-selection.md`
- **Why:** A reader comparing the memo to the financial model would see a significant discrepancy (CHF 4.7B vs CHF 213M) without the year label. The correction prevents a false impression of inconsistency.

**Change 3 — Memo trimmed from 1,039 words to ~550 words**
- **What changed:** The original draft was approximately 1,039 words — nearly double the instructor's 400–600 word target. Repetitive sections were removed and the prose was tightened to ~550 words without removing any graded element.
- **Commit:** `d9b4028` — `docs/decisions/2026-05-16-ha-nestle-selection.md`
- **Why:** The instructor's rubric note stated "a senior analyst memo is short." A 1,039-word memo fails that standard regardless of content quality.

---

## What I chose not to change

The memo's three directional hypotheses (leverage deterioration, margin pressure, working capital improvement) were retained unchanged. All three were directionally confirmed by the Stage 3 financial model and the Stage 5 ratio analysis — making them the strongest structural element of the memo rather than a correction target.

---

## Methodological lesson

The most important lesson from the Stage 2 revision cycle was about the relationship between the memo and the financial model: the memo is not just a company selection document — it is the hypothesis register that the Stage 5 analysis either confirms or challenges. Writing the hypotheses in falsifiable form ("I expect X because Y") gave the final analysis a built-in structure for evaluation. Next time I would write the memo with explicit named-range references (even as placeholders) so the hypothesis-to-ratio mapping is machine-readable from Stage 2 onward, not retrofitted at Stage 5.
