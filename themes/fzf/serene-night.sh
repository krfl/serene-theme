#!/bin/bash
# Serene Night theme for fzf
# A warm, dark color scheme for nighttime coding

export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:#d4cfc4,bg:#1e1d1a,hl:#8fae7a \
  --color=fg+:#d4cfc4,bg+:#3d3420,hl+:#9fa883 \
  --color=info:#857c6d,prompt:#9fa883,pointer:#9fa883 \
  --color=marker:#d4a574,spinner:#d4a574,header:#857c6d \
  --color=border:#3d3a33,gutter:#2a2826 \
  --color=preview-fg:#d4cfc4,preview-bg:#2a2826"
