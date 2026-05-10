# MODUL 3 — PERANCANGAN SISTEM
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 3.1 Pendahuluan

Perancangan sistem adalah tahap yang menerjemahkan seluruh kebutuhan yang telah dianalisis pada Modul 2 ke dalam bentuk rancangan teknis yang konkret. Modul ini mencakup: Use Case Diagram, Activity Diagram, Sequence Diagram, ERD (menggunakan data aktual database simset_rbtv), Arsitektur Sistem MVC, serta perancangan antarmuka pengguna lengkap termasuk layout, navbar, dan semua halaman.

---

## 3.2 Use Case Diagram

Use Case Diagram menggambarkan interaksi antara aktor dan sistem. SimAset memiliki dua aktor: **Admin** dan **Staff**.

> **[GAMBAR 3.1: Use Case Diagram SimAset — menampilkan dua aktor (Admin dan Staff) dengan seluruh use case yang dapat dilakukan masing-masing, termasuk relasi include dan extend]**

### 3.2.1 Use Case Staff

Staff dapat melakukan semua operasional harian:

| Modul | Use Case |
|-------|----------|
| Autentikasi | Login, Logout, Reset Password, Edit Profil |
| Aset | Lihat daftar, Tambah, Edit, Detail, Hapus (soft delete), Batch delete, Upload foto |
| Barang | Lihat, Tambah, Edit, Hapus master barang |
| Ruangan | Lihat, Tambah, Edit, Hapus ruangan (validasi aset) |
| QR Code | Generate, Cetak individual, Batch print, Scanner web |
| Maintenance | Lihat dashboard, Set maintenance, Selesaikan maintenance |
| Import | Import aset/barang dari Excel/CSV, Download template |
| Export | Export aset/barang ke Excel/PDF/CSV |
| Laporan | Cetak laporan aset, per ruangan, maintenance |

### 3.2.2 Use Case Admin (Tambahan)

Selain semua use case Staff, Admin juga dapat:

| Modul | Use Case |
|-------|----------|
| Pengguna | Lihat daftar, Tambah, Edit, Hapus, Kirim email notifikasi |
| Audit Log | Lihat semua log, Filter by user/aktivitas/kata kunci |

---

## 3.3 Activity Diagram

### 3.3.1 Activity Diagram: Login

```
[MULAI]
   |
   v
Buka /login
   |
   v
Input email + password
   |
   v
[Validasi input kosong?] --Ya--> Tampilkan error validasi
   |Tidak
   v
POST /login -> LoginRequest::authenticate()
   |
   v
[Rate limit exceeded?] --Ya--> "Too many attempts, tunggu X detik"
   |Tidak
   v
Auth::attempt(email, password)
   |
   |--Gagal--> RateLimiter::hit() -> "Kredensial tidak cocok"
   |
   v Berhasil
session()->regenerate()
   |
   v
ActivityLog::create(Login, ...)
   |
   v
Redirect /dashboard
   |
[SELESAI]
```

> **[GAMBAR 3.2: Activity Diagram Login dengan swimlane Pengguna dan Sistem]**

### 3.3.2 Activity Diagram: Tambah Aset

```
[MULAI]
   |
   v
GET /aset/create
   |
   v
Sistem load dropdown: Barang aktif (BRG-001, BRG-002) + Ruangan (Studio 1, Ruang Editing, dll)
   |
   v
Pengguna isi form: barang, ruangan, kondisi, status, tanggal, serial, foto, harga, sumber
   |
   v
POST /aset
   |
   v
[Validasi server-side gagal?] --Ya--> Redirect back + errors per field
   |Tidak
   v
Asset::generateKode() -- gap-filling: cek AST-001,002,003(del) -> return AST-004
   |
   v
[Ada foto?] --Ya--> simpan ke public/foto_aset/{timestamp}_{nama}
   |
   v
Asset::create($data) dengan created_by = auth()->id()
   |
   v
ActivityLogger::logAsset(Create, "Menambahkan aset baru: ...")
   |
   v
Redirect /aset + flash success
   |
[SELESAI]
```

> **[GAMBAR 3.3: Activity Diagram Tambah Aset dengan swimlane Pengguna, Controller, Model, Database]**

### 3.3.3 Activity Diagram: Maintenance

```
[SET MAINTENANCE]
   |
   v
Buka detail aset (contoh: AST-001 Kamera Sony A7)
   |
   v
Klik "Set Maintenance" -> modal konfirmasi + input keterangan
   |
   v
POST /maintenance/AST-001/set
   |
   v
Asset::update([status => Maintenance, updated_by => auth()->id()])
   |
   v
ActivityLogger::logAsset(Update, "Aset masuk maintenance: ...")
   |
   v
Redirect back + success

[SELESAIKAN MAINTENANCE]
   |
   v
Buka /maintenance -> klik "Selesai" pada AST-001
   |
   v
Modal: pilih kondisi akhir (Baik/Rusak Ringan/Rusak Berat) + keterangan
   |
   v
PATCH /maintenance/AST-001/complete
   |
   v
[Validasi kondisi wajib?] --Gagal--> error
   |
   v
Asset::update([status => Aktif, kondisi => $request->kondisi])
   |
   v
ActivityLogger::logAsset(Update, "Maintenance selesai: ...")
   |
   v
User::where(role,admin)->where(is_active,1)->get()
   |
   v
Mail::to(magangrbtv@gmail.com)->send(new MaintenanceAlert($asset, selesai))
   |
   v
Redirect /maintenance + success
[SELESAI]
```

