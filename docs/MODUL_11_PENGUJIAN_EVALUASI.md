# MODUL 11 — PENGUJIAN SISTEM DAN EVALUASI
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 11.1 Pendahuluan

Pengujian sistem adalah tahap akhir yang sangat penting dalam pengembangan SimAset. Tahap ini memastikan bahwa seluruh fitur dan fungsi sistem berjalan sesuai dengan kebutuhan yang telah dirumuskan pada Modul 2, dan bahwa sistem memenuhi standar kualitas yang ditetapkan. Pengujian dilakukan secara sistematis menggunakan skenario yang mencakup semua modul fungsional, dengan menggunakan data aktual dari database `simset_rbtv` sebagai konteks pengujian.

Pengujian tidak hanya berfokus pada apakah sistem dapat dijalankan, tetapi juga pada aspek kualitas seperti keandalan validasi input, ketepatan logika bisnis, keamanan akses, dan kemudahan penggunaan.

---

## 11.2 Metode Pengujian

### 11.2.1 Blackbox Testing

Blackbox testing menguji fungsi-fungsi sistem dari perspektif pengguna akhir, tanpa memperhatikan struktur internal kode. Pengujian dilakukan dengan memberikan input tertentu dan mengamati apakah output yang dihasilkan sesuai dengan yang diharapkan.

**Keunggulan blackbox testing:**
- Menguji sistem dari sudut pandang pengguna yang sebenarnya
- Tidak memerlukan pengetahuan tentang implementasi internal
- Dapat menemukan bug yang tidak terdeteksi saat code review
- Memvalidasi bahwa semua kebutuhan fungsional terpenuhi

### 11.2.2 Usability Testing

Usability testing menguji kemudahan penggunaan sistem dari sudut pandang pengguna akhir. Pengujian dilakukan dengan meminta pengguna menyelesaikan tugas-tugas tertentu sambil mengamati kesulitan yang mereka hadapi.

---

## 11.3 Skenario Blackbox Testing Lengkap

### 11.3.1 Modul Autentikasi (9 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 1 | Login Admin valid | magangrbtv@gmail.com / Magang123 | Redirect ke /dashboard | ✅ |
| 2 | Login Staff valid | reffkip@gmail.com / (password) | Redirect ke /dashboard | ✅ |
| 3 | Login email tidak terdaftar | unknown@test.com / apapun | "Kredensial tidak cocok" | ✅ |
| 4 | Login password salah | magangrbtv@gmail.com / salah123 | "Kredensial tidak cocok" | ✅ |
| 5 | Login field email kosong | (kosong) / Magang123 | Error "email wajib diisi" | ✅ |
| 6 | Login field password kosong | magangrbtv@gmail.com / (kosong) | Error "password wajib diisi" | ✅ |
| 7 | Akses /dashboard tanpa login | GET /dashboard | Redirect ke /login | ✅ |
| 8 | Logout | Klik tombol Logout | Session dihapus, redirect /login | ✅ |
| 9 | Akses /dashboard setelah logout | GET /dashboard | Redirect ke /login | ✅ |

### 11.3.2 Modul Hak Akses (5 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 10 | Staff akses /users | Login reffki, GET /users | HTTP 403 Forbidden | ✅ |
| 11 | Staff akses /audit-log | Login reffki, GET /audit-log | HTTP 403 Forbidden | ✅ |
| 12 | Admin akses /users | Login Admin Magang, GET /users | Halaman daftar user tampil | ✅ |
| 13 | Admin akses /audit-log | Login Admin Magang, GET /audit-log | 39 record tampil | ✅ |
| 14 | Akses /aset/AST-001/detail tanpa login | GET /aset/AST-001/detail | Halaman detail tampil (publik) | ✅ |

