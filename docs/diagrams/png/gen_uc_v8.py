"""
Use Case Diagram v8 — wide, not tall.
Login di tengah, fitur dibagi grid 2 kolom kiri & kanan Login.
Admin di kiri luar, Staff di kanan luar.
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
# GROUP HELPER — main UC + extends in a horizontal row
# main UC on left, extends spread to the right
# ─────────────────────────────────────────────────────────────────────────────
def place_group(d, key, main_lbl, extends, cx_main, cy_main, ext_dir="right"):
    """
    Draw main UC at (cx_main, cy_main).
    Extends placed in a column to the right or left.
    Returns dict of drawn positions.
    """
    drawn = {}
    mrx,mry = draw_ell(d,cx_main,cy_main,main_lbl,FB)
    drawn[key]=(cx_main,cy_main,mrx,mry)

    if not extends:
        return drawn

    esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
    max_erx=max(rx for _,rx,ry in esz)
    max_ery=max(ry for _,rx,ry in esz)
    n=len(extends); ext_h=n*(max_ery*2)+(n-1)*10

    if ext_dir=="right":
        cx_e=cx_main+mrx+18+max_erx
    else:
        cx_e=cx_main-mrx-18-max_erx

    start_ey=cy_main-ext_h//2+max_ery
    for i,(lbl,erx,ery) in enumerate(esz):
        ey=start_ey+i*(ery*2+10)
        draw_ell(d,cx_e,ey,lbl,FS)
        drawn[lbl]=(cx_e,ey,erx,ery)
        conn(d,(cx_e,ey),(erx,ery),(cx_main,cy_main),(mrx,mry),"<<extend>>",dash=True)

    return drawn

def group_width(main_lbl, extends, ext_dir="right"):
    mrx,mry=ell_r(main_lbl,FB)
    if not extends: return mrx*2
    esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
    max_erx=max(rx for _,rx,ry in esz)
    return mrx*2+18+max_erx*2

def group_height(main_lbl, extends):
    _,mry=ell_r(main_lbl,FB)
    if not extends: return mry*2
    esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
    max_ery=max(ry for _,rx,ry in esz)
    n=len(extends)
    ext_h=n*(max_ery*2)+(n-1)*10
    return max(mry*2,ext_h)

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
# Kiri Login (2 kolom × N baris)
LEFT_GROUPS = [
    # col 0 (paling kiri)
    [
        ("aset",    "Manajemen Aset",
         ["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"]),
        ("barang",  "Manajemen Barang",
         ["Tambah Barang","Edit Barang","Hapus Barang"]),
        ("ruangan", "Manajemen Ruangan",
         ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"]),
    ],
    # col 1 (dekat Login)
    [
        ("qr",          "QR Code",
         ["Generate QR","Scan QR","Cetak Massal"]),
        ("maintenance", "Maintenance",
         ["Set Maintenance","Selesaikan\nMaintenance"]),
        ("dashboard",   "Dashboard", []),
    ],
]

# Kanan Login (1 kolom)
RIGHT_GROUPS = [
    [
        ("import",  "Import Data",
         ["Import Aset","Import Barang","Download Template"]),
        ("export",  "Export & Laporan",
         ["Export Excel","Export PDF","Laporan Ruangan","Laporan Maintenance"]),
    ],
]

# Admin-only (dekat Admin, kiri luar)
ADMIN_GROUPS = [
    ("pengguna", "Kelola Pengguna",
     ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"]),
    ("auditlog", "Audit Log",
     ["Filter Audit Log"]),
]

# ─────────────────────────────────────────────────────────────────────────────
# COMPUTE LAYOUT
# ─────────────────────────────────────────────────────────────────────────────
VGAP=20; HGAP=30; PAD=18; TITLE_H=22; BPAD=14
ACTOR_W=55; ACTOR_GAP=28

# Compute column widths for left groups
# Left col 0: extends go LEFT (toward actor), main UC on right side of col
# Left col 1: extends go LEFT, main UC on right side
# Right col 0: extends go RIGHT

def col_dims(groups, ext_dir):
    w = max(group_width(lbl,ext,ext_dir) for _,lbl,ext in groups)
    h = sum(group_height(lbl,ext) for _,lbl,ext in groups) + VGAP*(len(groups)-1)
    return w,h

lc0_w,lc0_h = col_dims(LEFT_GROUPS[0], "left")
lc1_w,lc1_h = col_dims(LEFT_GROUPS[1], "left")
rc0_w,rc0_h = col_dims(RIGHT_GROUPS[0], "right")

login_rx,login_ry = ell_r("Login",FB)

# Admin-only column (left of everything)
adm_w = max(group_width(lbl,ext,"right") for _,lbl,ext in ADMIN_GROUPS)
adm_h = sum(group_height(lbl,ext) for _,lbl,ext in ADMIN_GROUPS) + VGAP*(len(ADMIN_GROUPS)-1)

# Total height = max of all columns
total_h = max(lc0_h, lc1_h, rc0_h, adm_h, login_ry*2+40)

# X positions (left to right):
# actor_admin | adm_col | gap | lc0 | gap | lc1 | gap | login | gap | rc0 | gap | actor_staff
x_actor_admin = PAD + ACTOR_W//2
x_adm_col     = x_actor_admin + ACTOR_W//2 + ACTOR_GAP
# adm extends go RIGHT from main UC
x_lc0         = x_adm_col + adm_w + HGAP
x_lc1         = x_lc0 + lc0_w + HGAP
x_login       = x_lc1 + lc1_w + HGAP + login_rx
x_rc0         = x_login + login_rx + HGAP
x_actor_staff = x_rc0 + rc0_w + ACTOR_GAP + ACTOR_W//2

W = x_actor_staff + ACTOR_W//2 + PAD + 10
H = TITLE_H + BPAD*2 + total_h + PAD*2 + 20
Y_OFF = TITLE_H + BPAD + PAD

def gy(y): return y + Y_OFF

# Center y for each column
login_y   = gy(total_h//2)
adm_y0    = gy((total_h-adm_h)//2)
lc0_y0    = gy((total_h-lc0_h)//2)
lc1_y0    = gy((total_h-lc1_h)//2)
rc0_y0    = gy((total_h-rc0_h)//2)

# ─────────────────────────────────────────────────────────────────────────────
# DRAW
# ─────────────────────────────────────────────────────────────────────────────
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)

# border + title
d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([8,8,8+tw+10,8+TITLE_H],fill=BG,outline=BLACK,width=1)
d.text((12,10),tag,font=FT,fill=BLACK)

# system boundary
bx0=x_adm_col-8; bx1=x_rc0+rc0_w+8
d.rectangle([bx0,8+TITLE_H+4,bx1,H-12],fill=(255,255,252),outline=BLACK,width=1)

all_drawn={}

# ── Login ─────────────────────────────────────────────────────────────────────
lrx,lry=draw_ell(d,x_login,login_y,"Login",FB)
all_drawn["login"]=(x_login,login_y,lrx,lry)

# ── Admin-only groups ─────────────────────────────────────────────────────────
y=adm_y0
for key,main_lbl,extends in ADMIN_GROUPS:
    gh=group_height(main_lbl,extends)
    cy_m=y+gh//2
    # main UC: right side of adm col, extends go right
    mrx,mry=ell_r(main_lbl,FB)
    cx_m=x_adm_col+mrx
    drawn=place_group(d,key,main_lbl,extends,cx_m,cy_m,"right")
    all_drawn.update(drawn)
    y+=gh+VGAP

# ── Left col 0 ────────────────────────────────────────────────────────────────
y=lc0_y0
for key,main_lbl,extends in LEFT_GROUPS[0]:
    gh=group_height(main_lbl,extends)
    cy_m=y+gh//2
    mrx,mry=ell_r(main_lbl,FB)
    # main UC on right side of col, extends go left
    cx_m=x_lc0+lc0_w-mrx
    drawn=place_group(d,key,main_lbl,extends,cx_m,cy_m,"left")
    all_drawn.update(drawn)
    y+=gh+VGAP

# ── Left col 1 ────────────────────────────────────────────────────────────────
y=lc1_y0
for key,main_lbl,extends in LEFT_GROUPS[1]:
    gh=group_height(main_lbl,extends)
    cy_m=y+gh//2
    mrx,mry=ell_r(main_lbl,FB)
    cx_m=x_lc1+lc1_w-mrx
    drawn=place_group(d,key,main_lbl,extends,cx_m,cy_m,"left")
    all_drawn.update(drawn)
    y+=gh+VGAP

# ── Right col 0 ───────────────────────────────────────────────────────────────
y=rc0_y0
for key,main_lbl,extends in RIGHT_GROUPS[0]:
    gh=group_height(main_lbl,extends)
    cy_m=y+gh//2
    mrx,mry=ell_r(main_lbl,FB)
    cx_m=x_rc0+mrx
    drawn=place_group(d,key,main_lbl,extends,cx_m,cy_m,"right")
    all_drawn.update(drawn)
    y+=gh+VGAP

# ── Include: all main UCs → Login ─────────────────────────────────────────────
all_main_keys=[k for k,*_ in ADMIN_GROUPS+LEFT_GROUPS[0]+LEFT_GROUPS[1]+RIGHT_GROUPS[0]]
for k in all_main_keys:
    if k in all_drawn:
        uc=all_drawn[k]
        conn(d,(uc[0],uc[1]),(uc[2],uc[3]),
               (x_login,login_y),(lrx,lry),"<<include>>",dash=True)

# ── Actors ────────────────────────────────────────────────────────────────────
actor(d,x_actor_admin,login_y-20,"Admin")
actor(d,x_actor_staff,login_y-20,"Staff")

# Admin → semua main UCs
for k in ["login"]+all_main_keys:
    if k in all_drawn:
        uc=all_drawn[k]
        aline(d,x_actor_admin,login_y-20,uc[0],uc[1],uc[2],uc[3])

# Staff → shared UCs only (bukan admin-only)
admin_only_keys=[k for k,*_ in ADMIN_GROUPS]
staff_keys=["login"]+[k for k,*_ in LEFT_GROUPS[0]+LEFT_GROUPS[1]+RIGHT_GROUPS[0]]
for k in staff_keys:
    if k in all_drawn:
        uc=all_drawn[k]
        aline(d,x_actor_staff,login_y-20,uc[0],uc[1],uc[2],uc[3])

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
