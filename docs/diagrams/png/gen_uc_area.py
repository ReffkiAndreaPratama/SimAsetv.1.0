"""
Use Case Diagram — layout area/grup per fitur.
Setiap fitur punya kotak area sendiri dengan use case utama + extend di dalamnya.
Tidak ada tumpang tindih.
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

FB=F(11); FS=F(10); FT=F(11,True); FSM=F(9); FG=F(9,True)
BG=(255,255,255); BOXF=(255,255,204); BLACK=(0,0,0); GRAY=(110,110,110)
AREA_BD=(160,160,140); AREA_BG=(252,252,248)

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
# AREA BUILDER
# Setiap area = kotak dengan label grup + use case utama + extend items
# ─────────────────────────────────────────────────────────────────────────────
class Area:
    """
    Represents a feature group area.
    main_uc: (key, label) — use case utama
    extends: [label, ...] — extend items
    layout: "row" = extends di kanan main, "col" = extends di bawah main
    """
    IPAD=10   # inner padding
    ELL_GAP=14 # gap between ellipses

    def __init__(self, group_label, main_key, main_label, extends, layout="row"):
        self.group_label=group_label
        self.main_key=main_key
        self.main_label=main_label
        self.extends=extends
        self.layout=layout
        self._compute()

    def _compute(self):
        IP=self.IPAD; EG=self.ELL_GAP
        # main ellipse size
        self.mrx,self.mry=ell_r(self.main_label,FB)
        # extend ellipse sizes
        self.esz=[(lbl,*ell_r(lbl,FS,px=12,py=8)) for lbl in self.extends]

        if self.layout=="row":
            # main on left, extends on right in a column
            n=len(self.extends)
            if n==0:
                self.w=self.mrx*2+IP*2
                self.h=self.mry*2+IP*2+16
            else:
                max_erx=max(rx for _,rx,ry in self.esz)
                max_ery=max(ry for _,rx,ry in self.esz)
                ext_col_h=n*(max_ery*2)+(n-1)*EG
                self.w=IP+self.mrx*2+EG+max_erx*2+IP
                self.h=max(self.mry*2,ext_col_h)+IP*2+16
        else:
            # main on top, extends in a row below
            n=len(self.extends)
            if n==0:
                self.w=self.mrx*2+IP*2
                self.h=self.mry*2+IP*2+16
            else:
                max_erx=max(rx for _,rx,ry in self.esz)
                max_ery=max(ry for _,rx,ry in self.esz)
                ext_row_w=n*(max_erx*2)+(n-1)*EG
                self.w=max(self.mrx*2,ext_row_w)+IP*2
                self.h=IP*2+16+self.mry*2+EG+max_ery*2

    def draw(self, d, x0, y0):
        """Draw area at top-left (x0,y0). Returns dict of drawn positions."""
        IP=self.IPAD; EG=self.ELL_GAP
        x1=x0+self.w; y1=y0+self.h

        # group label only (no box)
        bb=FG.getbbox(self.group_label); tw=bb[2]-bb[0]
        d.text((x0+4,y0+2),self.group_label,font=FG,fill=GRAY)

        drawn={}
        content_y0=y0+16  # below group label

        if self.layout=="row":
            n=len(self.extends)
            if n==0:
                cx=x0+IP+self.mrx; cy=(content_y0+y1)//2
                draw_ell(d,cx,cy,self.main_label,FB)
                drawn[self.main_key]=(cx,cy,self.mrx,self.mry)
            else:
                max_erx=max(rx for _,rx,ry in self.esz)
                max_ery=max(ry for _,rx,ry in self.esz)
                ext_col_h=n*(max_ery*2)+(n-1)*EG
                # main uc: vertically centered
                cx_m=x0+IP+self.mrx
                cy_m=(content_y0+y1)//2
                draw_ell(d,cx_m,cy_m,self.main_label,FB)
                drawn[self.main_key]=(cx_m,cy_m,self.mrx,self.mry)
                # extends: column on right
                cx_e=x0+IP+self.mrx*2+EG+max_erx
                start_y=cy_m-ext_col_h//2
                for i,(lbl,erx,ery) in enumerate(self.esz):
                    ey=start_y+i*(ery*2+EG)+ery
                    draw_ell(d,cx_e,ey,lbl,FS)
                    drawn[lbl]=(cx_e,ey,erx,ery)
                    # extend arrow
                    conn(d,(cx_e,ey),(erx,ery),(cx_m,cy_m),(self.mrx,self.mry),
                         "<<extend>>",dash=True)
        else:
            n=len(self.extends)
            max_erx=max((rx for _,rx,ry in self.esz),default=0)
            max_ery=max((ry for _,rx,ry in self.esz),default=0)
            ext_row_w=n*(max_erx*2)+(n-1)*EG if n else 0
            # main uc: top center
            cx_m=x0+self.w//2; cy_m=content_y0+IP+self.mry
            draw_ell(d,cx_m,cy_m,self.main_label,FB)
            drawn[self.main_key]=(cx_m,cy_m,self.mrx,self.mry)
            if n:
                # extends: row below
                start_x=x0+(self.w-ext_row_w)//2+max_erx
                ey=cy_m+self.mry+EG+max_ery
                for i,(lbl,erx,ery) in enumerate(self.esz):
                    ex=start_x+i*(erx*2+EG)
                    draw_ell(d,ex,ey,lbl,FS)
                    drawn[lbl]=(ex,ey,erx,ery)
                    conn(d,(ex,ey),(erx,ery),(cx_m,cy_m),(self.mrx,self.mry),
                         "<<extend>>",dash=True)

        return drawn

# ─────────────────────────────────────────────────────────────────────────────
# DEFINE ALL AREAS
# ─────────────────────────────────────────────────────────────────────────────
areas = [
    Area("Autentikasi",      "login",       "Login",
         [], "row"),

    Area("Manajemen Aset",   "aset",        "Manajemen Aset",
         ["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"], "row"),

    Area("Manajemen Barang", "barang",      "Manajemen Barang",
         ["Tambah Barang","Edit Barang","Hapus Barang"], "row"),

    Area("Manajemen Ruangan","ruangan",     "Manajemen Ruangan",
         ["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"], "row"),

    Area("QR Code",          "qr",          "QR Code",
         ["Generate QR","Scan QR","Cetak Massal"], "row"),

    Area("Maintenance",      "maintenance", "Maintenance",
         ["Set Maintenance","Selesaikan\nMaintenance"], "row"),

    Area("Import Data",      "import",      "Import Data",
         ["Import Aset","Import Barang","Download Template"], "row"),

    Area("Export & Laporan", "export",      "Export & Laporan",
         ["Export Excel","Export PDF","Laporan Ruangan","Laporan Maintenance"], "row"),

    Area("Dashboard",        "dashboard",   "Dashboard",
         [], "row"),

    Area("Kelola Pengguna\n(Admin Only)", "pengguna", "Kelola Pengguna",
         ["Tambah Pengguna","Edit Pengguna","Hapus Pengguna"], "row"),

    Area("Audit Log\n(Admin Only)",       "auditlog", "Audit Log",
         ["Filter Audit Log"], "row"),
]

# ─────────────────────────────────────────────────────────────────────────────
# GRID LAYOUT — 3 columns
# ─────────────────────────────────────────────────────────────────────────────
# Arrange areas in a 3-column grid
# Col 0: Login, Aset, Barang, Ruangan
# Col 1: QR, Maintenance, Import, Export
# Col 2: Dashboard, Pengguna, Auditlog

GRID = [
    # (area_index, col, row)
    (0,  1, 0),   # Login — center top
    (1,  0, 1),   # Aset
    (2,  0, 2),   # Barang
    (3,  0, 3),   # Ruangan
    (4,  1, 1),   # QR
    (5,  1, 2),   # Maintenance
    (6,  1, 3),   # Import
    (7,  1, 4),   # Export
    (8,  2, 1),   # Dashboard
    (9,  2, 2),   # Pengguna
    (10, 2, 3),   # Auditlog
]

# Compute column widths and row heights
n_cols=3; n_rows=5
col_w=[0]*n_cols; row_h=[0]*n_rows

for ai,col,row in GRID:
    a=areas[ai]
    col_w[col]=max(col_w[col],a.w)
    row_h[row]=max(row_h[row],a.h)

COL_GAP=20; ROW_GAP=16
ACTOR_W=60; ACTOR_GAP=24
PAD=16; TITLE_H=22; BPAD=14

# x positions of columns
col_x=[0]*n_cols
col_x[0]=PAD+ACTOR_W+ACTOR_GAP
col_x[1]=col_x[0]+col_w[0]+COL_GAP
col_x[2]=col_x[1]+col_w[1]+COL_GAP
W_content=col_x[2]+col_w[2]+ACTOR_GAP+ACTOR_W+PAD
W=W_content

# y positions of rows
row_y=[0]*n_rows
row_y[0]=PAD+TITLE_H+BPAD+10
for r in range(1,n_rows):
    row_y[r]=row_y[r-1]+row_h[r-1]+ROW_GAP

H=row_y[n_rows-1]+row_h[n_rows-1]+PAD+20

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
bx0=col_x[0]-8; bx1=col_x[2]+col_w[2]+8
by0=8+TITLE_H+4; by1=H-12
# system boundary only (no area boxes inside)
d.rectangle([bx0,by0,bx1,by1],fill=(255,255,252),outline=BLACK,width=1)

# Draw all areas and collect positions
all_drawn={}  # key/label → (cx,cy,rx,ry)
for ai,col,row in GRID:
    a=areas[ai]
    x0=col_x[col]
    # center area vertically in its row cell
    y0=row_y[row]+(row_h[row]-a.h)//2
    drawn=a.draw(d,x0,y0)
    all_drawn.update(drawn)

# ── Include: all main UCs → Login ─────────────────────────────────────────────
login_uc=all_drawn["login"]
main_keys=["aset","barang","ruangan","qr","maintenance",
           "import","export","dashboard","pengguna","auditlog"]
for k in main_keys:
    if k in all_drawn:
        uc=all_drawn[k]
        conn(d,(uc[0],uc[1]),(uc[2],uc[3]),
               (login_uc[0],login_uc[1]),(login_uc[2],login_uc[3]),
               "<<include>>",dash=True)

# ── Actors ────────────────────────────────────────────────────────────────────
# Actor y = middle of diagram
mid_y=(row_y[1]+row_y[n_rows-1]+row_h[n_rows-1])//2
x_admin=PAD+ACTOR_W//2
x_staff=col_x[2]+col_w[2]+ACTOR_GAP+ACTOR_W//2

actor(d,x_admin,mid_y-20,"Admin")
actor(d,x_staff,mid_y-20,"Staff")

# Admin → all main UCs (left side)
admin_keys=["login","aset","barang","ruangan","qr","maintenance",
            "import","export","dashboard","pengguna","auditlog"]
for k in admin_keys:
    if k in all_drawn:
        uc=all_drawn[k]
        aline(d,x_admin,mid_y-20,uc[0],uc[1],uc[2],uc[3])

# Staff → all except admin-only
staff_keys=["login","aset","barang","ruangan","qr","maintenance",
            "import","export","dashboard"]
for k in staff_keys:
    if k in all_drawn:
        uc=all_drawn[k]
        aline(d,x_staff,mid_y-20,uc[0],uc[1],uc[2],uc[3])

path=f"{OUT}/UC_SimAset.png"
img.save(path,"PNG",dpi=(150,150))
print(f"UC_SimAset.png  ({W}x{H})")
