# `build_chart13.py`

**Path:** `analysis/charts/build_chart13.py` (also kept at `research/build_chart13.py` in working copy).
**Stage:** 3 (chart builders, run after deltas exist).

## What it does

Builds the chart on **slide 16**: subgroup Pre→Post-COVID Δ for Troy SD vs the
four-district recovery cohort.

- **X axis:** 7 subgroups — All, Asian, White, Black, Hispanic, ECD, Not-ECD.
- **Y axis:** Pre→Post Δ on the SEDA cs scale (grade-level units).
- **5 series, 5 distinct hues** (mandatory — see `STYLE.md` contrast rule):

| District | Color | Role |
|---|---|---|
| Troy SD | `#C8302F` (ACCENT_RED) | Protagonist district |
| Spring Branch ISD | `#1F7A3D` (ACCENT_GREEN) | Biggest gainer |
| Palo Alto USD | `#1F3A5F` (TROY_BLUE) | Calkins-exit peer |
| West Baton Rouge | `#B7791F` (ACCENT_ORANGE) | Wit & Wisdom |
| Johnson City TN | `#5E2D8C` (purple) | 5th-series differentiator |

## Inputs

- `research/seda_2025_pooled.json`.

## Outputs

- `research/charts/chart13_post_covid_recovery.png` (200 DPI, embedded into slide 16).

## Why it exists — and why the palette is rigid

An earlier version used overlapping blues/greens that the user couldn't
distinguish (see [prompt 20](../prompts/20-design-validation-feedback.md)).
The replacement palette is intentionally a 5-hue maximally-distinct set, and
the colors are aligned with the deck's semantic palette so a reader who has
internalized "red = Troy" on one chart sees the same coding here.

## Pitfalls

- Adding a 6th district will break the contrast guarantee. If you need 6+
  series, switch to small multiples instead of a single grouped bar chart.
- `delta()` returns None for small-N; the chart currently plots None as 0.
  If you change that, update the chart caption.
