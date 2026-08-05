import os
import base64

ASSETS_BASE = r"c:\Users\joseph.francis\My Projects\newPersonal\Github README profile\josephfrancis60\assets"
BADGES_DIR  = os.path.join(ASSETS_BASE, "badges")
CARDS_DIR   = os.path.join(ASSETS_BASE, "cards")
os.makedirs(CARDS_DIR, exist_ok=True)

# Badge dimensions (from script output)
BADGE_DIMS = {
    "angular": (118, 33), "angularjs": (132, 33), "arduino": (118, 33),
    "azure": (103, 33), "bootstrap": (132, 33), "canva": (103, 33),
    "claude": (110, 33), "cplusplus": (88, 33), "csharp": (80, 33),
    "css": (95, 33), "docker": (110, 33), "dotnet": (95, 33),
    "elevenlabs": (140, 33), "express": (118, 33), "fastapi": (118, 33),
    "figma": (103, 33), "flask": (103, 33), "git": (88, 33),
    "github": (110, 33), "gnubash": (95, 33), "googlecloud": (155, 33),
    "html5": (103, 33), "javascript": (140, 33), "jwt": (88, 33),
    "kubernetes": (140, 33), "langchain": (132, 33), "langgraph": (132, 33),
    "markdown": (125, 33), "mssql": (110, 33), "mui": (88, 33),
    "mysql": (103, 33), "n8n": (88, 33), "netlify": (118, 33),
    "nextjs": (118, 33), "nodedotjs": (118, 33), "npm": (88, 33),
    "openapiinitiative": (118, 33), "postgresql": (140, 33), "postman": (118, 33),
    "powerbi": (125, 33), "powershell": (140, 33), "python": (110, 33),
    "raspberrypi": (155, 33), "react": (103, 33), "render": (110, 33),
    "sqlite": (110, 33), "swagger": (118, 33), "twilio": (110, 33),
    "typescript": (140, 33), "vercel": (110, 33), "vite": (95, 33),
    "winterminal": (155, 33),
}

CARD_WIDTH  = 380
GAP         = 6    # px between badges
BADGE_H     = 33
PAD_TOP     = 52   # space from top for header + decorations
PAD_LEFT    = 14
PAD_BOT     = 14
ACCENT_COLORS = {
    "ai":        "#FF2E88",
    "build":     "#00F0FF",
    "cloud":     "#4D9FFF",
    "data":      "#9B5DE5",
    "toolkit":   "#FFD700",
    "languages": "#39FF14",
}

CARDS = {
    "ai": {
        "title": "AI SYSTEMS",
        "color": ACCENT_COLORS["ai"],
        "badges": ["n8n", "langchain", "langgraph", "claude", "elevenlabs"],
    },
    "build": {
        "title": "BUILD STACK",
        "color": ACCENT_COLORS["build"],
        "badges": ["react", "nextjs", "dotnet", "nodedotjs", "express", "fastapi", "flask", "vite", "angular", "bootstrap"],
    },
    "cloud": {
        "title": "INFRASTRUCTURE",
        "color": ACCENT_COLORS["cloud"],
        "badges": ["docker", "kubernetes", "azure", "googlecloud", "github", "git", "vercel", "render", "netlify"],
    },
    "data": {
        "title": "DATA",
        "color": ACCENT_COLORS["data"],
        "badges": ["postgresql", "mssql", "mysql", "sqlite", "jwt"],
    },
    "toolkit": {
        "title": "CREATOR TOOLKIT",
        "color": ACCENT_COLORS["toolkit"],
        "badges": ["postman", "swagger", "openapiinitiative", "figma", "canva", "powerbi", "twilio", "arduino", "raspberrypi"],
    },
    "languages": {
        "title": "LANGUAGES",
        "color": ACCENT_COLORS["languages"],
        "badges": ["python", "csharp", "cplusplus", "typescript", "javascript", "html5", "css", "markdown", "gnubash", "powershell"],
    },
}

def layout_badges(badges, card_width, pad_left, gap):
    """Pack badges into rows, centre each row."""
    rows = []
    current_row = []
    current_w = 0
    inner_w = card_width - 2 * pad_left

    for badge in badges:
        bw, bh = BADGE_DIMS.get(badge, (110, 33))
        needed = bw + (gap if current_row else 0)
        if current_w + needed > inner_w and current_row:
            rows.append(current_row)
            current_row = [badge]
            current_w = bw
        else:
            current_row.append(badge)
            current_w += needed
    if current_row:
        rows.append(current_row)
    return rows

