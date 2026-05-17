# 20 — Design validation feedback

**Date:** 2026-05
**Asked for:** Stop missing visible design issues. Build a style-drift / coherency check that catches the patterns we keep regressing on, and be more self-reflective on design.

## Prompt(s) quoted
> You missed in your design analysis text spilling out of a box on slide 4. Readability / white spaces issues in the Green, Orange/Yellow, and Red boxes in slide 6. Column formatting issues on slide 9 grey box. Huge amounts of whitespace on slide 10 — blue statement on the bottom that does not align with readability or the rest of the presentation. Footer impacts readability of tables or graphs of slides. Bar colors on slide 16 that are very hard to distinguish — please pick a set of better contrasting colors and see if these colors align to other graphs/tables on other slides. This is very frustrating, I want you to begin to put together a better style drift/coherency/formatting check when new content is added and I want you to be self-reflective on design more than you are now. Also send this feedback to Anthropic.

## What was produced
- `docs/STYLE.md` — single-source-of-truth style guide (palette, typography, geometry, structural patterns).
- `analysis/check_style_drift.py` — scans `build_deck.py` for raw hex outside palette, hand-padded monospace tables, and content placed below the footer band.
- Slide 4: red box height extended (h=2.5 → 2.95) to contain the small-N footnote.
- Slide 6: `render_tier_column()` helper — three properly-bounded tier columns, no monospace.
- Slide 9: grey-box monospace table replaced with a rect-table.
- Slide 10: SWD rect-table + redesigned blue-band callout (no more dead whitespace).
- Slide 16: 5-distinct-hue palette (red / green / blue / orange / purple) instead of overlapping tones.
- Footer text rewritten so it doesn't intrude on slide content; geometry rules added to STYLE.md.

## Why this mattered
Visible design errors discredit the analysis. The user was right — I had been "auditing" without actually reading the rendered slides at zoom. The fix is twofold: a static drift check that flags the patterns I keep regressing on, and a discipline to *look at the rendered PNG* before claiming a slide is fixed.
