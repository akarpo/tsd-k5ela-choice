"""Rebuild chart13 — Long Beach natural experiment time series.

Slide 17 "Long Beach USD — the natural experiment is now empirically visible."
Shows cs-scale trajectory 2009-2025 for Troy, Long Beach, and 4 recovery
districts. Uses CHART_* bright palette from STYLE.md.
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "seda_2025_pooled.json")
OUT = os.path.join(os.path.dirname(__file__), "..", "charts", "chart13_post_covid_recovery.png")

with open(DATA) as f:
    pooled = json.load(f)

DISTRICTS = [
    ("Troy SD",           "Troy SD",           "#DC3545", 2.5, "-"),
    ("Long Beach USD",    "Long Beach USD",    "#6C757D",  2.5, "--"),
    ("Spring Branch ISD", "Spring Branch ISD",  "#28A745", 1.5, "-"),
    ("Palo Alto USD",     "Palo Alto USD",      "#4A90D9", 1.5, "-"),
    ("West Baton Rouge",  "West Baton Rouge",   "#F0A030", 1.5, "-"),
    ("Johnson City",      "Johnson City TN",    "#9B59B6", 1.5, "-"),
]
YEARS = list(range(2009, 2026))

fig, ax = plt.subplots(figsize=(11.5, 7.5))

for dkey, dlabel, color, lw, ls in DISTRICTS:
    xs, ys = [], []
    for yr in YEARS:
        v = (pooled.get(dkey, {}).get(str(yr), {}) or {}).get("all")
        if v is not None:
            xs.append(yr)
            ys.append(v)
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=ls, label=dlabel,
            marker="o", markersize=3)

# Shade COVID gap
ax.axvspan(2019.5, 2021.5, alpha=0.08, color="#888888")
ax.text(2020.5, ax.get_ylim()[1] * 0.95, "COVID\ngap", ha="center", fontsize=7,
        color="#888888", va="top")

ax.set_xticks(YEARS)
ax.set_xticklabels([str(y) for y in YEARS], fontsize=8, rotation=45, ha="right")
ax.set_ylabel("SEDA cs score (grade-level units above/below national norm)", fontsize=9)
ax.set_title(
    "Post-COVID Recovery  —  Spring Branch +0.28, Palo Alto +0.13\n"
    "Troy −0.25 declined more than TX BL peers (Frisco, Coppell)",
    fontsize=11, fontweight="bold", color="#1F3A5F"
)
ax.legend(loc="lower left", fontsize=8, ncol=3, framealpha=0.95)
ax.grid(axis="y", linestyle=":", alpha=0.3)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(OUT, dpi=200, bbox_inches="tight", facecolor="white")
print(f"Wrote: {OUT}")
