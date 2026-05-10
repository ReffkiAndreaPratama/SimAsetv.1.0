# MODUL 4 — PERSIAPAN LINGKUNGAN PENGEMBANGAN
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 4.1 Pendahuluan

Persiapan lingkungan pengembangan adalah tahap yang sering diremehkan namun sangat menentukan kelancaran seluruh proses pengembangan sistem. Lingkungan yang tidak disiapkan dengan benar akan menyebabkan berbagai masalah teknis yang membuang waktu, seperti error konfigurasi yang sulit didiagnosis, kegagalan koneksi database, ketidakcocokan versi library, hingga perbedaan perilaku sistem antara lingkungan development dan production.

Modul ini membahas secara rinci dan langkah demi langkah seluruh proses persiapan lingkungan pengembangan SimAset, mulai dari instalasi perangkat lunak yang diperlukan, konfigurasi environment, migrasi database, hingga pengujian awal untuk memastikan semua komponen berjalan dengan benar sebelum proses implementasi fitur dimulai.

---

## 4.2 Kebutuhan Perangkat Lunak

Sebelum memulai instalasi, pastikan semua perangkat lunak berikut tersedia di komputer pengembang:

### 4.2.1 Perangkat Lunak Wajib

| Perangkat Lunak | Versi Minimum | Versi yang Digunakan | Fungsi |
|-----------------|---------------|----------------------|--------|
| PHP | 8.2 | 8.5.2 | Bahasa pemrograman backend utama |
| Composer | 2.0 | 2.x | Dependency manager untuk PHP |
| Node.js | 18.x | 18.x+ | Runtime JavaScript untuk build frontend |
| NPM | 9.x | 9.x+ | Package manager JavaScript |
| MySQL | 8.0 | 8.0.30 | Database server |
| Git | 2.x | 2.x | Version control |

### 4.2.2 Perangkat Lunak Pendukung (Opsional tapi Direkomendasikan)

| Perangkat Lunak | Fungsi |
|-----------------|--------|
| Laragon (Windows) | Paket all-in-one: Apache + PHP + MySQL + Node.js |
| Visual Studio Code | Code editor dengan ekstensi PHP dan Laravel |
| TablePlus / phpMyAdmin | GUI untuk manajemen database MySQL |
| Postman | Testing API endpoint |
| Browser Chrome/Firefox | Pengujian antarmuka dengan DevTools |

### 4.2.3 Ekstensi PHP yang Harus Aktif

Pastikan ekstensi PHP berikut sudah aktif di `php.ini`:

```ini
extension=pdo
extension=pdo_mysql
extension=pdo_sqlite
extension=mbstring
extension=openssl
extension=tokenizer
extension=xml
extension=ctype
extension=json
extension=bcmath
extension=fileinfo
extension=gd          ; untuk ImageHelper (resize foto aset)
extension=zip         ; untuk export Excel (Maatwebsite)
extension=curl        ; untuk QR code via API eksternal
```

---

## 4.3 Instalasi Web Server Lokal dengan Laragon

Laragon adalah paket development environment modern untuk Windows yang menyertakan Apache, PHP, MySQL, Node.js, npm, dan git dalam satu instalasi yang mudah dikelola. Laragon sangat direkomendasikan karena kemudahan penggunaannya dan dukungan untuk multiple versi PHP.

### 4.3.1 Langkah Instalasi Laragon

**Langkah 1: Download Laragon**

Buka browser dan akses `https://laragon.org/download/`. Pilih versi **Laragon Full** yang mencakup semua komponen yang dibutuhkan (Apache, MySQL, PHP, Node.js, npm, git). Ukuran file sekitar 150-200 MB.

> **[GAMBAR 4.1: Halaman download Laragon di laragon.org dengan pilihan versi Full dan Lite]**

**Langkah 2: Jalankan Installer**

Setelah download selesai, jalankan file installer. Pilih direktori instalasi (disarankan `C:\laragon` atau `D:\laragon` untuk menghindari masalah permission di folder Program Files). Klik Next dan tunggu proses instalasi selesai.

**Langkah 3: Jalankan Laragon**

Setelah instalasi selesai, buka Laragon dari Start Menu atau shortcut di desktop. Klik tombol **Start All** di pojok kiri bawah untuk menjalankan Apache dan MySQL secara bersamaan.

