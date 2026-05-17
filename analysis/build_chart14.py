"""Rebuild chart14 — Subgroup Pre/Post-COVID Δ: Troy vs Recovery Districts.

Slide 16 "Recovery is possible — and it tracks with curriculum choice."
5 series (Troy + 4 recovery districts), 7 subgroups.

Uses CHART_* bright palette from STYLE.md for bar readability.
"""
import csv, json, os
from statistics import mean
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "seda_2025_pooled.json")
OUT = os.path.join(os.path.dirname(__file__), "..", "charts", "chart14_subgroup_compare.png")

with open(DATA) as f:
    pooled = json.load(f)

def delta(d, sg):
    pre, post = [], []
    for y in (2017, 2018, 2019):
        v = (pooled.get(d, {}).get(str(y), {}) or {}).get(sg)
        if v is not None: pre.append(v)
    for y in (2022, 2023, 2024, 2025):
        v = (pooled.get(d, {}).get(str(y), {}) or {}).get(sg)
        if v is not None: post.append(v)
    if len(pre) < 2 or len(post) < 2: return None
    return mean(post) - mean(pre)

DISTRICTS = [
    ("Troy SD",           "Troy SD",          "#DC3545"),
    ("Spring Branch ISD", "Spring Branch ISD", "#28A745"),
    ("Palo Alto USD",     "Palo Alto USD",     "#4A90D9"),
    ("West Baton Rouge",  "West Baton Rouge",  "#F0A030"),
    ("Johnson City",      "Johnson City TN",   "#9B59B6"),
]
SUBGROUPS = [
    ("all", "All"), ("asn", "Asian"), ("wht", "White"), ("blk", "Black"),
    ("hsp", "Hispanic"), ("ecd", "ECD"), ("nec", "Not-ECD"),
]

fig, ax = plt.subplots(figsize=(11.5, 7.5))
n_sg = len(SUBGROUPS)
n_d = len(DISTRICTS)
bar_w = 0.15
x = np.arange(n_sg)

for i, (dkey, dlabel, color) in enumerate(DISTRICTS):
    vals = []
    for sg, _ in SUBGROUPS:
        v = delta(dkey, sg)
        vals.append(v if v is not None else 0.0)
    offset = (i - (n_d - 1) / 2) * bar_w
    ax.bar(x + offset, vals, width=bar_w, color=color, label=dlabel,
           edgecolor="white", linewidth=0.5)

ax.set_xticks(x)
ax.set_xticklabels([lbl for _, lbl in SUBGROUPS], fontsize=10)
ax.axhline(0, color="#555", lw=0.8)
ax.set_ylabel("Pre→Post-COVID Δ (SEDA cs scale, grade-level units)", fontsize=10)
ax.set_title(
    "Subgroup Pre/Post COVID Δ  —  Troy vs Recovering Districts\n"
    "Troy declined in EVERY subgroup. SoR-aligned districts (Spring Branch, Palo Alto, West Baton Rouge) gained.",
    fontsize=11, fontweight="bold", color="#1F3A5F"
)
ax.legend(loc="lower left", fontsize=9, ncol=5, framealpha=0.95)
ax.grid(axis="y", linestyle=":", alpha=0.4)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_ylim(-0.5, 0.85)

plt.tight_layout()
plt.savefig(OUT, dpi=200, bbox_inches="tight", facecolor="white")
print(f"Wrote: {OUT}")
