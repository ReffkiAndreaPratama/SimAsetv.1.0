"""
Diagram generator v3 — layout presisi, tidak ada overlap, tidak ada yang keluar kotak.
Semua ukuran dihitung dari konten teks secara dinamis.
"""
from PIL import Image, ImageDraw, ImageFont
import os, math, textwrap

OUT = "docs/diagrams/png"
os.makedirs(OUT, exist_ok=True)

# ─── FONTS ───────────────────────────────────────────────────────────────────
def _font(size, bold=False):
    candidates = (
        ["C:/Windows/Fonts/arialbd.ttf","C:/Windows/Fonts/calibrib.ttf"]
        if bold else
        ["C:/Windows/Fonts/arial.ttf","C:/Windows/Fonts/calibri.ttf","C:/Windows/Fonts/verdana.ttf"]
    )
    for p in candidates:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

FB  = _font(12)        # body
FS  = _font(10)        # small / labels
FH  = _font(12, True)  # header bold
FT  = _font(11, True)  # title bold

# ─── COLORS ──────────────────────────────────────────────────────────────────
WHITE  = (255,255,255)
BG     = (255,255,255)
SWBG   = (255,255,248)
SWHDR  = (255,255,215)
BOXF   = (255,255,204)
BOXBD  = (130,130,90)
DIAF   = (255,255,255)
DIABD  = (60,60,60)
BLACK  = (0,0,0)
GRAY   = (110,110,110)
LGRAY  = (190,190,190)

# ─── TEXT MEASUREMENT ────────────────────────────────────────────────────────
def text_size(txt, font):
    """Return (width, height) of multi-line text."""
    lines = txt.split("\n")
    lh = font.size + 3
    w = max((lambda bb: bb[2]-bb[0])(font.getbbox(ln)) for ln in lines)
    return w, lh * len(lines)

def box_size(txt, font, pad_x=16, pad_y=10):
    """Minimum box size to fit text with padding."""
    tw, th = text_size(txt, font)
    return tw + pad_x*2, th + pad_y*2

