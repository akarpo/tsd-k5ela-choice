"""Rebuild chart11 — Pre→Post-COVID Δ ranking for 49 districts.

Horizontal bar chart, color-coded by curriculum type. Sized to fit
slide 5 without overflowing into the footer (target: ~5.8 in tall
when embedded at 8.0 in wide).
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "seda_subgroup_delta.csv")
OUT = os.path.join(os.path.dirname(__file__), "..", "charts", "chart11_seda_pre_post_covid.png")

SOR_DISTRICTS = {
    "Spring Branch ISD", "Palo Alto USD", "West Baton Rouge", "Johnson City",
    "Marion County", "Fond du Lac SD", "Aldine ISD", "Steubenville City",
    "Atlanta PS", "Baltimore City PS", "Brandywine SD", "East Hartford SD",
    "Roanoke County PS", "College Community SD", "Kuna Joint SD",
    "Pierre SD 32-2", "Sikeston R-6", "Starkville-Oktibbeha",
    "Bethlehem Area SD", "East Chicago", "Detroit DPSCD",
    "Seaford SD", "Dover SD",
}
BL_DISTRICTS = {
    "Troy SD", "West Bloomfield SD", "Bloomfield Hills", "Birmingham PS",
    "Northville PS", "Novi CSD", "Rochester CSD", "Walled Lake CS",
    "Coppell ISD", "Plano ISD", "Frisco ISD",
    "West Windsor-Plainsboro", "Millburn Twp", "Princeton PS",
    "Wayne County PS", "Valley Stream 30",
    "Long Beach USD",
}
MIXED_DISTRICTS = {
    "Bellevue SD", "Issaquah SD", "Lake Washington SD",
    "Dublin USD", "Milpitas USD", "Walnut Valley USD",
    "Garden Grove Unified", "Sanger Unified", "Modesto City Elem",
    "Brownsville ISD",
}

TROY_BLUE = "#1F3A5F"
ACCENT_RED = "#C8302F"
ACCENT_GREEN = "#1F7A3D"
ACCENT_ORANGE = "#B7791F"
GRAY_MID = "#777777"

rows = []
with open(DATA) as f:
    for r in csv.DictReader(f):
        if r["subgroup"] == "All":
            rows.append((r["district"], float(r["delta"])))

rows.sort(key=lambda x: x[1], reverse=True)

names = [r[0] for r in rows]
deltas = [r[1] for r in rows]

colors = []
for name in names:
    if name == "Troy SD":
        colors.append(ACCENT_RED)
    elif name in SOR_DISTRICTS:
        colors.append(ACCENT_GREEN)
    elif name in MIXED_DISTRICTS:
        colors.append(ACCENT_ORANGE)
    elif name in BL_DISTRICTS:
        colors.append("#CC4444")
    else:
        colors.append(GRAY_MID)

fig_w, fig_h = 8.0, 5.8
fig, ax = plt.subplots(figsize=(fig_w, fig_h))

y_pos = np.arange(len(names))
bars = ax.barh(y_pos, deltas, color=colors, edgecolor="white", linewidth=0.3, height=0.7)

ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontsize=6.5)
ax.invert_yaxis()
ax.axvline(0, color="#555", lw=0.6)

ax.set_xlabel("Pre→Post-COVID Δ (SEDA cs scale, ≈ 0.253 grade levels)", fontsize=8)
ax.set_title(
    "SEDA 2025.1 cs RLA G3-G5  —  Pre-COVID → Post-COVID Δ\n"
    "Troy SD ranks 3rd-WORST of 49 districts (Δ = −0.253 grade levels)",
    fontsize=9, fontweight="bold", color=TROY_BLUE, pad=8
)

troy_idx = names.index("Troy SD")
ax.get_yticklabels()[troy_idx].set_fontweight("bold")
ax.get_yticklabels()[troy_idx].set_color(ACCENT_RED)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=ACCENT_GREEN, label="SoR / structured literacy"),
    Patch(facecolor=ACCENT_ORANGE, label="Mixed / transitioning"),
    Patch(facecolor="#CC4444", label="Balanced literacy (stayed)"),
    Patch(facecolor=ACCENT_RED, label="Troy SD"),
]
ax.legend(handles=legend_elements, loc="lower right", fontsize=7, framealpha=0.9)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.3)

plt.tight_layout()
plt.savefig(OUT, dpi=200, bbox_inches="tight", facecolor="white")
print(f"Wrote: {OUT}  ({fig_w}x{fig_h} in, {len(rows)} districts)")
