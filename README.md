# Corporate Finance Portfolio — Ha Tuan Nghiep

**Course:** BUS-629 International Corporate Finance — VEMBA 33, Shidler College of Business, University of Hawaiʻi at Mānoa
**Company analyzed:** Nestlé S.A. (NESN, SIX Swiss Exchange)
**Peer comparison:** Unilever PLC (ULVR, LSE)
**Reporting standard:** IFRS · Currency: CHF (Nestlé) / EUR (Unilever) · Fiscal year end: December 31

---

## What you will find here

This repository is the complete project portfolio for a corporate finance ratio analysis of Nestlé S.A. across FY2024–FY2025, extended with a programmatic peer comparison against Unilever PLC. It covers the full analytical lifecycle: company selection, financial model population, technical specification, LLM-assisted analysis, manual verification, strategic evaluation, and programmatic conformance checking. Each stage builds on the previous one — the spec drives the LLM output, the LLM output is verified against the financial model, and the final analysis reflects both the numbers and the judgment of an analyst who spent 14 months inside Nestlé's operations.

The repo is organized so that a manager, auditor, or peer can navigate it in under five minutes without opening every file.

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

Four artifacts built beyond the course requirements, applying the instructor's suggested directions from Stage 4 feedback:

| Artifact | Location | What it demonstrates |
|---|---|---|
| Parameterized spec template | `docs/templates/spec-template.md` | Reusable IFRS ratio analysis framework — swap inputs yaml for any company. Includes §12 Monte Carlo sensitivity specification. |
| Nestlé inputs file | `docs/specs/2026-05-20-ha-nestle-inputs.yaml` | Clean data/logic separation; all 45+ named-range values with source documentation |
| Unilever inputs file | `docs/specs/2026-05-22-ha-unilever-inputs.yaml` | Direction 4 validation — extracted from FY2025 audited PDF; proves template is company-agnostic |
| Python ratio harness | `analysis/ratio_harness.py` | Programmatic conformance checker — reads xlsx, recomputes 23 ratios, compares to LLM output, reports PASS/FAIL. Monte Carlo EVA sensitivity via `--sensitivity` flag. |
| FMCG peer comparison | `analysis/peer_comparison.py` | Reads both yaml files, computes all ratios side by side, produces analyst commentary on 6 key divergences |
| Replenishment case study | `analysis/case-studies/2026-05-22-replenishment-as-cash-flow-engine.md` | Standalone industry intelligence: how operational discipline becomes a balance-sheet feature |
| Operational context annex | `analysis/operational-context.md` | Reusable insider context from Nestlé Vietnam tenure — injectable into future LLM runs |
| AI tooling reflection | `docs/decisions/2026-05-20-ha-ai-tooling-experiment.md` | Honest reflection connecting AI-assisted analysis to SME management at Tan Hung Firm |

---

## Key results

**Ratio harness:** 23/23 PASS at 100% — LLM output arithmetically confirmed against Stage 3 workbook. Du Pont ROE rounding gap (22.2483% full precision vs 22.1228% early-rounded) caught and quantified automatically.

**Monte Carlo (5,000 trials):** P(EVA > 0) = 100%. Break-even WACC = 11.78% (278bps headroom). WACC dominates EVA uncertainty by 32× over tax rate.

**FMCG peer comparison — Nestlé vs Unilever FY2025:**

| Ratio | Nestlé (CHF) | Unilever (EUR) | Winner |
|---|---|---|---|
| ROC (avg) | 12.4% | 14.9% | Unilever |
| ROE (avg) | 25.9% | 32.0% | Unilever |
| EVA headroom above WACC | 3.4pp | 5.9pp | Unilever |
| Break-even WACC headroom | 2.8pp | 5.2pp | Unilever |
| Asset turnover | 0.64x | 0.63x | Tied |
| Days in inventory | 99.4 days | 70.5 days | Unilever |
| Debt ratio | 74.0% | 74.6% | Tied |
| Current ratio | 0.786x | 0.79x | Tied |
| TIE | 5.67x | 8.83x | Unilever |

**Direction 4 confirmed:** `spec-template.md` ran identically for both companies — only the inputs yaml changed.

---

## Running the tools

```bash
# Install dependencies
pip install openpyxl pyyaml --break-system-packages

# Ratio conformance harness (23 ratios, PASS/FAIL)
python analysis/ratio_harness.py

# Ratio harness + Monte Carlo EVA sensitivity (5,000 trials)
python analysis/ratio_harness.py --sensitivity

# FMCG peer comparison — Nestlé vs Unilever
python analysis/peer_comparison.py
```

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
│   ├── decisions/                     ← Stage 2 memo, feedback responses, AI tooling reflection
│   ├── specs/                         ← Stage 4 spec + Nestlé and Unilever inputs yaml
│   ├── feedback/                      ← Instructor PR review files (Stages 4 and 5)
│   ├── templates/                     ← Parameterized spec template (§12 Monte Carlo)
│   └── plans/                         ← Planning documents
│
├── analysis/
│   ├── ratio_harness.py               ← Conformance checker + Monte Carlo (Direction 1 + 3)
│   ├── peer_comparison.py             ← Nestlé vs Unilever side-by-side (Direction 4)
│   ├── operational-context.md         ← Nestlé Vietnam insider knowledge annex
│   ├── case-studies/
│   │   └── 2026-05-22-replenishment-as-cash-flow-engine.md
│   └── validation/
│       └── 2026-05-20-ha-nestle-stage5-verification.md
│
└── deliverables/
    ├── prompt-log.md                  ← All AI sessions logged (Stages 0–5 + extensions)
    ├── 2026-05-20-ha-nestle-llm-raw.md
    ├── 2026-05-20-ha-nestle-final-analysis.md
    └── 2026-05-20-ha-nestle-spec-retrospective.md
```

---

## About the analyst

Ha Tuan Nghiep is Operations Manager at Tan Hung Firm (Ho Chi Minh City, Vietnam) and an MBA candidate at the Shidler College of Business, University of Hawaiʻi at Mānoa (VEMBA 33). Prior to his MBA, he worked at Nestlé Vietnam as a Supply Chain Management Trainee (June 2022–August 2023), managing the coffee product line and contributing to 10 cross-border export-import projects between Vietnam and Japan. He holds a Bachelor of Business in Logistics & Supply Chain Management with Distinction (GPA 3.3/4.0) from RMIT University Vietnam and has 4 peer-reviewed publications (2 Q1, 1 Q2, 1 A-rank).

→ [bio.md](bio.md) · [resume.md](resume.md) · [LinkedIn](https://www.linkedin.com/in/ha-tuan-nghiep)
