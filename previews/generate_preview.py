#!/usr/bin/env python3
"""Generate the marketing preview cards (preview-day.svg, preview-dark.svg)
from palette.toml, so swatches never drift from the source of truth.

Run:  python3 previews/generate_preview.py
Out:  previews/preview-day.svg, previews/preview-dark.svg
"""

import os

import serene_palette

# Each swatch maps a label to a palette (section, key). Order fills a 6-wide
# grid, row by row. Keys are the canonical roles documented in COLOR_GUIDE.md.
SWATCHES = [
    ("Background", "aged-paper",      "deep-earth"),
    ("Foreground", "warm-ink",        "parchment"),
    ("String",     "forest",          "meadow-sage"),
    ("Keyword",    "olive",           "golden-moss"),
    ("Function",   "bronze",          "honey"),
    ("Type",       "caramel",         "warm-tan"),
    ("Number",     "clay",            "copper"),
    ("Operator",   "charcoal",        "worn-leather"),
    ("Comment",    "weathered-stone", "weathered-stone"),
    ("Error",      "terracotta",      "sunset-clay"),
    ("Selection",  "golden-sand",     "warm-umber"),
]

THEMES = [
    {
        "out": "preview-day.svg",
        "section": "day",
        "swatch_key": 1,                 # index into the (day, night) key pair
        "title": "SERENE DAY",
        "subtitle": "Eye-friendly light theme with warm earth tones",
        "features": ["Reduces glare", "Meets WCAG AA", "~10:1 body-text contrast",
                     "Reduces eye strain", "Warm earth tones", "Perfect for daytime"],
    },
    {
        "out": "preview-dark.svg",
        "section": "night",
        "swatch_key": 2,
        "title": "SERENE NIGHT",
        "subtitle": "Eye-friendly dark theme with warm earth tones",
        "features": ["Low blue-light palette", "Meets WCAG AA", "~10:1 body-text contrast",
                     "Reduces eye strain", "Warm earth tones", "Perfect for evening"],
    },
]

FOOTER = "Available for Wezterm, Helix, VS Code, and Zed"


def build_svg(theme, palette):
    sec = palette[theme["section"]]
    bg = sec["aged-paper"] if theme["section"] == "day" else sec["deep-earth"]
    fg = sec["warm-ink"] if theme["section"] == "day" else sec["parchment"]
    muted = sec["weathered-stone"]                       # label / caption color
    ki = theme["swatch_key"]

    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg width="1200" height="630" xmlns="http://www.w3.org/2000/svg">',
        '  <defs>',
        '    <style>',
        "      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;display=swap');",
        "      .sans { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }",
        '      .title { font-size: 56px; font-weight: 700; letter-spacing: -2px; }',
        '      .subtitle { font-size: 20px; font-weight: 400; letter-spacing: -0.5px; }',
        '      .label { font-size: 13px; font-weight: 500; text-transform: uppercase; letter-spacing: 1px; }',
        "      .hex { font-family: 'SF Mono', Monaco, 'Courier New', monospace; font-size: 12px; font-weight: 400; }",
        '    </style>',
        '  </defs>',
        '',
        f'  <rect width="1200" height="630" fill="{bg}"/>',
        '',
        f'  <text x="80" y="100" class="sans title" fill="{fg}">{theme["title"]}</text>',
        f'  <text x="80" y="135" class="sans subtitle" fill="{muted}">{theme["subtitle"]}</text>',
        '',
        '  <g transform="translate(80, 200)">',
    ]

    for i, (label, day_key, night_key) in enumerate(SWATCHES):
        key = (day_key, night_key)[ki - 1]
        color = sec[key]
        col, row = i % 6, i // 6
        x, y = col * 120, row * 180
        cx = x + 45
        ly, hy = y + 115, y + 135
        stroke = ' stroke="{}" stroke-width="1.5"'.format(muted) if label == "Background" else ""
        out.append(f'    <rect x="{x}" y="{y}" width="90" height="90" rx="8" fill="{color}"{stroke}/>')
        out.append(f'    <text x="{cx}" y="{ly}" class="sans label" fill="{muted}" text-anchor="middle">{label}</text>')
        out.append(f'    <text x="{cx}" y="{hy}" class="hex" fill="{muted}" text-anchor="middle" opacity="0.7">{color}</text>')

    out.append('  </g>')
    out.append('')
    out.append('  <g transform="translate(820, 200)">')
    out.append(f'    <text y="30" class="sans label" fill="{muted}">KEY FEATURES</text>')
    out.append('')
    out.append(f'    <text y="70" class="sans" fill="{fg}" font-size="16" font-weight="400">')
    for j, feat in enumerate(theme["features"]):
        dy = 0 if j == 0 else 35
        out.append(f'      <tspan x="0" dy="{dy}">✓ {feat}</tspan>')
    out.append('    </text>')
    out.append('  </g>')
    out.append('')
    out.append(f'  <text x="80" y="600" class="sans" fill="{muted}" font-size="14" opacity="0.7">{FOOTER}</text>')
    out.append('</svg>')
    return "\n".join(out) + "\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    palette = serene_palette.load_palette()
    for theme in THEMES:
        path = os.path.join(here, theme["out"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_svg(theme, palette))
        print(f"Wrote {os.path.relpath(path)}")


if __name__ == "__main__":
    main()
