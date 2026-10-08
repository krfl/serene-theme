# Color Guide

Reference of all colors used across the Serene theme family. There are two palettes. Fallow uses warm earth tones only. Meadow uses muted colors from the whole color wheel. Both share the base colors below.

In editors that can show them, Serene puts subtle background tints behind syntax elements. Tints never change the foreground.

Every syntax token meets **WCAG AA (4.5:1)** against every background it renders on: base, active-line highlight and tints. Body text targets ~10:1. Syntax colors stay in a 4.5 to 7:1 band, low enough to separate tokens without glare but never below the AA floor. Variables and properties at night are the exception on the high side (about 8.9:1), since they sit close to body text. Diagnostic accents (error, warning, info, hint) are tuned for salience and carry non-color cues, so they are not held to the AA text floor.

## Base Colors

Shared by Fallow and Meadow.

| Role | Day | Night |
|---|---|---|
| Background | `#f5f2ed` | `#1e1d1a` |
| Foreground | `#3d3a33` | `#d4cfc4` |
| Selection | `#e3d5b8` | `#3d3420` |
| Cursor line | `#ebe6db` | `#2a2826` |
| Border | `#d4cfc4` | `#3d3a33` |
| Line number | `#b5ad9a` | `#5a5549` |
| Line number active | `#7a7260` | `#7a7565` |

## Fallow Syntax Colors

These colors are identical across all editors (VSCode, Helix, Zed, OpenCode).

| Semantic Role | Day Name | Day Hex | Night Name | Night Hex |
|---|---|---|---|---|
| Comment | comment | `#6e665a` | comment | `#968e7f` |
| String | forest | `#536f44` | sage | `#8fae7a` |
| Number / Constant | clay | `#9e523c` | terracotta | `#c99976` |
| Enum constant | terracotta red | `#8b4a38` | terracotta red | `#bc816b` |
| Keyword / Storage | olive | `#606b44` | olive | `#a8a378` |
| Flow control | terracotta red | `#8b4a38` | terracotta red | `#bc816b` |
| Operator | charcoal | `#5a5240` | stone | `#b5a899` |
| Punctuation | taupe | `#6a6350` | muted punctuation | `#9a8f81` |
| Function | bronze | `#875f33` | sand | `#d4a574` |
| Constructor | bronze | `#875f33` | sand | `#d4a574` |
| Class / Type | caramel | `#7c6340` | tan | `#b8956d` |
| Variable / Property | taupe | `#6a6350` | beige | `#c8baa8` |
| Namespace / Annotation | terracotta red | `#8b4a38` | terracotta red | `#bc816b` |
| Tag / Markup link | olive | `#606b44` | olive | `#a8a378` |
| Tag attribute | bronze | `#875f33` | sand | `#d4a574` |
| Markup list | charcoal | `#5a5240` | stone | `#a89984` |
| Markup heading | bronze | `#875f33` | sand | `#d4a574` |
| Markup bold/italic | caramel | `#7c6340` | tan | `#b8956d` |
| Markup code | forest | `#536f44` | sage | `#8fae7a` |
| Markup quote | comment | `#6e665a` | comment | `#968e7f` |

## Meadow Syntax Colors

Comment, operator, punctuation, variable and markup list are the same as in Fallow.

| Semantic Role | Name | Day Hex | Night Hex |
|---|---|---|---|
| String | leaf | `#496842` | `#8aa983` |
| Number / Constant | cinnamon | `#845540` | `#c69681` |
| Enum constant | spruce | `#356967` | `#79aaa7` |
| Keyword / Storage | plum | `#7d5371` | `#bf94b2` |
| Flow control | spruce | `#356967` | `#79aaa7` |
| Function | slate blue | `#3f6386` | `#80a4c7` |
| Constructor | slate blue | `#3f6386` | `#80a4c7` |
| Class / Type | ochre | `#6d602f` | `#ada172` |
| Namespace / Annotation | spruce | `#356967` | `#79aaa7` |
| Tag / Markup link | plum | `#7d5371` | `#bf94b2` |
| Tag attribute | slate blue | `#3f6386` | `#80a4c7` |
| Markup heading | slate blue | `#3f6386` | `#80a4c7` |
| Markup bold/italic | ochre | `#6d602f` | `#ada172` |
| Markup code | leaf | `#496842` | `#8aa983` |
| Diff deleted / Invalid | rosewood | `#86534c` | `#c9948d` |

Meadow also has its own error and info colors, so they don't get mixed up with numbers and namespaces. Warning is the same as in Fallow.

| Diagnostic | Name | Day Hex | Night Hex |
|---|---|---|---|
| Error | poppy | `#aa4f4f` | `#d77876` |
| Info | lagoon | `#007785` | `#42a0af` |

## Tints

Shown in Helix and Obsidian. The VSCode themes include them too, but VSCode doesn't draw background colors behind syntax. These are subtle tints that match each color family.

### Fallow Day

| Color Family | Background |
|---|---|
| Green (string, code) | `#e8ede0` |
| Yellow (keyword, storage, tag, link, list) | `#edecd4` |
| Orange (number, function, heading, tag attr) | `#f7ead8` |
| Brown (type, JSON key, CSS class) | `#f2ebe0` |
| Red (enum, flow, annotation, namespace) | `#f5e8de` |

### Fallow Night

