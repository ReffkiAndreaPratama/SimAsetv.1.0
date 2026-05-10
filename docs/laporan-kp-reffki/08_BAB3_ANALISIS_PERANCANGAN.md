# BAB III ANALISIS KEBUTUHAN DAN PERANCANGAN SISTEM

## 3.1 Analisis Sistem Berjalan

Sebelum pengembangan sistem dilakukan, penulis melakukan analisis terhadap sistem pengelolaan aset yang sedang berjalan di RBTV Bengkulu. Analisis dilakukan melalui observasi langsung dan wawancara dengan staf administrasi yang bertanggung jawab atas pengelolaan aset.

### 3.1.1 Kondisi Sistem Saat Ini

Berdasarkan hasil analisis, sistem pengelolaan aset yang berjalan di RBTV Bengkulu memiliki karakteristik sebagai berikut:

1. **Pencatatan Manual:** Data aset dicatat secara manual menggunakan buku inventaris fisik dan spreadsheet Microsoft Excel yang tidak terintegrasi.
2. **Tidak Ada Pelacakan Real-Time:** Tidak tersedia sistem untuk memantau lokasi dan kondisi aset secara real-time.
3. **Proses Pelaporan Lambat:** Pembuatan laporan aset memerlukan waktu yang lama karena harus merekap data dari berbagai sumber secara manual.
4. **Tidak Ada Sistem Maintenance:** Tidak ada sistem yang mencatat dan mengingatkan jadwal perawatan aset.
5. **Risiko Kehilangan Data:** Data yang tersimpan dalam dokumen fisik dan file spreadsheet rentan terhadap kerusakan dan kehilangan.
6. **Tidak Ada Audit Trail:** Tidak ada catatan mengenai siapa yang melakukan perubahan data dan kapan perubahan tersebut dilakukan.

### 3.1.2 Permasalahan yang Diidentifikasi

Dari analisis sistem berjalan, permasalahan utama yang diidentifikasi adalah:

- Ketidakakuratan data aset akibat pencatatan manual yang rentan terhadap kesalahan.
- Kesulitan dalam melacak lokasi dan kondisi aset yang tersebar di berbagai ruangan.
- Tidak adanya sistem notifikasi untuk aset yang memerlukan perawatan.
- Proses pencarian dan pelaporan data aset yang tidak efisien.
- Tidak adanya kontrol akses yang jelas terhadap data aset.

---

## 3.2 Analisis Kebutuhan

### 3.2.1 Kebutuhan Fungsional

Berdasarkan hasil analisis sistem berjalan dan wawancara dengan pengguna, kebutuhan fungsional sistem dirumuskan sebagai berikut:

**Tabel 3.1 Kebutuhan Fungsional Sistem**

| No | Kode | Kebutuhan Fungsional | Aktor |
|----|------|---------------------|-------|
| 1 | KF-01 | Sistem menyediakan fitur login dan logout dengan autentikasi berbasis session | Admin, Staff |
| 2 | KF-02 | Sistem menampilkan dashboard dengan statistik dan grafik kondisi aset | Admin, Staff |
| 3 | KF-03 | Sistem menyediakan CRUD (Create, Read, Update, Delete) data aset | Admin, Staff |
| 4 | KF-04 | Sistem mendukung upload foto untuk setiap aset | Admin, Staff |
| 5 | KF-05 | Sistem menyediakan fitur pencarian dan filter aset berdasarkan berbagai kriteria | Admin, Staff |
| 6 | KF-06 | Sistem menyediakan CRUD data barang sebagai master data | Admin, Staff |
| 7 | KF-07 | Sistem menyediakan CRUD data ruangan sebagai master data | Admin, Staff |
| 8 | KF-08 | Sistem dapat generate QR Code untuk setiap aset | Admin, Staff |
| 9 | KF-09 | Sistem menyediakan fitur scanner QR Code untuk identifikasi aset | Admin, Staff |
| 10 | KF-10 | Sistem mendukung batch print QR Code untuk multiple aset | Admin, Staff |
| 11 | KF-11 | Sistem menyediakan fitur pelacakan maintenance aset | Admin, Staff |
| 12 | KF-12 | Sistem mengirimkan notifikasi email saat maintenance selesai | Admin |
| 13 | KF-13 | Sistem mendukung import data aset dan barang dari file Excel/CSV | Admin, Staff |
| 14 | KF-14 | Sistem mendukung export data aset dan barang ke format Excel dan PDF | Admin, Staff |
| 15 | KF-15 | Sistem menyediakan laporan aset, laporan per ruangan, dan laporan maintenance | Admin, Staff |
| 16 | KF-16 | Sistem menyediakan CRUD pengguna dengan role Admin dan Staff | Admin |
| 17 | KF-17 | Sistem mencatat seluruh aktivitas pengguna dalam audit log | Admin |
| 18 | KF-18 | Sistem mendukung soft delete untuk data aset dan barang | Admin, Staff |
| 19 | KF-19 | Sistem mendukung batch delete untuk multiple aset | Admin, Staff |
| 20 | KF-20 | Sistem menyediakan fitur edit profil dan ubah password | Admin, Staff |

