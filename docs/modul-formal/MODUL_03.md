# MODUL 3 - PERANCANGAN SISTEM

## 3.1 Pendahuluan

Perancangan sistem merupakan tahapan penting dalam siklus pengembangan perangkat lunak yang bertujuan untuk menerjemahkan kebutuhan sistem yang telah dianalisis pada Modul 2 ke dalam bentuk rancangan teknis dan visual. Tahap ini menjadi jembatan antara analisis kebutuhan dan implementasi sistem.

Dalam konteks SimAset, perancangan sistem dilakukan untuk memastikan bahwa sistem yang dikembangkan mampu memenuhi kebutuhan pengguna, mudah digunakan, serta dapat dikembangkan di masa depan. Perancangan yang baik akan meminimalkan kesalahan pada tahap implementasi dan meningkatkan kualitas sistem secara keseluruhan.

Pendekatan perancangan yang digunakan dalam modul ini meliputi pemodelan sistem menggunakan Unified Modeling Language (UML), perancangan basis data menggunakan Entity Relationship Diagram (ERD), serta perancangan antarmuka pengguna (User Interface dan User Experience).

## 3.2 Perancangan Use Case Diagram

Use Case Diagram digunakan untuk menggambarkan interaksi antara aktor dan sistem serta fungsi-fungsi utama yang disediakan oleh sistem. Diagram ini memberikan gambaran umum mengenai apa saja yang dapat dilakukan oleh masing-masing aktor.

### 3.2.1 Aktor Sistem

SimAset melibatkan dua aktor utama, yaitu:

1. Admin
2. Staff

> **[GAMBAR 3.1: Use Case Diagram SimAset yang menampilkan dua aktor (Admin dan Staff) dengan seluruh use case yang dapat dilakukan masing-masing aktor]**

### 3.2.2 Use Case Staff

Staff memiliki peran sebagai pengguna operasional. Use case yang dapat dilakukan oleh Staff antara lain:

- Login ke sistem
- Logout dari sistem
- Mengelola data aset (tambah, lihat, edit, hapus)
- Mengelola master data barang (tambah, ubah, hapus)
- Mengelola master data ruangan (tambah, ubah, hapus)
- Generate dan mencetak QR Code aset
- Memindai QR Code untuk melihat detail aset
- Menandai aset masuk maintenance
- Menandai maintenance selesai
- Import data aset/barang dari Excel/CSV
- Export data ke Excel, PDF, CSV
- Mencetak laporan aset, per ruangan, dan maintenance
- Mengedit profil sendiri

Use case ini dirancang agar Staff dapat mengelola data aset secara cepat dan mudah.

### 3.2.3 Use Case Admin

Admin memiliki peran sebagai pengelola sistem. Use case yang dapat dilakukan oleh Admin meliputi seluruh use case Staff ditambah:

- Mengelola akun pengguna (tambah, ubah, hapus)
- Melihat audit log seluruh aktivitas pengguna
- Memfilter audit log berdasarkan pengguna dan jenis aktivitas

Use Case Diagram menunjukkan pemisahan hak akses yang jelas antara Admin dan Staff guna menjaga keamanan dan integritas data sistem.

## 3.3 Perancangan Activity Diagram

Activity Diagram digunakan untuk menggambarkan alur aktivitas atau proses bisnis yang terjadi dalam sistem. Diagram ini membantu memahami urutan aktivitas dari awal hingga akhir.

### 3.3.1 Activity Diagram Admin

Activity Diagram Admin menggambarkan alur kerja admin sebagai berikut:

1. Admin membuka halaman login.
2. Admin memasukkan email dan password.
3. Sistem melakukan proses autentikasi.
4. Jika login berhasil, admin diarahkan ke dashboard.
5. Admin memilih menu yang diinginkan (aset, barang, ruangan, pengguna, audit log).
6. Admin melakukan proses tambah, ubah, atau hapus data.
7. Sistem menyimpan perubahan data ke database.
8. Sistem mencatat aktivitas ke tabel log_aktivitas.
9. Admin logout dari sistem.

Diagram ini menegaskan bahwa seluruh aktivitas admin harus melalui proses autentikasi untuk menjaga keamanan sistem.

> **[GAMBAR 3.2: Activity Diagram Admin SimAset dengan swimlane Admin dan Sistem]**

