# 22 — Document the prompts

**Date:** 2026-05-17
**Asked for:** Write `.md` files for all the prompts that shaped this project, plus `.md` files for the tooling we built, and push them to GitHub as part of the repo.

## Prompt(s) quoted
> Write .md files for all the prompts along with .md files for tooling you've created, and upload these to github, I dont mind that they're there. They need to be part of the project.

## What was produced
- `docs/prompts/README.md` — chronological index of the 22 prompts.
- `docs/prompts/01-…22-….md` — one file per prompt with quoted ask, produced artifacts, and why-it-mattered context.
- `docs/tooling/` — per-script docs for `extract_seda_subset`, `compute_deltas`, `build_chart13`, `build_chart_troy_swd`, `analyze_troy_swd`, `check_style_drift`, and `troy_swd_ela` (in `tools-mischooldata`).

## Why this mattered
The deck is the output of a multi-day collaboration, not a one-shot generation. Without this trail, the reasoning behind specific slides (especially the surprises — SWD, "0 of 50", SoR-doesn't-guarantee-recovery) reads as fait accompli. With it, anyone auditing or extending the work can see *why* a slide exists, not just *what* it says.
