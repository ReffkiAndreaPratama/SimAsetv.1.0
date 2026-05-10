"""
Final diagram generator — persis gaya foto:
Activity: garis vertikal pemisah swimlane, kotak rounded kuning, panah tipis
Use Case: rapi, terstruktur, tidak berantakan
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

FB = F(12); FS = F(10); FH = F(12,True); FT = F(11,True); FSM = F(9)

# ── COLORS ────────────────────────────────────────────────────────────────────
BG    = (255,255,255)
SWBG  = (255,255,240)   # swimlane bg — kuning sangat muda
SWHDR = (255,255,215)   # swimlane header
BOXF  = (255,255,204)   # box fill
BOXBD = (0,0,0)         # box border — hitam tipis
DIAF  = (255,255,255)
DIABD = (0,0,0)
BLACK = (0,0,0)
GRAY  = (100,100,100)
LGRAY = (180,180,180)

# ── PRIMITIVES ────────────────────────────────────────────────────────────────
def tc(d, cx, cy, txt, font, color=BLACK):
    lines = txt.split("\n"); lh = font.size+2
    y = cy - lh*len(lines)//2
    for ln in lines:
        bb = font.getbbox(ln); tw = bb[2]-bb[0]
        d.text((cx-tw//2, y), ln, font=font, fill=color); y += lh

def measure(txt, font):
    lines = txt.split("\n"); lh = font.size+2
    w = max(font.getbbox(ln)[2]-font.getbbox(ln)[0] for ln in lines)
    return w, lh*len(lines)

def rbox(d, cx, cy, txt, font, minw=0, minh=0):
    tw,th = measure(txt,font)
    w = max(tw+20, minw); h = max(th+14, minh)
    x0,y0 = cx-w//2, cy-h//2
    d.rounded_rectangle([x0,y0,x0+w,y0+h], radius=6,
                         fill=BOXF, outline=BOXBD, width=1)
    tc(d,cx,cy,txt,font)
    return w,h

def arrow(d, x1,y1,x2,y2, lbl="", font=None, lbl_side="left"):
    d.line([(x1,y1),(x2,y2)], fill=BLACK, width=1)
    ang = math.atan2(y2-y1,x2-x1); s=7
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                          int(y2-s*math.sin(ang-da)))], fill=BLACK, width=1)
    if lbl and font:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=font.getbbox(lbl); tw=bb[2]-bb[0]
        ox = 6 if lbl_side=="right" else -tw-6
        d.text((mx+ox, my-font.size-2), lbl, font=font, fill=GRAY)

def darrow(d, x1,y1,x2,y2, lbl="", font=None):
    dx,dy=x2-x1,y2-y1; L=max(1,math.hypot(dx,dy)); n=int(L/7)
    for i in range(n):
        if i%2==0:
            t1,t2=i/n,min(1,(i+.5)/n)
            d.line([(int(x1+dx*t1),int(y1+dy*t1)),
                    (int(x1+dx*t2),int(y1+dy*t2))], fill=BLACK, width=1)
    ang=math.atan2(dy,dx); s=7
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                          int(y2-s*math.sin(ang-da)))], fill=BLACK, width=1)
    if lbl and font:
        mx,my=(x1+x2)//2,(y1+y2)//2
        bb=font.getbbox(lbl); tw=bb[2]-bb[0]
        d.text((mx-tw//2,my-font.size-2),lbl,font=font,fill=GRAY)

def snode(d,cx,cy,r=9): d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
def enode(d,cx,cy,r=9):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLACK)
    d.ellipse([cx-r+3,cy-r+3,cx+r-3,cy+r-3],fill=BG)
    d.ellipse([cx-r+6,cy-r+6,cx+r-6,cy+r-6],fill=BLACK)
def fbar(d,x0,y,x1): d.rectangle([x0,y-4,x1,y+4],fill=BLACK)
def vl(d,x,y1,y2): d.line([(x,y1),(x,y2)],fill=BLACK,width=1)
def hl(d,x1,y,x2): d.line([(x1,y),(x2,y)],fill=BLACK,width=1)

def dia(d,cx,cy,txt,font,w=None,h=None):
    tw,th=measure(txt,font)
    if w is None: w=tw+36
    if h is None: h=th+24
    pts=[(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
    d.polygon(pts,fill=DIAF,outline=DIABD,width=1)
    tc(d,cx,cy,txt,font,GRAY)
    return w//2,h//2  # half_w, half_h

# ═══════════════════════════════════════════════════════════════════════════
# ACTIVITY DIAGRAM BUILDER
# Persis gaya foto: garis vertikal pemisah, header kuning, kotak rounded
# ═══════════════════════════════════════════════════════════════════════════
class Act:
    PAD=14; TITLE_H=20; HDR_H=28; GAP=16; ARR=20; MINBW=150

    def __init__(self, title, l1, l2, w1=None, w2=None):
        self.title=title; self.l1=l1; self.l2=l2
        self._w1=w1; self._w2=w2; self._steps=[]

    def start(self,lane=0):       self._steps.append(("S",lane))
    def end(self,lane=0):         self._steps.append(("E",lane))
    def act(self,lane,txt):       self._steps.append(("A",lane,txt))
    def dec(self,lane,txt,y_lbl="Ya",n_lbl="Tidak"):
                                  self._steps.append(("D",lane,txt,y_lbl,n_lbl))
    def cross(self,f,t,lbl=""):   self._steps.append(("C",f,t,lbl,False))
    def cret(self,f,t,lbl=""):    self._steps.append(("C",f,t,lbl,True))
    def sep(self,txt=""):         self._steps.append(("SEP",txt))
    def fork_start(self,lane,items):
        """items: list of labels for parallel boxes"""
        self._steps.append(("FK",lane,items))

    def _auto_w(self):
        w=[self.MINBW,self.MINBW]
        for s in self._steps:
            if s[0]=="A":
                tw,_=measure(s[2],FB); w[s[1]]=max(w[s[1]],tw+28)
            elif s[0]=="D":
                tw,_=measure(s[2],FS); w[s[1]]=max(w[s[1]],tw+44)
        if self._w1: w[0]=self._w1
        if self._w2: w[1]=self._w2
        return w

    def render(self,fname):
        P=self.PAD; TH=self.TITLE_H; HH=self.HDR_H
        G=self.GAP; AR=self.ARR
        w=self._auto_w()
        TW=w[0]+w[1]+P*2

        # measure height
        y=P+TH+HH+G
        for s in self._steps:
            if s[0]=="S":   y+=9+AR
            elif s[0]=="E": y+=AR+18+G
            elif s[0]=="A":
                _,bh=measure(s[2],FB); y+=bh+14+AR
            elif s[0]=="D":
                _,th=measure(s[2],FS); y+=th+24+AR
            elif s[0]=="SEP": y+=18
            elif s[0]=="FK":
                n=len(s[2]); y+=8+60+8+AR  # fork bar + boxes + join bar
        TH2=y+P+10

        img=Image.new("RGB",(TW,TH2),BG)
        d=ImageDraw.Draw(img)

        # outer border
        d.rectangle([P,P,TW-P,TH2-P],outline=BLACK,width=1)
        # title tag (top-left small box like foto)
        tag=self.title
        bb=FT.getbbox(tag); tw=bb[2]-bb[0]
        d.rectangle([P,P,P+tw+10,P+TH],fill=BG,outline=BLACK,width=1)
        d.text((P+5,P+3),tag,font=FT,fill=BLACK)

        # swimlane backgrounds
        sw_top=P+TH
        cx=[P+w[0]//2, P+w[0]+w[1]//2]
        for i in range(2):
            x0=P+sum(w[:i]); x1=x0+w[i]
            d.rectangle([x0,sw_top,x1,TH2-P],fill=SWBG,outline=BLACK,width=1)
            d.rectangle([x0,sw_top,x1,sw_top+HH],fill=SWHDR,outline=BLACK,width=1)
            lbl=[self.l1,self.l2][i]
            tc(d,cx[i],sw_top+HH//2,lbl,FH)

        # vertical divider line (the key feature from foto)
        div_x=P+w[0]
        d.line([(div_x,sw_top),(div_x,TH2-P)],fill=BLACK,width=1)

        # draw steps
        y=P+TH+HH+G
        for s in self._steps:
            t=s[0]
            if t=="S":
                lx=cx[s[1]]
                snode(d,lx,y); arrow(d,lx,y+9,lx,y+9+AR); y+=9+AR
            elif t=="E":
                lx=cx[s[1]]
                arrow(d,lx,y,lx,y+AR); enode(d,lx,y+AR+9); y+=AR+18+G
            elif t=="A":
                lane,txt=s[1],s[2]
                lx=cx[lane]; tw2,bh=measure(txt,FB)
                bw=max(tw2+20,self.MINBW); bh2=bh+14
                cy_b=y+bh2//2
                d.rounded_rectangle([lx-bw//2,y,lx+bw//2,y+bh2],
                                     radius=6,fill=BOXF,outline=BOXBD,width=1)
                tc(d,lx,cy_b,txt,FB)
                arrow(d,lx,y+bh2,lx,y+bh2+AR)
                y+=bh2+AR
            elif t=="D":
                lane,txt,ylbl,nlbl=s[1],s[2],s[3],s[4]
                lx=cx[lane]; tw2,th=measure(txt,FS)
                dw=tw2+40; dh=th+24; hw=dw//2; hh=dh//2
                cy_d=y+hh
                pts=[(lx,cy_d-hh),(lx+hw,cy_d),(lx,cy_d+hh),(lx-hw,cy_d)]
                d.polygon(pts,fill=DIAF,outline=DIABD,width=1)
                tc(d,lx,cy_d,txt,FS,GRAY)
                # Yes — down
                arrow(d,lx,cy_d+hh,lx,cy_d+hh+AR,ylbl,FS,"right")
                # No — right to edge, with label
                no_x=lx+hw+6
                no_end=min(P+w[0]+w[1]-20, lx+hw+90)
                hl(d,lx+hw,cy_d,no_end)
                # arrowhead right
                d.polygon([(no_end,cy_d),(no_end-7,cy_d-4),(no_end-7,cy_d+4)],fill=BLACK)
                bb=FS.getbbox(nlbl); ntw=bb[2]-bb[0]
                d.text((lx+hw+8,cy_d-FS.size-2),nlbl,font=FS,fill=GRAY)
                y=cy_d+hh+AR
            elif t=="C":
                f,to,lbl,ret=s[1],s[2],s[3],s[4]
                x1=cx[f]; x2=cx[to]
                if ret: darrow(d,x1,y,x2,y,lbl,FS)
                else:   arrow(d,x1,y,x2,y,lbl,FS)
                # don't advance y — cross is at current y
            elif t=="SEP":
                txt=s[1]
                hl(d,P+4,y+7,TW-P-4)
                d.line([(P+4,y+7),(TW-P-4,y+7)],fill=LGRAY,width=1)
                if txt:
                    bb=FS.getbbox(txt); tw2=bb[2]-bb[0]
                    d.text((cx[0]-tw2//2,y+9),txt,font=FS,fill=GRAY)
                y+=18
            elif t=="FK":
                lane,items=s[1],s[2]
                lx=cx[lane]; n=len(items)
                spacing=70; total=(n-1)*spacing
                xs=[lx-total//2+i*spacing for i in range(n)]
                x0f=min(xs)-30; x1f=max(xs)+30
                # fork bar
                fbar(d,x0f,y,x1f)
                arrow(d,lx,y-AR,lx,y-4)
                # fan out
                for xi in xs: arrow(d,xi,y+4,xi,y+4+AR)
                y+=4+AR
                # boxes
                bh=44
                for xi,lbl in zip(xs,items):
                    tw2,th=measure(lbl,FS); bw=max(tw2+16,60)
                    d.rounded_rectangle([xi-bw//2,y,xi+bw//2,y+bh],
                                         radius=5,fill=BOXF,outline=BOXBD,width=1)
                    tc(d,xi,y+bh//2,lbl,FS)
                y+=bh
                # fan in
                for xi in xs: arrow(d,xi,y,xi,y+AR)
                y+=AR
                fbar(d,x0f,y,x1f)
                y+=4

        path=f"{OUT}/{fname}"
        img.save(path,"PNG",dpi=(150,150))
        print(f"  {fname}  ({TW}x{TH2})")

# ═══════════════════════════════════════════════════════════════════════════
# ALL ACTIVITY DIAGRAMS
# ═══════════════════════════════════════════════════════════════════════════

def make_all_activities():

    # ── ACT-01 LOGIN ─────────────────────────────────────────────────────────
    g=Act("act  Login & Logout — SimAset","Pengguna","Sistem",290,360)
    g.start(0)
    g.act(0,"Login")
    g.cross(0,1); g.act(1,"Menampilkan Login"); g.cret(1,0)
    g.act(0,"Input Email & Password")
    g.cross(0,1); g.act(1,"Autentikasi")
    g.dec(1,"Akun\nterdaftar?","Ya","Tidak")
    g.act(1,"Menampilkan Dashboard"); g.cret(1,0)
    g.act(0,"Pilih Menu")
    g.cross(0,1); g.act(1,"Menampilkan Halaman")
    g.act(1,"Proses Aksi\n(CRUD / QR / Export / dll)")
    g.act(1,"Menyimpan Data"); g.cret(1,0)
    g.act(0,"Logout"); g.cross(0,1)
    g.act(1,"Selesai"); g.cret(1,0)
    g.end(0)
    g.render("ACT_01_Login.png")

    # ── ACT-02 MANAJEMEN ASET ────────────────────────────────────────────────
    g=Act("act  Manajemen Aset — SimAset","Pengguna","Sistem",290,380)
    g.start(0)
    g.act(0,'Pilih menu "Aset"')
    g.cross(0,1); g.act(1,"Query Aset\nTampilkan daftar + stats + filter"); g.cret(1,0)
    g.fork_start(0,["Tambah\nAset","Lihat\nAset","Edit\nAset","Hapus\nAset","Generate\nQR"])
    g.cross(0,1); g.act(1,"Proses & Simpan ke Database\nLog Aktivitas"); g.cret(1,0)
    g.act(0,"Selesai"); g.end(0)
    g.render("ACT_02_Aset.png")

    # ── ACT-03 MANAJEMEN BARANG ──────────────────────────────────────────────
    g=Act("act  Manajemen Barang — SimAset","Pengguna","Sistem",290,380)
    g.start(0)
    g.act(0,'Pilih menu "Barang"')
    g.cross(0,1); g.act(1,"Query Barang\nTampilkan daftar + filter"); g.cret(1,0)
    g.fork_start(0,["Tambah\nBarang","Lihat\nBarang","Edit\nBarang","Hapus\nBarang"])
    g.cross(0,1); g.act(1,"Proses & Simpan ke Database\nLog Aktivitas"); g.cret(1,0)
    g.act(0,"Selesai"); g.end(0)
    g.render("ACT_03_Barang.png")

    # ── ACT-04 MANAJEMEN RUANGAN ─────────────────────────────────────────────
    g=Act("act  Manajemen Ruangan — SimAset","Pengguna","Sistem",290,380)
    g.start(0)
    g.act(0,'Pilih menu "Ruangan"')
    g.cross(0,1); g.act(1,"Query Ruangan + withCount(assets)\nTampilkan daftar + stats"); g.cret(1,0)
    g.fork_start(0,["Tambah\nRuangan","Lihat\nRuangan","Edit\nRuangan","Hapus\nRuangan"])
    g.cross(0,1)
    g.dec(1,"Ada aset\ndi ruangan?","Tidak","Ya — Tolak")
    g.act(1,"Proses & Simpan ke Database"); g.cret(1,0)
    g.act(0,"Selesai"); g.end(0)
    g.render("ACT_04_Ruangan.png")

    # ── ACT-05 KELOLA PENGGUNA ───────────────────────────────────────────────
    g=Act("act  Kelola Pengguna (Admin Only) — SimAset","Admin","Sistem",290,380)
    g.start(0)
    g.act(0,'Klik "Kelola Pengguna"')
    g.cross(0,1); g.act(1,"Cek middleware role:admin"); 
    g.dec(1,"Role =\nadmin?","Ya","Tidak — 403")
    g.act(1,"Tampilkan daftar pengguna"); g.cret(1,0)
    g.fork_start(0,["Tambah\nPengguna","Edit\nPengguna","Hapus\nPengguna"])
    g.cross(0,1); g.act(1,"Validasi → Proses\nKirim Email (opsional)\nLog Aktivitas"); g.cret(1,0)
    g.act(0,"Selesai"); g.end(0)
    g.render("ACT_05_Pengguna.png")

    # ── ACT-06 SCANNER QR ────────────────────────────────────────────────────
    g=Act("act  Scanner QR Code — SimAset","Pengguna","Sistem",290,380)
    g.start(0)
    g.act(0,'Klik menu "QR Scanner"')
    g.cross(0,1); g.act(1,"Tampilkan halaman scanner\nMinta izin kamera browser"); g.cret(1,0)
    g.act(0,"Izinkan kamera\nArahkan ke QR Code aset")
    g.cross(0,1); g.act(1,"Decode QR → Parse kode_aset\nGET /aset/{kode}/detail [PUBLIK]")
    g.dec(1,"Aset\nditemukan?","Ya","Tidak — 404")
    g.act(1,"Tampilkan detail aset:\nNama, Kategori, Ruangan,\nKondisi, Status, Serial"); g.cret(1,0)
    g.act(0,"Melihat detail aset"); g.end(0)
    g.render("ACT_06_ScannerQR.png")

    # ── ACT-07 IMPORT DATA ───────────────────────────────────────────────────
    g=Act("act  Import Data (Excel/CSV) — SimAset","Pengguna","Sistem",290,380)
    g.start(0)
    g.act(0,'Pilih menu "Import"')
    g.cross(0,1); g.act(1,"Tampilkan halaman import\n(tipe: Aset / Barang)\n+ tombol Download Template"); g.cret(1,0)
    g.act(0,"Download Template (opsional)\nIsi data → Upload file\nKlik Import")
    g.cross(0,1); g.act(1,"POST /import {file, type}\nValidasi: mimes:xlsx,xls,csv")
    g.dec(1,"File\nvalid?","Ya","Tidak")
    g.act(1,"Baca baris → Validasi per baris\ncreate() per record\nHitung: X berhasil, Y gagal")
    g.act(1,"Redirect + flash hasil import"); g.cret(1,0)
    g.act(0,"Lihat hasil di daftar data"); g.end(0)
    g.render("ACT_07_Import.png")

    # ── ACT-08 EXPORT & LAPORAN ──────────────────────────────────────────────
    g=Act("act  Export & Laporan — SimAset","Pengguna","Sistem",290,380)
    g.start(0)
    g.act(0,'Pilih menu "Laporan"')
    g.cross(0,1); g.act(1,"Tampilkan halaman laporan\n(daftar ruangan + jumlah aset)"); g.cret(1,0)
    g.fork_start(0,["Laporan\nAset","Cetak\nPDF","Export\nExcel","Laporan\nRuangan","Laporan\nMaintenance"])
    g.cross(0,1); g.act(1,"Query data dengan filter\nGenerate PDF / Excel / CSV\nDownload file"); g.cret(1,0)
    g.act(0,"File berhasil diunduh"); g.end(0)
    g.render("ACT_08_Export.png")

    # ── ACT-09 AUDIT LOG ─────────────────────────────────────────────────────
    g=Act("act  Audit Log — SimAset","Admin","Sistem",290,380)
    g.start(0)
    g.act(0,'Klik "Log Aktivitas"')
    g.cross(0,1); g.act(1,"Cek middleware role:admin\nActivityLog::with('user')\n->orderBy('created_at','desc')->paginate(20)"); g.cret(1,0)
    g.act(0,"Atur filter:\n- Kata kunci\n- Pengguna\n- Modul (Login/Create/Update/Delete)\nKlik Filter")
    g.cross(0,1); g.act(1,"Query dengan WHERE clause\nTampilkan hasil (paginated 20/hal)"); g.cret(1,0)
    g.act(0,"Melihat riwayat aktivitas"); g.end(0)
    g.render("ACT_09_AuditLog.png")

    # ── ACT-10 MAINTENANCE ───────────────────────────────────────────────────
    g=Act("act  Maintenance Aset — SimAset","Staff / Admin","Sistem",290,380)
    g.start(0)
    g.sep("— Set Aset ke Maintenance —")
    g.act(0,"Buka Detail Aset\nKlik Set Maintenance")
    g.cross(0,1); g.act(1,"Modal konfirmasi + keterangan")
    g.act(0,"Input keterangan → Konfirmasi")
    g.cross(0,1); g.act(1,"update([status=>'Maintenance'])\nLog Aktivitas"); g.cret(1,0)
    g.sep("— Selesaikan Maintenance —")
    g.act(0,"Buka menu Maintenance\nKlik Selesai pada aset")
    g.cross(0,1); g.act(1,"Modal: pilih kondisi akhir (wajib)")
    g.act(0,"Pilih kondisi → Konfirmasi Selesai")
    g.cross(0,1); g.act(1,"Validasi kondisi required")
    g.dec(1,"Validasi\ngagal?","Tidak","Ya")
    g.act(1,"update([status=>'Aktif', kondisi])\nLog Aktivitas\nKirim email ke semua Admin aktif"); g.cret(1,0)
    g.act(0,"Aset kembali Aktif\nAdmin terima email notifikasi"); g.end(0)
    g.render("ACT_10_Maintenance.png")

make_all_activities()
print()

# ═══════════════════════════════════════════════════════════════════════════
# USE CASE DIAGRAM — rapi, terstruktur, tidak berantakan
# Strategi: pisah per grup, susun vertikal, garis rapi
# ═══════════════════════════════════════════════════════════════════════════
def make_usecase():
    W,H = 1200, 860
    img = Image.new("RGB",(W,H),BG)
    d   = ImageDraw.Draw(img)

    # outer border + title tag
    d.rectangle([8,8,W-8,H-8],outline=BLACK,width=1)
    d.rectangle([8,8,130,26],fill=BG,outline=BLACK,width=1)
    d.text((12,10),"uc  Use Case Diagram",font=FT,fill=BLACK)

    # system boundary
    d.rectangle([120,28,W-60,H-20],fill=(255,255,250),outline=BLACK,width=1)

    # ── ACTOR HELPERS ─────────────────────────────────────────────────────────
    def actor(cx,cy,lbl):
        r=11
        d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BG,outline=BLACK,width=1)
        d.line([(cx,cy+r),(cx,cy+r+26)],fill=BLACK,width=1)
        d.line([(cx-18,cy+r+10),(cx+18,cy+r+10)],fill=BLACK,width=1)
        d.line([(cx,cy+r+26),(cx-14,cy+r+44)],fill=BLACK,width=1)
        d.line([(cx,cy+r+26),(cx+14,cy+r+44)],fill=BLACK,width=1)
        bb=FB.getbbox(lbl); tw=bb[2]-bb[0]
        d.text((cx-tw//2,cy+r+48),lbl,font=FB,fill=BLACK)

    # ── ELLIPSE HELPER ────────────────────────────────────────────────────────
    def ell(cx,cy,txt,font=FB):
        lines=txt.split("\n"); lh=font.size+2
        tw=max(font.getbbox(ln)[2]-font.getbbox(ln)[0] for ln in lines)
        th=lh*len(lines)
        rx=tw//2+16; ry=th//2+10
        d.ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=BOXF,outline=BLACK,width=1)
        tc(d,cx,cy,txt,font)
        return rx,ry

    # ── EDGE POINT ────────────────────────────────────────────────────────────
    def ep(cx,cy,rx,ry,tx,ty):
        dx,dy=tx-cx,ty-cy; L=max(1,math.hypot(dx,dy))
        denom=math.sqrt((dx/L/rx)**2+(dy/L/ry)**2)
        if denom==0: return cx,cy
        t=1/denom
        return int(cx+dx/L*t),int(cy+dy/L*t)

    # ── CONNECT ───────────────────────────────────────────────────────────────
    def conn(x1,y1,x2,y2,lbl="",dashed=False):
        if dashed:
            dx,dy=x2-x1,y2-y1; L=max(1,math.hypot(dx,dy)); n=int(L/7)
            for i in range(n):
                if i%2==0:
                    t1,t2=i/n,min(1,(i+.5)/n)
                    d.line([(int(x1+dx*t1),int(y1+dy*t1)),
                            (int(x1+dx*t2),int(y1+dy*t2))],fill=BLACK,width=1)
        else:
            d.line([(x1,y1),(x2,y2)],fill=BLACK,width=1)
        # arrowhead
        ang=math.atan2(y2-y1,x2-x1); s=7
        for da in [.4,-.4]:
            d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),
                              int(y2-s*math.sin(ang-da)))],fill=BLACK,width=1)
        if lbl:
            mx,my=(x1+x2)//2,(y1+y2)//2
            bb=FSM.getbbox(lbl); tw=bb[2]-bb[0]
            d.text((mx-tw//2,my-FSM.size-1),lbl,font=FSM,fill=GRAY)

    def uc_conn(c1,r1, c2,r2, lbl="",dashed=False):
        x1,y1=ep(*c1,*r1,*c2[:2])
        x2,y2=ep(*c2,*r2,*c1[:2])
        conn(x1,y1,x2,y2,lbl,dashed)

    def actor_line(ax,ay, cx,cy,rx,ry):
        ex,ey=ep(cx,cy,rx,ry,ax,ay)
        d.line([(ax,ay),(ex,ey)],fill=BLACK,width=1)

    # ── LAYOUT ────────────────────────────────────────────────────────────────
    # Actors
    ADMIN_X,ADMIN_Y = 65, 430
    STAFF_X,STAFF_Y = W-35, 430
    actor(ADMIN_X,ADMIN_Y,"Admin")
    actor(STAFF_X,STAFF_Y,"Staff")

    # Login — center
    LX,LY = 640,430
    lrx,lry = ell(LX,LY,"Login")
    LC=(LX,LY); LR=(lrx,lry)

    # ── MAIN USE CASES (2 rows: top & bottom) ─────────────────────────────────
    # Top row — 5 use cases
    top_ucs = [
        ("Manajemen\nAset",    220, 160),
        ("Manajemen\nBarang",  400, 160),
        ("Manajemen\nRuangan", 580, 160),
        ("QR Code",            760, 160),
        ("Maintenance",        940, 160),
    ]
    # Bottom row — 5 use cases
    bot_ucs = [
        ("Import Data",        220, 700),
        ("Export &\nLaporan",  400, 700),
        ("Dashboard",          580, 700),
        ("Kelola\nPengguna",   760, 700),
        ("Audit Log",          940, 700),
    ]

    top_data={}; bot_data={}
    for lbl,cx,cy in top_ucs:
        rx,ry=ell(cx,cy,lbl); top_data[lbl]=(cx,cy,rx,ry)
    for lbl,cx,cy in bot_ucs:
        rx,ry=ell(cx,cy,lbl); bot_data[lbl]=(cx,cy,rx,ry)

    all_main = {**top_data,**bot_data}

    # ── CRUD EXTENDS (small ellipses around each main UC) ─────────────────────
    # Each main UC gets 3-4 small extends above/below
    extends_map = {
        "Manajemen\nAset":    (["Tambah Aset","Edit Aset","Hapus Aset","Detail Aset"], "above"),
        "Manajemen\nBarang":  (["Tambah Barang","Edit Barang","Hapus Barang"], "above"),
        "Manajemen\nRuangan": (["Tambah Ruangan","Edit Ruangan","Hapus Ruangan"], "above"),
        "QR Code":            (["Generate QR","Scan QR","Cetak Massal"], "above"),
        "Maintenance":        (["Set Maintenance","Selesaikan\nMaintenance"], "above"),
        "Import Data":        (["Import Aset","Import Barang","Download\nTemplate"], "below"),
        "Export &\nLaporan":  (["Export Excel","Export PDF","Laporan\nRuangan","Laporan\nMaintenance"], "below"),
        "Dashboard":          ([], "below"),
        "Kelola\nPengguna":   (["Tambah\nPengguna","Edit\nPengguna","Hapus\nPengguna"], "below"),
        "Audit Log":          (["Filter\nAudit Log"], "below"),
    }

    ext_data={}
    for uc_lbl,(ext_list,direction) in extends_map.items():
        if not ext_list: continue
        cx,cy,rx,ry = all_main[uc_lbl]
        n=len(ext_list); spacing=max(90,rx*2+10)
        total=(n-1)*spacing
        for i,elbl in enumerate(ext_list):
            ex=cx-total//2+i*spacing
            ey=cy-80 if direction=="above" else cy+80
            erx,ery=ell(ex,ey,elbl,FSM)
            ext_data[elbl]=(ex,ey,erx,ery)
            # extend arrow: child → parent
            x1,y1=ep(ex,ey,erx,ery,cx,cy)
            x2,y2=ep(cx,cy,rx,ry,ex,ey)
            conn(x1,y1,x2,y2,"<<extend>>",dashed=True)

    # ── INCLUDE: main UCs → Login ─────────────────────────────────────────────
    include_ucs = [k for k in all_main if k!="Dashboard"]
    for lbl in include_ucs:
        cx,cy,rx,ry=all_main[lbl]
        x1,y1=ep(cx,cy,rx,ry,LX,LY)
        x2,y2=ep(LX,LY,lrx,lry,cx,cy)
        conn(x1,y1,x2,y2,"<<include>>",dashed=True)

    # ── ACTOR → MAIN USE CASES ────────────────────────────────────────────────
    admin_ucs = list(all_main.keys())
    staff_ucs = [k for k in all_main if k not in ("Kelola\nPengguna","Audit Log")]

    for lbl in admin_ucs:
        cx,cy,rx,ry=all_main[lbl]
        actor_line(ADMIN_X,ADMIN_Y,cx,cy,rx,ry)
    for lbl in staff_ucs:
        cx,cy,rx,ry=all_main[lbl]
        actor_line(STAFF_X,STAFF_Y,cx,cy,rx,ry)

    # ── ACTOR → LOGIN ─────────────────────────────────────────────────────────
    actor_line(ADMIN_X,ADMIN_Y,LX,LY,lrx,lry)
    actor_line(STAFF_X,STAFF_Y,LX,LY,lrx,lry)

    path=f"{OUT}/UC_SimAset.png"
    img.save(path,"PNG",dpi=(150,150))
    print(f"  UC_SimAset.png  ({W}x{H})")

make_usecase()
print(f"\nSelesai! Semua file di: {OUT}/")
