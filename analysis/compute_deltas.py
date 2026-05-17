"""Compute pre-COVID → post-COVID Δ for every district × subgroup.

Outputs:
- seda_subgroup_delta.csv: district × subgroup × pre/post/Δ
- Prints the master ranking table to stdout.

Pre-COVID window: 2017-2019 mean
Post-COVID window: 2022-2025 mean
Δ = post mean − pre mean (in SEDA grade-level units)

Usage:
    python3 compute_deltas.py
"""

import csv
import json
import os
from statistics import mean

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
POOLED = os.path.join(DATA_DIR, "seda_2025_pooled.json")
OUT_CSV = os.path.join(DATA_DIR, "seda_subgroup_delta.csv")

SUBGROUPS = [
    ("all", "All"),
    ("asn", "Asian"),
    ("wht", "White"),
    ("blk", "Black"),
    ("hsp", "Hispanic"),
    ("ecd", "EconDis"),
    ("nec", "Not-ECD"),
]
PRE_YEARS = [2017, 2018, 2019]
POST_YEARS = [2022, 2023, 2024, 2025]


def get(pooled, district, year, sg):
    return (pooled.get(district, {}).get(str(year), {}) or {}).get(sg)


def delta(pooled, district, sg):
    pre = [get(pooled, district, y, sg) for y in PRE_YEARS
           if get(pooled, district, y, sg) is not None]
    post = [get(pooled, district, y, sg) for y in POST_YEARS
            if get(pooled, district, y, sg) is not None]
    if len(pre) < 2 or len(post) < 2:
        return None, None, None
    pre_m, post_m = mean(pre), mean(post)
    return pre_m, post_m, post_m - pre_m


def main():
    with open(POOLED) as f:
        pooled = json.load(f)

    districts = sorted(pooled.keys())
    rows = []
    for d in districts:
        for sg_code, sg_name in SUBGROUPS:
            pre, post, d_val = delta(pooled, d, sg_code)
            if d_val is not None:
                rows.append((d, sg_name, pre, post, d_val))

    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["district", "subgroup", "pre_2017_19", "post_2022_25", "delta"])
        for d, sg, pre, post, dv in rows:
            w.writerow([d, sg, f"{pre:.4f}", f"{post:.4f}", f"{dv:.4f}"])
    print(f"Wrote {OUT_CSV} ({len(rows)} rows)")

    # All Students ranking
    print("\nPRE-COVID → POST-COVID Δ — ALL STUDENTS, ranked by Δ (worst first)")
    print("=" * 85)
    print(f"{'Rank':<6}{'District':<35}{'Pre':>10}{'Post':>10}{'Δ':>10}")
    all_rows = [r for r in rows if r[1] == "All"]
    all_rows.sort(key=lambda r: r[4])
    for i, (d, _, pre, post, dv) in enumerate(all_rows, 1):
        marker = "  ◄ TROY" if d == "Troy SD" else ""
        print(f"{i:<6}{d:<35}{pre:>+10.3f}{post:>+10.3f}{dv:>+10.3f}{marker}")


if __name__ == "__main__":
    main()
