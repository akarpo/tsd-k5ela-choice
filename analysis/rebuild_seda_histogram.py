"""Rebuild chart_seda_ela_peers.png — clean histogram without overlapping annotation."""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os

CHART_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'charts')
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'seda_ela_peers_full.csv')

df = pd.read_csv(DATA)
troy = df[df['sid'] == 2634260].iloc[0]
deltas = df['delta'].dropna()

troy_delta = troy['delta']
median_delta = deltas.median()
q1 = deltas.quantile(0.25)
q3 = deltas.quantile(0.75)

fig, ax = plt.subplots(figsize=(11, 5.5))

bins = np.linspace(deltas.min() - 0.02, deltas.max() + 0.02, 40)
n, bin_edges, patches = ax.hist(deltas, bins=bins, color='#7BA7CC', edgecolor='white', linewidth=0.5)

# Color Troy's bin red
troy_bin = np.digitize(troy_delta, bin_edges) - 1
troy_bin = min(troy_bin, len(patches) - 1)
patches[troy_bin].set_facecolor('#B02121')

# Quartile + median lines
for val, label, ls in [(q1, 'Q1', '--'), (median_delta, 'Median', '-'), (q3, 'Q3', '--')]:
    ax.axvline(val, color='#555555', linestyle=ls, linewidth=1, alpha=0.7)
    ax.text(val, ax.get_ylim()[1] * 0.97, f' {label}', fontsize=8, color='#555555', va='top')

# Troy annotation — positioned clearly above the bar, not overlapping
ax.annotate(f'Troy\n(Δ = {troy_delta:.3f})',
            xy=(troy_delta, n[troy_bin]),
            xytext=(troy_delta + 0.08, n[troy_bin] + max(n) * 0.15),
            fontsize=10, fontweight='bold', color='#B02121',
            arrowprops=dict(arrowstyle='->', color='#B02121', lw=1.5),
            ha='center', va='bottom')

# Stats line as subtitle, not an overlapping box
ax.set_title(
    'Troy vs. 504 Level-Matched Peers — K-5 ELA Post-COVID Change (SEDA 2025.1)\n'
    f'Troy Δ = {troy_delta:.3f}  |  Median Δ = {median_delta:.3f}  |  '
    f'Troy underperforms median by {abs(troy_delta - median_delta):.3f} grade levels',
    fontsize=12, fontweight='bold', pad=12, linespacing=1.6)

ax.set_xlabel('Post-COVID Δ (SEDA cs_mn_all: grade-level units vs national norm)', fontsize=10)
ax.set_ylabel('Number of districts', fontsize=10)
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=9)

plt.tight_layout()
OUT = os.path.join(CHART_DIR, 'chart_seda_ela_peers.png')
plt.savefig(OUT, dpi=200, bbox_inches='tight', facecolor='white')
print(f'Saved: {OUT}')
plt.close()