def get_badge_base64(badge_name):
    badge_path = os.path.join(BADGES_DIR, f"{badge_name}.svg")
    if os.path.exists(badge_path):
        with open(badge_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/svg+xml;base64,{encoded}"
    return ""

def render_card(key, cfg):
    color = cfg["color"]
    title = cfg["title"]
    badges = cfg["badges"]

    rows = layout_badges(badges, CARD_WIDTH, PAD_LEFT, GAP)
    inner_w = CARD_WIDTH - 2 * PAD_LEFT

    # calculate total height
    total_rows = len(rows)
    card_height = PAD_TOP + total_rows * (BADGE_H + GAP) - GAP + PAD_BOT

    # Build badge image elements
    badge_imgs = []
    y = PAD_TOP
    for row in rows:
        row_total_w = sum(BADGE_DIMS.get(b, (110, 33))[0] for b in row) + GAP * (len(row) - 1)
        x = PAD_LEFT + (inner_w - row_total_w) // 2   # centre align
        for badge in row:
            bw, bh = BADGE_DIMS.get(badge, (110, 33))
            
            # Embed badge as base64
            href = get_badge_base64(badge)
            
            badge_imgs.append(
                f'  <image href="{href}" x="{x}" y="{y}" width="{bw}" height="{bh}"/>'
            )
            x += bw + GAP
        y += BADGE_H + GAP

    badge_block = "\n".join(badge_imgs)

    svg = f"""<svg width="{CARD_WIDTH}" height="{card_height}" viewBox="0 0 {CARD_WIDTH} {card_height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" shape-rendering="crispEdges" role="img" aria-label="{title}">
  <title>{title}</title>
  <!-- Shadow -->
  <rect x="4" y="4" width="{CARD_WIDTH - 4}" height="{card_height - 4}" fill="#000000" opacity="0.55"/>
  <!-- Background -->
  <rect x="0" y="0" width="{CARD_WIDTH}" height="{card_height}" fill="#0D0221"/>
  <!-- Color tint -->
  <rect x="0" y="0" width="{CARD_WIDTH}" height="{card_height}" fill="{color}" opacity="0.06"/>
  <!-- Outer border -->
  <rect x="2" y="2" width="{CARD_WIDTH - 4}" height="{card_height - 4}" fill="none" stroke="{color}" stroke-width="2"/>
  <!-- Top accent strip -->
  <rect x="2" y="2" width="{CARD_WIDTH - 4}" height="34" fill="{color}" opacity="0.12"/>
  <!-- Corner TL -->
  <rect x="0"  y="0"  width="10" height="2"  fill="{color}"/>
  <rect x="0"  y="0"  width="2"  height="10" fill="{color}"/>
  <!-- Corner TR -->
  <rect x="{CARD_WIDTH - 10}" y="0"            width="10" height="2"  fill="{color}"/>
  <rect x="{CARD_WIDTH - 2}"  y="0"            width="2"  height="10" fill="{color}"/>
  <!-- Corner BL -->
  <rect x="0"                  y="{card_height - 2}"  width="10" height="2"  fill="{color}"/>
  <rect x="0"                  y="{card_height - 10}" width="2"  height="10" fill="{color}"/>
  <!-- Corner BR -->
  <rect x="{CARD_WIDTH - 10}"  y="{card_height - 2}"  width="10" height="2"  fill="{color}"/>
  <rect x="{CARD_WIDTH - 2}"   y="{card_height - 10}" width="2"  height="10" fill="{color}"/>
  <!-- Status dot -->
  <rect x="14" y="13" width="6" height="6" fill="{color}">
    <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
  </rect>
  <!-- Title -->
  <text x="28" y="20" font-family="'Courier New', monospace" font-size="11" font-weight="700" letter-spacing="2" fill="{color}" dominant-baseline="central">// {title}</text>
  <!-- Separator line -->
  <rect x="2" y="36" width="{CARD_WIDTH - 4}" height="1" fill="{color}" opacity="0.4"/>
  <!-- Badges -->
{badge_block}
</svg>"""
    return svg

for key, cfg in CARDS.items():
    svg_content = render_card(key, cfg)
    out_path = os.path.join(CARDS_DIR, f"card-{key}.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Created card-{key}.svg (base64 embedded)")

print("Cards successfully regenerated with base64 embedded badges!")
