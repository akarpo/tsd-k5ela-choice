# tsd-k5ela-choice

A web presentation of a quantitative analysis pressure-testing Troy School District's (Michigan) K-5 ELA curriculum choice as it shifts from balanced literacy to the Science of Reading.

**Live:** https://tsd-k5ela-choice.karpowitsch.org

**Download deck (PDF):** [Troy_K5_ELA_Executive_Summary_v4.pdf](slides/) — also available in the parent project folder.

---

## What this is

A 27-slide executive summary that asks one question:

> Is Collaborative Literacy 3rd Ed. + UFLI Foundations the right K-5 ELA choice for Troy's balanced-literacy → Science of Reading transition?

And answers it with three convergent pieces of evidence from a 50-district national benchmark on the Stanford Education Data Archive (SEDA) 2025.1 cohort-standardized scale, 2009–2025:

- **0 of 50** outperformer + peer districts use Collaborative Literacy as their K-5 core.
- **19 of 20** Education Scorecard 2026 ELA-relevant outperformer districts (demographic-adjusted gain methodology) run, supplement, or are transitioning to SoR-aligned curricula. Only Wayne County NC stayed in pure balanced literacy.
- **3 of 3** of Troy's stronger alternatives (Amplify CKLA, EL Education, Wit & Wisdom) have named district adoptions with post-COVID recovery evidence — Marion County KY + Fond du Lac WI (CKLA), Detroit DPSCD (EL Education), West Baton Rouge + Baltimore (Wit & Wisdom).

The deck includes the honest pre-COVID baseline (Troy gained on aggregate, with uneven subgroup performance), the post-COVID collapse (Troy ranks 47 of 49 on pre→post-COVID Δ), and case studies of two districts on Michigan's MDE Section 35m approved list that adopted Amplify CKLA and are now leapfrogging their state averages (Marion County KY, Fond du Lac WI).

Full appendix with 43 cited references and a project-file map for verification.

---

## Controls

| Action | Input |
|---|---|
| Next slide | <kbd>→</kbd> · <kbd>Space</kbd> · <kbd>PageDown</kbd> · click right half · swipe left |
| Previous slide | <kbd>←</kbd> · <kbd>PageUp</kbd> · click left half · swipe right |
| First / Last | <kbd>Home</kbd> / <kbd>End</kbd> |
| Fullscreen | <kbd>F</kbd> |
| Jump to slide 1-9 | press the number |
| Deep-link to slide N | URL hash `#slide=N` (e.g. `?#slide=12`) |

All 27 slides preload on page open for instant navigation.

---

## Slide map

| # | Slide |
|---|---|
| 1 | Title |
| 2 | The question — and the one-line answer (three convergent evidence points) |
| 3 | The honest pre-COVID picture — Troy gained on aggregate, but subgroups were uneven |
| 4 | The post-COVID collapse is the real signal |
| 5 | Troy ranks 47 of 49 nationally on pre/post-COVID Δ |
| 6 | Comprehensive view — 49 districts, every Δ tier, both curriculum types |
| 7 | Education Scorecard 2026 DOTR — second independent benchmark |
| 8 | Of 8 Michigan affluent peers, Troy fell the furthest |
| 9 | Troy's worst subgroup declines are the affluent ones |
| 10 | The subgroup data refutes the three common defenses |
| 11 | Asian subgroup: Troy ranks 34 of 35 districts on post-COVID Δ |
| 12 | Not-Econ-Disadvantaged subgroup: Troy ranks 42 of 46 |
| 13 | CKLA-adopting districts on the MDE-approved list are leapfrogging their states |
| 14 | How they did it — Marion County KY and Fond du Lac WI playbooks |
| 15 | Recovery is possible — and it tracks with curriculum choice |
| 16 | Long Beach USD — the natural experiment is now empirically visible |
| 17 | Why balanced literacy fails when school and home reading routines both break down |
| 18 | Tested hypothesis — does SoR help only early grades? |
| 19 | Curriculum verdict — Troy's options on the MI Section 35m list |
| 20 | Recommendation — three paths ranked |
| 21 | Curriculum is necessary but not sufficient — and what to track |
| 22 | Appendix — Methodology |
| 23-26 | References (1-4 of 5) — Primary datasets, Curriculum evidence, SoR research, District case studies |
| 27 | References (5 of 5) — Project artifacts + how to verify |

---

## Methodology in one paragraph

The primary metric is the SEDA cohort-standardized (cs) score — NAEP-anchored grade-level units. `0.0` = at national grade-level norm; `+1.0` = one grade above. Pre-COVID baseline = 2017-2019 mean; post-COVID = 2022-2025 mean. Grades pooled G3-G5 (ELA only). 2020 and 2021 omitted by SEDA (testing canceled). District universe = 50 districts: Troy + 7 MI affluent peers + 7 workbook peer districts across CA/TX/NJ/WA + 3 SoR-shift Pacific NW peers + 17 Education Scorecard 2026 "Districts on the Rise" outperformers + 8 sustained outperformers (Steubenville, Aldine, Brownsville, Sanger, Garden Grove, Long Beach, Seaford, Valley Stream 30).

See slide 22 of the deck for full methodology, and slides 23-27 for all 43 cited references + project artifact map.

---

## Repository structure