### 3.3.2 Activity Diagram Staff

Activity Diagram Staff menggambarkan alur penggunaan sistem oleh Staff:

1. Staff membuka halaman login.
2. Staff memasukkan email dan password.
3. Sistem melakukan proses autentikasi.
4. Jika login berhasil, Staff diarahkan ke dashboard.
5. Staff memilih menu operasional (aset, barang, ruangan, QR Code, maintenance).
6. Staff melakukan pengelolaan data sesuai kebutuhan.
7. Sistem menyimpan perubahan dan mencatat aktivitas.
8. Staff dapat mencetak QR Code atau laporan sesuai kebutuhan.
9. Staff logout dari sistem.

Diagram ini menunjukkan bahwa sistem dirancang sederhana dan mudah digunakan oleh Staff dengan berbagai latar belakang teknis.

> **[GAMBAR 3.3: Activity Diagram Staff SimAset dengan swimlane Staff dan Sistem]**

## 3.4 Perancangan Sequence Diagram

Sequence Diagram digunakan untuk menggambarkan urutan interaksi antara aktor dan komponen sistem secara kronologis.

### 3.4.1 Sequence Diagram Admin

Sequence Diagram Admin menggambarkan proses:

- Admin mengirimkan permintaan login dengan email dan password.
- Sistem memverifikasi data login ke database melalui LoginRequest.
- Sistem melakukan session regenerate dan mencatat log Login.
- Sistem mengembalikan redirect ke halaman dashboard.
- Admin mengelola data aset (CRUD).
- Sistem menyimpan data ke database dan mencatat log aktivitas.

Diagram ini memperlihatkan alur komunikasi antara Admin, Middleware, Controller, Model, dan Database secara detail.

> **[GAMBAR 3.4: Sequence Diagram Admin SimAset]**

### 3.4.2 Sequence Diagram Staff

Sequence Diagram Staff menggambarkan:

- Staff mengakses halaman utama setelah login.
- Sistem mengambil data aset dari database dengan eager loading.
- Sistem menampilkan data dan statistik di dashboard.
- Staff memilih aset dan sistem menampilkan detail informasi.
- Staff dapat memindai QR Code untuk mengakses detail aset tanpa login.

Diagram ini menunjukkan bagaimana sistem merespons setiap permintaan Staff secara efisien.

> **[GAMBAR 3.5: Sequence Diagram Staff SimAset]**

## 3.5 Perancangan Basis Data (Entity Relationship Diagram / ERD)

Perancangan basis data bertujuan untuk mengelola data secara terstruktur dan terintegrasi. ERD digunakan untuk menggambarkan hubungan antar entitas dalam sistem. Database SimAset menggunakan MySQL 8.0.30 dengan nama database **simset_rbtv**.

### 3.5.1 Entitas Utama

- **users** — data pengguna sistem (Admin dan Staff)
- **barang** — master data jenis/tipe barang
- **ruangan** — master data lokasi/ruangan
- **aset** — data aset fisik (tabel utama)
- **log_aktivitas** — audit trail aktivitas pengguna

Setiap aset memiliki relasi dengan barang (sebagai jenis barang) dan ruangan (sebagai lokasi penempatan). ERD ini menjadi dasar dalam pembuatan tabel database pada tahap implementasi.

> **[GAMBAR 3.6: Entity Relationship Diagram (ERD) SimAset yang menampilkan semua entitas, atribut, dan relasi antar tabel]**

### 3.5.2 Langkah-langkah Pembuatan ERD

Perangkat lunak: Draw.io

1. Buka Draw.io lalu buat diagram baru, pilih blank diagram, ubah nama dan klik Create.
2. Tambahkan entitas (tabel), properti (kolom), dan relasi yang tersedia di bagian panel sebelah kiri.
3. Hubungkan relasi dengan cara memilih garis Crow's Foot (kaki gagak) yang sesuai dengan logika data (misal: One-to-Many), lalu tarik ujung garis dari satu tabel ke tabel lainnya hingga muncul titik hijau (terkunci).
4. Simpan ERD, klik File > Export as > PNG/PDF untuk mengunduh hasilnya.

**Skema tabel aktual dari database simset_rbtv:**

