#!/usr/bin/env python3
"""Render a syntax-highlighted code sample as SVG for each variant, using the
real editor backgrounds and (for clarity variants) the tint backgrounds behind
colored tokens.

Run:  python3 previews/generate_sample.py
Out:  previews/syntax-sample.svg
"""

import os

import serene_palette

# --- Code sample as (role, text) tokens ------------------------------------
# Roles: cm comment, kw keyword, fl flow-control, fn function, ty type,
#        st string, nu number, cn constant, op operator, pu punctuation,
#        va variable, pr property, ws whitespace.
LINES = [
    [("cm", "// Serene theme syntax highlighting sample")],
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
_R = serene_palette.resolve()
DAY_BG, NIGHT_BG = serene_palette.backgrounds()

# short token code -> serene_palette role (pr/property shares variable, fg is body)
_CODE_ROLE = {
    "cm": "comment", "st": "string", "kw": "keyword", "fl": "flow",
    "fn": "function", "ty": "type", "nu": "number", "cn": "constant",
    "op": "operator", "pu": "punctuation", "va": "variable", "pr": "variable",
    "fg": "body",
}
DAY = {code: _R[role]["day"] for code, role in _CODE_ROLE.items()}
NIGHT = {code: _R[role]["night"] for code, role in _CODE_ROLE.items()}

# clarity tints exist only for these token codes
_CLARITY_CODES = ("st", "kw", "fn", "ty", "nu", "cn", "fl")
CLAR_DAY = {c: _R[_CODE_ROLE[c]]["day_clarity"] for c in _CLARITY_CODES}
CLAR_NIGHT = {c: _R[_CODE_ROLE[c]]["night_clarity"] for c in _CLARITY_CODES}

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


def build_svg(day_fg, night_fg, heading, subtitle):
    py0 = HEADER
    py1 = HEADER + PANEL_H + 28
    height = py1 + PANEL_H + 56
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" '
        f'viewBox="0 0 {W} {height}" font-family="{SANS}">',
        f'<rect width="{W}" height="{height}" fill="{PAGE}"/>',
        f'<text x="24" y="36" font-size="20" font-weight="700" fill="{INK}">{esc(heading)}</text>',
        f'<text x="24" y="60" font-size="13" fill="{MUTED}">{esc(subtitle)}</text>',
    ]
    c0, c1 = 24, 24 + PANEL_W + GAP
    parts.append(panel(c0, py0, "Day (Regular)", DAY_BG, day_fg, None, False))
    parts.append(panel(c1, py0, "Day (Clarity)", DAY_BG, day_fg, CLAR_DAY, False))
    parts.append(panel(c0, py1, "Night (Regular)", NIGHT_BG, night_fg, None, True))
    parts.append(panel(c1, py1, "Night (Clarity)", NIGHT_BG, night_fg, CLAR_NIGHT, True))
    parts.append(f'<text x="24" y="{height - 22}" font-size="11.5" fill="{MUTED}">'
                 f'Regular = foreground colors only · Clarity = subtle tint behind '
                 f'strings, keywords, functions, types, numbers, constants and flow-control.</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "syntax-sample.svg")
    heading = "Serene syntax sample"
    subtitle = ("Same snippet across all four variants, on the real editor "
                "backgrounds. Every key token meets WCAG AA (4.5:1).")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_svg(DAY, NIGHT, heading, subtitle))
    print(f"Wrote {os.path.relpath(path)}")


if __name__ == "__main__":
    main()
