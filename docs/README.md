# MODUL PENGEMBANGAN SIMASET
## Sistem Informasi Manajemen Aset RBTV Bengkulu

**Versi:** 1.0 | **Tahun:** 2026 | **Database:** simset_rbtv (MySQL 8.0.30) | **Framework:** Laravel 12 + PHP 8.5.2

---

## Daftar Modul

| No | Modul | Topik Utama | File |
|----|-------|-------------|------|
| 1 | Pendahuluan Sistem | Deskripsi, latar belakang, tujuan, aktor, tech stack | [MODUL_01_PENDAHULUAN.md](MODUL_01_PENDAHULUAN.md) |
| 2 | Analisis Kebutuhan | 6 masalah sistem lama, 85+ kebutuhan fungsional, analisis pengguna | [MODUL_02_ANALISIS_KEBUTUHAN.md](MODUL_02_ANALISIS_KEBUTUHAN.md) |
| 3 | Perancangan Sistem | Use case, activity diagram, sequence diagram, ERD aktual, arsitektur MVC, UI/UX | [MODUL_03_PERANCANGAN_SISTEM.md](MODUL_03_PERANCANGAN_SISTEM.md) |
| 4 | Persiapan Lingkungan | Instalasi Laragon, Composer, Node.js, konfigurasi .env, migrasi, troubleshooting | [MODUL_04_PERSIAPAN_LINGKUNGAN.md](MODUL_04_PERSIAPAN_LINGKUNGAN.md) |
| 5 | Implementasi Database | DDL aktual, skema tabel, FK constraints, model Eloquent, seeder, gap-filling, soft delete | [MODUL_05_IMPLEMENTASI_DATABASE.md](MODUL_05_IMPLEMENTASI_DATABASE.md) |
| 6 | Autentikasi & Hak Akses | Laravel Breeze, RoleMiddleware, SecurityHeaders, ActivityLogger, matriks akses | [MODUL_06_AUTENTIKASI_HAK_AKSES.md](MODUL_06_AUTENTIKASI_HAK_AKSES.md) |
| 7 | Manajemen Data Aset | CRUD aset, foto, batch delete, filter, barang, ruangan, dashboard statistik | [MODUL_07_MANAJEMEN_ASET.md](MODUL_07_MANAJEMEN_ASET.md) |
| 8 | QR Code & Maintenance | Generate/cetak/scan QR, maintenance tracking, email notifikasi | [MODUL_08_QRCODE_MAINTENANCE.md](MODUL_08_QRCODE_MAINTENANCE.md) |
| 9 | Import, Export & Laporan | Import Excel/CSV, export Excel/PDF/CSV, laporan per ruangan | [MODUL_09_IMPORT_EXPORT_LAPORAN.md](MODUL_09_IMPORT_EXPORT_LAPORAN.md) |
| 10 | Audit Log & Manajemen User | 39 record log aktual, CRUD user, validasi password, avatar generator | [MODUL_10_AUDIT_LOG_USER.md](MODUL_10_AUDIT_LOG_USER.md) |
| 11 | Pengujian & Evaluasi | 85 skenario blackbox testing (100%), usability testing, evaluasi | [MODUL_11_PENGUJIAN_EVALUASI.md](MODUL_11_PENGUJIAN_EVALUASI.md) |
| 12 | Penutup & Pengembangan Lanjutan | Kesimpulan, keterbatasan, 10 rekomendasi, panduan deployment | [MODUL_12_PENUTUP.md](MODUL_12_PENUTUP.md) |

---

## Data Aktual Database `simset_rbtv`

### Pengguna (tabel `users`)
| ID | Nama | Email | Role |
|----|------|-------|------|
| 2 | Staff RBTV | staff@rbtv.id | staff |
| 3 | Admin Magang | magangrbtv@gmail.com | admin |
| 4 | reffki | reffkip@gmail.com | staff |

### Barang (tabel `barang`)
| Kode | Nama | Kategori | Status |
|------|------|----------|--------|
| BRG-001 | Kamera Sony A7 | Kamera | aktif |
| BRG-002 | Mic Wireless Rode | Audio | aktif |
| BRG-003 | printer epson l200 | Peralatan Kantor | aktif *(soft-deleted)* |

### Ruangan (tabel `ruangan`)
| ID | Nama | Lantai |
|----|------|--------|
| 1 | Studio 1 | Lantai 1 |
| 2 | Studio 2 | Lantai 2 |
| 3 | Ruang Editing | Lantai 1 |
| 4 | Ruang Redaksi | 5 |

### Aset (tabel `aset`)
| Kode | Barang | Ruangan | Kondisi | Status |
|------|--------|---------|---------|--------|
| AST-001 | Kamera Sony A7 | Ruang Editing | Baik | **Maintenance** |
| AST-002 | Kamera Sony A7 | Ruang Editing | Baik | Aktif |
| AST-003 | printer epson l200 | Ruang Redaksi | Baik | Aktif *(soft-deleted)* |

---

## Fitur Utama Sistem

- ✅ CRUD aset dengan foto, kondisi, status, dan informasi perolehan
- ✅ Auto-generate kode aset/barang dengan algoritma gap-filling
- ✅ QR code per aset (generate via qrserver.com API, cetak SVG, batch print, scanner web)
- ✅ Maintenance tracking dengan notifikasi email otomatis ke Admin
- ✅ Import massal dari Excel/CSV dengan validasi per baris
- ✅ Export ke Excel (styling profesional), PDF, dan CSV (UTF-8 BOM)
- ✅ Laporan aset, per ruangan, dan maintenance
- ✅ Dashboard dengan statistik real-time dan Chart.js
- ✅ Manajemen pengguna dengan role Admin/Staff (admin only)
- ✅ Audit log otomatis — 39 record aktual dari 3 pengguna
- ✅ Security headers dan CSRF protection

---

## Setup Cepat

```bash
# Clone dan install
git clone [repo-url] && cd simaset-rbtv
composer install && npm install && npm run build

# Setup environment
cp .env.example .env && php artisan key:generate
# Edit .env: DB_DATABASE=simset_rbtv, DB_USERNAME=root

# Buat database di MySQL
mysql -u root -e "CREATE DATABASE simset_rbtv CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Migrasi dan seed
php artisan migrate --seed

# Jalankan
php artisan serve
```

Akses di: `http://127.0.0.1:8000`
Login: `magangrbtv@gmail.com` / `Magang123`

---

*SimAset v1.0 — Kerja Praktik Teknik Informatika Universitas Bengkulu, 2026*
