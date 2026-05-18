"""Find Troy's K-5 ELA peers from the full SEDA 2025.1 dataset.

Mirrors the methodology from the G6-G7 Math analysis:
  - Subject: rla (ELA/reading)
  - Grades: 3, 4, 5 (SEDA doesn't have K-2 test data)
  - Peer selection: pre-COVID (2017-2019) cs_mn_all within ±0.25 of Troy
  - Minimum enrollment: ≥150 tested per grade-year
  - Must have data for 2017-2019 AND 2022-2025
  - Rank all peers by post-COVID delta (post minus pre)
"""
import csv
from collections import defaultdict

SEDA_FILE = "/Users/Alex/Downloads/tsd-g6g7math-choice/seda_admindist_long_cs_2025.1.csv"

def safe_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None

def avg(vals):
    vals = [v for v in vals if v is not None]
    return sum(vals) / len(vals) if vals else None

GRADES = ("3", "4", "5")
PRE_YEARS = ("2017", "2018", "2019")
POST_YEARS = ("2022", "2023", "2024", "2025")

print("Scanning full SEDA file for ELA grades 3-5...")
districts = defaultdict(dict)

row_count = 0
with open(SEDA_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row_count += 1
        if row["subject"] != "rla":
            continue
        if row["grade"] not in GRADES:
            continue
        sid = row["sedaadmin"]
        gr = row["grade"]
        yr = row["year"]
        districts[sid][(gr, yr)] = {
            "name": row["sedaadminname"],
            "state": row["stateabb"],
            "cs_all": safe_float(row["cs_mn_all"]),
            "cs_asn": safe_float(row["cs_mn_asn"]),
            "cs_wht": safe_float(row["cs_mn_wht"]),
            "cs_ecd": safe_float(row["cs_mn_ecd"]),
            "cs_nec": safe_float(row["cs_mn_nec"]),
            "cs_blk": safe_float(row["cs_mn_blk"]),
            "cs_hsp": safe_float(row["cs_mn_hsp"]),
            "n_all": safe_float(row["tot_asmt_all"]),
            "n_asn": safe_float(row["tot_asmt_asn"]),
        }

print(f"Scanned {row_count:,} rows, found {len(districts):,} districts with G3-5 ELA data")

# Compute metrics for each district
results = []
for sid, data in districts.items():
    name = None
    state = None
    for k, v in data.items():
        name = v["name"]
        state = v["state"]
        break

    # Pre-COVID: 2017-2019, grades 3-5 pooled
    pre_vals = []
    pre_n = []
    for gr in GRADES:
        for yr in PRE_YEARS:
            d = data.get((gr, yr))
            if d and d["cs_all"] is not None:
                pre_vals.append(d["cs_all"])
            if d and d["n_all"] is not None:
                pre_n.append(d["n_all"])
    pre_avg = avg(pre_vals) if len(pre_vals) >= 4 else None
    pre_n_avg = avg(pre_n) if pre_n else None

    # Post-COVID: 2022-2025, grades 3-5 pooled
    post_vals = []
    for gr in GRADES:
        for yr in POST_YEARS:
            d = data.get((gr, yr))
            if d and d["cs_all"] is not None:
                post_vals.append(d["cs_all"])
    post_avg = avg(post_vals) if len(post_vals) >= 4 else None

    # Asian subgroup
    asn_pre = []
    for gr in GRADES:
        for yr in PRE_YEARS:
            d = data.get((gr, yr))
            if d and d["cs_asn"] is not None:
                asn_pre.append(d["cs_asn"])
    asn_pre_avg = avg(asn_pre) if len(asn_pre) >= 2 else None

    asn_post = []
    for gr in GRADES:
        for yr in POST_YEARS:
            d = data.get((gr, yr))
            if d and d["cs_asn"] is not None:
                asn_post.append(d["cs_asn"])
    asn_post_avg = avg(asn_post) if len(asn_post) >= 2 else None

    # White subgroup
    wht_pre = []
    for gr in GRADES:
        for yr in PRE_YEARS:
            d = data.get((gr, yr))
            if d and d["cs_wht"] is not None:
                wht_pre.append(d["cs_wht"])
    wht_pre_avg = avg(wht_pre) if len(wht_pre) >= 2 else None

    wht_post = []
    for gr in GRADES:
        for yr in POST_YEARS:
            d = data.get((gr, yr))
            if d and d["cs_wht"] is not None:
                wht_post.append(d["cs_wht"])
    wht_post_avg = avg(wht_post) if len(wht_post) >= 2 else None

    # ECD subgroup
    ecd_pre = []
    for gr in GRADES:
        for yr in PRE_YEARS:
            d = data.get((gr, yr))
            if d and d["cs_ecd"] is not None:
                ecd_pre.append(d["cs_ecd"])
    ecd_pre_avg = avg(ecd_pre) if len(ecd_pre) >= 2 else None

    ecd_post = []
    for gr in GRADES:
        for yr in POST_YEARS:
            d = data.get((gr, yr))
            if d and d["cs_ecd"] is not None:
                ecd_post.append(d["cs_ecd"])
    ecd_post_avg = avg(ecd_post) if len(ecd_post) >= 2 else None

    # Asian enrollment share
    asn_n_vals = [data.get((gr, yr), {}).get("n_asn")
                  for gr in GRADES for yr in ("2018", "2019")]
    all_n_vals = [data.get((gr, yr), {}).get("n_all")
                  for gr in GRADES for yr in ("2018", "2019")]
    asn_n = sum(v for v in asn_n_vals if v) if any(v for v in asn_n_vals) else 0
    all_n = sum(v for v in all_n_vals if v) if any(v for v in all_n_vals) else 0
    asn_share = asn_n / all_n if all_n > 0 else 0

    if pre_avg is not None and post_avg is not None:
        delta = post_avg - pre_avg
        asn_delta = (asn_post_avg - asn_pre_avg) if (asn_post_avg is not None and asn_pre_avg is not None) else None
        wht_delta = (wht_post_avg - wht_pre_avg) if (wht_post_avg is not None and wht_pre_avg is not None) else None
        ecd_delta = (ecd_post_avg - ecd_pre_avg) if (ecd_post_avg is not None and ecd_pre_avg is not None) else None

        results.append({
            "sid": sid,
            "name": name,
            "state": state,
            "pre_avg": pre_avg,
            "post_avg": post_avg,
            "delta": delta,
            "pre_n_avg": pre_n_avg,
            "asn_share": asn_share,
            "asn_pre": asn_pre_avg,
            "asn_post": asn_post_avg,
            "asn_delta": asn_delta,
            "wht_pre": wht_pre_avg,
            "wht_post": wht_post_avg,
            "wht_delta": wht_delta,
            "ecd_pre": ecd_pre_avg,
            "ecd_post": ecd_post_avg,
            "ecd_delta": ecd_delta,
        })

print(f"\n{len(results):,} districts with complete pre/post-COVID ELA G3-5 data")

# Find Troy
troy = next(r for r in results if r["sid"] == "2634260")
print(f"\nTroy SD: pre={troy['pre_avg']:+.3f}, post={troy['post_avg']:+.3f}, "
      f"Δ={troy['delta']:+.3f}, Asian share={troy['asn_share']:.1%}")

# === PEER SET: Level-matched (±0.25 of Troy's pre-COVID ELA) ===
TROY_PRE = troy["pre_avg"]
MIN_N = 150
peers = [r for r in results
         if abs(r["pre_avg"] - TROY_PRE) <= 0.25
         and (r["pre_n_avg"] or 0) >= MIN_N]
peers.sort(key=lambda x: x["delta"])

print(f"\n{'='*110}")
print(f"ELA PEER SET: Districts with pre-COVID G3-5 ELA within ±0.25 of Troy ({TROY_PRE:+.3f})")
print(f"Enrollment ≥{MIN_N}/grade-year — {len(peers)} districts found")
print(f"{'='*110}")

troy_rank = next(i for i, r in enumerate(peers, 1) if r["sid"] == "2634260")
pct = troy_rank / len(peers) * 100
print(f"\nTroy rank: {troy_rank} of {len(peers)} (1=worst decline, {pct:.0f}th percentile)")

# Show distribution
print(f"\n{'Rank':<5} {'District':<45} {'State':>5} {'Pre':>8} {'Post':>8} {'Δ':>8} {'Asn%':>6} {'N':>6}")
print("-" * 100)
show_indices = (
    list(range(min(15, len(peers))))
    + list(range(max(0, troy_rank-6), min(len(peers), troy_rank+5)))
    + list(range(max(0, len(peers)-15), len(peers)))
)
show_indices = sorted(set(show_indices))
last_i = -1
for i in show_indices:
    if i > last_i + 1:
        print("  ...")
    r = peers[i]
    marker = " <<<" if r["sid"] == "2634260" else ""
    print(f" {i+1:<4} {r['name']:<45} {r['state']:>5} "
          f"{r['pre_avg']:+.3f}  {r['post_avg']:+.3f}  {r['delta']:+.3f}  "
          f"{r['asn_share']:>5.1%}  {r['pre_n_avg']:>5.0f}{marker}")
    last_i = i

# Compare to math peer set
print(f"\n\n{'='*110}")
print("COMPARISON: ELA vs Math peer selection")
print(f"{'='*110}")

# Check overlap with math peers
math_peers_file = "/Users/Alex/Downloads/tsd-g6g7math-choice/data/seda_math_peers_full.csv"
math_peer_sids = set()
with open(math_peers_file) as f:
    for row in csv.DictReader(f):
        math_peer_sids.add(row["sid"])

ela_peer_sids = {r["sid"] for r in peers}
overlap = ela_peer_sids & math_peer_sids
ela_only = ela_peer_sids - math_peer_sids
math_only = math_peer_sids - ela_peer_sids

print(f"\nMath peers (G6-G7): {len(math_peer_sids)}")
print(f"ELA peers (G3-5):  {len(ela_peer_sids)}")
print(f"Overlap:           {len(overlap)}")
print(f"ELA-only:          {len(ela_only)}")
print(f"Math-only:         {len(math_only)}")
print(f"Overlap rate:      {len(overlap)/len(ela_peer_sids):.0%} of ELA peers are also math peers")

# MI peers specifically
mi_peers = [r for r in peers if r["state"] == "MI"]
mi_peers.sort(key=lambda x: x["delta"])
print(f"\n\nMichigan districts in ELA peer set: {len(mi_peers)}")
mi_troy_rank = next(i for i, r in enumerate(mi_peers, 1) if r["sid"] == "2634260")
print(f"Troy rank among MI peers: {mi_troy_rank} of {len(mi_peers)}")
print(f"\n{'Rank':<5} {'District':<45} {'Pre':>8} {'Post':>8} {'Δ':>8}")
print("-" * 80)
for i, r in enumerate(mi_peers):
    marker = " <<<" if r["sid"] == "2634260" else ""
    print(f" {i+1:<4} {r['name']:<45} "
          f"{r['pre_avg']:+.3f}  {r['post_avg']:+.3f}  {r['delta']:+.3f}{marker}")

# Quartile analysis
n = len(peers)
q1 = peers[n//4]["delta"]
q2 = peers[n//2]["delta"]
q3 = peers[3*n//4]["delta"]
print(f"\n\nDistribution of post-COVID Δ across {n} ELA peers:")
print(f"  Q1 (25th pct): {q1:+.3f}")
print(f"  Median:        {q2:+.3f}")
print(f"  Q3 (75th pct): {q3:+.3f}")
print(f"  Troy:          {troy['delta']:+.3f} (rank {troy_rank}, {pct:.0f}th percentile)")

# Troy subgroup comparison
print(f"\n\nTroy subgroup deltas vs peer medians:")
for sub, key in [("All", "delta"), ("Asian", "asn_delta"), ("White", "wht_delta"), ("ECD", "ecd_delta")]:
    troy_val = troy.get(key)
    peer_vals = sorted([r[key] for r in peers if r.get(key) is not None])
    if peer_vals and troy_val is not None:
        med = peer_vals[len(peer_vals)//2]
        rank = sum(1 for v in peer_vals if v < troy_val) + 1
        print(f"  {sub:<10} Troy={troy_val:+.3f}  Median={med:+.3f}  Rank {rank}/{len(peer_vals)}")

# Write full peer data to CSV
OUT = "/Users/Alex/Downloads/tsd-k5ela-choice/data/seda_ela_peers_full.csv"
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["sid", "name", "state", "pre_avg", "post_avg",
                                       "delta", "pre_n_avg", "asn_share",
                                       "asn_pre", "asn_post", "asn_delta",
                                       "wht_pre", "wht_post", "wht_delta",
                                       "ecd_pre", "ecd_post", "ecd_delta"])
    w.writeheader()
    for r in peers:
        w.writerow(r)
print(f"\n\nWrote {len(peers)} level-matched ELA peers to {OUT}")
