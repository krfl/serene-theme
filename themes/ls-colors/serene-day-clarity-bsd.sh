#!/bin/bash
# Serene Day Clarity - LSCOLORS configuration for BSD ls (macOS default)
# Source this file in your shell: source serene-day-clarity-bsd.sh
# Or add it to your ~/.bashrc or ~/.zshrc

# LSCOLORS format (BSD ls on macOS):
# 11 pairs of letters (foreground + background) for:
# 1. directory
# 2. symbolic link
# 3. socket
# 4. pipe
# 5. executable
# 6. block special
# 7. character special
# 8. executable with setuid
# 9. executable with setgid
# 10. directory writable by others, with sticky bit
# 11. directory writable by others, without sticky bit

# Color codes:
# a = black, b = red, c = green, d = brown, e = blue, f = magenta, g = cyan, h = light grey
# A-H = bold versions of the above
# x = default (transparent background)

# Serene Day Clarity mapping:
# directories: green (cx - green, default bg)
# symlinks: cyan (gx - cyan, default bg)
# executables: yellow (dx - brown/yellow, default bg)
# special files: appropriate colors matching theme

export LSCOLORS="cxgxfxdxbxegedabagacad"

# For GNU ls (if installed via homebrew: brew install coreutils)
# This provides much richer color support
export LS_COLORS="\
rs=0:\
di=32:\
ln=36:\
mh=00:\
pi=40;33:\
so=35:\
do=35:\
bd=40;33;\
cd=40;33:\
or=40;31:\
mi=37;41:\
su=37;41:\
sg=30;43:\
ca=30;41:\
tw=30;42:\
ow=34;42:\
st=37;44:\
ex=1;33:\
*.tar=31:\
*.tgz=31:\
*.arc=31:\
*.arj=31:\
*.taz=31:\
*.lha=31:\
*.lz4=31:\
*.lzh=31:\
*.lzma=31:\
*.tlz=31:\
*.txz=31:\
*.tzo=31:\
*.t7z=31:\
*.zip=31:\
*.z=31:\
*.dz=31:\
*.gz=31:\
*.lrz=31:\
*.lz=31:\
*.lzo=31:\
*.xz=31:\
*.zst=31:\
*.tzst=31:\
*.bz2=31:\
*.bz=31:\
*.tbz=31:\
*.tbz2=31:\
*.tz=31:\
*.deb=31:\
*.rpm=31:\
*.jar=31:\
*.war=31:\
*.ear=31:\
*.sar=31:\
*.rar=31:\
*.alz=31:\
*.ace=31:\
*.zoo=31:\
*.cpio=31:\
*.7z=31:\
*.rz=31:\
*.cab=31:\
*.wim=31:\
*.swm=31:\
*.dwm=31:\
*.esd=31:\
*.jpg=35:\
*.jpeg=35:\
*.mjpg=35:\
*.mjpeg=35:\
*.gif=35:\
*.bmp=35:\
*.pbm=35:\
*.pgm=35:\
*.ppm=35:\
*.tga=35:\
*.xbm=35:\
*.xpm=35:\
*.tif=35:\
*.tiff=35:\
*.png=35:\
*.svg=35:\
*.svgz=35:\
*.mng=35:\
*.pcx=35:\
*.mov=35:\
*.mpg=35:\
*.mpeg=35:\
*.m2v=35:\
*.mkv=35:\
*.webm=35:\
*.webp=35:\
*.ogm=35:\
*.mp4=35:\
*.m4v=35:\
*.mp4v=35:\
*.vob=35:\
*.qt=35:\
*.nuv=35:\
*.wmv=35:\
*.asf=35:\
*.rm=35:\
*.rmvb=35:\
*.flc=35:\
*.avi=35:\
*.fli=35:\
*.flv=35:\
*.gl=35:\
*.dl=35:\
*.xcf=35:\
*.xwd=35:\
*.yuv=35:\
*.cgm=35:\
*.emf=35:\
*.ogv=35:\
*.ogx=35:\
*.aac=35:\
*.au=35:\
*.flac=35:\
*.m4a=35:\
*.mid=35:\
*.midi=35:\
*.mka=35:\
*.mp3=35:\
*.mpc=35:\
*.ogg=35:\
*.ra=35:\
*.wav=35:\
*.oga=35:\
*.opus=35:\
*.spx=35:\
*.xspf=35:\
*.pdf=31:\
*.ps=31:\
*.txt=30:\
*.patch=30:\
*.diff=30:\
*.log=90:\
*.tex=30:\
*.doc=35:\
*.docx=35:\
*.ppt=35:\
*.pptx=35:\
*.xls=35:\
*.xlsx=35:\
*.md=30:\
*.markdown=30:\
*.json=33:\
*.yaml=33:\
*.yml=33:\
*.xml=33:\
*.toml=33:\
*.ini=33:\
*.conf=33:\
*.config=33:\
*.py=32:\
*.js=32:\
*.ts=32:\
*.jsx=32:\
*.tsx=32:\
*.sh=32:\
*.bash=32:\
*.zsh=32:\
*.fish=32:\
*.rb=32:\
*.go=32:\
*.rs=32:\
*.c=32:\
*.cpp=32:\
*.h=32:\
*.hpp=32:\
*.java=32:\
*.class=35:\
*.vim=32:\
*.lua=32:\
*.php=32:\
*.css=35:\
*.scss=35:\
*.html=33:\
*.htm=33:\
"

# Enable color output for ls
export CLICOLOR=1

echo "Serene Day Clarity (BSD/macOS) colors loaded"
