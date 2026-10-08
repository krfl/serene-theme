#!/usr/bin/env python3
"""Render a syntax-highlighted code sample as SVG for each palette, using the
real editor backgrounds and the tints behind colored tokens, with the palette
shown as swatches underneath.

Run:  python3 previews/generate_sample.py
Out:  previews/syntax-sample-fallow.svg, previews/syntax-sample-meadow.svg
"""

import os

import serene_palette

# --- Code sample as (role, text) tokens ------------------------------------
# Roles: cm comment, kw keyword, fl flow-control, fn function, ty type,
#        st string, nu number, cn constant, op operator, pu punctuation,
#        va variable, pr property, ws whitespace.
LINES = [
    [("cm", "// Serene syntax highlighting sample")],
    [],
    [("kw", "import"), ("ws", " "), ("pu", "{"), ("ws", " "), ("fn", "readFile"),
     ("ws", " "), ("pu", "}"), ("ws", " "), ("kw", "from"), ("ws", " "), ("st", '"fs/promises"')],
    [],
    [("kw", "const"), ("ws", " "), ("cn", "MAX_RETRIES"), ("ws", " "), ("op", "="), ("ws", " "), ("nu", "3")],
    [("kw", "let"), ("ws", " "), ("va", "palette"), ("op", ":"), ("ws", " "),
     ("ty", "Palette"), ("ws", " "), ("op", "="), ("ws", " "), ("cn", "null")],
    [],
    [("kw", "interface"), ("ws", " "), ("ty", "Theme"), ("ws", " "), ("pu", "{")],
    [("ws", "  "), ("pr", "name"), ("op", ":"), ("ws", " "), ("ty", "string")],
    [("ws", "  "), ("pr", "contrast"), ("op", ":"), ("ws", " "), ("ty", "number")],
    [("pu", "}")],
    [],
    [("kw", "function"), ("ws", " "), ("fn", "loadTheme"), ("pu", "("), ("va", "path"),
     ("op", ":"), ("ws", " "), ("ty", "string"), ("pu", ")"), ("op", ":"), ("ws", " "),
     ("ty", "Theme"), ("ws", " "), ("pu", "{")],
    [("ws", "  "), ("kw", "const"), ("ws", " "), ("va", "raw"), ("ws", " "), ("op", "="),
     ("ws", " "), ("fn", "readFile"), ("pu", "("), ("va", "path"), ("pu", ")")],
    [("ws", "  "), ("kw", "if"), ("ws", " "), ("pu", "("), ("va", "raw"), ("ws", " "),
     ("op", "==="), ("ws", " "), ("cn", "null"), ("pu", ")"), ("ws", " "), ("pu", "{")],
    [("ws", "    "), ("fl", "throw"), ("ws", " "), ("kw", "new"), ("ws", " "),
     ("ty", "Error"), ("pu", "("), ("st", '"missing theme"'), ("pu", ")")],
    [("ws", "  "), ("pu", "}")],
    [("ws", "  "), ("fl", "return"), ("ws", " "), ("fn", "parse"), ("pu", "("), ("va", "raw"), ("pu", ")")],
    [("pu", "}")],
]

# --- Color tables ----------------------------------------------------------
# Built from palette.toml via serene_palette; no hex is hardcoded here.
DAY_BG, NIGHT_BG = serene_palette.backgrounds()

# short token code -> serene_palette role (pr/property shares variable, fg is body)
_CODE_ROLE = {
    "cm": "comment", "st": "string", "kw": "keyword", "fl": "flow",
    "fn": "function", "ty": "type", "nu": "number", "cn": "constant",
    "op": "operator", "pu": "punctuation", "va": "variable", "pr": "variable",
    "fg": "body",
}
# tints exist only for these token codes
_TINT_CODES = ("st", "kw", "fn", "ty", "nu", "cn", "fl")


def colors(name):
    """(day_fg, night_fg, day_tint, night_tint) maps for one palette."""
    r = serene_palette.resolve(name)
    day = {code: r[role]["day"] for code, role in _CODE_ROLE.items()}
    night = {code: r[role]["night"] for code, role in _CODE_ROLE.items()}
    day_tint = {c: r[_CODE_ROLE[c]]["day_clarity"] for c in _TINT_CODES}
    night_tint = {c: r[_CODE_ROLE[c]]["night_clarity"] for c in _TINT_CODES}
    return day, night, day_tint, night_tint


# --- Palette legend ----------------------------------------------------------
# Shown under the code panels. A string is a role from serene_palette.ROLE_KEYS,
# drawn on its tint if it has one. A (day_key, night_key) pair is a plain
# palette color, drawn on the editor background.
_BASE_TOP = [("Background", ("aged-paper", "deep-earth")),
             ("Text", ("warm-ink", "parchment")),
             ("Selection", ("golden-sand", "warm-umber")),
             ("Comment", "comment")]
_BASE_END = [("Operator", "operator"),
             ("Punctuation", "punctuation"),
             ("Variable, property", "variable")]
LEGEND = {
    "fallow": _BASE_TOP + [
        ("String", "string"),
        ("Keyword", "keyword"),
        ("Function", "function"),
        ("Type", "type"),
        ("Number, constant", "number"),
        ("Flow, namespace, error", "flow"),
    ] + _BASE_END,
    "meadow": _BASE_TOP + [
        ("String", "string"),
        ("Keyword", "keyword"),
        ("Function", "function"),
        ("Type", "type"),
        ("Number, constant", "number"),
        ("Flow, namespace", "flow"),
        ("Error", ("poppy", "poppy")),
    ] + _BASE_END,
}
LEGEND_ROW = 54


