# 11 — PDF export

**Date:** 2026-04
**Asked for:** A PDF version of the deck, generated reproducibly from the PowerPoint.

## Prompt(s) quoted
> Generate a PDF of the deck.

## What was produced
- AppleScript automation driving PowerPoint to export the .pptx → .pdf.
- `deck/Troy_K5_ELA_Executive_Summary.pdf` checked into the repo alongside the .pptx.
- `pdftoppm`-based path to render slide PNGs at 144 DPI for the web presentation.

## Why this mattered
A static PDF is the artifact most stakeholders will actually read. Tying it to a one-shot script (rather than File→Export by hand) made the build reproducible.
