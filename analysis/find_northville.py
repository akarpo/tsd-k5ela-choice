"""Find Northville's district code — likely Wayne RESA (ISD 133)."""
import sys, time
from mischooldata import MiSchoolDataReport

URL = "https://www.mischooldata.org/grades-3-8-state-testing-includes-psat-data-proficiency/"

with MiSchoolDataReport(URL, headless=False, step_pause_ms=3000,
                        report_pause_ms=8000) as r:
    # Try Wayne RESA
    r.select("isds", "119")
    time.sleep(3)
    options = r.page.query_selector_all("#districts option")
    print(f"Wayne RESA ({len(options)} districts):")
    for opt in options:
        val = opt.get_attribute("value")
        text = opt.inner_text().strip()
        if "north" in text.lower():
            print(f"  value={val:>6s}  text={text}")