### 11.3.3 Modul Manajemen Aset (17 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 15 | Tampilkan daftar aset | GET /aset | AST-001 (Maintenance) dan AST-002 (Aktif) tampil | ✅ |
| 16 | Filter status Maintenance | status=Maintenance | Hanya AST-001 tampil | ✅ |
| 17 | Filter status Aktif | status=Aktif | Hanya AST-002 tampil | ✅ |
| 18 | Filter kondisi Baik | kondisi=Baik | AST-001 dan AST-002 tampil | ✅ |
| 19 | Cari "Kamera" | search=Kamera | AST-001 dan AST-002 tampil | ✅ |
| 20 | Cari "ggG" (serial AST-001) | search=ggG | Hanya AST-001 tampil | ✅ |
| 21 | Tambah aset valid | BRG-001, Ruang Editing, Baik, Aktif, 2026-05-04 | Aset tersimpan dengan kode AST-004 | ✅ |
| 22 | Tambah aset tanpa kode barang | kode_barang kosong | Error "kode barang wajib diisi" | ✅ |
| 23 | Tambah aset kode barang tidak ada | kode_barang=BRG-999 | Error "tidak ditemukan di database" | ✅ |
| 24 | Tambah aset serial duplikat | serial_number=ggG (milik AST-001) | Error "serial number sudah terdaftar" | ✅ |
| 25 | Upload foto valid | File .jpg 500KB | Foto tersimpan di public/foto_aset/ | ✅ |
| 26 | Upload foto format salah | File .pdf | Error "format tidak valid" | ✅ |
| 27 | Upload foto terlalu besar | File .jpg 3MB | Error "ukuran melebihi 2MB" | ✅ |
| 28 | Lihat detail AST-001 | GET /aset/AST-001 | Detail lengkap: Kamera Sony A7, Ruang Editing, Maintenance | ✅ |
| 29 | Edit AST-002 ubah kondisi | kondisi=Rusak Ringan | Data terupdate, log Update tercatat | ✅ |
| 30 | Hapus AST-002 | DELETE /aset/AST-002 | Soft delete, tidak muncul di daftar | ✅ |
| 31 | Batch delete AST-001 + AST-002 | Centang keduanya, klik Hapus | 2 aset ter-soft-delete | ✅ |

### 11.3.4 Modul Master Data Barang (5 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 32 | Tampilkan daftar barang | GET /barang | BRG-001 dan BRG-002 tampil (BRG-003 tidak) | ✅ |
| 33 | Tambah barang valid | Nama, Komputer, aktif | Barang tersimpan dengan kode BRG-004 | ✅ |
| 34 | Tambah barang tanpa nama | nama_barang kosong | Error validasi | ✅ |
| 35 | Edit BRG-002 | Ubah nama | Data terupdate | ✅ |
| 36 | Hapus BRG-002 (tidak ada aset) | DELETE /barang/BRG-002 | Soft delete berhasil | ✅ |

### 11.3.5 Modul Master Data Ruangan (5 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 37 | Tampilkan daftar ruangan | GET /ruangan | 4 ruangan tampil dengan jumlah aset | ✅ |
| 38 | Tambah ruangan valid | Nama, Lantai 3 | Ruangan tersimpan | ✅ |
| 39 | Edit Ruang Redaksi | Ubah lantai | Data terupdate | ✅ |
| 40 | Hapus Ruang Editing (ada 2 aset) | DELETE /ruangan/3 | Error "masih memiliki 2 aset" | ✅ |
| 41 | Hapus Studio 1 (kosong) | DELETE /ruangan/1 | Ruangan terhapus | ✅ |

### 11.3.6 Modul QR Code (8 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 42 | Generate QR AST-001 (online) | Klik Generate QR | File PNG tersimpan di qr_codes/ | ✅ |
| 43 | Generate QR AST-001 (sudah ada) | Klik Generate QR lagi | "QR Code sudah ada" | ✅ |
| 44 | Generate QR (offline) | Tanpa internet | Error "Gagal generate QR Code" | ✅ |
| 45 | Cetak QR individual AST-001 | Klik Cetak QR | Halaman cetak terbuka, auto-print | ✅ |
| 46 | Batch print AST-001 + AST-002 | Pilih 2 aset, Print QR | Halaman batch print dengan 2 QR | ✅ |
| 47 | Scan QR AST-001 | Pindai QR code | Browser buka /aset/AST-001/detail | ✅ |
| 48 | Scanner web — AST-001 | Input kode AST-001 | Info: Kamera Sony A7, Maintenance | ✅ |
| 49 | Scanner web — kode tidak ada | Input AST-999 | "Aset tidak ditemukan" | ✅ |

### 11.3.7 Modul Maintenance (5 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 50 | Dashboard maintenance | GET /maintenance | AST-001 tampil, Total=1 | ✅ |
| 51 | Set AST-002 ke maintenance | POST /maintenance/AST-002/set | Status AST-002 → Maintenance | ✅ |
| 52 | Selesaikan maintenance AST-001 | kondisi=Baik, PATCH /maintenance/AST-001/complete | Status → Aktif, email terkirim | ✅ |
| 53 | Filter maintenance kondisi Baik | kondisi=Baik | AST-001 tampil | ✅ |
| 54 | Log maintenance tercatat | Cek audit log | Log Update maintenance tampil | ✅ |

