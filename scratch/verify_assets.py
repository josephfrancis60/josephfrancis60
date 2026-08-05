"""
verify_assets.py - Quick XML & path validation
"""
import os
import xml.etree.ElementTree as ET

REPO = r"c:\Users\joseph.francis\My Projects\newPersonal\Github README profile\josephfrancis60"

CHECK_DIRS = [
    "assets/banners",
    "assets/tabs",
    "assets/cards",
    "assets/decorations",
    "assets/social",
    "assets/badges",
]

ok = 0
errors = []

for rel_dir in CHECK_DIRS:
    abs_dir = os.path.join(REPO, rel_dir)
    if not os.path.isdir(abs_dir):
        errors.append(f"MISSING DIR: {rel_dir}")
        continue
    for fname in sorted(os.listdir(abs_dir)):
        if not fname.endswith(".svg"):
            continue
        fpath = os.path.join(abs_dir, fname)
        try:
            ET.parse(fpath)
            ok += 1
            print(f"  OK  {rel_dir}/{fname}")
        except ET.ParseError as e:
            errors.append(f"XML ERROR in {rel_dir}/{fname}: {e}")
            print(f"  !!  {rel_dir}/{fname}  ->  {e}")

# Check workflow files
for wf_rel in [".github/workflows/snake.yml", ".github/workflows/metrics.yml"]:
    wf = os.path.join(REPO, wf_rel)
    if os.path.isfile(wf):
        print(f"  OK  {wf_rel}")
    else:
        errors.append(f"MISSING: {wf_rel}")

# Check README references (only paths that should be in README)
readme = os.path.join(REPO, "README.md")
if os.path.isfile(readme):
    with open(readme, encoding="utf-8") as f:
        content = f.read()
    required_refs = [
        "banner-header.svg", "banner-footer.svg",
        "tab-about.svg", "tab-mission-control.svg",
        "tab-contributions.svg", "tab-performance.svg",
        "capability-panel.svg",
        "card-ai.svg", "card-build.svg", "card-cloud.svg",
        "card-data.svg", "card-toolkit.svg", "card-languages.svg",
        "github-contribution-grid-snake-dark-1.svg",
        "metrics-activity.svg",
        "metrics-languages.svg",
        "metrics-achievements.svg",
        "metrics-discussions.svg",
    ]
    for token in required_refs:
        if token not in content:
            errors.append(f"README missing reference: {token}")
    print(f"  OK  README.md ({len(content):,} bytes, {content.count(chr(10))+1} lines)")
else:
    errors.append("MISSING: README.md")

# Summary
print(f"\n{'='*40}")
print(f"SVGs validated OK : {ok}")
if errors:
    print(f"Issues            : {len(errors)}")
    for e in errors:
        print(f"  !! {e}")
else:
    print("All checks passed!")
