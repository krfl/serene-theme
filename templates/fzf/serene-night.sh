#!/bin/bash
# Serene Night theme for fzf
# A warm, dark color scheme for nighttime coding

export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:{{night.parchment}},bg:{{night.deep-earth}},hl:{{night.meadow-sage}} \
  --color=fg+:{{night.parchment}},bg+:{{night.warm-umber}},hl+:{{night.sage-grass}} \
  --color=info:{{night.weathered-stone}},prompt:{{night.sage-grass}},pointer:{{night.sage-grass}} \
  --color=marker:{{night.honey}},spinner:{{night.honey}},header:{{night.weathered-stone}} \
  --color=border:{{night.warm-ink}},gutter:{{night.dark-walnut}} \
  --color=preview-fg:{{night.parchment}},preview-bg:{{night.dark-walnut}}"
