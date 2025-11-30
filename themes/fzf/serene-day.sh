#!/bin/bash
# Serene Day theme for fzf
# A warm, light color scheme for daytime coding

export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:#3d3a33,bg:#f5f2ed,hl:#5a7a4a \
  --color=fg+:#3d3a33,bg+:#e3d5b8,hl+:#657047 \
  --color=info:#857d6d,prompt:#657047,pointer:#657047 \
  --color=marker:#9a6c3a,spinner:#9a6c3a,header:#857d6d \
  --color=border:#d4cfc4,gutter:#ebe6db \
  --color=preview-fg:#3d3a33,preview-bg:#ebe6db"
