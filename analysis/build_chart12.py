"""Rebuild chart12 — MI affluent peers SEDA cs time series 2009-2025.

Generates chart12_mi_peers_2009_2025.png with a taller aspect ratio
suitable for a side-by-side layout on slide 8.
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "seda_2025_pooled.json")
OUT = os.path.join(os.path.dirname(__file__), "..", "charts", "chart12_mi_peers_2009_2025.png")

with open(DATA) as f:
    pooled = json.load(f)

DISTRICTS = [
    ("Troy SD",            "Troy SD",           "#DC3545", 2.8, "-"),
    ("West Bloomfield SD", "West Bloomfield",   "#F0A030", 1.5, "-"),
    ("Rochester CSD",      "Rochester CSD",     "#4A90D9", 1.5, "-"),
    ("Novi CSD",           "Novi CSD",          "#28A745", 1.5, "-"),
    ("Northville PS",      "Northville PS",     "#9B59B6", 1.5, "-"),
    ("Birmingham PS",      "Birmingham PS",     "#6C757D", 1.5, "-"),
    ("Bloomfield Hills",   "Bloomfield Hills",  "#17A2B8", 1.5, "-"),
    ("Walled Lake CSD",    "Walled Lake",       "#8B4513", 1.2, "--"),
]
YEARS = list(range(2009, 2026))

fig, ax = plt.subplots(figsize=(9.5, 7.0))

for dkey, dlabel, color, lw, ls in DISTRICTS:
    xs, ys = [], []
    for yr in YEARS:
        v = (pooled.get(dkey, {}).get(str(yr), {}) or {}).get("all")
        if v is not None:
            xs.append(yr)
            ys.append(v)
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=ls, label=dlabel,
            marker="o", markersize=3)

ax.axvspan(2019.5, 2021.5, alpha=0.08, color="#888888")
ax.text(2020.5, ax.get_ylim()[1] * 0.97, "COVID\ngap", ha="center", fontsize=8,
        color="#888888", va="top")

ax.set_xticks(YEARS)
ax.set_xticklabels([str(y) for y in YEARS], fontsize=8, rotation=45, ha="right")
ax.set_ylabel("SEDA cs score (grade-level units above national norm)", fontsize=9)
ax.set_title(
    "MI Affluent Peers — SEDA cs G3–G5 ELA (aggregate), 2009–2025\n"
    "Troy had largest 10-yr GAIN pre-COVID, then steepest DECLINE post-COVID",
    fontsize=11, fontweight="bold", color="#1F3A5F"
)
ax.legend(loc="lower left", fontsize=8.5, ncol=2, framealpha=0.95)
ax.grid(axis="y", linestyle=":", alpha=0.3)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(OUT, dpi=180, bbox_inches="tight", facecolor="white")
print(f"Wrote: {OUT}")
