"""Find the correct district codes from the MI School Data dropdown."""
import sys, time
from mischooldata import MiSchoolDataReport

URL = "https://www.mischooldata.org/grades-3-8-state-testing-includes-psat-data-proficiency/"

with MiSchoolDataReport(URL, headless=False, step_pause_ms=3000,
                        report_pause_ms=8000) as r:
    r.select("isds", "106")
    time.sleep(3)
    # Get all district options
    options = r.page.query_selector_all("#districts option")
    print(f"Found {len(options)} districts in Oakland ISD:")
    for opt in options:
        val = opt.get_attribute("value")
        text = opt.inner_text().strip()
        if any(k in text.lower() for k in ["birm", "bloom", "north", "novi", "roch", "wall", "west bloom", "troy"]):
            print(f"  value={val:>6s}  text={text}")