### 11.3.8 Modul Import (6 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 55 | Import aset valid | CSV: BRG-001, Ruang Editing, Baik, Aktif | Aset tersimpan | ✅ |
| 56 | Import aset kode barang tidak ada | BRG-999 di kolom A | Error per baris dilaporkan | ✅ |
| 57 | Import file format salah | File .pdf | Error "File harus berformat Excel atau CSV" | ✅ |
| 58 | Import barang kode duplikat | BRG-001 (sudah ada) | Error "Kode Barang sudah ada" | ✅ |
| 59 | Download template aset | GET /import/template?type=aset | File CSV template terunduh | ✅ |
| 60 | Import campuran valid/invalid | 3 valid, 2 invalid | 3 berhasil, 2 error dilaporkan | ✅ |

### 11.3.9 Modul Export (5 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 61 | Export aset Excel tanpa filter | GET /export/aset/excel | File .xlsx dengan AST-001 dan AST-002 | ✅ |
| 62 | Export aset Excel filter Maintenance | status=Maintenance | File .xlsx hanya AST-001 | ✅ |
| 63 | Export aset PDF | GET /export/aset/pdf | File .pdf terunduh | ✅ |
| 64 | Export barang Excel | GET /export/barang/excel | File .xlsx BRG-001 dan BRG-002 | ✅ |
| 65 | Buka CSV di Excel | Buka file .csv | Karakter Indonesia terbaca benar | ✅ |

### 11.3.10 Modul Laporan (4 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 66 | Laporan aset PDF | GET /laporan/assets/cetak | PDF landscape dengan semua aset | ✅ |
| 67 | Laporan Ruang Editing PDF | GET /laporan/ruangan/3 | PDF dengan AST-001 dan AST-002 | ✅ |
| 68 | Laporan maintenance PDF | GET /laporan/maintenance/pdf | PDF dengan AST-001 | ✅ |
| 69 | Laporan maintenance CSV | GET /laporan/maintenance/csv | CSV dengan AST-001 | ✅ |

### 11.3.11 Modul Dashboard (5 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 70 | Tampilkan dashboard | GET /dashboard | Semua komponen tampil | ✅ |
| 71 | Statistik total aset | - | Total=2, Aktif=1, Maintenance=1 | ✅ |
| 72 | Statistik total barang | - | Total=2 (BRG-003 tidak dihitung) | ✅ |
| 73 | Chart distribusi kondisi | - | Chart tampil: Baik=2 | ✅ |
| 74 | Recent assets | - | AST-001 dan AST-002 tampil | ✅ |

### 11.3.12 Modul Manajemen Pengguna (7 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 75 | Tampilkan daftar user | GET /users | 3 user tampil | ✅ |
| 76 | Tambah user valid | Nama, email baru, Admin123, staff | User tersimpan | ✅ |
| 77 | Tambah user email duplikat | magangrbtv@gmail.com | Error "email sudah digunakan" | ✅ |
| 78 | Tambah user password lemah | "password" | Error validasi password | ✅ |
| 79 | Edit reffki tanpa ganti password | Kosongkan field password | Password tidak berubah | ✅ |
| 80 | Hapus Staff RBTV (id=2) | DELETE /users/2 | User terhapus | ✅ |
| 81 | Hapus akun sendiri (Admin Magang) | DELETE /users/3 | Error "Tidak bisa menghapus akun sendiri" | ✅ |

### 11.3.13 Modul Audit Log (4 Skenario)

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 82 | Tampilkan audit log | GET /audit-log | 39 record tampil, terbaru di atas | ✅ |
| 83 | Filter by user reffki | user_id=4 | Hanya log dari reffki (id=4) tampil | ✅ |
| 84 | Filter by aktivitas Create | module=Create | Log id=1 dan id=18 tampil | ✅ |
| 85 | Cari "AST-001" | search=AST-001 | Log id=17 (Update AST-001) tampil | ✅ |

---

## 11.4 Ringkasan Hasil Blackbox Testing

| Modul | Total Skenario | Berhasil | Gagal | Persentase |
|-------|---------------|----------|-------|------------|
| Autentikasi | 9 | 9 | 0 | 100% |
| Hak Akses | 5 | 5 | 0 | 100% |
| Manajemen Aset | 17 | 17 | 0 | 100% |
| Master Barang | 5 | 5 | 0 | 100% |
| Master Ruangan | 5 | 5 | 0 | 100% |
| QR Code | 8 | 8 | 0 | 100% |
| Maintenance | 5 | 5 | 0 | 100% |
| Import | 6 | 6 | 0 | 100% |
| Export | 5 | 5 | 0 | 100% |
| Laporan | 4 | 4 | 0 | 100% |
| Dashboard | 5 | 5 | 0 | 100% |
| Manajemen User | 7 | 7 | 0 | 100% |
| Audit Log | 4 | 4 | 0 | 100% |
| **Total** | **85** | **85** | **0** | **100%** |

