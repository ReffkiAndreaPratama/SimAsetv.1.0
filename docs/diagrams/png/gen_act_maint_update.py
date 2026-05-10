"""Update ACT_10 Maintenance — tambahkan Export PDF/CSV di halaman maintenance."""
import os, math
from PIL import Image, ImageDraw, ImageFont

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

def arr_v(d,x,y1,y2,lbl=""):
    d.line([(x,y1),(x,y2)],fill=BLACK,width=1)
    d.polygon([(x,y2),(x-5,y2-8),(x+5,y2-8)],fill=BLACK)
    if lbl:
        bb=FS.getbbox(lbl); tw=bb[2]-bb[0]
        d.text((x+5,(y1+y2)//2-FS.size//2),lbl,font=FS,fill=GRAY)

def arr_h_r(d,x1,y,x2):
    d.line([(x1,y),(x2,y)],fill=BLACK,width=1)
    d.polygon([(x2,y),(x2-8,y-4),(x2-8,y+4)],fill=BLACK)

def arr_h_l(d,x1,y,x2):
    d.line([(x1,y),(x2,y)],fill=BLACK,width=1)
    d.polygon([(x2,y),(x2+8,y-4),(x2+8,y+4)],fill=BLACK)

def diamond(d,cx,cy,txt,f):
    tw,th=msz(txt,f); w=tw+44; h=th+28
    pts=[(cx,cy-h//2),(cx+w//2,cy),(cx,cy+h//2),(cx-w//2,cy)]
    d.polygon(pts,fill=(255,255,255),outline=BLACK,width=1)
    tc(d,cx,cy,txt,f,GRAY)
    return w//2,h//2

class Act:
    PAD=16; HDR=28; TITLE=20; ARR=20; GAP=10

    def __init__(self,title,l1,l2,w1=300,w2=420):
        self.title=title; self.l1=l1; self.l2=l2
        self.w1=w1; self.w2=w2; self._rows=[]

    def start(self):                 self._rows.append(("S",))
    def end(self):                   self._rows.append(("E",))
    def act(self,lane,txt,minw=120): self._rows.append(("A",lane,txt,minw))
    def cross(self,f,t):             self._rows.append(("X",f,t))
    def ret(self,f,t):               self._rows.append(("R",f,t))
    def dec(self,lane,txt,yes="Ya",no="Tidak"):
                                     self._rows.append(("D",lane,txt,yes,no))
    def fork(self,lane,items):       self._rows.append(("F",lane,items))
    def sep(self,txt=""):            self._rows.append(("SEP",txt))

    def _rh(self,row):
        t=row[0]
        if t=="S":  return 9+self.ARR
        if t=="E":  return self.ARR+18+self.GAP
        if t=="A":  return box_wh(row[2],FB,row[3])[1]+self.ARR
        if t=="D":  return msz(row[2],FS)[1]+28+self.ARR
        if t=="F":
            bh=max(box_wh(it,FS,60)[1] for it in row[2])
            return self.ARR+8+bh+self.ARR
        if t in ("X","R"): return 0
        if t=="SEP": return 18
        return 0

    def render(self,fname):
        P=self.PAD; H_=self.HDR; T=self.TITLE; AR=self.ARR
        w1,w2=self.w1,self.w2; TW=w1+w2+P*2
        ch=sum(self._rh(r) for r in self._rows)+self.GAP*2
        TH=P+T+H_+ch+P+10

        img=Image.new("RGB",(TW,TH),BG); d=ImageDraw.Draw(img)
        d.rectangle([P,P,TW-P,TH-P],outline=BLACK,width=1)
        bb=FT.getbbox(self.title); tw=bb[2]-bb[0]
        d.rectangle([P,P,P+tw+8,P+T],fill=BG,outline=BLACK,width=1)
        d.text((P+4,P+3),self.title,font=FT,fill=BLACK)

        sw=P+T; cx=[P+w1//2, P+w1+w2//2]
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
                lx=cx[lane]; _,th=msz(txt,FS); dh=th+28; hh=dh//2
                cy_d=y+hh
                hw,_=diamond(d,lx,cy_d,txt,FS)
                arr_v(d,lx,cy_d+hh,cy_d+hh+AR)
                d.text((lx+6,cy_d+hh+2),yes,font=FS,fill=GRAY)
                no_end=TW-P-16
                d.line([(lx+hw,cy_d),(no_end,cy_d)],fill=BLACK,width=1)
                d.polygon([(no_end,cy_d),(no_end-8,cy_d-4),(no_end-8,cy_d+4)],fill=BLACK)
                d.text((lx+hw+4,cy_d-FS.size-2),no,font=FS,fill=GRAY)
                y=cy_d+hh+AR
            elif t=="X":
                f,to=row[1],row[2]
                if f<to: arr_h_r(d,cx[f]+100,y,cx[to]-100)
                else:    arr_h_l(d,cx[f]-100,y,cx[to]+100)
            elif t=="R":
                f,to=row[1],row[2]
                if f<to: arr_h_r(d,cx[f]+100,y,cx[to]-100)
                else:    arr_h_l(d,cx[f]-100,y,cx[to]+100)
            elif t=="F":
                lane,items=row[1],row[2]
                lx=cx[lane]; n=len(items)
                bh=max(box_wh(it,FS,60)[1] for it in items)
                bws=[box_wh(it,FS,60)[0] for it in items]
                sp=max(max(bws)+8,68); total=(n-1)*sp
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
                y+=18

        path=f"{OUT}/{fname}"
        img.save(path,"PNG",dpi=(150,150))
        print(f"  {fname}  ({TW}x{TH})")


# ============================================================
# ACT-10 MAINTENANCE — dengan Export PDF/CSV
# ============================================================
def act_maintenance():
    g=Act("act  Maintenance Aset — SimAset","Staff / Admin","Sistem",300,420)
    g.start()
    g.act(0,'Buka menu "Maintenance"')
    g.cross(0,1)
    g.act(1,"Query aset WHERE status=Maintenance\nTampilkan daftar + statistik")
    g.ret(1,0)

    # Fork: 3 aksi dari halaman maintenance
    g.fork(0,["Set\nMaintenance","Selesaikan\nMaintenance","Export\nPDF/CSV"])
    g.cross(0,1)

    g.sep("Set Aset ke Maintenance")
    g.act(1,"Tampilkan modal konfirmasi\n+ input keterangan (opsional)")
    g.ret(1,0)
    g.act(0,"Input keterangan\nKlik Konfirmasi")
    g.cross(0,1)
    g.act(1,"update([status=Maintenance])\nLog Aktivitas")
    g.ret(1,0)

    g.sep("Selesaikan Maintenance")
    g.act(1,"Tampilkan modal:\n- Pilih kondisi akhir (wajib)\n- Input keterangan")
    g.ret(1,0)
    g.act(0,"Pilih kondisi akhir\nKlik Konfirmasi Selesai")
    g.cross(0,1)
    g.act(1,"Validasi kondisi required")
    g.dec(1,"Validasi\ngagal?","Tidak","Ya")
    g.act(1,"update([status=Aktif, kondisi])\nLog Aktivitas\nKirim email ke Admin aktif")
    g.ret(1,0)

    g.sep("Export Laporan Maintenance")
    g.act(1,"GET /laporan/maintenance/pdf\natau /laporan/maintenance/csv\nGenerate file & Download")
    g.ret(1,0)

    g.act(0,"Selesai")
    g.end()
    g.render("ACT_10_Maintenance.png")

act_maintenance()
print("Selesai!")