**Tabel `users`**

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| id | int PK AUTO_INCREMENT | Primary key |
| name | varchar(100) NOT NULL | Nama pengguna |
| email | varchar(100) UNIQUE | Email login |
| password | varchar(255) | Hash bcrypt |
| role | enum(admin,staff) | Peran pengguna |
| is_active | tinyint(1) DEFAULT 1 | Status aktif |
| last_login_at | timestamp NULL | Login terakhir |
| created_at | timestamp | Waktu dibuat |
| updated_at | timestamp | Waktu diperbarui |

**Tabel `barang`**

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| kode_barang | varchar(20) PK | Format BRG-001 |
| nama_barang | varchar(150) NOT NULL | Nama barang |
| kategori | enum(Kamera,Audio,Komputer,Lighting,Furniture,Peralatan Kantor) | Kategori |
| status | enum(aktif,nonaktif) DEFAULT aktif | Status |
| keterangan | text NULL | Catatan |
| created_at | timestamp | Waktu dibuat |
| updated_at | timestamp | Waktu diperbarui |
| deleted_at | timestamp NULL | Soft delete |

**Tabel `ruangan`**

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| id | int PK AUTO_INCREMENT | Primary key |
| nama | varchar(100) NOT NULL | Nama ruangan |
| lantai | varchar(50) NULL | Lantai/lokasi |
| keterangan | text NULL | Catatan |
| created_at | timestamp | Waktu dibuat |

**Tabel `aset` (tabel utama)**

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| kode_aset | varchar(20) PK | Format AST-001 |
| kode_barang | varchar(20) FK→barang | Jenis barang |
| ruangan_id | int FK→ruangan (SET NULL) | Lokasi aset |
| kondisi | enum(Baik,Rusak Ringan,Rusak Berat) | Kondisi fisik |
| status | enum(Aktif,Maintenance,Non-Aktif) | Status operasional |
| serial_number | varchar(100) NULL | Nomor seri |
| foto | varchar(255) NULL | Nama file foto |
| jumlah | int DEFAULT 1 | Jumlah unit |
| tanggal_perolehan | date NULL | Tanggal diperoleh |
| harga_perolehan | decimal(15,2) NULL | Harga perolehan |
| sumber_perolehan | varchar(255) NULL | Sumber perolehan |
| keterangan | text NULL | Catatan |
| created_by | int NULL | User pembuat |
| updated_by | int NULL | User pengubah |
| created_at | timestamp | Waktu dibuat |
| updated_at | timestamp | Waktu diperbarui |
| deleted_at | timestamp NULL | Soft delete |

**Tabel `log_aktivitas`**

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| id | bigint UNSIGNED PK AUTO_INCREMENT | Primary key |
| user_id | bigint UNSIGNED FK→users (SET NULL) | Pengguna |
| aktivitas | varchar(255) NOT NULL | Jenis aktivitas |
| keterangan | text NULL | Detail aktivitas |
| ip_address | varchar(45) NULL | IP address |
| user_agent | text NULL | Browser info |
| created_at | timestamp NULL | Waktu aktivitas |
| updated_at | timestamp NULL | Waktu diperbarui |

**Foreign Key Constraints aktual:**

```sql
CONSTRAINT fk_aset_barang
  FOREIGN KEY (kode_barang) REFERENCES barang(kode_barang)
  ON DELETE RESTRICT ON UPDATE CASCADE,

CONSTRAINT fk_aset_ruangan
  FOREIGN KEY (ruangan_id) REFERENCES ruangan(id)
  ON DELETE SET NULL ON UPDATE CASCADE
```

> **[GAMBAR 3.7: Tampilan struktur tabel database simset_rbtv di phpMyAdmin]**

## 3.6 Perancangan Antarmuka Pengguna (UI/UX)

Perancangan antarmuka pengguna bertujuan untuk menciptakan sistem yang menarik, mudah digunakan, dan nyaman bagi pengguna.

### 3.6.1 Antarmuka Staff

Antarmuka Staff dirancang dengan fokus pada:

- Dashboard dengan kartu statistik aset (total, aktif, maintenance, non-aktif)
- Navigasi sidebar yang sederhana dan intuitif
- Tabel data aset dengan filter multi-kriteria dan pagination
- Form input yang terstruktur dengan validasi real-time
- Desain responsif untuk berbagai perangkat

