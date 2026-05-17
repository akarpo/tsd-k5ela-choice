# `extract_seda_subset.py`

**Path:** `analysis/extract_seda_subset.py`
**Stage:** 1 (first script in the pipeline)

## What it does

Reads the raw SEDA 2025.1 cohort-standardized (cs) scale data files and writes
out the 50-district subset used everywhere downstream. The 50 districts are
the universe defined in [prompt 06](../prompts/06-comprehensive-50-district-seda.md)
— Troy SD + matched peers + sustained outperformers + recovery cohort.

## Inputs

- SEDA 2025.1 raw release (district-level cs-scale ELA, by year × subgroup).
- Hard-coded list of the 50 district keys (NCES IDs).

## Outputs

- `research/seda_2025_pooled.json` — district → year → subgroup → cs-score, the
  canonical lookup used by `compute_deltas.py` and every chart builder.

## Why it exists

The raw SEDA release is too big to carry in the repo and includes far more
districts than the analysis needs. Pinning to a 50-district subset (chosen
in advance, not after seeing results) is what keeps the analysis from being
implicitly curated.

## Pitfalls

- **Subgroup keys differ across SEDA releases.** The 2025.1 file uses `all`,
  `asn`, `wht`, `blk`, `hsp`, `ecd`, `nec`. If you bump SEDA versions, re-verify.
- **Small-N suppression** is handled downstream (chart builders skip None values).
  The extraction script preserves None rather than zero-filling.
