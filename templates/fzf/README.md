# Serene fzf Themes

Two warm, earthy color schemes for [fzf](https://github.com/junegunn/fzf) (fuzzy finder).

## Available Themes

- **serene-day.sh** - Light theme with warm earth tones, perfect for daytime use
- **serene-night.sh** - Dark theme with muted, comfortable colors for nighttime use

## Installation

### Option 1: Source in your shell configuration

Add one of these lines to your shell configuration file (`.bashrc`, `.zshrc`, etc.):

```bash
# For serene-day
source /path/to/serene-theme/themes/fzf/serene-day.sh

# For serene-night
source /path/to/serene-theme/themes/fzf/serene-night.sh
```

### Option 2: Copy the color settings directly

Copy the `export FZF_DEFAULT_OPTS` line from the theme file directly into your shell configuration.

### Option 3: Manually set the colors

You can also set the colors directly in your configuration:

**Serene Day:**
```bash
export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:{{day.warm-ink}},bg:{{day.aged-paper}},hl:{{day.forest}} \
  --color=fg+:{{day.warm-ink}},bg+:{{day.golden-sand}},hl+:{{day.olive}} \
  --color=info:{{day.weathered-stone}},prompt:{{day.olive}},pointer:{{day.olive}} \
  --color=marker:{{day.bronze}},spinner:{{day.bronze}},header:{{day.weathered-stone}} \
  --color=border:{{day.light-taupe}},gutter:{{day.pale-wheat}} \
  --color=preview-fg:{{day.warm-ink}},preview-bg:{{day.pale-wheat}}"
```

**Serene Night:**
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

### Serene Day
- Background: `{{day.aged-paper}}` (warm light beige)
- Foreground: `{{day.warm-ink}}` (dark brown)
- Selection: `{{day.golden-sand}}` (soft tan)
- Highlights: `{{day.forest}}` / `{{day.olive}}` (muted greens)
- Accent: `{{day.bronze}}` (warm amber)

### Serene Night
- Background: `{{night.deep-earth}}` (deep warm black)
- Foreground: `{{night.parchment}}` (soft beige)
- Selection: `{{night.warm-umber}}` (dark olive)
- Highlights: `{{night.meadow-sage}}` / `{{night.sage-grass}}` (sage greens)
- Accent: `{{night.honey}}` (golden amber)

## Switching Between Themes

To easily switch between day and night themes, you can create shell functions:

```bash
fzf-day() {
  source /path/to/serene-theme/themes/fzf/serene-day.sh
}

fzf-night() {
  source /path/to/serene-theme/themes/fzf/serene-night.sh
}
```

## Requirements

- fzf with 24-bit color support (recent versions)
- Terminal emulator with true color support

## License

Part of the Serene Theme collection.
