# 21 — Strip versioning and local paths

**Date:** 2026-05
**Asked for:** Remove version numbering (`v4`, etc.) from the presentation and all tooling. Remove all `/Users/Alex/...` local paths from on-deck text and from scripts. Everything visible should reference GitHub, not a local workstation.

## Prompt(s) quoted
> Remove references to version numbering from the presentation. Remove references to where the project is stored \Users\Alex. Everything should reference what's available on Github.
> Remove references to version number from the tooling as well.

## What was produced
- `deck/Troy_K5_ELA_Executive_Summary_v4.pptx` renamed → `deck/Troy_K5_ELA_Executive_Summary.pptx` (via `git mv`).
- `build_deck_v4.py` renamed → `build_deck.py`.
- Title slide: `/Users/Alex/Downloads/tsd-k5ela/` → `github.com/akarpo/tsd-k5ela-choice`.
- Footer text: `Executive Summary  •  github.com/akarpo/tsd-k5ela-choice`.
- README slide-map updated; all "v4" tokens removed across the repo.

## Why this mattered
A deck with a `v4` watermark or a `/Users/Alex/...` path on the title slide reads as a draft. Anchoring to the public GitHub URL signals "this is the artifact" and makes the deck self-locating — anyone with the PDF can find the source.
