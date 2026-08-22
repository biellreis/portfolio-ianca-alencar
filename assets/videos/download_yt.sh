#!/bin/bash
videos=(
  "qeDnCzRX0CM:yt_aulao_saeb"
  "PxFWjh2ZCoI:yt_portal"
  "PWyqmtj5CQQ:yt_simulado"
  "qV4ElqEn6fE:yt_viradao"
)

for item in "${videos[@]}"; do
  id="${item%%:*}"
  name="${item##*:}"
  echo "Downloading $name ($id)..."
  /opt/homebrew/bin/yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" \
    --download-sections "*00:05-00:13" \
    --force-overwrites \
    -o "/Users/gabrielreis/Portfolio Ianca Alencar/assets/videos/${name}_raw.%(ext)s" \
    "https://www.youtube.com/watch?v=$id"
    
  raw_file=$(ls "/Users/gabrielreis/Portfolio Ianca Alencar/assets/videos/${name}_raw."* 2>/dev/null | head -n 1)
  if [ -n "$raw_file" ]; then
    ffmpeg -y -i "$raw_file" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "/Users/gabrielreis/Portfolio Ianca Alencar/assets/videos/${name}.mp4"
    rm "$raw_file"
  fi
done