> **[GAMBAR 3.8: Wireframe antarmuka Staff SimAset dengan sidebar navigasi dan area konten]**

### 3.6.2 Antarmuka Admin

Antarmuka Admin dirancang dalam bentuk dashboard yang menyediakan:

- Semua fitur antarmuka Staff
- Menu tambahan: Kelola Pengguna dan Log Aktivitas
- Badge role "Administrator" di sidebar untuk membedakan dari Staff
- Akses ke audit log dengan filter pengguna dan jenis aktivitas

> **[GAMBAR 3.9: Wireframe antarmuka Admin SimAset dengan menu tambahan administrasi]**

## 3.7 Arsitektur Sistem

### 3.7.1 Gambaran Umum Arsitektur Sistem

Arsitektur sistem menggambarkan struktur keseluruhan sistem serta hubungan antar komponen utama yang membentuk SimAset. Arsitektur ini dirancang untuk memastikan sistem dapat berjalan secara terstruktur, mudah dipelihara, serta mendukung pengembangan lanjutan di masa depan.

Sistem ini menggunakan arsitektur berbasis web client-server, di mana proses pengolahan data dilakukan di sisi server, sementara pengguna mengakses sistem melalui browser pada perangkat desktop maupun mobile. Pendekatan ini dipilih karena sesuai dengan kebutuhan sistem informasi manajemen aset yang harus dapat diakses secara luas tanpa instalasi aplikasi tambahan.

> **[GAMBAR 3.10: Diagram arsitektur sistem SimAset lengkap dengan semua layer dan komponen]**

### 3.7.2 Komponen Arsitektur Sistem

Secara umum, arsitektur sistem terdiri dari tiga komponen utama, yaitu:

1. **Client (Pengguna Sistem)**
   Client merupakan pihak yang mengakses sistem melalui web browser. Client terdiri dari dua jenis pengguna, yaitu:
   a. Admin, yang mengakses dashboard pengelolaan sistem termasuk manajemen pengguna dan audit log.
   b. Staff, yang mengakses fitur operasional untuk mengelola data aset sehari-hari.
   Client berfungsi untuk menampilkan antarmuka pengguna (UI) dan menerima input dari pengguna.

2. **Server (Aplikasi Web)**
   Server merupakan inti dari sistem yang bertanggung jawab dalam memproses logika aplikasi. Pada sistem ini, server dikembangkan menggunakan framework Laravel 12 yang menerapkan pola Model-View-Controller (MVC).
   a. Model bertugas mengelola data dan berinteraksi dengan database melalui Eloquent ORM.
   b. View bertugas menampilkan data kepada pengguna menggunakan Blade Template.
   c. Controller bertugas mengatur alur logika dan permintaan dari client.

3. **Database Server**
   Database server digunakan untuk menyimpan seluruh data sistem, seperti data aset, master barang, master ruangan, data pengguna, serta log aktivitas. Sistem ini menggunakan MySQL 8.0.30 dengan nama database simset_rbtv karena stabil, mudah digunakan, dan kompatibel dengan Laravel.

### 3.7.3 Arsitektur Model-View-Controller (MVC)

Penerapan arsitektur MVC pada sistem ini bertujuan untuk memisahkan logika bisnis, tampilan, dan pengelolaan data agar sistem lebih terstruktur dan mudah dikembangkan.

1. **Model**
   Model bertanggung jawab terhadap pengelolaan data, termasuk proses penyimpanan, pengambilan, dan validasi data. Model pada sistem ini antara lain:
   a. Model Asset (tabel aset)
   b. Model Barang (tabel barang)
   c. Model Ruangan (tabel ruangan)
   d. Model User (tabel users)
   e. Model ActivityLog (tabel log_aktivitas)

2. **View**
   View merupakan komponen yang menampilkan data kepada pengguna. Pada sistem ini, view dibuat menggunakan Blade Template Laravel untuk menampilkan halaman dashboard, daftar aset, halaman detail aset, form tambah/edit, serta halaman QR Code.

3. **Controller**
   Controller berfungsi sebagai penghubung antara model dan view. Controller menerima permintaan dari client, memproses logika aplikasi, dan menentukan data apa yang akan ditampilkan. Sistem ini memiliki 13 controller utama.

### 3.7.4 Integrasi QR Code