### 3.2.2 Kebutuhan Non-Fungsional

**Tabel 3.2 Kebutuhan Non-Fungsional Sistem**

| No | Kode | Kebutuhan Non-Fungsional | Kategori |
|----|------|-------------------------|----------|
| 1 | KNF-01 | Sistem dapat diakses melalui perangkat desktop maupun mobile (responsif) | Portabilitas |
| 2 | KNF-02 | Antarmuka sederhana, informatif, dan ramah pengguna (user-friendly) | Usabilitas |
| 3 | KNF-03 | Performa sistem cepat dalam menampilkan data dan memproses request | Performa |
| 4 | KNF-04 | Sistem menggunakan HTTPS dan security headers untuk keamanan | Keamanan |
| 5 | KNF-05 | Data yang dihapus tidak hilang secara permanen (soft delete) | Keandalan |
| 6 | KNF-06 | Sistem mendukung pagination untuk menampilkan data dalam jumlah besar | Performa |
| 7 | KNF-07 | Password pengguna disimpan dalam bentuk hash (bcrypt) | Keamanan |
| 8 | KNF-08 | Sistem memiliki validasi input di sisi server untuk mencegah data tidak valid | Keamanan |
| 9 | KNF-09 | Sistem menggunakan CSRF protection untuk mencegah serangan CSRF | Keamanan |
| 10 | KNF-10 | Sistem dapat dioperasikan oleh pengguna dengan pelatihan minimal | Usabilitas |

---

## 3.3 Perancangan Sistem

### 3.3.1 Use Case Diagram

> **Gambar 3.1 Use Case Diagram Sistem**

Diagram use case menunjukkan bahwa sistem memiliki dua aktor utama, yaitu **Staff** dan **Admin**. Staff memiliki akses ke fitur operasional utama, sedangkan Admin memiliki seluruh akses Staff ditambah fitur manajemen pengguna dan audit log.

**Aktor dan Use Case:**

**Staff (semua pengguna terautentikasi):**
- Login / Logout
- Melihat Dashboard
- Mengelola Aset (CRUD, batch delete, foto)
- Mengelola Barang (CRUD)
- Mengelola Ruangan (CRUD)
- Generate & Scan QR Code
- Batch Print QR Code
- Mengelola Maintenance (set, complete)
- Import Data (aset, barang)
- Export Data (Excel, PDF)
- Melihat Laporan
- Edit Profil

**Admin (tambahan dari Staff):**
- Mengelola Pengguna (CRUD, role management)
- Melihat Audit Log

---

### 3.3.2 Activity Diagram

> **Gambar 3.2 Activity Diagram Login**

Activity Diagram Login menggambarkan alur aktivitas pengguna saat melakukan proses autentikasi. Pengguna membuka halaman login dan memasukkan email serta password. Sistem melakukan verifikasi kredensial; jika gagal, pengguna dikembalikan ke halaman login dengan pesan error. Jika berhasil, pengguna diarahkan ke halaman dashboard. Sistem juga mencatat aktivitas login ke dalam audit log.

