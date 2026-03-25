# Color Guide

Reference of all colors used across the Serene theme family. All variants (regular and clarity) use the same foreground colors. Clarity variants add subtle background colors on syntax elements but never alter the foreground.

## Base Colors

| Role | Day | Night |
|---|---|---|
| Background | `#f5f2ed` | `#1e1d1a` |
| Foreground | `#3d3a33` | `#d4cfc4` |
| Selection | `#e3d5b8` | `#3d3420` |
| Cursor line | `#ebe6db` | `#2a2826` |
| Border | `#d4cfc4` | `#3d3a33` |
| Line number | `#b5ad9a` | `#5a5549` |
| Line number active | `#7a7260` | `#7a7565` |

## Syntax Colors

These colors are identical across all editors (VSCode, Helix, Zed, OpenCode) for both regular and clarity variants.

| Semantic Role | Day Name | Day Hex | Night Name | Night Hex |
|---|---|---|---|---|
| Comment | comment | `#857c6d` | comment | `#857c6d` |
| String | forest | `#5a7a4a` | sage | `#8fae7a` |
| Number / Constant | clay | `#a5563f` | terracotta | `#c99976` |
| Enum constant | terracotta red | `#8b4a38` | terracotta red | `#b87860` |
| Keyword / Storage | olive | `#657047` | olive | `#a8a378` |
| Flow control | terracotta red | `#8b4a38` | terracotta red | `#b87860` |
| Operator | charcoal | `#5a5240` | stone | `#b5a899` |
| Punctuation | taupe | `#6a6350` | muted punctuation | `#9a8f81` |
| Function | bronze | `#9a6c3a` | sand | `#d4a574` |
| Constructor | bronze | `#9a6c3a` | sand | `#d4a574` |
| Class / Type | caramel | `#8b6f47` | tan | `#b8956d` |
| Variable / Property | taupe | `#6a6350` | beige | `#c8baa8` |
| Namespace / Annotation | terracotta red | `#8b4a38` | terracotta red | `#b87860` |
| Tag / Markup link | olive | `#657047` | olive | `#a8a378` |
| Tag attribute | bronze | `#9a6c3a` | sand | `#d4a574` |
| Markup list | charcoal | `#5a5240` | stone | `#a89984` |
| Markup heading | bronze | `#9a6c3a` | sand | `#d4a574` |
| Markup bold/italic | caramel | `#8b6f47` | tan | `#b8956d` |
| Markup code | forest | `#5a7a4a` | sage | `#8fae7a` |
| Markup quote | comment | `#857c6d` | comment | `#857c6d` |

## Clarity Backgrounds

Used only in clarity variants (VSCode, Helix). These are subtle tints that match each color family.

### Day Clarity

| Color Family | Background |
|---|---|
| Green (string, code) | `#e8ede0` |
| Yellow (keyword, storage, tag, link, list) | `#edecd4` |
| Orange (number, function, heading, tag attr) | `#f7ead8` |
| Brown (type, JSON key, CSS class) | `#f2ebe0` |
| Red (enum, flow, annotation, namespace) | `#f5e8de` |

### Night Clarity

| Color Family | Background |
|---|---|
| Green (string, code) | `#242520` |
| Yellow (storage, tag, link, list) | `#26261e` |
| Orange (number, function, heading, tag attr) | `#2a251e` |
| Brown (type, JSON key, CSS class, property) | `#26241f` |
| Red (enum, flow, annotation, namespace) | `#2a231e` |

## ANSI Terminal Colors

Used in terminal emulators (Wezterm, VSCode terminal, Zed terminal, Apple Terminal).

### Day

| ANSI Color | Hex | Name |
|---|---|---|
| Black | `#4a4538` | dark taupe |
| Red | `#8b4a38` | terracotta red |
| Green | `#5a7a4a` | forest green |
| Yellow | `#9a6c3a` | warm bronze |
| Blue | `#5c7554` | deep sage |
| Magenta | `#8b6f47` | caramel brown |
| Cyan | `#6d6555` | warm charcoal |
| White | `#7b7568` | warm mid-gray |
| Bright Black | `#35322a` | deep warm brown |
| Bright Red | `#8b4a38` | terracotta red |
| Bright Green | `#657047` | deep olive |
| Bright Yellow | `#9a6c3a` | bronze |
| Bright Blue | `#5c7554` | sage |
| Bright Magenta | `#8b6340` | chocolate |
| Bright Cyan | `#a89984` | warm stone |
| Bright White | `#f5f2ed` | warm off-white |

### Night

| ANSI Color | Hex | Name |
|---|---|---|
| Black | `#585a50` | warm olive-gray |
| Red | `#b87860` | terracotta red |
| Green | `#8fae7a` | soft sage |
| Yellow | `#d4a574` | warm sand |
| Blue | `#9aaa82` | warm sage |
| Magenta | `#b8956d` | muted tan |
| Cyan | `#a89984` | warm stone |
| White | `#c8baa8` | light beige |
| Bright Black | `#7a7c6e` | warm olive-gray |
| Bright Red | `#b87860` | terracotta red |
| Bright Green | `#9fa883` | olive |
| Bright Yellow | `#d4a574` | sand |
| Bright Blue | `#9aaa82` | sage |
| Bright Magenta | `#ba9c7e` | warm brown |
| Bright Cyan | `#a89984` | stone |
| Bright White | `#d4cfc4` | soft cream |

## Shell Colors (Fish, FZF)

Fish and FZF use the same syntax palette as above. The comment color is `#857c6d` across all tools.

## Editor Support Matrix

| Editor | Day | Night | Day Clarity | Night Clarity |
|---|---|---|---|---|
| VSCode | yes | yes | yes | yes |
| Helix | yes | yes | yes | yes |
| Zed | yes | yes | no | no |
| OpenCode | yes | yes | no | no |
| Wezterm | yes | yes | no | no |
| Apple Terminal | yes | yes | no | no |
| Fish | yes | yes | no | no |
| FZF | yes | yes | no | no |
| Obsidian | yes | yes | yes | yes |

Clarity variants are only created for editors that support background colors on syntax elements.

## Notes

- Comment color `#857c6d` is shared across day and night variants.
- ANSI terminal colors are identical across all terminal-capable editors (Wezterm, VSCode, Zed, Apple Terminal).
- Regular and clarity variants always use the same foreground colors. Clarity only adds backgrounds.
