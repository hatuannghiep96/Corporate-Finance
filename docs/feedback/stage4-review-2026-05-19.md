# Stage 4 review — 2026-05-19

Reviewing the Stage 4 spec at `docs/specs/2026-05-20-ha-nestle-spec.md`

## Section coverage

| Section | Present | Word count |
|---|---|---|
| 1. Scope & Objective | ✓ | 132 |
| 2. Model Architecture | ✓ | 184 |
| 3. Data Inputs | ✓ | 446 |
| 4. Named Range Conventions | ✓ | 139 |
| 5. Derived Inputs | ✓ | 220 |
| 6. Ratio Definitions & Formulas | ✓ | 169 |
| 7. Validation Rules | ✓ | 413 |
| 8. Analysis Requirements (Part B) | ✓ | 154 |
| 9. Du Pont Decomposition (Part B) | ✓ | 218 |
| 10. Strategic Recommendations (Part B) | ✓ | 312 |
| 11. Output Format (Part B) | ✓ | 310 |

## Observations

- Spec length: **2491 words** (brief targets 3–5 pages, ~1,500–2,500 words — right at the top of the window).
- Named-range notation usage: **314 hit(s)** — cohort-leading density across `BAL_*`, `INC_*`, `CASH_*`, `RATIO_*`, `startYear_*`, `currentYear_*`, `avg_*`.
- §5 Ratio Definitions: all six categories present — Performance (3 ratios), Profitability (6), Efficiency (7), Leverage (3), Liquidity (3), Du Pont (4 components + 2 final ratios).
- §6 Validation: 6 rules including a Du Pont ROE time-mismatch caveat and a structural-NWC-is-not-an-error note.
- §9 Strategic Recommendations: 5 candidate recs with explicit "Ratio X → indicates Y → action → primary risk" structural template, tied to Nestlé management KPIs (ROIC 14.1%, net debt/EBITDA 2.90x target range).
- Prompt log (in `deliverables/prompt-log.md` on your repo): **1407 words** with 3 strong HIL signals.

### Kindly-worded suggestions for improvement

**Stage 4 rubric notes**

- Strong submission across all four criteria. A few specific things to call out as positive signal:
  - **Cohort-leading named-range density.** 314 hits across the spec is the most in the cohort — every formula and data input is anchored to a named range, which means your Stage 5 LLM will have zero ambiguity about which cell holds which value. This is exactly the discipline the spec rubric is rewarding.
  - **§6 Rule 4 — Du Pont ROE time-mismatch caveat.** Recognizing at the spec stage that Du Pont ROE won't exactly equal direct ROE (because leverage uses current-year assets while turnover uses prior-year assets) is sophisticated. Most students surface this as a Stage 5 surprise.
  - **§6 Rule 6 — Structural-negative-NWC note.** Calling out explicitly that Nestlé's negative NWC is structurally normal (supplier-terms-driven, not a liquidity problem) pre-empts a likely Stage 5 LLM false-positive. The LLM would otherwise flag (8,725) as a red-line liquidity issue. This kind of business-context caveat is what separates a spec from a checklist.
  - **§7 cross-references to management KPIs.** Tying your benchmarks to Nestlé's stated ROIC (14.1%) and net debt/EBITDA target (2.90x) rather than abstract textbook thresholds will keep the Stage 5 analysis grounded in what actually matters to a Nestlé reviewer.
  - **§9 Recommendation framework.** The "Ratio X shows Y → indicates Z → Recommendation: [action] → Primary risk: [trade-off]" template is a clean constraint for the Stage 5 LLM and will produce more uniform, comparable recommendations.
- One small structural note for future specs: the canonical template carries "Named Range Conventions" as its own §4 — you folded those conventions into §2 (color coding) and §3 (inline column headers), which is fine because the conventions are clearly enforced (314 hits). If you want the spec to be even more skim-able for a reviewer, breaking out a short standalone Naming Conventions section (prefix glossary: `BAL_*`, `INC_*`, etc.) would make the convention discoverable at a glance.

**Looking ahead to Stage 5**

- **Stage 5 — LLM analysis + manual verification.** Run your Stage 4 spec through the LLM of your choice, then verify at least five of its ratio outputs against the workbook by hand. Given how explicit your §3 inputs and §5 formulas are, the LLM output should be reproducible — and the verification step is where you catch any drift between the spec's named-range references and the workbook's actual cell formulas.
- The polish rubric grades how cleanly the prior four stages tie together as a single deliverable, so revisit your earlier files with fresh eyes when you reach Stage 5.


*This review is feedback-only — no scores included.* Score numbers live in the internal grade report and the instructor's email; this file is intended for review against your repo state.