# ─── DRAWING PRIMITIVES ──────────────────────────────────────────────────────
def draw_text_center(d, cx, cy, txt, font, color=BLACK):
    lines = txt.split("\n")
    lh = font.size + 3
    total_h = lh * len(lines)
    y = cy - total_h // 2
    for ln in lines:
        bb = font.getbbox(ln)
        tw = bb[2] - bb[0]
        d.text((cx - tw//2, y), ln, font=font, fill=color)
        y += lh

def draw_box(d, cx, cy, txt, font, min_w=0, min_h=0):
    """Draw rounded rect, return (x0,y0,x1,y1)."""
    bw, bh = box_size(txt, font)
    w = max(bw, min_w)
    h = max(bh, min_h)
    x0, y0 = cx - w//2, cy - h//2
    d.rounded_rectangle([x0,y0,x0+w,y0+h], radius=7,
                         fill=BOXF, outline=BOXBD, width=1)
    draw_text_center(d, cx, cy, txt, font)
    return x0, y0, x0+w, y0+h

def draw_diamond(d, cx, cy, txt, font):
    tw, th = text_size(txt, font)
    w = tw + 40; h = th + 28
    pts = [(cx, cy-h//2),(cx+w//2, cy),(cx, cy+h//2),(cx-w//2, cy)]
    d.polygon(pts, fill=DIAF, outline=DIABD, width=1)
    draw_text_center(d, cx, cy, txt, font, GRAY)
    return w//2, h//2   # half_w, half_h

def draw_arrow(d, x1,y1,x2,y2, lbl="", font=None, above=True):
    d.line([(x1,y1),(x2,y2)], fill=BLACK, width=1)
    ang = math.atan2(y2-y1, x2-x1); s=7
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),int(y2-s*math.sin(ang-da)))],
               fill=BLACK, width=1)
    if lbl and font:
        mx,my = (x1+x2)//2, (y1+y2)//2
        bb = font.getbbox(lbl); tw = bb[2]-bb[0]
        dy = -13 if above else 4
        d.text((mx-tw//2, my+dy), lbl, font=font, fill=GRAY)

def draw_darrow(d, x1,y1,x2,y2, lbl="", font=None):
    """Dashed arrow (return message)."""
    dx,dy = x2-x1, y2-y1
    L = max(1, math.hypot(dx,dy)); n = int(L/7)
    for i in range(n):
        if i%2==0:
            t1,t2 = i/n, min(1,(i+.5)/n)
            d.line([(int(x1+dx*t1),int(y1+dy*t1)),(int(x1+dx*t2),int(y1+dy*t2))],
                   fill=BLACK, width=1)
    ang = math.atan2(dy,dx); s=7
    for da in [.4,-.4]:
        d.line([(x2,y2),(int(x2-s*math.cos(ang-da)),int(y2-s*math.sin(ang-da)))],
               fill=BLACK, width=1)
    if lbl and font:
        mx,my = (x1+x2)//2, (y1+y2)//2
        bb = font.getbbox(lbl); tw = bb[2]-bb[0]
        d.text((mx-tw//2, my-13), lbl, font=font, fill=GRAY)

def draw_fork(d, x0, y, x1):
    d.rectangle([x0, y-4, x1, y+4], fill=BLACK)

def draw_start(d, cx, cy, r=9):
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=BLACK)

def draw_end(d, cx, cy, r=9):
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=BLACK)
    d.ellipse([cx-r+3,cy-r+3,cx+r-3,cy+r-3], fill=BG)
    d.ellipse([cx-r+6,cy-r+6,cx+r-6,cy+r-6], fill=BLACK)

def vline(d,x,y1,y2): d.line([(x,y1),(x,y2)],fill=BLACK,width=1)
def hline(d,x1,y,x2): d.line([(x1,y),(x2,y)],fill=BLACK,width=1)

# ─── ACTIVITY DIAGRAM ENGINE ─────────────────────────────────────────────────
class ActivityDiagram:
    """
    Two-lane activity diagram.
    All elements are measured and placed precisely — no overlap, no overflow.
    """
    PAD    = 16   # outer padding
    TITLE_H= 20   # title bar height
    HDR_H  = 26   # swimlane header height
    GAP    = 14   # vertical gap between elements
    ARROW  = 18   # arrow segment length
    MIN_BW = 160  # minimum box width

    def __init__(self, title, lane1, lane2, lane1_w=None, lane2_w=None):
        self.title  = title
        self.lanes  = [lane1, lane2]
        self._items = []   # list of layout items
        self._lw    = [lane1_w, lane2_w]  # will be computed

    # ── item adders ──────────────────────────────────────────────────────────
    def start(self, lane=0):
        self._items.append(("start", lane))

    def end(self, lane=0):
        self._items.append(("end", lane))

    def action(self, lane, txt):
        self._items.append(("action", lane, txt))

    def decision(self, lane, txt, yes_label="Ya", no_label="Tidak",
                 yes_dir="down", no_dir="right"):
        """yes_dir: down=continue, no_dir: right=branch to note"""
        self._items.append(("decision", lane, txt, yes_label, no_label, yes_dir, no_dir))

    def cross(self, from_lane, to_lane, lbl=""):
        """Arrow crossing swimlane boundary."""
        self._items.append(("cross", from_lane, to_lane, lbl))

    def cross_return(self, from_lane, to_lane, lbl=""):
        self._items.append(("cross_ret", from_lane, to_lane, lbl))

    def separator(self, txt=""):
        self._items.append(("sep", txt))

    def note(self, lane, txt):
        self._items.append(("note", lane, txt))

    # ── measure ──────────────────────────────────────────────────────────────
    def _measure(self):
        """Compute required lane widths from content."""
        needed = [self.MIN_BW, self.MIN_BW]
        for item in self._items:
            if item[0] in ("action","note"):
                lane, txt = item[1], item[2]
                w,_ = box_size(txt, FB)
                needed[lane] = max(needed[lane], w + 40)
            elif item[0] == "decision":
                lane, txt = item[1], item[2]
                tw,_ = text_size(txt, FS)
                needed[lane] = max(needed[lane], tw + 80)
        for i in range(2):
            if self._lw[i] is None:
                self._lw[i] = needed[i]

    # ── render ───────────────────────────────────────────────────────────────
    def render(self, filename):
        self._measure()
        P = self.PAD; TH = self.TITLE_H; HH = self.HDR_H
        G = self.GAP; AH = self.ARROW

        lw = self._lw
        total_w = lw[0] + lw[1] + P*2
        cx = [P + lw[0]//2, P + lw[0] + lw[1]//2]

        # ── first pass: compute total height ─────────────────────────────────
        y = P + TH + HH + G
        for item in self._items:
            t = item[0]
            if t == "start":
                y += 9 + AH
            elif t == "end":
                y += 9 + G
            elif t == "action":
                txt = item[2]
                _,bh = box_size(txt, FB)
                y += bh + AH
            elif t == "decision":
                txt = item[2]
                _,th = text_size(txt, FS)
                dh = th + 28
                y += dh + AH
            elif t in ("cross","cross_ret"):
                y += 0   # same y as previous
            elif t == "sep":
                y += 16
            elif t == "note":
                txt = item[2]
                _,nh = box_size(txt, FS, pad_x=10, pad_y=6)
                y += nh + G
        total_h = y + P + 20

        # ── create canvas ────────────────────────────────────────────────────
        img = Image.new("RGB", (total_w, total_h), BG)
        d   = ImageDraw.Draw(img)

        # outer border
        d.rectangle([P,P,total_w-P,total_h-P], outline=BLACK, width=1)
        # title
        d.text((P+4, P+3), self.title, font=FT, fill=BLACK)

        # swimlane backgrounds
        sw_top = P + TH
        for i in range(2):
            x0 = P + sum(lw[:i])
            x1 = x0 + lw[i]
            d.rectangle([x0,sw_top,x1,total_h-P], fill=SWBG, outline=BLACK, width=1)
            d.rectangle([x0,sw_top,x1,sw_top+HH], fill=SWHDR, outline=BLACK, width=1)
            draw_text_center(d, cx[i], sw_top+HH//2, self.lanes[i], FH)

        # ── second pass: draw elements ────────────────────────────────────────
        y = P + TH + HH + G
        prev_box_bot = [y, y]   # bottom y of last element per lane
        prev_cx_y    = [y, y]   # last y position per lane

        def lane_cx(lane): return cx[lane]

        for item in self._items:
            t = item[0]

            if t == "start":
                lane = item[1]
                lx = lane_cx(lane)
                draw_start(d, lx, y)
                draw_arrow(d, lx, y+9, lx, y+9+AH)
                y += 9 + AH
                prev_box_bot[lane] = y

            elif t == "end":
                lane = item[1]
                lx = lane_cx(lane)
                draw_arrow(d, lx, y, lx, y+AH)
                draw_end(d, lx, y+AH+9)
                y += AH + 18 + G

            elif t == "action":
                lane, txt = item[1], item[2]
                lx = lane_cx(lane)
                bw, bh = box_size(txt, FB)
                bw = max(bw, self.MIN_BW)
                cy_box = y + bh//2
                draw_box(d, lx, cy_box, txt, FB, min_w=bw)
                draw_arrow(d, lx, cy_box+bh//2, lx, cy_box+bh//2+AH)
                prev_box_bot[lane] = cy_box + bh//2
                y = cy_box + bh//2 + AH

            elif t == "decision":
                lane, txt, ylbl, nlbl = item[1], item[2], item[3], item[4]
                lx = lane_cx(lane)
                tw, th = text_size(txt, FS)
                dw = tw + 40; dh = th + 28
                hw, hh = dw//2, dh//2
                cy_d = y + hh
                draw_diamond(d, lx, cy_d, txt, FS)
                # Yes arrow (down)
                draw_arrow(d, lx, cy_d+hh, lx, cy_d+hh+AH, ylbl, FS)
                # No arrow (right) — to note box
                no_x = lx + hw + 8
                no_end = P + lw[0] + lw[1] - 30
                draw_arrow(d, lx+hw, cy_d, no_end, cy_d, nlbl, FS)
                # note box for "Tidak" branch
                note_txt = "Tampilkan\npesan error"
                nw, nh = box_size(note_txt, FS, pad_x=8, pad_y=6)
                nx0 = no_end + 4
                if nx0 + nw > total_w - P - 4:
                    nx0 = total_w - P - nw - 4
                d.rounded_rectangle([nx0, cy_d-nh//2, nx0+nw, cy_d+nh//2],
                                     radius=5, fill=BOXF, outline=BOXBD, width=1)
                draw_text_center(d, nx0+nw//2, cy_d, note_txt, FS)
                prev_box_bot[lane] = cy_d + hh
                y = cy_d + hh + AH

            elif t == "cross":
                from_l, to_l, lbl = item[1], item[2], item[3]
                # horizontal arrow at current y
                x1 = cx[from_l] + (lw[from_l]//2 if from_l < to_l else -lw[from_l]//2)
                x2 = cx[to_l]   - (lw[to_l]//2   if from_l < to_l else -lw[to_l]//2)
                draw_arrow(d, x1, y, x2, y, lbl, FS)

            elif t == "cross_ret":
                from_l, to_l, lbl = item[1], item[2], item[3]
                x1 = cx[from_l] + (lw[from_l]//2 if from_l < to_l else -lw[from_l]//2)
                x2 = cx[to_l]   - (lw[to_l]//2   if from_l < to_l else -lw[to_l]//2)
                draw_darrow(d, x1, y, x2, y, lbl, FS)

            elif t == "sep":
                txt = item[1]
                d.line([(P+4, y+6), (total_w-P-4, y+6)], fill=LGRAY, width=1)
                if txt:
                    bb = FS.getbbox(txt); tw = bb[2]-bb[0]
                    d.text((P + lw[0]//2 - tw//2, y+8), txt, font=FS, fill=GRAY)
                y += 16

            elif t == "note":
                lane, txt = item[1], item[2]
                lx = lane_cx(lane)
                nw, nh = box_size(txt, FS, pad_x=10, pad_y=6)
                nw = max(nw, 120)
                d.rounded_rectangle([lx-nw//2, y, lx+nw//2, y+nh],
                                     radius=5, fill=BOXF, outline=BOXBD, width=1)
                draw_text_center(d, lx, y+nh//2, txt, FS)
                y += nh + G

        path = f"{OUT}/{filename}"
        img.save(path, "PNG", dpi=(150,150))
        print(f"  {filename}  ({total_w}x{total_h})")

# ─── SEQUENCE DIAGRAM ENGINE ─────────────────────────────────────────────────
class SequenceDiagram:
    """
    Sequence diagram with precise layout.
    Lifelines auto-spaced, messages measured from text.
    """
    PAD     = 14
    TITLE_H = 20
    BOX_H   = 38
    MSG_GAP = 26   # vertical gap between messages
    LIFE_PAD= 20   # extra space after last message

    def __init__(self, title, participants):
        """participants: list of label strings"""
        self.title = title
        self.parts = participants
        self.msgs  = []

    def msg(self, src, tgt, txt, ret=False, self_call=False):
        self.msgs.append((src, tgt, txt, ret, self_call))

    def _part_width(self, lbl):
        tw, _ = text_size(lbl, FS)
        return max(tw + 24, 100)

    def render(self, filename):
        P = self.PAD; TH = self.TITLE_H; BH = self.BOX_H
        MG = self.MSG_GAP

        # compute x centers with enough spacing
        xs = {}
        x = P
        for lbl in self.parts:
            pw = self._part_width(lbl)
            # also check all messages involving this participant
            xs[lbl] = x + pw//2
            x += pw + 30   # 30px gap between lifelines

        total_w = x + P
        total_h = P + TH + BH + len(self.msgs)*MG + self.LIFE_PAD + P + 20

        img = Image.new("RGB", (total_w, total_h), BG)
        d   = ImageDraw.Draw(img)

        # border + title
        d.rectangle([P,P,total_w-P,total_h-P], outline=BLACK, width=1)
        d.text((P+4, P+3), self.title, font=FT, fill=BLACK)

        # lifeline headers
        y_hdr = P + TH
        for lbl in self.parts:
            cx = xs[lbl]
            pw = self._part_width(lbl)
            d.rounded_rectangle([cx-pw//2, y_hdr, cx+pw//2, y_hdr+BH],
                                  radius=5, fill=(255,255,204), outline=BLACK, width=1)
            draw_text_center(d, cx, y_hdr+BH//2, lbl, FS)

        # dashed lifelines
        for lbl in self.parts:
            cx = xs[lbl]
            y = y_hdr + BH
            while y < total_h - P - 10:
                d.line([(cx,y),(cx,min(y+5,total_h-P-10))], fill=LGRAY, width=1)
                y += 10

        # messages
        y = y_hdr + BH + MG
        for src, tgt, txt, ret, self_call in self.msgs:
            x1 = xs[src]; x2 = xs[tgt]

            if self_call:
                # self-call loop box
                loop_w = 28; loop_h = 18
                d.line([(x1,y),(x1+loop_w,y)], fill=BLACK, width=1)
                d.line([(x1+loop_w,y),(x1+loop_w,y+loop_h)], fill=BLACK, width=1)
                d.line([(x1+loop_w,y+loop_h),(x1,y+loop_h)], fill=BLACK, width=1)
                d.polygon([(x1,y+loop_h),(x1+8,y+loop_h-4),(x1+8,y+loop_h+4)], fill=BLACK)
                # label to the right
                d.text((x1+loop_w+4, y), txt, font=FS, fill=BLACK)
                y += MG
                continue

            # measure label
            bb = FS.getbbox(txt); tw = bb[2]-bb[0]
            mx = (x1+x2)//2

            if ret:
                # dashed return arrow
                dx = x2-x1; L = max(1,abs(dx)); n = int(L/7)
                for j in range(n):
                    if j%2==0:
                        t1,t2 = j/n, min(1,(j+.5)/n)
                        d.line([(int(x1+dx*t1),y),(int(x1+dx*t2),y)], fill=BLACK, width=1)
                if x2>x1: d.polygon([(x2,y),(x2-8,y-4),(x2-8,y+4)], fill=BLACK)
                else:      d.polygon([(x2,y),(x2+8,y-4),(x2+8,y+4)], fill=BLACK)
            else:
                d.line([(x1,y),(x2,y)], fill=BLACK, width=1)
                if x2>x1: d.polygon([(x2,y),(x2-8,y-4),(x2-8,y+4)], fill=BLACK)
                else:      d.polygon([(x2,y),(x2+8,y-4),(x2+8,y+4)], fill=BLACK)

            # label — centered above arrow, clipped to canvas
            lx = mx - tw//2
            lx = max(P+2, min(lx, total_w-P-tw-2))
            d.text((lx, y-13), txt, font=FS, fill=BLACK)
            y += MG

        path = f"{OUT}/{filename}"
        img.save(path, "PNG", dpi=(150,150))
        print(f"  {filename}  ({total_w}x{total_h})")

# ═════════════════════════════════════════════════════════════════════════════
# ACTIVITY DIAGRAMS
# ═════════════════════════════════════════════════════════════════════════════

# ── ACT-01 LOGIN ─────────────────────────────────────────────────────────────
def act_login():
    g = ActivityDiagram("act  Login & Logout — SimAset RBTV Bengkulu",
                        "Pengguna", "Sistem", 300, 380)
    g.start(0)
    g.action(0, "Buka halaman /login")
    g.cross(0, 1)
    g.action(1, "Tampilkan halaman login")
    g.cross_return(1, 0)
    g.action(0, "Input Email & Password")
    g.cross(0, 1)
    g.action(1, "Validasi input\n(email required, password required)")
    g.decision(1, "Input\nvalid?", "Ya", "Tidak")
    g.action(1, "Cek Rate Limit\n(5x/menit per email+IP)")
    g.decision(1, "Rate\nlimit?", "Tidak", "Ya")
    g.action(1, "Cari user by email\nCek is_active = 1\nAuth::attempt(email, password)")
    g.decision(1, "Kredensial\nbenar?", "Ya", "Tidak")
    g.action(1, "session()->regenerate()\nUpdate last_login_at\nActivityLogger::logAuth('Login',...)")
    g.action(1, "redirect()->route('dashboard')")
    g.cross_return(1, 0)
    g.action(0, "Melihat Dashboard")
    g.separator("— Logout —")
    g.action(0, "Klik tombol Logout")
    g.cross(0, 1)
    g.action(1, "logAuth('Logout',...)\nAuth::logout()\nsession()->invalidate()\nsession()->regenerateToken()")
    g.action(1, "redirect('/')")
    g.cross_return(1, 0)
    g.action(0, "Kembali ke halaman Login")
    g.end(0)
    g.render("ACT_01_Login.png")

act_login()

# ── ACT-02 MANAJEMEN ASET ────────────────────────────────────────────────────
def act_aset():
    g = ActivityDiagram("act  Manajemen Aset (CRUD + QR) — SimAset RBTV Bengkulu",
                        "Pengguna", "Sistem", 280, 420)
    g.start(0)
    g.action(0, 'Pilih menu "Aset"')
    g.cross(0, 1)
    g.action(1, "Asset::with([barang,ruangan])\n->paginate(15)\nTampilkan daftar + stats + filter")
    g.cross_return(1, 0)
    g.action(0, "Pilih aksi")
    g.separator("— Tambah Aset —")
    g.action(0, "Isi Form Aset\n(Barang*, Ruangan*, Kondisi*,\nStatus*, Tgl Perolehan*, Serial,\nJumlah, Harga, Sumber, Foto)")
    g.action(0, "Klik Simpan Aset")
    g.cross(0, 1)
    g.action(1, "Validasi server-side\n(required, exists, unique, dll)")
    g.decision(1, "Validasi\ngagal?", "Tidak", "Ya")
    g.action(1, "generateKode() [gap-filling]\nSimpan foto ke public/foto_aset/\nAsset::create([..., created_by])\nlogAsset('Create',...)")
    g.cross_return(1, 0)
    g.separator("— Edit Aset —")
    g.action(0, "Klik Edit (✏) pada aset")
    g.cross(0, 1)
    g.action(1, "Load aset + dropdown Barang & Ruangan\nTampilkan form edit terisi")
    g.cross_return(1, 0)
    g.action(0, "Ubah data → Klik Simpan")
    g.cross(0, 1)
    g.action(1, "Validasi → $asset->update([..., updated_by])\nlogAsset('Update',...)")
    g.cross_return(1, 0)
    g.separator("— Hapus Aset —")
    g.action(0, "Klik Hapus (🗑)\nKonfirmasi SweetAlert2")
    g.cross(0, 1)
    g.action(1, "$asset->delete() [Soft Delete: isi deleted_at]\nlogAsset('Delete',...)")
    g.cross_return(1, 0)
    g.separator("— Generate QR Code —")
    g.action(0, "Klik Generate QR Code")
    g.cross(0, 1)
    g.action(1, "Cek file QR ada?\nRequest API qrserver.com\nSimpan PNG ke public/qr_codes/")
    g.cross_return(1, 0)
    g.end(0)
    g.render("ACT_02_Aset.png")

act_aset()

# ── ACT-03 MANAJEMEN BARANG ──────────────────────────────────────────────────
def act_barang():
    g = ActivityDiagram("act  Manajemen Barang (CRUD) — SimAset RBTV Bengkulu",
                        "Pengguna", "Sistem", 280, 420)
    g.start(0)
    g.action(0, 'Pilih menu "Barang"')
    g.cross(0, 1)
    g.action(1, "Query Barang dari database\nTampilkan daftar (tabel + filter)")
    g.cross_return(1, 0)
    g.action(0, "Pilih aksi")
    g.separator("— Tambah Barang —")
    g.action(0, "Isi form:\nNama Barang*, Kategori*, Status*,\nKeterangan")
    g.action(0, "Klik Simpan")
    g.cross(0, 1)
    g.action(1, "Validasi (nama*, kategori*, status*)\ngenerateKode() [BRG-001, BRG-002,...]\nBarang::create()\nredirect + success")
    g.cross_return(1, 0)
    g.separator("— Edit Barang —")
    g.action(0, "Klik Edit pada barang")
    g.cross(0, 1)
    g.action(1, "Load barang → Tampilkan form edit\nValidasi → $barang->update()\nredirect + success")
    g.cross_return(1, 0)
    g.separator("— Hapus Barang —")
    g.action(0, "Klik Hapus → Konfirmasi")
    g.cross(0, 1)
    g.action(1, "$barang->delete() [Soft Delete]\nredirect + success")
    g.cross_return(1, 0)
    g.separator("— Lihat Detail —")
    g.action(0, "Klik Detail barang")
    g.cross(0, 1)
    g.action(1, "Barang::with([aset])->findOrFail()\nview(barang.show)\nTampilkan detail + daftar aset terkait")
    g.cross_return(1, 0)
    g.end(0)
    g.render("ACT_03_Barang.png")

act_barang()

# ── ACT-04 MANAJEMEN RUANGAN ─────────────────────────────────────────────────
def act_ruangan():
    g = ActivityDiagram("act  Manajemen Ruangan (CRUD) — SimAset RBTV Bengkulu",
                        "Pengguna", "Sistem", 280, 420)
    g.start(0)
    g.action(0, 'Pilih menu "Ruangan"')
    g.cross(0, 1)
    g.action(1, "Ruangan::withCount('assets')->paginate(15)\nTampilkan daftar + stats")
    g.cross_return(1, 0)
    g.action(0, "Pilih aksi")
    g.separator("— Tambah Ruangan —")
    g.action(0, "Isi form:\nNama Ruangan*, Lantai, Keterangan")
    g.action(0, "Klik Simpan")
    g.cross(0, 1)
    g.action(1, "Validasi (nama*)\nRuangan::create()\nredirect + success")
    g.cross_return(1, 0)
    g.separator("— Edit Ruangan —")
    g.action(0, "Klik Edit pada ruangan")
    g.cross(0, 1)
    g.action(1, "Load ruangan → Tampilkan form edit\nValidasi → $ruangan->update()\nredirect + success")
    g.cross_return(1, 0)
    g.separator("— Hapus Ruangan —")
    g.action(0, "Klik Hapus → Konfirmasi")
    g.cross(0, 1)
    g.action(1, "Cek: $ruangan->assets()->count() > 0?\nJika ada aset: TOLAK + pesan error\nJika kosong: $ruangan->delete()")
    g.cross_return(1, 0)
    g.end(0)
    g.render("ACT_04_Ruangan.png")

act_ruangan()

# ── ACT-05 KELOLA PENGGUNA ───────────────────────────────────────────────────
def act_pengguna():
    g = ActivityDiagram("act  Kelola Pengguna (Admin Only) — SimAset RBTV Bengkulu",
                        "Admin", "Sistem", 280, 420)
    g.start(0)
    g.action(0, 'Klik menu "Kelola Pengguna"')
    g.cross(0, 1)
    g.action(1, "Cek middleware role:admin\n(RoleMiddleware::handle())")
    g.decision(1, "Role =\nadmin?", "Ya", "Tidak")
    g.action(1, "User::orderBy('role')->get()\nview(users.index)")
    g.cross_return(1, 0)
    g.action(0, "Pilih aksi")
    g.separator("— Tambah Pengguna —")
    g.action(0, "Isi form:\nNama*, Email*, Password*\n(min 8, upper+lower+angka)\nRole*, Kirim Email?")
    g.action(0, "Klik Simpan")
    g.cross(0, 1)
    g.action(1, "Validasi (email unique, password regex)\nHash::make(password)\nUser::create([..., is_active:true])\nKirim AkunBaruMail (jika dicentang)\nredirect + success")
    g.cross_return(1, 0)
    g.separator("— Edit Pengguna —")
    g.action(0, "Klik Edit pada pengguna")
    g.cross(0, 1)
    g.action(1, "Load user → Tampilkan form edit\nValidasi → $user->update()\nredirect + success")
    g.cross_return(1, 0)
    g.separator("— Hapus Pengguna —")
    g.action(0, "Klik Hapus → Konfirmasi")
    g.cross(0, 1)
    g.action(1, "Cek: bukan akun sendiri\n$user->delete() [hard delete]\nredirect + success")
    g.cross_return(1, 0)
    g.end(0)
    g.render("ACT_05_Pengguna.png")

act_pengguna()

# ── ACT-06 SCANNER QR ────────────────────────────────────────────────────────
def act_qr():
    g = ActivityDiagram("act  Scanner QR Code — SimAset RBTV Bengkulu",
                        "Pengguna", "Sistem", 280, 420)
    g.start(0)
    g.action(0, 'Klik menu "QR Scanner"')
    g.cross(0, 1)
    g.action(1, "GET /qrcode/scanner\nview(qrcode.scanner)\nMinta izin kamera browser")
    g.cross_return(1, 0)
    g.action(0, "Izinkan akses kamera")
    g.action(0, "Arahkan kamera ke\nQR Code aset fisik")
    g.cross(0, 1)
    g.action(1, "Decode QR (JavaScript)\nBaca URL dari QR\nParse kode_aset dari URL")
    g.action(1, "GET /aset/{kode}/detail [route PUBLIK]\nAsset::with([barang,ruangan,creator])\n->where('kode_aset',$kode)->firstOrFail()")
    g.decision(1, "Aset\nditemukan?", "Ya", "Tidak")
    g.action(1, "Tampilkan detail aset:\nNama Barang, Kategori, Ruangan,\nKondisi, Status, Serial, Tgl Perolehan")
    g.cross_return(1, 0)
    g.action(0, "Melihat detail aset")
    g.end(0)
    g.render("ACT_06_ScannerQR.png")

act_qr()

# ── ACT-07 IMPORT DATA ───────────────────────────────────────────────────────
def act_import():
    g = ActivityDiagram("act  Import Data (Excel/CSV) — SimAset RBTV Bengkulu",
                        "Pengguna", "Sistem", 280, 420)
    g.start(0)
    g.action(0, 'Pilih menu "Import"')
    g.cross(0, 1)
    g.action(1, "Tampilkan halaman import\n(pilih tipe: Aset / Barang)\n+ tombol Download Template")
    g.cross_return(1, 0)
    g.action(0, "Download Template (opsional)\nIsi data di template Excel/CSV")
    g.action(0, "Pilih tipe (Aset / Barang)\nUpload file Excel/CSV\nKlik Import")
    g.cross(0, 1)
    g.action(1, "POST /import {file, type}\nValidasi: mimes:xlsx,xls,csv\ntype in:aset,barang")
    g.decision(1, "File\nvalid?", "Ya", "Tidak")
    g.action(1, "Baca setiap baris data\nValidasi per baris\nAsset::create() / Barang::create()\nHitung: X berhasil, Y gagal")
    g.action(1, "redirect + flash:\n'Import selesai: X berhasil, Y gagal'")
    g.cross_return(1, 0)
    g.action(0, "Lihat hasil import\ndi daftar data")
    g.end(0)
    g.render("ACT_07_Import.png")

act_import()

# ── ACT-08 EXPORT & LAPORAN ──────────────────────────────────────────────────
def act_export():
    g = ActivityDiagram("act  Export & Laporan — SimAset RBTV Bengkulu",
                        "Pengguna", "Sistem", 280, 420)
    g.start(0)
    g.action(0, 'Pilih menu "Laporan"')
    g.cross(0, 1)
    g.action(1, "Tampilkan halaman laporan\n(daftar ruangan + jumlah aset)")
    g.cross_return(1, 0)
    g.action(0, "Pilih jenis laporan")
    g.separator("— Laporan Aset —")
    g.action(0, "Atur filter (opsional)\nKlik Tampilkan")
    g.cross(0, 1)
    g.action(1, "Query aset dengan filter\nTampilkan tabel hasil")
    g.cross_return(1, 0)
    g.action(0, "Pilih format output")
    g.separator("— Cetak PDF —")
    g.action(0, "Klik Cetak PDF")
    g.cross(0, 1)
    g.action(1, "GET /laporan/assets/cetak\nBarryvdh DomPDF\nDownload PDF (A4 landscape)")
    g.cross_return(1, 0)
    g.separator("— Export Excel —")
    g.action(0, "Klik Export Excel")
    g.cross(0, 1)
    g.action(1, "GET /laporan/assets/export\nMaatwebsite Excel\nDownload .xlsx")
    g.cross_return(1, 0)
    g.separator("— Laporan Per Ruangan —")
    g.action(0, "Klik nama ruangan")
    g.cross(0, 1)
    g.action(1, "GET /laporan/ruangan/{id}\nQuery aset di ruangan\nDomPDF → Download PDF")
    g.cross_return(1, 0)
    g.separator("— Laporan Maintenance —")
    g.action(0, "Klik Laporan Maintenance\nPilih format (PDF / CSV)")
    g.cross(0, 1)
    g.action(1, "Query status=Maintenance\nGenerate PDF atau CSV\nDownload file")
    g.cross_return(1, 0)
    g.end(0)
    g.render("ACT_08_Export.png")

act_export()

# ── ACT-09 AUDIT LOG ─────────────────────────────────────────────────────────
def act_auditlog():
    g = ActivityDiagram("act  Audit Log (Activity Log) — SimAset RBTV Bengkulu",
                        "Admin", "Sistem", 280, 420)
    g.start(0)
    g.action(0, 'Klik menu "Log Aktivitas"')
    g.cross(0, 1)
    g.action(1, "Cek middleware role:admin\nActivityLog::with('user')\n->orderBy('created_at','desc')\n->paginate(20)\nTampilkan tabel log")
    g.cross_return(1, 0)
    g.action(0, "Atur filter (opsional):\n- Kata kunci\n- Pengguna\n- Modul (Login/Create/Update/Delete)\nKlik Filter")
    g.cross(0, 1)
    g.action(1, "Query dengan WHERE clause:\naktivitas LIKE %keyword%\nuser_id = $user_id\naktivitas LIKE %module%\nTampilkan hasil (paginated 20/hal)")
    g.cross_return(1, 0)
    g.action(0, "Melihat riwayat\naktivitas pengguna")
    g.end(0)
    g.render("ACT_09_AuditLog.png")

act_auditlog()

# ── ACT-10 MAINTENANCE ───────────────────────────────────────────────────────
def act_maintenance():
    g = ActivityDiagram("act  Maintenance Aset — SimAset RBTV Bengkulu",
                        "Staff / Admin", "Sistem", 280, 420)
    g.start(0)
    g.separator("— Set Aset ke Maintenance —")
    g.action(0, "Buka Detail Aset\nKlik Set Maintenance")
    g.cross(0, 1)
    g.action(1, "Tampilkan modal konfirmasi\n+ input keterangan (opsional)")
    g.cross_return(1, 0)
    g.action(0, "Input keterangan (opsional)\nKlik Konfirmasi")
    g.cross(0, 1)
    g.action(1, "POST /maintenance/{kode}/set\nupdate([status=>'Maintenance', updated_by])\nlogAsset('Update','Aset masuk maintenance...')\nredirect back + success")
    g.cross_return(1, 0)
    g.separator("— Selesaikan Maintenance —")
    g.action(0, "Buka menu Maintenance\nKlik Selesai pada aset")
    g.cross(0, 1)
    g.action(1, "Tampilkan modal:\n- Pilih kondisi akhir (wajib)\n- Input keterangan")
    g.cross_return(1, 0)
    g.action(0, "Pilih kondisi akhir\n(Baik / Rusak Ringan / Rusak Berat)\nKlik Konfirmasi Selesai")
    g.cross(0, 1)
    g.action(1, "PATCH /maintenance/{kode}/complete\nValidasi: kondisi required")
    g.decision(1, "Validasi\ngagal?", "Tidak", "Ya")
    g.action(1, "update([status=>'Aktif', kondisi, updated_by])\nlogAsset('Update','Maintenance selesai...')\nQuery Admin aktif\nMail::to()->send(MaintenanceAlert)")
    g.cross_return(1, 0)
    g.action(0, "Aset kembali berstatus Aktif\nAdmin menerima email notifikasi")
    g.end(0)
    g.render("ACT_10_Maintenance.png")

act_maintenance()

# ═════════════════════════════════════════════════════════════════════════════
# SEQUENCE DIAGRAMS
# ═════════════════════════════════════════════════════════════════════════════

# ── SEQ-01 LOGIN ─────────────────────────────────────────────────────────────
def seq_login():
    s = SequenceDiagram("sd  Sequence — Login SimAset RBTV Bengkulu", [
        ":Admin", ":Browser", ":Router", ":AuthController",
        ":LoginRequest", ":RateLimiter", ":User Model", ":Database", ":ActivityLogger"
    ])
    s.msg(":Admin",":Browser","Buka /login")
    s.msg(":Browser",":Router","GET /login [middleware:guest]")
    s.msg(":Router",":AuthController","create()")
    s.msg(":AuthController",":Browser","view(auth.login)",ret=True)
    s.msg(":Browser",":Admin","Halaman login ditampilkan",ret=True)
    s.msg(":Admin",":Browser","Input email+password → Klik Masuk")
    s.msg(":Browser",":Router","POST /login {email, password}")
    s.msg(":Router",":AuthController","store(LoginRequest)")
    s.msg(":AuthController",":LoginRequest","validate() [email, password required]")
    s.msg(":LoginRequest",":RateLimiter","tooManyAttempts(throttleKey, 5)")
    s.msg(":RateLimiter",":LoginRequest","false (belum terlampaui)",ret=True)
    s.msg(":LoginRequest",":User Model","where('email',$email)->first()")
    s.msg(":User Model",":Database","SELECT * FROM users WHERE email=?")
    s.msg(":Database",":User Model","User record",ret=True)
    s.msg(":User Model",":LoginRequest","$user",ret=True)
    s.msg(":LoginRequest",":LoginRequest","Cek is_active = 1",self_call=True)
    s.msg(":LoginRequest",":LoginRequest","Auth::attempt(email, password)",self_call=True)
    s.msg(":LoginRequest",":RateLimiter","clear(throttleKey)")
    s.msg(":AuthController",":AuthController","session()->regenerate()",self_call=True)
    s.msg(":AuthController",":User Model","update([last_login_at => now()])")
    s.msg(":User Model",":Database","UPDATE users SET last_login_at=NOW()")
    s.msg(":AuthController",":ActivityLogger","logAuth('Login','User berhasil login...')")
    s.msg(":ActivityLogger",":Database","INSERT INTO log_aktivitas")
    s.msg(":AuthController",":Browser","redirect()->route('dashboard') [302]",ret=True)
    s.msg(":Browser",":Admin","Diarahkan ke /dashboard",ret=True)
    s.render("SEQ_01_Login.png")

seq_login()

# ── SEQ-02 TAMBAH ASET ───────────────────────────────────────────────────────
def seq_tambah_aset():
    s = SequenceDiagram("sd  Sequence — Tambah Aset Baru — SimAset RBTV Bengkulu", [
        ":Pengguna", ":Browser", ":AssetController",
        ":Barang Model", ":Ruangan Model", ":Asset Model",
        ":Database", ":FileSystem", ":ActivityLogger"
    ])
    s.msg(":Pengguna",":Browser","Klik + Tambah Aset")
    s.msg(":Browser",":AssetController","GET /aset/create")
    s.msg(":AssetController",":Barang Model","where('status','aktif')->get()")
    s.msg(":Barang Model",":Database","SELECT kode_barang,nama_barang FROM barang WHERE status=aktif")
    s.msg(":Database",":Barang Model","[BRG-001 Kamera Sony A7, BRG-002 Mic Rode]",ret=True)
    s.msg(":AssetController",":Ruangan Model","orderBy('nama')->get()")
    s.msg(":Ruangan Model",":Database","SELECT * FROM ruangan ORDER BY nama")
    s.msg(":Database",":Ruangan Model","[Studio 1, Studio 2, Ruang Editing, Ruang Redaksi]",ret=True)
    s.msg(":AssetController",":Browser","view(aset.create, compact(barangs,ruangans))",ret=True)
    s.msg(":Browser",":Pengguna","Form tambah aset ditampilkan",ret=True)
    s.msg(":Pengguna",":Browser","Isi form → Klik Simpan Aset")
    s.msg(":Browser",":AssetController","POST /aset {kode_barang,ruangan_id,kondisi,status,...}")
    s.msg(":AssetController",":AssetController","$request->validate([...])",self_call=True)
    s.msg(":AssetController",":Asset Model","generateKode() [gap-filling]")
    s.msg(":Asset Model",":Database","SELECT kode_aset FROM aset WITH TRASHED")
    s.msg(":Database",":Asset Model","[AST-001, AST-002]",ret=True)
    s.msg(":Asset Model",":AssetController","'AST-003' (kode baru)",ret=True)
    s.msg(":AssetController",":FileSystem","foto->move(public/foto_aset/, timestamp_nama)")
    s.msg(":FileSystem",":AssetController","nama file tersimpan",ret=True)
    s.msg(":AssetController",":Asset Model","Asset::create([kode_aset=AST-003,...,created_by])")
    s.msg(":Asset Model",":Database","INSERT INTO aset (...) VALUES (...)")
    s.msg(":Database",":Asset Model","Record tersimpan",ret=True)
    s.msg(":AssetController",":ActivityLogger","logAsset('Create','Menambahkan aset baru...')")
    s.msg(":ActivityLogger",":Database","INSERT INTO log_aktivitas")
    s.msg(":AssetController",":Browser","redirect()->route('aset.index') + flash success",ret=True)
    s.msg(":Browser",":Pengguna","Daftar aset + notifikasi sukses",ret=True)
    s.render("SEQ_02_TambahAset.png")

seq_tambah_aset()

# ── SEQ-03 SCAN QR ───────────────────────────────────────────────────────────
def seq_qr():
    s = SequenceDiagram("sd  Sequence — Generate & Scan QR Code — SimAset RBTV Bengkulu", [
        ":Pengguna", ":Browser", ":QrCodeController",
        ":AssetController", ":Asset Model",
        ":Database", ":qrserver.com", ":FileSystem"
    ])
    s.msg(":Pengguna",":Browser","Klik Generate QR Code (AST-001)")
    s.msg(":Browser",":AssetController","POST /aset/AST-001/generate-qr")
    s.msg(":AssetController",":Asset Model","where('kode_aset','AST-001')->firstOrFail()")
    s.msg(":Asset Model",":Database","SELECT * FROM aset WHERE kode_aset=AST-001")
    s.msg(":Database",":Asset Model","Asset record",ret=True)
    s.msg(":AssetController",":FileSystem","glob(qr_codes/qr_AST-001*.png)")
    s.msg(":FileSystem",":AssetController","[] (belum ada file)",ret=True)
    s.msg(":AssetController",":qrserver.com","GET ?size=300x300&data={url_detail_aset}")
    s.msg(":qrserver.com",":AssetController","PNG binary data (300x300)",ret=True)
    s.msg(":AssetController",":FileSystem","file_put_contents(qr_AST-001_{ts}.png)")
    s.msg(":AssetController",":Browser","redirect()->back() + success",ret=True)
    s.msg(":Browser",":Pengguna","QR Code berhasil di-generate",ret=True)
    s.msg(":Pengguna",":Browser","Buka menu QR Scanner")
    s.msg(":Browser",":QrCodeController","GET /qrcode/scanner")
    s.msg(":QrCodeController",":Browser","view(qrcode.scanner) [akses kamera]",ret=True)
    s.msg(":Pengguna",":Browser","Arahkan kamera ke QR Code aset fisik")
    s.msg(":Browser",":Browser","Decode QR → URL: /aset/AST-001/detail",self_call=True)
    s.msg(":Browser",":AssetController","GET /aset/AST-001/detail [route PUBLIK]")
    s.msg(":AssetController",":Asset Model","with([barang,ruangan,creator])->firstOrFail()")
    s.msg(":Asset Model",":Database","SELECT aset.*,barang.*,ruangan.* WHERE kode_aset=AST-001")
    s.msg(":Database",":Asset Model","{Kamera Sony A7, Ruang Editing, Maintenance}",ret=True)
    s.msg(":AssetController",":Browser","view(aset.show, compact(asset))",ret=True)
    s.msg(":Browser",":Pengguna","Detail: Kamera Sony A7 | Maintenance | Ruang Editing",ret=True)
    s.render("SEQ_03_ScanQR.png")

seq_qr()

# ── SEQ-04 MAINTENANCE ───────────────────────────────────────────────────────
def seq_maintenance():
    s = SequenceDiagram("sd  Sequence — Maintenance Aset — SimAset RBTV Bengkulu", [
        ":Staff/Admin", ":Browser", ":MaintenanceController",
        ":Asset Model", ":User Model",
        ":Database", ":ActivityLogger", ":SMTP Server"
    ])
    s.msg(":Staff/Admin",":Browser","Buka detail AST-001 → Klik Set Maintenance")
    s.msg(":Browser",":MaintenanceController","POST /maintenance/AST-001/set {keterangan}")
    s.msg(":MaintenanceController",":Asset Model","where('kode_aset','AST-001')->firstOrFail()")
    s.msg(":Asset Model",":Database","SELECT * FROM aset WHERE kode_aset=AST-001")
    s.msg(":Database",":Asset Model","Asset record",ret=True)
    s.msg(":MaintenanceController",":Asset Model","update([status=>'Maintenance', updated_by])")
    s.msg(":Asset Model",":Database","UPDATE aset SET status=Maintenance WHERE kode_aset=AST-001")
    s.msg(":MaintenanceController",":ActivityLogger","logAsset('Update','Aset masuk maintenance...')")
    s.msg(":ActivityLogger",":Database","INSERT INTO log_aktivitas")
    s.msg(":MaintenanceController",":Browser","redirect()->back() + success",ret=True)
    s.msg(":Browser",":Staff/Admin","Notifikasi sukses",ret=True)
    s.msg(":Staff/Admin",":Browser","Buka /maintenance → Klik Selesai pada AST-001")
    s.msg(":Browser",":MaintenanceController","PATCH /maintenance/AST-001/complete {kondisi:Baik}")
    s.msg(":MaintenanceController",":Asset Model","where('kode_aset','AST-001')->firstOrFail()")
    s.msg(":Asset Model",":Database","SELECT * FROM aset WHERE kode_aset=AST-001")
    s.msg(":Database",":Asset Model","Asset record",ret=True)
    s.msg(":MaintenanceController",":MaintenanceController","validate([kondisi required|in:Baik,...])",self_call=True)
    s.msg(":MaintenanceController",":Asset Model","update([status=>'Aktif',kondisi=>'Baik',updated_by])")
    s.msg(":Asset Model",":Database","UPDATE aset SET status=Aktif,kondisi=Baik WHERE kode_aset=AST-001")
    s.msg(":MaintenanceController",":ActivityLogger","logAsset('Update','Maintenance selesai...')")
    s.msg(":ActivityLogger",":Database","INSERT INTO log_aktivitas")
    s.msg(":MaintenanceController",":User Model","where('role','admin')->where('is_active',1)->get()")
    s.msg(":User Model",":Database","SELECT * FROM users WHERE role=admin AND is_active=1")
    s.msg(":Database",":User Model","[Admin Magang (magangrbtv@gmail.com)]",ret=True)
    s.msg(":MaintenanceController",":SMTP Server","Mail::to(admin)->send(MaintenanceAlert)")
    s.msg(":SMTP Server",":Staff/Admin","Email: Maintenance Selesai — Kamera Sony A7",ret=True)
    s.msg(":MaintenanceController",":Browser","redirect()->route('maintenance.index') + success",ret=True)
    s.msg(":Browser",":Staff/Admin","Dashboard maintenance + notifikasi sukses",ret=True)
    s.render("SEQ_04_Maintenance.png")

seq_maintenance()

# ── SEQ-05 KELOLA PENGGUNA ───────────────────────────────────────────────────
def seq_pengguna():
    s = SequenceDiagram("sd  Sequence — Kelola Pengguna (Admin) — SimAset RBTV Bengkulu", [
        ":Admin", ":Browser", ":Router",
        ":UserController", ":User Model",
        ":Database", ":AkunBaruMail", ":ActivityLogger"
    ])
    s.msg(":Admin",":Browser","Klik menu Kelola Pengguna")
    s.msg(":Browser",":Router","GET /users [middleware:role:admin]")
    s.msg(":Router",":Router","Cek role=admin → abort(403) jika bukan",self_call=True)
    s.msg(":Router",":UserController","index()")
    s.msg(":UserController",":User Model","User::orderBy('role')->get()")
    s.msg(":User Model",":Database","SELECT * FROM users ORDER BY role")
    s.msg(":Database",":User Model","[Admin Magang(admin), Staff RBTV(staff), reffki(staff)]",ret=True)
    s.msg(":UserController",":Browser","view(users.index, compact(users))",ret=True)
    s.msg(":Browser",":Admin","Daftar pengguna ditampilkan",ret=True)
    s.msg(":Admin",":Browser","Klik + Tambah Pengguna → Isi form → Submit")
    s.msg(":Browser",":UserController","POST /users {name,email,password,role,kirim_email}")
    s.msg(":UserController",":UserController","validate([email unique, password regex])",self_call=True)
    s.msg(":UserController",":User Model","User::create([...,password=>Hash::make(pwd),is_active:true])")
    s.msg(":User Model",":Database","INSERT INTO users (name,email,password,role,is_active,...)")
    s.msg(":Database",":User Model","User record (id=5)",ret=True)
    s.msg(":UserController",":AkunBaruMail","new AkunBaruMail(user, plainPassword) [jika dicentang]")
    s.msg(":AkunBaruMail",":Admin","Email: Akun baru dibuat (email+password awal)",ret=True)
    s.msg(":UserController",":ActivityLogger","logUser('Create','Menambahkan pengguna baru...')")
    s.msg(":ActivityLogger",":Database","INSERT INTO log_aktivitas")
    s.msg(":UserController",":Browser","redirect()->route('users.index') + success",ret=True)
    s.msg(":Browser",":Admin","Daftar pengguna + notifikasi sukses",ret=True)
    s.render("SEQ_05_Pengguna.png")

seq_pengguna()

print(f"\nSelesai! Semua diagram ada di: {OUT}/")
