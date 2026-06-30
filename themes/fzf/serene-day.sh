#!/bin/bash
# Serene Day theme for fzf
# A warm, light color scheme for daytime coding

export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:#3d3a33,bg:#f5f2ed,hl:#536f44 \
  --color=fg+:#3d3a33,bg+:#e3d5b8,hl+:#606b44 \
  --color=info:#6e665a,prompt:#606b44,pointer:#606b44 \
  --color=marker:#875f33,spinner:#875f33,header:#6e665a \
  --color=border:#d4cfc4,gutter:#ebe6db \
  --color=preview-fg:#3d3a33,preview-bg:#ebe6db"
