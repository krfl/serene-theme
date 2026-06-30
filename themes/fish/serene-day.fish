# Serene Day - Eye-friendly light theme for Fish shell
# Reduces glare and eye strain with warm earth tones
# Based on optometry research for computer vision syndrome
#
# To use this theme, add to your ~/.config/fish/config.fish:
#   source /path/to/serene-day.fish

# Syntax Highlighting Colors
set -g fish_color_normal 3d3a33                  # Normal text - warm dark gray
set -g fish_color_command 5c7554                 # Commands - deep sage
set -g fish_color_keyword 7c6340                 # Keywords - caramel brown
set -g fish_color_quote 536f44                   # Quoted strings - forest green
set -g fish_color_redirection 875f33             # Redirections - warm bronze
set -g fish_color_end 7c6340                     # End keyword - caramel brown
set -g fish_color_error 8b4a38                   # Errors - terracotta red
set -g fish_color_param 3d3a33                   # Parameters - warm dark gray
set -g fish_color_comment 6e665a                 # Comments - medium gray
set -g fish_color_selection --background=e3d5b8 # Selection - warm beige background
set -g fish_color_operator 875f33               # Operators - warm bronze
set -g fish_color_escape 875f33                  # Escape sequences - warm bronze
set -g fish_color_autosuggestion 6e665a          # Autosuggestions - medium gray
set -g fish_color_cwd 5c7554                     # Current directory - deep sage
set -g fish_color_user 5c7554                    # Username - deep sage
set -g fish_color_host 5c7554                    # Hostname - deep sage
set -g fish_color_host_remote 7c6340             # Remote hostname - caramel brown
set -g fish_color_cancel 8b4a38                  # Cancel (^C) - terracotta red
set -g fish_color_search_match --background=e3d5b8 # Search match - warm beige

# Pager Colors (completion menu)
set -g fish_pager_color_progress 6e665a          # Progress bar - medium gray
set -g fish_pager_color_prefix 5c7554 --bold    # Matching prefix - deep sage bold
set -g fish_pager_color_completion 3d3a33       # Completion text - warm dark gray
set -g fish_pager_color_description 6e665a      # Description - medium gray
set -g fish_pager_color_selected_background --background=e3d5b8 # Selected item

# Valid path - underline only (no color change)
set -g fish_color_valid_path --underline
