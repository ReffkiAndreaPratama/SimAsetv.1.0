"""
Diagram Activity & Sequence per fitur — compact, no wasted space
Gaya: putih, kotak rounded kuning muda, swimlane tipis, font Arial
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = "docs/diagrams/png"
os.makedirs(OUT, exist_ok=True)

# ─── COLORS ──────────────────────────────────────────────────────────────────
BG       = (255,255,255)
SW_BG    = (255,255,245)
SW_HDR   = (255,255,210)
SW_BD    = (0,0,0)
BOX_F    = (255,255,204)
BOX_BD   = (140,140,100)
DIA_F    = (255,255,255)
DIA_BD   = (60,60,60)
BLACK    = (0,0,0)
GRAY     = (100,100,100)
LGRAY    = (180,180,180)

# ─── FONTS ───────────────────────────────────────────────────────────────────
def F(size, bold=False):
    for p in (["C:/Windows/Fonts/arialbd.ttf"] if bold else
              ["C:/Windows/Fonts/arial.ttf","C:/Windows/Fonts/calibri.ttf"]):
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

# ─── PRIMITIVES ──────────────────────────────────────────────────────────────
def tc(d, cx, cy, txt, font, color=BLACK):
    lines = txt.split("\n")
    lh = font.size + 2
    y = cy - lh*len(lines)//2
    for ln in lines:
        bb = d.textbbox((0,0),ln,font=font)
        d.text((cx-(bb[2]-bb[0])//2, y), ln, font=font, fill=color)
        y += lh

def box(d, cx, cy, txt, w, h, font):
    x0,y0 = cx-w//2, cy-h//2
    d.rounded_rectangle([x0,y0,x0+w,y0+h], radius=7, fill=BOX_F, outline=BOX_BD, width=1)
    tc(d, cx, cy, txt, font)
    return y0, y0+h          # top, bot

def dia(d, cx, cy, txt, w, h, font):
    pts = [(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
    d.polygon(pts, fill=DIA_F, outline=DIA_BD, width=1)
    tc(d, cx, cy, txt, font, GRAY)
    return cy-h//2, cy+h//2

def arr(d, x1,y1,x2,y2, lbl="", font=None, side="top"):
    d.line([(x1,y1),(x2,y2)], fill=BLACK, width=1)
    ang = math.atan2(y2-y1,x2-x1); s=7
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)
    if lbl and font:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=d.textbbox((0,0),lbl,font=font); tw=bb[2]-bb[0]
        dy = -13 if side=="top" else 3
        d.text((mx-tw//2, my+dy), lbl, font=font, fill=GRAY)

def darr(d, x1,y1,x2,y2, lbl="", font=None):
    """dashed arrow"""
    dx,dy=x2-x1,y2-y1; L=max(1,math.hypot(dx,dy)); n=int(L/7)
    for i in range(n):
        if i%2==0:
            t1,t2=i/n,min(1,(i+.5)/n)
            d.line([(int(x1+dx*t1),int(y1+dy*t1)),(int(x1+dx*t2),int(y1+dy*t2))],fill=BLACK,width=1)
    ang=math.atan2(dy,dx); s=7
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)
    if lbl and font:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=d.textbbox((0,0),lbl,font=font); tw=bb[2]-bb[0]
        d.text((mx-tw//2,my-13),lbl,font=font,fill=GRAY)

def fbar(d, x0,y,x1): d.rectangle([x0,y-4,x1,y+4],fill=BLACK)

def snode(d,cx,cy,r=9): d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)

def enode(d,cx,cy,r=9):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
    d.ellipse([cx-r+3,cy-r+3,cx+r-3,cy+r-3],fill=BG)
    d.ellipse([cx-r+6,cy-r+6,cx+r-6,cy+r-6],fill=BLACK)

def vline(d,x,y1,y2): d.line([(x,y1),(x,y2)],fill=BLACK,width=1)
def hline(d,x1,y,x2): d.line([(x1,y),(x2,y)],fill=BLACK,width=1)

# ─── SWIMLANE BUILDER ────────────────────────────────────────────────────────
def make_canvas(title, lanes, content_h, pad=14):
    """
    lanes: list of (label, width)
    Returns (img, draw, [cx_list], y_content_start, HDR_H, PAD)
    """
    HDR_H = 28; TITLE_H = 22; PAD = pad
    total_w = sum(w for _,w in lanes)
    W = total_w + PAD*2
    H = TITLE_H + HDR_H + content_h + PAD*2
    img = Image.new("RGB",(W,H),BG)
    d   = ImageDraw.Draw(img)
    FT  = F(11,bold=True); FH = F(11,bold=True)

    # outer border
    d.rectangle([PAD,PAD,W-PAD,H-PAD],outline=BLACK,width=1)
    # title
    d.text((PAD+4,PAD+3), title, font=FT, fill=BLACK)

    # swimlane backgrounds + headers
    x = PAD
    cxs = []
    y0 = PAD+TITLE_H
    for lbl,w in lanes:
        d.rectangle([x,y0,x+w,H-PAD],fill=SW_BG,outline=BLACK,width=1)
        d.rectangle([x,y0,x+w,y0+HDR_H],fill=SW_HDR,outline=BLACK,width=1)
        cx = x+w//2; cxs.append(cx)
        bb=d.textbbox((0,0),lbl,font=FH); tw=bb[2]-bb[0]
        d.text((cx-tw//2,y0+HDR_H//2-FH.size//2),lbl,font=FH,fill=BLACK)
        x += w

    y_start = y0+HDR_H+18
    return img, d, cxs, y_start

def save(img, name):
    p = f"{OUT}/{name}"
    img.save(p,"PNG",dpi=(150,150))
    print(f"  {name}")

# ═══════════════════════════════════════════════════════════════════════════
# ACT-01  LOGIN & LOGOUT
# ═══════════════════════════════════════════════════════════════════════════
def act_login():
    FB=F(12); FS=F(10)
    img,d,cxs,y = make_canvas("act  Login & Logout — SimAset",
                               [("Pengguna",340),("Sistem",420)], 820)
    C1,C2 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38
    box(d,C1,y,"Login",130,28,FB); arr(d,C1+65,y,C2-100,y,font=FS)
    box(d,C2,y,"Menampilkan Halaman Login",230,28,FB)
    darr(d,C2-115,y+14,C1+65,y+14); arr(d,C1,y+14,C1,y+38); y+=52

    box(d,C1,y,"Input Email & Password",200,28,FB); arr(d,C1+100,y,C2-100,y,font=FS)
    box(d,C2,y,"Validasi Input\n(email required, password required)",260,36,FB)
    arr(d,C2,y+18,C2,y+42); y+=56

    td,bd = dia(d,C2,y+24,"Input\nvalid?",100,48,FS)
    arr(d,C2,bd,C2,bd+20,"Ya",FS)
    arr(d,C2+50,y+24,C2+160,y+24,font=FS,side="top")
    d.text((C2+165,y+16),"Tidak",font=FS,fill=GRAY)
    box(d,C2+240,y+24,"Tampilkan\nerror field",110,36,FB)
    darr(d,C2+240,y+6,C1+100,y+6)
    y = bd+38

    box(d,C2,y,"Cek Rate Limit\n(5x/menit per email+IP)",220,36,FB)
    arr(d,C2,y+18,C2,y+42); y+=56

    td,bd = dia(d,C2,y+24,"Rate limit?",100,44,FS)
    arr(d,C2,bd,C2,bd+20,"Tidak",FS)
    arr(d,C2+50,y+24,C2+160,y+24,font=FS)
    d.text((C2+165,y+16),"Ya",font=FS,fill=GRAY)
    box(d,C2+240,y+24,"Error:\nTerlalu banyak\npercobaan",110,44,FB)
    y = bd+38

    box(d,C2,y,"Cari user by email\nCek is_active = 1\nAuth::attempt(email, pwd)",240,48,FB)
    arr(d,C2,y+24,C2,y+52); y+=66

    td,bd = dia(d,C2,y+22,"Kredensial\nbenar?",100,44,FS)
    arr(d,C2,bd,C2,bd+20,"Ya",FS)
    arr(d,C2+50,y+22,C2+160,y+22,font=FS)
    d.text((C2+165,y+14),"Tidak",font=FS,fill=GRAY)
    box(d,C2+240,y+22,"Error:\nKredensial\ntidak cocok",110,44,FB)
    darr(d,C2+240,y+4,C1+100,y+4)
    y = bd+38

    box(d,C2,y,"session()->regenerate()\nUpdate last_login_at\nActivityLogger::logAuth('Login',...)",280,48,FB)
    arr(d,C2,y+24,C2,y+52); y+=66

    box(d,C2,y,"redirect()->route('dashboard')",230,28,FB)
    darr(d,C2-115,y,C1+100,y)
    box(d,C1,y,"Melihat Dashboard",180,28,FB)
    arr(d,C1,y+14,C1,y+38); y+=52

    # LOGOUT
    d.line([(14,y-4),(img.width-14,y-4)],fill=LGRAY,width=1)
    d.text((C1-60,y),"— Logout —",font=FS,fill=GRAY); y+=18

    box(d,C1,y,'Klik "Logout"',150,28,FB); arr(d,C1+75,y,C2-100,y,font=FS)
    box(d,C2,y,"logAuth('Logout',...)\nAuth::logout()\nsession()->invalidate()",240,48,FB)
    arr(d,C2-120,y+24,C1+75,y+24)
    box(d,C1,y+24,"Kembali ke /login",170,28,FB)
    arr(d,C1,y+38,C1,y+62); y+=76

    enode(d,C1,y)
    save(img,"ACT_01_Login.png")

act_login()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-02  MANAJEMEN ASET (CRUD + QR + Maintenance)
# ═══════════════════════════════════════════════════════════════════════════
def act_aset():
    FB=F(12); FS=F(10)
    img,d,cxs,y = make_canvas("act  Manajemen Aset (CRUD + QR) — SimAset",
                               [("Pengguna",340),("Sistem",460)], 1380)
    C1,C2 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38
    box(d,C1,y,'Pilih menu "Aset"',180,28,FB)
    arr(d,C1+90,y,C2-130,y,font=FS)
    box(d,C2,y,"Asset::with([barang,ruangan])\n->orderBy('kode_aset')->paginate(15)\nTampilkan daftar + stats + filter",300,48,FB)
    darr(d,C2-150,y+24,C1+90,y+24)
    arr(d,C1,y+14,C1,y+42); y+=60

    td,bd = dia(d,C1,y+26,"Pilih\naksi?",110,52,FS); y=bd+16

    # ── TAMBAH ──
    d.text((C1-155,y+4),"Tambah",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Isi Form Aset\n(Barang*, Ruangan*, Kondisi*,\nStatus*, Tgl Perolehan*, Serial,\nJumlah, Harga, Sumber, Foto)",220,64,FB)
    arr(d,C1+110,y+32,C2-130,y+32,font=FS)
    box(d,C2,y,"Validasi server-side\n→ generateKode() gap-filling\n→ simpan foto ke public/foto_aset/\n→ Asset::create([..., created_by])\n→ ActivityLogger::logAsset('Create',...)",320,72,FB)
    arr(d,C1,y+32,C1,y+80); y+=96

    # ── EDIT ──
    d.text((C1-145,y+4),"Edit",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Klik Edit (✏)\npada baris aset",180,36,FB)
    arr(d,C1+90,y+18,C2-130,y+18,font=FS)
    box(d,C2,y,"Load aset + dropdown Barang & Ruangan\n→ Tampilkan form edit terisi\n→ Validasi → $asset->update([..., updated_by])\n→ logAsset('Update',...)",320,56,FB)
    arr(d,C1,y+18,C1,y+52); y+=68

    # ── HAPUS ──
    d.text((C1-155,y+4),"Hapus",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Klik Hapus (🗑)\nKonfirmasi SweetAlert2",200,36,FB)
    arr(d,C1+100,y+18,C2-130,y+18,font=FS)
    box(d,C2,y,"$asset->delete() [Soft Delete: isi deleted_at]\n→ logAsset('Delete',...)\n→ redirect + flash success",320,48,FB)
    arr(d,C1,y+18,C1,y+52); y+=68

    # ── HAPUS MASSAL ──
    d.text((C1-175,y+4),"Batch\nHapus",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Centang beberapa aset\nKlik 'Hapus Terpilih'",200,36,FB)
    arr(d,C1+100,y+18,C2-130,y+18,font=FS)
    box(d,C2,y,"POST /aset/batch-destroy {kodes[]}\nLoop: $asset->delete() + log\n→ redirect + flash 'X aset dihapus'",320,48,FB)
    arr(d,C1,y+18,C1,y+52); y+=68

    # ── DETAIL ──
    d.text((C1-155,y+4),"Detail",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Klik Detail (👁)",160,28,FB)
    arr(d,C1+80,y,C2-130,y,font=FS)
    box(d,C2,y,"Asset::with([barang,ruangan,creator,updater])\n→ view(aset.show)",320,36,FB)
    darr(d,C2-160,y,C1+80,y)
    arr(d,C1,y+14,C1,y+38); y+=52

    # ── GENERATE QR ──
    d.text((C1-165,y+4),"Generate\nQR",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Klik 'Generate QR Code'",200,28,FB)
    arr(d,C1+100,y,C2-130,y,font=FS)
    box(d,C2,y,"Cek file QR ada?\n→ Request API qrserver.com\n→ Simpan PNG ke public/qr_codes/\n→ redirect + success",320,56,FB)
    arr(d,C1,y+14,C1,y+42); y+=58

    # ── SET MAINTENANCE ──
    d.text((C1-175,y+4),"Set\nMaint.",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Klik 'Set Maintenance'",200,28,FB)
    arr(d,C1+100,y,C2-130,y,font=FS)
    box(d,C2,y,"update([status=>'Maintenance', updated_by])\n→ logAsset('Update','Aset masuk maintenance...')",320,36,FB)
    arr(d,C1,y+14,C1,y+38); y+=52

    arr(d,C1,y,C1,y+24); y+=24
    enode(d,C1,y)
    save(img,"ACT_02_Aset.png")

act_aset()

# ═══════════════════════════════════════════════════════════════════════════
# GENERIC CRUD ACTIVITY
# ═══════════════════════════════════════════════════════════════════════════
def act_crud(title, menu_label, actions, filename, extra_note=""):
    """
    actions: list of (user_label, sys_label)
    """
    FB=F(12); FS=F(10)
    content_h = 60 + len(actions)*80 + (40 if extra_note else 0) + 60
    img,d,cxs,y = make_canvas(title, [("Pengguna",340),("Sistem",460)], content_h)
    C1,C2 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38
    box(d,C1,y,f'Pilih menu "{menu_label}"',200,28,FB)
    arr(d,C1+100,y,C2-130,y,font=FS)
    box(d,C2,y,f"Query {menu_label} dari database\n→ Tampilkan daftar (tabel + filter)",300,36,FB)
    darr(d,C2-150,y+18,C1+100,y+18)
    arr(d,C1,y+14,C1,y+42); y+=56

    td,bd = dia(d,C1,y+26,"Pilih\naksi?",110,52,FS); y=bd+16

    for i,(ulbl,slbl) in enumerate(actions):
        lines_u = ulbl.count("\n")+1; lines_s = slbl.count("\n")+1
        h = max(lines_u,lines_s)*16+20
        d.text((C1-len(ulbl.split("\n")[0])*6-30, y+h//2-8), ulbl.split("\n")[0], font=FS, fill=GRAY)
        arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+h//2); arr(d,C1-130,y+h//2,C1-80,y+h//2)
        box(d,C1,y,ulbl,200,h,FB)
        arr(d,C1+100,y+h//2,C2-130,y+h//2,font=FS)
        box(d,C2,y,slbl,320,h,FB)
        arr(d,C1,y+h,C1,y+h+16); y+=h+24

    if extra_note:
        d.text((C2-150,y), extra_note, font=FS, fill=GRAY); y+=18

    arr(d,C1,y,C1,y+20); y+=20
    enode(d,C1,y)
    save(img, filename)

# ═══════════════════════════════════════════════════════════════════════════
# ACT-03  MANAJEMEN BARANG
# ═══════════════════════════════════════════════════════════════════════════
act_crud(
    "act  Manajemen Barang (CRUD) — SimAset",
    "Barang",
    [
        ("Tambah Barang",
         "Validasi (nama*, kategori*, status*)\n→ generateKode() [BRG-001, BRG-002,...]\n→ Barang::create()\n→ redirect + success"),
        ("Edit Barang",
         "Load barang → Form edit terisi\n→ Validasi → $barang->update()\n→ redirect + success"),
        ("Hapus Barang\n(Soft Delete)",
         "$barang->delete() [isi deleted_at]\n→ redirect + success"),
        ("Lihat Detail\nBarang",
         "Barang::with([aset])->findOrFail()\n→ view(barang.show)\n→ Tampilkan detail + daftar aset"),
    ],
    "ACT_03_Barang.png",
    extra_note="Kode Barang di-generate otomatis (gap-filling)"
)

# ═══════════════════════════════════════════════════════════════════════════
# ACT-04  MANAJEMEN RUANGAN
# ═══════════════════════════════════════════════════════════════════════════
act_crud(
    "act  Manajemen Ruangan (CRUD) — SimAset",
    "Ruangan",
    [
        ("Tambah Ruangan",
         "Validasi (nama*, lantai, keterangan)\n→ Ruangan::create()\n→ redirect + success"),
        ("Edit Ruangan",
         "Load ruangan → Form edit terisi\n→ Validasi → $ruangan->update()\n→ redirect + success"),
        ("Hapus Ruangan",
         "Cek: $ruangan->assets()->count() > 0?\n→ Jika ada aset: TOLAK + error\n→ Jika kosong: $ruangan->delete()"),
        ("Lihat Detail\nRuangan",
         "Ruangan::with([assets.barang])->findOrFail()\n→ view(ruangan.show)\n→ Tampilkan detail + daftar aset"),
    ],
    "ACT_04_Ruangan.png",
    extra_note="Validasi: Ruangan tidak bisa dihapus jika masih ada aset terdaftar"
)

# ═══════════════════════════════════════════════════════════════════════════
# ACT-05  KELOLA PENGGUNA (Admin Only)
# ═══════════════════════════════════════════════════════════════════════════
def act_pengguna():
    FB=F(12); FS=F(10)
    img,d,cxs,y = make_canvas("act  Kelola Pengguna (Admin Only) — SimAset",
                               [("Admin",340),("Sistem",460)], 900)
    C1,C2 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38
    box(d,C1,y,'Klik "Kelola Pengguna"',200,28,FB)
    arr(d,C1+100,y,C2-130,y,font=FS)
    box(d,C2,y,"Cek middleware role:admin\n(RoleMiddleware::handle())",280,36,FB)
    arr(d,C2,y+18,C2,y+42); y+=56

    td,bd = dia(d,C2,y+22,"Role =\nadmin?",100,44,FS)
    arr(d,C2,bd,C2,bd+20,"Ya",FS)
    arr(d,C2-50,y+22,C2-180,y+22,font=FS)
    d.text((C2-260,y+14),"Tidak",font=FS,fill=GRAY)
    box(d,C2-330,y+22,"HTTP 403\nForbidden",110,36,FB)
    y=bd+38

    box(d,C2,y,"User::orderBy('role')->get()\n→ view(users.index)",280,36,FB)
    darr(d,C2-140,y+18,C1+100,y+18)
    arr(d,C1,y+18,C1,y+42); y+=56

    td,bd = dia(d,C1,y+26,"Pilih\naksi?",110,52,FS); y=bd+16

    # TAMBAH
    d.text((C1-155,y+4),"Tambah",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Isi form:\nNama*, Email*, Password*\n(min 8, upper+lower+angka)\nRole*, Kirim Email?",220,64,FB)
    arr(d,C1+110,y+32,C2-130,y+32,font=FS)
    box(d,C2,y,"Validasi → Hash::make(password)\n→ User::create([..., is_active:true])\n→ Kirim AkunBaruMail (jika dicentang)\n→ redirect + success",300,64,FB)
    arr(d,C1,y+32,C1,y+80); y+=96

    # EDIT
    d.text((C1-145,y+4),"Edit",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Klik Edit pada pengguna",200,28,FB)
    arr(d,C1+100,y,C2-130,y,font=FS)
    box(d,C2,y,"Load user → Form edit\n→ Validasi → $user->update()\n→ redirect + success",300,48,FB)
    arr(d,C1,y+14,C1,y+52); y+=68

    # HAPUS
    d.text((C1-155,y+4),"Hapus",font=FS,fill=GRAY)
    arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+4); arr(d,C1-130,y+4,C1-80,y+4)
    box(d,C1,y,"Klik Hapus → Konfirmasi",200,28,FB)
    arr(d,C1+100,y,C2-130,y,font=FS)
    box(d,C2,y,"Cek: bukan akun sendiri\n→ $user->delete() [hard delete]\n→ redirect + success",300,48,FB)
    arr(d,C1,y+14,C1,y+52); y+=68

    arr(d,C1,y,C1,y+20); y+=20
    enode(d,C1,y)
    save(img,"ACT_05_Pengguna.png")

act_pengguna()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-06  SCANNER QR CODE
# ═══════════════════════════════════════════════════════════════════════════
def act_qr():
    FB=F(12); FS=F(10)
    img,d,cxs,y = make_canvas("act  Scanner QR Code — SimAset",
                               [("Pengguna",340),("Sistem",460)], 680)
    C1,C2 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38
    box(d,C1,y,'Klik menu "QR Scanner"',200,28,FB)
    arr(d,C1+100,y,C2-130,y,font=FS)
    box(d,C2,y,"GET /qrcode/scanner\n→ view(qrcode.scanner)\n→ Minta izin kamera browser",300,48,FB)
    darr(d,C2-150,y+24,C1+100,y+24)
    arr(d,C1,y+14,C1,y+42); y+=56

    box(d,C1,y,"Izinkan akses kamera",190,28,FB)
    arr(d,C1,y+14,C1,y+38); y+=52

    box(d,C1,y,"Arahkan kamera ke\nQR Code aset fisik",200,36,FB)
    arr(d,C1+100,y+18,C2-130,y+18,font=FS)
    box(d,C2,y,"Decode QR (JavaScript)\n→ Baca URL dari QR\n→ Parse kode_aset dari URL",300,48,FB)
    arr(d,C2,y+24,C2,y+52); y+=68

    box(d,C2,y,"GET /aset/{kode}/detail [route PUBLIK]\nAsset::with([barang,ruangan,creator])\n->where('kode_aset',$kode)->firstOrFail()",320,48,FB)
    arr(d,C2,y+24,C2,y+52); y+=64

    td,bd = dia(d,C2,y+22,"Aset\nditemukan?",100,44,FS)
    arr(d,C2,bd,C2,bd+20,"Ya",FS)
    arr(d,C2+50,y+22,C2+180,y+22,font=FS)
    d.text((C2+185,y+14),"Tidak",font=FS,fill=GRAY)
    box(d,C2+260,y+22,"HTTP 404\nAset tidak\nditemukan",110,44,FB)
    y=bd+38

    box(d,C2,y,"Tampilkan detail aset:\nNama Barang, Kategori, Ruangan,\nKondisi, Status, Serial, Tgl Perolehan",300,48,FB)
    darr(d,C2-150,y+24,C1+100,y+24)
    box(d,C1,y+24,"Melihat detail aset",180,28,FB)
    arr(d,C1,y+38,C1,y+62); y+=80

    enode(d,C1,y)
    save(img,"ACT_06_ScannerQR.png")

act_qr()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-07  IMPORT DATA
# ═══════════════════════════════════════════════════════════════════════════
def act_import():
    FB=F(12); FS=F(10)
    img,d,cxs,y = make_canvas("act  Import Data (Excel/CSV) — SimAset",
                               [("Pengguna",340),("Sistem",460)], 780)
    C1,C2 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38
    box(d,C1,y,'Pilih menu "Import"',190,28,FB)
    arr(d,C1+95,y,C2-130,y,font=FS)
    box(d,C2,y,"Tampilkan halaman import\n(pilih tipe: Aset / Barang)\n+ tombol Download Template",300,48,FB)
    darr(d,C2-150,y+24,C1+95,y+24)
    arr(d,C1,y+14,C1,y+42); y+=56

    td,bd = dia(d,C1,y+22,"Perlu\ntemplate?",100,44,FS)
    arr(d,C1,bd,C1,bd+20,"Tidak",FS)
    arr(d,C1-50,y+22,C1-160,y+22,font=FS)
    d.text((C1-230,y+14),"Ya",font=FS,fill=GRAY)
    vline(d,C1-160,y+22,bd+10); arr(d,C1-160,bd+10,C1-80,bd+10)
    box(d,C1-260,y+22,"Download\nTemplate\n(CSV)",100,48,FB)
    y=bd+28

    box(d,C1,y,"Pilih tipe (Aset / Barang)\nUpload file Excel/CSV\nKlik 'Import'",210,48,FB)
    arr(d,C1+105,y+24,C2-130,y+24,font=FS)
    box(d,C2,y,"POST /import {file, type}\nValidasi: mimes:xlsx,xls,csv\ntype in:aset,barang",300,48,FB)
    arr(d,C2,y+24,C2,y+52); y+=68

    td,bd = dia(d,C2,y+22,"File\nvalid?",100,44,FS)
    arr(d,C2,bd,C2,bd+20,"Ya",FS)
    arr(d,C2+50,y+22,C2+180,y+22,font=FS)
    d.text((C2+185,y+14),"Tidak",font=FS,fill=GRAY)
    box(d,C2+260,y+22,"Error:\nFormat\ntidak valid",110,44,FB)
    y=bd+38

    box(d,C2,y,"Baca setiap baris data\n→ Validasi per baris\n→ Asset::create() / Barang::create()\n→ Hitung: X berhasil, Y gagal",300,56,FB)
    arr(d,C2,y+28,C2,y+56); y+=72

    box(d,C2,y,"redirect + flash:\n'Import selesai: X berhasil, Y gagal'",300,36,FB)
    darr(d,C2-150,y+18,C1+105,y+18)
    box(d,C1,y+18,"Lihat hasil import\ndi daftar data",190,36,FB)
    arr(d,C1,y+36,C1,y+60); y+=76

    enode(d,C1,y)
    save(img,"ACT_07_Import.png")

act_import()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-08  EXPORT & LAPORAN
# ═══════════════════════════════════════════════════════════════════════════
def act_export():
    FB=F(12); FS=F(10)
    img,d,cxs,y = make_canvas("act  Export & Laporan — SimAset",
                               [("Pengguna",340),("Sistem",460)], 900)
    C1,C2 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38
    box(d,C1,y,'Pilih menu "Laporan"',190,28,FB)
    arr(d,C1+95,y,C2-130,y,font=FS)
    box(d,C2,y,"Tampilkan halaman laporan\n(daftar ruangan + jumlah aset)",300,36,FB)
    darr(d,C2-150,y+18,C1+95,y+18)
    arr(d,C1,y+14,C1,y+42); y+=56

    td,bd = dia(d,C1,y+26,"Pilih\njenis?",110,52,FS); y=bd+16

    for ulbl,slbl in [
        ("Laporan Aset\n(atur filter)",
         "GET /laporan/assets\nQuery aset dengan filter\n→ Tampilkan tabel hasil"),
        ("Cetak PDF\nLaporan Aset",
         "GET /laporan/assets/cetak\n→ Barryvdh DomPDF\n→ Download PDF (A4 landscape)"),
        ("Export Excel\nLaporan Aset",
         "GET /laporan/assets/export\n→ Maatwebsite Excel\n→ Download .xlsx"),
        ("Laporan Per\nRuangan",
         "GET /laporan/ruangan/{id}\n→ Query aset di ruangan\n→ DomPDF → Download PDF"),
        ("Laporan\nMaintenance PDF",
         "GET /laporan/maintenance/pdf\n→ Query status=Maintenance\n→ DomPDF → Download"),
        ("Laporan\nMaintenance CSV",
         "GET /laporan/maintenance/csv\n→ Query status=Maintenance\n→ Generate CSV → Download"),
    ]:
        lines_u=ulbl.count("\n")+1; lines_s=slbl.count("\n")+1
        h=max(lines_u,lines_s)*16+20
        d.text((C1-len(ulbl.split("\n")[0])*5-30,y+h//2-8),ulbl.split("\n")[0],font=FS,fill=GRAY)
        arr(d,C1-55,y-26,C1-130,y-26); vline(d,C1-130,y-26,y+h//2); arr(d,C1-130,y+h//2,C1-80,y+h//2)
        box(d,C1,y,ulbl,200,h,FB)
        arr(d,C1+100,y+h//2,C2-130,y+h//2,font=FS)
        box(d,C2,y,slbl,320,h,FB)
        arr(d,C1,y+h,C1,y+h+16); y+=h+24

    arr(d,C1,y,C1,y+20); y+=20
    enode(d,C1,y)
    save(img,"ACT_08_Export.png")

act_export()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-09  AUDIT LOG
# ═══════════════════════════════════════════════════════════════════════════
def act_auditlog():
    FB=F(12); FS=F(10)
    img,d,cxs,y = make_canvas("act  Audit Log (Activity Log) — SimAset",
                               [("Admin",340),("Sistem",460)], 560)
    C1,C2 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38
    box(d,C1,y,'Klik "Log Aktivitas"',190,28,FB)
    arr(d,C1+95,y,C2-130,y,font=FS)
    box(d,C2,y,"Cek middleware role:admin\nActivityLog::with('user')\n->orderBy('created_at','desc')->paginate(20)\n→ Tampilkan tabel log",300,56,FB)
    darr(d,C2-150,y+28,C1+95,y+28)
    arr(d,C1,y+14,C1,y+42); y+=72

    box(d,C1,y,"Atur filter (opsional):\n- Kata kunci\n- Pengguna\n- Modul (Login/Create/\n  Update/Delete)\nKlik 'Filter'",220,80,FB)
    arr(d,C1+110,y+40,C2-130,y+40,font=FS)
    box(d,C2,y,"Query dengan WHERE clause:\n- aktivitas LIKE %keyword%\n- user_id = $user_id\n- aktivitas LIKE %module%\n→ Tampilkan hasil (paginated 20/hal)",300,80,FB)
    darr(d,C2-150,y+40,C1+110,y+40)
    arr(d,C1,y+80,C1,y+104); y+=120

    box(d,C1,y,"Melihat riwayat\naktivitas pengguna",200,36,FB)
    arr(d,C1,y+18,C1,y+42); y+=56

    enode(d,C1,y)
    save(img,"ACT_09_AuditLog.png")

act_auditlog()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-10  MAINTENANCE
# ═══════════════════════════════════════════════════════════════════════════
def act_maintenance():
    FB=F(12); FS=F(10)
    img,d,cxs,y = make_canvas("act  Maintenance Aset — SimAset",
                               [("Staff / Admin",320),("Sistem",420),("Admin (Email)",220)], 900)
    C1,C2,C3 = cxs

    snode(d,C1,y); arr(d,C1,y+9,C1,y+28); y+=38

    # ── SET MAINTENANCE ──────────────────────────────────────────────────────
    d.line([(14,y-2),(img.width-14,y-2)],fill=LGRAY,width=1)
    d.text((C1-80,y+2),"— Set Aset ke Maintenance —",font=FS,fill=GRAY); y+=18

    box(d,C1,y,"Buka Detail Aset\nKlik 'Set Maintenance'",200,36,FB)
    arr(d,C1+100,y+18,C2-110,y+18,font=FS)
    box(d,C2,y,"Tampilkan modal konfirmasi\n+ input keterangan (opsional)",280,36,FB)
    darr(d,C2-140,y+18,C1+100,y+18)
    arr(d,C1,y+18,C1,y+52); y+=68

    box(d,C1,y,"Input keterangan\nKlik 'Konfirmasi'",200,36,FB)
    arr(d,C1+100,y+18,C2-110,y+18,font=FS)
    box(d,C2,y,"POST /maintenance/{kode}/set\nupdate([status=>'Maintenance',\nupdated_by=>auth()->id()])\n→ logAsset('Update','Aset masuk maintenance...')\n→ redirect back + success",280,72,FB)
    darr(d,C2-140,y+36,C1+100,y+36)
    arr(d,C1,y+18,C1,y+52); y+=88

    # ── SELESAIKAN MAINTENANCE ───────────────────────────────────────────────
    d.line([(14,y-2),(img.width-14,y-2)],fill=LGRAY,width=1)
    d.text((C1-90,y+2),"— Selesaikan Maintenance —",font=FS,fill=GRAY); y+=18

    box(d,C1,y,"Buka menu 'Maintenance'\nKlik 'Selesai' pada aset",200,36,FB)
    arr(d,C1+100,y+18,C2-110,y+18,font=FS)
    box(d,C2,y,"Tampilkan modal:\n- Pilih kondisi akhir (wajib)\n- Input keterangan",280,48,FB)
    darr(d,C2-140,y+24,C1+100,y+24)
    arr(d,C1,y+18,C1,y+52); y+=68

    box(d,C1,y,"Pilih kondisi akhir\n(Baik/Rusak Ringan/Rusak Berat)\nKlik 'Konfirmasi Selesai'",210,48,FB)
    arr(d,C1+105,y+24,C2-110,y+24,font=FS)
    box(d,C2,y,"PATCH /maintenance/{kode}/complete\nValidasi: kondisi required",280,36,FB)
    arr(d,C2,y+18,C2,y+42); y+=58

    td,bd = dia(d,C2,y+22,"Validasi\ngagal?",100,44,FS)
    arr(d,C2,bd,C2,bd+20,"Tidak",FS)
    arr(d,C2+50,y+22,C2+160,y+22,font=FS)
    d.text((C2+165,y+14),"Ya",font=FS,fill=GRAY)
    box(d,C2+230,y+22,"Error:\nkondisi\nwajib diisi",100,44,FB)
    y=bd+38

    box(d,C2,y,"update([status=>'Aktif',\nkondisi=>$request->kondisi,\nupdated_by=>auth()->id()])\n→ logAsset('Update','Maintenance selesai...')\n→ Query Admin aktif\n→ Mail::to()->send(MaintenanceAlert)",280,88,FB)
    arr(d,C2+140,y+44,C3-60,y+44,font=FS)
    box(d,C3,y+44,"Terima email:\n'Maintenance\nSelesai'\n{nama} ({kode})\nKondisi: {kondisi}",160,72,FB)
    darr(d,C2-140,y+44,C1+105,y+44)
    box(d,C1,y+44,"Aset kembali\nberstatus Aktif",190,36,FB)
    arr(d,C1,y+62,C1,y+86); y+=104

    enode(d,C1,y)
    save(img,"ACT_10_Maintenance.png")

act_maintenance()

# ═══════════════════════════════════════════════════════════════════════════
# SEQUENCE DIAGRAM BUILDER  (compact, no wasted space)
# ═══════════════════════════════════════════════════════════════════════════
def make_seq(title, parts, msgs):
    """
    parts: [(label, x_center)]
    msgs:  [(src_label, tgt_label, text, is_return, is_self)]
    """
    FS=F(10); FH=F(11,bold=True); FT=F(11,bold=True)
    BOX_W=120; BOX_H=36; MSG_GAP=28
    PAD=12; TITLE_H=20; HDR_BOT=PAD+TITLE_H+BOX_H

    # auto-size width
    max_x = max(x for _,x in parts)
    W = max_x + BOX_W//2 + PAD + 20
    H = HDR_BOT + len(msgs)*MSG_GAP + 60
    img = Image.new("RGB",(W,H),BG)
    d   = ImageDraw.Draw(img)

    # border + title
    d.rectangle([PAD,PAD,W-PAD,H-PAD],outline=BLACK,width=1)
    d.text((PAD+4,PAD+3),title,font=FT,fill=BLACK)

    # lifeline headers
    xs = {lbl:x for lbl,x in parts}
    for lbl,x in parts:
        bw=max(BOX_W, len(lbl)*7+16)
        d.rectangle([x-bw//2,PAD+TITLE_H,x+bw//2,PAD+TITLE_H+BOX_H],
                    fill=(255,255,204),outline=BLACK,width=1)
        lines=lbl.split("\n"); lh=FS.size+2; total=lh*len(lines)
        yy=PAD+TITLE_H+BOX_H//2-total//2
        for ln in lines:
            bb=d.textbbox((0,0),ln,font=FS); tw=bb[2]-bb[0]
            d.text((x-tw//2,yy),ln,font=FS,fill=BLACK); yy+=lh

    # dashed lifelines
    for lbl,x in parts:
        y=PAD+TITLE_H+BOX_H
        while y<H-PAD-20:
            d.line([(x,y),(x,min(y+5,H-PAD-20))],fill=LGRAY,width=1); y+=10

    # messages
    y = HDR_BOT + 20
    for i,(src,tgt,txt,ret,self_) in enumerate(msgs):
        x1=xs[src]; x2=xs[tgt]
        if self_:
            # self-call loop
            d.line([(x1,y),(x1+30,y)],fill=BLACK,width=1)
            d.line([(x1+30,y),(x1+30,y+14)],fill=BLACK,width=1)
            d.line([(x1+30,y+14),(x1,y+14)],fill=BLACK,width=1)
            d.polygon([(x1,y+14),(x1+8,y+10),(x1+8,y+18)],fill=BLACK)
            bb=d.textbbox((0,0),txt,font=FS); tw=bb[2]-bb[0]
            d.text((x1+34,y),txt,font=FS,fill=BLACK)
            y+=MSG_GAP; continue
        if ret:
            # dashed return
            dx=x2-x1; L=abs(dx); n=int(L/6)
            for j in range(n):
                if j%2==0:
                    t1,t2=j/n,min(1,(j+.5)/n)
                    d.line([(int(x1+dx*t1),y),(int(x1+dx*t2),y)],fill=BLACK,width=1)
            if x2>x1: d.polygon([(x2,y),(x2-8,y-4),(x2-8,y+4)],fill=BLACK)
            else:      d.polygon([(x2,y),(x2+8,y-4),(x2+8,y+4)],fill=BLACK)
        else:
            d.line([(x1,y),(x2,y)],fill=BLACK,width=1)
            if x2>x1: d.polygon([(x2,y),(x2-8,y-4),(x2-8,y+4)],fill=BLACK)
            else:      d.polygon([(x2,y),(x2+8,y-4),(x2+8,y+4)],fill=BLACK)
        # label
        mx=(x1+x2)//2
        bb=d.textbbox((0,0),txt,font=FS); tw=bb[2]-bb[0]
        d.text((mx-tw//2,y-13),txt,font=FS,fill=BLACK)
        y+=MSG_GAP

    return img

# ═══════════════════════════════════════════════════════════════════════════
# SEQ-01  LOGIN
# ═══════════════════════════════════════════════════════════════════════════
def seq_login():
    parts=[
        (":Admin",80),(":Browser",230),(":Router",390),
        (":AuthController",560),(":LoginRequest",730),
        (":RateLimiter",890),(":User Model",1040),
        (":Database",1190),(":ActivityLogger",1360),
    ]
    msgs=[
        # src, tgt, text, return, self
        (":Admin",":Browser","Buka /login",False,False),
        (":Browser",":Router","GET /login [middleware:guest]",False,False),
        (":Router",":AuthController","create()",False,False),
        (":AuthController",":Browser","view(auth.login)",True,False),
        (":Browser",":Admin","Halaman login",True,False),
        (":Admin",":Browser","Input email+password → Klik Masuk",False,False),
        (":Browser",":Router","POST /login {email,password}",False,False),
        (":Router",":AuthController","store(LoginRequest)",False,False),
        (":AuthController",":LoginRequest","validate() [email,password required]",False,False),
        (":LoginRequest",":RateLimiter","tooManyAttempts(key,5)",False,False),
        (":RateLimiter",":LoginRequest","false (belum terlampaui)",True,False),
        (":LoginRequest",":User Model","where('email',$email)->first()",False,False),
        (":User Model",":Database","SELECT * FROM users WHERE email=?",False,False),
        (":Database",":User Model","User record",True,False),
        (":User Model",":LoginRequest","$user",True,False),
        (":LoginRequest",":LoginRequest","Cek is_active=1",False,True),
        (":LoginRequest",":LoginRequest","Auth::attempt(email,password)",False,True),
        (":LoginRequest",":RateLimiter","clear(throttleKey)",False,False),
        (":AuthController",":AuthController","session()->regenerate()",False,True),
        (":AuthController",":User Model","update([last_login_at=>now()])",False,False),
        (":User Model",":Database","UPDATE users SET last_login_at=NOW()",False,False),
        (":AuthController",":ActivityLogger","logAuth('Login','User berhasil login...')",False,False),
        (":ActivityLogger",":Database","INSERT INTO log_aktivitas",False,False),
        (":AuthController",":Browser","redirect()->route('dashboard') [302]",True,False),
        (":Browser",":Admin","Diarahkan ke /dashboard",True,False),
    ]
    img=make_seq("sd  Sequence — Login SimAset",parts,msgs)
    save(img,"SEQ_01_Login.png")

seq_login()

# ═══════════════════════════════════════════════════════════════════════════
# SEQ-02  TAMBAH ASET
# ═══════════════════════════════════════════════════════════════════════════
def seq_tambah_aset():
    parts=[
        (":Pengguna",80),(":Browser",230),(":AssetController",400),
        (":Barang Model",570),(":Ruangan Model",720),(":Asset Model",880),
        (":Database",1040),(":FileSystem",1190),(":ActivityLogger",1360),
    ]
    msgs=[
        (":Pengguna",":Browser","Klik + Tambah Aset",False,False),
        (":Browser",":AssetController","GET /aset/create",False,False),
        (":AssetController",":Barang Model","where('status','aktif')->get()",False,False),
        (":Barang Model",":Database","SELECT kode_barang,nama_barang FROM barang WHERE status=aktif",False,False),
        (":Database",":Barang Model","[BRG-001 Kamera Sony A7, BRG-002 Mic Rode]",True,False),
        (":AssetController",":Ruangan Model","orderBy('nama')->get()",False,False),
        (":Ruangan Model",":Database","SELECT * FROM ruangan ORDER BY nama",False,False),
        (":Database",":Ruangan Model","[Studio 1, Studio 2, Ruang Editing, Ruang Redaksi]",True,False),
        (":AssetController",":Browser","view(aset.create, compact(barangs,ruangans))",True,False),
        (":Browser",":Pengguna","Form tambah aset ditampilkan",True,False),
        (":Pengguna",":Browser","Isi form → Klik Simpan Aset",False,False),
        (":Browser",":AssetController","POST /aset {kode_barang,ruangan_id,kondisi,status,...}",False,False),
        (":AssetController",":AssetController","$request->validate([...])",False,True),
        (":AssetController",":Asset Model","generateKode() [gap-filling]",False,False),
        (":Asset Model",":Database","SELECT kode_aset FROM aset WITH TRASHED",False,False),
        (":Database",":Asset Model","[AST-001, AST-002]",True,False),
        (":Asset Model",":AssetController","'AST-003' (kode baru)",True,False),
        (":AssetController",":FileSystem","foto->move(public/foto_aset/,timestamp_nama)",False,False),
        (":FileSystem",":AssetController","nama file tersimpan",True,False),
        (":AssetController",":Asset Model","Asset::create([kode_aset=AST-003,...,created_by])",False,False),
        (":Asset Model",":Database","INSERT INTO aset (...) VALUES (...)",False,False),
        (":Database",":Asset Model","Record tersimpan",True,False),
        (":AssetController",":ActivityLogger","logAsset('Create','Menambahkan aset baru...')",False,False),
        (":ActivityLogger",":Database","INSERT INTO log_aktivitas",False,False),
        (":AssetController",":Browser","redirect()->route('aset.index') + flash success",True,False),
        (":Browser",":Pengguna","Daftar aset + notifikasi sukses",True,False),
    ]
    img=make_seq("sd  Sequence — Tambah Aset Baru",parts,msgs)
    save(img,"SEQ_02_TambahAset.png")

seq_tambah_aset()

# ═══════════════════════════════════════════════════════════════════════════
# SEQ-03  SCAN QR CODE
# ═══════════════════════════════════════════════════════════════════════════
def seq_qr():
    parts=[
        (":Pengguna",80),(":Browser",230),(":QrCodeController",400),
        (":AssetController",570),(":Asset Model",730),
        (":Database",890),(":qrserver.com API",1060),(":FileSystem",1230),
    ]
    msgs=[
        (":Pengguna",":Browser","Klik Generate QR Code (AST-001)",False,False),
        (":Browser",":AssetController","POST /aset/AST-001/generate-qr",False,False),
        (":AssetController",":Asset Model","where('kode_aset','AST-001')->firstOrFail()",False,False),
        (":Asset Model",":Database","SELECT * FROM aset WHERE kode_aset=AST-001",False,False),
        (":Database",":Asset Model","Asset record",True,False),
        (":AssetController",":FileSystem","glob(qr_codes/qr_AST-001*.png)",False,False),
        (":FileSystem",":AssetController","[] (belum ada file)",True,False),
        (":AssetController",":qrserver.com API","GET ?size=300x300&data={url_detail_aset}",False,False),
        (":qrserver.com API",":AssetController","PNG binary data (300x300)",True,False),
        (":AssetController",":FileSystem","file_put_contents(qr_AST-001_{ts}.png)",False,False),
        (":AssetController",":Browser","redirect()->back() + success",True,False),
        (":Browser",":Pengguna","QR Code berhasil di-generate",True,False),
        (":Pengguna",":Browser","Buka menu QR Scanner",False,False),
        (":Browser",":QrCodeController","GET /qrcode/scanner",False,False),
        (":QrCodeController",":Browser","view(qrcode.scanner) [akses kamera]",True,False),
        (":Pengguna",":Browser","Arahkan kamera ke QR Code aset fisik",False,False),
        (":Browser",":Browser","Decode QR → URL: /aset/AST-001/detail",False,True),
        (":Browser",":AssetController","GET /aset/AST-001/detail [route PUBLIK]",False,False),
        (":AssetController",":Asset Model","with([barang,ruangan,creator])->firstOrFail()",False,False),
        (":Asset Model",":Database","SELECT aset.*,barang.*,ruangan.* WHERE kode_aset=AST-001",False,False),
        (":Database",":Asset Model","{Kamera Sony A7, Ruang Editing, Maintenance}",True,False),
        (":AssetController",":Browser","view(aset.show, compact(asset))",True,False),
        (":Browser",":Pengguna","Detail: Kamera Sony A7 | Maintenance | Ruang Editing",True,False),
    ]
    img=make_seq("sd  Sequence — Generate & Scan QR Code",parts,msgs)
    save(img,"SEQ_03_ScanQR.png")

seq_qr()

# ═══════════════════════════════════════════════════════════════════════════
# SEQ-04  MAINTENANCE
# ═══════════════════════════════════════════════════════════════════════════
def seq_maintenance():
    parts=[
        (":Staff/Admin",80),(":Browser",230),(":MaintenanceController",420),
        (":Asset Model",600),(":User Model",760),
        (":Database",920),(":ActivityLogger",1080),(":SMTP Server",1240),
    ]
    msgs=[
        (":Staff/Admin",":Browser","Buka detail AST-001 → Klik Set Maintenance",False,False),
        (":Browser",":MaintenanceController","POST /maintenance/AST-001/set {keterangan}",False,False),
        (":MaintenanceController",":Asset Model","where('kode_aset','AST-001')->firstOrFail()",False,False),
        (":Asset Model",":Database","SELECT * FROM aset WHERE kode_aset=AST-001",False,False),
        (":Database",":Asset Model","Asset record",True,False),
        (":MaintenanceController",":Asset Model","update([status=>'Maintenance',updated_by=>auth()->id()])",False,False),
        (":Asset Model",":Database","UPDATE aset SET status=Maintenance WHERE kode_aset=AST-001",False,False),
        (":MaintenanceController",":ActivityLogger","logAsset('Update','Aset masuk maintenance...')",False,False),
        (":ActivityLogger",":Database","INSERT INTO log_aktivitas",False,False),
        (":MaintenanceController",":Browser","redirect()->back() + success",True,False),
        (":Browser",":Staff/Admin","Notifikasi sukses",True,False),
        (":Staff/Admin",":Browser","Buka /maintenance → Klik Selesai pada AST-001",False,False),
        (":Browser",":MaintenanceController","PATCH /maintenance/AST-001/complete {kondisi:Baik}",False,False),
        (":MaintenanceController",":Asset Model","where('kode_aset','AST-001')->firstOrFail()",False,False),
        (":Asset Model",":Database","SELECT * FROM aset WHERE kode_aset=AST-001",False,False),
        (":Database",":Asset Model","Asset record",True,False),
        (":MaintenanceController",":MaintenanceController","validate([kondisi required|in:Baik,...])",False,True),
        (":MaintenanceController",":Asset Model","update([status=>'Aktif',kondisi=>'Baik',updated_by])",False,False),
        (":Asset Model",":Database","UPDATE aset SET status=Aktif,kondisi=Baik WHERE kode_aset=AST-001",False,False),
        (":MaintenanceController",":ActivityLogger","logAsset('Update','Maintenance selesai...')",False,False),
        (":ActivityLogger",":Database","INSERT INTO log_aktivitas",False,False),
        (":MaintenanceController",":User Model","where('role','admin')->where('is_active',1)->get()",False,False),
        (":User Model",":Database","SELECT * FROM users WHERE role=admin AND is_active=1",False,False),
        (":Database",":User Model","[Admin Magang (magangrbtv@gmail.com)]",True,False),
        (":MaintenanceController",":SMTP Server","Mail::to(admin)->send(MaintenanceAlert($asset,'selesai'))",False,False),
        (":SMTP Server",":Staff/Admin","Email: Maintenance Selesai — Kamera Sony A7",True,False),
        (":MaintenanceController",":Browser","redirect()->route('maintenance.index') + success",True,False),
        (":Browser",":Staff/Admin","Dashboard maintenance + notifikasi sukses",True,False),
    ]
    img=make_seq("sd  Sequence — Maintenance Aset",parts,msgs)
    save(img,"SEQ_04_Maintenance.png")

seq_maintenance()

# ═══════════════════════════════════════════════════════════════════════════
# SEQ-05  KELOLA PENGGUNA
# ═══════════════════════════════════════════════════════════════════════════
def seq_pengguna():
    parts=[
        (":Admin",80),(":Browser",220),(":Router",380),
        (":UserController",540),(":User Model",700),
        (":Database",860),(":AkunBaruMail",1020),(":ActivityLogger",1180),
    ]
    msgs=[
        (":Admin",":Browser","Klik menu Kelola Pengguna",False,False),
        (":Browser",":Router","GET /users [middleware:role:admin]",False,False),
        (":Router",":Router","Cek role=admin → abort(403) jika bukan",False,True),
        (":Router",":UserController","index()",False,False),
        (":UserController",":User Model","User::orderBy('role')->get()",False,False),
        (":User Model",":Database","SELECT * FROM users ORDER BY role",False,False),
        (":Database",":User Model","[Admin Magang(admin), Staff RBTV(staff), reffki(staff)]",True,False),
        (":UserController",":Browser","view(users.index, compact(users))",True,False),
        (":Browser",":Admin","Daftar pengguna ditampilkan",True,False),
        (":Admin",":Browser","Klik + Tambah Pengguna → Isi form → Submit",False,False),
        (":Browser",":UserController","POST /users {name,email,password,role,kirim_email}",False,False),
        (":UserController",":UserController","validate([email unique, password regex, role in:admin,staff])",False,True),
        (":UserController",":User Model","User::create([...,password=>Hash::make(pwd),is_active:true])",False,False),
        (":User Model",":Database","INSERT INTO users (name,email,password,role,is_active,...)",False,False),
        (":Database",":User Model","User record (id=5)",True,False),
        (":UserController",":AkunBaruMail","new AkunBaruMail(user, plainPassword) [jika dicentang]",False,False),
        (":AkunBaruMail",":Admin","Email: Akun baru dibuat (email+password awal)",True,False),
        (":UserController",":ActivityLogger","logUser('Create','Menambahkan pengguna baru...')",False,False),
        (":ActivityLogger",":Database","INSERT INTO log_aktivitas",False,False),
        (":UserController",":Browser","redirect()->route('users.index') + success",True,False),
        (":Browser",":Admin","Daftar pengguna + notifikasi sukses",True,False),
    ]
    img=make_seq("sd  Sequence — Kelola Pengguna (Admin)",parts,msgs)
    save(img,"SEQ_05_Pengguna.png")

seq_pengguna()

print(f"\nSelesai! Semua diagram ada di: {OUT}/")
