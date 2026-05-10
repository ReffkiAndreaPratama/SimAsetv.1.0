"""
Use Case Diagram v9 — final clean version.
- Garis <<include>> digambar SEBELUM elips agar tidak menutupi teks
- Setiap garis masuk ke Login dari sudut berbeda (spread)
- Aktor hanya ke kolom terdekat
- Tidak ada arrow yang tumpang tindih dengan teks
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

def conn_pts(d,x1,y1,x2,y2,lbl="",dash=True):
    """Connect two points directly."""
    if dash: dline(d,x1,y1,x2,y2)
    else:    d.line([(x1,y1),(x2,y2)],fill=BLACK,width=1)
    ah(d,x2,y2,x1,y1)
    if lbl:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=FSM.getbbox(lbl); tw=bb[2]-bb[0]
        ang=math.atan2(y2-y1,x2-x1)
        ox=int(-math.sin(ang)*10); oy=int(math.cos(ang)*10)
        d.text((mx-tw//2+ox,my-FSM.size//2+oy),lbl,font=FSM,fill=GRAY)

def conn(d,c1,r1,c2,r2,lbl="",dash=True):
    x1,y1=ep(*c1,*r1,*c2[:2]); x2,y2=ep(*c2,*r2,*c1[:2])
    conn_pts(d,x1,y1,x2,y2,lbl,dash)

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

def grp_w(main_lbl,extends):
    mrx,_=ell_r(main_lbl,FB)
    if not extends: return mrx*2
    esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
    max_erx=max(rx for _,rx,ry in esz)
    return mrx*2+18+max_erx*2

def grp_h(main_lbl,extends):
    _,mry=ell_r(main_lbl,FB)
    if not extends: return mry*2
    esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
    max_ery=max(ry for _,rx,ry in esz)
    n=len(extends)
    return max(mry*2, n*(max_ery*2)+(n-1)*10)

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────────────
# DATA — susunan area per kolom
# Admin di kiri → kolom A & B di kiri Login
# Staff di kanan → kolom C & D di kanan Login
# Admin hanya terhubung ke kolom A (terdekat)
# Staff hanya terhubung ke kolom D (terdekat)
# Kolom B & C terhubung ke Login via <<include>> saja
# ─────────────────────────────────────────────────────────────────────────────

# Kolom A — paling kiri, dekat Admin
# Admin-only + fitur yang Admin sering pakai
COL_A = [
    ("pengguna","Kelola Pengguna",
     ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"],"admin_only"),
    ("auditlog","Audit Log",
     ["Filter Audit Log"],"admin_only"),
    ("aset","Manajemen Aset",
     ["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"],"both"),
]

# Kolom B — kiri dekat Login
COL_B = [
    ("barang","Manajemen Barang",
     ["Tambah Barang","Edit Barang","Hapus Barang"],"both"),
    ("ruangan","Manajemen Ruangan",
     ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"],"both"),
]

# Kolom C — kanan dekat Login
COL_C = [
    ("qr","QR Code",
     ["Generate QR","Scan QR","Cetak Massal"],"both"),
    ("maintenance","Maintenance",
     ["Set Maintenance","Selesaikan\nMaintenance"],"both"),
    ("import","Import Data",
     ["Import Aset","Import Barang","Download Template"],"both"),
]

# Kolom D — paling kanan, dekat Staff
COL_D = [
    ("export","Export & Laporan",
     ["Export Excel","Export PDF","Laporan Ruangan","Laporan Maintenance"],"both"),
]

# ─────────────────────────────────────────────────────────────────────────────
# DIMENSIONS
# ─────────────────────────────────────────────────────────────────────────────
VGAP=30; HGAP=50; PAD=18; TITLE_H=22; BPAD=14
ACTOR_W=55; ACTOR_GAP=40

def col_dims(col):
    w=max(grp_w(lbl,ext) for _,lbl,ext,_ in col)
    h=sum(grp_h(lbl,ext) for _,lbl,ext,_ in col)+VGAP*(len(col)-1)
    return w,h

a_w,a_h=col_dims(COL_A)
b_w,b_h=col_dims(COL_B)
c_w,c_h=col_dims(COL_C)
d_w,d_h=col_dims(COL_D)
login_rx,login_ry=ell_r("Login",FB)

total_h=max(a_h,b_h,c_h,d_h,login_ry*2+40)

x_actor_admin = PAD+ACTOR_W//2
x_col_a       = x_actor_admin+ACTOR_W//2+ACTOR_GAP
x_col_b       = x_col_a+a_w+HGAP
x_login       = x_col_b+b_w+HGAP+login_rx
x_col_c       = x_login+login_rx+HGAP
x_col_d       = x_col_c+c_w+HGAP
x_actor_staff = x_col_d+d_w+ACTOR_GAP+ACTOR_W//2

W=x_actor_staff+ACTOR_W//2+PAD+10
H=TITLE_H+BPAD*2+total_h+PAD*2+20
Y_OFF=TITLE_H+BPAD+PAD

def gy(y): return y+Y_OFF

login_y=gy(total_h//2)
def col_y0(h): return gy((total_h-h)//2)
a_y0=col_y0(a_h); b_y0=col_y0(b_h)
c_y0=col_y0(c_h); d_y0=col_y0(d_h)

# ─────────────────────────────────────────────────────────────────────────────
# COLLECT POSITIONS (without drawing yet)
# ─────────────────────────────────────────────────────────────────────────────
def collect_positions(col, x_col, y0, ext_dir):
    """Compute all (cx,cy,rx,ry) for main UCs and extends without drawing."""
    positions={}
    y=y0
    for key,main_lbl,extends,_ in col:
        gh=grp_h(main_lbl,extends)
        cy_m=y+gh//2
        mrx,mry=ell_r(main_lbl,FB)
        if ext_dir=="right":
            cx_m=x_col+mrx
        else:
            cx_m=x_col+grp_w(main_lbl,extends)-mrx
        positions[key]=(cx_m,cy_m,mrx,mry)
        if extends:
            esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
            max_erx=max(rx for _,rx,ry in esz)
            max_ery=max(ry for _,rx,ry in esz)
            n=len(extends); ext_h=n*(max_ery*2)+(n-1)*10
            cx_e=(cx_m+mrx+18+max_erx) if ext_dir=="right" else (cx_m-mrx-18-max_erx)
            start_ey=cy_m-ext_h//2+max_ery
            for i,(lbl,erx,ery) in enumerate(esz):
                ey=start_ey+i*(ery*2+10)
                positions[lbl]=(cx_e,ey,erx,ery)
        y+=gh+VGAP
    return positions

all_pos={}
all_pos.update(collect_positions(COL_A,x_col_a,a_y0,"right"))
all_pos.update(collect_positions(COL_B,x_col_b,b_y0,"right"))
all_pos.update(collect_positions(COL_C,x_col_c,c_y0,"left"))
all_pos.update(collect_positions(COL_D,x_col_d,d_y0,"left"))
all_pos["login"]=(x_login,login_y,login_rx,login_ry)

# ─────────────────────────────────────────────────────────────────────────────
# DRAW — order: lines first, then ellipses on top
# ─────────────────────────────────────────────────────────────────────────────
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)

# border + title
d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([8,8,8+tw+10,8+TITLE_H],fill=BG,outline=BLACK,width=1)
d.text((12,10),tag,font=FT,fill=BLACK)

# system boundary
bx0=x_col_a-8; bx1=x_col_d+d_w+8
d.rectangle([bx0,8+TITLE_H+4,bx1,H-12],fill=(255,255,252),outline=BLACK,width=1)

# ── STEP 1: Draw <<include>> lines FIRST (behind everything) ─────────────────
all_main_keys=[k for k,*_ in COL_A+COL_B+COL_C+COL_D]
lx,ly,lrx,lry=all_pos["login"]

for k in all_main_keys:
    if k not in all_pos: continue
    cx,cy,rx,ry=all_pos[k]
    # edge point on UC ellipse toward Login
    x1,y1=ep(cx,cy,rx,ry,lx,ly)
    # edge point on Login ellipse toward UC
    x2,y2=ep(lx,ly,lrx,lry,cx,cy)
    dline(d,x1,y1,x2,y2)
    ah(d,x2,y2,x1,y1)
    # label at midpoint, offset perpendicular
    mx,my=(x1+x2)//2,(y1+y2)//2
    ang=math.atan2(y2-y1,x2-x1)
    ox=int(-math.sin(ang)*10); oy=int(math.cos(ang)*10)
    bb2=FSM.getbbox("<<include>>"); tw2=bb2[2]-bb2[0]
    d.text((mx-tw2//2+ox,my-FSM.size//2+oy),"<<include>>",font=FSM,fill=GRAY)

# ── STEP 2: Draw <<extend>> lines (behind ellipses) ──────────────────────────
def draw_extend_lines(col, x_col, y0, ext_dir):
    y=y0
    for key,main_lbl,extends,_ in col:
        gh=grp_h(main_lbl,extends)
        cy_m=y+gh//2
        mrx,mry=ell_r(main_lbl,FB)
        cx_m=all_pos[key][0]; cy_m=all_pos[key][1]
        if extends:
            esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
            for lbl,erx,ery in esz:
                if lbl not in all_pos: continue
                cx_e,ey,erx2,ery2=all_pos[lbl]
                x1,y1=ep(cx_e,ey,erx2,ery2,cx_m,cy_m)
                x2,y2=ep(cx_m,cy_m,mrx,mry,cx_e,ey)
                dline(d,x1,y1,x2,y2)
                ah(d,x2,y2,x1,y1)
                mx2,my2=(x1+x2)//2,(y1+y2)//2
                ang=math.atan2(y2-y1,x2-x1)
                ox=int(-math.sin(ang)*10); oy=int(math.cos(ang)*10)
                bb3=FSM.getbbox("<<extend>>"); tw3=bb3[2]-bb3[0]
                d.text((mx2-tw3//2+ox,my2-FSM.size//2+oy),"<<extend>>",font=FSM,fill=GRAY)
        y+=gh+VGAP

draw_extend_lines(COL_A,x_col_a,a_y0,"right")
draw_extend_lines(COL_B,x_col_b,b_y0,"right")
draw_extend_lines(COL_C,x_col_c,c_y0,"left")
draw_extend_lines(COL_D,x_col_d,d_y0,"left")

# ── STEP 3: Draw actor lines with bend to avoid overlap ──────────────────────
# Strategy: actor → vertical waypoint at actor x → horizontal to UC edge
# Each UC gets a unique waypoint y so lines don't overlap

admin_y=login_y-20; staff_y=login_y-20

# All main UC keys with their access level
all_main_with_acc = [(k,acc) for k,lbl,ext,acc in COL_A+COL_B+COL_C+COL_D]

# Admin connects to all UCs
admin_ucs = [(k,acc) for k,acc in all_main_with_acc]
# Staff connects to "both" only
staff_ucs = [(k,acc) for k,acc in all_main_with_acc if acc=="both"]

def actor_line(d, ax, ay, cx, cy, rx, ry):
    """Straight line from actor to UC edge."""
    ex, ey = ep(cx, cy, rx, ry, ax, ay)
    d.line([(ax, ay), (ex, ey)], fill=BLACK, width=1)

admin_y = login_y - 20
staff_y = login_y - 20

# Admin → hanya kolom A (terdekat, garis pendek, tidak melewati UC lain)
for k,lbl,ext,acc in COL_A:
    if k in all_pos:
        cx,cy,rx,ry = all_pos[k]
        actor_line(d, x_actor_admin, admin_y, cx, cy, rx, ry)

# Staff → hanya kolom D (terdekat, garis pendek, tidak melewati UC lain)
for k,lbl,ext,acc in COL_D:
    if k in all_pos:
        cx,cy,rx,ry = all_pos[k]
        actor_line(d, x_actor_staff, staff_y, cx, cy, rx, ry)

# ── STEP 4: Draw ALL ellipses ON TOP of lines ─────────────────────────────────
# This ensures no line covers any ellipse text

def draw_all_ellipses(col, x_col, y0, ext_dir):
    y=y0
    for key,main_lbl,extends,_ in col:
        gh=grp_h(main_lbl,extends)
        cx_m,cy_m,mrx,mry=all_pos[key]
        draw_ell(d,cx_m,cy_m,main_lbl,FB)
        if extends:
            esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in extends]
            for lbl,erx,ery in esz:
                if lbl in all_pos:
                    cx_e,ey,_,_=all_pos[lbl]
                    draw_ell(d,cx_e,ey,lbl,FS)
        y+=gh+VGAP

draw_all_ellipses(COL_A,x_col_a,a_y0,"right")
draw_all_ellipses(COL_B,x_col_b,b_y0,"right")
draw_all_ellipses(COL_C,x_col_c,c_y0,"left")
draw_all_ellipses(COL_D,x_col_d,d_y0,"left")

# Login ellipse on top
draw_ell(d,lx,ly,"Login",FB)

# ── STEP 5: Draw actors ON TOP ────────────────────────────────────────────────
actor(d,x_actor_admin,admin_y,"Admin")
actor(d,x_actor_staff,staff_y,"Staff")

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
