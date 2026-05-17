# `check_style_drift.py`

**Path:** `analysis/check_style_drift.py`
**Stage:** 6 (run *after* every edit to `build_deck.py`)

## What it does

Static scanner over `build_deck.py` that flags the three patterns we keep
regressing on:

1. **Raw hex outside the palette.** Any `"#RRGGBB"` string literal whose
   value isn't in the palette block (see `STYLE.md`).
2. **Hand-padded monospace tables.** Consecutive string-literal lines with
   runs of 4+ spaces that aren't followed by `font="Consolas"` — almost
   always a fake-column layout that breaks when PowerPoint substitutes a
   proportional font.
3. **Content below the footer band.** `add_text(s, Inches(x), Inches(y), …)`
   calls with `y > 7.05` — collide with the footer at y=7.15.

## Output

Findings grouped by kind, with the source line number. The script returns
non-zero exit code only on the highest-confidence category
(`CONTENT_BELOW_FOOTER`) so it can sit in a pre-push hook later without
flapping.

## Why it exists

[Prompt 20](../prompts/20-design-validation-feedback.md) — I had been claiming
"design audited" without catching visible regressions. A static scanner is
not a substitute for opening the rendered PNG, but it catches the dumbest
classes of drift automatically.

## Known false-positives

- The footer-collision check fires on the `footer()` function definition
  itself (lines that *legitimately* place text at y=7.15 because that's
  the footer band).
- The monospace check fires on some lines that *do* set `font="Consolas"`
  but the context-window heuristic misses it.

These are tracked for refinement; the script intentionally over-reports.
Treat any flag as "verify this before committing," not "auto-fail."

## How to run

```bash
python analysis/check_style_drift.py analysis/build_deck.py
```
