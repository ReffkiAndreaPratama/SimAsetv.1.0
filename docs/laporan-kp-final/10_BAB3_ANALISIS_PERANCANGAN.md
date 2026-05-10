# BAB III ANALISIS DAN PERANCANGAN

## 3.1 Deskripsi Singkat Instansi

RBTV Bengkulu (Rakyat Bengkulu Televisi) merupakan stasiun televisi lokal yang beroperasi di Kota Bengkulu, Provinsi Bengkulu. RBTV Bengkulu berdiri sebagai media penyiaran lokal yang menyajikan berbagai program siaran, meliputi berita daerah, hiburan, dan program informasi yang ditujukan bagi masyarakat Bengkulu dan sekitarnya. Dalam menjalankan kegiatan operasionalnya, RBTV Bengkulu didukung oleh sumber daya manusia yang terdiri dari tim redaksi, tim produksi, tim teknis, dan staf administrasi.

Kegiatan operasional RBTV Bengkulu meliputi produksi program siaran, penyiaran langsung (live broadcast), pengelolaan teknis peralatan siaran, serta administrasi umum. Dalam mendukung seluruh kegiatan tersebut, RBTV Bengkulu memiliki berbagai aset barang berupa peralatan produksi seperti kamera, perangkat editing, peralatan audio, serta perlengkapan kantor seperti komputer, printer, dan perangkat jaringan. Aset-aset tersebut digunakan secara rutin dengan intensitas yang cukup tinggi sehingga memerlukan pengelolaan yang tertib dan terdokumentasi dengan baik.

Visi RBTV Bengkulu adalah menjadi stasiun televisi lokal terpercaya yang memberikan informasi aktual dan hiburan berkualitas bagi masyarakat Bengkulu. Misi yang diemban meliputi menyajikan program siaran yang informatif, edukatif, dan menghibur, serta mendukung perkembangan budaya dan potensi daerah Bengkulu.

Struktur organisasi RBTV Bengkulu terdiri dari Direktur Utama, Direktur Operasional, Kepala Redaksi, Kepala Produksi, Kepala Teknik, dan Kepala Administrasi, yang masing-masing membawahi staf sesuai bidang tugasnya. Pengelolaan aset barang berada di bawah tanggung jawab bagian administrasi yang bertugas mencatat, memantau, dan melaporkan kondisi seluruh aset yang dimiliki instansi.

*(Gambar 3.1 Struktur Organisasi RBTV Bengkulu)*

---

## 3.2 Analisis Masalah

### 3.2.1 Langkah-langkah Analisis

Analisis masalah dilakukan untuk mengidentifikasi kelemahan dan permasalahan yang terdapat pada sistem pengelolaan aset yang sedang berjalan di RBTV Bengkulu. Langkah-langkah analisis yang dilakukan adalah sebagai berikut:

1. **Observasi Lapangan**, yaitu pengamatan langsung terhadap proses pengelolaan aset yang sedang berjalan, meliputi cara pencatatan data aset, penyimpanan dokumen, pembaruan kondisi barang, dan penyusunan laporan inventaris.

2. **Wawancara**, yaitu pengumpulan informasi melalui tanya jawab dengan staf administrasi dan pengguna sistem terkait kendala yang dihadapi dalam pengelolaan aset sehari-hari.

3. **Analisis Dokumen**, yaitu pemeriksaan terhadap dokumen dan file spreadsheet yang digunakan sebagai media pencatatan aset untuk mengidentifikasi ketidaklengkapan dan inkonsistensi data.

4. **Analisis PIECES**, yaitu evaluasi sistem yang berjalan menggunakan kerangka kerja PIECES (Performance, Information, Economy, Control, Efficiency, Service) untuk mendapatkan gambaran menyeluruh mengenai kelemahan sistem.

### 3.2.2 Hasil Analisis

