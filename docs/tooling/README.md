# Tooling

These are the scripts that produce every number, chart, and slide in the deck.
A third party should be able to clone the repo, run them in order, and reproduce
the artifacts.

## Run order

1. **`extract_seda_subset.py`** — slice the 50-district subset out of raw SEDA 2025.1.
2. **`compute_deltas.py`** — compute Pre→Post-COVID Δ (cs scale) at All + subgroup level.
3. **Chart builders** (parallel, independent):
   - `build_chart13.py` — subgroup Δ across Troy + recovery cohort (slide 16).
   - `build_chart_troy_swd.py` — Troy SWD vs non-SWD vs State by grade (slide 10).
   - (other chart scripts live next to these.)
4. **`analyze_troy_swd.py`** — Pre/Post Δ summary stats for the SWD slide.
5. **`build_deck.py`** — assembles the .pptx from the chart PNGs + the computed numbers.
6. **`check_style_drift.py`** — static drift check; run after every edit to `build_deck.py`.

The Troy SWD M-STEP data itself comes from a scraper in a separate repo:
**`tools-schooldata/examples/troy_swd_ela.py`** — that script writes
`troy_swd_ela.csv` (bundled locally at `data/troy_swd_ela.csv`) which
`analyze_troy_swd.py` and `build_chart_troy_swd.py` both consume.

## Per-script docs

| Script | What it does |
|---|---|
| [extract-seda-subset.md](extract-seda-subset.md) | Pulls the 50-district slice from SEDA 2025.1. |
| [compute-deltas.md](compute-deltas.md) | Computes Pre→Post-COVID Δ at All + subgroup level. |
| [build-chart13.md](build-chart13.md) | Builds slide 16's 5-district × 7-subgroup bar chart. |
| [build-chart-troy-swd.md](build-chart-troy-swd.md) | Builds slide 10's Troy SWD by-grade panel chart. |
| [analyze-troy-swd.md](analyze-troy-swd.md) | Summary stats on Troy SWD M-STEP from the scraped CSV. |
| [check-style-drift.md](check-style-drift.md) | Static drift check against the style guide. |
| [troy-swd-ela.md](troy-swd-ela.md) | The `tools-schooldata` scraper for Troy SWD M-STEP. |
