# `troy_swd_ela.py` (in `tools-mischooldata`)

**Path:** `examples/troy_swd_ela.py` in the
[`tools-mischooldata`](https://github.com/akarpo/tools-mischooldata) repo
(separate from this one).
**Stage:** 0 — produces the CSV that this repo's `analyze_troy_swd.py` and
`build_chart_troy_swd.py` both consume.

## What it does

Drives MI School Data's grades 3-8 proficiency report via Playwright,
cascading through its dropdown chain to land on Troy SD × ELA × SWD
subgroup, then scrapes the year × grade table.

URL:
`https://www.mischooldata.org/grades-3-8-state-testing-includes-psat-data-proficiency/`

Constants:

- `ISD_OAKLAND = "106"`
- `DISTRICT_TROY = "1608"`

The dropdown cascade must run in order:
`isds → districts → schoolYears → assessmentPrograms → subjects → grades →
reportCategories`. The SWD subgroup option only appears in `reportCategories`
*after* a district is selected (the menu expands from 2 options to 7).

## Iteration

- Years: 2014-15 through 2024-25 (11 school years).
- Grades: 3, 4, 5.
- One pull per (year, grade) — the SWD cell either reports or is suppressed.

## Output

`examples/troy_swd_ela.csv` — 26 rows after one G5 2021-22 suppression.

Columns:

```
school_year, grade,
swd_pct, swd_n,
non_swd_pct, non_swd_n,
all_pct, all_n,
oakland_all_pct, state_all_pct
```

## Why it exists

MI School Data publishes SWD performance but doesn't offer a bulk
year-by-grade CSV export for a single district + subgroup. The deck needed
a 10-year window for the Calkins-era story, so a scraper was the path of
least resistance.

## Pitfalls

- **bootstrap-multiselect** doesn't update its `selected` array if you set
  it via JS directly — you have to drive the actual `<select>` element and
  trigger the change event.
- **The `results-frame` iframe** is where the actual table renders; the
  outer page just hosts the controls. Don't try to scrape the outer DOM.
- **MI School Data URL changes.** I burned a probe round on 7 candidate URLs
  that all 404'd before finding the real path by crawling the homepage. If
  the URL above breaks, do the same.