> **Gambar 3.3 Activity Diagram Manajemen Aset**

Activity Diagram Manajemen Aset menggambarkan alur aktivitas pengguna dalam mengelola data aset. Setelah login, pengguna mengakses menu Aset dan dapat memilih tindakan: tambah aset baru, melihat daftar aset, mengedit data aset, atau menghapus aset. Setiap tindakan yang berhasil akan disimpan ke database dan dicatat dalam audit log. Pengguna juga dapat melakukan pencarian dan filter aset berdasarkan berbagai kriteria.

> **Gambar 3.4 Activity Diagram QR Code**

Activity Diagram QR Code menggambarkan alur aktivitas pengguna dalam menggunakan fitur QR Code. Pengguna dapat memilih aset dan generate QR Code, kemudian mengunduh atau mencetak QR Code tersebut. Untuk scanner, pengguna membuka halaman scanner dan memindai QR Code aset; sistem akan menampilkan detail aset yang sesuai.

> **Gambar 3.5 Activity Diagram Maintenance**

Activity Diagram Maintenance menggambarkan alur aktivitas pengelolaan maintenance aset. Staff dapat menandai aset masuk maintenance dengan mengisi keterangan. Saat maintenance selesai, staff menandai selesai dan mengisi kondisi aset terkini. Sistem secara otomatis mengirimkan notifikasi email ke seluruh admin dan mencatat aktivitas ke audit log.

---

### 3.3.3 Sequence Diagram

> **Gambar 3.6 Sequence Diagram Admin**

Sequence Diagram Admin menggambarkan alur interaksi antara aktor Admin dengan komponen sistem, yaitu halaman Login, Dashboard, modul Manajemen Aset, modul Manajemen Pengguna, modul Audit Log, dan Database. Proses dimulai ketika admin memasukkan email dan password, lalu sistem melakukan validasi. Setelah login berhasil, admin dapat mengakses seluruh fitur sistem termasuk manajemen pengguna dan audit log yang hanya tersedia untuk role admin.

> **Gambar 3.7 Sequence Diagram Staff**

Sequence Diagram Staff menggambarkan alur interaksi antara aktor Staff dengan komponen sistem. Staff memiliki akses ke fitur operasional seperti manajemen aset, barang, ruangan, QR Code, maintenance, import/export, dan laporan. Setiap operasi yang dilakukan staff berinteraksi dengan database melalui controller yang sesuai, dan aktivitas dicatat secara otomatis oleh middleware LogActivity.

---

### 3.3.4 Class Diagram

> **Gambar 3.8 Class Diagram**

Class Diagram menggambarkan struktur logis dari sistem SimAset, termasuk kelas-kelas utama, atribut, metode, dan hubungan antar kelas.

**Kelas-kelas utama:**

- **User:** Atribut: id, name, email, password, role, is_active, last_login_at. Metode: isAdmin(), isStaff(), sendPasswordResetNotification().
- **Asset:** Atribut: kode_aset, kode_barang, ruangan_id, kondisi, status, serial_number, foto, jumlah, tanggal_perolehan, harga_perolehan, sumber_perolehan, keterangan, created_by, updated_by. Metode: generateKode(), getNamaBarangAttribute(), getKategoriAttribute(), getNamaRuanganAttribute().
- **Barang:** Atribut: kode_barang, nama_barang, kategori, status, keterangan. Metode: generateKode().
- **Ruangan:** Atribut: id, nama, lantai, keterangan. Metode: getNamaRuanganAttribute().
- **ActivityLog:** Atribut: id, user_id, aktivitas, keterangan, ip_address, user_agent.

**Relasi antar kelas:**
- Asset *→ 1 Barang (belongsTo)
- Asset *→ 1 Ruangan (belongsTo)
- Asset *→ 1 User/creator (belongsTo)
- Barang 1 → * Asset (hasMany)
- Ruangan 1 → * Asset (hasMany)
- User 1 → * ActivityLog (hasMany)

---

### 3.3.5 Entity Relationship Diagram (ERD)

> **Gambar 3.9 Entity Relationship Diagram (ERD)**

