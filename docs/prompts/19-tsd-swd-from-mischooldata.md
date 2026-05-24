# 19 — Troy SWD performance via tools-schooldata

[Note: `tools-schooldata` was renamed to `tools-schooldata` on 2026-05-24 to match the GitHub repo name.]

**Date:** 2026-05
**Asked for:** Use the user's `tools-schooldata` scraper to pull Troy's Students with Disabilities (SWD) M-STEP ELA performance over the curriculum-implementation window, find what the data says, and integrate into the deck.

## Prompt(s) quoted
> I want you to use a tool in my repo "tools-schooldata" to calculate TSD SPD ELA performance over this period as well. Let me know what you find and then we can then figure out how to incorporate this as part of the analysis.

(Follow-up clarification: SWD = Students With Disabilities.)

## What was produced
- `examples/troy_swd_ela.py` in `tools-schooldata` — scrapes Troy SWD M-STEP %Adv+Prof for G3–G5, 2014-15 through 2024-25.
- `examples/troy_swd_ela.csv` — 26 rows (10 years × 3 grades, one G5 2021-22 suppression).
- `research/analyze_troy_swd.py` — Pre/Post-COVID Δ summary (G3 SWD Δ = −11.6 pp; non-SWD Δ = −6.7 pp; gap widened by +5.0 pp).
- `research/build_chart_troy_swd.py` — 3-panel by-grade chart for the new slide.
- New slide 10 in the deck (SWD subgroup), with a 4-column rect-table and blue band callout.

## Why this mattered
SWD is a high-visibility subgroup with statutory protections. A K-5 ELA recommendation that doesn't say anything about how Troy's most vulnerable readers fared during the Calkins era is incomplete — and exposes the analysis to a "you missed the kids who needed help most" rebuttal. The data showed the gap *widened* under Calkins, which is now its own slide with its own evidence trail.