> **[GAMBAR 11.1: Grafik batang hasil blackbox testing per modul, semua menunjukkan 100% berhasil]**

---

## 11.5 Usability Testing

### 11.5.1 Metode

Usability testing dilakukan dengan metode **think-aloud** — pengguna diminta menggunakan sistem sambil mengungkapkan pikiran mereka secara lisan. Pengujian dilakukan terhadap:
- 1 pengguna dengan latar belakang teknis (Admin)
- 2 pengguna tanpa latar belakang teknis (Staff)

### 11.5.2 Tugas yang Diberikan

1. Login ke sistem menggunakan akun yang diberikan
2. Tambah aset baru: Kamera Sony A7 (BRG-001) di Ruang Editing, kondisi Baik, status Aktif
3. Cari aset dengan kata kunci "Kamera"
4. Set aset AST-002 ke status Maintenance
5. Selesaikan maintenance AST-002 dengan kondisi akhir Baik
6. Export laporan aset ke Excel
7. Scan QR code aset menggunakan halaman scanner

### 11.5.3 Hasil Usability Testing

| Aspek | Penilaian | Catatan |
|-------|-----------|---------|
| Kemudahan navigasi | Baik | Menu sidebar jelas dan konsisten |
| Kemudahan pengisian form | Baik | Label dan placeholder informatif |
| Kejelasan pesan error | Baik | Pesan error spesifik per field |
| Kemudahan pencarian | Baik | Filter multi-kriteria mudah dipahami |
| Kemudahan QR code | Cukup | Pengguna non-teknis perlu panduan singkat |
| Responsivitas mobile | Cukup | Beberapa tabel perlu scroll horizontal di mobile |
| Kecepatan loading | Baik | Halaman loading dalam waktu wajar |
| Kejelasan status aset | Sangat Baik | Badge berwarna sangat membantu (merah=Maintenance, hijau=Aktif) |

> **[GAMBAR 11.2: Tampilan halaman daftar aset dengan badge status berwarna yang memudahkan identifikasi visual kondisi aset]**

---

## 11.6 Evaluasi Fungsional

| Kebutuhan Fungsional | Status |
|---------------------|--------|
| Autentikasi dan otorisasi berbasis role | ✅ Terpenuhi |
| CRUD aset dengan validasi lengkap | ✅ Terpenuhi |
| Auto-generate kode dengan gap-filling | ✅ Terpenuhi |
| Upload dan manajemen foto aset | ✅ Terpenuhi |
| Batch delete aset | ✅ Terpenuhi |
| CRUD master barang dan ruangan | ✅ Terpenuhi |
| Proteksi hapus ruangan berisi aset | ✅ Terpenuhi |
| Generate dan cetak QR code | ✅ Terpenuhi |
| Scanner QR code berbasis web | ✅ Terpenuhi |
| Halaman detail publik (tanpa login) | ✅ Terpenuhi |
| Maintenance tracking | ✅ Terpenuhi |
| Email notifikasi maintenance | ✅ Terpenuhi |
| Import massal dari Excel/CSV | ✅ Terpenuhi |
| Export ke Excel dengan styling | ✅ Terpenuhi |
| Export ke PDF | ✅ Terpenuhi |
| Export ke CSV dengan UTF-8 BOM | ✅ Terpenuhi |
| Laporan per ruangan PDF | ✅ Terpenuhi |
| Dashboard dengan statistik dan chart | ✅ Terpenuhi |
| Manajemen pengguna (admin only) | ✅ Terpenuhi |
| Audit log seluruh aktivitas | ✅ Terpenuhi |

---

## 11.7 Evaluasi Non-Fungsional

| Aspek | Evaluasi |
|-------|----------|
| **Keamanan** | Security headers diterapkan ke semua response, CSRF protection aktif, password di-hash bcrypt, role-based access control berfungsi, rate limiting mencegah brute force |
| **Kemudahan Penggunaan** | Antarmuka intuitif dengan navigasi konsisten, pesan error spesifik per field, badge berwarna untuk status aset, konfirmasi sebelum operasi destruktif |
| **Kinerja** | Pagination 15 item mencegah loading berlebihan, eager loading mengurangi query N+1, index database pada kolom yang sering difilter (status, kode_barang, ruangan_id) |
| **Keandalan** | Validasi input ketat di semua form, soft delete mencegah kehilangan data, error handling di semua operasi kritis, logging error ke laravel.log |
| **Pemeliharaan** | Kode terstruktur MVC, 14 migration terdokumentasi, seeder dapat direproduksi, komentar kode pada bagian kompleks |
| **Kompatibilitas** | Berjalan di Chrome/Firefox/Edge/Safari, export Excel kompatibel dengan Microsoft Excel, QR code dapat dipindai oleh scanner standar |

