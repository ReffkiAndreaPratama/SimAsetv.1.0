# Dokumentasi Kode — SimAset RBTV Bengkulu

**Versi:** 1.0  
**Tanggal:** 9 Mei 2026  
**Deskripsi:** Sistem Informasi Manajemen Aset Barang Kantor Rakyat Bengkulu Televisi (RBTV) berbasis web menggunakan Laravel 12 dan MySQL.

---

## Daftar Isi

1. [Gambaran Umum](#1-gambaran-umum)
2. [Stack Teknologi](#2-stack-teknologi)
3. [Struktur Database](#3-struktur-database)
4. [Struktur Direktori](#4-struktur-direktori)
5. [Models](#5-models)
6. [Controllers](#6-controllers)
7. [Middleware](#7-middleware)
8. [Routes](#8-routes)
9. [Views](#9-views)
10. [Export & Import](#10-export--import)
11. [Alur Kerja Fitur Utama](#11-alur-kerja-fitur-utama)
12. [Keamanan](#12-keamanan)
13. [Email](#13-email)
14. [Dependencies](#14-dependencies)
15. [Catatan Penting & Keputusan Desain](#15-catatan-penting--keputusan-desain)
16. [Instalasi & Setup](#16-instalasi--setup)

---

## 1. Gambaran Umum

**SimAset** adalah aplikasi web untuk mengelola aset barang kantor RBTV Bengkulu secara digital. Sistem ini menggantikan pencatatan manual dengan fitur:

- CRUD aset, barang, dan ruangan
- Manajemen maintenance aset
- Generate & scan QR Code
- Export laporan PDF, Excel, CSV
- Import data massal via Excel/CSV
- Role-based access control (Admin & Staff)
- Audit log aktivitas pengguna

**URL Lokal:** `http://localhost:8000`  
**Database:** MySQL — `simset`

---

## 2. Stack Teknologi

### Backend
| Teknologi | Versi | Fungsi |
|---|---|---|
| PHP | 8.2+ | Bahasa pemrograman server-side |
| Laravel | 12.x | Framework MVC |
| MySQL | 8.0+ | Database |

### Frontend
| Teknologi | Fungsi |
|---|---|
| HTML5 / CSS3 / JavaScript | Struktur, styling, interaktivitas |
| Bootstrap 5.3.3 | CSS framework (via CDN) |
| Font Awesome 6 | Icon library (via CDN) |
| Chart.js | Grafik dashboard |
| jsQR 1.4.0 | QR Code scanner via kamera |

### Library PHP
| Package | Versi | Fungsi |
|---|---|---|
| barryvdh/laravel-dompdf | ^3.1 | Generate PDF |
| maatwebsite/excel | ^3.1 | Import/Export Excel |
| simplesoftwareio/simple-qrcode | ^4.2 | Generate QR Code SVG |
| intervention/image | ^4.0 | Image processing |

---

## 3. Struktur Database

### Tabel `users`
| Kolom | Tipe | Keterangan |
|---|---|---|
| id_user | INT AUTO_INCREMENT PK | Primary key |
| nama | VARCHAR(100) | Nama lengkap |
| email | VARCHAR(100) UNIQUE | Email login |
| password_hash | VARCHAR(255) | Password bcrypt |
| role | ENUM('admin','staff') | Hak akses |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

### Tabel `barang`
| Kolom | Tipe | Keterangan |
|---|---|---|
| kode_barang | VARCHAR(20) PK | Format: BRG-001 |
| nama_barang | VARCHAR(100) | Nama jenis barang |
| kategori | VARCHAR(100) | Kategori barang |
| jumlah | INT DEFAULT 0 | Jumlah stok |
| keterangan | TEXT | Catatan |

### Tabel `ruangan`
| Kolom | Tipe | Keterangan |
|---|---|---|
| kode_ruangan | VARCHAR(20) PK | Format: RNG-001 |
| nama_ruangan | VARCHAR(100) | Nama ruangan |
| lantai | VARCHAR(20) | Lantai gedung |
| keterangan | TEXT | Catatan |

### Tabel `aset`
| Kolom | Tipe | Keterangan |
|---|---|---|
| kode_aset | VARCHAR(20) PK | Format: AST-001 |
| kode_barang | VARCHAR(20) FK | Referensi barang |
| kode_ruangan | VARCHAR(20) FK | Referensi ruangan |
| id_user | INT FK | User yang input |
| serial_number | VARCHAR(100) | Nomor seri |
| kondisi | VARCHAR(100) | Baik/Rusak Ringan/Rusak Berat |
| status | VARCHAR(50) | Aktif/Maintenance/Non-Aktif |
| harga | DECIMAL(15,2) | Harga perolehan |
| keterangan | TEXT | Catatan |
| foto | VARCHAR(255) | Nama file foto |

### Tabel `log_aktivitas`
| Kolom | Tipe | Keterangan |
|---|---|---|
| id_log | INT AUTO_INCREMENT PK | Primary key |
| id_user | INT FK | User pelaku |
| aktivitas | VARCHAR(255) | Jenis aktivitas |
| ip_address | VARCHAR(45) | IP address |
| keterangan | TEXT | Detail aktivitas |
| created_at | TIMESTAMP | |

---

## 4. Struktur Direktori

```
app/
├── Exports/
│   ├── AssetExportFile.php      — Excel export aset dengan styling
│   └── BarangExportFile.php     — Excel export barang dengan styling
├── Helpers/
│   └── ActivityLogger.php       — Static helper untuk log aktivitas
├── Http/
│   ├── Controllers/
│   │   ├── Auth/                — Breeze auth controllers
│   │   ├── AssetController.php
│   │   ├── AuditLogController.php
│   │   ├── BarangController.php
│   │   ├── DashboardController.php
│   │   ├── ExportController.php
│   │   ├── ImportController.php
│   │   ├── LaporanController.php
│   │   ├── MaintenanceController.php
│   │   ├── ProfileController.php
│   │   ├── QrCodeController.php
│   │   ├── RuanganController.php
│   │   └── UserController.php
│   ├── Middleware/
│   │   ├── LogActivity.php
│   │   ├── RoleMiddleware.php
│   │   └── SecurityHeaders.php
│   └── Requests/
│       ├── Auth/LoginRequest.php
│       └── ProfileUpdateRequest.php
├── Imports/
│   └── AssetImport.php
├── Mail/
│   ├── AkunBaruMail.php
│   └── MaintenanceAlert.php
├── Models/
│   ├── ActivityLog.php
│   ├── Asset.php
│   ├── Barang.php
│   ├── Ruangan.php
│   └── User.php
├── Notifications/
│   └── ResetPasswordNotification.php
└── Providers/
    └── AppServiceProvider.php

database/
├── migrations/
│   ├── 2026_05_08_073431_add_foto_to_aset_table.php
│   └── 2026_05_08_100000_create_all_tables.php
└── seeders/
    ├── AdminSeeder.php
    ├── BarangSeeder.php
    ├── DatabaseSeeder.php
    └── StaffSeeder.php

public/
├── foto_aset/     — Upload foto aset
├── qr_codes/      — File QR code PNG
├── logo.png
└── logoweb.png

resources/views/
├── aset/          — index, create, edit, show, qr
├── audit_log/     — index
├── auth/          — login, forgot-password, reset-password
├── barang/        — index, create, edit, show
├── components/    — form-styles, page-styles, dll
├── emails/        — akunbaru, maintenance-alert, reset-password
├── errors/        — 403, 404, 500
├── laporan/       — index, aset_pdf, barang_pdf, maintenance_pdf, ruangan_pdf
├── layouts/       — app, auth, guest, navigation
├── maintenance/   — index
├── profile/       — edit
├── qrcode/        — scanner, single, batch_print
├── ruangan/       — index, create, edit, show
├── users/         — index, create, edit
└── dashboard.blade.php

routes/
├── web.php
└── auth.php
```

---

## 5. Models

### `Asset` — `app/Models/Asset.php`
- **Tabel:** `aset`
- **Primary Key:** `kode_aset` (string)
- **Fillable:** kode_aset, kode_barang, kode_ruangan, id_user, serial_number, kondisi, status, harga, keterangan, foto

**Relasi:**
```php
barang()   → belongsTo(Barang, 'kode_barang')
ruangan()  → belongsTo(Ruangan, 'kode_ruangan')
user()     → belongsTo(User, 'id_user')
```

**Method penting:**
```php
Asset::generateKode() // Generate kode AST-001, AST-002, dst (gap-filling)
```

---

### `Barang` — `app/Models/Barang.php`
- **Tabel:** `barang`
- **Primary Key:** `kode_barang` (string)

**Relasi:**
```php
aset() → hasMany(Asset, 'kode_barang')
```

**Method penting:**
```php
Barang::generateKode() // Generate kode BRG-001, BRG-002, dst
```

---

### `Ruangan` — `app/Models/Ruangan.php`
- **Tabel:** `ruangan`
- **Primary Key:** `kode_ruangan` (string)

**Relasi:**
```php
assets() → hasMany(Asset, 'kode_ruangan')
```

---

### `User` — `app/Models/User.php`
- **Tabel:** `users`
- **Primary Key:** `id_user` (integer)

**Override Laravel default:**
```php
getAuthPassword()       // return $this->password_hash
getAuthIdentifierName() // return 'id_user'
```

**Method helper:**
```php
isAdmin() // return $this->role === 'admin'
isStaff() // return $this->role === 'staff'
```

---

### `ActivityLog` — `app/Models/ActivityLog.php`
- **Tabel:** `log_aktivitas`
- **Primary Key:** `id_log`
- **Timestamps:** hanya `created_at` (tidak ada `updated_at`)

---

## 6. Controllers

### `AssetController`
| Method | Route | Fungsi |
|---|---|---|
| index | GET /aset | Daftar aset dengan filter & pagination |
| create | GET /aset/create | Form tambah aset |
| store | POST /aset | Simpan aset baru + upload foto |
| show | GET /aset/{kode} | Detail aset |
| edit | GET /aset/{kode}/edit | Form edit aset |
| update | PUT /aset/{kode} | Update aset + ganti/hapus foto |
| destroy | DELETE /aset/{kode} | Hapus aset + hapus file foto |
| batchDestroy | POST /aset/batch-destroy | Hapus banyak aset sekaligus |
| generateQr | POST /aset/{kode}/generate-qr | Generate QR PNG via api.qrserver.com |
| showQr | GET /aset/{kode}/qr | Halaman cetak QR |
| detail | GET /aset/{kode}/detail | Detail publik (untuk scan QR) |

---

### `BarangController`
| Method | Route | Fungsi |
|---|---|---|
| index | GET /barang | Daftar barang dengan filter |
| create | GET /barang/create | Form tambah barang |
| store | POST /barang | Simpan barang baru |
| show | GET /barang/{kode} | Detail barang |
| edit | GET /barang/{kode}/edit | Form edit barang |
| update | PUT /barang/{kode} | Update barang |
| destroy | DELETE /barang/{kode} | Hapus barang |

---

### `RuanganController`
| Method | Route | Fungsi |
|---|---|---|
| index | GET /ruangan | Daftar ruangan |
| create | GET /ruangan/create | Form tambah ruangan |
| store | POST /ruangan | Simpan ruangan baru |
| show | GET /ruangan/{kode} | Detail ruangan + daftar aset |
| edit | GET /ruangan/{kode}/edit | Form edit ruangan |
| update | PUT /ruangan/{kode} | Update ruangan |
| destroy | DELETE /ruangan/{kode} | Hapus ruangan (cek aset dulu) |

---

### `MaintenanceController`
| Method | Route | Fungsi |
|---|---|---|
| index | GET /maintenance | Daftar aset maintenance |
| setMaintenance | POST /maintenance/{kode}/set | Set aset ke status Maintenance |
| complete | PATCH /maintenance/{kode}/complete | Selesaikan maintenance → kirim email admin |

---

### `ExportController`
| Method | Route | Fungsi |
|---|---|---|
| excelAset | GET /export/aset/excel | Download Excel aset |
| pdfAset | GET /export/aset/pdf | Download PDF aset |
| excelBarang | GET /export/barang/excel | Download Excel barang |
| pdfBarang | GET /export/barang/pdf | Download PDF barang |

---

### `LaporanController`
| Method | Route | Fungsi |
|---|---|---|
| index | GET /laporan | Halaman laporan |
| cetakAset | GET /laporan/assets/cetak | PDF semua aset |
| exportAset | GET /laporan/assets/export | CSV semua aset |
| laporanRuangan | GET /laporan/ruangan/{kode} | PDF aset per ruangan |
| exportMaintenancePdf | GET /laporan/maintenance/pdf | PDF maintenance |
| exportMaintenanceCsv | GET /laporan/maintenance/csv | CSV maintenance |

---

### `ImportController`
| Method | Route | Fungsi |
|---|---|---|
| store | POST /import | Proses import file Excel/CSV |
| template | GET /import/template | Download template CSV |

---

### `QrCodeController`
| Method | Route | Fungsi |
|---|---|---|
| scanner | GET /qrcode/scanner | Halaman scanner QR |
| batchPrint | GET /qrcode/batch-print | Cetak banyak QR sekaligus |
| download | GET /qrcode/{kode}/download | Download/cetak QR satu aset |
| search | GET /qrcode/search | Cari aset by kode (JSON) |

---

### `DashboardController`
Mengambil statistik: total aset, aktif, maintenance, non-aktif, rusak, total barang, total ruangan, distribusi kondisi & kategori, 10 aset terbaru.

---

### `UserController` *(Admin only)*
CRUD pengguna + kirim email notifikasi akun baru.

### `AuditLogController` *(Admin only)*
Tampilkan log aktivitas dengan filter user, modul, dan pencarian.

---

## 7. Middleware

### `RoleMiddleware` — `app/Http/Middleware/RoleMiddleware.php`
Cek role user. Dipakai di route group admin.
```php
// Penggunaan di routes/web.php
Route::middleware('role:admin')->group(function () { ... });
```

### `SecurityHeaders` — `app/Http/Middleware/SecurityHeaders.php`
Menambahkan security headers ke semua response:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: SAMEORIGIN`
- `X-XSS-Protection: 1; mode=block`
- `Referrer-Policy: strict-origin-when-cross-origin`

### `LogActivity` — `app/Http/Middleware/LogActivity.php`
Terminable middleware — log HTTP actions (Create/Update/Delete) untuk aset, barang, ruangan.

> *Catatan: Middleware ini tidak di-append global. Logging utama dilakukan manual via `ActivityLogger::logAsset()` di controller.*

---

## 8. Routes

### Auth Routes (`routes/auth.php`)
```
GET  /login                  → AuthenticatedSessionController@create
POST /login                  → AuthenticatedSessionController@store
POST /logout                 → AuthenticatedSessionController@destroy
GET  /forgot-password        → PasswordResetLinkController@create
POST /forgot-password        → PasswordResetLinkController@store
GET  /reset-password/{token} → NewPasswordController@create
POST /reset-password         → NewPasswordController@store
```

### Web Routes (`routes/web.php`)
Semua route di bawah middleware `auth`:

```
GET    /dashboard
GET    /aset                    aset.index
POST   /aset                    aset.store
GET    /aset/create             aset.create
GET    /aset/{kode}             aset.show
PUT    /aset/{kode}             aset.update
DELETE /aset/{kode}             aset.destroy
GET    /aset/{kode}/edit        aset.edit
POST   /aset/{kode}/generate-qr aset.generateQr
GET    /aset/{kode}/qr          aset.showQr
GET    /aset/{kode}/detail      assets.detail

GET    /barang                  barang.index
POST   /barang                  barang.store
GET    /barang/create           barang.create
GET    /barang/{kode}           barang.show
PUT    /barang/{kode}           barang.update
DELETE /barang/{kode}           barang.destroy

GET    /ruangan                 ruangan.index
POST   /ruangan                 ruangan.store
GET    /ruangan/create          ruangan.create
GET    /ruangan/{kode}          ruangan.show
PUT    /ruangan/{kode}          ruangan.update
DELETE /ruangan/{kode}          ruangan.destroy

GET    /maintenance             maintenance.index
POST   /maintenance/{kode}/set  maintenance.set
PATCH  /maintenance/{kode}/complete maintenance.complete

POST   /import                  import.store
GET    /import/template         import.template

GET    /export/aset/excel       export.aset.excel
GET    /export/aset/pdf         export.aset.pdf
GET    /export/barang/excel     export.barang.excel
GET    /export/barang/pdf       export.barang.pdf

GET    /laporan                 laporan.index
GET    /laporan/assets/cetak    laporan.aset.cetak
GET    /laporan/assets/export   laporan.aset.export
GET    /laporan/ruangan/{kode}  laporan.ruangan
GET    /laporan/maintenance/pdf laporan.maintenance.pdf
GET    /laporan/maintenance/csv laporan.maintenance.csv

GET    /qrcode/scanner          qrcode.scanner
GET    /qrcode/batch-print      qrcode.batch-print
GET    /qrcode/search           qrcode.search
GET    /qrcode/{kode}/download  qrcode.download

GET    /profile                 profile.edit
PATCH  /profile                 profile.update
DELETE /profile                 profile.destroy

# Admin only:
GET    /users                   users.index
POST   /users                   users.store
GET    /users/create            users.create
GET    /users/{user}/edit       users.edit
PUT    /users/{user}            users.update
DELETE /users/{user}            users.destroy
GET    /audit-log               audit-log.index
```

---

## 9. Views

### Layout Utama — `resources/views/layouts/app.blade.php`
Layout utama dengan sidebar navigasi. Menggunakan Bootstrap 5 via CDN.

### Komponen Reusable
| File | Fungsi |
|---|---|
| `components/page-styles.blade.php` | CSS untuk halaman index/detail |
| `components/form-styles.blade.php` | CSS untuk halaman form |

### Halaman Auth
| File | Fungsi |
|---|---|
| `auth/login.blade.php` | Halaman login (standalone, tidak extend layout) |
| `auth/forgot-password.blade.php` | Lupa password (extend layouts/auth) |
| `auth/reset-password.blade.php` | Reset password dengan strength indicator |

---

## 10. Export & Import

### Export Excel
**`AssetExportFile`** dan **`BarangExportFile`** mengimplementasikan:
- `FromCollection` — data dari Eloquent
- `WithHeadings` — header kolom
- `WithStyles` — styling warna header & alternating rows
- `ShouldAutoSize` — auto lebar kolom
- `WithEvents` — freeze pane, total row

### Export PDF
Menggunakan **DomPDF** via `Pdf::loadView()`. Template di `resources/views/laporan/`:
- `aset_pdf.blade.php` — Laporan semua aset
- `barang_pdf.blade.php` — Laporan master barang
- `ruangan_pdf.blade.php` — Laporan aset per ruangan
- `maintenance_pdf.blade.php` — Laporan aset maintenance

### Export CSV
Menggunakan PHP native `fputcsv()` dengan:
- BOM UTF-8 untuk kompatibilitas Excel Indonesia
- Delimiter semicolon (`;`)
- Header informasi di baris pertama

### Import
**`ImportController::processImport()`** — membaca file Excel/CSV baris per baris:
```
Kolom aset: kode_barang, kode_ruangan, kondisi, status, serial_number, harga, keterangan
Kolom barang: kode_barang, nama_barang, kategori, jumlah, keterangan
```

---

## 11. Alur Kerja Fitur Utama

### Login
```
GET /login → view auth.login
POST /login → LoginRequest::authenticate()
  → cari user by email
  → Hash::check(password, password_hash)
  → Auth::login($user)
  → redirect /dashboard
```

### Tambah Aset
```
GET /aset/create → form dengan dropdown barang & ruangan
POST /aset → validasi → Asset::generateKode()
  → upload foto ke public/foto_aset/ (jika ada)
  → Asset::create()
  → ActivityLogger::logAsset('Create')
  → redirect aset.index
```

### Generate & Scan QR
```
Generate: POST /aset/{kode}/generate-qr
  → fetch https://api.qrserver.com/v1/create-qr-code/
  → simpan PNG di public/qr_codes/

Scan: GET /qrcode/scanner → jsQR decode kamera
  → GET /qrcode/search?code={kode} → JSON
  → tampil detail aset
```

### Maintenance
```
Set: POST /maintenance/{kode}/set → status = 'Maintenance'
Selesai: PATCH /maintenance/{kode}/complete
  → status = 'Aktif', kondisi = baru
  → ActivityLogger::log()
  → Mail::to(admins)->send(new MaintenanceAlert())
```

### Import Aset
```
Modal upload → POST /import (type=aset)
  → baca file Excel/CSV
  → loop rows → validateAndCreateAsset()
  → return summary: X berhasil, Y gagal
```

---

## 12. Keamanan

| Mekanisme | Implementasi |
|---|---|
| Autentikasi | Laravel session-based auth |
| Password | bcrypt via `Hash::make()` |
| CSRF | `@csrf` di semua form |
| Role-Based Access | `RoleMiddleware` — admin vs staff |
| Input Validation | `Request::validate()` di semua controller |
| Security Headers | `SecurityHeaders` middleware |
| Rate Limiting | Login throttle 5x/menit di `LoginRequest` |

---

## 13. Email

3 jenis email menggunakan Laravel Mail + SMTP Gmail:

| Class | Trigger | Penerima |
|---|---|---|
| `AkunBaruMail` | Admin buat user baru (opsional) | User baru |
| `MaintenanceAlert` | Maintenance selesai | Semua admin |
| `ResetPasswordNotification` | Lupa password | User yang request |

**Konfigurasi `.env`:**
```env
MAIL_MAILER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=email@gmail.com
MAIL_PASSWORD=app_password
```

---

## 14. Dependencies

### Production (`composer.json` require)
| Package | Versi | Fungsi |
|---|---|---|
| php | ^8.2 | Runtime |
| laravel/framework | ^12.0 | Core framework |
| laravel/tinker | ^2.10.1 | REPL debugging |
| barryvdh/laravel-dompdf | ^3.1 | Generate PDF |
| maatwebsite/excel | ^3.1 | Import/Export Excel |
| simplesoftwareio/simple-qrcode | ^4.2 | Generate QR SVG |
| intervention/image | ^4.0 | Image processing |

### Development (`require-dev`)
| Package | Fungsi |
|---|---|
| laravel/breeze | Scaffolding autentikasi |
| fakerphp/faker | Data palsu untuk seeder |
| phpunit/phpunit | Unit testing |
| laravel/pint | Code style fixer |

---

## 15. Catatan Penting & Keputusan Desain

**1. String Primary Key**
Tabel `aset`, `barang`, `ruangan` menggunakan string PK (AST-001, BRG-001, RNG-001). Model perlu:
```php
public $incrementing = false;
protected $keyType = 'string';
```

**2. Gap-Filling Kode**
`generateKode()` mengisi nomor yang kosong. Jika AST-001 dihapus dan ada AST-002, kode berikutnya adalah AST-001 bukan AST-003.

**3. Kolom Password**
Kolom bernama `password_hash` bukan `password` (default Laravel). Perlu override `getAuthPassword()` di model User.

**4. Dual QR Generation**
- `AssetController::generateQrCodeImage()` → external API qrserver.com → simpan PNG
- `QrCodeController::download()` → SimpleSoftwareIO lokal → SVG

**5. Foto Aset**
Disimpan di `public/foto_aset/` (bukan `storage/`). Langsung accessible via URL tanpa symlink.

**6. CSV Delimiter Semicolon**
Semua export CSV pakai `;` bukan `,` untuk kompatibilitas Excel Indonesia.

**7. Hard Delete**
Tidak menggunakan `SoftDeletes` trait. Semua delete adalah hard delete.

**8. Role System Sederhana**
Hanya 2 role: `admin` dan `staff`. Staff akses semua fitur operasional. Admin tambahan: kelola pengguna & audit log.

**9. LogActivity Middleware**
Tidak aktif global. Logging dilakukan manual via `ActivityLogger::logAsset()` di controller.

---

## 16. Instalasi & Setup

```bash
# 1. Clone & install dependencies
git clone <repo>
cd <folder>
composer install

# 2. Setup environment
cp .env.example .env
php artisan key:generate

# 3. Konfigurasi database di .env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=simset
DB_USERNAME=root
DB_PASSWORD=

# 4. Migrasi & seed
php artisan migrate
php artisan db:seed

# 5. Jalankan server
php artisan serve
```

**Akun default setelah seeder:**
| Email | Password | Role |
|---|---|---|
| magangrbtv@gmail.com | Admin@123 | Admin |
| reffkip@gmail.com | (sesuai seeder) | Staff |

---

*Dokumentasi ini dibuat otomatis berdasarkan kode project SimAset v1.0*
