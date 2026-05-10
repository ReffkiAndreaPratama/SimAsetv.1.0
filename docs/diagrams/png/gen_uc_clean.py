"""
Use Case Diagram CLEAN — layout 2 kolom seperti foto contoh.

Layout:
Admin (kiri) → use case kiri kolom → Login (tengah) ← use case kanan kolom ← Staff (kanan)
Extend items di luar masing-masing kolom.
Aktor hanya terhubung ke use case di sisi mereka + Login.
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

def ell_r(txt,f,px=16,py=10):
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

def ah(d,x2,y2,x1,y1,s=7):
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

def aline(d,ax,ay,cx,cy,rx,ry):
    ex,ey=ep(cx,cy,rx,ry,ax,ay)
    d.line([(ax,ay),(ex,ey)],fill=BLACK,width=1)

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
# Kolom KIRI (Admin side) — use case yang lebih sering dipakai Admin
LEFT_UCS = [
    ("aset",        "Manajemen Aset"),
    ("barang",      "Manajemen Barang"),
    ("ruangan",     "Manajemen Ruangan"),
    ("qr",          "QR Code"),
    ("maintenance", "Maintenance"),
    ("pengguna",    "Kelola Pengguna"),  # Admin only
    ("auditlog",    "Audit Log"),        # Admin only
]

# Kolom KANAN (Staff side)
RIGHT_UCS = [
    ("import",      "Import Data"),
    ("export",      "Export & Laporan"),
    ("dashboard",   "Dashboard"),
]

# Login di tengah
LOGIN = ("login", "Login")

# Extend items
# (parent_key, items, side_of_extends)
# side: "outer" = di luar kolom (kiri untuk left col, kanan untuk right col)
EXT = [
    ("aset",        ["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"],              "left"),
    ("barang",      ["Tambah Barang","Edit Barang","Hapus Barang"],                       "left"),
    ("ruangan",     ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"],                    "left"),
    ("qr",          ["Generate QR","Scan QR","Cetak Massal"],                             "left"),
    ("maintenance", ["Set Maintenance","Selesaikan\nMaintenance"],                        "left"),
    ("pengguna",    ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"],                 "left"),
    ("auditlog",    ["Filter Audit Log"],                                                  "left"),
    ("import",      ["Import Aset","Import Barang","Download Template"],                  "right"),
    ("export",      ["Export Excel","Export PDF","Laporan Ruangan","Laporan Maintenance"],"right"),
]

# ─────────────────────────────────────────────────────────────────────────────
# SIZES
# ─────────────────────────────────────────────────────────────────────────────
all_ucs = LEFT_UCS + RIGHT_UCS + [LOGIN]
uc_sz   = {k:ell_r(lbl,FB) for k,lbl in all_ucs}
ext_sz  = {lbl:ell_r(lbl,FS,px=13,py=9)
           for _,items,_ in EXT for lbl in items}

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT
# ─────────────────────────────────────────────────────────────────────────────
ROW_GAP=22

def col_layout(ucs, ext_data, side):
    """Compute row heights for a column."""
    rows=[]
    for k,lbl in ucs:
        uc_ry=uc_sz[k][1]
        items=next((it for pk,it,s in ext_data if pk==k),[])
        max_ery=max((ext_sz[it][1] for it in items),default=0)
        rows.append(max(uc_ry,max_ery)*2+ROW_GAP)
    return rows

left_rows  = col_layout(LEFT_UCS,  EXT, "left")
right_rows = col_layout(RIGHT_UCS, EXT, "right")

# Align rows: left and right columns share y space
# Left has more rows, right has fewer — center right vertically
n_left=len(left_rows); n_right=len(right_rows)
total_left_h  = sum(left_rows)
total_right_h = sum(right_rows)

# y positions for left column
TOP=50; TITLE_H=22; BPAD=16
y_left=[]; y=TOP
for rh in left_rows:
    y_left.append(y+rh//2); y+=rh
total_h=y

# y positions for right column — centered vertically
right_start=(total_h-total_right_h)//2+TOP
y_right=[]; y=right_start
for rh in right_rows:
    y_right.append(y+rh//2); y+=rh

# Login y = middle of left column
login_y=y_left[len(y_left)//2]

# Column x positions
max_uc_rx_L  = max(uc_sz[k][0] for k,_ in LEFT_UCS)
max_uc_rx_R  = max(uc_sz[k][0] for k,_ in RIGHT_UCS)
max_uc_rx_LG = uc_sz["login"][0]

max_ext_rx_L = max((ext_sz[it][0] for pk,items,s in EXT for it in items if s=="left"),default=50)
max_ext_rx_R = max((ext_sz[it][0] for pk,items,s in EXT for it in items if s=="right"),default=50)

PAD=16; ACT_W=50; ACT_GAP=30; EXT_GAP=26; COL_GAP=50

x_admin    = PAD+ACT_W//2
x_ext_L    = x_admin+ACT_W//2+ACT_GAP+max_ext_rx_L
x_col_L    = x_ext_L+max_ext_rx_L+EXT_GAP+max_uc_rx_L
x_login    = x_col_L+max_uc_rx_L+COL_GAP+max_uc_rx_LG
x_col_R    = x_login+max_uc_rx_LG+COL_GAP+max_uc_rx_R
x_ext_R    = x_col_R+max_uc_rx_R+EXT_GAP+max_ext_rx_R
x_staff    = x_ext_R+max_ext_rx_R+ACT_GAP+ACT_W//2

W=x_staff+ACT_W//2+PAD+10
H=TITLE_H+BPAD*2+total_h+TOP+30
Y_OFF=TITLE_H+BPAD+8

def gy(y): return y+Y_OFF

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
bx0=x_ext_L-max_ext_rx_L-8; bx1=x_ext_R+max_ext_rx_R+8
d.rectangle([bx0,8+TITLE_H+4,bx1,H-12],fill=(255,255,252),outline=BLACK,width=1)

# ── Draw use cases ────────────────────────────────────────────────────────────
uc_d={}

# Left column
for i,(k,lbl) in enumerate(LEFT_UCS):
    cx=x_col_L; cy=gy(y_left[i])
    rx,ry=draw_ell(d,cx,cy,lbl,FB)
    uc_d[k]=(cx,cy,rx,ry)

# Right column
for i,(k,lbl) in enumerate(RIGHT_UCS):
    cx=x_col_R; cy=gy(y_right[i])
    rx,ry=draw_ell(d,cx,cy,lbl,FB)
    uc_d[k]=(cx,cy,rx,ry)

# Login
lx=x_login; ly=gy(login_y)
lrx,lry=draw_ell(d,lx,ly,"Login",FB)
uc_d["login"]=(lx,ly,lrx,lry)

# ── Extend ellipses & arrows ──────────────────────────────────────────────────
for pk,items,side in EXT:
    if pk not in uc_d: continue
    pcx,pcy,prx,pry=uc_d[pk]
    n=len(items)
    max_ery=max(ext_sz[it][1] for it in items)
    sp=max_ery*2+16; total=(n-1)*sp
    ex=x_ext_L if side=="left" else x_ext_R
    for i,lbl in enumerate(items):
        ey=pcy-total//2+i*sp
        rx,ry=ext_sz[lbl]
        draw_ell(d,ex,ey,lbl,FS)
        conn(d,(ex,ey),(rx,ry),(pcx,pcy),(prx,pry),"<<extend>>",dash=True)

# ── Include: all main UCs → Login ─────────────────────────────────────────────
for k,lbl in LEFT_UCS+RIGHT_UCS:
    uc=uc_d[k]
    conn(d,(uc[0],uc[1]),(uc[2],uc[3]),(lx,ly),(lrx,lry),"<<include>>",dash=True)

# ── Actors ────────────────────────────────────────────────────────────────────
admin_y=gy(login_y)-20; staff_y=gy(login_y)-20
actor(d,x_admin,admin_y,"Admin")
actor(d,x_staff,staff_y,"Staff")

# Admin → left column UCs + Login (short lines, no crossing)
for k,lbl in LEFT_UCS+[LOGIN]:
    uc=uc_d[k]
    aline(d,x_admin,admin_y,uc[0],uc[1],uc[2],uc[3])

# Staff → right column UCs + Login + shared UCs
staff_ucs=[k for k,lbl in RIGHT_UCS]+["login","aset","barang","ruangan","qr","maintenance"]
for k in staff_ucs:
    if k in uc_d:
        uc=uc_d[k]
        aline(d,x_staff,staff_y,uc[0],uc[1],uc[2],uc[3])

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
