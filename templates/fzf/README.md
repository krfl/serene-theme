# Serene fzf Themes

Color schemes for [fzf](https://github.com/junegunn/fzf) (fuzzy finder). Fallow uses warm earth tones and Meadow uses muted colors from the whole color wheel.

## Available Themes

- **serene-fallow-day.sh** - Light theme with warm earth tones
- **serene-fallow-night.sh** - Dark theme with warm earth tones
- **serene-meadow-day.sh** - Light theme with muted colors from the whole color wheel
- **serene-meadow-night.sh** - Dark theme with muted colors from the whole color wheel

## Installation

### Option 1: Source in your shell configuration

Add one of these lines to your shell configuration file (`.bashrc`, `.zshrc`, etc.):

```bash
# For serene-fallow-day
source /path/to/serene-theme/themes/fzf/serene-fallow-day.sh

# For serene-fallow-night
source /path/to/serene-theme/themes/fzf/serene-fallow-night.sh

# Meadow works the same way
source /path/to/serene-theme/themes/fzf/serene-meadow-day.sh
```

### Option 2: Copy the color settings directly

Copy the `export FZF_DEFAULT_OPTS` line from the theme file directly into your shell configuration.

### Option 3: Manually set the colors

You can also set the colors directly in your configuration:

**Serene Fallow Day:**
```bash
export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:{{day.warm-ink}},bg:{{day.aged-paper}},hl:{{day.forest}} \
  --color=fg+:{{day.warm-ink}},bg+:{{day.golden-sand}},hl+:{{day.olive}} \
  --color=info:{{day.weathered-stone}},prompt:{{day.olive}},pointer:{{day.olive}} \
  --color=marker:{{day.bronze}},spinner:{{day.bronze}},header:{{day.weathered-stone}} \
  --color=border:{{day.light-taupe}},gutter:{{day.pale-wheat}} \
  --color=preview-fg:{{day.warm-ink}},preview-bg:{{day.pale-wheat}}"
```

**Serene Fallow Night:**
```bash
export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:{{night.parchment}},bg:{{night.deep-earth}},hl:{{night.meadow-sage}} \
  --color=fg+:{{night.parchment}},bg+:{{night.warm-umber}},hl+:{{night.sage-grass}} \
  --color=info:{{night.weathered-stone}},prompt:{{night.sage-grass}},pointer:{{night.sage-grass}} \
  --color=marker:{{night.honey}},spinner:{{night.honey}},header:{{night.weathered-stone}} \
  --color=border:{{night.warm-ink}},gutter:{{night.dark-walnut}} \
  --color=preview-fg:{{night.parchment}},preview-bg:{{night.dark-walnut}}"
```

## Color Palette

### Serene Fallow Day
- Background: `{{day.aged-paper}}` (warm light beige)
- Foreground: `{{day.warm-ink}}` (dark brown)
- Selection: `{{day.golden-sand}}` (soft tan)
- Highlights: `{{day.forest}}` / `{{day.olive}}` (muted greens)
- Accent: `{{day.bronze}}` (warm amber)

### Serene Fallow Night
- Background: `{{night.deep-earth}}` (deep warm black)
- Foreground: `{{night.parchment}}` (soft beige)
- Selection: `{{night.warm-umber}}` (dark olive)
- Highlights: `{{night.meadow-sage}}` / `{{night.sage-grass}}` (sage greens)
- Accent: `{{night.honey}}` (golden amber)

## Switching Between Themes

To easily switch between day and night themes, you can create shell functions:

```bash
fzf-day() {
  source /path/to/serene-theme/themes/fzf/serene-fallow-day.sh
}

fzf-night() {
  source /path/to/serene-theme/themes/fzf/serene-fallow-night.sh
}
```

## Requirements

- fzf with 24-bit color support (recent versions)
- Terminal emulator with true color support

## License

Part of the Serene Theme collection.
