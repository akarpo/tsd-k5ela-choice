# Reproducibility

This analysis is fully reproducible from the data and scripts in this repo. The only external inputs are the Stanford Education Data Archive (SEDA) public bulk files, which are downloaded automatically by the extraction script.

## Environment

- Python 3.9+
- Required packages: `python-pptx`, `matplotlib`, `openpyxl` (only for the original workbook reader, optional)

```bash
pip install python-pptx matplotlib openpyxl
```

For PowerPoint → PDF → PNG rendering of the deck (only needed if you want to regenerate slide images for the web viewer):

- macOS with Microsoft PowerPoint installed (uses AppleScript)
- Poppler tools (`pdftoppm`): `brew install poppler`

## Three-step reproduction

### 1. Re-extract SEDA data

```bash
cd analysis
python3 extract_seda_subset.py
```

This downloads the SEDA 2025.1 administrative-district long file (~88 MB) and state-level long file (~5 MB) into `data/_raw_seda_*.csv` (gitignored — they're too large to commit), then filters to the 50 target districts and pools G3-G5 ELA scores. Output:

- `data/seda_2025_pooled.json` — 50 districts × 13 years × 7 subgroups
- `data/seda_2025_state.json` — state-level G3-G5 means

### 2. Compute pre/post-COVID Δ

```bash
python3 compute_deltas.py
```

Outputs `data/seda_subgroup_delta.csv` and prints the master ranking table to stdout. The ranking confirms Troy's 47-of-49 position.

### 3. Rebuild the deck

```bash
python3 build_deck.py
```

Writes `Troy_K5_ELA_Executive_Summary_v4.pptx` (the deck) using the data files and matplotlib charts. The script embeds chart PNGs from `charts/` and renders all 24 slides.

## Optional: regenerate matplotlib charts

The chart-generation code is embedded throughout `analysis/build_deck.py` and reads from `data/seda_2025_pooled.json` and `data/seda_2025_state.json`. To regenerate charts independently, copy the relevant matplotlib blocks from `build_deck.py` or extract them into a standalone script.

The 19 PNGs in `charts/` are the canonical chart images embedded in the deck.

## Optional: regenerate slide images for the web viewer

Slide PNGs (24 images at 144 DPI in `slides/`) are rendered from the PowerPoint deck via:

```bash
# Convert PPTX to PDF via PowerPoint AppleScript
osascript -e '
  tell application "Microsoft PowerPoint"
    open POSIX file "'"$(pwd)"'/deck/Troy_K5_ELA_Executive_Summary_v4.pptx"
    delay 4
    save active presentation in (POSIX file "/tmp/deck.pdf") as save as PDF
    close active presentation saving no
  end tell'

# Render each page to PNG
pdftoppm -png -r 144 /tmp/deck.pdf /tmp/v4
for i in $(seq -f "%02g" 1 24); do
  cp /tmp/v4-${i}.png slides/${i}.png
done
```

Push to GitHub; Cloudflare Pages auto-redeploys to `tsd-k5ela-choice.karpowitsch.org`.

## Verifying a specific claim

Every cited statistic in the deck has a chain of provenance:

| Claim type | Verify by |
|---|---|
| Cs value for district × year × subgroup | `data/seda_2025_pooled.json` → cross-check against the raw SEDA bulk file |
| Pre/post-COVID Δ | `data/seda_subgroup_delta.csv` row matching |
| Ranking position (e.g., "Troy 47 of 49") | Re-run `compute_deltas.py` and count rows |
| Raw-percent district trajectory | `data/master_dataset.csv` |
| External source (EdReports, Reading League, etc.) | Slide footnote → appendix slides 20-24 of the deck |

## Differences from the live deck

If you regenerate the deck and the numbers differ, possible reasons:

1. **SEDA has released a new version.** This analysis uses v2025.1 (2026 release). Later versions may re-process earlier-year scores or add new years.
2. **A district's NCES LEA ID has changed.** Check the TARGETS dictionary in `extract_seda_subset.py`.
3. **You're pooling differently.** The default is G3-G5 n-weighted mean. Single-grade or unweighted analyses will produce different numbers.

## Things this repo does NOT reproduce

This repo includes the SEDA-based quantitative analysis. It does NOT include:

- The 20 Education Scorecard 2026 case-study PDFs (linked in appendix slide 23)
- The 14 Section 35m curriculum reviews (EdReports / Reading League CNRs — public, but third-party)
- The original Oakland County 115 raw report (linked in appendix slide 20)

All of these are linked by URL in the deck's appendix (slides 20-24).
