# MODUL PENGGUNAAN
## SimAset — Sistem Manajemen Aset RBTV Bengkulu
### Versi 1.0 · Mei 2026

---

## DAFTAR ISI

1. [Deskripsi Sistem](#1-deskripsi-sistem)
2. [Login](#2-login)
3. [Lupa Password & Reset Password](#3-lupa-password--reset-password)
4. [Dashboard](#4-dashboard) — `👤 Admin & Staff`
5. [Kelola Aset](#5-kelola-aset) — `👤 Admin & Staff`
6. [Kelola Barang](#6-kelola-barang) — `👤 Admin & Staff`
7. [Kelola Ruangan](#7-kelola-ruangan) — `👤 Admin & Staff`
8. [Kelola Pengguna](#8-kelola-pengguna) — `🔒 Admin saja`
9. [QR Code](#9-qr-code) — `👤 Admin & Staff`
10. [Maintenance](#10-maintenance) — `👤 Admin & Staff`
11. [Laporan, Export & Import](#11-laporan-export--import) — `👤 Admin & Staff`
12. [Audit Log](#12-audit-log) — `🔒 Admin saja`
13. [Profil & Ganti Password](#13-profil--ganti-password) — `👤 Admin & Staff`
14. [Logout](#14-logout)
15. [Hak Akses per Role](#15-hak-akses-per-role)
16. [Dampak Sistem](#16-dampak-sistem)
17. [Pesan Error Umum](#17-pesan-error-umum)

---

## 1. DESKRIPSI SISTEM

**SimAset** adalah aplikasi web yang dikembangkan untuk mendukung pengelolaan aset barang kantor RBTV Bengkulu secara digital, terpusat, dan terstruktur. Sistem ini dibangun menggunakan framework **Laravel** dan dapat diakses melalui browser dari perangkat apa pun — komputer, laptop, maupun smartphone.

Sebelum adanya SimAset, pencatatan aset dilakukan secara manual menggunakan dokumen fisik atau spreadsheet yang rentan terhadap kesalahan dan kehilangan data. SimAset hadir untuk menggantikan proses tersebut dengan sistem yang lebih andal dan mudah digunakan.

### Ruang Lingkup

| No | Fitur | Keterangan |
|----|-------|-----------|
| 1 | Manajemen Aset | Catat, pantau, dan kelola seluruh aset kantor |
| 2 | Manajemen Barang & Ruangan | Master data jenis barang dan lokasi |
| 3 | QR Code | Identifikasi aset via scan QR |
| 4 | Maintenance | Lacak dan kelola perawatan aset |
| 5 | Laporan & Export | Cetak laporan PDF, export Excel/CSV |
| 6 | Import Massal | Upload data dari file Excel/CSV |
| 7 | Audit Log | Rekam jejak seluruh aktivitas pengguna |
| 8 | Manajemen Pengguna | Kelola akun Admin dan Staff |

### Kebutuhan Akses

- Jaringan internet aktif
- Browser modern — Chrome, Firefox, atau Edge (versi terbaru)
- Akun yang dibuat oleh Admin (tidak ada registrasi mandiri)

### Struktur Role

| Role | Akses |
|------|-------|
| **Staff** | Semua fitur operasional — aset, barang, ruangan, QR, maintenance, laporan, export, import |
| **Admin** | Semua yang bisa dilakukan Staff, **ditambah** kelola pengguna dan audit log |

---

## 2. LOGIN

> **[Gambar 1 — Halaman Login]**

1. Buka URL sistem di browser
2. Masukkan **Email** dan **Password**
3. Centang **"Ingat Saya"** jika ingin sesi tetap aktif
4. Klik **"Masuk"**

Sistem mencatat waktu login dan mengarahkan ke Dashboard.

**Akun default (seeder):**

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@rbtv.co.id | Admin123 |
| Staff | staff@rbtv.co.id | Staff123 |

**Jika login gagal:**

| Pesan | Penyebab | Solusi |
|-------|----------|--------|
| "These credentials do not match" | Email atau password salah | Periksa kembali atau gunakan Lupa Password |
| "Akun Anda belum aktif" | Akun dinonaktifkan Admin | Hubungi Admin |

---

## 3. LUPA PASSWORD & RESET PASSWORD

> **[Gambar 2 — Halaman Forgot Password]**
> **[Gambar 3 — Email Reset Password yang Diterima]**
> **[Gambar 4 — Halaman Buat Password Baru]**

### Langkah 1 — Minta Link Reset
1. Di halaman login, klik **"Lupa Password?"**
2. Masukkan **email** yang terdaftar
3. Klik **"Email Password Reset Link"**
4. Cek kotak masuk email (termasuk folder Spam)

### Langkah 2 — Buat Password Baru
1. Klik tombol **"Buat Password Baru"** di email
2. Isi **Password Baru** dan **Konfirmasi Password Baru**
3. Klik **"Reset Password"**

**Syarat password:** minimal 8 karakter, mengandung huruf besar, huruf kecil, dan angka.

> Tautan reset hanya berlaku **60 menit**. Jika kedaluwarsa, ulangi dari Langkah 1.

---

## 4. DASHBOARD

> 👤 **Dapat diakses oleh: Admin & Staff**

> **[Gambar 5 — Tampilan Dashboard]**

Halaman utama setelah login. Menampilkan ringkasan kondisi aset secara real-time.

### Kartu Statistik

| Kartu | Isi |
|-------|-----|
| Total Aset | Jumlah seluruh aset tercatat |
| Aset Aktif | Aset berstatus Aktif |
| Aset Non-Aktif | Aset berstatus Non-Aktif |
| Aset Maintenance | Aset sedang dalam perawatan |
| Aset Rusak | Kondisi Rusak Ringan + Rusak Berat |
| Total Barang | Jumlah jenis barang di katalog |
| Total Ruangan | Jumlah ruangan terdaftar |
| Aset Bulan Ini | Aset yang ditambahkan bulan berjalan |

### Grafik
- **Distribusi Kondisi** — Pie chart kondisi seluruh aset
- **Distribusi Kategori** — Bar chart 5 kategori aset terbanyak

### Tabel Aset Terbaru
10 aset yang paling baru ditambahkan beserta kode, nama barang, ruangan, status, kondisi, dan tanggal.

---

## 5. KELOLA ASET

> 👤 **Dapat diakses oleh: Admin & Staff**

### Daftar Aset

> **[Gambar 6 — Halaman Daftar Aset]**

- Tabel menampilkan semua aset, 15 data per halaman
- **Pencarian:** kode aset, serial number, nama barang, nama ruangan
- **Filter:** Status, Kondisi, Kategori — bisa dikombinasikan

### Tambah Aset Baru

> **[Gambar 7 — Form Tambah Aset]**

1. Klik **"+ Tambah Aset"**
2. Isi formulir:

| Field | Keterangan | Wajib |
|-------|-----------|:-----:|
| Nama Barang | Pilih dari katalog (dropdown) | ✓ |
| Ruangan | Pilih lokasi aset (dropdown) | ✓ |
| Kondisi | Baik / Rusak Ringan / Rusak Berat | ✓ |
| Status | Aktif / Maintenance / Non-Aktif | ✓ |
| Tanggal Perolehan | Format YYYY-MM-DD | ✓ |
| Serial Number | Nomor seri unik perangkat | — |
| Jumlah | Default: 1 | — |
| Harga Perolehan | Nilai aset (angka) | — |
| Sumber Perolehan | Pembelian / Hibah / Sumbangan / Pinjaman / Lainnya | — |
| Keterangan | Catatan tambahan | — |
| Foto Aset | JPG/PNG/GIF, maks. 2 MB | — |

3. Klik **"Simpan"** — Kode Aset dibuat otomatis (format: AST-001, AST-002, dst.)

### Edit Aset

> **[Gambar 8 — Form Edit Aset]**

1. Klik tombol **Edit** di baris aset
2. Ubah data yang diperlukan
3. Untuk ganti foto: upload foto baru, atau centang **"Hapus Foto"**
4. Klik **"Simpan Perubahan"**

### Hapus Aset

1. Klik tombol **Hapus** di baris aset → konfirmasi dialog
2. Data dihapus secara *soft delete* — tersimpan di database, tidak tampil di daftar

### Hapus Massal

1. Centang beberapa baris aset
2. Klik **"Hapus Terpilih"** → konfirmasi

### Detail Aset

> **[Gambar 9 — Halaman Detail Aset]**

Klik kode aset atau tombol **Detail** untuk melihat informasi lengkap, foto, QR code, dan tombol aksi (Edit, Generate QR, Set Maintenance).

---

## 6. KELOLA BARANG

> 👤 **Dapat diakses oleh: Admin & Staff**

> **[Gambar 10 — Halaman Daftar Barang]**

Barang adalah master data jenis barang. Setiap aset harus terhubung ke satu jenis barang.

### Tambah Barang

> **[Gambar 11 — Form Tambah Barang]**

1. Klik **"+ Tambah Barang"**
2. Isi formulir:

| Field | Keterangan | Wajib |
|-------|-----------|:-----:|
| Kode Barang | Kode unik, contoh: BRG-001 | ✓ |
| Nama Barang | Nama jenis barang | ✓ |
| Kategori | Kamera / Audio / Komputer / Lighting / Furniture / Peralatan Kantor / Lainnya | ✓ |
| Status | aktif / nonaktif | ✓ |
| Keterangan | Deskripsi tambahan | — |

3. Klik **"Simpan"**

### Edit & Hapus Barang

- **Edit:** klik Edit → ubah data → Simpan
- **Hapus:** klik Hapus → konfirmasi

> Barang tidak bisa dihapus jika masih ada aset yang menggunakannya.

### Detail Barang

> **[Gambar 12 — Halaman Detail Barang]**

Klik **Detail** untuk melihat daftar aset yang menggunakan barang tersebut.

---

## 7. KELOLA RUANGAN

> 👤 **Dapat diakses oleh: Admin & Staff**

> **[Gambar 13 — Halaman Daftar Ruangan]**

Ruangan adalah master data lokasi penyimpanan aset.

### Tambah Ruangan

> **[Gambar 14 — Form Tambah Ruangan]**

1. Klik **"+ Tambah Ruangan"**
2. Isi formulir:

| Field | Keterangan | Wajib |
|-------|-----------|:-----:|
| Nama Ruangan | Nama ruangan | ✓ |
| Lantai | Nomor/nama lantai | — |
| Keterangan | Fungsi atau lokasi detail | — |

3. Klik **"Simpan"**

### Aset per Ruangan

> **[Gambar 15 — Halaman Detail Ruangan]**

Klik **Detail** untuk melihat daftar seluruh aset di ruangan tersebut.

---

## 8. KELOLA PENGGUNA

> 🔒 **Dapat diakses oleh: Admin saja**

> **[Gambar 16 — Halaman Daftar Pengguna]**

### Tambah Pengguna

> **[Gambar 17 — Form Tambah Pengguna]**

1. Klik **"+ Tambah Pengguna"**
2. Isi formulir:

| Field | Keterangan | Wajib |
|-------|-----------|:-----:|
| Nama | Nama lengkap | ✓ |
| Email | Alamat email unik | ✓ |
| Password | Min. 8 karakter, huruf besar+kecil+angka | ✓ |
| Role | Admin / Staff | ✓ |
| Status | Aktif / Nonaktif | ✓ |
| Kirim Email | Kirim notifikasi akun ke email pengguna | — |

3. Klik **"Tambah"**

Jika **"Kirim Email"** dicentang, sistem otomatis mengirim email berisi informasi akun ke pengguna baru.

### Edit Pengguna

> **[Gambar 18 — Form Edit Pengguna]**

1. Klik **Edit** di baris pengguna
2. Ubah data yang diperlukan — kolom Password bisa dikosongkan jika tidak ingin diubah
3. Klik **"Simpan Perubahan"**

### Hapus Pengguna

1. Klik **Hapus** → konfirmasi

> Admin tidak dapat menghapus akun dirinya sendiri.

---

## 9. QR CODE

> 👤 **Dapat diakses oleh: Admin & Staff**

### Generate QR Code

> **[Gambar 19 — Tombol Generate QR di Halaman Detail Aset]**
> **[Gambar 20 — Tampilan QR Code yang Dihasilkan]**

1. Buka halaman detail aset
2. Klik **"Generate QR Code"**
3. Sistem membuat file QR code (PNG) yang tersimpan di server
4. Klik **"Download QR"** untuk mengunduh

> Jika QR sudah pernah di-generate, sistem menampilkan pesan "QR Code sudah ada."

### Cetak QR Massal

> **[Gambar 21 — Halaman Cetak QR Massal]**

1. Di daftar aset, centang aset yang ingin dicetak QR-nya
2. Klik **"Cetak QR Terpilih"**
3. Halaman cetak terbuka — gunakan **Ctrl+P** untuk mencetak

### Scanner QR

> **[Gambar 22 — Halaman Scanner QR]**

1. Akses Sidebar → **QR Scanner**
2. Izinkan akses kamera di browser
3. Arahkan kamera ke QR code aset
4. Sistem menampilkan: nama barang, kategori, ruangan, kondisi, status, jumlah, serial number
5. Klik **"Lihat Detail"** untuk membuka halaman lengkap aset

> Scanner juga mendukung pencarian manual — ketik kode aset di kolom search.

---

## 10. MAINTENANCE

> 👤 **Dapat diakses oleh: Admin & Staff**

### Dashboard Maintenance

> **[Gambar 23 — Dashboard Maintenance]**

Menampilkan daftar aset berstatus Maintenance dengan statistik:

| Kartu | Isi |
|-------|-----|
| Total Maintenance | Aset berstatus Maintenance |
| Rusak Berat | Aset kondisi Rusak Berat |
| Rusak Ringan | Aset kondisi Rusak Ringan |
| Total Rusak | Gabungan keduanya |

Filter: cari berdasarkan kode/nama aset, atau saring berdasarkan kondisi.

### Tandai Aset Masuk Maintenance

> **[Gambar 24 — Tombol Set Maintenance di Detail Aset]**

1. Buka halaman detail aset
2. Klik **"Set Maintenance"**
3. Isi **Keterangan** (opsional) — contoh: "Layar retak, perlu penggantian"
4. Klik **"Simpan"**

Status aset berubah menjadi **Maintenance** dan email notifikasi dikirim ke semua Admin.

### Tandai Maintenance Selesai

> **[Gambar 25 — Form Tandai Maintenance Selesai]**

1. Di halaman Maintenance, klik **"Tandai Selesai"** pada aset yang sudah selesai dirawat
2. Isi formulir:

| Field | Keterangan | Wajib |
|-------|-----------|:-----:|
| Kondisi Setelah Maintenance | Baik / Rusak Ringan / Rusak Berat | ✓ |
| Keterangan | Catatan hasil perawatan | — |

3. Klik **"Selesai"**

Status aset kembali menjadi **Aktif** dan email notifikasi dikirim ke semua Admin.

---

## 11. LAPORAN, EXPORT & IMPORT

> 👤 **Dapat diakses oleh: Admin & Staff**

> **[Gambar 26 — Halaman Laporan & Export (hub utama)]**

Halaman ini adalah satu pintu untuk semua kebutuhan data.

### Laporan Aset

> **[Gambar 27 — Halaman Laporan Aset dengan Filter]**

1. Klik kartu **"Laporan Aset Lengkap"**
2. Atur filter: Ruangan, Kondisi, Status, atau Nama Barang
3. Pilih aksi:
   - **Lihat** — tampilkan di browser dengan statistik ringkas
   - **Cetak PDF** — unduh PDF (A4 landscape)
   - **Export CSV** — unduh CSV (bisa dibuka di Excel)

**Kolom laporan:** No, Kode Aset, Nama Barang, Kategori, Ruangan, Kondisi, Status, Tgl Perolehan, Jumlah

### Export Aset / Barang ke Excel atau PDF

> **[Gambar 28 — Halaman Export dengan Form Filter]**

1. Pilih kartu export yang diinginkan (Aset Excel, Aset PDF, Barang Excel, Barang PDF)
2. Klik **"Filter & Export"** untuk filter detail, atau **"Download Semua"** untuk langsung unduh
3. Filter aset: Status, Kondisi, Ruangan, Kategori, Nama Barang, Rentang Tanggal
4. Filter barang: Status, Kategori, Nama Barang

### Laporan per Ruangan

> **[Gambar 29 — Kartu Laporan per Ruangan]**

1. Scroll ke section **"Laporan per Ruangan"**
2. Pilih ruangan → klik **"Cetak PDF"**

> Ruangan tanpa aset tidak bisa dicetak laporannya.

### Laporan Maintenance

> **[Gambar 30 — Kartu Laporan Maintenance]**

Pilih **Cetak PDF** atau **Export CSV** untuk laporan seluruh aset berstatus Maintenance.

**Kolom:** No, Kode Aset, Nama Barang, Kategori, Ruangan, Kondisi, Serial Number, Keterangan, Terakhir Diperbarui

### Import Data Massal

> **[Gambar 31 — Halaman Import Data]**
> **[Gambar 32 — Contoh Template CSV Import Aset]**

1. Scroll ke section **"Import Data"** → klik **"Import Aset"** atau **"Import Barang"**
2. Klik **"Download Template"** untuk mengunduh template CSV
3. Isi template, simpan sebagai CSV dengan pemisah titik koma (`;`)
4. Upload file → klik **"Import"**
5. Sistem menampilkan hasil: jumlah berhasil dan baris yang gagal beserta alasannya

**Format template import aset:**

| Kolom | Keterangan | Contoh |
|-------|-----------|--------|
| Kode Barang | Harus sudah ada di katalog | BRG-001 |
| Nama Ruangan | Harus sudah ada di data ruangan | Ruang Studio |
| Kondisi | Baik / Rusak Ringan / Rusak Berat | Baik |
| Status | Aktif / Maintenance / Non-Aktif | Aktif |
| Jumlah | Angka bulat | 1 |
| Tanggal Perolehan | YYYY-MM-DD | 2026-01-15 |
| Harga Perolehan | Angka tanpa titik/koma | 5000000 |
| Sumber Perolehan | Pembelian / Hibah / Sumbangan / Pinjaman / Lainnya | Pembelian |
| Keterangan | Catatan tambahan | — |

**Format template import barang:** Kode Barang, Nama Barang, Kategori, Status (aktif/nonaktif)

**Catatan:**
- Format file: XLSX, XLS, atau CSV
- Baris pertama adalah header — tidak diproses sebagai data
- Kode Barang dan Nama Ruangan harus sudah terdaftar sebelum import aset
- Kode Barang yang sudah ada akan ditolak saat import barang

---

## 12. AUDIT LOG

> 🔒 **Dapat diakses oleh: Admin saja**

> **[Gambar 33 — Halaman Audit Log]**

Rekam jejak seluruh aktivitas pengguna di sistem.

### Informasi yang Ditampilkan

| Kolom | Keterangan |
|-------|-----------|
| Waktu | Tanggal dan jam aktivitas |
| Pengguna | Nama dan email pelaku |
| Aksi | Login, Create, Update, Delete, dll. |
| Keterangan | Detail perubahan yang dilakukan |
| IP Address | Alamat IP pengguna |

Filter tersedia: nama pengguna, jenis aksi, atau kata kunci keterangan.

---

## 13. PROFIL & GANTI PASSWORD

> 👤 **Dapat diakses oleh: Admin & Staff**

> **[Gambar 34 — Halaman Edit Profil]**

### Ubah Informasi Profil

1. Klik nama pengguna di pojok kanan atas → pilih **Edit Profil**
2. Ubah **Nama** dan/atau **Email**
3. Klik **"Simpan Perubahan"**

### Ganti Password

> **[Gambar 35 — Form Ubah Kata Sandi]**

1. Di halaman profil, scroll ke bagian **"Ubah Kata Sandi"**
2. Isi **Kata Sandi Saat Ini**
3. Isi **Kata Sandi Baru** (min. 8 karakter, huruf besar+kecil+angka)
4. Isi **Konfirmasi Kata Sandi**
5. Klik **"Perbarui Kata Sandi"**

---

## 14. LOGOUT

> **[Gambar 36 — Tombol Logout di Sidebar]**

1. Klik tombol **Logout** di bagian bawah sidebar
2. Sesi langsung diakhiri dan diarahkan ke halaman login

> Selalu logout setelah selesai, terutama di perangkat bersama.

---

## 15. HAK AKSES PER ROLE

| Fitur | Admin | Staff |
|-------|:-----:|:-----:|
| Dashboard | ✓ | ✓ |
| Kelola Aset (CRUD, hapus massal) | ✓ | ✓ |
| Kelola Barang | ✓ | ✓ |
| Kelola Ruangan | ✓ | ✓ |
| QR Code (generate, scan, cetak) | ✓ | ✓ |
| Maintenance (set + selesaikan) | ✓ | ✓ |
| Import Data | ✓ | ✓ |
| Export & Laporan | ✓ | ✓ |
| Edit Profil & Ganti Password | ✓ | ✓ |
| **Kelola Pengguna** | ✓ | — |
| **Audit Log** | ✓ | — |

---

## 16. DAMPAK SISTEM

Penerapan SimAset memberikan dampak positif bagi beberapa pihak di lingkungan RBTV Bengkulu.

### A. Dampak bagi Staf dan Pengelola Aset

- Mempermudah pencatatan dan penelusuran aset secara digital — tidak lagi bergantung pada dokumen fisik atau spreadsheet manual
- Mempercepat proses identifikasi aset melalui fitur scan QR code
- Memudahkan pemantauan kondisi dan status aset secara real-time dari mana saja
- Mengurangi risiko kehilangan data akibat kerusakan dokumen fisik

### B. Dampak bagi Manajemen RBTV

- Menyediakan laporan aset yang akurat dan dapat dicetak kapan saja untuk keperluan audit atau evaluasi
- Memudahkan pengambilan keputusan terkait pengadaan, perawatan, atau penghapusan aset berdasarkan data kondisi yang tercatat
- Meningkatkan akuntabilitas pengelolaan aset melalui fitur audit log yang merekam seluruh aktivitas pengguna
- Mendukung efisiensi operasional dengan sistem maintenance yang terstruktur dan terdokumentasi

### C. Dampak bagi Pengembangan Sistem Informasi

- Menjadi contoh penerapan sistem informasi manajemen aset berbasis web di lingkungan perusahaan media
- Memberikan dasar pengembangan lanjutan, seperti integrasi dengan sistem keuangan atau pengadaan barang
- Meningkatkan literasi digital staf dalam penggunaan sistem informasi berbasis web

---

## 17. PESAN ERROR UMUM

| Kode / Pesan | Penyebab | Solusi |
|-------------|----------|--------|
| **403 Forbidden** | Tidak punya izin akses | Hubungi Admin |
| **404 Not Found** | Halaman atau data tidak ditemukan | Kembali ke Dashboard |
| **500 Server Error** | Kesalahan internal sistem | Hubungi Administrator |
| "These credentials do not match" | Email atau password salah | Periksa kembali atau gunakan Lupa Password |
| "Akun Anda belum aktif" | Akun dinonaktifkan | Hubungi Admin |
| "The given data was invalid" | Isian formulir tidak valid | Periksa pesan merah di bawah tiap field |
| "CSRF token mismatch" | Sesi browser kedaluwarsa | Refresh halaman (F5) lalu coba lagi |
| "File harus berformat Excel atau CSV" | Format file import salah | Gunakan .xlsx, .xls, atau .csv |
| "Kode Barang tidak ditemukan" | Kode barang belum ada di katalog | Tambahkan barang ke katalog terlebih dahulu |
| "QR Code sudah ada" | QR sudah pernah di-generate | Langsung gunakan tombol Download QR |
| Email reset tidak masuk | Masuk ke Spam atau email salah | Cek folder Spam atau pastikan email benar |

---

*SimAset — Sistem Manajemen Aset RBTV Bengkulu*
*Modul Penggunaan v1.0 · Mei 2026*
*Disusun untuk keperluan Kerja Praktik — Teknik Informatika Universitas Bengkulu*
