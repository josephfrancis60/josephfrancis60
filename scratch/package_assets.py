"""
Package all the new/modified assets into a ZIP for easy review/distribution.
"""
import os
import zipfile

REPO_ROOT = r"c:\Users\joseph.francis\My Projects\newPersonal\Github README profile\josephfrancis60"
OUTPUT_ZIP = os.path.join(REPO_ROOT, "dashboard-assets.zip")

include_dirs = [
    "assets/banners",
    "assets/tabs",
    "assets/cards",
    "assets/decorations",
    "assets/social",
    "assets/metrics",
]

include_files = [
    ".github/workflows/metrics.yml",
    "README.md",
]

with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
    # Specific directories
    for dir_rel in include_dirs:
        dir_abs = os.path.join(REPO_ROOT, dir_rel)
        if not os.path.isdir(dir_abs):
            continue
        for filename in os.listdir(dir_abs):
            fpath = os.path.join(dir_abs, filename)
            if os.path.isfile(fpath):
                arcname = os.path.join(dir_rel, filename)
                zf.write(fpath, arcname)
                print(f"  +  {arcname}")

    # Individual files
    for frel in include_files:
        fabs = os.path.join(REPO_ROOT, frel)
        if os.path.isfile(fabs):
            zf.write(fabs, frel)
            print(f"  +  {frel}")

    # All redesigned badges (the modified ones + all badge files)
    badges_dir = os.path.join(REPO_ROOT, "assets", "badges")
    for fname in os.listdir(badges_dir):
        fpath = os.path.join(badges_dir, fname)
        if os.path.isfile(fpath):
            zf.write(fpath, os.path.join("assets/badges", fname))
            print(f"  +  assets/badges/{fname}")

print(f"\nZIP created: {OUTPUT_ZIP}")
print(f"Size: {os.path.getsize(OUTPUT_ZIP):,} bytes")
