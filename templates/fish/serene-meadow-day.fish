# Serene Meadow Day - Eye-friendly light theme for Fish shell
# Reduces glare and eye strain with muted colors
# Based on optometry research for computer vision syndrome
#
# To use this theme, add to your ~/.config/fish/config.fish:
#   source /path/to/serene-meadow-day.fish

# Syntax Highlighting Colors
set -g fish_color_normal {{day.warm-ink|nohash}}                  # Normal text - warm dark gray
set -g fish_color_command {{day.slate-blue|nohash}}                 # Command - slate blue
set -g fish_color_keyword {{day.plum|nohash}}                 # Keyword - plum
set -g fish_color_quote {{day.leaf|nohash}}                   # Quote - leaf
set -g fish_color_redirection {{day.spruce|nohash}}             # Redirection - spruce
set -g fish_color_end {{day.plum|nohash}}                     # End - plum
set -g fish_color_error {{day.rosewood|nohash}}                   # Error - rosewood
set -g fish_color_param {{day.warm-ink|nohash}}                   # Parameters - warm dark gray
set -g fish_color_comment {{day.weathered-stone|nohash}}                 # Comments - medium gray
set -g fish_color_selection --background={{day.golden-sand|nohash}} # Selection - warm beige background
set -g fish_color_operator {{day.spruce|nohash}}               # Operator - spruce
set -g fish_color_escape {{day.spruce|nohash}}                  # Escape - spruce
set -g fish_color_autosuggestion {{day.weathered-stone|nohash}}          # Autosuggestions - medium gray
set -g fish_color_cwd {{day.leaf|nohash}}                     # Cwd - leaf
set -g fish_color_user {{day.slate-blue|nohash}}                    # User - slate blue
set -g fish_color_host {{day.slate-blue|nohash}}                    # Host - slate blue
set -g fish_color_host_remote {{day.ochre|nohash}}             # Host remote - ochre
set -g fish_color_cancel {{day.rosewood|nohash}}                  # Cancel - rosewood
set -g fish_color_search_match --background={{day.golden-sand|nohash}} # Search match - warm beige

# Pager Colors (completion menu)
set -g fish_pager_color_progress {{day.weathered-stone|nohash}}          # Progress bar - medium gray
set -g fish_pager_color_prefix {{day.slate-blue|nohash}} --bold    # Matching prefix - slate blue bold
set -g fish_pager_color_completion {{day.warm-ink|nohash}}       # Completion text - warm dark gray
set -g fish_pager_color_description {{day.weathered-stone|nohash}}      # Description - medium gray
set -g fish_pager_color_selected_background --background={{day.golden-sand|nohash}} # Selected item

# Valid path - underline only (no color change)
set -g fish_color_valid_path --underline
