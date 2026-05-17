# tsd-k5ela-choice

A web presentation of a quantitative analysis pressure-testing Troy School District's (Michigan) K-5 ELA curriculum choice as it shifts from balanced literacy to the Science of Reading.

**Live:** https://tsd-k5ela-choice.karpowitsch.org

**Download deck (PDF):** [Troy_K5_ELA_Executive_Summary_v4.pdf](slides/) — also available in the parent project folder.

---

## What this is

A 24-slide executive summary that asks one question:

> Is Collaborative Literacy 3rd Ed. + UFLI Foundations the right K-5 ELA choice for Troy's balanced-literacy → Science of Reading transition?

And answers it with three convergent pieces of evidence from a 50-district national benchmark on the Stanford Education Data Archive (SEDA) 2025.1 cohort-standardized scale, 2009–2025:

- **0 of 50** outperformer + peer districts use Collaborative Literacy as their K-5 core.
- **4 of 4** districts that gained post-COVID on the SEDA scale run structured-literacy programs.
- **3 of 3** of Troy's stronger alternatives (Amplify CKLA, EL Education, Wit & Wisdom) have direct post-COVID recovery evidence.

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

All 24 slides preload on page open for instant navigation.

---

## Slide map

| # | Slide |
|---|---|
| 1 | Title |
| 2 | The question — and the one-line answer (three convergent evidence points) |
| 3 | The honest pre-COVID picture — Troy gained on aggregate, but subgroups were uneven |
| 4 | The post-COVID collapse is the real signal |
| 5 | Of 50 demographically-comparable + outperformer districts, Troy ranks 47 of 49 |
| 6 | Of 8 Michigan affluent peers, Troy fell the furthest |
| 7 | Troy's worst subgroup declines are the affluent ones |
| 8 | The subgroup data refutes the three common defenses |
| 9 | Asian subgroup: Troy ranks 34 of 35 districts on post-COVID Δ |
| 10 | Not-Econ-Disadvantaged subgroup: Troy ranks 42 of 46 |
| 11 | CKLA-adopting districts on the MDE-approved list are leapfrogging their states |
| 12 | How they did it — Marion County KY and Fond du Lac WI playbooks |
| 13 | Recovery is possible — and it tracks with curriculum choice |
| 14 | Long Beach USD — the natural experiment is now empirically visible |
| 15 | Why balanced literacy fails when school and home reading routines both break down |
| 16 | Curriculum verdict — Troy's options on the MI Section 35m list |
| 17 | Recommendation — three paths ranked |
| 18 | Curriculum is necessary but not sufficient — and what to track |
| 19 | Appendix — Methodology |
| 20-23 | References (4 lists) — Primary datasets, Curriculum evidence, SoR research, District case studies |
| 24 | Project artifacts + how to verify |

---

## Methodology in one paragraph

The primary metric is the SEDA cohort-standardized (cs) score — NAEP-anchored grade-level units. `0.0` = at national grade-level norm; `+1.0` = one grade above. Pre-COVID baseline = 2017-2019 mean; post-COVID = 2022-2025 mean. Grades pooled G3-G5 (ELA only). 2020 and 2021 omitted by SEDA (testing canceled). District universe = 50 districts: Troy + 7 MI affluent peers + 7 workbook peer districts across CA/TX/NJ/WA + 3 SoR-shift Pacific NW peers + 17 Education Scorecard 2026 "Districts on the Rise" outperformers + 8 sustained outperformers (Steubenville, Aldine, Brownsville, Sanger, Garden Grove, Long Beach, Seaford, Valley Stream 30).

See slide 19 of the deck for full methodology, and slides 20-24 for all 43 cited references.

---

## Repository structure

```
.
├── index.html              vanilla-JS slide viewer, ~8 KB, no dependencies
├── slides/                 24 PNG renders at 144 DPI, ~6 MB total
│   ├── 01.png
│   └── …
└── README.md
```

No build step. No frameworks. Three files total.

---

## Tech stack

- **HTML/CSS/JS** — vanilla, no dependencies
- **Slide rendering** — generated from a Python `python-pptx` build script in the parent project (`build_deck_v4.py`), exported to PDF via macOS PowerPoint AppleScript, rasterized to PNG via `pdftoppm` at 144 DPI
- **Hosting** — Cloudflare Pages, deployed on git push (per the karpowitsch.org convention)
- **Data sources** — Stanford Education Data Archive 6.0 and 2025.1, Education Scorecard 2026, individual state DOE files (CAASPP, M-STEP, STAAR, LEAP, MAAP, TCAP, NJSLA, SBA, OST), plus Oakland County local data for MI affluent peer 2025 comparisons

---

## Source attribution

This is one district's analysis prepared by a parent + community member, not a Troy School District official document. The analysis is **forward-looking** about curriculum recovery, not a retrospective critique of past district decisions. Slide 3 explicitly acknowledges that pre-COVID Troy was gaining on the aggregate national-norm scale; the case for change is centered on the post-COVID trajectory and the comparative recovery patterns at peer districts.

Every quantitative claim is anchored to a numbered reference in slides 20-24. The underlying project (analysis files, raw data extracts, charts, master CSV) lives at `/Users/Alex/Downloads/tsd-k5ela/` on the author's machine — the deck's appendix shows a full file map. The 50-district master dataset (2,544 rows: district × year × grade × subgroup × % proficient) is available on request.

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
for i in $(seq -f "%02g" 1 24); do
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