> **[GAMBAR 3.4: Activity Diagram Maintenance (Set dan Selesai) dengan notifikasi email ke Admin]**

---

## 3.4 Sequence Diagram

### 3.4.1 Sequence Diagram: Login

```
Pengguna  Browser  Router  AuthController  LoginRequest  User  Session  ActivityLog
   |         |       |           |              |          |       |          |
   |--POST /login-->  |           |              |          |       |          |
   |         |------> |           |              |          |       |          |
   |         |        |--store()-->              |          |       |          |
   |         |        |           |--validate()-->          |       |          |
   |         |        |           |--authenticate()         |       |          |
   |         |        |           |              |--attempt()|      |          |
   |         |        |           |              |<--true/false     |          |
   |         |        |           |--session()->regenerate()-->     |          |
   |         |        |           |--ActivityLog::create()--------->|          |
   |         |        |           |--redirect()->intended(/dashboard)          |
   |<--302 /dashboard-|           |              |          |       |          |
```

> **[GAMBAR 3.5: Sequence Diagram Login SimAset]**

### 3.4.2 Sequence Diagram: Tambah Aset

```
Pengguna  Browser  AssetController  Asset::generateKode  DB  ActivityLog
   |         |            |                  |            |       |
   |--POST /aset-->        |                  |            |       |
   |         |--store()-->  |                  |            |       |
   |         |            |--validate()        |            |       |
   |         |            |--generateKode()-->  |            |       |
   |         |            |  withTrashed()->pluck(kode_aset) |       |
   |         |            |  [AST-001,AST-002,AST-003(del)]  |       |
   |         |            |<--AST-004           |            |       |
   |         |            |--foto->move(public/foto_aset/)   |       |
   |         |            |--Asset::create($data)----------->|       |
   |         |            |--logAsset(Create, ...)---------->|       |
   |         |<--redirect /aset + success                    |       |
```

> **[GAMBAR 3.6: Sequence Diagram Tambah Aset Baru]**

### 3.4.3 Sequence Diagram: Scan QR Code

```
Smartphone  Browser  Router  AssetController  Asset  Barang  Ruangan
    |           |       |          |            |       |        |
    |--scan QR AST-001-->           |            |       |        |
    |           |--GET /aset/AST-001/detail-->   |       |        |
    |           |       |--detail(AST-001)-->     |       |        |
    |           |       |          |--with([barang,ruangan,creator])
    |           |       |          |--where(kode_aset,AST-001)-->  |
    |           |       |          |<--asset: Kamera Sony A7       |
    |           |       |          |   ruangan: Ruang Editing      |
    |           |       |          |   status: Maintenance         |
    |           |<--view aset.show (detail lengkap)                |
    |<--tampilkan: Kamera Sony A7, Maintenance, Ruang Editing      |
```

> **[GAMBAR 3.7: Sequence Diagram Scan QR Code dan tampilkan detail aset]**

---

## 3.5 Entity Relationship Diagram (ERD)

Database SimAset menggunakan MySQL 8.0.30 dengan nama database **simset_rbtv**.

