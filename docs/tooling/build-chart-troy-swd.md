# `build_chart_troy_swd.py`

**Path:** `analysis/charts/build_chart_troy_swd.py` (working copy: `research/build_chart_troy_swd.py`).
**Stage:** 3

## What it does

Builds the chart on **slide 10** (the SWD slide added per
[prompt 19](../prompts/19-tsd-swd-from-mischooldata.md)).

3-panel layout, one panel per grade (G3, G4, G5). Each panel plots four
series across school years 2014-15 → 2024-25:

- Troy SWD (% Adv+Prof)
- Troy non-SWD
- Troy All
- Michigan state All (context line)

## Inputs

- `tools-mischooldata/examples/troy_swd_ela.csv` (from
  [`troy_swd_ela.py`](troy-swd-ela.md) in the `tools-mischooldata` repo).

## Outputs

- `research/charts/chart_swd_deck.png` (sized 11.5 × 3.7 in, embedded into slide 10).

## Why it exists

The SWD story is "the gap widened under Calkins." A single by-year line per
grade is the cleanest way to show that. The non-SWD line is the comparison
baseline; the State All line provides external context so a reader can see
whether Troy's drop is unique or part of a Michigan-wide pattern.

## Pitfalls

- **G5 2021-22 is suppressed** in the M-STEP data — the chart skips that
  point rather than connecting through it.
- The chart embeds at a non-default aspect ratio (11.5 × 3.7) because slide 10
  pairs it with a right-side panel. If you change those dimensions, recheck
  slide 10 in PowerPoint.
