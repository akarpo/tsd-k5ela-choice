"""Rebuild chart19_ckla_cohort_effect.png — clean version without overlapping annotations."""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

CHART_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'charts')
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'seda_2009_2025_extract.csv')

df = pd.read_csv(DATA, low_memory=False)
df['cs_mn_all'] = pd.to_numeric(df['cs_mn_all'], errors='coerce')
df['tot_asmt_all'] = pd.to_numeric(df['tot_asmt_all'], errors='coerce')

DISTRICTS = {
    2634260: ('Troy SD MI (Calkins UoS)', '#B02121', '-'),
    2103780: ('Marion County KY (CKLA + LETRS, ~2022)', '#1F7A3D', '-'),
    5504680: ('Fond du Lac WI (CKLA + weekly PD)', '#CC6A11', '-'),
}

fig, ax = plt.subplots(figsize=(10.5, 5.25))

for sid, (label, color, ls) in DISTRICTS.items():
    sub = df[(df['sedaadmin'] == sid) & (df['subject'] == 'rla') & (df['grade'].isin([3, 4, 5]))]
    yearly = sub.groupby('year').apply(
        lambda g: np.average(g['cs_mn_all'].dropna(), weights=g.loc[g['cs_mn_all'].notna(), 'tot_asmt_all'])
        if g['cs_mn_all'].notna().any() else np.nan
    ).dropna()
    ax.plot(yearly.index, yearly.values, color=color, linestyle=ls, linewidth=2.5,
            marker='o', markersize=4, label=label, zorder=3)

# Shade COVID gap
ax.axvspan(2019.5, 2021.5, color='#dddddd', alpha=0.5, zorder=1)
ax.text(2020.5, ax.get_ylim()[1] * 0.95, 'COVID\ngap', ha='center', va='top',
        fontsize=8, color='#888888', style='italic')

# CKLA adoption annotation — arrow only, no overlapping box
# Marion County adopted CKLA ~2022
ax.annotate('CKLA adopted\n~2022',
            xy=(2022, 0.15), xytext=(2016, 0.42),
            fontsize=9, color='#1F7A3D', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#1F7A3D', lw=1.5),
            ha='center', va='bottom')

# Troy peak annotation
troy_sub = df[(df['sedaadmin'] == 2634260) & (df['subject'] == 'rla') & (df['grade'].isin([3, 4, 5]))]
troy_yearly = troy_sub.groupby('year').apply(
    lambda g: np.average(g['cs_mn_all'].dropna(), weights=g.loc[g['cs_mn_all'].notna(), 'tot_asmt_all'])
    if g['cs_mn_all'].notna().any() else np.nan
).dropna()
peak_year = troy_yearly.idxmax()
peak_val = troy_yearly.max()
current_val = troy_yearly.iloc[-1] if len(troy_yearly) > 0 else 0
decline = current_val - peak_val

ax.annotate(f'Troy: {decline:+.2f} from {int(peak_year)} peak',
            xy=(troy_yearly.index[-1], current_val),
            xytext=(troy_yearly.index[-1] - 3, current_val + 0.15),
            fontsize=9, color='#B02121', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#B02121', lw=1.5),
            ha='center', va='bottom')

ax.set_title(
    'CKLA cohort effect arriving — Marion County and Fond du Lac, 2009-2025\n'
    'Both districts on MDE Section 35m-equivalent list with Amplify CKLA',
    fontsize=12, fontweight='bold', pad=10, linespacing=1.5)
ax.set_xlabel('Year', fontsize=10)
ax.set_ylabel('SEDA cs G3-G5 ELA (grade-level units vs national norm)', fontsize=10)
ax.legend(loc='lower left', fontsize=9, framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=9)
ax.set_xticks(range(2009, 2026))
ax.set_xticklabels([str(y) for y in range(2009, 2026)], fontsize=8, rotation=45, ha='right')

plt.tight_layout()
OUT = os.path.join(CHART_DIR, 'chart19_ckla_cohort_effect.png')
plt.savefig(OUT, dpi=200, bbox_inches='tight', facecolor='white')
print(f'Saved: {OUT}')
plt.close()
