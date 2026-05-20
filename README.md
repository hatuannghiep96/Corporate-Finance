# Corporate Finance Portfolio — Ha Tuan Nghiep

**Course:** BUS-629 International Corporate Finance — VEMBA 33, Shidler College of Business, University of Hawaiʻi at Mānoa
**Company analyzed:** Nestlé S.A. (NESN, SIX Swiss Exchange)
**Reporting standard:** IFRS · Currency: CHF · Fiscal year end: December 31

---

## What you will find here

This repository is the complete project portfolio for a corporate finance ratio analysis of Nestlé S.A. across FY2024–FY2025. It covers the full analytical lifecycle: company selection, financial model population, technical specification, LLM-assisted analysis, manual verification, and strategic evaluation. Each stage builds on the previous one — the spec drives the LLM output, the LLM output is verified against the financial model, and the final analysis reflects both the numbers and the judgment of an analyst who spent 14 months inside Nestlé's operations.

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
│   └── builds/                        ← Stage 3 populated workbook
│       └── 2026-05-20-ha-nestle-financials.xlsx
│
├── docs/
│   ├── decisions/                     ← Stage 2 company selection memo
│   ├── specs/                         ← Stage 4 technical specification
│   ├── feedback/                      ← Instructor PR review files
│   └── plans/                         ← Planning documents
│
├── analysis/
│   └── validation/                    ← Stage 5 manual verification table
│
└── deliverables/
    ├── prompt-log.md                  ← All AI sessions logged (Stages 0–5)
    ├── 2026-05-20-ha-nestle-llm-raw.md          ← Stage 5 raw LLM output
    ├── 2026-05-20-ha-nestle-final-analysis.md   ← Stage 5 evaluated analysis
    └── 2026-05-20-ha-nestle-spec-retrospective.md ← Stage 5 spec retrospective
```

---

## About the analyst

Ha Tuan Nghiep is Operations Manager at Tan Hung Firm (Ho Chi Minh City, Vietnam) and an MBA candidate at the Shidler College of Business, University of Hawaiʻi at Mānoa (VEMBA 33). Prior to his MBA, he worked at Nestlé Vietnam as a Supply Chain Management Trainee (June 2022–August 2023), managing the coffee product line and contributing to 10 cross-border export-import projects. He holds a Bachelor of Business in Logistics & Supply Chain Management with Distinction (GPA 3.3/4.0) from RMIT University Vietnam and has 4 peer-reviewed publications (2 Q1, 1 Q2, 1 A-rank).

→ [bio.md](bio.md) · [resume.md](resume.md) · [LinkedIn](https://www.linkedin.com/in/ha-tuan-nghiep)
