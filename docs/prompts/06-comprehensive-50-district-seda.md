# 06 — Full 50-district SEDA universe

**Date:** 2026-04
**Asked for:** Stop cherry-picking — refactor to use the full 50-district SEDA universe, not the 28-district workbook subset I started with.

## Prompt(s) quoted
> Use the full 50 districts, not the 28 I had in the workbook. Cherry-picking the comparison set hides as much as it shows.

## What was produced
- `analysis/extract_seda_subset.py` widened to the 50 districts.
- All Pre→Post-COVID Δ and grade-level recomputes redone on the 50-district set.
- Several rankings shifted — Troy moved within the distribution, and "4 of 4" claims became "X of 50" claims.

## Why this mattered
The 28-district set was implicitly curated. Expanding to 50 made every distributional claim honest, and surfaced findings the smaller set hid — including the SoR-doesn't-guarantee-recovery counter-examples later cited on slide 17.
