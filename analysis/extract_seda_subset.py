"""Extract the 50-district SEDA subset used in this analysis.

This script:
1. Downloads the SEDA 2025.1 administrative-district long file (~88 MB).
2. Filters to the 50 target districts by NCES LEA ID.
3. Pools G3-G5 ELA scores by district × year × subgroup (n-weighted).
4. Writes seda_2025_pooled.json and seda_2025_state.json.

Source: Reardon, S. F., et al. (2026). Stanford Education Data Archive
v2025.1. https://edopportunity.org/trends/data/downloads/

Usage:
    python3 extract_seda_subset.py
"""

import csv
import json
import os
import urllib.request
from statistics import mean

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
SEDA_URL = "https://stacks.stanford.edu/file/hm970gr1371/seda_admindist_long_cs_2025.1.csv"
STATE_URL = "https://stacks.stanford.edu/file/hm970gr1371/seda_state_long_cs_2025.1.csv"

# 50 target districts, keyed by NCES LEA ID (sedaadmin in SEDA 2025.1)
TARGETS = {
    "2634260": "Troy SD",
    # MI affluent peers
    "2606090": "Bloomfield Hills", "2605850": "Birmingham PS",
    "2625980": "Northville PS", "2626130": "Novi CSD",
    "2629940": "Rochester CSD", "2635160": "Walled Lake CSD",
    "2635820": "West Bloomfield SD",
    # In-state MI outperformer
    "2601103": "Detroit DPSCD",
    # CA workbook peers + outperformers
    "629610": "Palo Alto USD", "624500": "Milpitas USD",
    "641280": "Walnut Valley USD", "600019": "Dublin USD",
    "622500": "Long Beach Unified", "614880": "Garden Grove Unified",
    "625130": "Modesto City Elem", "635250": "Sanger Unified",
    # TX districts
    "4807710": "Aldine ISD", "4811680": "Brownsville ISD",
    "4815210": "Coppell ISD", "4835100": "Plano ISD",
    "4820010": "Frisco ISD", "4841100": "Spring Branch ISD",
    # NJ
    "3417700": "West Windsor-Plainsboro", "3410200": "Millburn Twp",
    "3413410": "Princeton PS",
    # WA SoR-shift peers
    "5300390": "Bellevue SD", "5303750": "Issaquah SD",
    "5304230": "Lake Washington SD",
    # Sustained outperformers + DOTR
    "3904482": "Steubenville City", "2201920": "West Baton Rouge",
    "2103780": "Marion County", "4702130": "Johnson City",
    "1300120": "Atlanta PS", "2400090": "Baltimore City PS",
    "5504680": "Fond du Lac SD", "1001530": "Seaford SD",
    "1001240": "Brandywine SD", "5103330": "Roanoke County PS",
    "901260": "East Hartford SD", "3629490": "Valley Stream UFSD 30",
    "4203570": "Bethlehem Area SD", "1802880": "East Chicago",
    "2928260": "Sikeston R-6", "3704880": "Wayne County PS",
    "3302640": "Dover SD", "1907860": "College Community SD",
    "1601770": "Kuna Joint", "4655260": "Pierre SD",
    "2800189": "Starkville-Oktibbeha",
}
TARGET_STATES = {"MI", "CA", "TX", "NJ", "WA", "OH", "LA", "KY", "TN",
                 "GA", "MD", "WI", "DE", "VA", "CT", "NY", "PA", "IN",
                 "MO", "NC", "NH", "IA", "ID", "SD", "MS"}


def safe_float(v):
    if v in ("", None):
        return None
    try:
        return float(v)
    except ValueError:
        return None


def download(url, dest):
    if os.path.exists(dest):
        print(f"  Already have: {dest}")
        return
    print(f"  Downloading: {url}")
    urllib.request.urlretrieve(url, dest)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # Step 1: Download SEDA files
    seda_path = os.path.join(OUT_DIR, "_raw_seda_admindist.csv")
    state_path = os.path.join(OUT_DIR, "_raw_seda_state.csv")
    print("Downloading SEDA 2025.1 raw files (~93 MB total)…")
    download(SEDA_URL, seda_path)
    download(STATE_URL, state_path)

    # Step 2: Extract target districts, ELA (rla) only, G3-G5 only
    print(f"\nExtracting {len(TARGETS)} target districts, ELA G3-G5…")
    rows = []
    with open(seda_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["sedaadmin"] not in TARGETS:
                continue
            if row["subject"] != "rla":
                continue
            if row["grade"] not in ("3", "4", "5"):
                continue
            rows.append(row)
    print(f"  Extracted {len(rows)} rows")

    # Step 3: Pool G3-G5 by district × year × subgroup (n-weighted)
    by_dist_year = {}
    SUBGROUPS = ["all", "asn", "blk", "hsp", "wht", "ecd", "nec"]
    for r in rows:
        key = (TARGETS[r["sedaadmin"]], int(r["year"]))
        by_dist_year.setdefault(key, []).append({
            sg: safe_float(r.get(f"cs_mn_{sg}")) for sg in SUBGROUPS
        } | {
            "n_all": safe_float(r.get("tot_asmt_all")) or 0,
        })

    def pool(sg, grade_vals):
        nums, dens = 0.0, 0.0
        for gv in grade_vals:
            if gv[sg] is not None and gv["n_all"] > 0:
                nums += gv[sg] * gv["n_all"]
                dens += gv["n_all"]
        return nums / dens if dens > 0 else None

    pooled = {}
    for (district, year), gvs in by_dist_year.items():
        pooled.setdefault(district, {})[str(year)] = {
            sg: pool(sg, gvs) for sg in SUBGROUPS
        }

    out_pooled = os.path.join(OUT_DIR, "seda_2025_pooled.json")
    with open(out_pooled, "w") as f:
        json.dump(pooled, f, indent=2, default=str)
    print(f"  Wrote {out_pooled}")

    # Step 4: State-level G3-G5 means (for state-relative position)
    print("\nExtracting state-level G3-G5 ELA means…")
    state_data = {}
    with open(state_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["subject"] != "rla":
                continue
            if row["grade"] not in ("3", "4", "5"):
                continue
            st = row["stateabb"]
            if st not in TARGET_STATES:
                continue
            v = safe_float(row.get("cs_mn_all"))
            if v is None:
                continue
            state_data.setdefault((st, int(row["year"])), []).append(v)
    state_pooled = {f"{st}_{y}": mean(vs) for (st, y), vs in state_data.items()}
    out_state = os.path.join(OUT_DIR, "seda_2025_state.json")
    with open(out_state, "w") as f:
        json.dump(state_pooled, f, indent=2)
    print(f"  Wrote {out_state}")
    print(f"\nDone. {len(pooled)} districts × years pooled.")


if __name__ == "__main__":
    main()
