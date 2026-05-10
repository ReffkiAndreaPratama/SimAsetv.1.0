import os
BASE = "docs/diagrams/drawio"
os.makedirs(BASE, exist_ok=True)

def w(fname, content):
    with open(os.path.join(BASE, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {fname}")

# ─────────────────────────────────────────────────────────────────────────────
# HELPER: wrap content in mxfile envelope
# ─────────────────────────────────────────────────────────────────────────────
def mxfile(diagram_name, cells):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2026-05-07" version="21.0.0">
  <diagram name="{diagram_name}">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1654" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
{cells}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

# ─────────────────────────────────────────────────────────────────────────────
# HELPER: entity table for ERD
# ─────────────────────────────────────────────────────────────────────────────
def erd_entity(eid, label, x, y, w, rows, color="#dae8fc", stroke="#6c8ebf"):
    h = 30 + len(rows)*30
    cells = f'        <mxCell id="{eid}" value="{label}" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;fillColor={color};strokeColor={stroke};" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'
    for i, (tag, col) in enumerate(rows):
        rid = f"{eid}r{i}"
        bottom = "1" if i == 0 else "0"
        cells += f'        <mxCell id="{rid}" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontSize=11;top=0;left=0;right=0;bottom={bottom};" vertex="1" parent="{eid}"><mxGeometry y="{30+i*30}" width="{w}" height="30" as="geometry"/></mxCell>\n'
        cells += f'        <mxCell id="{rid}a" value="{tag}" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;fontSize=10;" vertex="1" parent="{rid}"><mxGeometry width="50" height="30" as="geometry"><mxRectangle width="50" height="30" as="alternateBounds"/></mxGeometry></mxCell>\n'
        cells += f'        <mxCell id="{rid}b" value="{col}" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;overflow=hidden;fontSize=11;" vertex="1" parent="{rid}"><mxGeometry x="50" width="{w-50}" height="30" as="geometry"><mxRectangle width="{w-50}" height="30" as="alternateBounds"/></mxGeometry></mxCell>\n'
    return cells, h

def erd_rel(eid, src, tgt, label, src_end="ERmany", tgt_end="ERone"):
    return f'        <mxCell id="{eid}" value="{label}" style="edgeStyle=entityRelationEdgeStyle;endArrow={tgt_end};startArrow={src_end};exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontSize=11;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

# ─────────────────────────────────────────────────────────────────────────────
# 01 ERD
# ─────────────────────────────────────────────────────────────────────────────
print("01_ERD.drawio")
cells = ""

# users
c, _ = erd_entity("users", "users", 40, 40, 300, [
    ("PK", "id : INT AUTO_INCREMENT"),
    ("",   "name : VARCHAR(100) NOT NULL"),
    ("UQ", "email : VARCHAR(100) NOT NULL"),
    ("",   "password : VARCHAR(255) NOT NULL"),
    ("",   "role : ENUM(admin, staff)"),
    ("",   "is_active : TINYINT(1) DEFAULT 1"),
    ("",   "last_login_at : TIMESTAMP NULL"),
    ("",   "created_at : TIMESTAMP"),
    ("",   "updated_at : TIMESTAMP NULL"),
], "#dae8fc", "#6c8ebf")
cells += c

# barang
c, _ = erd_entity("barang", "barang", 40, 420, 320, [
    ("PK", "kode_barang : VARCHAR(20) [BRG-001]"),
    ("",   "nama_barang : VARCHAR(150) NOT NULL"),
    ("",   "kategori : ENUM(Kamera,Audio,Komputer,...)"),
    ("",   "status : ENUM(aktif, nonaktif)"),
    ("",   "keterangan : TEXT NULL"),
    ("",   "created_at : TIMESTAMP"),
    ("",   "updated_at : TIMESTAMP NULL"),
    ("",   "deleted_at : TIMESTAMP NULL [SoftDelete]"),
], "#d5e8d4", "#82b366")
cells += c

# ruangan
c, _ = erd_entity("ruangan", "ruangan", 700, 40, 280, [
    ("PK", "id : INT AUTO_INCREMENT"),
    ("",   "nama : VARCHAR(100) NOT NULL"),
    ("",   "lantai : VARCHAR(50) NULL"),
    ("",   "keterangan : TEXT NULL"),
    ("",   "created_at : TIMESTAMP"),
], "#fff2cc", "#d6b656")
cells += c

# aset
c, _ = erd_entity("aset", "aset", 700, 300, 340, [
    ("PK", "kode_aset : VARCHAR(20) [AST-001]"),
    ("FK", "kode_barang : VARCHAR(20) NOT NULL"),
    ("FK", "ruangan_id : INT NULL"),
    ("",   "kondisi : ENUM(Baik,Rusak Ringan,Rusak Berat)"),
    ("",   "status : ENUM(Aktif,Maintenance,Non-Aktif)"),
    ("",   "serial_number : VARCHAR(100) NULL"),
    ("",   "foto : VARCHAR(255) NULL"),
    ("",   "jumlah : INT DEFAULT 1"),
    ("",   "tanggal_perolehan : DATE NULL"),
    ("",   "harga_perolehan : DECIMAL(15,2) NULL"),
    ("",   "sumber_perolehan : VARCHAR(255) NULL"),
    ("",   "keterangan : TEXT NULL"),
    ("",   "created_by : INT NULL [ref users]"),
    ("",   "updated_by : INT NULL [ref users]"),
    ("",   "created_at : TIMESTAMP"),
    ("",   "updated_at : TIMESTAMP NULL"),
    ("",   "deleted_at : TIMESTAMP NULL [SoftDelete]"),
], "#f8cecc", "#b85450")
cells += c

# log_aktivitas
c, _ = erd_entity("log_akt", "log_aktivitas", 1200, 40, 300, [
    ("PK", "id : BIGINT UNSIGNED AUTO_INCREMENT"),
    ("",   "user_id : BIGINT UNSIGNED NULL [ref users]"),
    ("",   "aktivitas : VARCHAR(255) NOT NULL"),
    ("",   "keterangan : TEXT NULL"),
    ("",   "ip_address : VARCHAR(45) NULL"),
    ("",   "user_agent : TEXT NULL"),
    ("",   "created_at : TIMESTAMP NULL"),
    ("",   "updated_at : TIMESTAMP NULL"),
], "#e1d5e7", "#9673a6")
cells += c

# sessions
c, _ = erd_entity("sessions", "sessions", 1200, 380, 280, [
    ("PK", "id : VARCHAR(255)"),
    ("",   "user_id : BIGINT UNSIGNED NULL"),
    ("",   "ip_address : VARCHAR(45) NULL"),
    ("",   "user_agent : TEXT NULL"),
    ("",   "payload : LONGTEXT NOT NULL"),
    ("",   "last_activity : INT NOT NULL"),
], "#f5f5f5", "#666666")
cells += c

# password_reset_tokens
c, _ = erd_entity("pwd_reset", "password_reset_tokens", 1200, 620, 280, [
    ("PK", "email : VARCHAR(255)"),
    ("",   "token : VARCHAR(255) NOT NULL"),
    ("",   "created_at : TIMESTAMP NULL"),
], "#f5f5f5", "#666666")
cells += c

# Relations
# barang 1 -- N aset (FK RESTRICT)
cells += '        <mxCell id="rel1" value="1" style="edgeStyle=entityRelationEdgeStyle;endArrow=ERmanyToOne;startArrow=ERmandOne;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.3;entryDx=0;entryDy=0;fontSize=12;fontStyle=1;" edge="1" parent="1" source="barang" target="aset"><mxGeometry relative="1" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="rel1lbl" value="memiliki&#xa;(RESTRICT del, CASCADE upd)" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;" vertex="1" connectable="0" parent="rel1"><mxGeometry x="-0.1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry></mxCell>\n'

# ruangan 1 -- N aset (FK SET NULL)
cells += '        <mxCell id="rel2" value="1" style="edgeStyle=entityRelationEdgeStyle;endArrow=ERmanyToOne;startArrow=ERmandOne;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.1;entryDx=0;entryDy=0;fontSize=12;fontStyle=1;" edge="1" parent="1" source="ruangan" target="aset"><mxGeometry relative="1" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="rel2lbl" value="menampung&#xa;(SET NULL del, CASCADE upd)" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;" vertex="1" connectable="0" parent="rel2"><mxGeometry x="-0.1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry></mxCell>\n'

# users 1 -- N aset (created_by, no FK)
cells += '        <mxCell id="rel3" value="membuat (created_by)&#xa;[no FK constraint]" style="edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;startArrow=none;exitX=1;exitY=0.3;exitDx=0;exitDy=0;entryX=0;entryY=0.85;entryDx=0;entryDy=0;fontSize=10;" edge="1" parent="1" source="users" target="aset"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

# users 1 -- N log_aktivitas (no FK)
cells += '        <mxCell id="rel4" value="mencatat (user_id)&#xa;[no FK constraint]" style="edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;startArrow=none;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontSize=10;" edge="1" parent="1" source="users" target="log_akt"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

# users 1 -- N sessions
cells += '        <mxCell id="rel5" value="memiliki sesi" style="edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;startArrow=none;exitX=1;exitY=0.7;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontSize=10;" edge="1" parent="1" source="users" target="sessions"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

# users 1 -- N pwd_reset
cells += '        <mxCell id="rel6" value="reset password" style="edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;startArrow=none;exitX=1;exitY=0.9;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontSize=10;" edge="1" parent="1" source="users" target="pwd_reset"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

# FK legend note
cells += '        <mxCell id="note1" value="&lt;b&gt;FK Constraints Aktual:&lt;/b&gt;&lt;br&gt;fk_aset_barang: ON DELETE RESTRICT ON UPDATE CASCADE&lt;br&gt;fk_aset_ruangan: ON DELETE SET NULL ON UPDATE CASCADE&lt;br&gt;&lt;br&gt;Garis putus-putus = referensi logis (tidak ada FK di DB)" style="text;html=1;strokeColor=#d6b656;fillColor=#fffacd;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;fontSize=11;whiteSpace=wrap;" vertex="1" parent="1"><mxGeometry x="40" y="700" width="500" height="80" as="geometry"/></mxCell>\n'

w("01_ERD.drawio", mxfile("ERD - SimAset RBTV Bengkulu", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 02 USE CASE DIAGRAM
# ─────────────────────────────────────────────────────────────────────────────
print("02_UseCase.drawio")

def actor(eid, label, x, y):
    return f'''        <mxCell id="{eid}" value="{label}" style="shape=mxgraph.flowchart.actor;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="50" height="80" as="geometry"/></mxCell>\n'''

def usecase(eid, label, x, y, w=160, h=40):
    return f'        <mxCell id="{eid}" value="{label}" style="ellipse;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def uc_arrow(eid, src, tgt, label="", dashed=False, style_extra=""):
    dash = "dashed=1;" if dashed else ""
    return f'        <mxCell id="{eid}" value="{label}" style="edgeStyle=orthogonalEdgeStyle;{dash}endArrow=open;startArrow=none;fontSize=10;{style_extra}" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

def uc_include(eid, src, tgt):
    return f'        <mxCell id="{eid}" value="&lt;&lt;include&gt;&gt;" style="edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;startArrow=none;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

def uc_extend(eid, src, tgt):
    return f'        <mxCell id="{eid}" value="&lt;&lt;extend&gt;&gt;" style="edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;startArrow=none;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

def boundary(eid, label, x, y, w, h):
    return f'        <mxCell id="{eid}" value="{label}" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];shape=mxgraph.flowchart.start_2;fillColor=none;strokeColor=#1a3470;fontStyle=1;fontSize=13;verticalAlign=top;strokeWidth=2;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

cells = ""

# System boundary
cells += '        <mxCell id="sys" value="Sistem Informasi Manajemen Aset (SimAset) — RBTV Bengkulu" style="swimlane;startSize=30;fillColor=none;strokeColor=#1a3470;fontStyle=1;fontSize=13;verticalAlign=top;strokeWidth=2;" vertex="1" parent="1"><mxGeometry x="150" y="20" width="1300" height="1100" as="geometry"/></mxCell>\n'

# Actors
cells += actor("admin", "Admin", 20, 200)
cells += actor("staff", "Staff", 20, 700)

# ── Autentikasi group
cells += '        <mxCell id="grp_auth" value="Autentikasi" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="20" y="40" width="280" height="220" as="geometry"/></mxCell>\n'
cells += usecase("uc_login",    "Login",                    30,  50, 220, 40)
cells += usecase("uc_logout",   "Logout",                   30,  100, 220, 40)
cells += usecase("uc_forgot",   "Lupa Password",            30,  150, 220, 40)
cells += usecase("uc_reset",    "Reset Password (via Token)",30, 200, 220, 40)

# ── Dashboard
cells += '        <mxCell id="grp_dash" value="Dashboard" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="320" y="40" width="240" height="100" as="geometry"/></mxCell>\n'
cells += usecase("uc_dash",     "Lihat Dashboard\n(Statistik &amp; Grafik)", 30, 40, 180, 50)

# ── Manajemen Aset
cells += '        <mxCell id="grp_aset" value="Manajemen Aset" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="580" y="40" width="240" height="340" as="geometry"/></mxCell>\n'
cells += usecase("uc_aset_list",   "Lihat Daftar Aset\n(+ Filter &amp; Cari)", 30, 40, 180, 50)
cells += usecase("uc_aset_add",    "Tambah Aset Baru",    30,  100, 180, 40)
cells += usecase("uc_aset_edit",   "Edit Data Aset",      30,  150, 180, 40)
cells += usecase("uc_aset_detail", "Lihat Detail Aset",   30,  200, 180, 40)
cells += usecase("uc_aset_del",    "Hapus Aset (Soft Delete)", 30, 250, 180, 40)
cells += usecase("uc_aset_batch",  "Hapus Massal (Batch)", 30, 300, 180, 40)

# ── Manajemen Barang
cells += '        <mxCell id="grp_brg" value="Manajemen Barang (Master)" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="840" y="40" width="220" height="260" as="geometry"/></mxCell>\n'
cells += usecase("uc_brg_list",  "Lihat Daftar Barang",  20, 40, 180, 40)
cells += usecase("uc_brg_add",   "Tambah Barang",        20, 90, 180, 40)
cells += usecase("uc_brg_edit",  "Edit Barang",          20, 140, 180, 40)
cells += usecase("uc_brg_del",   "Hapus Barang",         20, 190, 180, 40)
cells += usecase("uc_brg_show",  "Lihat Detail Barang",  20, 240, 180, 40)

# ── Manajemen Ruangan
cells += '        <mxCell id="grp_rng" value="Manajemen Ruangan (Master)" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="1080" y="40" width="200" height="220" as="geometry"/></mxCell>\n'
cells += usecase("uc_rng_list",  "Lihat Daftar Ruangan", 10, 40, 180, 40)
cells += usecase("uc_rng_add",   "Tambah Ruangan",       10, 90, 180, 40)
cells += usecase("uc_rng_edit",  "Edit Ruangan",         10, 140, 180, 40)
cells += usecase("uc_rng_del",   "Hapus Ruangan\n(validasi: tidak ada aset)", 10, 190, 180, 50)

# ── QR Code
cells += '        <mxCell id="grp_qr" value="QR Code" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="20" y="280" width="240" height="260" as="geometry"/></mxCell>\n'
cells += usecase("uc_qr_gen",    "Generate QR Code",     20, 40, 200, 40)
cells += usecase("uc_qr_view",   "Lihat QR Code",        20, 90, 200, 40)
cells += usecase("uc_qr_dl",     "Download QR Code (PNG)",20,140, 200, 40)
cells += usecase("uc_qr_batch",  "Cetak QR Massal",      20, 190, 200, 40)
cells += usecase("uc_qr_scan",   "Scan QR Code\n(via Kamera Browser)", 20, 240, 200, 50)

# ── Maintenance
cells += '        <mxCell id="grp_maint" value="Maintenance" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="280" y="280" width="240" height="180" as="geometry"/></mxCell>\n'
cells += usecase("uc_maint_list", "Lihat Dashboard\nMaintenance",  20, 40, 200, 50)
cells += usecase("uc_maint_set",  "Set Aset ke Maintenance",       20, 100, 200, 40)
cells += usecase("uc_maint_done", "Selesaikan Maintenance",        20, 150, 200, 40)

# ── Import
cells += '        <mxCell id="grp_imp" value="Import Data" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="540" y="400" width="240" height="180" as="geometry"/></mxCell>\n'
cells += usecase("uc_imp_aset",  "Import Aset (Excel/CSV)",  20, 40, 200, 40)
cells += usecase("uc_imp_brg",   "Import Barang (Excel/CSV)",20, 90, 200, 40)
cells += usecase("uc_imp_tmpl",  "Download Template Import", 20, 140, 200, 40)

# ── Export & Laporan
cells += '        <mxCell id="grp_exp" value="Export &amp; Laporan" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="800" y="320" width="240" height="280" as="geometry"/></mxCell>\n'
cells += usecase("uc_exp_axls",  "Export Aset ke Excel",     20, 40, 200, 40)
cells += usecase("uc_exp_apdf",  "Export Aset ke PDF",       20, 90, 200, 40)
cells += usecase("uc_exp_bxls",  "Export Barang ke Excel",   20, 140, 200, 40)
cells += usecase("uc_exp_bpdf",  "Export Barang ke PDF",     20, 190, 200, 40)
cells += usecase("uc_lap_rng",   "Laporan Per Ruangan (PDF)",20, 240, 200, 40)
cells += usecase("uc_lap_maint", "Laporan Maintenance\n(PDF/CSV)", 20, 290, 200, 50)

# ── Admin Only
cells += '        <mxCell id="grp_adm" value="Administrasi (Admin Only)" style="swimlane;startSize=25;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="1060" y="280" width="220" height="320" as="geometry"/></mxCell>\n'
cells += usecase("uc_usr_list",  "Lihat Daftar Pengguna",    10, 40, 200, 40)
cells += usecase("uc_usr_add",   "Tambah Pengguna Baru",     10, 90, 200, 40)
cells += usecase("uc_usr_edit",  "Edit Data Pengguna",       10, 140, 200, 40)
cells += usecase("uc_usr_del",   "Hapus Pengguna",           10, 190, 200, 40)
cells += usecase("uc_audit",     "Lihat Audit Log",          10, 240, 200, 40)
cells += usecase("uc_audit_flt", "Filter Audit Log",         10, 290, 200, 40)

# ── Profil
cells += '        <mxCell id="grp_prof" value="Profil" style="swimlane;startSize=25;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;fontSize=11;" vertex="1" parent="sys"><mxGeometry x="20" y="560" width="240" height="140" as="geometry"/></mxCell>\n'
cells += usecase("uc_prof_edit", "Edit Profil",              20, 40, 200, 40)
cells += usecase("uc_prof_pwd",  "Ganti Password",           20, 90, 200, 40)
cells += usecase("uc_prof_del",  "Hapus Akun Sendiri",       20, 140, 200, 40)

# ── Arrows: Admin → all
for uc in ["uc_login","uc_logout","uc_forgot","uc_reset","uc_dash",
           "uc_aset_list","uc_aset_add","uc_aset_edit","uc_aset_detail","uc_aset_del","uc_aset_batch",
           "uc_brg_list","uc_brg_add","uc_brg_edit","uc_brg_del","uc_brg_show",
           "uc_rng_list","uc_rng_add","uc_rng_edit","uc_rng_del",
           "uc_qr_gen","uc_qr_view","uc_qr_dl","uc_qr_batch","uc_qr_scan",
           "uc_maint_list","uc_maint_set","uc_maint_done",
           "uc_imp_aset","uc_imp_brg","uc_imp_tmpl",
           "uc_exp_axls","uc_exp_apdf","uc_exp_bxls","uc_exp_bpdf","uc_lap_rng","uc_lap_maint",
           "uc_usr_list","uc_usr_add","uc_usr_edit","uc_usr_del","uc_audit","uc_audit_flt",
           "uc_prof_edit","uc_prof_pwd","uc_prof_del"]:
    cells += f'        <mxCell id="adm_{uc}" value="" style="edgeStyle=orthogonalEdgeStyle;endArrow=open;startArrow=none;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="admin" target="{uc}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

# Staff → all except admin-only
for uc in ["uc_login","uc_logout","uc_forgot","uc_reset","uc_dash",
           "uc_aset_list","uc_aset_add","uc_aset_edit","uc_aset_detail","uc_aset_del","uc_aset_batch",
           "uc_brg_list","uc_brg_add","uc_brg_edit","uc_brg_del","uc_brg_show",
           "uc_rng_list","uc_rng_add","uc_rng_edit","uc_rng_del",
           "uc_qr_gen","uc_qr_view","uc_qr_dl","uc_qr_batch","uc_qr_scan",
           "uc_maint_list","uc_maint_set","uc_maint_done",
           "uc_imp_aset","uc_imp_brg","uc_imp_tmpl",
           "uc_exp_axls","uc_exp_apdf","uc_exp_bxls","uc_exp_bpdf","uc_lap_rng","uc_lap_maint",
           "uc_prof_edit","uc_prof_pwd","uc_prof_del"]:
    cells += f'        <mxCell id="stf_{uc}" value="" style="edgeStyle=orthogonalEdgeStyle;endArrow=open;startArrow=none;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="staff" target="{uc}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

# include/extend
cells += uc_include("inc1", "uc_login",     "uc_login")   # placeholder — login includes log
cells += uc_extend("ext1",  "uc_reset",     "uc_forgot")
cells += uc_extend("ext2",  "uc_aset_batch","uc_aset_list")
cells += uc_extend("ext3",  "uc_qr_batch",  "uc_aset_list")
cells += uc_include("inc2", "uc_qr_scan",   "uc_aset_detail")
cells += uc_include("inc3", "uc_maint_done","uc_maint_done")  # placeholder
cells += uc_extend("ext4",  "uc_audit_flt", "uc_audit")

w("02_UseCase.drawio", mxfile("Use Case Diagram - SimAset RBTV", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# ACTIVITY DIAGRAM HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def act_start(eid, x, y):
    return f'        <mxCell id="{eid}" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="30" height="30" as="geometry"/></mxCell>\n'

def act_end(eid, x, y):
    return f'        <mxCell id="{eid}" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="30" height="30" as="geometry"/></mxCell>\n'

def act_action(eid, label, x, y, w=200, h=40):
    return f'        <mxCell id="{eid}" value="{label}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def act_decision(eid, label, x, y, w=120, h=60):
    return f'        <mxCell id="{eid}" value="{label}" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def act_fork(eid, x, y, w=200, h=8, horiz=True):
    return f'        <mxCell id="{eid}" value="" style="shape=mxgraph.flowchart.start_2;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def act_arrow(eid, src, tgt, label="", ex=0.5, ey=1, nx=0.5, ny=0):
    return f'        <mxCell id="{eid}" value="{label}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

def act_swimlane(eid, label, x, y, w, h, color="#dae8fc"):
    return f'        <mxCell id="{eid}" value="{label}" style="swimlane;startSize=30;fillColor={color};strokeColor=#6c8ebf;fontStyle=1;fontSize=12;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def act_note(eid, label, x, y, w=200, h=50):
    return f'        <mxCell id="{eid}" value="{label}" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;fontSize=10;fillColor=#fffacd;strokeColor=#d6b656;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

# ─────────────────────────────────────────────────────────────────────────────
# 03 ACTIVITY: LOGIN
# ─────────────────────────────────────────────────────────────────────────────
print("03_Activity_Login.drawio")
cells = ""

# Swimlanes
cells += '        <mxCell id="sw_root" value="Activity Diagram — Login &amp; Logout" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;swimlaneHead=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="900" height="1200" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_user" value="Pengguna" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="300" height="1200" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_sys"  value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="300" y="0" width="600" height="1200" as="geometry"/></mxCell>\n'

# Start
cells += '        <mxCell id="ls" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_user"><mxGeometry x="135" y="40" width="30" height="30" as="geometry"/></mxCell>\n'
# User actions
cells += '        <mxCell id="la1" value="Buka halaman /login" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_user"><mxGeometry x="50" y="100" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="la2" value="Input Email dan Password" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_user"><mxGeometry x="50" y="180" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="la3" value="Klik tombol &quot;Masuk&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_user"><mxGeometry x="50" y="260" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="la4" value="Melihat Dashboard" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_user"><mxGeometry x="50" y="900" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="la5" value="Klik tombol &quot;Logout&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_user"><mxGeometry x="50" y="980" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="le" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_user"><mxGeometry x="135" y="1140" width="30" height="30" as="geometry"/></mxCell>\n'

# System actions
cells += '        <mxCell id="ls1" value="Validasi input (email, password required)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="100" width="500" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ld1" value="Input valid?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="200" y="170" width="160" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls2" value="Tampilkan error validasi" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="420" y="180" width="180" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls3" value="Cek rate limit (5x/menit per email+IP)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="260" width="500" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ld2" value="Rate limit?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="200" y="330" width="160" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls4" value="Tampilkan: &quot;Terlalu banyak percobaan&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="420" y="340" width="180" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls5" value="Cari user by email di tabel users" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="420" width="500" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ld3" value="User ada?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="200" y="490" width="160" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls6" value="Error: &quot;User tidak ditemukan&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="420" y="500" width="180" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ld4" value="is_active = 1?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="200" y="580" width="160" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls7" value="Error: &quot;Akun belum aktif&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="420" y="590" width="180" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls8" value="Auth::attempt(email, password)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="670" width="500" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ld5" value="Password benar?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="200" y="740" width="160" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls9" value="Error: &quot;Kredensial tidak cocok&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="420" y="750" width="180" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls10" value="session()-&gt;regenerate() | Update last_login_at" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="830" width="500" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls11" value="ActivityLogger::logAuth(&#39;Login&#39;, ...) → INSERT log_aktivitas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="890" width="500" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls12" value="redirect()-&gt;route(&#39;dashboard&#39;)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="950" width="500" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls13" value="ActivityLogger::logAuth(&#39;Logout&#39;) | Auth::logout() | session()-&gt;invalidate()" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="1040" width="500" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ls14" value="redirect(&#39;/&#39;) → halaman Login" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_sys"><mxGeometry x="50" y="1110" width="500" height="40" as="geometry"/></mxCell>\n'

# Arrows (within swimlanes use parent references)
for src, tgt, lbl in [
    ("ls","la1",""), ("la1","la2",""), ("la2","la3",""), ("la3","ls1",""),
    ("ls1","ld1",""), ("ld1","ls3","Ya"), ("ld1","ls2","Tidak"),
    ("ls2","la2",""), ("ls3","ld2",""), ("ld2","ls5","Tidak"),
    ("ld2","ls4","Ya"), ("ls4","la2",""), ("ls5","ld3",""),
    ("ld3","ld4","Ya"), ("ld3","ls6","Tidak"), ("ls6","la2",""),
    ("ld4","ls8","Ya"), ("ld4","ls7","Tidak"), ("ls7","la2",""),
    ("ls8","ld5",""), ("ld5","ls10","Ya"), ("ld5","ls9","Tidak"),
    ("ls9","la2",""), ("ls10","ls11",""), ("ls11","ls12",""),
    ("ls12","la4",""), ("la4","la5",""), ("la5","ls13",""),
    ("ls13","ls14",""), ("ls14","le",""),
]:
    cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

w("03_Activity_Login.drawio", mxfile("Activity Diagram - Login", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# SEQUENCE DIAGRAM HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def seq_lifeline(eid, label, x, y=20, w=120, h=60, color="#dae8fc", stroke="#6c8ebf"):
    return f'        <mxCell id="{eid}" value="{label}" style="shape=mxgraph.uml.lifeline;whiteSpace=wrap;html=1;fillColor={color};strokeColor={stroke};fontStyle=1;fontSize=11;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def seq_actor(eid, label, x, y=20):
    return f'        <mxCell id="{eid}" value="{label}" style="shape=mxgraph.flowchart.actor;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=11;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="50" height="80" as="geometry"/></mxCell>\n'

def seq_msg(eid, src, tgt, label, y, dashed=False, ret=False):
    arrow = "open" if not ret else "open"
    dash = "dashed=1;" if dashed or ret else ""
    return f'        <mxCell id="{eid}" value="{label}" style="edgeStyle=orthogonalEdgeStyle;{dash}endArrow={arrow};startArrow=none;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;fontSize=10;align=center;verticalAlign=bottom;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry y="{y}" relative="1" as="geometry"/></mxCell>\n'

def seq_box(eid, label, x, y, w, h, color="#e3f2fd"):
    return f'        <mxCell id="{eid}" value="{label}" style="swimlane;startSize=20;fillColor={color};strokeColor=#1a3470;fontSize=10;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def seq_note(eid, label, x, y, w=180, h=50):
    return f'        <mxCell id="{eid}" value="{label}" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;fontSize=10;fillColor=#fffacd;strokeColor=#d6b656;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

# ─────────────────────────────────────────────────────────────────────────────
# 04 ACTIVITY: MANAJEMEN ASET (CRUD + QR)
# ─────────────────────────────────────────────────────────────────────────────
print("04_Activity_Aset.drawio")
cells = ""

# Swimlanes container
cells += '        <mxCell id="sw_root" value="Activity Diagram — Manajemen Aset (CRUD + QR Code)" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="1100" height="1400" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_u" value="Pengguna" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="350" height="1400" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_s" value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="350" y="0" width="750" height="1400" as="geometry"/></mxCell>\n'

# Start
cells += '        <mxCell id="as" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_u"><mxGeometry x="160" y="30" width="30" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="a1" value="Login ke sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="75" y="90" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="a2" value="Pilih menu &quot;Aset&quot; dari sidebar" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="75" y="160" width="200" height="40" as="geometry"/></mxCell>\n'

# System loads list
cells += '        <mxCell id="as1" value="Query aset dengan relasi barang &amp; ruangan&#xa;Asset::with([&#39;barang&#39;,&#39;ruangan&#39;])-&gt;paginate(15)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="160" width="650" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as2" value="Tampilkan halaman daftar aset&#xa;(tabel + 4 stats card + filter bar)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="230" width="650" height="50" as="geometry"/></mxCell>\n'

# Decision: pilih aksi
cells += '        <mxCell id="ad1" value="Pilih aksi?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="115" y="240" width="120" height="60" as="geometry"/></mxCell>\n'

# ── TAMBAH
cells += '        <mxCell id="a3" value="Klik &quot;+ Tambah Aset&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="75" y="340" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as3" value="Load dropdown Barang aktif + Ruangan&#xa;Tampilkan form tambah aset (4 section card)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="340" width="650" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="a4" value="Isi form: Barang*, Ruangan*, Kondisi*,&#xa;Status*, Tgl Perolehan*, Serial, Jumlah,&#xa;Harga, Sumber, Keterangan, Foto" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="75" y="420" width="200" height="70" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="a5" value="Klik &quot;Simpan Aset&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="75" y="520" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as4" value="Validasi server-side (required, exists, unique, dll)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="520" width="650" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ad2" value="Validasi&#xa;gagal?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="270" y="590" width="110" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as5" value="Redirect back + error per field" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="450" y="600" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as6" value="Asset::generateKode() — gap-filling&#xa;(cari nomor terkecil yang belum dipakai)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="680" width="650" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ad3" value="Ada foto?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="270" y="760" width="110" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as7" value="Simpan foto ke public/foto_aset/" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="450" y="770" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as8" value="Asset::create($data) [created_by = auth()-&gt;id()]" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="850" width="650" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as9" value="ActivityLogger::logAsset(&#39;Create&#39;, ...) → INSERT log_aktivitas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="910" width="650" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as10" value="Redirect ke /aset + flash success" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="970" width="650" height="40" as="geometry"/></mxCell>\n'

# ── EDIT (abbreviated)
cells += '        <mxCell id="a6" value="Klik Edit (✏) pada aset" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="75" y="1040" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as11" value="Load aset + dropdown → Tampilkan form edit → Validasi → $asset-&gt;update() → Log → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="1040" width="650" height="50" as="geometry"/></mxCell>\n'

# ── HAPUS
cells += '        <mxCell id="a7" value="Klik Hapus (🗑) → Konfirmasi SweetAlert2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="75" y="1120" width="200" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as12" value="$asset-&gt;delete() [Soft Delete: isi deleted_at] → Log → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="1120" width="650" height="50" as="geometry"/></mxCell>\n'

# ── QR CODE
cells += '        <mxCell id="a8" value="Klik &quot;Generate QR Code&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="75" y="1200" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="as13" value="Cek file QR ada? → Request API qrserver.com → Simpan PNG → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="50" y="1200" width="650" height="50" as="geometry"/></mxCell>\n'

# End
cells += '        <mxCell id="ae" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_u"><mxGeometry x="160" y="1330" width="30" height="30" as="geometry"/></mxCell>\n'

# Arrows
for src, tgt, lbl in [
    ("as","a1",""), ("a1","a2",""), ("a2","as1",""), ("as1","as2",""),
    ("as2","ad1",""), ("ad1","a3","Tambah"), ("a3","as3",""), ("as3","a4",""),
    ("a4","a5",""), ("a5","as4",""), ("as4","ad2",""), ("ad2","as6","Tidak"),
    ("ad2","as5","Ya"), ("as5","a4",""), ("as6","ad3",""), ("ad3","as8","Tidak"),
    ("ad3","as7","Ya"), ("as7","as8",""), ("as8","as9",""), ("as9","as10",""),
    ("as10","ae",""), ("ad1","a6","Edit"), ("a6","as11",""), ("as11","ae",""),
    ("ad1","a7","Hapus"), ("a7","as12",""), ("as12","ae",""),
    ("ad1","a8","QR"), ("a8","as13",""), ("as13","ae",""),
]:
    cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

w("04_Activity_Aset.drawio", mxfile("Activity Diagram - Manajemen Aset", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# GENERIC CRUD ACTIVITY HELPER
# ─────────────────────────────────────────────────────────────────────────────
def crud_activity(fname, title, entity, fields_add, fields_edit, extra_note=""):
    cells = ""
    cells += f'        <mxCell id="sw_root" value="{title}" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="1000" height="1100" as="geometry"/></mxCell>\n'
    cells += '        <mxCell id="sw_u" value="Pengguna" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="320" height="1100" as="geometry"/></mxCell>\n'
    cells += '        <mxCell id="sw_s" value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="320" y="0" width="680" height="1100" as="geometry"/></mxCell>\n'

    cells += '        <mxCell id="cs" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_u"><mxGeometry x="145" y="30" width="30" height="30" as="geometry"/></mxCell>\n'
    cells += f'        <mxCell id="c1" value="Login ke sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="90" width="200" height="40" as="geometry"/></mxCell>\n'
    cells += f'        <mxCell id="c2" value="Pilih menu &quot;{entity}&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="160" width="200" height="40" as="geometry"/></mxCell>\n'
    cells += f'        <mxCell id="cs1" value="Query {entity} dari database → Tampilkan daftar (tabel + filter)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="160" width="600" height="50" as="geometry"/></mxCell>\n'
    cells += '        <mxCell id="cd1" value="Pilih aksi?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="100" y="240" width="120" height="60" as="geometry"/></mxCell>\n'

    # TAMBAH
    cells += f'        <mxCell id="c3" value="Klik &quot;+ Tambah {entity}&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="340" width="200" height="40" as="geometry"/></mxCell>\n'
    cells += f'        <mxCell id="cs2" value="Tampilkan form tambah {entity}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="340" width="600" height="40" as="geometry"/></mxCell>\n'
    cells += f'        <mxCell id="c4" value="Isi form: {fields_add}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="410" width="200" height="60" as="geometry"/></mxCell>\n'
    cells += '        <mxCell id="c5" value="Klik &quot;Simpan&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="500" width="200" height="40" as="geometry"/></mxCell>\n'
    cells += '        <mxCell id="cs3" value="Validasi server-side" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="500" width="600" height="40" as="geometry"/></mxCell>\n'
    cells += '        <mxCell id="cd2" value="Validasi&#xa;gagal?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="250" y="570" width="110" height="60" as="geometry"/></mxCell>\n'
    cells += '        <mxCell id="cs4" value="Redirect back + error per field" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="430" y="580" width="200" height="40" as="geometry"/></mxCell>\n'
    cells += f'        <mxCell id="cs5" value="{entity}::create($data) → ActivityLogger::log(&#39;Create&#39;) → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="660" width="600" height="50" as="geometry"/></mxCell>\n'

    # EDIT
    cells += '        <mxCell id="c6" value="Klik Edit (✏) pada baris data" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="740" width="200" height="40" as="geometry"/></mxCell>\n'
    cells += f'        <mxCell id="cs6" value="Load data → Tampilkan form edit → Validasi → update() → Log → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="740" width="600" height="50" as="geometry"/></mxCell>\n'

    # HAPUS
    cells += '        <mxCell id="c7" value="Klik Hapus (🗑) → Konfirmasi" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="820" width="200" height="40" as="geometry"/></mxCell>\n'
    cells += f'        <mxCell id="cs7" value="delete() [Soft Delete] → ActivityLogger::log(&#39;Delete&#39;) → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="820" width="600" height="50" as="geometry"/></mxCell>\n'

    if extra_note:
        cells += f'        <mxCell id="cnote" value="{extra_note}" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;fontSize=10;fillColor=#fffacd;strokeColor=#d6b656;" vertex="1" parent="sw_s"><mxGeometry x="40" y="900" width="600" height="60" as="geometry"/></mxCell>\n'

    # End
    cells += '        <mxCell id="ce" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_u"><mxGeometry x="145" y="1040" width="30" height="30" as="geometry"/></mxCell>\n'

    for src, tgt, lbl in [
        ("cs","c1",""), ("c1","c2",""), ("c2","cs1",""), ("cs1","cd1",""),
        ("cd1","c3","Tambah"), ("c3","cs2",""), ("cs2","c4",""), ("c4","c5",""),
        ("c5","cs3",""), ("cs3","cd2",""), ("cd2","cs5","Tidak"), ("cd2","cs4","Ya"),
        ("cs4","c4",""), ("cs5","ce",""),
        ("cd1","c6","Edit"), ("c6","cs6",""), ("cs6","ce",""),
        ("cd1","c7","Hapus"), ("c7","cs7",""), ("cs7","ce",""),
    ]:
        cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

    w(fname, mxfile(title, cells))
    print(f"  done: {fname}")

# 05 Barang CRUD
crud_activity(
    "05_Activity_Barang.drawio",
    "Activity Diagram — Manajemen Barang (CRUD)",
    "Barang",
    "Nama Barang*, Kategori*, Status*,&#xa;Keterangan",
    "Nama Barang, Kategori, Status, Keterangan",
    "Kode Barang di-generate otomatis (gap-filling: BRG-001, BRG-002, ...)"
)

# 06 Ruangan CRUD
crud_activity(
    "06_Activity_Ruangan.drawio",
    "Activity Diagram — Manajemen Ruangan (CRUD)",
    "Ruangan",
    "Nama Ruangan*, Lantai, Keterangan",
    "Nama Ruangan, Lantai, Keterangan",
    "Validasi hapus: Ruangan tidak bisa dihapus jika masih ada aset terdaftar"
)

# ─────────────────────────────────────────────────────────────────────────────
# 07 ACTIVITY: SCANNER QR CODE
# ─────────────────────────────────────────────────────────────────────────────
print("07_Activity_ScannerQR.drawio")
cells = ""
cells += '        <mxCell id="sw_root" value="Activity Diagram — Scanner QR Code" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="900" height="900" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_u" value="Pengguna" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="300" height="900" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_s" value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="300" y="0" width="600" height="900" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="qs" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_u"><mxGeometry x="135" y="30" width="30" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="q1" value="Login ke sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="90" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="q2" value="Klik menu &quot;QR Scanner&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="160" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="qs1" value="Tampilkan halaman scanner (GET /qrcode/scanner)&#xa;Minta izin akses kamera browser" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="160" width="520" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="q3" value="Izinkan akses kamera" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="240" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="q4" value="Arahkan kamera ke QR Code aset" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="310" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="qs2" value="Decode QR Code (JavaScript QR decoder)&#xa;Hasil: URL → http://host/aset/{kode_aset}/detail" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="310" width="520" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="qs3" value="GET /aset/{kode_aset}/detail (route publik)&#xa;Asset::with([barang,ruangan,creator])-&gt;firstOrFail()" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="390" width="520" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="qd1" value="Aset&#xa;ditemukan?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="210" y="470" width="120" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="qs4" value="Tampilkan HTTP 404 — Aset tidak ditemukan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="380" y="480" width="180" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="qs5" value="Tampilkan halaman detail aset:&#xa;Kode, Nama Barang, Kategori, Ruangan,&#xa;Kondisi, Status, Serial Number, Tgl Perolehan, Foto" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="560" width="520" height="70" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="q5" value="Melihat detail aset" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="660" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="qnote" value="Route /aset/{kode}/detail adalah PUBLIK&#xa;(tidak perlu login) — siapapun yang scan QR&#xa;bisa melihat info aset" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;fontSize=10;fillColor=#fffacd;strokeColor=#d6b656;" vertex="1" parent="sw_s"><mxGeometry x="40" y="660" width="520" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="qe" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_u"><mxGeometry x="135" y="840" width="30" height="30" as="geometry"/></mxCell>\n'

for src, tgt, lbl in [
    ("qs","q1",""), ("q1","q2",""), ("q2","qs1",""), ("qs1","q3",""),
    ("q3","q4",""), ("q4","qs2",""), ("qs2","qs3",""), ("qs3","qd1",""),
    ("qd1","qs5","Ya"), ("qd1","qs4","Tidak"), ("qs4","qe",""),
    ("qs5","q5",""), ("q5","qe",""),
]:
    cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

w("07_Activity_ScannerQR.drawio", mxfile("Activity Diagram - Scanner QR Code", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 08 ACTIVITY: IMPORT DATA
# ─────────────────────────────────────────────────────────────────────────────
print("08_Activity_Import.drawio")
cells = ""
cells += '        <mxCell id="sw_root" value="Activity Diagram — Import Data (Excel/CSV)" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="900" height="1000" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_u" value="Pengguna" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="300" height="1000" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_s" value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="300" y="0" width="600" height="1000" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="is" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_u"><mxGeometry x="135" y="30" width="30" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="i1" value="Login ke sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="90" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="i2" value="Pilih menu Import" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="160" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="is1" value="Tampilkan halaman import (pilih tipe: Aset/Barang)&#xa;+ tombol Download Template" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="160" width="520" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="id1" value="Perlu&#xa;template?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="90" y="240" width="120" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="i3" value="Klik &quot;Download Template&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="330" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="is2" value="GET /import/template → Generate CSV template → Download" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="330" width="520" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="i4" value="Isi data di template Excel/CSV" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="400" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="i5" value="Pilih tipe (Aset/Barang)&#xa;Upload file Excel/CSV" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="470" width="200" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="i6" value="Klik &quot;Import&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="550" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="is3" value="POST /import {file, type}&#xa;Validasi: file required, mimes:xlsx,xls,csv; type in:aset,barang" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="550" width="520" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="id2" value="File valid?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="210" y="630" width="120" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="is4" value="Error: &quot;File harus berformat Excel atau CSV&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="380" y="640" width="180" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="is5" value="Baca setiap baris → Validasi per baris&#xa;(kode_barang exists, kondisi valid, dll)&#xa;→ Asset::create() / Barang::create()" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="720" width="520" height="70" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="is6" value="Hitung: X berhasil, Y gagal&#xa;Redirect + flash message hasil import" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="820" width="520" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="i7" value="Melihat hasil import di daftar data" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="900" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ie" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_u"><mxGeometry x="135" y="960" width="30" height="30" as="geometry"/></mxCell>\n'

for src, tgt, lbl in [
    ("is","i1",""), ("i1","i2",""), ("i2","is1",""), ("is1","id1",""),
    ("id1","i3","Ya"), ("i3","is2",""), ("is2","i4",""), ("i4","i5",""),
    ("id1","i5","Tidak"), ("i5","i6",""), ("i6","is3",""), ("is3","id2",""),
    ("id2","is5","Valid"), ("id2","is4","Tidak"), ("is4","i5",""),
    ("is5","is6",""), ("is6","i7",""), ("i7","ie",""),
]:
    cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

w("08_Activity_Import.drawio", mxfile("Activity Diagram - Import Data", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 09 ACTIVITY: EXPORT & LAPORAN
# ─────────────────────────────────────────────────────────────────────────────
print("09_Activity_Export.drawio")
cells = ""
cells += '        <mxCell id="sw_root" value="Activity Diagram — Export &amp; Laporan" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="1000" height="1100" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_u" value="Pengguna" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="300" height="1100" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_s" value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="300" y="0" width="700" height="1100" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="es" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_u"><mxGeometry x="135" y="30" width="30" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="e1" value="Login ke sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="90" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="e2" value="Pilih menu &quot;Laporan &amp; Export&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="160" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es1" value="Tampilkan halaman index laporan&#xa;(daftar ruangan + jumlah aset masing-masing)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="160" width="620" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ed1" value="Pilih jenis?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="90" y="240" width="120" height="60" as="geometry"/></mxCell>\n'

# Laporan Aset
cells += '        <mxCell id="e3" value="Klik &quot;Laporan Aset&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="340" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es2" value="Tampilkan form filter (Ruangan, Kondisi, Status, Kata Kunci)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="340" width="620" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="e4" value="Atur filter (opsional)&#xa;Klik &quot;Tampilkan&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="410" width="200" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es3" value="Query aset dengan filter → Tampilkan tabel hasil" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="410" width="620" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ed2" value="Format?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="90" y="490" width="120" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es4" value="GET /laporan/assets/cetak → Barryvdh DomPDF → Download PDF" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="490" width="620" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es5" value="GET /laporan/assets/export → Maatwebsite Excel → Download .xlsx" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="550" width="620" height="40" as="geometry"/></mxCell>\n'

# Laporan Per Ruangan
cells += '        <mxCell id="e5" value="Klik nama ruangan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="620" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es6" value="GET /laporan/ruangan/{id} → Query aset di ruangan → Generate PDF → Download" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="620" width="620" height="40" as="geometry"/></mxCell>\n'

# Laporan Maintenance
cells += '        <mxCell id="e6" value="Klik &quot;Laporan Maintenance&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="690" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ed3" value="Format?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="90" y="760" width="120" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es7" value="GET /laporan/maintenance/pdf → Query status=Maintenance → DomPDF → Download" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="760" width="620" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es8" value="GET /laporan/maintenance/csv → Generate CSV → Download" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="820" width="620" height="40" as="geometry"/></mxCell>\n'

# Export Langsung
cells += '        <mxCell id="e7" value="Klik &quot;Export&quot; dari halaman Aset/Barang" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="890" width="200" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="es9" value="GET /export/aset/excel atau /export/aset/pdf&#xa;AssetExportFile::query() → Excel::download() / Pdf::download()" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="890" width="620" height="50" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="ee" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_u"><mxGeometry x="135" y="1050" width="30" height="30" as="geometry"/></mxCell>\n'

for src, tgt, lbl in [
    ("es","e1",""), ("e1","e2",""), ("e2","es1",""), ("es1","ed1",""),
    ("ed1","e3","Laporan Aset"), ("e3","es2",""), ("es2","e4",""), ("e4","es3",""),
    ("es3","ed2",""), ("ed2","es4","PDF"), ("ed2","es5","Excel"),
    ("es4","ee",""), ("es5","ee",""),
    ("ed1","e5","Per Ruangan"), ("e5","es6",""), ("es6","ee",""),
    ("ed1","e6","Maintenance"), ("e6","ed3",""), ("ed3","es7","PDF"),
    ("ed3","es8","CSV"), ("es7","ee",""), ("es8","ee",""),
    ("ed1","e7","Export Langsung"), ("e7","es9",""), ("es9","ee",""),
]:
    cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

w("09_Activity_Export.drawio", mxfile("Activity Diagram - Export dan Laporan", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 10 ACTIVITY: KELOLA PENGGUNA (Admin Only)
# ─────────────────────────────────────────────────────────────────────────────
print("10_Activity_Pengguna.drawio")
cells = ""
cells += '        <mxCell id="sw_root" value="Activity Diagram — Kelola Pengguna (Admin Only)" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="1000" height="1100" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_u" value="Admin" style="swimlane;startSize=30;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="320" height="1100" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_s" value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="320" y="0" width="680" height="1100" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="ps" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_u"><mxGeometry x="145" y="30" width="30" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="p1" value="Login sebagai Admin" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="90" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="p2" value="Klik menu &quot;Kelola Pengguna&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="160" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ps1" value="Cek middleware role:admin&#xa;(RoleMiddleware::handle() → abort(403) jika bukan admin)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="160" width="600" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="pd0" value="Role = admin?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="250" y="240" width="120" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ps0" value="HTTP 403 Forbidden" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="430" y="250" width="180" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ps2" value="User::orderBy(&#39;role&#39;)-&gt;get()&#xa;Tampilkan daftar pengguna (Nama, Email, Role, Status, Aksi)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="330" width="600" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="pd1" value="Pilih aksi?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="100" y="420" width="120" height="60" as="geometry"/></mxCell>\n'

# TAMBAH
cells += '        <mxCell id="p3" value="Klik &quot;+ Tambah Pengguna&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="520" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ps3" value="Tampilkan form tambah pengguna" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="520" width="600" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="p4" value="Isi: Nama*, Email*, Password*&#xa;(min 8, uppercase, lowercase, angka),&#xa;Role*, Kirim Email (opsional)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="590" width="200" height="70" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ps4" value="Validasi → Hash password → User::create()&#xa;→ Kirim email (jika dicentang) → Log → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="590" width="600" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="pd2" value="Kirim&#xa;email?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="250" y="670" width="110" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ps5" value="Mail::to()-&gt;send(new AkunBaruMail(user, plainPassword))" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="420" y="680" width="200" height="40" as="geometry"/></mxCell>\n'

# EDIT
cells += '        <mxCell id="p5" value="Klik Edit pada pengguna" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="760" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ps6" value="Load user → Form edit → Validasi → update() → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="760" width="600" height="40" as="geometry"/></mxCell>\n'

# HAPUS
cells += '        <mxCell id="p6" value="Klik Hapus → Konfirmasi" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="830" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ps7" value="Cek: tidak bisa hapus akun sendiri&#xa;→ $user-&gt;delete() (hard delete) → Redirect" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="830" width="600" height="50" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="pe" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_u"><mxGeometry x="145" y="1040" width="30" height="30" as="geometry"/></mxCell>\n'

for src, tgt, lbl in [
    ("ps","p1",""), ("p1","p2",""), ("p2","ps1",""), ("ps1","pd0",""),
    ("pd0","ps2","Ya"), ("pd0","ps0","Tidak"), ("ps0","pe",""),
    ("ps2","pd1",""), ("pd1","p3","Tambah"), ("p3","ps3",""), ("ps3","p4",""),
    ("p4","ps4",""), ("ps4","pd2",""), ("pd2","ps5","Ya"), ("pd2","pe","Tidak"),
    ("ps5","pe",""), ("pd1","p5","Edit"), ("p5","ps6",""), ("ps6","pe",""),
    ("pd1","p6","Hapus"), ("p6","ps7",""), ("ps7","pe",""),
]:
    cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

w("10_Activity_Pengguna.drawio", mxfile("Activity Diagram - Kelola Pengguna", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 11 ACTIVITY: AUDIT LOG
# ─────────────────────────────────────────────────────────────────────────────
print("11_Activity_AuditLog.drawio")
cells = ""
cells += '        <mxCell id="sw_root" value="Activity Diagram — Audit Log (Activity Log)" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="900" height="800" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_u" value="Admin" style="swimlane;startSize=30;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="300" height="800" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_s" value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="300" y="0" width="600" height="800" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="als" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_u"><mxGeometry x="135" y="30" width="30" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="al1" value="Login sebagai Admin" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="90" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="al2" value="Klik menu &quot;Log Aktivitas&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="160" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="als1" value="Cek middleware role:admin → abort(403) jika bukan admin" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="160" width="520" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="als2" value="ActivityLog::with(&#39;user&#39;)-&gt;orderBy(&#39;created_at&#39;,&#39;desc&#39;)-&gt;paginate(20)&#xa;Tampilkan tabel log (id, user, aktivitas, keterangan, ip, waktu)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="230" width="520" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="al3" value="Atur filter (opsional):&#xa;- Kata kunci&#xa;- Pengguna&#xa;- Modul (Login/Create/Update/Delete)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="330" width="200" height="80" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="al4" value="Klik &quot;Filter&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="440" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="als3" value="Query dengan WHERE clause sesuai filter&#xa;(search LIKE, user_id =, aktivitas LIKE)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="440" width="520" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="als4" value="Tampilkan hasil filter (paginated 20/halaman)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="40" y="520" width="520" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="al5" value="Melihat riwayat aktivitas pengguna" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="50" y="600" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="alnote" value="Log dicatat otomatis oleh ActivityLogger::log()&#xa;setiap kali ada Login, Logout, Create, Update, Delete&#xa;Menyimpan: user_id, aktivitas, keterangan, ip_address, user_agent" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;fontSize=10;fillColor=#fffacd;strokeColor=#d6b656;" vertex="1" parent="sw_s"><mxGeometry x="40" y="590" width="520" height="70" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ale" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_u"><mxGeometry x="135" y="740" width="30" height="30" as="geometry"/></mxCell>\n'

for src, tgt, lbl in [
    ("als","al1",""), ("al1","al2",""), ("al2","als1",""), ("als1","als2",""),
    ("als2","al3",""), ("al3","al4",""), ("al4","als3",""), ("als3","als4",""),
    ("als4","al5",""), ("al5","ale",""),
]:
    cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

w("11_Activity_AuditLog.drawio", mxfile("Activity Diagram - Audit Log", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 12 ACTIVITY: MAINTENANCE
# ─────────────────────────────────────────────────────────────────────────────
print("12_Activity_Maintenance.drawio")
cells = ""
cells += '        <mxCell id="sw_root" value="Activity Diagram — Maintenance Aset" style="shape=pool;startSize=30;horizontal=1;childLayout=stackLayout;horizontalStack=1;resizeParent=1;resizeParentMax=0;collapsible=0;marginBottom=0;fillColor=#1a3470;fontColor=#ffffff;strokeColor=#1a3470;fontStyle=1;fontSize=13;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="1100" height="1100" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_u" value="Staff / Admin" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="0" y="0" width="320" height="1100" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_s" value="Sistem" style="swimlane;startSize=30;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="320" y="0" width="500" height="1100" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="sw_a" value="Admin (Email)" style="swimlane;startSize=30;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;fontSize=12;horizontal=0;" vertex="1" parent="sw_root"><mxGeometry x="820" y="0" width="280" height="1100" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="ms" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="sw_u"><mxGeometry x="145" y="30" width="30" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="m1" value="Login ke sistem" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="90" width="200" height="40" as="geometry"/></mxCell>\n'

# SET MAINTENANCE
cells += '        <mxCell id="msec1" value="BAGIAN 1: Set Aset ke Maintenance" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;fontSize=11;fontStyle=1;" vertex="1" parent="sw_u"><mxGeometry x="10" y="150" width="290" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="m2" value="Buka detail aset&#xa;Klik &quot;Set Maintenance&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="200" width="200" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms1" value="Tampilkan modal konfirmasi + input keterangan (opsional)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="200" width="440" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="m3" value="Input keterangan (opsional)&#xa;Klik &quot;Konfirmasi&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="280" width="200" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms2" value="POST /maintenance/{kode}/set&#xa;$asset-&gt;update([status=&gt;Maintenance, updated_by=&gt;auth()-&gt;id()])&#xa;ActivityLogger::logAsset(&#39;Update&#39;, &#39;Aset masuk maintenance...&#39;)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="280" width="440" height="70" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms3" value="Redirect back + flash success" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="370" width="440" height="40" as="geometry"/></mxCell>\n'

# SELESAIKAN MAINTENANCE
cells += '        <mxCell id="msec2" value="BAGIAN 2: Selesaikan Maintenance" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;fontSize=11;fontStyle=1;" vertex="1" parent="sw_u"><mxGeometry x="10" y="440" width="290" height="30" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="m4" value="Buka menu &quot;Maintenance&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="490" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms4" value="Query aset WHERE status=&#39;Maintenance&#39;&#xa;Tampilkan dashboard maintenance + statistik" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="490" width="440" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="m5" value="Klik &quot;Selesai&quot; pada aset" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="570" width="200" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms5" value="Tampilkan modal: pilih kondisi akhir (wajib) + keterangan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="570" width="440" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="m6" value="Pilih kondisi akhir&#xa;(Baik/Rusak Ringan/Rusak Berat)&#xa;Klik &quot;Konfirmasi Selesai&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffde7;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_u"><mxGeometry x="60" y="640" width="200" height="70" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms6" value="PATCH /maintenance/{kode}/complete&#xa;Validasi: kondisi required" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="640" width="440" height="50" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="md1" value="Validasi&#xa;gagal?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="170" y="720" width="110" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms7" value="Error: kondisi wajib dipilih" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="340" y="730" width="100" height="40" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms8" value="$asset-&gt;update([status=&gt;Aktif, kondisi=&gt;$request-&gt;kondisi, updated_by=&gt;auth()-&gt;id()])&#xa;ActivityLogger::logAsset(&#39;Update&#39;, &#39;Maintenance selesai...&#39;)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="810" width="440" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms9" value="User::where(role,admin)-&gt;where(is_active,1)-&gt;get()&#xa;Loop: Mail::to($admin-&gt;email)-&gt;send(new MaintenanceAlert($asset,&#39;selesai&#39;))" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="890" width="440" height="60" as="geometry"/></mxCell>\n'
cells += '        <mxCell id="ms10" value="Redirect ke /maintenance + flash success" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="sw_s"><mxGeometry x="30" y="970" width="440" height="40" as="geometry"/></mxCell>\n'

# Admin receives email
cells += '        <mxCell id="ma1" value="Menerima email notifikasi:&#xa;&quot;Maintenance Selesai:&#xa;{nama_aset} ({kode})&#xa;Kondisi akhir: {kondisi}&quot;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="sw_a"><mxGeometry x="40" y="890" width="200" height="80" as="geometry"/></mxCell>\n'

cells += '        <mxCell id="me" value="" style="ellipse;aspect=fixed;fillColor=#000000;strokeColor=#000000;double=1;" vertex="1" parent="sw_u"><mxGeometry x="145" y="1040" width="30" height="30" as="geometry"/></mxCell>\n'

for src, tgt, lbl in [
    ("ms","m1",""), ("m1","m2",""), ("m2","ms1",""), ("ms1","m3",""),
    ("m3","ms2",""), ("ms2","ms3",""), ("ms3","m4",""),
    ("m4","ms4",""), ("ms4","m5",""), ("m5","ms5",""), ("ms5","m6",""),
    ("m6","ms6",""), ("ms6","md1",""), ("md1","ms8","Tidak"), ("md1","ms7","Ya"),
    ("ms7","m6",""), ("ms8","ms9",""), ("ms9","ms10",""), ("ms9","ma1",""),
    ("ms10","me",""),
]:
    cells += f'        <mxCell id="arr_{src}_{tgt}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry"/></mxCell>\n'

w("12_Activity_Maintenance.drawio", mxfile("Activity Diagram - Maintenance Aset", cells))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# SEQUENCE DIAGRAM BUILDER
# ─────────────────────────────────────────────────────────────────────────────
def build_sequence(fname, title, participants, messages):
    """
    participants: list of (id, label, x, color, stroke)
    messages: list of (id, src_id, tgt_id, label, y, dashed, ret_arrow)
    """
    cells = ""
    # Title
    cells += f'        <mxCell id="title" value="{title}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="20" y="10" width="1400" height="40" as="geometry"/></mxCell>\n'

    # Lifelines
    for pid, plabel, px, pcolor, pstroke in participants:
        # Header box
        cells += f'        <mxCell id="{pid}_hdr" value="{plabel}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={pcolor};strokeColor={pstroke};fontStyle=1;fontSize=11;" vertex="1" parent="1"><mxGeometry x="{px}" y="60" width="130" height="50" as="geometry"/></mxCell>\n'
        # Dashed lifeline
        cells += f'        <mxCell id="{pid}_line" value="" style="endArrow=none;dashed=1;edgeStyle=orthogonalEdgeStyle;strokeColor={pstroke};" edge="1" parent="1" source="{pid}_hdr" target="{pid}_end"><mxGeometry relative="1" as="geometry"/></mxCell>\n'
        cells += f'        <mxCell id="{pid}_end" value="" style="ellipse;aspect=fixed;fillColor=none;strokeColor=none;" vertex="1" parent="1"><mxGeometry x="{px+55}" y="1200" width="20" height="20" as="geometry"/></mxCell>\n'

    # Messages
    for mid, src, tgt, label, y, dashed, ret in messages:
        sx = next(px+65 for pid,_,px,_,_ in participants if pid==src)
        tx = next(px+65 for pid,_,px,_,_ in participants if pid==tgt)
        dash = "dashed=1;" if dashed or ret else ""
        end_arrow = "open" if ret else "block"
        end_fill = "0" if ret else "1"
        cells += f'        <mxCell id="{mid}" value="{label}" style="edgeStyle=orthogonalEdgeStyle;{dash}endArrow={end_arrow};endFill={end_fill};exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fontSize=10;align=center;verticalAlign=bottom;" edge="1" parent="1" source="{src}_hdr" target="{tgt}_hdr"><mxGeometry y="{y}" relative="1" as="geometry"><Array as="points"><mxPoint x="{sx}" y="{y}"/><mxPoint x="{tx}" y="{y}"/></Array></mxGeometry></mxCell>\n'

    return mxfile(title, cells)

# ─────────────────────────────────────────────────────────────────────────────
# 13 SEQUENCE: LOGIN
# ─────────────────────────────────────────────────────────────────────────────
print("13_Sequence_Login.drawio")

participants = [
    ("actor",   ":Pengguna",              30,  "#dae8fc", "#6c8ebf"),
    ("browser", ":Browser",              200,  "#dae8fc", "#6c8ebf"),
    ("router",  ":Router\n(routes/auth)", 370,  "#d5e8d4", "#82b366"),
    ("ctrl",    ":AuthenticatedSession\nController", 540, "#d5e8d4", "#82b366"),
    ("req",     ":LoginRequest",          710,  "#fff2cc", "#d6b656"),
    ("ratelim", ":RateLimiter",           880,  "#fff2cc", "#d6b656"),
    ("umodel",  ":User (Model)",         1050,  "#e1d5e7", "#9673a6"),
    ("db",      ":Database (MySQL)",     1220,  "#f8cecc", "#b85450"),
    ("logger",  ":ActivityLogger",       1390,  "#d5e8d4", "#82b366"),
]

messages = [
    # id, src, tgt, label, y, dashed, return
    ("m1",  "actor",   "browser",  "Buka /login",                          130, False, False),
    ("m2",  "browser", "router",   "GET /login [middleware: guest]",        160, False, False),
    ("m3",  "router",  "ctrl",     "create()",                             190, False, False),
    ("m4",  "ctrl",    "browser",  "view(auth.login)",                     220, False, True),
    ("m5",  "browser", "actor",    "Halaman login ditampilkan",            250, False, True),
    ("m6",  "actor",   "browser",  "Input email+password → Klik Masuk",   290, False, False),
    ("m7",  "browser", "router",   "POST /login {email, password}",        320, False, False),
    ("m8",  "router",  "ctrl",     "store(LoginRequest)",                  350, False, False),
    ("m9",  "ctrl",    "req",      "validate() [email, password required]",380, False, False),
    ("m10", "req",     "ratelim",  "tooManyAttempts(throttleKey, 5)",      420, False, False),
    ("m11", "ratelim", "req",      "false (belum terlampaui)",             450, False, True),
    ("m12", "req",     "umodel",   "User::where(email)->first()",          490, False, False),
    ("m13", "umodel",  "db",       "SELECT * FROM users WHERE email=?",    520, False, False),
    ("m14", "db",      "umodel",   "User record",                          550, False, True),
    ("m15", "umodel",  "req",      "$user",                                580, False, True),
    ("m16", "req",     "req",      "Cek is_active = 1",                    610, False, False),
    ("m17", "req",     "req",      "Auth::attempt(email, password)",       640, False, False),
    ("m18", "req",     "db",       "Verifikasi password hash",             670, False, False),
    ("m19", "db",      "req",      "match = true",                         700, False, True),
    ("m20", "req",     "ratelim",  "clear(throttleKey)",                   730, False, False),
    ("m21", "req",     "ctrl",     "void (authenticate selesai)",          760, False, True),
    ("m22", "ctrl",    "ctrl",     "session()->regenerate()",              790, False, False),
    ("m23", "ctrl",    "umodel",   "update([last_login_at => now()])",     820, False, False),
    ("m24", "umodel",  "db",       "UPDATE users SET last_login_at=NOW()", 850, False, False),
    ("m25", "ctrl",    "logger",   "logAuth(Login, User berhasil login...)",880, False, False),
    ("m26", "logger",  "db",       "INSERT INTO log_aktivitas",            910, False, False),
    ("m27", "ctrl",    "browser",  "redirect()->route(dashboard) [302]",   950, False, True),
    ("m28", "browser", "actor",    "Diarahkan ke /dashboard",              980, False, True),
]

w("13_Sequence_Login.drawio", build_sequence("13_Sequence_Login.drawio", "Sequence Diagram — Login", participants, messages))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 14 SEQUENCE: TAMBAH ASET
# ─────────────────────────────────────────────────────────────────────────────
print("14_Sequence_TambahAset.drawio")

participants = [
    ("actor",   ":Pengguna\n(Staff/Admin)",  30,  "#dae8fc", "#6c8ebf"),
    ("browser", ":Browser",                 200,  "#dae8fc", "#6c8ebf"),
    ("ctrl",    ":AssetController",          370,  "#d5e8d4", "#82b366"),
    ("bmodel",  ":Barang (Model)",           540,  "#e1d5e7", "#9673a6"),
    ("rmodel",  ":Ruangan (Model)",          710,  "#e1d5e7", "#9673a6"),
    ("amodel",  ":Asset (Model)",            880,  "#e1d5e7", "#9673a6"),
    ("db",      ":Database (MySQL)",        1050,  "#f8cecc", "#b85450"),
    ("fs",      ":FileSystem\n(foto_aset)", 1220,  "#fff2cc", "#d6b656"),
    ("logger",  ":ActivityLogger",          1390,  "#d5e8d4", "#82b366"),
]

messages = [
    ("m1",  "actor",   "browser",  "Klik + Tambah Aset",                          130, False, False),
    ("m2",  "browser", "ctrl",     "GET /aset/create",                            160, False, False),
    ("m3",  "ctrl",    "bmodel",   "Barang::where(status,aktif)->get()",           190, False, False),
    ("m4",  "bmodel",  "db",       "SELECT kode_barang,nama_barang FROM barang WHERE status=aktif", 220, False, False),
    ("m5",  "db",      "bmodel",   "[BRG-001 Kamera Sony A7, BRG-002 Mic Rode]",  250, False, True),
    ("m6",  "ctrl",    "rmodel",   "Ruangan::orderBy(nama)->get()",                280, False, False),
    ("m7",  "rmodel",  "db",       "SELECT * FROM ruangan ORDER BY nama",          310, False, False),
    ("m8",  "db",      "rmodel",   "[Studio 1, Studio 2, Ruang Editing, ...]",     340, False, True),
    ("m9",  "ctrl",    "browser",  "view(aset.create, compact(barangs,ruangans))", 370, False, True),
    ("m10", "browser", "actor",    "Form tambah aset ditampilkan",                 400, False, True),
    ("m11", "actor",   "browser",  "Isi form → Klik Simpan Aset",                 440, False, False),
    ("m12", "browser", "ctrl",     "POST /aset {kode_barang, ruangan_id, kondisi, status, ...}", 470, False, False),
    ("m13", "ctrl",    "ctrl",     "$request->validate([kode_barang required|exists, ...])", 500, False, False),
    ("m14", "ctrl",    "amodel",   "Asset::generateKode() [gap-filling]",          540, False, False),
    ("m15", "amodel",  "db",       "SELECT kode_aset FROM aset WITH TRASHED",      570, False, False),
    ("m16", "db",      "amodel",   "[AST-001, AST-002]",                           600, False, True),
    ("m17", "amodel",  "ctrl",     "AST-003 (kode baru)",                          630, False, True),
    ("m18", "ctrl",    "fs",       "foto->move(public/foto_aset/, timestamp_nama)", 660, False, False),
    ("m19", "fs",      "ctrl",     "nama file tersimpan",                          690, False, True),
    ("m20", "ctrl",    "amodel",   "Asset::create([kode_aset=AST-003, kode_barang=BRG-001, ...])", 720, False, False),
    ("m21", "amodel",  "db",       "INSERT INTO aset (...) VALUES (...)",           750, False, False),
    ("m22", "db",      "amodel",   "Record tersimpan",                             780, False, True),
    ("m23", "ctrl",    "logger",   "logAsset(Create, Menambahkan aset baru: ...)", 810, False, False),
    ("m24", "logger",  "db",       "INSERT INTO log_aktivitas",                    840, False, False),
    ("m25", "ctrl",    "browser",  "redirect()->route(aset.index) + flash success", 880, False, True),
    ("m26", "browser", "actor",    "Halaman daftar aset + notifikasi sukses",       910, False, True),
]

w("14_Sequence_TambahAset.drawio", build_sequence("14_Sequence_TambahAset.drawio", "Sequence Diagram — Tambah Aset Baru", participants, messages))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 15 SEQUENCE: SCAN QR CODE
# ─────────────────────────────────────────────────────────────────────────────
print("15_Sequence_ScanQR.drawio")

participants = [
    ("actor",   ":Pengguna",              30,  "#dae8fc", "#6c8ebf"),
    ("browser", ":Browser",              200,  "#dae8fc", "#6c8ebf"),
    ("qctrl",   ":QrCodeController",     370,  "#d5e8d4", "#82b366"),
    ("actrl",   ":AssetController",      540,  "#d5e8d4", "#82b366"),
    ("amodel",  ":Asset (Model)",        710,  "#e1d5e7", "#9673a6"),
    ("db",      ":Database (MySQL)",     880,  "#f8cecc", "#b85450"),
    ("qrapi",   ":qrserver.com\n(API)",  1050, "#fff2cc", "#d6b656"),
    ("fs",      ":FileSystem\n(qr_codes)",1220,"#fff2cc", "#d6b656"),
]

messages = [
    ("m1",  "actor",   "browser",  "Klik Generate QR Code pada AST-001",          130, False, False),
    ("m2",  "browser", "actrl",    "POST /aset/AST-001/generate-qr",              160, False, False),
    ("m3",  "actrl",   "amodel",   "Asset::where(kode_aset,AST-001)->firstOrFail()",190, False, False),
    ("m4",  "amodel",  "db",       "SELECT * FROM aset WHERE kode_aset=AST-001",   220, False, False),
    ("m5",  "db",      "amodel",   "Asset record",                                 250, False, True),
    ("m6",  "actrl",   "fs",       "glob(qr_codes/qr_AST-001*.png)",               280, False, False),
    ("m7",  "fs",      "actrl",    "[] (belum ada)",                               310, False, True),
    ("m8",  "actrl",   "qrapi",    "GET api.qrserver.com?size=300x300&data={url}", 350, False, False),
    ("m9",  "qrapi",   "actrl",    "PNG binary data (300x300)",                    380, False, True),
    ("m10", "actrl",   "fs",       "file_put_contents(qr_AST-001_{ts}.png)",       410, False, False),
    ("m11", "actrl",   "browser",  "redirect()->back() + success",                 450, False, True),
    ("m12", "browser", "actor",    "Notifikasi: QR Code berhasil di-generate",     480, False, True),
    ("m13", "actor",   "browser",  "Buka menu QR Scanner",                         520, False, False),
    ("m14", "browser", "qctrl",    "GET /qrcode/scanner",                          550, False, False),
    ("m15", "qctrl",   "browser",  "view(qrcode.scanner) [akses kamera]",          580, False, True),
    ("m16", "actor",   "browser",  "Arahkan kamera ke QR Code aset fisik",         620, False, False),
    ("m17", "browser", "browser",  "Decode QR → URL: /aset/AST-001/detail",        650, False, False),
    ("m18", "browser", "actrl",    "GET /aset/AST-001/detail [route publik]",       680, False, False),
    ("m19", "actrl",   "amodel",   "Asset::with([barang,ruangan,creator])->firstOrFail()", 710, False, False),
    ("m20", "amodel",  "db",       "SELECT aset.*, barang.*, ruangan.* WHERE kode_aset=AST-001", 740, False, False),
    ("m21", "db",      "amodel",   "{kode:AST-001, nama:Kamera Sony A7, ruangan:Ruang Editing, status:Maintenance}", 770, False, True),
    ("m22", "actrl",   "browser",  "view(aset.show, compact(asset))",              810, False, True),
    ("m23", "browser", "actor",    "Detail aset: Kamera Sony A7 | Maintenance | Ruang Editing", 840, False, True),
]

w("15_Sequence_ScanQR.drawio", build_sequence("15_Sequence_ScanQR.drawio", "Sequence Diagram — Scan QR Code", participants, messages))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 16 SEQUENCE: MAINTENANCE
# ─────────────────────────────────────────────────────────────────────────────
print("16_Sequence_Maintenance.drawio")

participants = [
    ("actor",   ":Staff/Admin",           30,  "#dae8fc", "#6c8ebf"),
    ("browser", ":Browser",              200,  "#dae8fc", "#6c8ebf"),
    ("ctrl",    ":MaintenanceController", 370,  "#d5e8d4", "#82b366"),
    ("amodel",  ":Asset (Model)",         540,  "#e1d5e7", "#9673a6"),
    ("umodel",  ":User (Model)",          710,  "#e1d5e7", "#9673a6"),
    ("db",      ":Database (MySQL)",      880,  "#f8cecc", "#b85450"),
    ("logger",  ":ActivityLogger",       1050,  "#d5e8d4", "#82b366"),
    ("mail",    ":MaintenanceAlert\n(Mail)", 1220, "#fff2cc", "#d6b656"),
    ("smtp",    ":SMTP Server",          1390,  "#f8cecc", "#b85450"),
]

messages = [
    ("m1",  "actor",   "browser",  "Buka detail AST-001 → Klik Set Maintenance",  130, False, False),
    ("m2",  "browser", "ctrl",     "POST /maintenance/AST-001/set {keterangan}",   160, False, False),
    ("m3",  "ctrl",    "amodel",   "Asset::where(kode_aset,AST-001)->firstOrFail()",190, False, False),
    ("m4",  "amodel",  "db",       "SELECT * FROM aset WHERE kode_aset=AST-001",   220, False, False),
    ("m5",  "db",      "amodel",   "Asset record",                                 250, False, True),
    ("m6",  "ctrl",    "amodel",   "update([status=>Maintenance, updated_by=>auth()->id()])", 280, False, False),
    ("m7",  "amodel",  "db",       "UPDATE aset SET status=Maintenance WHERE kode_aset=AST-001", 310, False, False),
    ("m8",  "ctrl",    "logger",   "logAsset(Update, Aset masuk maintenance...)",  350, False, False),
    ("m9",  "logger",  "db",       "INSERT INTO log_aktivitas",                    380, False, False),
    ("m10", "ctrl",    "browser",  "redirect()->back() + success",                 420, False, True),
    ("m11", "browser", "actor",    "Notifikasi sukses",                            450, False, True),
    ("m12", "actor",   "browser",  "Buka menu Maintenance → Klik Selesai",         490, False, False),
    ("m13", "browser", "ctrl",     "PATCH /maintenance/AST-001/complete {kondisi:Baik}", 520, False, False),
    ("m14", "ctrl",    "amodel",   "Asset::where(kode_aset,AST-001)->firstOrFail()",550, False, False),
    ("m15", "amodel",  "db",       "SELECT * FROM aset WHERE kode_aset=AST-001",   580, False, False),
    ("m16", "db",      "amodel",   "Asset record",                                 610, False, True),
    ("m17", "ctrl",    "ctrl",     "validate([kondisi required|in:Baik,...])",      640, False, False),
    ("m18", "ctrl",    "amodel",   "update([status=>Aktif, kondisi=>Baik, updated_by=>...])", 670, False, False),
    ("m19", "amodel",  "db",       "UPDATE aset SET status=Aktif, kondisi=Baik WHERE kode_aset=AST-001", 700, False, False),
    ("m20", "ctrl",    "logger",   "logAsset(Update, Maintenance selesai: Kamera Sony A7...)", 730, False, False),
    ("m21", "logger",  "db",       "INSERT INTO log_aktivitas",                    760, False, False),
    ("m22", "ctrl",    "umodel",   "User::where(role,admin)->where(is_active,1)->get()", 800, False, False),
    ("m23", "umodel",  "db",       "SELECT * FROM users WHERE role=admin AND is_active=1", 830, False, False),
    ("m24", "db",      "umodel",   "[Admin Magang (magangrbtv@gmail.com)]",         860, False, True),
    ("m25", "ctrl",    "mail",     "new MaintenanceAlert($asset, selesai)",         890, False, False),
    ("m26", "ctrl",    "smtp",     "Mail::to(admin@email)->send($mail)",            920, False, False),
    ("m27", "smtp",    "actor",    "Email: Maintenance Selesai: Kamera Sony A7",    950, False, True),
    ("m28", "ctrl",    "browser",  "redirect()->route(maintenance.index) + success", 990, False, True),
    ("m29", "browser", "actor",    "Dashboard maintenance + notifikasi sukses",    1020, False, True),
]

w("16_Sequence_Maintenance.drawio", build_sequence("16_Sequence_Maintenance.drawio", "Sequence Diagram — Maintenance Aset", participants, messages))
print("  done")

# ─────────────────────────────────────────────────────────────────────────────
# 17 SEQUENCE: KELOLA PENGGUNA
# ─────────────────────────────────────────────────────────────────────────────
print("17_Sequence_Pengguna.drawio")

participants = [
    ("actor",   ":Admin",                 30,  "#f8cecc", "#b85450"),
    ("browser", ":Browser",              200,  "#dae8fc", "#6c8ebf"),
    ("router",  ":Router\n(role:admin)", 370,  "#d5e8d4", "#82b366"),
    ("ctrl",    ":UserController",        540,  "#d5e8d4", "#82b366"),
    ("umodel",  ":User (Model)",          710,  "#e1d5e7", "#9673a6"),
    ("db",      ":Database (MySQL)",      880,  "#f8cecc", "#b85450"),
    ("mail",    ":AkunBaruMail",         1050,  "#fff2cc", "#d6b656"),
    ("smtp",    ":SMTP Server",          1220,  "#f8cecc", "#b85450"),
    ("logger",  ":ActivityLogger",       1390,  "#d5e8d4", "#82b366"),
]

messages = [
    ("m1",  "actor",   "browser",  "Klik menu Kelola Pengguna",                   130, False, False),
    ("m2",  "browser", "router",   "GET /users",                                  160, False, False),
    ("m3",  "router",  "router",   "Cek middleware role:admin",                   190, False, False),
    ("m4",  "router",  "ctrl",     "index()",                                     220, False, False),
    ("m5",  "ctrl",    "umodel",   "User::orderBy(role)->get()",                  250, False, False),
    ("m6",  "umodel",  "db",       "SELECT * FROM users ORDER BY role",           280, False, False),
    ("m7",  "db",      "umodel",   "[Admin Magang(admin), Staff RBTV(staff), reffki(staff)]", 310, False, True),
    ("m8",  "ctrl",    "browser",  "view(users.index, compact(users))",           340, False, True),
    ("m9",  "browser", "actor",    "Daftar pengguna ditampilkan",                 370, False, True),
    ("m10", "actor",   "browser",  "Klik + Tambah Pengguna",                      410, False, False),
    ("m11", "browser", "ctrl",     "GET /users/create",                           440, False, False),
    ("m12", "ctrl",    "browser",  "view(users.create)",                          470, False, True),
    ("m13", "actor",   "browser",  "Isi form: Nama, Email, Password, Role, Kirim Email", 510, False, False),
    ("m14", "browser", "ctrl",     "POST /users {name, email, password, role, kirim_email}", 540, False, False),
    ("m15", "ctrl",    "ctrl",     "validate([name required, email unique, password regex, role in:admin,staff])", 570, False, False),
    ("m16", "ctrl",    "umodel",   "User::create([name, email, Hash::make(password), role, is_active:true])", 610, False, False),
    ("m17", "umodel",  "db",       "INSERT INTO users (name,email,password,role,is_active,...)", 640, False, False),
    ("m18", "db",      "umodel",   "User record (id=5)",                          670, False, True),
    ("m19", "ctrl",    "mail",     "new AkunBaruMail(user, plainPassword)",        710, False, False),
    ("m20", "ctrl",    "smtp",     "Mail::to(email)->send($mail)",                740, False, False),
    ("m21", "smtp",    "actor",    "Email: Akun baru dibuat (email+password)",     770, False, True),
    ("m22", "ctrl",    "logger",   "logUser(Create, Menambahkan pengguna baru...)",800, False, False),
    ("m23", "logger",  "db",       "INSERT INTO log_aktivitas",                   830, False, False),
    ("m24", "ctrl",    "browser",  "redirect()->route(users.index) + success",    870, False, True),
    ("m25", "browser", "actor",    "Daftar pengguna + notifikasi sukses",          900, False, True),
]

w("17_Sequence_Pengguna.drawio", build_sequence("17_Sequence_Pengguna.drawio", "Sequence Diagram — Kelola Pengguna (Admin)", participants, messages))
print("  done")

print("\nSemua diagram selesai dibuat!")
