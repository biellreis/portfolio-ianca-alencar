import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Canvas dimensions (Standard Open Graph 1200 x 630 px)
W, H = 1200, 630

# 1. Base Dark Canvas
img = Image.new('RGB', (W, H), '#0A080D')

# 2. Glowing Radial Lights (Luxury Obsidian & Rose Quartz / Champagne)
glow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_layer)

def draw_radial_gradient(d, cx, cy, radius, r, g, b, alpha_max):
    for i in range(radius, 0, -4):
        ratio = i / radius
        alpha = int(alpha_max * (1.0 - math.pow(ratio, 1.4)))
        if alpha > 0:
            d.ellipse([cx - i, cy - i, cx + i, cy + i], fill=(r, g, b, alpha))

# Large Rose Quartz ambient light on right orb
draw_radial_gradient(glow_draw, 980, 270, 460, 255, 122, 158, 150)
# Warm Champagne / Amethyst on bottom-left
draw_radial_gradient(glow_draw, 240, 520, 420, 192, 132, 252, 70)
draw_radial_gradient(glow_draw, 640, 150, 360, 247, 215, 181, 60)

glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(32))
img.paste(Image.alpha_composite(Image.new('RGBA', (W, H), (10, 8, 13, 255)), glow_layer).convert('RGB'), (0, 0))

# 3. Card Frame (Satin Glass Bento Frame with Smooth Glow)
margin = 26
card_rect = [margin, margin, W - margin, H - margin]
card_overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
card_draw = ImageDraw.Draw(card_overlay)

# Dark glass panel fill
card_draw.rounded_rectangle(card_rect, radius=24, fill=(18, 12, 26, 180), outline=(255, 182, 205, 60), width=2)
# Top satin light reflection
card_draw.line([(margin + 28, margin + 1), (W - margin - 28, margin + 1)], fill=(255, 195, 215, 160), width=2)

img_rgba = Image.alpha_composite(img.convert('RGBA'), card_overlay)
img = img_rgba.convert('RGB')

# 4. Fonts
font_outfit = 'assets/fonts/Outfit.ttf'
font_sans = 'assets/fonts/PlusJakartaSans.ttf'

font_badge = ImageFont.truetype(font_sans, 13)
font_title = ImageFont.truetype(font_outfit, 76)
font_h1 = ImageFont.truetype(font_outfit, 34)
font_h2 = ImageFont.truetype(font_outfit, 34)
font_pill_title = ImageFont.truetype(font_sans, 15)
font_pill_desc = ImageFont.truetype(font_sans, 13)
font_footer = ImageFont.truetype(font_sans, 14)
font_orb_ia = ImageFont.truetype(font_outfit, 72)
font_orb_sub = ImageFont.truetype(font_sans, 12)

# Helper function to draw bold text via subpixel offsets
def draw_text_bold(target_draw, pos, text, font, fill, weight=2):
    x, y = pos
    for dx in range(weight):
        for dy in range(weight):
            target_draw.text((x + dx, y + dy), text, font=font, fill=fill)

draw = ImageDraw.Draw(img)

# 5. Top Eyebrow Badge: "MARKETING ESTRATÉGICO & AUDIOVISUAL"
bx, by = 68, 62
badge_text = "MARKETING ESTRATÉGICO & AUDIOVISUAL"
badge_bbox = font_badge.getbbox(badge_text)
bw = badge_bbox[2] - badge_bbox[0] + 44
bh = 32

badge_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bdraw = ImageDraw.Draw(badge_layer)
bdraw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=999, fill=(255, 122, 158, 30), outline=(255, 182, 205, 95), width=1)
# Glowing dot inside badge
bdraw.ellipse([bx + 12, by + 11, bx + 20, by + 19], fill=(255, 122, 158, 255))
bdraw.ellipse([bx + 14, by + 13, bx + 18, by + 17], fill=(255, 255, 255, 255))

img_rgba = Image.alpha_composite(img.convert('RGBA'), badge_layer)
img = img_rgba.convert('RGB')
draw = ImageDraw.Draw(img)
draw_text_bold(draw, (bx + 28, by + 7), badge_text, font=font_badge, fill='#FF7A9E', weight=1)

# 6. Main Name Title: "Ianca Alencar" (Bolded & Glowing)
draw_text_bold(draw, (68, 116), "Ianca Alencar", font=font_title, fill='#FAF6F8', weight=2)

# 7. Impact Headline: "Estratégia comprovada que gera resultados reais."
line1 = "Estratégia comprovada "
line2 = "que gera resultados reais."
ly = 218
draw_text_bold(draw, (68, ly), line1, font=font_h1, fill='#FAF6F8', weight=2)
bbox1 = font_h1.getbbox(line1)
w1 = bbox1[2] - bbox1[0]
draw_text_bold(draw, (68 + w1, ly), line2, font=font_h2, fill='#FF7A9E', weight=2)