# --- Layout ----------------------------------------------------------------
W = 1012
PANEL_W, PANEL_H = 470, 422
GAP = 24
HEADER = 86
CHARW = 7.8
LH = 19
FS = 13
CODE_PAD = 18
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, Segoe UI, Roboto, sans-serif"
PAGE = "#faf8f4"
INK = "#3d3a33"
MUTED = "#8a826f"
CARD_STROKE = "#e6e3dd"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def panel(px, py, title, base_bg, fg, clarity_bg, is_night):
    out = [f'<g transform="translate({px},{py})">']
    out.append(f'<rect x="0" y="0" width="{PANEL_W}" height="{PANEL_H}" rx="10" '
               f'fill="{base_bg}" stroke="{CARD_STROKE}"/>')
    # title bar in panel-fg so it reads on the real background
    out.append(f'<text x="{CODE_PAD}" y="26" font-family="{SANS}" font-size="13" '
               f'font-weight="600" fill="{fg["fg"]}" opacity="0.75">{esc(title)}</text>')

    code_x = CODE_PAD
    code_y = 44
    for i, line in enumerate(LINES):
        top = code_y + i * LH
        baseline = top + 14
        col = 0
        for role, text in line:
            n = len(text)
            if role == "ws":
                col += n
                continue
            x = code_x + col * CHARW
            if clarity_bg and role in clarity_bg:
                out.append(f'<rect x="{x:.1f}" y="{top + 1}" width="{n * CHARW:.1f}" '
                           f'height="{LH - 1}" fill="{clarity_bg[role]}"/>')
            style = ' font-style="italic"' if role == "cm" else ""
            out.append(f'<text x="{x:.1f}" y="{baseline}" font-family="{MONO}" '
                       f'font-size="{FS}" fill="{fg[role]}"{style} '
                       f'xml:space="preserve">{esc(text)}</text>')
            col += n
    out.append("</g>")
    return "\n".join(out)


def legend(px, py, title, name, section, bg, palette):
    """One swatch per color: the color as a small square on its tint, or on the
    editor background when it has no tint."""
    roles = serene_palette.resolve(name, palette)
    items = LEGEND[name]
    out = [f'<g transform="translate({px},{py})">',
           f'<text x="0" y="0" font-size="13" font-weight="600" fill="{INK}">{esc(title)}</text>']
    rows = (len(items) + 1) // 2
    for i, (label, ref) in enumerate(items):
        if isinstance(ref, str):
            color = roles[ref][section]
            back = roles[ref][f"{section}_clarity"] or bg
        else:
            color = palette[section][ref[0] if section == "day" else ref[1]]
            back = bg
        x = (i // rows) * (PANEL_W // 2)
        y = 18 + (i % rows) * LEGEND_ROW
        out.append(f'<rect x="{x}" y="{y}" width="44" height="44" rx="12" fill="{back}" stroke="{CARD_STROKE}"/>')
        edge = f' stroke="{MUTED}" stroke-opacity="0.5"' if color == back else ""
        out.append(f'<rect x="{x + 11}" y="{y + 11}" width="22" height="22" rx="7" fill="{color}"{edge}/>')
        out.append(f'<text x="{x + 56}" y="{y + 19}" font-size="13" font-weight="500" fill="{INK}">{esc(label)}</text>')
        hexes = color if back == bg else f"{color} on {back}"
        out.append(f'<text x="{x + 56}" y="{y + 37}" font-family="{MONO}" font-size="12" fill="{MUTED}">{hexes}</text>')
    out.append("</g>")
    return "\n".join(out), 18 + rows * LEGEND_ROW


def build_svg(name, heading, subtitle):
    day_fg, night_fg, day_tint, night_tint = colors(name)
    title = name.capitalize()
    palette = serene_palette.load_palette()
    py0 = HEADER
    py1 = HEADER + PANEL_H + 28
    c0, c1 = 24, 24 + PANEL_W + GAP
    day_legend, legend_h = legend(c0, py1 + PANEL_H + 48, f"{title} Day colors", name, "day", DAY_BG, palette)
    night_legend, _ = legend(c1, py1 + PANEL_H + 48, f"{title} Night colors", name, "night", NIGHT_BG, palette)
    height = py1 + PANEL_H + 48 + legend_h + 48
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" '
        f'viewBox="0 0 {W} {height}" font-family="{SANS}">',
        f'<rect width="{W}" height="{height}" fill="{PAGE}"/>',
        f'<text x="24" y="36" font-size="20" font-weight="700" fill="{INK}">{esc(heading)}</text>',
        f'<text x="24" y="60" font-size="13" fill="{MUTED}">{esc(subtitle)}</text>',
    ]
    parts.append(panel(c0, py0, f"{title} Day", DAY_BG, day_fg, day_tint, False))
    parts.append(panel(c1, py0, f"{title} Day Alt", DAY_BG, day_fg, None, False))
    parts.append(panel(c0, py1, f"{title} Night", NIGHT_BG, night_fg, night_tint, True))
    parts.append(panel(c1, py1, f"{title} Night Alt", NIGHT_BG, night_fg, None, True))
    parts.append(day_legend)
    parts.append(night_legend)
    parts.append(f'<text x="24" y="{height - 22}" font-size="11.5" fill="{MUTED}">'
                 f'The default puts a soft tint behind strings, keywords, functions, types, '
                 f'numbers, constants and flow control. Alt leaves it out.</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    subtitle = ("Same snippet in Day and Night, with and without tints, on the real editor "
                "backgrounds. Every key token meets WCAG AA (4.5:1).")
    for name in serene_palette.ROLE_KEYS:
        path = os.path.join(here, f"syntax-sample-{name}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_svg(name, f"Serene {name.capitalize()}", subtitle))
        print(f"Wrote {os.path.relpath(path)}")


if __name__ == "__main__":
    main()
