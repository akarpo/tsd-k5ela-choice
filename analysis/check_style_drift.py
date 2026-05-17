"""Style-drift scanner for the deck build script.

Run this whenever you edit `build_deck.py` or any chart-generation script.
It flags the patterns that have historically broken the deck:

  1. Raw hex colors (#RRGGBB) outside the palette block.
  2. Hand-padded monospace tables (a string literal where multiple lines
     contain runs of 4+ spaces — almost always a fake column).
  3. add_text() calls that place content below y=7.05 (the footer band),
     unless the call is inside the footer() function definition itself.

Exit code is 1 if any HIGH-confidence problem is found.

This script is intentionally conservative — it under-reports rather than
over-reports. The goal is to catch the patterns I keep regressing on, not
to do a full layout audit.
"""
import argparse
import re
import sys


PALETTE = {
    "#1F3A5F",  # TROY_BLUE
    "#C8302F",  # ACCENT_RED
    "#1F7A3D",  # ACCENT_GREEN
    "#B7791F",  # ACCENT_ORANGE
    "#5E2D8C",  # ACCENT_PURPLE
    "#E8F5EE",  # LIGHT_GREEN
    "#FFF4E0",  # LIGHT_ORANGE
    "#FBE7E6",  # LIGHT_RED
    "#F2F4F7",  # GRAY_LIGHT
    "#333333",  # GRAY_DARK
    "#777777",  # GRAY_MID
    "#FFFFFF",  # WHITE
    "#555",     # chart axis
    "#666",     # chart axis (state All)
    "#999933",  # defenses background (kept for now)
    "#996633",  # defenses background (kept for now)
    "#993322",  # defenses background (kept for now)
    "#003366",  # defenses background (kept for now)
    "#DC3545",  # CHART_RED (Troy / protagonist)
    "#28A745",  # CHART_GREEN (Spring Branch / biggest gainer)
    "#4A90D9",  # CHART_BLUE (Palo Alto / Calkins-exit)
    "#F0A030",  # CHART_AMBER (West Baton Rouge / W&W)
    "#9B59B6",  # CHART_PURPLE (Johnson City / 5th series)
    "#6C757D",  # CHART_GRAY (BL peers / neutral)
    "#ADB5BD",  # CHART_GRAY_LIGHT (secondary neutral)
    "#CC4444",  # BL-stayed bars on chart11
}


def _footer_def_range(src):
    """Return (start_line, end_line) of the `def footer(` definition, or None.

    We exempt this range from the footer-collision check because that function
    is *what defines* the footer at y=7.15. Flagging it would be circular.
    """
    lines = src.split("\n")
    start = None
    for i, line in enumerate(lines, 1):
        if re.match(r'\s*def\s+footer\s*\(', line):
            start = i
            break
    if start is None:
        return None
    # End of def = next non-indented line, or EOF.
    end = len(lines)
    for j in range(start, len(lines)):
        line = lines[j]
        if j > start and line and not line[0].isspace():
            end = j
            break
    return (start, end)


def _enclosing_add_text_uses_consolas(src, line_no):
    """Heuristic: walk backward from `line_no` to find the nearest add_text(...)
    call header. If that call (anywhere in its argument list, even across lines)
    contains font="Consolas", treat the inner string literal as a legitimate
    monospace use and skip it.
    """
    lines = src.split("\n")
    # Look back up to 30 lines for an add_text( opener.
    for k in range(line_no - 1, max(0, line_no - 30) - 1, -1):
        if "add_text(" in lines[k]:
            # Take that line plus the next ~12 (typical call spans <12 lines).
            chunk = "\n".join(lines[k:min(len(lines), k + 14)])
            if 'font="Consolas"' in chunk or "font='Consolas'" in chunk:
                return True
            # Stop searching past the first add_text we find.
            return False
    return False


def scan(path):
    with open(path) as f:
        src = f.read()
    lines = src.split("\n")
    issues = []
    footer_range = _footer_def_range(src)

    # 1) raw hex outside palette
    palette_upper = {p.upper() for p in PALETTE}
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("#"):
            continue  # comments
        for m in re.finditer(r'"(#[0-9A-Fa-f]{3,6})"', line):
            hx = m.group(1)
            if hx.upper() not in palette_upper:
                issues.append((i, "HEX_OUTSIDE_PALETTE",
                               f'raw color "{hx}" not in palette'))

    # 2) hand-padded monospace tables
    block = []
    for i, line in enumerate(lines, 1):
        if '"""' in line:
            continue
        if ('"' in line
                and re.search(r'    [^ ]', line)
                and 'Consolas' not in line
                and 'font=' not in line):
            block.append((i, line))
        else:
            if len(block) >= 3 and all('    ' in l for _, l in block):
                first_line_no = block[0][0]
                if not _enclosing_add_text_uses_consolas(src, first_line_no):
                    issues.append((first_line_no,
                                   "POSSIBLE_MONOSPACE_DRIFT",
                                   f"{len(block)} consecutive lines with run "
                                   f"of spaces — verify alignment"))
            block = []

    # 3) add_text below y=7.05 — but skip calls inside the footer() definition.
    for m in re.finditer(
            r'add_text\([^)]*Inches\(([\d.]+)\),\s*Inches\(([\d.]+)\)', src):
        y = float(m.group(2))
        if y > 7.05:
            line_no = src[:m.start()].count("\n") + 1
            if footer_range and footer_range[0] <= line_no <= footer_range[1]:
                continue  # the footer band itself — expected
            issues.append((line_no, "CONTENT_BELOW_FOOTER",
                           f"y={y} > 7.05; will collide with footer"))

    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default="analysis/build_deck.py")
    args = ap.parse_args()

    issues = scan(args.path)
    if not issues:
        print(f"OK — no drift detected in {args.path}")
        return 0

    by_kind = {}
    for line, kind, msg in issues:
        by_kind.setdefault(kind, []).append((line, msg))

    print(f"{len(issues)} style-drift findings in {args.path}:\n")
    for kind, items in by_kind.items():
        print(f"  [{kind}]  ({len(items)})")
        for line, msg in items[:6]:
            print(f"    L{line}:  {msg}")
        if len(items) > 6:
            print(f"    ... and {len(items)-6} more")
        print()

    # exit non-zero only on the highest-confidence categories
    if "CONTENT_BELOW_FOOTER" in by_kind:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