Salah satu komponen penting dalam arsitektur sistem ini adalah integrasi QR Code. Sistem menggunakan dua pendekatan untuk generate QR Code:

1. **SimpleSoftwareIO QrCode** — untuk generate QR Code dalam format SVG, digunakan di halaman cetak (tidak memerlukan internet).
2. **qrserver.com API** — untuk generate QR Code dalam format PNG, disimpan di filesystem (memerlukan koneksi internet).

Alur integrasi QR Code adalah sebagai berikut:

1. Sistem generate kode unik aset (AST-001, AST-002, dst.).
2. QR Code di-generate berisi URL menuju halaman detail aset publik.
3. QR Code dicetak dan ditempel pada fisik aset.
4. Pengguna memindai QR Code menggunakan kamera smartphone.
5. Browser membuka halaman detail aset secara langsung tanpa perlu login.

Integrasi ini memungkinkan identifikasi aset secara cepat dan akurat di lapangan.

### 3.7.5 Alur Komunikasi Sistem

Alur komunikasi sistem menggambarkan bagaimana data mengalir dari client ke server dan sebaliknya:

1. Client mengirim permintaan (request) melalui browser.
2. Server menerima request melalui routing Laravel (routes/web.php).
3. Middleware dieksekusi: SecurityHeaders, auth, role:admin (jika diperlukan).
4. Controller memproses request dan memanggil model.
5. Model berinteraksi dengan database melalui Eloquent ORM.
6. Data dikembalikan ke controller.
7. Controller mengirim data ke view (Blade template).
8. View ditampilkan kembali ke client.
9. Middleware LogActivity mencatat aktivitas di fase terminate.

Alur ini memastikan sistem berjalan secara terstruktur dan efisien.

### 3.7.6 Keamanan Arsitektur Sistem

Keamanan sistem merupakan bagian penting dalam perancangan arsitektur. Beberapa aspek keamanan yang diterapkan antara lain:

1. Autentikasi pengguna menggunakan sistem login berbasis session (Laravel Breeze).
2. Pembatasan hak akses menggunakan RoleMiddleware (admin/staff).
3. Security Headers: X-Content-Type-Options, X-Frame-Options, X-XSS-Protection.
4. Validasi input data server-side untuk mencegah kesalahan dan serangan.
5. Penggunaan session yang aman dengan CSRF protection.
6. Password disimpan dalam bentuk hash bcrypt.
7. Rate limiting untuk mencegah serangan brute force.

Pendekatan keamanan ini memastikan hanya pihak berwenang yang dapat mengelola data sistem.

### 3.7.7 Kelebihan Arsitektur Sistem

Beberapa kelebihan dari arsitektur sistem yang digunakan antara lain:

1. Mudah dikembangkan dan dipelihara dengan struktur MVC yang terorganisir.
2. Struktur kode yang rapi mengikuti konvensi Laravel.
3. Mendukung pengembangan fitur lanjutan seperti API atau aplikasi mobile.
4. Cocok untuk sistem informasi manajemen aset berbasis web.
5. Dapat diakses dari berbagai perangkat tanpa instalasi tambahan.

### 3.7.8 Ringkasan Arsitektur Sistem

Arsitektur sistem yang digunakan pada SimAset dirancang dengan pendekatan client-server dan pola MVC. Integrasi QR Code menggunakan SimpleSoftwareIO dan qrserver.com API menjadi komponen utama dalam identifikasi aset. Dengan arsitektur ini, sistem diharapkan dapat berjalan secara stabil, aman, dan mudah dikembangkan di masa depan.

## 3.8 Kesimpulan Modul

Modul 3 ini membahas perancangan SimAset secara menyeluruh, mulai dari perancangan proses bisnis menggunakan Use Case Diagram, alur aktivitas sistem melalui Activity Diagram, interaksi antar komponen melalui Sequence Diagram, hingga perancangan struktur basis data menggunakan Entity Relationship Diagram (ERD) dan perancangan antarmuka pengguna.

Hasil perancangan sistem pada modul ini menjadi acuan utama dalam proses implementasi sistem pada modul-modul berikutnya. Dengan perancangan yang terstruktur dan terdokumentasi dengan baik, diharapkan proses pengembangan sistem dapat berjalan lebih efektif, terarah, dan sesuai dengan kebutuhan pengguna.