# Subtitle explanation
subtitle = "Liderança de equipes criativas, crescimento orgânico, grandes eventos e produções 4K."
draw.text((68, 270), subtitle, font=font_footer, fill='#BCAAB8')

# 8. 4 Bento Grid Cards (2x2 Grid with balanced spacing)
bento_cards = [
    ("01", "Equipes & Gestão Ágil", "Processos claros e alto padrão", 68, 324),
    ("02", "+50% Audiência Real", "Crescimento orgânico qualificado", 442, 324),
    ("03", "600+ Grandes Eventos", "Experiência de palco e estrutura", 68, 412),
    ("04", "Cinema 4K & Ao Vivo", "Produção de vídeo e broadcast", 442, 412),
]

bento_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bdraw = ImageDraw.Draw(bento_layer)

for num, title, desc, px, py in bento_cards:
    pw, ph = 354, 72
    bdraw.rounded_rectangle([px, py, px + pw, py + ph], radius=14, fill=(34, 22, 46, 210), outline=(255, 182, 205, 55), width=1)

img_rgba = Image.alpha_composite(img.convert('RGBA'), bento_layer)
img = img_rgba.convert('RGB')
draw = ImageDraw.Draw(img)

for num, title, desc, px, py in bento_cards:
    num_str = f"{num} · "
    nbox = font_pill_title.getbbox(num_str)
    nw = nbox[2] - nbox[0]
    
    draw_text_bold(draw, (px + 16, py + 14), num_str, font=font_pill_title, fill='#FF7A9E', weight=2)
    draw_text_bold(draw, (px + 16 + nw, py + 14), title, font=font_pill_title, fill='#FAF6F8', weight=2)
    draw.text((px + 16, py + 40), desc, font=font_pill_desc, fill='#9E8D9D')

# 9. Right Stage: 3D Frosted Glass Orb with Monogram "IA"
orb_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
odraw = ImageDraw.Draw(orb_layer)

ox, oy = 990, 270
# Concentric light rings
odraw.ellipse([ox - 150, oy - 150, ox + 150, oy + 150], outline=(255, 182, 205, 30), width=1)
odraw.ellipse([ox - 126, oy - 126, ox + 126, oy + 126], outline=(255, 182, 205, 60), width=2)

# Frosted Glass Sphere
r_orb = 96
# Subtle gradient inside orb
for r_step in range(r_orb, 0, -2):
    ratio = r_step / r_orb
    r_val = int(48 + 30 * (1 - ratio))
    g_val = int(24 + 15 * (1 - ratio))
    b_val = int(60 + 40 * (1 - ratio))
    odraw.ellipse([ox - r_step, oy - r_step, ox + r_step, oy + r_step], fill=(r_val, g_val, b_val, 240))

odraw.ellipse([ox - r_orb, oy - r_orb, ox + r_orb, oy + r_orb], outline=(255, 215, 230, 180), width=2)

img_rgba = Image.alpha_composite(img.convert('RGBA'), orb_layer)
img = img_rgba.convert('RGB')
draw = ImageDraw.Draw(img)

# Monogram "IA" in center of Orb
ia_text = "IA"
ibox = font_orb_ia.getbbox(ia_text)
iw = ibox[2] - ibox[0]
ih = ibox[3] - ibox[1]
draw_text_bold(draw, (ox - iw//2, oy - ih//2 - 4), ia_text, font=font_orb_ia, fill='#FFFFFF', weight=2)

# Satin pill below Orb
pill_orb_text = "PORTFÓLIO OFICIAL"
pobox = font_orb_sub.getbbox(pill_orb_text)
pow = pobox[2] - pobox[0] + 28
poh = 28
pox, poy = ox - pow//2, oy + 116

orb_pill_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
opdraw = ImageDraw.Draw(orb_pill_layer)
opdraw.rounded_rectangle([pox, poy, pox + pow, poy + poh], radius=999, fill=(255, 122, 158, 30), outline=(255, 182, 205, 80), width=1)
img_rgba = Image.alpha_composite(img.convert('RGBA'), orb_pill_layer)
img = img_rgba.convert('RGB')
draw = ImageDraw.Draw(img)
draw_text_bold(draw, (pox + 14, poy + 6), pill_orb_text, font=font_orb_sub, fill='#FBBFD0', weight=1)

# 10. Bottom Footer Divider & Labels
div_y = 525
draw.line([(68, div_y), (W - 68, div_y)], fill=(255, 182, 205, 40), width=1)

# Left footer with star
draw.ellipse([68, 558, 74, 564], fill='#FF7A9E')
draw.text((84, 553), "Direção Criativa & Estratégia · Super Ensino", font=font_footer, fill='#FAF6F8')
draw.text((W - 350, 553), "Manaus, AM · Brasil", font=font_footer, fill='#BCAAB8')

# 11. Save Optimized JPEG
img.save('assets/og-image.jpg', 'JPEG', quality=95, optimize=True)
print("Successfully generated finalized assets/og-image.jpg (1200x630)")
