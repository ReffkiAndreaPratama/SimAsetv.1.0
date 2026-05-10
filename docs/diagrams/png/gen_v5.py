"""
Activity Diagram v5 — pixel-perfect sesuai foto contoh.

Analisis foto:
- Cross-lane: panah ORTHOGONAL (horizontal lurus, bukan diagonal)
- Return dari Sistem ke Pengguna: panah horizontal ke kiri dengan sudut siku
- Decision "Tidak/Gagal": panah ke KANAN dengan label di samping, tidak loop
- Decision "Ya/Terdaftar": panah ke BAWAH dengan label di samping
- Fork/Join: bar hitam, panah diagonal ke kotak
- Semua panah SOLID
- Garis vertikal pemisah swimlane
- Kotak rounded kuning muda
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

FB=F(12); FS=F(10); FH=F(12,True); FT=F(11,True); FSM=F(9)

BG    = (255,255,255)
SWBG  = (255,255,240)
SWHDR = (255,255,215)
BOXF  = (255,255,204)
BOXBD = (0,0,0)
BLACK = (0,0,0)
GRAY  = (100,100,100)
LGRAY = (180,180,180)

def msz(txt, font):
    lines=txt.split("\n"); lh=font.size+2
    w=max(font.getbbox(ln)[2]-font.getbbox(ln)[0] for ln in lines)
    return w, lh*len(lines)

def tc(d, cx, cy, txt, font, color=BLACK):
    lines=txt.split("\n"); lh=font.size+2
    y=cy-lh*len(lines)//2
    for ln in lines:
        bb=font.getbbox(ln); tw=bb[2]-bb[0]
        d.text((cx-tw//2,y),ln,font=font,fill=color); y+=lh

def arrowhead(d, x2, y2, x1, y1, s=7):
    ang=math.atan2(y2-y1,x2-x1)
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                          int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)

def arr_v(d, x, y1, y2, lbl="", lbl_right=True):
    """Vertical solid arrow."""
    d.line([(x,y1),(x,y2)],fill=BLACK,width=1)
    arrowhead(d,x,y2,x,y1)
    if lbl:
        bb=FS.getbbox(lbl); tw=bb[2]-bb[0]
        ox=6 if lbl_right else -tw-6
        d.text((x+ox,(y1+y2)//2-FS.size//2),lbl,font=FS,fill=GRAY)

def arr_h(d, x1, y, x2, lbl="", lbl_above=True):
    """Horizontal solid arrow."""
    d.line([(x1,y),(x2,y)],fill=BLACK,width=1)
    arrowhead(d,x2,y,x1,y)
    if lbl:
        bb=FS.getbbox(lbl); tw=bb[2]-bb[0]
        dy=-FS.size-2 if lbl_above else 3
        d.text(((x1+x2)//2-tw//2,y+dy),lbl,font=FS,fill=GRAY)

def arr_ortho(d, x1,y1, x2,y2, lbl="", lbl_above=True):
    """
    Orthogonal arrow: go horizontal then vertical (L-shape).
    Used for cross-lane arrows like in the foto.
    """
    # horizontal segment
    d.line([(x1,y1),(x2,y1)],fill=BLACK,width=1)
    # vertical segment
    d.line([(x2,y1),(x2,y2)],fill=BLACK,width=1)
    arrowhead(d,x2,y2,x2,y1)
    if lbl:
        bb=FS.getbbox(lbl); tw=bb[2]-bb[0]
        dy=-FS.size-2 if lbl_above else 3
        d.text(((x1+x2)//2-tw//2,y1+dy),lbl,font=FS,fill=GRAY)

def arr_diag(d, x1,y1, x2,y2):
    """Diagonal solid arrow (for fork fan-out)."""
    d.line([(x1,y1),(x2,y2)],fill=BLACK,width=1)
    arrowhead(d,x2,y2,x1,y1)

def draw_box(d, cx, cy, txt, font, minw=120):
    tw,th=msz(txt,font); w=max(tw+20,minw); h=th+14
    x0,y0=cx-w//2,cy-h//2
    d.rounded_rectangle([x0,y0,x0+w,y0+h],radius=6,fill=BOXF,outline=BOXBD,width=1)
    tc(d,cx,cy,txt,font)
    return w,h

def draw_diamond(d, cx, cy, txt, font):
    tw,th=msz(txt,font); w=tw+44; h=th+28
    pts=[(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
    d.polygon(pts,fill=(255,255,255),outline=BLACK,width=1)
    tc(d,cx,cy,txt,font,GRAY)
    return w//2,h//2

def fbar(d,x0,y,x1): d.rectangle([x0,y-4,x1,y+4],fill=BLACK)
def snode(d,cx,cy,r=9): d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
def enode(d,cx,cy,r=9):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
    d.ellipse([cx-r+3,cy-r+3,cx+r-3,cy+r-3],fill=BG)
    d.ellipse([cx-r+6,cy-r+6,cx+r-6,cy+r-6],fill=BLACK)

# ─── CANVAS BUILDER ──────────────────────────────────────────────────────────
def make_canvas(title, l1, l2, w1, w2, content_h):
    P=14; TH=20; HH=28
    TW=w1+w2+P*2
    TH2=P+TH+HH+content_h+P+16
    img=Image.new("RGB",(TW,TH2),BG)
    d=ImageDraw.Draw(img)

    # outer border
    d.rectangle([P,P,TW-P,TH2-P],outline=BLACK,width=1)

    # title tag
    bb=FT.getbbox(title); tw=bb[2]-bb[0]
    d.rectangle([P,P,P+tw+10,P+TH],fill=BG,outline=BLACK,width=1)
    d.text((P+5,P+3),title,font=FT,fill=BLACK)

    # swimlane backgrounds
    sw_top=P+TH
    cx1=P+w1//2; cx2=P+w1+w2//2
    for i,(w,lbl) in enumerate([(w1,l1),(w2,l2)]):
        x0=P+(w1 if i else 0); x1=x0+w
        if i==0: x0=P
        d.rectangle([x0,sw_top,x0+w,TH2-P],fill=SWBG,outline=BLACK,width=1)
        d.rectangle([x0,sw_top,x0+w,sw_top+HH],fill=SWHDR,outline=BLACK,width=1)
        tc(d,(x0+x0+w)//2,sw_top+HH//2,lbl,FH)

    # vertical divider
    div_x=P+w1
    d.line([(div_x,sw_top),(div_x,TH2-P)],fill=BLACK,width=1)

    y_start=P+TH+HH+14
    return img,d,cx1,cx2,div_x,P,w1,w2,TW,TH2,y_start

def save(img,fname,TW,TH2):
    path=f"{OUT}/{fname}"
    img.save(path,"PNG",dpi=(150,150))
    print(f"  {fname}  ({TW}x{TH2})")

# ═══════════════════════════════════════════════════════════════════════════
# ACT-01  LOGIN  — persis seperti foto
# ═══════════════════════════════════════════════════════════════════════════
def act_login():
    W1,W2=280,360; G=16; AR=20
    # measure content height first
    # items: start, box, cross+box+return, box, cross+box+dec+box+return,
    #        box, cross+box, box, cross+box+return, box, cross, box, return, end
    CH = 9+AR + (28+14+AR) + (28+14+AR) + (28+14+AR) + (28+28+AR) + (28+14+AR) + \
         (28+14+AR) + (28+14+AR) + (28+14+AR) + (28+14+AR) + (28+14+AR) + 18+AR+G
    img,d,C1,C2,DX,P,w1,w2,TW,TH2,y = make_canvas(
        "act  Login & Logout — SimAset","Pengguna","Sistem",W1,W2,900)

    # START
    snode(d,C1,y); arr_v(d,C1,y+9,y+9+AR); y+=9+AR

    # [Pengguna] Login
    bw,bh=draw_box(d,C1,y+bh//2 if False else y+(28+14)//2,"Login",FB,140)
    by=y+(bh)//2
    draw_box(d,C1,by,"Login",FB,140)
    # arrow right to Sistem
    arr_h(d,C1+70,by,C2-90)
    # [Sistem] Menampilkan Login
    draw_box(d,C2,by,"Menampilkan Login",FB,180)
    # return arrow left
    arr_h(d,C2-90,by+bh//2+8,C1+70,lbl_above=False)
    arr_v(d,C1,y+bh,y+bh+AR); y+=bh+AR

    # [Pengguna] Username dan Password
    bw2,bh2=msz("Username dan Password",FB); bh2+=14; bw2=max(bw2+20,160)
    draw_box(d,C1,y+bh2//2,"Username dan Password",FB,160)
    arr_h(d,C1+bw2//2,y+bh2//2,C2-90)
    # [Sistem] Autentikasi
    draw_box(d,C2,y+bh2//2,"Autentikasi",FB,150)
    arr_v(d,C2,y+bh2,y+bh2+AR); y+=bh2+AR

    # [Sistem] Decision: Akun terdaftar?
    hw,hh=draw_diamond(d,C2,y+hh if False else y+30,"Akun\nterdaftar?",FS)
    hw,hh=draw_diamond(d,C2,y+30,"Akun\nterdaftar?",FS)
    cy_d=y+30
    # "Akun Tidak Terdaftar" → right
    arr_h(d,C2+hw,cy_d,C2+hw+80,"Akun Tidak\nTerdaftar")
    # "Akun Terdaftar" → down
    arr_v(d,C2,cy_d+hh,cy_d+hh+AR,"Akun Terdaftar",lbl_right=True)
    y=cy_d+hh+AR

    # [Sistem] Menampilkan Dashboard
    bw3,bh3=msz("Menampilkan Dashboard",FB); bh3+=14; bw3=max(bw3+20,200)
    draw_box(d,C2,y+bh3//2,"Menampilkan Dashboard",FB,200)
    # return arrow to Pengguna
    arr_h(d,C2-bw3//2,y+bh3//2,C1+90)
    # [Pengguna] Pilih Menu
    draw_box(d,C1,y+bh3//2,"Pilih Menu Aset",FB,160)
    arr_v(d,C1,y+bh3,y+bh3+AR)
    # [Pengguna] arrow right to Sistem
    arr_h(d,C1+80,y+bh3//2+bh3//2+AR//2,C2-bw3//2,lbl_above=False)
    y+=bh3+AR

    # [Sistem] Menampilkan Halaman Aset
    bw4,bh4=msz("Menampilkan Halaman Aset",FB); bh4+=14; bw4=max(bw4+20,220)
    draw_box(d,C2,y+bh4//2,"Menampilkan Halaman Aset",FB,220)
    arr_v(d,C2,y+bh4,y+bh4+AR); y+=bh4+AR

    # FORK in Pengguna lane
    items=["Tambah\nAset","Lihat\nAset","Edit\nAset","Ekspor\nAset","Hapus\nAset"]
    n=len(items); sp=68; total=(n-1)*sp
    xs=[C1-total//2+i*sp for i in range(n)]
    x0f=min(xs)-36; x1f=max(xs)+36
    # incoming arrow to fork
    arr_v(d,C1,y-AR,y-4)
    fbar(d,x0f,y,x1f)
    # fan out (diagonal like foto)
    y_box=y+AR+4
    for xi in xs: arr_diag(d,xi,y+4,xi,y_box-22+4)
    # boxes
    bh_box=44
    for xi,lbl in zip(xs,items):
        tw_b,_=msz(lbl,FS); bw_b=max(tw_b+16,62)
        d.rounded_rectangle([xi-bw_b//2,y_box-22,xi+bw_b//2,y_box-22+bh_box],
                             radius=5,fill=BOXF,outline=BOXBD,width=1)
        tc(d,xi,y_box-22+bh_box//2,lbl,FS)
    # fan in (diagonal)
    for xi in xs: arr_diag(d,xi,y_box-22+bh_box,C1,y_box-22+bh_box+AR)
    y_join=y_box-22+bh_box+AR
    fbar(d,x0f,y_join,x1f)
    # arrow from join to Sistem
    arr_h(d,x1f,y_join,C2-bw4//2)
    arr_v(d,C2,y_join,y_join+AR)
    y=y_join+AR

    # [Sistem] Menyimpan Data
    bw5,bh5=msz("Menyimpan Data",FB); bh5+=14; bw5=max(bw5+20,180)
    draw_box(d,C2,y+bh5//2,"Menyimpan Data",FB,180)
    arr_v(d,C2,y+bh5,y+bh5+AR); y+=bh5+AR

    # [Sistem] Selesai → return to Pengguna Logout
    bw6,bh6=msz("Selesai",FB); bh6+=14; bw6=max(bw6+20,120)
    draw_box(d,C2,y+bh6//2,"Selesai",FB,120)
    arr_h(d,C2-bw6//2,y+bh6//2,C1+80)
    draw_box(d,C1,y+bh6//2,"Logout",FB,120)
    arr_v(d,C1,y+bh6,y+bh6+AR); y+=bh6+AR

    # END
    enode(d,C1,y+9)

    save(img,"ACT_01_Login.png",TW,TH2)

act_login()
