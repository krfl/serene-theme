#!/usr/bin/env python3
"""Generates theme files from templates + palette.toml."""

import os
import re
import sys
import tomllib


def parse_palette(path):
    """Parse palette.toml."""
    with open(path, "rb") as f:
        return tomllib.load(f)


def apply_filter(value, filt):
    """Apply a filter to a hex color value."""
    if filt == "nohash":
        return value.lstrip("#")
    if filt.startswith("alpha:"):
        alpha = filt.split(":")[1]
        return value + alpha
    raise ValueError(f"Unknown filter: {filt}")


def render(content, palette):
    """Replace {{section.color-name}} and {{section.color-name|filter}} placeholders."""

    def replacer(match):
        ref = match.group(1)
        parts = [p.strip() for p in ref.split("|")]
        color_ref = parts[0]
        filters = parts[1:]

        if "." not in color_ref:
            raise ValueError(f"Invalid reference '{color_ref}' (expected section.color)")
        section, color = color_ref.split(".", 1)
        if section not in palette:
            raise ValueError(f"Unknown section: {section}")
        if color not in palette[section]:
            raise ValueError(f"Unknown color '{color}' in [{section}]")

        value = palette[section][color]
        for filt in filters:
            value = apply_filter(value, filt)
        return value

    return re.sub(r"\{\{(.+?)\}\}", replacer, content)


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    palette_path = os.path.join(root, "palette.toml")
    templates_dir = os.path.join(root, "templates")
    themes_dir = os.path.join(root, "themes")

    if not os.path.exists(palette_path):
        print("Error: palette.toml not found", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(templates_dir):
        print("Error: templates/ directory not found", file=sys.stderr)
        sys.exit(1)

    palette = parse_palette(palette_path)

    count = 0
    errors = 0
    for dirpath, _, filenames in os.walk(templates_dir):
        for filename in sorted(filenames):
            template_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(template_path, templates_dir)
            output_path = os.path.join(themes_dir, rel_path)

            with open(template_path, encoding="utf-8") as f:
                content = f.read()

            try:
                rendered = render(content, palette)
            except ValueError as e:
                print(f"  ERROR {rel_path}: {e}", file=sys.stderr)
                errors += 1
                continue

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(rendered)

            count += 1
            print(f"  {rel_path}")

    print(f"\nGenerated {count} files.", end="")
    if errors:
        print(f" {errors} errors.", end="")
    print()

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