---

## 11.8 Kesimpulan Modul

Modul 11 ini telah membahas pengujian dan evaluasi SimAset secara menyeluruh. Blackbox testing dengan 85 skenario yang mencakup semua modul fungsional menunjukkan bahwa seluruh fitur sistem berjalan sesuai dengan perancangan — 100% skenario berhasil. Usability testing menunjukkan bahwa sistem mudah digunakan dengan beberapa area yang dapat ditingkatkan (panduan QR code untuk pengguna non-teknis, optimasi tampilan mobile).

Berdasarkan hasil pengujian dan evaluasi, SimAset dinyatakan **siap digunakan** sebagai sistem informasi manajemen aset RBTV Bengkulu.

---

*Kembali ke: [Modul 10 — Audit Log dan Manajemen Pengguna](MODUL_10_AUDIT_LOG_USER.md)*
*Lanjut ke: [Modul 12 — Penutup dan Pengembangan Lanjutan](MODUL_12_PENUTUP.md)*

---

## 11.3 Skenario Blackbox Testing Lengkap

### 11.3.1 Modul Autentikasi

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 1 | Login Admin valid | magangrbtv@gmail.com / Magang123 | Redirect ke /dashboard | Berhasil |
| 2 | Login Staff valid | reffkip@gmail.com / password | Redirect ke /dashboard | Berhasil |
| 3 | Login email tidak terdaftar | unknown@test.com / apapun | "Kredensial tidak cocok" | Berhasil |
| 4 | Login password salah | magangrbtv@gmail.com / salah | "Kredensial tidak cocok" | Berhasil |
| 5 | Login field email kosong | (kosong) / Magang123 | Error validasi email wajib | Berhasil |
| 6 | Login field password kosong | magangrbtv@gmail.com / (kosong) | Error validasi password wajib | Berhasil |
| 7 | Akses /dashboard tanpa login | GET /dashboard | Redirect ke /login | Berhasil |
| 8 | Logout | Klik tombol Logout | Session dihapus, redirect /login | Berhasil |
| 9 | Akses /dashboard setelah logout | GET /dashboard | Redirect ke /login | Berhasil |

> **[GAMBAR 11.1: Tampilan pesan error login saat kredensial salah]**

### 11.3.2 Modul Hak Akses

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 10 | Staff akses /users | Login reffki, GET /users | HTTP 403 Forbidden | Berhasil |
| 11 | Staff akses /audit-log | Login reffki, GET /audit-log | HTTP 403 Forbidden | Berhasil |
| 12 | Admin akses /users | Login Admin Magang, GET /users | Halaman daftar user tampil | Berhasil |
| 13 | Admin akses /audit-log | Login Admin Magang | 39 record tampil | Berhasil |
| 14 | Akses /aset/AST-001/detail tanpa login | GET /aset/AST-001/detail | Halaman detail tampil (publik) | Berhasil |

### 11.3.3 Modul Manajemen Aset

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 15 | Tampilkan daftar aset | GET /aset | AST-001 (Maintenance) dan AST-002 (Aktif) tampil | Berhasil |
| 16 | Filter status Maintenance | status=Maintenance | Hanya AST-001 tampil | Berhasil |
| 17 | Filter status Aktif | status=Aktif | Hanya AST-002 tampil | Berhasil |
| 18 | Filter kondisi Baik | kondisi=Baik | AST-001 dan AST-002 tampil | Berhasil |
| 19 | Cari "Kamera" | search=Kamera | AST-001 dan AST-002 tampil | Berhasil |
| 20 | Cari serial "ggG" | search=ggG | Hanya AST-001 tampil | Berhasil |
| 21 | Tambah aset valid | BRG-001, Ruang Editing, Baik, Aktif, 2026-05-04 | Aset tersimpan kode AST-004 | Berhasil |
| 22 | Tambah aset tanpa kode barang | kode_barang kosong | Error validasi | Berhasil |
| 23 | Tambah aset kode barang tidak ada | kode_barang=BRG-999 | Error "tidak ditemukan" | Berhasil |
| 24 | Tambah aset serial duplikat | serial_number=ggG (milik AST-001) | Error "sudah terdaftar" | Berhasil |
| 25 | Upload foto valid | File .jpg 500KB | Foto tersimpan di public/foto_aset/ | Berhasil |
| 26 | Upload foto format salah | File .pdf | Error "format tidak valid" | Berhasil |
| 27 | Upload foto terlalu besar | File .jpg 3MB | Error "ukuran melebihi 2MB" | Berhasil |
| 28 | Lihat detail AST-001 | GET /aset/AST-001 | Detail: Kamera Sony A7, Ruang Editing, Maintenance | Berhasil |
| 29 | Edit AST-002 ubah kondisi | kondisi=Rusak Ringan | Data terupdate, log Update tercatat | Berhasil |
| 30 | Hapus AST-002 | DELETE /aset/AST-002 | Soft delete, tidak muncul di daftar | Berhasil |
| 31 | Batch delete | Centang AST-001+AST-002, hapus | 2 aset ter-soft-delete | Berhasil |