> **[GAMBAR 4.2: Tampilan Laragon Control Panel setelah berhasil dijalankan, menampilkan Apache dan MySQL berstatus Running]**

**Langkah 4: Verifikasi Instalasi**

Buka browser dan akses `http://localhost`. Halaman welcome Laragon harus muncul. Buka terminal Laragon (klik kanan pada icon Laragon di system tray > Terminal) dan jalankan:

```bash
php -v
# Output: PHP 8.x.x (cli)

mysql --version
# Output: mysql  Ver 8.0.30

node -v
# Output: v18.x.x

npm -v
# Output: 9.x.x
```

---

## 4.4 Instalasi Composer

Composer adalah dependency manager untuk PHP yang digunakan untuk menginstal dan mengelola semua package Laravel dan library pihak ketiga yang digunakan SimAset.

### 4.4.1 Instalasi di Windows

**Cara 1: Menggunakan Windows Installer (Direkomendasikan)**

1. Unduh Composer Installer dari `https://getcomposer.org/Composer-Setup.exe`
2. Jalankan installer
3. Pada langkah "Settings Check", arahkan ke PHP yang digunakan Laragon, contoh: `C:\laragon\bin\php\php8.x\php.exe`
4. Klik Next hingga selesai

**Cara 2: Menggunakan Command Line**

Buka terminal Laragon dan jalankan:

```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php composer-setup.php
php -r "unlink('composer-setup.php');"
move composer.phar C:\laragon\bin\composer\composer.phar
```

**Verifikasi:**
```bash
composer --version
# Output: Composer version 2.x.x
```

> **[GAMBAR 4.3: Tampilan terminal setelah Composer berhasil diinstal dengan output versi]**

---

## 4.5 Persiapan Database MySQL

Sebelum menjalankan migrasi, database `simset_rbtv` harus dibuat terlebih dahulu di MySQL.

### 4.5.1 Membuat Database via phpMyAdmin

1. Buka browser, akses `http://localhost/phpmyadmin`
2. Login dengan username `root` dan password kosong (default Laragon)
3. Klik tab **Databases**
4. Pada field "Create database", ketik `simset_rbtv`
5. Pilih collation `utf8mb4_unicode_ci`
6. Klik **Create**

> **[GAMBAR 4.4: Tampilan phpMyAdmin saat membuat database simset_rbtv dengan collation utf8mb4_unicode_ci]**

### 4.5.2 Membuat Database via Command Line

```bash
mysql -u root -p
# (tekan Enter jika password kosong)

CREATE DATABASE simset_rbtv
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

SHOW DATABASES;
# simset_rbtv harus muncul dalam daftar

EXIT;
```

---

## 4.6 Clone dan Setup Proyek

### 4.6.1 Clone Repository

```bash
# Masuk ke direktori web Laragon
cd C:\laragon\www

# Clone repository
git clone https://github.com/[username]/simaset-rbtv.git

# Masuk ke direktori proyek
cd simaset-rbtv
```

### 4.6.2 Instalasi Dependency PHP

```bash
composer install
```

Perintah ini akan membaca `composer.json` dan mengunduh semua package yang diperlukan ke folder `vendor/`. Proses ini membutuhkan koneksi internet dan mungkin memakan waktu beberapa menit tergantung kecepatan koneksi. Package yang akan diinstal antara lain:

- `laravel/framework` ^12.0 — core framework
- `barryvdh/laravel-dompdf` ^3.1 — generate PDF
- `intervention/image` ^4.0 — resize foto
- `maatwebsite/excel` ^3.1 — import/export Excel
- `simplesoftwareio/simple-qrcode` ^4.2 — generate QR code SVG

> **[GAMBAR 4.5: Tampilan terminal saat composer install berjalan, menampilkan progress download package]**

### 4.6.3 Instalasi Dependency JavaScript

```bash
npm install
```

Perintah ini mengunduh semua package JavaScript ke folder `node_modules/`. Package utama yang diinstal:

- `tailwindcss` ^3.1.0 — CSS framework
- `alpinejs` ^3.4.2 — JavaScript framework ringan
- `laravel-vite-plugin` ^2.0.0 — integrasi Vite dengan Laravel
- `axios` ^1.11.0 — HTTP client untuk AJAX

---

## 4.7 Konfigurasi Environment (.env)

