"""Pull SWD M-STEP data for Troy's 7 MI affluent peer districts.

Uses the mischooldata scraper. Outputs peer_swd_ela.csv with:
  school_year, district, grade, swd_pct, non_swd_pct, all_pct
"""
import csv, os, sys, time
sys.path.insert(0, "/Users/Alex/Downloads/tools-mischooldata")
from mischooldata import MiSchoolDataReport

URL = "https://www.mischooldata.org/grades-3-8-state-testing-includes-psat-data-proficiency/"

# Oakland ISD = 106 for all except Northville (Wayne RESA = 119)
PEERS = [
    ("106", "943",  "Birmingham PS"),
    ("106", "947",  "Bloomfield Hills"),
    ("106", "1435", "Novi CSD"),
    ("106", "1518", "Rochester CSD"),
    ("106", "1640", "Walled Lake CSD"),
    ("106", "1658", "West Bloomfield SD"),
    ("119", "1430", "Northville PS"),
]

YEARS = [
    ("26", "2024-25"),
    ("25", "2023-24"),
    ("24", "2022-23"),
    ("23", "2021-22"),
    ("22", "2020-21"),
    ("20", "2018-19"),
    ("19", "2017-18"),
    ("18", "2016-17"),
    ("15", "2015-16"),
]
GRADES = [("Grade03", 3), ("Grade04", 4), ("Grade05", 5)]


def pct_to_float(s):
    s = (s or "").strip().rstrip("%").replace(",", "")
    if not s or s == "*" or s.lower() in ("ns", "n/a", "<5", ">95"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def parse_tables(tables, dist_name_fragment):
    out = {"swd_pct": None, "non_swd_pct": None, "all_pct": None, "state_swd_pct": None}
    for t in tables:
        for row in t:
            if len(row) < 5:
                continue
            # SWD/non-SWD rows: [DistrictName, AssessProg, Subject, Category, %Prof, ...]
            if len(row) >= 11 and row[2] == "English Language Arts":
                if row[3] == "Students With Disabilities" and "%" in str(row[4]):
                    out["swd_pct"] = pct_to_float(row[4])
                elif row[3] == "Students Without Disabilities" and "%" in str(row[4]):
                    out["non_swd_pct"] = pct_to_float(row[4])
            # Peer/comparison table: [LocType, Name, Prog, Subject, Category, %Prof, ...]
            if len(row) >= 12:
                if row[0] == "District" and row[4] == "All Students" and "%" in str(row[5]):
                    out["all_pct"] = pct_to_float(row[5])
                # State SWD row
                if row[0] == "Statewide" and row[3] == "English Language Arts":
                    if row[4] == "Students With Disabilities" and "%" in str(row[5]):
                        out["state_swd_pct"] = pct_to_float(row[5])
                    elif row[4] == "All Students" and "%" in str(row[5]):
                        if out.get("state_all_pct") is None:
                            out["state_all_pct"] = pct_to_float(row[5])
    return out


def main():
    rows = []
    out_path = os.path.join(os.path.dirname(__file__), "..", "data", "peer_swd_ela.csv")

    with MiSchoolDataReport(URL, headless=True, step_pause_ms=4000,
                            report_pause_ms=10000) as r:
        r.select("assessmentPrograms", "Mstep")
        r.select("subjects", "Ela")

        current_isd = None
        current_dist = None

        for isd_code, dist_code, dist_label in PEERS:
            print(f"\n=== {dist_label} (ISD={isd_code}, dist={dist_code}) ===")
            if isd_code != current_isd:
                r.select("isds", isd_code)
                current_isd = isd_code
                time.sleep(2)
            r.select("districts", dist_code)
            current_dist = dist_code
            time.sleep(1)

            for year_code, year_label in YEARS:
                r.select("schoolYears", year_code)
                for grade_code, grade_int in GRADES:
                    r.select("grades", grade_code)
                    r.select("reportCategories", "StudentsWithDisabilities")
                    cls, txt = r.view_button_state()
                    if "disabled" in cls:
                        print(f"  {year_label} G{grade_int}: disabled, skip")
                        continue
                    t0 = time.time()
                    r.fire_report()
                    tables = r.results_tables(min_rows=1)
                    parsed = parse_tables(tables, dist_label)
                    parsed.update({
                        "school_year": year_label,
                        "district": dist_label,
                        "grade": grade_int,
                    })
                    rows.append(parsed)
                    print(f"  {year_label} G{grade_int}: SWD={parsed['swd_pct']}%  "
                          f"non-SWD={parsed['non_swd_pct']}%  All={parsed['all_pct']}%  "
                          f"State-SWD={parsed.get('state_swd_pct')}%  "
                          f"({time.time()-t0:.0f}s)")

                    with open(out_path, "w", newline="") as f:
                        w = csv.DictWriter(f, fieldnames=[
                            "school_year", "district", "grade",
                            "swd_pct", "non_swd_pct", "all_pct",
                            "state_swd_pct", "state_all_pct",
                        ], extrasaction="ignore")
                        w.writeheader()
                        for r2 in rows:
                            w.writerow(r2)

    print(f"\nDone — {len(rows)} rows -> {out_path}")


if __name__ == "__main__":
    main()
