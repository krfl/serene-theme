# Serene Meadow Night - Eye-friendly dark theme for Fish shell
# Reduces blue light and eye strain with muted colors
# Based on optometry research for computer vision syndrome
#
# To use this theme, add to your ~/.config/fish/config.fish:
#   source /path/to/serene-meadow-night.fish

# Syntax Highlighting Colors
set -g fish_color_normal d4cfc4                  # Normal text - soft cream
set -g fish_color_command 80a4c7                 # Command - slate blue
set -g fish_color_keyword bf94b2                 # Keyword - plum
set -g fish_color_quote 8aa983                   # Quote - leaf
set -g fish_color_redirection 79aaa7             # Redirection - spruce
set -g fish_color_end bf94b2                     # End - plum
set -g fish_color_error c9948d                   # Error - rosewood
set -g fish_color_param d4cfc4                   # Parameters - soft cream
set -g fish_color_comment 968e7f                 # Comments - warm gray
set -g fish_color_selection --background=3d3420 # Selection - dark olive background
set -g fish_color_operator 79aaa7               # Operator - spruce
set -g fish_color_escape 79aaa7                  # Escape - spruce
set -g fish_color_autosuggestion a89984          # Autosuggestions - warm stone
set -g fish_color_cwd 8aa983                     # Cwd - leaf
set -g fish_color_user 80a4c7                    # User - slate blue
set -g fish_color_host 80a4c7                    # Host - slate blue
set -g fish_color_host_remote ada172             # Host remote - ochre
set -g fish_color_cancel c9948d                  # Cancel - rosewood
set -g fish_color_search_match --background=3d3420 # Search match - dark olive

# Pager Colors (completion menu)
set -g fish_pager_color_progress a89984          # Progress bar - warm stone
set -g fish_pager_color_prefix 80a4c7 --bold    # Matching prefix - slate blue bold
set -g fish_pager_color_completion d4cfc4       # Completion text - soft cream
set -g fish_pager_color_description a89984      # Description - warm stone
set -g fish_pager_color_selected_background --background=3d3420 # Selected item

# Valid path - underline only (no color change)
set -g fish_color_valid_path --underline