> **[GAMBAR 11.2: Tampilan halaman daftar aset dengan filter aktif menampilkan hasil pencarian]**

### 11.3.4 Modul Master Barang

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 32 | Tampilkan daftar barang | GET /barang | BRG-001 dan BRG-002 tampil (BRG-003 tidak) | Berhasil |
| 33 | Tambah barang valid | Nama, Komputer, aktif | Barang tersimpan kode BRG-004 | Berhasil |
| 34 | Tambah barang tanpa nama | nama_barang kosong | Error validasi | Berhasil |
| 35 | Edit BRG-002 | Ubah nama | Data terupdate | Berhasil |
| 36 | Hapus BRG-002 (tidak ada aset) | DELETE /barang/BRG-002 | Soft delete berhasil | Berhasil |

### 11.3.5 Modul Master Ruangan

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 37 | Tampilkan daftar ruangan | GET /ruangan | 4 ruangan tampil dengan jumlah aset | Berhasil |
| 38 | Tambah ruangan valid | Nama, Lantai 3 | Ruangan tersimpan | Berhasil |
| 39 | Edit Ruang Redaksi | Ubah lantai | Data terupdate | Berhasil |
| 40 | Hapus Ruang Editing (ada 2 aset) | DELETE /ruangan/3 | Error "masih memiliki 2 aset" | Berhasil |
| 41 | Hapus Studio 1 (kosong) | DELETE /ruangan/1 | Ruangan terhapus | Berhasil |

> **[GAMBAR 11.3: Tampilan pesan error saat mencoba hapus Ruang Editing yang masih memiliki 2 aset]**

### 11.3.6 Modul QR Code

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 42 | Generate QR AST-001 (online) | Klik Generate QR | File PNG tersimpan di qr_codes/ | Berhasil |
| 43 | Generate QR AST-001 (sudah ada) | Klik Generate QR lagi | "QR Code sudah ada" | Berhasil |
| 44 | Generate QR (offline) | Tanpa internet | Error "Gagal generate QR Code" | Berhasil |
| 45 | Cetak QR individual AST-001 | Klik Cetak QR | Halaman cetak terbuka, auto-print | Berhasil |
| 46 | Batch print AST-001+AST-002 | Pilih 2 aset, Print QR | Halaman batch print dengan 2 QR | Berhasil |
| 47 | Scan QR AST-001 | Pindai QR code | Browser buka /aset/AST-001/detail | Berhasil |
| 48 | Scanner web — AST-001 | Input kode AST-001 | Info: Kamera Sony A7, Maintenance | Berhasil |
| 49 | Scanner web — kode tidak ada | Input AST-999 | "Aset tidak ditemukan" | Berhasil |

### 11.3.7 Modul Maintenance

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 50 | Dashboard maintenance | GET /maintenance | AST-001 tampil, Total=1 | Berhasil |
| 51 | Set AST-002 ke maintenance | POST /maintenance/AST-002/set | Status AST-002 → Maintenance | Berhasil |
| 52 | Selesaikan maintenance AST-001 | kondisi=Baik, PATCH /maintenance/AST-001/complete | Status → Aktif, email terkirim | Berhasil |
| 53 | Filter maintenance kondisi Baik | kondisi=Baik | AST-001 tampil | Berhasil |
| 54 | Log maintenance tercatat | Cek audit log | Log Update maintenance tampil | Berhasil |

### 11.3.8 Modul Import

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 55 | Import aset valid | CSV: BRG-001, Ruang Editing, Baik, Aktif | Aset tersimpan | Berhasil |
| 56 | Import aset kode barang tidak ada | BRG-999 di kolom A | Error per baris dilaporkan | Berhasil |
| 57 | Import file format salah | File .pdf | Error "File harus berformat Excel atau CSV" | Berhasil |
| 58 | Import barang kode duplikat | BRG-001 (sudah ada) | Error "Kode Barang sudah ada" | Berhasil |
| 59 | Download template aset | GET /import/template?type=aset | File CSV template terunduh | Berhasil |
| 60 | Import campuran valid/invalid | 3 valid, 2 invalid | 3 berhasil, 2 error dilaporkan | Berhasil |

