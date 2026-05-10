"""
Use Case Diagram v2 — rapi, tidak tumpang tindih, persis gaya foto.

Strategi layout:
- Semua use case utama disusun dalam KOLOM vertikal di tengah
- Extend items disusun di KIRI atau KANAN use case utama
- Jarak antar elemen dihitung dari ukuran teks
- Tidak ada posisi hardcode yang bisa overlap
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

BG    = (255,255,255)
BOXF  = (255,255,204)
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

def ellipse_rx_ry(txt, font, px=18, py=12):
    tw,th=msz(txt,font)
    return tw//2+px, th//2+py

def draw_ellipse(d, cx, cy, txt, font=FB):
    rx,ry=ellipse_rx_ry(txt,font)
    d.ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=BOXF,outline=BLACK,width=1)
    tc(d,cx,cy,txt,font)
    return rx,ry

def edge_pt(cx,cy,rx,ry,tx,ty):
    dx,dy=tx-cx,ty-cy; L=max(1,math.hypot(dx,dy))
    denom=math.sqrt((dx/L/rx)**2+(dy/L/ry)**2)
    if denom==0: return cx,cy
    t=1/denom
    return int(cx+dx/L*t),int(cy+dy/L*t)

def dashed_line(d,x1,y1,x2,y2):
    dx,dy=x2-x1,y2-y1; L=max(1,math.hypot(dx,dy)); n=int(L/7)
    for i in range(n):
        if i%2==0:
            t1,t2=i/n,min(1,(i+.5)/n)
            d.line([(int(x1+dx*t1),int(y1+dy*t1)),
                    (int(x1+dx*t2),int(y1+dy*t2))],fill=BLACK,width=1)

def arrowhead(d,x2,y2,x1,y1,s=7):
    ang=math.atan2(y2-y1,x2-x1)
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                          int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)

def connect(d, c1,r1, c2,r2, lbl="", dashed=True, arrow=True):
    """Connect two ellipses edge-to-edge."""
    x1,y1=edge_pt(*c1,*r1,*c2[:2])
    x2,y2=edge_pt(*c2,*r2,*c1[:2])
    if dashed: dashed_line(d,x1,y1,x2,y2)
    else:      d.line([(x1,y1),(x2,y2)],fill=BLACK,width=1)
    if arrow:  arrowhead(d,x2,y2,x1,y1)
    if lbl:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=FSM.getbbox(lbl); tw=bb[2]-bb[0]
        # offset label slightly
        ang=math.atan2(y2-y1,x2-x1)
        ox=int(-math.sin(ang)*10); oy=int(math.cos(ang)*10)
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

def actor_to_ell(d,ax,ay,cx,cy,rx,ry):
    ex,ey=edge_pt(cx,cy,rx,ry,ax,ay)
    d.line([(ax,ay),(ex,ey)],fill=BLACK,width=1)

# ─── LAYOUT ENGINE ───────────────────────────────────────────────────────────
def make_uc():
    """
    Layout:
    - Use case utama disusun dalam 2 kolom vertikal (kiri & kanan dari Login)
    - Login di tengah
    - Extend items di sisi luar masing-masing use case utama
    - Aktor Admin di kiri, Staff di kanan
    """

    # ── Define use cases ─────────────────────────────────────────────────────
    # Format: (key, label, extends_to_key, side_of_extends)
    # side: "left"=extend di kiri UC, "right"=extend di kanan UC,
    #       "above"=extend di atas, "below"=extend di bawah

    main_ucs = [
        # key,              label,                  col, row
        ("login",           "Login",                 2,   4),   # center
        ("aset",            "Manajemen\nAset",        1,   1),
        ("barang",          "Manajemen\nBarang",      1,   2),
        ("ruangan",         "Manajemen\nRuangan",     1,   3),
        ("qr",              "QR Code",                1,   5),
        ("maintenance",     "Maintenance",            1,   6),
        ("import",          "Import Data",            3,   1),
        ("export",          "Export &\nLaporan",      3,   2),
        ("dashboard",       "Dashboard",              3,   3),
        ("pengguna",        "Kelola\nPengguna",       3,   5),
        ("auditlog",        "Audit Log",              3,   6),
    ]

    extends = [
        # (child_label, parent_key, side)
        # Aset extends — left side
        ("Tambah Aset",     "aset",     "left"),
        ("Edit Aset",       "aset",     "left"),
        ("Hapus Aset",      "aset",     "left"),
        ("Detail Aset",     "aset",     "left"),
        # Barang extends — left
        ("Tambah Barang",   "barang",   "left"),
        ("Edit Barang",     "barang",   "left"),
        ("Hapus Barang",    "barang",   "left"),
        # Ruangan extends — left
        ("Tambah Ruangan",  "ruangan",  "left"),
        ("Edit Ruangan",    "ruangan",  "left"),
        ("Hapus Ruangan",   "ruangan",  "left"),
        # QR extends — left
        ("Generate QR",     "qr",       "left"),
        ("Scan QR",         "qr",       "left"),
        ("Cetak Massal",    "qr",       "left"),
        # Maintenance extends — left
        ("Set Maintenance", "maintenance","left"),
        ("Selesaikan\nMaintenance","maintenance","left"),
        # Import extends — right
        ("Import Aset",     "import",   "right"),
        ("Import Barang",   "import",   "right"),
        ("Download\nTemplate","import", "right"),
        # Export extends — right
        ("Export Excel",    "export",   "right"),
        ("Export PDF",      "export",   "right"),
        ("Laporan\nRuangan","export",   "right"),
        ("Laporan\nMaintenance","export","right"),
        # Pengguna extends — right
        ("Tambah\nPengguna","pengguna", "right"),
        ("Edit Pengguna",   "pengguna", "right"),
        ("Hapus Pengguna",  "pengguna", "right"),
        # Audit extends — right
        ("Filter\nAudit Log","auditlog","right"),
    ]

    # ── Compute sizes ─────────────────────────────────────────────────────────
    # For each main UC, compute its ellipse size
    uc_sizes = {}
    for key,lbl,col,row in main_ucs:
        rx,ry=ellipse_rx_ry(lbl,FB)
        uc_sizes[key]=(rx,ry)

    # For each extend, compute size
    ext_sizes = {}
    for lbl,parent,side in extends:
        rx,ry=ellipse_rx_ry(lbl,FS,px=14,py=10)
        ext_sizes[lbl]=(rx,ry)

    # ── Compute positions ─────────────────────────────────────────────────────
    # Grid: 4 columns (0=actor_admin, 1=left_ucs, 2=center, 3=right_ucs, 4=actor_staff)
    # Row spacing based on max height of elements in that row

    # Group extends by parent
    from collections import defaultdict
    ext_by_parent = defaultdict(list)
    for lbl,parent,side in extends:
        ext_by_parent[parent].append((lbl,side))

    # Column x positions
    # We need to figure out max extend width on each side
    max_ext_w_left  = 0
    max_ext_w_right = 0
    for lbl,parent,side in extends:
        rx,ry=ext_sizes[lbl]
        if side=="left":  max_ext_w_left  = max(max_ext_w_left,  rx*2+10)
        if side=="right": max_ext_w_right = max(max_ext_w_right, rx*2+10)

    # Main UC column widths
    max_uc_w = max(rx*2 for rx,ry in uc_sizes.values()) + 20

    # Layout x:
    # actor_admin | gap | [ext_left] | gap | [main_left] | gap | [login] | gap | [main_right] | gap | [ext_right] | gap | actor_staff
    PAD=20
    ACTOR_W=60
    GAP_ACT=30
    GAP_EXT=30
    GAP_UC=40
    GAP_LOGIN=50

    x_actor_admin = ACTOR_W//2 + PAD
    x_ext_left    = x_actor_admin + ACTOR_W//2 + GAP_ACT + max_ext_w_left//2
    x_main_left   = x_ext_left + max_ext_w_left//2 + GAP_EXT + max_uc_w//2
    x_login       = x_main_left + max_uc_w//2 + GAP_LOGIN + uc_sizes["login"][0]
    x_main_right  = x_login + uc_sizes["login"][0] + GAP_LOGIN + max_uc_w//2
    x_ext_right   = x_main_right + max_uc_w//2 + GAP_EXT + max_ext_w_right//2
    x_actor_staff = x_ext_right + max_ext_w_right//2 + GAP_ACT + ACTOR_W//2

    W = x_actor_staff + ACTOR_W//2 + PAD + 10

    # Row y positions — compute per row
    # Rows 1-6 for main UCs, row 4 = login
    # For each row, height = max(main_uc_ry*2, max_ext_ry*2 for that row) + row_gap
    ROW_GAP = 30

    # Collect rows
    rows = {}
    for key,lbl,col,row in main_ucs:
        if row not in rows: rows[row]=[]
        rows[row].append(key)

    # Compute y for each row
    row_ys = {}
    y = 80  # start y (after title + boundary)
    for r in sorted(rows.keys()):
        keys_in_row = rows[r]
        # max height of main UCs in this row
        max_ry = max(uc_sizes[k][1] for k in keys_in_row)
        # max height of extends for UCs in this row
        for k in keys_in_row:
            for lbl,side in ext_by_parent.get(k,[]):
                rx,ry=ext_sizes[lbl]
                max_ry=max(max_ry,ry)
        row_ys[r] = y + max_ry
        y += max_ry*2 + ROW_GAP

    H_content = y + 40

    # ── Assign positions to main UCs ──────────────────────────────────────────
    uc_pos = {}
    col_x = {1: x_main_left, 2: x_login, 3: x_main_right}
    for key,lbl,col,row in main_ucs:
        uc_pos[key] = (col_x[col], row_ys[row])

    # ── Assign positions to extends ───────────────────────────────────────────
    # For each parent, distribute extends vertically around parent y
    ext_pos = {}
    for parent_key, ext_list in ext_by_parent.items():
        px,py = uc_pos[parent_key]
        prx,pry = uc_sizes[parent_key]
        side = ext_list[0][1]  # all same side for a parent
        n = len(ext_list)

        # x position of extends
        if side=="left":
            ex = x_ext_left
        else:
            ex = x_ext_right

        # y positions: distribute vertically centered on parent y
        # spacing = max height of extend ellipses + gap
        max_ery = max(ext_sizes[lbl][1] for lbl,_ in ext_list)
        spacing = max_ery*2 + 16
        total_h = (n-1)*spacing
        start_y = py - total_h//2

        for i,(lbl,_) in enumerate(ext_list):
            ey = start_y + i*spacing
            ext_pos[lbl] = (ex, ey)

    # ── Canvas ────────────────────────────────────────────────────────────────
    TITLE_H=22; BOUND_PAD=16
    H = H_content + TITLE_H + BOUND_PAD*2 + 60
    img = Image.new("RGB",(W,H),BG)
    d   = ImageDraw.Draw(img)

    # outer border
    d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
    # title tag
    tag="uc  Use Case Diagram — SimAset RBTV Bengkulu"
    bb=FT.getbbox(tag); tw=bb[2]-bb[0]
    d.rectangle([8,8,8+tw+10,8+TITLE_H],fill=BG,outline=BLACK,width=1)
    d.text((12,10),tag,font=FT,fill=BLACK)

    # system boundary
    bx0=x_ext_left-max_ext_w_left//2-10
    bx1=x_ext_right+max_ext_w_right//2+10
    by0=8+TITLE_H+4
    by1=H-20
    d.rectangle([bx0,by0,bx1,by1],fill=(255,255,252),outline=BLACK,width=1)

    # offset all y by title+boundary
    Y_OFF = by0 + BOUND_PAD + 20

    def gy(y): return y + Y_OFF  # global y

    # ── Draw actors ───────────────────────────────────────────────────────────
    mid_y = gy(row_ys[3])  # middle row y
    actor(d, x_actor_admin, mid_y-20, "Admin")
    actor(d, x_actor_staff, mid_y-20, "Staff")

    # ── Draw main use cases ───────────────────────────────────────────────────
    drawn_uc = {}  # key → (cx,cy,rx,ry)
    for key,lbl,col,row in main_ucs:
        cx,cy = uc_pos[key]; cy=gy(cy)
        rx,ry = uc_sizes[key]
        draw_ellipse(d,cx,cy,lbl,FB)
        drawn_uc[key]=(cx,cy,rx,ry)

    # ── Draw extend ellipses ──────────────────────────────────────────────────
    drawn_ext = {}  # lbl → (cx,cy,rx,ry)
    for lbl,parent,side in extends:
        cx,cy=ext_pos[lbl]; cy=gy(cy)
        rx,ry=ext_sizes[lbl]
        draw_ellipse(d,cx,cy,lbl,FS)
        drawn_ext[lbl]=(cx,cy,rx,ry)

    # ── Draw extend arrows ────────────────────────────────────────────────────
    for lbl,parent,side in extends:
        ec=drawn_ext[lbl]; pc=drawn_uc[parent]
        connect(d,(ec[0],ec[1]),(ec[2],ec[3]),
                  (pc[0],pc[1]),(pc[2],pc[3]),"<<extend>>",dashed=True,arrow=True)

    # ── Draw include arrows (main UCs → Login) ────────────────────────────────
    lc=drawn_uc["login"]
    for key,lbl,col,row in main_ucs:
        if key=="login": continue
        uc=drawn_uc[key]
        connect(d,(uc[0],uc[1]),(uc[2],uc[3]),
                  (lc[0],lc[1]),(lc[2],lc[3]),"<<include>>",dashed=True,arrow=True)

    # ── Draw actor lines ──────────────────────────────────────────────────────
    admin_x=x_actor_admin; admin_y=gy(row_ys[3])-20
    staff_x=x_actor_staff; staff_y=gy(row_ys[3])-20

    admin_ucs=list(drawn_uc.keys())
    staff_ucs=[k for k in drawn_uc if k not in ("pengguna","auditlog")]

    for k in admin_ucs:
        uc=drawn_uc[k]
        actor_to_ell(d,admin_x,admin_y,uc[0],uc[1],uc[2],uc[3])
    for k in staff_ucs:
        uc=drawn_uc[k]
        actor_to_ell(d,staff_x,staff_y,uc[0],uc[1],uc[2],uc[3])

    path=f"{OUT}/UC_SimAset.png"
    img.save(path,"PNG",dpi=(150,150))
    print(f"  UC_SimAset.png  ({W}x{H})")

make_uc()
