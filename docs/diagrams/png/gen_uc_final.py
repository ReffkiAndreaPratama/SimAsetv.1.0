"""
Use Case Diagram FINAL — bersih seperti foto contoh.

Layout persis foto:
- Admin di KIRI LUAR boundary
- Staff di KANAN LUAR boundary  
- Use case utama dalam 1 KOLOM di tengah
- Extend items di kiri/kanan use case masing-masing
- Aktor hanya terhubung ke use case yang ada di sisi mereka
- Tidak ada garis yang melintasi seluruh diagram
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
# DATA — use case utama dalam urutan vertikal
# ─────────────────────────────────────────────────────────────────────────────
# (key, label, admin_only)
MAIN = [
    ("aset",        "Manajemen Aset",    False),
    ("barang",      "Manajemen Barang",  False),
    ("ruangan",     "Manajemen Ruangan", False),
    ("qr",          "QR Code",           False),
    ("maintenance", "Maintenance",       False),
    ("login",       "Login",             False),  # Login di tengah
    ("import",      "Import Data",       False),
    ("export",      "Export & Laporan",  False),
    ("dashboard",   "Dashboard",         False),
    ("pengguna",    "Kelola Pengguna",   True),
    ("auditlog",    "Audit Log",         True),
]

# Extend items — kiri untuk baris atas, kanan untuk baris bawah
# (parent_key, items, side)
EXT = [
    ("aset",        ["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"],              "left"),
    ("barang",      ["Tambah Barang","Edit Barang","Hapus Barang"],                       "left"),
    ("ruangan",     ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"],                    "left"),
    ("qr",          ["Generate QR","Scan QR","Cetak Massal"],                             "left"),
    ("maintenance", ["Set Maintenance","Selesaikan\nMaintenance"],                        "left"),
    ("import",      ["Import Aset","Import Barang","Download Template"],                  "right"),
    ("export",      ["Export Excel","Export PDF","Laporan Ruangan","Laporan Maintenance"],"right"),
    ("pengguna",    ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"],                 "right"),
    ("auditlog",    ["Filter Audit Log"],                                                  "right"),
]

# ─────────────────────────────────────────────────────────────────────────────
# SIZES
# ─────────────────────────────────────────────────────────────────────────────
uc_sz  = {k:ell_r(lbl,FB) for k,lbl,_ in MAIN}
ext_sz = {lbl:ell_r(lbl,FS,px=13,py=9)
          for _,items,_ in EXT for lbl in items}

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT
# ─────────────────────────────────────────────────────────────────────────────
ROW_GAP = 24

# Row heights
row_h = []
for k,lbl,_ in MAIN:
    uc_ry = uc_sz[k][1]
    ext_items = next((items for pk,items,_ in EXT if pk==k),[])
    max_ery = max((ext_sz[it][1] for it in ext_items),default=0)
    row_h.append(max(uc_ry,max_ery)*2 + ROW_GAP)

# Column x
max_uc_rx    = max(rx for rx,ry in uc_sz.values())
max_ext_rx_L = max((ext_sz[it][0] for _,items,s in EXT for it in items if s=="left"),default=50)
max_ext_rx_R = max((ext_sz[it][0] for _,items,s in EXT for it in items if s=="right"),default=50)

PAD=16; ACT_W=50; ACT_GAP=28; EXT_GAP=28

# x positions (left to right):
# actor_admin | boundary_start | ext_left | main_uc | ext_right | boundary_end | actor_staff
x_admin   = PAD + ACT_W//2
x_bnd_l   = x_admin + ACT_W//2 + ACT_GAP
x_ext_L   = x_bnd_l + 10 + max_ext_rx_L
x_main    = x_ext_L + max_ext_rx_L + EXT_GAP + max_uc_rx
x_ext_R   = x_main + max_uc_rx + EXT_GAP + max_ext_rx_R
x_bnd_r   = x_ext_R + max_ext_rx_R + 10
x_staff   = x_bnd_r + ACT_GAP + ACT_W//2

W = x_staff + ACT_W//2 + PAD + 10

# y positions
TOP = 55; TITLE_H=22; BPAD=16
y_rows=[]; y=TOP
for rh in row_h:
    y_rows.append(y+rh//2); y+=rh
H_cont=y+30
H=TITLE_H+BPAD*2+H_cont+20
Y_OFF=TITLE_H+BPAD+8

def gy(y): return y+Y_OFF

# ─────────────────────────────────────────────────────────────────────────────
# DRAW
# ─────────────────────────────────────────────────────────────────────────────
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)

# outer border
d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
# title tag
tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([8,8,8+tw+10,8+TITLE_H],fill=BG,outline=BLACK,width=1)
d.text((12,10),tag,font=FT,fill=BLACK)

# system boundary
d.rectangle([x_bnd_l,8+TITLE_H+4,x_bnd_r,H-12],
             fill=(255,255,252),outline=BLACK,width=1)

# ── Main use cases ────────────────────────────────────────────────────────────
uc_d={}
for i,(k,lbl,_) in enumerate(MAIN):
    cx=x_main; cy=gy(y_rows[i])
    rx,ry=draw_ell(d,cx,cy,lbl,FB)
    uc_d[k]=(cx,cy,rx,ry)

# ── Extend ellipses & arrows ──────────────────────────────────────────────────
for pk,items,side in EXT:
    if pk not in uc_d: continue
    pcx,pcy,prx,pry=uc_d[pk]
    n=len(items)
    max_ery=max(ext_sz[it][1] for it in items)
    sp=max_ery*2+16
    total=(n-1)*sp
    ex=x_ext_L if side=="left" else x_ext_R
    for i,lbl in enumerate(items):
        ey=gy(pcy-Y_OFF-total//2+i*sp)  # relative to parent y
        # recalculate: center extends around parent cy
        ey=pcy-total//2+i*sp
        rx,ry=ext_sz[lbl]
        draw_ell(d,ex,ey,lbl,FS)
        conn(d,(ex,ey),(rx,ry),(pcx,pcy),(prx,pry),"<<extend>>",dash=True)

# ── Include: main UCs → Login ─────────────────────────────────────────────────
lc=uc_d["login"]
for k,lbl,_ in MAIN:
    if k=="login": continue
    uc=uc_d[k]
    conn(d,(uc[0],uc[1]),(uc[2],uc[3]),
           (lc[0],lc[1]),(lc[2],lc[3]),"<<include>>",dash=True)

# ── Actors ────────────────────────────────────────────────────────────────────
# Actor y = middle of diagram
mid_y=gy(y_rows[len(y_rows)//2])
actor(d,x_admin,mid_y-20,"Admin")
actor(d,x_staff,mid_y-20,"Staff")

# Aktor hanya terhubung ke use case yang BERDEKATAN secara vertikal
# (bukan ke semua — itu yang bikin jaring laba-laba)
# Admin → use case di sisi kiri (baris 0-4) + Login
# Staff → use case di sisi kanan (baris 6-8) + Login
admin_connect = ["aset","barang","ruangan","qr","maintenance","login",
                 "pengguna","auditlog"]
staff_connect = ["import","export","dashboard","login",
                 "aset","barang","ruangan","qr","maintenance"]

for k in admin_connect:
    if k in uc_d:
        uc=uc_d[k]
        aline(d,x_admin,mid_y-20,uc[0],uc[1],uc[2],uc[3])

for k in staff_connect:
    if k in uc_d:
        uc=uc_d[k]
        aline(d,x_staff,mid_y-20,uc[0],uc[1],uc[2],uc[3])

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
