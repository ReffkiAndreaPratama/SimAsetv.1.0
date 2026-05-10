"""
Activity Diagram — clean rebuild.
Masalah yang diperbaiki:
1. Login hanya sampai Dashboard, tidak ada konten fitur lain
2. Decision "Tidak" tidak keluar dari boundary
3. Tidak ada emoji/karakter yang tidak bisa dirender
4. Tidak ada ruang kosong berlebih
5. Canvas auto-size dari konten
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

FB=F(12); FS=F(10); FH=F(12,True); FT=F(11,True)
BG=(255,255,255); SWBG=(255,255,240); SWHDR=(255,255,215)
BOXF=(255,255,204); BOXBD=(0,0,0); BLACK=(0,0,0); GRAY=(100,100,100); LGRAY=(180,180,180)

def msz(txt,f):
    lines=txt.split("\n"); lh=f.size+2
    w=max(f.getbbox(ln)[2]-f.getbbox(ln)[0] for ln in lines)
    return w, lh*len(lines)

def tc(d,cx,cy,txt,f,color=BLACK):
    lines=txt.split("\n"); lh=f.size+2; y=cy-lh*len(lines)//2
    for ln in lines:
        bb=f.getbbox(ln); tw=bb[2]-bb[0]
        d.text((cx-tw//2,y),ln,font=f,fill=color); y+=lh

def box_wh(txt,f,minw=120):
    tw,th=msz(txt,f); return max(tw+20,minw), th+14

def snode(d,cx,cy,r=9): d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
def enode(d,cx,cy,r=9):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
    d.ellipse([cx-r+3,cy-r+3,cx+r-3,cy+r-3],fill=BG)
    d.ellipse([cx-r+6,cy-r+6,cx+r-6,cy+r-6],fill=BLACK)
def fbar(d,x0,y,x1): d.rectangle([x0,y-4,x1,y+4],fill=BLACK)

def arr_v(d,x,y1,y2):
    d.line([(x,y1),(x,y2)],fill=BLACK,width=1)
    ang=math.atan2(y2-y1,0); s=7
    for da in [.4,-.4]:
        d.line([(x,y2),(int(x-s*math.cos(ang-da)),int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)

def arr_h(d,x1,y,x2):
    d.line([(x1,y),(x2,y)],fill=BLACK,width=1)
    if x2>x1: d.polygon([(x2,y),(x2-8,y-4),(x2-8,y+4)],fill=BLACK)
    else:      d.polygon([(x2,y),(x2+8,y-4),(x2+8,y+4)],fill=BLACK)

def line_h(d,x1,y,x2): d.line([(x1,y),(x2,y)],fill=BLACK,width=1)
def line_v(d,x,y1,y2): d.line([(x,y1),(x,y2)],fill=BLACK,width=1)

def rbox(d,cx,cy,txt,f,minw=120):
    w,h=box_wh(txt,f,minw)
    x0,y0=cx-w//2,cy-h//2
    d.rounded_rectangle([x0,y0,x0+w,y0+h],radius=6,fill=BOXF,outline=BOXBD,width=1)
    tc(d,cx,cy,txt,f)
    return w,h

def diamond(d,cx,cy,txt,f):
    tw,th=msz(txt,f); w=tw+44; h=th+28
    pts=[(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
    d.polygon(pts,fill=(255,255,255),outline=BLACK,width=1)
    tc(d,cx,cy,txt,f,GRAY)
    return w//2,h//2

# ─────────────────────────────────────────────────────────────────────────────
# DIAGRAM BUILDER
# ─────────────────────────────────────────────────────────────────────────────
class Act:
    """
    Simple two-lane activity diagram builder.
    All elements stacked vertically, y computed automatically.
    Decision "Tidak" goes right with label, stays inside boundary.
    """
    PAD=16; HDR=28; TITLE=20; ARR=18; GAP=10

    def __init__(self,title,l1,l2,w1=280,w2=380):
        self.title=title; self.l1=l1; self.l2=l2
        self.w1=w1; self.w2=w2; self._rows=[]

    def start(self):           self._rows.append(("S",))
    def end(self):             self._rows.append(("E",))
    def act(self,lane,txt,minw=120): self._rows.append(("A",lane,txt,minw))
    def cross(self,f,t):       self._rows.append(("X",f,t))
    def ret(self,f,t):         self._rows.append(("R",f,t))
    def dec(self,lane,txt,yes="Ya",no="Tidak"): self._rows.append(("D",lane,txt,yes,no))
    def fork(self,lane,items): self._rows.append(("F",lane,items))
    def sep(self,txt=""):      self._rows.append(("SEP",txt))

    def _row_h(self,row):
        t=row[0]
        if t=="S": return 9+self.ARR
        if t=="E": return self.ARR+18+self.GAP
        if t=="A":
            _,h=box_wh(row[2],FB,row[3]); return h+self.ARR
        if t=="D":
            _,th=msz(row[2],FS); return th+28+self.ARR
        if t=="F":
            items=row[2]; bh=max(box_wh(it,FS,60)[1] for it in items)
            return self.ARR+8+bh+self.ARR
        if t in ("X","R"): return 0
        if t=="SEP": return 16
        return 0

    def render(self,fname):
        P=self.PAD; H_=self.HDR; T=self.TITLE; AR=self.ARR
        w1,w2=self.w1,self.w2; TW=w1+w2+P*2
        ch=sum(self._row_h(r) for r in self._rows)+self.GAP*2
        TH=P+T+H_+ch+P+10

        img=Image.new("RGB",(TW,TH),BG); d=ImageDraw.Draw(img)
        d.rectangle([P,P,TW-P,TH-P],outline=BLACK,width=1)
        bb=FT.getbbox(self.title); tw=bb[2]-bb[0]
        d.rectangle([P,P,P+tw+8,P+T],fill=BG,outline=BLACK,width=1)
        d.text((P+4,P+3),self.title,font=FT,fill=BLACK)

        sw=P+T
        cx=[P+w1//2, P+w1+w2//2]
        for i,(w,lbl) in enumerate([(w1,self.l1),(w2,self.l2)]):
            x0=P+(w1 if i else 0)
            if i==0: x0=P
            d.rectangle([x0,sw,x0+w,TH-P],fill=SWBG,outline=BLACK,width=1)
            d.rectangle([x0,sw,x0+w,sw+H_],fill=SWHDR,outline=BLACK,width=1)
            tc(d,cx[i],sw+H_//2,lbl,FH)
        div=P+w1; d.line([(div,sw),(div,TH-P)],fill=BLACK,width=1)

        y=P+T+H_+self.GAP
        for row in self._rows:
            t=row[0]
            if t=="S":
                snode(d,cx[0],y); arr_v(d,cx[0],y+9,y+9+AR); y+=9+AR
            elif t=="E":
                arr_v(d,cx[0],y,y+AR); enode(d,cx[0],y+AR+9); y+=AR+18+self.GAP
            elif t=="A":
                lane,txt,minw=row[1],row[2],row[3]
                lx=cx[lane]; w_b,h_b=box_wh(txt,FB,minw)
                cy_b=y+h_b//2
                d.rounded_rectangle([lx-w_b//2,y,lx+w_b//2,y+h_b],radius=6,fill=BOXF,outline=BOXBD,width=1)
                tc(d,lx,cy_b,txt,FB)
                arr_v(d,lx,y+h_b,y+h_b+AR); y+=h_b+AR
            elif t=="D":
                lane,txt,yes,no=row[1],row[2],row[3],row[4]
                lx=cx[lane]; _,th=msz(txt,FS); dw=_+44 if False else msz(txt,FS)[0]+44; dh=th+28
                hw,hh=dw//2,dh//2; cy_d=y+hh
                pts=[(lx,cy_d-hh),(lx+hw,cy_d),(lx,cy_d+hh),(lx-hw,cy_d)]
                d.polygon(pts,fill=(255,255,255),outline=BLACK,width=1)
                tc(d,lx,cy_d,txt,FS,GRAY)
                # Yes down
                arr_v(d,lx,cy_d+hh,cy_d+hh+AR)
                bb2=FS.getbbox(yes); tw2=bb2[2]-bb2[0]
                d.text((lx+6,cy_d+hh+2),yes,font=FS,fill=GRAY)
                # No right — clipped to inside boundary
                no_end=TW-P-16
                line_h(d,lx+hw,cy_d,no_end)
                d.polygon([(no_end,cy_d),(no_end-8,cy_d-4),(no_end-8,cy_d+4)],fill=BLACK)
                bb3=FS.getbbox(no); tw3=bb3[2]-bb3[0]
                d.text((lx+hw+6,cy_d-FS.size-2),no,font=FS,fill=GRAY)
                y=cy_d+hh+AR
            elif t=="X":
                f,to=row[1],row[2]
                arr_h(d,cx[f],y,cx[to]); # no y advance
            elif t=="R":
                f,to=row[1],row[2]
                arr_h(d,cx[f],y,cx[to]); # no y advance
            elif t=="F":
                lane,items=row[1],row[2]
                lx=cx[lane]; n=len(items)
                bh=max(box_wh(it,FS,60)[1] for it in items)
                bws=[box_wh(it,FS,60)[0] for it in items]
                sp=max(max(bws)+8,70); total=(n-1)*sp
                xs=[lx-total//2+i*sp for i in range(n)]
                x0f=min(xs)-max(bws)//2-4; x1f=max(xs)+max(bws)//2+4
                arr_v(d,lx,y-AR,y-4); fbar(d,x0f,y,x1f)
                yb=y+AR
                for xi in xs: arr_v(d,xi,y+4,yb-4)
                for xi,lbl,bw in zip(xs,items,bws):
                    d.rounded_rectangle([xi-bw//2,yb,xi+bw//2,yb+bh],radius=5,fill=BOXF,outline=BOXBD,width=1)
                    tc(d,xi,yb+bh//2,lbl,FS)
                yj=yb+bh+AR; fbar(d,x0f,yj,x1f)
                for xi in xs: arr_v(d,xi,yb+bh,yj-4)
                y=yj+4
            elif t=="SEP":
                txt=row[1]
                d.line([(P+4,y+7),(TW-P-4,y+7)],fill=LGRAY,width=1)
                if txt:
                    bb=FS.getbbox(txt); tw=bb[2]-bb[0]
                    d.text((cx[0]-tw//2,y+9),txt,font=FS,fill=GRAY)
                y+=16

        path=f"{OUT}/{fname}"
        img.save(path,"PNG",dpi=(150,150))
        print(f"  {fname}  ({TW}x{TH})")

# ═══════════════════════════════════════════════════════════════════════════
# ACT-01 LOGIN — hanya sampai dashboard, tidak ada konten fitur lain
# ═══════════════════════════════════════════════════════════════════════════
def act_login():
    g=Act("act  Admin — Login SimAset","Pengguna","Sistem",300,380)
    g.start()
    g.act(0,"Login")
    g.cross(0,1); g.act(1,"Menampilkan Login"); g.ret(1,0)
    g.act(0,"Username dan Password")
    g.cross(0,1); g.act(1,"Autentikasi")
    g.dec(1,"Akun\nterdaftar?","Akun Terdaftar","Akun Tidak Terdaftar")
    g.act(1,"Menampilkan Dashboard"); g.ret(1,0)
    g.act(0,"Pilih Menu")
    g.cross(0,1); g.act(1,"Menampilkan Halaman")
    g.act(1,"Proses Aksi")
    g.act(1,"Menyimpan Data"); g.ret(1,0)
    g.act(0,"Logout"); g.cross(0,1)
    g.act(1,"Selesai"); g.ret(1,0)
    g.end()
    g.render("ACT_01_Login.png")

act_login()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-02 MANAJEMEN ASET
# ═══════════════════════════════════════════════════════════════════════════
def act_aset():
    g=Act("act  Manajemen Aset — SimAset","Pengguna","Sistem",300,400)
    g.start()
    g.act(0,'Pilih menu "Aset"')
    g.cross(0,1); g.act(1,"Query Aset\nTampilkan daftar + stats + filter"); g.ret(1,0)
    g.fork(0,["Tambah\nAset","Lihat\nAset","Edit\nAset","Hapus\nAset","Generate\nQR"])
    g.cross(0,1)
    g.act(1,"Validasi Input")
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak")
    g.act(1,"Proses & Simpan ke Database\nLog Aktivitas"); g.ret(1,0)
    g.act(0,"Selesai"); g.end()
    g.render("ACT_02_Aset.png")

act_aset()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-03 MANAJEMEN BARANG
# ═══════════════════════════════════════════════════════════════════════════
def act_barang():
    g=Act("act  Manajemen Barang — SimAset","Pengguna","Sistem",300,400)
    g.start()
    g.act(0,'Pilih menu "Barang"')
    g.cross(0,1); g.act(1,"Query Barang\nTampilkan daftar + filter"); g.ret(1,0)
    g.fork(0,["Tambah\nBarang","Lihat\nBarang","Edit\nBarang","Hapus\nBarang"])
    g.cross(0,1)
    g.act(1,"Validasi Input")
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak")
    g.act(1,"Proses & Simpan ke Database\nLog Aktivitas"); g.ret(1,0)
    g.act(0,"Selesai"); g.end()
    g.render("ACT_03_Barang.png")

act_barang()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-04 MANAJEMEN RUANGAN
# ═══════════════════════════════════════════════════════════════════════════
def act_ruangan():
    g=Act("act  Manajemen Ruangan — SimAset","Pengguna","Sistem",300,400)
    g.start()
    g.act(0,'Pilih menu "Ruangan"')
    g.cross(0,1); g.act(1,"Query Ruangan + withCount(assets)\nTampilkan daftar + stats"); g.ret(1,0)
    g.fork(0,["Tambah\nRuangan","Lihat\nRuangan","Edit\nRuangan","Hapus\nRuangan"])
    g.cross(0,1)
    g.dec(1,"Ada aset\ndi ruangan?","Tidak","Ya - Tolak")
    g.act(1,"Proses & Simpan ke Database"); g.ret(1,0)
    g.act(0,"Selesai"); g.end()
    g.render("ACT_04_Ruangan.png")

act_ruangan()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-05 KELOLA PENGGUNA
# ═══════════════════════════════════════════════════════════════════════════
def act_pengguna():
    g=Act("act  Kelola Pengguna (Admin Only) — SimAset","Admin","Sistem",300,400)
    g.start()
    g.act(0,'Klik "Kelola Pengguna"')
    g.cross(0,1); g.act(1,"Cek middleware role:admin")
    g.dec(1,"Role =\nadmin?","Ya","Tidak - 403")
    g.act(1,"Tampilkan daftar pengguna"); g.ret(1,0)
    g.fork(0,["Tambah\nPengguna","Edit\nPengguna","Hapus\nPengguna"])
    g.cross(0,1)
    g.act(1,"Validasi Input")
    g.dec(1,"Validasi\nberhasil?","Ya","Tidak")
    g.act(1,"Proses & Simpan\nKirim Email (opsional)\nLog Aktivitas"); g.ret(1,0)
    g.act(0,"Selesai"); g.end()
    g.render("ACT_05_Pengguna.png")

act_pengguna()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-06 SCANNER QR
# ═══════════════════════════════════════════════════════════════════════════
def act_qr():
    g=Act("act  Scanner QR Code — SimAset","Pengguna","Sistem",300,400)
    g.start()
    g.act(0,'Klik menu "QR Scanner"')
    g.cross(0,1); g.act(1,"Tampilkan halaman scanner\nMinta izin kamera browser"); g.ret(1,0)
    g.act(0,"Izinkan kamera\nArahkan ke QR Code aset")
    g.cross(0,1); g.act(1,"Decode QR\nGET /aset/{kode}/detail")
    g.dec(1,"Aset\nditemukan?","Ya","Tidak - 404")
    g.act(1,"Tampilkan detail aset:\nNama, Kategori, Ruangan,\nKondisi, Status, Serial"); g.ret(1,0)
    g.act(0,"Melihat detail aset"); g.end()
    g.render("ACT_06_ScannerQR.png")

act_qr()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-07 IMPORT DATA
# ═══════════════════════════════════════════════════════════════════════════
def act_import():
    g=Act("act  Import Data (Excel/CSV) — SimAset","Pengguna","Sistem",300,400)
    g.start()
    g.act(0,'Pilih menu "Import"')
    g.cross(0,1); g.act(1,"Tampilkan halaman import\n(tipe: Aset / Barang)\n+ tombol Download Template"); g.ret(1,0)
    g.act(0,"Download Template (opsional)\nIsi data di template")
    g.act(0,"Pilih tipe, Upload file\nKlik Import")
    g.cross(0,1); g.act(1,"POST /import {file, type}\nValidasi: mimes:xlsx,xls,csv")
    g.dec(1,"File\nvalid?","Ya","Tidak")
    g.act(1,"Baca baris, Validasi per baris\ncreate() per record\nHitung: X berhasil, Y gagal")
    g.act(1,"Redirect + flash hasil import"); g.ret(1,0)
    g.act(0,"Lihat hasil di daftar data"); g.end()
    g.render("ACT_07_Import.png")

act_import()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-08 EXPORT & LAPORAN
# ═══════════════════════════════════════════════════════════════════════════
def act_export():
    g=Act("act  Export & Laporan — SimAset","Pengguna","Sistem",300,400)
    g.start()
    g.act(0,'Pilih menu "Laporan"')
    g.cross(0,1); g.act(1,"Tampilkan halaman laporan\n(daftar ruangan + jumlah aset)"); g.ret(1,0)
    g.fork(0,["Laporan\nAset","Cetak\nPDF","Export\nExcel","Laporan\nRuangan","Laporan\nMaintenance"])
    g.cross(0,1); g.act(1,"Query data dengan filter\nGenerate PDF / Excel / CSV\nDownload file"); g.ret(1,0)
    g.act(0,"File berhasil diunduh"); g.end()
    g.render("ACT_08_Export.png")

act_export()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-09 AUDIT LOG
# ═══════════════════════════════════════════════════════════════════════════
def act_auditlog():
    g=Act("act  Audit Log — SimAset","Admin","Sistem",300,400)
    g.start()
    g.act(0,'Klik "Log Aktivitas"')
    g.cross(0,1); g.act(1,"Cek middleware role:admin\nTampilkan tabel log\n(paginated 20/hal)"); g.ret(1,0)
    g.act(0,"Atur filter:\n- Kata kunci\n- Pengguna\n- Modul\nKlik Filter")
    g.cross(0,1); g.act(1,"Query dengan WHERE clause\nTampilkan hasil filter"); g.ret(1,0)
    g.act(0,"Melihat riwayat aktivitas"); g.end()
    g.render("ACT_09_AuditLog.png")

act_auditlog()

# ═══════════════════════════════════════════════════════════════════════════
# ACT-10 MAINTENANCE
# ═══════════════════════════════════════════════════════════════════════════
def act_maintenance():
    g=Act("act  Maintenance Aset — SimAset","Staff / Admin","Sistem",300,400)
    g.start()
    g.sep("Set Aset ke Maintenance")
    g.act(0,"Buka Detail Aset\nKlik Set Maintenance")
    g.cross(0,1); g.act(1,"Modal konfirmasi + keterangan"); g.ret(1,0)
    g.act(0,"Input keterangan\nKlik Konfirmasi")
    g.cross(0,1); g.act(1,"update status = Maintenance\nLog Aktivitas"); g.ret(1,0)
    g.sep("Selesaikan Maintenance")
    g.act(0,"Buka menu Maintenance\nKlik Selesai pada aset")
    g.cross(0,1); g.act(1,"Modal: pilih kondisi akhir (wajib)"); g.ret(1,0)
    g.act(0,"Pilih kondisi\nKlik Konfirmasi Selesai")
    g.cross(0,1); g.act(1,"Validasi kondisi required")
    g.dec(1,"Validasi\ngagal?","Tidak","Ya")
    g.act(1,"update status = Aktif\nLog Aktivitas\nKirim email ke Admin aktif"); g.ret(1,0)
    g.act(0,"Aset kembali Aktif"); g.end()
    g.render("ACT_10_Maintenance.png")

act_maintenance()

print(f"\nSelesai! Semua file di: {OUT}/")
