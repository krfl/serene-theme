#!/usr/bin/env python3
"""Shared palette access for the preview generators.

Holds the single syntax-role -> palette-key mapping so no generator hardcodes
hex values. Reads ../palette.toml, the project's source of truth.
"""

import os
import tomllib

# palette -> role -> (day_fg_key, night_fg_key, day_tint_key | None, night_tint_key | None)
ROLE_KEYS = {
    "fallow": {
        "body":        ("warm-ink",        "parchment",       None,              None),
        "comment":     ("weathered-stone", "weathered-stone", None,              None),
        "string":      ("forest",          "meadow-sage",     "sage-mist",       "moss-shadow"),
        "keyword":     ("olive",           "golden-moss",     "olive-mist",      "olive-shadow"),
        "function":    ("bronze",          "honey",           "bronze-mist",     "amber-shadow"),
        "type":        ("caramel",         "warm-tan",        "caramel-mist",    "earth-shadow"),
        "number":      ("clay",            "copper",          "bronze-mist",     "amber-shadow"),
        "constant":    ("clay",            "copper",          "bronze-mist",     "amber-shadow"),
        "flow":        ("terracotta",      "sunset-clay",     "terracotta-mist", "umber-shadow"),
        "operator":    ("charcoal",        "worn-leather",    None,              None),
        "punctuation": ("taupe",           "dry-clay",        None,              None),
        "variable":    ("taupe",           "pale-hide",       None,              None),
    },
    "meadow": {
        "body":        ("warm-ink",        "parchment",       None,              None),
        "comment":     ("weathered-stone", "weathered-stone", None,              None),
        "string":      ("leaf",            "leaf",            "leaf-mist",       "leaf-shadow"),
        "keyword":     ("plum",            "plum",            "plum-mist",       "plum-shadow"),
        "function":    ("slate-blue",      "slate-blue",      "slate-mist",      "slate-shadow"),
        "type":        ("ochre",           "ochre",           "ochre-mist",      "ochre-shadow"),
        "number":      ("cinnamon",        "cinnamon",        "cinnamon-mist",   "cinnamon-shadow"),
        "constant":    ("cinnamon",        "cinnamon",        "cinnamon-mist",   "cinnamon-shadow"),
        "flow":        ("spruce",          "spruce",          "spruce-mist",     "spruce-shadow"),
        "operator":    ("charcoal",        "worn-leather",    None,              None),
        "punctuation": ("taupe",           "dry-clay",        None,              None),
        "variable":    ("taupe",           "pale-hide",       None,              None),
    },
}
BG_KEYS = {"day": "aged-paper", "night": "deep-earth"}


def load_palette():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "..", "palette.toml"), "rb") as f:
        return tomllib.load(f)


def resolve(name, palette=None):
    """role -> dict(day, night, day_clarity, night_clarity) of hex values for one palette."""
    p = palette or load_palette()
    d, n, dc, nc = p["day"], p["night"], p["day-clarity"], p["night-clarity"]
    out = {}
    for role, (dk, nk, dck, nck) in ROLE_KEYS[name].items():
        out[role] = {
            "day": d[dk],
            "night": n[nk],
            "day_clarity": dc[dck] if dck else None,
            "night_clarity": nc[nck] if nck else None,
        }
    return out


def backgrounds(palette=None):
    """Return (day_bg, night_bg) hex values."""
    p = palette or load_palette()
    return p["day"][BG_KEYS["day"]], p["night"][BG_KEYS["night"]]
