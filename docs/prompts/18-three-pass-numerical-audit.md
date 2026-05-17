# 18 — Three-pass numerical audit

**Date:** 2026-05
**Asked for:** Run three independent consistency passes over the deck. Every cited number must match the underlying source data exactly.

## Prompt(s) quoted
> Its extremely important that you maintain analytical / cited number consistency with the analysis. I want you to do three passes on this to ensure this is air tight.

## What was produced
- Pass 1 (deck-to-script): walk every cited number on every slide back to the script that produced it.
- Pass 2 (script-to-data): walk every script's outputs back to the raw SEDA / M-STEP files.
- Pass 3 (cross-slide): verify that the same construct quoted on multiple slides resolves to the same number.
- Errors caught: Hispanic 2019→2025 was wrong sign on slide 4 (–0.10 cited, actually +0.08); slide 6 tier counts didn't sum to 49; slide 18 grade-level table had wrong district names + wrong sign on SoR-recent G3; slide 18 G3 Top-5 row 5 was Dover (rank 7) instead of College Community (rank 5); slide 19 universe bullets summed to 47/50.

## Why this mattered
Without this pass, the deck had load-bearing wrong numbers. A board-level audience will notice a single bad number and discount the rest. Forcing three independent passes is what shook the obvious errors out.
