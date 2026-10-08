# Serene Meadow Night - Eye-friendly dark theme for Fish shell
# Reduces blue light and eye strain with muted colors
# Based on optometry research for computer vision syndrome
#
# To use this theme, add to your ~/.config/fish/config.fish:
#   source /path/to/serene-meadow-night.fish

# Syntax Highlighting Colors
set -g fish_color_normal {{night.parchment|nohash}}                  # Normal text - soft cream
set -g fish_color_command {{night.slate-blue|nohash}}                 # Command - slate blue
set -g fish_color_keyword {{night.plum|nohash}}                 # Keyword - plum
set -g fish_color_quote {{night.leaf|nohash}}                   # Quote - leaf
set -g fish_color_redirection {{night.spruce|nohash}}             # Redirection - spruce
set -g fish_color_end {{night.plum|nohash}}                     # End - plum
set -g fish_color_error {{night.rosewood|nohash}}                   # Error - rosewood
set -g fish_color_param {{night.parchment|nohash}}                   # Parameters - soft cream
set -g fish_color_comment {{night.weathered-stone|nohash}}                 # Comments - warm gray
set -g fish_color_selection --background={{night.warm-umber|nohash}} # Selection - dark olive background
set -g fish_color_operator {{night.spruce|nohash}}               # Operator - spruce
set -g fish_color_escape {{night.spruce|nohash}}                  # Escape - spruce
set -g fish_color_autosuggestion {{night.sandstone|nohash}}          # Autosuggestions - warm stone
set -g fish_color_cwd {{night.leaf|nohash}}                     # Cwd - leaf
set -g fish_color_user {{night.slate-blue|nohash}}                    # User - slate blue
set -g fish_color_host {{night.slate-blue|nohash}}                    # Host - slate blue
set -g fish_color_host_remote {{night.ochre|nohash}}             # Host remote - ochre
set -g fish_color_cancel {{night.rosewood|nohash}}                  # Cancel - rosewood
set -g fish_color_search_match --background={{night.warm-umber|nohash}} # Search match - dark olive

# Pager Colors (completion menu)
set -g fish_pager_color_progress {{night.sandstone|nohash}}          # Progress bar - warm stone
set -g fish_pager_color_prefix {{night.slate-blue|nohash}} --bold    # Matching prefix - slate blue bold
set -g fish_pager_color_completion {{night.parchment|nohash}}       # Completion text - soft cream
set -g fish_pager_color_description {{night.sandstone|nohash}}      # Description - warm stone
set -g fish_pager_color_selected_background --background={{night.warm-umber|nohash}} # Selected item

# Valid path - underline only (no color change)
set -g fish_color_valid_path --underline
