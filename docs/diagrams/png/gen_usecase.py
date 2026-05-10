"""
Use Case Diagram — SimAset RBTV Bengkulu
Gaya persis foto contoh:
- Background putih, border tipis
- Elips kuning muda untuk use case
- Stick figure untuk aktor
- Aktor di kiri (Admin) dan kanan (Staff)
- Garis langsung aktor → use case utama
- CRUD di-extend dari use case utama masing-masing
- Semua use case utama <<include>> ke Login
- Panah putus-putus untuk include/extend dengan label
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = "docs/diagrams/png"
os.makedirs(OUT, exist_ok=True)

def F(size, bold=False):
    for p in (["C:/Windows/Fonts/arialbd.ttf"] if bold
              else ["C:/Windows/Fonts/arial.ttf","C:/Windows/Fonts/calibri.ttf"]):
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

FB = F(11)
FS = F(10)
FH = F(11, True)
FT = F(11, True)

# ── COLORS ────────────────────────────────────────────────────────────────────
BG      = (255,255,255)
UC_F    = (255,255,204)   # use case fill
UC_BD   = (0,0,0)
BD_F    = (255,255,240)   # system boundary fill
BD_BD   = (0,0,0)
BLACK   = (0,0,0)
GRAY    = (100,100,100)
LGRAY   = (180,180,180)

# ── CANVAS ────────────────────────────────────────────────────────────────────
W, H = 1400, 980
img = Image.new("RGB", (W,H), BG)
d   = ImageDraw.Draw(img)

# ── HELPERS ───────────────────────────────────────────────────────────────────
def tc(cx, cy, txt, font=FB, color=BLACK):
    lines = txt.split("\n")
    lh = font.size + 2
    y = cy - lh*len(lines)//2
    for ln in lines:
        bb = font.getbbox(ln); tw = bb[2]-bb[0]
        d.text((cx-tw//2, y), ln, font=font, fill=color)
        y += lh

def ellipse(cx, cy, txt, font=FB, rx=None, ry=None):
    """Draw use case ellipse, auto-size from text."""
    lines = txt.split("\n")
    lh = font.size + 2
    tw = max(font.getbbox(ln)[2]-font.getbbox(ln)[0] for ln in lines)
    th = lh * len(lines)
    if rx is None: rx = tw//2 + 18
    if ry is None: ry = th//2 + 12
    d.ellipse([cx-rx, cy-ry, cx+rx, cy+ry], fill=UC_F, outline=UC_BD, width=1)
    tc(cx, cy, txt, font)
    return rx, ry

def actor(cx, cy, lbl):
    """Draw stick figure actor."""
    r = 11
    # head
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=BG, outline=BLACK, width=1)
    # body
    d.line([(cx, cy+r), (cx, cy+r+28)], fill=BLACK, width=1)
    # arms
    d.line([(cx-20, cy+r+10), (cx+20, cy+r+10)], fill=BLACK, width=1)
    # legs
    d.line([(cx, cy+r+28), (cx-16, cy+r+48)], fill=BLACK, width=1)
    d.line([(cx, cy+r+28), (cx+16, cy+r+48)], fill=BLACK, width=1)
    # label
    bb = FB.getbbox(lbl); tw = bb[2]-bb[0]
    d.text((cx-tw//2, cy+r+52), lbl, font=FB, fill=BLACK)

def line_to(x1,y1,x2,y2, dashed=False, color=BLACK):
    if not dashed:
        d.line([(x1,y1),(x2,y2)], fill=color, width=1)
    else:
        dx,dy = x2-x1, y2-y1
        L = max(1,math.hypot(dx,dy)); n = int(L/7)
        for i in range(n):
            if i%2==0:
                t1,t2 = i/n, min(1,(i+.5)/n)
                d.line([(int(x1+dx*t1),int(y1+dy*t1)),
                        (int(x1+dx*t2),int(y1+dy*t2))], fill=color, width=1)

def arrowhead(x2,y2, x1,y1, size=7):
    ang = math.atan2(y2-y1, x2-x1)
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-size*math.cos(ang-da)),
                          int(y2-size*math.sin(ang-da)))], fill=BLACK, width=1)

def connect(x1,y1,x2,y2, lbl="", dashed=False, arrow=True):
    """Draw line/arrow between two points, with optional label."""
    line_to(x1,y1,x2,y2,dashed)
    if arrow:
        arrowhead(x2,y2,x1,y1)
    if lbl:
        mx,my = (x1+x2)//2, (y1+y2)//2
        bb = FS.getbbox(lbl); tw = bb[2]-bb[0]
        # offset label perpendicular to line
        ang = math.atan2(y2-y1,x2-x1)
        ox = int(-math.sin(ang)*12); oy = int(math.cos(ang)*12)
        d.text((mx-tw//2+ox, my-FS.size//2+oy), lbl, font=FS, fill=GRAY)

def edge_point(cx, cy, rx, ry, tx, ty):
    """Point on ellipse edge toward (tx,ty)."""
    dx,dy = tx-cx, ty-cy
    L = max(1,math.hypot(dx,dy))
    # parametric ellipse: find t where (rx*cos t, ry*sin t) is in direction (dx,dy)
    # approximate: scale
    scale = min(rx/max(1,abs(dx)), ry/max(1,abs(dy))) if dx!=0 or dy!=0 else 1
    ex = cx + dx/L * rx * abs(dx/L*rx + dy/L*ry) / max(1,abs(dx/L*rx + dy/L*ry)) * (rx)
    ey = cy + dy/L * ry * abs(dx/L*rx + dy/L*ry) / max(1,abs(dx/L*rx + dy/L*ry)) * (ry)
    # simpler: just use direction scaled to ellipse
    if L == 0: return cx, cy
    # solve: (x/rx)^2 + (y/ry)^2 = 1, x=t*dx/L, y=t*dy/L
    # t^2 * ((dx/L/rx)^2 + (dy/L/ry)^2) = 1
    denom = math.sqrt((dx/L/rx)**2 + (dy/L/ry)**2)
    if denom == 0: return cx, cy
    t = 1/denom
    return int(cx + dx/L*t), int(cy + dy/L*t)

def uc_connect(cx1,cy1,rx1,ry1, cx2,cy2,rx2,ry2, lbl="", dashed=False, arrow=True):
    """Connect two ellipses edge-to-edge."""
    ex1,ey1 = edge_point(cx1,cy1,rx1,ry1,cx2,cy2)
    ex2,ey2 = edge_point(cx2,cy2,rx2,ry2,cx1,cy1)
    connect(ex1,ey1,ex2,ey2,lbl,dashed,arrow)

def actor_to_uc(ax,ay, cx,cy,rx,ry):
    """Line from actor center to ellipse edge."""
    ex,ey = edge_point(cx,cy,rx,ry,ax,ay)
    connect(ax,ay,ex,ey,dashed=False,arrow=False)

# ── OUTER FRAME ───────────────────────────────────────────────────────────────
d.rectangle([8,8,W-8,H-8], outline=BLACK, width=1)
d.text((12,11), "uc  Use Case Diagram — SimAset RBTV Bengkulu", font=FT, fill=BLACK)

# ── SYSTEM BOUNDARY ───────────────────────────────────────────────────────────
BX0,BY0,BX1,BY1 = 115, 36, W-115, H-28
d.rectangle([BX0,BY0,BX1,BY1], fill=BD_F, outline=BD_BD, width=1)

# ── ACTORS ────────────────────────────────────────────────────────────────────
ACT_ADMIN_X, ACT_ADMIN_Y = 55,  460
ACT_STAFF_X, ACT_STAFF_Y = W-55, 460
actor(ACT_ADMIN_X, ACT_ADMIN_Y, "Admin")
actor(ACT_STAFF_X, ACT_STAFF_Y, "Staff")

# ── USE CASES — positions (cx, cy) ───────────────────────────────────────────
# Login (center)
LOGIN_X, LOGIN_Y = 700, 470

# Main use cases (aktor langsung terhubung)
UCS = {
    # (cx, cy, label, rx, ry)
    "login":          (700, 470,   "Login",                    55, 26),

    # Admin + Staff — baris atas (main use cases)
    "aset":           (240,  230,  "Manajemen\nAset",                  62, 30),
    "barang":         (430,  230,  "Manajemen\nBarang",                62, 30),
    "ruangan":        (620,  230,  "Manajemen\nRuangan",               62, 30),
    "qr":             (810,  230,  "QR Code",                          52, 26),
    "maintenance":    (1000, 230,  "Maintenance",                      62, 26),
    "import":         (240,  700,  "Import Data",                      58, 26),
    "export":         (430,  700,  "Export &\nLaporan",                58, 30),
    "dashboard":      (620,  700,  "Dashboard",                        52, 26),

    # Admin only — baris bawah kanan
    "pengguna":       (810,  700,  "Kelola\nPengguna",                 58, 30),
    "auditlog":       (1000, 700,  "Audit Log",                        52, 26),

    # CRUD extends for Aset — baris paling atas
    "aset_tambah":    (140,  110,  "Tambah Aset",                      56, 22),
    "aset_edit":      (250,  68,   "Edit Aset",                        48, 22),
    "aset_hapus":     (360,  68,   "Hapus Aset",                       48, 22),
    "aset_detail":    (460,  110,  "Lihat Detail\nAset",               56, 26),

    # CRUD extends for Barang
    "brg_tambah":     (340,  110,  "Tambah\nBarang",                   52, 26),
    "brg_edit":       (450,  68,   "Edit Barang",                      50, 22),
    "brg_hapus":      (560,  68,   "Hapus Barang",                     52, 22),

    # CRUD extends for Ruangan
    "rng_tambah":     (530,  110,  "Tambah\nRuangan",                  54, 26),
    "rng_edit":       (640,  68,   "Edit Ruangan",                     52, 22),
    "rng_hapus":      (750,  68,   "Hapus Ruangan",                    54, 22),

    # QR extends
    "qr_gen":         (720,  110,  "Generate QR",                      54, 22),
    "qr_scan":        (840,  110,  "Scan QR",                          46, 22),
    "qr_print":       (950,  110,  "Cetak QR\nMassal",                 52, 26),

    # Maintenance extends
    "maint_set":      (910,  150,  "Set\nMaintenance",                 52, 26),
    "maint_done":     (1060, 150,  "Selesaikan\nMaintenance",          62, 26),

    # Import extends — baris bawah
    "imp_aset":       (150,  820,  "Import Aset",                      54, 22),
    "imp_barang":     (270,  860,  "Import Barang",                    56, 22),
    "imp_tmpl":       (390,  820,  "Download\nTemplate",               54, 26),

    # Export extends
    "exp_excel":      (330,  820,  "Export Excel",                     54, 22),
    "exp_pdf":        (450,  860,  "Export PDF",                       50, 22),
    "lap_ruangan":    (570,  820,  "Laporan Per\nRuangan",             60, 26),
    "lap_maint":      (700,  860,  "Laporan\nMaintenance",             58, 26),

    # Pengguna extends
    "usr_tambah":     (720,  820,  "Tambah\nPengguna",                 54, 26),
    "usr_edit":       (850,  820,  "Edit Pengguna",                    56, 22),
    "usr_hapus":      (980,  820,  "Hapus Pengguna",                   58, 22),

    # Audit extends
    "audit_filter":   (1080, 820,  "Filter\nAudit Log",                52, 26),
}

# ── DRAW ALL ELLIPSES ─────────────────────────────────────────────────────────
drawn = {}
for key,(cx,cy,lbl,rx,ry) in UCS.items():
    ellipse(cx,cy,lbl,FB,rx,ry)
    drawn[key] = (cx,cy,rx,ry)

# ── ACTOR → MAIN USE CASES (direct lines, no arrow) ──────────────────────────
# Admin → all
admin_targets = ["aset","barang","ruangan","qr","maintenance",
                 "import","export","dashboard","pengguna","auditlog","login"]
for k in admin_targets:
    cx,cy,rx,ry = drawn[k]
    actor_to_uc(ACT_ADMIN_X, ACT_ADMIN_Y, cx,cy,rx,ry)

# Staff → subset (no pengguna, no auditlog)
staff_targets = ["aset","barang","ruangan","qr","maintenance",
                 "import","export","dashboard","login"]
for k in staff_targets:
    cx,cy,rx,ry = drawn[k]
    actor_to_uc(ACT_STAFF_X, ACT_STAFF_Y, cx,cy,rx,ry)

# ── INCLUDE: main use cases → Login ──────────────────────────────────────────
include_targets = ["aset","barang","ruangan","qr","maintenance",
                   "import","export","dashboard","pengguna","auditlog"]
lx,ly,lrx,lry = drawn["login"]
for k in include_targets:
    cx,cy,rx,ry = drawn[k]
    uc_connect(cx,cy,rx,ry, lx,ly,lrx,lry, "<<include>>", dashed=True, arrow=True)

# ── EXTEND: CRUD → parent use case ───────────────────────────────────────────
extends = [
    # (child_key, parent_key)
    ("aset_tambah",  "aset"),
    ("aset_edit",    "aset"),
    ("aset_hapus",   "aset"),
    ("aset_detail",  "aset"),

    ("brg_tambah",   "barang"),
    ("brg_edit",     "barang"),
    ("brg_hapus",    "barang"),

    ("rng_tambah",   "ruangan"),
    ("rng_edit",     "ruangan"),
    ("rng_hapus",    "ruangan"),

    ("qr_gen",       "qr"),
    ("qr_scan",      "qr"),
    ("qr_print",     "qr"),

    ("maint_set",    "maintenance"),
    ("maint_done",   "maintenance"),

    ("imp_aset",     "import"),
    ("imp_barang",   "import"),
    ("imp_tmpl",     "import"),

    ("exp_excel",    "export"),
    ("exp_pdf",      "export"),
    ("lap_ruangan",  "export"),
    ("lap_maint",    "export"),

    ("usr_tambah",   "pengguna"),
    ("usr_edit",     "pengguna"),
    ("usr_hapus",    "pengguna"),

    ("audit_filter", "auditlog"),
]

for child_k, parent_k in extends:
    cx,cy,rx,ry = drawn[child_k]
    px,py,prx,pry = drawn[parent_k]
    uc_connect(cx,cy,rx,ry, px,py,prx,pry, "<<extend>>", dashed=True, arrow=True)

# ── SAVE ──────────────────────────────────────────────────────────────────────
path = f"{OUT}/UC_SimAset.png"
img.save(path, "PNG", dpi=(150,150))
print(f"Saved: {path}  ({W}x{H}px)")
