# SimAset — Sistem Informasi Manajemen Aset
### RBTV Bengkulu

Aplikasi web berbasis Laravel untuk mengelola aset barang kantor RBTV Bengkulu secara digital dan terpusat.

---

## Tech Stack

- **Backend:** Laravel 12 (PHP)
- **Frontend:** Bootstrap 5 + Blade
- **Database:** MySQL / SQLite
- **Auth:** Laravel Breeze (session-based)
- **Export:** Maatwebsite Excel + DomPDF
- **QR Code:** SimpleSoftwareIO QR Code
- **Charts:** Chart.js

---

## Instalasi

```bash
# 1. Clone & install dependencies
composer install
npm install && npm run build

# 2. Setup environment
cp .env.example .env
php artisan key:generate

# 3. Konfigurasi database di .env, lalu jalankan migrasi
php artisan migrate --seed

# 4. Jalankan server
php artisan serve
```

## Akun Default (Seeder)

| Role  | Email               | Password  |
|-------|---------------------|-----------|
| Admin | admin@rbtv.com      | Admin123  |
| Staff | staff@rbtv.com      | Staff123  |

---

## Fitur Utama

- Manajemen Aset (CRUD, soft delete, batch delete, foto)
- Manajemen Barang & Ruangan (master data)
- QR Code per aset (generate, download, batch print, scanner)
- Maintenance tracking (set masuk, tandai selesai, notifikasi email)
- Import massal dari Excel/CSV
- Export ke Excel & PDF dengan filter
- Laporan aset, per ruangan, dan maintenance
- Audit log seluruh aktivitas pengguna
- Manajemen pengguna dengan role Admin/Staff

---

## Dokumentasi Penggunaan

Lihat **MODUL_PENGGUNAAN.md** untuk panduan lengkap penggunaan sistem.

---

## Konfigurasi Mail (Production)

Ubah `MAIL_MAILER=log` menjadi `MAIL_MAILER=smtp` di `.env` dan isi konfigurasi SMTP.
Lihat komentar di `.env.example` untuk contoh konfigurasi Gmail/SMTP.

---

*SimAset v1.0 — Kerja Praktik Teknik Informatika Universitas Bengkulu, 2026*