Berdasarkan hasil observasi dan analisis yang dilakukan, ditemukan berbagai kelemahan pada sistem pengelolaan aset yang sedang berjalan. Hasil analisis menggunakan kerangka PIECES disajikan pada Tabel 3.1 berikut.

**Tabel 3.1 Analisis PIECES Sistem Pengelolaan Aset RBTV Bengkulu**

| Aspek | Kondisi Sistem Lama | Permasalahan |
|---|---|---|
| **Performance** | Pencatatan dilakukan secara manual menggunakan dokumen tertulis dan spreadsheet | Proses pencarian data memerlukan waktu lama karena harus memeriksa beberapa file secara manual |
| **Information** | Data aset tersimpan di beberapa file terpisah tanpa integrasi | Informasi kondisi dan lokasi aset tidak selalu akurat dan tidak mencerminkan kondisi aktual |
| **Economy** | Penggunaan kertas dan waktu staf yang besar untuk pencatatan dan pelaporan manual | Pemborosan sumber daya akibat proses yang tidak efisien dan potensi kesalahan yang memerlukan koreksi |
| **Control** | Tidak ada sistem kontrol akses dan validasi data yang memadai | Risiko pencatatan ganda, kehilangan data, dan tidak adanya jejak audit perubahan data |
| **Efficiency** | Proses pembaruan kondisi aset dan penyusunan laporan dilakukan secara manual | Waktu dan tenaga yang dibutuhkan tidak sebanding dengan hasil yang diperoleh |
| **Service** | Informasi aset tidak dapat diakses secara cepat dan akurat oleh pihak yang membutuhkan | Keterlambatan penyajian informasi kepada manajemen untuk keperluan pengambilan keputusan |

Berdasarkan hasil analisis PIECES tersebut, dapat disimpulkan bahwa sistem pengelolaan aset yang berjalan di RBTV Bengkulu memiliki kelemahan utama pada aspek integrasi data, kecepatan akses informasi, kontrol data, dan efisiensi proses. Kondisi ini menunjukkan perlunya pengembangan sistem informasi manajemen aset berbasis web yang mampu mengatasi seluruh kelemahan tersebut.

---

## 3.3 Analisis Kebutuhan

### 3.3.1 Kebutuhan Perangkat Keras

Kebutuhan perangkat keras yang diperlukan dalam pengembangan dan implementasi sistem dibagi menjadi dua, yaitu perangkat keras untuk pengembangan dan perangkat keras untuk implementasi.

**Tabel 3.2 Kebutuhan Perangkat Keras Pengembangan**

| No | Komponen | Spesifikasi Minimum |
|---|---|---|
| 1 | Prosesor | Intel Core i5 atau setara |
| 2 | RAM | 8 GB |
| 3 | Penyimpanan | 256 GB SSD |
| 4 | Sistem Operasi | Windows 10 / Linux Ubuntu 20.04 |
| 5 | Koneksi Jaringan | LAN / Wi-Fi |

**Tabel 3.3 Kebutuhan Perangkat Keras Implementasi**

| No | Komponen | Spesifikasi Minimum |
|---|---|---|
| 1 | Server | Prosesor Dual Core, RAM 4 GB, Storage 100 GB |
| 2 | Komputer Klien | Prosesor Intel Core i3, RAM 4 GB |
| 3 | Jaringan | Switch/Router dengan koneksi LAN |
| 4 | Browser | Google Chrome / Mozilla Firefox versi terbaru |

### 3.3.2 Kebutuhan Perangkat Lunak

**Tabel 3.4 Kebutuhan Perangkat Lunak**

| No | Perangkat Lunak | Fungsi |
|---|---|---|
| 1 | PHP 8.1 | Bahasa pemrograman server-side |
| 2 | Laravel 10 | Framework pengembangan aplikasi web |
| 3 | MySQL 8.0 | Sistem manajemen basis data |
| 4 | Apache/Nginx | Web server |
| 5 | Composer | Manajemen dependensi PHP |
| 6 | Visual Studio Code | Editor kode program |
| 7 | Git | Version control system |
| 8 | Google Chrome | Browser untuk pengujian |

