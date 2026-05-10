"""
Activity Diagram v4 — persis gaya foto:
- Garis vertikal pemisah swimlane
- Semua panah SOLID (tidak ada putus-putus)
- Decision "Tidak/Gagal" → panah solid ke KANAN lalu loop balik ke atas
- Decision "Ya" → lanjut ke bawah
- Cross-lane pakai panah solid horizontal
- Return dari Sistem ke Pengguna pakai panah solid horizontal
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = "docs/diagrams/png"
os.makedirs(OUT, exist_ok=True)

# ── FONTS ─────────────────────────────────────────────────────────────────────
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

# ── DRAW HELPERS ──────────────────────────────────────────────────────────────
def tc(d, cx, cy, txt, font, color=BLACK):
    lines=txt.split("\n"); lh=font.size+2
    y=cy-lh*len(lines)//2
    for ln in lines:
        bb=font.getbbox(ln); tw=bb[2]-bb[0]
        d.text((cx-tw//2,y),ln,font=font,fill=color); y+=lh

def msz(txt, font):
    lines=txt.split("\n"); lh=font.size+2
    w=max(font.getbbox(ln)[2]-font.getbbox(ln)[0] for ln in lines)
    return w, lh*len(lines)

def solid_arrow(d, x1,y1,x2,y2, lbl="", font=None, lbl_above=True):
    """Solid arrow — always solid, never dashed."""
    d.line([(x1,y1),(x2,y2)],fill=BLACK,width=1)
    ang=math.atan2(y2-y1,x2-x1); s=7
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                          int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)
    if lbl and font:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=font.getbbox(lbl); tw=bb[2]-bb[0]
        dy=-font.size-2 if lbl_above else 3
        d.text((mx-tw//2,my+dy),lbl,font=font,fill=GRAY)

def draw_box(d, cx, cy, txt, font, minw=120):
    tw,th=msz(txt,font)
    w=max(tw+20,minw); h=th+14
    x0,y0=cx-w//2,cy-h//2
    d.rounded_rectangle([x0,y0,x0+w,y0+h],radius=6,fill=BOXF,outline=BOXBD,width=1)
    tc(d,cx,cy,txt,font)
    return w,h

def draw_diamond(d, cx, cy, txt, font):
    tw,th=msz(txt,font)
    w=tw+44; h=th+28
    pts=[(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
    d.polygon(pts,fill=(255,255,255),outline=BLACK,width=1)
    tc(d,cx,cy,txt,font,GRAY)
    return w//2,h//2

def draw_fork(d,x0,y,x1): d.rectangle([x0,y-4,x1,y+4],fill=BLACK)
def snode(d,cx,cy,r=9):   d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
def enode(d,cx,cy,r=9):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
    d.ellipse([cx-r+3,cy-r+3,cx+r-3,cy+r-3],fill=BG)
    d.ellipse([cx-r+6,cy-r+6,cx+r-6,cy+r-6],fill=BLACK)

# ── ACTIVITY DIAGRAM ENGINE ───────────────────────────────────────────────────
class Act:
    """
    Two-lane activity diagram.
    Steps are added sequentially; y advances automatically.
    Decision: "Ya" continues down, "Tidak/Gagal" goes right then loops back.
    All arrows are SOLID.
    """
    PAD=14; TITLE_H=20; HDR_H=28; GAP=14; ARR=20; MINBW=140

    def __init__(self, title, l1, l2, w1=260, w2=360):
        self.title=title; self.l1=l1; self.l2=l2
        self.w1=w1; self.w2=w2
        self._steps=[]

    # ── step adders ──────────────────────────────────────────────────────────
    def start(self):          self._steps.append(("START",))
    def end(self):            self._steps.append(("END",))
    def act(self, lane, txt): self._steps.append(("ACT", lane, txt))
    def cross(self, f, t, lbl=""):  self._steps.append(("CROSS", f, t, lbl))
    def dec(self, lane, txt, yes="Ya", no="Tidak"):
        """Decision: yes→down, no→right+back"""
        self._steps.append(("DEC", lane, txt, yes, no))
    def fork(self, lane, items):
        """Fork/join with parallel boxes."""
        self._steps.append(("FORK", lane, items))
    def sep(self, txt=""):    self._steps.append(("SEP", txt))

    # ── render ────────────────────────────────────────────────────────────────
    def render(self, fname):
        P=self.PAD; TH=self.TITLE_H; HH=self.HDR_H
        G=self.GAP; AR=self.ARR
        w1,w2=self.w1,self.w2
        TW=w1+w2+P*2

        # ── pass 1: compute total height ─────────────────────────────────────
        y=P+TH+HH+G
        for s in self._steps:
            t=s[0]
            if t=="START":  y+=9+AR
            elif t=="END":  y+=AR+18+G
            elif t=="ACT":
                _,bh=msz(s[2],FB); y+=bh+14+AR
            elif t=="DEC":
                _,th=msz(s[2],FS); y+=th+28+AR
            elif t=="FORK":
                y+=8+52+8+AR
            elif t=="SEP":  y+=18
            elif t=="CROSS": pass  # no height
        TH2=y+P+16

        # ── create canvas ─────────────────────────────────────────────────────
        img=Image.new("RGB",(TW,TH2),BG)
        d=ImageDraw.Draw(img)

        # outer border
        d.rectangle([P,P,TW-P,TH2-P],outline=BLACK,width=1)

        # title tag (top-left small box)
        tag=self.title
        bb=FT.getbbox(tag); tw=bb[2]-bb[0]
        d.rectangle([P,P,P+tw+10,P+TH],fill=BG,outline=BLACK,width=1)
        d.text((P+5,P+3),tag,font=FT,fill=BLACK)

        # swimlane backgrounds
        sw_top=P+TH
        cx=[P+w1//2, P+w1+w2//2]

        for i,(w,lbl) in enumerate([(w1,self.l1),(w2,self.l2)]):
            x0=P+sum([w1,w2][:i]); x1=x0+w
            d.rectangle([x0,sw_top,x1,TH2-P],fill=SWBG,outline=BLACK,width=1)
            d.rectangle([x0,sw_top,x1,sw_top+HH],fill=SWHDR,outline=BLACK,width=1)
            tc(d,cx[i],sw_top+HH//2,lbl,FH)

        # vertical divider (the key line from foto)
        div_x=P+w1
        d.line([(div_x,sw_top),(div_x,TH2-P)],fill=BLACK,width=1)

        # ── pass 2: draw elements ─────────────────────────────────────────────
        y=P+TH+HH+G
        # track last "return" y for loop-back arrows
        last_dec_no_y={}   # lane → y of "no" branch target

        for s in self._steps:
            t=s[0]

            if t=="START":
                lx=cx[0]
                snode(d,lx,y)
                solid_arrow(d,lx,y+9,lx,y+9+AR)
                y+=9+AR

            elif t=="END":
                lx=cx[0]
                solid_arrow(d,lx,y,lx,y+AR)
                enode(d,lx,y+AR+9)
                y+=AR+18+G

            elif t=="ACT":
                lane,txt=s[1],s[2]
                lx=cx[lane]
                tw2,bh=msz(txt,FB)
                bw=max(tw2+20,self.MINBW); bh2=bh+14
                cy_b=y+bh2//2
                d.rounded_rectangle([lx-bw//2,y,lx+bw//2,y+bh2],
                                     radius=6,fill=BOXF,outline=BOXBD,width=1)
                tc(d,lx,cy_b,txt,FB)
                solid_arrow(d,lx,y+bh2,lx,y+bh2+AR)
                y+=bh2+AR

            elif t=="DEC":
                lane,txt,yes_lbl,no_lbl=s[1],s[2],s[3],s[4]
                lx=cx[lane]
                tw2,th=msz(txt,FS)
                hw,hh=tw2//2+22,th//2+14
                cy_d=y+hh

                draw_diamond(d,lx,cy_d,txt,FS)

                # YES → down (solid arrow)
                solid_arrow(d,lx,cy_d+hh,lx,cy_d+hh+AR,yes_lbl,FS,lbl_above=False)

                # NO → right then label (solid arrow going right)
                no_end_x=TW-P-20
                # horizontal line right
                d.line([(lx+hw,cy_d),(no_end_x,cy_d)],fill=BLACK,width=1)
                # arrowhead pointing right
                d.polygon([(no_end_x,cy_d),(no_end_x-8,cy_d-4),(no_end_x-8,cy_d+4)],fill=BLACK)
                # label on the horizontal line
                bb=FS.getbbox(no_lbl); ntw=bb[2]-bb[0]
                d.text((lx+hw+6,cy_d-FS.size-2),no_lbl,font=FS,fill=GRAY)

                y=cy_d+hh+AR

            elif t=="FORK":
                lane,items=s[1],s[2]
                lx=cx[lane]
                n=len(items)
                # compute spacing so boxes fit in lane
                max_bw=max(msz(it,FS)[0]+16 for it in items)
                spacing=max(max_bw+10,68)
                total=(n-1)*spacing
                # center fork in lane
                xs=[lx-total//2+i*spacing for i in range(n)]
                x0f=min(xs)-max_bw//2-4
                x1f=max(xs)+max_bw//2+4

                # incoming arrow to fork bar
                solid_arrow(d,lx,y-AR,lx,y-4)

                # fork bar
                draw_fork(d,x0f,y,x1f)

                # fan-out arrows
                for xi in xs:
                    solid_arrow(d,xi,y+4,xi,y+4+AR)
                y+=4+AR

                # boxes
                bh=44
                for xi,lbl in zip(xs,items):
                    tw2,_=msz(lbl,FS); bw=max(tw2+16,60)
                    d.rounded_rectangle([xi-bw//2,y,xi+bw//2,y+bh],
                                         radius=5,fill=BOXF,outline=BOXBD,width=1)
                    tc(d,xi,y+bh//2,lbl,FS)
                y+=bh

                # fan-in arrows
                for xi in xs:
                    solid_arrow(d,xi,y,xi,y+AR)
                y+=AR

                # join bar
                draw_fork(d,x0f,y,x1f)
                y+=4

            elif t=="SEP":
                txt=s[1]
                d.line([(P+4,y+7),(TW-P-4,y+7)],fill=LGRAY,width=1)
                if txt:
                    bb=FS.getbbox(txt); tw2=bb[2]-bb[0]
                    d.text((cx[0]-tw2//2,y+9),txt,font=FS,fill=GRAY)
                y+=18

            elif t=="CROSS":
                f,to,lbl=s[1],s[2],s[3]
                x1=cx[f]; x2=cx[to]
                solid_arrow(d,x1,y,x2,y,lbl,FS)
                # don't advance y

        path=f"{OUT}/{fname}"
        img.save(path,"PNG",dpi=(150,150))
        print(f"  {fname}  ({TW}x{TH2})")

# ═══════════════════════════════════════════════════════════════════════════
# ALL ACTIVITY DIAGRAMS
# ═══════════════════════════════════════════════════════════════════════════

# ── ACT-01 LOGIN ─────────────────────────────────────────────────────────────
def act_login():
    g=Act("act  Login & Logout — SimAset","Pengguna","Sistem",280,360)
    g.start()
    g.act(0,"Login")
    g.cross(0,1); g.act(1,"Menampilkan Halaman Login"); g.cross(1,0)
    g.act(0,"Input Email & Password")
    g.cross(0,1); g.act(1,"Autentikasi\n(cek email, is_active, password)")
    g.dec(1,"Akun\nterdaftar?","Ya","Tidak — kembali")
    g.act(1,"Menampilkan Dashboard"); g.cross(1,0)
    g.act(0,"Pilih Menu")
    g.cross(0,1); g.act(1,"Menampilkan Halaman")
    g.act(1,"Proses Aksi")
    g.act(1,"Menyimpan Data"); g.cross(1,0)
    g.act(0,"Logout"); g.cross(0,1)
    g.act(1,"Selesai"); g.cross(1,0)
    g.end()
    g.render("ACT_01_Login.png")

act_login()

# ── ACT-02 MANAJEMEN ASET ────────────────────────────────────────────────────
def act_aset():
    g=Act("act  Manajemen Aset — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.act(0,'Pilih menu "Aset"')
    g.cross(0,1); g.act(1,"Query Aset\nTampilkan daftar + stats + filter"); g.cross(1,0)
    g.fork(0,["Tambah\nAset","Lihat\nAset","Edit\nAset","Hapus\nAset","Generate\nQR"])
    g.cross(0,1)
    g.act(1,"Validasi Input")
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak — kembali")
    g.act(1,"Proses & Simpan ke Database\nLog Aktivitas"); g.cross(1,0)
    g.act(0,"Selesai"); g.end()
    g.render("ACT_02_Aset.png")

act_aset()

# ── ACT-03 MANAJEMEN BARANG ──────────────────────────────────────────────────
def act_barang():
    g=Act("act  Manajemen Barang — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.act(0,'Pilih menu "Barang"')
    g.cross(0,1); g.act(1,"Query Barang\nTampilkan daftar + filter"); g.cross(1,0)
    g.fork(0,["Tambah\nBarang","Lihat\nBarang","Edit\nBarang","Hapus\nBarang"])
    g.cross(0,1)
    g.act(1,"Validasi Input")
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak — kembali")
    g.act(1,"Proses & Simpan ke Database\nLog Aktivitas"); g.cross(1,0)
    g.act(0,"Selesai"); g.end()
    g.render("ACT_03_Barang.png")

act_barang()

# ── ACT-04 MANAJEMEN RUANGAN ─────────────────────────────────────────────────
def act_ruangan():
    g=Act("act  Manajemen Ruangan — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.act(0,'Pilih menu "Ruangan"')
    g.cross(0,1); g.act(1,"Query Ruangan + withCount(assets)\nTampilkan daftar + stats"); g.cross(1,0)
    g.fork(0,["Tambah\nRuangan","Lihat\nRuangan","Edit\nRuangan","Hapus\nRuangan"])
    g.cross(0,1)
    g.dec(1,"Ada aset\ndi ruangan?","Tidak","Ya — Tolak")
    g.act(1,"Proses & Simpan ke Database"); g.cross(1,0)
    g.act(0,"Selesai"); g.end()
    g.render("ACT_04_Ruangan.png")

act_ruangan()

# ── ACT-05 KELOLA PENGGUNA ───────────────────────────────────────────────────
def act_pengguna():
    g=Act("act  Kelola Pengguna (Admin Only) — SimAset","Admin","Sistem",280,380)
    g.start()
    g.act(0,'Klik "Kelola Pengguna"')
    g.cross(0,1); g.act(1,"Cek middleware role:admin")
    g.dec(1,"Role =\nadmin?","Ya","Tidak — 403")
    g.act(1,"Tampilkan daftar pengguna"); g.cross(1,0)
    g.fork(0,["Tambah\nPengguna","Edit\nPengguna","Hapus\nPengguna"])
    g.cross(0,1)
    g.act(1,"Validasi Input")
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak — kembali")
    g.act(1,"Proses & Simpan\nKirim Email (opsional)\nLog Aktivitas"); g.cross(1,0)
    g.act(0,"Selesai"); g.end()
    g.render("ACT_05_Pengguna.png")

act_pengguna()

# ── ACT-06 SCANNER QR ────────────────────────────────────────────────────────
def act_qr():
    g=Act("act  Scanner QR Code — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.act(0,'Klik menu "QR Scanner"')
    g.cross(0,1); g.act(1,"Tampilkan halaman scanner\nMinta izin kamera browser"); g.cross(1,0)
    g.act(0,"Izinkan kamera\nArahkan ke QR Code aset")
    g.cross(0,1); g.act(1,"Decode QR → Parse kode_aset\nGET /aset/{kode}/detail [PUBLIK]")
    g.dec(1,"Aset\nditemukan?","Ya","Tidak — 404")
    g.act(1,"Tampilkan detail aset:\nNama, Kategori, Ruangan,\nKondisi, Status, Serial"); g.cross(1,0)
    g.act(0,"Melihat detail aset"); g.end()
    g.render("ACT_06_ScannerQR.png")

act_qr()

# ── ACT-07 IMPORT DATA ───────────────────────────────────────────────────────
def act_import():
    g=Act("act  Import Data (Excel/CSV) — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.act(0,'Pilih menu "Import"')
    g.cross(0,1); g.act(1,"Tampilkan halaman import\n(tipe: Aset / Barang)\n+ tombol Download Template"); g.cross(1,0)
    g.act(0,"Download Template (opsional)\nIsi data → Upload file\nKlik Import")
    g.cross(0,1); g.act(1,"POST /import {file, type}\nValidasi: mimes:xlsx,xls,csv")
    g.dec(1,"File\nvalid?","Ya","Tidak — kembali")
    g.act(1,"Baca baris → Validasi per baris\ncreate() per record\nHitung: X berhasil, Y gagal")
    g.act(1,"Redirect + flash hasil import"); g.cross(1,0)
    g.act(0,"Lihat hasil di daftar data"); g.end()
    g.render("ACT_07_Import.png")

act_import()

# ── ACT-08 EXPORT & LAPORAN ──────────────────────────────────────────────────
def act_export():
    g=Act("act  Export & Laporan — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.act(0,'Pilih menu "Laporan"')
    g.cross(0,1); g.act(1,"Tampilkan halaman laporan\n(daftar ruangan + jumlah aset)"); g.cross(1,0)
    g.fork(0,["Laporan\nAset","Cetak\nPDF","Export\nExcel","Laporan\nRuangan","Laporan\nMaintenance"])
    g.cross(0,1); g.act(1,"Query data dengan filter\nGenerate PDF / Excel / CSV\nDownload file"); g.cross(1,0)
    g.act(0,"File berhasil diunduh"); g.end()
    g.render("ACT_08_Export.png")

act_export()

# ── ACT-09 AUDIT LOG ─────────────────────────────────────────────────────────
def act_auditlog():
    g=Act("act  Audit Log — SimAset","Admin","Sistem",280,380)
    g.start()
    g.act(0,'Klik "Log Aktivitas"')
    g.cross(0,1); g.act(1,"Cek middleware role:admin\nActivityLog::with('user')\n->orderBy('created_at','desc')->paginate(20)"); g.cross(1,0)
    g.act(0,"Atur filter:\n- Kata kunci\n- Pengguna\n- Modul (Login/Create/Update/Delete)\nKlik Filter")
    g.cross(0,1); g.act(1,"Query dengan WHERE clause\nTampilkan hasil (paginated 20/hal)"); g.cross(1,0)
    g.act(0,"Melihat riwayat aktivitas"); g.end()
    g.render("ACT_09_AuditLog.png")

act_auditlog()

# ── ACT-10 MAINTENANCE ───────────────────────────────────────────────────────
def act_maintenance():
    g=Act("act  Maintenance Aset — SimAset","Staff / Admin","Sistem",280,380)
    g.start()
    g.sep("— Set Aset ke Maintenance —")
    g.act(0,"Buka Detail Aset\nKlik Set Maintenance")
    g.cross(0,1); g.act(1,"Modal konfirmasi + keterangan"); g.cross(1,0)
    g.act(0,"Input keterangan → Konfirmasi")
    g.cross(0,1); g.act(1,"update([status=>'Maintenance'])\nLog Aktivitas"); g.cross(1,0)
    g.sep("— Selesaikan Maintenance —")
    g.act(0,"Buka menu Maintenance\nKlik Selesai pada aset")
    g.cross(0,1); g.act(1,"Modal: pilih kondisi akhir (wajib)"); g.cross(1,0)
    g.act(0,"Pilih kondisi → Konfirmasi Selesai")
    g.cross(0,1); g.act(1,"Validasi kondisi required")
    g.dec(1,"Validasi\ngagal?","Tidak","Ya — kembali")
    g.act(1,"update([status=>'Aktif', kondisi])\nLog Aktivitas\nKirim email ke semua Admin aktif"); g.cross(1,0)
    g.act(0,"Aset kembali Aktif\nAdmin terima email notifikasi"); g.end()
    g.render("ACT_10_Maintenance.png")

act_maintenance()

print(f"\nSelesai! Semua file di: {OUT}/")
