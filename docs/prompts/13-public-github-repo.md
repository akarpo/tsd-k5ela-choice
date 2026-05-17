# 13 — Public GitHub repo

**Date:** 2026-04
**Asked for:** Push the whole project — deck source, analysis scripts, data, generated artifacts — to a public GitHub repo so the work is verifiable.

## Prompt(s) quoted
> Push it all to a public repo. The whole point is that someone hostile can audit it.

## What was produced
- `github.com/akarpo/tsd-k5ela-choice` (public).
- `.assetsignore` to keep `.git/` out of the Cloudflare Pages deploy.
- R2-bucket externalization for assets >25 MB (see [reference_cloudflare_r2_large_files]).
- All `/Users/Alex/...` paths later stripped from on-deck text (see prompt 21).

## Why this mattered
An evidence-based recommendation that can't be inspected is not evidence-based. Making the repo public is what raises this from "trust me" to "check my work."
