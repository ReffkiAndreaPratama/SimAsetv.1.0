"""
Activity Diagram — Alur Proses Inbound (OCR)
Gaya persis seperti contoh foto: swimlane vertikal, rounded rect,
diamond decision, fork/join bar hitam, panah dengan label
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

# ─────────────────────────────────────────────────────────────────────────────
# CANVAS
# ─────────────────────────────────────────────────────────────────────────────
W, H = 1700, 2400
img = Image.new("RGB", (W, H), (255, 255, 255))
d   = ImageDraw.Draw(img)

# ─────────────────────────────────────────────────────────────────────────────
# FONTS
# ─────────────────────────────────────────────────────────────────────────────
def get_font(size, bold=False):
    paths = []
    if bold:
        paths = ["C:/Windows/Fonts/arialbd.ttf","C:/Windows/Fonts/calibrib.ttf","C:/Windows/Fonts/verdanab.ttf"]
    else:
        paths = ["C:/Windows/Fonts/arial.ttf","C:/Windows/Fonts/calibri.ttf","C:/Windows/Fonts/verdana.ttf"]
    for p in paths:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

FT  = get_font(20, bold=True)   # title
FH  = get_font(14, bold=True)   # header
FB  = get_font(12)              # body
FS  = get_font(11)              # small
FL  = get_font(11)              # label on arrow

# ─────────────────────────────────────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────────────────────────────────────
TITLE_BG  = (26,  52, 112)
TITLE_FG  = (255,255,255)
HDR1      = (108,142,191)   # Operator header
HDR2      = (130,179,102)   # Sistem header
HDR3      = (214,182, 86)   # OCR header
BG1       = (218,232,252)   # Operator bg
BG2       = (213,232,212)   # Sistem bg
BG3       = (255,242,204)   # OCR bg
BOX_OP    = ((255,253,231),(214,182, 86))  # fill, stroke — Operator actions
BOX_SYS   = ((213,232,212),(130,179,102))  # Sistem actions
BOX_OCR   = ((255,242,204),(214,182, 86))  # OCR actions
BOX_ERR   = ((248,206,204),(184, 84, 80))  # error/fallback
BORDER    = (44, 62, 80)
BLACK     = (0,0,0)
GRAY      = (120,120,120)
NOTE_BG   = (255,250,205)
NOTE_BD   = (214,182, 86)

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT — 3 swimlane columns
# ─────────────────────────────────────────────────────────────────────────────
PAD      = 28
TITLE_H  = 48
HDR_H    = 34
SW_TOP   = PAD + TITLE_H + 2

SW_W = [310, 400, 930]          # widths: Operator, Sistem, OCR
SW_X = [PAD, PAD+SW_W[0], PAD+SW_W[0]+SW_W[1]]
SW_H = H - SW_TOP - PAD
TOTAL_W  = sum(SW_W)

CX = [SW_X[i] + SW_W[i]//2 for i in range(3)]   # center x of each lane

# ─────────────────────────────────────────────────────────────────────────────
# DRAW HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def rr(x0,y0,x1,y1, fill, stroke, sw=2, r=10):
    d.rounded_rectangle([x0,y0,x1,y1], radius=r, fill=fill, outline=stroke, width=sw)

def text_center(cx, cy, txt, font, color=(0,0,0)):
    lines = txt.split("\n")
    lh = font.size + 3
    total = lh * len(lines)
    y = cy - total//2
    for line in lines:
        bb = d.textbbox((0,0), line, font=font)
        tw = bb[2]-bb[0]
        d.text((cx - tw//2, y), line, font=font, fill=color)
        y += lh

def action(cx, cy, txt, w, h, colors=BOX_SYS, font=None):
    if font is None: font = FB
    x0,y0 = cx-w//2, cy-h//2
    rr(x0,y0,x0+w,y0+h, colors[0], colors[1])
    text_center(cx, cy, txt, font)
    return y0, y0+h   # top, bot

def diamond(cx, cy, txt, w=130, h=64):
    pts = [(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
    d.polygon(pts, fill=(255,242,204), outline=(214,182,86), width=2)
    text_center(cx, cy, txt, FS)
    return cy-h//2, cy+h//2

def fork_bar(x0, y, x1, h=8):
    d.rectangle([x0, y-h//2, x1, y+h//2], fill=BLACK)

def arrow(x1,y1,x2,y2, lbl="", lbl_side="right"):
    d.line([(x1,y1),(x2,y2)], fill=BLACK, width=2)
    ang = math.atan2(y2-y1, x2-x1)
    sz  = 9
    for da in [0.45,-0.45]:
        ax = x2 - sz*math.cos(ang-da)
        ay = y2 - sz*math.sin(ang-da)
        d.line([(x2,y2),(int(ax),int(ay))], fill=BLACK, width=2)
    if lbl:
        mx,my = (x1+x2)//2, (y1+y2)//2
        bb = d.textbbox((0,0), lbl, font=FL)
        tw = bb[2]-bb[0]
        off = 8 if lbl_side=="right" else -tw-8
        d.text((mx+off, my-14), lbl, font=FL, fill=GRAY)

def start_node(cx,cy,r=13):
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=BLACK)

def end_node(cx,cy,r=13):
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=BLACK)
    d.ellipse([cx-r+4,cy-r+4,cx+r-4,cy+r-4], fill=(255,255,255))
    d.ellipse([cx-r+8,cy-r+8,cx+r-8,cy+r-8], fill=BLACK)

def note_box(x,y,txt,w=190):
    lines = txt.split("\n")
    lh = FS.size+3
    h  = lh*len(lines)+12
    fold=12
    pts=[(x,y),(x+w-fold,y),(x+w,y+fold),(x+w,y+h),(x,y+h)]
    d.polygon(pts, fill=NOTE_BG, outline=NOTE_BD, width=1)
    d.line([(x+w-fold,y),(x+w-fold,y+fold),(x+w,y+fold)], fill=NOTE_BD, width=1)
    ty=y+6
    for line in lines:
        d.text((x+7,ty), line, font=FS, fill=(60,60,60))
        ty+=lh

def dashed_v(cx, y0, y1, color=(200,200,200)):
    y = y0
    while y < y1:
        d.line([(cx,y),(cx,min(y+5,y1))], fill=color, width=1)
        y += 10

# ─────────────────────────────────────────────────────────────────────────────
# DRAW FRAME
# ─────────────────────────────────────────────────────────────────────────────
# Title
d.rectangle([PAD, PAD, PAD+TOTAL_W, PAD+TITLE_H], fill=TITLE_BG)
text_center(PAD+TOTAL_W//2, PAD+TITLE_H//2,
            "act   Alur Proses Inbound — Penerimaan Barang dengan OCR", FT, TITLE_FG)

# Swimlane backgrounds
for i in range(3):
    bg = [BG1,BG2,BG3][i]
    d.rectangle([SW_X[i], SW_TOP, SW_X[i]+SW_W[i], SW_TOP+SW_H], fill=bg, outline=BORDER, width=2)

# Swimlane headers
hdrs = [("Operator", HDR1), ("Sistem (Laravel)", HDR2), ("OCR Microservice (FastAPI :8001)", HDR3)]
for i,(lbl,hc) in enumerate(hdrs):
    d.rectangle([SW_X[i], SW_TOP, SW_X[i]+SW_W[i], SW_TOP+HDR_H], fill=hc)
    text_center(CX[i], SW_TOP+HDR_H//2, lbl, FH, (255,255,255))

# Outer border
d.rectangle([PAD, PAD, PAD+TOTAL_W, SW_TOP+SW_H], outline=BORDER, width=3)

# Dashed center guides (subtle)
for i in range(3):
    dashed_v(CX[i], SW_TOP+HDR_H+5, SW_TOP+SW_H-5)

# ─────────────────────────────────────────────────────────────────────────────
# DIAGRAM ELEMENTS  (y increases downward)
# ─────────────────────────────────────────────────────────────────────────────
y = SW_TOP + HDR_H + 45

# ── START ─────────────────────────────────────────────────────────────────────
start_node(CX[0], y)
arrow(CX[0], y+13, CX[0], y+38)
y += 55

# ── 1. Operator: Unggah Foto Dokumen ─────────────────────────────────────────
t,b = action(CX[0], y, "Unggah Foto\nDokumen", 220, 50, BOX_OP)
# cross-lane arrow to Sistem
arrow(CX[0]+110, y, CX[1]-200, y)
arrow(CX[0], b, CX[0], b+20)
y_op1 = y

# ── 2. Sistem: InboundController → OcrService ────────────────────────────────
t2,b2 = action(CX[1], y, "InboundController\n→ OcrService.php (client)", 320, 50, BOX_SYS)
arrow(CX[1], b2, CX[1], b2+22)
y += 75

# ── 3. Sistem: Konversi ke base64 ────────────────────────────────────────────
t3,b3 = action(CX[1], y, "Konversi file ke base64", 280, 44, BOX_SYS)
arrow(CX[1], b3, CX[1], b3+22)
y += 68

# ── 4. Sistem: HTTP POST → FastAPI ───────────────────────────────────────────
t4,b4 = action(CX[1], y, "HTTP POST → FastAPI\n(port 8001)  /ocr  endpoint", 320, 50, BOX_SYS)
# cross-lane arrow to OCR
arrow(CX[1]+160, y, CX[2]-280, y)
y += 75

# ── 5. OCR: Deteksi tipe dokumen ─────────────────────────────────────────────
t5,b5 = action(CX[2], y, "Deteksi Tipe Dokumen\n(SIR20 / RSS1 / DO / SK)", 400, 50, BOX_OCR)
arrow(CX[2], b5, CX[2], b5+22)
y += 75

# ── 6. OCR: Pipeline Preprocessing ──────────────────────────────────────────
t6,b6 = action(CX[2], y,
    "Pipeline Preprocessing:\nEXIF Rotate  →  Auto-Crop  →  Deskew\n→  CLAHE  →  Resize",
    560, 62, BOX_OCR)
arrow(CX[2], b6, CX[2], b6+22)
y += 90

# ── 7. FORK bar ───────────────────────────────────────────────────────────────
FORK_X0 = CX[2] - 230
FORK_X1 = CX[2] + 230
fork_bar(FORK_X0, y, FORK_X1)
arrow(CX[2], y-22, CX[2], y-4)
d.text((FORK_X0, y+6), "«fork»  — Fire parallel requests (Racing Strategy)", font=FS, fill=GRAY)

CX_L = CX[2] - 185   # Groq branch center
CX_R = CX[2] + 185   # OpenRouter branch center

arrow(CX_L, y+4, CX_L, y+38)
arrow(CX_R, y+4, CX_R, y+38)
y_fork = y
y += 58

# ── 8a/8b. Parallel: Groq + OpenRouter ───────────────────────────────────────
action(CX_L, y, "Request ke\nGroq API", 200, 48, BOX_OCR)
action(CX_R, y, "Request ke\nOpenRouter API", 200, 48, BOX_OCR)
arrow(CX_L, y+24, CX_L, y+55)
arrow(CX_R, y+24, CX_R, y+55)
y += 75

# ── 9. JOIN bar ───────────────────────────────────────────────────────────────
fork_bar(FORK_X0, y, FORK_X1)
arrow(CX_L, y-4, CX_L, y)
arrow(CX_R, y-4, CX_R, y)
d.text((FORK_X0, y+6), "«join»  — Terima respons pertama yang valid (JSON)", font=FS, fill=GRAY)
arrow(CX[2], y+4, CX[2], y+38)
y += 58

# ── 10. OCR: Post-processing ─────────────────────────────────────────────────
t10,b10 = action(CX[2], y,
    "Post-processing:\nFix ditto marks  ·  Cross-validate bale count\nFix year  ·  Validasi struktur JSON",
    580, 62, BOX_OCR)
arrow(CX[2], b10, CX[2], b10+22)
y += 90

# ── 11. Decision: JSON valid? ────────────────────────────────────────────────
top_d, bot_d = diamond(CX[2], y, "JSON\nvalid?", w=130, h=64)
arrow(CX[2], bot_d, CX[2], bot_d+35, "Ya")

# Tidak → fallback note
arrow(CX[2]+65, y, CX[2]+290, y, "Tidak")
note_box(CX[2]+295, y-35,
         "Fallback:\nCoba model\nberikutnya\natau return\nerror 422", w=170)

y = bot_d + 55

# ── 12. OCR: Kembalikan JSON ─────────────────────────────────────────────────
t12,b12 = action(CX[2], y, "Kembalikan JSON hasil\nekstraksi ke Laravel", 380, 50, BOX_OCR)
# cross-lane arrow back to Sistem
arrow(CX[2]-190, y, CX[1]+160, y)
y += 75

# ── 13. Sistem: Pre-filled Form + Preview ────────────────────────────────────
t13,b13 = action(CX[1], y, "Tampilkan Pre-filled Form\n+ Preview Gambar Dokumen", 340, 50, BOX_SYS)
# cross-lane arrow to Operator
arrow(CX[1]-170, y, CX[0]+110, y)
y += 75

# ── 14. Operator: Review & Koreksi ───────────────────────────────────────────
t14,b14 = action(CX[0], y, "Review & Koreksi\n(Human-in-the-Loop)", 240, 50, BOX_OP)
arrow(CX[0], b14, CX[0], b14+22)
y += 75

# ── 15. Decision: Data benar? ────────────────────────────────────────────────
top_d2, bot_d2 = diamond(CX[0], y, "Data\nbenar?", w=120, h=60)
arrow(CX[0], bot_d2, CX[0], bot_d2+35, "Ya")

# Tidak → loop back to review
arrow(CX[0]-60, y, CX[0]-140, y, "Tidak", lbl_side="left")
arrow(CX[0]-140, y, CX[0]-140, y-75)
arrow(CX[0]-140, y-75, CX[0]-120, y-75)

y = bot_d2 + 55

# ── 16. Operator: Submit ─────────────────────────────────────────────────────
t16,b16 = action(CX[0], y, "Submit Form", 200, 44, BOX_OP)
# cross-lane arrow to Sistem
arrow(CX[0]+100, y, CX[1]-170, y)
y += 68

# ── 17. Sistem: Simpan ke DB + Update Stok ───────────────────────────────────
t17,b17 = action(CX[1], y, "Simpan Data ke Database\n+ Update Stok Barang", 340, 50, BOX_SYS)
arrow(CX[1], b17, CX[1], b17+22)
y += 75

# ── 18. Sistem: Konfirmasi ────────────────────────────────────────────────────
t18,b18 = action(CX[1], y, "Tampilkan Konfirmasi\nBerhasil", 280, 44, BOX_SYS)
# cross-lane arrow to Operator
arrow(CX[1]-140, y, CX[0]+110, y)
y += 68

# ── 19. Operator: Selesai ─────────────────────────────────────────────────────
t19,b19 = action(CX[0], y, "Proses Selesai", 200, 44, BOX_OP)
arrow(CX[0], b19, CX[0], b19+30)
y += 75

# ── END ───────────────────────────────────────────────────────────────────────
end_node(CX[0], y)

# ─────────────────────────────────────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────────────────────────────────────
out = "docs/diagrams/drawio/Activity_Inbound_OCR.png"
img.save(out, "PNG", dpi=(150,150))
print(f"Saved: {out}  ({W}x{H}px)")
