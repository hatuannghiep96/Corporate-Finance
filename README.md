# Corporate Finance Portfolio — Ha Tuan Nghiep

**Course:** BUS-629 International Corporate Finance — VEMBA 33, Shidler College of Business, University of Hawaiʻi at Mānoa
**Company analyzed:** Nestlé S.A. (NESN, SIX Swiss Exchange)
**Reporting standard:** IFRS · Currency: CHF · Fiscal year end: December 31

---

## What you will find here

This repository is the complete project portfolio for a corporate finance ratio analysis of Nestlé S.A. across FY2024–FY2025. It covers the full analytical lifecycle: company selection, financial model population, technical specification, LLM-assisted analysis, manual verification, strategic evaluation, and programmatic conformance checking. Each stage builds on the previous one — the spec drives the LLM output, the LLM output is verified against the financial model, and the final analysis reflects both the numbers and the judgment of an analyst who spent 14 months inside Nestlé's operations.

The repo is organized so that a manager, auditor, or peer can navigate it in under five minutes without opening every file. Start with this README, then follow the stage links below.

---

## Project status

| Stage | Description | Weight | Status | Key commit |
|---|---|---|---|---|
| Stage 0 | Repo setup — bio, resume, structure, commit conventions | 5% | ✅ 98.22% | `d025fc1` |
| Stage 1 | Excel performance ratios template | 20% | ✅ 100% | `2c9da9e` |
| Stage 2 | Company selection memo — Nestlé S.A. | 10% | ✅ 97.11% | `7b64d30` |
| Stage 3 | Financial model — FY2024 + FY2025 IFRS financials | 30% | ✅ 99% | `a41d54b` |
| Stage 4 | Technical specification for LLM analysis | 20% | ✅ 100% | `d5bfdd8` |
| Stage 5 | LLM analysis, verification, retrospective, repo polish | 15% | ✅ Submitted | `de1c4e5` |

---

## Portfolio extensions (post-grade)

Three artifacts built beyond the course requirements, applying the instructor's suggested directions:

| Artifact | Location | What it demonstrates |
|---|---|---|
| Parameterized spec template | `docs/templates/spec-template.md` | Reusable IFRS ratio analysis framework — swap `nestle-inputs.yaml` for any company |
| Nestlé inputs file | `docs/specs/2026-05-20-ha-nestle-inputs.yaml` | Clean data/logic separation; Unilever-runnable by replacing this file |
| Python ratio harness | `analysis/ratio_harness.py` | Programmatic conformance checker — reads xlsx, recomputes 23 ratios, compares to LLM output, reports PASS/FAIL |
| Replenishment case study | `analysis/case-studies/2026-05-22-replenishment-as-cash-flow-engine.md` | Standalone industry intelligence: how operational discipline becomes a balance-sheet feature |
| AI tooling reflection | `docs/decisions/2026-05-20-ha-ai-tooling-experiment.md` | Honest reflection on AI-assisted analysis applied to SME context |

**Harness result:** 23/23 ratios PASS at 100% — LLM output arithmetically confirmed against Stage 3 workbook. Du Pont ROE rounding gap (22.2483% full precision vs 22.1228% early-rounded) caught and quantified automatically.

---

## Repo structure

```
Corporate-Finance/
├── README.md                          ← You are here
├── bio.md                             ← Professional bio (190 words)
├── resume.md                          ← Penn-style resume
├── CLAUDE.md                          ← Claude Code conventions
├── LICENSE                            ← MIT license
├── .gitignore                         ← Excludes Excel temp files
│
├── data/                              ← Source financial statements (xlsx)
│   ├── 2024_income-statement_nestle.xlsx
│   ├── 2024_balance-sheet_nestle.xlsx
│   ├── 2024_cash-flow-statement_nestle.xlsx
│   ├── 2025_income-statement_nestle.xlsx
│   ├── 2025_balance-sheet_nestle.xlsx
│   └── 2025_cash-flow-statement_nestle.xlsx
│
├── models/
│   ├── templates/                     ← Unmodified Stage 1 template
│   │   ├── performance-ratios-template.xlsx
│   │   └── spec-template.md           ← Parameterized spec (Direction 4)
│   └── builds/                        ← Stage 3 populated workbook
│       └── 2026-05-20-ha-nestle-financials.xlsx
│
├── docs/
│   ├── decisions/                     ← Stage 2 memo + feedback responses
│   ├── specs/                         ← Stage 4 spec + Nestlé inputs yaml
│   ├── feedback/                      ← Instructor PR review files
│   ├── templates/                     ← Parameterized spec template
│   └── plans/                         ← Planning documents
│
├── analysis/
│   ├── ratio_harness.py               ← Python conformance checker (Direction 1)
│   ├── case-studies/                  ← Standalone portfolio pieces
│   │   └── 2026-05-22-replenishment-as-cash-flow-engine.md
│   └── validation/                    ← Stage 5 manual verification table
│       └── 2026-05-20-ha-nestle-stage5-verification.md
│
└── deliverables/
    ├── prompt-log.md                  ← All AI sessions logged (Stages 0–5)
    ├── 2026-05-20-ha-nestle-llm-raw.md          ← Stage 5 raw LLM output
    ├── 2026-05-20-ha-nestle-final-analysis.md   ← Stage 5 evaluated analysis
    └── 2026-05-20-ha-nestle-spec-retrospective.md ← Stage 5 spec retrospective
```

---

## Running the ratio harness

```bash
# Install dependency
pip install openpyxl --break-system-packages

# Run from repo root
python analysis/ratio_harness.py
```

Output: PASS/FAIL for all 23 ratios, Du Pont rounding gap analysis, balance sheet validation. To run for a different company, update `WORKBOOK_PATH` and `ANALYSIS_PATH` in the config section and swap the analyst assumptions.

---

## About the analyst

Ha Tuan Nghiep is Operations Manager at Tan Hung Firm (Ho Chi Minh City, Vietnam) and an MBA candidate at the Shidler College of Business, University of Hawaiʻi at Mānoa (VEMBA 33). Prior to his MBA, he worked at Nestlé Vietnam as a Supply Chain Management Trainee (June 2022–August 2023), managing the coffee product line and contributing to 10 cross-border export-import projects. He holds a Bachelor of Business in Logistics & Supply Chain Management with Distinction (GPA 3.3/4.0) from RMIT University Vietnam and has 4 peer-reviewed publications (2 Q1, 1 Q2, 1 A-rank).

→ [bio.md](bio.md) · [resume.md](resume.md) · [LinkedIn](https://www.linkedin.com/in/ha-tuan-nghiep)
