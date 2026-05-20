---
purpose: "Reflection on AI-assisted financial analysis workflow — what worked, what didn't, and applicability to real-world SME management"
author: Ha Tuan Nghiep
date: 2026-05-20
courses: [BUS-629]
---

# AI Tooling Experiment — Reflection Memo

**Author:** Ha Tuan Nghiep
**Date:** 2026-05-20
**Context:** BUS-629 Stage 5 — post-project reflection on AI-assisted financial analysis workflow

---

## What I tried

Over the course of this project I used Claude (Sonnet 4.6) across two interfaces — claude.ai for thinking, drafting, and analysis generation, and Claude Code in the terminal for all git operations, file management, and repo execution. The workflow followed a spec-driven design pattern: write a precise technical specification, feed it to the LLM, verify the output by hand, and annotate corrections with explicit reasoning. No prior coding or GitHub experience was assumed at the start.

## What it did well

The most striking outcome was not the ratio analysis itself — it was the accessibility. I came into this project with no GitHub background and no coding knowledge. Within a single session, Claude Code was handling git rebases, renaming commits across 18-commit histories, and pushing verified financial workbooks to a public portfolio repo. The LLM's ratio output was arithmetically reliable across 25+ computations, with zero material errors and only two rounding artifacts caught in manual verification. For structured, well-specified tasks, the accuracy is production-grade.

The second standout was the spec-driven workflow itself. Writing a precise specification before running the analysis forced me to think through every formula, every named range, and every validation rule before touching a number. That discipline — specify first, execute second, verify third — is directly transferable to managing a business, not just an MBA assignment.

## What it got wrong and where I had to intervene

Two rounding corrections were needed in the Du Pont decomposition — the LLM rounded intermediate components before multiplying, compounding error across four steps. Both were caught by manual verification. More importantly, the LLM's strategic recommendations were directionally correct but initially lacked specific numeric targets. The "so what?" — the executive judgment about which way Nestlé's inflection point should resolve — required a human with operational context to write credibly.

## Whether I would use it on a real engagement

Yes — and the application I have in mind is closer to home than Nestlé. Tan Hung Firm, my family's fermented bean curd manufacturer in Ho Chi Minh City, currently runs on experience and cash flow intuition with no formal data collection or financial ratio tracking. The same workflow I applied to a CHF 89B FMCG giant is applicable at any scale: build a structured data collection system, define the ratios that matter for a Vietnamese SME (gross margin by product line, inventory turnover, receivables days from distributors), write a spec, run the analysis, verify the outputs, and act on the recommendations.

The gap between what Nestlé does — a demand-sensing replenishment system eliminating bullwhip effects across 188 countries — and what Tan Hung does today is not a technology gap. It is a data structure gap. AI tools accelerate the analysis layer, but they cannot run on air. The first step for Tan Hung is not Claude — it is building the records that Claude would eventually read.

That is the most valuable thing this project taught me: the discipline of structured data and precise specification is the prerequisite for everything else, at any scale.