File `.env` adalah file konfigurasi utama yang menyimpan semua variabel environment seperti koneksi database, konfigurasi mail, dan pengaturan aplikasi. File ini tidak di-commit ke Git karena berisi informasi sensitif.

### 4.7.1 Membuat File .env

```bash
cp .env.example .env
```

### 4.7.2 Generate Application Key

```bash
php artisan key:generate
```

Perintah ini mengisi variabel `APP_KEY` di file `.env` dengan string enkripsi yang unik dan aman. Application key digunakan untuk enkripsi session, cookie, dan data sensitif lainnya.

### 4.7.3 Konfigurasi Variabel Penting

Buka file `.env` dengan text editor dan sesuaikan nilai-nilai berikut:

```env
# ── Konfigurasi Aplikasi ──────────────────────────────────────
APP_NAME="SimAset RBTV"
APP_ENV=local
APP_KEY=base64:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
APP_DEBUG=true
APP_URL=http://localhost:8000

APP_LOCALE=id
APP_TIMEZONE=Asia/Jakarta

# ── Konfigurasi Database ──────────────────────────────────────
# Gunakan MySQL (sesuai database aktual simset_rbtv)
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=simset_rbtv
DB_USERNAME=root
DB_PASSWORD=

# ── Konfigurasi Session ───────────────────────────────────────
SESSION_DRIVER=database
SESSION_LIFETIME=120

# ── Konfigurasi Mail ──────────────────────────────────────────
# Development: gunakan 'log' agar email tidak benar-benar terkirim
# Email akan tercatat di storage/logs/laravel.log
MAIL_MAILER=log
MAIL_FROM_ADDRESS="noreply@rbtv.co.id"
MAIL_FROM_NAME="SimAset RBTV"

# Production: ganti dengan konfigurasi SMTP
# MAIL_MAILER=smtp
# MAIL_HOST=smtp.gmail.com
# MAIL_PORT=587
# MAIL_USERNAME=your-email@gmail.com
# MAIL_PASSWORD=your-app-password
# MAIL_ENCRYPTION=tls

# ── Konfigurasi Cache & Queue ─────────────────────────────────
CACHE_STORE=database
QUEUE_CONNECTION=database
```

**Penjelasan variabel penting:**

| Variabel | Nilai | Keterangan |
|----------|-------|------------|
| APP_NAME | SimAset RBTV | Nama aplikasi yang tampil di browser tab |
| APP_ENV | local | Environment: local/staging/production |
| APP_DEBUG | true | Tampilkan error detail (false di production) |
| DB_DATABASE | simset_rbtv | Nama database yang sudah dibuat |
| DB_USERNAME | root | Username MySQL (default Laragon: root) |
| DB_PASSWORD | (kosong) | Password MySQL (default Laragon: kosong) |
| MAIL_MAILER | log | Driver email: log untuk dev, smtp untuk production |
| SESSION_DRIVER | database | Session disimpan di tabel sessions |

---

## 4.8 Migrasi Database dan Seeder

### 4.8.1 Menjalankan Migrasi

```bash
php artisan migrate
```

Perintah ini membaca semua file migration di folder `database/migrations/` dan membuat tabel-tabel yang diperlukan di database `simset_rbtv`. Urutan eksekusi migration:

| Urutan | File Migration | Tabel yang Dibuat/Diubah |
|--------|---------------|--------------------------|
| 1 | 2026_04_29_133436_create_missing_tables_from_schema | aset, barang, ruangan, users, sessions, log_aktivitas |
| 2 | 2026_04_29_141823_alter_aset_table_add_missing_columns | Tambah kolom jumlah, updated_by ke aset |
| 3 | 2026_04_29_141913_add_deleted_at_to_aset_table | Tambah deleted_at ke aset |
| 4 | 2026_04_29_142111_drop_foreign_key_kode_barang_on_aset | Penyesuaian FK |
| 5 | 2026_04_29_142359_create_riwayat_mutasi_table | Tabel riwayat_mutasi |
| 6 | 2026_04_29_142535_convert_aset_id_to_bigint | Konversi tipe ID |
| 7 | 2026_04_29_144500_add_missing_user_columns | Tambah role, is_active, last_login_at ke users |
| 8 | 2026_04_29_144600_add_updated_at_to_users | Tambah updated_at ke users |
| 9 | 2026_04_29_150000_add_qr_column_to_aset | Kolom QR code |
| 10 | 2026_04_29_153313_add_deleted_at_to_barang_table | Tambah deleted_at ke barang |
| 11 | 2026_04_29_210600_remove_foto_profil_from_users | Hapus kolom foto_profil |
| 12 | 2026_05_02_000001_fix_missing_columns | Perbaikan kolom |
| 13 | 2026_05_02_100000_add_keterangan_to_barang_and_ruangan | Tambah keterangan ke barang & ruangan |
| 14 | 2026_05_02_200000_add_harga_sumber_to_aset | Tambah harga_perolehan & sumber_perolehan ke aset |