```
.
├── README.md                        this file
├── index.html                       vanilla-JS slide viewer (~8 KB, no dependencies)
├── slides/                          27 PNG renders at 144 DPI (~7 MB) — served by index.html
├── deck/
│   └── Troy_K5_ELA_Executive_Summary_v4.pptx   the source PowerPoint deck
├── analysis/                        Python scripts to reproduce the analysis
│   ├── build_deck.py                builds the .pptx from data + charts
│   ├── extract_seda_subset.py       downloads SEDA + extracts 50-district subset
│   └── compute_deltas.py            computes pre/post-COVID Δ matrix
├── data/                            processed data files
│   ├── master_dataset.csv           2,544 rows — district × year × grade × subgroup × % proficient on state tests
│   ├── seda_2025_pooled.json        SEDA cs RLA G3-G5 pooled per district × year × subgroup
│   ├── seda_2025_state.json         State-level SEDA averages by year
│   ├── seda_subgroup_delta.csv      Pre/post-COVID Δ matrix per subgroup × district
│   ├── seda_2009_2019_extract.csv   Raw SEDA 6.0 extract (50 districts × G3-G5 ELA)
│   └── seda_2009_2025_extract.csv   Raw SEDA 2025.1 extract (50 districts × G3-G5 ELA)
├── charts/                          19 matplotlib PNGs embedded in the deck
├── reports/                         supporting analysis documents (markdown)
│   ├── synthesis.md                 master synthesis report
│   ├── quantitative_analysis.md     28-district analysis with 6 charts
│   ├── seda_2025_analysis.md        SEDA 2025.1 pre/post-COVID deep dive
│   ├── troy_data_brief.md           Troy M-STEP trajectory + subgroup tables
│   ├── curriculum_evaluations.md    All 14 Section 35m approved curricula evaluated
│   ├── collab_lit_ufli_pressure_test.md   Collab Lit + UFLI critique
│   ├── peer_district_cases.md       Peer-district transition cases
│   ├── education_scorecard_2026_dotr.md   20 DOTR outperformer case studies
│   └── sustained_outperformers.md   17 sustained-outperformer districts
└── docs/                            methodology + reproducibility documentation
    ├── METHODOLOGY.md               metric definitions, time windows, district universe
    ├── REPRODUCIBILITY.md           how to reproduce every claim in 3 commands
    └── DISTRICT_UNIVERSE.md         all 50 districts with NCES LEA IDs
```

The web viewer (`index.html` + `slides/`) has no dependencies. The reproduction pipeline (`analysis/` + `data/`) requires Python 3.9 + `python-pptx` + `matplotlib`.

## Reproduce in three commands

```bash
cd analysis
python3 extract_seda_subset.py    # downloads SEDA + extracts 50-district subset
python3 compute_deltas.py          # computes pre/post-COVID Δ matrix + prints ranking
python3 build_deck.py              # regenerates the .pptx deck
```

See [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md) for full instructions including the deck-rendering pipeline.

---

## Tech stack

- **HTML/CSS/JS** — vanilla, no dependencies
- **Slide rendering** — generated from a Python `python-pptx` build script in the parent project (`build_deck_v4.py`), exported to PDF via macOS PowerPoint AppleScript, rasterized to PNG via `pdftoppm` at 144 DPI
- **Hosting** — Cloudflare Pages, deployed on git push (per the karpowitsch.org convention)
- **Data sources** — Stanford Education Data Archive 6.0 and 2025.1, Education Scorecard 2026, individual state DOE files (CAASPP, M-STEP, STAAR, LEAP, MAAP, TCAP, NJSLA, SBA, OST), plus Oakland County local data for MI affluent peer 2025 comparisons

---

## Source attribution

This is one district's analysis prepared by a parent + community member, not a Troy School District official document. The analysis is **forward-looking** about curriculum recovery, not a retrospective critique of past district decisions. Slide 3 explicitly acknowledges that pre-COVID Troy was gaining on the aggregate national-norm scale; the case for change is centered on the post-COVID trajectory and the comparative recovery patterns at peer districts.

Every quantitative claim is anchored to a numbered reference in slides 23-27. The underlying project (analysis files, raw data extracts, charts, master CSV) lives at `/Users/Alex/Downloads/tsd-k5ela/` on the author's machine — the deck's appendix shows a full file map. The 50-district master dataset (2,544 rows: district × year × grade × subgroup × % proficient) is available on request.

---

## Regenerating the slide images

If the source deck (`Troy_K5_ELA_Executive_Summary_v4.pptx`) is edited, regenerate slide PNGs with:

```bash
# From the parent project folder
cd /path/to/tsd-k5ela
osascript -e '
  tell application "Microsoft PowerPoint"
    open POSIX file "/full/path/Troy_K5_ELA_Executive_Summary_v4.pptx"
    delay 4
    save active presentation in (POSIX file "/tmp/deck.pdf") as save as PDF
    close active presentation saving no
  end tell'
pdftoppm -png -r 144 /tmp/deck.pdf /tmp/v4
for i in $(seq -f "%02g" 1 27); do
  cp /tmp/v4-${i}.png /path/to/tsd-k5ela-choice/slides/${i}.png
done
git add slides/ && git commit -m "Regenerate slides" && git push
```

Cloudflare Pages will auto-deploy on push.

---

## License

Content (slides, analysis, conclusions): all rights reserved by the author. Cite or quote with attribution and a link back.

Code (`index.html`): MIT.

---

## Contact

Issues / corrections / data questions: open an issue on this repo.
