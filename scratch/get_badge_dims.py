import os
import re

dir_path = r"c:\Users\joseph.francis\My Projects\newPersonal\Github README profile\josephfrancis60\assets\badges"
for filename in os.listdir(dir_path):
    if filename.endswith(".svg"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'<svg[^>]*width="([\d\.]+)"[^>]*height="([\d\.]+)"', content)
            if match:
                print(f"{filename}: width={match.group(1)}, height={match.group(2)}")
            else:
                print(f"{filename}: No match")