> **[GAMBAR 4.6: Tampilan terminal saat php artisan migrate berjalan, menampilkan daftar migration yang berhasil dieksekusi]**

### 4.8.2 Menjalankan Seeder

```bash
php artisan db:seed
```

Seeder mengisi data awal ke database. `DatabaseSeeder` memanggil tiga seeder secara berurutan:

1. **AdminSeeder** — Membuat akun admin:
   - Admin RBTV (admin@rbtv.co.id / Admin123)
   - Magang RBTV (magangrbtv@gmail.com / Magang123)

2. **StaffSeeder** — Membuat akun staff:
   - Staff RBTV (staff@rbtv.co.id / Staff123)

3. **BarangSeeder** — Membuat data contoh:
   - 7 ruangan (Studio Utama, Ruang Editing, dll.)
   - 23 master barang (Kamera, Audio, Komputer, dll.)
   - ~23 aset instances

### 4.8.3 Migrasi + Seeder Sekaligus

```bash
# Setup lengkap dari awal
php artisan migrate --seed

# Reset total dan mulai dari awal (HATI-HATI: menghapus semua data)
php artisan migrate:fresh --seed
```

> **[GAMBAR 4.7: Tampilan phpMyAdmin setelah migrasi berhasil, menampilkan semua tabel database simset_rbtv]**

---

## 4.9 Build Frontend Assets

### 4.9.1 Development Mode

```bash
npm run dev
```

Perintah ini menjalankan Vite dalam mode development dengan Hot Module Replacement (HMR). Biarkan terminal ini tetap berjalan selama proses development — setiap perubahan pada file CSS atau JavaScript akan otomatis ter-refresh di browser.

### 4.9.2 Production Build

```bash
npm run build
```

Perintah ini mengkompilasi, meminifikasi, dan mengoptimalkan semua asset CSS dan JavaScript ke direktori `public/build/`. Wajib dijalankan sebelum deploy ke production atau saat menjalankan aplikasi tanpa `npm run dev`.

---

## 4.10 Menjalankan Server Development

```bash
php artisan serve
```

Aplikasi akan berjalan di `http://127.0.0.1:8000`. Buka URL ini di browser untuk mengakses SimAset.

**Menjalankan semua service sekaligus:**

```bash
composer run dev
```

Perintah ini menjalankan secara bersamaan (menggunakan `concurrently`):
- `php artisan serve` — web server Laravel
- `php artisan queue:listen --tries=1` — queue worker untuk email
- `php artisan pail --timeout=0` — real-time log viewer
- `npm run dev` — Vite dev server

> **[GAMBAR 4.8: Tampilan halaman login SimAset pertama kali diakses di browser setelah setup berhasil]**

---

## 4.11 Struktur Folder Proyek

Berikut adalah struktur folder lengkap proyek SimAset beserta penjelasan fungsi setiap folder:

