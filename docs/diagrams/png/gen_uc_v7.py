"""
Use Case Diagram v7 — layout semantik:
- Login di tengah
- Admin di kiri, fitur admin-only di kiri atas/bawah
- Staff di kanan, fitur operasional di kanan
- Fitur bersama di tengah sekitar Login
- Tidak ada kotak area, tidak ada tumpang tindih
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = "docs/diagrams/png"
os.makedirs(OUT, exist_ok=True)

def F(sz,bold=False):
    for p in (["C:/Windows/Fonts/arialbd.ttf"] if bold
              else ["C:/Windows/Fonts/arial.ttf","C:/Windows/Fonts/calibri.ttf"]):
        if os.path.exists(p):
            try: return ImageFont.truetype(p,sz)
            except: pass
    return ImageFont.load_default()

FB=F(11); FS=F(10); FT=F(11,True); FSM=F(9)
BG=(255,255,255); BOXF=(255,255,204); BLACK=(0,0,0); GRAY=(110,110,110)

def msz(txt,f):
    lines=txt.split("\n"); lh=f.size+2
    w=max(f.getbbox(ln)[2]-f.getbbox(ln)[0] for ln in lines)
    return w,lh*len(lines)

def tc(d,cx,cy,txt,f,color=BLACK):
    lines=txt.split("\n"); lh=f.size+2; y=cy-lh*len(lines)//2
    for ln in lines:
        bb=f.getbbox(ln); tw=bb[2]-bb[0]
        d.text((cx-tw//2,y),ln,font=f,fill=color); y+=lh

def ell_r(txt,f,px=14,py=9):
    tw,th=msz(txt,f); return tw//2+px,th//2+py

def draw_ell(d,cx,cy,txt,f=FB):
    rx,ry=ell_r(txt,f)
    d.ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=BOXF,outline=BLACK,width=1)
    tc(d,cx,cy,txt,f); return rx,ry

def ep(cx,cy,rx,ry,tx,ty):
    dx,dy=tx-cx,ty-cy; L=max(1,math.hypot(dx,dy))
    denom=math.sqrt((dx/L/rx)**2+(dy/L/ry)**2)
    if denom==0: return cx,cy
    return int(cx+dx/L/denom),int(cy+dy/L/denom)

def dline(d,x1,y1,x2,y2):
    dx,dy=x2-x1,y2-y1; L=max(1,math.hypot(dx,dy)); n=int(L/7)
    for i in range(n):
        if i%2==0:
            t1,t2=i/n,min(1,(i+.5)/n)
            d.line([(int(x1+dx*t1),int(y1+dy*t1)),
                    (int(x1+dx*t2),int(y1+dy*t2))],fill=BLACK,width=1)

def ah(d,x2,y2,x1,y1,s=6):
    ang=math.atan2(y2-y1,x2-x1)
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                          int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)

def conn(d,c1,r1,c2,r2,lbl="",dash=True):
    x1,y1=ep(*c1,*r1,*c2[:2]); x2,y2=ep(*c2,*r2,*c1[:2])
    if dash: dline(d,x1,y1,x2,y2)
    else:    d.line([(x1,y1),(x2,y2)],fill=BLACK,width=1)
    ah(d,x2,y2,x1,y1)
    if lbl:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=FSM.getbbox(lbl); tw=bb[2]-bb[0]
        ang=math.atan2(y2-y1,x2-x1)
        ox=int(-math.sin(ang)*10); oy=int(math.cos(ang)*10)
        d.text((mx-tw//2+ox,my-FSM.size//2+oy),lbl,font=FSM,fill=GRAY)

def actor(d,cx,cy,lbl):
    r=12
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BG,outline=BLACK,width=1)
    d.line([(cx,cy+r),(cx,cy+r+28)],fill=BLACK,width=1)
    d.line([(cx-20,cy+r+11),(cx+20,cy+r+11)],fill=BLACK,width=1)
    d.line([(cx,cy+r+28),(cx-15,cy+r+48)],fill=BLACK,width=1)
    d.line([(cx,cy+r+28),(cx+15,cy+r+48)],fill=BLACK,width=1)
    bb=FB.getbbox(lbl); tw=bb[2]-bb[0]
    d.text((cx-tw//2,cy+r+52),lbl,font=FB,fill=BLACK)

def aline(d,ax,ay,cx,cy,rx,ry):
    ex,ey=ep(cx,cy,rx,ry,ax,ay)
    d.line([(ax,ay),(ex,ey)],fill=BLACK,width=1)

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT PLAN
# ─────────────────────────────────────────────────────────────────────────────
#
#  [Admin]                                              [Staff]
#    |                                                    |
#    |  [Kelola Pengguna]  [Login]  [Manajemen Aset]      |
#    |  Tambah/Edit/Hapus    (ctr)  Tambah/Edit/Hapus/Det |
#    |                              [Manajemen Barang]    |
#    |  [Audit Log]                 Tambah/Edit/Hapus     |
#    |  Filter                      [Manajemen Ruangan]   |
#    |                              Tambah/Edit/Hapus     |
#    |                              [QR Code]             |
#    |                              Generate/Scan/Cetak   |
#    |                              [Maintenance]         |
#    |                              Set/Selesaikan        |
#    |                              [Import Data]         |
#    |                              Aset/Barang/Template  |
#    |                              [Export & Laporan]    |
#    |                              Excel/PDF/Ruangan/Mnt |
#    |                              [Dashboard]           |
#
# Kolom kiri  = Admin-only features
# Kolom tengah= Login
# Kolom kanan = Shared features (Staff + Admin)
#
# ─────────────────────────────────────────────────────────────────────────────

# Semua use case dengan posisi (cx, cy) — dihitung dari grid
# Format: key, label, font, (col, row)
# col: 0=admin-only, 1=center(login), 2=shared
# row: 0..N

# Shared features (kanan) — per grup: main UC + extends di bawahnya
SHARED_GROUPS = [
    ("aset",        "Manajemen Aset",
     ["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"]),
    ("barang",      "Manajemen Barang",
     ["Tambah Barang","Edit Barang","Hapus Barang"]),
    ("ruangan",     "Manajemen Ruangan",
     ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"]),
    ("qr",          "QR Code",
     ["Generate QR","Scan QR","Cetak Massal"]),
    ("maintenance", "Maintenance",
     ["Set Maintenance","Selesaikan\nMaintenance"]),
    ("import",      "Import Data",
     ["Import Aset","Import Barang","Download Template"]),
    ("export",      "Export & Laporan",
     ["Export Excel","Export PDF","Laporan Ruangan","Laporan Maintenance"]),
    ("dashboard",   "Dashboard", []),
]

# Admin-only features (kiri)
ADMIN_GROUPS = [
    ("pengguna",    "Kelola Pengguna",
     ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"]),
    ("auditlog",    "Audit Log",
     ["Filter Audit Log"]),
]

# ─────────────────────────────────────────────────────────────────────────────
# COMPUTE SIZES
# ─────────────────────────────────────────────────────────────────────────────
def group_size(main_lbl, extends):
    """
    Layout: main UC on left, extends in column on right.
    Returns (width, height, main_rx, main_ry, ext_info)
    """
    mrx,mry = ell_r(main_lbl,FB)
    if not extends:
        return mrx*2+20, mry*2+16, mrx, mry, []

    esz = [(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
    max_erx = max(rx for _,rx,ry in esz)
    max_ery = max(ry for _,rx,ry in esz)
    n = len(extends)
    ext_h = n*(max_ery*2) + (n-1)*10

    w = 10 + mrx*2 + 16 + max_erx*2 + 10
    h = max(mry*2, ext_h) + 16
    return w, h, mrx, mry, esz

# Compute shared column layout
HGAP = 14  # vertical gap between groups in same column
shared_sizes = [group_size(lbl,ext) for _,lbl,ext in SHARED_GROUPS]
admin_sizes  = [group_size(lbl,ext) for _,lbl,ext in ADMIN_GROUPS]

shared_col_w = max(w for w,h,*_ in shared_sizes)
admin_col_w  = max(w for w,h,*_ in admin_sizes)

shared_col_h = sum(h for w,h,*_ in shared_sizes) + HGAP*(len(shared_sizes)-1)
admin_col_h  = sum(h for w,h,*_ in admin_sizes)  + HGAP*(len(admin_sizes)-1)

# Login size
login_rx,login_ry = ell_r("Login",FB)

# Canvas dimensions
PAD=20; TITLE_H=22; BPAD=16
ACTOR_W=55; ACTOR_GAP=30; COL_GAP=50

total_h = max(shared_col_h, admin_col_h, login_ry*2) + PAD*2 + TITLE_H + BPAD*2 + 40

# x positions
x_admin_actor = PAD + ACTOR_W//2
x_admin_col   = x_admin_actor + ACTOR_W//2 + ACTOR_GAP
x_login       = x_admin_col + admin_col_w + COL_GAP + login_rx
x_shared_col  = x_login + login_rx + COL_GAP
x_staff_actor = x_shared_col + shared_col_w + ACTOR_GAP + ACTOR_W//2

W = x_staff_actor + ACTOR_W//2 + PAD + 10

# y offset
Y_OFF = TITLE_H + BPAD + 10

# Login y = vertical center
login_y = Y_OFF + total_h//2

# Admin column y start = centered
admin_y_start = Y_OFF + (total_h - admin_col_h)//2

# Shared column y start = top
shared_y_start = Y_OFF + 20

H = Y_OFF + total_h + PAD + 20

# ─────────────────────────────────────────────────────────────────────────────
# DRAW
# ─────────────────────────────────────────────────────────────────────────────
img = Image.new("RGB",(W,H),BG)
d   = ImageDraw.Draw(img)

# border + title
d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([8,8,8+tw+10,8+TITLE_H],fill=BG,outline=BLACK,width=1)
d.text((12,10),tag,font=FT,fill=BLACK)

# system boundary
bx0=x_admin_col-8; bx1=x_shared_col+shared_col_w+8
d.rectangle([bx0,8+TITLE_H+4,bx1,H-12],fill=(255,255,252),outline=BLACK,width=1)

all_drawn = {}  # key/lbl → (cx,cy,rx,ry)

# ── Draw Login (center) ───────────────────────────────────────────────────────
lrx,lry = draw_ell(d,x_login,login_y,"Login",FB)
all_drawn["login"]=(x_login,login_y,lrx,lry)

# ── Draw Admin-only groups (left column) ──────────────────────────────────────
y = admin_y_start
for i,(key,main_lbl,extends) in enumerate(ADMIN_GROUPS):
    w,h,mrx,mry,esz = admin_sizes[i]
    cy_m = y + h//2
    cx_m = x_admin_col + mrx

    draw_ell(d,cx_m,cy_m,main_lbl,FB)
    all_drawn[key]=(cx_m,cy_m,mrx,mry)

    if esz:
        max_erx=max(rx for _,rx,ry in esz)
        max_ery=max(ry for _,rx,ry in esz)
        n=len(esz); ext_h=n*(max_ery*2)+(n-1)*10
        cx_e=cx_m+mrx+16+max_erx
        start_ey=cy_m-ext_h//2+max_ery
        for j,(lbl,erx,ery) in enumerate(esz):
            ey=start_ey+j*(ery*2+10)
            draw_ell(d,cx_e,ey,lbl,FS)
            all_drawn[lbl]=(cx_e,ey,erx,ery)
            conn(d,(cx_e,ey),(erx,ery),(cx_m,cy_m),(mrx,mry),"<<extend>>",dash=True)

    y += h + HGAP

# ── Draw Shared groups (right column) ─────────────────────────────────────────
y = shared_y_start
for i,(key,main_lbl,extends) in enumerate(SHARED_GROUPS):
    w,h,mrx,mry,esz = shared_sizes[i]
    cy_m = y + h//2
    cx_m = x_shared_col + mrx

    draw_ell(d,cx_m,cy_m,main_lbl,FB)
    all_drawn[key]=(cx_m,cy_m,mrx,mry)

    if esz:
        max_erx=max(rx for _,rx,ry in esz)
        max_ery=max(ry for _,rx,ry in esz)
        n=len(esz); ext_h=n*(max_ery*2)+(n-1)*10
        cx_e=cx_m+mrx+16+max_erx
        start_ey=cy_m-ext_h//2+max_ery
        for j,(lbl,erx,ery) in enumerate(esz):
            ey=start_ey+j*(ery*2+10)
            draw_ell(d,cx_e,ey,lbl,FS)
            all_drawn[lbl]=(cx_e,ey,erx,ery)
            conn(d,(cx_e,ey),(erx,ery),(cx_m,cy_m),(mrx,mry),"<<extend>>",dash=True)

    y += h + HGAP

# ── Include: all main UCs → Login ─────────────────────────────────────────────
for key in [k for k,*_ in ADMIN_GROUPS+SHARED_GROUPS]:
    if key in all_drawn:
        uc=all_drawn[key]
        conn(d,(uc[0],uc[1]),(uc[2],uc[3]),
               (x_login,login_y),(lrx,lry),"<<include>>",dash=True)

# ── Actors ────────────────────────────────────────────────────────────────────
actor(d,x_admin_actor,login_y-20,"Admin")
actor(d,x_staff_actor,login_y-20,"Staff")

# Admin → admin-only UCs + Login + shared UCs
for k in ["login"]+[k for k,*_ in ADMIN_GROUPS]+[k for k,*_ in SHARED_GROUPS]:
    if k in all_drawn:
        uc=all_drawn[k]
        aline(d,x_admin_actor,login_y-20,uc[0],uc[1],uc[2],uc[3])

# Staff → Login + shared UCs only
for k in ["login"]+[k for k,*_ in SHARED_GROUPS]:
    if k in all_drawn:
        uc=all_drawn[k]
        aline(d,x_staff_actor,login_y-20,uc[0],uc[1],uc[2],uc[3])

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
