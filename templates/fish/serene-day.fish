# Serene Day - Eye-friendly light theme for Fish shell
# Reduces glare and eye strain with warm earth tones
# Based on optometry research for computer vision syndrome
#
# To use this theme, add to your ~/.config/fish/config.fish:
#   source /path/to/serene-day.fish

# Syntax Highlighting Colors
set -g fish_color_normal {{day.warm-ink|nohash}}                  # Normal text - warm dark gray
set -g fish_color_command {{day.fern|nohash}}                 # Commands - deep sage
set -g fish_color_keyword {{day.caramel|nohash}}                 # Keywords - caramel brown
set -g fish_color_quote {{day.forest|nohash}}                   # Quoted strings - forest green
set -g fish_color_redirection {{day.bronze|nohash}}             # Redirections - warm bronze
set -g fish_color_end {{day.caramel|nohash}}                     # End keyword - caramel brown
set -g fish_color_error {{day.terracotta|nohash}}                   # Errors - terracotta red
set -g fish_color_param {{day.warm-ink|nohash}}                   # Parameters - warm dark gray
set -g fish_color_comment {{day.weathered-stone|nohash}}                 # Comments - medium gray
set -g fish_color_selection --background={{day.golden-sand|nohash}} # Selection - warm beige background
set -g fish_color_operator {{day.bronze|nohash}}               # Operators - warm bronze
set -g fish_color_escape {{day.bronze|nohash}}                  # Escape sequences - warm bronze
set -g fish_color_autosuggestion {{day.weathered-stone|nohash}}          # Autosuggestions - medium gray
set -g fish_color_cwd {{day.fern|nohash}}                     # Current directory - deep sage
set -g fish_color_user {{day.fern|nohash}}                    # Username - deep sage
set -g fish_color_host {{day.fern|nohash}}                    # Hostname - deep sage
set -g fish_color_host_remote {{day.caramel|nohash}}             # Remote hostname - caramel brown
set -g fish_color_cancel {{day.terracotta|nohash}}                  # Cancel (^C) - terracotta red
set -g fish_color_search_match --background={{day.golden-sand|nohash}} # Search match - warm beige

# Pager Colors (completion menu)
set -g fish_pager_color_progress {{day.weathered-stone|nohash}}          # Progress bar - medium gray
set -g fish_pager_color_prefix {{day.fern|nohash}} --bold    # Matching prefix - deep sage bold
set -g fish_pager_color_completion {{day.warm-ink|nohash}}       # Completion text - warm dark gray
set -g fish_pager_color_description {{day.weathered-stone|nohash}}      # Description - medium gray
set -g fish_pager_color_selected_background --background={{day.golden-sand|nohash}} # Selected item

# Valid path - underline only (no color change)
set -g fish_color_valid_path --underline