```
simaset-rbtv/
│
├── app/                          ← Kode aplikasi utama
│   ├── Console/
│   │   └── Commands/             ← Artisan commands kustom
│   │       ├── DropExtraTables.php
│   │       └── FixUsersSchema.php
│   ├── Exports/                  ← Kelas export Excel
│   │   ├── AssetExportFile.php   ← Export aset ke .xlsx dengan styling
│   │   └── BarangExportFile.php  ← Export barang ke .xlsx
│   ├── Helpers/                  ← Helper classes
│   │   ├── ActivityLogger.php    ← Mencatat aktivitas ke log_aktivitas
│   │   └── ImageHelper.php       ← Resize foto aset
│   ├── Http/
│   │   ├── Controllers/          ← 13 controller
│   │   │   ├── Auth/             ← 8 controller autentikasi (Breeze)
│   │   │   ├── AssetController.php
│   │   │   ├── BarangController.php
│   │   │   ├── RuanganController.php
│   │   │   ├── UserController.php
│   │   │   ├── QrCodeController.php
│   │   │   ├── MaintenanceController.php
│   │   │   ├── LaporanController.php
│   │   │   ├── ExportController.php
│   │   │   ├── ImportController.php
│   │   │   ├── DashboardController.php
│   │   │   ├── AuditLogController.php
│   │   │   └── ProfileController.php
│   │   ├── Middleware/           ← 3 middleware kustom
│   │   │   ├── LogActivity.php
│   │   │   ├── RoleMiddleware.php
│   │   │   └── SecurityHeaders.php
│   │   └── Requests/             ← Form request validation
│   │       ├── Auth/LoginRequest.php
│   │       └── ProfileUpdateRequest.php
│   ├── Imports/
│   │   └── AssetImport.php       ← Import aset dari Excel
│   ├── Mail/                     ← Kelas email
│   │   ├── AkunBaruMail.php      ← Email notifikasi akun baru
│   │   └── MaintenanceAlert.php  ← Email notifikasi maintenance selesai
│   ├── Models/                   ← 5 Eloquent model
│   │   ├── ActivityLog.php
│   │   ├── Asset.php
│   │   ├── Barang.php
│   │   ├── Ruangan.php
│   │   └── User.php
│   ├── Notifications/
│   │   └── ResetPasswordNotification.php
│   ├── Providers/
│   │   └── AppServiceProvider.php
│   └── View/Components/          ← Blade components
│       ├── AppLayout.php
│       └── GuestLayout.php
│
├── bootstrap/
│   └── app.php                   ← Registrasi middleware global
│
├── config/                       ← File konfigurasi
│   ├── app.php
│   ├── auth.php
│   ├── database.php
│   ├── excel.php                 ← Konfigurasi Maatwebsite Excel
│   ├── mail.php
│   └── ...
│
├── database/
│   ├── migrations/               ← 14 file migration
│   ├── seeders/                  ← 4 seeder
│   │   ├── AdminSeeder.php
│   │   ├── StaffSeeder.php
│   │   ├── BarangSeeder.php
│   │   └── DatabaseSeeder.php
│   └── database.sqlite           ← File SQLite (jika pakai SQLite)
│
├── docs/                         ← Dokumentasi modul pengembangan
│
├── public/                       ← File yang dapat diakses publik
│   ├── build/                    ← Hasil build Vite (CSS/JS)
│   ├── css/
│   │   └── glass-ui.css          ← CSS tambahan
│   ├── foto_aset/                ← Upload foto aset
│   │   └── 1777735186_AST-001.png ← Contoh foto dari AST-003
│   ├── foto_profil/              ← Upload foto profil
│   ├── qr_codes/                 ← File QR code yang di-generate
│   │   ├── qr_AST-001_*.png
│   │   └── qr_BRG-002_*.png
│   └── index.php                 ← Entry point aplikasi
│
├── resources/
│   ├── css/
│   │   └── app.css               ← CSS utama (Tailwind directives)
│   ├── js/
│   │   ├── app.js                ← JS utama (Alpine.js, Axios)
│   │   └── bootstrap.js
│   └── views/                    ← 60+ Blade template files
│       ├── aset/                 ← index, create, edit, show, qr
│       ├── audit_log/            ← index
│       ├── auth/                 ← login, forgot-password, dll
│       ├── barang/               ← index, create, edit, show
│       ├── components/           ← 18 reusable components
│       ├── emails/               ← Template email
│       ├── export/               ← aset, barang
│       ├── import/               ← aset-import
│       ├── laporan/              ← index, aset, aset_pdf, dll
│       ├── layouts/              ← app, auth, guest, navigation
│       ├── maintenance/          ← index
│       ├── profile/              ← edit
│       ├── qrcode/               ← scanner, batch_print, single
│       ├── ruangan/              ← index, create, edit, show
│       ├── users/                ← index, create, edit
│       └── dashboard.blade.php
│
├── routes/
│   ├── auth.php                  ← Route autentikasi (Breeze)
│   ├── console.php               ← Route Artisan commands
│   └── web.php                   ← Route web utama
│
├── storage/                      ← Log, cache, session files
│   └── logs/
│       └── laravel.log           ← Log aplikasi dan email (dev mode)
│
├── .env                          ← Environment variables (tidak di-commit)
├── .env.example                  ← Template environment variables
├── artisan                       ← CLI Laravel
├── composer.json                 ← Dependency PHP
├── package.json                  ← Dependency JavaScript
└── README.md                     ← Dokumentasi singkat
```

