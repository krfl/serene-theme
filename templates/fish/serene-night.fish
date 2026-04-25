# Serene Night - Eye-friendly dark theme for Fish shell
# Reduces blue light and eye strain with warm earth tones
# Based on optometry research for computer vision syndrome
#
# To use this theme, add to your ~/.config/fish/config.fish:
#   source /path/to/serene-night.fish

# Syntax Highlighting Colors
set -g fish_color_normal {{night.parchment|nohash}}                  # Normal text - soft cream
set -g fish_color_command {{night.spring-sage|nohash}}                 # Commands - warm sage
set -g fish_color_keyword {{night.warm-tan|nohash}}                 # Keywords - muted tan
set -g fish_color_quote {{night.meadow-sage|nohash}}                   # Quoted strings - soft sage
set -g fish_color_redirection {{night.honey|nohash}}             # Redirections - warm sand
set -g fish_color_end {{night.warm-tan|nohash}}                     # End keyword - muted tan
set -g fish_color_error {{night.sunset-clay|nohash}}                   # Errors - terracotta red
set -g fish_color_param {{night.parchment|nohash}}                   # Parameters - soft cream
set -g fish_color_comment {{night.weathered-stone|nohash}}                 # Comments - warm gray
set -g fish_color_selection --background={{night.warm-umber|nohash}} # Selection - dark olive background
set -g fish_color_operator {{night.honey|nohash}}               # Operators - warm sand
set -g fish_color_escape {{night.honey|nohash}}                  # Escape sequences - warm sand
set -g fish_color_autosuggestion {{night.sandstone|nohash}}          # Autosuggestions - warm stone
set -g fish_color_cwd {{night.spring-sage|nohash}}                     # Current directory - warm sage
set -g fish_color_user {{night.spring-sage|nohash}}                    # Username - warm sage
set -g fish_color_host {{night.spring-sage|nohash}}                    # Hostname - warm sage
set -g fish_color_host_remote {{night.warm-tan|nohash}}             # Remote hostname - muted tan
set -g fish_color_cancel {{night.sunset-clay|nohash}}                  # Cancel (^C) - terracotta red
set -g fish_color_search_match --background={{night.warm-umber|nohash}} # Search match - dark olive

# Pager Colors (completion menu)
set -g fish_pager_color_progress {{night.sandstone|nohash}}          # Progress bar - warm stone
set -g fish_pager_color_prefix {{night.spring-sage|nohash}} --bold    # Matching prefix - warm sage bold
set -g fish_pager_color_completion {{night.parchment|nohash}}       # Completion text - soft cream
set -g fish_pager_color_description {{night.sandstone|nohash}}      # Description - warm stone
set -g fish_pager_color_selected_background --background={{night.warm-umber|nohash}} # Selected item

# Valid path - underline only (no color change)
set -g fish_color_valid_path --underline
