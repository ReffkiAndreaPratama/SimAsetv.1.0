"""
Generate Activity Diagram PNG — Alur Proses Inbound (OCR)
Gaya: swimlane 3 kolom, rounded rect, diamond, fork/join bar
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

# ── Canvas ────────────────────────────────────────────────────────────────────
W, H = 1654, 2200
BG   = (255, 255, 255)
img  = Image.new("RGB", (W, H), BG)
d    = ImageDraw.Draw(img)

# ── Fonts ─────────────────────────────────────────────────────────────────────
def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/Arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

F_TITLE  = font(22, bold=True)
F_HEADER = font(15, bold=True)
F_BODY   = font(13)
F_SMALL  = font(11)
F_LABEL  = font(12)

# ── Colors ────────────────────────────────────────────────────────────────────
C_TITLE_BG   = (26,  52, 112)   # dark blue header
C_TITLE_FG   = (255, 255, 255)
C_SW1_BG     = (218, 232, 252)  # Operator  — light blue
C_SW1_HDR    = (108, 142, 191)
C_SW2_BG     = (213, 232, 212)  # Sistem    — light green
C_SW2_HDR    = (130, 179, 102)
C_SW3_BG     = (255, 242, 204)  # OCR Microservice — yellow
C_SW3_HDR    = (214, 182, 86)
C_ACTION_BG  = (255, 253, 231)  # action box fill
C_ACTION_BD  = (214, 182, 86)   # action box border
C_PROC_BG    = (213, 232, 212)
C_PROC_BD    = (130, 179, 102)
C_OCR_BG     = (255, 242, 204)
C_OCR_BD     = (214, 182, 86)
C_FORK       = (0,   0,   0)
C_ARROW      = (0,   0,   0)
C_DECISION   = (255, 242, 204)
C_DECISION_BD= (214, 182, 86)
C_START      = (0,   0,   0)
C_END_OUTER  = (0,   0,   0)
C_END_INNER  = (0,   0,   0)
C_BORDER     = (44,  62,  80)
C_NOTE_BG    = (255, 250, 205)
C_NOTE_BD    = (214, 182, 86)

# ── Layout ────────────────────────────────────────────────────────────────────
MARGIN   = 30
TITLE_H  = 50
HDR_H    = 36
SW_TOP   = MARGIN + TITLE_H + 4   # y where swimlanes start

# 3 swimlane columns
SW_W1 = 320   # Operator
SW_W2 = 420   # Sistem (Laravel)
SW_W3 = 820   # OCR Microservice
SW_TOTAL = SW_W1 + SW_W2 + SW_W3

X1 = MARGIN              # Operator left
X2 = MARGIN + SW_W1      # Sistem left
X3 = MARGIN + SW_W1 + SW_W2  # OCR left

SW_H = H - SW_TOP - MARGIN

# ── Helpers ───────────────────────────────────────────────────────────────────
def rounded_rect(draw, xy, r=10, fill=None, outline=None, width=2):
    x0,y0,x1,y1 = xy
    draw.rounded_rectangle([x0,y0,x1,y1], radius=r, fill=fill, outline=outline, width=width)

def center_text(draw, cx, cy, text, font, fill=(0,0,0)):
    lines = text.split("\n")
    lh = font.size + 4
    total = lh * len(lines)
    y = cy - total // 2
    for line in lines:
        bb = draw.textbbox((0,0), line, font=font)
        tw = bb[2] - bb[0]
        draw.text((cx - tw//2, y), line, font=font, fill=fill)
        y += lh

def wrap_text(text, font, max_w, draw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        bb = draw.textbbox((0,0), test, font=font)
        if bb[2]-bb[0] <= max_w:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def draw_action(draw, cx, cy, text, w=240, h=44, bg=C_ACTION_BG, bd=C_ACTION_BD, fnt=None):
    if fnt is None: fnt = F_BODY
    x0, y0 = cx - w//2, cy - h//2
    rounded_rect(draw, [x0,y0,x0+w,y0+h], r=10, fill=bg, outline=bd, width=2)
    lines = text.split("\n")
    lh = fnt.size + 3
    total = lh * len(lines)
    y = cy - total//2
    for line in lines:
        bb = draw.textbbox((0,0), line, font=fnt)
        tw = bb[2]-bb[0]
        draw.text((cx - tw//2, y), line, font=fnt, fill=(0,0,0))
        y += lh
    return (x0, y0, x0+w, y0+h)

def draw_decision(draw, cx, cy, text, w=130, h=65):
    pts = [(cx, cy-h//2), (cx+w//2, cy), (cx, cy+h//2), (cx-w//2, cy)]
    draw.polygon(pts, fill=C_DECISION, outline=C_DECISION_BD)
    lines = text.split("\n")
    lh = F_SMALL.size + 3
    total = lh * len(lines)
    y = cy - total//2
    for line in lines:
        bb = draw.textbbox((0,0), line, font=F_SMALL)
        tw = bb[2]-bb[0]
        draw.text((cx - tw//2, y), line, font=F_SMALL, fill=(0,0,0))
        y += lh
    return cy - h//2, cy + h//2   # top_y, bot_y

def draw_fork(draw, x0, y, x1, h=8):
    draw.rectangle([x0, y-h//2, x1, y+h//2], fill=C_FORK)

def draw_arrow(draw, x1, y1, x2, y2, label="", color=C_ARROW):
    draw.line([(x1,y1),(x2,y2)], fill=color, width=2)
    # arrowhead
    angle = math.atan2(y2-y1, x2-x1)
    size  = 10
    for da in [0.4, -0.4]:
        ax = x2 - size*math.cos(angle-da)
        ay = y2 - size*math.sin(angle-da)
        draw.line([(x2,y2),(int(ax),int(ay))], fill=color, width=2)
    if label:
        mx, my = (x1+x2)//2, (y1+y2)//2
        bb = draw.textbbox((0,0), label, font=F_SMALL)
        tw = bb[2]-bb[0]
        draw.text((mx - tw//2 + 6, my - 14), label, font=F_SMALL, fill=(80,80,80))

def draw_start(draw, cx, cy, r=14):
    draw.ellipse([cx-r,cy-r,cx+r,cy+r], fill=C_START)

def draw_end(draw, cx, cy, r=14):
    draw.ellipse([cx-r,cy-r,cx+r,cy+r], fill=C_END_OUTER)
    draw.ellipse([cx-r+4,cy-r+4,cx+r-4,cy+r-4], fill=(255,255,255))
    draw.ellipse([cx-r+8,cy-r+8,cx+r-8,cy+r-8], fill=C_END_INNER)

def draw_note(draw, x, y, text, w=200):
    lines = text.split("\n")
    lh = F_SMALL.size + 3
    h  = lh * len(lines) + 14
    fold = 14
    pts = [(x,y),(x+w-fold,y),(x+w,y+fold),(x+w,y+h),(x,y+h)]
    draw.polygon(pts, fill=C_NOTE_BG, outline=C_NOTE_BD)
    draw.line([(x+w-fold,y),(x+w-fold,y+fold),(x+w,y+fold)], fill=C_NOTE_BD, width=1)
    ty = y + 7
    for line in lines:
        draw.text((x+8, ty), line, font=F_SMALL, fill=(60,60,60))
        ty += lh

# ── Draw swimlane frame ───────────────────────────────────────────────────────
# Title bar
d.rectangle([MARGIN, MARGIN, MARGIN+SW_TOTAL, MARGIN+TITLE_H], fill=C_TITLE_BG)
title = "act  Alur Proses Inbound — OCR (Penerimaan Barang)"
bb = d.textbbox((0,0), title, font=F_TITLE)
tw = bb[2]-bb[0]
d.text((MARGIN + SW_TOTAL//2 - tw//2, MARGIN + TITLE_H//2 - F_TITLE.size//2),
       title, font=F_TITLE, fill=C_TITLE_FG)

# Swimlane backgrounds
d.rectangle([X1, SW_TOP, X1+SW_W1, SW_TOP+SW_H], fill=C_SW1_BG, outline=C_BORDER, width=2)
d.rectangle([X2, SW_TOP, X2+SW_W2, SW_TOP+SW_H], fill=C_SW2_BG, outline=C_BORDER, width=2)
d.rectangle([X3, SW_TOP, X3+SW_W3, SW_TOP+SW_H], fill=C_SW3_BG, outline=C_BORDER, width=2)

# Swimlane headers
d.rectangle([X1, SW_TOP, X1+SW_W1, SW_TOP+HDR_H], fill=C_SW1_HDR)
d.rectangle([X2, SW_TOP, X2+SW_W2, SW_TOP+HDR_H], fill=C_SW2_HDR)
d.rectangle([X3, SW_TOP, X3+SW_W3, SW_TOP+HDR_H], fill=C_SW3_HDR)

for x, w, label in [(X1,SW_W1,"Operator"), (X2,SW_W2,"Sistem (Laravel)"), (X3,SW_W3,"OCR Microservice (FastAPI)")]:
    bb = d.textbbox((0,0), label, font=F_HEADER)
    tw = bb[2]-bb[0]
    d.text((x + w//2 - tw//2, SW_TOP + HDR_H//2 - F_HEADER.size//2),
           label, font=F_HEADER, fill=(255,255,255))

# Outer border
d.rectangle([MARGIN, MARGIN, MARGIN+SW_TOTAL, SW_TOP+SW_H], outline=C_BORDER, width=3)

# ── Content positions ─────────────────────────────────────────────────────────
CX1 = X1 + SW_W1//2   # center Operator
CX2 = X2 + SW_W2//2   # center Sistem
CX3 = X3 + SW_W3//2   # center OCR

Y0 = SW_TOP + HDR_H + 40   # first element y

# ── 1. START ──────────────────────────────────────────────────────────────────
y = Y0
draw_start(d, CX1, y)
draw_arrow(d, CX1, y+14, CX1, y+40)

# ── 2. Operator: Unggah Foto Dokumen ─────────────────────────────────────────
y += 55
box1 = draw_action(d, CX1, y, "Unggah Foto\nDokumen", w=220, h=48,
                   bg=C_ACTION_BG, bd=C_ACTION_BD)
draw_arrow(d, CX1, y+24, CX1, y+60)

# ── 3. Sistem: InboundController → OcrService ────────────────────────────────
y += 80
# Arrow crosses swimlane: Operator → Sistem
draw_arrow(d, CX1, y-20, CX2, y-20)
box2 = draw_action(d, CX2, y, "InboundController\n→ OcrService.php", w=300, h=48,
                   bg=C_PROC_BG, bd=C_PROC_BD)
draw_arrow(d, CX2, y+24, CX2, y+55)

# ── 4. Sistem: Konversi ke base64 ────────────────────────────────────────────
y += 75
box3 = draw_action(d, CX2, y, "Konversi file\nke base64", w=260, h=44,
                   bg=C_PROC_BG, bd=C_PROC_BD)
draw_arrow(d, CX2, y+22, CX2, y+50)

# ── 5. Sistem: HTTP POST → FastAPI ───────────────────────────────────────────
y += 68
box4 = draw_action(d, CX2, y, "HTTP POST → FastAPI\n(port 8001) /ocr", w=300, h=48,
                   bg=C_PROC_BG, bd=C_PROC_BD)

# Arrow crosses to OCR lane
draw_arrow(d, CX2 + 150, y, CX3 - 200, y)

# ── 6. OCR: Deteksi tipe dokumen ─────────────────────────────────────────────
y += 70
box5 = draw_action(d, CX3, y, "Deteksi Tipe Dokumen\n(SIR20 / RSS1 / DO / SK)", w=380, h=48,
                   bg=C_OCR_BG, bd=C_OCR_BD)
draw_arrow(d, CX3, y+24, CX3, y+55)

# ── 7. OCR: Pipeline Preprocessing ──────────────────────────────────────────
y += 75
box6 = draw_action(d, CX3, y,
    "Pipeline Preprocessing:\nEXIF Rotate → Auto-Crop → Deskew\n→ CLAHE → Resize",
    w=500, h=60, bg=C_OCR_BG, bd=C_OCR_BD)
draw_arrow(d, CX3, y+30, CX3, y+62)

# ── 8. FORK: Fire parallel requests ──────────────────────────────────────────
y += 90
fork_x0 = CX3 - 220
fork_x1 = CX3 + 220
draw_fork(d, fork_x0, y, fork_x1)
draw_arrow(d, CX3, y-30, CX3, y-4)

# Label fork
d.text((fork_x0 - 5, y - 22), "«fork»", font=F_SMALL, fill=(80,80,80))

# Two parallel branches
CX3L = CX3 - 180   # Groq branch
CX3R = CX3 + 180   # OpenRouter branch

draw_arrow(d, CX3L, y+4, CX3L, y+40)
draw_arrow(d, CX3R, y+4, CX3R, y+40)

y_fork = y

# ── 9a. Groq request ─────────────────────────────────────────────────────────
y_par = y + 60
box7a = draw_action(d, CX3L, y_par, "Request ke\nGroq API", w=200, h=44,
                    bg=C_OCR_BG, bd=C_OCR_BD)

# ── 9b. OpenRouter request ───────────────────────────────────────────────────
box7b = draw_action(d, CX3R, y_par, "Request ke\nOpenRouter API", w=200, h=44,
                    bg=C_OCR_BG, bd=C_OCR_BD)

draw_arrow(d, CX3L, y_par+22, CX3L, y_par+55)
draw_arrow(d, CX3R, y_par+22, CX3R, y_par+55)

# ── 10. JOIN: Terima respons pertama ─────────────────────────────────────────
y_join = y_par + 75
draw_fork(d, fork_x0, y_join, fork_x1)
draw_arrow(d, CX3L, y_join-4, CX3L, y_join)
draw_arrow(d, CX3R, y_join-4, CX3R, y_join)
d.text((fork_x0 - 5, y_join + 6), "«join» — Racing Strategy: ambil respons pertama yang valid", font=F_SMALL, fill=(80,80,80))
draw_arrow(d, CX3, y_join+4, CX3, y_join+40)

# ── 11. OCR: Post-processing ─────────────────────────────────────────────────
y = y_join + 60
box8 = draw_action(d, CX3, y,
    "Post-processing:\nFix ditto marks · Cross-validate bale count\nFix year · Validasi JSON",
    w=520, h=60, bg=C_OCR_BG, bd=C_OCR_BD)
draw_arrow(d, CX3, y+30, CX3, y+62)

# ── 12. Decision: JSON valid? ────────────────────────────────────────────────
y += 82
top_d, bot_d = draw_decision(d, CX3, y, "JSON\nvalid?", w=120, h=60)
draw_arrow(d, CX3, bot_d, CX3, bot_d+35, label="Ya")

# No branch → retry note
draw_arrow(d, CX3 + 60, y, CX3 + 260, y, label="Tidak")
draw_note(d, CX3 + 265, y - 30,
          "Fallback:\nCoba model\nberikutnya\natau error", w=160)

# ── 13. OCR → Sistem: Kembalikan JSON ────────────────────────────────────────
y = bot_d + 55
box9 = draw_action(d, CX3, y, "Kembalikan JSON\nhasil ekstraksi ke Laravel", w=380, h=48,
                   bg=C_OCR_BG, bd=C_OCR_BD)

# Arrow back to Sistem lane
draw_arrow(d, CX3 - 190, y, CX2 + 150, y)

# ── 14. Sistem: Pre-filled Form + Preview ────────────────────────────────────
y += 70
box10 = draw_action(d, CX2, y, "Tampilkan Pre-filled Form\n+ Preview Gambar Dokumen", w=320, h=48,
                    bg=C_PROC_BG, bd=C_PROC_BD)

# Arrow to Operator
draw_arrow(d, CX2 - 150, y, CX1 + 110, y)

# ── 15. Operator: Review & Koreksi ───────────────────────────────────────────
y += 70
box11 = draw_action(d, CX1, y, "Review & Koreksi\n(Human-in-the-Loop)", w=240, h=48,
                    bg=C_ACTION_BG, bd=C_ACTION_BD)
draw_arrow(d, CX1, y+24, CX1, y+55)

# ── 16. Decision: Data benar? ────────────────────────────────────────────────
y += 75
top_d2, bot_d2 = draw_decision(d, CX1, y, "Data\nbenar?", w=120, h=60)
draw_arrow(d, CX1, bot_d2, CX1, bot_d2+35, label="Ya")

# No → back to review
draw_arrow(d, CX1 - 60, y, CX1 - 130, y, label="Tidak")
draw_arrow(d, CX1 - 130, y, CX1 - 130, y - 75)
draw_arrow(d, CX1 - 130, y - 75, CX1 - 120, y - 75)

# ── 17. Operator: Submit ─────────────────────────────────────────────────────
y = bot_d2 + 55
box12 = draw_action(d, CX1, y, "Submit Form", w=200, h=44,
                    bg=C_ACTION_BG, bd=C_ACTION_BD)

# Arrow to Sistem
draw_arrow(d, CX1 + 100, y, CX2 - 150, y)

# ── 18. Sistem: Simpan ke DB + Update Stok ───────────────────────────────────
y += 70
box13 = draw_action(d, CX2, y, "Simpan Data ke Database\n+ Update Stok Barang", w=320, h=48,
                    bg=C_PROC_BG, bd=C_PROC_BD)
draw_arrow(d, CX2, y+24, CX2, y+55)

# ── 19. Sistem: Tampilkan konfirmasi ─────────────────────────────────────────
y += 75
box14 = draw_action(d, CX2, y, "Tampilkan Konfirmasi\nBerhasil", w=280, h=44,
                    bg=C_PROC_BG, bd=C_PROC_BD)

# Arrow to Operator
draw_arrow(d, CX2 - 140, y, CX1 + 110, y)

# ── 20. END ───────────────────────────────────────────────────────────────────
y += 65
draw_arrow(d, CX1, y - 22, CX1, y)
draw_end(d, CX1, y + 14)

# ── Vertical connector lines (dashed guide) ───────────────────────────────────
# Draw vertical dashed lines inside each swimlane as flow guides
for cx in [CX1, CX2, CX3]:
    for yy in range(SW_TOP + HDR_H + 10, SW_TOP + SW_H - 10, 12):
        d.line([(cx, yy), (cx, yy+6)], fill=(200,200,200), width=1)

# ── Save ──────────────────────────────────────────────────────────────────────
out = "docs/diagrams/drawio/Activity_Inbound_OCR.png"
img.save(out, "PNG", dpi=(150,150))
print(f"Saved: {out}  ({W}x{H}px)")
