#!/bin/bash
DIR="/Users/gabrielreis/Portfolio Ianca Alencar/assets/videos"

posts=(
  "DPmZD-pjpeJ:ig_aulao"
  "DVEFdSNDpJL:ig_joao_pessoa"
  "DSJR8OHDmfh:ig_premiastro"
  "DPrOV72DhB7:ig_viradao"
  "DM1BsG9vdgX:ig_professores"
  "DQ9dVa3DswU:ig_bastidores"
)

for item in "${posts[@]}"; do
  id="${item%%:*}"
  name="${item##*:}"
  echo "Downloading Instagram post $name ($id)..."
  /opt/homebrew/bin/yt-dlp --cookies-from-browser safari -f "best[ext=mp4]/best" \
    --force-overwrites \
    -o "$DIR/${name}_raw.%(ext)s" \
    "https://www.instagram.com/p/${id}/"
    
  raw_file=$(ls "$DIR/${name}_raw."* 2>/dev/null | head -n 1)
  if [ -n "$raw_file" ]; then
    # Generate high quality looping preview (8-10 seconds, 720p vertical, faststart, silent)
    ffmpeg -y -i "$raw_file" -t 12 -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -an -movflags +faststart "$DIR/${name}.mp4"
    rm "$raw_file"
    echo "Created $DIR/${name}.mp4"
  fi
done

# Clean any leftover downloaded full videos from workspace root if any
rm -f /Users/gabrielreis/Portfolio\ Ianca\ Alencar/Video\ by\ superensino*

ls -lh "$DIR"/ig_*.mp4