> **[GAMBAR 4.9: Tampilan struktur folder proyek SimAset di VS Code Explorer]**

---

## 4.12 Pengujian Awal Lingkungan

Setelah semua langkah setup selesai, lakukan pengujian awal untuk memastikan semua komponen berjalan dengan benar:

### 4.12.1 Cek Koneksi Database

```bash
php artisan db:show
```

Output harus menampilkan informasi koneksi ke database `simset_rbtv` tanpa error.

### 4.12.2 Cek Status Migrasi

```bash
php artisan migrate:status
```

Semua migration harus berstatus `Ran`. Jika ada yang berstatus `Pending`, jalankan `php artisan migrate` lagi.

### 4.12.3 Test Login ke Sistem

1. Buka browser, akses `http://127.0.0.1:8000`
2. Halaman login harus muncul
3. Login dengan `magangrbtv@gmail.com` / `Magang123`
4. Dashboard harus tampil dengan data statistik

### 4.12.4 Cek Direktori Upload

Pastikan direktori berikut ada dan dapat ditulis:

```bash
# Cek di PowerShell
Test-Path "public\foto_aset"    # Harus True
Test-Path "public\foto_profil"  # Harus True
Test-Path "public\qr_codes"     # Harus True
```

Jika belum ada, buat secara manual:

```bash
New-Item -ItemType Directory -Path "public\foto_aset"
New-Item -ItemType Directory -Path "public\foto_profil"
New-Item -ItemType Directory -Path "public\qr_codes"
```

---

## 4.13 Troubleshooting Umum

### Error: `SQLSTATE[HY000] [2002] Connection refused`

**Penyebab:** MySQL belum berjalan atau konfigurasi koneksi salah.

**Solusi:**
1. Pastikan MySQL sudah berjalan di Laragon (klik Start All)
2. Cek nilai `DB_HOST`, `DB_PORT`, `DB_USERNAME`, `DB_PASSWORD` di `.env`
3. Pastikan database `simset_rbtv` sudah dibuat

### Error: `Vite manifest not found at: .../public/build/manifest.json`

**Penyebab:** Frontend assets belum di-build.

**Solusi:**
```bash
npm run build
# atau jalankan npm run dev di terminal terpisah
```

### Error: `Class "SimpleSoftwareIO\QrCode\..." not found`

**Penyebab:** Autoloader belum diperbarui setelah instalasi package.

**Solusi:**
```bash
composer dump-autoload
php artisan config:clear
php artisan cache:clear
```

### Error: `The stream or file .../storage/logs/laravel.log could not be opened`

**Penyebab:** Direktori storage tidak memiliki permission yang cukup.

**Solusi (Linux/macOS):**
```bash
chmod -R 775 storage bootstrap/cache
chown -R $USER:www-data storage bootstrap/cache
```

### Error: `php_gd extension not found`

**Penyebab:** Ekstensi GD PHP belum aktif (diperlukan untuk ImageHelper).

**Solusi:**
1. Buka `php.ini` di direktori PHP Laragon
2. Cari `;extension=gd` dan hapus tanda titik koma di depannya
3. Restart Apache di Laragon

---

## 4.14 Kesimpulan Modul

Modul 4 ini telah membahas secara lengkap dan detail seluruh tahapan persiapan lingkungan pengembangan SimAset. Dimulai dari identifikasi kebutuhan perangkat lunak, instalasi Laragon sebagai web server lokal, instalasi Composer dan Node.js, persiapan database MySQL `simset_rbtv`, konfigurasi file `.env` dengan semua variabel yang diperlukan, migrasi database dan seeder, build frontend assets, hingga pengujian awal dan troubleshooting masalah umum.

Dengan lingkungan pengembangan yang telah disiapkan dan diverifikasi dengan benar, proses implementasi fitur-fitur sistem pada modul-modul berikutnya dapat berjalan dengan lancar tanpa hambatan teknis yang tidak perlu.

---

*Kembali ke: [Modul 3 — Perancangan Sistem](MODUL_03_PERANCANGAN_SISTEM.md)*
*Lanjut ke: [Modul 5 — Implementasi Database](MODUL_05_IMPLEMENTASI_DATABASE.md)*
