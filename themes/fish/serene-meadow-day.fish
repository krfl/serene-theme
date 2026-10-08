# Serene Meadow Day - Eye-friendly light theme for Fish shell
# Reduces glare and eye strain with muted colors
# Based on optometry research for computer vision syndrome
#
# To use this theme, add to your ~/.config/fish/config.fish:
#   source /path/to/serene-meadow-day.fish

# Syntax Highlighting Colors
set -g fish_color_normal 3d3a33                  # Normal text - warm dark gray
set -g fish_color_command 3f6386                 # Command - slate blue
set -g fish_color_keyword 7d5371                 # Keyword - plum
set -g fish_color_quote 496842                   # Quote - leaf
set -g fish_color_redirection 356967             # Redirection - spruce
set -g fish_color_end 7d5371                     # End - plum
set -g fish_color_error 86534c                   # Error - rosewood
set -g fish_color_param 3d3a33                   # Parameters - warm dark gray
set -g fish_color_comment 6e665a                 # Comments - medium gray
set -g fish_color_selection --background=e3d5b8 # Selection - warm beige background
set -g fish_color_operator 356967               # Operator - spruce
set -g fish_color_escape 356967                  # Escape - spruce
set -g fish_color_autosuggestion 6e665a          # Autosuggestions - medium gray
set -g fish_color_cwd 496842                     # Cwd - leaf
set -g fish_color_user 3f6386                    # User - slate blue
set -g fish_color_host 3f6386                    # Host - slate blue
set -g fish_color_host_remote 6d602f             # Host remote - ochre
set -g fish_color_cancel 86534c                  # Cancel - rosewood
set -g fish_color_search_match --background=e3d5b8 # Search match - warm beige

# Pager Colors (completion menu)
set -g fish_pager_color_progress 6e665a          # Progress bar - medium gray
set -g fish_pager_color_prefix 3f6386 --bold    # Matching prefix - slate blue bold
set -g fish_pager_color_completion 3d3a33       # Completion text - warm dark gray
set -g fish_pager_color_description 6e665a      # Description - medium gray
set -g fish_pager_color_selected_background --background=e3d5b8 # Selected item

# Valid path - underline only (no color change)
set -g fish_color_valid_path --underline