> **[GAMBAR 11.4: Tampilan hasil import dengan pesan "Berhasil import 3 data aset" dan daftar error baris yang gagal]**

### 11.3.9 Modul Export

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 61 | Export aset Excel tanpa filter | GET /export/aset/excel | File .xlsx dengan AST-001 dan AST-002 | Berhasil |
| 62 | Export aset Excel filter Maintenance | status=Maintenance | File .xlsx hanya AST-001 | Berhasil |
| 63 | Export aset PDF | GET /export/aset/pdf | File .pdf terunduh | Berhasil |
| 64 | Export barang Excel | GET /export/barang/excel | File .xlsx BRG-001 dan BRG-002 | Berhasil |
| 65 | Buka CSV di Excel | Buka file .csv | Karakter Indonesia terbaca benar | Berhasil |

### 11.3.10 Modul Laporan

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 66 | Laporan aset PDF | GET /laporan/assets/cetak | PDF landscape dengan semua aset | Berhasil |
| 67 | Laporan Ruang Editing PDF | GET /laporan/ruangan/3 | PDF dengan AST-001 dan AST-002 | Berhasil |
| 68 | Laporan maintenance PDF | GET /laporan/maintenance/pdf | PDF dengan AST-001 | Berhasil |
| 69 | Laporan maintenance CSV | GET /laporan/maintenance/csv | CSV dengan AST-001 | Berhasil |

> **[GAMBAR 11.5: Contoh laporan aset PDF landscape dengan header RBTV dan tabel data aset]**

### 11.3.11 Modul Dashboard

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 70 | Tampilkan dashboard | GET /dashboard | Semua komponen tampil | Berhasil |
| 71 | Statistik total aset | - | Total=2, Aktif=1, Maintenance=1 | Berhasil |
| 72 | Statistik total barang | - | Total=2 (BRG-003 tidak dihitung) | Berhasil |
| 73 | Chart distribusi kondisi | - | Chart tampil: Baik=2 | Berhasil |
| 74 | Recent assets | - | AST-001 dan AST-002 tampil | Berhasil |

### 11.3.12 Modul Manajemen Pengguna

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 75 | Tampilkan daftar user | GET /users | 3 user tampil | Berhasil |
| 76 | Tambah user valid | Nama, email baru, Admin123, staff | User tersimpan | Berhasil |
| 77 | Tambah user email duplikat | magangrbtv@gmail.com | Error "email sudah digunakan" | Berhasil |
| 78 | Tambah user password lemah | "password" | Error validasi password | Berhasil |
| 79 | Edit reffki tanpa ganti password | Kosongkan field password | Password tidak berubah | Berhasil |
| 80 | Hapus Staff RBTV (id=2) | DELETE /users/2 | User terhapus | Berhasil |
| 81 | Hapus akun sendiri (Admin Magang) | DELETE /users/3 | Error "Tidak bisa menghapus akun sendiri" | Berhasil |

### 11.3.13 Modul Audit Log

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 82 | Tampilkan audit log | GET /audit-log | 39 record tampil, terbaru di atas | Berhasil |
| 83 | Filter by user reffki | user_id=4 | Hanya log dari reffki tampil | Berhasil |
| 84 | Filter by aktivitas Create | module=Create | Log id=1 dan id=18 tampil | Berhasil |
| 85 | Cari "AST-001" | search=AST-001 | Log id=17 (Update AST-001) tampil | Berhasil |

---

## 11.4 Ringkasan Hasil Blackbox Testing

| Modul | Total Skenario | Berhasil | Gagal | Persentase |
|-------|---------------|----------|-------|------------|
| Autentikasi | 9 | 9 | 0 | 100% |
| Hak Akses | 5 | 5 | 0 | 100% |
| Manajemen Aset | 17 | 17 | 0 | 100% |
| Master Barang | 5 | 5 | 0 | 100% |
| Master Ruangan | 5 | 5 | 0 | 100% |
| QR Code | 8 | 8 | 0 | 100% |
| Maintenance | 5 | 5 | 0 | 100% |
| Import | 6 | 6 | 0 | 100% |
| Export | 5 | 5 | 0 | 100% |
| Laporan | 4 | 4 | 0 | 100% |
| Dashboard | 5 | 5 | 0 | 100% |
| Manajemen User | 7 | 7 | 0 | 100% |
| Audit Log | 4 | 4 | 0 | 100% |
| **TOTAL** | **85** | **85** | **0** | **100%** |

