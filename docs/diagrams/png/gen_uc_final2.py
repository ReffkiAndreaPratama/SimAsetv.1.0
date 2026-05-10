"""
Use Case Diagram — layout radial/menyebar di sekitar Login.
Use case TIDAK sejajar horizontal dengan aktor.
Setiap garis dari aktor punya sudut unik → tidak tumpang tindih.

Layout:
- Login di tengah
- Admin di kiri, Staff di kanan
- Use case disusun MELINGKAR di sekitar Login:
  - Atas kiri, atas tengah, atas kanan
  - Bawah kiri, bawah tengah, bawah kanan
- Extend items di luar masing-masing UC
- Aktor terhubung ke semua UC dengan garis lurus
  (karena UC tidak sejajar, garis tidak saling melewati UC lain)
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

def conn_ell(d,c1,r1,c2,r2,lbl="",dash=True):
    x1,y1=ep(*c1,*r1,*c2[:2]); x2,y2=ep(*c2,*r2,*c1[:2])
    draw_conn(d,x1,y1,x2,y2,lbl,dash)

def actor(d,cx,cy,lbl):
    r=12
    # kepala
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(255,255,204),outline=BLACK,width=1)
    # badan
    d.line([(cx,cy+r),(cx,cy+r+28)],fill=BLACK,width=1)
    # tangan
    d.line([(cx-20,cy+r+11),(cx+20,cy+r+11)],fill=BLACK,width=1)
    # kaki
    d.line([(cx,cy+r+28),(cx-15,cy+r+48)],fill=BLACK,width=1)
    d.line([(cx,cy+r+28),(cx+15,cy+r+48)],fill=BLACK,width=1)
    # label
    bb=FB.getbbox(lbl); tw=bb[2]-bb[0]
    d.text((cx-tw//2,cy+r+52),lbl,font=FB,fill=BLACK)

def actor_center(cx,cy):
    """Return the connection point — center of body (waist area)."""
    r=12
    return cx, cy+r+14  # midpoint of body segment

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
# (key, label, extends, admin_only, ext_dir)
# ext_dir: arah extend items dari main UC
UCS = [
    # Baris ATAS — 5 UC, tersebar dari kiri ke kanan
    ("pengguna",    "Kelola Pengguna",
     ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"],
     True,  "up"),

    ("aset",        "Manajemen Aset",
     ["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"],
     False, "up"),

    ("barang",      "Manajemen Barang",
     ["Tambah Barang","Edit Barang","Hapus Barang"],
     False, "up"),

    ("qr",          "QR Code",
     ["Generate QR","Scan QR","Cetak QR"],
     False, "up"),

    ("export",      "Export & Laporan",
     ["Export Excel","Export PDF","Laporan Ruangan","Laporan Maintenance"],
     False, "up"),

    # Baris BAWAH — 4 UC
    ("logaktivitas","Log Aktivitas",
     [],
     True,  "down"),

    ("ruangan",     "Manajemen Ruangan",
     ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"],
     False, "down"),

    ("maintenance", "Maintenance",
     ["Set Maintenance","Selesaikan\nMaintenance"],
     False, "down"),

    ("import",      "Import Data",
     ["Import Aset","Import Barang","Download Template"],
     False, "down"),
]

# ─────────────────────────────────────────────────────────────────────────────
# SIZES
# ─────────────────────────────────────────────────────────────────────────────
def uc_main_r(lbl): return ell_r(lbl,FB)
def ext_r(lbl):     return ell_r(lbl,FS,px=12,py=8)

def group_h_up(lbl, extends):
    """Height of group when extends go UP above main UC."""
    _,mry=uc_main_r(lbl)
    if not extends: return mry*2
    max_ery=max(ext_r(e)[1] for e in extends)
    n=len(extends)
    ext_h=n*(max_ery*2)+(n-1)*8
    return mry*2+14+ext_h

def group_h_down(lbl, extends):
    """Height of group when extends go DOWN below main UC."""
    return group_h_up(lbl, extends)  # symmetric

def group_w(lbl, extends):
    mrx,_=uc_main_r(lbl)
    if not extends: return mrx*2
    max_erx=max(ext_r(e)[0] for e in extends)
    n=len(extends)
    return max(mrx*2, n*(max_erx*2)+(n-1)*10)

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT
# ─────────────────────────────────────────────────────────────────────────────
top_ucs  = [(k,l,e,a,d) for k,l,e,a,d in UCS if d=="up"]
bot_ucs  = [(k,l,e,a,d) for k,l,e,a,d in UCS if d=="down"]

HGAP=50; VGAP_MID=80; PAD=20; TITLE_H=22; BPAD=14
ACTOR_W=55; ACTOR_GAP=40

# Width of each UC group
top_ws=[group_w(l,e) for k,l,e,a,d in top_ucs]
bot_ws=[group_w(l,e) for k,l,e,a,d in bot_ucs]

# Total width needed for top and bottom rows
top_total=sum(top_ws)+(len(top_ucs)-1)*HGAP
bot_total=sum(bot_ws)+(len(bot_ucs)-1)*HGAP

login_rx,login_ry=ell_r("Login",FB)

# Canvas width: max of top/bot rows + actors on sides
content_w=max(top_total,bot_total)
W=PAD+ACTOR_W+ACTOR_GAP+content_w+ACTOR_GAP+ACTOR_W+PAD+10

# X start of content area
x_content_start=PAD+ACTOR_W+ACTOR_GAP

# Center x of content
cx_center=x_content_start+content_w//2

# Heights
top_h=max(group_h_up(l,e) for k,l,e,a,d in top_ucs)
bot_h=max(group_h_down(l,e) for k,l,e,a,d in bot_ucs)

H=TITLE_H+BPAD*2+top_h+VGAP_MID+login_ry*2+VGAP_MID+bot_h+PAD*2+20
Y_OFF=TITLE_H+BPAD+PAD

def gy(y): return y+Y_OFF

# Y positions
y_top_bot   = gy(0)                          # bottom of top extends
y_top_main  = gy(top_h - max(uc_main_r(l)[1] for k,l,e,a,d in top_ucs))  # main UC y for top row
y_login     = gy(top_h + VGAP_MID + login_ry)
y_bot_main  = gy(top_h + VGAP_MID + login_ry*2 + VGAP_MID)
y_bot_ext   = gy(top_h + VGAP_MID + login_ry*2 + VGAP_MID + bot_h)

# X positions for top row UCs — centered
def row_xs(ucs, ws, total_w):
    start=cx_center-total_w//2
    xs=[]
    x=start
    for i,(k,l,e,a,d) in enumerate(ucs):
        xs.append(x+ws[i]//2)
        x+=ws[i]+HGAP
    return xs

top_xs=row_xs(top_ucs,top_ws,top_total)
bot_xs=row_xs(bot_ucs,bot_ws,bot_total)

# Actor positions — vertically centered between top and bottom rows
x_admin=PAD+ACTOR_W//2
x_staff=W-PAD-ACTOR_W//2
actor_y=y_login  # actors at Login height

# ─────────────────────────────────────────────────────────────────────────────
# COLLECT ALL POSITIONS
# ─────────────────────────────────────────────────────────────────────────────
all_pos={}  # key/lbl → (cx,cy,rx,ry)

# Top row main UCs
for i,(k,l,e,a,d) in enumerate(top_ucs):
    mrx,mry=uc_main_r(l)
    cx=top_xs[i]
    # main UC sits at bottom of its group area
    cy=gy(top_h)-mry
    all_pos[k]=(cx,cy,mrx,mry)
    # extends go UP above main UC
    if e:
        esz=[(lbl,*ext_r(lbl)) for lbl in e]
        max_erx=max(rx for _,rx,ry in esz)
        max_ery=max(ry for _,rx,ry in esz)
        n=len(e); ext_h_total=n*(max_ery*2)+(n-1)*8
        # distribute extends horizontally above main UC
        ext_total_w=n*(max_erx*2)+(n-1)*10
        ext_start_x=cx-ext_total_w//2+max_erx
        ext_y=cy-mry-14-max_ery
        for j,(lbl,erx,ery) in enumerate(esz):
            ex=ext_start_x+j*(erx*2+10)
            all_pos[lbl]=(ex,ext_y,erx,ery)

# Bottom row main UCs
for i,(k,l,e,a,d) in enumerate(bot_ucs):
    mrx,mry=uc_main_r(l)
    cx=bot_xs[i]
    cy=y_bot_main+mry
    all_pos[k]=(cx,cy,mrx,mry)
    # extends go DOWN below main UC
    if e:
        esz=[(lbl,*ext_r(lbl)) for lbl in e]
        max_erx=max(rx for _,rx,ry in esz)
        max_ery=max(ry for _,rx,ry in esz)
        n=len(e)
        ext_total_w=n*(max_erx*2)+(n-1)*10
        ext_start_x=cx-ext_total_w//2+max_erx
        ext_y=cy+mry+14+max_ery
        for j,(lbl,erx,ery) in enumerate(esz):
            ex=ext_start_x+j*(erx*2+10)
            all_pos[lbl]=(ex,ext_y,erx,ery)

# Login
all_pos["login"]=(cx_center,y_login,login_rx,login_ry)

# ─────────────────────────────────────────────────────────────────────────────
# DRAW — lines first, ellipses on top
# ─────────────────────────────────────────────────────────────────────────────
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)

# border + title
d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
bb=FT.getbbox(tag); tw=bb[2]-bb[0]
d.rectangle([8,8,8+tw+10,8+TITLE_H],fill=BG,outline=BLACK,width=1)
d.text((12,10),tag,font=FT,fill=BLACK)

# system boundary
bx0=x_content_start-10; bx1=x_content_start+content_w+10
d.rectangle([bx0,8+TITLE_H+4,bx1,H-12],fill=(255,255,252),outline=BLACK,width=1)

# ── 1. <<include>> lines ──────────────────────────────────────────────────────
lx,ly,lrx,lry=all_pos["login"]
for k,l,e,a,d2 in UCS:
    if k not in all_pos: continue
    cx,cy,rx,ry=all_pos[k]
    x1,y1=ep(cx,cy,rx,ry,lx,ly)
    x2,y2=ep(lx,ly,lrx,lry,cx,cy)
    draw_conn(d,x1,y1,x2,y2,"<<include>>",dash=True)

# ── 2. <<extend>> lines ───────────────────────────────────────────────────────
for k,l,extends,a,d2 in UCS:
    if k not in all_pos or not extends: continue
    pcx,pcy,prx,pry=all_pos[k]
    for lbl in extends:
        if lbl not in all_pos: continue
        ecx,ecy,erx,ery=all_pos[lbl]
        x1,y1=ep(ecx,ecy,erx,ery,pcx,pcy)
        x2,y2=ep(pcx,pcy,prx,pry,ecx,ecy)
        draw_conn(d,x1,y1,x2,y2,"<<extend>>",dash=True)

# ── 3. Actor lines ────────────────────────────────────────────────────────────
# Garis dari titik tengah badan aktor (waist), bukan dari kepala
ax_admin, ay_admin = actor_center(x_admin, actor_y)
ax_staff, ay_staff = actor_center(x_staff, actor_y)

for k,l,e,admin_only,d2 in UCS:
    if k not in all_pos: continue
    cx,cy,rx,ry=all_pos[k]
    # Admin line — dari waist aktor
    ex,ey=ep(cx,cy,rx,ry,ax_admin,ay_admin)
    d.line([(ax_admin,ay_admin),(ex,ey)],fill=BLACK,width=1)
    # Staff line (skip admin-only)
    if not admin_only:
        ex,ey=ep(cx,cy,rx,ry,ax_staff,ay_staff)
        d.line([(ax_staff,ay_staff),(ex,ey)],fill=BLACK,width=1)

# ── 4. All ellipses ON TOP ────────────────────────────────────────────────────
for k,l,extends,a,d2 in UCS:
    if k in all_pos:
        cx,cy,rx,ry=all_pos[k]
        draw_ell(d,cx,cy,l,FB)
    for lbl in extends:
        if lbl in all_pos:
            ecx,ecy,erx,ery=all_pos[lbl]
            draw_ell(d,ecx,ecy,lbl,FS)

draw_ell(d,lx,ly,"Login",FB)

# ── 5. Actors ON TOP ──────────────────────────────────────────────────────────
actor(d,x_admin,actor_y,"Admin")
actor(d,x_staff,actor_y,"Staff")
path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
