"""
Generate semua diagram PNG bergaya natural seperti contoh foto:
- Background putih/abu muda
- Kotak rounded kuning muda (#ffffcc / #fffde7)
- Swimlane header kuning muda, border tipis hitam
- Font Arial, ukuran wajar
- Garis hitam tipis, panah kecil
- Sangat clean, tidak berwarna-warni
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = "docs/diagrams/png"
os.makedirs(OUT, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL STYLE  (persis seperti foto contoh)
# ─────────────────────────────────────────────────────────────────────────────
BG          = (255, 255, 255)   # putih
SW_BG       = (255, 255, 240)   # swimlane background — kuning sangat muda
SW_HDR_BG   = (255, 255, 220)   # swimlane header — kuning muda
SW_HDR_BD   = (180, 180, 160)   # swimlane border
BOX_FILL    = (255, 255, 204)   # kotak aksi — kuning muda (#ffffcc)
BOX_BD      = (160, 160, 120)   # border kotak
DEC_FILL    = (255, 255, 255)   # diamond — putih
DEC_BD      = (80,  80,  80)    # diamond border
LINE        = (0,   0,   0)     # garis & panah
GRAY        = (100, 100, 100)   # label kecil
TITLE_FG    = (0,   0,   0)
NOTE_FILL   = (255, 255, 240)
NOTE_BD     = (160, 160, 120)

def get_font(size, bold=False):
    paths = (["C:/Windows/Fonts/arialbd.ttf","C:/Windows/Fonts/calibrib.ttf"]
             if bold else
             ["C:/Windows/Fonts/arial.ttf","C:/Windows/Fonts/calibri.ttf",
              "C:/Windows/Fonts/verdana.ttf"])
    for p in paths:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

# ─────────────────────────────────────────────────────────────────────────────
# DRAWING PRIMITIVES
# ─────────────────────────────────────────────────────────────────────────────
def rr(d, x0,y0,x1,y1, fill=BOX_FILL, bd=BOX_BD, r=8, lw=1):
    d.rounded_rectangle([x0,y0,x1,y1], radius=r, fill=fill, outline=bd, width=lw)

def txt_c(d, cx, cy, text, font, color=(0,0,0)):
    lines = text.split("\n")
    lh = font.size + 3
    total = lh * len(lines)
    y = cy - total // 2
    for line in lines:
        bb = d.textbbox((0,0), line, font=font)
        tw = bb[2] - bb[0]
        d.text((cx - tw//2, y), line, font=font, fill=color)
        y += lh

def txt_l(d, x, y, text, font, color=(0,0,0)):
    d.text((x, y), text, font=font, fill=color)

def box(d, cx, cy, text, w, h, font, fill=BOX_FILL, bd=BOX_BD):
    x0,y0 = cx-w//2, cy-h//2
    rr(d, x0,y0,x0+w,y0+h, fill=fill, bd=bd, r=8, lw=1)
    txt_c(d, cx, cy, text, font)
    return y0, y0+h

def diamond(d, cx, cy, w, h, font):
    pts = [(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
    d.polygon(pts, fill=DEC_FILL, outline=DEC_BD)
    # no text inside (label outside)
    return cy-h//2, cy+h//2

def fork(d, x0, y, x1, h=6):
    d.rectangle([x0, y-h//2, x1, y+h//2], fill=(0,0,0))

def arr(d, x1,y1,x2,y2, lbl="", font=None, lbl_dx=6, lbl_dy=-14):
    d.line([(x1,y1),(x2,y2)], fill=LINE, width=1)
    ang = math.atan2(y2-y1, x2-x1)
    sz = 8
    for da in [0.4,-0.4]:
        ax = x2 - sz*math.cos(ang-da)
        ay = y2 - sz*math.sin(ang-da)
        d.line([(x2,y2),(int(ax),int(ay))], fill=LINE, width=1)
    if lbl and font:
        mx,my = (x1+x2)//2, (y1+y2)//2
        bb = d.textbbox((0,0), lbl, font=font)
        tw = bb[2]-bb[0]
        d.text((mx+lbl_dx, my+lbl_dy), lbl, font=font, fill=GRAY)

def start(d, cx, cy, r=10):
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=(0,0,0))

def end(d, cx, cy, r=10):
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=(0,0,0))
    d.ellipse([cx-r+3,cy-r+3,cx+r-3,cy+r-3], fill=(255,255,255))
    d.ellipse([cx-r+6,cy-r+6,cx+r-6,cy+r-6], fill=(0,0,0))

def line_h(d, x1, y, x2, lw=1):
    d.line([(x1,y),(x2,y)], fill=LINE, width=lw)

def line_v(d, x, y1, y2, lw=1):
    d.line([(x,y1),(x,y2)], fill=LINE, width=lw)

def note(d, x, y, text, font, w=160):
    lines = text.split("\n")
    lh = font.size+3
    h = lh*len(lines)+10
    fold=10
    pts=[(x,y),(x+w-fold,y),(x+w,y+fold),(x+w,y+h),(x,y+h)]
    d.polygon(pts, fill=NOTE_FILL, outline=NOTE_BD, width=1)
    d.line([(x+w-fold,y),(x+w-fold,y+fold),(x+w,y+fold)], fill=NOTE_BD, width=1)
    ty=y+5
    for ln in lines:
        d.text((x+6,ty), ln, font=font, fill=(60,60,60))
        ty+=lh

print("Fonts loaded, starting generation...")

# ═════════════════════════════════════════════════════════════════════════════
# 1. ACTIVITY DIAGRAM — LOGIN  (gaya persis foto: 2 swimlane, clean)
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_login():
    W, H = 900, 1300
    img = Image.new("RGB",(W,H),BG)
    d   = ImageDraw.Draw(img)
    FB  = get_font(13)
    FS  = get_font(11)
    FH  = get_font(13, bold=True)
    FT  = get_font(12, bold=True)

    # ── frame & title ────────────────────────────────────────────────────────
    d.rectangle([10,10,W-10,H-10], outline=(0,0,0), width=1)
    d.text((16,14), "act  Admin — Login SimAset", font=FT, fill=(0,0,0))

    # ── swimlanes ─────────────────────────────────────────────────────────────
    MX, MY = 10, 36
    SW_H   = H - MY - 10
    SW_W1  = 380   # Pengguna
    SW_W2  = W - MX*2 - SW_W1
    HDR_H  = 30
    CX1    = MX + SW_W1//2
    CX2    = MX + SW_W1 + SW_W2//2

    # backgrounds
    d.rectangle([MX,MY, MX+SW_W1, MY+SW_H], fill=SW_BG, outline=(0,0,0), width=1)
    d.rectangle([MX+SW_W1,MY, MX+SW_W1+SW_W2, MY+SW_H], fill=SW_BG, outline=(0,0,0), width=1)
    # headers
    d.rectangle([MX,MY, MX+SW_W1, MY+HDR_H], fill=SW_HDR_BG, outline=(0,0,0), width=1)
    d.rectangle([MX+SW_W1,MY, MX+SW_W1+SW_W2, MY+HDR_H], fill=SW_HDR_BG, outline=(0,0,0), width=1)
    txt_c(d, CX1, MY+HDR_H//2, "Pengguna", FH)
    txt_c(d, CX2, MY+HDR_H//2, "Sistem", FH)

    y = MY + HDR_H + 45

    # START
    start(d, CX1, y)
    arr(d, CX1, y+10, CX1, y+35)
    y += 50

    # Login → Menampilkan Login
    t,b = box(d, CX1, y, "Login", 140, 34, FB)
    arr(d, CX1+70, y, CX2-80, y, font=FS)
    t2,b2 = box(d, CX2, y, "Menampilkan Login", 200, 34, FB)
    # return arrow
    arr(d, CX2-100, b2, CX1+70, b2, font=FS)
    arr(d, CX1, b, CX1, b+25)
    y += 60

    # Username dan Password → Autentikasi
    t,b = box(d, CX1, y, "Username dan Password", 220, 34, FB)
    arr(d, CX1+110, y, CX2-100, y, font=FS)
    t2,b2 = box(d, CX2, y, "Autentikasi", 160, 34, FB)
    arr(d, CX2, b2, CX2, b2+25)
    y += 60

    # Decision
    dy = y + 30
    diamond(d, CX2, dy, 100, 50, FB)
    # label Tidak
    d.text((CX2+55, dy-18), "Akun Tidak", font=FS, fill=GRAY)
    d.text((CX2+55, dy-5),  "Terdaftar",  font=FS, fill=GRAY)
    arr(d, CX2+50, dy, CX2+130, dy, font=FS)
    # loop back (Tidak)
    line_v(d, CX2+130, dy, dy-80)
    line_h(d, CX2+130, dy-80, CX2+10)
    # label Ya / Akun Terdaftar
    d.text((CX2-90, dy+30), "Akun Terdaftar", font=FS, fill=GRAY)
    arr(d, CX2, dy+25, CX2, dy+55)
    y = dy + 75

    # Menampilkan Dashboard → Pilih Menu
    t2,b2 = box(d, CX2, y, "Menampilkan Dashboard", 220, 34, FB)
    arr(d, CX2-110, y, CX1+110, y, font=FS)
    t,b = box(d, CX1, y, "Pilih Menu Aset", 180, 34, FB)
    arr(d, CX1, b, CX1, b+25)
    arr(d, CX1+90, b+12, CX2-110, b+12, font=FS)
    y += 60

    # Menampilkan Halaman Aset
    t2,b2 = box(d, CX2, y, "Menampilkan Halaman Aset", 240, 34, FB)
    arr(d, CX2, b2, CX2, b2+20)
    y += 60

    # FORK
    FK0, FK1 = CX1-160, CX1+160
    fork(d, FK0, y, FK1)
    arr(d, CX1, y-20, CX1, y-3)

    # 5 action boxes fan out
    actions = ["Tambah\nAset","Lihat\nAset","Edit\nAset","Export\nAset","Hapus\nAset"]
    xs = [CX1-160, CX1-80, CX1, CX1+80, CX1+160]
    y_act = y + 60
    for i,(lbl,cx) in enumerate(zip(actions,xs)):
        arr(d, cx, y+3, cx, y_act-17)
        box(d, cx, y_act, lbl, 70, 44, FS)
        arr(d, cx, y_act+22, cx, y_act+50)

    # JOIN
    y_join = y_act + 70
    fork(d, FK0, y_join, FK1)
    for cx in xs:
        arr(d, cx, y_join-3, cx, y_join)

    arr(d, CX1, y_join+3, CX1, y_join+25)
    # cross to Sistem
    arr(d, CX1+10, y_join+14, CX2-110, y_join+14, font=FS)
    y = y_join + 40

    # Menyimpan Data
    t2,b2 = box(d, CX2, y, "Menyimpan Data", 180, 34, FB)
    arr(d, CX2, b2, CX2, b2+25)
    y += 60

    # Selesai → Logout
    t2,b2 = box(d, CX2, y, "Selesai", 120, 34, FB)
    arr(d, CX2-60, y, CX1+70, y, font=FS)
    t,b = box(d, CX1, y, "Logout", 140, 34, FB)
    arr(d, CX1, b, CX1, b+30)
    y += 65

    # END
    end(d, CX1, y)

    img.save(f"{OUT}/01_Activity_Login.png","PNG",dpi=(150,150))
    print("  01_Activity_Login.png")

gen_activity_login()

# ═════════════════════════════════════════════════════════════════════════════
# 2. ACTIVITY DIAGRAM — MANAJEMEN ASET (CRUD + QR)
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_aset():
    W, H = 900, 1500
    img = Image.new("RGB",(W,H),BG)
    d   = ImageDraw.Draw(img)
    FB  = get_font(13)
    FS  = get_font(11)
    FH  = get_font(13, bold=True)
    FT  = get_font(12, bold=True)

    d.rectangle([10,10,W-10,H-10], outline=(0,0,0), width=1)
    d.text((16,14), "act  Manajemen Aset — SimAset RBTV Bengkulu", font=FT, fill=(0,0,0))

    MX,MY = 10,36
    SW_H  = H-MY-10
    SW_W1 = 380; SW_W2 = W-MX*2-SW_W1
    HDR_H = 30
    CX1   = MX+SW_W1//2; CX2 = MX+SW_W1+SW_W2//2

    d.rectangle([MX,MY,MX+SW_W1,MY+SW_H], fill=SW_BG, outline=(0,0,0), width=1)
    d.rectangle([MX+SW_W1,MY,MX+SW_W1+SW_W2,MY+SW_H], fill=SW_BG, outline=(0,0,0), width=1)
    d.rectangle([MX,MY,MX+SW_W1,MY+HDR_H], fill=SW_HDR_BG, outline=(0,0,0), width=1)
    d.rectangle([MX+SW_W1,MY,MX+SW_W1+SW_W2,MY+HDR_H], fill=SW_HDR_BG, outline=(0,0,0), width=1)
    txt_c(d,CX1,MY+HDR_H//2,"Pengguna",FH)
    txt_c(d,CX2,MY+HDR_H//2,"Sistem",FH)

    y = MY+HDR_H+45
    start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50

    # Login
    t,b = box(d,CX1,y,"Login ke Sistem",180,34,FB)
    arr(d,CX1,b,CX1,b+25); y+=60

    # Pilih menu Aset
    t,b = box(d,CX1,y,'Pilih menu "Aset"',180,34,FB)
    arr(d,CX1+90,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Query Aset + Tampilkan\nDaftar (tabel + filter)",240,44,FB)
    arr(d,CX2-120,y+22,CX1+90,y+22,font=FS)
    arr(d,CX1,b,CX1,b+25); y+=70

    # Decision: pilih aksi
    dy = y+30
    diamond(d,CX1,dy,120,55,FB)
    txt_c(d,CX1,dy,"Pilih\naksi?",FS)
    y = dy+55

    # TAMBAH branch
    arr(d,CX1-60,dy,CX1-140,dy,font=FS)
    line_v(d,CX1-140,dy,y+10)
    arr(d,CX1-140,y+10,CX1-80,y+10)
    d.text((CX1-200,dy-8),"Tambah",font=FS,fill=GRAY)
    t,b = box(d,CX1,y,"Isi Form Aset\n(Barang, Ruangan,\nKondisi, Status, dll)",200,60,FB)
    arr(d,CX1+100,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Validasi → generateKode()\n→ Asset::create()\n→ Log Aktivitas",260,60,FB)
    arr(d,CX1,b,CX1,b+20); y+=90

    # EDIT branch
    t,b = box(d,CX1,y,"Edit Data Aset",180,34,FB)
    arr(d,CX1+90,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Load Aset → Form Edit\n→ Validasi → update()\n→ Log Aktivitas",260,60,FB)
    arr(d,CX1,b,CX1,b+20); y+=70

    # HAPUS branch
    t,b = box(d,CX1,y,"Hapus Aset\n(Konfirmasi)",180,44,FB)
    arr(d,CX1+90,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Soft Delete\n(isi deleted_at)\n→ Log Aktivitas",220,60,FB)
    arr(d,CX1,b,CX1,b+20); y+=80

    # QR CODE branch
    t,b = box(d,CX1,y,"Generate / Scan\nQR Code",180,44,FB)
    arr(d,CX1+90,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Request API qrserver.com\n→ Simpan PNG\n→ Tampilkan / Download",260,60,FB)
    arr(d,CX1,b,CX1,b+20); y+=80

    # Selesai
    t,b = box(d,CX1,y,"Selesai / Logout",180,34,FB)
    arr(d,CX1,b,CX1,b+30); y+=65
    end(d,CX1,y)

    img.save(f"{OUT}/02_Activity_Aset.png","PNG",dpi=(150,150))
    print("  02_Activity_Aset.png")

gen_activity_aset()

# ═════════════════════════════════════════════════════════════════════════════
# 3. ACTIVITY DIAGRAM — MANAJEMEN BARANG
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_barang():
    W, H = 900, 1200
    img = Image.new("RGB",(W,H),BG)
    d   = ImageDraw.Draw(img)
    FB  = get_font(13); FS = get_font(11)
    FH  = get_font(13,bold=True); FT = get_font(12,bold=True)

    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"act  Manajemen Barang — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))

    MX,MY=10,36; SW_H=H-MY-10; SW_W1=380; SW_W2=W-MX*2-SW_W1; HDR_H=30
    CX1=MX+SW_W1//2; CX2=MX+SW_W1+SW_W2//2

    for x0,x1 in [(MX,MX+SW_W1),(MX+SW_W1,MX+SW_W1+SW_W2)]:
        d.rectangle([x0,MY,x1,MY+SW_H],fill=SW_BG,outline=(0,0,0),width=1)
        d.rectangle([x0,MY,x1,MY+HDR_H],fill=SW_HDR_BG,outline=(0,0,0),width=1)
    txt_c(d,CX1,MY+HDR_H//2,"Pengguna",FH)
    txt_c(d,CX2,MY+HDR_H//2,"Sistem",FH)

    y=MY+HDR_H+45
    start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50

    t,b=box(d,CX1,y,"Login ke Sistem",180,34,FB)
    arr(d,CX1,b,CX1,b+25); y+=60

    t,b=box(d,CX1,y,'Pilih menu "Barang"',190,34,FB)
    arr(d,CX1+95,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Query Barang → Tampilkan\nDaftar (tabel + filter)",240,44,FB)
    arr(d,CX2-120,y+22,CX1+95,y+22,font=FS)
    arr(d,CX1,b,CX1,b+25); y+=70

    dy=y+30; diamond(d,CX1,dy,120,55,FB); txt_c(d,CX1,dy,"Pilih\naksi?",FS); y=dy+55

    for lbl,sys_lbl in [
        ("Tambah Barang","generateKode() → Barang::create()\n→ Log Aktivitas"),
        ("Edit Barang","Load → Form Edit → update()\n→ Log Aktivitas"),
        ("Hapus Barang","Soft Delete (deleted_at)\n→ Log Aktivitas"),
        ("Lihat Detail","Tampilkan detail barang\n+ daftar aset terkait"),
    ]:
        t,b=box(d,CX1,y,lbl,180,44,FB)
        arr(d,CX1+90,y,CX2-110,y,font=FS)
        box(d,CX2,y,sys_lbl,260,44,FB)
        arr(d,CX1,b,CX1,b+20); y+=75

    t,b=box(d,CX1,y,"Selesai / Logout",180,34,FB)
    arr(d,CX1,b,CX1,b+30); y+=65
    end(d,CX1,y)

    img.save(f"{OUT}/03_Activity_Barang.png","PNG",dpi=(150,150))
    print("  03_Activity_Barang.png")

gen_activity_barang()

# ═════════════════════════════════════════════════════════════════════════════
# 4. ACTIVITY DIAGRAM — MANAJEMEN RUANGAN
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_ruangan():
    W,H=900,1150
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    FB=get_font(13); FS=get_font(11); FH=get_font(13,bold=True); FT=get_font(12,bold=True)
    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"act  Manajemen Ruangan — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))
    MX,MY=10,36; SW_H=H-MY-10; SW_W1=380; SW_W2=W-MX*2-SW_W1; HDR_H=30
    CX1=MX+SW_W1//2; CX2=MX+SW_W1+SW_W2//2
    for x0,x1 in [(MX,MX+SW_W1),(MX+SW_W1,MX+SW_W1+SW_W2)]:
        d.rectangle([x0,MY,x1,MY+SW_H],fill=SW_BG,outline=(0,0,0),width=1)
        d.rectangle([x0,MY,x1,MY+HDR_H],fill=SW_HDR_BG,outline=(0,0,0),width=1)
    txt_c(d,CX1,MY+HDR_H//2,"Pengguna",FH); txt_c(d,CX2,MY+HDR_H//2,"Sistem",FH)
    y=MY+HDR_H+45; start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50
    t,b=box(d,CX1,y,"Login ke Sistem",180,34,FB); arr(d,CX1,b,CX1,b+25); y+=60
    t,b=box(d,CX1,y,'Pilih menu "Ruangan"',190,34,FB)
    arr(d,CX1+95,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Query Ruangan + withCount(assets)\n→ Tampilkan Daftar",260,44,FB)
    arr(d,CX2-130,y+22,CX1+95,y+22,font=FS); arr(d,CX1,b,CX1,b+25); y+=70
    dy=y+30; diamond(d,CX1,dy,120,55,FB); txt_c(d,CX1,dy,"Pilih\naksi?",FS); y=dy+55
    for lbl,sys_lbl in [
        ("Tambah Ruangan","Validasi → Ruangan::create()\n→ Redirect + success"),
        ("Edit Ruangan","Load → Form Edit → update()\n→ Redirect + success"),
        ("Hapus Ruangan","Cek: ada aset?\n→ Jika ada: tolak\n→ Jika tidak: delete()"),
        ("Lihat Detail","Tampilkan ruangan\n+ daftar aset di ruangan"),
    ]:
        t,b=box(d,CX1,y,lbl,180,44,FB)
        arr(d,CX1+90,y,CX2-110,y,font=FS)
        box(d,CX2,y,sys_lbl,260,55,FB)
        arr(d,CX1,b,CX1,b+20); y+=80
    t,b=box(d,CX1,y,"Selesai / Logout",180,34,FB); arr(d,CX1,b,CX1,b+30); y+=65
    end(d,CX1,y)
    img.save(f"{OUT}/04_Activity_Ruangan.png","PNG",dpi=(150,150))
    print("  04_Activity_Ruangan.png")

gen_activity_ruangan()

# ═════════════════════════════════════════════════════════════════════════════
# 5. ACTIVITY DIAGRAM — SCANNER QR CODE
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_qr():
    W,H=900,1100
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    FB=get_font(13); FS=get_font(11); FH=get_font(13,bold=True); FT=get_font(12,bold=True)
    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"act  Scanner QR Code — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))
    MX,MY=10,36; SW_H=H-MY-10; SW_W1=380; SW_W2=W-MX*2-SW_W1; HDR_H=30
    CX1=MX+SW_W1//2; CX2=MX+SW_W1+SW_W2//2
    for x0,x1 in [(MX,MX+SW_W1),(MX+SW_W1,MX+SW_W1+SW_W2)]:
        d.rectangle([x0,MY,x1,MY+SW_H],fill=SW_BG,outline=(0,0,0),width=1)
        d.rectangle([x0,MY,x1,MY+HDR_H],fill=SW_HDR_BG,outline=(0,0,0),width=1)
    txt_c(d,CX1,MY+HDR_H//2,"Pengguna",FH); txt_c(d,CX2,MY+HDR_H//2,"Sistem",FH)
    y=MY+HDR_H+45; start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50
    t,b=box(d,CX1,y,"Login ke Sistem",180,34,FB); arr(d,CX1,b,CX1,b+25); y+=60
    t,b=box(d,CX1,y,'Klik menu "QR Scanner"',200,34,FB)
    arr(d,CX1+100,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Tampilkan Halaman Scanner\n(GET /qrcode/scanner)\nMinta izin kamera browser",260,55,FB)
    arr(d,CX2-130,y+27,CX1+100,y+27,font=FS); arr(d,CX1,b,CX1,b+25); y+=70
    t,b=box(d,CX1,y,"Izinkan akses kamera",200,34,FB); arr(d,CX1,b,CX1,b+25); y+=60
    t,b=box(d,CX1,y,"Arahkan kamera ke\nQR Code aset fisik",200,44,FB)
    arr(d,CX1+100,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Decode QR Code (JavaScript)\n→ Baca URL dari QR\n→ Parse kode_aset",260,55,FB)
    arr(d,CX1,b,CX1,b+25); y+=75
    arr(d,CX1+100,y-12,CX2-110,y-12,font=FS)
    box(d,CX2,y-12,"GET /aset/{kode}/detail\nAsset::with([barang,ruangan])\n->firstOrFail()",260,55,FB)
    dy=y+40; diamond(d,CX2,dy,130,55,FB); txt_c(d,CX2,dy,"Aset\nditemukan?",FS)
    arr(d,CX2,dy+27,CX2,dy+55,lbl="Ya",font=FS)
    arr(d,CX2+65,dy,CX2+180,dy,font=FS)
    d.text((CX2+185,dy-8),"Tidak",font=FS,fill=GRAY)
    box(d,CX2+280,dy,"HTTP 404\nAset tidak\nditemukan",120,55,FB)
    y=dy+75
    box(d,CX2,y,"Tampilkan Detail Aset:\nNama, Kategori, Ruangan,\nKondisi, Status, Serial",260,60,FB)
    arr(d,CX2-130,y+30,CX1+100,y+30,font=FS)
    t,b=box(d,CX1,y+30,"Melihat detail aset",200,34,FB)
    arr(d,CX1,b,CX1,b+30); y+=110
    end(d,CX1,y)
    img.save(f"{OUT}/05_Activity_ScannerQR.png","PNG",dpi=(150,150))
    print("  05_Activity_ScannerQR.png")

gen_activity_qr()

# ═════════════════════════════════════════════════════════════════════════════
# 6. ACTIVITY — IMPORT DATA
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_import():
    W,H=900,1200
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    FB=get_font(13); FS=get_font(11); FH=get_font(13,bold=True); FT=get_font(12,bold=True)
    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"act  Import Data — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))
    MX,MY=10,36; SW_H=H-MY-10; SW_W1=380; SW_W2=W-MX*2-SW_W1; HDR_H=30
    CX1=MX+SW_W1//2; CX2=MX+SW_W1+SW_W2//2
    for x0,x1 in [(MX,MX+SW_W1),(MX+SW_W1,MX+SW_W1+SW_W2)]:
        d.rectangle([x0,MY,x1,MY+SW_H],fill=SW_BG,outline=(0,0,0),width=1)
        d.rectangle([x0,MY,x1,MY+HDR_H],fill=SW_HDR_BG,outline=(0,0,0),width=1)
    txt_c(d,CX1,MY+HDR_H//2,"Pengguna",FH); txt_c(d,CX2,MY+HDR_H//2,"Sistem",FH)
    y=MY+HDR_H+45; start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50
    t,b=box(d,CX1,y,"Login ke Sistem",180,34,FB); arr(d,CX1,b,CX1,b+25); y+=60
    t,b=box(d,CX1,y,"Pilih menu Import",180,34,FB)
    arr(d,CX1+90,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Tampilkan halaman import\n(pilih tipe: Aset / Barang)\n+ tombol Download Template",260,55,FB)
    arr(d,CX2-130,y+27,CX1+90,y+27,font=FS); arr(d,CX1,b,CX1,b+25); y+=75
    dy=y+25; diamond(d,CX1,dy,130,50,FB); txt_c(d,CX1,dy,"Perlu\ntemplate?",FS)
    arr(d,CX1-65,dy,CX1-160,dy,font=FS); d.text((CX1-220,dy-8),"Ya",font=FS,fill=GRAY)
    line_v(d,CX1-160,dy,dy+60); arr(d,CX1-160,dy+60,CX1-90,dy+60)
    arr(d,CX1+65,dy,CX1+160,dy,font=FS); d.text((CX1+165,dy-8),"Tidak",font=FS,fill=GRAY)
    arr(d,CX1+160,dy,CX1+160,dy+60); arr(d,CX1+160,dy+60,CX1+90,dy+60)
    arr(d,CX1,dy+25,CX1,dy+55)
    y=dy+75
    t,b=box(d,CX1,y,"Pilih tipe (Aset/Barang)\nUpload file Excel/CSV",200,44,FB)
    arr(d,CX1,b,CX1,b+25); y+=70
    t,b=box(d,CX1,y,'Klik "Import"',160,34,FB)
    arr(d,CX1+80,y,CX2-110,y,font=FS)
    box(d,CX2,y,"POST /import {file, type}\nValidasi: mimes:xlsx,xls,csv",260,44,FB)
    arr(d,CX1,b,CX1,b+25); y+=65
    dy2=y+25; diamond(d,CX2,dy2,130,50,FB); txt_c(d,CX2,dy2,"File\nvalid?",FS)
    arr(d,CX2,dy2+25,CX2,dy2+55,lbl="Ya",font=FS)
    arr(d,CX2+65,dy2,CX2+200,dy2); d.text((CX2+205,dy2-8),"Tidak",font=FS,fill=GRAY)
    box(d,CX2+290,dy2,"Error:\nFormat\ntidak valid",110,50,FB)
    y=dy2+75
    box(d,CX2,y,"Baca baris → Validasi per baris\n→ create() per record\n→ Hitung berhasil/gagal",260,60,FB)
    arr(d,CX2-130,y+30,CX1+100,y+30,font=FS)
    t,b=box(d,CX1,y+30,"Lihat hasil import\ndi daftar data",200,44,FB)
    arr(d,CX1,b,CX1,b+30); y+=110
    end(d,CX1,y)
    img.save(f"{OUT}/06_Activity_Import.png","PNG",dpi=(150,150))
    print("  06_Activity_Import.png")

gen_activity_import()

# ═════════════════════════════════════════════════════════════════════════════
# 7. ACTIVITY — EXPORT & LAPORAN
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_export():
    W,H=900,1300
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    FB=get_font(13); FS=get_font(11); FH=get_font(13,bold=True); FT=get_font(12,bold=True)
    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"act  Export & Laporan — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))
    MX,MY=10,36; SW_H=H-MY-10; SW_W1=380; SW_W2=W-MX*2-SW_W1; HDR_H=30
    CX1=MX+SW_W1//2; CX2=MX+SW_W1+SW_W2//2
    for x0,x1 in [(MX,MX+SW_W1),(MX+SW_W1,MX+SW_W1+SW_W2)]:
        d.rectangle([x0,MY,x1,MY+SW_H],fill=SW_BG,outline=(0,0,0),width=1)
        d.rectangle([x0,MY,x1,MY+HDR_H],fill=SW_HDR_BG,outline=(0,0,0),width=1)
    txt_c(d,CX1,MY+HDR_H//2,"Pengguna",FH); txt_c(d,CX2,MY+HDR_H//2,"Sistem",FH)
    y=MY+HDR_H+45; start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50
    t,b=box(d,CX1,y,"Login ke Sistem",180,34,FB); arr(d,CX1,b,CX1,b+25); y+=60
    t,b=box(d,CX1,y,'Pilih menu "Laporan"',190,34,FB)
    arr(d,CX1+95,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Tampilkan halaman laporan\n(daftar ruangan + jumlah aset)",260,44,FB)
    arr(d,CX2-130,y+22,CX1+95,y+22,font=FS); arr(d,CX1,b,CX1,b+25); y+=70
    dy=y+30; diamond(d,CX1,dy,130,55,FB); txt_c(d,CX1,dy,"Pilih\njenis?",FS); y=dy+55
    for lbl,sys_lbl in [
        ("Laporan Aset\n(atur filter)","Query aset dengan filter\n→ Tampilkan tabel hasil"),
        ("Cetak PDF","GET /laporan/assets/cetak\n→ DomPDF → Download PDF"),
        ("Export Excel","GET /laporan/assets/export\n→ Maatwebsite → Download .xlsx"),
        ("Laporan Per Ruangan","GET /laporan/ruangan/{id}\n→ Query aset → PDF → Download"),
        ("Laporan Maintenance\n(PDF / CSV)","Query status=Maintenance\n→ Generate PDF atau CSV\n→ Download"),
    ]:
        t,b=box(d,CX1,y,lbl,200,44,FB)
        arr(d,CX1+100,y,CX2-110,y,font=FS)
        box(d,CX2,y,sys_lbl,260,55,FB)
        arr(d,CX1,b,CX1,b+20); y+=80
    t,b=box(d,CX1,y,"Selesai / Logout",180,34,FB); arr(d,CX1,b,CX1,b+30); y+=65
    end(d,CX1,y)
    img.save(f"{OUT}/07_Activity_Export.png","PNG",dpi=(150,150))
    print("  07_Activity_Export.png")

gen_activity_export()

# ═════════════════════════════════════════════════════════════════════════════
# 8. ACTIVITY — KELOLA PENGGUNA (Admin Only)
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_pengguna():
    W,H=900,1250
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    FB=get_font(13); FS=get_font(11); FH=get_font(13,bold=True); FT=get_font(12,bold=True)
    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"act  Kelola Pengguna (Admin Only) — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))
    MX,MY=10,36; SW_H=H-MY-10; SW_W1=380; SW_W2=W-MX*2-SW_W1; HDR_H=30
    CX1=MX+SW_W1//2; CX2=MX+SW_W1+SW_W2//2
    for x0,x1 in [(MX,MX+SW_W1),(MX+SW_W1,MX+SW_W1+SW_W2)]:
        d.rectangle([x0,MY,x1,MY+SW_H],fill=SW_BG,outline=(0,0,0),width=1)
        d.rectangle([x0,MY,x1,MY+HDR_H],fill=SW_HDR_BG,outline=(0,0,0),width=1)
    txt_c(d,CX1,MY+HDR_H//2,"Admin",FH); txt_c(d,CX2,MY+HDR_H//2,"Sistem",FH)
    y=MY+HDR_H+45; start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50
    t,b=box(d,CX1,y,"Login sebagai Admin",200,34,FB); arr(d,CX1,b,CX1,b+25); y+=60
    t,b=box(d,CX1,y,'Klik "Kelola Pengguna"',200,34,FB)
    arr(d,CX1+100,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Cek middleware role:admin\n→ abort(403) jika bukan admin",260,44,FB)
    arr(d,CX1,b,CX1,b+25); y+=65
    dy=y+25; diamond(d,CX2,dy,130,50,FB); txt_c(d,CX2,dy,"Role =\nadmin?",FS)
    arr(d,CX2,dy+25,CX2,dy+55,lbl="Ya",font=FS)
    arr(d,CX2-65,dy,CX2-200,dy); d.text((CX2-280,dy-8),"Tidak",font=FS,fill=GRAY)
    box(d,CX2-370,dy,"HTTP 403\nForbidden",100,44,FB)
    y=dy+75
    box(d,CX2,y,"User::orderBy('role')->get()\n→ Tampilkan daftar pengguna",260,44,FB)
    arr(d,CX2-130,y+22,CX1+100,y+22,font=FS); arr(d,CX1,y+22+17,CX1,y+22+42); y+=80
    dy2=y+25; diamond(d,CX1,dy2,120,55,FB); txt_c(d,CX1,dy2,"Pilih\naksi?",FS); y=dy2+55
    for lbl,sys_lbl in [
        ("Tambah Pengguna\n(Nama, Email, Password,\nRole, Kirim Email?)","Validasi → Hash password\n→ User::create()\n→ Kirim email (opsional)\n→ Log Aktivitas"),
        ("Edit Pengguna","Load user → Form edit\n→ Validasi → update()\n→ Log Aktivitas"),
        ("Hapus Pengguna","Cek: bukan akun sendiri\n→ $user->delete()\n→ Log Aktivitas"),
    ]:
        t,b=box(d,CX1,y,lbl,200,60,FB)
        arr(d,CX1+100,y,CX2-110,y,font=FS)
        box(d,CX2,y,sys_lbl,260,60,FB)
        arr(d,CX1,b,CX1,b+20); y+=90
    t,b=box(d,CX1,y,"Selesai / Logout",180,34,FB); arr(d,CX1,b,CX1,b+30); y+=65
    end(d,CX1,y)
    img.save(f"{OUT}/08_Activity_Pengguna.png","PNG",dpi=(150,150))
    print("  08_Activity_Pengguna.png")

gen_activity_pengguna()

# ═════════════════════════════════════════════════════════════════════════════
# 9. ACTIVITY — AUDIT LOG
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_auditlog():
    W,H=900,1000
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    FB=get_font(13); FS=get_font(11); FH=get_font(13,bold=True); FT=get_font(12,bold=True)
    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"act  Audit Log (Activity Log) — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))
    MX,MY=10,36; SW_H=H-MY-10; SW_W1=380; SW_W2=W-MX*2-SW_W1; HDR_H=30
    CX1=MX+SW_W1//2; CX2=MX+SW_W1+SW_W2//2
    for x0,x1 in [(MX,MX+SW_W1),(MX+SW_W1,MX+SW_W1+SW_W2)]:
        d.rectangle([x0,MY,x1,MY+SW_H],fill=SW_BG,outline=(0,0,0),width=1)
        d.rectangle([x0,MY,x1,MY+HDR_H],fill=SW_HDR_BG,outline=(0,0,0),width=1)
    txt_c(d,CX1,MY+HDR_H//2,"Admin",FH); txt_c(d,CX2,MY+HDR_H//2,"Sistem",FH)
    y=MY+HDR_H+45; start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50
    t,b=box(d,CX1,y,"Login sebagai Admin",200,34,FB); arr(d,CX1,b,CX1,b+25); y+=60
    t,b=box(d,CX1,y,'Klik "Log Aktivitas"',190,34,FB)
    arr(d,CX1+95,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Cek middleware role:admin\nActivityLog::with('user')\n->orderBy('created_at','desc')\n->paginate(20)",260,65,FB)
    arr(d,CX2-130,y+32,CX1+95,y+32,font=FS); arr(d,CX1,b,CX1,b+25); y+=80
    t,b=box(d,CX1,y,"Atur filter (opsional):\n- Kata kunci\n- Pengguna\n- Modul (Login/Create/\n  Update/Delete)",200,80,FB)
    arr(d,CX1,b,CX1,b+25); y+=105
    t,b=box(d,CX1,y,'Klik "Filter"',160,34,FB)
    arr(d,CX1+80,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Query dengan WHERE clause\n(search LIKE, user_id=,\naktivitas LIKE)\n→ Tampilkan hasil (paginated)",260,65,FB)
    arr(d,CX2-130,y+32,CX1+80,y+32,font=FS); arr(d,CX1,b,CX1,b+25); y+=80
    t,b=box(d,CX1,y,"Melihat riwayat\naktivitas pengguna",200,44,FB)
    arr(d,CX1,b,CX1,b+30); y+=75
    end(d,CX1,y)
    img.save(f"{OUT}/09_Activity_AuditLog.png","PNG",dpi=(150,150))
    print("  09_Activity_AuditLog.png")

gen_activity_auditlog()

# ═════════════════════════════════════════════════════════════════════════════
# 10. ACTIVITY — MAINTENANCE
# ═════════════════════════════════════════════════════════════════════════════
def gen_activity_maintenance():
    W,H=1100,1400
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    FB=get_font(13); FS=get_font(11); FH=get_font(13,bold=True); FT=get_font(12,bold=True)
    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"act  Maintenance Aset — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))
    MX,MY=10,36; SW_H=H-MY-10; SW_W1=320; SW_W2=380; SW_W3=W-MX*2-SW_W1-SW_W2; HDR_H=30
    CX1=MX+SW_W1//2; CX2=MX+SW_W1+SW_W2//2; CX3=MX+SW_W1+SW_W2+SW_W3//2
    for x0,x1,lbl in [(MX,MX+SW_W1,"Staff / Admin"),(MX+SW_W1,MX+SW_W1+SW_W2,"Sistem"),(MX+SW_W1+SW_W2,MX+SW_W1+SW_W2+SW_W3,"Admin (Email)")]:
        d.rectangle([x0,MY,x1,MY+SW_H],fill=SW_BG,outline=(0,0,0),width=1)
        d.rectangle([x0,MY,x1,MY+HDR_H],fill=SW_HDR_BG,outline=(0,0,0),width=1)
        txt_c(d,(x0+x1)//2,MY+HDR_H//2,lbl,FH)
    y=MY+HDR_H+45; start(d,CX1,y); arr(d,CX1,y+10,CX1,y+35); y+=50
    t,b=box(d,CX1,y,"Login ke Sistem",180,34,FB); arr(d,CX1,b,CX1,b+25); y+=60

    # SET MAINTENANCE
    d.text((MX+15,y),"— Set Aset ke Maintenance —",font=FS,fill=GRAY)
    y+=20
    t,b=box(d,CX1,y,"Buka Detail Aset\nKlik 'Set Maintenance'",200,44,FB)
    arr(d,CX1+100,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Tampilkan modal konfirmasi\n+ input keterangan (opsional)",260,44,FB)
    arr(d,CX2-130,y+22,CX1+100,y+22,font=FS); arr(d,CX1,b,CX1,b+25); y+=70
    t,b=box(d,CX1,y,"Input keterangan\nKlik 'Konfirmasi'",200,44,FB)
    arr(d,CX1+100,y,CX2-110,y,font=FS)
    box(d,CX2,y,"POST /maintenance/{kode}/set\nupdate([status=>Maintenance])\n→ Log Aktivitas",260,55,FB)
    arr(d,CX2-130,y+27,CX1+100,y+27,font=FS); arr(d,CX1,b,CX1,b+25); y+=80

    # SELESAIKAN MAINTENANCE
    d.text((MX+15,y),"— Selesaikan Maintenance —",font=FS,fill=GRAY)
    y+=20
    t,b=box(d,CX1,y,"Buka menu 'Maintenance'\nKlik 'Selesai' pada aset",200,44,FB)
    arr(d,CX1+100,y,CX2-110,y,font=FS)
    box(d,CX2,y,"Tampilkan modal:\n- Pilih kondisi akhir (wajib)\n- Input keterangan",260,55,FB)
    arr(d,CX2-130,y+27,CX1+100,y+27,font=FS); arr(d,CX1,b,CX1,b+25); y+=80
    t,b=box(d,CX1,y,"Pilih kondisi akhir\nKlik 'Konfirmasi Selesai'",200,44,FB)
    arr(d,CX1+100,y,CX2-110,y,font=FS)
    box(d,CX2,y,"PATCH /maintenance/{kode}/complete\nValidasi kondisi required",260,44,FB)
    arr(d,CX1,b,CX1,b+25); y+=65
    dy=y+25; diamond(d,CX2,dy,130,50,FB); txt_c(d,CX2,dy,"Validasi\ngagal?",FS)
    arr(d,CX2,dy+25,CX2,dy+55,lbl="Tidak",font=FS)
    arr(d,CX2+65,dy,CX2+200,dy); d.text((CX2+205,dy-8),"Ya",font=FS,fill=GRAY)
    box(d,CX2+290,dy,"Error:\nkondisi\nwajib diisi",110,44,FB)
    y=dy+75
    box(d,CX2,y,"update([status=>Aktif, kondisi=>...])\n→ Log Aktivitas\n→ Query semua Admin aktif\n→ Kirim email notifikasi",260,70,FB)
    arr(d,CX2+130,y+35,CX3-80,y+35,font=FS)
    box(d,CX3,y+35,"Terima email:\n'Maintenance Selesai'\n{nama_aset} ({kode})\nKondisi: {kondisi}",200,70,FB)
    arr(d,CX2-130,y+35,CX1+100,y+35,font=FS)
    t,b=box(d,CX1,y+35,"Aset kembali\nberstatus Aktif",180,44,FB)
    arr(d,CX1,b,CX1,b+30); y+=120
    end(d,CX1,y)
    img.save(f"{OUT}/10_Activity_Maintenance.png","PNG",dpi=(150,150))
    print("  10_Activity_Maintenance.png")

gen_activity_maintenance()

# ═════════════════════════════════════════════════════════════════════════════
# 11. ERD — Entity Relationship Diagram (gaya Chen: elips atribut, kotak entitas, diamond relasi)
# ═════════════════════════════════════════════════════════════════════════════
def gen_erd():
    W,H=1600,1100
    img=Image.new("RGB",(W,H),(240,240,240))
    d=ImageDraw.Draw(img)
    FB=get_font(13); FS=get_font(11); FH=get_font(14,bold=True); FT=get_font(14,bold=True)

    def entity(cx,cy,lbl,w=120,h=40):
        d.rectangle([cx-w//2,cy-h//2,cx+w//2,cy+h//2],fill=(255,255,255),outline=(0,0,0),width=2)
        txt_c(d,cx,cy,lbl,FH)
    def attr(cx,cy,lbl,underline=False):
        bb=d.textbbox((0,0),lbl,font=FB)
        tw,th=bb[2]-bb[0],bb[3]-bb[1]
        ew,eh=tw+24,th+16
        d.ellipse([cx-ew//2,cy-eh//2,cx+ew//2,cy+eh//2],fill=(255,255,255),outline=(0,0,0),width=1)
        d.text((cx-tw//2,cy-th//2),lbl,font=FB,fill=(0,0,0))
        if underline:
            d.line([(cx-tw//2,cy+th//2+1),(cx+tw//2,cy+th//2+1)],fill=(0,0,0),width=1)
    def rel(cx,cy,lbl,w=90,h=45):
        pts=[(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
        d.polygon(pts,fill=(255,255,255),outline=(0,0,0),width=1)
        txt_c(d,cx,cy,lbl,FS)
    def conn(x1,y1,x2,y2,card1="",card2=""):
        d.line([(x1,y1),(x2,y2)],fill=(0,0,0),width=1)
        if card1: d.text((x1+4,y1-14),card1,font=FS,fill=(0,0,0))
        if card2: d.text((x2-20,y2-14),card2,font=FS,fill=(0,0,0))

    # ── USERS ─────────────────────────────────────────────────────────────────
    UX,UY=800,120
    entity(UX,UY,"users",140,40)
    for ax,ay,lbl,ul in [(680,50,"id",True),(760,50,"name",False),(840,50,"email",False),
                          (920,50,"password",False),(700,170,"role",False),(900,170,"is_active",False)]:
        attr(ax,ay,lbl,ul); conn(ax,ay,UX,UY)

    # ── BARANG ────────────────────────────────────────────────────────────────
    BX,BY=300,500
    entity(BX,BY,"barang",140,40)
    for ax,ay,lbl,ul in [(150,400,"kode_barang",True),(280,400,"nama_barang",False),
                          (420,400,"kategori",False),(150,600,"status",False),(300,620,"keterangan",False)]:
        attr(ax,ay,lbl,ul); conn(ax,ay,BX,BY)

    # ── RUANGAN ───────────────────────────────────────────────────────────────
    RX,RY=800,500
    entity(RX,RY,"ruangan",140,40)
    for ax,ay,lbl,ul in [(660,420,"id",True),(780,420,"nama",False),
                          (900,420,"lantai",False),(800,600,"keterangan",False)]:
        attr(ax,ay,lbl,ul); conn(ax,ay,RX,RY)

    # ── ASET ──────────────────────────────────────────────────────────────────
    AX,AY=1250,500
    entity(AX,AY,"aset",140,40)
    for ax,ay,lbl,ul in [(1100,400,"kode_aset",True),(1220,400,"kondisi",False),
                          (1360,400,"status",False),(1480,400,"serial_number",False),
                          (1100,600,"jumlah",False),(1220,600,"tanggal_perolehan",False),
                          (1380,600,"harga_perolehan",False),(1500,600,"sumber_perolehan",False),
                          (1250,680,"keterangan",False)]:
        attr(ax,ay,lbl,ul); conn(ax,ay,AX,AY)

    # ── LOG_AKTIVITAS ─────────────────────────────────────────────────────────
    LX,LY=1350,120
    entity(LX,LY,"log_aktivitas",160,40)
    for ax,ay,lbl,ul in [(1200,50,"id",True),(1320,50,"aktivitas",False),
                          (1460,50,"keterangan",False),(1550,50,"ip_address",False)]:
        attr(ax,ay,lbl,ul); conn(ax,ay,LX,LY)

    # ── RELATIONS ─────────────────────────────────────────────────────────────
    # barang 1--N aset
    rel(780,500,"memiliki",90,40)
    conn(BX+70,BY,780-45,500,"1","N")
    conn(780+45,500,AX-70,AY,"","")

    # ruangan 1--N aset
    rel(1025,500,"menampung",100,40)
    conn(RX+70,RY,1025-50,500,"1","N")
    conn(1025+50,500,AX-70,AY,"","")

    # users 1--N aset (created_by)
    rel(1025,300,"membuat",90,40)
    conn(UX+70,UY,1025-45,300,"1","N")
    conn(1025+45,300,AX-70,AY-30,"","")

    # users 1--N log_aktivitas
    rel(1075,120,"mencatat",90,40)
    conn(UX+70,UY,1075-45,120,"1","N")
    conn(1075+45,120,LX-80,LY,"","")

    img.save(f"{OUT}/11_ERD.png","PNG",dpi=(150,150))
    print("  11_ERD.png")

gen_erd()

# ═════════════════════════════════════════════════════════════════════════════
# 12. USE CASE DIAGRAM
# ═════════════════════════════════════════════════════════════════════════════
def gen_usecase():
    W,H=1400,1000
    img=Image.new("RGB",(W,H),(245,245,245))
    d=ImageDraw.Draw(img)
    FB=get_font(12); FS=get_font(10); FH=get_font(12,bold=True); FT=get_font(13,bold=True)

    # outer boundary
    d.rectangle([10,10,W-10,H-10],fill=(255,255,255),outline=(0,0,0),width=1)
    d.text((16,14),"uc  Use Case Diagram — SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))

    # system boundary
    d.rectangle([120,40,W-120,H-40],fill=(255,255,250),outline=(0,0,0),width=1)
    d.text((130,44),"Sistem Informasi Manajemen Aset (SimAset)",font=FH,fill=(0,0,0))

    def actor(cx,cy,lbl):
        # head
        d.ellipse([cx-12,cy-50,cx+12,cy-26],fill=(255,255,255),outline=(0,0,0),width=1)
        # body
        d.line([(cx,cy-26),(cx,cy+10)],fill=(0,0,0),width=1)
        # arms
        d.line([(cx-20,cy-10),(cx+20,cy-10)],fill=(0,0,0),width=1)
        # legs
        d.line([(cx,cy+10),(cx-15,cy+35)],fill=(0,0,0),width=1)
        d.line([(cx,cy+10),(cx+15,cy+35)],fill=(0,0,0),width=1)
        bb=d.textbbox((0,0),lbl,font=FB)
        tw=bb[2]-bb[0]
        d.text((cx-tw//2,cy+40),lbl,font=FB,fill=(0,0,0))

    def uc(cx,cy,lbl,w=140,h=40):
        d.ellipse([cx-w//2,cy-h//2,cx+w//2,cy+h//2],fill=(255,255,204),outline=(0,0,0),width=1)
        lines=lbl.split("\n"); lh=FB.size+2; total=lh*len(lines); y=cy-total//2
        for ln in lines:
            bb=d.textbbox((0,0),ln,font=FB); tw=bb[2]-bb[0]
            d.text((cx-tw//2,y),ln,font=FB,fill=(0,0,0)); y+=lh

    def arr_uc(x1,y1,x2,y2,lbl="",dashed=False):
        if dashed:
            dx,dy=x2-x1,y2-y1; length=max(1,math.sqrt(dx*dx+dy*dy))
            steps=int(length/8)
            for i in range(steps):
                t1=i/steps; t2=min(1,(i+0.5)/steps)
                if i%2==0:
                    d.line([(int(x1+dx*t1),int(y1+dy*t1)),(int(x1+dx*t2),int(y1+dy*t2))],fill=(0,0,0),width=1)
        else:
            d.line([(x1,y1),(x2,y2)],fill=(0,0,0),width=1)
        ang=math.atan2(y2-y1,x2-x1); sz=7
        for da in [0.4,-0.4]:
            ax=x2-sz*math.cos(ang-da); ay=y2-sz*math.sin(ang-da)
            d.line([(x2,y2),(int(ax),int(ay))],fill=(0,0,0),width=1)
        if lbl:
            mx,my=(x1+x2)//2,(y1+y2)//2
            bb=d.textbbox((0,0),lbl,font=FS); tw=bb[2]-bb[0]
            d.text((mx-tw//2,my-14),lbl,font=FS,fill=(80,80,80))

    # Actors
    actor(60,500,"Admin")
    actor(W-60,500,"Staff")

    # Use cases — grouped
    # Auth
    uc(350,120,"Login",120,36); uc(550,120,"Logout",120,36)
    uc(750,120,"Lupa Password",140,36); uc(950,120,"Reset Password",140,36)

    # Aset
    uc(280,240,"Lihat Daftar Aset",160,36); uc(480,240,"Tambah Aset",130,36)
    uc(660,240,"Edit Aset",110,36); uc(820,240,"Hapus Aset",110,36)
    uc(980,240,"Detail Aset",120,36); uc(1150,240,"Hapus Massal",130,36)

    # Barang & Ruangan
    uc(280,360,"Kelola Barang\n(CRUD)",130,44); uc(480,360,"Kelola Ruangan\n(CRUD)",130,44)

    # QR & Maintenance
    uc(680,360,"Generate QR",130,36); uc(850,360,"Scan QR",110,36)
    uc(1000,360,"Cetak QR Massal",150,36); uc(1180,360,"Maintenance",120,36)

    # Import/Export/Laporan
    uc(280,480,"Import Aset/Barang",160,36); uc(500,480,"Export Aset/Barang",160,36)
    uc(720,480,"Laporan PDF/Excel",160,36); uc(940,480,"Laporan Per Ruangan",170,36)
    uc(1160,480,"Laporan Maintenance",170,36)

    # Admin only
    uc(400,620,"Kelola Pengguna\n(Admin Only)",160,44); uc(700,620,"Lihat Audit Log\n(Admin Only)",160,44)
    uc(1000,620,"Filter Audit Log",150,36)

    # Profil
    uc(700,760,"Edit Profil",120,36); uc(900,760,"Ganti Password",140,36)

    # Arrows: Admin → all
    for tx,ty in [(350,120),(550,120),(750,120),(950,120),
                  (280,240),(480,240),(660,240),(820,240),(980,240),(1150,240),
                  (280,360),(480,360),(680,360),(850,360),(1000,360),(1180,360),
                  (280,480),(500,480),(720,480),(940,480),(1160,480),
                  (400,620),(700,620),(1000,620),(700,760),(900,760)]:
        arr_uc(100,500,tx,ty)

    # Staff → subset
    for tx,ty in [(350,120),(550,120),(750,120),(950,120),
                  (280,240),(480,240),(660,240),(820,240),(980,240),(1150,240),
                  (280,360),(480,360),(680,360),(850,360),(1000,360),(1180,360),
                  (280,480),(500,480),(720,480),(940,480),(1160,480),
                  (700,760),(900,760)]:
        arr_uc(W-100,500,tx,ty)

    # include/extend
    arr_uc(850,360,980,240,"<<include>>",dashed=True)
    arr_uc(1000,620,700,620,"<<extend>>",dashed=True)

    img.save(f"{OUT}/12_UseCase.png","PNG",dpi=(150,150))
    print("  12_UseCase.png")

gen_usecase()

# ═════════════════════════════════════════════════════════════════════════════
# 13. SEQUENCE DIAGRAM — LOGIN
# ═════════════════════════════════════════════════════════════════════════════
def gen_sequence_login():
    W,H=1500,1100
    img=Image.new("RGB",(W,H),(255,255,255))
    d=ImageDraw.Draw(img)
    FB=get_font(12); FS=get_font(10); FH=get_font(12,bold=True); FT=get_font(13,bold=True)

    d.rectangle([10,10,W-10,H-10],outline=(0,0,0),width=1)
    d.text((16,14),"sd  Sequence Diagram — Login SimAset RBTV Bengkulu",font=FT,fill=(0,0,0))

    # Participants
    parts = [
        (":Admin",        80),
        (":Browser",      260),
        (":Router",       430),
        (":AuthController",600),
        (":LoginRequest", 780),
        (":RateLimiter",  950),
        (":User (Model)", 1110),
        (":Database",     1300),
        (":ActivityLogger",1460),
    ]
    TOP_Y = 50
    BOX_H = 50
    LIFE_Y2 = H - 60

    # Draw lifeline headers + dashed lines
    for lbl,x in parts:
        bw = max(110, len(lbl)*8)
        d.rectangle([x-bw//2, TOP_Y, x+bw//2, TOP_Y+BOX_H],
                    fill=(255,255,204), outline=(0,0,0), width=1)
        txt_c(d, x, TOP_Y+BOX_H//2, lbl, FS)
        # dashed lifeline
        y=TOP_Y+BOX_H
        while y < LIFE_Y2:
            d.line([(x,y),(x,min(y+6,LIFE_Y2))],fill=(180,180,180),width=1)
            y+=12

    def msg(x1,y,x2,lbl,ret=False,num=""):
        color=(0,0,0)
        if ret:
            # dashed return
            dx,dy2=x2-x1,0; length=abs(dx); steps=int(length/8)
            for i in range(steps):
                t1=i/steps; t2=min(1,(i+0.5)/steps)
                if i%2==0:
                    d.line([(int(x1+dx*t1),y),(int(x1+dx*t2),y)],fill=color,width=1)
        else:
            d.line([(x1,y),(x2,y)],fill=color,width=1)
        # arrowhead
        if x2>x1:
            d.polygon([(x2,y),(x2-8,y-4),(x2-8,y+4)],fill=color)
        else:
            d.polygon([(x2,y),(x2+8,y-4),(x2+8,y+4)],fill=color)
        # label
        mx=(x1+x2)//2
        full=f"{num}: {lbl}" if num else lbl
        bb=d.textbbox((0,0),full,font=FS); tw=bb[2]-bb[0]
        d.text((mx-tw//2,y-14),full,font=FS,fill=(0,0,0))

    # activation boxes
    def act_box(x,y1,y2,w=12):
        d.rectangle([x-w//2,y1,x+w//2,y2],fill=(255,255,255),outline=(0,0,0),width=1)

    xs = {lbl:x for lbl,x in parts}
    y = TOP_Y+BOX_H+30

    msg(xs[":Admin"],y,xs[":Browser"],"Buka /login",num="1"); y+=40
    msg(xs[":Browser"],y,xs[":Router"],"GET /login [guest]",num="2"); y+=35
    msg(xs[":Router"],y,xs[":AuthController"],"create()",num="3"); y+=35
    msg(xs[":AuthController"],y,xs[":Browser"],"view(auth.login)",ret=True,num="4"); y+=40
    msg(xs[":Browser"],y,xs[":Admin"],"Halaman login",ret=True); y+=45

    msg(xs[":Admin"],y,xs[":Browser"],"Input email+password → Klik Masuk",num="5"); y+=40
    msg(xs[":Browser"],y,xs[":Router"],"POST /login {email,password}",num="6"); y+=35
    msg(xs[":Router"],y,xs[":AuthController"],"store(LoginRequest)",num="7"); y+=35
    msg(xs[":AuthController"],y,xs[":LoginRequest"],"validate()",num="8"); y+=35
    msg(xs[":LoginRequest"],y,xs[":RateLimiter"],"tooManyAttempts(key,5)",num="9"); y+=35
    msg(xs[":RateLimiter"],y,xs[":LoginRequest"],"false",ret=True); y+=35
    msg(xs[":LoginRequest"],y,xs[":User (Model)"],"where(email)->first()",num="10"); y+=35
    msg(xs[":User (Model)"],y,xs[":Database"],"SELECT * FROM users WHERE email=?",num="11"); y+=35
    msg(xs[":Database"],y,xs[":User (Model)"],"User record",ret=True); y+=35
    msg(xs[":User (Model)"],y,xs[":LoginRequest"],"$user",ret=True); y+=35
    msg(xs[":LoginRequest"],y,xs[":LoginRequest"],"Cek is_active=1",num="12"); y+=35
    msg(xs[":LoginRequest"],y,xs[":LoginRequest"],"Auth::attempt(email,pwd)",num="13"); y+=35
    msg(xs[":LoginRequest"],y,xs[":RateLimiter"],"clear(key)",num="14"); y+=35
    msg(xs[":AuthController"],y,xs[":AuthController"],"session()->regenerate()",num="15"); y+=35
    msg(xs[":AuthController"],y,xs[":User (Model)"],"update([last_login_at=>now()])",num="16"); y+=35
    msg(xs[":User (Model)"],y,xs[":Database"],"UPDATE users SET last_login_at=NOW()"); y+=35
    msg(xs[":AuthController"],y,xs[":ActivityLogger"],"logAuth('Login','User berhasil login...')",num="17"); y+=35
    msg(xs[":ActivityLogger"],y,xs[":Database"],"INSERT INTO log_aktivitas"); y+=35
    msg(xs[":AuthController"],y,xs[":Browser"],"redirect()->route('dashboard') [302]",ret=True,num="18"); y+=35
    msg(xs[":Browser"],y,xs[":Admin"],"Diarahkan ke /dashboard",ret=True); y+=35

    img.save(f"{OUT}/13_Sequence_Login.png","PNG",dpi=(150,150))
    print("  13_Sequence_Login.png")

gen_sequence_login()

print("\nSemua diagram PNG selesai dibuat di folder:", OUT)
