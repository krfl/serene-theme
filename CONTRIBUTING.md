# Contributing

Thanks for wanting to help out. This file covers how the build works and a few rules. For the actual colors, see [COLOR_GUIDE.md](COLOR_GUIDE.md). For the why behind them, see the [README](README.md).

## How it works

Every color lives in `palette.toml`. The files in `templates/` are theme files with placeholders like `{{day.forest}}` instead of hex codes. Running the build fills them in and writes the result to `themes/`, using the same folder layout.

```sh
python3 build.py                      # rebuild everything in themes/ (needs Python 3.11+)
python3 previews/generate_preview.py  # preview-{fallow,meadow}-{day,night}.svg
python3 previews/generate_sample.py   # syntax-sample-fallow.svg and syntax-sample-meadow.svg
```

Don't edit anything in `themes/` or the SVGs in `previews/` by hand. The next build will overwrite your changes. Edit `palette.toml` or a template, then rebuild.

There are two filters you can tack onto a placeholder. `{{night.parchment|nohash}}` drops the `#`, for formats that want bare hex. `{{day.forest|alpha:40}}` adds an alpha value and gives you `#536f4440`. Only use that one in the JSON themes (VSCode, Zed, OpenCode), since terminal configs usually don't understand 8-digit hex.

Some things that might trip you up:

- **The build never deletes files.** If you rename or remove a template, the old file stays in `themes/` until you delete it yourself.
- **There's no way to escape `{{`.** The build reads every file in `templates/`, even `fzf/README.md`, so a stray `{{` in a comment will break it. Same goes for a typo in a placeholder. The build tells you which file failed and exits with an error.
- Palette names describe the color, not what it's used for. It's `forest`, not `string`, and the templates decide which color goes where. Some names exist in both `[day]` and `[night]` with different values (like `weathered-stone`), so check which section you're pulling from.
- Helix templates have their own `[palette]` block at the bottom, with names like `comment` and `error`. The rest of the file uses those names, and only that block points at `palette.toml`.
- The previews keep their own copy of which color goes with which role, in `ROLE_KEYS` in `previews/serene_palette.py`. There's one mapping for Fallow and one for Meadow. If you change a template so strings use a different color, update `ROLE_KEYS` too, or the previews will show the old mapping.

## The rules

There are two palettes. Fallow uses only warm earth tones. Meadow uses the whole color wheel, muted to the same lightness, and shares backgrounds, body text, comments, operators, punctuation and variables with Fallow. Within a palette, a string should be the same hex in every editor, and that goes for every other role too. Day and night get their own colors, each tuned for its own background, so don't copy one into the other.

The default versions put soft tints behind some tokens. The Alt versions leave the tints out and are otherwise identical, so if you change a color in one, change it in the other. Alt only exists for editors that can color the background behind syntax. Right now that's VSCode, Helix and Obsidian. Everything else gets one version per palette and mode, without tints.

Keep it easy on the eyes. Low saturation, no pure white or black, and no bright or saturated blues and purples. Fallow stays warm all the way through. Body text sits around 10:1 contrast. Syntax colors sit between 4.5:1 and 7:1 and never go below 4.5:1, and that includes the active line and the tints. Error and warning colors are the exception, since they also get squiggles and icons.

## Changing a color

1. Change the value in `palette.toml`, or change which color a template uses.
2. Run `python3 build.py`.
3. Check the contrast with an online WCAG checker (we don't have a script for this yet), and actually try it in an editor, in both a bright and a dark room.
4. If a color shown in the previews changed, update `ROLE_KEYS` if needed and regenerate the SVGs.
5. Commit the templates and the regenerated `themes/` together.

## Adding a new editor

Make a folder in `templates/` with `serene-fallow-day`, `serene-fallow-night`, `serene-meadow-day` and `serene-meadow-night` files, using placeholders instead of hex codes. Copy the role mapping from an existing theme. Helix is a good one to start from. Run the build, check what ends up in `themes/` and add the editor to the support table in [COLOR_GUIDE.md](COLOR_GUIDE.md). If the editor can put backgrounds behind syntax, the main files get tints and you add `-alt` files without them.
