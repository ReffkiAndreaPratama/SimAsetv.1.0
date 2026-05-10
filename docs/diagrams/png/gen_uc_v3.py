"""
Use Case Diagram v3 — bersih, tidak seperti jaring laba-laba.

Aturan:
1. Aktor hanya terhubung ke use case UTAMA (bukan ke extend)
2. Extend items hanya terhubung ke parent-nya saja
3. Include hanya dari use case utama ke Login
4. Layout: use case utama dalam 1 kolom vertikal di tengah
5. Extend items di kiri/kanan use case utama masing-masing
6. Tidak ada garis yang melintasi area lain
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = "docs/diagrams/png"
os.makedirs(OUT, exist_ok=True)

def F(sz, bold=False):
    for p in (["C:/Windows/Fonts/arialbd.ttf"] if bold
              else ["C:/Windows/Fonts/arial.ttf","C:/Windows/Fonts/calibri.ttf"]):
        if os.path.exists(p):
            try: return ImageFont.truetype(p, sz)
            except: pass
    return ImageFont.load_default()

FB=F(11); FS=F(10); FH=F(11,True); FT=F(11,True); FSM=F(9)

BG    = (255,255,255)
BOXF  = (255,255,204)
BLACK = (0,0,0)
GRAY  = (110,110,110)

def msz(txt, font):
    lines=txt.split("\n"); lh=font.size+2
    w=max(font.getbbox(ln)[2]-font.getbbox(ln)[0] for ln in lines)
    return w, lh*len(lines)

def tc(d, cx, cy, txt, font, color=BLACK):
    lines=txt.split("\n"); lh=font.size+2
    y=cy-lh*len(lines)//2
    for ln in lines:
        bb=font.getbbox(ln); tw=bb[2]-bb[0]
        d.text((cx-tw//2,y),ln,font=font,fill=color); y+=lh

def ell_r(txt, font, px=16, py=10):
    tw,th=msz(txt,font)
    return tw//2+px, th//2+py

def draw_ell(d, cx, cy, txt, font=FB):
    rx,ry=ell_r(txt,font)
    d.ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=BOXF,outline=BLACK,width=1)
    tc(d,cx,cy,txt,font)
    return rx,ry

def ep(cx,cy,rx,ry,tx,ty):
    dx,dy=tx-cx,ty-cy; L=max(1,math.hypot(dx,dy))
    denom=math.sqrt((dx/L/rx)**2+(dy/L/ry)**2)
    if denom==0: return cx,cy
    return int(cx+dx/L/denom), int(cy+dy/L/denom)

def dline(d,x1,y1,x2,y2):
    dx,dy=x2-x1,y2-y1; L=max(1,math.hypot(dx,dy)); n=int(L/7)
    for i in range(n):
        if i%2==0:
            t1,t2=i/n,min(1,(i+.5)/n)
            d.line([(int(x1+dx*t1),int(y1+dy*t1)),
                    (int(x1+dx*t2),int(y1+dy*t2))],fill=BLACK,width=1)

def ahdraw(d,x2,y2,x1,y1,s=7):
    ang=math.atan2(y2-y1,x2-x1)
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                          int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)

def conn_ell(d,c1,r1,c2,r2,lbl="",dashed=True):
    x1,y1=ep(*c1,*r1,*c2[:2])
    x2,y2=ep(*c2,*r2,*c1[:2])
    if dashed: dline(d,x1,y1,x2,y2)
    else:      d.line([(x1,y1),(x2,y2)],fill=BLACK,width=1)
    ahdraw(d,x2,y2,x1,y1)
    if lbl:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=FSM.getbbox(lbl); tw=bb[2]-bb[0]
        ang=math.atan2(y2-y1,x2-x1)
        ox=int(-math.sin(ang)*11); oy=int(math.cos(ang)*11)
        d.text((mx-tw//2+ox,my-FSM.size//2+oy),lbl,font=FSM,fill=GRAY)

def actor(d,cx,cy,lbl):
    r=11
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BG,outline=BLACK,width=1)
    d.line([(cx,cy+r),(cx,cy+r+26)],fill=BLACK,width=1)
    d.line([(cx-18,cy+r+10),(cx+18,cy+r+10)],fill=BLACK,width=1)
    d.line([(cx,cy+r+26),(cx-14,cy+r+44)],fill=BLACK,width=1)
    d.line([(cx,cy+r+26),(cx+14,cy+r+44)],fill=BLACK,width=1)
    bb=FB.getbbox(lbl); tw=bb[2]-bb[0]
    d.text((cx-tw//2,cy+r+48),lbl,font=FB,fill=BLACK)

def actor_line(d,ax,ay,cx,cy,rx,ry):
    ex,ey=ep(cx,cy,rx,ry,ax,ay)
    d.line([(ax,ay),(ex,ey)],fill=BLACK,width=1)

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
# Use case utama — disusun dalam 1 kolom vertikal
# Format: (key, label, actor_access)
# actor_access: "both"=Admin+Staff, "admin"=Admin only
MAIN_UCS = [
    ("aset",        "Manajemen Aset",       "both"),
    ("barang",      "Manajemen Barang",      "both"),
    ("ruangan",     "Manajemen Ruangan",     "both"),
    ("qr",          "QR Code",               "both"),
    ("maintenance", "Maintenance",           "both"),
    ("import",      "Import Data",           "both"),
    ("export",      "Export & Laporan",      "both"),
    ("dashboard",   "Dashboard",             "both"),
    ("pengguna",    "Kelola Pengguna",       "admin"),
    ("auditlog",    "Audit Log",             "admin"),
    ("login",       "Login",                 "both"),
]

# Extend items per use case
# Format: (parent_key, [labels], side)
# side: "left" atau "right"
EXTENDS = [
    ("aset",        ["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"],         "left"),
    ("barang",      ["Tambah Barang","Edit Barang","Hapus Barang"],                  "left"),
    ("ruangan",     ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"],               "left"),
    ("qr",          ["Generate QR","Scan QR","Cetak Massal"],                        "left"),
    ("maintenance", ["Set Maintenance","Selesaikan\nMaintenance"],                   "left"),
    ("import",      ["Import Aset","Import Barang","Download Template"],             "right"),
    ("export",      ["Export Excel","Export PDF","Laporan Ruangan","Laporan\nMaintenance"], "right"),
    ("pengguna",    ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"],            "right"),
    ("auditlog",    ["Filter Audit Log"],                                             "right"),
]

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT CALCULATION
# ─────────────────────────────────────────────────────────────────────────────
# Compute ellipse sizes
uc_sz  = {k: ell_r(lbl,FB) for k,lbl,_ in MAIN_UCS}
ext_sz = {}
for pk,items,side in EXTENDS:
    for lbl in items:
        ext_sz[lbl] = ell_r(lbl,FS,px=14,py=9)

# Row heights — each main UC gets its own row
# Row height = max(uc_ry, max extend_ry for that UC) * 2 + gap
ROW_GAP = 28

# Separate login from the rest
main_no_login = [(k,l,a) for k,l,a in MAIN_UCS if k!="login"]
# Login will be placed at the bottom center

# Compute row heights
row_heights = []
for k,lbl,_ in main_no_login:
    uc_ry = uc_sz[k][1]
    # find extends for this UC
    ext_items = next((items for pk,items,_ in EXTENDS if pk==k), [])
    max_ext_ry = max((ext_sz[it][1] for it in ext_items), default=0)
    rh = max(uc_ry, max_ext_ry)*2 + ROW_GAP
    row_heights.append(rh)

# Column x positions
# [actor_admin] [ext_left] [main_uc] [ext_right] [actor_staff]
# Compute max widths
max_uc_rx  = max(rx for rx,ry in uc_sz.values())
max_ext_rx_left  = max((ext_sz[it][0] for pk,items,side in EXTENDS
                         for it in items if side=="left"), default=60)
max_ext_rx_right = max((ext_sz[it][0] for pk,items,side in EXTENDS
                         for it in items if side=="right"), default=60)

PAD       = 20
ACTOR_GAP = 35
EXT_GAP   = 30
UC_GAP    = 0   # main UC column is single

x_admin      = PAD + 30
x_ext_left   = x_admin + 30 + ACTOR_GAP + max_ext_rx_left
x_main       = x_ext_left + max_ext_rx_left + EXT_GAP + max_uc_rx
x_ext_right  = x_main + max_uc_rx + EXT_GAP + max_ext_rx_right
x_staff      = x_ext_right + max_ext_rx_right + ACTOR_GAP + 30

W = x_staff + 50

# Compute y for each row
TITLE_H = 22; BOUND_PAD = 18; TOP_PAD = 60
y_rows = []
y = TOP_PAD
for rh in row_heights:
    y_rows.append(y + rh//2)
    y += rh

# Login at bottom center
LOGIN_GAP = 40
y_login = y + LOGIN_GAP + uc_sz["login"][1]
y += LOGIN_GAP + uc_sz["login"][1]*2

H_content = y + 40
H = TITLE_H + BOUND_PAD*2 + H_content + 20

# ─────────────────────────────────────────────────────────────────────────────
# DRAW
# ─────────────────────────────────────────────────────────────────────────────
img = Image.new("RGB",(W,H),BG)
d   = ImageDraw.Draw(img)

Y_OFF = TITLE_H + BOUND_PAD + 10  # global y offset

def gy(y): return y + Y_OFF

# outer border
d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
# title tag
tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([8,8,8+tw+10,8+TITLE_H],fill=BG,outline=BLACK,width=1)
d.text((12,10),tag,font=FT,fill=BLACK)

# system boundary
bx0=x_ext_left-max_ext_rx_left-8
bx1=x_ext_right+max_ext_rx_right+8
by0=8+TITLE_H+4
by1=H-12
d.rectangle([bx0,by0,bx1,by1],fill=(255,255,252),outline=BLACK,width=1)

# ── Draw main use cases ───────────────────────────────────────────────────────
uc_drawn = {}  # key → (cx,cy,rx,ry)
for i,(k,lbl,_) in enumerate(main_no_login):
    cx=x_main; cy=gy(y_rows[i])
    rx,ry=draw_ell(d,cx,cy,lbl,FB)
    uc_drawn[k]=(cx,cy,rx,ry)

# Login
lx=x_main; ly=gy(y_login)
lrx,lry=draw_ell(d,lx,ly,"Login",FB)
uc_drawn["login"]=(lx,ly,lrx,lry)

# ── Draw extend ellipses & arrows ─────────────────────────────────────────────
ext_drawn = {}
for pk,items,side in EXTENDS:
    if pk not in uc_drawn: continue
    pcx,pcy,prx,pry = uc_drawn[pk]
    n=len(items)
    max_ery=max(ext_sz[it][1] for it in items)
    spacing=max_ery*2+18
    total=(n-1)*spacing
    start_y=pcy-total//2

    ex = x_ext_left if side=="left" else x_ext_right

    for i,lbl in enumerate(items):
        ey=start_y+i*spacing
        rx,ry=ext_sz[lbl]
        draw_ell(d,ex,ey,lbl,FS)
        ext_drawn[lbl]=(ex,ey,rx,ry)
        # extend arrow: child → parent
        conn_ell(d,(ex,ey),(rx,ry),(pcx,pcy),(prx,pry),"<<extend>>",dashed=True)

# ── Include arrows: main UCs → Login ─────────────────────────────────────────
for k,lbl,_ in main_no_login:
    uc=uc_drawn[k]
    conn_ell(d,(uc[0],uc[1]),(uc[2],uc[3]),
               (lx,ly),(lrx,lry),"<<include>>",dashed=True)

# ── Actors ────────────────────────────────────────────────────────────────────
mid_y = gy(y_rows[len(y_rows)//2])
actor(d,x_admin,mid_y-20,"Admin")
actor(d,x_staff,mid_y-20,"Staff")

# Actor → main UCs only (not extends)
# Batasi: aktor hanya terhubung ke use case yang LANGSUNG relevan
# (bukan semua — itu yang bikin jaring laba-laba)
# Admin → semua, Staff → semua kecuali admin-only
# Tapi gambar garis hanya ke use case yang ada di "baris" terdekat aktor
# Solusi: aktor terhubung ke use case via 1 garis ke Login saja,
# sisanya via include/extend (seperti foto contoh)
# Aktor hanya langsung ke: Login + use case utama (tanpa extend)
for k,lbl,access in MAIN_UCS:
    uc=uc_drawn[k]
    actor_line(d,x_admin,mid_y-20,uc[0],uc[1],uc[2],uc[3])
    if access=="both":
        actor_line(d,x_staff,mid_y-20,uc[0],uc[1],uc[2],uc[3])

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
