"""
Activity Diagram v6 — engine presisi, persis gaya foto.

Cara kerja:
- Setiap elemen punya tinggi tetap, y dihitung kumulatif
- Cross-lane: panah horizontal lurus (orthogonal)
- Decision: "Ya" ke bawah, "Tidak" ke kanan (label di kanan diamond)
- Fork/Join: bar hitam, panah diagonal ke kotak
- Semua panah SOLID
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

FB=F(12); FS=F(10); FH=F(12,True); FT=F(11,True)

# ── COLORS ────────────────────────────────────────────────────────────────────
BG    = (255,255,255)
SWBG  = (255,255,240)
SWHDR = (255,255,215)
BOXF  = (255,255,204)
BOXBD = (0,0,0)
BLACK = (0,0,0)
GRAY  = (100,100,100)
LGRAY = (180,180,180)

# ── CONSTANTS ─────────────────────────────────────────────────────────────────
PAD    = 14    # outer padding
TITLE_H= 20    # title tag height
HDR_H  = 28    # swimlane header height
ARR    = 18    # arrow segment length
GAP    = 6     # extra gap between elements
BOX_PX = 20    # box horizontal padding
BOX_PY = 12    # box vertical padding
LH_FB  = FB.size + 2
LH_FS  = FS.size + 2

def msz(txt, font):
    lh = font.size+2
    lines = txt.split("\n")
    w = max(font.getbbox(ln)[2]-font.getbbox(ln)[0] for ln in lines)
    return w, lh*len(lines)

def box_h(txt, font=FB):
    _,th = msz(txt,font); return th+BOX_PY*2

def box_w(txt, font=FB, minw=120):
    tw,_ = msz(txt,font); return max(tw+BOX_PX*2, minw)

def dia_hw(txt):
    tw,th = msz(txt,FS); return tw//2+22, th//2+14

# ── DRAW PRIMITIVES ───────────────────────────────────────────────────────────
def tc(d, cx, cy, txt, font, color=BLACK):
    lines=txt.split("\n"); lh=font.size+2
    y=cy-lh*len(lines)//2
    for ln in lines:
        bb=font.getbbox(ln); tw=bb[2]-bb[0]
        d.text((cx-tw//2,y),ln,font=font,fill=color); y+=lh

def ah(d, x2,y2, x1,y1, s=7):
    """Arrowhead at (x2,y2) pointing from (x1,y1)."""
    ang=math.atan2(y2-y1,x2-x1)
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                          int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)

def av(d, x, y1, y2, lbl="", right=True):
    """Vertical arrow down."""
    d.line([(x,y1),(x,y2)],fill=BLACK,width=1); ah(d,x,y2,x,y1)
    if lbl:
        bb=FS.getbbox(lbl); tw=bb[2]-bb[0]
        ox=5 if right else -tw-5
        d.text((x+ox,(y1+y2)//2-FS.size//2),lbl,font=FS,fill=GRAY)

def ah_r(d, x1,y,x2, lbl="", above=True):
    """Horizontal arrow right."""
    d.line([(x1,y),(x2,y)],fill=BLACK,width=1); ah(d,x2,y,x1,y)
    if lbl:
        bb=FS.getbbox(lbl); tw=bb[2]-bb[0]
        dy=-FS.size-2 if above else 3
        d.text(((x1+x2)//2-tw//2,y+dy),lbl,font=FS,fill=GRAY)

def ah_l(d, x1,y,x2, lbl="", above=True):
    """Horizontal arrow left."""
    d.line([(x1,y),(x2,y)],fill=BLACK,width=1); ah(d,x2,y,x1,y)
    if lbl:
        bb=FS.getbbox(lbl); tw=bb[2]-bb[0]
        dy=-FS.size-2 if above else 3
        d.text(((x1+x2)//2-tw//2,y+dy),lbl,font=FS,fill=GRAY)

def rbox(d, cx, cy, txt, font=FB, minw=120):
    w=box_w(txt,font,minw); h=box_h(txt,font)
    x0,y0=cx-w//2,cy-h//2
    d.rounded_rectangle([x0,y0,x0+w,y0+h],radius=6,fill=BOXF,outline=BOXBD,width=1)
    tc(d,cx,cy,txt,font)
    return w,h

def diamond(d, cx, cy, txt):
    hw,hh=dia_hw(txt)
    pts=[(cx,cy-hh),(cx+hw,cy),(cx,cy+hh),(cx-hw,cy)]
    d.polygon(pts,fill=(255,255,255),outline=BLACK,width=1)
    tc(d,cx,cy,txt,FS,GRAY)
    return hw,hh

def forkbar(d,x0,y,x1): d.rectangle([x0,y-4,x1,y+4],fill=BLACK)
def snode(d,cx,cy,r=9): d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
def enode(d,cx,cy,r=9):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
    d.ellipse([cx-r+3,cy-r+3,cx+r-3,cy+r-3],fill=BG)
    d.ellipse([cx-r+6,cy-r+6,cx+r-6,cy+r-6],fill=BLACK)

# ── DIAGRAM CLASS ─────────────────────────────────────────────────────────────
class Diagram:
    def __init__(self, title, lane1, lane2, w1=280, w2=360):
        self.title=title; self.lane1=lane1; self.lane2=lane2
        self.w1=w1; self.w2=w2
        self.rows=[]   # list of row dicts

    # ── row builders ─────────────────────────────────────────────────────────
    def start(self):
        self.rows.append({"t":"start"})

    def end(self):
        self.rows.append({"t":"end"})

    def node(self, lane, txt, minw=120):
        """Single action box in one lane."""
        self.rows.append({"t":"node","lane":lane,"txt":txt,"minw":minw})

    def pair(self, txt0, txt1, arrow="right", ret=True):
        """
        Two boxes side by side.
        arrow: "right" = left→right, "left" = right→left
        ret: draw return arrow after
        """
        self.rows.append({"t":"pair","txt0":txt0,"txt1":txt1,
                          "arrow":arrow,"ret":ret})

    def dec(self, lane, txt, yes_lbl="Ya", no_lbl="Tidak"):
        """
        Decision diamond.
        yes → down, no → right (label beside diamond)
        """
        self.rows.append({"t":"dec","lane":lane,"txt":txt,
                          "yes":yes_lbl,"no":no_lbl})

    def fork(self, lane, items):
        """Fork/join with parallel boxes."""
        self.rows.append({"t":"fork","lane":lane,"items":items})

    def sep(self, txt=""):
        self.rows.append({"t":"sep","txt":txt})

    # ── height calculator ─────────────────────────────────────────────────────
    def _row_h(self, row):
        t=row["t"]
        if t=="start":  return 9+ARR
        if t=="end":    return ARR+18+GAP
        if t=="node":
            return box_h(row["txt"])+ARR
        if t=="pair":
            h0=box_h(row["txt0"]); h1=box_h(row["txt1"])
            h=max(h0,h1)
            return h + (ARR if row["ret"] else 0)
        if t=="dec":
            _,hh=dia_hw(row["txt"])
            return hh*2+ARR
        if t=="fork":
            items=row["items"]
            bh=max(box_h(it,FS) for it in items)
            return ARR+8+bh+ARR
        if t=="sep":    return 16
        return 0

    # ── render ────────────────────────────────────────────────────────────────
    def render(self, fname):
        w1,w2=self.w1,self.w2
        P=PAD; TH=TITLE_H; HH=HDR_H
        TW=w1+w2+P*2

        # total content height
        ch=sum(self._row_h(r) for r in self.rows)+GAP*2
        TH2=P+TH+HH+ch+P+10

        img=Image.new("RGB",(TW,TH2),BG)
        d=ImageDraw.Draw(img)

        # outer border
        d.rectangle([P,P,TW-P,TH2-P],outline=BLACK,width=1)

        # title tag
        bb=FT.getbbox(self.title); tw=bb[2]-bb[0]
        d.rectangle([P,P,P+tw+10,P+TH],fill=BG,outline=BLACK,width=1)
        d.text((P+5,P+3),self.title,font=FT,fill=BLACK)

        # swimlane backgrounds + headers
        sw_top=P+TH
        cx=[P+w1//2, P+w1+w2//2]
        for i,(w,lbl) in enumerate([(w1,self.lane1),(w2,self.lane2)]):
            x0=P+(w1 if i else 0)
            if i==0: x0=P
            d.rectangle([x0,sw_top,x0+w,TH2-P],fill=SWBG,outline=BLACK,width=1)
            d.rectangle([x0,sw_top,x0+w,sw_top+HH],fill=SWHDR,outline=BLACK,width=1)
            tc(d,(x0*2+w)//2,sw_top+HH//2,lbl,FH)

        # vertical divider
        div_x=P+w1
        d.line([(div_x,sw_top),(div_x,TH2-P)],fill=BLACK,width=1)

        # draw rows
        y=P+TH+HH+GAP
        for row in self.rows:
            t=row["t"]

            if t=="start":
                snode(d,cx[0],y)
                av(d,cx[0],y+9,y+9+ARR)
                y+=9+ARR

            elif t=="end":
                av(d,cx[0],y,y+ARR)
                enode(d,cx[0],y+ARR+9)
                y+=ARR+18+GAP

            elif t=="node":
                lane=row["lane"]; txt=row["txt"]; minw=row["minw"]
                lx=cx[lane]
                w_b=box_w(txt,FB,minw); h_b=box_h(txt,FB)
                rbox(d,lx,y+h_b//2,txt,FB,minw)
                av(d,lx,y+h_b,y+h_b+ARR)
                y+=h_b+ARR

            elif t=="pair":
                txt0=row["txt0"]; txt1=row["txt1"]
                arrow=row["arrow"]; ret=row["ret"]
                h0=box_h(txt0); h1=box_h(txt1); h=max(h0,h1)
                cy_row=y+h//2
                w0=box_w(txt0,FB); w1b=box_w(txt1,FB)
                rbox(d,cx[0],cy_row,txt0,FB)
                rbox(d,cx[1],cy_row,txt1,FB)
                # forward arrow
                if arrow=="right":
                    ah_r(d,cx[0]+w0//2,cy_row,cx[1]-w1b//2)
                else:
                    ah_l(d,cx[1]-w1b//2,cy_row,cx[0]+w0//2)
                # return arrow (one row below center)
                if ret:
                    ret_y=cy_row+h//2+6
                    ah_l(d,cx[1]-w1b//2,ret_y,cx[0]+w0//2)
                    av(d,cx[0],y+h,y+h+ARR)
                    y+=h+ARR
                else:
                    y+=h

            elif t=="dec":
                lane=row["lane"]; txt=row["txt"]
                yes_lbl=row["yes"]; no_lbl=row["no"]
                lx=cx[lane]
                hw,hh=dia_hw(txt)
                cy_d=y+hh
                diamond(d,lx,cy_d,txt)
                # YES → down
                av(d,lx,cy_d+hh,cy_d+hh+ARR,yes_lbl,right=True)
                # NO → right (solid arrow to right edge of lane)
                no_x=P+w1+w2-20
                ah_r(d,lx+hw,cy_d,no_x,no_lbl)
                y=cy_d+hh+ARR

            elif t=="fork":
                lane=row["lane"]; items=row["items"]
                lx=cx[lane]
                n=len(items)
                bh_items=max(box_h(it,FS) for it in items)
                bw_items=[box_w(it,FS,60) for it in items]
                sp=max(max(bw_items)+8, 70)
                total=(n-1)*sp
                xs=[lx-total//2+i*sp for i in range(n)]
                x0f=min(xs)-max(bw_items)//2-4
                x1f=max(xs)+max(bw_items)//2+4

                # arrow into fork bar
                av(d,lx,y-ARR,y-4)
                forkbar(d,x0f,y,x1f)

                # fan-out diagonal arrows
                y_box=y+ARR
                for xi in xs:
                    d.line([(xi,y+4),(xi,y_box-4)],fill=BLACK,width=1)
                    ah(d,xi,y_box-4,xi,y+4)

                # boxes
                for xi,lbl,bw_i in zip(xs,items,bw_items):
                    d.rounded_rectangle([xi-bw_i//2,y_box,xi+bw_i//2,y_box+bh_items],
                                         radius=5,fill=BOXF,outline=BOXBD,width=1)
                    tc(d,xi,y_box+bh_items//2,lbl,FS)

                # fan-in diagonal arrows
                y_join=y_box+bh_items+ARR
                for xi in xs:
                    d.line([(xi,y_box+bh_items),(xi,y_join-4)],fill=BLACK,width=1)
                    ah(d,xi,y_join-4,xi,y_box+bh_items)

                forkbar(d,x0f,y_join,x1f)
                y=y_join+4

            elif t=="sep":
                txt=row["txt"]
                d.line([(P+4,y+7),(TW-P-4,y+7)],fill=LGRAY,width=1)
                if txt:
                    bb=FS.getbbox(txt); tw=bb[2]-bb[0]
                    d.text((cx[0]-tw//2,y+9),txt,font=FS,fill=GRAY)
                y+=16

        path=f"{OUT}/{fname}"
        img.save(path,"PNG",dpi=(150,150))
        print(f"  {fname}  ({TW}x{TH2})")

# ═══════════════════════════════════════════════════════════════════════════
# ALL DIAGRAMS
# ═══════════════════════════════════════════════════════════════════════════

# ── ACT-01 LOGIN ─────────────────────────────────────────────────────────────
def act_login():
    g=Diagram("act  Login & Logout — SimAset","Pengguna","Sistem",280,360)
    g.start()
    g.pair("Login","Menampilkan Login",arrow="right",ret=True)
    g.pair("Username dan Password","Autentikasi",arrow="right",ret=False)
    g.dec(1,"Akun\nterdaftar?","Akun Terdaftar","Akun Tidak Terdaftar")
    g.pair("Pilih Menu Aset","Menampilkan Dashboard",arrow="left",ret=False)
    g.node(1,"Menampilkan Halaman Aset",minw=200)
    g.fork(0,["Tambah\nAset","Lihat\nAset","Edit\nAset","Ekspor\nAset","Hapus\nAset"])
    g.node(1,"Menyimpan Data",minw=160)
    g.pair("Logout","Selesai",arrow="left",ret=False)
    g.end()
    g.render("ACT_01_Login.png")

act_login()

# ── ACT-02 MANAJEMEN ASET ────────────────────────────────────────────────────
def act_aset():
    g=Diagram("act  Manajemen Aset — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.pair('Pilih menu "Aset"',"Query Aset\nTampilkan daftar + stats + filter",
           arrow="right",ret=True)
    g.fork(0,["Tambah\nAset","Lihat\nAset","Edit\nAset","Hapus\nAset","Generate\nQR"])
    g.node(1,"Validasi Input",minw=160)
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak — kembali")
    g.node(1,"Proses & Simpan ke Database\nLog Aktivitas",minw=240)
    g.pair("Selesai","Konfirmasi Berhasil",arrow="left",ret=False)
    g.end()
    g.render("ACT_02_Aset.png")

act_aset()

# ── ACT-03 MANAJEMEN BARANG ──────────────────────────────────────────────────
def act_barang():
    g=Diagram("act  Manajemen Barang — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.pair('Pilih menu "Barang"',"Query Barang\nTampilkan daftar + filter",
           arrow="right",ret=True)
    g.fork(0,["Tambah\nBarang","Lihat\nBarang","Edit\nBarang","Hapus\nBarang"])
    g.node(1,"Validasi Input",minw=160)
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak — kembali")
    g.node(1,"Proses & Simpan ke Database\nLog Aktivitas",minw=240)
    g.pair("Selesai","Konfirmasi Berhasil",arrow="left",ret=False)
    g.end()
    g.render("ACT_03_Barang.png")

act_barang()

# ── ACT-04 MANAJEMEN RUANGAN ─────────────────────────────────────────────────
def act_ruangan():
    g=Diagram("act  Manajemen Ruangan — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.pair('Pilih menu "Ruangan"',"Query Ruangan + withCount(assets)\nTampilkan daftar + stats",
           arrow="right",ret=True)
    g.fork(0,["Tambah\nRuangan","Lihat\nRuangan","Edit\nRuangan","Hapus\nRuangan"])
    g.dec(1,"Ada aset\ndi ruangan?","Tidak","Ya — Tolak")
    g.node(1,"Proses & Simpan ke Database",minw=220)
    g.pair("Selesai","Konfirmasi Berhasil",arrow="left",ret=False)
    g.end()
    g.render("ACT_04_Ruangan.png")

act_ruangan()

# ── ACT-05 KELOLA PENGGUNA ───────────────────────────────────────────────────
def act_pengguna():
    g=Diagram("act  Kelola Pengguna (Admin Only) — SimAset","Admin","Sistem",280,380)
    g.start()
    g.pair('Klik "Kelola Pengguna"',"Cek middleware role:admin",
           arrow="right",ret=False)
    g.dec(1,"Role =\nadmin?","Ya","Tidak — 403")
    g.pair("Pilih Aksi","Tampilkan daftar pengguna",arrow="left",ret=False)
    g.fork(0,["Tambah\nPengguna","Edit\nPengguna","Hapus\nPengguna"])
    g.node(1,"Validasi Input",minw=160)
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak — kembali")
    g.node(1,"Proses & Simpan\nKirim Email (opsional)\nLog Aktivitas",minw=240)
    g.pair("Selesai","Konfirmasi Berhasil",arrow="left",ret=False)
    g.end()
    g.render("ACT_05_Pengguna.png")

act_pengguna()

# ── ACT-06 SCANNER QR ────────────────────────────────────────────────────────
def act_qr():
    g=Diagram("act  Scanner QR Code — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.pair('Klik menu "QR Scanner"',"Tampilkan halaman scanner\nMinta izin kamera browser",
           arrow="right",ret=True)
    g.node(0,"Izinkan kamera\nArahkan ke QR Code aset",minw=200)
    g.pair("Scan QR Code","Decode QR → Parse kode_aset\nGET /aset/{kode}/detail [PUBLIK]",
           arrow="right",ret=False)
    g.dec(1,"Aset\nditemukan?","Ya","Tidak — 404")
    g.node(1,"Tampilkan detail aset:\nNama, Kategori, Ruangan,\nKondisi, Status, Serial",minw=240)
    g.pair("Melihat detail aset","Detail ditampilkan",arrow="left",ret=False)
    g.end()
    g.render("ACT_06_ScannerQR.png")

act_qr()

# ── ACT-07 IMPORT DATA ───────────────────────────────────────────────────────
def act_import():
    g=Diagram("act  Import Data (Excel/CSV) — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.pair('Pilih menu "Import"',"Tampilkan halaman import\n(tipe: Aset / Barang)\n+ tombol Download Template",
           arrow="right",ret=True)
    g.node(0,"Download Template (opsional)\nIsi data → Upload file\nKlik Import",minw=220)
    g.pair("Upload & Submit","POST /import {file, type}\nValidasi: mimes:xlsx,xls,csv",
           arrow="right",ret=False)
    g.dec(1,"File\nvalid?","Ya","Tidak — kembali")
    g.node(1,"Baca baris → Validasi per baris\ncreate() per record\nHitung: X berhasil, Y gagal",minw=260)
    g.node(1,"Redirect + flash hasil import",minw=220)
    g.pair("Lihat hasil di daftar data","Import selesai",arrow="left",ret=False)
    g.end()
    g.render("ACT_07_Import.png")

act_import()

# ── ACT-08 EXPORT & LAPORAN ──────────────────────────────────────────────────
def act_export():
    g=Diagram("act  Export & Laporan — SimAset","Pengguna","Sistem",280,380)
    g.start()
    g.pair('Pilih menu "Laporan"',"Tampilkan halaman laporan\n(daftar ruangan + jumlah aset)",
           arrow="right",ret=True)
    g.fork(0,["Laporan\nAset","Cetak\nPDF","Export\nExcel","Laporan\nRuangan","Laporan\nMaintenance"])
    g.node(1,"Query data dengan filter\nGenerate PDF / Excel / CSV\nDownload file",minw=240)
    g.pair("File berhasil diunduh","Proses selesai",arrow="left",ret=False)
    g.end()
    g.render("ACT_08_Export.png")

act_export()

# ── ACT-09 AUDIT LOG ─────────────────────────────────────────────────────────
def act_auditlog():
    g=Diagram("act  Audit Log — SimAset","Admin","Sistem",280,380)
    g.start()
    g.pair('Klik "Log Aktivitas"',"Cek middleware role:admin\nActivityLog::with('user')\n->orderBy('created_at','desc')->paginate(20)",
           arrow="right",ret=True)
    g.node(0,"Atur filter:\n- Kata kunci\n- Pengguna\n- Modul (Login/Create/Update/Delete)\nKlik Filter",minw=220)
    g.pair("Klik Filter","Query dengan WHERE clause\nTampilkan hasil (paginated 20/hal)",
           arrow="right",ret=True)
    g.node(0,"Melihat riwayat aktivitas",minw=180)
    g.end()
    g.render("ACT_09_AuditLog.png")

act_auditlog()

# ── ACT-10 MAINTENANCE ───────────────────────────────────────────────────────
def act_maintenance():
    g=Diagram("act  Maintenance Aset — SimAset","Staff / Admin","Sistem",280,380)
    g.start()
    g.sep("— Set Aset ke Maintenance —")
    g.pair("Buka Detail Aset\nKlik Set Maintenance","Modal konfirmasi + keterangan",
           arrow="right",ret=True)
    g.pair("Input keterangan → Konfirmasi","update([status=>'Maintenance'])\nLog Aktivitas",
           arrow="right",ret=True)
    g.sep("— Selesaikan Maintenance —")
    g.pair("Buka menu Maintenance\nKlik Selesai pada aset","Modal: pilih kondisi akhir (wajib)",
           arrow="right",ret=True)
    g.pair("Pilih kondisi → Konfirmasi Selesai","Validasi kondisi required",
           arrow="right",ret=False)
    g.dec(1,"Validasi\ngagal?","Tidak","Ya — kembali")
    g.node(1,"update([status=>'Aktif', kondisi])\nLog Aktivitas\nKirim email ke semua Admin aktif",minw=260)
    g.pair("Aset kembali Aktif\nAdmin terima email notifikasi","Proses selesai",
           arrow="left",ret=False)
    g.end()
    g.render("ACT_10_Maintenance.png")

act_maintenance()

print(f"\nSelesai! Semua file di: {OUT}/")
