#!/bin/bash
# Serene Day theme for fzf
# A warm, light color scheme for daytime coding

export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \
  --color=fg:{{day.warm-ink}},bg:{{day.aged-paper}},hl:{{day.forest}} \
  --color=fg+:{{day.warm-ink}},bg+:{{day.golden-sand}},hl+:{{day.olive}} \
  --color=info:{{day.weathered-stone}},prompt:{{day.olive}},pointer:{{day.olive}} \
  --color=marker:{{day.bronze}},spinner:{{day.bronze}},header:{{day.weathered-stone}} \
  --color=border:{{day.light-taupe}},gutter:{{day.pale-wheat}} \
  --color=preview-fg:{{day.warm-ink}},preview-bg:{{day.pale-wheat}}"
