"""Rebuild SWD chart — Troy SWD vs Peer-7 SWD avg vs MI State All.

Three line graphs (G3, G4, G5) showing:
  - Troy SWD (red, bold)
  - Peer-7 SWD average (blue)
  - MI State All (gray dashed, floor reference)

Removes Troy-All and Troy non-SWD per user request.
"""
import csv, os
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

TROY_SRC = os.path.join(os.path.dirname(__file__), "..", "data", "troy_swd_ela.csv")
PEER_SRC = os.path.join(os.path.dirname(__file__), "..", "data", "peer_swd_ela.csv")
OUT = os.path.join(os.path.dirname(__file__), "..", "charts", "chart_swd_deck.png")

# Load Troy
troy_rows = []
with open(TROY_SRC) as f:
    for r in csv.DictReader(f):
        troy_rows.append(r)

# Load peers
peer_rows = []
with open(PEER_SRC) as f:
    for r in csv.DictReader(f):
        peer_rows.append(r)

YEARS = ["2015-16", "2016-17", "2017-18", "2018-19", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
SHORT = ["'16", "'17", "'18", "'19", "'21", "'22", "'23", "'24", "'25"]

def interpolate_series(series_dict, years):
    vals = [series_dict.get(y) for y in years]
    for i in range(len(vals)):
        if vals[i] is None:
            left = next((vals[j] for j in range(i-1, -1, -1) if vals[j] is not None), None)
            right = next((vals[j] for j in range(i+1, len(vals)) if vals[j] is not None), None)
            if left is not None and right is not None:
                vals[i] = (left + right) / 2
            elif left is not None:
                vals[i] = left
            elif right is not None:
                vals[i] = right
    return {y: v for y, v in zip(years, vals) if v is not None}

# Organize Troy SWD and State All by (year, grade)
troy_swd_raw = {}
troy_state = {}
for r in troy_rows:
    key = (r["school_year"], int(r["grade"]))
    try:
        if r["swd_pct"] and r["swd_pct"].strip() not in ("", "%"):
            troy_swd_raw[key] = float(r["swd_pct"])
    except ValueError:
        pass
    try:
        if r["state_all_pct"] and r["state_all_pct"].strip() not in ("", "%"):
            troy_state[key] = float(r["state_all_pct"])
    except ValueError:
        pass

# Interpolate Troy SWD missing values per grade
troy_swd = {}
for g in [3, 4, 5]:
    series = {y: troy_swd_raw.get((y, g)) for y in YEARS}
    filled = interpolate_series(series, YEARS)
    for y, v in filled.items():
        troy_swd[(y, g)] = v

# Compute peer-7 SWD average with interpolation for suppressed values
# First build per-district time series, then interpolate gaps
peer_by_dist = defaultdict(lambda: defaultdict(dict))
for r in peer_rows:
    try:
        if r["swd_pct"] and r["swd_pct"].strip():
            val = float(r["swd_pct"])
            peer_by_dist[r["district"]][int(r["grade"])][r["school_year"]] = val
    except (ValueError, KeyError):
        pass

# For each district/grade, interpolate missing years then average
peer_swd_lists = defaultdict(list)
for dist, grades in peer_by_dist.items():
    for g, yr_vals in grades.items():
        filled = interpolate_series(yr_vals, YEARS)
        for yr, val in filled.items():
            peer_swd_lists[(yr, g)].append(val)

peer_swd_avg = {k: sum(v)/len(v) for k, v in peer_swd_lists.items() if v}

TROY_BLUE = "#1F3A5F"
ACCENT_RED = "#C8302F"
PEER_BLUE = "#4A90D9"

fig, axes = plt.subplots(1, 3, figsize=(11.5, 5.0), sharey=True)

for ax, g in zip(axes, [3, 4, 5]):
    # Troy SWD
    t_vals = [troy_swd.get((y, g)) for y in YEARS]
    # Peer-7 SWD avg
    p_vals = [peer_swd_avg.get((y, g)) for y in YEARS]
    # MI State All
    s_vals = [troy_state.get((y, g)) for y in YEARS]

    def plot_line(vals, **kw):
        xs = [x for x, v in zip(SHORT, vals) if v is not None]
        ys = [v for v in vals if v is not None]
        ax.plot(xs, ys, **kw)

    plot_line(t_vals, color=ACCENT_RED, marker='o', lw=2.5, ms=6, label='Troy SWD')
    plot_line(p_vals, color=PEER_BLUE, marker='s', lw=2.0, ms=5, label='Peer-7 SWD avg')
    plot_line(s_vals, color='#666', linestyle='--', lw=1.3, alpha=0.85, label='MI State All')

    # COVID gap shading
    ax.axvspan("'19", "'21", color='#ddd', alpha=0.5, zorder=0)

    ax.set_title(f'Grade {g}  ELA  %Adv+Prof', fontsize=11, fontweight='bold', color=TROY_BLUE)
    ax.set_ylim(0, 60)
    ax.grid(axis='y', linestyle=':', alpha=0.4)
    ax.tick_params(axis='x', labelsize=8.5)
    ax.tick_params(axis='y', labelsize=8.5)
    if g == 3:
        ax.set_ylabel('% Advanced or Proficient', fontsize=9.5)
        ax.legend(loc='upper right', fontsize=8, framealpha=0.9)

plt.suptitle("Troy SWD vs MI Affluent Peer-7 SWD Average — M-STEP G3–G5 ELA",
             fontsize=11, fontweight='bold', color=TROY_BLUE, y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(OUT, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Wrote: {OUT}")
