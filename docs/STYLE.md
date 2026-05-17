# Deck style guide

The deck has one source of truth for visual style: this document. The build
script (`analysis/build_deck.py`) and every chart-generation script in
`analysis/charts/` must use the same palette + typographic rules. If you add
a new chart or slide, check it against this guide and against the drift-check
script (`analysis/check_style_drift.py`) before committing.

## Color palette (single source of truth)

Every accent/semantic color used in the deck and every chart MUST come from
this palette. Do not introduce new colors per slide.

| Role | Hex | When to use |
|---|---|---|
| `TROY_BLUE`    | `#1F3A5F` | Deck primary; title bars; neutral headers; "Troy" line on Troy-only charts |
| `ACCENT_RED`   | `#C8302F` | Decline / Troy on comparison charts / urgent alerts; bars where Troy is the protagonist |
| `ACCENT_GREEN` | `#1F7A3D` | Gain / recovery / strong outperformers (e.g. Spring Branch) |
| `ACCENT_ORANGE`| `#B7791F` | Moderate / Wit & Wisdom districts (West Baton Rouge) |
| `ACCENT_PURPLE`| `#5E2D8C` | Reserved for a 5th-series differentiator (e.g. Johnson City TN) |
| `LIGHT_GREEN`  | `#E8F5EE` | Background tint behind ACCENT_GREEN content |
| `LIGHT_ORANGE` | `#FFF4E0` | Background tint behind ACCENT_ORANGE content |
| `LIGHT_RED`    | `#FBE7E6` | Background tint behind ACCENT_RED content |
| `GRAY_LIGHT`   | `#F2F4F7` | Neutral panel background |
| `GRAY_DARK`    | `#333333` | Body text |
| `GRAY_MID`     | `#777777` | Captions, secondary labels, axis tick labels |
| `WHITE`        | `#FFFFFF` | Header-bar text on colored bars |

**Chart-specific contrast rule:** when 4+ series are plotted on one chart,
they must use distinct hues (red/green/blue/orange/purple — *not* two greens
or two blues). If you can't tell two series apart in a screenshot at 200%
zoom, fix the chart, don't fix the legend.

## Typography

- All deck text uses the system default font, EXCEPT numeric/tabular data which
  uses `Consolas` for alignment.
- **Do not hand-pad monospace strings with spaces to fake columns.** PowerPoint
  silently falls back to a proportional font on some machines, and Unicode
  superscript characters have different widths than ASCII. Use real positioned
  text boxes (a rect-table) for any 2+ column tabular layout. See
  `render_tier_column` (slide 6) and the slide 8 / slide 9 rect-tables for the
  pattern.

## Geometry rules

- Slide canvas: 13.333 in × 7.5 in (16:9).
- Footer band sits at y=7.15; no slide content may extend below y=7.05.
- Title bar reserves y=0 → y=0.95.
- Default content area: y=1.0 → y=7.0  (6.0 in tall).
- Bottom callouts: y=6.78 → y=7.05 (≤ 0.3 in tall).
- Box outline + inner text padding: 0.15 in on all sides.
- Inner text containers (text frames) MUST be sized to fit their content.
  Specifically: if you change the font size of a text block, recompute its
  height. Spilled-text bugs are nearly always a height mismatch.

## Slide structural patterns

These patterns repeat across the deck and should not be redesigned per slide:

1. **Chart left + 2 stacked panels right** (used on slides 4, 9, 10, 16, 17):
   - Chart: x=0.3, w=8.5, top=1.0
   - Top panel: x=8.95, w=4.1, top=1.0, h=2.95
   - Bottom panel: x=8.95, w=4.1, top=4.05, h=2.65
   - Optional bottom callout band at y=6.78 spanning the full width.

2. **Three equal columns** (slides 2, 6, 18):
   - Margins 0.4 in; gap 0.25 in; column width = (12.5 − 2×0.25) / 3 ≈ 4.05 in.

3. **Numbered rows with text body** (slides 11, 21, 22):
   - Number badge: 0.55 in square; row height 1.2 in; left-aligned title in TROY_BLUE.

## When you add a new slide

1. Pick the structural pattern that fits (above). Do not invent layout.
2. Pull all colors from the palette table. Do not hand-code a new hex.
3. Tables go in rect-tables, never monospace.
4. Render the deck and visually check every slide you touched, plus the two
   slides on either side. The `slides/` PNGs in this repo are the
   review-of-record — open them, don't trust the source.
5. Run `analysis/check_style_drift.py`. It scans the build script for the
   patterns most likely to drift (raw `#xxxxxx` colors outside the palette
   block, monospace tables with hand-padded spaces, boxes whose declared height
   is smaller than the contained text height).

## When you change a value on a slide

If you change the text in a panel, re-verify the panel's height. The Edit tool
won't catch a spilled text bug; only re-rendering and looking at the slide
will.
