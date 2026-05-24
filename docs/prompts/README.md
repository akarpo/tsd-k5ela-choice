# Prompts log

Chronological record of the user prompts that shaped this analysis. Each file
in this folder captures one prompt (or one tight cluster of prompts) and what
was produced in response.

This exists because the analysis is the *output* of a multi-day collaboration,
not a single one-shot generation. Anyone trying to extend or audit the work
can read these in order to see *why* a particular slide, dataset, or design
decision exists.

## Index (chronological)

| # | File | What the user asked for |
|---|---|---|
| 01 | [01-kickoff.md](01-kickoff.md) | Initial Troy curriculum-choice analysis: SEDA + peer districts + curriculum verdict |
| 02 | [02-education-scorecard.md](02-education-scorecard.md) | Identify curricula used by the 20 Education Scorecard "Districts on the Rise" |
| 03 | [03-executive-deck.md](03-executive-deck.md) | Build the executive summary PowerPoint |
| 04 | [04-steubenville-sustained-outperformers.md](04-steubenville-sustained-outperformers.md) | Include Steubenville + other sustained outperformers as a separate evidence layer |
| 05 | [05-mde-curriculum-comparison.md](05-mde-curriculum-comparison.md) | Add slides comparing districts that use MDE-list curricula |
| 06 | [06-comprehensive-50-district-seda.md](06-comprehensive-50-district-seda.md) | Refactor to use the full 50-district SEDA universe instead of the 28-district workbook |
| 07 | [07-seda-2025-update.md](07-seda-2025-update.md) | Switch to SEDA 2025.1 (2009-2025 coverage including post-COVID) |
| 08 | [08-subgroups-and-ecd.md](08-subgroups-and-ecd.md) | Add racial subgroups + ECD/non-ECD breakdowns |
| 09 | [09-deck-upgrade.md](09-deck-upgrade.md) | Full deck refactor — citations, appendix, references |
| 10 | [10-citations-and-appendix.md](10-citations-and-appendix.md) | Numbered citations with appendix reference slides |
| 11 | [11-pdf-export.md](11-pdf-export.md) | Generate a PDF version of the deck |
| 12 | [12-javascript-presentation.md](12-javascript-presentation.md) | Convert deck into a JS web presentation |
| 13 | [13-public-github-repo.md](13-public-github-repo.md) | Push to a public GitHub repo (`tsd-k5ela-choice`) for verifiability |
| 14 | [14-reproducibility.md](14-reproducibility.md) | Include scripts so a third party can reproduce every claim |
| 15 | [15-jargon-cleanup.md](15-jargon-cleanup.md) | Strip made-up jargon ("home compensation strained", etc.) |
| 16 | [16-cherrypicking-callout.md](16-cherrypicking-callout.md) | Flag that "4 of 4 districts gained" implied N=4 not N=49; expand to honest comprehensive view |
| 17 | [17-grade-level-hypothesis.md](17-grade-level-hypothesis.md) | Test the "BL helps for later grades" hypothesis |
| 18 | [18-three-pass-numerical-audit.md](18-three-pass-numerical-audit.md) | Three-pass numerical consistency audit; require every cited number to match source data |
| 19 | [19-tsd-swd-from-mischooldata.md](19-tsd-swd-from-mischooldata.md) | Pull Troy SWD M-STEP performance via the `tools-schooldata` scraper |
| 20 | [20-design-validation-feedback.md](20-design-validation-feedback.md) | Real design issues missed in earlier audit; introduce structured style/drift check |
| 21 | [21-versioning-and-local-paths.md](21-versioning-and-local-paths.md) | Strip `v4` from filenames and `/Users/Alex/...` from the deck; reference GitHub instead |
| 22 | [22-document-the-prompts.md](22-document-the-prompts.md) | Add `.md` files for prompts and tooling and push them to GitHub |

## Format

Each file follows the same structure:

```
# <slug>

**Date:** YYYY-MM-DD  
**Asked for:** <one sentence>

## Prompt(s) quoted
> ...

## What was produced
- artifact 1 (path)
- artifact 2 (path)

## Why this mattered
<one paragraph context>
```

If you read these in order, the deck's structure (and its surprises — the SWD
finding, the "0 of 50" answer, the SoR-doesn't-guarantee-recovery caveat) come
out as a thread rather than as a fait accompli.