> **[GAMBAR 11.6: Grafik batang hasil blackbox testing per modul, semua menunjukkan 100% berhasil]**

---

## 11.5 Usability Testing

### 11.5.1 Metode

Usability testing dilakukan dengan metode **think-aloud** — pengguna diminta menggunakan sistem sambil mengungkapkan pikiran mereka secara lisan. Pengujian dilakukan terhadap 3 pengguna: 1 Admin dan 2 Staff dengan latar belakang teknis yang berbeda.

### 11.5.2 Tugas yang Diberikan

1. Login ke sistem menggunakan akun yang diberikan
2. Tambah aset baru: Kamera Sony A7 (BRG-001) di Ruang Editing, kondisi Baik, status Aktif
3. Cari aset dengan kata kunci "Kamera"
4. Set aset AST-002 ke status Maintenance
5. Selesaikan maintenance AST-002 dengan kondisi akhir Baik
6. Export laporan aset ke Excel
7. Scan QR code aset menggunakan halaman scanner

### 11.5.3 Hasil Usability Testing

| Aspek | Penilaian | Catatan |
|-------|-----------|---------|
| Kemudahan navigasi | Baik | Menu sidebar jelas dan konsisten |
| Kemudahan pengisian form | Baik | Label dan placeholder informatif |
| Kejelasan pesan error | Baik | Pesan error spesifik per field |
| Kemudahan pencarian | Baik | Filter multi-kriteria mudah dipahami |
| Kemudahan QR code | Cukup | Pengguna non-teknis perlu panduan singkat |
| Responsivitas mobile | Cukup | Beberapa tabel perlu scroll horizontal |
| Kecepatan loading | Baik | Halaman loading dalam waktu wajar |
| Kejelasan status aset | Sangat Baik | Badge berwarna sangat membantu |

> **[GAMBAR 11.7: Grafik radar hasil usability testing menampilkan skor per aspek]**

---

## 11.6 Evaluasi Fungsional

| Kebutuhan Fungsional | Status |
|---------------------|--------|
| Autentikasi dan otorisasi berbasis role | Terpenuhi |
| CRUD aset dengan validasi lengkap | Terpenuhi |
| Auto-generate kode dengan gap-filling | Terpenuhi |
| Upload dan manajemen foto aset | Terpenuhi |
| Batch delete aset | Terpenuhi |
| CRUD master barang dan ruangan | Terpenuhi |
| Proteksi hapus ruangan berisi aset | Terpenuhi |
| Generate dan cetak QR code | Terpenuhi |
| Scanner QR code berbasis web | Terpenuhi |
| Halaman detail publik (tanpa login) | Terpenuhi |
| Maintenance tracking | Terpenuhi |
| Email notifikasi maintenance | Terpenuhi |
| Import massal dari Excel/CSV | Terpenuhi |
| Export ke Excel dengan styling | Terpenuhi |
| Export ke PDF | Terpenuhi |
| Export ke CSV dengan UTF-8 BOM | Terpenuhi |
| Laporan per ruangan PDF | Terpenuhi |
| Dashboard dengan statistik dan chart | Terpenuhi |
| Manajemen pengguna (admin only) | Terpenuhi |
| Audit log seluruh aktivitas | Terpenuhi |

---

## 11.7 Evaluasi Non-Fungsional

| Aspek | Evaluasi |
|-------|----------|
| Keamanan | Security headers, CSRF, bcrypt, role-based access, rate limiting |
| Kemudahan Penggunaan | Antarmuka intuitif, badge berwarna, konfirmasi sebelum hapus |
| Kinerja | Pagination 15 item, eager loading, index database pada kolom status |
| Keandalan | Validasi ketat, soft delete, error handling, logging |
| Pemeliharaan | MVC terstruktur, 14 migration terdokumentasi, seeder reproducible |
| Kompatibilitas | Chrome/Firefox/Edge/Safari, Excel kompatibel, QR scanner standar |

---

## 11.8 Kesimpulan Modul

Pengujian blackbox dengan 85 skenario menunjukkan 100% berhasil. Usability testing menunjukkan sistem mudah digunakan dengan beberapa area yang dapat ditingkatkan. Berdasarkan hasil pengujian dan evaluasi, SimAset dinyatakan **siap digunakan** sebagai sistem informasi manajemen aset RBTV Bengkulu.

---

*Kembali ke: [Modul 10](MODUL_10_AUDIT_LOG_USER.md)*
*Lanjut ke: [Modul 12](MODUL_12_PENUTUP.md)*