ERD menggambarkan hubungan antar entitas dalam database sistem SimAset.

**Entitas dan Atribut:**

**Tabel 3.3 Struktur Tabel Aset**

| Kolom | Tipe Data | Keterangan |
|-------|-----------|-----------|
| kode_aset | VARCHAR (PK) | Kode unik aset (format: AST-001) |
| kode_barang | VARCHAR (FK) | Referensi ke tabel barang |
| ruangan_id | INT (FK) | Referensi ke tabel ruangan |
| serial_number | VARCHAR | Nomor seri aset (nullable, unique) |
| kondisi | ENUM | Baik / Rusak Ringan / Rusak Berat |
| status | ENUM | Aktif / Maintenance / Non-Aktif |
| jumlah | INT | Jumlah unit aset |
| tanggal_perolehan | DATE | Tanggal aset diperoleh |
| harga_perolehan | DECIMAL | Harga perolehan aset |
| sumber_perolehan | ENUM | Pembelian / Hibah / Sumbangan / Pinjaman / Lainnya |
| foto | VARCHAR | Nama file foto aset |
| keterangan | TEXT | Catatan tambahan |
| created_by | INT (FK) | ID pengguna yang membuat |
| updated_by | INT (FK) | ID pengguna yang terakhir mengubah |
| created_at, updated_at | TIMESTAMP | Waktu pembuatan dan pembaruan |
| deleted_at | TIMESTAMP | Waktu penghapusan (soft delete) |

**Tabel 3.4 Struktur Tabel Barang**

| Kolom | Tipe Data | Keterangan |
|-------|-----------|-----------|
| kode_barang | VARCHAR (PK) | Kode unik barang (format: BRG-001) |
| nama_barang | VARCHAR | Nama barang |
| kategori | VARCHAR | Kategori barang |
| status | ENUM | aktif / nonaktif |
| keterangan | TEXT | Catatan tambahan |
| created_at, updated_at | TIMESTAMP | Waktu pembuatan dan pembaruan |
| deleted_at | TIMESTAMP | Waktu penghapusan (soft delete) |

**Tabel 3.5 Struktur Tabel Ruangan**

| Kolom | Tipe Data | Keterangan |
|-------|-----------|-----------|
| id | INT (PK, AI) | ID ruangan |
| nama | VARCHAR | Nama ruangan |
| lantai | VARCHAR | Lantai/lokasi ruangan |
| keterangan | TEXT | Catatan tambahan |
| created_at, updated_at | TIMESTAMP | Waktu pembuatan dan pembaruan |

**Tabel 3.6 Struktur Tabel Users**

| Kolom | Tipe Data | Keterangan |
|-------|-----------|-----------|
| id | INT (PK, AI) | ID pengguna |
| name | VARCHAR | Nama lengkap pengguna |
| email | VARCHAR (unique) | Email pengguna |
| password | VARCHAR | Password (hashed bcrypt) |
| role | ENUM | admin / staff |
| is_active | BOOLEAN | Status aktif pengguna |
| last_login_at | TIMESTAMP | Waktu login terakhir |
| created_at, updated_at | TIMESTAMP | Waktu pembuatan dan pembaruan |

**Tabel 3.7 Struktur Tabel Log Aktivitas**

| Kolom | Tipe Data | Keterangan |
|-------|-----------|-----------|
| id | INT (PK, AI) | ID log |
| user_id | INT (FK) | Referensi ke tabel users |
| aktivitas | VARCHAR | Jenis aktivitas (Login, Create, Update, Delete, dll) |
| keterangan | TEXT | Deskripsi detail aktivitas |
| ip_address | VARCHAR | Alamat IP pengguna |
| user_agent | TEXT | Informasi browser/device pengguna |
| created_at, updated_at | TIMESTAMP | Waktu pencatatan |

**Relasi antar entitas:**
- Aset *—1 Barang (Many-to-One): Satu barang dapat memiliki banyak aset
- Aset *—1 Ruangan (Many-to-One): Satu ruangan dapat memiliki banyak aset
- Aset *—1 Users/creator (Many-to-One): Satu pengguna dapat membuat banyak aset
- Log Aktivitas *—1 Users (Many-to-One): Satu pengguna dapat memiliki banyak log aktivitas

