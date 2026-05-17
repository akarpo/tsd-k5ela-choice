# Expanded District Universe for Quantitative Analysis

## Goal
Examine K-5 ELA scores across all relevant districts: Troy's existing peers, other affluent suburban high-performers, demographic-adjusted post-COVID outperformers (Education Scorecard 2026), and sustained outperformers (Steubenville-style 10+ year track records).

## Universe (45 districts)

### Already in workbook (8 districts)
| District | State | Test | Status |
|---|---|---|---|
| Troy SD | MI | M-STEP | Subject district |
| Palo Alto USD | CA | CAASPP | Existing peer (SoR-shift case) |
| Milpitas USD | CA | CAASPP | Existing peer |
| Walnut Valley USD | CA | CAASPP | Existing peer |
| Dublin USD | CA | CAASPP | Existing peer |
| Coppell ISD | TX | STAAR/TAPR | Existing peer |
| West Windsor-Plainsboro | NJ | NJSLA | Existing peer |
| Bellevue SD | WA | SBA | Existing peer (SoR-shift case) |

### Michigan affluent peers — Troy's local comparators (7 to collect)
| District | State | Test | Why |
|---|---|---|---|
| Bloomfield Hills SD | MI | M-STEP | Affluent Oakland County peer |
| Birmingham PS | MI | M-STEP | Affluent Oakland County peer |
| Northville PS | MI | M-STEP | Affluent Oakland/Wayne County peer |
| Novi CSD | MI | M-STEP | Affluent peer, Asian-heavy |
| Rochester CSD | MI | M-STEP | Affluent Oakland County peer |
| West Bloomfield SD | MI | M-STEP | Affluent Oakland County peer |
| Walled Lake CSD | MI | M-STEP | Affluent Oakland County peer |

### SoR-shift peer districts (2 to collect)
| District | State | Test | Why |
|---|---|---|---|
| Lake Washington SD | WA | SBA | Tracking real-time SoR adoption (~Troy demographics) |
| Issaquah SD | WA | SBA | Recent Benchmark Advance adoption |

### DOTR Reading-Only outperformers (3 to collect)
| District | State | Test | Why |
|---|---|---|---|
| Modesto City Elementary | CA | CAASPP | +13 demo-adjusted weeks; Benchmark+UFLI+LETRS |
| West Baton Rouge | LA | LEAP | Wit & Wisdom+Fundations; K-3 57%→68% in 1 yr |
| Roanoke County | VA | SOL | Closest demographic peer; W&W+RGR+Heggerty |

### DOTR Math+Reading outperformers (17 to collect — ELA-relevant subset)
| District | State | Test | Why |
|---|---|---|---|
| Detroit DPSCD | MI | M-STEP | In-state MI validator; EL Education |
| Marion County | KY | KSA | Amplify CKLA + LETRS |
| Baltimore City | MD | MCAP | Wit & Wisdom; large urban proof |
| Atlanta APS | GA | Milestones | +7 NAEP G4 reading 2022-2024 |
| Fond du Lac | WI | Forward | #1 WI reading growth; Amplify CKLA |
| Pierre SD | SD | SBA | Open Court + OG/Heggerty/Barton |
| East Hartford | CT | SBA | Fundamentals Unlimited + Fundations + Heggerty |
| Johnson City | TN | TCAP | TN HQIM mandate |
| Spring Branch ISD | TX | STAAR | High EB population |
| Kuna Joint | ID | ISAT | HMH Into Reading planned |
| Starkville-Oktibbeha | MS | MAAP | MS state mandate |
| East Chicago | IN | ILEARN | Heggerty + Reading Horizons |
| Sikeston R-6 | MO | MAP | State LETRS via Read, Lead, Exceed |
| Wayne County | NC | NCCT | Stayed balanced literacy |
| College Community | IA | ISASP | MTSS focus |
| Dover | NH | SAS | Most Troy-like demographics |
| Brandywine | DE | SBAC | SoR K-2 phonics |

### Sustained outperformers (8 to collect — Steubenville-style)
| District | State | Test | Why |
|---|---|---|---|
| Steubenville City | OH | OST | 25 yrs Success for All; 93-100% G3 reading |
| Aldine ISD | TX | STAAR | Broad Prize 2009; upgraded to CKLA 2020 |
| Seaford SD | DE | SBAC | Exited BL for Bookworms; 32%→53% |
| Brownsville ISD | TX | STAAR | Broad Prize 2008; structured bilingual |
| Sanger Unified | CA | CAASPP | PLC + Open Court; sustained from 2004 |
| Garden Grove USD | CA | CAASPP | Broad Prize 2004; Open Court 20+ years |
| Long Beach USD | CA | CAASPP | Natural experiment: Cohn→TC UoS drift |
| Valley Stream 30 | NY | NYSESLAT | Only BL-using sustained outperformer |

## Methodology

**Data collection priorities (in order):**
1. G3 ELA % proficient (or state equivalent), 2019-2025 all available years
2. G4 + G5 ELA % proficient
3. Key subgroups: All Students, Asian, White, Black, Hispanic/Latino, Econ Disadvantaged, English Learner, SWD
4. State average for relative positioning
5. K-5 ELA curriculum + adoption year + SoR status

**Comparability note:** Within-district trends are valid across states. Absolute % values are NOT cross-state comparable (different tests, different thresholds). State-relative position (district - state) is the best cross-state comparison.

**Output format:** Long-format CSV with columns: district, state, year, test, threshold, grade, subgroup, n_tested, pct_met, source_url.
