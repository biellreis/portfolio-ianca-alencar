import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Canvas dimensions (Standard Open Graph 1200 x 630 px)
W, H = 1200, 630

# 1. Base Dark Canvas
img = Image.new('RGB', (W, H), '#0A080D')

# 2. Glowing Radial Lights (Luxury Silk Obsidian & Rose Quartz / Champagne)
glow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_layer)

def draw_radial_gradient(d, cx, cy, radius, r, g, b, alpha_max):
    for i in range(radius, 0, -4):
        ratio = i / radius
        alpha = int(alpha_max * (1.0 - math.pow(ratio, 1.4)))
        if alpha > 0:
            d.ellipse([cx - i, cy - i, cx + i, cy + i], fill=(r, g, b, alpha))

# Large Rose Quartz ambient light on top right
draw_radial_gradient(glow_draw, 960, 200, 480, 255, 122, 158, 110)
# Warm Champagne / Orchid depth on bottom-left
draw_radial_gradient(glow_draw, 220, 520, 440, 192, 132, 252, 70)
# Soft center glow
draw_radial_gradient(glow_draw, 600, 280, 380, 247, 215, 181, 50)

glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(32))
img.paste(Image.alpha_composite(Image.new('RGBA', (W, H), (10, 8, 13, 255)), glow_layer).convert('RGB'), (0, 0))

# 3. Card Frame (Satin Glass Bento Frame with Smooth Glow)
margin = 26
card_rect = [margin, margin, W - margin, H - margin]
card_overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
card_draw = ImageDraw.Draw(card_overlay)

# Dark glass panel fill
card_draw.rounded_rectangle(card_rect, radius=24, fill=(18, 12, 26, 175), outline=(255, 182, 205, 55), width=2)
# Top satin light reflection
card_draw.line([(margin + 28, margin + 1), (W - margin - 28, margin + 1)], fill=(255, 195, 215, 150), width=2)

img_rgba = Image.alpha_composite(img.convert('RGBA'), card_overlay)
img = img_rgba.convert('RGB')

# 4. Fonts
font_outfit = 'assets/fonts/Outfit.ttf'
font_sans = 'assets/fonts/PlusJakartaSans.ttf'

font_badge = ImageFont.truetype(font_sans, 13)
font_title = ImageFont.truetype(font_outfit, 82)
font_h1 = ImageFont.truetype(font_outfit, 38)
font_h2 = ImageFont.truetype(font_outfit, 38)
font_pill_title = ImageFont.truetype(font_sans, 16)
font_pill_desc = ImageFont.truetype(font_sans, 13)
font_footer = ImageFont.truetype(font_sans, 14)

# Helper function to draw bold text via subpixel offsets
def draw_text_bold(target_draw, pos, text, font, fill, weight=2):
    x, y = pos
    for dx in range(weight):
        for dy in range(weight):
            target_draw.text((x + dx, y + dy), text, font=font, fill=fill)

draw = ImageDraw.Draw(img)

# 5. Top Eyebrow (Clean text without border/circle pill)
bx, by = 68, 62
badge_text = "MARKETING ESTRATÉGICO & AUDIOVISUAL"

# Draw subtle dot indicator
draw.ellipse([bx, by + 4, bx + 7, by + 11], fill='#FF7A9E')
draw_text_bold(draw, (bx + 16, by), badge_text, font=font_badge, fill='#FF7A9E', weight=1)

# 6. Main Name Title: "Ianca Alencar" (Large & Luxurious)
draw_text_bold(draw, (68, 102), "Ianca Alencar", font=font_title, fill='#FAF6F8', weight=2)

# 7. Impact Headline: "Estratégia comprovada que gera resultados reais."
line1 = "Estratégia comprovada "
line2 = "que gera resultados reais."
ly = 212
draw_text_bold(draw, (68, ly), line1, font=font_h1, fill='#FAF6F8', weight=2)
bbox1 = font_h1.getbbox(line1)
w1 = bbox1[2] - bbox1[0]
draw_text_bold(draw, (68 + w1, ly), line2, font=font_h2, fill='#FF7A9E', weight=2)

# Subtitle explanation
subtitle = "Liderança de equipes criativas, crescimento orgânico, grandes eventos e produções 4K."
draw.text((68, 268), subtitle, font=font_footer, fill='#BCAAB8')

# 8. 4 Wide Bento Cards (2x2 Grid spanning the full width)
# Total content width = 1200 - 68*2 = 1064px. Two cards of 518px with 28px gap.
cw, ch = 518, 76
gap_x = 28
row1_y = 324
row2_y = 414

bento_cards = [
    ("01", "Equipes & Gestão Ágil", "Coordenação ativa de processos claros e alto padrão", 68, row1_y),
    ("02", "+50% Audiência Real", "Crescimento orgânico qualificado sem atalhos", 68 + cw + gap_x, row1_y),
    ("03", "600+ Grandes Eventos", "Planejamento de palco, iluminação e estrutura", 68, row2_y),
    ("04", "Cinema 4K & Ao Vivo", "Produções audiovisuais e transmissões estáveis", 68 + cw + gap_x, row2_y),
]

bento_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bdraw = ImageDraw.Draw(bento_layer)

for num, title, desc, px, py in bento_cards:
    bdraw.rounded_rectangle([px, py, px + cw, py + ch], radius=14, fill=(34, 22, 46, 210), outline=(255, 182, 205, 55), width=1)

img_rgba = Image.alpha_composite(img.convert('RGBA'), bento_layer)
img = img_rgba.convert('RGB')
draw = ImageDraw.Draw(img)

for num, title, desc, px, py in bento_cards:
    num_str = f"{num} · "
    nbox = font_pill_title.getbbox(num_str)
    nw = nbox[2] - nbox[0]
    
    draw_text_bold(draw, (px + 20, py + 16), num_str, font=font_pill_title, fill='#FF7A9E', weight=2)
    draw_text_bold(draw, (px + 20 + nw, py + 16), title, font=font_pill_title, fill='#FAF6F8', weight=2)
    draw.text((px + 20, py + 42), desc, font=font_pill_desc, fill='#9E8D9D')

# 9. Bottom Footer Divider & Labels
div_y = 525
draw.line([(68, div_y), (W - 68, div_y)], fill=(255, 182, 205, 40), width=1)

# Left footer
draw.ellipse([68, 558, 74, 564], fill='#FF7A9E')
draw.text((84, 553), "Direção Criativa & Estratégia · Super Ensino", font=font_footer, fill='#FAF6F8')
draw.text((W - 350, 553), "Manaus, AM · Brasil", font=font_footer, fill='#BCAAB8')

# 10. Save Optimized JPEG
img.save('assets/og-image.jpg', 'JPEG', quality=95, optimize=True)
print("Successfully generated clean, ultra-luxury assets/og-image.jpg (1200x630)")
