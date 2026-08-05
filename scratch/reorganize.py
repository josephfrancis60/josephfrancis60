import os
import shutil

base_dir = r"c:\Users\joseph.francis\My Projects\newPersonal\Github README profile\josephfrancis60\assets"

folders = ["banners", "tabs", "cards", "decorations", "social"]
for f in folders:
    os.makedirs(os.path.join(base_dir, f), exist_ok=True)

# Move banner-header.svg and banner-footer.svg
for banner in ["banner-header.svg", "banner-footer.svg"]:
    src = os.path.join(base_dir, banner)
    dst = os.path.join(base_dir, "banners", banner)
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"Moved {banner} to banners/")

# Move social badges
badges_dir = os.path.join(base_dir, "badges")
for filename in os.listdir(badges_dir):
    if filename.startswith("social-"):
        src = os.path.join(badges_dir, filename)
        dst = os.path.join(base_dir, "social", filename)
        shutil.move(src, dst)
        print(f"Moved {filename} to social/")
