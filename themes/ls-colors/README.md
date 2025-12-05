# Serene LS_COLORS

LS_COLORS/LSCOLORS configurations for the Serene Clarity theme variants.

## About

These configurations bring Serene's color palette to your terminal file listings when using `ls` or compatible tools.

**Important:** Background colors are **not practical** for file listings because:
- BSD `ls` (macOS default) doesn't support them
- They reduce readability and create visual clutter
- Terminal support varies significantly

These configurations focus on **foreground colors only** for the best experience across all platforms.

## Available Variants

### macOS (BSD ls)
- **serene-night-clarity-bsd.sh** - Dark theme for macOS default ls
- **serene-day-clarity-bsd.sh** - Light theme for macOS default ls

### Linux (GNU ls) / Advanced
- **serene-night-clarity.sh** - Dark theme with 256-color support
- **serene-day-clarity.sh** - Light theme with 256-color support

## Installation

### Quick Setup

Source the appropriate theme file for your system:

**macOS (default BSD ls):**
```bash
# Night Clarity
source /path/to/serene-theme/themes/ls-colors/serene-night-clarity-bsd.sh

# Day Clarity
source /path/to/serene-theme/themes/ls-colors/serene-day-clarity-bsd.sh
```

**Linux (GNU ls):**
```bash
# Night Clarity
source /path/to/serene-theme/themes/ls-colors/serene-night-clarity.sh

# Day Clarity
source /path/to/serene-theme/themes/ls-colors/serene-day-clarity.sh
```

### Permanent Setup

Add the appropriate line to your shell configuration file:

**For macOS with Zsh** (`~/.zshrc`):
```bash
source /path/to/serene-theme/themes/ls-colors/serene-night-clarity-bsd.sh
```

**For macOS with Bash** (`~/.bash_profile`):
```bash
source /path/to/serene-theme/themes/ls-colors/serene-night-clarity-bsd.sh
```

**For Linux** (`~/.bashrc` or `~/.zshrc`):
```bash
source /path/to/serene-theme/themes/ls-colors/serene-night-clarity.sh
```

Then reload your shell: `source ~/.zshrc` (or `~/.bashrc` / `~/.bash_profile`).

## Color Mapping

All colors are **foreground only** (no backgrounds) for optimal readability.

### Night Clarity
- **Directories**: Bold Green
- **Executables**: Bold Yellow
- **Symlinks**: Cyan
- **Archives**: Red
- **Media files**: Magenta
- **Code files**: Green
- **Config files**: Yellow (JSON, YAML, etc.)
- **Documents**: White/Default

### Day Clarity
- **Directories**: Green
- **Executables**: Bold Yellow
- **Symlinks**: Cyan
- **Archives**: Red
- **Media files**: Magenta
- **Code files**: Green
- **Config files**: Yellow (JSON, YAML, etc.)
- **Documents**: Black/Default

## Testing

To see the colors in action, run:

```bash
ls -lah
```

Or use a specialized tool like `dircolors -p` to inspect the current configuration.

## Compatibility

- ✅ **macOS BSD `ls`** - Use `-bsd.sh` files
- ✅ **GNU `ls`** (Linux) - Use standard `.sh` files
- ✅ `tree`
- ✅ `fd`
- ✅ `eza` (foreground colors work)
- ✅ Most terminal file managers

## Customization

### BSD ls (macOS)

The `-bsd.sh` files use `LSCOLORS` with a simple 11-pair format. Each pair is foreground+background:
- **Colors**: `a-h` (normal), `A-H` (bold), `x` (default/transparent)
- **Values**: a=black, b=red, c=green, d=brown, e=blue, f=magenta, g=cyan, h=light grey

Example: `LSCOLORS="Cxgxfxdxbxegedabagacad"`
- `Cx` = directories: bold green foreground, default background

### GNU ls (Linux)

The standard `.sh` files use `LS_COLORS` with detailed file type mappings:

**Basic ANSI codes:**
- `30-37`: Standard foreground colors
- `90-97`: Bright foreground colors
- `1`: Bold, `3`: Italic, `4`: Underline

**256-color support:**
- `38;5;N`: Foreground (N = 0-255)
- `48;5;N`: Background (N = 0-255) - not recommended for readability

**Combine with semicolons:** `1;32` (bold green)

## Related

- [Serene Theme Repository](https://github.com/your-repo/serene-theme)
- [LS_COLORS Documentation](https://man7.org/linux/man-pages/man5/dir_colors.5.html)
