# 14 — Reproducibility scripts

**Date:** 2026-04
**Asked for:** Make sure every quantitative claim in the deck has a corresponding script in the repo that regenerates it from raw data.

## Prompt(s) quoted
> A third party should be able to clone the repo, run a script, and get every number on every slide.

## What was produced
- `analysis/extract_seda_subset.py` — pull the 50-district slice from raw SEDA 2025.1.
- `analysis/compute_deltas.py` — Pre→Post-COVID Δ at All + subgroup level.
- `analysis/build_chart*.py` — every chart in the deck.
- `analysis/build_deck.py` — assembles the .pptx from those outputs.
- README pointing to the scripts in the order they run.

## Why this mattered
Cited numbers in a PDF are still opaque. Cited numbers + the script that produced them is not. This is what made the "three-pass numerical audit" later actually possible — there was a script to point at, not just a spreadsheet I couldn't share.
