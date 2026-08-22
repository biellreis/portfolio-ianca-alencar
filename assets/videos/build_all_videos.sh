#!/bin/bash
DIR="/Users/gabrielreis/Portfolio Ianca Alencar/assets/videos"

# 1. Generate Vertical 9:16 cuts (540x960, 30fps, CRF 22, silent, faststart)
# Reel 1: Aulão Manaus
ffmpeg -y -ss 00:00:00 -t 8 -i "$DIR/yt_viradao.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/ig_aulao.mp4"

# Reel 2: João Pessoa
ffmpeg -y -ss 00:00:00 -t 8 -i "$DIR/yt_portal.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/ig_joao_pessoa.mp4"

# Reel 3: PremiAstro
ffmpeg -y -ss 00:00:00 -t 8 -i "$DIR/yt_inclusao.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/ig_premiastro.mp4"

# Reel 4: Viradão 8k
ffmpeg -y -ss 00:00:00 -t 8 -i "$DIR/yt_aulao_saeb.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/ig_viradao.mp4"

# Reel 5: Professores
ffmpeg -y -ss 00:00:00 -t 8 -i "$DIR/yt_simulado.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/ig_professores.mp4"

# Reel 6: Bastidores
ffmpeg -y -ss 00:00:03 -t 8 -i "$DIR/yt_inclusao.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/3:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/ig_bastidores.mp4"

# Eventos
cp "$DIR/ig_joao_pessoa.mp4" "$DIR/event_joao_pessoa.mp4"
cp "$DIR/ig_premiastro.mp4" "$DIR/event_premiastro.mp4"
cp "$DIR/ig_viradao.mp4" "$DIR/event_viradao.mp4"
cp "$DIR/yt_viradao.mp4" "$DIR/event_live.mp4"

# TikTok Vertical clips
ffmpeg -y -ss 00:00:02 -t 8 -i "$DIR/yt_simulado.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/tiktok_experimento.mp4"
ffmpeg -y -ss 00:00:01 -t 8 -i "$DIR/yt_portal.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)*0.7:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/tiktok_rotina.mp4"
ffmpeg -y -ss 00:00:00 -t 8 -i "$DIR/yt_aulao_saeb.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/tiktok_dicas.mp4"
ffmpeg -y -ss 00:00:04 -t 8 -i "$DIR/yt_inclusao.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)*0.2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/tiktok_bastidores.mp4"
ffmpeg -y -ss 00:00:01 -t 8 -i "$DIR/yt_viradao.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=540:960" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$DIR/tiktok_quiz.mp4"

echo "All videos built successfully!"
ls -lh "$DIR"
