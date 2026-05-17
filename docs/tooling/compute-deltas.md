# `compute_deltas.py`

**Path:** `analysis/compute_deltas.py`
**Stage:** 2

## What it does

Computes the Pre→Post-COVID Δ for each (district, subgroup) pair on the SEDA
cs scale. The window definitions are:

- **Pre-COVID window:** mean of 2017, 2018, 2019.
- **Post-COVID window:** mean of 2022, 2023, 2024, 2025.
- **Δ = mean(post) − mean(pre)**, requires ≥2 non-null years in each window.

## Inputs

- `research/seda_2025_pooled.json` (from `extract_seda_subset.py`).

## Outputs

- Per-district per-subgroup Δ values used on slides 4, 6, 8, 9, 16, 17, 18.
- Distribution stats (median, rank) used in the tier-column slide (6) and the
  "X of 50" callouts.

## Why it exists

Every quantitative claim in the deck that reads "Troy declined X cs units"
or "District Y gained Y units" runs through this function. Centralizing it
in one script means the three-pass numerical audit only has one definition
of "Pre→Post Δ" to verify, not one per slide.

## Pitfalls

- **The 2-year minimum is load-bearing.** A district with only one Pre year
  and three Post years would otherwise post a noisy Δ that looks comparable
  to a district with full coverage. The minimum is intentional.
- **Subgroup small-N.** Hispanic at Troy is small-N — `delta()` returns
  the number, but the deck footnotes it (slide 4).