### 3.3.3 Kebutuhan Fungsional

Kebutuhan fungsional menggambarkan fungsi-fungsi yang harus tersedia dalam sistem agar seluruh kebutuhan pengguna terpenuhi dan permasalahan yang ada dapat diselesaikan.

**Tabel 3.5 Kebutuhan Fungsional Sistem**

| No | Fungsi | Deskripsi |
|---|---|---|
| 1 | Autentikasi Pengguna | Sistem menyediakan fitur login dan logout dengan validasi kredensial pengguna |
| 2 | Manajemen Aset | Sistem dapat menambah, mengubah, menghapus, dan menampilkan data aset |
| 3 | Manajemen Kategori Barang | Sistem dapat mengelola kategori/jenis barang yang digunakan sebagai pengelompokan aset |
| 4 | Manajemen Ruangan | Sistem dapat mengelola data ruangan sebagai lokasi penempatan aset |
| 5 | QR Code Aset | Sistem dapat menghasilkan dan mencetak QR Code untuk setiap aset |
| 6 | Pemindaian QR Code | Sistem dapat memindai QR Code untuk menampilkan detail aset secara cepat |
| 7 | Manajemen Pemeliharaan | Sistem dapat mencatat dan memantau jadwal serta riwayat pemeliharaan aset |
| 8 | Import Data | Sistem dapat mengimpor data aset dari file Excel |
| 9 | Export Data | Sistem dapat mengekspor data aset ke format Excel dan PDF |
| 10 | Laporan Aset | Sistem dapat menghasilkan laporan inventaris aset secara otomatis |
| 11 | Manajemen Pengguna | Administrator dapat mengelola akun pengguna dan hak akses |
| 12 | Audit Log | Sistem mencatat seluruh aktivitas pengguna sebagai jejak audit |

### 3.3.4 Kebutuhan Non-Fungsional

Kebutuhan non-fungsional merupakan kebutuhan tambahan yang tidak berkaitan langsung dengan fungsi utama sistem, namun diperlukan agar sistem dapat berjalan secara optimal.

1. **Keamanan:** Sistem dilengkapi dengan mekanisme autentikasi berbasis sesi, enkripsi password menggunakan bcrypt, dan middleware untuk kontrol akses berdasarkan peran pengguna.
2. **Performa:** Sistem mampu merespons permintaan pengguna dalam waktu kurang dari 3 detik pada kondisi jaringan normal.
3. **Ketersediaan:** Sistem dapat diakses selama jam operasional instansi melalui jaringan intranet.
4. **Kemudahan Penggunaan:** Antarmuka sistem dirancang intuitif sehingga dapat digunakan tanpa pelatihan teknis yang mendalam.
5. **Skalabilitas:** Sistem dirancang agar dapat dikembangkan lebih lanjut dengan penambahan fitur baru tanpa mengubah struktur inti sistem.

---

## 3.4 Analisis Kelayakan Sistem

Analisis kelayakan dilakukan untuk menilai apakah sistem yang diusulkan layak untuk dikembangkan dan diimplementasikan di RBTV Bengkulu. Analisis kelayakan mencakup tiga aspek utama, yaitu:

1. **Kelayakan Teknis:** Sistem dikembangkan menggunakan teknologi yang sudah matang dan banyak digunakan, yaitu framework Laravel dan MySQL. Infrastruktur jaringan yang tersedia di RBTV Bengkulu sudah memadai untuk mendukung operasional sistem berbasis web. Sumber daya manusia yang ada mampu mengoperasikan sistem setelah mendapatkan pelatihan singkat.

2. **Kelayakan Operasional:** Sistem yang diusulkan dirancang untuk menggantikan proses manual yang selama ini digunakan, sehingga dapat langsung diintegrasikan ke dalam alur kerja yang sudah ada. Antarmuka yang intuitif memudahkan staf administrasi dalam mengadopsi sistem baru tanpa hambatan yang berarti.

