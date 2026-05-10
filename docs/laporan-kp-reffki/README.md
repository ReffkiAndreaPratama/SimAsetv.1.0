# Laporan Kerja Praktik — Reffki Andrea Pratama

## Rancang Bangun Sistem Informasi Manajemen Aset Barang Kantor Berbasis Web pada Rakyat Bengkulu Televisi (RBTV)

**Program Studi Informatika — Fakultas Teknik — Universitas Bengkulu — 2025/2026**

---

## Identitas Mahasiswa

| | |
|--|--|
| **Nama** | Reffki Andrea Pratama |
| **NPM** | G1A023039 |
| **Program Studi** | Informatika |
| **Fakultas** | Teknik |
| **Universitas** | Universitas Bengkulu |
| **Tempat KP** | Rakyat Bengkulu Televisi (RBTV) |

---

## Struktur Dokumen

| File | Isi |
|------|-----|
| [00_COVER.md](00_COVER.md) | Halaman Judul |
| [01_HALAMAN_PENGESAHAN.md](01_HALAMAN_PENGESAHAN.md) | Halaman Pengesahan |
| [02_DAFTAR_ISI.md](02_DAFTAR_ISI.md) | Daftar Isi |
| [02b_KATA_PENGANTAR.md](02b_KATA_PENGANTAR.md) | Kata Pengantar |
| [03_DAFTAR_GAMBAR.md](03_DAFTAR_GAMBAR.md) | Daftar Gambar |
| [04_DAFTAR_TABEL.md](04_DAFTAR_TABEL.md) | Daftar Tabel |
| [05_DAFTAR_ISTILAH.md](05_DAFTAR_ISTILAH.md) | Daftar Istilah / Glosarium |
| [06_BAB1_PENDAHULUAN.md](06_BAB1_PENDAHULUAN.md) | BAB I — Pendahuluan |
| [07_BAB2_TINJAUAN_PUSTAKA.md](07_BAB2_TINJAUAN_PUSTAKA.md) | BAB II — Tinjauan Pustaka & Landasan Teori |
| [08_BAB3_ANALISIS_PERANCANGAN.md](08_BAB3_ANALISIS_PERANCANGAN.md) | BAB III — Analisis Kebutuhan & Perancangan |
| [09_BAB4_IMPLEMENTASI.md](09_BAB4_IMPLEMENTASI.md) | BAB IV — Implementasi & Pengujian |
| [10_BAB5_KESIMPULAN.md](10_BAB5_KESIMPULAN.md) | BAB V — Kesimpulan & Saran |
| [11_DAFTAR_PUSTAKA.md](11_DAFTAR_PUSTAKA.md) | Daftar Pustaka |
| [12_LAMPIRAN.md](12_LAMPIRAN.md) | Lampiran (Logbook, Kuesioner, Source Code) |

---

## Ringkasan Sistem yang Dibangun

**Nama Sistem:** SimAset (Sistem Informasi Manajemen Aset)
**Versi:** v1.0
**Instansi:** Rakyat Bengkulu Televisi (RBTV) Bengkulu

### Tech Stack

| Layer | Teknologi |
|-------|-----------|
| Backend | Laravel 12 (PHP 8.2) |
| Frontend | Tailwind CSS + Alpine.js + Bootstrap 5 |
| Database | SQLite (dev) / MySQL (prod) |
| Authentication | Laravel Breeze (session-based) |
| Export | DomPDF + Maatwebsite Excel |
| QR Code | SimpleSoftwareIO/simple-qrcode |
| Charts | Chart.js |
| Build Tool | Vite |

### Modul Sistem

| No | Modul | Akses |
|----|-------|-------|
| 1 | Dashboard (statistik, grafik, aset terbaru) | Admin, Staff |
| 2 | Manajemen Aset (CRUD, batch delete, foto, filter) | Admin, Staff |
| 3 | Manajemen Barang (master data) | Admin, Staff |
| 4 | Manajemen Ruangan (master data) | Admin, Staff |
| 5 | QR Code (generate, scanner, batch print) | Admin, Staff |
| 6 | Maintenance (set, complete, notifikasi email) | Admin, Staff |
| 7 | Import Data (Excel/CSV) | Admin, Staff |
| 8 | Export Data (Excel/PDF) | Admin, Staff |
| 9 | Laporan (aset, ruangan, maintenance) | Admin, Staff |
| 10 | Manajemen Pengguna (CRUD, role) | Admin only |
| 11 | Audit Log (seluruh aktivitas) | Admin only |
| 12 | Profil (edit profil, ubah password) | Admin, Staff |

### Hasil Pengujian

| Kelompok Responden | Rata-rata Skor | Kategori |
|-------------------|---------------|----------|
| User/Staff (12 responden) | 4.61 | Sangat Layak |
| Admin (1 responden) | 4.65 | Sangat Layak |
