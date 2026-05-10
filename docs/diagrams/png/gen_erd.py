"""
ERD gaya Chen — layout bersih, tidak ada tumpang tindih.
Prinsip: setiap entitas punya zona eksklusif untuk atributnya.
Jarak antar entitas cukup besar agar zona tidak overlap.
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

FB=F(13,True); FN=F(11); FNB=F(11,True); FS=F(10); FT=F(11,True)
BG=(235,235,235); WHITE=(255,255,255); BLACK=(0,0,0)

def ell_rx_ry(lbl, pk=False):
    font = FNB if pk else FN
    bb = font.getbbox(lbl)
    return (bb[2]-bb[0])//2+13, (bb[3]-bb[1])//2+8

def ep_rect(cx,cy,ew,eh,tx,ty):
    dx,dy=tx-cx,ty-cy; L=max(1,math.hypot(dx,dy))
    hw,hh=ew//2,eh//2
    if L==0: return cx,cy
    t = min(hw/max(1e-9,abs(dx/L)), hh/max(1e-9,abs(dy/L)))
    return int(cx+dx/L*t), int(cy+dy/L*t)

def ep_ell(cx,cy,rx,ry,tx,ty):
    dx,dy=tx-cx,ty-cy; L=max(1,math.hypot(dx,dy))
    denom=math.sqrt((dx/L/rx)**2+(dy/L/ry)**2)
    if denom==0: return cx,cy
    return int(cx+dx/L/denom), int(cy+dy/L/denom)

# ─────────────────────────────────────────────────────────────────────────────
# ENTITY POSITIONS
# Zona per entitas (lebar ~300px, tinggi ~300px):
#
#  Row 1 (y=300):  users(cx=500)          log_aktivitas(cx=1200)
#  Row 2 (y=700):  barang(cx=200)  ruangan(cx=700)  aset(cx=1200)
#
# Jarak horizontal antar entitas baris bawah: 500px → cukup untuk atribut
# ─────────────────────────────────────────────────────────────────────────────
EW=130; EH=38

UX,UY   = 500,  300    # users
LX,LY   = 1200, 300    # log_aktivitas
BX,BY   = 200,  700    # barang
RX,RY   = 700,  700    # ruangan
AX,AY   = 1200, 700    # aset

# Diamonds — di jalur langsung antara dua entitas
DC_X,DC_Y = 850,  300   # mencatat: users→log (horizontal)
DM_X,DM_Y = 850,  500   # membuat: users→aset (diagonal)
DP_X,DP_Y = 450,  700   # memiliki: barang→aset (horizontal, antara barang & ruangan)
DN_X,DN_Y = 950,  700   # menampung: ruangan→aset (horizontal, antara ruangan & aset)

DW=90; DH=44

# ─────────────────────────────────────────────────────────────────────────────
# ATTRIBUTES — setiap entitas punya zona eksklusif
#
# users (500,300):
#   Atas: id, name, email, password, role  → y=300-120 sampai 300-160
#   Kiri: is_active                         → x=500-180
#   (relasi ke kanan: mencatat, membuat — jadi kiri & atas aman)
#
# log_aktivitas (1200,300):
#   Atas: id, aktivitas, keterangan, ip_address, user_agent
#   (relasi dari kiri — atas & kanan aman)
#
# barang (200,700):
#   Atas: kode_barang, nama_barang, kategori
#   Bawah: status, keterangan
#   (relasi ke kanan — kiri & atas & bawah aman)
#
# ruangan (700,700):
#   Atas: id, nama, lantai
#   Bawah: keterangan
#   (relasi ke kanan — atas & bawah aman, kiri ada diamond memiliki)
#
# aset (1200,700):
#   Atas: kode_aset, kondisi, status, serial_number, foto
#   Bawah: jumlah, tanggal_perolehan, harga_perolehan, sumber_perolehan, keterangan
#   (relasi dari kiri — atas & bawah & kanan aman)
# ─────────────────────────────────────────────────────────────────────────────

ATTRS_USERS = [
    # Atas — 5 atribut tersebar
    ("id",        UX-160, UY-145, True),
    ("name",      UX-60,  UY-165, False),
    ("email",     UX+50,  UY-165, False),
    ("password",  UX+170, UY-145, False),
    ("role",      UX+200, UY-75,  False),
    # Kiri bawah
    ("is_active", UX-190, UY+20,  False),
]

ATTRS_LOG = [
    # Atas — 5 atribut
    ("id",         LX-130, LY-145, True),
    ("aktivitas",  LX-10,  LY-165, False),
    ("keterangan", LX+120, LY-145, False),
    ("ip_address", LX+240, LY-90,  False),
    ("user_agent", LX+240, LY+20,  False),
]

ATTRS_BARANG = [
    # Atas
    ("kode_barang", BX-150, BY-145, True),
    ("nama_barang", BX-10,  BY-165, False),
    ("kategori",    BX+120, BY-140, False),
    # Bawah
    ("status",      BX-120, BY+140, False),
    ("keterangan",  BX+30,  BY+155, False),
]

ATTRS_RUANGAN = [
    # Atas
    ("id",         RX-110, RY-150, True),
    ("nama",       RX+20,  RY-170, False),
    ("lantai",     RX+140, RY-145, False),
    # Bawah — keterangan di bawah, tidak ke kiri (ada diamond memiliki)
    ("keterangan", RX+20,  RY+155, False),
]

ATTRS_ASET = [
    # Atas — 5 atribut di kanan (relasi membuat datang dari kiri-atas)
    ("kode_aset",         AX-130, AY-150, True),
    ("kondisi",           AX+10,  AY-170, False),
    ("status",            AX+140, AY-150, False),
    ("serial_number",     AX+260, AY-110, False),
    ("foto",              AX+290, AY-30,  False),
    # Bawah — 5 atribut tersebar
    ("jumlah",            AX-260, AY+120, False),
    ("tanggal_perolehan", AX-120, AY+160, False),
    ("harga_perolehan",   AX+30,  AY+170, False),
    ("sumber_perolehan",  AX+185, AY+155, False),
    ("keterangan",        AX+290, AY+80,  False),
]

ALL_ATTRS = ATTRS_USERS+ATTRS_LOG+ATTRS_BARANG+ATTRS_RUANGAN+ATTRS_ASET

# ─────────────────────────────────────────────────────────────────────────────
# CANVAS SIZE — auto dari bounding box
# ─────────────────────────────────────────────────────────────────────────────
PAD=60  # padding besar agar semua elemen masuk
min_x=min_y=9999; max_x=max_y=0

def expand(x0,y0,x1,y1):
    global min_x,min_y,max_x,max_y
    min_x=min(min_x,x0); min_y=min(min_y,y0)
    max_x=max(max_x,x1); max_y=max(max_y,y1)

for cx,cy in [(UX,UY),(BX,BY),(RX,RY),(AX,AY)]:
    expand(cx-EW//2,cy-EH//2,cx+EW//2,cy+EH//2)
expand(LX-80,LY-EH//2,LX+80,LY+EH//2)
for cx,cy,dw,dh in [(DC_X,DC_Y,DW,DH),(DM_X,DM_Y,DW,DH),
                     (DP_X,DP_Y,DW,DH),(DN_X,DN_Y,110,DH)]:
    expand(cx-dw//2,cy-dh//2,cx+dw//2,cy+dh//2)
for lbl,ax,ay,pk in ALL_ATTRS:
    rx,ry=ell_rx_ry(lbl,pk)
    expand(ax-rx,ay-ry,ax+rx,ay+ry)

OX=PAD-min_x; OY=PAD+30-min_y
W=max_x-min_x+PAD*2; H=max_y-min_y+PAD*2+30

def o(x,y): return x+OX, y+OY

# ─────────────────────────────────────────────────────────────────────────────
# DRAW
# ─────────────────────────────────────────────────────────────────────────────
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)

def ln(x1,y1,x2,y2): d.line([(x1,y1),(x2,y2)],fill=BLACK,width=1)

def draw_entity(cx,cy,lbl,ew=EW,eh=EH):
    cx,cy=o(cx,cy)
    d.rectangle([cx-ew//2,cy-eh//2,cx+ew//2,cy+eh//2],fill=WHITE,outline=BLACK,width=3)
    bb=FB.getbbox(lbl); tw=bb[2]-bb[0]; th=bb[3]-bb[1]
    d.text((cx-tw//2,cy-th//2),lbl,font=FB,fill=BLACK)

def draw_attr(cx,cy,lbl,pk=False):
    cx,cy=o(cx,cy); font=FNB if pk else FN
    rx,ry=ell_rx_ry(lbl,pk)
    d.ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=WHITE,outline=BLACK,width=1)
    bb=font.getbbox(lbl); tw=bb[2]-bb[0]; th=bb[3]-bb[1]
    d.text((cx-tw//2,cy-th//2),lbl,font=font,fill=BLACK)
    if pk: d.line([(cx-tw//2,cy+th//2+1),(cx+tw//2,cy+th//2+1)],fill=BLACK,width=1)

def draw_diamond(cx,cy,lbl,dw=DW,dh=DH):
    cx,cy=o(cx,cy)
    pts=[(cx,cy-dh//2),(cx+dw//2,cy),(cx,cy+dh//2),(cx-dw//2,cy)]
    d.polygon(pts,fill=WHITE,outline=BLACK,width=1)
    bb=FN.getbbox(lbl); tw=bb[2]-bb[0]; th=bb[3]-bb[1]
    d.text((cx-tw//2,cy-th//2),lbl,font=FN,fill=BLACK)

def rel_line(e1x,e1y,ew1,eh1, dx,dy,dw,dh, e2x,e2y,ew2,eh2, c1="", c2="", off1=13, off2=13):
    """Garis relasi tanpa arrowhead — ERD Chen standar.
    c1 = kardinalitas dekat entity1, c2 = kardinalitas dekat entity2."""
    e1o=o(e1x,e1y); do=o(dx,dy); e2o=o(e2x,e2y)
    # entity1 → diamond
    p1=ep_rect(*e1o,ew1,eh1,*do); p2=ep_ell(*do,dw//2,dh//2,*e1o)
    ln(*p1,*p2)
    if c1:
        ang=math.atan2(p2[1]-p1[1],p2[0]-p1[0])
        lx=p1[0]+int(math.cos(ang)*24); ly=p1[1]+int(math.sin(ang)*24)
        ox=int(-math.sin(ang)*off1); oy=int(math.cos(ang)*off1)
        bb=FS.getbbox(c1); tw=bb[2]-bb[0]
        d.text((lx-tw//2+ox, ly+oy-FS.size//2), c1, font=FS, fill=BLACK)
    # diamond → entity2
    p3=ep_ell(*do,dw//2,dh//2,*e2o); p4=ep_rect(*e2o,ew2,eh2,*do)
    ln(*p3,*p4)
    if c2:
        ang2=math.atan2(p4[1]-p3[1],p4[0]-p3[0])
        lx2=p4[0]-int(math.cos(ang2)*24); ly2=p4[1]-int(math.sin(ang2)*24)
        ox2=int(-math.sin(ang2)*off2); oy2=int(math.cos(ang2)*off2)
        bb2=FS.getbbox(c2); tw2=bb2[2]-bb2[0]
        d.text((lx2-tw2//2+ox2, ly2+oy2-FS.size//2), c2, font=FS, fill=BLACK)

def attr_conn(ecx,ecy,ew,eh, acx,acy,lbl,pk=False):
    eo=o(ecx,ecy); ao=o(acx,acy)
    rx,ry=ell_rx_ry(lbl,pk)
    p1=ep_rect(*eo,ew,eh,*ao); p2=ep_ell(*ao,rx,ry,*eo)
    ln(*p1,*p2)

# ── 1. Relation lines — garis polos, kardinalitas 1 dan M ────────────────────
rel_line(UX,UY,EW,EH,  DC_X,DC_Y,DW,DH,  LX,LY,160,EH,  "1","M")
rel_line(UX,UY,EW,EH,  DM_X,DM_Y,DW,DH,  AX,AY,EW,EH,   "1","M", off2=20)
rel_line(BX,BY,EW,EH,  DP_X,DP_Y,DW,DH,  AX,AY,EW,EH,   "1","M")
rel_line(RX,RY,EW,EH,  DN_X,DN_Y,110,DH, AX,AY,EW,EH,   "1","M", off2=-13)

# ── 2. Attribute lines ────────────────────────────────────────────────────────
for lbl,ax,ay,pk in ATTRS_USERS:   attr_conn(UX,UY,EW,EH,   ax,ay,lbl,pk)
for lbl,ax,ay,pk in ATTRS_LOG:     attr_conn(LX,LY,160,EH,  ax,ay,lbl,pk)
for lbl,ax,ay,pk in ATTRS_BARANG:  attr_conn(BX,BY,EW,EH,   ax,ay,lbl,pk)
for lbl,ax,ay,pk in ATTRS_RUANGAN: attr_conn(RX,RY,EW,EH,   ax,ay,lbl,pk)
for lbl,ax,ay,pk in ATTRS_ASET:    attr_conn(AX,AY,EW,EH,   ax,ay,lbl,pk)

# ── 3. Attribute ellipses ─────────────────────────────────────────────────────
for lbl,ax,ay,pk in ALL_ATTRS: draw_attr(ax,ay,lbl,pk)

# ── 4. Entities & diamonds on top ────────────────────────────────────────────
draw_entity(UX,UY,"users")
draw_entity(LX,LY,"log_aktivitas",ew=160)
draw_entity(BX,BY,"barang")
draw_entity(RX,RY,"ruangan")
draw_entity(AX,AY,"aset")
draw_diamond(DC_X,DC_Y,"mencatat")
draw_diamond(DM_X,DM_Y,"membuat")
draw_diamond(DP_X,DP_Y,"memiliki")
draw_diamond(DN_X,DN_Y,"menampung",dw=110)

# ── 5. Border + title ─────────────────────────────────────────────────────────
# Border = seluruh canvas minus 4px margin
d.rectangle([4,4,W-4,H-4],outline=BLACK,width=2)
tag="ERD — Sistem Informasi Manajemen Aset SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([4,4,4+tw+10,4+24],fill=BG,outline=BLACK,width=1)
d.text((8,7),tag,font=FT,fill=BLACK)

path=f"{OUT}/ERD_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"ERD_SimAset.png  ({W}x{H})")
