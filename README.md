# SimAset — Sistem Informasi Manajemen Aset
### Rakyat Bengkulu Televisi (RBTV)

> Aplikasi web berbasis Laravel 12 untuk mengelola aset barang kantor RBTV Bengkulu secara digital, terpusat, dan terdokumentasi.

---

## Daftar Isi

- [Tentang Aplikasi](#tentang-aplikasi)
- [Fitur Utama](#fitur-utama)
- [Tech Stack](#tech-stack)
- [Struktur Database](#struktur-database)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi Lokal](#instalasi-lokal)
- [Konfigurasi Environment](#konfigurasi-environment)
- [Akun Default](#akun-default)
- [Struktur Proyek](#struktur-proyek)
- [Panduan Fitur](#panduan-fitur)
- [Deployment](#deployment)
- [Keamanan](#keamanan)
- [Kontribusi](#kontribusi)

---

## Tentang Aplikasi

SimAset adalah sistem informasi manajemen aset yang dikembangkan sebagai proyek Kerja Praktik (KP) Teknik Informatika Universitas Bengkulu tahun 2026. Sistem ini dirancang untuk menggantikan pencatatan aset manual di RBTV Bengkulu dengan solusi digital yang mencakup:

- Pencatatan dan pelacakan aset secara real-time
- Manajemen siklus hidup aset (aktif → maintenance → non-aktif)
- Identifikasi aset via QR Code
- Pelaporan dan ekspor data dalam berbagai format
- Audit trail seluruh aktivitas pengguna

---

## Fitur Utama

### Manajemen Aset
- CRUD lengkap dengan kode aset otomatis (`AST-001`, `AST-002`, dst.)
- Upload foto aset (JPEG, PNG, GIF, maks. 2 MB)
- Filter multi-kriteria: status, kondisi, kategori, ruangan, pencarian teks
- Batch delete (hapus banyak aset sekaligus)
- Soft validation serial number (unik per aset)
- Tiga status aset: **Aktif**, **Maintenance**, **Non-Aktif**
- Tiga kondisi aset: **Baik**, **Rusak Ringan**, **Rusak Berat**

### Manajemen Barang & Ruangan (Master Data)
- CRUD data barang dengan kategori dan jumlah stok
- CRUD data ruangan dengan informasi lantai
- Relasi barang → aset dan ruangan → aset

### QR Code
- Generate QR Code per aset (via API qrserver.com)
- Download & cetak QR Code satu aset
- Batch print QR Code untuk banyak aset sekaligus
- Scanner QR Code berbasis kamera browser (real-time)
- QR Code mengarah ke halaman detail aset

### Maintenance
- Tandai aset masuk maintenance dari halaman detail
- Daftar semua aset dalam status maintenance
- Tandai maintenance selesai dengan update kondisi
- Notifikasi email otomatis ke semua admin saat maintenance selesai

### Import & Export
- **Import** data aset dan barang dari file Excel (`.xlsx`, `.xls`) atau CSV
- Template CSV tersedia untuk diunduh
- Validasi baris per baris dengan laporan error detail
- **Export** aset ke Excel (`.xlsx`) dan PDF dengan filter aktif
- **Export** barang ke Excel dan PDF
- **Export** laporan maintenance ke PDF dan CSV
- **Laporan per ruangan** dalam format PDF

### Laporan
- Laporan aset dengan filter: ruangan, kondisi, status, periode tanggal
- Laporan per ruangan (PDF)
- Laporan maintenance (PDF & CSV)
- Header laporan otomatis: nama pencetak, tanggal, periode

### Audit Log
- Pencatatan otomatis setiap aktivitas: login, logout, CRUD aset, maintenance
- Tampilan log dengan filter pengguna dan aksi
- Informasi: pengguna, aktivitas, IP address, waktu

### Manajemen Pengguna (Admin Only)
- CRUD pengguna dengan dua role: **Admin** dan **Staff**
- Validasi password: min. 8 karakter, huruf besar, huruf kecil, angka
- Kirim notifikasi email akun baru (opsional)
- Reset password dengan link via email

### Dashboard
- Statistik ringkas: total aset, aktif, maintenance, non-aktif, rusak
- Grafik distribusi kondisi aset (Chart.js)
- Grafik distribusi kategori aset (top 5)
- Tabel aset terbaru dan log aktivitas terkini
- Counter aset yang ditambahkan bulan ini

---

## Tech Stack

| Layer | Teknologi |
|---|---|
| Backend | Laravel 12 (PHP 8.2+) |
| Frontend | Bootstrap 5 + Blade Templates |
| Database | MySQL / SQLite |
| Autentikasi | Laravel Breeze (session-based) |
| Export Excel | Maatwebsite Excel 3.1 |
| Export PDF | barryvdh/laravel-dompdf 3.1 |
| QR Code | SimpleSoftwareIO QR Code 4.2 |
| Image Processing | Intervention Image 4.0 |
| Charts | Chart.js (CDN) |
| Build Tool | Vite |

---

## Struktur Database

```
users
├── id_user (PK, auto increment)
├── nama
├── email (unique)
├── password_hash
├── role (admin | staff)
└── timestamps

barang
├── kode_barang (PK, e.g. BRG-001)
├── nama_barang
├── kategori
├── jumlah
├── keterangan
└── timestamps

ruangan
├── kode_ruangan (PK, e.g. RNG-001)
├── nama_ruangan
├── lantai
├── keterangan
└── timestamps

aset
├── kode_aset (PK, e.g. AST-001)
├── kode_barang (FK → barang)
├── kode_ruangan (FK → ruangan)
├── id_user (FK → users)
├── serial_number (unique, nullable)
├── kondisi (Baik | Rusak Ringan | Rusak Berat)
├── status (Aktif | Maintenance | Non-Aktif)
├── harga (decimal 15,2)
├── keterangan
├── foto (filename)
└── timestamps

log_aktivitas
├── id_log (PK, auto increment)
├── id_user (FK → users)
├── aktivitas
├── ip_address
├── keterangan
└── created_at
```

---

## Persyaratan Sistem

- PHP >= 8.2 dengan ekstensi: `pdo`, `pdo_mysql` (atau `pdo_sqlite`), `zip`, `gd`
- Composer >= 2.x
- Node.js >= 18.x & npm
- MySQL 8.x / MariaDB 10.x (atau SQLite untuk development)
- Web server: Apache / Nginx / PHP built-in server

---

## Instalasi Lokal

### 1. Clone repositori

```bash
git clone https://github.com/your-org/simaset.git
cd simaset
```

### 2. Install dependensi

```bash
composer install
npm install && npm run build
```

### 3. Setup environment

```bash
cp .env.example .env
php artisan key:generate
```

### 4. Konfigurasi database

Edit file `.env` sesuai database yang digunakan:

**SQLite (development cepat):**
```env
DB_CONNECTION=sqlite
# Biarkan DB_HOST, DB_DATABASE, dll. dikomentari
```

Buat file database SQLite:
```bash
touch database/database.sqlite
```

**MySQL:**
```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=simaset
DB_USERNAME=root
DB_PASSWORD=your_password
```

### 5. Jalankan migrasi dan seeder

```bash
# Migrasi + seed data awal (admin, staff, barang contoh)
php artisan migrate --seed

# Atau hanya migrasi tanpa seed
php artisan migrate
```

### 6. Jalankan server

```bash
php artisan serve
```

Akses aplikasi di: `http://localhost:8000`

### Setup Cepat (satu perintah)

```bash
composer run setup
```

Perintah ini menjalankan: `composer install` → copy `.env` → `key:generate` → `migrate` → `npm install` → `npm run build`.

---

## Konfigurasi Environment

### Variabel Penting

```env
APP_NAME=SimAset
APP_ENV=local          # Ganti ke 'production' saat deploy
APP_DEBUG=true         # Ganti ke 'false' saat production
APP_URL=http://localhost

DB_CONNECTION=sqlite   # atau mysql

SESSION_DRIVER=database
QUEUE_CONNECTION=database
CACHE_STORE=database
```

### Konfigurasi Mail (Notifikasi)

Default menggunakan `log` driver (email ditulis ke log file, tidak dikirim).

Untuk production dengan Gmail:
```env
MAIL_MAILER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your@gmail.com
MAIL_PASSWORD=your_app_password   # Gunakan App Password, bukan password akun
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=noreply@rbtv.co.id
MAIL_FROM_NAME="SimAset RBTV"
```

> **Catatan:** Untuk Gmail, aktifkan 2FA lalu buat App Password di pengaturan akun Google.

---

## Akun Default

Setelah menjalankan `php artisan migrate --seed`:

| Role  | Email              | Password  | Akses |
|-------|--------------------|-----------|-------|
| Admin | admin@rbtv.com     | Admin123  | Semua fitur |
| Staff | staff@rbtv.com     | Staff123  | Aset, Barang, Ruangan, QR, Laporan |

> **Penting:** Ganti password default segera setelah instalasi di lingkungan production.

### Perbedaan Hak Akses

| Fitur | Admin | Staff |
|---|:---:|:---:|
| Dashboard | ✅ | ✅ |
| Manajemen Aset (CRUD) | ✅ | ✅ |
| Manajemen Barang (CRUD) | ✅ | ✅ |
| Manajemen Ruangan (CRUD) | ✅ | ✅ |
| QR Code & Scanner | ✅ | ✅ |
| Maintenance | ✅ | ✅ |
| Import & Export | ✅ | ✅ |
| Laporan | ✅ | ✅ |
| Audit Log | ✅ | ❌ |
| Manajemen Pengguna | ✅ | ❌ |

---

## Struktur Proyek

```
simaset/
├── app/
│   ├── Exports/            # Kelas export Excel (Aset, Barang)
│   ├── Helpers/            # ActivityLogger
│   ├── Http/
│   │   ├── Controllers/    # AssetController, MaintenanceController, dll.
│   │   ├── Middleware/     # RoleMiddleware, SecurityHeaders, LogActivity
│   │   └── Requests/       # Form request validation
│   ├── Imports/            # AssetImport
│   ├── Mail/               # AkunBaruMail, MaintenanceAlert
│   ├── Models/             # Asset, Barang, Ruangan, User, ActivityLog
│   └── Providers/
├── database/
│   ├── migrations/         # Skema database
│   └── seeders/            # AdminSeeder, StaffSeeder, BarangSeeder
├── docs/
│   └── diagrams/           # ERD, Use Case, Activity, Sequence diagrams
├── resources/
│   └── views/              # Blade templates
├── routes/
│   └── web.php             # Definisi route
├── public/
│   ├── foto_aset/          # Upload foto aset (auto-created)
│   └── qr_codes/           # File QR Code (auto-created)
├── .env.example
├── composer.json
└── Dockerfile
```

---

## Panduan Fitur

### Import Data Aset dari Excel/CSV

1. Unduh template: **Import → Download Template CSV**
2. Isi data sesuai kolom:

| Kolom | Keterangan | Contoh |
|---|---|---|
| Kode Barang | Harus ada di master barang | `BRG-001` |
| Kode Ruangan | Opsional, harus ada di master ruangan | `RNG-001` |
| Kondisi | `Baik` / `Rusak Ringan` / `Rusak Berat` | `Baik` |
| Status | `Aktif` / `Maintenance` / `Non-Aktif` | `Aktif` |
| Serial Number | Opsional, harus unik | `SN-12345` |
| Harga | Angka, tanpa titik ribuan | `5000000` |
| Keterangan | Opsional | `Laptop bagian redaksi` |

3. Upload file → sistem memproses baris per baris dan melaporkan error

### Generate & Cetak QR Code

- **Satu aset:** Halaman detail aset → tombol **Generate QR** → **Download/Cetak**
- **Batch print:** Centang beberapa aset di daftar → **Cetak QR Terpilih** → halaman print otomatis terbuka
- **Scanner:** Menu **QR Scanner** → izinkan akses kamera → arahkan ke QR Code

### Alur Maintenance

```
Aset Aktif
    ↓ (Set Maintenance dari detail aset)
Aset Maintenance
    ↓ (Tandai Selesai + update kondisi)
Aset Aktif  ← notifikasi email ke semua admin
```

---

## Deployment

### Docker

```bash
docker build -t simaset .
docker run -p 10000:10000 \
  -e APP_KEY=your_key \
  -e DB_CONNECTION=mysql \
  -e DB_HOST=your_db_host \
  -e DB_DATABASE=db \
  -e DB_USERNAME=root \
  -e DB_PASSWORD=your_password \
  
```

### Vercel / Shared Hosting

File `.vercelignore` dan `api/index.php` sudah tersedia untuk deployment ke Vercel atau shared hosting berbasis PHP.

Langkah umum untuk shared hosting:
1. Upload semua file ke `public_html` (atau subdirektori)
2. Pastikan `public/` menjadi document root
3. Set variabel environment di panel hosting atau file `.env`
4. Jalankan `php artisan migrate --seed` via SSH atau terminal hosting

### Optimasi Production

```bash
php artisan config:cache
php artisan route:cache
php artisan view:cache
php artisan optimize
```

---

## Keamanan

Aplikasi menerapkan beberapa lapisan keamanan:

- **SecurityHeaders Middleware** — menambahkan header HTTP keamanan (X-Frame-Options, X-Content-Type-Options, CSP, dll.)
- **RoleMiddleware** — pembatasan akses berdasarkan role (admin/staff)
- **CSRF Protection** — semua form dilindungi token CSRF Laravel
- **Input Validation** — validasi ketat di semua form dan request
- **File Upload Security** — ekstensi file dideteksi dari MIME type, bukan nama file (mencegah path traversal)
- **CSV Injection Prevention** — karakter formula (`=`, `+`, `-`, `@`) di awal nilai CSV di-escape
- **Password Policy** — minimal 8 karakter, kombinasi huruf besar, kecil, dan angka
- **Audit Log** — seluruh aktivitas pengguna tercatat dengan IP address

---

## Kontribusi

Proyek ini dikembangkan sebagai bagian dari Kerja Praktik. Untuk pertanyaan atau kontribusi:

1. Fork repositori
2. Buat branch fitur: `git checkout -b feature/nama-fitur`
3. Commit perubahan: `git commit -m "feat: deskripsi singkat"`
4. Push ke branch: `git push origin feature/nama-fitur`
5. Buat Pull Request

---

*SimAset v1.0 — Kerja Praktik Teknik Informatika, Universitas Bengkulu, 2026*
*Dikembangkan untuk Rakyat Bengkulu Televisi (RBTV)*
