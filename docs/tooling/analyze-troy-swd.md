# `analyze_troy_swd.py`

**Path:** `analysis/analyze_troy_swd.py` (working copy: `research/analyze_troy_swd.py`).
**Stage:** 4

## What it does

Reads the scraped Troy SWD CSV and computes the Pre→Post-COVID summary stats
that appear on **slide 10**:

- Per-grade SWD Δ (Pre window mean − Post window mean, in percentage points).
- Per-grade non-SWD Δ.
- Per-grade gap change (Δ_non-SWD − Δ_SWD).

Windows match SEDA conventions: Pre = 2017-18, 2018-19, 2019-20 school
years; Post = 2021-22, 2022-23, 2023-24, 2024-25.

## Inputs

- `tools-mischooldata/examples/troy_swd_ela.csv`.

## Outputs

- Stdout summary used to populate the slide 10 rect-table.
- Headline finding: G3 SWD Δ = −11.6 pp; non-SWD Δ = −6.7 pp; gap widened by +5.0 pp.

## Why it exists

The chart alone shows the trend; the deck needs the *number*. Putting the
arithmetic in a script (not in the build_deck source) means the three-pass
audit can re-run it and verify the cited number against the CSV directly.

## Pitfalls

- **M-STEP percent-proficient is not on the SEDA cs scale.** Don't quote
  these Δ values in cs-scale units — they're percentage points. The deck
  labels them as such.
- **Small-N years** (where the SWD cell has <30 students) are not separately
  flagged here; verify against the scraper's `swd_n` column before quoting.
