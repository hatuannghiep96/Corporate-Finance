# CLAUDE.md — Corporate Finance Portfolio
# BUS-629 International Corporate Finance | VEMBA 33
# Shidler College of Business, University of Hawaiʻi at Mānoa
# Student: Ha Tuan Nghiep | GitHub: hatuannghiep96

---

## What this repo is

This is a finance course portfolio repo — NOT a software project.
It contains memos, financial models, data, and analysis for BUS-629.
Do not treat it like a code project. There is no code to debug or test.

---

## Commit message rules (MANDATORY)

Every commit message must follow this format:
- Start with a VERB (Add, Fix, Update, Remove, Rename, Draft, Complete)
- Name the specific file or area changed
- Add the WHY if it is not obvious

GOOD examples:
- "Add Stage 2 company selection memo for Nestle SA"
- "Fix placeholder READMEs — add purpose and naming conventions"
- "Update BIO.md — correct Nestle job title and add H1 2023 award"
- "Add Nestle FY2024 financial statements to data/"

BAD examples (never use these):
- "update"
- "fix"
- "wip"
- "Update README.md"
- "changes"
- "fix typo"

---

## File naming conventions (MANDATORY)

Memos and docs:
YYYY-MM-DD-{lastname}-{company}-{slug}.md
Example: 2026-05-16-ha-nestle-selection.md

Excel models:
YYYY-MM-DD_stage#_description_v#.xlsx
Example: 2026-10-15_stage3_nestle-ratios-v1.xlsx

Validation reports:
YYYY-MM-DD_stage#_validation-report.md

All folder names must be LOWERCASE with hyphens, no spaces.

---

## Folder structure

Corporate-Finance/
├── README.md          # Bio (150-200 words, public facing)
├── BIO.md             # Extended bio
├── RESUME.md          # Penn-style resume
├── .gitignore         # Blocks Excel temp files and OS junk
├── docs/
│   ├── decisions/     # Stage 2 memos and decision documents
│   ├── specs/         # Stage 4 technical specifications
│   ├── plans/         # Project plans and timelines
│   └── templates/     # Course templates — never edit originals
├── models/
│   ├── templates/     # Instructor-provided Excel templates — never modify
│   └── builds/        # Populated working models (Stage 3+)
├── data/              # Source financial statements and data
├── analysis/
│   └── validation/    # Model validation and audit reports
└── deliverables/      # Final submission-ready outputs only
    └── prompt-log.md  # AI prompt log — update after every stage

---

## Company being analyzed

Nestlé S.A. (NESN, Swiss Exchange)
- Reporting standard: IFRS
- Reporting currency: CHF
- Fiscal year end: December 31
- Data source: nestle.com/investors/publications
- FY2023 and FY2024 financial statements

---

## Prompt log requirement

Every time AI is used to produce a deliverable, update:
deliverables/prompt-log.md

Each entry must include:
- Date and tool used
- Purpose of the prompt
- Full prompt given
- What AI produced
- Where AI fell short
- What the student corrected

---

## Stage status tracker

| Stage | Weight | Status | Notes |
|-------|--------|--------|-------|
| Stage 0 — Repo Setup | 5% | ✅ Complete (91%) | READMEs fixed per feedback |
| Stage 1 — Template | 20% | ✅ Complete | performance-ratios-template.xlsx uploaded |
| Stage 2 — Company Memo | 10% | ✅ Complete | Nestle SA selected, memo committed |
| Stage 3 — Financial Model | 30% | ⏳ Pending | Download FY2023/2024 statements first |
| Stage 4 — Specs | 20% | ⏳ Pending | |
| Stage 5 — Final | 15% | ⏳ Pending | |

---

## Important reminders

- NEVER commit a file called RESUME without .md extension
- NEVER modify files in models/templates/ — always copy to models/builds/ first
- NEVER commit Excel temp files (~$*.xlsx) — .gitignore handles this
- ALWAYS add a README.md to every new folder created
- ALWAYS check git log --oneline after pushing to verify commit messages
- Instructor GitHub handle: adamwstauffer (Write collaborator — already added)