> **[GAMBAR 3.8: ERD SimAset lengkap menampilkan semua entitas, atribut, dan relasi dengan notasi crow's foot]**

### 3.5.1 Entitas dan Atribut

**Tabel `users`**

| Kolom | Tipe | Constraint | Keterangan |
|-------|------|------------|------------|
| id | int | PK, AUTO_INCREMENT | Primary key |
| name | varchar(100) | NOT NULL | Nama lengkap |
| email | varchar(100) | UNIQUE, NOT NULL | Email login |
| password | varchar(255) | NOT NULL | Hash bcrypt |
| role | enum(admin,staff) | DEFAULT staff | Peran pengguna |
| is_active | tinyint(1) | DEFAULT 1 | Status aktif |
| last_login_at | timestamp | NULL | Login terakhir |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | |
| updated_at | timestamp | NULL | |

Data aktual: id=2 (Staff RBTV, staff), id=3 (Admin Magang, admin), id=4 (reffki, staff)

**Tabel `barang`**

| Kolom | Tipe | Constraint | Keterangan |
|-------|------|------------|------------|
| kode_barang | varchar(20) | PK | Format BRG-001 |
| nama_barang | varchar(150) | NOT NULL | Nama barang |
| kategori | enum(Kamera,Audio,Komputer,Lighting,Furniture,Peralatan Kantor) | NOT NULL | |
| status | enum(aktif,nonaktif) | DEFAULT aktif | |
| keterangan | text | NULL | |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | |
| updated_at | timestamp | NULL ON UPDATE | |
| deleted_at | timestamp | NULL | Soft delete |

Data aktual: BRG-001 (Kamera Sony A7), BRG-002 (Mic Wireless Rode), BRG-003 (printer epson l200, soft-deleted)

**Tabel `ruangan`**

| Kolom | Tipe | Constraint | Keterangan |
|-------|------|------------|------------|
| id | int | PK, AUTO_INCREMENT | |
| nama | varchar(100) | NOT NULL | Nama ruangan |
| lantai | varchar(50) | NULL | Lantai/lokasi |
| keterangan | text | NULL | |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | |

Data aktual: id=1 (Studio 1, Lantai 1), id=2 (Studio 2, Lantai 2), id=3 (Ruang Editing, Lantai 1), id=4 (Ruang Redaksi, lantai 5)

**Tabel `aset` (tabel utama)**

| Kolom | Tipe | Constraint | Keterangan |
|-------|------|------------|------------|
| kode_aset | varchar(20) | PK | Format AST-001 |
| kode_barang | varchar(20) | FK→barang (RESTRICT del, CASCADE upd) | |
| ruangan_id | int | FK→ruangan (SET NULL del, CASCADE upd) | |
| kondisi | enum(Baik,Rusak Ringan,Rusak Berat) | DEFAULT Baik | |
| status | enum(Aktif,Maintenance,Non-Aktif) | DEFAULT Aktif | |
| serial_number | varchar(100) | NULL | Nomor seri |
| foto | varchar(255) | NULL | Nama file foto |
| jumlah | int | DEFAULT 1 | Jumlah unit |
| tanggal_perolehan | date | NULL | |
| harga_perolehan | decimal(15,2) | NULL | |
| sumber_perolehan | varchar(255) | NULL | Pembelian/Hibah/dll |
| keterangan | text | NULL | |
| created_by | int | NULL | FK implisit ke users |
| updated_by | int | NULL | FK implisit ke users |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | |
| updated_at | timestamp | NULL ON UPDATE | |
| deleted_at | timestamp | NULL | Soft delete |

Data aktual:
- AST-001: BRG-001, ruangan_id=3, Baik, **Maintenance**, serial=ggG
- AST-002: BRG-001, ruangan_id=3, Baik, Aktif, serial=hgfx
- AST-003: BRG-003, ruangan_id=4, Baik, Aktif, foto=1777735186_AST-001.png, **soft-deleted**

**Tabel `log_aktivitas`**

| Kolom | Tipe | Constraint | Keterangan |
|-------|------|------------|------------|
| id | bigint UNSIGNED | PK, AUTO_INCREMENT=40 | |
| user_id | bigint UNSIGNED | FK→users (SET NULL) | |
| aktivitas | varchar(255) | NOT NULL | Login/Create/Update/Delete |
| keterangan | text | NULL | Detail aktivitas |
| ip_address | varchar(45) | NULL | |
| user_agent | text | NULL | |
| created_at | timestamp | NULL | |
| updated_at | timestamp | NULL | |

Data aktual: 39 record — 35 Login, 2 Create, 2 Update, 1 Delete

### 3.5.2 Relasi Antar Tabel

```
users (1) ----[created_by]----> (M) aset
users (1) ----[updated_by]----> (M) aset
users (1) ----[user_id]-------> (M) log_aktivitas  [SET NULL on delete]
barang (1) --[RESTRICT del]---> (M) aset  [kode_barang FK]
ruangan (1) -[SET NULL del]---> (M) aset  [ruangan_id FK]
```

**FK Constraints aktual dari SQL dump:**
```sql
CONSTRAINT fk_aset_barang
  FOREIGN KEY (kode_barang) REFERENCES barang(kode_barang)
  ON DELETE RESTRICT ON UPDATE CASCADE,

CONSTRAINT fk_aset_ruangan
  FOREIGN KEY (ruangan_id) REFERENCES ruangan(id)
  ON DELETE SET NULL ON UPDATE CASCADE
```

**Index yang ada di tabel aset:**
```sql
PRIMARY KEY (kode_aset)
KEY idx_kode_barang (kode_barang)
KEY idx_ruangan_id (ruangan_id)
KEY idx_status (status)
```

---

## 3.6 Arsitektur Sistem

SimAset menggunakan arsitektur **Client-Server berbasis web** dengan pola **MVC (Model-View-Controller)**.

```
+------------------------------------------------------------------+
|                        CLIENT LAYER                              |
|  Browser (Chrome/Firefox/Edge/Safari)                            |
|  Blade Templates + Tailwind CSS + Alpine.js + Chart.js           |
+------------------------------------------------------------------+
                    | HTTP Request/Response
                    v
+------------------------------------------------------------------+
|                        SERVER LAYER                              |
|  Laravel 12 (PHP 8.5.2) — Apache/Nginx                          |
|                                                                  |
|  routes/web.php + routes/auth.php                               |
|       |                                                          |
|       v                                                          |
|  Middleware Stack:                                               |
|    SecurityHeaders (semua request)                               |
|    auth (semua route authenticated)                              |
|    role:admin (users, audit-log)                                 |
|    LogActivity (terminate phase)                                 |
|       |                                                          |
|       v                                                          |
|  Controllers (13 controller):                                    |
|    DashboardController, AssetController, BarangController        |
|    RuanganController, QrCodeController, MaintenanceController    |
|    LaporanController, ExportController, ImportController         |
|    UserController, AuditLogController, ProfileController         |
|    Auth/* (8 controller Breeze)                                  |
|       |                                                          |
|       v                                                          |
|  Models (Eloquent ORM):                                          |
|    Asset, Barang, Ruangan, User, ActivityLog                     |
|       |                                                          |
|       v                                                          |
|  Helpers: ActivityLogger, ImageHelper                            |
|  Exports: AssetExportFile, BarangExportFile                      |
|  Imports: AssetImport                                            |
|  Mail: AkunBaruMail, MaintenanceAlert                            |
+------------------------------------------------------------------+
                    | Eloquent ORM (PDO)
                    v
+------------------------------------------------------------------+
|                      DATABASE LAYER                              |
|  MySQL 8.0.30 — Database: simset_rbtv                            |
|  Tabel: users, barang, ruangan, aset, log_aktivitas, sessions    |
+------------------------------------------------------------------+
                    |
                    v
+------------------------------------------------------------------+
|                    EXTERNAL SERVICES                             |
|  qrserver.com API — Generate QR code PNG                         |
|  SMTP Server (Gmail/lainnya) — Email notifikasi                  |
+------------------------------------------------------------------+
```

> **[GAMBAR 3.9: Diagram arsitektur sistem SimAset lengkap dengan semua layer dan komponen]**

### 3.6.1 Daftar Route Lengkap

Semua route didefinisikan di `routes/web.php`:

| Method | URL | Controller | Nama Route | Akses |
|--------|-----|------------|------------|-------|
| GET | / | redirect | - | Publik |
| GET | /login | AuthenticatedSessionController@create | login | Guest |
| POST | /login | AuthenticatedSessionController@store | - | Guest |
| POST | /logout | closure | logout | Auth |
| GET | /dashboard | DashboardController@index | dashboard | Auth |
| GET | /profile | ProfileController@edit | profile.edit | Auth |
| PATCH | /profile | ProfileController@update | profile.update | Auth |
| DELETE | /profile | ProfileController@destroy | profile.destroy | Auth |
| GET | /aset | AssetController@index | aset.index | Auth |
| GET | /aset/create | AssetController@create | aset.create | Auth |
| POST | /aset | AssetController@store | aset.store | Auth |
| GET | /aset/{kode} | AssetController@show | aset.show | Auth |
| GET | /aset/{kode}/edit | AssetController@edit | aset.edit | Auth |
| PUT | /aset/{kode} | AssetController@update | aset.update | Auth |
| DELETE | /aset/{kode} | AssetController@destroy | aset.destroy | Auth |
| POST | /aset/batch-destroy | AssetController@batchDestroy | aset.batch-destroy | Auth |
| POST | /aset/{kode}/generate-qr | AssetController@generateQr | aset.generateQr | Auth |
| GET | /aset/{kode}/qr | AssetController@showQr | aset.showQr | Auth |
| GET | /aset/{kode}/detail | AssetController@detail | assets.detail | **Publik** |
| GET | /barang | BarangController@index | barang.index | Auth |
| GET | /barang/create | BarangController@create | barang.create | Auth |
| POST | /barang | BarangController@store | barang.store | Auth |
| GET | /barang/{kode} | BarangController@show | barang.show | Auth |
| GET | /barang/{kode}/edit | BarangController@edit | barang.edit | Auth |
| PUT | /barang/{kode} | BarangController@update | barang.update | Auth |
| DELETE | /barang/{kode} | BarangController@destroy | barang.destroy | Auth |
| GET | /ruangan | RuanganController@index | ruangan.index | Auth |
| GET | /ruangan/create | RuanganController@create | ruangan.create | Auth |
| POST | /ruangan | RuanganController@store | ruangan.store | Auth |
| GET | /ruangan/{id} | RuanganController@show | ruangan.show | Auth |
| GET | /ruangan/{id}/edit | RuanganController@edit | ruangan.edit | Auth |
| PUT | /ruangan/{id} | RuanganController@update | ruangan.update | Auth |
| DELETE | /ruangan/{id} | RuanganController@destroy | ruangan.destroy | Auth |
| GET | /qrcode/scanner | QrCodeController@scanner | qrcode.scanner | Auth |
| GET | /qrcode/search | QrCodeController@search | qrcode.search | Auth |
| GET | /qrcode/batch-print | QrCodeController@batchPrint | qrcode.batch-print | Auth |
| GET | /qrcode/{kode}/download | QrCodeController@download | qrcode.download | Auth |
| GET | /maintenance | MaintenanceController@index | maintenance.index | Auth |
| POST | /maintenance/{kode}/set | MaintenanceController@setMaintenance | maintenance.set | Auth |
| PATCH | /maintenance/{kode}/complete | MaintenanceController@complete | maintenance.complete | Auth |
| GET | /import/aset | ImportController@createAset | import.aset | Auth |
| GET | /import/barang | ImportController@createBarang | import.barang | Auth |
| POST | /import | ImportController@store | import.store | Auth |
| GET | /import/template | ImportController@template | import.template | Auth |
| GET | /export/aset | ExportController@indexAset | export.aset | Auth |
| GET | /export/aset/excel | ExportController@excelAset | export.aset.excel | Auth |
| GET | /export/aset/pdf | ExportController@pdfAset | export.aset.pdf | Auth |
| GET | /export/barang | ExportController@indexBarang | export.barang | Auth |
| GET | /export/barang/excel | ExportController@excelBarang | export.barang.excel | Auth |
| GET | /export/barang/pdf | ExportController@pdfBarang | export.barang.pdf | Auth |
| GET | /laporan | LaporanController@index | laporan.index | Auth |
| GET | /laporan/assets | LaporanController@aset | laporan.aset | Auth |
| GET | /laporan/assets/cetak | LaporanController@cetakAset | laporan.aset.cetak | Auth |
| GET | /laporan/assets/export | LaporanController@exportAset | laporan.aset.export | Auth |
| GET | /laporan/ruangan/{id} | LaporanController@laporanRuangan | laporan.ruangan | Auth |
| GET | /laporan/maintenance/pdf | LaporanController@exportMaintenancePdf | laporan.maintenance.pdf | Auth |
| GET | /laporan/maintenance/csv | LaporanController@exportMaintenanceCsv | laporan.maintenance.csv | Auth |
| GET | /users | UserController@index | users.index | **Admin** |
| GET | /users/create | UserController@create | users.create | **Admin** |
| POST | /users | UserController@store | users.store | **Admin** |
| GET | /users/{id}/edit | UserController@edit | users.edit | **Admin** |
| PUT | /users/{id} | UserController@update | users.update | **Admin** |
| DELETE | /users/{id} | UserController@destroy | users.destroy | **Admin** |
| GET | /audit-log | AuditLogController@index | audit-log.index | **Admin** |


---

## 3.7 Perancangan Antarmuka Pengguna (UI/UX)

### 3.7.1 Layout Utama (layouts/app.blade.php)

Semua halaman authenticated menggunakan layout utama yang terdiri dari:

```
+----------------------------------------------------------+
|  SIDEBAR (280px, fixed, gradient biru #1a3470→#1e45b8)  |
|  +----------------------------------------------------+  |
|  | Logo SimAset + Logo RBTV                          |  |
|  | Badge role: [Administrator] atau [Staff]          |  |
|  +----------------------------------------------------+  |
|  | MENU NAVIGASI:                                    |  |
|  |  Dashboard                                        |  |
|  |  -- Data Master --                                |  |
|  |  > Master Data (dropdown)                         |  |
|  |    - Aset                                         |  |
|  |    - Barang                                       |  |
|  |    - Ruangan                                      |  |
|  |  -- Operasional --                                |  |
|  |  QR Scanner                                       |  |
|  |  Maintenance [badge kuning jika ada]              |  |
|  |  -- Data & Laporan --                             |  |
|  |  Laporan & Export                                 |  |
|  |  -- Administrasi (Admin only) --                  |  |
|  |  Kelola Pengguna                                  |  |
|  |  Log Aktivitas                                    |  |
|  +----------------------------------------------------+  |
|  | Footer: RBTV Bengkulu | SimAset v1.0              |  |
|  | [Tombol Logout merah]                             |  |
|  +----------------------------------------------------+  |
+----------------------------------------------------------+

+----------------------------------------------------------+
|  MAIN CONTENT (margin-left: 280px di desktop)            |
|  +----------------------------------------------------+  |
|  | HEADER (sticky, height 64px):                     |  |
|  |  [Hamburger] [Judul Halaman] [User Dropdown]      |  |
|  +----------------------------------------------------+  |
|  |                                                    |  |
|  |  CONTENT AREA (padding 24px 28px 32px)            |  |
|  |  @yield('content')                                |  |
|  |                                                    |  |
|  +----------------------------------------------------+  |
|  | FOOTER: SimAset — RBTV | v1.0 | © 2026           |  |
|  +----------------------------------------------------+  |
+----------------------------------------------------------+
```

> **[GAMBAR 3.10: Tampilan layout utama SimAset dengan sidebar navigasi biru, header sticky, dan area konten]**

**Fitur responsif layout:**
- Desktop (≥1024px): sidebar selalu tampil, hamburger tersembunyi
- Tablet/Mobile (<1024px): sidebar tersembunyi, hamburger tampil, sidebar muncul sebagai overlay
- Sidebar overlay menggunakan `transform: translateX(-100%)` → `translateX(0)` dengan transisi 0.3s

**Teknologi frontend yang digunakan:**
- Bootstrap 5.3.3 (CDN) — grid, komponen, modal
- Font Awesome 6.4.0 (CDN) — ikon
- Inter font (Google Fonts) — tipografi
- SweetAlert2 (CDN) — dialog konfirmasi hapus
- Chart.js (CDN) — grafik di dashboard
- Alpine.js 3.x (npm) — interaktivitas ringan
- Tailwind CSS 3.x (npm, via Vite) — utility classes
- Bootstrap 5 collapse — dropdown sidebar

### 3.7.2 Halaman Login (auth/login.blade.php)

Halaman login menggunakan layout dua kolom khusus (bukan layout utama):

```
+------------------------+------------------+
|   LEFT PANEL           |   RIGHT PANEL    |
|   (gradient biru tua)  |   (putih, 500px) |
|                        |                  |
|  Logo SimAset + RBTV   |  Logo SimAset    |
|                        |  + Logo RBTV     |
|  "Kelola Aset Kantor   |                  |
|   dengan Lebih Mudah"  |  "Masuk ke       |
|                        |   Sistem"        |
|  Fitur-fitur:          |                  |
|  - Manajemen aset      |  [Email input]   |
|  - QR Code             |  [Password input]|
|  - Laporan PDF/Excel   |  [Ingat Saya]    |
|  - Audit trail         |  [Lupa Password?]|
|                        |  [Masuk →]       |
|  © 2026 RBTV           |                  |
+------------------------+------------------+
```

> **[GAMBAR 3.11: Tampilan halaman login SimAset dengan panel kiri biru dan panel kanan form login]**

**Fitur keamanan login:**
- Rate limiting: 5 percobaan gagal per menit per email+IP
- Session regeneration setelah login berhasil
- CSRF token di setiap form
- Toggle show/hide password

### 3.7.3 Halaman Dashboard (dashboard.blade.php)

```
+----------------------------------------------------------+
|  HERO: "Selamat Datang, Admin Magang! 👋"               |
|  [Badge tanggal hari ini]                                |
+----------------------------------------------------------+
|  [ALERT MAINTENANCE] jika ada aset maintenance           |
|  "1 Aset Sedang Maintenance → [Lihat]"                  |
+----------------------------------------------------------+
|  METRIC CARDS (6 kartu, grid auto-fit min 200px):        |
|  [Total Aset: 2]  [Aktif: 1]  [Maintenance: 1]          |
|  [Rusak: 0]       [Non-Aktif: 0]  [Ruangan: 4]          |
+----------------------------------------------------------+
|  CHARTS ROW:                                             |
|  [Donut: Distribusi Kondisi]  [Bar: Top 5 Kategori]     |
+----------------------------------------------------------+
|  BOTTOM ROW:                                             |
|  [Tabel Recent Assets]  [Aktivitas Terbaru + Quick Links]|
+----------------------------------------------------------+
```

> **[GAMBAR 3.12: Tampilan dashboard SimAset dengan metric cards, chart distribusi kondisi, dan tabel aset terbaru]**

### 3.7.4 Halaman Daftar Aset (aset/index.blade.php)

```
+----------------------------------------------------------+
|  HERO: "Kelola Aset" [Export] [Import] [+ Tambah Aset]  |
+----------------------------------------------------------+
|  STATS (4 kartu): Total | Aktif | Maintenance | Non-Aktif|
+----------------------------------------------------------+
|  FILTER BAR:                                             |
|  [Search...] [Status▼] [Kondisi▼] [Kategori▼] [Cari]   |
+----------------------------------------------------------+
|  BULK ACTION BAR (muncul saat ada yang dicentang):       |
|  "X aset dipilih" [Cetak QR] [Hapus Terpilih]           |
+----------------------------------------------------------+
|  TABEL DATA:                                             |
|  ☐ | Foto | Kode | Nama Barang | Kategori | Ruangan |   |
|    | Tgl  | Jml  | Kondisi     | Status   | Aksi    |   |
|  ☐ | 📷  | AST-001 | Kamera Sony A7 | Kamera | Ruang Editing |
|    | 01 Mei 2026 | 1 | Baik | [Maintenance] | 👁✏🔲🗑 |
|  ☐ | 📷  | AST-002 | Kamera Sony A7 | Kamera | Ruang Editing |
|    | 01 Mei 2026 | 1 | Baik | [Aktif]       | 👁✏🔲🗑 |
+----------------------------------------------------------+
|  Menampilkan 1-2 dari 2 data  |  < 1 >                  |
+----------------------------------------------------------+
```

> **[GAMBAR 3.13: Tampilan halaman daftar aset dengan filter bar, tabel data AST-001 (Maintenance) dan AST-002 (Aktif)]**

### 3.7.5 Halaman Form Tambah/Edit Aset

Form dibagi menjadi 4 card section:

```
+----------------------------------------------------------+
|  CARD 1: Informasi Barang                                |
|  [Dropdown Barang*] [Serial Number]                      |
+----------------------------------------------------------+
|  CARD 2: Lokasi & Waktu                                  |
|  [Dropdown Ruangan*] [Tanggal Perolehan*]                |
|  [Harga Perolehan Rp] [Sumber Perolehan▼]               |
+----------------------------------------------------------+
|  CARD 3: Kondisi & Status                                |
|  [Kondisi*▼] [Status*▼] [Jumlah]                        |
|  [Keterangan textarea]                                   |
+----------------------------------------------------------+
|  CARD 4: Foto Aset (Opsional)                            |
|  [Upload file] [Preview foto]                            |
+----------------------------------------------------------+
|  [Batal] [Simpan Aset]                                   |
+----------------------------------------------------------+
```

> **[GAMBAR 3.14: Tampilan form tambah aset baru dengan 4 section card dan preview foto]**

### 3.7.6 Halaman Detail Aset (aset/show.blade.php)

```
+----------------------------------------------------------+
|  HERO: "Kamera Sony A7 [AST-001]"                       |
|  Kamera · Ruang Editing  [Edit] [Kembali]               |
+----------------------------------------------------------+
|  KOLOM KIRI (8/12):          | KOLOM KANAN (4/12):      |
|  Card: Informasi Aset        | Card: Foto Aset           |
|  - Kode Aset: AST-001        | [foto atau placeholder]   |
|  - Kode Barang: BRG-001      |                           |
|  - Nama: Kamera Sony A7      | Card: QR Code             |
|  - Kategori: Kamera          | [QR image atau generate]  |
|  - Serial: ggG               | [Download] [Cetak] [Label]|
|  - Ruangan: Ruang Editing    |                           |
|  - Tgl Perolehan: 01 Mei 2026| Card: Informasi Sistem    |
|  - Harga: —                  | - Dibuat: 01 Mei 2026     |
|  - Kondisi: [Baik]           | - Diperbarui: 02 Mei 2026 |
|  - Status: [Maintenance]     | - Dibuat Oleh: Admin Magang|
|  - Jumlah: 1 unit            |                           |
|                              | Card: Aksi Cepat          |
|                              | [Edit] [Hapus] [Kembali]  |
+----------------------------------------------------------+
```

> **[GAMBAR 3.15: Tampilan halaman detail aset AST-001 (Kamera Sony A7) dengan badge Maintenance merah]**

### 3.7.7 Halaman Maintenance (maintenance/index.blade.php)

```
+----------------------------------------------------------+
|  HERO (gradient coklat/amber): "Manajemen Maintenance"  |
+----------------------------------------------------------+
|  STATS (4 kartu):                                        |
|  [Total Maintenance: 1] [Rusak Berat: 0]                |
|  [Rusak Ringan: 0]      [Total Bermasalah: 0]           |
+----------------------------------------------------------+
|  FILTER: [Search] [Kondisi▼] [Cari]                     |
+----------------------------------------------------------+
|  TABEL:                                                  |
|  # | Kode | Nama Barang | Ruangan | Kondisi | Ket | Aksi|
|  1 | AST-001 | Kamera Sony A7 | Ruang Editing | Baik | — |
|    |         |                |               |      | [👁] [✓ Selesai] |
+----------------------------------------------------------+
```

> **[GAMBAR 3.16: Tampilan dashboard maintenance menampilkan AST-001 dengan tombol Selesai]**

**Modal Selesaikan Maintenance:**
```
+------------------------------------------+
|  Selesaikan Maintenance                  |
|  Tandai maintenance aset Kamera Sony A7  |
|  (AST-001) sebagai selesai.              |
|                                          |
|  Kondisi Setelah Maintenance*:           |
|  [Baik ▼]                               |
|                                          |
|  Catatan (opsional):                     |
|  [textarea]                              |
|                                          |
|  [Batal]  [✓ Konfirmasi Selesai]        |
+------------------------------------------+
```

> **[GAMBAR 3.17: Modal konfirmasi selesaikan maintenance dengan pilihan kondisi akhir]**

### 3.7.8 Halaman QR Scanner (qrcode/scanner.blade.php)

```
+----------------------------------------------------------+
|  KOLOM KIRI: Area Pindai                                 |
|  +--------------------------------------------------+    |
|  | [Video kamera / placeholder]                    |    |
|  | [Scan frame + scan line animasi]                |    |
|  +--------------------------------------------------+    |
|  | [Buka Kamera] [Hentikan]                        |    |
|  | ---- ATAU ----                                  |    |
|  | Upload Foto QR Code: [input file]               |    |
|  | ---- ATAU ----                                  |    |
|  | Kode Manual: [input] [Cari]                     |    |
+----------------------------------------------------------+
|  KOLOM KANAN: Hasil Pencarian                            |
|  [Belum Ada Hasil / Loading / Hasil Ditemukan]           |
|  Jika ditemukan:                                         |
|  - Kode Aset: AST-001                                   |
|  - Nama: Kamera Sony A7                                  |
|  - Ruangan: Ruang Editing                               |
|  - Status: [Maintenance]                                 |
|  [Lihat Detail Lengkap →]                               |
+----------------------------------------------------------+
```

> **[GAMBAR 3.18: Tampilan halaman QR Scanner dengan area kamera dan panel hasil pencarian]**

### 3.7.9 Halaman Import (import/aset-import.blade.php)

```
+----------------------------------------------------------+
|  KOLOM KIRI: Upload File                                 |
|  1. Pilih Jenis Data: [Data Aset] [Master Barang]       |
|  2. Upload File: [drag & drop zone]                     |
|     Format: .xlsx, .xls, .csv                           |
|  [Proses Import]                                        |
|  Download Template: [Template Aset] [Template Barang]   |
+----------------------------------------------------------+
|  KOLOM KANAN: Struktur File                              |
|  Tabel format kolom A-I (untuk aset):                   |
|  A: Kode Barang [Wajib]                                 |
|  B: Nama Ruangan [Opsional]                             |
|  C: Kondisi [Opsional]                                  |
|  D: Status [Opsional]                                   |
|  E: Jumlah [Opsional]                                   |
|  F: Tanggal Perolehan [Opsional]                        |
|  G: Harga Perolehan [Opsional]                          |
|  H: Sumber Perolehan [Opsional]                         |
|  I: Keterangan [Opsional]                               |
+----------------------------------------------------------+
```

> **[GAMBAR 3.19: Tampilan halaman import data dengan drag-drop zone dan tabel format kolom]**

### 3.7.10 Halaman Laporan (laporan/index.blade.php)

```
+----------------------------------------------------------+
|  LAPORAN ASET                                            |
|  [Laporan Aset Lengkap: Lihat | PDF | CSV]              |
|  [Export Aset Excel: Filter & Export | Download Semua]  |
|  [Export Aset PDF: Filter & Export | Cetak PDF]         |
+----------------------------------------------------------+
|  LAPORAN MASTER BARANG                                   |
|  [Export Barang Excel] [Export Barang PDF]              |
+----------------------------------------------------------+
|  LAPORAN PER RUANGAN                                     |
|  [Studio 1: Tidak ada aset]                             |
|  [Studio 2: Tidak ada aset]                             |
|  [Ruang Editing: 2 aset → Cetak PDF]                   |
|  [Ruang Redaksi: 0 aset]                               |
+----------------------------------------------------------+
|  LAPORAN MAINTENANCE                                     |
|  [Cetak PDF] [Export CSV]                               |
+----------------------------------------------------------+
|  IMPORT DATA                                             |
|  [Import Aset] [Import Barang]                          |
+----------------------------------------------------------+
```

> **[GAMBAR 3.20: Tampilan halaman laporan & export dengan card per kategori laporan]**

### 3.7.11 Halaman Audit Log (audit_log/index.blade.php)

```
+----------------------------------------------------------+
|  FILTER: [Search] [Pengguna▼] [Aktivitas▼] [Cari]      |
+----------------------------------------------------------+
|  TABEL (20 per halaman, terbaru di atas):               |
|  # | Waktu | Pengguna | Aktivitas | Deskripsi | IP      |
|  1 | 13:03 | [Admin Magang] | [Login] | User berhasil login... | 127.0.0.1 |
|  2 | 07:42 | [Admin Magang] | [Update] | Mengupdate aset: Kamera Sony A7 (AST-001) | |
|  3 | 08:19 | [Admin Magang] | [Delete] | Menghapus aset: printer epson l200 (AST-003) | |
+----------------------------------------------------------+
```

Badge warna aktivitas:
- Login: hijau (#ECFDF5)
- Logout: kuning (#FFFBEB)
- Create: biru muda (#ECFEFF)
- Update: biru (#EFF6FF)
- Delete: merah (#FEF2F2)

> **[GAMBAR 3.21: Tampilan halaman audit log dengan 39 record aktivitas dan badge warna per jenis aktivitas]**

### 3.7.12 Halaman Kelola Pengguna (users/index.blade.php)

```
+----------------------------------------------------------+
|  STATS: [Total: 3] [Admin: 1] [Staff: 2]               |
+----------------------------------------------------------+
|  TABEL:                                                  |
|  # | Pengguna | Role | Status | Terdaftar | Login Terakhir | Aksi |
|  1 | [AM] Admin Magang | [Admin] | [Aktif] | 29 Apr 2026 | 02 Mei 2026 | ✏ |
|  2 | [SR] Staff RBTV   | [Staff] | [Aktif] | 29 Apr 2026 | Belum pernah | ✏🗑 |
|  3 | [R]  reffki       | [Staff] | [Aktif] | 02 Mei 2026 | 02 Mei 2026 | ✏🗑 |
+----------------------------------------------------------+
```

> **[GAMBAR 3.22: Tampilan halaman kelola pengguna dengan 3 user aktual dan avatar inisial berwarna]**

### 3.7.13 Komponen Blade yang Digunakan

| Komponen | File | Fungsi |
|----------|------|--------|
| saas-card | components/saas-card.blade.php | Card dengan header, body, footer |
| saas-table | components/saas-table.blade.php | Tabel responsif standar |
| modal | components/modal.blade.php | Dialog modal Alpine.js |
| input-error | components/input-error.blade.php | Pesan error form |
| input-label | components/input-label.blade.php | Label form |
| text-input | components/text-input.blade.php | Input text standar |
| primary-button | components/primary-button.blade.php | Tombol aksi utama |
| secondary-button | components/secondary-button.blade.php | Tombol sekunder |
| danger-button | components/danger-button.blade.php | Tombol hapus |
| page-styles | components/page-styles.blade.php | CSS untuk halaman daftar |
| form-styles | components/form-styles.blade.php | CSS untuk halaman form |

### 3.7.14 Status Badge dan Pill

Sistem menggunakan CSS class konsisten untuk status:

| Status | Class | Warna |
|--------|-------|-------|
| Aktif | pill-aktif | Hijau (#ECFDF5, #059669) |
| Maintenance | pill-maintenance | Kuning (#FFFBEB, #D97706) |
| Non-Aktif | pill-nonaktif | Abu (#F9FAFB, #6B7280) |
| Baik | pill-baik | Hijau muda |
| Rusak Ringan | pill-rusak-r | Oranye |
| Rusak Berat | pill-rusak-b | Merah |

---

## 3.8 Kesimpulan Modul

Modul 3 ini telah merancang sistem SimAset secara menyeluruh dan komprehensif. Use Case Diagram menggambarkan perbedaan hak akses Admin dan Staff. Empat Activity Diagram menjelaskan alur proses bisnis utama. Tiga Sequence Diagram menggambarkan urutan interaksi antar komponen.

Perancangan basis data menggunakan data aktual dari database `simset_rbtv` — setiap tabel dijelaskan dengan DDL yang tepat, constraint FK aktual, dan contoh data nyata. Arsitektur sistem Client-Server MVC digambarkan lengkap dengan 13 controller dan semua route. Perancangan UI/UX mencakup semua 13+ halaman dengan wireframe ASCII yang detail.

---

*Kembali ke: [Modul 2 — Analisis Kebutuhan](MODUL_02_ANALISIS_KEBUTUHAN.md)*
*Lanjut ke: [Modul 4 — Persiapan Lingkungan](MODUL_04_PERSIAPAN_LINGKUNGAN.md)*
