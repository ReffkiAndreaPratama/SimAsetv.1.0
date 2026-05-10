"""
Use Case Diagram — layout persis seperti foto contoh.
Login di tengah, UC menyebar melingkar, extend di dekat UC masing-masing.
Target ukuran: ~1200x900 (mendekati persegi/A4 landscape).
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

def draw_conn(d,x1,y1,x2,y2,lbl="",dash=True):
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
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(255,255,204),outline=BLACK,width=1)
    d.line([(cx,cy+r),(cx,cy+r+28)],fill=BLACK,width=1)
    d.line([(cx-20,cy+r+11),(cx+20,cy+r+11)],fill=BLACK,width=1)
    d.line([(cx,cy+r+28),(cx-15,cy+r+48)],fill=BLACK,width=1)
    d.line([(cx,cy+r+28),(cx+15,cy+r+48)],fill=BLACK,width=1)
    bb=FB.getbbox(lbl); tw=bb[2]-bb[0]
    d.text((cx-tw//2,cy+r+52),lbl,font=FB,fill=BLACK)

def actor_waist(cx,cy):
    return cx, cy+12+14  # waist = head_r + body_mid

# ─────────────────────────────────────────────────────────────────────────────
# CANVAS — target ~1200x900
# ─────────────────────────────────────────────────────────────────────────────
W, H = 1200, 920
img = Image.new("RGB",(W,H),BG)
d   = ImageDraw.Draw(img)

# border + title
d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([8,8,8+tw+10,8+22],fill=BG,outline=BLACK,width=1)
d.text((12,10),tag,font=FT,fill=BLACK)

# system boundary
d.rectangle([90,30,W-90,H-20],fill=(255,255,252),outline=BLACK,width=1)

# ─────────────────────────────────────────────────────────────────────────────
# POSITIONS — Login di tengah, UC menyebar
# ─────────────────────────────────────────────────────────────────────────────
LX, LY = W//2, H//2 + 20   # Login center

# Semua posisi (cx, cy) untuk main UC
# Disusun melingkar di sekitar Login
# Atas: Kelola Aset, Kelola Barang, Kelola Ruangan
# Kiri: Kelola Pengguna, Log Aktivitas
# Kanan: QR Code, Import Data
# Bawah: Maintenance, Export Data

POS = {
    # Atas kiri
    "aset":        (LX-320, LY-240),
    # Atas tengah
    "barang":      (LX,     LY-260),
    # Atas kanan
    "ruangan":     (LX+300, LY-220),
    # Kiri atas
    "pengguna":    (LX-380, LY-80),
    # Kiri bawah
    "logaktivitas":(LX-360, LY+100),
    # Kanan atas
    "qr":          (LX+360, LY-80),
    # Kanan bawah
    "import":      (LX+340, LY+100),
    # Bawah kiri
    "maintenance": (LX-200, LY+240),
    # Bawah kanan
    "export":      (LX+180, LY+250),
}

# Extend items — (parent_key, [labels], direction_angle_deg)
# angle: arah extend dari main UC (0=kanan, 90=bawah, 180=kiri, 270=atas)
EXTENDS = {
    "aset":        (["Tambah Aset","Edit Aset","Hapus Aset"],        "left-up"),
    "barang":      (["Tambah Barang","Edit Barang","Hapus Barang"],   "up"),
    "ruangan":     (["Tambah Ruangan","Edit Ruangan","Edit Ruangan"], "right-up"),
    "pengguna":    (["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"], "left"),
    "qr":          (["Scan QR","Generate QR","Cetak QR"],             "right"),
    "import":      (["Import Aset","Import Barang"],                  "right"),
    "export":      (["Export PDF","Export Excel"],                    "down"),
    "maintenance": (["Set Maintenance","Selesaikan\nMaintenance"],    "down"),
    "logaktivitas":([], ""),
}

# Fix: hapus duplikat ruangan
EXTENDS["ruangan"] = (["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"], "right-up")

# ─────────────────────────────────────────────────────────────────────────────
# COMPUTE EXTEND POSITIONS
# ─────────────────────────────────────────────────────────────────────────────
def ext_positions(pcx, pcy, items, direction):
    """Place extend items in a cluster around parent, in given direction."""
    if not items: return {}
    n = len(items)
    result = {}
    # base offset from parent
    offsets = {
        "up":       (0, -1),
        "down":     (0,  1),
        "left":     (-1, 0),
        "right":    (1,  0),
        "left-up":  (-0.7, -0.7),
        "right-up": (0.7, -0.7),
        "left-down":(-0.7, 0.7),
        "right-down":(0.7, 0.7),
    }
    ox, oy = offsets.get(direction, (0,-1))
    dist = 90  # distance from parent to extend cluster center
    # cluster center
    ccx = pcx + int(ox * dist)
    ccy = pcy + int(oy * dist)
    # spread items perpendicular to direction
    perp_x, perp_y = -oy, ox  # perpendicular
    spread = 70
    if n == 1:
        result[items[0]] = (ccx, ccy)
    elif n == 2:
        for i, lbl in enumerate(items):
            result[lbl] = (
                ccx + int(perp_x * spread * (i - 0.5)),
                ccy + int(perp_y * spread * (i - 0.5))
            )
    else:
        for i, lbl in enumerate(items):
            t = (i - (n-1)/2) / max(1, n-1)
            result[lbl] = (
                ccx + int(perp_x * spread * t * (n-1)),
                ccy + int(perp_y * spread * t * (n-1))
            )
    return result

all_ext_pos = {}
for key, (items, direction) in EXTENDS.items():
    if key in POS and items:
        pcx, pcy = POS[key]
        all_ext_pos.update(ext_positions(pcx, pcy, items, direction))

# ─────────────────────────────────────────────────────────────────────────────
# DRAW — lines first, ellipses on top
# ─────────────────────────────────────────────────────────────────────────────

# 1. <<include>> lines: main UC → Login
for key, (pcx, pcy) in POS.items():
    mrx, mry = ell_r(
        {"aset":"Manajemen Aset","barang":"Manajemen Barang",
         "ruangan":"Manajemen Ruangan","pengguna":"Kelola Pengguna",
         "logaktivitas":"Log Aktivitas","qr":"QR Code",
         "import":"Import Data","maintenance":"Maintenance",
         "export":"Export Data"}.get(key, key), FB)
    lrx, lry = ell_r("Login", FB)
    x1,y1 = ep(pcx,pcy,mrx,mry,LX,LY)
    x2,y2 = ep(LX,LY,lrx,lry,pcx,pcy)
    draw_conn(d,x1,y1,x2,y2,"<<include>>",dash=True)

# 2. <<extend>> lines: extend → main UC
for key, (items, direction) in EXTENDS.items():
    if key not in POS or not items: continue
    pcx, pcy = POS[key]
    lbl_main = {"aset":"Manajemen Aset","barang":"Manajemen Barang",
                "ruangan":"Manajemen Ruangan","pengguna":"Kelola Pengguna",
                "qr":"QR Code","import":"Import Data",
                "maintenance":"Maintenance","export":"Export Data"}.get(key,key)
    prx,pry = ell_r(lbl_main,FB)
    for lbl in items:
        if lbl not in all_ext_pos: continue
        ecx,ecy = all_ext_pos[lbl]
        erx,ery = ell_r(lbl,FS)
        x1,y1=ep(ecx,ecy,erx,ery,pcx,pcy)
        x2,y2=ep(pcx,pcy,prx,pry,ecx,ecy)
        draw_conn(d,x1,y1,x2,y2,"<<extend>>",dash=True)

# 3. Actor lines
ADMIN_X, ADMIN_Y = 50, LY
STAFF_X, STAFF_Y = W-50, LY
aw_admin_x, aw_admin_y = actor_waist(ADMIN_X, ADMIN_Y)
aw_staff_x, aw_staff_y = actor_waist(STAFF_X, STAFF_Y)

admin_keys = list(POS.keys())
staff_keys = [k for k in POS if k not in ("pengguna","logaktivitas")]

labels_map = {
    "aset":"Manajemen Aset","barang":"Manajemen Barang",
    "ruangan":"Manajemen Ruangan","pengguna":"Kelola Pengguna",
    "logaktivitas":"Log Aktivitas","qr":"QR Code",
    "import":"Import Data","maintenance":"Maintenance","export":"Export Data"
}

for k in admin_keys:
    pcx,pcy=POS[k]; lbl=labels_map.get(k,k)
    rx,ry=ell_r(lbl,FB)
    ex,ey=ep(pcx,pcy,rx,ry,aw_admin_x,aw_admin_y)
    d.line([(aw_admin_x,aw_admin_y),(ex,ey)],fill=BLACK,width=1)

for k in staff_keys:
    pcx,pcy=POS[k]; lbl=labels_map.get(k,k)
    rx,ry=ell_r(lbl,FB)
    ex,ey=ep(pcx,pcy,rx,ry,aw_staff_x,aw_staff_y)
    d.line([(aw_staff_x,aw_staff_y),(ex,ey)],fill=BLACK,width=1)

# 4. Draw all ellipses ON TOP
# Main UCs
for key,(pcx,pcy) in POS.items():
    lbl=labels_map.get(key,key)
    draw_ell(d,pcx,pcy,lbl,FB)

# Extend items
for lbl,(ecx,ecy) in all_ext_pos.items():
    draw_ell(d,ecx,ecy,lbl,FS)

# Login
draw_ell(d,LX,LY,"Login",FB)

# 5. Actors ON TOP
actor(d,ADMIN_X,ADMIN_Y,"Admin")
actor(d,STAFF_X,STAFF_Y,"Staff")

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
