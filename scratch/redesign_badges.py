import os

badges_dir = r"c:\Users\joseph.francis\My Projects\newPersonal\Github README profile\josephfrancis60\assets\badges"

# 1. Markdown
markdown_path = os.path.join(badges_dir, "markdown.svg")
if os.path.exists(markdown_path):
    with open(markdown_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Replace #000000 with #FFFFFF, except the shadow one on line 3
    # Let's do selective replace. Line 3 has 'fill="#000000" opacity="0.55"'
    # We can replace opacity="0.14" fill="#000000" or just lines individually.
    lines = content.splitlines()
    for i in range(len(lines)):
        if "opacity=\"0.55\"" not in lines[i]:
            lines[i] = lines[i].replace("#000000", "#FFFFFF")
    with open(markdown_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Redesigned Markdown badge")

# 2. Angular
angular_path = os.path.join(badges_dir, "angular.svg")
if os.path.exists(angular_path):
    with open(angular_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("#0F0F11", "#E23237")
    with open(angular_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Redesigned Angular badge")

# 3. Windows Terminal
win_terminal_path = os.path.join(badges_dir, "winterminal.svg")
if os.path.exists(win_terminal_path):
    with open(win_terminal_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("#4D4D4D", "#3CA4FF")
    with open(win_terminal_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Redesigned Windows Terminal badge")

# 4. Bootstrap
bootstrap_path = os.path.join(badges_dir, "bootstrap.svg")
if os.path.exists(bootstrap_path):
    with open(bootstrap_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("#7952B3", "#9B5DE5")
    with open(bootstrap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Redesigned Bootstrap badge")

# 5. CSS
css_path = os.path.join(badges_dir, "css.svg")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("#663399", "#264DE4")
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Redesigned CSS badge")
