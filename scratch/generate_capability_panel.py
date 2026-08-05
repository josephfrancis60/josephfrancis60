"""
generate_capability_panel.py  — fixed version using literal triangle character
"""
import os
import xml.etree.ElementTree as ET

ASSETS_BASE = r"c:\Users\joseph.francis\My Projects\newPersonal\Github README profile\josephfrancis60\assets"
CARDS_DIR = os.path.join(ASSETS_BASE, "cards")
os.makedirs(CARDS_DIR, exist_ok=True)

PANEL_WIDTH = 560
capabilities = [
    "Multi-Agent AI Systems",
    "Workflow Automation",
    "Voice and Conversational AI",
    "AI Integration and API Engineering",
    "Full-Stack AI Applications",
]

line_h  = 28
pad_t   = 52
pad_b   = 18
panel_h = pad_t + len(capabilities) * line_h + pad_b
color   = "#00F0FF"
W       = PANEL_WIDTH

lines_parts = []
y = pad_t
for cap in capabilities:
    # Use plain > as arrow prefix (safe XML), no special unicode entities
    lines_parts.append(
        f'  <text x="28" y="{y}" font-family="Courier New, monospace" '
        f'font-size="12" font-weight="700" letter-spacing="0.5" fill="{color}" '
        f'dominant-baseline="central">&gt; {cap}</text>'
    )
    y += line_h

lines_block = "\n".join(lines_parts)

svg_lines = [
    f'<svg width="{W}" height="{panel_h}" viewBox="0 0 {W} {panel_h}"',
    f'     xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges"',
    f'     role="img" aria-label="SYSTEM CAPABILITIES">',
    f'  <title>SYSTEM CAPABILITIES</title>',
    f'  <!-- Shadow -->',
    f'  <rect x="4" y="4" width="{W-4}" height="{panel_h-4}" fill="#000000" opacity="0.55"/>',
    f'  <!-- Background -->',
    f'  <rect x="0" y="0" width="{W}" height="{panel_h}" fill="#0D0221"/>',
    f'  <!-- Tint -->',
    f'  <rect x="0" y="0" width="{W}" height="{panel_h}" fill="{color}" opacity="0.06"/>',
    f'  <!-- Border -->',
    f'  <rect x="2" y="2" width="{W-4}" height="{panel_h-4}" fill="none" stroke="{color}" stroke-width="2"/>',
    f'  <!-- Top strip -->',
    f'  <rect x="2" y="2" width="{W-4}" height="34" fill="{color}" opacity="0.12"/>',
    f'  <!-- Corner TL -->',
    f'  <rect x="0" y="0" width="10" height="2" fill="{color}"/>',
    f'  <rect x="0" y="0" width="2" height="10" fill="{color}"/>',
    f'  <!-- Corner TR -->',
    f'  <rect x="{W-10}" y="0" width="10" height="2" fill="{color}"/>',
    f'  <rect x="{W-2}" y="0" width="2" height="10" fill="{color}"/>',
    f'  <!-- Corner BL -->',
    f'  <rect x="0" y="{panel_h-2}" width="10" height="2" fill="{color}"/>',
    f'  <rect x="0" y="{panel_h-10}" width="2" height="10" fill="{color}"/>',
    f'  <!-- Corner BR -->',
    f'  <rect x="{W-10}" y="{panel_h-2}" width="10" height="2" fill="{color}"/>',
    f'  <rect x="{W-2}" y="{panel_h-10}" width="2" height="10" fill="{color}"/>',
    f'  <!-- Blink dot -->',
    f'  <rect x="14" y="13" width="6" height="6" fill="{color}">',
    f'    <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>',
    f'  </rect>',
    f'  <!-- Title -->',
    f'  <text x="28" y="20" font-family="Courier New, monospace" font-size="11"',
    f'        font-weight="700" letter-spacing="2" fill="{color}" dominant-baseline="central">',
    f'    // SYSTEM CAPABILITIES',
    f'  </text>',
    f'  <!-- Separator -->',
    f'  <rect x="2" y="36" width="{W-4}" height="1" fill="{color}" opacity="0.4"/>',
    lines_block,
    f'</svg>',
]

svg = "\n".join(svg_lines)

out = os.path.join(CARDS_DIR, "capability-panel.svg")
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)

try:
    ET.parse(out)
    print(f"capability-panel.svg: XML OK  ({len(svg)} bytes)")
except ET.ParseError as e:
    print(f"XML ERROR: {e}")
