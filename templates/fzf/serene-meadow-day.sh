#!/bin/bash
# Serene Meadow Day theme for fzf
# A warm, light color scheme for daytime coding

export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:{{day.warm-ink}},bg:{{day.aged-paper}},hl:{{day.leaf}} \
  --color=fg+:{{day.warm-ink}},bg+:{{day.golden-sand}},hl+:{{day.plum}} \
  --color=info:{{day.weathered-stone}},prompt:{{day.plum}},pointer:{{day.plum}} \
  --color=marker:{{day.spruce}},spinner:{{day.spruce}},header:{{day.weathered-stone}} \
  --color=border:{{day.light-taupe}},gutter:{{day.pale-wheat}} \
  --color=preview-fg:{{day.warm-ink}},preview-bg:{{day.pale-wheat}}"
