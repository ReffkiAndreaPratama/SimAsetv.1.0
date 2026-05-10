"""
Use Case Diagram — grid layout presisi, tidak ada overlap.
Analisis foto: UC disusun dalam grid 3 kolom x 3 baris.
Extend items di atas/bawah UC, tersebar horizontal.
Semua posisi dihitung dari grid — tidak ada yang tumpang tindih.
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

def conn(d,x1,y1,x2,y2,lbl="",dash=True):
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

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
W, H = 1200, 920

# Grid: 5 kolom UC utama, 3 baris (atas, tengah=Login, bawah)
# Kolom x positions (5 kolom UC + Login di tengah)
PAD_L = 130   # left padding (untuk aktor Admin)
PAD_R = 130   # right padding (untuk aktor Staff)
INNER_W = W - PAD_L - PAD_R  # 940px

# 5 kolom UC utama, tersebar merata
N_COLS = 5
COL_W = INNER_W // N_COLS  # ~188px per kolom
col_x = [PAD_L + COL_W*i + COL_W//2 for i in range(N_COLS)]
# col_x[0..4] = x center masing-masing kolom

# 3 baris: atas, tengah (Login), bawah
ROW_TOP    = 200   # y center baris atas (UC utama)
ROW_MID    = 460   # y center Login
ROW_BOT    = 720   # y center baris bawah (UC utama)

# Extend items: 80px di atas/bawah UC utama
EXT_ABOVE  = 90    # jarak extend di atas UC
EXT_BELOW  = 90    # jarak extend di bawah UC

# ─────────────────────────────────────────────────────────────────────────────
# DATA — UC utama dengan posisi grid
# ─────────────────────────────────────────────────────────────────────────────
# Format: (key, label, col_idx, row, admin_only, extends, ext_dir)
# row: "top" atau "bot"
# ext_dir: "above" atau "below"

UCS = [
    # Baris ATAS — 5 UC di 5 kolom
    ("pengguna",    "Kelola Pengguna",   0, "top", True,
     ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"], "above"),

    ("aset",        "Kelola Aset",       1, "top", False,
     ["Tambah Aset","Edit Aset","Hapus Aset"], "above"),

    ("barang",      "Kelola Barang",     2, "top", False,
     ["Tambah Barang","Edit Barang","Hapus Barang"], "above"),

    ("ruangan",     "Kelola Ruangan",    3, "top", False,
     ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"], "above"),

    ("qr",          "QR Code",           4, "top", False,
     ["Scan QR","Generate QR","Cetak QR"], "above"),

    # Baris BAWAH — 4 UC (kolom 0,1,3,4 — kolom 2 kosong di bawah Login)
    ("logaktivitas","Log Aktivitas",     0, "bot", True,
     [], "below"),

    ("maintenance", "Maintenance",       1, "bot", False,
     ["Set Maintenance","Selesaikan\nMaintenance"], "below"),

    ("import",      "Import Data",       3, "bot", False,
     ["Import Aset","Import Barang"], "below"),

    ("export",      "Export Data",       4, "bot", False,
     ["Export PDF","Export Excel"], "below"),
]

# ─────────────────────────────────────────────────────────────────────────────
# COMPUTE ALL POSITIONS
# ─────────────────────────────────────────────────────────────────────────────
all_pos = {}   # key/lbl → (cx, cy, rx, ry)

for key,lbl,col,row,admin_only,extends,ext_dir in UCS:
    cx = col_x[col]
    cy = ROW_TOP if row=="top" else ROW_BOT
    rx,ry = ell_r(lbl,FB)
    all_pos[key] = (cx,cy,rx,ry)

    if not extends: continue

    # Place extend items in a horizontal row above/below UC
    n = len(extends)
    esz = [(e, *ell_r(e,FS)) for e in extends]
    max_erx = max(r for _,r,_ in esz)
    max_ery = max(r for _,_,r in esz)
    gap = 12  # gap between extend ellipses

    # total width of extend row
    total_w = sum(erx*2 for _,erx,_ in esz) + gap*(n-1)
    start_x = cx - total_w//2

    ey = cy - ry - EXT_ABOVE - max_ery if ext_dir=="above" else cy + ry + EXT_BELOW + max_ery

    x = start_x
    for e,erx,ery in esz:
        ecx = x + erx
        all_pos[e] = (ecx, ey, erx, ery)
        x += erx*2 + gap

# Login
lrx,lry = ell_r("Login",FB)
all_pos["login"] = (W//2, ROW_MID, lrx, lry)

# ─────────────────────────────────────────────────────────────────────────────
# DRAW
# ─────────────────────────────────────────────────────────────────────────────
img = Image.new("RGB",(W,H),BG)
d   = ImageDraw.Draw(img)

# border + title
d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([8,8,8+tw+10,8+22],fill=BG,outline=BLACK,width=1)
d.text((12,10),tag,font=FT,fill=BLACK)

# system boundary
d.rectangle([PAD_L-20,30,W-PAD_R+20,H-20],fill=(255,255,252),outline=BLACK,width=1)

LX,LY,LRX,LRY = all_pos["login"]

# ── 1. <<include>> lines ──────────────────────────────────────────────────────
for key,lbl,col,row,admin_only,extends,ext_dir in UCS:
    cx,cy,rx,ry = all_pos[key]
    x1,y1 = ep(cx,cy,rx,ry,LX,LY)
    x2,y2 = ep(LX,LY,LRX,LRY,cx,cy)
    conn(d,x1,y1,x2,y2,"<<include>>",dash=True)

# ── 2. <<extend>> lines ───────────────────────────────────────────────────────
for key,lbl,col,row,admin_only,extends,ext_dir in UCS:
    if not extends: continue
    pcx,pcy,prx,pry = all_pos[key]
    for e in extends:
        if e not in all_pos: continue
        ecx,ecy,erx,ery = all_pos[e]
        x1,y1 = ep(ecx,ecy,erx,ery,pcx,pcy)
        x2,y2 = ep(pcx,pcy,prx,pry,ecx,ecy)
        conn(d,x1,y1,x2,y2,"<<extend>>",dash=True)

# ── 3. Actor lines ────────────────────────────────────────────────────────────
ADMIN_X, ADMIN_Y = 55, ROW_MID
STAFF_X, STAFF_Y = W-55, ROW_MID
# waist point
aw_ax, aw_ay = ADMIN_X, ADMIN_Y+12+14
aw_sx, aw_sy = STAFF_X, STAFF_Y+12+14

for key,lbl,col,row,admin_only,extends,ext_dir in UCS:
    cx,cy,rx,ry = all_pos[key]
    # Admin → semua
    ex,ey = ep(cx,cy,rx,ry,aw_ax,aw_ay)
    d.line([(aw_ax,aw_ay),(ex,ey)],fill=BLACK,width=1)
    # Staff → bukan admin_only
    if not admin_only:
        ex,ey = ep(cx,cy,rx,ry,aw_sx,aw_sy)
        d.line([(aw_sx,aw_sy),(ex,ey)],fill=BLACK,width=1)

# ── 4. All ellipses ON TOP ────────────────────────────────────────────────────
for key,lbl,col,row,admin_only,extends,ext_dir in UCS:
    cx,cy,rx,ry = all_pos[key]
    draw_ell(d,cx,cy,lbl,FB)
    for e in extends:
        if e in all_pos:
            ecx,ecy,erx,ery = all_pos[e]
            draw_ell(d,ecx,ecy,e,FS)

draw_ell(d,LX,LY,"Login",FB)

# ── 5. Actors ON TOP ──────────────────────────────────────────────────────────
actor(d,ADMIN_X,ADMIN_Y,"Admin")
actor(d,STAFF_X,STAFF_Y,"Staff")

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
