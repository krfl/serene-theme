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
  --color=fg:#3d3a33,bg:#f5f2ed,hl:#536f44 \
  --color=fg+:#3d3a33,bg+:#e3d5b8,hl+:#606b44 \
  --color=info:#6e665a,prompt:#606b44,pointer:#606b44 \
  --color=marker:#875f33,spinner:#875f33,header:#6e665a \
  --color=border:#d4cfc4,gutter:#ebe6db \
  --color=preview-fg:#3d3a33,preview-bg:#ebe6db"
```

**Serene Night:**
```bash
export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:#d4cfc4,bg:#1e1d1a,hl:#8fae7a \
  --color=fg+:#d4cfc4,bg+:#3d3420,hl+:#9fa883 \
  --color=info:#968e7f,prompt:#9fa883,pointer:#9fa883 \
  --color=marker:#d4a574,spinner:#d4a574,header:#968e7f \
  --color=border:#3d3a33,gutter:#2a2826 \
  --color=preview-fg:#d4cfc4,preview-bg:#2a2826"
```

## Color Palette

### Serene Day
- Background: `#f5f2ed` (warm light beige)
- Foreground: `#3d3a33` (dark brown)
- Selection: `#e3d5b8` (soft tan)
- Highlights: `#536f44` / `#606b44` (muted greens)
- Accent: `#875f33` (warm amber)

### Serene Night
- Background: `#1e1d1a` (deep warm black)
- Foreground: `#d4cfc4` (soft beige)
- Selection: `#3d3420` (dark olive)
- Highlights: `#8fae7a` / `#9fa883` (sage greens)
- Accent: `#d4a574` (golden amber)

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