3. **Kelayakan Ekonomi:** Pengembangan sistem menggunakan teknologi open-source sehingga tidak memerlukan biaya lisensi perangkat lunak. Manfaat yang diperoleh dari sistem, berupa penghematan waktu, pengurangan kesalahan pencatatan, dan peningkatan akurasi laporan, dinilai lebih besar dibandingkan biaya pengembangan yang dikeluarkan.

---

## 3.5 Perancangan Sistem

### 3.5.1 Perancangan Proses

Perancangan proses dilakukan menggunakan pendekatan Unified Modeling Language (UML) yang meliputi Use Case Diagram, Activity Diagram, dan Class Diagram.

**a. Use Case Diagram**

Use Case Diagram menggambarkan interaksi antara aktor dengan sistem. Sistem ini memiliki dua aktor utama, yaitu Administrator dan Staff. Administrator memiliki hak akses penuh terhadap seluruh fitur sistem, sedangkan Staff memiliki hak akses terbatas sesuai peran yang ditetapkan.

Fungsi-fungsi utama yang tersedia dalam sistem meliputi: login, mengelola data aset, mengelola kategori barang, mengelola ruangan, mencetak QR Code, memindai QR Code, mencatat pemeliharaan, mengimpor data, mengekspor data, melihat laporan, mengelola pengguna, dan melihat audit log.

*(Gambar 3.2 Use Case Diagram)*

**b. Activity Diagram Login**

Activity Diagram Login menggambarkan alur proses autentikasi pengguna ke dalam sistem. Pengguna memasukkan email dan password pada halaman login. Sistem memvalidasi kredensial yang dimasukkan. Apabila kredensial valid, sistem mengarahkan pengguna ke halaman dashboard sesuai peran. Apabila tidak valid, sistem menampilkan pesan kesalahan dan pengguna diminta memasukkan kembali kredensialnya.

*(Gambar 3.3 Activity Diagram Login)*

**c. Activity Diagram Pengelolaan Aset**

Activity Diagram Pengelolaan Aset menggambarkan alur proses pengelolaan data aset dalam sistem. Administrator atau Staff mengakses menu Data Aset. Sistem menampilkan daftar aset yang tersimpan. Pengguna dapat memilih untuk menambah aset baru, mengubah data aset yang ada, atau menghapus aset. Setiap perubahan data disimpan ke dalam basis data dan sistem mencatat aktivitas tersebut pada audit log.

*(Gambar 3.4 Activity Diagram Pengelolaan Aset)*

**d. Activity Diagram Pembuatan Laporan**

Activity Diagram Pembuatan Laporan menggambarkan alur proses pembuatan laporan inventaris aset. Pengguna mengakses menu Laporan. Sistem menampilkan form filter laporan berdasarkan periode, kategori, atau kondisi aset. Pengguna menentukan parameter laporan yang diinginkan. Sistem mengambil data dari basis data sesuai parameter yang dipilih dan menghasilkan laporan dalam format yang dapat dicetak atau diunduh.

*(Gambar 3.5 Activity Diagram Pembuatan Laporan)*

**e. Class Diagram**

Class Diagram menggambarkan struktur kelas-kelas yang terdapat dalam sistem beserta atribut dan metode yang dimiliki masing-masing kelas, serta relasi antar kelas. Kelas-kelas utama dalam sistem ini meliputi User, Asset, Barang, Ruangan, Maintenance, ActivityLog, dan AuditLog.

*(Gambar 3.6 Class Diagram)*

### 3.5.2 Perancangan Basis Data dan Relasi Antar Tabel

Perancangan basis data dilakukan menggunakan Entity Relationship Diagram (ERD) untuk menggambarkan entitas-entitas yang terlibat dalam sistem beserta relasi antar entitas tersebut.

