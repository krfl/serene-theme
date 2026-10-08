#!/bin/bash
# Serene Meadow Night theme for fzf
# A warm, dark color scheme for nighttime coding

export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:{{night.parchment}},bg:{{night.deep-earth}},hl:{{night.leaf}} \
  --color=fg+:{{night.parchment}},bg+:{{night.warm-umber}},hl+:{{night.plum}} \
  --color=info:{{night.weathered-stone}},prompt:{{night.plum}},pointer:{{night.plum}} \
  --color=marker:{{night.spruce}},spinner:{{night.spruce}},header:{{night.weathered-stone}} \
  --color=border:{{night.warm-ink}},gutter:{{night.dark-walnut}} \
  --color=preview-fg:{{night.parchment}},preview-bg:{{night.dark-walnut}}"