| Color Family | Background |
|---|---|
| Green (string, code) | `#242520` |
| Yellow (storage, tag, link, list) | `#26261e` |
| Orange (number, function, heading, tag attr) | `#2a251e` |
| Brown (type, JSON key, CSS class, property) | `#26241f` |
| Red (enum, flow, annotation, namespace) | `#2a231e` |

### Meadow

| Color Family | Day | Night |
|---|---|---|
| Green (string, code) | `#e2ede0` | `#20271f` |
| Plum (keyword, storage, tag, link) | `#f4e4ef` | `#2a2227` |
| Blue (function, heading, tag attr) | `#deebf8` | `#1e252c` |
| Orange (number, constant) | `#f7e5dd` | `#2b221e` |
| Ochre (type, CSS class) | `#eee9d9` | `#27251c` |
| Teal (enum, flow, annotation, namespace) | `#daefed` | `#1c2726` |
| Red (diff deleted) | `#f8e4e1` | `#2c2220` |

## ANSI Terminal Colors

Used in terminal emulators (Wezterm, Ghostty, Alacritty, Kitty, VSCode terminal, Zed terminal).

### Fallow Day

| ANSI Color | Hex | Name |
|---|---|---|
| Black | `#4a4538` | dark taupe |
| Red | `#8b4a38` | terracotta red |
| Green | `#536f44` | forest green |
| Yellow | `#875f33` | warm bronze |
| Blue | `#5c7554` | deep sage |
| Magenta | `#7c6340` | caramel brown |
| Cyan | `#6d6555` | warm charcoal |
| White | `#7b7568` | warm mid-gray |
| Bright Black | `#35322a` | deep warm brown |
| Bright Red | `#8b4a38` | terracotta red |
| Bright Green | `#606b44` | deep olive |
| Bright Yellow | `#875f33` | bronze |
| Bright Blue | `#5c7554` | sage |
| Bright Magenta | `#8b6340` | chocolate |
| Bright Cyan | `#a89984` | warm stone |
| Bright White | `#f5f2ed` | warm off-white |

### Fallow Night

| ANSI Color | Hex | Name |
|---|---|---|
| Black | `#585a50` | warm olive-gray |
| Red | `#bc816b` | terracotta red |
| Green | `#8fae7a` | soft sage |
| Yellow | `#d4a574` | warm sand |
| Blue | `#9aaa82` | warm sage |
| Magenta | `#b8956d` | muted tan |
| Cyan | `#a89984` | warm stone |
| White | `#c8baa8` | light beige |
| Bright Black | `#7a7c6e` | warm olive-gray |
| Bright Red | `#bc816b` | terracotta red |
| Bright Green | `#9fa883` | olive |
| Bright Yellow | `#d4a574` | sand |
| Bright Blue | `#9aaa82` | sage |
| Bright Magenta | `#ba9c7e` | warm brown |
| Bright Cyan | `#a89984` | stone |
| Bright White | `#d4cfc4` | soft cream |

### Meadow

Black, white, bright black and bright white are the same as in Fallow. The bright colors are a step darker on Day and a step lighter on Night.

| ANSI Color | Name | Day | Night |
|---|---|---|---|
| Red | rosewood | `#86534c` | `#c9948d` |
| Green | leaf | `#496842` | `#8aa983` |
| Yellow | ochre | `#6d602f` | `#ada172` |
| Blue | slate blue | `#3f6386` | `#80a4c7` |
| Magenta | plum | `#7d5371` | `#bf94b2` |
| Cyan | spruce | `#356967` | `#79aaa7` |
| Bright Red | rosewood | `#77453e` | `#d9a39c` |
| Bright Green | leaf | `#3b5a34` | `#99b992` |
| Bright Yellow | ochre | `#5e5220` | `#bdb081` |
| Bright Blue | slate blue | `#315577` | `#8fb3d7` |
| Bright Magenta | plum | `#6e4562` | `#cfa3c1` |
| Bright Cyan | spruce | `#265a58` | `#88bab7` |

## Shell Colors (Fish, FZF)

Fish and FZF use the same syntax colors as the other editors, for each palette. The comment color is `#6e665a` (day) / `#968e7f` (night) across all tools and both palettes.

## Editor Support Matrix

| Editor | Fallow | Meadow | Tints |
|---|---|---|---|
| VSCode | yes | yes | included, not shown |
| Helix | yes | yes | yes |
| Obsidian | yes | yes | yes |
| Zed | yes | yes | no |
| OpenCode | yes | yes | no |
| Wezterm | yes | yes | no |
| Ghostty | yes | yes | no |
| Alacritty | yes | yes | no |
| Kitty | yes | yes | no |
| Fish | yes | yes | no |
| FZF | yes | yes | no |

Editors that can't put backgrounds behind syntax get the same theme without the tints.

## Notes

- Comment uses separate day (`#6e665a`) and night (`#968e7f`) values. Each clears WCAG AA 4.5:1 on every background it renders on, including the active line. One shared value cannot meet AA on both day and night.
- Within a palette, ANSI terminal colors are identical across all terminal-capable editors (Wezterm, Ghostty, Alacritty, Kitty, VSCode, Zed).
- The tints only add backgrounds. Text colors are the same in every editor, with or without tints.
- In VSCode and Zed, Meadow keeps Fallow's UI colors. Syntax, terminal, error and info colors change.
- All six Meadow syntax hues share the same lightness. That keeps any one of them from standing out, but it also means lightness can't help tell them apart, which matters for colorblind users (see the FAQ in the README).