Entitas-entitas utama dalam sistem ini adalah:
- **Asset (Aset):** Menyimpan data seluruh aset barang yang dimiliki RBTV Bengkulu.
- **Barang:** Menyimpan data kategori/jenis barang sebagai pengelompokan aset.
- **Ruangan:** Menyimpan data ruangan sebagai lokasi penempatan aset.
- **User (Pengguna):** Menyimpan data akun pengguna sistem beserta peran dan hak aksesnya.
- **Maintenance:** Menyimpan data riwayat pemeliharaan aset.
- **ActivityLog:** Menyimpan catatan seluruh aktivitas pengguna dalam sistem.

Relasi antar entitas yang terbentuk adalah sebagai berikut:
- Satu Barang dapat memiliki banyak Aset (one-to-many).
- Satu Ruangan dapat memiliki banyak Aset (one-to-many).
- Satu Aset dapat memiliki banyak catatan Maintenance (one-to-many).
- Satu User dapat memiliki banyak catatan ActivityLog (one-to-many).

*(Gambar 3.7 Entity Relationship Diagram (ERD))*

### 3.5.3 Perancangan Struktur Tabel

Berdasarkan ERD yang telah dirancang, struktur tabel-tabel dalam basis data sistem adalah sebagai berikut.

**Tabel 3.6 Struktur Tabel aset**

| No | Nama Kolom | Tipe Data | Keterangan |
|---|---|---|---|
| 1 | id | BIGINT UNSIGNED | Primary Key, Auto Increment |
| 2 | kode_aset | VARCHAR(50) | Kode unik aset |
| 3 | nama_aset | VARCHAR(255) | Nama aset |
| 4 | kode_barang | VARCHAR(50) | Foreign Key ke tabel barang |
| 5 | id_ruangan | BIGINT UNSIGNED | Foreign Key ke tabel ruangan |
| 6 | kondisi | ENUM | Kondisi aset (Baik/Rusak Ringan/Rusak Berat) |
| 7 | tahun_perolehan | YEAR | Tahun perolehan aset |
| 8 | harga_perolehan | DECIMAL(15,2) | Harga perolehan aset |
| 9 | sumber_perolehan | VARCHAR(100) | Sumber perolehan aset |
| 10 | foto | VARCHAR(255) | Path foto aset |
| 11 | qr_code | VARCHAR(255) | Path file QR Code |
| 12 | keterangan | TEXT | Keterangan tambahan |
| 13 | created_at | TIMESTAMP | Waktu data dibuat |
| 14 | updated_at | TIMESTAMP | Waktu data diperbarui |
| 15 | deleted_at | TIMESTAMP | Waktu data dihapus (soft delete) |

**Tabel 3.7 Struktur Tabel barang**

| No | Nama Kolom | Tipe Data | Keterangan |
|---|---|---|---|
| 1 | id | BIGINT UNSIGNED | Primary Key, Auto Increment |
| 2 | kode_barang | VARCHAR(50) | Kode unik kategori barang |
| 3 | nama_barang | VARCHAR(255) | Nama kategori barang |
| 4 | satuan | VARCHAR(50) | Satuan barang |
| 5 | keterangan | TEXT | Keterangan tambahan |
| 6 | created_at | TIMESTAMP | Waktu data dibuat |
| 7 | updated_at | TIMESTAMP | Waktu data diperbarui |
| 8 | deleted_at | TIMESTAMP | Waktu data dihapus (soft delete) |

**Tabel 3.8 Struktur Tabel ruangan**

| No | Nama Kolom | Tipe Data | Keterangan |
|---|---|---|---|
| 1 | id | BIGINT UNSIGNED | Primary Key, Auto Increment |
| 2 | nama_ruangan | VARCHAR(255) | Nama ruangan |
| 3 | kode_ruangan | VARCHAR(50) | Kode unik ruangan |
| 4 | keterangan | TEXT | Keterangan tambahan |
| 5 | created_at | TIMESTAMP | Waktu data dibuat |
| 6 | updated_at | TIMESTAMP | Waktu data diperbarui |