---

### 3.3.6 Data Flow Diagram (DFD)

> **Gambar 3.10 Data Flow Diagram Level 0**

DFD Level 0 menunjukkan gambaran umum aliran data pada sistem SimAset. Sistem digambarkan sebagai satu proses besar yang berinteraksi dengan dua entitas eksternal, yaitu **Admin** dan **Staff**. Admin memberikan input berupa data pengguna, data aset, dan konfigurasi sistem, serta menerima keluaran berupa laporan, audit log, dan konfirmasi operasi. Staff memberikan input berupa data aset, data barang, data ruangan, dan permintaan laporan, serta menerima keluaran berupa informasi aset, QR Code, dan laporan. Diagram ini memperlihatkan bahwa sistem berfungsi sebagai pusat pemrosesan data yang menjembatani kebutuhan operasional antara admin dan staff dalam pengelolaan aset.

> **Gambar 3.11 Data Flow Diagram Level 1**

DFD Level 1 merinci proses internal sistem menjadi beberapa proses utama:

- **Proses 1.0 Autentikasi:** Menangani proses login, logout, dan verifikasi identitas pengguna.
- **Proses 2.0 Manajemen Aset:** Menangani CRUD aset, pencarian, filter, dan pengelolaan foto aset.
- **Proses 3.0 Manajemen Master Data:** Menangani CRUD barang dan ruangan.
- **Proses 4.0 QR Code:** Menangani generate, download, batch print, dan scanner QR Code.
- **Proses 5.0 Maintenance:** Menangani pelacakan status maintenance dan notifikasi email.
- **Proses 6.0 Import/Export:** Menangani import data dari Excel/CSV dan export ke Excel/PDF.
- **Proses 7.0 Laporan:** Menangani pembuatan laporan aset, ruangan, dan maintenance.
- **Proses 8.0 Manajemen Pengguna:** Menangani CRUD pengguna dan role management (Admin only).
- **Proses 9.0 Audit Log:** Menangani pencatatan dan tampilan log aktivitas (Admin only).

---

### 3.3.7 Perancangan Antarmuka (Prototype)

> **Gambar 3.12 Prototype Halaman Login**

Halaman Login merupakan titik masuk utama bagi pengguna untuk mengakses sistem. Tampilan terdiri dari form email dan password, tombol "Masuk", serta opsi "Ingat Saya" dan "Lupa Password?". Desain dibuat minimalis dan responsif agar mudah digunakan di berbagai perangkat.

> **Gambar 3.13 Prototype Dashboard**

Halaman Dashboard menampilkan ringkasan statistik sistem secara visual, meliputi total aset, aset aktif, aset maintenance, aset non-aktif, total barang, dan total ruangan. Dashboard juga menampilkan grafik distribusi kondisi aset, grafik top 5 kategori barang, dan daftar 10 aset terbaru. Navigasi utama berada di sidebar kiri dengan menu-menu utama sistem.

> **Gambar 3.14 Prototype Halaman Aset**

Halaman Aset menampilkan daftar seluruh aset dalam bentuk tabel dengan kolom kode aset, nama barang, kategori, ruangan, kondisi, status, dan aksi. Tersedia fitur pencarian, filter berdasarkan status/kondisi/kategori, dan tombol tambah aset baru. Setiap baris aset memiliki tombol aksi untuk melihat detail, edit, generate QR, dan hapus.

> **Gambar 3.15 Prototype Halaman QR Code**

Halaman QR Code menampilkan fitur scanner berbasis web yang dapat memindai QR Code aset menggunakan kamera perangkat. Hasil scan menampilkan informasi detail aset secara real-time. Tersedia juga fitur batch print untuk mencetak multiple QR Code sekaligus.

> **Gambar 3.16 Prototype Dashboard Admin**

Dashboard Admin menampilkan seluruh fitur yang tersedia untuk role admin, termasuk menu tambahan Manajemen Pengguna dan Audit Log. Panel admin menampilkan statistik pengguna aktif dan log aktivitas terbaru.
