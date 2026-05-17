# 12 — JavaScript web presentation

**Date:** 2026-04
**Asked for:** Convert the deck into a JavaScript web presentation hosted at a public URL.

## Prompt(s) quoted
> Stand up a web presentation version — same slides, browser-deliverable.

## What was produced
- Static slide PNGs rendered at 144 DPI from the PDF.
- A minimal HTML/JS slideshow consuming those PNGs.
- Hosted at `tsd-k5ela-choice.karpowitsch.org` via Cloudflare Pages.

## Why this mattered
A web URL is shareable. A .pptx attachment is not. Hosting via Cloudflare Pages (auto-deploying on Git push) means every fix to the deck propagates without manual upload steps.