**Tabel 3.9 Struktur Tabel users**

| No | Nama Kolom | Tipe Data | Keterangan |
|---|---|---|---|
| 1 | id | BIGINT UNSIGNED | Primary Key, Auto Increment |
| 2 | name | VARCHAR(255) | Nama lengkap pengguna |
| 3 | email | VARCHAR(255) | Alamat email (unik) |
| 4 | password | VARCHAR(255) | Password terenkripsi (bcrypt) |
| 5 | role | ENUM | Peran pengguna (admin/staff) |
| 6 | email_verified_at | TIMESTAMP | Waktu verifikasi email |
| 7 | created_at | TIMESTAMP | Waktu data dibuat |
| 8 | updated_at | TIMESTAMP | Waktu data diperbarui |

**Tabel 3.10 Struktur Tabel activity_log**

| No | Nama Kolom | Tipe Data | Keterangan |
|---|---|---|---|
| 1 | id | BIGINT UNSIGNED | Primary Key, Auto Increment |
| 2 | user_id | BIGINT UNSIGNED | Foreign Key ke tabel users |
| 3 | action | VARCHAR(100) | Jenis aksi yang dilakukan |
| 4 | description | TEXT | Deskripsi aktivitas |
| 5 | ip_address | VARCHAR(45) | Alamat IP pengguna |
| 6 | created_at | TIMESTAMP | Waktu aktivitas terjadi |

### 3.5.4 Perancangan Interface/Antarmuka

Perancangan antarmuka dilakukan untuk memberikan gambaran tampilan sistem sebelum tahap implementasi. Antarmuka dirancang dengan memperhatikan kemudahan penggunaan, konsistensi tampilan, dan kesesuaian dengan kebutuhan pengguna.

**a. Prototype Halaman Login**

Halaman login merupakan halaman pertama yang ditampilkan kepada pengguna. Halaman ini berisi form input email dan password, tombol login, serta tautan untuk reset password. Desain halaman login dibuat sederhana dan bersih untuk memudahkan pengguna dalam mengakses sistem.

*(Gambar 3.8 Prototype Halaman Login)*

**b. Prototype Halaman Dashboard**

Halaman dashboard menampilkan ringkasan informasi aset secara keseluruhan, meliputi total aset, jumlah aset berdasarkan kondisi (baik, rusak ringan, rusak berat), jumlah kategori barang, dan jumlah ruangan. Dashboard juga menampilkan grafik distribusi aset dan daftar aset terbaru yang ditambahkan ke dalam sistem.

*(Gambar 3.9 Prototype Halaman Dashboard)*

**c. Prototype Halaman Data Aset**

Halaman data aset menampilkan tabel daftar seluruh aset yang tersimpan dalam sistem. Tabel dilengkapi dengan fitur pencarian, filter berdasarkan kategori dan kondisi, serta tombol aksi untuk melihat detail, mengubah, dan menghapus data aset. Terdapat pula tombol untuk menambah aset baru dan mengekspor data.

*(Gambar 3.10 Prototype Halaman Data Aset)*

**d. Prototype Halaman Tambah Aset**

Halaman tambah aset berisi form input untuk memasukkan data aset baru, meliputi kode aset, nama aset, kategori barang, ruangan, kondisi, tahun perolehan, harga perolehan, sumber perolehan, foto, dan keterangan. Form dilengkapi dengan validasi input untuk memastikan data yang dimasukkan lengkap dan sesuai format.

*(Gambar 3.11 Prototype Halaman Tambah Aset)*

**e. Prototype Halaman Laporan**

Halaman laporan menyediakan form filter untuk menentukan parameter laporan yang akan dihasilkan, meliputi periode waktu, kategori barang, kondisi aset, dan ruangan. Setelah parameter ditentukan, sistem menampilkan laporan dalam format tabel yang dapat dicetak atau diunduh dalam format PDF maupun Excel.

*(Gambar 3.12 Prototype Halaman Laporan)*
